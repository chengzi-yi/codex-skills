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
