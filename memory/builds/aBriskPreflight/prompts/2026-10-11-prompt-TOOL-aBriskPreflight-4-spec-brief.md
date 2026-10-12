# Spec brief — TOOL-aBriskPreflight-4: preflight starts its bounded probes together and collects each at its own check

**Serves:** research TOOL-aBriskPreflight-4

Read first: the build README, the prompt record and the baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`).

## What the trace shows

In the peer's 1561 s old-code preflight, `run_bounded` waited 754 s on four children, started and
awaited ONE AFTER ANOTHER inside `verb_preflight`'s precondition block in
`tools/unattended/unattended.sh`:

| Child | Started by | Wall |
|---|---|---|
| `$WIRING_CHECK` (`bash tools/check-wiring.sh --check`) | `check_wiring` | 544 s |
| `$LANDER --carry --slug <slug>` | `check_lander_mode` → `run_lander` | 57 s |
| `$LANDER --prepared --slug <slug>` | the same loop | 43 s |
| `$GATE_PROFILE_CMD` (`run-gates.sh --print-profile`) | `derive_gate_backstop` | 55 s |

None reads another's output, and every one sits in the block that runs to its end with `|| true`
after each check, so every collect point is reached on every path through that block.

## The mechanism, one

The four children are STARTED together at the top of that block and each is COLLECTED where it is
read today, so the block's printed lines, their order, every refusal number and every refusal's
text are unchanged; only the waits overlap. `run_bounded` today starts, records and waits in one
call; the spec splits it into a start half and a collect half (or an equivalent), keeping:

- the capture through FILES and never a substitution (the function's header: a substitution waits
  for the last inherited write end, which is a decoration, not a bound);
- the wrapper carrying the repository root as its `$0`, the exec-marker wait before
  `write_proc_record`, the process-ledger record per child, `</dev/null`;
- `RB_OUT`, `RB_STDOUT`, `RB_ERR`, `RB_TOOK` and the return status exactly as each caller reads them,
  `RB_TOOK` measured from that child's own start;
- `RB_BOUND` per call (the gates-green arm's backstop override) and `GATE_BOUND_LIVE`'s unbounded
  path.

Every other `run_bounded` caller (`--close`, `--dispatch`, the ask generator, the lander) keeps the
synchronous form.

## Things the spec must settle, with the reason

- Whether the lander's `--carry` and `--prepared` may run concurrently with each other and with the
  wiring check: read `tools/push-main.sh` for a lock, a verdict file or a git write either flag
  takes; the claim write already refuses while `push-main-active` exists.
- What happens to a started child when the block is left early by a path the spec finds, so no
  child outlives the verb unrecorded.
- Whether running four children at once on a loaded host is a net win — the A/B decides, and the
  spec says what result would make it lose.

## Out of scope

- The driver's readers `fact`, `runmd_of`, `readme_of` (aSparedSpawn-8 S1).
- The children's own cost: units 1, 2 and 3 own the wiring check's; `push-main.sh` and
  `run-gates.sh` are not edited here.

## Acceptance shape

- A preflight's printed lines in the same order before and after on one tree, the four probes'
  lines included.
- A stub `$WIRING_CHECK` that sleeps and a stub lander that sleeps, run under a sliced
  `unattended.test.sh` arm or a hermetic probe built from that suite's setup: the precondition
  block's wall is about the longest child, not their sum, and each child's refusal still prints at
  its own position with its own number.
- Each child still has a ledger row, and a child that outlives its bound is still killed and named.
- Witnesses in §6 by basename.

## Conventions

- Tier-2: a process-management change on a refusal path.
- Lexicon verbs for new functions; `gen_map.py --write`; the unattended kit's version bumped once at
  the end of the build, in every carrier `bash tools/check-kit-versions.sh` names.
- Order: 2, after unit 5 (same file).
