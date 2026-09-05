# Infrastructure, configuration and tooling

Read this reference for deployment, runtime, networking, observability, linting, formatting, builds, CI, internal automation and developer experience.

## The audience can be internal

Map developers, reviewers, CI, operators, support, security, dependent services and the person on call. Identify who benefits, who pays the cost and who maintains the solution.

For a new lint rule or configuration, the transformation may be providing feedback or preventing an error class that currently goes undetected. Do not invent an existing feature.

## Useful scenarios

- local execution, CI, preview/staging and production;
- first setup and repeated use;
- success, warnings, true errors and false positives;
- partial failures, retries, timeouts and recovery;
- gradual rollout, rollback and compatibility across versions;
- missing/rotated credentials and insufficient permissions;
- diagnosis by someone unfamiliar with the implementation;
- legitimate exceptions, auditable bypasses and exception expiry;
- cost, quotas, saturation and vendor dependence.

## Options and criteria

Compare prevention versus detection, local versus CI enforcement, errors versus warnings, automation versus manual steps, managed versus self-hosted services, synchronous execution versus queues/workflows, and central versus per-workspace configuration when these dimensions matter.

Judge feedback time, determinism, false positives/negatives, affected consumers, operability, rollback, total cost, lock-in and ownership. Stricter rules lose value if the team learns to ignore the signal.

## Constraints to investigate

Look for silent bypasses, rules that work on only one machine, secrets in configuration/logs, deployments without rollback, alerts without owners, non-idempotent automation and failures that disproportionately block the workspace. Record only plausible risks and describe the desired behavior.

## Leave for research and implementation planning

Exact files, final commands, provider APIs, literal configuration, rollout sequences and executable proofs belong to `/exiva` and `/pl`. `hi` decides policies, audiences and operational guarantees.
