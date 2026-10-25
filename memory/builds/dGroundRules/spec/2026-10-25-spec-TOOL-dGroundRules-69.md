# TOOL-dGroundRules-69 — the strict case's source under the policy fixtures guard, so the leg's full run traces no read outside it

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-1 · base 3d86915c · streams tooling · order 23

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-69-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-69-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-69-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-69-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The `policy fixtures` leg runs with `--strict-from`, and that run's guard trace reports one read
outside the leg's guard. That read is the `on-invalid-strict` case's source, the dClosedLoop v2
architecture record. `TOOL-dGroundRules-67` guarded the twelve paths that a run without
`--strict-from` reports, and that run skips the strict case, so this read was never traced. One guard
line closes it.

## 2. Scope (IN)

- **S1** — The guard line. The `policy fixtures` row of `tools/gate-legs.json` gains the one line §4
  "The guard line" gives, as an in-place insert of that line and no other byte. Observed by AC1 and
  AC2.
- **S2** — The gates the insert can move. The builder runs the direct checks §4 "What the insert can
  move" names. It re-stamps or re-keys what they demand and writes nothing else. This spec measured
  that only the kickoff manifest's audit stamp is demanded. Observed by AC3.

## 3. Non-goals (OUT)

- `tools/policy/check_policy.py`. The guard trace and the guard-census check are graders this unit
  feeds and does not change, and so is the strict case's own judgement of the v2 record.
- Any other spec, the §7 of another build's spec included.
- Any guard line other than the one §4 gives. The main loop's full run reported no other path.

### Edges

none

This unit carries out the follow-through of `TOOL-dGroundRules-67` (CLOSED), whose sweep guarded the
paths of a run without `--strict-from`. It changes nothing that unit built.

## 4. Design

### Evidence

The main loop ran the leg's own argv,
`python {prefix}/policy/check_policy.py --fixture --strict-from memory/builds/dClosedLoop/build/`,
in a scratch clone of `3d86915cf`. It printed 895 assertions and 1 wrong. The wrong line was
`policy-fixture: guard-trace · WRONG <v2> · not under the policy fixtures guard`, where `<v2>` is
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`. Every other
case line was green. The brief records the run, and this spec did not repeat it.

The read comes from `run_on_invalid_strict`. It finds v2 with a glob over the `--strict-from`
directory (`tools/policy/check_policy.py:1868`), which opens no file, and it then reads the one file
it found (`:1875`). That open is the read the audit hook keeps (`:3964-4005`). With no `--strict-from`
the case returns at `:1864-1867` before either step, so the read never happens.

### The guard line

The trace joins each kept read to the guard through `read_legs_for` (`:3859-3877`). That function asks
the spec-token checker's `--legs-for -`, whose trip rule is `check_guard_trips`
(`tools/memory-tree/design_lib.py:589-598`). A guard trips on the exact path or on anything under it as
a directory. The guard-census check, `check_guard_lines` (`TOOL-dGroundRules-37`,
`tools/policy/check_policy.py:4070-4093`), asks `git ls-files` about each guard line and reds one that
lists nothing. Both candidates pass both checks. The file is tracked, and the directory lists 370
tracked files at `3d86915cf`. Neither is broad, since each would sit only in this row.

The pick is the file. The trace keys on files a case opens, and this case opens exactly one. On cost,
measured on 2026-10-25 from `4592ab001` (2026-10-20, the commit the owner froze v2 at) to `3d86915cf`:
none of the 618 commits touched the file, while 141 touched the directory, so a directory guard would
run the leg on about one commit in four and the file guard on none. The figures are PINNED to that
range.

The line goes into the `policy fixtures` row's `guard` list directly after `"AGENTS.md",` and before
`"help/policy.md"` (`tools/gate-legs.json:1837-1838`). It ends in a comma, so taking it out again still
parses, and AC1's staged break depends on that. The file is edited in place, never re-dumped. The
line carries no `{prefix}` token, because the record lives under `memory/`, not under the tool root.

```
      "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
```

What the file guard does not check: a second file whose name ends `-architecture-v2.md`, added to that
directory, changes the strict case's verdict (`:1869-1872`) and trips no guard. A rename or deletion
of v2 does trip the guard, because the old path is in the diff, and the census check then reds the
line as naming no tracked file.

### What the insert can move

The builder runs each check below after S1 and acts only on what it demands.

| Gate | What it keys on | Measured on 2026-10-25 at `3d86915cf` |
|---|---|---|
| install-prefix | No waiver registry exists (`tools/check-install-prefix.sh:24-28`). Its `--offenders` keys carry no line number (`:8-12`). | The line spells no kit path. No segment of it names a directory under `tools/`, so it adds no hit. |
| spec-token waivers | The guards join's hit names a spec's first declared path that trips a leg (`tools/check-spec-tokens.py:1589-1622`). | With either candidate, no live spec's `policy fixtures` hit appears or re-keys. The probe covered 36 live specs, 23 of which trip the leg today. No live spec declares a path under that directory. Nothing to re-key. |
| kickoff manifest | Check 5 refuses a staged change to a watched path, `tools/gate-legs.json` among them, unless the staged audit block moves `last-audit` (`skills/session-kickoff/manifest-check.sh:1640-1655`). | Demanded. |
| leg join | The guards join's non-broad guards (`derive_guarded_legs`), not the first guard `--legs-for` prints per leg. | Four legs: `run-gates canary`, `run-gates gov canary`, `measure-legs selftest` and `policy fixtures`. |

The stamp moves in `memory/guides/SESSION-KICKOFF.md`, in the form `TOOL-dGroundRules-67`'s build
commit `4f76c4b39` used: `last-audit: <ISO datetime> @ <full sha of HEAD>`. No §B claim reads the
`policy fixtures` guard, so the stamp moves and the body does not. The committer adds a
`manifest-audit:` trailer to the commit message, as that commit did.

`tools/govkit/govkit.py:2611` skips `selftests` legs, and `tools/run-gates/measure_legs.py:3225` grades
only its own row's guard, so neither reads this line.

### Alternatives rejected

- The directory `memory/builds/dClosedLoop/build/`. It would catch a second `-architecture-v2.md`
  file in that directory. It would also run the leg on about a quarter of commits in exchange for a
  case the owner's freeze of v2 makes unlikely. The trace never asks for a directory, because it
  records files.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. AC1's staged break runs from the
root of a scratch clone `D`, made after S1 is written, as below.

```
D="$TEMP/d69"; rm -rf "$D"
git -c core.longpaths=true clone -q --branch branch/unattended-dgroundrules-e47ae1 . "$D"
cp tools/gate-legs.json "$D/tools/gate-legs.json"
sed -i '\#^      "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",$#d' "$D/tools/gate-legs.json"
```

The leg's full run is a whole-suite form the bar join refuses in a criterion. AC1 runs the strict case
alone, which still runs the guard trace and the census check after it (`tools/policy/check_policy.py:4480-4483`).
The `policy fixtures` leg on §6 runs the whole leg at the close, through the main loop.

- **AC1** — When `python tools/policy/check_policy.py --fixture --strict-from memory/builds/dClosedLoop/build/ on-invalid-strict 2>&1 | grep -c "guard-trace.*WRONG"` runs, it prints `0`.
  The same run's `strict cell(s) in memory/builds/dClosedLoop/build/` line is present, which shows
  the case read v2 and the trace saw the read.
  Red when: the guard line is absent again. The staged break is the same command run from the root of
  `D`, which prints `1`, the `WRONG` line naming v2. At `3d86915cf` the same output follows from
  `:1875` and `:4042-4044`; this spec derived that from the code and did not run it.
- **AC2** — When `python tools/check-spec-tokens.py --legs-for memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -c "policy fixtures <-"` runs, it prints `1`.
  At `3d86915cf` it printed `0`.
  Red when: the line is left out of the guard, or is spelled with a `{prefix}` token that resolves
  under `tools/`.
- **AC3** — When `git diff 3d86915cf -- memory/guides/SESSION-KICKOFF.md | grep -c "^+last-audit: "` runs, it prints `1`.
  At `3d86915cf` it printed `0`.
  Red when: `tools/gate-legs.json` changes and the audit stamp does not move, which check 5 of
  `skills/session-kickoff/manifest-check.sh` refuses at commit.

## 6. Gates

`policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The first four are the legs whose non-broad guard `tools/gate-legs.json` trips, as the guards join
reads them through `derive_guarded_legs`. `run-gates canary` is among them, because its guard names
`tools/gate-legs.json` beside the broad `tools/`, and `--legs-for` prints only the broad one. `recall floor` and
`recall floor arms` are the legs `memory/guides/SESSION-KICKOFF.md` trips, from `--legs-for` at
`3d86915cf`. The next three are the unguarded legs §4 "What the insert can move" names. This unit adds
no suite arm and declares no arm line.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the build run's rescope add row for this unit and its spec
  brief, `memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-69-spec-brief.md`,
  grounded at `3d86915cf`. Picks the file over the directory, as the brief recommended, on the
  trace's file-keyed reads and the measured commit counts. Two points depart from the brief, both
  measured. The install-prefix gate holds no waiver rows to re-key. The spec-token waivers need no
  re-key either, since no live spec's hit moves. Only the audit stamp is demanded, and it gets a
  criterion of its own, AC3.
  Folded in before commit, from the main loop's INPROGRESS token sweep: §6 gains
  `run-gates canary`, the guards hit `run-gates canary <- tools/gate-legs.json`, and §4's leg-join
  row now reads the join's non-broad guards, not the first guard `--legs-for` prints.

## 9. Reuse audit

Every seam this unit touches already exists, and it builds no new mechanism. The guard list is the
`policy fixtures` row of `tools/gate-legs.json`, the row `TOOL-dGroundRules-67` S1 extended. That row
is graded by `check_guard_trace` through `--legs-for` and by `check_guard_lines` through `git ls-files`.
The stamp is the kickoff manifest's own `last-audit` key.
`python tools/codebase-map/reuse_lookup.py "add the strict case's source file to the policy fixtures gate leg guard list"`
ranked name stems only (`legs`, `leg`, `fixture`, `load_policy`), and none of them widens a guard. The
recall probe returned `TOOL-dGroundRules-37` and `TOOL-dGroundRules-33`, whose checks this line must
satisfy, and `TOOL-dGroundRules-67`, whose insert this one follows. It also returned asks
`TOOL-dGroundRules-109` and `TOOL-dGroundRules-111`, whose waiver rows this unit leaves as they stand.

Recall terms used: `python tools/memory-recall/query.py "policy fixtures guard misses the strict case's source read, on-invalid-strict traced only with --strict-from" --terms "guard-trace policy fixtures on-invalid-strict strict-from architecture-v2 gate-legs.json guard census names no file git tracks manifest-audit re-stamp"`
