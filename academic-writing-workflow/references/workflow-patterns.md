# Workflow Patterns

These patterns encode the user's preferred writing workflow.

Use the mode relevant to draft development, argument review, or technical writing. Local-editing mechanics live in the entrypoint and `writing-principles.md`.

## Draft Development

- Lay out a short working plan before major drafting or restructuring.
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

## Technical Exposition

- Use for writing model-solution, estimation, moment, and counterfactual descriptions inside a paper, appendix, or slide artifact.
- Base statements on source documents, code, tables, notes, or supplied draft context.
- State what is directly documented and what is inferred.
- Explain the economic role of technical objects, not only the computational step.
- Keep enough detail that another graduate student could reproduce the key number or procedure from the paper and appendices.
