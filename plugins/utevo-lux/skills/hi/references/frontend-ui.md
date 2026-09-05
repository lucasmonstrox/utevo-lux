# UI and frontend

Read this reference when the task changes a screen, navigation, form, visualization or interaction. Use only branches that affect the decision.

## What to explore

- **Audience and context:** role, frequency, knowledge, device, environment, urgency and authority. Distinguish the operator from the beneficiary.
- **Job and entry point:** what triggered the visit, what information is already available, what the person wants to decide/do and where they need to go next.
- **Hierarchy:** primary, secondary and progressively revealed information; density; navigation; relationships with adjacent flows.
- **Real states:** initial, loading, empty, partial, error, unauthorized, conflict, success, repetition and recovery/undo when material.
- **Interaction and feedback:** primary action, dangerous actions, error prevention, confirmation, perceived latency, editing, keyboard, mobile and continuity across sessions.
- **Accessibility and language:** focus order, assistive technology, contrast, target sizes, nonvisual alternatives and copy that explains consequences instead of internal jargon.
- **Trust:** data source and freshness, automation versus human action, reversibility and explanations for system decisions.

## UI precedents

Start with the design system and comparable internal flows, then look at competitors and analogous products. Compare entire flows and states, beyond the successful screenshot. Record the precedent's assumptions about audience, data volume and platform.

## Exploration through mockups

When at least two plausible structures exist and the choice is material, produce **three to five structurally distinct mockups** before settling on an option. Do not manufacture five variants for a trivial change.

First fix a shared mini-brief: the same audience, scenario, content/data, platform and constraints. Vary navigation, hierarchy, density, disclosure or interaction hypotheses, beyond colors, borders or button positions.

For each mockup, state:

- the hypothesis it tests;
- the scenario where it works best and where it fails;
- cognitive and operational cost;
- constraints it respects or puts under pressure.

Present them progressively: **one visual hypothesis and one question per message**. Compare finalists after the user understands the directions; do not dump five mockups with five analyses. Use an available visual tool, or low-fidelity wireframes if none is available. Mockups are disposable decision aids and do not authorize production code. After the choice, preserve the direction and reason; do not turn every variation into a requirement.

## Leave for implementation planning

Do not turn the discussion into choosing components, files, hooks, state managers or CSS classes unless that changes an already identified visible constraint. These mechanisms belong to `/pl`.
