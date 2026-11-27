#!/usr/bin/env node
/**
 * verify.mjs: read-only browser verification for frontend-design.
 *
 * It loads pages, takes screenshots and measures. It never clicks, types, submits or logs in.
 * Every design value (viewports, colours, fonts, budgets, selectors) comes from the config file,
 * which is filled from the design system or the brand kit's design.md. This script holds none.
 * The one exception is the performance fallback below: the published Core Web Vitals "good"
 * thresholds, used only when the config sets no budget.
 *
 * Usage:
 *   node verify.mjs --config verify.config.json --out <dir> <url> [<url> ...]
 *   node verify.mjs --inventory-only [--config c.json] --out <dir> <url> [<url> ...]
 *   node verify.mjs --discover-breakpoints <url>
 *   node verify.mjs --self-test
 * Options:
 *   --inventory-only              no design values needed: status, console, requests, links, images,
 *                                 headings, forms, JSON-LD, tag hosts, axe. No screenshots, viewport
 *                                 checks, rules or budgets. The config is optional (tags, blockRequests).
 *   --baseline <inventory.json>   compare headings, links and form fields with an earlier run
 *   --browser-path <path>         use this Chrome or Chromium (or set VERIFY_BROWSER_PATH)
 *   --max-links <n>               internal links to status-check per page (default 40)
 *
 * Needs: npm install playwright (and optionally @axe-core/playwright) where you run it.
 * Exit code 1 when a Floor check fails or a self-test expectation is not met.
 */
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));

// Published Core Web Vitals "good" thresholds. Fallback only: a design system budget wins.
const WEB_VITALS_GOOD = { lcpMs: 2500, cls: 0.1 };
const ACTION_LINK = /logout|log-out|signout|delete|remove|unsubscribe|cart|checkout|add-to|[?&]action=|[?&]nonce=/i;

// ---------- args ----------
function parseArgs(argv) {
  const a = { urls: [], maxLinks: 40 };
  for (let i = 0; i < argv.length; i++) {
    const k = argv[i];
    if (k === '--config') a.config = argv[++i];
    else if (k === '--out') a.out = argv[++i];
    else if (k === '--baseline') a.baseline = argv[++i];
    else if (k === '--browser-path') a.browserPath = argv[++i];
    else if (k === '--max-links') a.maxLinks = Number(argv[++i]);
    else if (k === '--discover-breakpoints') a.discover = true;
    else if (k === '--inventory-only') a.inventoryOnly = true;
    else if (k === '--self-test') a.selfTest = true;
    else if (k.startsWith('--')) throw new Error(`Unknown option ${k}`);
    else a.urls.push(k);
  }
  return a;
}

async function loadPlaywright() {
  for (const base of [process.cwd() + '/', HERE + '/']) {
    try {
      const req = createRequire(base);
      return req('playwright');
    } catch { /* try next */ }
  }
  throw new Error('playwright is not installed. Run: npm install playwright (in the folder you run this from).');
}

async function launch(pw, browserPath) {
  const exe = browserPath || process.env.VERIFY_BROWSER_PATH;
  if (exe) return pw.chromium.launch({ executablePath: exe });
  try { return await pw.chromium.launch(); } catch { /* fall back to an installed Chrome */ }
  return pw.chromium.launch({ channel: 'chrome' });
}

// ---------- config ----------
function loadConfig(file, inventoryOnly) {
  if (inventoryOnly) {
    const cfg = file ? JSON.parse(fs.readFileSync(file, 'utf8')) : {};
    // No design value is needed: the browser's own default viewport is used and nothing visual is judged.
    return { ...cfg, viewports: [{ name: 'default' }], rules: [], aboveFold: undefined, minTargetPx: undefined, inventoryOnly: true };
  }
  if (!file) throw new Error('--config is required: viewports come from the design system, not from this script.');
  const cfg = JSON.parse(fs.readFileSync(file, 'utf8'));
  const vps = cfg.viewports;
  if (!Array.isArray(vps) || !vps.length) throw new Error('config.viewports is empty. Fill it from the design system or the brand kit design.md (Verification section).');
  for (const v of vps) {
    if (!v.name || !Number.isFinite(v.width) || !Number.isFinite(v.height) || v.width <= 0 || v.height <= 0) {
      throw new Error(`Invalid viewport ${JSON.stringify(v)}: needs name, width and height as numbers.`);
    }
  }
  return cfg;
}

const slug = (u) => u.replace(/^https?:\/\//, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '').slice(0, 80) || 'page';

function parseColour(s) {
  if (!s) return null;
  s = s.trim();
  let m = s.match(/^#([0-9a-f]{3}|[0-9a-f]{6})$/i);
  if (m) {
    let h = m[1];
    if (h.length === 3) h = [...h].map((c) => c + c).join('');
    return { r: parseInt(h.slice(0, 2), 16), g: parseInt(h.slice(2, 4), 16), b: parseInt(h.slice(4, 6), 16), a: 1 };
  }
  m = s.match(/^rgba?\(\s*([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:[ ,/]+([\d.]+%?))?\s*\)$/i);
  if (m) {
    let a = m[4] === undefined ? 1 : m[4].endsWith('%') ? parseFloat(m[4]) / 100 : parseFloat(m[4]);
    return { r: +m[1], g: +m[2], b: +m[3], a };
  }
  return null;
}
const dist = (x, y) => Math.hypot(x.r - y.r, x.g - y.g, x.b - y.b);
const inSet = (c, set, tol) => set.some((t) => dist(c, t) <= tol);

// ---------- in-page collectors ----------
const COLLECT = {
  overflow: () => {
    const de = document.documentElement;
    const vw = de.clientWidth;
    const wide = [];
    for (const el of document.body.querySelectorAll('*')) {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      if (r.width && cs.visibility !== 'hidden' && cs.display !== 'none' && r.right > vw + 1 && cs.position !== 'fixed') {
        wide.push(el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : ''));
        if (wide.length >= 5) break;
      }
    }
    return { scrollW: de.scrollWidth, clientW: vw, wide };
  },
  inventory: () => ({
    headings: [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map((h) => [h.tagName.toLowerCase(), h.textContent.trim().replace(/\s+/g, ' ').slice(0, 120)]),
    links: [...document.querySelectorAll('a[href]')].map((a) => [a.textContent.trim().replace(/\s+/g, ' ').slice(0, 80), a.getAttribute('href')]),
    forms: [...document.querySelectorAll('form')].map((f) => ({
      action: f.getAttribute('action') || '',
      fields: [...f.querySelectorAll('input,select,textarea')].map((i) => (i.name || i.id || i.type) + ':' + (i.type || i.tagName.toLowerCase())),
    })),
    landmarks: ['header', 'nav', 'main', 'footer'].map((t) => [t, document.querySelectorAll(t).length]),
    imagesNoAlt: [...document.querySelectorAll('img')].filter((i) => !i.hasAttribute('alt')).map((i) => i.currentSrc || i.src).slice(0, 10),
    brokenImages: [...document.querySelectorAll('img')].filter((i) => i.complete && i.naturalWidth === 0 && (i.currentSrc || i.src)).map((i) => i.currentSrc || i.src).slice(0, 10),
    jsonld: [...document.querySelectorAll('script[type="application/ld+json"]')].map((s) => {
      try { const j = JSON.parse(s.textContent); return { types: [].concat(j['@graph'] ? j['@graph'].map((n) => n['@type']) : j['@type']).flat().filter(Boolean) }; }
      catch { return { error: 'invalid JSON' }; }
    }),
  }),
  animations: () => document.getAnimations().filter((a) => a.playState === 'running').length,
  breakpoints: () => {
    const out = new Set();
    for (const sheet of document.styleSheets) {
      let rules; try { rules = sheet.cssRules; } catch { continue; }
      const walk = (rs) => { for (const r of rs) { if (r.media) { for (const m of r.media.mediaText.matchAll(/(?:min|max)-width:\s*([\d.]+)px/g)) out.add(+m[1]); } if (r.cssRules) walk(r.cssRules); } };
      walk(rules);
    }
    return [...out].sort((a, b) => a - b);
  },
  focus: (maxStops) => {
    const sel = 'a[href],button,input,select,textarea,[tabindex]:not([tabindex="-1"])';
    const els = [...document.querySelectorAll(sel)].filter((e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width && r.height && cs.visibility !== 'hidden' && cs.display !== 'none'; }).slice(0, maxStops);
    const bad = [];
    for (const e of els) {
      e.focus({ focusVisible: true });
      const cs = getComputedStyle(e);
      const ring = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || (cs.boxShadow && cs.boxShadow !== 'none');
      if (!ring) bad.push(e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + ' "' + (e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 30) + '"');
      e.blur();
    }
    return { checked: els.length, bad: bad.slice(0, 8) };
  },
  targets: (min) => {
    const bad = [];
    for (const e of document.querySelectorAll('a[href],button,input,select,textarea')) {
      const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
      if (!r.width || cs.visibility === 'hidden' || cs.display === 'none' || e.type === 'hidden') continue;
      if (cs.display === 'inline' && e.tagName === 'A') continue; // inline text links are exempt
      if (r.width < min || r.height < min) bad.push(e.tagName.toLowerCase() + ' "' + (e.textContent || '').trim().slice(0, 30) + '" ' + Math.round(r.width) + 'x' + Math.round(r.height));
    }
    return bad.slice(0, 8);
  },
  perf: () => new Promise((resolve) => {
    let lcp = 0, cls = 0;
    new PerformanceObserver((l) => { for (const e of l.getEntries()) lcp = e.startTime; }).observe({ type: 'largest-contentful-paint', buffered: true });
    new PerformanceObserver((l) => { for (const e of l.getEntries()) if (!e.hadRecentInput) cls += e.value; }).observe({ type: 'layout-shift', buffered: true });
    setTimeout(() => {
      const bytes = performance.getEntriesByType('resource').reduce((s, r) => s + (r.transferSize || 0), 0)
        + (performance.getEntriesByType('navigation')[0]?.transferSize || 0);
      resolve({ lcp, cls, bytes });
    }, 1500);
  }),
};

// Config rules run in the page. All selectors, colours and tolerances come from the config.
async function runRules(page, rules, tokens, tol) {
  const results = [];
  for (const rule of rules || []) {
    const r = await page.evaluate(({ rule, tokens, tol }) => {
      const parse = (s) => { const m = s.match(/rgba?\(\s*([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:[ ,/]+([\d.]+%?))?\s*\)/); if (!m) return null; const a = m[4] === undefined ? 1 : m[4].endsWith('%') ? parseFloat(m[4]) / 100 : parseFloat(m[4]); return { r: +m[1], g: +m[2], b: +m[3], a }; };
      const hex = (h) => { h = h.replace('#', ''); if (h.length === 3) h = [...h].map((c) => c + c).join(''); return { r: parseInt(h.slice(0, 2), 16), g: parseInt(h.slice(2, 4), 16), b: parseInt(h.slice(4, 6), 16) }; };
      const dist = (x, y) => Math.hypot(x.r - y.r, x.g - y.g, x.b - y.b);
      const label = (e) => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + ' "' + (e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 30) + '"';
      const visible = (e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
      const bad = [];
      let seen = 0;
      if (rule.type === 'filled') {
        for (const e of document.querySelectorAll(rule.selector)) { if (!visible(e)) continue; seen++; const c = parse(getComputedStyle(e).backgroundColor); const img = getComputedStyle(e).backgroundImage; if ((!c || c.a === 0) && img === 'none') bad.push(label(e)); }
      } else if (rule.type === 'alignBottom') {
        const per = rule.tolerance ?? 0;
        for (const parent of document.querySelectorAll(rule.container)) {
          // Only items that sit side by side form a row: group by the top edge of the container's child
          // that holds the element, so cards stacked on a narrow viewport are not compared.
          const items = [...parent.querySelectorAll(rule.selector)].filter(visible).map((e) => {
            let c = e; while (c.parentElement && c.parentElement !== parent) c = c.parentElement;
            return { e, b: e.getBoundingClientRect().bottom, top: Math.round(c.getBoundingClientRect().top) };
          });
          seen += items.length;
          const rows = new Map();
          for (const it of items) { const k = Math.round(it.top / (per + 1)); rows.set(k, [...(rows.get(k) || []), it]); }
          for (const row of rows.values()) { if (row.length > 1) { const max = Math.max(...row.map((x) => x.b)); for (const x of row) if (max - x.b > per) bad.push(label(x.e)); } }
        }
      } else if (rule.type === 'forbidPair') {
        const t = (rule.tolerance ?? 0); const fg = rule.text.map(hex); const bg = rule.background.map(hex);
        for (const e of document.querySelectorAll(rule.selector || '*')) {
          if (!visible(e) || ![...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) continue;
          const cs = getComputedStyle(e); const c = parse(cs.color); const b = parse(cs.backgroundColor);
          if (!c || !b || b.a === 0) continue; seen++;
          if (fg.some((f) => dist(f, c) <= t) && bg.some((x) => dist(x, b) <= t)) bad.push(label(e));
        }
      } else if (rule.type === 'background') {
        const allowed = rule.allowed.map(hex); const t = rule.tolerance ?? 0;
        for (const e of document.querySelectorAll(rule.selector)) { if (!visible(e)) continue; seen++; const b = parse(getComputedStyle(e).backgroundColor); const eff = !b || b.a === 0 ? null : b; if (eff && !allowed.some((a) => dist(a, eff) <= t)) bad.push(label(e) + ' ' + getComputedStyle(e).backgroundColor); }
      } else if (rule.type === 'onlyTokens') {
        const cols = (tokens.colours || []).map(hex); const fonts = (tokens.fontFamilies || []).map((f) => f.toLowerCase());
        const generic = new Set(['serif', 'sans-serif', 'monospace', 'system-ui', 'cursive', 'fantasy', 'inherit', 'initial', 'ui-sans-serif', 'ui-serif', 'ui-monospace']);
        const off = new Set();
        for (const e of document.body.querySelectorAll('*')) {
          if (!visible(e)) continue; const cs = getComputedStyle(e);
          const hasText = [...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
          if (cols.length) {
            const test = (v, what) => { const c = parse(v); if (c && c.a > 0 && !cols.some((t2) => dist(t2, c) <= tol)) { off.add(what + ' ' + v + ' on ' + e.tagName.toLowerCase()); } };
            if (hasText) test(cs.color, 'text');
            test(cs.backgroundColor, 'background');
            if (parseFloat(cs.borderTopWidth) > 0) test(cs.borderTopColor, 'border');
          }
          if (fonts.length && hasText) { const first = cs.fontFamily.split(',')[0].trim().replace(/["']/g, '').toLowerCase(); if (!generic.has(first) && !fonts.includes(first)) off.add('font ' + first + ' on ' + e.tagName.toLowerCase()); }
        }
        seen = 1; bad.push(...[...off].slice(0, 10));
      }
      return { seen, bad: bad.slice(0, 8), count: bad.length };
    }, { rule, tokens, tol });
    results.push({ id: `rule:${rule.name || rule.type}`, tier: rule.tier || 'Reflex', status: r.seen === 0 ? 'not-verified' : r.count ? 'fail' : 'pass', detail: r.seen === 0 ? 'no matching elements' : r.count ? `${r.count} breach(es): ${r.bad.join('; ')}` : `${r.seen} checked` });
  }
  return results;
}

// ---------- one page ----------
async function verifyPage(browser, url, cfg, outDir, opts, axeBuilder) {
  const results = [];
  const add = (id, tier, status, detail) => results.push({ id, tier, status, detail });
  const dir = path.join(outDir, slug(url));
  fs.mkdirSync(dir, { recursive: true });
  const origin = new URL(url).origin;
  let inventory = null;
  const hostsSeen = new Map();

  for (const vp of cfg.viewports) {
    const ctx = await browser.newContext(cfg.inventoryOnly ? {} : { viewport: { width: vp.width, height: vp.height }, isMobile: !!vp.mobile, hasTouch: !!vp.mobile });
    const page = await ctx.newPage();
    const consoleErrors = []; const failed = [];
    // Requests the config blocks on purpose (analytics, ad pixels) are recorded as fired, not as failures.
    const ignore = [/ERR_BLOCKED_BY_CLIENT/, ...(cfg.ignoreConsoleErrors || []).map((r) => new RegExp(r))];
    page.on('console', (m) => { if (m.type() === 'error' && !ignore.some((r) => r.test(m.text()))) consoleErrors.push(m.text().slice(0, 160)); });
    page.on('pageerror', (e) => consoleErrors.push('pageerror: ' + String(e.message).slice(0, 160)));
    page.on('requestfailed', (r) => { if (!/ABORTED|BLOCKED_BY_CLIENT/.test(r.failure()?.errorText || '')) failed.push(`${r.url().slice(0, 100)} (${r.failure()?.errorText})`); });
    page.on('response', (r) => { if (r.status() >= 400) failed.push(`${r.status()} ${r.url().slice(0, 100)}`); });
    const block = (cfg.blockRequests || []).map((r) => new RegExp(r));
    await page.route('**/*', (route) => {
      const u = route.request().url();
      try { const h = new URL(u).host; hostsSeen.set(h, (hostsSeen.get(h) || 0) + 1); } catch { /* ignore */ }
      if (block.some((r) => r.test(u))) return route.abort('blockedbyclient');
      return route.continue();
    });

    let resp;
    try { resp = await page.goto(url, { waitUntil: 'load', timeout: 45000 }); }
    catch (e) { add(`load@${vp.name}`, 'Floor', 'fail', 'page did not load: ' + e.message.split('\n')[0]); await ctx.close(); continue; }
    if (resp && resp.status() >= 400) add(`status@${vp.name}`, 'Floor', 'fail', `HTTP ${resp.status()}`);

    const perf = await page.evaluate(COLLECT.perf);
    if (!cfg.inventoryOnly) {
      await page.screenshot({ path: path.join(dir, `${vp.name}-fold.png`) });
      await page.screenshot({ path: path.join(dir, `${vp.name}-full.png`), fullPage: true });
      const ov = await page.evaluate(COLLECT.overflow);
      const overflowing = ov.scrollW > ov.clientW + 1;
      add(`overflow@${vp.name}`, 'Floor', overflowing ? 'fail' : 'pass', overflowing ? `page is ${ov.scrollW}px wide in a ${ov.clientW}px viewport; wide elements: ${ov.wide.join(', ') || 'none found'}` : 'no horizontal scroll');
    }
    add(`console@${vp.name}`, 'Floor', consoleErrors.length ? 'fail' : 'pass', consoleErrors.length ? `${consoleErrors.length} error(s): ${consoleErrors.slice(0, 3).join(' | ')}` : 'no console errors');
    add(`requests@${vp.name}`, 'Floor', failed.length ? 'fail' : 'pass', failed.length ? `${failed.length} failed: ${[...new Set(failed)].slice(0, 3).join(' | ')}` : 'no failed requests');

    const b = cfg.inventoryOnly ? null : (cfg.budgets || {});
    if (b) {
    const lcpMax = b.lcpMs ?? WEB_VITALS_GOOD.lcpMs; const clsMax = b.cls ?? WEB_VITALS_GOOD.cls;
    const src = b.lcpMs === undefined ? 'web-vitals fallback' : 'design system budget';
    add(`lcp@${vp.name}`, 'Reflex', perf.lcp > lcpMax ? 'fail' : 'pass', `${Math.round(perf.lcp)}ms vs ${lcpMax}ms (${src}); one lab run, not field data`);
    add(`cls@${vp.name}`, 'Reflex', perf.cls > clsMax ? 'fail' : 'pass', `${perf.cls.toFixed(3)} vs ${clsMax} (${b.cls === undefined ? 'web-vitals fallback' : 'design system budget'})`);
    if (b.transferKb !== undefined) add(`weight@${vp.name}`, 'Reflex', perf.bytes / 1024 > b.transferKb ? 'fail' : 'pass', `${Math.round(perf.bytes / 1024)}KB vs ${b.transferKb}KB (design system budget)`);
    }

    if (cfg.inventoryOnly) { /* nothing visual is judged without design values */ }
    else if (cfg.aboveFold) {
      const miss = [];
      for (const [what, sel] of Object.entries(cfg.aboveFold)) {
        const ok = await page.evaluate(({ sel, h }) => { const e = document.querySelector(sel); if (!e) return false; const r = e.getBoundingClientRect(); return r.width > 0 && r.top >= 0 && r.bottom <= h; }, { sel, h: vp.height });
        if (!ok) miss.push(what);
      }
      add(`aboveFold@${vp.name}`, 'Floor', miss.length ? 'fail' : 'pass', miss.length ? `not fully visible without scrolling: ${miss.join(', ')}` : 'all configured elements visible');
    } else if (vp === cfg.viewports[0]) add('aboveFold', 'Floor', 'not-verified', 'config.aboveFold not set by the design system');

    if (cfg.inventoryOnly) { /* skipped */ }
    else if (typeof cfg.minTargetPx === 'number') {
      const bad = await page.evaluate(COLLECT.targets, cfg.minTargetPx);
      add(`targets@${vp.name}`, 'Reflex', bad.length ? 'fail' : 'pass', bad.length ? `below ${cfg.minTargetPx}px: ${bad.join('; ')}` : 'ok');
    } else if (vp === cfg.viewports[0]) add('targets', 'Reflex', 'not-verified', 'config.minTargetPx not set by the design system');

    const tokens = cfg.tokens || {}; const tol = cfg.colourTolerance ?? 0;
    for (const r of await runRules(page, cfg.rules, tokens, tol)) { r.id += '@' + vp.name; results.push(r); }

    if (vp === cfg.viewports[0]) {
      inventory = await page.evaluate(COLLECT.inventory);
      add('alt-text', 'Floor', inventory.imagesNoAlt.length ? 'fail' : 'pass', inventory.imagesNoAlt.length ? `${inventory.imagesNoAlt.length} image(s) without an alt attribute: ${inventory.imagesNoAlt.slice(0, 2).join(', ')}` : 'every image has an alt attribute (empty alt is allowed for decoration)');
      add('broken-images', 'Floor', inventory.brokenImages.length ? 'fail' : 'pass', inventory.brokenImages.length ? inventory.brokenImages.slice(0, 3).join(', ') : 'none');
      const ld = inventory.jsonld;
      add('json-ld', 'Info', ld.some((x) => x.error) ? 'fail' : 'pass', ld.length ? ld.map((x) => x.error || [].concat(x.types).join('/')).join(', ') : 'none found');
      const h1 = inventory.headings.filter((h) => h[0] === 'h1').length;
      add('h1', 'Floor', h1 === 1 ? 'pass' : 'fail', `${h1} h1 element(s)`);
      if (vp.mobile && !cfg.inventoryOnly) {
        const meta = await page.evaluate(() => !!document.querySelector('meta[name="viewport"]'));
        add('viewport-meta', 'Floor', meta ? 'pass' : 'fail', meta ? 'present' : 'missing: mobile browsers will lay the page out on a wide virtual viewport');
      }

      if (axeBuilder) {
        try {
          const axe = await new axeBuilder({ page }).analyze();
          const serious = axe.violations.filter((v) => ['serious', 'critical'].includes(v.impact));
          add('axe', 'Floor', serious.length ? 'fail' : 'pass', serious.length ? serious.slice(0, 4).map((v) => `${v.id} (${v.nodes.length})`).join(', ') : `${axe.violations.length} minor/moderate finding(s), none serious; automated checks cover only part of WCAG`);
        } catch (e) { add('axe', 'Floor', 'not-verified', 'axe failed: ' + e.message.split('\n')[0]); }
      } else add('axe', 'Floor', 'not-verified', '@axe-core/playwright not installed');

      if (!cfg.inventoryOnly) {
        const f = await page.evaluate(COLLECT.focus, 40);
        add('focus-visible', 'Floor', f.bad.length ? 'fail' : 'pass', f.bad.length ? `no visible indicator on: ${f.bad.join('; ')} (heuristic: outline or shadow)` : `${f.checked} focusable element(s) show an indicator (heuristic)`);
      }

      // Same-origin links, status only, skipping anything that looks like an action.
      const hrefs = [...new Set(inventory.links.map((l) => l[1]).filter((h) => h && !h.startsWith('#') && !/^(mailto|tel|javascript):/i.test(h)))]
        .map((h) => { try { return new URL(h, url).href; } catch { return null; } })
        .filter((h) => h && h.startsWith(origin) && !ACTION_LINK.test(h)).slice(0, cfg.maxLinks ?? 40);
      const dead = [];
      for (const h of hrefs) { try { const r = await ctx.request.head(h, { timeout: 15000, maxRedirects: 5 }); if (r.status() >= 400 && r.status() !== 405) dead.push(`${r.status()} ${h}`); } catch (e) { dead.push(`error ${h}`); } }
      add('internal-links', 'Floor', dead.length ? 'fail' : 'pass', dead.length ? dead.slice(0, 4).join(' | ') : `${hrefs.length} internal link(s) answered (HEAD only; action-like links skipped)`);
    }

    if (vp === cfg.viewports[0] && !cfg.inventoryOnly) {
      await page.emulateMedia({ reducedMotion: 'reduce' });
      await page.reload({ waitUntil: 'load' });
      const running = await page.evaluate(COLLECT.animations);
      add('reduced-motion', 'Floor', running ? 'fail' : 'pass', running ? `${running} animation(s) still running with reduced motion requested` : 'no animations running with reduced motion requested');
    }
    await ctx.close();
  }

  if (cfg.tags) {
    const hosts = [...hostsSeen.keys()];
    for (const t of cfg.tags.expected || []) add(`tag:${t}`, 'Reflex', hosts.some((h) => h.includes(t)) ? 'pass' : 'fail', hosts.some((h) => h.includes(t)) ? 'request seen (blocked before sending if listed in blockRequests)' : 'no request seen');
    for (const t of cfg.tags.forbidden || []) add(`tag-forbidden:${t}`, 'Floor', hosts.some((h) => h.includes(t)) ? 'fail' : 'pass', hosts.some((h) => h.includes(t)) ? 'request seen' : 'none seen');
  }
  add('third-party-hosts', 'Info', 'pass', [...hostsSeen.keys()].filter((h) => !origin.endsWith(h)).join(', ') || 'none');
  if (!cfg.tags) add('tags', 'Info', 'not-verified', 'config.tags not set; hosts listed above only');

  return { url, inventory, results };
}

function diffInventory(before, after) {
  const out = [];
  const key = (a) => JSON.stringify(a);
  const miss = (b, a) => { const s = new Set(a.map(key)); return b.filter((x) => !s.has(key(x))); };
  const h = miss(before.headings, after.headings), l = miss(before.links, after.links);
  const bf = before.forms.flatMap((f) => f.fields), af = after.forms.flatMap((f) => f.fields);
  const f = bf.filter((x) => !af.includes(x));
  out.push({ id: 'inventory:headings-removed', tier: 'Floor', status: h.length ? 'fail' : 'pass', detail: h.length ? h.slice(0, 4).map((x) => x.join(' ')).join(' | ') : 'none removed' });
  out.push({ id: 'inventory:links-removed', tier: 'Floor', status: l.length ? 'fail' : 'pass', detail: l.length ? l.slice(0, 4).map((x) => `${x[0]} -> ${x[1]}`).join(' | ') : 'none removed' });
  out.push({ id: 'inventory:form-fields-removed', tier: 'Floor', status: f.length ? 'fail' : 'pass', detail: f.length ? f.slice(0, 6).join(', ') : 'none removed' });
  return out;
}

function summarise(pages, outDir) {
  const lines = [];
  let floorFail = 0, fail = 0, nv = 0, pass = 0;
  for (const p of pages) {
    lines.push(`# ${p.url}`);
    for (const r of p.results) {
      if (r.status === 'pass') pass++;
      else if (r.status === 'not-verified') nv++;
      else { fail++; if (r.tier === 'Floor') floorFail++; }
      if (r.status === 'fail') lines.push(`FAIL [${r.tier}] ${r.id}: ${r.detail}`);
      else if (r.status === 'not-verified') lines.push(`NOT VERIFIED ${r.id}: ${r.detail}`);
    }
  }
  const head = `verify: ${pass} passed, ${fail} failed (${floorFail} Floor), ${nv} not verified. Screenshots and JSON: ${outDir}`;
  return { text: [head, ...lines].join('\n'), floorFail };
}

async function run(args) {
  const cfg = loadConfig(args.config, args.inventoryOnly);
  cfg.maxLinks = args.maxLinks;
  if (!args.urls.length) throw new Error('Give at least one URL.');
  for (const u of args.urls) if (!/^https?:\/\//i.test(u)) throw new Error(`Only http and https URLs: ${u}`);
  const outDir = args.out || 'verification';
  fs.mkdirSync(outDir, { recursive: true });
  const pw = await loadPlaywright();
  let axeBuilder = null;
  for (const base of [process.cwd() + '/', HERE + '/']) { try { axeBuilder = createRequire(base)('@axe-core/playwright').AxeBuilder; break; } catch { /* optional */ } }
  const browser = await launch(pw, args.browserPath);
  const pages = [];
  try {
    for (const u of args.urls) {
      const p = await verifyPage(browser, u, cfg, outDir, args, axeBuilder);
      if (args.baseline) { const before = JSON.parse(fs.readFileSync(args.baseline, 'utf8')); const b = before[u] || (Object.keys(before).length === 1 ? Object.values(before)[0] : before); if (b.headings && p.inventory) p.results.push(...diffInventory(b, p.inventory)); }
      pages.push(p);
    }
  } finally { await browser.close(); }
  const report = { generated: new Date().toISOString(), config: path.basename(args.config), pages: pages.map((p) => ({ url: p.url, results: p.results })) };
  fs.writeFileSync(path.join(outDir, 'verification.json'), JSON.stringify(report, null, 2));
  fs.writeFileSync(path.join(outDir, 'inventory.json'), JSON.stringify(Object.fromEntries(pages.map((p) => [p.url, p.inventory])), null, 2));
  const s = summarise(pages, outDir);
  fs.writeFileSync(path.join(outDir, 'verification.md'), s.text + '\n');
  console.log(s.text);
  return { pages, floorFail: s.floorFail };
}

async function discover(args) {
  const pw = await loadPlaywright();
  const browser = await launch(pw, args.browserPath);
  try {
    const page = await browser.newPage();
    await page.goto(args.urls[0], { waitUntil: 'load' });
    const bp = await page.evaluate(COLLECT.breakpoints);
    discover.last = bp;
    console.log(bp.length ? `Media query widths in the page's own CSS (px): ${bp.join(', ')}\nPropose viewports to the design system from these; do not adopt them silently.` : 'No readable media queries found (cross-origin sheets are skipped).');
  } finally { await browser.close(); }
}

// ---------- self-test: a planted violation must be seen failing ----------
async function selfTest(args) {
  const dir = path.join(HERE, 'fixtures');
  const server = http.createServer((req, res) => {
    const f = path.join(dir, req.url.split('?')[0].replace(/^\//, '') || 'good.html');
    if (!fs.existsSync(f) || !f.startsWith(dir)) { res.writeHead(404); return res.end('not found'); }
    res.writeHead(200, { 'content-type': f.endsWith('.json') ? 'application/json' : 'text/html' }); res.end(fs.readFileSync(f));
  });
  await new Promise((r) => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}`;
  const cfgFile = path.join(dir, 'selftest.config.json');
  const tmp = fs.mkdtempSync(path.join(process.env.TMPDIR || '/tmp', 'verify-'));
  let ok = true;
  try {
    const good = await run({ ...args, config: cfgFile, out: path.join(tmp, 'good'), urls: [`${base}/good.html`], maxLinks: 10 });
    const bad = await run({ ...args, config: cfgFile, out: path.join(tmp, 'bad'), urls: [`${base}/bad.html`], maxLinks: 10 });
    // Redesign path: the clean page's inventory is the baseline, the bad page is the "after".
    const baseFile = path.join(tmp, 'good', 'inventory.json');
    const diffed = await run({ ...args, config: cfgFile, out: path.join(tmp, 'diff'), urls: [`${base}/bad.html`], maxLinks: 10, baseline: baseFile });
    // Inventory-only path: no design values, no visual checks.
    const inv = await run({ ...args, config: cfgFile, out: path.join(tmp, 'inv'), urls: [`${base}/bad.html`], maxLinks: 10, inventoryOnly: true });
    const ids = (r) => new Set(r.pages[0].results.filter((x) => x.status === 'fail').map((x) => x.id.replace(/@.*/, '')));
    const failed = ids(bad);
    const expected = ['overflow', 'console', 'alt-text', 'broken-images', 'h1', 'rule:button-fill', 'rule:cta-align', 'rule:no-pair', 'rule:tokens', 'rule:section-bg', 'reduced-motion', 'internal-links', 'aboveFold', 'targets', 'tag-forbidden:tracker.invalid'];
    const missing = expected.filter((e) => !failed.has(e));
    const diffMissing = ['inventory:headings-removed', 'inventory:links-removed'].filter((e) => !ids(diffed).has(e));
    const invAll = inv.pages[0].results.map((x) => x.id.replace(/@.*/, ''));
    const invBad = invAll.filter((i) => i.startsWith('rule:') || ['overflow', 'aboveFold', 'targets', 'focus-visible', 'reduced-motion', 'viewport-meta'].includes(i));
    const invMissing = ['console', 'alt-text', 'h1', 'internal-links', 'tag-forbidden:tracker.invalid'].filter((e) => !ids(inv).has(e));
    const goodFloor = good.pages[0].results.filter((r) => r.status === 'fail' && r.tier === 'Floor');
    const goodNoTag = good.pages[0].results.find((r) => r.id === 'tag:analytics.invalid');
    const bpHtml = path.join(dir, 'good.html');
    await discover({ ...args, urls: [`${base}/good.html`] });
    const bp = discover.last || [];
    console.log('\nself-test');
    console.log(missing.length ? `FAIL: planted violations not caught: ${missing.join(', ')}` : `ok: all ${expected.length} planted violations caught`);
    console.log(diffMissing.length ? `FAIL: baseline diff missed: ${diffMissing.join(', ')}` : 'ok: baseline diff reports removed headings and links');
    console.log(invMissing.length || invBad.length ? `FAIL: inventory-only mode (missed: ${invMissing.join(', ') || 'none'}; ran visual checks: ${invBad.join(', ') || 'none'})` : 'ok: inventory-only mode runs the objective checks and none of the visual ones');
    console.log(goodFloor.length ? `FAIL: clean page failed: ${goodFloor.map((r) => r.id).join(', ')}` : 'ok: clean page has no Floor failure');
    console.log(goodNoTag && goodNoTag.status === 'pass' ? 'ok: a blocked analytics request is recorded as fired and not sent' : 'FAIL: blocked request was not recorded');
    console.log(bp.includes(640) && bp.includes(900) ? 'ok: breakpoints discovered from the page CSS' : `FAIL: breakpoints discovered: ${bp.join(', ') || 'none'}`);
    ok = !missing.length && !diffMissing.length && !invMissing.length && !invBad.length && !goodFloor.length && goodNoTag?.status === 'pass' && bp.includes(640) && bp.includes(900);
  } finally { server.close(); fs.rmSync(tmp, { recursive: true, force: true }); }
  return ok;
}

const args = parseArgs(process.argv.slice(2));
try {
  if (args.selfTest) process.exit((await selfTest(args)) ? 0 : 1);
  else if (args.discover) await discover(args);
  else { const r = await run(args); process.exit(r.floorFail ? 1 : 0); }
} catch (e) { console.error('verify: ' + e.message); process.exit(2); }
