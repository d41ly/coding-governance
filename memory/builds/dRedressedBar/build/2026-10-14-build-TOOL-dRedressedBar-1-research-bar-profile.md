# The full bar with self-tests at ebce889c7 — reds, causes and profile

**Serves:** research TOOL-dRedressedBar-1..9

The owner asked for the full bar with every self-test, profiled, with every red and its cause. This
is that record. The run was on node `d`, in worktree `gov-bar-profile-failures-b80cc3` at
`ebce889c7`, with the tree clean, on 2026-10-13. The commands were:

```
GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh                      # run 1
GATE_REGEN_CHECK=0 GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh   # run 2
```

## Verdicts

- **Run 1** — exit 2, REFUSED in 15 s. The regen preflight found `memory/gotchas/INDEX.md` stale:
  12 outputs were declared, 11 fresh and 1 stale.
- **Run 2** — exit 1, wall 21628 s. Its last line reads `gates RED — the 21600s wall fired; the run
  was killed, not the legs`. 139 of 140 legs reported, and 16 of them are red. The run-gates canary
  timed out at its 13200 s ceiling, was retried, and was still running when the whole-run wall fired.
- `GATE_REGEN_CHECK=0` was set only so run 2 would list the reds past the refusal. It leaks into
  nested runners: the canary's regen-refusal arms `1s-a`, `1s-b`, `1s-e` and `1t-e` read rc 0 because
  of it. That is a separate finding and is out of this build's scope. The pre-push hook scrubs the
  knob, and govkit sets it itself, so no other red depends on it.

## Reds and causes

Each row gives the leg, then the cause, then the unit that fixes it.

| Leg | Cause | Unit |
|---|---|---|
| regen preflight (run 1) · memory hygiene (check 17) | The merge `ebce889c7` resolved `memory/gotchas/INDEX.md` with `merge=ours` to local main's copy and did not re-render it. It lost origin's two rows. | 7 |
| kickoff-manifest ratchet | Check 5: `tools/gate-legs.json` moved after `last-audit`. Check 9: the body was unchanged across 15 watched commits. | kickoff repair `2e187ee8b` |
| lexicon naming predicates · lexicon wiring | 1088 verb offenders against a pin of 1087. The one arrival is `clean` at `tools/unattended/gate-guard.js:689`. | 2 |
| shell hygiene (a fork spent on builtin work) | There are unregistered fork sites in the adopt-branch-reconcile, adopt-roles and format-guard sources. `unattended-build.test.sh` grew past its registry rows. | 5 |
| install-prefix (shipped surface) | `'workflows'` in `format-guard.js:333` and `adopt-roles.test.sh:228` names Claude's session directory, which the ban's rule 4 reads as the kit. | 4 |
| method carriers | `.claude/agents/gov-reuse-scout.md` names `BUILD-METHOD.md` and is not declared. | 7 |
| harness arms | The exits at `tools/roles/adopt-roles.sh:209` and `:217` have no positive arm. | 6 |
| tier2-review self-test · foreign-prefix parity | TOOL-aOrientedCast-27 moved the prelude anchors, so 0 of the 322 floor assertions ran. The roles adopter suite prints no probe marker. | 1 |
| unattended-build self-test | The GH33 call sites glue `build_gh33_writer`'s two arguments into one word, so `$2` is unbound. | 1 |
| run-gates turnstile | Arm 44's sed seam rewrites `cat "$d/pid"`, but the runner now reads the pid with `read -r`. 0 of 2 reads are routed. | 1 |
| pre-push self-test | Eleven arms read the merge-loss skip line, because their fixtures carry no lexicon kit. | 1 |
| push-main self-test | Arms 28 and 29 clone HEAD, whose index is already stale, so the regenerated index can never equal it. This is the INDEX red again. | 7 |
| govkit selftest | There are four fixture causes: the PV cascade (46 arms), aQuenchedHarness-3 (2), the runner apply (3), and the default-gained cluster (5). The last of these exposes a product defect in `govkit update`. | 3 and 9 |
| run-gates canary | Arm 11g AC14 hangs. Its FIFO server dies on a failed open or a SIGPIPE, and the nested bar it holds has no bound. | 8 |

The standalone re-runs in the confirmation pass, without the knob, gave these results:
- push-main: rc 1, 353 s.
- unattended-build: rc 1, 109 s.
- turnstile: rc 1, 904 s.
- govkit: rc 1, 6413 s. Its 103 failures run against a tree this session committed to mid-run, so
  the count is mixed-state and only its red stands.

## Profile

Per-leg seconds come from `<gate-work>/<n>.sec`. End times come from each leg's `.rc` mtime, and
start is end minus seconds. Host load was sampled every 10 s: CPU load percentage, free memory and
process counts.

- **Phases.** The pool ran 8 wide from 18:50:33 to 19:18:22 local. In that time 139 legs finished,
  and the last to end was `govkit selftest`. From 19:18 to 22:30 the canary ran alone until its
  ceiling, then from 22:30 to 00:50 its retry ran alone until the 21600 s whole-run wall fired.
  **About 87% of the run's wall time was one hung leg.**
- **Totals.** The sum of leg seconds was 23536 s over the first attempt's 13200 s span, a mean
  concurrency of 1.78. The selftests chunk accounts for 22002 s of it, of which 13200 s is the canary.
- **Host.** Mean CPU was 7% during the pool phase and 1% while the canary hung. Free memory never
  fell below 7952 MB of 32419 MB. At most 78 bash processes ran at once. The bar is bound by
  spawn cost here, never by CPU or memory.

| Chunk | Legs | Sum s | Max s | Red |
|---|---:|---:|---:|---:|
| selftests | 67 | 22002 | 13200 | 7 + canary |
| declarations | 37 | 1321 | 451 | 3 |
| product | 18 | 84 | 52 | 2 |
| records | 4 | 69 | 65 | 2 |
| wiring | 12 | 41 | 28 | 1 |
| e2e | 2 | 19 | 11 | 0 |

The ten slowest legs, with the share of each leg's ceiling it used:

| Leg | Verdict | s | Ceiling | Share |
|---|---|---:|---:|---:|
| run-gates canary | timeout | 13200 | 13200 | 100% |
| govkit selftest | FAIL | 1670 | 11750 | 14% |
| run-gates turnstile | FAIL | 969 | 8210 | 12% |
| run-gates evidence | ok | 779 | 7040 | 11% |
| memory-hygiene self-test | ok | 737 | 4800 | 15% |
| pre-push self-test | FAIL | 616 | 1780 | 35% |
| manifest-check self-test | ok | 585 | 4370 | 13% |
| unattended kit gate | ok | 451 | 16040 | 3% |
| push-main self-test | FAIL | 416 | 580 | 72% |
| run-selftests self-test | ok | 364 | 2040 | 18% |

The canary's ledger history on this node runs from 413 s to 3395 s, so the timeout is a hang and not
cost. Without it, this bar is about 28 minutes at width 8. The ceilings are generous: no other leg
used more than 72% of its own.
