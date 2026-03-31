---
name: atomic-slice-commit-loop
description: 'Use for plan-driven implementation slices that need focused checks, readme.md sync, and atomic conventional commits. Load repo slice guidance for local paths and escalation rules when available.'
argument-hint: 'Provide plan item, target files, and expected slice outcome.'
user-invocable: true
---

# Atomic Slice Commit Loop

## What This Skill Produces

A sequence of small, independently understandable implementation commits, each with focused checks and synchronized documentation.

## When to Use

- Implementing tasks from `plan/`.
- Refactoring active code without mixing unrelated changes.
- Maintaining continuous `readme.md` alignment.

## Required Inputs

- Selected plan item and acceptance target.
- Candidate files for the smallest useful slice.
- Required checks for the slice.

## Procedure

1. Select one smallest useful slice.
   - Define one intent and one acceptance condition.
   - Limit touched files to what is necessary.
   - If `.agents/references/atomic-slice-commit-loop/repo-slice-guidance.md` exists in the current repo, read it before selecting files or checks.
2. Implement minimal changes.
   - Preserve behavior unless the slice explicitly changes behavior.
   - Keep code deterministic and reproducible.
3. Run focused checks.
   - Execute tests or analysis checks relevant to this slice only.
   - Follow any repo-specific escalation or validation rules from repo guidance when present.
4. Sync documentation.
   - Update `readme.md` with what changed and how to run or validate it.
   - Update any additional repo-specific doc targets from repo guidance when relevant.
5. Commit atomically.
   - Use Conventional Commits with clear scope.
   - Ensure the commit is independently understandable and reversible.
6. Summarize and continue.
   - Record outcome, risks, and the next smallest slice.
   - Repeat loop.

## Decision Branches

- If repo guidance points this work to an experiment or validation workflow, switch before widening the slice.
- If validation fails, stop and report the cause before continuing.

## Output Format

1. Slice goal.
2. Files changed.
3. Checks and outcome.
4. `readme.md` updates.
5. Commit hash and message.
6. Next slice.

## Completion Checks

- One commit equals one intent.
- Checks are relevant and passed, or failed with a clear reason.
- `readme.md` reflects the accepted change.
