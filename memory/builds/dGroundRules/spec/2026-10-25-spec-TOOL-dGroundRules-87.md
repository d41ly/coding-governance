# TOOL-dGroundRules-87 — the spec tokens leg's ceiling covers the packet join over a live chain run, sized through `derive-ceilings.py --observed` from a reading of the leg alone

**Status:** DEFERRED · rev-1 · 2026-10-25 · node a · Tier-1 · base 87917c2f · streams tooling · order 34

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-87-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-87-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-87-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-87-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar at `263d31d59` timed the `spec tokens (a spec's own names resolve)` leg out at its
180 s ceiling twice, in the pool and on its serial retry, and attributed it CONTENDED
(`memory/builds/dGroundRules/RUN.md:18`). The leg is healthy and slow: while a chain build's run is
live, its packet join runs the dClosedLoop packet instrument, and the instrument's
`carries.py --report` spawns one `git show` per chain spec revision. This unit raises that one leg's
ceiling from evidence, through the out-of-band route `tools/run-gates/derive-ceilings.py` keeps for
a leg killed at its own ceiling, so the close's bar can go green. The owner authorized it at the
hand-off (`memory/builds/dGroundRules/RUN.md:576`).

## 2. Scope (IN)

- **S1** — The ceiling of `spec tokens (a spec's own names resolve)` in `tools/gate-legs.json`
  (`:1700`, 180 today) becomes C, the value §4 "The value" derives from the builder's reading R.
  Its row in `tools/run-gates/ceiling-evidence.txt` (`:132`, `2.6` from the runner today) rises to
  R, written by `derive-ceilings.py --write --observed` with the `--how` text §4 gives, so the
  row's source column carries how R was taken. No other row of either file moves. Observed by AC1,
  AC2 and AC4.
- **S2** — The `last-audit` stamp of `memory/guides/SESSION-KICKOFF.md` (`:5`) advances by the stamp
  rule at `:23`, in the same commit as S1, because `tools/gate-legs.json` is a `watch:` path (`:6`).
  `last-body-change` (`:8`) stays. Observed by AC3.

## 3. Non-goals (OUT)

- `carries.py`, `packet.py` and every other dClosedLoop instrument. The spawn cost lives in
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py:127-133`, and its
  cure is ask `TOOL-dGroundRules-112`, filed in this build's backlog. It cannot land in this run:
  the instrument is pinned, and `packet.py --repin` refuses inside a live chain run.
- Any other leg's ceiling, and `tools/run-gates/ceiling-margin.txt`.
- The run-gates runner, and the census of foreign gate work it stamps on each `.leg` row.
- Any adopter release. The leg is gov-only, an `[[exempt_leg]]` of `tools/govkit/registry.toml`
  (`:391-396`), so no shipped manifest carries its ceiling.
- Any help page. `help/measure-legs.md:73` documents the `--observed` route and names no leg's
  value.
- Any §B claim of the kickoff manifest. §B names `tools/check-spec-tokens.py` at `:65-66` for its
  `--list` and its carries join, never this leg's ceiling, so S2 re-stamps with no body change.

## 4. Design

### Evidence

- The main loop on node a, at the close: the leg alone took 170 to 173 s at HEAD, and 5 s at
  origin/main `462d20f35`, where no chain run is live. The difference is the packet join's
  `packet.py --check dGroundRules`, 169 s, and inside it `carries.py --report dGroundRules`, 143 s
  over 4095 `git show` spawns (the ask's row in `memory/builds/dGroundRules/BACKLOG.md`).
- The close's bar at `263d31d59`: the leg killed at 180 s twice, in the pool and on its serial
  retry (`memory/builds/dGroundRules/RUN.md:18`).
- The join runs only while a chain build's run is live: `scan_live_packets` skips a build whose
  `RUN.md` has no `phase:` line or whose last one is in `LIVE_EXCLUDED`, LANDED, ABORTED or LANDING
  (`tools/check-spec-tokens.py:1377`, `:1397-1405`), and prints its live count on every run
  (`:1813-1817`). dGroundRules holds the chain packet
  `memory/builds/dGroundRules/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, and its
  `RUN.md` reads `phase: VERIFYING` at `87917c2fe`.
- An in-band reading cannot size this ceiling. A failing row enters the record at its ceiling, never
  above it (`tools/run-gates/derive-ceilings.py:199`, the admission rule in its docstring), and
  `--report` in this worktree at `87917c2fe` reads 0 legs with a reading over 4 retained runs, all
  282 set aside as contended. The `--observed` route exists for exactly this case
  (`tools/run-gates/derive-ceilings.py:40-56`, `TOOL-cMendedVintage-17`).

### The reading

The builder takes one reading R of the leg alone, at the build commit's tree, with the chain run
still live:

1. **A free host.** `ps -ef` lists no `run-gates.sh`, no `run-selftests.sh` and no other gate
   checker or suite, this worktree's or another's.
2. **The leg alone.** From the repository root, `time python tools/check-spec-tokens.py`, the leg's
   own argv (`tools/gate-legs.json:1693-1696`). It exits 0, and its packet join line reports a live
   count of 1 or more. R is the `real` time in seconds, to one decimal, the precision the evidence
   file writes (`tools/run-gates/derive-ceilings.py:627`). A reading taken where the line reports
   0 live chain runs argues nothing, and the builder reports it and stops.

### The write

The evidence row comes first, from a run record holding no admitted reading, so no other row moves.
`python tools/run-gates/derive-ceilings.py --report` in this worktree prints
`# 0 leg(s) with a reading`. Where it prints any other count, the builder writes from a scratch clone
of the build commit and copies back only `tools/run-gates/ceiling-evidence.txt`, as `9c756ce7d` did.
The write, `<node>` being the node R was taken on, which the tool refuses to default (`:570-574`):

```
GOV_NODE=<node> python tools/run-gates/derive-ceilings.py --write --observed "spec tokens (a spec's own names resolve)=<R>" --how "<how>"
```

The `--how` text, one line with no tab (`:422-424`), in the shape of the `unattended-build
self-test` row (`tools/run-gates/ceiling-evidence.txt:142`), `<sha8>` being the build commit's
parent:

```
the leg alone in the worktree at <sha8> on a host running no other gate suite, its packet join over 1 live chain run, real <R>s; killed at its 180 s ceiling twice under the close's bar at 263d31d5, in the pool and on its serial retry
```

The summary line reads `0 raised` and `1 raised by --observed` (`:633-639`). R clears the stored
2.6 s, so the monotone refusal at `:581-586` does not fire. A `raised` count above 0 means the run
record held an admitted reading after all: the builder restores the file and writes from the clone.

### The value

`--check` passes a leg when its ceiling is at least its evidenced maximum plus
`max(floor, fraction × max)` (`tools/run-gates/derive-ceilings.py:663`, `:683`), and the margin file
declares a floor of 120 s and a fraction of 1.0 (`tools/run-gates/ceiling-margin.txt:26`). For any
R of 120 s or more the fraction half governs, so the ceiling must be at least 2R. Every ceiling in
`tools/gate-legs.json` is a multiple of 10, 59 distinct values from 120 to 16040, so C is the least
multiple of 10 at or above 2R, which is 10 × ⌈R / 5⌉. At the evidence's 170.0 to 173.0 s, C is
340 to 350; at 173.0 s, C is 350. The out-of-band row falls to the headroom branch, never the
REACHED one, which grades runner rows alone (`:679`).

### When the ceiling comes back down

Once `TOOL-dGroundRules-112` lands and the owner repins the instrument, a reading of the leg alone
over a live chain run supports a lower bound. Lowering takes `--write --reset` with `--observed`
for this leg, from a record holding no admitted reading, as `9c756ce7d` lowered the foreign-prefix
parity leg, and the ceiling then falls to the margin's value for that reading. Until then every
chain build's close pays the join's cost under this ceiling.

### What this does not check

- The cost. The raise bounds a hang and leaves the 4095 spawns where they are; `TOOL-dGroundRules-112`
  owns them.
- The leg's contended duration. Only the solo reading is measured; the margin's fraction is the whole
  of the headroom above it, and a bar contended past 2R still kills the leg.
- The load R was taken under. An `--observed` row is admitted uncensused, and its `--how` text is
  the only record of the host (`tools/run-gates/derive-ceilings.py:49-52`). On Windows `ps -ef`
  sees only processes an MSYS shell spawned.
- `--check` reads the two tracked files alone (`:643`), never whether R was taken as `--how` says.

### Rollout

This unit builds at order 34, after `TOOL-dGroundRules-86`. The builder sets this spec's status from
DEFERRED to INPROGRESS before its first write, because `tools/` is under `ROUTED_PATHS`. S2's stamp
is `last-audit: <date -Iseconds> @ <git rev-parse HEAD>`, both taken when the builder stages, and
the commit message carries a manifest delta line in the shape of `9c756ce7d`'s: none to §B, the
`last-audit` re-stamped for the watched `tools/gate-legs.json`, whose only change is one leg's
ceiling. The commit also states R, C and the node. The main loop re-renders the build README and
runs the bar at the close.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree, in Git Bash, with S1 and S2
applied and staged and before the unit's commit. R and C are the builder's reading and the value §4
derives from it; the figures quoted for a red are at R = 173.0.

- **AC1** — When `python tools/run-gates/derive-ceilings.py --check` runs, it exits 0 and prints a `ceiling-evidence:` line, and its stderr names `spec tokens (a spec's own names resolve)` among the ceilings backed by a reading taken outside the runner, with R, the node and the `--how` text.
  Red when: the evidence row is written and the ceiling left at 180. Then it prints `CEILING-EVIDENCE FAILED — spec tokens (a spec's own names resolve): ceiling 180s does not clear its evidenced maximum 173.0s` ending `(short by 166s)`, and exits 1. The builder observes this red between the write and the ceiling edit.
  figure: DERIVED. The shortfall is R + R − 180, re-derived from the row at check time.
- **AC2** — When `time python tools/check-spec-tokens.py` runs, it exits 0, its `spec-tokens: packet join ·` line reports a live count of 1 or more, and its `real` seconds sit under C by at least the margin's 120 s floor.
  Red when: the same command runs in a clone at origin/main `462d20f35`, where no chain run is live. Then the line reads `spec-tokens: packet join · 0 live chain run(s) · 0 packet(s) checked` and `real` is near 5 s, a reading without the join that would size no ceiling here.
  figure: DERIVED. The pass's own reading, which varies from R; the main loop measured 170 to 173 s at the close. The floor is `tools/run-gates/ceiling-margin.txt:26`.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs, it prints no `MANIFEST check 5 FAILED` line and exits 0.
  Red when: S1 is staged without S2. Then it prints `MANIFEST check 5 FAILED — staged changes touch watched files:` with the indented path `tools/gate-legs.json`, and exits 1.
- **AC4** — When `git diff --cached --numstat -- tools/gate-legs.json tools/run-gates/ceiling-evidence.txt` runs, it prints two lines whose added and deleted counts are both 1. Then `git diff --cached -U0 -- tools/gate-legs.json` shows one hunk, at line 1700, whose added line is the `"ceiling":` key with C, and `git diff --cached -U0 -- tools/run-gates/ceiling-evidence.txt` shows one added line opening `spec tokens (a spec's own names resolve)` with R.
  Red when: a second leg's ceiling is also edited. Then the `tools/gate-legs.json` line counts 2 added and 2 deleted.

## 6. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `leg ceilings clear their evidenced maximum` · `kickoff-manifest ratchet` · `spec tokens (a spec's own names resolve)`

Run through `derive_guarded_legs` at `87917c2fe`, `python tools/check-spec-tokens.py --legs-for`
over the three files touched names six guarded legs under the broad floor of 5. `tools/gate-legs.json`
trips `run-gates canary`, `run-gates gov canary`, `measure-legs selftest` and `policy fixtures`
through its own path, a guard those four legs carry. `--legs-for` prints `run-gates canary` against
its first matching guard, the broad `tools/`, so its exact `tools/gate-legs.json` guard is read from
the leg's row (`tools/gate-legs.json:1146-1150`).
`memory/guides/SESSION-KICKOFF.md` trips `recall floor` and `recall floor arms` through `memory/`.
`tools/run-gates/ceiling-evidence.txt` trips only broad guards.

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

- rev-1 · 2026-10-25 · initial draft from this unit's spec brief, grounded at `87917c2fe`.
  `tools/run-gates/derive-ceilings.py` and `tools/run-gates/ceiling-margin.txt` were read whole, and
  the raise follows `2fe73530e`, which first raised a ceiling through `--observed`, and `9c756ce7d`,
  which wrote its row from a record holding no admitted reading. Two things the brief did not name
  the tree adds. The commit must re-stamp `last-audit`, because `tools/gate-legs.json` is a watched
  path and the pre-commit's staged manifest check refuses a watched change without it; that is S2.
  And the ceiling's rounding to a multiple of 10 is read from the manifest's own values, never typed.
  Follow-up for the main loop, not a fork: once `TOOL-dGroundRules-112` lands and is repinned, a
  later unit lowers this ceiling as §4 "When the ceiling comes back down" says. This unit's brief
  and this role's prompt, untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-87-spec-brief.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-87-1-spec-writer.md
```

## 9. Reuse audit

The seam is the derivation tool's own out-of-band route: `derive-ceilings.py --write --observed`
with `--how` (`tools/run-gates/derive-ceilings.py:396-425`, `:564-588`), the margin it reads, and
the leg's existing row in `tools/gate-legs.json`. Nothing is built. The procedure reuses
`2fe73530e` for the out-of-band reading and the margin's sizing, `9c756ce7d` for a write from a
clean run record, and both for the `last-audit` re-stamp.
`python tools/codebase-map/reuse_lookup.py "raise one gate leg ceiling from an out-of-band reading recorded in the evidence file"`
ranked only name stems (`read`, `read_text`, `legs`, `leg`, `records`), none of which writes
evidence or a ceiling, so no existing seam fits beyond the tool above. The recall probe returned
`TOOL-cMendedVintage-17`, the ruling that a ceiling may be raised from a reading taken outside the
runner (`memory/DECISIONS.md:205`), and `TOOL-dDeclaredLoop-71`'s note of the `--observed` form.

Recall terms used: `python tools/memory-recall/query.py "raise a leg ceiling from a reading taken outside the runner with derive-ceilings observed" --terms "derive-ceilings --observed --how ceiling-evidence ceiling-margin leg ceiling raise killed at its ceiling spec tokens packet join carries.py"`
