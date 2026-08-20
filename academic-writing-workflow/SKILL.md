---
name: academic-writing-workflow
description: >-
  Edit and develop the argument and exposition of academic economics papers,
  appendices, and presentation slides. Use for local prose edits, requested drafting,
  paper or deck planning and restructuring, and source-grounded technical writing
  within those artifacts. Do not use for build-only or submission-packaging work,
  websites or CVs, standalone explanations, or maintenance of analysis-design and
  output-interpretation notes.
---

# Academic Writing Workflow

Edit academic economics papers and slides in context while preserving their technical meaning, evidence, and project conventions.

## Scope And Ownership

- Own paper, appendix, abstract, academic-slide, and writing-plan content.
- Do not use this skill for build-only or submission-packaging tasks, websites or CVs, standalone technical explanations, or non-writing artifacts.
- Treat `analysis-design` and `output-interpretation` notes as grounded sources, not owned artifacts. If the user explicitly requests changes to both a note and a writing artifact, follow the repository's owning workflow for each surface; do not create or update an extra note by default.
- Route by the requested artifact and purpose, not generic verbs such as `plan`, `write`, `revise`, or `interpret`. If the intended artifact cannot be inferred, ask which surface the user wants rather than creating multiple artifacts.

## Editing Invariants

- Default stance: edit, diagnose, and suggest; do not draft substantive paper or slide content unless explicitly asked.
- Preserve claims, notation, citations, empirical qualifications, model assumptions, hedge strength, and LaTeX/Beamer structure unless explicitly asked to change substance.
- Resolve every added or changed technical claim, number, sample definition, result, or mechanism to current draft material, tables, code, or supplied notes. Label inference and flag conflicts instead of silently reconciling them.
- Do not invent parameter values, sample definitions, citations, results, or mechanisms when the evidence is insufficient.
- Use the smallest useful intervention and avoid unrelated cleanup.
- Treat `[# ...]` as an editorial instruction to apply and remove within the requested scope.
- Treat plain `[...]` as draft prose only when the user or surrounding editorial context identifies it as markup. Never treat LaTeX optional arguments, citations, equations, or unrelated TODO styles as edit markers.

## Workflow

1. Identify the requested mode: advice, review, direct edit, or requested drafting.
   - Suggestions remain non-mutating.
   - Direct edits change only the requested surface.
   - Reviews lead with actionable findings rather than unsolicited rewrites.
2. Ground the work in context.
   - Inspect the selected text and its surrounding paragraph, subsection, section, frame, or neighbouring frames.
   - Identify the local purpose of the text: motivation, fact, model object, mechanism, estimation detail, result, identification, counterfactual, implication, transition, or slide takeaway.
   - Resolve the Git root containing the target artifact and load only the relevant repo map when present.
3. Choose the smallest useful intervention.
   - For proofreading, fix grammar, word order, tense, articles, punctuation, and awkward phrasing.
   - For flow, improve topic sentences, transitions, sentence order, and repetition.
   - For structure, diagnose missing links before rewriting; prefer local restructuring before whole-section rewrites.
   - For technical exposition, distinguish source-grounded facts from interpretation or suggested framing.
4. Verify the requested outcome and build only when warranted.
   - Never build for advice-only, review-only, or chat-only output.
   - Follow explicit user instructions and repo-local build policy first; never build when the user opts out.
   - Without such instructions, skip compilation for wording-only edits.
   - After direct changes to commands, environments, labels, citations, inputs, tables, figures, frame structure, or other render-sensitive structure, compile only when source checks are insufficient to validate the edit.
5. Return output in the user's working style.
   - For selected text, provide a revised version and a brief note on the main editing logic.
   - For file edits or reviews, summarize the requested scope, evidence limitations, and any broader issue deliberately left untouched.

## Task Routing

- For local prose or editorial-markup edits, read `references/writing-principles.md` and enough surrounding context.
- For draft development, read `references/workflow-patterns.md` and `references/structural-paper-architecture.md` when the empirical-structural architecture is relevant.
- For slide writing, editing, or restructuring, read `references/slide-writing-principles.md`, the repo slide map when present, and enough neighbouring frames to preserve the talk flow.
- For structure, consistency, or argument-chain review, read `references/workflow-patterns.md`, `references/structural-paper-architecture.md`, and the repo draft map when present.
- For technical writing inside an owned artifact, read `references/workflow-patterns.md` and the underlying code, documentation, tables, notes, or draft context.
- Load only the references needed for the task.

## Optional Repo Context

Repo-specific references should stay in the target artifact's Git repository rather than in this user-level skill. When present, use:

- `<git-root>/.agents/references/academic-writing-workflow/repo-draft-map.md` for local draft structure, project-specific terminology, English variant preferences, paper-specific argument chains, and validation conventions.
- `<git-root>/.agents/references/academic-writing-workflow/repo-slide-map.md` for local deck structure, timing, slide-role patterns, presentation rules, deck-specific terminology, and validation conventions.

Treat repo maps as replaceable context for style and structure, not factual authority. Verify technical claims against live sources, do not assume maps exist, and do not require them for general academic writing tasks.
