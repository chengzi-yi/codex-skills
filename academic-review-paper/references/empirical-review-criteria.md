# Empirical Review Criteria

Use only the criteria relevant to the paper's actual claims and research design. A descriptive paper need not satisfy a causal design, and a causal paper should not receive credit merely for descriptive robustness.

## Contents

- Claim and design map
- Identification
- Estimation and inference
- Mechanisms
- External validity and implementation
- Data and presentation

## Claim And Design Map

For each central empirical claim, identify:

- the outcome and population;
- the variation or comparison supporting it;
- whether the claim is descriptive, predictive, structural, or causal;
- the identifying assumptions stated or implied;
- the main table, figure, or specification carrying the claim.

Flag a mismatch when the prose is more causal or general than the design supports.

## Identification

Evaluate threats that are plausible for the actual design rather than reciting every possible threat. Relevant questions may include:

- What generates treatment, exposure, or comparison-group variation?
- Are timing, selection, anticipation, spillovers, attrition, measurement, or equilibrium responses capable of generating the result?
- For instruments, are relevance, exclusion, monotonicity, and the complier interpretation defensible?
- For difference-in-differences or event studies, are treatment timing, comparison groups, pre-trends, anticipation, and heterogeneous effects handled appropriately?
- For experiments, are randomization, implementation fidelity, noncompliance, attrition, interference, and analysis choices transparent?
- For matching or weighting, are overlap, balance, extreme weights, estimand, and selection-on-observables assumptions explicit?
- For panels or regressions, could fixed effects, controls, trends, functional form, or post-treatment variables absorb or create the relevant variation?

Separate a design limitation from a correctable implementation error. When stronger identification is unavailable, consider whether narrowing the claim is the honest response.

## Estimation And Inference

Check whether the estimator and uncertainty match the assignment mechanism and data structure. Consider clustering, serial and spatial correlation, generated regressors, multiple outcomes or specifications, small-sample corrections, functional form, missingness, outliers, and weak identification when relevant.

For null or imprecise results, ask what effect sizes the design can rule out. MDEs, confidence intervals, equivalence bounds, or power calculations are useful only when they illuminate the substantive claim.

Recheck formulas and table notes against the reported estimand. If code is unavailable, distinguish a likely text error from a verified implementation error.

## Mechanisms

Ask whether mechanism evidence distinguishes the proposed channel from credible alternatives. Useful evidence may include direct measures, timing, heterogeneous effects motivated ex ante, mediators handled with appropriate causal caution, or tests whose predictions differ across mechanisms.

Do not demand arbitrary heterogeneity cuts. Suggest a test only when its result would change the interpretation. For mixed empirical-model papers, connect these tests to model objects and predictions using the model review criteria.

## External Validity And Implementation

Assess generalization relative to the population, institutional setting, time period, policy scale, and equilibrium environment actually studied. When relevant:

- distinguish an intervention as designed from what was implemented;
- consider displacement, spillovers, market clearing, or general-equilibrium effects;
- compare benefits with costs or implementation burdens;
- identify which observable comparisons could inform representativeness.

These are conditional questions, not universal requirements.

## Data And Presentation

Check whether a reader can reconstruct:

- sample construction, exclusions, timing, units, and missingness;
- variable and outcome definitions;
- treatment, control, weights, fixed effects, controls, and standard errors;
- the relationship between raw data, transformed measures, and reported samples;
- whether tables and figures are self-contained and consistent with the text.

Inspect discrepancies across the abstract, main text, tables, figures, appendices, and robustness samples. Distinguish accounting or measurement mechanics from economic performance where relevant.
