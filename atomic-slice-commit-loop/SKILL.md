---
name: atomic-slice-commit-loop
description: Execute plan-driven implementation as one or more validated, atomic Git commits. Use when landing approved work in small reviewable slices; do not use for planning, read-only review, or requests that explicitly require changes to remain uncommitted.
---

# Atomic Slice Commit Loop

Land an approved implementation plan as a sequence of independently reviewable, validated local commits.

## Commit Policy

- Commit each completed slice by default.
- If the user explicitly requests uncommitted changes, staging only, or review before commit, preserve that requested final state instead.
- If the user switches to uncommitted review after this workflow creates a commit, verify the target commit and intervening history, then undo only that workflow-created commit while retaining its changes. Do not rewrite unrelated history.
- Never push unless the user explicitly requests it.

## Preflight

Before changing files:

1. Resolve the Git root for every target and read the applicable `AGENTS.md` instructions.
2. If `<git-root>/.agents/references/atomic-slice-commit-loop/repo-slice-guidance.md` exists, read it before choosing files, checks, or documentation targets.
3. Record each repository's branch plus staged, unstaged, and untracked state. Preserve all unrelated changes.
4. Derive the next slice's intent, acceptance condition, focused checks, and documentation impact from the approved plan and repository guidance.

## Slice And Validate

1. Select the smallest useful slice with one intent and one acceptance condition.
   - Keep the implementation, tests, and necessary documentation for that intent together.
   - Split work only when every resulting commit is independently useful and passes its own checks.
   - A commit cannot span Git repositories; treat each repository as a separate commit boundary.
2. Implement only the changes required for that intent.
3. Run the focused checks required to demonstrate its acceptance condition, plus any checks required by repository guidance.
   - Repair and rerun failures caused by the slice.
   - For a pre-existing failure, establish the baseline and confirm that focused evidence still demonstrates the slice's acceptance condition.
   - Do not commit with an unresolved slice-caused failure.
   - Stop before widening the slice when resolution requires a new product, design, or scope decision.
4. Synchronize documentation only when accepted behavior, a public interface, usage, validation instructions, or repository guidance changed.
   - Use the repository-designated documentation target; do not assume it is `README.md`.
   - When documentation is unchanged and the reason matters, record why in the handoff.

## Commit And Continue

For each passing slice:

1. Stage only the intended paths or hunks, preserving unrelated staged and unstaged work.
2. Inspect the staged diff and confirm it contains one intent, its tests, and any required documentation.
3. Create a concise, intent-first Conventional Commit.
4. Inspect the committed diff and recheck repository status to confirm unrelated work remains intact.
5. Continue automatically through the remaining approved plan items while their scope and acceptance conditions remain clear. Otherwise stop and report the required decision or blocker.

## Handoff

Group the final summary by repository and report:

- commit hash, message, and intent, or the explicitly requested uncommitted state;
- checks and outcomes;
- documentation updated or intentionally unchanged;
- remaining work or blockers;
- final staged and unstaged state.

Completion requires every authorized plan item to be implemented or explicitly reported as blocked, every committed slice to satisfy its acceptance condition, unrelated worktree state to remain intact, and no push without explicit authorization.
