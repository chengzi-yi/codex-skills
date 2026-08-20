---
name: academic-review-paper
description: Review an academic economics manuscript from an explicit file path for author-side pre-submission critique, work-in-progress discussant preparation, or a permitted journal-referee assignment. Use for source-grounded evaluation of contribution, identification, theory, quantitative discipline, empirics-model links, and presentation. Do not use for proofreading-only edits, standalone explanations, literature reviews, submission packaging, or manuscript rewriting.
---

# Academic Review Paper

Produce a rigorous, source-grounded economics manuscript review calibrated to the paper's stage and the user's role. Prioritize the concerns that could materially change the paper rather than reproducing a generic referee checklist.

## Inputs And Routing

Require an explicit manuscript file path with extension `.pdf`, `.tex`, `.qmd`, `.md`, or `.docx`. Do not infer a paper from a project name, repository, or current folder. From the user's prompt, also identify any requested purpose, focus or depth, and report destination.

Route the purpose as follows:

- **Author review**: default when the purpose is not otherwise clear. Produce a pre-submission assessment and revision roadmap.
- **Discussant review**: use for a work-in-progress discussion, seminar, conference, or discussant request. Produce prioritized concerns, constructive questions, and presentation-facing takeaways; do not add a journal verdict.
- **Journal referee**: before reading the manuscript, require confirmation that the user is permitted to use AI assistance for the assignment. Confirmation already present in the prompt is sufficient. After confirmation, keep the workflow local-only: do not browse, upload manuscript content, or disclose identifying details externally unless the user separately authorizes external verification and it is compatible with the applicable policy.

The default depth is a prioritized review. Recognize these legacy mode tokens when the user supplies them:

- `quick`: concise prioritized review.
- `methodology`: focus on applicable empirical and/or model methods.
- `da-only`: adversarial stress test only.
- `full`: comprehensive prioritized review plus a non-duplicative adversarial stress test and synthesis.

Do not add numeric scores, accept/reject recommendations, or confidential editor comments unless the user explicitly requests them or they are required for a confirmed journal-referee assignment.

## Read And Map The Manuscript

1. Verify that the manuscript exists and has a supported extension. If not, ask for a valid explicit path.
2. Read the full artifact before reviewing it:
   - For PDF, use direct reading when reliable. Otherwise run `python3 scripts/extract_pdf_text.py "<paper.pdf>"`. If extraction fails or the file is image-only, ask for OCR or extracted text. Never modify the PDF.
   - For LaTeX, follow reachable `\input{}` and `\include{}` files and inspect appendices, tables, figures, captions, and relevant bibliography material referenced by the manuscript.
   - For other formats, use the available local reader and inspect embedded or linked tables and figures when possible.
3. Build a coverage map of the main text and supporting surfaces actually inspected. Record anything unreadable, missing, or not visually verifiable; do not imply complete coverage when it was not achieved.
4. Classify the manuscript for routing:
   - **empirical-only**: empirical analysis without a substantive formal model;
   - **theory-only**: formal or conceptual theory with little original empirical analysis;
   - **quantitative-model**: calibrated, estimated, simulated, or structural model used for quantitative discipline or counterfactuals;
   - **mixed empirical-model**: empirical evidence and a substantive theory or quantitative model jointly support the contribution.

## Load Review Guidance

- Always read [review-calibration.md](references/review-calibration.md).
- Read [empirical-review-criteria.md](references/empirical-review-criteria.md) when the paper makes descriptive, empirical, or causal claims.
- Read [theory-quantitative-review-criteria.md](references/theory-quantitative-review-criteria.md) when the paper contains a substantive theoretical, structural, calibrated, estimated, or simulated model.
- Mixed papers require both criteria references.
- Read [review-report-template.md](references/review-report-template.md) before writing the report.

## Conduct The Review

Reconstruct the paper's research question, claimed contribution, argument chain, evidence or model discipline, and conclusions before criticizing it. Evaluate contribution, literature positioning, exposition, and transparency for every paper, then apply only the routed empirical or model criteria.

Distinguish clearly among:

- statements and literature characterizations made by the manuscript;
- direct empirical evidence shown in the manuscript;
- model assumptions, mechanisms, and output;
- reviewer inference or proposed interpretation;
- externally verified facts or literature.

Do not present the manuscript's account of prior literature as independently verified. Do not browse by default. If the user requests external literature verification, use primary sources, cite them, and label what was verified. For a confidential journal assignment, obtain explicit authorization before any external lookup and avoid queries that reveal confidential draft details.

Prioritize findings by materiality without forcing a fixed count. Give each major concern a stable identifier (`MC1`, `MC2`, and so on) and include:

- an exact section, page, equation, table, figure, assumption, moment, or counterfactual locator;
- the claim or conclusion at issue;
- the evidence and reasoning supporting the concern;
- why the concern matters and its materiality;
- confidence (`high`, `medium`, or `low`);
- a feasible response, or the design decision or new evidence required when no reliable fix can be prescribed.

Recheck any alleged formula error, contradiction, invalid estimator, proof gap, or critical inconsistency against the source before reporting it. If code, derivations, data, or other decisive evidence is unavailable, label the finding provisional and say what would resolve it.

For `full`, use the adversarial pass to sharpen or challenge the prioritized findings, not to restate them. For `da-only`, construct the strongest skeptical case while retaining source locators, uncertainty, and applicable evidence boundaries.

## Write The Report

Follow the shared findings structure and include only the module for the routed purpose. Keep stable finding identifiers so follow-up questions can refer back to them. Report coverage limitations explicitly.

Save a report by default:

- With no destination, create `review_[sanitized_paper_name]_[YYYY-MM-DD].md` in the working directory.
- With an existing directory destination, create the same auto-named file there.
- If an auto-named file already exists, do not overwrite it; add `_[HHMMSS]` before `.md`.
- With an existing `.md` destination, append under the exact heading `#review_[sanitized_paper_name]_[YYYY-MM-DD]`. If that heading already exists, ask before appending another review.
- For a missing destination, a non-directory folder target, or a non-Markdown file target, ask for a valid existing directory or existing `.md` file. Do not create the missing explicit target.

Tell the user the full report path and the important coverage or verification limitations. Do not include the absolute local manuscript path, output path, skill implementation name, or skill version inside the report itself.

## Boundaries

- Review the manuscript; do not edit or rewrite it unless the user separately requests that work.
- Do not fabricate facts, results, proofs, tables, equations, citations, or source coverage.
- Offer concrete options for presentational choices, but do not force substantive fixes unsupported by the paper's evidence or available data.
- Do not stage, commit, or push the manuscript or generated report unless the user separately requests Git operations.

## Bundled Resources

- `scripts/extract_pdf_text.py`: read-only PDF text extraction using `pdftotext` with `pypdf` fallback.
- `references/review-calibration.md`: purpose, tone, prioritization, confidence, and adversarial calibration.
- `references/empirical-review-criteria.md`: empirical identification, inference, mechanisms, and transparency.
- `references/theory-quantitative-review-criteria.md`: theory, quantitative discipline, validation, and empirics-model links.
- `references/review-report-template.md`: shared findings structure and purpose-specific report modules.
