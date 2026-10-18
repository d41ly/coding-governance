# Brief — aScoutedSeam: the measured prompt principles, generalized and handed to the session building a multi-step development flow

**Serves:** research TOOL-aScoutedSeam-3

## The prompt

> another session is currently building out a development flow of 5 steps and several agent roles to work through the flow. Seems like these discoveries can be applied to all the workflows and prompts in this rebuild. Can you package it as a handoff for another session to orient in and understand how to systemically apply these principles to its own work?

## The brief

### Goal
State the build's measured findings as general principles for any agent step. Give them a procedure
for applying them to a multi-step flow, and hand them to another session through a `gov-session`
handoff that it can orient from with no access to this conversation.

### Items
1. **A principles record** in this build's `build/` folder. Each principle is marked MEASURED or
   TRANSFER and cites the record that measured it. The record also holds a prompt skeleton, a procedure
   for applying the principles to a flow (calls, classification, listers, edge rows, ranking), the
   measurement method, the anti-patterns met, and the limits.
2. **A `gov-session` handoff** under `prompts/`. It names a reading order and the records the receiving
   session produces in its own build, and it marks transfer to other task kinds as a hypothesis to
   measure.

### Acceptance
Both are committed. The handoff names only repository paths, and memory hygiene, spec tokens and the
build-index checks pass.

### Gates
memory hygiene · spec tokens · build README slot contract

### Non-goals
- No edit to the receiving session's build or files.
- No product code, and no change to any spec.

## Owner confirmation

Asked: nothing; the request names its deliverable. Whether to land it on main so another node can read it
is asked separately.
