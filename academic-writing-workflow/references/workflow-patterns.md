# Workflow Patterns

These patterns encode the user's preferred writing workflow.

For local editing, first determine the edit scope, then determine the edit type. For drafting, structure review, or file implementation, use the relevant workflow mode directly.

## Operating Principles

- Scan relevant context before drafting or editing.
- Lay out a short working plan before major drafting or restructuring.
- Work in controlled steps and avoid broad rewrites unless requested.
- Preserve technical meaning, notation, and claim strength.
- Treat the user as the primary author: suggest reasoning and structure, but do not replace the user's writing.

## Local Editing

### Scope

#### Slice-Local Markup

- Use bracket markup as the edit boundary: `[...]` is intended prose, and `[#...]` is an instruction.
- Resolve the marked sentence or slice first; touch neighboring prose only when needed to make the local revision grammatical and coherent.
- Preserve the user's manual wording where possible, but smooth tense, articles, punctuation, and sentence integration.
- Preserve notation and hedge strength; if the marked sentence has a logic conflict, flag it before polishing.
- Remove all `[#...]` comments from the final prose and mention unresolved or conflicting instructions separately.

#### Paragraph-By-Paragraph

- Edit selected paragraphs sequentially when the user provides local text.
- For each selected paragraph, identify its role, improve grammar and flow, reduce repetition, clarify transitions, and keep edits local unless the surrounding argument is inconsistent.
- When a paragraph has overlapping closing or opening claims, move the "what I do" statement to the most natural paragraph and make the other paragraph purely motivation, evidence, or contribution.

### Edit Type

#### Grammar And Flow

- A grammar-first pass fixes sentence mechanics and readability without changing substance.
- A flow-first pass may reorder sentences, split paragraphs, or add transition phrases.
- When both are needed, fix logic and flow before micro-polishing.
- Minimize bracketed values and parenthetical notation when numbers can be integrated into prose.

#### Structure And Consistency

- Diagnose redundancy before changing structure.
- When table or moment classifications change, update:
  - table organization and notes
  - nearby explanatory paragraphs
  - model-fit discussion
  - terminology throughout the draft
- Check consistency of targeted versus implied moments, notation, parameter names, plural forms, and section references.
- Survey the full paper before changing notation to avoid conflicts.

#### Technical Exposition

- Use for local edits or drafting of model-solution, estimation, moment, and counterfactual descriptions.
- Base statements on source documents, code, tables, notes, or supplied draft context.
- State what is directly documented and what is inferred.
- Explain the economic role of technical objects, not only the computational step.
- Keep enough detail that another graduate student could reproduce the key number or procedure from the paper and appendices.

## Draft Development

- Build the paper top-down: establish the section framework and paragraph roles early.
- When starting from code documentation, analysis notes, or preliminary results, read the supplied material before proposing structure.
- Build a backbone before drafting prose: section outline, paragraph roles, required evidence, model or estimation objects, and unresolved questions.
- Follow the empirical-plus-structural arc: question, facts, model, estimation, fit/identification, counterfactuals, implications.
- Do not fill in prose unless the user explicitly asks for a draft paragraph or section.
- Draft sections bottom-up: refine individual paragraphs and sections as evidence stabilizes.
- Back-integrate new section content into the introduction only after the section is reasonably stable.
- Update the abstract last so it reflects the current finalized content.

## Argument-Chain Review

- Check whether motivating facts justify the model ingredients.
- Check whether model mechanisms speak to the empirical patterns.
- Check whether estimated parameters are tied to moments and identification.
- Discuss model fit before counterfactual interpretation.
- Make counterfactuals answer the original question and clarify implications.
- Back-integrate stabilized section changes into the abstract and introduction.

## Direct File Edits

- Apply minimal edits when the user asks for implementation.
- Keep unrelated style cleanup out of the patch.
- If a requested edit reveals a broader consistency issue, flag it separately rather than silently rewriting the whole draft.
