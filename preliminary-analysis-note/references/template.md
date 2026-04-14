# Template

```md
---
created: YYYY-MM-DDTHH:MM:SS+ZZZZ
commit: abc1234
tags:
  - preliminary-analysis
  - <topic>
---

# <Title>

<One-line context>

## Runs

- <run 1>
- <run 2>

## At a glance

- <finding 1>
- <finding 2>
- <finding 3>

## Results

| Run | Key metric 1 | Key metric 2 | Comment |
| --- | ---: | ---: | --- |
| ... | ... | ... | ... |

## Interpretation

- <condensed interpretation 1>
- <condensed interpretation 2>
- <condensed interpretation 3>
- Define any metric, variable, or flag shown in `Results` that a reader would not understand from context alone.
- If a table column uses abbreviated names, spell them out here before interpreting the comparison.

## Source outputs

- `<path 1>`
- `<path 2>`
```

# Usage Notes

- Filename pattern: `<scope>_<topic>_<YYYY-MM-DD>.md`
- Use lowercase snake_case for `<scope>` and `<topic>`.
- Use a table only when it improves comparison; otherwise use short bullets.
- Add case-specific sections only when they carry important information.
- If the note becomes long, cut prose before cutting findings.
- When the comparison is preliminary, make caveats explicit and brief.
- Do not assume the reader knows what reported metrics mean; use `Interpretation` to define them when they appear in `Results`.
