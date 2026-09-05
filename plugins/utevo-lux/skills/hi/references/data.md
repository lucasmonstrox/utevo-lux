# Data, schemas and queries

Read this reference when a direction creates, changes, derives, migrates or retains persistent state.

## Data meaning

Before discussing tables or columns, clarify:

- which domain fact is represented and who owns it;
- source of truth versus projection, cache, snapshot or event;
- identity, tenant scope and relationships;
- valid states, transitions, time semantics and required history;
- missing versus unknown versus not applicable;
- authorship, provenance, auditability and explainability;
- sensitivity, purpose, retention, export and deletion;
- who reads, who writes and with what consistency.

## Scenarios that expose the model

Include creation, correction, duplication, concurrency, stale reads, backfills, deletion, restoration, import, reprocessing and schema evolution only when plausible. For derived state, ask how divergence from the source can be detected and repaired.

## Modeling options

Compare models by the invariants and access patterns they must support. Relevant dimensions include normalized data versus snapshots, events versus current state, references versus historical copies, computation on read versus materialization, and structured fields versus extensible payloads.

For each option, make explicit:

- what it can guarantee;
- main queries and expected volume/cardinality;
- write, read and operational costs;
- compatibility and evolution path;
- behavior during migration and rollback;
- information lost or made ambiguous.

Settle semantics and guarantees in the discussion. Exact indexes, constraints, expand/backfill/contract migrations and queries belong to `/exiva` and `/equip`, guided by the access patterns decided here.

## Derive concrete constraints

Determine whether losing authorship/history, mixing tenants, overwriting the source of truth, allowing invalid states, deleting audit data or retaining data without a purpose would be unacceptable. Do not record these automatically; connect each to a real scenario and impact.
