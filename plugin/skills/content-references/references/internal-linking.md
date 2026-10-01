# Internal Link Architecture

Part of the `content-references` shared library. Loaded by
`web-content-pipeline` (and any other content-generation skill) during
drafting, not as a post-publish afterthought, since link placement and
anchor text are easiest to get right while the section is being written.

**Not covered here:** topic cannibalization. `keyword-clustering` flags it
at the planning stage from page-intersection and SERP-overlap evidence, and
`seo-audit` checks for it site-wide on published content. Re-deriving that
logic here would duplicate work those two skills already do.

## Contents

- [Why Internal Links Matter](#why-internal-links-matter)
- [Link Density Targets](#link-density-targets)
- [Anchor Text Distribution](#anchor-text-distribution)
- [Link Placement Strategy](#link-placement-strategy)
- [Bidirectional Linking](#bidirectional-linking)
- [Hub-and-Spoke Model](#hub-and-spoke-model)
- [Orphan Page Detection](#orphan-page-detection)
- [Internal Link Audit Checklist](#internal-link-audit-checklist)
- [Link Velocity Guidelines](#link-velocity-guidelines)
- [Internal Link Tracking](#internal-link-tracking)

## Why Internal Links Matter

Internal links are the primary mechanism for distributing page authority
across a site. They tell search engines and AI systems which pages are
important, how content relates, and what the site's topical structure
looks like.

John Mueller (Google): internal linking is "supercritical for SEO," helping
Google understand site structure and page importance.

seoClarity case study: a 23% organic traffic increase from internal link
optimization alone, with no new content published.

---

## Link Density Targets

The number of internal links per post should scale with content length.

| Post Length | Internal Links | Notes |
|-------------|---------------|-------|
| < 1,000 words | 3-5 | Short posts, fewer natural insertion points |
| 1,000-2,000 words | 5-7 | Standard blog posts |
| 2,000-3,000 words | 7-10 | Detailed guides |
| 3,000+ words (pillar) | 8-12 | Comprehensive pillar pages |

### Hard rules

- **Minimum:** 3 contextual internal links per post, no exceptions
- **Maximum:** 10 links per post for standard content, 12 for pillar pages
- **No orphan posts:** every published post must be linked from at least
  one other page on the site
- **No dead ends:** every post must link out to at least 3 other pages

---

## Anchor Text Distribution

Anchor text is the visible, clickable text of a hyperlink. Optimizing it
matters, but overusing exact-match anchors triggers spam signals.

### Recommended distribution

| Anchor Type | Target Share | Example for "technical SEO" |
|-------------|-------------|----------------------------|
| Exact match | 5-10% | "technical SEO" |
| Partial match | 20-30% | "technical SEO best practices," "guide to technical SEO" |
| Semantic/related | 30-40% | "site architecture optimization," "crawlability improvements" |
| Branded | 10-15% | "our SEO guide," "[Brand] technical audit" |
| Natural/contextual | 15-25% | "the framework we outlined earlier," "as we discussed" |

### Anchor text rules

- **Descriptive:** the anchor should tell the reader what they'll find at
  the destination
- **Natural:** must read naturally in the sentence; if removing the link
  leaves awkward phrasing, rewrite
- **Varied:** vary anchors naturally and avoid manipulative repetition;
  exact repeats are fine when they're the clearest wording
- **Relevant:** anchor text must relate to the destination page's topic
- **Reasonable length:** 2-6 words is ideal, never a full sentence

### Anchor text anti-patterns: never use

| Pattern | Problem | Fix |
|---------|---------|-----|
| "click here" | Zero topical signal | "Read our [technical SEO checklist]" |
| "this article" | No descriptive value | "Our [guide to crawl budget optimization]" |
| "read more" | Generic, no context | "[How structured data improves AI visibility]" |
| "learn more" | Generic, no context | "Learn [how to audit your internal links]" |
| Naked URLs | Unreadable, no context | Replace with descriptive text |
| Full sentence as anchor | Looks spammy, dilutes signal | Reduce to 2-6 key words |
| Same exact anchor everywhere | Over-optimization signal | Vary anchor text across pages |

---

## Link Placement Strategy

Where a link sits on the page affects how much weight it carries. Links
higher on the page and within body content carry meaningfully more
authority than links in footers or sidebars.

### Placement priority

| Location | Weight | Notes |
|----------|--------|-------|
| First 2-3 paragraphs | Highest | Most crawled, most clicked |
| Within body content (contextual) | High | Natural editorial links |
| After key sections (H2s) | Medium-High | Contextually relevant transitions |
| Table of contents | Medium | Navigation aid, passes some authority |
| Related posts section | Medium-Low | Algorithmic, less editorial signal |
| Sidebar | Low | Often templated, discounted |
| Footer | Lowest | Heavily discounted by search engines |

### Best practices

1. Place the most important internal link in the first 2-3 paragraphs
2. Link to the pillar page early in every supporting article
3. Distribute links naturally throughout the body, not clustered together
4. End sections with transitional links to related content
5. Avoid stacking every link into a "Related Articles" block at the bottom

---

## Bidirectional Linking

When page A links to page B, page B should link back to page A where
contextually relevant. This creates a strong topical relationship signal.

### Implementation process

1. When publishing a new post that links to existing content:
   - open each linked page
   - find a natural place to add a link back to the new post
   - use anchor text that isn't identical to the forward link

2. When updating an existing post:
   - check whether the linked pages reciprocate
   - add reciprocal links where missing

### Example

**Post A**, "Complete Guide to Technical SEO," contains: "...proper
[schema markup implementation](/blog/schema-guide) is essential for AI
visibility."

**Post B**, "Schema Markup Implementation Guide," should link back: "...
schema is a critical component of [technical SEO
optimization](/blog/technical-seo-guide), affecting how search engines
interpret your content."

---

## Hub-and-Spoke Model

The hub-and-spoke (pillar-cluster) model is the most effective internal
linking architecture for topical authority.

### Requirements

| Element | Specification |
|---------|--------------|
| Pillar page | 3,000-4,000 words, covers the topic broadly |
| Supporting articles (spokes) | 8-12 articles, each covers a subtopic in depth |
| Pillar to spoke links | Pillar links to ALL supporting articles |
| Spoke to pillar links | Every supporting article links back to the pillar |
| Spoke to spoke links | Cross-link related subtopics where natural |
| Anchor text to pillar | Varied: different anchor text from each spoke |

Each spoke should link to the pillar and to 2-3 related spokes.

---

## Orphan Page Detection

Orphan pages have zero internal links pointing to them. They're invisible
to crawlers navigating via internal links and are only discovered through
`sitemap.xml`, which carries less authority signal.

### How to find orphan pages

1. **Site crawl:** use a crawler (Screaming Frog, Sitebulb) to map all
   internal links and identify pages with zero inbound internal links.
2. **Manual check:** for each published post URL, search the rest of the
   site for links pointing to it:
   ```bash
   grep -r "/blog/your-post-slug" ./content/ --include="*.md"
   ```
3. **CMS/database query:** query the content database for pages not
   referenced in any other page's body content.

### Fixing orphan pages

1. Identify 2-3 topically related existing pages
2. Add a contextual link from each related page to the orphan
3. Ensure the orphan page links back to at least one of those pages
4. If no related content exists, consider whether the orphan should be
   consolidated into another page or removed

---

## Internal Link Audit Checklist

Run this per post at publish time, and site-wide quarterly.

### Per-post checks

| Check | Pass Criteria | Fail Action |
|-------|---------------|-------------|
| Internal link count | 3-10 links (length-dependent) | Add links to related content |
| No orphan status | At least 1 internal link points to this page | Add links from 2-3 related pages |
| Anchor text variety | No single anchor used more than twice for the same destination | Vary anchor text |
| No generic anchors | Zero instances of "click here," "read more," "this article" | Replace with descriptive text |
| Bidirectional links | Linked pages reciprocate where relevant | Add reciprocal links |
| Pillar link present | If part of a topic cluster, links to/from the pillar | Add pillar connection |
| Links functional | All internal links return 200 | Fix broken links (301 or remove) |
| Link placement | At least 1 link in the first 3 paragraphs | Move the important link higher |
| No over-linking | No paragraph has more than 2 internal links | Remove the least relevant link |
| Anchor describes destination | Reader can predict what they'll find | Rewrite anchor text |

### Site-wide checks

| Check | Pass Criteria | Fail Action |
|-------|---------------|-------------|
| Orphan page count | 0 orphan pages | Link to all orphans from related content |
| Pillar coverage | Every topic cluster has a pillar page | Create missing pillar pages |
| Spoke count per pillar | 8-12 supporting articles | Create more supporting content |
| Average internal links per page | 5-8 | Bulk-add links to under-linked pages |
| Max clicks from homepage | Any page reachable in 3-4 clicks | Restructure navigation |
| Broken internal links | 0 broken links (404s) | Fix or remove all broken links |

Cannibalization isn't a row here on purpose, run `keyword-clustering` at
the planning stage or `seo-audit` site-wide instead.

---

## Link Velocity Guidelines

When adding internal links to existing content, avoid bulk-updating every
page at once unless there's QA coverage. Pace changes so crawl logs,
broken links, and editorial relevance can be reviewed.

| Action | Recommended Pace |
|--------|-----------------|
| New post with links | Normal: add all links at publish time |
| Updating existing posts | 3-5 posts per week maximum |
| New pillar page launch | Update all spokes within 1-2 weeks |
| Site-wide link audit fix | Spread changes over 2-4 weeks |
| Fixing orphan pages | 2-3 per day |

---

## Internal Link Tracking

Maintain a simple tracking mechanism to keep link health visible over
time.

### Recommended fields

| Field | Purpose |
|-------|---------|
| Source URL | Page containing the link |
| Destination URL | Page being linked to |
| Anchor text | Clickable text used |
| Date added | When the link was created |
| Context | Why this link exists (editorial, navigation, pillar-spoke) |
| Status | Active, broken, or removed |

This tracking helps identify over-linked pages (too many pages linking to
one destination), under-linked pages (valuable content with few inbound
links), stale anchor text that needs updating after content refreshes, and
broken links after URL changes or content deletion.
