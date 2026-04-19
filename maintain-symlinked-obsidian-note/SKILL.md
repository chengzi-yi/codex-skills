---
name: maintain-symlinked-obsidian-note
description: Use when working from a code repository that contains a symlink to an Obsidian note stored under a different git root, and the note should be updated safely from repository context without replacing the symlink or leaking private vault content into repo-tracked docs.
---

# Maintain Symlinked Obsidian Note

Use this when the repository is the source of truth for scripts, configs, and outputs, but the note itself lives in an Obsidian vault under another git root.

## Workflow

1. Discover the note topology.
   - Find the repo-side note path and confirm it is a symlink.
   - Resolve the symlink target and identify both git roots.
   - Confirm the target note is owned by the vault root, not the working repo root.
2. Load local instructions before editing.
   - Read nearby `AGENTS.md`, `README.md`, entry scripts, or other repo-specific context files first.
   - Read the current target note to infer its conventions: heading structure, Obsidian link style, callouts, comments, and math formatting.
3. Use implementation context as source of truth.
   - Prefer live code, configs, and output paths over stale prose.
   - If a public and private note must stay aligned, align structure and terminology while preserving different visibility boundaries.
4. Edit the vault target directly.
   - Never replace the repo-side symlink with a regular file.
   - Never delete the symlink during a rewrite.
   - Keep private annotations, callouts, and note-local conventions in the vault note unless the user asks to remove them.
5. Validate the split-root workflow before finishing.
   - Verify the repo-side path is still a symlink to the vault target.
   - Verify changes appear under the correct git roots.
   - Verify note links, equations, and other note-local syntax still follow the target note's conventions.

## Guardrails

- Treat the vault target as the editable artifact and the repo-side note as a pointer only.
- Do not commit the vault-owned note from the working repository git root.
- Preserve clickable Obsidian-style links when the note already uses them, including `file:///absolute/path` links when that is the established convention.
- Preserve math as LaTeX when the note uses it, with `$...$` inline and `$$...$$` only for standalone display equations.
- Keep private notes, comments, or personal annotations out of any public repo-tracked documentation.
- Prefer verified file paths over guessed paths.

## Useful Checks

```bash
ls -l "<repo-side-note>"
readlink "<repo-side-note>"
git -C "<repo-root>" rev-parse --show-toplevel
git -C "<vault-root-or-note-dir>" rev-parse --show-toplevel
git -C "<repo-root>" status --short -- "<repo-side-note>" "<related-public-doc>"
git -C "<vault-root>" status --short -- "<vault-target-note>"
```

Add note-specific checks when relevant, for example link-style or formatting validation with `rg`.

## Example Requests

- "Update the Obsidian note linked into this repo without touching the symlink."
- "Restructure the private vault note using the current pipeline scripts as source of truth."
- "Align the private Obsidian note with the public repo README, but keep private annotations out."
