---
name: academic-review-paper
description: Pre-submission referee-style review of economics manuscripts from an explicit paper file path. Use for empirical, theoretical, quantitative macro, structural, or mixed empirical-model papers when Codex should simulate a skeptical economics referee, stress-test identification, theory, model assumptions, calibration, counterfactuals, robustness, and presentation, then produce a prioritized revision roadmap.
---

# Academic Review Paper
*v2.0 - Pre-submission economics self-review with empirical, theory, and quantitative-model stress testing*

Simulate a rigorous peer review of an academic economics manuscript before submission. Combine top-journal referee judgment with an adversarial stress test and editorial synthesis. Tailor the review to the manuscript type: empirical-only, theory-only, quantitative-model, or mixed empirical-model.

**Argument:** `$ARGUMENTS`
- Must contain a path to a paper file: `.pdf`, `.tex`, `.qmd`, `.md`, or `.docx`
- May also contain one mode: `full`, `quick`, `methodology`, or `da-only`
- May also contain one report output target after the manuscript path: an existing folder or an existing `.md` file
- If no valid file path is provided, stop and ask the user for the manuscript file path.

**Modes** (append to argument):
- `full` (default) - Referee pass + Devil's Advocate stress test + Editorial Synthesis
- `quick` - Single-pass referee report only
- `methodology` - Deep dive on empirical methods and/or model methods, depending on manuscript type
- `da-only` - Devil's Advocate stress test only

Examples:
- `/academic-review-paper /path/to/paper/main.tex full`
- `/academic-review-paper /path/to/manuscript.pdf methodology`
- `/academic-review-paper /path/to/paper.pdf full /path/to/reports/`
- `/academic-review-paper /path/to/paper/main.tex methodology /path/to/reviews.md`

---

## Instructions

### Step 0: Locate, Read, and Classify the Paper

1. Parse `$ARGUMENTS` into a manuscript file path and optional mode. Default to `full`.
2. Treat the first valid supported manuscript file path as the paper, even when that paper is itself `.md`.
3. Treat the first additional path after the manuscript path as the optional report output target.
4. Require an explicit manuscript file path. Do not infer a project, repository, or folder from a short name.
5. Verify the manuscript file exists and has a supported extension. If not, ask for the paper file path.
6. Validate the optional report output target if supplied:
   - Existing directory: create the auto-named report file inside it.
   - Existing `.md` file: append the report to the end of the file under `#review_[sanitized_paper_name]_[YYYY-MM-DD]`.
   - Missing path, non-directory folder target, or non-`.md` file: stop and ask for a valid existing output folder or existing `.md` report file.
7. For PDFs, use direct reading when reliable; otherwise run the bundled read-only extractor: `python3 scripts/extract_pdf_text.py "<paper.pdf>"`. If extraction fails or the PDF is image-only, stop and ask for OCR text or extracted text. Do not modify the source PDF.
8. For LaTeX, read the main file and any reachable `\input{}` or `\include{}` files. Read the full paper end-to-end before reviewing.
9. Load `references/real-referee-patterns.md` when calibration would help. It contains referee-report patterns and macro/theory/quantitative-model review cues.
10. Classify the manuscript before the review:
   - **empirical-only**: reduced-form, experimental, quasi-experimental, or descriptive empirical paper with no formal model doing substantive work.
   - **theory-only**: formal model or conceptual theory paper with little or no original empirical analysis.
   - **quantitative-model**: calibrated, estimated, simulated, structural, DSGE, heterogeneous-agent, search/matching, trade, IO, finance, or macro model used for quantitative discipline or counterfactuals.
   - **mixed empirical-model**: empirical facts and a theory/quantitative model both support the contribution.
11. State the classification in the report. If classification is ambiguous, choose the closest type and explain the uncertainty.

### Step 1: Econ Referee Pass

Think like a referee at a top economics journal. Evaluate only dimensions relevant to the paper; mark non-applicable dimensions as `N/A` and exclude them from the average score.

#### 1.1 Argument Structure
- Is the research question clearly stated and well-motivated?
- Does the introduction establish why the question matters?
- Is the logical flow sound: question, literature, method/model, results, interpretation, conclusion?
- Are conclusions supported by the evidence, theory, or quantitative exercise actually presented?
- Are limitations acknowledged honestly without weakening the central claim unnecessarily?

#### 1.2 Empirical Identification and Econometrics
Use when the paper makes empirical or causal claims.
- Is the causal or descriptive claim credible? What variation identifies it?
- Are identifying assumptions explicit and plausible?
- Check threats: omitted variables, reverse causality, measurement error, selection, spillovers, SUTVA violations, attrition, weak instruments, parallel trends, exclusion restrictions, and post-treatment controls.
- Is the estimator appropriate for the design, including modern concerns such as TWFE with staggered adoption?
- Are standard errors, clustering, functional form, multiple testing, heterogeneity, power, null results, and MDEs handled well?
- Does the paper provide positive mechanism evidence, not just rule out alternatives?
- For interventions, does the paper distinguish program-as-designed from program-as-implemented and discuss costs or ROI when relevant?

#### 1.3 Theory and Model Logic
Use when the paper contains a formal model, mechanism model, structural model, or quantitative model.
- Why is a model needed? Could the same contribution be made with a verbal mechanism, accounting exercise, or reduced-form evidence?
- What is the core economic mechanism, and which assumptions are essential for it?
- Are assumptions standard, disciplined by evidence, and economically plausible in this setting?
- Which assumptions drive the main proposition, comparative static, mechanism, or welfare conclusion?
- Are propositions, equilibrium definitions, proofs, and comparative statics clear and internally consistent?
- Are there alternative mechanisms or simpler models that could generate the same qualitative result?
- Does the model clarify something important that the empirics or narrative alone cannot?

#### 1.4 Quantitative Discipline, Validation, and Counterfactuals
Use for quantitative, structural, calibrated, estimated, or simulated models.
- Are calibration or estimation targets well chosen, identified, and not mechanically reproducing the main result?
- Are externally calibrated parameters justified and sensitivity-tested?
- Does the model match untargeted moments or other validation evidence?
- Do simulated mechanisms line up with empirical facts in sign, magnitude, timing, and heterogeneity?
- Are counterfactuals within a credible support of the model and data?
- Are welfare, distributional, transition, and general-equilibrium implications interpreted carefully?
- What additional counterfactual or quantitative decomposition would make the model more useful?

#### 1.5 Empirics-Model Link
Use for mixed empirical-model papers.
- What connects the empirical results to the model objects, parameters, wedges, shocks, frictions, or moments?
- Are the empirical facts used to motivate, discipline, validate, or test the model? Which role is actually played?
- Does the model explain the empirical patterns, or does it merely sit beside them?
- Are key model mechanisms contradicted by any empirical result, heterogeneity pattern, or external evidence?
- Does the quantitative exercise extend the empirical evidence in a credible way, such as by measuring welfare, GE effects, dynamic responses, or policy counterfactuals?

#### 1.6 Literature Positioning and Framing
- Are the key papers in the right literatures cited and characterized fairly?
- Is the contribution differentiated from adjacent empirical, theoretical, and quantitative work?
- Is the paper framed around the broadest defensible question it answers?
- Avoid overclaiming "first paper to..." unless the paper can defend it.
- Does the introduction explain what the findings or model mechanism mean for the literature?

#### 1.7 Writing Quality
- Is the paper clear, concise, and appropriately paced?
- Does the abstract summarize question, method/model, findings, and contribution?
- Is notation consistent and intuitive?
- Are definitions, assumptions, propositions, tables, and figures self-contained?
- Is the paper length appropriate for the contribution?

#### 1.8 Presentation and Transparency
- Are data, sample construction, variable definitions, and summary statistics clear when relevant?
- Are model equations, timing, equilibrium objects, calibration tables, estimation details, and simulation algorithms clear when relevant?
- Are tables and figures referenced, labeled, and interpretable without guesswork?
- Are appendices used well for proofs, robustness, extra moments, computational details, and sensitivity analysis?
- Are empirical and quantitative results separated clearly enough that readers know what is evidence, what is model output, and what is inference?

Rate each applicable dimension 1-5. Use `N/A` for irrelevant dimensions and compute the overall score over applicable dimensions only.

Generate 3-5 referee objections. For each:
- State the objection clearly.
- Explain why it could be fatal or damaging.
- Suggest how the author could address it.

If mode is `quick`, write the review report and stop after Step 4. If mode is `methodology`, focus on the relevant empirical-methods and/or model-methods dimensions, then stop after Step 4.

### Step 2: Devil's Advocate Stress Test

Skip if mode is `quick` or `methodology`.

Switch perspective. You are no longer balanced; you are looking for every vulnerability that a skeptical referee could exploit. Do not repeat Step 1 unless the point becomes sharper under adversarial framing.

Run these challenges:

#### 2.1 Core Thesis Challenge
Construct the strongest possible argument against the paper's main conclusion in 200-300 words.

#### 2.2 Cherry-Picking Detection
- Are results, moments, specifications, assumptions, examples, or counterfactuals selectively reported?
- Does the paper emphasize supportive evidence while burying weaker tests, failed moments, or inconvenient comparative statics?
- Is the sample, model variant, calibration target, or benchmark economy suspiciously convenient?

#### 2.3 Confirmation Bias and Model Necessity
- Does the paper cite only evidence or theory supporting its hypothesis?
- Is the theoretical framework chosen because it predicts the desired result?
- Is the model necessary, or is it complexity that protects a simple claim from direct scrutiny?
- What would the paper lose if the model were removed or replaced with a simpler mechanism?

#### 2.4 Logic Chain and Assumption Fragility
- Trace the argument from assumptions or identifying variation through results to conclusions.
- Identify any point where the chain breaks or requires an unstated leap.
- For models, ask which assumptions are doing the work and whether relaxing them would overturn the mechanism, sign, magnitude, or welfare result.

#### 2.5 Overgeneralization and External Validity
- Do empirical results or model counterfactuals generalize beyond the sample, country, time period, calibration, or policy environment?
- Does the paper claim more generality than the evidence or model supports?
- Are counterfactuals extrapolating outside the region where the model was disciplined?

#### 2.6 Alternative Explanations and Observational Equivalence
List 2-4 alternative explanations or mechanisms not adequately ruled out. For each, explain what evidence, model extension, heterogeneity test, moment, or counterfactual would distinguish it from the author's story.

#### 2.7 Empirics-Model Disconnect
Use for mixed papers.
- Do the empirical facts actually discipline the model, or are they only motivation?
- Could the model fit the selected facts while missing the mechanism implied by the evidence?
- Are key parameters inferred from moments that could also reflect other frictions or shocks?

#### 2.8 Quantitative Counterfactual Overreach
Use for quantitative models.
- Are policy experiments credible and connected to variation in the data?
- Are welfare calculations transparent and sensitive to assumptions?
- Are transitional dynamics, distributional effects, and GE feedbacks handled or ignored in a way that changes conclusions?
- What could a quantitative model do here that the current exercise does not yet do?

#### 2.9 Stakeholder and Welfare Blind Spots
- Whose perspective is missing?
- Are distributional, welfare, market-clearing, fiscal, political-economy, or implementation implications ignored?
- Would policymakers or practitioners interpret the findings differently than the authors intend?

#### 2.10 "So What?" Test
- If the paper is exactly right, what changes?
- Is the contribution incremental or transformative?
- Does the paper answer a question economists, policymakers, or adjacent literatures are actually asking?

Classify each finding as:
- **CRITICAL**: Fatal flaw in the core argument; cannot be rescued without fundamental revision.
- **MAJOR**: Seriously undermines credibility but can be addressed with additional analysis, modeling, or writing.
- **MINOR**: Worth fixing but does not threaten the core argument.
- **OBSERVATION**: Not a defect, but an alternative perspective worth considering.

If mode is `da-only`, write the Devil's Advocate report and stop after Step 4.

### Step 3: Editorial Synthesis

Only runs in `full` mode.

#### 3.1 Consensus Analysis
- Where do the referee evaluation and Devil's Advocate agree?
- Where do they disagree?
- Which adversarial findings are genuine threats versus hypothetical concerns unlikely to bother a real reviewer?

#### 3.2 Decision
Based on the synthesis:
- **Strong Accept**: Excellent across applicable dimensions; only minor or observation-level concerns.
- **Accept with Minor Revision**: Strong paper with 1-2 addressable issues and no critical findings.
- **Revise and Resubmit**: Good potential, but multiple major issues or one addressable critical issue.
- **Reject**: Fundamental identification, model, argument, or contribution problems that cannot be fixed with revision.

#### 3.3 Revision Roadmap
Organize all findings into:
- **Priority 1 (Required)**: Must fix before submission.
- **Priority 2 (Strongly Recommended)**: Would significantly strengthen the paper.
- **Priority 3 (Nice to Have)**: Polish, framing, robustness, or presentation improvements.

### Step 4: Write the Report

Load `references/review-report-template.md` before writing the final report. Follow its structure while omitting sections that do not apply to the selected mode.

If no report output target was supplied, save the full report to the working directory as `review_[sanitized_paper_name]_[YYYY-MM-DD].md`.

If the report output target is an existing directory, save the full report inside that directory as `review_[sanitized_paper_name]_[YYYY-MM-DD].md`.

If the report output target is an existing `.md` file, append the report to the end of that file under the exact heading `#review_[sanitized_paper_name]_[YYYY-MM-DD]`. Do not replace existing file content.

Tell the user the full path to the output file.

---

## Bundled Resources

- `scripts/extract_pdf_text.py`: read-only PDF text extraction using `pdftotext` with `pypdf` fallback.
- `references/review-report-template.md`: final report template.
- `references/real-referee-patterns.md`: tone, referee-pattern, and macro/theory/quantitative-model calibration cues.

---

## Principles

- Be constructive: every criticism needs a feasible suggestion.
- Be specific: cite sections, equations, tables, pages, assumptions, moments, or counterfactuals.
- Think like a top economics referee: prioritize what would make a referee recommend rejection or become enthusiastic.
- Tailor the review to the manuscript type; do not demand irrelevant empirical tests from pure theory papers or irrelevant formal proofs from empirical-only papers.
- Distinguish direct evidence, model output, and inference.
- Distinguish fatal flaws from polish.
- Acknowledge strong execution and intellectual contribution when present.
- Be honest about uncertainty: if a section cannot be read clearly, say so.
- Do not fabricate facts, results, proofs, tables, or citations.
- Do not hallucinate citations. If suggesting missing references, tell the user to verify them.
- Offer choices rather than mandates when the issue is presentational or stylistic.
