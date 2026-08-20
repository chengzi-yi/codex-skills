# Academic Plotting Style Fallback

Use this reference only when explicit user instructions, venue requirements, repository guidance, and surrounding artifact conventions do not fully determine the visual design. It is a fallback, not a project style mandate.

## Semantic Clarity And Accessibility

- Assign colors and other encodings by stable semantic role, and preserve those mappings across related figures.
- Use a restrained palette with sufficient contrast against the background and between adjacent series.
- Do not rely on color alone for important multi-series paper figures. Combine color with line type, marker shape, direct labels, or another redundant encoding.
- Keep text, axes, reference lines, and grids subordinate to the evidence. Add frames or grids only when they improve comparison.
- Use a legible type family that supports the required symbols and matches the surrounding artifact when practical.

When no project palette exists, this accessible palette is an optional starting point:

- primary series: `#0072B2`
- secondary series: `#009E73`
- tertiary series: `#D55E00`
- quaternary series: `#CC79A7`
- highlighted benchmark or selected point: `#B2182B`
- neutral guide or grid: `#D0D0D0`

Verify that important series differ in luminance or redundant encoding as well as hue.

## Audience And Format

### Paper And Appendix Figures

- Design for the figure's intended physical placement, including column width, page width, or appendix layout.
- Preserve legibility after grayscale conversion or black-and-white printing.
- Prefer compact layouts only when labels, uncertainty, and distinctions remain readable at final size.
- Use vector output for line art and text when the repository and destination support it. For raster output, choose sufficient effective resolution at the final placement size.

### Presentation Figures

- Design for viewing at distance: larger type and marks, stronger contrast, and less visual density when necessary.
- Recompose panels, annotations, labels, and legends when a paper layout would be too dense on a slide.
- Preserve the meaning of colors, lines, markers, and reference objects shared with the paper version.

### Diagnostic And Analysis Figures

- Prioritize faithful comparison, visible support, and clear thresholds or reference values over decorative polish.
- Show coverage differences when they are analytically relevant; do not hide unequal support by silently truncating or filling series.
- Make provisional or diagnostic status clear when a figure is not yet intended for publication.

## Legends, Labels, And Annotations

- Use direct labels when they reduce lookup effort without crowding the plot.
- Keep a legend when multiple series or encodings would otherwise be ambiguous, especially when the figure may be read outside its immediate context.
- Remove a legend only when the mapping remains unambiguous from labels, panels, captions, or surrounding context.
- Use titles, captions, and annotations to add information rather than repeat filenames or axis labels.
- Keep thresholds, selected points, recession shading, and other annotations visually distinct but subordinate to the main evidence.

## Axes And Uncertainty

- Preserve units, transformations, and meaningful reference points. Label logarithmic, normalized, indexed, truncated, or broken axes explicitly.
- Choose limits from the approved data and the comparison purpose, with enough padding to avoid clipping. Do not manipulate limits to exaggerate or suppress variation.
- Show uncertainty intervals without changing their calculations. Ensure bands, whiskers, and interval endpoints are visible and correctly aligned with their estimates.
- Use shared axes only when they support the intended comparison and do not conceal material scale differences.

## Rendered Output

- Follow repository or venue format requirements first.
- Inspect the rendered artifact rather than relying only on plotting parameters or source code.
- Check clipping, overlap, font substitution, panel balance, legend placement, annotation collisions, and excess whitespace.
- Check the figure at its intended paper, appendix, slide, or diagnostic size.
- For important multi-series paper figures, inspect a grayscale rendering or equivalent non-color distinction.
