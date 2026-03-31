---
name: preliminary-analysis-note
description: 'Create or update concise Obsidian-style preliminary analysis notes. Load repo note guidance for local destinations, metrics, and examples when available.'
argument-hint: 'Provide the run scope, key outputs, headline findings, and target folder if it differs from the default.'
user-invocable: true
---

# Preliminary Analysis Note

Write a short analysis note that is easy to scan in Obsidian.

## Workflow

1. Collect the minimum metadata.
   - timestamp
   - relevant commit hash
   - run scope
   - source output files
2. If `.agents/references/preliminary-analysis-note/repo-note-guidance.md` exists in the current repo, read it for local destinations, metrics, and examples.
3. Keep the note compact.
   - one-line context
   - one short `At a glance` bullet list
   - one short `Results` section that fits the case
   - use a table in `Results` when it improves readability
   - optional case-specific sections only when they add signal
   - one short `Interpretation` section in bullets
4. Prefer direct statements over narrative.
5. State caveats plainly.

## Formatting Rules

- Use Obsidian-style YAML front matter.
- Keep prose short; prefer bullets for interpretation.
- Treat section layout as flexible after the core metadata and summary.
- Use numeric precision only as needed to support comparison.
- Use a table in `Results` only when it improves readability.
- Do not repeat the same finding in multiple sections.
- Keep source lists short and path-only.

## File Placement

- If the user gives a target folder, use it.
- Otherwise default to the repo destination from `.agents/references/preliminary-analysis-note/repo-note-guidance.md` when present.
- If no repo guidance is available, default to `output/preliminary_analysis/`.
- Use a lowercase snake_case filename with the date at the end.
- Default pattern: `<scope>_<topic>_<YYYY-MM-DD>.md`

## Reference Template

For the compact note skeleton, read [references/template.md](references/template.md).
