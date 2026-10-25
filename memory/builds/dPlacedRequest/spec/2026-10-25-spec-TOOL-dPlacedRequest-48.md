# TOOL-dPlacedRequest-48 — the request-lock race is placed by an announcing stub, not left to the scheduler

**Status:** OPEN · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 25 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 |
| [2026-10-25-build-TOOL-dPlacedRequest-48-deviation-481.md](../build/2026-10-25-build-TOOL-dPlacedRequest-48-deviation-481.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
confirmed **finding 16 at HIGH**, its item **H4**, which holds no other finding; its busy path is
finding 37 (item M17), an item of `TOOL-dPlacedRequest-49`. `TOOL-dPlacedRequest-43` S30 takes
`write_node_lock` on `requests.lock` around `--request`'s compare, copy and `.typed` append, and its
AC30 starts two background `--request` calls and expects exactly one `collision`. Nothing places the
second call inside the first call's compare-to-copy window. Without the lock the calls almost always
run one after the other, the second compare sees the first copy, and `TOOL-dPlacedRequest-30` S1
refuses it `collision` anyway, so AC30 is green on unlocked code and the racing overwrite of stored
words that S30 and its §5 security line claim to close ships unobserved. This unit repairs
`TOOL-dPlacedRequest-43`, at order 24, so it sits at order 25: the interleaving is placed by the
first call announcing it is inside the window, and the arm reds if that announcement never comes.

## 2. Scope (IN)

- **S1** — The placement seam. `--request`'s copy into `<git-common-dir>/requests/` is one external
  `cp` spawn, the step after the compare. The arm puts a stub `cp` first on `PATH`: its first call
  whose destination is under `requests/` takes `mkdir "$h/once"`, touches `$h/held`, and waits for
  `$h/release` under a 60 s bound before running the real `cp`; every other call runs the real `cp`
  at once. No product code carries a test hook. Observed by AC1.
- **S2** — The placed race. Call A starts in the background with `a.md`; the arm waits for `$h/held`
  under a 30 s bound, then runs call B with `b.md`, the two differing only in an ISO date, to its
  end, then touches `$h/release` and waits for A. B exits non-zero and writes nothing: the stored
  copy is byte-identical to `a.md` after A ends, `.typed` holds A's session alone, and the remote
  holds one record. A exits 0. A third call with `b.md` then exits 2 printing `collision`. Observed
  by AC1 and AC2.
- **S3** — The placement is live. When `$h/held` never appears within its bound, the arm reds with
  `request race never placed`, so a copy step that is not a `cp` spawn turns the arm red, never
  vacuously green. Observed by AC3.
- **S4** — One observation of the lock. `TOOL-dPlacedRequest-43` AC30 is rewritten in place, as a rev
  bump with its §9 line, to name this unit's arm as its observation. Observed by AC4.

## 3. Non-goals (OUT)

- No change to the lock itself or to where it is taken: `TOOL-dPlacedRequest-43` S30's.
- No busy outcome for `requests.lock`: finding 37's item of `TOOL-dPlacedRequest-49`; S2 asserts only
  that B writes nothing, which holds for a retry that times out, a single-shot refusal or a wait that
  ends in `collision`.
- No cross-node race: `TOOL-dPlacedRequest-30` §3 leaves it out.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-43` — S30's `requests.lock` around the compare, copy and append, which this arm observes, and AC30, which this unit rewrites in place; without the lock there is nothing for the placed race to observe
- **hands-off** `TOOL-dPlacedRequest-52` — the placed-race arm, S1, S2, AC2 and AC4, which that unit's items for findings 4, 12, 13, 15, 23, 24 and 31 bound, cite and re-scope; at order 25 B's lock wait has no bound, so this unit's own pass observes AC3 and the stub, and the race is read at that unit's pass

## 4. Design

### The arm

```
stub cp:   case dest in */requests/*.md)
             mkdir "$h/once" 2>/dev/null && { touch "$h/held"; wait for "$h/release", 60 s bound; } ;;
           esac; exec <real cp> "$@"
A:  PATH="$stub:$PATH" unattended.sh --request a.md &           (session s1)
    wait for "$h/held", 30 s bound, else bad "request race never placed"
B:  PATH="$stub:$PATH" unattended.sh --request b.md; rcB=$?      (session s2)
    touch "$h/release"; wait A; rcA=$?
assert rcA = 0, rcB != 0, cmp -s requests/<key>.md a.md, .typed = s1 alone, one remote record
C:  unattended.sh --request b.md -> exit 2, collision
```

B runs while A holds `requests.lock` inside its window, so a locked build makes B wait or refuse and
an unlocked build lets B copy `b.md` and exit 0. The bounded waits poll for a file, the shape
`memory/gotchas/fixed-sleep-does-not-place-a-signal.md` names: the test acts on an announcement,
never on a guess about the scheduler.

### Evidence

- `TOOL-dPlacedRequest-43` S30 and AC30; `TOOL-dPlacedRequest-30` §4 orders the compare before the
  copy and the copy before the `.typed` append.
- The suite already places PATH stubs ahead of the driver, for example
  `tools/unattended/unattended.test.sh:6098`, `PATH="$stubdir:$PATH" bash "$SCRIPT" --close tRun`.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: the placed-race arm
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md`: AC30 and its §9
  line. `TOOL-dPlacedRequest-44` writes this file at the same order, so the two passes run in
  sequence.

### Alternatives rejected

- **An environment hold seam in the driver.** It puts a wait any caller can arm into a shipped
  verb; a PATH stub holds only the arm's own processes.
- **A fixed sleep between the two calls.** It places nothing, the class this finding is filed under.

## 5. Production-readiness checklist

- security — none in product: the stub lives in the arm's scratch directory.
- perf / scale — three driver calls and at most one bounded wait per run of the arm.
- error / empty / loading states — a hold that never fires reds, named (S3).
- observability — the arm prints each call's exit and the stored copy's compare.
- risks — a builder who writes the copy without `cp` reds the arm; the red names the cause.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — none: a suite arm.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-19`'s: a bare remote and a clone under `%TEMP%` with a short name,
`RUN_CLAIMS=on`, a fixture `fleet.toml`.

- **AC1** — When the §4 arm runs, `$h/held` appears, B exits non-zero, A exits 0, `cmp -s` of
  `<git-common-dir>/requests/<key>.md` with `a.md` succeeds, and `grep -c ''` over `<key>.typed`
  prints 1.
  Red when: B copies, the staged case being a scratch copy of the driver with `requests.lock` removed,
  where B exits 0.
- **AC2** — When the third call runs `--request b.md` after A ends, it exits 2 printing `collision`.
  Red when: the compare is not re-run after the lock is released.
- **AC3** — When the stub is replaced by a pass-through `cp` that never touches `$h/held`, the arm
  prints `request race never placed` and fails.
  Red when: an unplaced race reads as a pass.
- **AC4** — When `grep -n 'AC30' 2026-10-25-spec-TOOL-dPlacedRequest-43.md` runs, the criterion names
  `TOOL-dPlacedRequest-48`.
  Red when: the unplaced two-background-call form stands as the lock's observation.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · the placed request race, staged by a scratch driver with `requests.lock` removed · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What places the second call inside the first call's window?** (a) A PATH stub `cp` that
  announces and holds; (b) an environment hold seam in the driver; (c) two background calls, as AC30
  reads. (c) places nothing; (b) ships a test hook in a verb. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 2, the suite's existing PATH-stub shape and the review's fix judged sound.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  16 (HIGH, item H4).
- rev-2 · 2026-10-25 · header above §1 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line, binding this audit-promoted unit, which carries no clause, to the decision that derives it.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.

## 10. Reuse audit

The seams reused are the suite's PATH-stub pattern (`tools/unattended/unattended.test.sh:6098`) and
the announce-then-act fix of `memory/gotchas/fixed-sleep-does-not-place-a-signal.md`; no product seam
is added. `python tools/codebase-map/reuse_lookup.py "place a race between two driver calls with a
blocking stub"` ranked `drive`, `render_charter_blocks` and `find_block`, name stems only, none a race
placement. `python tools/memory-recall/query.py "how does a test place a second call inside the first
call's critical section"` returned TOOL-aSparedSpawn-22, this audit's H4, TOOL-aReplayedCard-11 and
the `fixed-sleep-does-not-place-a-signal` class; none disagrees with source.

Recall terms used: race placement stub announce file ready file fixed sleep lock requests.lock collision cp hold
