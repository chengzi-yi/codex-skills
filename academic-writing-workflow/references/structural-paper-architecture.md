# Structural Paper Architecture

Use this as the default architecture for papers that combine empirical facts with structural estimation and counterfactuals.

## Motivation And Introduction

- Question: state the research question in plain language.
- Stakes: explain why readers should care through a puzzle, policy relevance, or gap in the literature.
- Literature position: say what existing work answers and why that answer is incomplete for this question.
- Methodology: preview the empirical facts, model, estimation, or counterfactual approach.
- Answer: state the main findings and magnitudes early.
- Contribution: explain what the paper adds relative to close work.

## Facts, Data, And Moments

- Start with motivating observations that discipline the paper.
- Describe data only to the extent needed to understand the facts, sample, measurement, and estimation.
- Present measurement choices before results that rely on them.
- Connect facts to moments when the structural estimation targets them.
- Separate targeted moments from implied or validation moments when that distinction matters.

## Theory, Model, And Mechanisms

- Give an overview of the model before equations.
- Explain states, choices, constraints, shocks, and payoffs in the order readers need them.
- Include only model details needed for estimation, interpretation, or counterfactuals in the main text.
- For each key model ingredient, explain the economic role and the empirical pattern it helps address.
- Place long derivations, numerical algorithms, or robustness variants in the appendix unless they are central to the argument.

## Quantitative Analysis

- Explain how the model is taken to the data.
- For estimation, distinguish:
  - externally calibrated or predefined parameters
  - first-stage or auxiliary estimates
  - structurally estimated parameters
  - targeted moments and weighting choices
- Discuss model fit before using the model for counterfactuals.
- Tie parameters to the moments or variation that identify them.
- Interpret parameter magnitudes economically, not only numerically.

## Counterfactuals And Implications

- State the counterfactual experiment before presenting results.
- Explain what mechanism changes in the experiment.
- Connect counterfactual outcomes back to the original question.
- Separate model-implied implications from policy recommendations.
- Report aggregate and distributional outcomes when both matter for the contribution.

## Conclusion

- Restate the answer to the question, not the full paper.
- Mention the main implication and any important limitation briefly.
- Do not introduce new results.
