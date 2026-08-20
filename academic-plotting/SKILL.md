---
name: academic-plotting
description: Design, audit, create, or restyle reproducible academic research figures and plotting code from approved data and metric definitions. Use for visual review, figure-family design, paper, appendix, and slide styling, and rendered-output QA. Do not use for choosing estimands or samples, changing statistical definitions, running upstream estimation or simulation, document layout, general data analysis, or manual bitmap editing.
---

# Academic Plotting

Own the visual presentation and approved composition of academic figures without silently changing their analytical meaning.

## Route The Request

- **Review or advice:** Inspect the requested figures and return prioritized findings. Do not edit files or run plotting or upstream pipelines.
- **Figure design:** Specify composition, encodings, and audience-appropriate layout from approved analytical objects. Keep suggestions non-mutating unless the user requests implementation.
- **Implementation or restyling:** Update the canonical plotting code and regenerate only the affected figure family.

Keep the output mode aligned with the request. Do not turn a review into an edit or a figure-design discussion into additional analysis.

## Preflight

Before changing code or figures:

1. Resolve the target artifact's Git root and read applicable `AGENTS.md`, repository plotting guidance, and venue requirements.
2. Identify the intended destination and display size, canonical plotting entrypoint, approved source artifacts and metric definitions, required outputs, and validation conditions.
3. Classify the request as presentation-only or analytically consequential.

Treat sample support, estimands, derived metrics, transformations, uncertainty definitions, and missing-value handling as analytical decisions. Follow the approved specification; never introduce common-support truncation, normalization, smoothing, sample changes, or companion figures for visual convenience. If a required analytical choice is unresolved, ask before plotting it.

Apply visual guidance in this order: explicit user instructions, venue requirements, repository guidance, surrounding artifact conventions, then the bundled fallback.

## Evidence And Computation Boundary

- Prefer approved saved tables, regression outputs, cached summaries, and other canonical intermediate artifacts.
- Plotting and lightweight transformations from those artifacts may proceed when their definitions are already approved. For a user-defined derived metric, verify its formula, bounds, missingness rules, and source values before plotting it.
- Require explicit user approval before running estimation, optimization, simulation, or upstream data regeneration. If the saved artifacts are missing, stale, or insufficient, stop and explain what upstream work would be required.
- Preserve values, uncertainty calculations, units, transformations, sample definitions, support, and disclosure or missing-value states unless the user explicitly changes the analytical specification.
- Make accepted changes reproducible from code. Do not manually alter bitmap outputs.

## Implementation Loop

- Prefer the canonical plotting pipeline so future runs inherit the change.
- Use a standalone helper only for an explicitly one-off result, an unavailable main pipeline, or an isolated preview. Do not maintain two drifting style implementations.
- Preview the smallest representative figure set needed to establish the visual direction. When the specification is clear, iterate autonomously; ask only when a material visual choice remains unresolved.
- Once the direction is settled, regenerate only the affected figure family and preserve unrelated output trees.
- Update plotting documentation only when stable commands, output locations, interfaces, validation instructions, or project style conventions changed. Do not force documentation churn for reviews or one-off visual adjustments.

## Visual Contract And QA

Preserve semantic mappings across related paper and slide variants while allowing format-specific aspect ratios, panel layouts, annotation density, titles, direct labels, and legend placement.

Keep paper figures interpretable in grayscale or black-and-white printing. Reinforce important multi-series color mappings with line type, marker shape, direct labels, or another redundant encoding; do not add needless distinctions to a single-series figure.

Read [references/academic-style.md](references/academic-style.md) when repository or venue guidance does not fully determine the design, or when a review explicitly asks for assessment against the fallback academic style.

Render the actual output at its intended size and inspect, as applicable:

- clipping, overlap, whitespace, font availability, and panel balance;
- axes, units, transformations, uncertainty bands, labels, legends, and annotations;
- panel order, series identity, year or sample support, and reference or recession shading;
- grayscale and color accessibility for important multi-series figures;
- output format and effective resolution.

Compare the plotted series, row counts, support, and derived values with the approved source artifacts. Do not accept a visually clean figure that changes the underlying evidence.

## Handoff

Report the review findings or figures and code changed, the source artifacts used, checks and visual-inspection outcomes, whether documentation changed, and whether any upstream computation ran. Flag unresolved analytical choices or rendering limitations.
