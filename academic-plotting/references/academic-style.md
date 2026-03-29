# Academic Plotting Style

## Default visual direction

- Use a restrained academic palette with clear semantic color mapping.
- Keep a white background, boxed frame, black axes and text, and a light gray grid.
- Use a serif math-friendly type family when available; `Computer Modern` is the default in the current Julia workflow.
- Remove decorative titles unless the user specifically wants them.
- For paper figures, assume black-and-white printing is a real use case.
- Do not rely on color alone to distinguish important series, benchmarks, or selected points in paper mode.

## Paper vs slides

Keep the same palette and semantics across both variants.

- Paper mode:
  - prioritize dense but readable layout
  - moderate line weights
  - larger-than-default labels suitable for manuscript screenshots or draft insertion
  - choose colors with distinct grayscale contrast, and add line-style or marker differences when multiple series must remain distinguishable after printing
- Slides mode:
  - increase guide, tick, and legend fonts
  - increase line widths
  - increase lower margin or whitespace if annotations or legends need more room

## Legend and annotation rules

- Default to removing legends when the mapping is obvious from axes or context.
- Keep a legend only when it carries real meaning, such as a highlighted benchmark or selected optimum.
- If the user is deciding between a legend and an annotation, treat that as a test-mode styling choice and replot only one canonical figure set.

## Confidence intervals

- Make interval bands readable.
- If a narrow y-range makes the interval look misleadingly thin or visually clipped, widen the y-range rather than changing the uncertainty calculation.

## Test mode

Use test mode for fast visual iteration.

- Reuse the preferred saved output table whenever possible.
- Replot one canonical figure set only.
- Skip upstream re-estimation and data regeneration unless plotting depends on a new code path that cannot be exercised otherwise.
- If a live run is unavoidable, use a smoke configuration only.

## Reference configuration

Use these as default starting points for academic figures. Adjust only when the figure family or publication format makes the defaults clearly too cramped or too loose.

### Semantic palette template

Use colors by role, not by variable name.

- primary series: `#0072B2`
- secondary series: `#009E73`
- tertiary series: `#D55E00`
- quaternary series: `#CC79A7`
- highlighted benchmark or selected point: `#B2182B`
- grid: `#D0D0D0`

For paper mode:

- prefer darker, higher-contrast colors over light hues such as yellow or pale cyan
- verify that adjacent series differ in luminance as well as hue
- when the palette alone is not safely distinguishable in grayscale, add dashes, dots, marker shapes, or direct labels

### Paper baseline

- size: about `1400x900`
- dpi: about `220`
- main line width: about `3.0`
- highlight or reference line width: about `2.5`
- ribbon alpha: about `0.18`
- guide font size: about `24`
- tick font size: about `19`
- legend font size: match the guide font size
- margins: allow extra bottom margin only when x-axis annotations or dense tick labels require it
- print-safety rule: the figure should remain readable if converted to grayscale or printed on a black-and-white printer

### Slides baseline

- size: about `1800x1100`
- dpi: about `220`
- main line width: about `5.0`
- highlight or reference line width: about `4.0`
- ribbon alpha: about `0.22`
- guide font size: about `28`
- tick font size: about `22`
- legend font size: match the guide font size
- margins: increase whitespace more aggressively than in paper mode

### Figure-family defaults

- profile or objective plots:
  - suppress the main-series legend when the line identity is obvious
  - keep a legend entry only for a benchmark, selected optimum, or highlighted reference if that is the only meaningful guide
- parameter-path plots:
  - suppress legends by default when one curve is shown per panel
  - remove titles unless they add information not already carried by filenames, captions, or surrounding text
- uncertainty bands:
  - widen the y-range if the interval looks visually clipped or implausibly thin
  - do not manipulate the interval itself to solve a readability problem
- print-safe distinction:
  - if a paper figure has multiple visually important series, ensure they remain distinguishable without color by combining color with line pattern or marker differences
