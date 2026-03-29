---
name: academic-plotting
description: Create or restyle figures for academic paper drafts and presentation slides, and patch plotting code so future runs inherit the same visual contract. Use when a user wants cleaner publication-ready plots, consistent palettes and typography, legend or annotation cleanup, thicker lines or larger fonts for slides, print-safe paper figures that remain legible in black-and-white, or fast aesthetics-only iteration without rerunning expensive estimation, optimization, or data generation.
---
# Academic Plotting

Use this skill when the task is about figure presentation rather than model estimation. Prefer replotting from saved tables or saved intermediate outputs. Only run upstream computation when the plotting code cannot be exercised from existing artifacts.

## Workflow

1. Find the canonical saved artifact that drives the figure.
   - Prefer saved tables, regression output tables, or cached panel summaries.
   - Avoid rerunning optimization, estimation, simulation, or data generation when the request is only aesthetic.
2. Decide whether the change belongs in:
   - a standalone replot helper
   - the main pipeline plotting code
   - both
3. Keep one visual contract across paper and slide variants.
   - Use the same palette, type family, and line semantics.
   - Change only size, font scale, line weight, and spacing between variants.
   - Require paper-mode choices to remain interpretable in grayscale or black-and-white printing.
4. Refresh only the smallest useful figure set.
   - For iterative aesthetics work, refresh one representative figure family only.
   - Do not regenerate unrelated output trees.
5. Sync the plotting documentation after the style is accepted.

## Test Mode

Enter test mode when the user is still tuning aesthetics.

- Use one preferred or canonical data source only.
- Skip re-optimization and re-estimation whenever possible.
- Reproduce only one set of figures to preview the visual change.
- If the main pipeline plotting code also needs to change, patch it after the preview style is accepted.
- If any execution is needed only to validate plotting wiring, use the smallest smoke configuration available.

## Style Contract

Read [references/academic-style.md](references/academic-style.md) for the default paper/slides configuration, palette, typography, legend policy, and the expected difference between production mode and test mode.

## Output Expectations

- Preserve the scientific content of the figure.
- Make style changes reproducible from code, not manual edits.
- If the task is aesthetics-only, state explicitly that no estimation or optimization was rerun.
