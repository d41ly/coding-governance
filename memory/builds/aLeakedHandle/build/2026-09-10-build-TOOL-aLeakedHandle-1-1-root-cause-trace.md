# Root-cause trace — the two reds and the misreported kill

**Serves:** research TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3

Written before the specs, from live observation on node `a`, 2026-09-10. Every figure here was read
off a running process, a tracked file or `<git-dir>/gate-ledger.tsv`. Nothing is estimated.

## The bar this starts from

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, profile `capable`, width 8,
wall 21600 s. Result `gates RED — 2/104 legs failed`.

| leg | rc | seconds | ceiling |
|---|---|---|---|
| `memory-hygiene self-test` | 124 | 900.240 | 900 |
| `unattended kit gate` | 137 | 4168.392 | 16040 |

A second unattended run (`aHoistedPass`) held the box for the whole bar. That matters for the
hygiene leg and is recorded here rather than argued later.

## Subject 1 — the `unattended kit gate` deadlock

**Observed, not inferred.** Before the kill, `/proc` on the two surviving MSYS processes:

- parent `1987`, `bash tools/unattended/check-unattended.sh`, state `S`, fd 3 -> `pipe:[17051020180284]`
- child `28720`, forked subshell, state `S`, fd 1 -> that same pipe, and fd 3 AND fd 4 -> `pipe:[17059610126308]`

The child holds BOTH ends of its own pipe and no descendant is alive. EOF can never arrive, so the
parent's read never returns. Zero CPU, zero git processes, 63 minutes.

**The site, from a traced standalone repro.** `PS4`-instrumented `bash -x` of the same script hung at
`lib-unattended.sh:132`, inside `pass_commit`, on
`GIT log --reverse --format=%H%x09%s <anchor>..HEAD`. The construct is a heredoc carrying a command
substitution:

```
  done <<PASSCOMMITS
$(GIT log --reverse --format="%H%x09%s" "$_pa..$_pto" 2>/dev/null)
PASSCOMMITS
```

**The class is already recorded.** `memory/gotchas/bounded-through-a-pipe-is-unbounded.md`: `$( )`
reads until EOF, EOF arrives when the last inherited write end closes, and under MSYS that is not
reliably the direct child. The gotcha names two prior instances, one of them in this same file's
sibling. The comment directly above this construct says `A HEREDOC, NEVER A PIPE`, because a piped
`while` would run in a subshell and break the function's `return` — so the fix for one recorded
gotcha walked into another recorded gotcha, and neither is gated.

**A third instance was live during this trace.** The `aHoistedPass` worktree's own
`check-unattended.sh` showed the identical fd signature (pid `172747` reading fd 3, pid `179450`
holding fd 1 plus both ends of a second pipe) at the same moment. The class reproduces across
sessions and is not specific to one tree.

**Prior art that is NOT this.** `TOOL-aBoundedCeiling-9` is a different red on the same leg
(check 15, `landed-anchor`). `TOOL-aBoundedVerdict-10` is the older no-deadline hang, whose anchor
half landed.

## Subject 2 — the ceiling gate is green by absence

`memory-hygiene self-test` blew a 900 s ceiling. The leg that exists to catch an unsafe ceiling,
`leg ceilings clear their evidenced maximum` (`tools/run-gates/derive-ceilings.py --check`), passed
on the same bar.

**Why.** `derive-ceilings.py` builds evidence from `<git-dir>/gate-run/*/*.leg` and skips any row
whose verdict is not `ok`:

> Only `ok` rows count: a leg that FAILED may have failed fast, and a maximum taken over failures is
> a measurement of the failure and not of the work.

`tools/run-gates/ceiling-evidence.txt` therefore carries 37 rows against 104 legs.
`memory-hygiene self-test` has NO row, so its ceiling is held above nothing, and an unbacked ceiling
is reported rather than failed. A leg that has never passed inside the retained window can never
acquire evidence — which is exactly the population whose ceiling is most likely wrong.

**The reasoning is sound for the general case and wrong for one member of it.** A leg killed at its
ceiling with rc=124 ran for the full ceiling. Its seconds are a valid LOWER BOUND on the work, which
is the one thing a monotone maximum needs. Excluding it discards the only evidence that would ever
raise the floor.

**What this build will NOT do.** `aJoinedCanon` parked the "raise the ceiling or make the suite
cheaper" question for the owner on 2026-09-07, with the measurement: the suite grew 99 -> 121
assertion points, passes standalone in about 11 minutes, exceeds 900 s under a full concurrent bar.
That is still the owner's, and `TOOL-aPooledSweep-4` carries a second reading (1126 s serial, 972 s
pooled). This build fixes the evidence pipeline, not the number.

**Prior art on the trap of doing otherwise.** `TOOL-aReapedSpinner-23` was WITHDRAWN for inferring a
mis-declared ceiling from a contended bar, and `TOOL-dRetiredFork-40` records a ceiling misread in
both directions.

## Subject 3 — an external kill is reported as a full-ceiling timeout

`tools/run-gates/run-gates.sh:1479-1480`:

```
{ [ "$rc" = 124 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s)"
{ [ "$rc" = 137 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s, killed)"
```

`fired` is the leg's DECLARED CEILING. The rc=137 branch therefore prints the ceiling where the
elapsed time belongs. Observed: a leg killed by an operator at 4168.392 s was reported as
`(timed out after 16040s, killed)`. `<git-dir>/gate-ledger.tsv` holds the true 4168.392, so the
summary and the ledger disagree by a factor of four on the same run.

**rc=137 does not mean the ceiling fired.** It means SIGKILL, which an operator, an OOM killer or a
CI cancel produces just as readily as `timeout -k`. Only the rc=124 branch can honestly claim the
ceiling. The elapsed figure the runner already computes for the ledger is the number this line
should print.

**Why it is worth a unit.** A wrong number entering diagnosis is how `TOOL-dRetiredFork-40` was got
wrong twice, and this one makes an operator hunt a four-hour hang that never happened.

## Probe record, for the specs' section 10

- `python tools/codebase-map/reuse_lookup.py` on both subjects returned `unscanned layers: .sh`. All
  three subjects are shell, so the map probe is BLIND here and no "no seam fits" claim may rest on
  it. Recorded per `memory/gotchas/` rather than paraphrased as a miss.
- `python tools/memory-recall/query.py`, terms
  `unattended leg ceiling timeout hang pipe subshell deadlock ls-remote bound spawn wall` and
  `hygiene selftest ceiling staged guard checker fixture slow leg cost verdict wall` and
  `run-gates leg rc timeout killed ceiling ledger summary verdict report elapsed fired sigkill`.
  Returns are cited inline above.
- `python tools/memory-tree/gotchas.py --for-paths` over the three touched files selected 23
  classes, `bounded-through-a-pipe-is-unbounded` among them.
