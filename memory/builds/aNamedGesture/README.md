---
slug: aNamedGesture
node: a
opened: 2026-08-25
streams: tooling
roster: TOOL
ids: TOOL-aNamedGesture-1 TOOL-aNamedGesture-2 TOOL-aNamedGesture-3
---

# aNamedGesture — the authorizing parameter gets a name, and the name carries the build

## The problem this build exists to solve
The unattended kit's prompt path opens with `Only when the invocation carries the authorizing
parameter`, and no file in this repository says what that parameter is. Its own spec listed naming it
as scope item S2 and the render shipped without it. So the one gesture that separates prose from a
run that will merge and push with no owner turn is a phrase, not a token: an agent cannot test for
it, an owner cannot type it, and two sessions can disagree about whether it was present. The gap is
worse than a missing default, because the Skill affirmatively tells the reader that this parameter IS
the authorization and then declines to name it.

## Expected improvements
- The gesture becomes a literal an agent tests the invocation for, instead of prose it interprets.
- The scope stops sitting BESIDE the parameter and becomes its argument, so one token carries both.
- An owner can hand over a prompt file instead of pasting a build's worth of prose into a chat line.
- `aPromptedMandate-5` item S2 stops being a scope item the render does not satisfy.

## Detriments if this is not built
- Every prompt-mode start is authorized by an agent's reading of prose, which is the inference the
  path's own non-goal forbids.
- Two agents can reach opposite verdicts on the same invocation, and neither is wrong on the text.
- The kit ships a Skill whose central precondition names nothing, so no adopter can audit it.

## Build-level rules
- **The token names the MODE it starts.** `--prompt` renders the `authorized-by: prompt` value it
  produces, so the gesture and the record it writes are one word. Owner ruling, 2026-08-25.
- **One PRODUCTION home for the literal.** `--prompt` is derived once, in `adopt-unattended.sh`. Both
  shipped confs declare the key BLANK, already this file's idiom for kit-owned, and the rendered Skill
  is where a reader learns the value. Two test fixtures also spell it, as the EXPECTED value of
  assertions, which is what makes the default falsifiable rather than a second source of it.
- **The value is carried by CONTENT into a `prompts/` RECORD, never by reference.** A file path is
  resolved and its bytes are written under the build's own `prompts/`, where this memory tree already
  sanctions prompt-kind files, with the source path recorded beside them. Not into this README: its
  heading canon is closed and its marker matcher reads column 1 blind to fencing, so a prompt quoting
  a generated-region marker would be refused after the push.
- **No new `fail` call site.** A new one costs an arm in `unarmed-branches.txt` and an `ARMS_FLOORS`
  bump, and buys nothing: the render's surviving-placeholder arm already catches the only
  machine-visible failure this key has.
- **Nothing verifies the gesture, and the spec says so.** No script in this kit sees the invocation.
  The parameter is the authorization GESTURE; the anchor is still the pushed build folder.

## Parked decisions
- **`--full` was the opening default and was replaced at kickoff.** It named a degree rather than a
  grant, so no value of it was obviously wrong, and `GATE_FULL` already means something else in this
  tree. Owner picked `--prompt` instead, 2026-08-25.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aNamedGesture-1` | 2 | the authorizing parameter is a declared conf key taking a path-or-prose value, rendered into the Skill, defaulting to `--prompt` |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-08-25 · streams tooling
ids TOOL-aNamedGesture-1 TOOL-aNamedGesture-2 TOOL-aNamedGesture-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aNamedGesture-1 — the authorizing parameter is a declared conf key that carries the build](spec/2026-08-25-spec-TOOL-aNamedGesture-1.md) | 1 | 2 | CLOSED | rev-5 | 2026-08-25 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aNamedGesture-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
