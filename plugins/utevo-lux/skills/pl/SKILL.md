---
name: pl
description: Turn a defined direction into an implementation plan with steps, dependencies, acceptance criteria and executable checks. Deliver it in the conversation without implementing or creating documentation.
---

# Pl

Usage: `/pl <task, brief or investigation>`, or the agent's native skill invocation.

Plan the work that `hunt` will execute. Deliver the plan **in the conversation**. Do not create documents, plan directories, feature records or code.

## 1. Recover intent and current state

Read local instructions, the request and available briefs/investigations. Consult existing documentation and code to verify assumptions.

- Preserve decisions, constraints, rejected options and established criteria.
- Check what is implemented. Plan only the missing work.
- Clarify material open product decisions one at a time, or recommend `exiva` for investigation. Do not hide unresolved research inside implementation steps.
- Ask for indispensable missing context. No other skill needs to be installed.

## 2. Map dependencies and impact

Use available conceptual search/LSP tools, or `rg` and targeted reads. Read actual contracts, schemas and dependencies. Examine history when it explains the area.

Identify files/symbols to change, consumers, dynamic references, prerequisites, surfaces that could regress and existing verification commands.

Code evidence uses file/line references and a hash when needed. Execution instructions prefer file/symbol references because lines move. Do not invent paths, commands, tables or services.

## 3. Write executable steps

Use [the plan format](templates/plan.md) as a guide. Scale detail to the task; trivial work does not need extensive architectural analysis.

Each step states intent, observable result, files/symbols, actual dependencies, local constraints and proof (command/action → expected result).

Do not prewrite the implementation. Include snippets only when their exact shape is a necessary contract.

- Prefer a first integrated slice that exposes risks early.
- Separate independent changes. Split steps that are too large to verify.
- Put important rules next to the step that needs them without reproducing the entire manual.
- State what to preserve, what to avoid and what is excluded.
- For data changes, distinguish expansion, migration and removal, with proof before each transition.
- Do not invent stubs to conceal dependencies. If stubs are part of the design, explain their contract, replacement and what they enable testing.

## 4. Plan verification

Proof must exercise the changed surface:

- UI: a real browser, relevant errors, variants, the main flow, console and network.
- API: actual requests/handlers and effects; wait for asynchronous effects where applicable.
- Data: schemas and queries demonstrating integrity, transformation and compatibility.
- Logic: a test that distinguishes correct from incorrect behavior using existing infrastructure.
- AI: cases that assess output contracts and behavior, beyond whether the model responded.

Typechecking and linting complement these proofs. A test without infrastructure cannot appear as a ready-to-run command: plan the necessary setup or state the limitation.

Include affected consumer regressions and the complete main flow. Name the behavior to test; avoid "add tests" without a concrete case.

## 5. Deliver the plan

Present the objective, acceptance criteria, steps, risks, checks and open items in the conversation. Identify execution blockers before suggesting `hunt`.

For operational risk, explain rollback and irreversible effects. Do not force this section onto trivial edits.

Could another agent execute without inventing decisions? Include any missing context in the message. Do not create documentation or status files.

In another session, the user supplies the plan or corresponding context. Do not assume access to earlier conversations or create persistence on your own.
