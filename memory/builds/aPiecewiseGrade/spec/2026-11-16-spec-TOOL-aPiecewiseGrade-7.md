# TOOL-aPiecewiseGrade-7 — an arm for the stale check's foreign-runtime clause

**Status:** INPROGRESS · rev-1 · 2026-11-16 · node a · Tier-1 · base aebbb4a72 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-7-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-7-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-7-review-brief.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-7-review-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-7-revision.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-7-revision.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The foreign-runtime clause of `check_dir_lock_stale` keeps a pid recorded by another runtime counted
as live, and no suite arm reds when it is deleted. This unit adds one plant to the driver suite whose
pid record names another runtime and a dead pid, expected held, so deleting the clause reds the suite.
It answers item 1 of `2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2`.

## 2. Scope (IN)

- **S1** — A fifth kind, `foreign`, in the AC13 loop of the TOOL-aPiecewiseGrade-6 block of
  `tools/unattended/unattended.test.sh`. Its plant is one `pid.driver` line carrying a dead pid, the
  token `-` and the runtime `otherhost:otheros`, written with `printf` and never through
  `write_pg6_pid`, with no `pid.checker` file. The loop's `same` expects `foreign:1:w-x`. Observed by
  AC1 and AC2.
- **S2** — The block's header comment lists the runtime clause among its RED-first staged breaks, and
  the AC13 comment and the `same` label count five plants and name the foreign one. Observed by AC2.
- **S3** — The suite's assertion count and its floors stay where they are, because the kind joins an
  existing assertion rather than adding one. Observed by AC3.

## 3. Non-goals (OUT)

- Any edit to `tools/unattended/unattended.sh` or any other product file. The shipped clause is
  correct; this unit adds only its arm.
- A version bump for the unattended kit. The suite ships as `engine`
  (`tools/unattended/kit.toml`), but the lander mints the bump at the push boundary and a branch owes
  none (`tools/govkit/govkit.py#cmd_epoch`).
- Item 2 of the same review, the spec-token checker's counter key-set arms, which
  TOOL-aPiecewiseGrade-8 writes.
- `FLOOR_SHARD_3` at `tools/unattended/unattended.test.sh@6d3ce6ef:20198` reads 451, and its comment
  block records no raise from TOOL-aPiecewiseGrade-6's region-three arms. A floor below the true count
  fails only to catch a shrink, never reds, and this unit moves no count, so it is left as found.
- Any edit to a CLOSED spec, the TOOL-aPiecewiseGrade-6 spec included.

## 4. Design

The clause sits at `tools/unattended/unattended.sh@13a5efd0:2563`, inside the pid loop of
`tools/unattended/unattended.sh#check_dir_lock_stale`. A record reads as gone only when its runtime
field equals this shell's `${HOSTNAME:-}:${OSTYPE:-}`, `check_proc_gone` answers gone and the end-file
test passes. Every pid plant in the TOOL-aPiecewiseGrade-6 block goes through `write_pg6_pid`
(`tools/unattended/unattended.test.sh@6d3ce6ef:7978`), which calls
`tools/unattended/unattended.sh#write_dir_lock_pid`, and that stamps the local runtime
(`tools/unattended/unattended.sh@13a5efd0:2573`). So no plant can tell the clause from its absence.
The plant must therefore write its line directly: a helper that shares the predicate's runtime stamp
cannot grade that stamp (the charter's `[class]` rule).

The kind joins the loop at `tools/unattended/unattended.test.sh@6d3ce6ef:8063` as one more `case` arm:

```bash
foreign) printf '%s - otherhost:otheros\n' "$(read_pg6_dead_pid)" > "$pg6_l/pid.driver" ;;
```

The loop already plants the lock with a deadline 600 s (DERIVED) out and owner `w-x` through `write_pg6_lock`,
calls `measure_pg6_call`, and records the busy-line count and the owner. With the clause, the runtime
mismatch reads the record live, the deadline holds, and the call runs busy: `foreign:1:w-x`. With the
clause deleted, `check_proc_gone` answers gone for the dead pid (`tools/unattended/unattended.sh#check_proc_gone`
returns 0 when `kill -0` fails), the empty end field passes, the one record reads gone, and the lock
is broken. The call then records and gives the lock back, so the entry reads `foreign:0:`. The
expected string at `tools/unattended/unattended.test.sh@6d3ce6ef:8075` gains ` foreign:1:w-x` at its
end, and the `for` list gains `foreign` last.

The header comment at `tools/unattended/unattended.test.sh@6d3ce6ef:8024` through `:8027` gains the
runtime clause in its RED-first list, and the `# AC13:` comment at `:8060` says five plants. The block
sits in region three (`:7545`), inside the checker-present branch (`:7774`), so it runs in gov.

The AC1 probe is `$SCRATCH/pg7.sh`, removed after the pass. It extracts `read_proc_token`,
`check_proc_gone` and `check_dir_lock_stale` from `tools/unattended/unattended.sh` with
`sed -n "/^<name>() {/,/^}\$/p"`, the extraction the GH37 block uses at `:18117`, and writes a second
copy with the clause cut by `sed`. It plants a lock directory holding `until` 600 s (DERIVED) out and the
foreign `pid.driver` line above, then calls the predicate from each copy in its own `$( )` and prints
`foreign <verdict> cut <verdict>`, each `stale` on exit 0 and `held` otherwise. The author ran this
probe against HEAD at writing time and it printed `foreign held cut stale`.

What the arm does not check: a dead pid that the host reuses before the call reads live under the cut
too, because `check_proc_gone` with token `-` answers not gone for a live pid. The arm then stays
green under the break. AC12's dead plants carry the same exposure.

### Alternatives rejected

- A standalone plant after the loop with its own `same`. It repeats the lock plant, the call and the
  owner read the loop already does, and it adds one assertion and a floor raise to region three for
  nothing the loop kind cannot say. The review's own Fix, judged sound by its skeptic, is the loop kind.
- Adding a runtime parameter to `write_pg6_pid` or `write_dir_lock_pid`. The first is an option one
  caller uses; the second moves product code, which §3 rules out.

### Files touched (estimate)

`tools/unattended/unattended.test.sh`

## 5. Acceptance criteria

- **AC1** — When `bash "$SCRATCH/pg7.sh"` runs, it prints `foreign held cut stale`.
  Red when: `check_dir_lock_stale` reads a dead pid recorded by another runtime as gone, or the cut
  copy is not cut, so the probe cannot tell the clause from its absence.
  fixture: the probe and its lock directory are made by the pass under `$SCRATCH`; the tree holds
  neither today.
- **AC2** — When `sed -n '/# AC13: /,/each hold the lock/p' tools/unattended/unattended.test.sh`
  runs, its output holds exactly one line opening `foreign)` that carries `printf` and
  `otherhost:otheros` and not `write_pg6_pid`, and its last line ends `foreign:1:w-x"`.
  Red when: the foreign plant is written through `write_pg6_pid`, which stamps the local runtime, or
  the expected string omits the kind, so the loop never grades it.
- **AC3** — When `git diff -U0 3300b594c -- tools/unattended/unattended.test.sh | grep -cE '^[-+] *(hit|miss|same) '`
  runs, it prints 2, and the same diff piped to `grep -cE '^[-+]FLOOR_'` prints 0.
  Red when: the arm is written as a new assertion, so the count moves and a floor is owed, or a floor
  line moves with no assertion behind it.
  fixture: the diff base is the HEAD this spec was written at. The 2 is the loop's one `same` line,
  removed and re-added with the longer expected string.
  figure: PINNED, counted off the design above at writing time.

## 6. Gates

`harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `spec tokens (the pass's own spec)` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 · the `foreign` kind in the AC13 loop of the TOOL-aPiecewiseGrade-6 block, expected `foreign:1:w-x`. Staged RED at the close by deleting `[ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ] && ` from `check_dir_lock_stale` in `tools/unattended/unattended.sh`, which turns the entry into `foreign:0:`, and GREEN once it is restored · none, the kind adds no assertion

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but the
spec-token checker's `--spec` over this file and the memory hygiene gate.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-16 · initial draft.

## 9. Reuse audit

The seam extended is the AC13 loop of the TOOL-aPiecewiseGrade-6 block,
`tools/unattended/unattended.test.sh@6d3ce6ef:8063`, with its `write_pg6_lock`, `read_pg6_dead_pid` and
`measure_pg6_call` helpers. `tools/codebase-map/reuse_lookup.py` named no closer seam: its candidates
were record and field helpers elsewhere, `check_pid_alive` and `read_pid_image` in
`tools/unattended/lib-unattended.sh`, and `load_driver_conf`, none of which plants a lock record. The
handoff's reuse block names the input tracer and the per-spec cache, which this unit does not touch.

Recall terms used: `python tools/codebase-map/reuse_lookup.py "plant a pid record in a directory lock with a foreign runtime field in the driver suite"`
