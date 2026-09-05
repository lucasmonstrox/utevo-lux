# Quality attributes

Read this reference when a nonfunctional attribute could eliminate an option or change the product. Do not turn every discussion into a universal requirements checklist.

## Method

For each material attribute, define:

1. the scenario and affected audience;
2. an observable condition or budget;
3. the consequence of failure;
4. how to compare options;
5. the accepted cost/trade-off;
6. how we will later know it worked.

## Possible perspectives

- **Performance:** perceived and backend latency, throughput, payload, volume/cardinality, frequency, peaks, cost and degradation. Use a range or order of magnitude when an exact number still requires `/exiva`.
- **Reliability:** required availability, consistency, tolerable loss, retry/idempotency, recovery, RPO/RTO when applicable and degraded behavior.
- **Accessibility:** critical tasks without a mouse, sight, color or audio; focus order, semantics, zoom, contrast and assistive technology. Include accessibility when choosing the interaction.
- **Privacy:** purpose, minimization, visibility, retention, deletion, export, consent and sensitive inferences.
- **Observability:** which operational question needs an answer, by whom, using which logs/metrics/traces/events, without leaking data.
- **Maintainability:** ownership, frequency of change, compatibility, diagnosability, configuration surface and evolution cost.

Vague terms do not settle a decision. "Fast," "resilient," "accessible" and "easy to maintain" need a scenario and observable evidence; `/pl` later defines executable proof that fits the repository.
