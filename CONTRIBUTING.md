# Contributing

This repo follows the [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) format. Each skill is a folder containing a `SKILL.md` and, optionally, a `references/` folder for supporting documents and a `scripts/` folder for helper code.

## Adding or editing a skill

1. **Folder name** = skill name, kebab-case (e.g. `negative-keywords`).
2. **`SKILL.md` frontmatter** is required:
   ```yaml
   ---
   name: your-skill-name
   description: >
     One paragraph covering what the skill does AND when to trigger it —
     the phrases or request types that should invoke it. This is what
     Claude reads to decide whether the skill applies.
   ---
   ```
   Optional frontmatter: `metadata.version` (semver) and `metadata.history` (one line, only when renaming or making a breaking change).
3. **Body** covers the actual instructions — inputs needed, step-by-step workflow, edge cases, and a "Related Skills" section at the end if it composes with others in this repo.
4. **references/** — put anything long, reusable, or reference-only here (frameworks, term glossaries, market data) rather than in the main body, and link to it by relative path.
5. **Never commit secrets.** No API keys, OAuth tokens, account IDs, or credentials in any skill file — see `security-policy/references/SECURITY.md` for the full policy these skills already follow.
6. **No client-identifying detail.** If a skill needs an illustrative example, use a generic placeholder (`Client A`, `acme-brand-kit`) rather than a real client or company name.

## Before opening a PR

- Run a quick read-through for anything that reads as brand/client-specific.
- If you're renaming a skill, update `metadata.history` and check nothing else in the repo still references the old name.
- Update `CHANGELOG.md` with a one-line entry.

## Reporting an issue

Open a GitHub issue with the skill name, what you expected, and what happened instead. If it's a triggering problem (the skill fires when it shouldn't, or doesn't fire when it should), include the exact prompt that caused it.
