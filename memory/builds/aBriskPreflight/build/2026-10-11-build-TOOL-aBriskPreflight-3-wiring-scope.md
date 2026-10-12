# TOOL-aBriskPreflight-3 — preflight's wiring scope, measured: the whole check stays

**Serves:** research TOOL-aBriskPreflight-3

Node `a`, 2026-10-11, the build pass. Spec rev-1. The tree measured is the run tip `2a64d49be`,
which carries units 1, 2, 4, 5 and 6 CLOSED; units 1 and 2 are the two that touch
`tools/check-wiring.sh`, and no unit was parked. The instrument is
`2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py`, which loads the build's counter,
`2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`, by path and restates none of it.

## The decision

`WIRING_CHECK` keeps the whole `--check` (C1). C1 and C2 both keep every verdict preflight reads;
C2 needs a new flag on `check-wiring.sh` and a new accepted token in the driver, a new public surface
on two shipped kits, which is M3's veto 2 under `may: none`. C1 is the only option surviving the
vetoes (spec §7 F2). C2 goes to the owner priced, as `TOOL-aBriskPreflight-8` in this build's
`BACKLOG.md`; the unattended kit's own hook wiring, which no wiring arm grades, is `TOOL-aBriskPreflight-9`.
No commit of this unit touches `tools/`, `.githooks/` or `.unattended.conf`.

## The trees and their hosts

| Run | Tree | Script | Local heads | Host line |
|---|---|---|---|---|
| `cw-base-traced` | `%TEMP%/bp/A` at `b726385f2` | blob at BASE `271a90045` (identical at `b726385f2`) | 38, the spec's reading | no line of its own; 20 to 29 min later `pf-real-base` spawn5=3.97 fork=0.08 paged=17319MB nonpaged=6280MB, and `hook-base` spawn5=3.73 (`…-1-runs.log`) |
| `cw-u12-traced` | `%TEMP%/bp/A`, detached checkout of `2a64d49be` | the tree's own `tools/check-wiring.sh` | 41 | `host label=cw-u12-traced at=14:00:06Z spawn5=9.45 fork=0.56 paged=19130MB nonpaged=6379MB committed=52931MB cpu=33%` |

One tree for both runs, wired, so the hooks, merge and skill arms read the same wiring. Three more
local heads exist now than at BASE; both straggler windows ran into the inventory's own `timeout 60`
(`note … exited 124` in both outputs), so the straggler windows compare as "the bound", not as a
walk of a given ref count. The host was about 2.4 times slower per spawn at the after run (spawn5
9.45 s against 3.7 to 4.0 s), so walls do not compare across the two runs; forks and execs do.

## The verdict probe (AC2), on the after tree

`awk '/^[a-z_]+\(\) *\{/{fn=$1} /unwired=\$\(\(unwired\+1\)\)/{print fn, NR}' tools/check-wiring.sh` at `2a64d49be`:

```
check_hook_modes() 721
check_hooks() 749
check_hooks() 763
check_hooks() 767
check_agentcap() 862
check_agentcap() 870
check_agentcap() 882
check_scratch_guard() 918
check_scratch_guard() 923
check_scratch_guard() 929
check_scratch_guard() 941
check_scratch_guard() 952
check_recall_opened() 982
check_recall_opened() 987
check_recall_opened() 993
check_recall_opened() 1006
check_recall_opened() 1009
check_card() 1044
check_card() 1049
check_card() 1055
check_card() 1067
check_card() 1079
check_eol() 1165
check_merge_rows() 1223
check_merge_rows() 1283
check_merge_rows() 1318
check_merge_rows() 1344
check_merge_rows() 1350
check_merge_rows() 1392
check_merge_rows() 1404
check_merge_rows() 1408
check_merge_rows() 1416
check_merge_ours() 1441
check_merge_ours() 1445
check_merge_ours() 1453
check_ssh_keepalive() 1479
check_ssh_keepalive() 1484
check_ssh_keepalive() 1545
check_ssh_keepalive() 1549
check_routed() 1591
check_routed() 1631
check_routed() 1656
check_skill_install() 1686
check_skill_install() 1724
check_skill_install() 1770
check_skill_install() 1776
```

The one `check_eol` site, `:1165`, sits inside the branch opened at `:1157`,
`if [ "$DO_FIX" = 1 ] && [ "$MODE" != session ]`, which returns at `:1172`, so it runs under `--fix`
only.
`check_backlog_stragglers` prints none. The ten other arms of the run list each print at least one
site; `check_hook_modes` is a helper `check_hooks` calls, not a run-list arm. The probe printed sites
in ten arms, so it is live and a site-free arm is a reading, not a dead probe.

## The staged breaks (AC3), on the after tree

Every break was written and undone by byte rewrites from saved bytes, never by a checkout, and was
preceded by a clean run of the same tree that exited 0 (`cw-u12-traced`, rc 0, no `UNWIRED` line).

| Run | Break | rc | Lines that decide it | Wall |
|---|---|---|---|---|
| `ac3-crlf` | `.claude/skills/drift-audit/SKILL.md` rewritten to CRLF in the working copy | 0 | `note     eol       — .claude/skills/drift-audit/SKILL.md holds CRLF despite its eol=lf pin; …`, and no `UNWIRED` line | 319.8 s |
| `ac3-matcher` | the `Workflow\|Agent` matcher in `.claude/settings.json` narrowed to `Workflow`, the stale value the agent-cap arm names | 1 | `UNWIRED  agent-cap — the hook is wired under matcher 'Workflow', not 'Workflow\|Agent'; …`, the one `UNWIRED` line | 281.6 s |
| `ac3-restored` | none, both files restored | 0 | no `UNWIRED` line; every line opens with the same status word as the clean run's | 285.0 s |

Against the clean run's output, each break changed exactly one line: the eol line from `ok` to
`note`, and the agent-cap line from `ok` to `UNWIRED`. The CRLF restore was confirmed by a byte count of CR in the file (0, as in the saved original) and
the settings restore by `cmp` against the saved bytes. An `od -c | grep` count of CR read 3 both with
the break in and after the restore, so it could not tell the two apart: the `msys-grep-counts-cr-on-every-line`
class, and the reason this record cites the byte count and the arm's own `note` instead.

## The windows

`python 2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py <trace> <check-wiring.sh>`, wall in
seconds from each window's first row to the next window's first row.

| Window | BASE wall | BASE forks | BASE execs | after wall | after forks | after execs |
|---|---|---|---|---|---|---|
| `(prelude)` | 11.6 | 10 | 7 | 31.1 | 14 | 11 |
| `check_hooks` | 37.6 | 17 | 20 | 62.7 | 19 | 22 |
| `check_agentcap` | 24.0 | 23 | 15 | 14.7 | 10 | 4 |
| `check_scratch_guard` | 47.6 | 66 | 43 | 24.7 | 19 | 8 |
| `check_recall_opened` | 27.7 | 33 | 21 | 13.6 | 11 | 4 |
| `check_card` | 40.5 | 56 | 36 | 32.5 | 19 | 8 |
| `check_routed` | 32.8 | 43 | 30 | 42.2 | 25 | 14 |
| `check_merge_rows` | 198.5 | 42 | 154 | 48.0 | 21 | 14 |
| `check_merge_ours` | 3.1 | 4 | 4 | 5.1 | 4 | 4 |
| `check_ssh_keepalive` | 9.5 | 6 | 4 | 15.9 | 6 | 4 |
| `check_eol` | 42.7 | 31 | 33 | 40.3 | 22 | 25 |
| `check_skill_install` | 20.6 | 18 | 18 | 34.5 | 18 | 18 |
| `check_backlog_stragglers` | 71.5 | 6 | 2 | 69.0 | 5 | 1 |
| TOTAL | 567.6 | 355 | 387 | 434.5 | 193 | 137 |

The prelude and `check_hooks` grew by six forks between them because unit 2 moved the settings
file's one read into the parent, ahead of the arms that used to read it each; the arms after them
shrank by more.

## The candidates

| Candidate | Arms it runs | BASE wall / forks / execs | `cw-u12-traced` wall / forks / execs | What it stops catching |
|---|---|---|---|---|
| C1 | the whole run list, twelve arms | 567.6 / 355 / 387 | 434.5 / 193 / 137 | nothing |
| C2 | every arm but `check_eol` and `check_backlog_stragglers` | 453.5 / 318 / 352 | 325.1 / 166 / 111 | no verdict preflight reads; on a refusal, the indented output loses those two arms' `ok`, `skip` and `note` lines. Their `UNWIRED` lines: none under `--check` (the eol arm's one is `--fix` only, the straggler arm has none) |
| C3 | the prelude and `check_hooks` | 49.2 / 27 / 27 | 93.8 / 33 / 33 | every `UNWIRED` line of nine arms: `UNWIRED  agent-cap`, `scratch`, `recall`, `card`, `routed`, `merge` (rows), `merge` (ours), `ssh` and `skill`; AC3's matcher break is the positive case |
| C4 | none of this script's arms | — | — | every verdict the script prints; the hooks it names are graded elsewhere |

C1 minus C2, the price of keeping the whole check: 114.2 s, 37 forks, 35 execs at BASE; 109.4 s,
27 forks, 26 execs at `cw-u12-traced`. The straggler window is wall with almost no traced spawn: its
cost is `migrate_backlog.py`'s own git calls, which the counter cannot see, and it ran to its own
60 s bound in both runs.

**C4, with its evidence.** The prompt's example is "the stop-guard, gate-guard, stall-recorder and
resume-tick wiring". `grep -c 'stop-guard\|gate-guard\|stall-recorder\|resume-tick' tools/check-wiring.sh`
prints 0 at `2a64d49be`. Their wiring is graded by the fragment loop of
`tools/unattended/adopt-unattended.sh --check` (`:642`, "the <name> hook is UNWIRED"), which runs as
the merge-bar leg `unattended skill wiring` only. So C4 selects no arm of this script; it is filed as
`TOOL-aBriskPreflight-9`, not taken.

## Result rows

| Criterion | Observation |
|---|---|
| AC1 | the instrument over `cw-base-traced` with the BASE `check-wiring.sh` printed 12 run-list rows plus `(prelude)`, rc 0, TOTAL 567.6 s / 355 / 387, equal to the counter's first line `trace rows 2040, wall 567.6s, forks 355, execs 387`. A scratch copy with one blank line inserted above its run list: rc 1, naming `check-wiring.sh:1754` and `check_hooks` as a run-list line that "matched 0 rows of the first process, not 1 -- the trace was not taken from this script" |
| AC2 | the probe output above: the eol site is `--fix`-only, the straggler arm has none, ten arms print sites |
| AC3 | the CRLF break printed the `note     eol` line naming `.claude/skills/drift-audit/SKILL.md`, no `UNWIRED` line, rc 0; the `Workflow` matcher break printed `UNWIRED  agent-cap`, rc 1; restored, rc 0 (the staged-breaks table above) |
| AC4 | the counter over `cw-u12-traced` with the after tree's `check-wiring.sh`: `trace rows 3510, wall 434.5s, forks 193, execs 137`, equal to C1's row above; C2, C3, the BASE rows and both host lines stand beside it |
| AC5 | observed at the commit: `git show --name-only --format= HEAD` lists nothing under `tools/` or `.githooks/` and not `.unattended.conf`; `WIRING_CHECK="bash tools/check-wiring.sh --check"` |
| AC6 | `TOOL-aBriskPreflight-8` (the selector, priced from this record) and `TOOL-aBriskPreflight-9` (the kit's hook wiring and `adopt-unattended.sh`), both in this build's `BACKLOG.md` with a `SEV` and a `KEEP` row |
