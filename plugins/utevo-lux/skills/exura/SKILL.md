---
name: exura
description: Address a PR's change requests by reading the full description, issues, reviews and discussions. Fix and test each change in its own commit, update the PR, and reply at the source with the commit and the evidence. Use when the user asks to address review feedback or requested changes.
---

# Exura

Usage: `/exura <PR URL or number> [--local]`.

Invoking the command explicitly asks for the whole cycle: read the requests, fix, verify, make **one commit per change**, push those commits to the PR's branch, and reply in the discussions they came from. `--local` prepares the commits and the replies without pushing or publishing. For requests in natural language, respect the actions that were authorized; this skill being selected automatically does not widen that authorization. Finish the local work and draft the replies before asking for a publishing authorization that is genuinely missing; never ask again for one already granted.

## 1. Read the whole context

Read [the GitHub context protocol](references/github-pr.md) and gather the same material as `look`: description, linked issues and their comments, relevant specs and plans, commits, diff, complete reviews, general comments, inline discussions with every reply, and checks.

- Record the current base and head, the PR's source repository and branch, and the state of the local tree. Confirm the PR is open and that the branch you will change is its own, including when it comes from a fork.
- Read the repository's instructions and the affected files. Read the product documentation and the feature/impact record where they exist; follow the search flow the local instructions describe.
- Do not rely on `reviewDecision` or the latest review alone. Read the bodies of the **`CHANGES_REQUESTED`** reviews, the requests inside `COMMENTED` reviews, the general comments and the threads, taking later replies and decisions into account.
- An old or dismissed review and a resolved thread are history; do not reopen them without evidence that the request still stands. `isOutdated` only means the position went stale: **it does not prove the problem was fixed**.

## 2. Turn the feedback into a queue of changes

A **change** is one logical, verifiable request to alter something. A comment carrying two independent requests produces two changes; several comments about the same cause can point to a single change. Read the replies before deciding what the reviewer meant.

Keep a short queue in the conversation, reconstructible from the PR's comments and commits. Do not create documentation or feature records:

| Origin | Request | State | Commit | Verification | Reply |
|---|---|---|---|---|---|
| URL or ID of the comment, review or item | Expected result | pending / fixed / already met / clarification / disagreement / blocked | SHA once it exists | Proof or limitation | Published URL or draft |

- Confirm each request against the current code. Apply a fix that satisfies the intent and the project's rules, not necessarily the suggested patch literally.
- Already met: identify the proof and the existing commit where you can locate it; do not create an empty commit.
- Disagreement: explain with evidence why the suggestion breaks a contract, contradicts a requirement or does not solve the problem; do not change code merely to silence a comment.
- Ambiguity that changes behavior: ask for clarification in the authorized channel and carry on with the independent changes. Do not answer on the reviewer's behalf or declare the request resolved.
- Distinguish optional suggestions from requirements; implement the ones the user's request covers and do not widen the PR on your own.

## 3. Fix one change at a time

1. Work on the correct head, in a clean checkout or your own worktree. Preserve other people's files and commits; do not stash, reset, rebase or force-push to quietly clear the way.
2. Locate the cause and its consumers before the patch. A fix in a shared function has to cover the affected callers. Follow the dependencies between changes without mixing independent requests.
3. For a bug or non-trivial logic, get a proof that fails before and passes after, preferring the existing harness or test. For a trivial adjustment, use proportionate verification; do not write tests that merely restate the implementation.
4. Make the smallest change that resolves the request and run the relevant checks. UI requires a real browser. Do not create or update documentation; if the review request depends on that, mark the item pending and explain the limitation.
5. Inspect the diff and the staging area. Make **one commit for this change**, including the implementation and any tests it needs. Do not include independent changes or work that was already in the workspace. Every commit must be coherent and verifiable.
6. Follow the repository's convention, with the feature ID where it applies. In the commit body, include `Review: <origin URL>` (every origin, if there are duplicates) and the verification you ran. Record the real SHA in the queue.

One comment carrying several requests can receive several commit links. A request that needs several files changed is still one change. Do not use amend or squash to merge distinct changes. If a change is blocked, record why and move on to the independent ones.

## 4. Update the PR and reply

- Run the final checks over the whole set of commits and the impact list. Fix failures your work caused before announcing success; pre-existing or external failures need evidence and must appear in the result.
- Before pushing, re-read the remote head. If it moved, preserve the new commits, reconcile without rewriting anyone else's history, and revalidate what changed; never overwrite the head you observed earlier. Push only the expected commits to the PR's source branch, with a normal push.
- Confirm the PR contains the commits you pushed. **Only then** reply in each discussion with the commit link and the concrete result of the verification. If the push fails, or you are in `--local`, keep the drafts; do not publish "fixed" pointing at a commit the reviewer cannot reach.
- Reply to inline comments in the original thread. Requests in a review body or a general comment get a reply on the PR with a direct link to the origin and the item addressed; do not open an artificial inline discussion.
- For duplicates, reply at each origin pointing to the same commit. For "already met", a disagreement or a clarification, reply according to the evidence, without simulating a fix.
- **Leave the thread open for the reviewer to check**, unless resolving it was explicitly requested. Do not dismiss reviews, approve your own work, or merge.

A short reply format, adapted to the language of the discussion:

```markdown
Fixed in [<short SHA>](<commit URL>): <what changed and how it meets the request>.
Verification: <command or scenario and the real result>.
Not covered: <what the check does not prove, when that matters>.
```

Before repeating any publication, check the thread and the queue: a resumed run or a timeout must not duplicate a reply or a commit. Use [the shared protocol](references/github-pr.md) to tell review, comment and thread IDs apart and to check what the API returned.

## 5. Close the round

Re-read the state of the PR, the discussions and the checks to identify changes still open, new requests, and interference from someone else. Fixed in the code, answered on GitHub, and accepted by the reviewer are three different states.

Deliver the mapping **request -> commit -> verification -> reply**, including items already met, disagreements, blocks, new requests and pending checks. Do not announce "all resolved" while items remain untouched, a publication is missing, or a necessary verification is inconclusive.
