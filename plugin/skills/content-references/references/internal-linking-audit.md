# Internal Linking: Audit (on demand)

Load this only when auditing an existing site section: orphan pages, link checklists, velocity and tracking. For drafting new content use `internal-linking-drafting.md`.

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
