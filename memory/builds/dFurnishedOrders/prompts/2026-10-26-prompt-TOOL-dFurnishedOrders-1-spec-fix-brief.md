**Serves:** research TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15

# Spec fix brief — dFurnishedOrders, what the spec stage's checks found before the spec commit

## The prompt

Fix the spec stage's findings listed in the brief below, in the dFurnishedOrders specs they name.

## The brief

### Goal

Fix every finding below in the spec it names, and nothing else, so the 20 specs the five writers of
`unattended-build.js` run `wf_681d731e-31c` authored (their returns:
`memory/builds/dFurnishedOrders/build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md`) pass
`tools/check-spec-tokens.py` and the memory-hygiene gate's checks 12 and 25 before the spec commit. The specs are
staged and not committed: every spec stays `rev-1` and a fix owes no §9 line, because a fix before the first commit
is still authoring. Every rule of the spec brief
`memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md` still binds.

### Items

- **F1 · the one-sided §3 edge (hygiene check 12).** TOOL-dFurnishedOrders-6 declares **consumes-from**
  `TOOL-dFurnishedOrders-8` naming the `### Method slices` block; unit 8 declares no **hands-off**
  `TOOL-dFurnishedOrders-6` back. Add that bullet to unit 8's §3 naming the same token, and make sure unit 8's text
  spells the token where it produces it.
- **F2 · hand-off tokens the receiver never names (`[handoff]`).** TOOL-dFurnishedOrders-14 hands
  `check_answered_range` to unit 6, and unit 6 never names it: name it in unit 6 where the hook calls the matcher.
  TOOL-dFurnishedOrders-15 hands `derive_return_arms` to unit 7, and unit 7 never names it: name it in unit 7 where
  the repair arm is composed (the brief's J3 spelling `compose_return_arms` is retired for the lexicon's
  `derive_return_arms`; use that one everywhere, and leave the old name only where unit 15 says it was renamed).
- **F3 · a suite named as an acceptance observation (`[bar]`).** TOOL-dFurnishedOrders-10's §6 names
  `adopt-roles.test.sh`, and TOOL-dFurnishedOrders-5's §6 names `check-protocol-parity.test.sh`. Rewrite each
  criterion to observe the unit's own code directly (the checker or the function on a staged break, a fixture, a
  probe the pass runs), and move the suite to a `New arm:` line in §7.
- **F4 · legs a files-touched path trips, absent from §7's leg line (`[guards]`).** Add each named leg to the §7
  leg line of its spec, verbatim, as `tools/gate-legs.json` spells it:
  - TOOL-dFurnishedOrders-14: `format-guard self-test`, `verifier fan-out self-test`, `review-join self-test`,
    `policy fixtures`.
  - TOOL-dFurnishedOrders-6: `format-guard self-test`, `verifier fan-out self-test`, `review-join self-test`,
    `recall floor arms`, `run-gates canary`, `run-gates gov canary`, `measure-legs selftest`, `govkit selftest`,
    `transition-audit arms`, `straggler-guard arms`, `govkit refusal join`, `govkit acceptance matrix`,
    `policy fixtures`.
  - TOOL-dFurnishedOrders-7: `recall floor`, `recall floor arms`, `policy fixtures`.
  - TOOL-dFurnishedOrders-9: `check-wiring self-test`, `policy fixtures`.
- **F5 · sibling disagreements the writers reported.** TOOL-dFurnishedOrders-11's S2 says the `### code-notes`
  block appears in every work order, while TOOL-dFurnishedOrders-18's F4 renders no block under
  `annotations.delivery = off`: unit 11 states the slot's block is absent under `off`, as unit 18 decides.
  TOOL-dFurnishedOrders-18's F3 adds `instructions` to unit 4's `ORDER_SLOTS`: unit 4 lists it among the slot
  points, so `render_slot` accepts it. Where either change adds a token a sibling hands or consumes, keep the §3
  edge both ways.
- **F6 · the run-wide sweep.** After F1 to F5, run `python tools/check-spec-tokens.py` and
  `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` in a throwaway clone under your scratch path with
  every spec of the folder committed there, and fix any red on a dFurnishedOrders spec the same way. A check-25 line
  reading `READER NOT IN TREE covers it` names a reader a parent creates and is not a red.

### Acceptance

`python tools/check-spec-tokens.py` prints no line naming a `memory/builds/dFurnishedOrders/spec/` file, and the
hygiene gate's checks 2, 12 and 25 print no FAILED line naming one, both in your clone.

### Gates

Only the two checks the Acceptance names, run by you in your clone; the main loop re-runs both on the real tree.

### Non-goals

Any new unit or new design, and any edit outside `memory/builds/dFurnishedOrders/spec/`. You commit nothing and render no
index: the main loop commits once after you return.
