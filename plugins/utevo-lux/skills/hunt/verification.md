# Verification by surface

Use the project's actual infrastructure. Do not assume another repository's language, framework, database, ports or commands.

| Surface | Evidence |
|---|---|
| UI | Interaction in a real browser, visible result, console and relevant requests. |
| API | Actual route/handler, response and effect. Wait for an observable condition for asynchronous work. |
| Data | Schema, queries and integrity before/after. Use test data and restore state created by the test. |
| Logic | A test that distinguishes incorrect from correct behavior. |
| AI | Output and action assessed against product criteria. Running without errors does not prove a correct answer. |

Typechecking, linting and builds complement these proofs. Discover commands in the project.

Cover relevant errors and variants, then finish with the main flow. Do not create an exhaustive matrix for a small edit.

Use available browser automation. With `agent-browser`: open → interactive snapshot → act → observe the result → check console/network. Refresh the snapshot when references expire. Close only the session created for the test. Use DevTools for races and complex requests when available. Without a browser, mark UI verification as pending.

Compare the full diff with the request and plan: omissions, scope expansion and regressions. Another agent can review when available and authorized.

Report results in the conversation. An unexecuted check is a limitation, not approval. Do not save documentation reports.
