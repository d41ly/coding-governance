# TOOL-aCarriedStop-9 — the routed commits leg's ceiling raised to 3540 s over its recorded contended readings, so the close's bar can finish it

**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-1 · base 8db6f4be · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md](../build/2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md) | journal | TOOL-aCarriedStop-1 TOOL-aCarriedStop-2 TOOL-aCarriedStop-3 |
| [2026-11-14-prompt-TOOL-aCarriedStop-9-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aCarriedStop-9-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar at `41c93c8b7` killed `routed commits name a specced unit` at its 760 s ceiling
twice, and every other leg was green. Run alone under load, the leg exits 0 in 1491.2 s in the
close's shape and in 1761.4 s in the landing push's shape. This unit records the larger reading
through the evidence tool's out-of-band route and raises the leg's ceiling to the margin rule's
minimum over it, so the close's bar can finish the leg and this build can land. The owner ordered it on 2026-11-14: "raise the routed-commits ceiling and land it".

## 2. Scope (IN)

- **S1** — The leg's row in `tools/run-gates/ceiling-evidence.txt` (line 119, 378.7 today) rises
  to R = 1761.4. It is written by `derive-ceilings.py --write --observed` with the `--how` text §4
  "The write" gives, in a scratch clone that holds no run record, and the file is copied back. No
  other row moves. Observed by AC2 and AC3.
- **S2** — The leg's `"ceiling"` in `tools/gate-legs.json` (line 1158, 760 today) becomes C = 3540,
  the value §4 "The value" derives from R. No other line of that file moves. Observed by AC1 and
  AC3.
- **S3** — The `last-audit` stamp of `memory/guides/SESSION-KICKOFF.md` (line 6) advances in the
  same commit as S2, because `tools/gate-legs.json` is one of its `watch:` paths (line 7).
  `last-body-change` stays. Observed by AC4.

## 3. Non-goals (OUT)

- `routed_commits.py` and how it grades. Its cost is a separate question, and the ceiling is a hang
  bound, not a cost verdict.
- Any other leg's ceiling, any other evidence row, any budget row in `selftest-budgets.txt`, and the
  pass-leg list. The leg is no pass leg (no `pass_leg` key at `tools/gate-legs.json@b62cb09b7611:1149`)
  and stays excluded from the derived list as `over-cap` at 378.7 and at 1761.4 alike, since the cap
  is 120 s (`tools/run-gates/pass_legs.py@a925dc42edce:58`, `:238`).
- `tools/run-gates/ceiling-margin.txt` and the run-gates runner.
- A new reading of the leg. R is the main loop's; the builder takes none, and none is taken on a
  quiet host, because the close's bar runs beside other sessions' work on this node.
- Any adopter release or kit version. The memory-tree descriptor row declares no ceiling
  (`tools/memory-tree/kit.toml@fdae4a7106f3:342-348`), and the evidence file ships withheld as
  project-owned (`tools/run-gates/kit.toml@ebe7850ef5c4:73`, `tools/govkit/registry.toml@75fd307ab092:741`).
- Any help page. No page under `help/` names this leg or its ceiling (grep over `help/`, 2026-11-14).
- Reconciling origin/main, which has since added legs to `tools/gate-legs.json`. That is the
  landing's work.

## 4. Design

### Evidence

Read at `5e2451f22`, the run branch tip. These files are byte-identical at the base `8db6f4be`.

- An in-band reading cannot size this ceiling. A failing row enters the record at its ceiling and
  never above it (`tools/run-gates/derive-ceilings.py@7d58ebdbff54:280-288`), so the close's two
  kills argue 760 at most. `--write --observed` is the route kept for this case (`:40-56`).
- `--write` re-derives every row from this worktree's run record before it applies `--observed`
  (`:504`, `:530-562`), and this worktree retains two runs under its `gate-run` directory. Written
  here, any admitted reading above its stored row would raise that row too. With no reading at all,
  `--observed` alone satisfies liveness (`:513`), every stored row is carried forward unchanged
  (`:552-562`), and only the observed row moves (`:576-588`).
- The observed reading must exceed the stored 378.7, or the write refuses and writes nothing
  (`:581-586`). It needs `GOV_NODE` (`:570-574`), and its `--how` text may hold no tab or newline
  (`:422-424`).
- The install-prefix leg grades this file, which sits under the tool root, and bans a kit segment
  followed by a file under any prefix (`tools/check-install-prefix.sh@401a476dfb69:48-53`). The
  `--how` text therefore names no path at all.
- `--check` passes a leg when `ceiling >= max + max(floor, fraction x max)` (`:668`, `:688`). The
  REACHED branch grades runner rows only (`:684`), and this row is out-of-band. The margin is a
  floor of 120 s and a fraction of 1.0 (`tools/run-gates/ceiling-margin.txt@171003169672:26`).
- The builder may run `--write` and `--report`. The role gate refuses a leg's argv compared word for
  word (`tools/hooks/scratch-guard.js@7c31933f6258:127-130`), and the leg runs `--check`
  (`tools/gate-legs.json@b62cb09b7611:2299-2309`). `gov-builder` is allowed `lexicon naming
  predicates` alone (`.claude/roles.json@2776be53ef32:125-131`). So `--check` is the main loop's.

### The reading

R is the largest reading on record for the leg, each taken by the main loop on node a. The first
three are the brief's; the fourth reached this writer from the main loop on 2026-11-14, after the
brief was written:

| At | Shape | Result | Host |
|---|---|---|---|
| `41c93c8b7`, the close's bar | WHOLE, in the pool and on retry | killed at 760 s twice | a spawn at 3.6x this clone's floor |
| `41c93c8b7`, alone | `GATE_PUSH_BASE=8db6f4be`, RANGE and WHOLE | rc 0, 957 s | not recorded |
| `5e2451f22`, alone, detached tree | `GATE_PUSH_BASE` unset, WHOLE | rc 0, 1491.2 s | 3 foreign gate processes at start, 26 at end |
| `5e2451f22`, same tree, right after | `GATE_PUSH_BASE=49358761`, RANGE and WHOLE | rc 0, 1761.4 s | 27 foreign gate processes at start, 9 at end |

The close's bar runs the leg with `GATE_PUSH_BASE` unset, so it grades WHOLE
(`tools/memory-tree/routed_commits.py#derive_commit_range`, `routed_commits.py@5e29003bb174:251-253`).
The landing push's bar sets it, and the leg then grades the range and WHOLE beside it (`:386`,
`:403`). The fourth reading is that shape, with the base origin main advertised by `ls-remote`.
Both 5e2451f22 readings are contended, because another session's full bar started in the primary
tree, and that is the load this node's close and push meet. R = 1761.4, the larger, PINNED,
measured by the main loop on node a.

### The write

The builder writes from a scratch clone outside the repository, at the commit the pass builds on:

```bash
git clone -q <repo root> <scratch> && git -C <scratch> checkout -q --detach <pass parent sha>
python <scratch>/tools/run-gates/derive-ceilings.py --report   # exits 2, DEAD PROBE: no reading
GOV_NODE=a python <scratch>/tools/run-gates/derive-ceilings.py --write \
  --observed "routed commits name a specced unit=1761.4" \
  --how "taken by the main loop on node a, the leg alone on a detached tree at 5e2451f2, read twice one after the other: GATE_PUSH_BASE unset so it graded WHOLE as the close's bar does, rc 0, 1491.2s, 3 foreign gate processes live at its start and 26 at its end, a full bar of another session having started in the primary tree; then GATE_PUSH_BASE=49358761, origin main from ls-remote, so it graded RANGE and WHOLE beside it as the landing push's bar does, rc 0, 1761.4s, 27 foreign gate processes live at its start and 9 at its end; both contended, the cost under the load the close and the push meet on this node; the larger governs; alone at 41c93c8b with GATE_PUSH_BASE=8db6f4be it read 957s, rc 0; killed at its 760 s ceiling twice under aCarriedStop's second close bar at 41c93c8b, a spawn at 3.6x this clone's floor; TOOL-aCarriedStop-9"
cp <scratch>/tools/run-gates/ceiling-evidence.txt tools/run-gates/ceiling-evidence.txt
```

The `--how` text is the one line inside the last pair of double quotes. It holds no tab, no slash
and no `$`. The summary line reads `wrote 131 row(s)` with `0 raised`, `1 raised by --observed` and
`0 held` (`:633-639`). Any other count means the clone held a reading, and the builder discards the
copy and starts from a fresh clone. The row's date column is the clone's HEAD commit date, which the
tool derives (`:527-528`).

### The value

For R of 120 s or more the fraction governs, so the ceiling must be at least 2R = 3522.8. The brief
rounds it up to a whole minute: C = 60 x ceil(3522.8 / 60) = 60 x 59 = 3540. It clears 2R by
17.2 s. DERIVED from R and the margin file. The unattended preflight's wall check compares
`GATE_WALL` with the largest ceiling (`tools/unattended/unattended.sh@95b8f8404cc3:7709-7715`), and
3540 sits under today's largest, 16040, so that check is unmoved.

The runner also reads an evidence row as a dispatch-order prior for a leg its timing cache does not
know (`tools/run-gates/run-gates.sh@bfc3ad495ef2:2880-2891`). The raise moves this leg earlier
there, as a scheduling hint that never changes a verdict (`:2822-2823`).

### What this does not check

- Whether 3540 s suffices under heavier load. R was taken with 27 foreign gate processes at its
  start, and a bar contended past 2R still kills the leg.
- The load R was taken under. An `--observed` row is admitted uncensused, and its `--how` text is the
  only record of the host (`tools/run-gates/derive-ceilings.py@7d58ebdbff54:49-52`).
- Whether R was taken as `--how` says. `--check` reads the tracked files alone (`:643-647`).
- Where the leg's time goes, or why it rose from 378.7 to 1761.4. That is the cost question the
  brief leaves out.

### Files touched (estimate)

- `tools/run-gates/ceiling-evidence.txt`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

All commands run from the worktree root in Git Bash. The first criterion is the main loop's, after
the pass commit. The other three are the builder's, with S1 to S3 staged and before the commit.

- **AC1** — When the main loop runs `python tools/run-gates/derive-ceilings.py --check` at the pass
  commit, it exits 0 and prints `ceiling-evidence: 131 of 174 leg(s) backed (13 of them
  out-of-band)`. Its stderr line of out-of-band ceilings names `routed commits name a specced unit
  1761.4s on node a`, followed by the `--how` text.
  Red when: the new row is read against the parent's ceiling of 760. The main loop runs the block
  below, and `--check` reads the manifest from `GATE_LEGS` first
  (`tools/run-gates/derive-ceilings.py@7d58ebdbff54:139-142`). It prints
  `CEILING-EVIDENCE FAILED — routed commits name a specced unit: ceiling 760s does not clear its evidenced maximum 1761.4s by the required max(120s, 1.0x) = 1761s (short by 2763s)`, names no
  other leg, and exits 1.
  permission: the `leg ceilings clear their evidenced maximum` leg runs this argv, and the role
  gate refuses it to `gov-builder`.
  figure: DERIVED. 131, 174 and 13 are counted from the two files at `5e2451f22`; the row is
  already out-of-band, so the count does not move. A merge of origin/main before the observation
  moves 174, and the count is then re-derived. 2763 is 1761.4 + 1761.4 − 760, rounded.

  ```bash
  TMP_LEGS=$(cygpath -m "$(mktemp)")
  git show HEAD^:tools/gate-legs.json > "$TMP_LEGS"
  GATE_LEGS="$TMP_LEGS" python tools/run-gates/derive-ceilings.py --check
  ```

- **AC2** — When `grep -n '^routed commits name a specced unit' tools/run-gates/ceiling-evidence.txt`
  runs, it prints line 119 with the fields `1761.4`, `1`, `a`, the clone's commit date and the
  `--how` text of §4 "The write", tab-separated.
  Red when: the write refused, so the row still reads `378.7`, or the `--how` text differs from §4.
- **AC3** — When `git diff --cached --numstat -- tools/gate-legs.json tools/run-gates/ceiling-evidence.txt`
  runs, it prints `1` added and `1` deleted for each file. `git diff --cached -U0 -- tools/gate-legs.json`
  shows one hunk at line 1158 whose added line is `"ceiling": 3540`, and
  `python -m json.tool tools/gate-legs.json > /dev/null` exits 0.
  Red when: the write ran in this worktree and its run record raised another row, so the evidence
  file shows more than one changed line; or a second ceiling was edited.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs, it prints no
  `MANIFEST check 5 FAILED` line and exits 0.
  Red when: S2 is staged without S3. It then prints `staged changes touch watched files:` naming
  `tools/gate-legs.json` (`skills/session-kickoff/manifest-check.sh@4d3d63c0fad1:1977-1987`) and
  exits 1.

## 6. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `leg ceilings clear their evidenced maximum` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `routed commits name a specced unit` · `spec tokens (a spec's own names resolve)`

`python tools/check-spec-tokens.py --legs-for` over the three files touched, run 2026-11-14 at
`5e2451f22`, names `run-gates gov canary`, `measure-legs selftest` and `policy fixtures` against
`tools/gate-legs.json`, and `recall floor` and `recall floor arms` against `memory/`. It names
`run-gates canary` under the broad `tools/` guard. The unguarded legs beside them read what this
unit changes: `leg ceilings clear their evidenced maximum` is AC1, `kickoff-manifest ratchet` is
AC4, `install-prefix (shipped surface)` grades the `--how` text, and `routed commits name a
specced unit` is the leg S2 bounds. The close's bar finishing that leg is the Goal's observation.
No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-14 · initial draft from the unit brief
  `2026-11-14-prompt-TOOL-aCarriedStop-9-brief`, grounded at `5e2451f22`, following
  `TOOL-dRankedPlan-83`, which raised this leg the same way. Two differences: the stored row exists,
  so the write replaces it rather than appending one; and the brief rounds C to a whole minute
  rather than to ten seconds. Before return it folds the main loop's fourth reading, sent by the
  coordinator after the brief: 1761.4 s in the landing push's shape, which becomes R and moves C
  from 3000 to 3540; the `--how` text names it beside the close-shaped 1491.2 s.

## 9. Reuse audit

The seam is the evidence tool's out-of-band route, `tools/run-gates/derive-ceilings.py#parse_observed`
and `tools/run-gates/derive-ceilings.py#cmd_write`, with the margin it reads and the leg's existing
row in `tools/gate-legs.json`. Nothing is built. The procedure reuses `TOOL-dRankedPlan-83`'s write
from a clean run record and `cf2c673f3`'s raise to the margin's minimum.
`python tools/codebase-map/reuse_lookup.py "record an out-of-band reading of a gate leg and raise its ceiling"`
ranked name stems only (`read`, `read_text`, `legs`, `leg`, `records`), none of which writes
evidence or a ceiling. The handoff named `write_chain_round`, `derive_chain_verdict` and
`check_chain_dispatch` in `tools/unattended/unattended.sh` as reuse; they write and read the
spec-audit chain record of units 1 to 3 and touch no ceiling, so no existing seam fits beyond the
tool above. The recall probe returned `TOOL-cMendedVintage-17` (the `--observed` ruling) first, then
`TOOL-dRankedPlan-83`, and `TOOL-dSafePassage-85`, which is why the `--how` text names no path.

Recall terms used: `python tools/memory-recall/query.py "how is a gate leg ceiling raised from a reading taken outside the runner" --terms "ceiling evidence observed how derive-ceilings margin headroom killed leg out-of-band raise routed commits"`
