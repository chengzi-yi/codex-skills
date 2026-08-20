# Writing Principles

Use these rules when proofreading, restructuring, or drafting academic economics prose. Choose the section that matches the part of the paper under revision.

## General Principles

### Structure And Organisation

- Identify the one central and novel contribution. State it concretely.
- Open with three questions: what puzzle or research question motivates the paper, what approach differs from the literature, and what the paper finds.
- Say what the paper finds, not only what it studies.
- Put the punchline early. Readers skim and should not wait for the main result.
- Use triangular or newspaper structure: most important claim first, details later.
- Put nothing before the main result that readers do not need to understand it.
- Do not write the paper as a travelogue of the research process.
- Keep the introduction focused on the question, contribution, method, and main findings.
- Use the literature review to position the paper against the closest work, not to catalogue every paper.
- Use appendices for robustness checks, derivations, implementation details, or side analyses that are not needed for the main narrative.

### Prose Style

- Keep prose short, active, precise, and concrete.
- Prefer subject-verb-object sentences with short grammatical subjects.
- Express key actions as verbs rather than nominalisations.
- Begin sentences with old information and end with new or stress-worthy information.
- Keep paragraph topics focused on a limited set of concepts.
- Use present tense for what the paper shows and for established findings unless past tense is clearly needed.
- Avoid throat-clearing: "It should be noted that", "it is worth noting", "This paper aims to", "A comment is in order". Just make the comment.
- Search for unnecessary "that" and delete setup phrases when the sentence works without them.
- Avoid adjectives that praise the work. Let facts and magnitudes carry the claim.
- Avoid vague "this". Name the antecedent: "This estimate", "This mechanism", "This pattern".
- Use "in which" for models, settings, and mechanisms; reserve "where" for places.
- When describing the sign of a causal link, state one direction. Add "and vice versa" only if the reverse direction is necessary.
- Avoid repeated claims. If the same idea appears twice, keep the sharper version.
- Avoid heavy parentheticals and footnotes for points that belong in the main text.
- Use "I" for sole-authored work when responsibility matters; otherwise tables, figures, estimates, or models can often be the subject.
- Preserve the artifact's established English variety; follow the repo map when it specifies one.

### Reader Orientation

- Make the paper easy to skim through clear titles, abstracts, section structure, paragraph roles, and visible main results.
- Keep definitions and key terms near where readers need them.
- Remind readers of key symbols and parameter names when definitions are distant.
- Repeat claims only when repetition helps orientation.

## Principles For Empirical Analysis

### Structure And Organisation

- State the empirical question and main result before describing all supporting details.
- Organise empirical sections around the chain: data, measurement, identification or model discipline, estimation, results, and interpretation.
- Explain data only to the extent needed for measurement, sample construction, identification, and interpretation.
- Avoid describing the search process behind the preferred specification.
- Put robustness checks and alternative specifications in the appendix unless they materially change the main claim.

### Prose Style

- Interpret empirical claims in economic language before technical defence.
- Distinguish what is measured, estimated, targeted, implied, or validated.
- Avoid overclaiming causality when identification supports only association or model fit.
- Specify the direction and magnitude of associations.
- Put numbers in context; numbers do not speak for themselves.

### Identification, Data, And Estimation

- Explain the source of variation or model discipline behind each central estimate or moment.
- Describe identification in economic terms: what generates variation, what belongs in the error term, and why the key variation is credible.
- Explain why instruments are correlated with the endogenous variable and excluded from the error term.
- Distinguish instruments, controls, fixed effects, targeted moments, implied moments, and validation moments.
- Consider carefully what controls belong in a specification; do not add all determinants mechanically.
- Document standard errors, simulations, moment construction, data transformations, and estimation procedures enough for replication.

### Tables, Figures, Numbers, And Supporting Materials

- Introduce each table or figure before interpreting it.
- State the main takeaway; do not restate every number.
- Discuss every important number in the text or remove it from the main table.
- Keep captions self-contained enough for a skimming reader.
- Report magnitudes in sensible units and with useful precision.
- Distinguish statistical significance, economic magnitude, and model interpretation.
- Guide the reader through tables and figures by describing the pattern, not by saying only that a table reports statistics.
- Tie tables, figures, and numbers back to the research question.

## Principles For Theoretical Model Writing

### Structure And Organisation

- Introduce the model verbally before equations.
- Explain what economic object, mechanism, empirical pattern, or counterfactual the model clarifies.
- Move from infrastructure to superstructure: primitives, agents, states, choices, timing, information, constraints, equilibrium or objective, then implications.
- Explain why each model ingredient is needed for the empirical pattern, estimation, or counterfactual.
- Use only the model needed for the empirical, estimation, or counterfactual purpose; avoid unused generality.
- Prefer the specialised model taken to the data over an abstract model that adds unused generality.
- Explain economic mechanisms before technical defence.

### Prose Style

- State model primitives directly: write "Consumers have power utility", not "I assume that consumers have power utility".
- Use precise technical terms; do not confuse functions with values, vectors with lists or profiles, or assumptions with interpretations.
- Separate formal definitions from economic interpretation.
- Make informal descriptions match formal statements.
- Use "in which" for models and mechanisms.
- Keep mathematical prose readable; do not start sentences with lower-case notation when a verbal construction works.

### Notation, Assumptions, Equations, And Proofs

- Choose notation that is mnemonic, standard when possible, and light enough to read.
- Do not introduce notation used only once or twice.
- Define important notation in the main text, not footnotes.
- Define symbols where readers can find them, and remind readers of names for key parameters when definitions are distant.
- Limited repetition is useful for key parameter names, symbols, and definitions when it keeps readers oriented.
- State definitions in logical order, using only terms already introduced.
- Give examples or intuition for novel definitions, assumptions, or mechanisms, especially boundary cases.
- Name assumptions and conditions by content when that helps readers remember their role.
- Group assumptions by economic object and explain logical relations between stronger and weaker assumptions.
- Make sure the class of objects satisfying assumptions is non-empty; give an example when helpful.
- Make formal statements skimmable through parallel theorem or proposition formats, clear assumptions, and clear conclusions.
- For proofs or derivations, give an informal roadmap before technical details and divide long arguments into meaningful steps.
- Be precise about which assumptions are used for each result; check for unused or redundant assumptions.

### Figures And Supporting Materials

- Use figures to illustrate definitions, mechanisms, model regions, or proof intuition.
- Label figures completely and keep notation consistent with the text.
- Do not let figures substitute for formal logic.
- Move long derivations, algorithm details, and auxiliary cases to supporting material when they are not needed for the main argument.
- Document model solution, simulation, estimation, and moment construction enough that another graduate student could reproduce the result.
