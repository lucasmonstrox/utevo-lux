# Security and abuse

Read this reference for identity, authorization, sensitive data, money, public endpoints, webhooks, uploads, secrets, external integrations, privileged actions or plausible harm.

The purpose in `hi` is to give the direction an abuse model and security invariants. Deep regulatory or technical research belongs to `/exiva`.

## Minimum model

1. **Assets:** what needs protection: data, money, availability, reputation, privileged actions or secrets.
2. **Actors:** legitimate users, roles with different privileges, external services, insiders, bots and attackers.
3. **Trust boundaries:** where identity, tenant, payload or origin can no longer be trusted.
4. **Abuse paths:** how the capability could be used, repeated, forged, enumerated, escalated or combined to cause harm.
5. **Impact and failure stance:** what happens when information is missing, a dependency fails or authorization is ambiguous; consciously choose between failing closed and degraded continuity.

## Select relevant scenarios

Explore only applicable cases: cross-tenant access, privilege escalation, replay/retry, enumeration, brute force/rate abuse, tampered payloads, SSRF/uploads, exfiltration through logs/errors, exposed secrets, manipulated automation, fraud, improper deletion and missing audit trails.

## Invariants and trade-offs

State observable boundaries: who can do what, on which resource, under which proof, and which events must be audited. Distinguish authentication, authorization and origin validation. Connect least privilege, consent/purpose, retention and redaction to real assets.

Security has friction, availability, cost and support trade-offs. Do not hide an accepted trade-off behind "secure enough"; record the tolerated threat, reason, mitigation and trigger for revisiting it.

Avoid generic constraints such as "do not expose data." Prefer a contextual example such as `accept tenant_id from the payload → derive the tenant from the authenticated identity`, only if that is the actual agreed contract.
