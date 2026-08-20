---
name: preliminary-analysis-note
description: >-
  Create or update a concise, repo-local preliminary analysis note for an
  output-bearing run or decision-bearing validation. Use for preserved
  comparisons, diagnostics, tables, figures, validation outcomes, and
  consequential failed or incomplete runs that need auditable provenance before
  durable interpretation. Do not use for prospective analysis design, maintained
  cross-run interpretation, papers, general documentation, or lightweight checks
  with no preserved evidence.
---

# Preliminary Analysis Note

Record an auditable, repo-local bridge between inspectable evidence and later durable interpretation. The note describes an analysis or decision slice; it does not design or run the analysis, replace maintained interpretation, or broaden the requested work.

## Decide Whether a Note Applies

Use this skill when the user explicitly requests a preliminary run note or applicable repository policy requires one. For implicit use, write a note only when the work:

- produces preserved outputs, metrics, diagnostics, tables, or figures that may be cited later;
- changes an accepted gate, baseline, comparison, or go/no-go decision; or
- ends in a consequential failed or incomplete result whose evidence affects later work.

Do not create a note for documentation-only work, syntax or load checks, linting, CLI help, text-only validation, or throwaway smoke tests with no preserved or decision-relevant evidence. If the user asks only for review or advice, return findings without editing.

Route prospective `analysis-design` and maintained cross-run `output-interpretation` notes to their owning workflow. Do not automatically update vault navigation, papers, READMEs, or durable interpretation notes.

## Ground the Note

1. Resolve the Git root that will own the note from the explicit target or the source outputs. Do not infer ownership from the task's current directory.
2. Read the `AGENTS.md` files applicable to the target and source artifacts. If the owning root contains `.agents/references/preliminary-analysis-note/repo-note-guidance.md`, read it for local destinations, metadata, metrics, and examples.
3. Apply instructions in this order: explicit user instructions, repository policy and note guidance, then this skill's fallback.
4. Identify the analysis or decision scope, acceptance or validation status, run and check identifiers, and the evidence needed to support the note.
5. Record each relevant source repository and revision, including branch and dirty-worktree state when available. When evidence crosses repositories, identify every root and revision rather than presenting one commit as universal provenance.

## Choose the Note Unit and Destination

- Default to one note per analysis or decision slice. Several tightly related runs may share one note when they answer the same question or support the same decision and each run's role is explicit.
- Update an existing note only when the user identifies it or it unambiguously represents the same continuing slice. Do not blend unrelated runs into a living topic note.
- Use an explicit target file or folder first, then the owning repository's guidance, then `output/preliminary_analysis/`.
- Without a local naming rule, use lowercase snake case with `<scope>_<topic>_<YYYY-MM-DD>.md`.
- Never overwrite an unrelated existing note. Add a short run identifier or time suffix when the fallback name collides.
- Prefer repository-relative paths for evidence inside the owning repository. Label external repositories and paths explicitly.

## Verify the Evidence

- Work from existing manifests, tables, figures, diagnostics, logs, or other inspectable artifacts. Do not rerun analysis, regenerate upstream data, or create evidence merely to populate the note.
- Trace every changed or added technical claim, number, status, and comparison to the inspected evidence. Inspect rendered figures before making visual claims.
- Distinguish direct output facts, derived comparisons, and interpretation or inference. Label inference and report conflicting evidence.
- Preserve definitions, units, sample or support differences, missingness, warnings, failed checks, and result-specific caveats that affect interpretation.
- Use explicit statuses such as successful, review-required, failed, incomplete, or no-go. Never describe an unresolved failure as an accepted result.
- If required evidence is missing, do not fill the gap from memory or task narration. Report the gap, or write a failure note only when the gap itself is the consequential outcome being recorded.

## Write the Note

Keep the note compact and adaptable. Use valid YAML frontmatter for stable metadata unless repository guidance specifies another convention; do not force one universal field schema. Make source revisions distinct from any commit that later records the note itself.

Include the following information, using only the headings that improve the note:

- provenance and one-line context: timestamps when useful, scope, status, run or check identifiers, source repositories and revisions, worktree state, and source artifacts;
- `At a glance`: the decision or status plus the smallest useful set of headline findings;
- results or evidence: precise findings, with a table only when it materially improves comparison;
- interpretation and caveats: define unfamiliar metrics or flags, separate evidence from inference, and state what the result does not establish; and
- source artifacts: a concise inventory with enough repository or artifact context to resolve each path.

Prefer direct statements, appropriate numeric precision, and short interpretation bullets. Do not repeat the same finding across sections. Include a `Runs` section, separate caveat section, or case-specific analysis only when it adds information.

## Finish

1. Recheck the note against every cited source and verify that its status, definitions, paths, and qualifications are accurate.
2. Validate YAML when present and inspect the diff for unsupported claims, duplicated findings, accidental changes outside the requested note, and unresolved filename collisions.
3. Leave source artifacts and unrelated worktree changes untouched. Let the owning implementation workflow handle staging and commits. Never push unless explicitly requested.
4. Report the note path, whether it was created or updated, the covered runs or checks, evidence inspected, status, validation performed, and unresolved evidence gaps.
