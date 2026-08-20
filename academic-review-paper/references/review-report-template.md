# Academic Review Paper Report Template

Use one prioritized findings list. Do not repeat the same concern as a major concern, referee objection, adversarial finding, and roadmap item. Cross-reference stable finding IDs instead.

## Contents

- Shared report
- Purpose-specific modules
- Optional adversarial module

## Shared Report

```markdown
# Manuscript Review: [Paper Title]

**Date:** [YYYY-MM-DD]
**Purpose:** [author review / discussant review / journal referee]
**Depth or focus:** [prioritized / quick / methodology / da-only / full / user-specified]
**Manuscript type:** [empirical-only / theory-only / quantitative-model / mixed empirical-model]
**Coverage:** [surfaces reviewed and any material limitations]

## Summary Assessment

[Restate the research question, approach, main contribution, and overall assessment fairly. Distinguish what the paper demonstrates from the reviewer's interpretation.]

## Strengths

- [Specific strength with a source locator and explanation of why it matters.]

## Prioritized Findings

### MC1: [Concern title]

- **Materiality:** [critical / major]
- **Confidence:** [high / medium / low]
- **Location:** [section, page, equation, table, figure, assumption, moment, or counterfactual]
- **Claim at issue:** [the conclusion or interpretation affected]
- **Evidence and reasoning:** [source-grounded analysis]
- **Why it matters:** [effect on identification, mechanism, validity, contribution, or interpretation]
- **Response path:** [feasible analysis/revision, or the design decision/evidence needed]

## Minor And Specific Comments

- **m1 — [location]:** [concise comment and response where useful]
```

Omit `Minor And Specific Comments` when it would add only low-value polish. Add no numeric score table unless the user explicitly requests scoring.

## Purpose-Specific Modules

Append only the module matching the review purpose.

### Author Review

```markdown
## Revision Roadmap

### Priority 1: Required Before Submission
- [MC identifier and concrete next action]

### Priority 2: Strongly Recommended
- [MC identifier and concrete next action]

### Priority 3: Optional Polish
- [Action only when it materially improves the paper]
```

### Discussant Review

```markdown
## Discussant Preparation

### Main Discussion Points
- [Finding ID, constructive framing, and why the audience should care]

### Questions For The Author
- [Question that could clarify or advance the paper]

### Presentation Takeaways
- [Concise framing suitable for an oral discussion or planning a slide]
```

Do not create presentation slides unless the user requests them.

### Journal Referee

```markdown
## Comments To The Authors

[Prioritized assessment written for the authors.]
```

Add `Confidential Comments To The Editor`, a recommendation, or journal-form scores only when the user requests them or the confirmed assignment requires them. Keep confidential comments separate from comments to authors.

## Optional Adversarial Module

Use for `full` and `da-only`. In `full`, do not repeat the prioritized findings.

```markdown
## Adversarial Stress Test

### Strongest Counter-Case
[The strongest source-grounded case against the central claim.]

### What The Balanced Review May Be Underweighting
- [New vulnerability or a sharper interpretation, cross-referencing MC IDs where relevant]

### Alternative Explanations Or Mechanisms
- [Alternative and the evidence, model comparison, or design change that would distinguish it]

## Synthesis

[For `full` only: explain which adversarial points change the priorities and which remain speculative.]
```
