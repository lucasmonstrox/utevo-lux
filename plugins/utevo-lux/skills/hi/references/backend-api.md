# Backend and API

Read this reference for endpoints, services, integrations, webhooks, jobs, events or contracts between systems.

## Actors and scenarios

Consider API clients, calling services, external integrations, operators, support, maintainers and hostile actors. Model the full lifecycle where material:

- valid request and observable result;
- invalid input and useful error;
- valid identity with insufficient authorization;
- duplicates, retries and idempotency;
- concurrency and event ordering;
- timeouts, external outages and partial failures;
- large volumes, pagination/filters and limits;
- client compatibility as the system evolves;
- operations, reconciliation and auditing.

## Contract decisions

Explore alternatives only where they change guarantees or consumers:

- synchronous, asynchronous or hybrid;
- resource, command, event or webhook;
- unit of atomicity and perceived consistency;
- input/output shape and semantics of absence, `null`, defaults and errors;
- error taxonomy, retryability and idempotency keys;
- pagination, ordering, filters and cursor stability;
- versioning, compatibility and deprecation;
- ownership, authentication, authorization and tenant scope;
- observability and reconciliation of external effects.

Sketch two or three comparable behavioral contracts when that makes a decision concrete. Introduce one hypothesis at a time and compare finalists in a later step; use the same scenarios for all and keep sketches separate from final code.

## Validation, queries and performance

- Define which invariants are validated at the boundary and which belong to the domain or storage.
- Give each error a consumer and a possible next action; a generic 400 rarely completes the scenario.
- Derive queries from actual access patterns: cardinality, filters, ordering, consistency and frequency. Do not prescribe indexes or caches without a workload.
- Replace "fast" with a budget or order of magnitude when performance could determine the option: latency, throughput, payload, fan-out, volume and cost.
- Treat caching, batching, queues and denormalization as options with invalidation, delay and operational costs.

## Constraints to investigate, not copy

Look for duplicate effects on retries, authorization enforced only in the UI, trust in external payloads, errors that leak secrets, silent breaking changes, untraceable operations and unbounded queries. Record only what is plausible for this task.

## Leave for implementation planning

Paths, function names, framework details, final SQL, tests and implementation order belong to `/pl`. `hi` establishes the guarantees those mechanisms must satisfy.
