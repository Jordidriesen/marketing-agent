# Internal Linking: Drafting Rules

Apply while drafting, not as a post-publish afterthought: link placement and anchor text are easiest to get right while the section is being written. Auditing an existing site section is a separate job, in `internal-linking-audit.md`.

**Not covered here:** topic cannibalization. `keyword-clustering` flags it
at the planning stage from page-intersection and SERP-overlap evidence, and
`seo-audit` checks for it site-wide on published content. Re-deriving that
logic here would duplicate work those two skills already do.

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
