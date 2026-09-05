---
name: hunt
description: Execute an implementation plan through verifiable steps, respect dependencies and demonstrate results in the actual workflow. Use to execute a plan or implement a defined task.
---

# Hunt

Usage: `/hunt <plan or defined task>`, or the agent's native skill invocation.

Execute the plan from the conversation or identified by the user. Do not create or update documentation, wishlists, plan files or feature records. Keep progress and results in the conversation.

## 1. Confirm the starting point

Read local instructions and relevant existing documentation. Check `git status --short`, recent history and the affected code. Preserve others' changes and commits.

- Already implemented and proven: report the evidence.
- Partial: execute only what is missing after checking the actual state.
- Plan available: read the objective, acceptance criteria, dependencies, steps and checks.
- No plan: trivial, unambiguous work can proceed directly. Broad work or open decisions need planning before code.
- Missing plan from another session: ask for its contents; do not pretend to know it.

Compare assumptions with the current repository. If one no longer holds, pause the affected step, explain the discrepancy and adjust the plan in the conversation before continuing.

## 2. Execute in dependency order

- Keep progress in the conversation. Update each step when its proof passes.
- Execute steps whose prerequisites are met; an open item blocks its dependents, not necessarily all work.
- Before editing, find the source and consumers of the behavior. Use available search/LSP tools, or `rg` and targeted reads.
- Reuse patterns and infrastructure. Make the smallest change satisfying the plan in integrated, verifiable slices.
- Reread each step's constraints before implementing. Do not import rules from another stack or introduce speculative abstractions.
- For data migrations, prove the transition before removing the old format.

Use the project's actual commands and versions. New tests verify behavior; trivial edits do not need artificial test suites.

## 3. Handle failures

When a test or analysis fails, record the exact error, locate the defect and fix its cause. Do not make random changes until checks turn green.

Two attempts with the same hypothesis and no progress call for reassessment: new evidence, a smaller reproduction or an explained blocker. Continue independent steps. Distinguish infrastructure failures from patch regressions.

Do not stash, reset, rebase, force-push or clear user data to simplify execution. Experiments with another Git state use an isolated checkout/worktree.

## 4. Verify

Read [the verification matrix](verification.md). Each plan criterion needs proof or an explicit limitation.

- Exercise the actual flow and run relevant checks.
- Retest affected consumers.
- Review the diff against the request and acceptance criteria. Use independent review when available and authorized; do not claim another reviewer when you reviewed it yourself.
- Unresolved failures remain open. Passing typechecks does not substitute for behavioral proof.

## 5. Deliver

Report changes, checks, results and open items in the conversation, with useful paths and evidence.

Respect session authorization for commits and remote actions. Implementation alone does not authorize publishing a PR, pushing, deploying or merging. When commits are authorized, include only this task's work and follow repository conventions.
