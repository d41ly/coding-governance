# TOOL-dPlacedRequest-48 — the request-lock race is placed by an announcing stub, not left to the scheduler

**Status:** CLOSED · rev-10 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 25 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 |
| [2026-10-25-build-TOOL-dPlacedRequest-48-deviation-481.md](../build/2026-10-25-build-TOOL-dPlacedRequest-48-deviation-481.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-48-deviation-482.md](../build/2026-10-25-build-TOOL-dPlacedRequest-48-deviation-482.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-48-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-48-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 TOOL-dPlacedRequest-100 |
| [2026-11-21-build-TOOL-dPlacedRequest-48-deviation-701.md](../build/2026-11-21-build-TOOL-dPlacedRequest-48-deviation-701.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-44-order-25-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-44-order-25-reground-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-50 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-44-pass-red-fix-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-44-pass-red-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-50 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-49 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
confirmed **finding 16 at HIGH**, its item **H4**, which holds no other finding; its busy path is
finding 37 (item M17), an item of `TOOL-dPlacedRequest-49`. The finding: nothing placed a second
`--request` call inside the first call's compare-to-copy window, so a criterion of two background
calls was green on unlocked code, and the racing overwrite of stored words the lock closes shipped
unobserved.

`TOOL-dPlacedRequest-43` has since built the lock and is CLOSED.
`tools/unattended/unattended.sh#write_request_record` takes `write_dir_lock_wait` on
`<git-common-dir>/requests.lock`, stem `node`, waiting 5 s (PINNED), around the fold compare, the copy and the
`.typed` append, and a lock still busy prints `requests.lock busy` and exits 2, writing nothing.
Spec 43's AC30 observes a planted, held lock directory, not two calls racing, and names this unit's
arm as the race's observation (its F6). The race is still unplaced. This unit places it: the first
call announces from inside its window, the second runs while it waits there, and the arm reds if the
announcement never comes.

## 2. Scope (IN)

- **S1** — The placement seam. `--request`'s copy is one external `cp` spawn, the step after the
  compare: `cp -- <file> <git-common-dir>/requests/<key>.md.<pid>`, into a temporary sibling named
  by the key's file name and the driver's process id, which `mv -n` then moves onto `<key>.md`. The
  arm puts a stub `cp` first on `PATH`. Its first call whose last argument matches
  `*/requests/*.md.*` takes `mkdir "$h/once"`, touches `$h/held`, and waits for `$h/release` under a
  60 s bound before running the real `cp`; every other call runs the real `cp` at once. No product
  code carries a test hook. Observed by AC1.
- **S2** — The placed race, over the lease fixture of the `TOOL-dPlacedRequest-43` block of
  `tools/unattended/unattended.test.sh`, driven through `run_request_arm`. Call A starts in the
  background with `a.md` under session `qA`; the arm waits for `$h/held` under a 30 s bound, then
  runs call B with `b.md` under session `qB` to its end, the two texts differing only in an ISO date
  so they key alike; then it touches `$h/release` and waits for A. B exits 2 printing
  `requests.lock busy` and writes nothing. A exits 0 printing `recorded`, the stored copy is
  byte-identical to `a.md`, `.typed` holds one line, `qA`'s, and the origin holds one request ref for
  the key. A third call with `b.md` then exits 2 printing `collision`. The arm prints the seconds from
  `$h/held` to B's end beside B's exit. Observed by AC1 and AC2.
- **S3** — The placement is live. When `$h/held` never appears within its bound, the arm reds with
  `request race never placed`, so a copy step that is not a `cp` spawn turns the arm red, never
  vacuously green. Observed by AC3.
- **S4** — One observation of the lock, an observation. Spec 43's AC30 already names this unit's
  placed-race arm as the race's observation and holds no two-background-call form; this unit writes
  nothing into spec 43. Observed by AC4.
- **S5** — The floors. `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by the arm's assertion count,
  each with a `RAISED` comment in the shape the `TOOL-dPlacedRequest-43` entries use.
  NOT OBSERVED: the floors are the suite's own count, read when the suite runs at the close, and that
  run is waived for this build's landing by README rule 8.

## 3. Non-goals (OUT)

- No change to the lock, its wait or where it is taken: `TOOL-dPlacedRequest-43` S30 built them.
- No new busy outcome: the busy line and exit 2 are built (43 S30), and S2 reads them as B's
  outcome.
- No re-run of a placement that overruns the lock's hold bound: `TOOL-dPlacedRequest-52`'s items for
  findings 12, 23 and 31.
- No cross-node race: `TOOL-dPlacedRequest-30` §3 leaves it out.
- No edit to spec 43, which is CLOSED.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-43` — S30's `requests.lock` around the compare, copy and append, which this arm observes, and AC30, which names this arm since that spec's rev-11; without the lock there is nothing for the placed race to observe
- **hands-off** `TOOL-dPlacedRequest-52` — the placed-race arm, S1, S2, AC2 and AC4, which that unit's items for findings 4, 12, 13, 15, 23, 24 and 31 bound, cite and re-scope; B's lock wait is bounded at 5 s (PINNED) in the tree, so this unit's own pass observes the race, and the overrun re-run is that unit's
- **hands-off** `TOOL-dPlacedRequest-56` — §4 Files touched, which that unit's item for finding 3 gives its sequence line
- **hands-off** `TOOL-dPlacedRequest-58` — the stub's write set, `$h/once` and `$h/held`, which that unit's reset clears and asserts absent before each attempt
- **hands-off** `TOOL-dPlacedRequest-61` — §4 Files touched, whose sequence sentence that unit's item for finding 10 fixes word for word

## 4. Design

### The arm

```
stub cp:   case "${!#}" in */requests/*.md.*)
             mkdir "$h/once" 2>/dev/null && { touch "$h/held"; wait for "$h/release", 60 s bound; } ;;
           esac; exec <real cp, read by command -v before PATH moves> "$@"
A:  PATH="$h/bin:$PATH" run_request_arm --request a.md &          (RQ_SID qA)
    wait for "$h/held", 30 s bound, else bad "request race never placed"; t0=$EPOCHSECONDS
B:  PATH="$h/bin:$PATH" RQ_SID=qB run_request_arm --request b.md; rcB=$?; t1=$EPOCHSECONDS
    touch "$h/release"; wait A; rcA=$?
assert rcB = 2 and "requests.lock busy", rcA = 0 and "recorded",
       cmp -s requests/<key>.md a.md, .typed = qA alone, one refs/gov/requests/<key> on the origin
C:  run_request_arm --request b.md -> exit 2, collision
```

B runs while A holds `requests.lock` inside its window, so the built driver makes B wait 5 s (PINNED) and
refuse, and an unlocked driver lets B find no stored copy, copy `b.md` and exit 0. The bounded waits
poll for a file, the shape `memory/gotchas/fixed-sleep-does-not-place-a-signal.md` names: the test
acts on an announcement, never on a guess about the scheduler.

### Placement

A block of its own in `tools/unattended/unattended.test.sh`, after the `TOOL-dPlacedRequest-43`
block's AC32 rows and before that block's `rm -rf "$LF"`, so it reuses the lease fixture
`write_lease_fixture` made and `tools/unattended/unattended.test.sh#run_request_arm`. Its texts carry
a marker of their own, so their key is new to the fixture's store.

### The timing the arm rests on

- B's wait: the `5` passed to `write_dir_lock_wait` in `write_request_record` (PINNED, 2026-11-20).
- A's hold: `tools/unattended/unattended.sh#write_dir_lock` writes `until` as the take plus
  `NODE_LOCK_BOUND`, 10 s (PINNED, 2026-11-20), and `tools/unattended/unattended.sh#check_dir_lock_stale`
  reads a passed `until` as stale, since this lock records no pid file.
- So B refuses before A's `until` while B reaches its lock attempt within 5 s (DERIVED, 10 less 5) of
  A's take. The 43 block's AC30 row measured a whole refused `--request` inside 6 s (PINNED, unit 43's
  acceptance ledger), so B's preamble took about 1 s at most (PINNED) on the build's node. A B that overruns
  breaks A's lock as stale, copies `b.md`, and reds the arm; the printed seconds name that cause.

### Evidence

- `tools/unattended/unattended.sh#write_request_record`: the lock call, then the compare, then
  `cp -- "$f" "$cdir/requests/$key.md.$$"` and `mv -n` onto `$key.md`, then the `.typed` append, then
  `remove_dir_lock`; read 2026-11-20.
- The driver before unit 43's lock copies through the same temporary sibling
  (`tools/unattended/unattended.sh@7e00d7e0:4626`, the blob at `dac2af17c`), so the stub fires on it
  too and the staged red reads the lock alone.
- The suite already places PATH stubs ahead of the driver: the `TOOL-dPlacedRequest-43` block writes a
  `git` stub into `$GH_BIN` and runs `PATH="$GH_BIN:$PATH" run_proc`
  (`tools/unattended/unattended.test.sh@2f86892d:21560`).

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: the placed-race block and the two floors with their
  `RAISED` comments
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **An environment hold seam in the driver.** It puts a wait any caller can arm into a shipped
  verb; a PATH stub holds only the arm's own processes.
- **A fixed sleep between the two calls.** It places nothing, the class this finding is filed under.
- **A stub keyed on the stored `<key>.md`.** The driver never copies onto that name; it copies onto
  the temporary sibling and moves, so such a stub never fires (F2).

## 5. Production-readiness checklist

- security — none in product: the stub lives in the arm's scratch directory.
- perf / scale — three driver calls, one 5 s (PINNED) lock wait and at most one bounded hold per run of the
  arm.
- error / empty / loading states — a hold that never fires reds, named (S3).
- observability — the arm prints each call's exit, B's seconds after the hold, and the stored copy's
  compare.
- risks — a builder who writes the copy without `cp` reds the arm, the red naming the cause; a slow
  node can let B overrun A's hold, which reds the arm with the seconds shown until
  `TOOL-dPlacedRequest-52` re-runs an overrun; the block adds commands to region eight, which a seam
  cuts if bash 5.3 on Cygwin segfaults, as the region's existing seams do.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — none: a suite arm.

## 6. Acceptance criteria

The fixture is the lease fixture of the `TOOL-dPlacedRequest-43` block: `write_lease_fixture`'s bare
origin and clone under `%TEMP%`, `RUN_CLAIMS=on`, driven by `run_request_arm`.

- **AC1** — When the §4 arm runs, `$h/held` appears, B exits 2 printing `requests.lock busy`, A exits
  0 printing `recorded`, `cmp -s` of `<git-common-dir>/requests/<key>.md` with `a.md` succeeds,
  `grep -c ''` over `<key>.typed` prints 1, and `git for-each-ref refs/gov/requests` run in the
  fixture's bare origin lists the key once.
  Red when: B copies; the staged case is the arm run with `SCRIPT` set to the driver of a worktree at
  `dac2af17c`, before unit 43's lock, where B exits 0 and the stored copy is `b.md`.
  figure: the one `.typed` line and the one ref PINNED; the 5 s wait and the 10 s hold PINNED,
  read 2026-11-20.
- **AC2** — When the third call runs `--request b.md` after A ends, it exits 2 printing `collision`.
  Red when: the compare is not re-run after the lock is released.
- **AC3** — When the stub is replaced by a pass-through `cp` that never touches `$h/held`, the arm
  prints `request race never placed` and fails.
  Red when: an unplaced race reads as a pass.
- **AC4** — When the AC30 paragraph of `2026-10-25-spec-TOOL-dPlacedRequest-43.md` is cut by
  `awk '/^- \*\*AC30\*\*/{f=1} f&&/^- \*\*AC3[1-9]\*\*/{exit} f'` and squeezed by
  `tr -s '[:space:]' ' '`, it names `TOOL-dPlacedRequest-48` and holds no `two background`.
  Red when: the unplaced two-background-call form stands as the lock's observation.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · the placed request race, staged by the driver of a worktree at `dac2af17c`, before unit 43's lock · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by the block's count · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What places the second call inside the first call's window?** (a) A PATH stub `cp` that
  announces and holds; (b) an environment hold seam in the driver; (c) two background calls, as AC30
  read when this unit was promoted. (c) places nothing; (b) ships a test hook in a verb. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 2, the suite's existing PATH-stub shape and the review's
  fix judged sound. widens: none · relaxes: none
- **F2 — Which spawn does the stub hold, now that the copy lands through a temporary sibling?**
  (a) The `cp` onto `<key>.md.<pid>`, matched by its last argument; (b) the `mv -n` onto `<key>.md`;
  (c) a `cp` whose destination is `<key>.md`, as rev-8 read. (c) never fires on the tree; (b) holds a
  step that is also inside the lock but sits after the copy, so a driver that moved the copy outside
  the lock would still be held. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the `cp` is the first spawn after the
  compare in `write_request_record`, the driver before the lock makes the same spawn, so the staged
  red reads the lock alone, and the brief names the copy the tree makes. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  16 (HIGH, item H4).
- rev-2 · 2026-10-25 · header above §1 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line, binding this audit-promoted unit, which carries no clause, to the decision that derives it.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edge to `TOOL-dPlacedRequest-56`, mirroring its consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edge to `TOOL-dPlacedRequest-58`, mirroring its consumes-from.
- rev-6 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-7 · 2026-11-19 · §1 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit` finding 15 (H3): the node lock is the shared `write_dir_lock` family, which `TOOL-dPlacedRequest-24` rev-5 S1 moves into `gov_feed_sh`, so every name of the lock factory this spec spells is that family's.
- rev-8 · 2026-11-19 · §4 Files touched · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-9 · 2026-11-20 · §1 · §2 S1 to S5 · §3 · §4 · §5 · §6 AC1 AC4 · §7 · §8 F2 · §10 · re-grounded
  by `2026-11-20-prompt-TOOL-dPlacedRequest-44-order-25-reground-brief`: unit 43's built lock read
  from `tools/unattended/unattended.sh#write_request_record`; S1's stub keyed on the temporary
  sibling the copy lands in (F2); S2's outcomes re-checked against the lock, B exiting 2 with
  `requests.lock busy`; S4 and AC4 reduced to an observation of spec 43's AC30, folded by its F6;
  the fixture named as the 43 block's lease fixture; S5 names the floors; the red stage named as the
  driver at `dac2af17c`; line citations swapped for symbol citations and blob pins.
- rev-10 · 2026-11-20 · §1 · §3 · §4 · §5 · the inline red fix `2026-11-20-prompt-TOOL-dPlacedRequest-44-pass-red-fix-brief`: each line carrying the request lock's wait pins it as PINNED on that line.

## 10. Reuse audit

The seams reused are the suite's PATH-stub pattern, the `TOOL-dPlacedRequest-43` block's lease
fixture with `tools/unattended/unattended.test.sh#run_request_arm`, and the announce-then-act fix of
`memory/gotchas/fixed-sleep-does-not-place-a-signal.md`; no product seam is added.
`python tools/codebase-map/reuse_lookup.py "place a race between two driver calls with a blocking
stub"`, re-run 2026-11-20, ranked `drive`, `run_driver`, `load_driver_conf` and
`render_charter_blocks`, name stems only, none a race placement. `python tools/memory-recall/query.py "how does a test place a second call inside the first
call's critical section"` with the terms below, re-run 2026-11-20, returned this spec,
`TOOL-aSparedSpawn-22`, the round-2 audit's H4, `TOOL-dPlacedRequest-52` and spec 43's requests-lock
design; none disagrees with source.

Recall terms used: race placement stub announce file ready file fixed sleep lock requests.lock collision cp hold
