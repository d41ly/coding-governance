# TOOL-dRankedPlan-82 — the spec tokens leg's ceiling covers the packet join over this run's live chain, sized through `derive-ceilings.py --observed` from a reading of the leg alone

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-1 · base ef0ac519 · streams tooling

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-82-deviation-821.md](../build/2026-10-27-build-TOOL-dRankedPlan-82-deviation-821.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-82-deviation-822.md](../build/2026-10-28-build-TOOL-dRankedPlan-82-deviation-822.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-82-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-1-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-82-2-builder.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-2-builder.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-82-3-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-3-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-82-revision-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-revision-brief.md) | research | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-82-spec-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar timed the `spec tokens (a spec's own names resolve)` leg out at its 390 s ceiling
twice, in the pool and on its serial retry, red OWN (`memory/builds/dRankedPlan/RUN.md:21`, `:358`).
The leg is healthy and slow: while a chain build's run is live, its packet join runs the dClosedLoop
packet instrument, and inside it `carries.py --report` spawns one `git show` per chain spec revision,
now over 954 chain specs. This unit raises that one leg's ceiling from evidence, through the
out-of-band route `tools/run-gates/derive-ceilings.py` keeps for a leg killed at its own ceiling, so
the close's bar can go green. The owner ordered it at the hand-off `owner-decision` of `be042d1e2`
(`memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-1-owner-review-until-no-high.md:36-43`).
It is built in this run, not carried forward to the build run, as that answer directs.

## 2. Scope (IN)

- **S1** — The ceiling of `spec tokens (a spec's own names resolve)` in `tools/gate-legs.json`
  (`:1700`, 390 today) becomes C = 830, the value §4 "The value" derives from the main loop's
  reading R = 411.0.
  Its row in `tools/run-gates/ceiling-evidence.txt` (`:132`, 195.0 from `TOOL-dGroundRules-87`'s
  out-of-band reading today) rises to R, written by `derive-ceilings.py --write --observed` with
  the `--how` text §4 gives, so the row's source column carries how R was taken. No other row of
  either file moves. Observed by AC1, AC2 and AC4.
- **S2** — The `last-audit` stamp of `memory/guides/SESSION-KICKOFF.md` (`:5`) advances by the stamp
  rule at `:23`, in the same commit as S1, because `tools/gate-legs.json` is a `watch:` path (`:6`).
  `last-body-change` (`:8`) stays. Observed by AC3.

## 3. Non-goals (OUT)

- `carries.py`, `packet.py` and every other dClosedLoop instrument. The spawn cost lives in
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py:127-134`, one
  `git log` per spec and one `git show` per revision of it, and its cure is ask
  `TOOL-dGroundRules-112` (`memory/builds/dGroundRules/BACKLOG.md:19`). It cannot land in this run:
  the instrument is pinned, and only the owner's `packet.py --repin` moves a pin, outside a live
  chain run.
- Any other leg's ceiling, and `tools/run-gates/ceiling-margin.txt`.
- The run-gates runner, and the census of foreign gate work it stamps on each `.leg` row.
- Any adopter release. The leg is gov-only, an `[[exempt_leg]]` of `tools/govkit/registry.toml`
  (`:391-396`), so no shipped manifest carries its ceiling.
- Any help page. `help/measure-legs.md:73` documents the `--observed` route and names no leg's
  value.
- Any §B claim of the kickoff manifest. §B names `tools/check-spec-tokens.py` at
  `memory/guides/SESSION-KICKOFF.md:65-66` for its `--list` and its carries join, never this leg's
  ceiling, so S2 re-stamps with no body change.

## 4. Design

### Evidence

- The main loop on node a with the host idle: `packet.py --check dRankedPlan` alone took 344 s,
  inside the leg's 390 s ceiling with nothing else of the leg counted (`RUN.md:358`). The leg alone
  is that join plus the rest of `tools/check-spec-tokens.py`'s walk, so R is above 344 s.
- The close's bar: the leg killed at 390 s twice, in the pool and on its serial retry, every other
  leg green after `b02b55c97` (`RUN.md:358`).
- The join runs only while a chain build's run is live: `scan_live_packets` skips a build whose
  `RUN.md` has no `phase:` line or whose last one is in `LIVE_EXCLUDED`, LANDED, ABORTED or LANDING
  (`tools/check-spec-tokens.py:1377`, `:1381-1403`), and prints its live count on every run
  (`:1813-1817`). At `ef0ac519` the 22 tracked chain packets hold one live run, dRankedPlan's, whose
  `RUN.md` reads `phase: BUILDING`; at origin/main `1a61f21a2` they hold none.
- An in-band reading cannot size this ceiling. A failing row enters the record at its ceiling, never
  above it (`tools/run-gates/derive-ceilings.py:219-225`, `:286-288`), and `--report` in this
  worktree at `ef0ac519` reads `0 leg(s) with a reading, over 2 retained run(s)`, all 78 set aside
  as contended. The `--observed` route exists for exactly this case
  (`tools/run-gates/derive-ceilings.py:40-56`, `TOOL-cMendedVintage-17`).

### The reading

R is the main loop's, and the builder takes no reading. The leg's argv
(`tools/gate-legs.json:1693-1696`) is a gate leg, and the role-gate arm of
`tools/hooks/scratch-guard.js` (`checkRoleGate`, `:1421-1451`, row G1) refuses every leg to a role
agent but those its allowlist names; the allowlist of `gov-builder` in `.claude/roles.json`
(`:11-18`) names `lexicon naming predicates` alone, and the arm refused this leg to the rev-1
builder live.

The main loop took one reading on node a at `cc8880ae6`, the tree clean and this run live:

1. **The census.** `ps -ef`, before and after the reading, listed no `run-gates.sh` but the idle
   orphan of `unattended-dgroundrules-0e6f4a` (pid 10907, from Oct 23), the one `64c85a989` found,
   left alone. Another worktree's `--dispatch` started its own `tools/check-spec-tokens.py` at
   23:44:14, overlapping the reading's last 61 s of 6m51s (23:38:24 to 23:45:15). The host was
   therefore not free for that last minute. Contention can only have lengthened the reading, so the
   overlap errs toward a higher C and never a lower one, and the `--how` text records it.
2. **The leg alone.** `time python tools/check-spec-tokens.py` exited 0 and printed
   `spec-tokens: packet join · 1 live chain run(s) · 1 packet(s) checked`, `real 6m50.960s`. R is
   that time in seconds to one decimal, the precision the evidence file writes
   (`tools/run-gates/derive-ceilings.py:627`): R = 411.0.

### The write

The builder writes the evidence row first, from a run record holding no admitted reading, so no
other row moves. `python tools/run-gates/derive-ceilings.py --report` in this worktree prints
`# 0 leg(s) with a reading`. Where it prints any other count, the builder writes from a scratch clone
of the build commit and copies back only `tools/run-gates/ceiling-evidence.txt`, as `9c756ce7d` did.
The write names node a, where R was taken, which the tool refuses to default (`:570-574`):

```
GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --observed "spec tokens (a spec's own names resolve)=411.0" --how "the leg alone in the worktree at cc8880ae on node a, its packet join over 1 live chain run, real 411.0s; the census held no gate suite but the idle orphan run-gates.sh of unattended-dgroundrules-0e6f4a, and another worktree's check-spec-tokens.py overlapped the reading's last 61s; killed at its 390 s ceiling twice under dRankedPlan's close bar, in the pool and on its serial retry"
```

The `--how` text is the one line inside the last pair of double quotes, with no tab (`:422-424`), in
the shape of the row it replaces (`tools/run-gates/ceiling-evidence.txt:132`).

The summary line reads `0 raised` and `1 raised by --observed` (`:633-639`). R clears the stored
195.0 s, so the monotone refusal at `:581-586` does not fire. A `raised` count above 0 means the run
record held an admitted reading after all: the builder restores the file and writes from the clone.

### The value

`--check` passes a leg when its ceiling is at least its evidenced maximum plus
`max(floor, fraction × max)` (`tools/run-gates/derive-ceilings.py:663`, `:683`), and the margin file
declares a floor of 120 s and a fraction of 1.0 (`tools/run-gates/ceiling-margin.txt:26`). For any
R of 120 s or more the fraction half governs, so the ceiling must be at least 2R. Every ceiling in
`tools/gate-legs.json` at `ef0ac519` is a multiple of 10, 60 distinct values from 120 to 16040, so C
is the least multiple of 10 at or above 2R, which is 10 × ⌈R / 5⌉. From R = 411.0 that is
C = 10 × ⌈411.0 / 5⌉ = 10 × 83 = 830, clearing 2R = 822 by 8 s. The out-of-band row falls to the
headroom branch, never the REACHED one, which grades runner rows alone (`:679`).

### When the ceiling comes back down

Once `TOOL-dGroundRules-112` lands and the owner repins the instrument, a reading of the leg alone
over a live chain run supports a lower bound. Lowering takes `--write --reset` with `--observed`
for this leg, from a record holding no admitted reading, as `9c756ce7d` lowered the foreign-prefix
parity leg, and the ceiling then falls to the margin's value for that reading. Until then every
chain build's close pays the join's cost under this ceiling.

### What this does not check

- The cost. The raise bounds a hang and leaves the spawns where they are; `TOOL-dGroundRules-112`
  owns them. The join's cost grows with the chain's spec revisions, so a later chain build's close
  can outrun C the way this one outran 390.
- The leg's contended duration. Only the solo reading is measured; the margin's fraction is the whole
  of the headroom above it, and a bar contended past 2R still kills the leg.
- The load R was taken under. An `--observed` row is admitted uncensused, and its `--how` text is
  the only record of the host (`tools/run-gates/derive-ceilings.py:49-52`). On Windows `ps -ef`
  sees only processes an MSYS shell spawned.
- `--check` reads the two tracked files alone (`:643-644`), never whether R was taken as `--how`
  says.

### Rollout

This unit builds in this run, once rev-2 is committed. It carries no `order` verb: rev-1 sat at
order 28, and `63350171b` removed the verb from the status header because the dispatch order gate
reads the 79 DEFERRED units as non-terminal, so a unit at order 28 could not dispatch. A unit with no
`order` verb is unordered and blocks nothing.

1. **Before the dispatch.** The main loop appends this unit's `## route` to the session card.
2. **The builder.** It sets this spec's status from DEFERRED to INPROGRESS before its first write,
   because `tools/` is under `ROUTED_PATHS`. It runs `--report` and the write of "The write", sets
   the ceiling to 830, and applies S2. S2's stamp is `last-audit: <date -Iseconds> @ <git rev-parse HEAD>`,
   both taken when the builder stages. It observes AC3 and AC4 on its staged change and commits. The
   commit message carries a manifest delta line in the shape of `64c85a989`'s: none to §B, the
   `last-audit` re-stamped for the watched `tools/gate-legs.json`, whose only change is one leg's
   ceiling. It also states R = 411.0 as the main loop's reading, C = 830 and node a.
3. **After the pass commit.** The main loop observes AC1's red and then its green, and AC2's red,
   re-renders the build README, re-runs the close and runs the bar there.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

All commands run from the repository root of the worktree, in Git Bash. R = 411.0 and C = 830 are
the main loop's reading and the value §4 derives from it. AC1 and AC2 are the main loop's, because
the role gate refuses both legs' argv to `gov-builder` (§4 "The reading"). AC3 and AC4 are the
builder's, with S1 and S2 applied and staged and before the unit's commit.

- **AC1** — When the main loop runs `python tools/run-gates/derive-ceilings.py --check` at the pass commit, after it lands on the run's branch, it exits 0 and prints a `ceiling-evidence:` line, and its stderr names `spec tokens (a spec's own names resolve)` among the ceilings backed by a reading taken outside the runner, as `411.0s on node a` followed by the `--how` text.
  Red when: the committed evidence row is read against the ceiling of 390 the pass commit's parent holds. The main loop observes it after the pass commit and before the green, HEAD being the pass commit, with no write under `tools/`: `--check` reads the leg manifest from `GATE_LEGS` before the sibling one (`tools/run-gates/derive-ceilings.py:139-142`), and reads nothing else of this change but the evidence file and the margin (`:643-647`). It runs `TMP_LEGS=$(cygpath -m "$(mktemp)")`, then `git show HEAD^:tools/gate-legs.json > "$TMP_LEGS"`, then `GATE_LEGS="$TMP_LEGS" python tools/run-gates/derive-ceilings.py --check`. Then it prints `CEILING-EVIDENCE FAILED — spec tokens (a spec's own names resolve): ceiling 390s does not clear its evidenced maximum 411.0s by the required max(120s, 1.0x) = 411s (short by 432s)` and exits 1, naming no other leg, since the parent's manifest differs from the pass's in this one ceiling.
  permission: the `leg ceilings clear their evidenced maximum` leg runs this argv, and the role gate refuses it to `gov-builder`.
  figure: DERIVED. The shortfall is re-derived from the row at check time (`tools/run-gates/derive-ceilings.py:683-686`): 411.0 + 411 − 390 = 432.
- **AC2** — When the main loop ran `time python tools/check-spec-tokens.py` on node a at `cc8880ae6`, before the builder's dispatch, it exited 0, its line read `spec-tokens: packet join · 1 live chain run(s) · 1 packet(s) checked`, and its `real 6m50.960s` sits under C = 830 by 419 s, more than the margin's 120 s floor. That reading is §4 "The reading", and it is this criterion's green.
  Red when: the main loop runs the same command in a scratch clone at origin/main `1a61f21a2`, where no chain run is live, after the pass commit and before the close. Then the line reads `spec-tokens: packet join · 0 live chain run(s) · 0 packet(s) checked` and `real` is far under the 344 s join, a reading without the join that would size no ceiling here.
  permission: the `spec tokens (a spec's own names resolve)` leg runs this argv, and the role gate refuses it to `gov-builder`.
  figure: PINNED. R = 411.0 is the main loop's one reading at `cc8880ae6`; the main loop measured the join alone at 344 s. The floor is `tools/run-gates/ceiling-margin.txt:26`.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs, it prints no `MANIFEST check 5 FAILED` line and exits 0.
  Red when: S1 is staged without S2. Then it prints `MANIFEST check 5 FAILED — staged changes touch watched files:` with the indented path `tools/gate-legs.json`, and exits 1.
- **AC4** — When `git diff --cached --numstat -- tools/gate-legs.json tools/run-gates/ceiling-evidence.txt` runs, it prints two lines whose added and deleted counts are both 1. Then `git diff --cached -U0 -- tools/gate-legs.json` shows one hunk, at line 1700, whose added line is the `"ceiling":` key with C, and `git diff --cached -U0 -- tools/run-gates/ceiling-evidence.txt` shows one added line opening `spec tokens (a spec's own names resolve)` with R.
  Red when: a second leg's ceiling is also edited. Then the `tools/gate-legs.json` line counts 2 added and 2 deleted.

## 6. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `leg ceilings clear their evidenced maximum` · `kickoff-manifest ratchet` · `spec tokens (a spec's own names resolve)`

Run through `derive_guarded_legs` (`tools/check-spec-tokens.py:589-608`) at `ef0ac519`,
`python tools/check-spec-tokens.py --legs-for` over the three files touched names six guarded legs
under the broad floor of 5 (`:362`). `tools/gate-legs.json` trips `run-gates canary`,
`run-gates gov canary`, `measure-legs selftest` and `policy fixtures` through its own path, a guard
those four legs carry. `--legs-for` prints `run-gates canary` against its first matching guard, the
broad `tools/`, so its exact `tools/gate-legs.json` guard is read from the leg's row
(`tools/gate-legs.json:1146-1150`). `memory/guides/SESSION-KICKOFF.md` trips `recall floor` and
`recall floor arms` through `memory/`. `tools/run-gates/ceiling-evidence.txt` trips only broad
guards.

The unguarded legs named beside them read what this unit changes:

- `leg ceilings clear their evidenced maximum` runs `derive-ceilings.py --check`
  (`tools/gate-legs.json:1846-1855`), observed by AC1.
- `kickoff-manifest ratchet` reads S2, observed by AC3 in its staged form.
- `spec tokens (a spec's own names resolve)` is the leg S1 bounds, observed by AC2, and it reads
  this spec while it is INPROGRESS.

The bar itself runs at the close. No arm is added or moved. No floor or pinned count moves; the one
ceiling that moves is S1's.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-27 · initial draft from this unit's spec brief, grounded at `ef0ac519`, following
  `TOOL-dGroundRules-87` section for section and its build `64c85a989`.
  `tools/run-gates/derive-ceilings.py` and `tools/run-gates/ceiling-margin.txt` were read whole at
  this base; neither differs in what §4 cites from the precedent's base. Two things the tree adds
  over the precedent. The free-host step now names the idle orphan `64c85a989` met, and the other
  chain instruments a concurrent reading would contend with. And AC2's red clone is origin/main
  `1a61f21a2`, where none of the 22 chain packets' runs is live. Follow-up for the main loop, not a
  fork: with this unit at order 28 and CLOSED in this run, the build run's last unit in build order
  is no longer `TOOL-dRankedPlan-81`, which `TOOL-dRankedPlan-17`'s DEFERRED row in this build's
  `BACKLOG.md` names as the unit that closes that ask; the main loop re-reads that row at the close.
  Once `TOOL-dGroundRules-112` lands and is repinned, a later unit lowers this ceiling as §4 "When
  the ceiling comes back down" says. This unit's brief and this role's prompt, untracked when this
  draft was written:

```
memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-spec-brief.md
memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-1-spec-writer.md
```

- rev-2 · 2026-10-27 · S1 · §4 · §5 · AC1 · AC2 · the reading is the main loop's, from the
  revision brief below. The builder dispatched at `cc8880ae6` stopped without a commit: the role-gate
  arm of `tools/hooks/scratch-guard.js` (`checkRoleGate`, row G1) refused it the argv of the
  `spec tokens (a spec's own names resolve)` leg live, and refuses it the argv of
  `leg ceilings clear their evidenced maximum` the same way, since the allowlist of `gov-builder`
  in `.claude/roles.json` names neither. S1 and §4 "The reading" now carry the main loop's R = 411.0
  at `cc8880ae6` with its census, its 61 s overlap with another worktree's checker stated, and
  "The value" carries C = 830. §4 "The write" gives the `--how` text whole. AC1 and AC2 are the main
  loop's, each saying when: AC2's green is that reading; AC1's red reads the committed row against
  the parent's manifest through `GATE_LEGS`, so nothing is written under `tools/`, and its green
  follows the pass commit. AC3 and AC4 stay the builder's, on its staged change. §4 "Rollout" says
  the header carries no `order` verb since `63350171b`, the main loop appends this unit's
  `## route` to the session card before the dispatch, and the builder sets INPROGRESS before its
  first write. The rev-1 follow-up above is withdrawn: with no `order` verb this unit sits in no
  build order, so `TOOL-dRankedPlan-81` stays the build run's last unit in build order. Every line
  §4 and §5 cite was re-read at `cc8880ae6`; `tools/`, `skills/` and `memory/guides/` are unchanged
  since `ef0ac519`, so the base stays. The revision brief and this role's prompt, untracked when
  this revision was written:

```
memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-revision-brief.md
memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-3-spec-writer.md
```

## 9. Reuse audit

The seam is the derivation tool's own out-of-band route: `derive-ceilings.py --write --observed`
with `--how` (`tools/run-gates/derive-ceilings.py:396-425`, `:564-588`), the margin it reads, and
the leg's existing row in `tools/gate-legs.json`. Nothing is built. The procedure reuses
`TOOL-dGroundRules-87`'s raise at `64c85a989` for the same leg, `9c756ce7d` for a write from a clean
run record, and both for the `last-audit` re-stamp.
`python tools/codebase-map/reuse_lookup.py "raise one gate leg ceiling from an out-of-band reading recorded in the evidence file"`
ranked only name stems (`read`, `read_text`, `legs`, `leg`, `records`), none of which writes
evidence or a ceiling, so no existing seam fits beyond the tool above. The recall probe returned
`TOOL-dGroundRules-87` first, then ask `TOOL-dGroundRules-112` and its KEEP row.

Recall terms used: `python tools/memory-recall/query.py "raise the spec tokens leg ceiling for the packet join over a live chain run" --terms "derive-ceilings --observed --how ceiling-evidence ceiling-margin spec tokens packet join carries.py TOOL-dGroundRules-87 TOOL-dGroundRules-112"`
