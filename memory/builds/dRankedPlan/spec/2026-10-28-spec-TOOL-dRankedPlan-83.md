# TOOL-dRankedPlan-83 — the routed commits leg's ceiling covers this run's close, sized through `derive-ceilings.py --observed` from the main loop's reading of the leg alone

**Status:** INPROGRESS · rev-1 · 2026-10-28 · node a · Tier-1 · base 922d6b94 · streams tooling

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dRankedPlan-83-deviation-831.md](../build/2026-10-28-build-TOOL-dRankedPlan-83-deviation-831.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dRankedPlan-83-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-83-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dRankedPlan-83-2-builder.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-83-2-builder.md) | journal | — |
| [2026-10-28-prompt-TOOL-dRankedPlan-83-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-83-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dRankedPlan-82 raised the spec tokens leg to 830 s, and that leg went green. The close's bar at
`9c135e17d` then redded only `routed commits name a specced unit`. It timed out at its 300 s ceiling
twice, in the pool and on its serial retry, and was attributed CONTENDED
(`memory/builds/dRankedPlan/RUN.md:21`, `:372`). The leg is healthy and slow. Its deviation join is
armed and joins every chain build's records over the whole history, and its spawns grow with the
chain-build specs' revisions (`tools/memory-tree/routed_commits.py:45-51`). This unit raises that one
leg's ceiling from evidence. It uses the out-of-band route `tools/run-gates/derive-ceilings.py` keeps
for a leg killed at its own ceiling, so the close's bar can go green. The owner ordered it at the
second hand-off `owner-decision` of `5232949ca`
(`memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-1-owner-review-until-no-high.md:45-49`).
It is built in this run, not carried forward to the build run, as that answer directs.

## 2. Scope (IN)

- **S1** — The ceiling of `routed commits name a specced unit` in `tools/gate-legs.json` (`:1104`,
  300 today) becomes C = 710. That is the value §4 "The value" derives from the main loop's reading
  R = 354.0. `tools/run-gates/ceiling-evidence.txt` holds no row for this leg today, and it gains one
  at R. The row is written by `derive-ceilings.py --write --observed` with the `--how` text §4 gives,
  so the row's source column carries how R was taken. The new row sorts in at line 114, between
  `review-protocol parity (kit vs dogfood)` and `row-grammar selftest`. No other row of either file
  moves. Observed by AC1, AC2 and AC4.
- **S2** — The `last-audit` stamp of `memory/guides/SESSION-KICKOFF.md` (`:5`) advances by the stamp
  rule at `:23`, in the same commit as S1, because `tools/gate-legs.json` is a `watch:` path (`:6`).
  `last-body-change` (`:8`) stays. Observed by AC3.

## 3. Non-goals (OUT)

- `tools/memory-tree/routed_commits.py`, its deviation join and every other checker. The join's
  whole-history half runs at every base (`tools/memory-tree/routed_commits.py:258-260`,
  `tools/memory-tree/deviation_join.py:816-817`). No ask names a cure for its cost.
- The four `DESIGN_*` keys of `.memory-tree.conf` (`:1020-1023`), which arm the join.
- Any other leg's ceiling, and `tools/run-gates/ceiling-margin.txt`.
- The run-gates runner, and the census of foreign gate work it stamps on each `.leg` row.
- Any adopter release. The leg ships in the memory-tree kit, and its descriptor row declares no
  ceiling (`tools/memory-tree/kit.toml:333-339`). A ceiling reaches a target only where the
  descriptor declares one (`tools/govkit/govkit.py:4448-4455`). The descriptor-to-manifest ceiling
  parity compares a declared ceiling alone (`:2895-2901`), so no shipped manifest carries this value.
- Any help page. `help/measure-legs.md:73` documents the `--observed` route and names no leg's
  value.
- Any §B claim of the kickoff manifest. §B names no routed commits leg and no ceiling, so S2
  re-stamps with no body change.

## 4. Design

### Evidence

- The close's bar at `9c135e17d` killed the leg at 300 s twice, in the pool and on its serial retry,
  attributed CONTENDED. Every other leg was green there (`RUN.md:372`).
- `RUN.md:372` records 358 s for the same leg at dWellOiledMachine's close. That build's own
  evidence text reads the 358 s as taken beside the spec tokens leg, not alone.
- The join is armed at every commit this run reads: the conf declares all four `DESIGN_*` keys at
  `9c135e17d`, at `922d6b94d` and at origin/main `1a61f21a2`. When armed, the join reads every
  chain-build spec's revisions over the whole history, at any base. Unlike unit 82's packet join, its
  cost does not depend on a chain run being live.
- An in-band reading cannot size this ceiling. A failing row enters the record at its ceiling and
  never above it (`tools/run-gates/derive-ceilings.py:219-225`, `:286-288`), so the close's two
  kills can argue no more than 300 s. The `--observed` route exists for exactly this case
  (`tools/run-gates/derive-ceilings.py:40-56`, `TOOL-cMendedVintage-17`).

### The reading

R is the main loop's, and the builder takes no reading and runs no gate leg. The role-gate arm of
`tools/hooks/scratch-guard.js` (`checkRoleGate`, `:1421`) refuses every leg's argv to a role agent
except the legs its allowlist names. The allowlist of `gov-builder` in `.claude/roles.json`
(`:11-18`) names `lexicon naming predicates` alone, as unit 82's §4 found live.

The main loop took three readings of the leg's argv (`tools/gate-legs.json:1096-1099`) on node a,
each by `time`. The first two were push-shaped, using `GATE_PUSH_BASE=1a61f21a2`, the prepared
merge's first parent:

1. **At `9c135e17d`, after the close.** Exit 0, 354.0 s. The range held 37 commits past that base.
   The census found another session's two staged hygiene checks running as the reading started.
2. **At `922d6b94d`.** Exit 0, `real 4m55.499s`, which is 295.5 s. The range held 39 commits past
   that base, and the reading ran from 03:44:56 to 03:49:52. Another worktree's `--dispatch` ran its
   `tools/check-spec-tokens.py` across part of it.

The main loop then took a third reading at `922d6b94d` in the close's shape, with `GATE_PUSH_BASE`
unset, by `env -u GATE_PUSH_BASE python3 tools/memory-tree/routed_commits.py` under `time` on node
a:

3. **At `922d6b94d`, close-shaped.** Exit 0, `real 4m35.977s`, which is 276.0 s, from 04:01:45 to
   04:06:21. Before the reading, the census found another worktree's `tools/check-spec-tokens.py`,
   started at 04:01:28, and its dSafePassage dispatch running. After the reading, that spec tokens
   run had ended.

All three censuses found the idle orphan `run-gates.sh` of `unattended-dgroundrules-0e6f4a` (pid 10907,
from Oct 23), the one unit 82 found, and left it alone. The evidence row records a maximum, so R is
the largest reading, written to one decimal, the precision the evidence file writes
(`tools/run-gates/derive-ceilings.py:627`): R = 354.0. The close-shaped 276.0 s sits below R.
Contention can only have lengthened any of the three readings. It therefore errs toward a higher C and never a lower one, and the `--how` text records it.

The close's bar runs the leg with `GATE_PUSH_BASE` unset. Only the pre-push hook exports it
(`.githooks/pre-push:2326`). Unset, the leg grades WHOLE alone
(`tools/memory-tree/routed_commits.py:216-218`). With a base set, it grades the RANGE and WHOLE
beside it (`:258-260`). Each population gets its own log pass (`:264-266`), and the join's
whole-history measure runs once in both shapes (`tools/memory-tree/deviation_join.py:816-817`). The
readings' shape therefore does the close's work and more, so R bounds the close's work as well as
the landing push's.

### The write

The builder writes the evidence row first, from a run record holding no admitted reading, so no
other row moves. `python tools/run-gates/derive-ceilings.py --report` in this worktree either prints
`# 0 leg(s) with a reading` or exits 2 with `DEAD PROBE` (`:435-441`). Either answer means no
admitted reading. If it prints any other count, the builder writes from a scratch clone of the
build commit and copies back only `tools/run-gates/ceiling-evidence.txt`, as `9c756ce7d` did. The
write names node a, where R was taken. The tool refuses to default the node (`:570-574`):

```
GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --observed "routed commits name a specced unit=354.0" --how "taken by the main loop, the leg alone on node a with GATE_PUSH_BASE=1a61f21a2, its deviation join armed, read twice with that base: at 9c135e17 after dRankedPlan's close, 37 commits past that base, rc 0, real 354.0s, another session's two staged hygiene checks running as it started; at 922d6b94, 39 commits past it, rc 0, real 295.5s, another worktree's dispatch running its check-spec-tokens.py across part of it; and a close-shaped reading at 922d6b94 with GATE_PUSH_BASE unset, rc 0, real 276.0s; all three censuses found the idle orphan run-gates.sh of unattended-dgroundrules-0e6f4a, pid 10907 from Oct 23; the largest governs; killed at its 300 s ceiling under dRankedPlan's close bar at 9c135e17, in the pool and on its serial retry"
```

The `--how` text is the one line inside the last pair of double quotes. It holds no tab
(`:422-424`).

The leg has no row today, so no stored maximum exists for it and the monotone refusal at
`:581-586` cannot fire. The write appends the row (`:587-588`). It re-prints the 119 existing rows
unchanged, sorted by name (`:625-627`), and the new row lands at line 114. The summary line reads
`derive-ceilings: wrote 120 row(s) to ceiling-evidence.txt (0 raised, 0 lowered by --reset, 0 dropped by --reset, 0 killed reading(s) removed by --reset, 1 raised by --observed, 0 held at a previous maximum; set aside`
followed by the record's set-aside counts (`:633-639`). The `0 held` holds because no admitted
reading enters the loop at `:530`. A `raised` or `held` count above 0, or a row count other than
120, means the run record held an admitted reading after all. The builder then restores the file
and writes from the clone.

### The value

`--check` passes a leg when its ceiling is at least its evidenced maximum plus
`max(floor, fraction × max)` (`tools/run-gates/derive-ceilings.py:663`, `:683`). The margin file
declares a floor of 120 s and a fraction of 1.0 (`tools/run-gates/ceiling-margin.txt:26`). For any R
of 120 s or more the fraction half governs, so the ceiling must be at least 2R. Every ceiling in
`tools/gate-legs.json` at `922d6b94` is a multiple of 10, across 60 distinct values. C is therefore
the least multiple of 10 at or above 2R, which is 10 × ⌈R / 5⌉. From R = 354.0 that is
C = 10 × ⌈354.0 / 5⌉ = 10 × 71 = 710, which clears 2R = 708 by 2 s. The out-of-band row falls to
the headroom branch, never the REACHED one, which grades runner rows alone (`:679`).

### When the ceiling comes back down

No ask names a cure for the join's cost, and no reading splits the leg's time between its own
grading and the join. The ceiling comes down only once a reading of the leg alone supports a lower
bound. Lowering takes `--write --reset` with `--observed` for this leg, from a record holding no
admitted reading, as `9c756ce7d` lowered the foreign-prefix parity leg. The ceiling then falls to
the margin's value for that reading. Until then every bar and every push in gov pays the join's
cost under this ceiling.

### What this does not check

- Where the leg's time goes. The raise bounds a hang and leaves the cost where it is. The code
  states that the armed join's spawns grow with the chain-build specs' revisions
  (`tools/memory-tree/routed_commits.py:48-51`, `:343-345`). Both shapes run its whole-history half
  (`tools/memory-tree/deviation_join.py:816-817`), and nothing here measures how much of R that half
  takes. The cost grows with the chain's spec revisions, so a later close can outrun C the way this
  one outran 300.
- The close's own shape, measured. Two readings set `GATE_PUSH_BASE`, and the close's bar runs
  WHOLE alone. §4 "The reading" argues from the code that the push shape does more work. The one
  WHOLE reading, 276.0 s, sat below R. Wall time under a different load can still run the other
  way.
- The leg's contended duration. Only solo readings are measured. The margin's fraction is the whole
  of the headroom above them, and a bar contended past 2R still kills the leg.
- The load R was taken under. An `--observed` row is admitted uncensused, and its `--how` text is
  the only record of the host (`tools/run-gates/derive-ceilings.py:49-52`). On Windows `ps -ef`
  sees only processes an MSYS shell spawned.
- Whether R was taken as `--how` says. `--check` reads the two tracked files alone (`:643-647`).

### Rollout

This unit builds in this run, once rev-1 is committed. It carries no `order` verb, as unit 82
explains: the dispatch order gate reads the DEFERRED units as non-terminal, and a unit with no
`order` verb is unordered and blocks nothing.

1. **Before the dispatch.** The main loop appends this unit's `## route` to the session card.
2. **The builder.** It sets this spec's status from DEFERRED to INPROGRESS before its first write,
   because `tools/` is under `ROUTED_PATHS`. It runs `--report` and the write of "The write", sets
   the ceiling to 710, and applies S2. S2's stamp is `last-audit: <date -Iseconds> @ <git rev-parse HEAD>`,
   both taken when the builder stages. It observes AC3 and AC4 on its staged change and commits. The
   commit message carries a manifest delta line in the shape of `026bc5055`'s: none to §B, and the
   `last-audit` re-stamped for the watched `tools/gate-legs.json`, whose only change is one leg's
   ceiling. It also states R = 354.0 as the main loop's reading, C = 710 and node a.
3. **After the pass commit.** The main loop observes AC1's red and then its green, and AC2's red. It
   then re-renders the build README, re-prepares onto origin/main, re-runs the close and runs the
   bar there.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

All commands run from the repository root of the worktree, in Git Bash. R = 354.0 is the main
loop's reading and C = 710 is the value §4 derives from it. AC1 and AC2 are the main loop's, because
the role gate refuses both legs' argv to `gov-builder` (§4 "The reading"). AC3 and AC4 are the
builder's, run with S1 and S2 applied and staged, before the unit's commit.

- **AC1** — When the main loop runs `python tools/run-gates/derive-ceilings.py --check` at the pass commit, after it lands on the run's branch, it exits 0 and prints `ceiling-evidence: 120 of 144 leg(s) backed (4 of them out-of-band)`. Its stderr names `routed commits name a specced unit` among the ceilings backed by a reading taken outside the runner, as `354.0s on node a` followed by the `--how` text.
  Red when: the committed evidence row is read against the ceiling of 300 that the pass commit's parent holds. The main loop observes this after the pass commit and before the green, with HEAD at the pass commit and no write under `tools/`. `--check` reads the leg manifest from `GATE_LEGS` before the sibling one (`tools/run-gates/derive-ceilings.py:139-142`), and reads nothing else of this change but the evidence file and the margin (`:643-647`). The main loop runs `TMP_LEGS=$(cygpath -m "$(mktemp)")`, then `git show HEAD^:tools/gate-legs.json > "$TMP_LEGS"`, then `GATE_LEGS="$TMP_LEGS" python tools/run-gates/derive-ceilings.py --check`. It prints `CEILING-EVIDENCE FAILED — routed commits name a specced unit: ceiling 300s does not clear its evidenced maximum 354.0s by the required max(120s, 1.0x) = 354s (short by 408s)` and exits 1. It names no other leg, since the parent's manifest differs from the pass's in this one ceiling.
  permission: the `leg ceilings clear their evidenced maximum` leg runs this argv, and the role gate refuses it to `gov-builder`.
  figure: DERIVED. The shortfall is re-derived from the row at check time (`tools/run-gates/derive-ceilings.py:683-686`): 354.0 + 354 − 300 = 408. The counts 120 of 144 and 4 out-of-band are derived from the two files at `922d6b94`, which hold 144 legs, 119 rows and 3 out-of-band rows, plus this unit's one row.
- **AC2** — Before the builder's dispatch, the main loop ran `GATE_PUSH_BASE=1a61f21a2 python tools/memory-tree/routed_commits.py` alone under `time` on node a at `9c135e17d`. It exited 0 with its deviation join armed, and its 354.0 s sits under C = 710 by 356 s, more than the margin's 120 s floor. Its reading at `922d6b94d`, 295.5 s and exit 0, sits under C by 414.5 s. Those readings are §4 "The reading", and they are this criterion's green.
  Red when: no base where the range holds few commits gives one. At any resolvable base the leg grades the whole history beside the range (`tools/memory-tree/routed_commits.py:258-260`), and the join's whole-history half runs regardless (`tools/memory-tree/deviation_join.py:816-817`). The two readings bear this out: the 39-commit range read faster than the 37-commit one. The red is therefore the leg with its join off. After the pass commit and before the close, the main loop makes a local full-history clone of the pass commit, since the leg refuses a shallow one (`tools/memory-tree/routed_commits.py:246-248`). It sets the four `DESIGN_*` values of that clone's `.memory-tree.conf` blank and runs the same command there. The output then holds the line `routed-commits: deviation join off — DESIGN_RECORD, DESIGN_BASELINE, DESIGN_VIEW, DESIGN_NODES are blank in .memory-tree.conf, so the join reads no history` and no `routed-commits: deviation: WHOLE · ` line. That reading leaves out the cost this ceiling bounds, so it sizes nothing here.
  permission: the `routed commits name a specced unit` leg runs this argv, and the role gate refuses it to `gov-builder`.
  figure: PINNED. R = 354.0 is the larger of the main loop's two readings, at `9c135e17d` and `922d6b94d`. The floor is `tools/run-gates/ceiling-margin.txt:26`.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs, it prints no `MANIFEST check 5 FAILED` line and exits 0.
  Red when: S1 is staged without S2. Then it prints `MANIFEST check 5 FAILED — staged changes touch watched files:` with the indented path `tools/gate-legs.json`, and exits 1.
- **AC4** — When `git diff --cached --numstat -- tools/gate-legs.json tools/run-gates/ceiling-evidence.txt` runs, it prints `1` added and `1` deleted for `tools/gate-legs.json`, and `1` added and `0` deleted for `tools/run-gates/ceiling-evidence.txt`. Then `git diff --cached -U0 -- tools/gate-legs.json` shows one hunk, at line 1104, whose added line is the `"ceiling":` key with C. And `git diff --cached -U0 -- tools/run-gates/ceiling-evidence.txt` shows one hunk adding line 114, a row opening `routed commits name a specced unit` with R.
  Red when: a second leg's ceiling is also edited, or the write moved another evidence row. Then the `tools/gate-legs.json` line counts read 2 added and 2 deleted, or the evidence file shows a deleted line.

## 6. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `leg ceilings clear their evidenced maximum` · `kickoff-manifest ratchet` · `routed commits name a specced unit` · `spec tokens (a spec's own names resolve)`

At `922d6b94`, `python tools/check-spec-tokens.py --legs-for` over the three files touched names the
same six guarded legs it named for unit 82, under the broad floor of 5 (`:362`). The guards are
unchanged since unit 82's base `ef0ac519`, because only unit 82's ceiling lines differ under
`tools/` since then. `tools/gate-legs.json` trips `run-gates gov canary`, `measure-legs selftest`
and `policy fixtures` through its own path. `--legs-for` prints `run-gates canary` against the broad
`tools/`, but its row also carries the exact `tools/gate-legs.json` guard
(`tools/gate-legs.json:1146-1150`). `memory/guides/SESSION-KICKOFF.md` trips `recall floor` and
`recall floor arms` through `memory/`. `tools/run-gates/ceiling-evidence.txt` trips only broad
guards.

The unguarded legs named beside them read what this unit changes:

- `leg ceilings clear their evidenced maximum` runs `derive-ceilings.py --check`
  (`tools/gate-legs.json:1846-1855`), observed by AC1.
- `kickoff-manifest ratchet` reads S2, observed by AC3 in its staged form.
- `routed commits name a specced unit` is the leg S1 bounds, observed by AC2.
- `spec tokens (a spec's own names resolve)` reads this spec while it is INPROGRESS.

The bar itself runs at the close. No arm is added or moved. No floor or pinned count moves, and the
one ceiling that moves is S1's.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-28 · initial draft from this unit's spec brief, grounded at `922d6b94`. It follows
  `TOOL-dRankedPlan-82` rev-2 section for section, along with its pass `026bc5055`.
  `tools/run-gates/derive-ceilings.py` was read whole at this base. Three things differ from unit 82.
  First, this leg had no evidence row, so the write appends one and the evidence diff is one added
  line. Second, the leg ships in the memory-tree kit, and its descriptor declares no ceiling, so no
  adopter manifest moves. Third, AC2 has no red at a few-commit base, for the reason AC2 gives, so
  its red is the join turned off in a clone. Three follow-ups for the main loop, none of them a fork.
  First, `TOOL-dWellOiledMachine-127` raises this same leg to 760. It is built at `09d6004c2` on
  `branch/unattended-dwelloiledmachine-b9baed` and is not on origin/main `57bc3b918`. Its row of
  378.7 sits at the same line 114, taken with `GATE_PUSH_BASE` unset, which is the close's shape.
  Its push-shaped reading at the same commit was 322.1 s. Whichever build lands second meets a
  conflict on `tools/gate-legs.json:1104` and on that row. The larger row and its ceiling, 378.7 and
  760, hold both readings, since the file is monotone and 760 clears 2 × 378.7. Second, that larger
  WHOLE reading is the case §4 "What this does not check" names, and the main loop's close-shaped
  reading settles it for this tree. Taken in this worktree at `922d6b94d` with `GATE_PUSH_BASE`
  unset, it read 276.0 s, below R = 354.0, so R and C stand (§4 "The reading", reading 3). Third, no ask names a cure for the join's cost. Filing one in the owning
  build's `BACKLOG.md` is what would let §4 "When the ceiling comes back down" happen.
  This unit's brief, this role's prompt and the deviation record the main loop wrote for this unit
  were untracked when this draft was written:

```
memory/builds/dRankedPlan/prompts/2026-10-28-prompt-TOOL-dRankedPlan-83-spec-brief.md
memory/builds/dRankedPlan/prompts/2026-10-28-prompt-TOOL-dRankedPlan-83-1-spec-writer.md
memory/builds/dRankedPlan/build/2026-10-28-build-TOOL-dRankedPlan-83-deviation-831.md
```

## 9. Reuse audit

The seam is the derivation tool's own out-of-band route: `derive-ceilings.py --write --observed`
with `--how` (`tools/run-gates/derive-ceilings.py:396-425`, `:564-588`), the margin it reads, and the
leg's existing row in `tools/gate-legs.json`. Nothing is built. The procedure reuses
`TOOL-dRankedPlan-82` rev-2 and its pass `026bc5055`, which raised the spec tokens leg the same way.
It also reuses `9c756ce7d` for a write from a clean run record.
`python tools/codebase-map/reuse_lookup.py "raise one gate leg ceiling from an out-of-band reading recorded in the evidence file"`
ranked only name stems (`read`, `read_text`, `legs`, `leg`, `records`), none of which writes
evidence or a ceiling. No existing seam fits beyond the tool above. The recall probe returned
`TOOL-dRankedPlan-82` first, then the owner's answer, then `TOOL-aRoutedQuill-9`, the leg's WHOLE-mode
spec.

Recall terms used: `python tools/memory-recall/query.py "raise the routed commits leg ceiling for the deviation join over every chain build" --terms "derive-ceilings --observed --how ceiling-evidence routed_commits deviation_join routed commits TOOL-dRankedPlan-82 TOOL-dWellOiledMachine-127"`
