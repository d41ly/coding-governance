# TOOL-dLandedVerdict-2 — the close-out: seven builds that landed and never said so
**Status:** INPROGRESS · rev-1 · 2026-08-19 · node d · Tier-1 · base 098bebd9 · streams tooling

## 1. Goal

Take the seven builds whose product work is confirmed on `main` and whose spec records still read
non-terminal, and make the records true. The drain is also `TOOL-dLandedVerdict-1`'s acceptance: its
pin falls by construction, which is the only evidence that the signal measures the thing it names.

## 2. Scope (IN)

**S1** — twenty-three spec status headers go terminal, in the same commit that reports the drain:

| build | specs | token today |
|---|---|---|
| `aTetheredRecord` | 7 | INPROGRESS |
| `cKeyedLaunchpad` | 7 | OPEN |
| `aDrainedSluice` | 4 | INPROGRESS |
| `aTimedTurnstile` | 2 | INPROGRESS |
| `aBatchedLintel` | 1 | INPROGRESS |
| `aGuardedTally` | 1 | INPROGRESS |
| `aWireWarden` | 1 | INPROGRESS |

- **S2** — each header keeps its `rev-N` and moves its DATE only. A status flip is not a material
  content change, so no rev bump and no §9 line, per `memory/TEMPLATE-SPEC.md`.
- **S3** — `memory/LIVE.md` and `memory/ledger/<month>.md` re-rendered with
  `python tools/memory-tree/gen_build_index.py --write`. Never hand-edited.
- **S4** — nine backlog rows go CLOSED, each carrying the landing commit as its reason: the seven
  `TOOL-aTetheredRecord-1..7` rows, and `TOOL-aTimedTurnstile-1` and `-2`.
- **S5** — each closed spec's §8 first non-blank line is verified machine-legal before the flip.
  Hygiene check 12 reads that line and nothing else, so a spec whose §8 does not resolve reds the
  moment its status goes terminal.

## 3. Non-goals (OUT)

- The five builds that landed and must NOT close — `aSealedCaravan`, `aTetheredConvoy`,
  `bConvergentLodestar`, `aMendedLedger`, `aQuarriedLantern`. Each has an unmet DoD, an unlanded unit
  or unratified owner decisions. They stay open and the new signal keeps reporting them, which is
  correct behaviour and not debt.
- `aWalkedCorpus`, whose one non-terminal spec is `DEFERRED` — a chosen state.
- `aDeployScout`, a research record with no status header, outside the signal's population entirely.
- The other five `aTimedTurnstile` backlog rows. They are unbuilt follow-ups and stay OPEN.
- Rotating any backlog shard. Nine rows become rotatable; rotation is a separate act with its own
  archive discipline.

## 4. Design

Mechanical, in one order that matters: verify §8 resolves (S5), flip the header, re-render, then
re-read the signal. Reversing the first two steps is how a terminal spec with an unresolved §8 reds
hygiene check 12 with the generator already run over it.

The nine backlog rows and the twenty-three headers are separate carriers of the same fact and are
committed together, because a reader who sees one updated and not the other cannot tell which is
current.

## 5. Production-readiness checklist

- security — N/A. Records only.
- perf / scale — `memory/LIVE.md` shrinks by six builds net, which returns read-path headroom that
  `TOOL-aRelaxedShard-3` records as scarce.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the drain is visible as a pin movement in `drift_report.py` output.
- risks — closing a build whose work did not land writes a false record permanently. Mitigated by
  the ground-truth pass: every one of the seven was verified at artifact level and then handed to a
  skeptic instructed to refute it. The five that failed refutation are OUT.
- testing + left-shift gates — the full bar; `TOOL-dLandedVerdict-1`'s signal is the left-shift.
- migration / rollback — `git revert` of one records-only commit.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs after the flips,
  `memory/LIVE.md` no longer lists any of the seven builds.
- **AC2** — When `python tools/drift-audit/drift_report.py` runs after the close-out, the
  `landed_specs_left_non_terminal` value is strictly lower than the pin
  `TOOL-dLandedVerdict-1` seeded, and the pin is lowered to the new measurement in the same commit.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, it is green — in particular
  check 12, which reds a terminal spec whose §8 does not resolve.
- **AC4** — When the TOOL shard is counted, its live-row total has fallen from 91 to 82, below the
  `live_backlog_rows_per_shard` tolerance of 89, and `python tools/drift-audit/drift_report.py`
  reports that signal in tolerance.
- **AC5** — When `git log` is consulted for each closed spec, the landing commit named in its
  backlog row is an ancestor of `main`.

## 7. Gates

`bash tools/run-gates.sh` with `GATE_FULL=1`. Records-only diffs skip the guarded self-test legs, so
the unguarded run would not exercise the drift-audit legs this unit's acceptance depends on.

## 8. Open questions

none — scope was resolved by the owner on 2026-08-19 (close all seven confirmed-closeable builds
rather than the two originally priced), and the exclusion list in §3 follows from the refutation pass
rather than from a judgement left open here.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft, after the ground-truth pass over all seventeen live builds.

## 10. Reuse audit

No new seam. The close-out runs entirely through existing machinery:
`tools/memory-tree/gen_build_index.py --write` owns the generated indexes, and the status vocabulary
is `memory/HYGIENE.md` check 8's. The procedure this unit follows is already recorded in this repo —
the `aLoosenedCeiling` review of 2026-08-18 states it: flip the spec status headers in the same
commit that lands the code, update the build README, re-render `memory/LIVE.md`, re-run the leg. This
unit is that remedy applied to a backlog of seven builds where it was skipped.
