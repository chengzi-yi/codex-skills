---
name: academic-writing-workflow
description: Guide academic economics writing for applied and structural papers and presentation slides. Use when drafting a paper backbone from notes, proofreading or rewriting selected paragraphs/sentences, restructuring sections, updating introductions or abstracts, editing Beamer/defense/seminar slides, explaining model/estimation/counterfactual methods from documentation, or reviewing consistency across empirical facts, model mechanisms, estimation, and implications.
---

# Academic Writing Workflow

Use this skill as a context-aware editor for academic economics papers and slides, especially work that combines empirical facts, structural modeling, estimation, and counterfactuals.

## Hard Rules

- Default stance: edit, diagnose, and suggest; do not draft substantive paper or slide content unless explicitly asked.
- Do not compile LaTeX, rebuild PDFs, or run document build commands unless explicitly asked.
- Preserve claims, notation, citations, empirical qualifications, model assumptions, hedge strength, and LaTeX/Beamer structure unless explicitly asked to change substance.
- Do not invent parameter values, sample definitions, citations, results, or mechanisms.
- Use the smallest useful intervention and avoid unrelated cleanup.
- Treat `[...]` as user-authored prose to incorporate; treat `[#...]` as instructions to apply and remove.
- Read additional repo-local context when present and relevant.

## Workflow

1. Ground the edit in context.
   - Inspect the selected text and its surrounding paragraph, subsection, section, frame, or neighbouring frames.
   - Identify the local purpose of the text: motivation, fact, model object, mechanism, estimation detail, result, identification, counterfactual, implication, transition, or slide takeaway.
   - For repo-specific drafts or slide decks, load the local repo map when available and relevant.

2. Choose the smallest useful intervention.
   - For proofreading, fix grammar, word order, tense, articles, punctuation, and awkward phrasing.
   - For flow, improve topic sentences, transitions, sentence order, and repetition.
   - For structure, diagnose missing links before rewriting; prefer local restructuring before whole-section rewrites.
   - For technical exposition, distinguish source-grounded facts from interpretation or suggested framing.

3. Return output in the user's working style.
   - For selected text, provide a revised version and a brief note on the main editing logic.
   - For direct file edits, apply only the requested edit and avoid unrelated cleanup.
   - For broader reviews, lead with actionable issues and the specific section-level fix.

## Task Routing

- For selected text, paragraph, sentence, or bracket-markup edits, read `references/writing-principles.md`, `references/workflow-patterns.md` -> `Local Editing`, and enough surrounding draft context.
- For draft backbones or new section planning, read `references/workflow-patterns.md` -> `Draft Development` and `references/structural-paper-architecture.md`.
- For slide writing, slide editing, Beamer frame rewriting, defense slides, seminar slides, or presentation outline work, read `references/slide-writing-principles.md` and enough neighbouring frames to preserve the talk flow.
- For structure, consistency, or argument-chain review, read `references/workflow-patterns.md` -> `Argument-Chain Review`, `references/structural-paper-architecture.md`, and the repo draft map if available.
- For technical exposition, model solution, estimation, moments, or counterfactual descriptions, read `references/workflow-patterns.md` -> `Technical Exposition` and ground statements in supplied code, documentation, tables, notes, or draft context.
- Load only the references needed for the task.

## Optional Repo Context

Repo-specific references should stay in the repo rather than in this user-level skill. When present, use:

- `.agents/references/academic-writing-workflow/repo-draft-map.md` for local draft structure, project-specific terminology, English variant preferences, and paper-specific argument chains.
- `.agents/references/academic-writing-workflow/repo-slide-map.md` for local deck structure, timing, slide-role patterns, presentation rules, and deck-specific terminology.

Treat repo maps as replaceable local context. Do not assume they exist outside the current repo, and do not require them for general academic writing tasks.
