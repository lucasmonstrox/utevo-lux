---
name: mission
description: Investigate a software problem through code and Git history, external research and evidence verification. Use to discover what exists, assess feasibility or compare approaches before planning.
---

# Mission

Usage: `/mission <topic or question>`, or the agent's native skill invocation.

Investigate to answer the request. Deliver research **in the conversation**; do not create or update documentation, wishlists, feature records or product code.

## 1. Scope the investigation

Read local instructions and relevant product documentation where available. Reuse the `hi` brief if present; preserve decisions, constraints and open questions. Otherwise, extract these from the request. Another skill is not a prerequisite.

Classify the effort and state the scope:

| Scope | Proportionate work |
|---|---|
| Lookup | One verifiable fact with sufficient evidence. |
| Comparison | Concrete options assessed against the same criteria. |
| Broad topic | Investigation tracks that could change the recommendation. |

Keep a short brief: central question, scope, constraints and what counts as answered. Ask one question at a time about ambiguity that changes the direction; verify discoverable facts yourself.

Set a proportionate research budget. Delegate only independent tracks when tools and authorization permit, with clear objectives, boundaries and evidence requirements. Do not require a specific provider, model or agent count.

## 2. Investigate the repository

- Inspect code, tests, schemas, migrations, dependencies and relevant history. Read existing investigations and decisions before repeating work.
- Use available conceptual search/LSP tools; otherwise narrow with `rg`, file search and targeted reads. Confirm dynamic references, aliases and strings.
- Distinguish working behavior, partial implementations/mocks and documentation-only claims. A signature does not prove complete behavior.
- Trace consumers and effects of shared contracts. Confirm data models in the actual schema; do not infer columns from the UI.
- Use `git log -- <paths>`, `git log --follow -- <file>` and `git log -S <term> -- <paths>` when history explains a decision.

Internal findings cite files/lines read in this session; cite a commit hash when history supports the conclusion. Data findings include the query and context without exposing secrets or unnecessary personal information.

An empty search does not prove absence. Try other terms, layers or representations. Revisit a refuted hypothesis only with new evidence.

## 3. Research external facts when needed

Search when the answer depends on current APIs, libraries, markets, rules or external facts. An entirely internal lookup does not need market research.

- Derive searches from open questions and affected actors.
- Start broadly and narrow; change terms, language or source type when needed.
- Prefer official documentation, source code, changelogs, issues and primary research. Secondary sources can help locate or supplement evidence.
- Read the actual page before relying on a decisive claim. Snippets and model memory are not proof.
- Check compatibility, maintenance, licensing, limits and costs where they matter.
- Distinguish inspiration from requirements: a competitor having something does not establish that this project needs it.

Keep a compact record in the conversation or working notes: answered, still unverified, next search. Stop when new results no longer change the decision or the research budget ends; state the gaps.

## 4. Verify and try to disprove

Classify decisive claims as verified, refuted, inferred or inconclusive. Cite sources and access dates for facts that age.

Check material numbers and claims against independent sources where possible. Several articles repeating one announcement are still one origin. Explain disagreements between sources.

Try to show why the recommendation could fail: an adverse scenario, hidden cost, incompatibility or simpler alternative. Independent review can help when available and authorized; do not invent problems to fill quotas.

If evidence invalidates the brief's direction, explain the conflict and revisit the decision with the user. Do not silently replace their intent.

## 5. Deliver in the conversation

For a simple lookup: answer, source and limitation. For a broader investigation:

- recommendation and confidence;
- what already exists, with evidence;
- options and material differences;
- gaps, risks and refuted hypotheses;
- decisive sources near the claims they support;
- questions that still prevent a decision.

Do not write a full implementation plan here. With a supported direction, suggest `equip`; if unavailable, supply enough context to continue. Do not create report files or invoke the next stage automatically.
