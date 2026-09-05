---
name: mission
description: Investigate a software problem through code and Git history, external research and evidence verification. Use to discover what exists, assess feasibility or compare approaches before planning.
---

# Mission

Usage: `/mission <topic or question>`, or the agent's native skill invocation.

Investigate to answer the request. Deliver research **in the conversation**; do not create or update documentation, wishlists, feature records or product code.

## 1. Scope the investigation

Read local instructions and relevant product documentation where available. Reuse the `hi` brief if present; preserve decisions, constraints and open questions. Otherwise, extract these from the request. Another skill is not a prerequisite.

Before the first tool call, write one line: what would settle this question, and what would count as enough evidence. Sometimes that is a single page, opened. Sometimes it is the same criteria applied to options that already have names. Sometimes the options are not known yet and finding them is the work.

Then spend to that line. The cheapest path that settles the question is the right one — spending more is not the same as answering better, and an investigation that outgrows its question is a cost, not a virtue. Keep a short brief alongside it: central question, constraints and what remains open. Ask one question at a time about ambiguity that changes the direction; verify discoverable facts yourself.

Delegate a track only when it is genuinely independent — separate question, separate sources, nothing to hand back mid-way. Work that shares context or depends on another track in flight belongs in one place. When delegating, give each track its objective, its boundaries and what evidence it must return. Do not require a specific provider, model or agent count.

## 2. Investigate the repository

- Inspect code, tests, schemas, migrations, dependencies and relevant history. Read existing investigations and decisions before repeating work.
- Search lexically and semantically; neither subsumes the other. Exact match is the stronger tool for identifiers, strings and dynamic references, and it is the one that still works after a rename. Conceptual search and LSP tools find what you could not name. Confirm anything decisive with a direct read.
- Distinguish working behavior, partial implementations/mocks and documentation-only claims. A signature does not prove complete behavior, and a passing test does not prove the behavior the test claims to cover.
- Trace consumers and effects of shared contracts. Confirm data models in the actual schema; do not infer columns from the UI.
- Use `git log -- <paths>`, `git log --follow -- <file>` and `git log -S <term> -- <paths>` when history explains a decision.

Internal findings cite files/lines read in this session; cite a commit hash when history supports the conclusion. Data findings include the query and context without exposing secrets or unnecessary personal information.

**An empty search does not prove absence.** It usually means the search was wrong, not that the thing is missing. After two failed formulations, change the strategy rather than the words: another layer, another representation, the consumer instead of the definition, history instead of the working tree. Report "not found" as a limitation, with what was searched. Revisit a refuted hypothesis only with new evidence.

## 3. Research external facts when needed

Search when the answer depends on current APIs, libraries, markets, rules or external facts. An entirely internal lookup does not need market research, and a stable, well-known fact does not need a citation hunt.

- Derive searches from open questions and affected actors.
- Start broadly and narrow; change terms, language or source type when needed.
- Prefer official documentation, source code, changelogs, issues and primary research. Secondary sources can help locate or supplement evidence.
- Read the actual page before relying on a decisive claim. Snippets and model memory are not proof.
- Check compatibility, maintenance, licensing, limits and costs where they matter.
- Distinguish inspiration from requirements: a competitor having something does not establish that this project needs it.

Keep a compact record in the conversation or working notes: answered, still unverified, next search. Stop when new results no longer change the decision or the research budget ends; state the gaps.

## 4. Verify and try to disprove

Label decisive claims as verified, refuted, inferred or inconclusive, and put the check next to the label so a reader can run it: the file and line, the commit, the query, the URL that was opened. The label is a pointer to evidence, not a substitute for it — a claim marked verified that nobody can re-check is still just an assertion.

Cite sources and access dates for facts that age. Check material numbers against independent sources; several articles repeating one announcement are still one origin. Explain disagreements between sources rather than picking the convenient one.

Then attack the recommendation, and do it from outside the work that produced it. Re-reading your own conclusion tends to confirm it. Prefer a check that has an independent source of truth: run the thing, query the data, open the competing document, or delegate the attack to a track that never saw the draft and has to find its own evidence. Look for the adverse scenario, the hidden cost, the incompatibility, the simpler alternative. Do not invent problems to fill quotas.

If evidence invalidates the brief's direction, explain the conflict and revisit the decision with the user. Do not silently replace their intent.

## 5. Deliver in the conversation

When one fact was the whole question: the answer, its source and its limitation. For a broader investigation:

- recommendation and confidence;
- what already exists, with evidence;
- options and material differences;
- gaps, risks and refuted hypotheses;
- decisive sources near the claims they support;
- questions that still prevent a decision.

Do not write a full implementation plan here. With a supported direction, suggest `equip`; if unavailable, supply enough context to continue. Do not create report files or invoke the next stage automatically.
