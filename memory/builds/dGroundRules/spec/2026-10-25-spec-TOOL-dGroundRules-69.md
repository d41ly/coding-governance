# TOOL-dGroundRules-69 — the strict case's source under the policy fixtures guard, so the leg's full run traces no read outside it

**Status:** CLOSED · rev-2 · 2026-10-25 · node d · Tier-1 · base 591cb00d · streams tooling · order 23

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-25-prompt-TOOL-dGroundRules-69-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-69-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-69-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-69-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The `policy fixtures` leg runs with `--strict-from`, and that run's guard trace reports one read
outside the leg's guard. That read is the `on-invalid-strict` case's source, the dClosedLoop v2
architecture record. `TOOL-dGroundRules-67` guarded the twelve paths that a run without
`--strict-from` reports, and that run skips the strict case, so this read was never traced. One guard
line, naming the directory `--strict-from` reads, closes it.

## 2. Scope (IN)

- **S1** — The guard line. The `policy fixtures` row of `tools/gate-legs.json` gains the one line §4
  "The guard line" gives, the directory `memory/builds/dClosedLoop/build/`, as an in-place insert of
  that line and no other byte. Observed by AC1 and AC2.
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
lists nothing. The directory lists 370 tracked files at `591cb00d7`, so the census passes it. The
guards join keeps it (`derive_guarded_legs`), because it sits only in this row and is not broad.

The pick is the directory, by the main loop's ruling on the builder's divergence (§8 rev-2). The file
line spells the id `PLAY-dClosedLoop-1` inside its filename, and §4 "What the insert can move" shows
the drift-audit signal that reds on it. A glob line naming only the v2 suffix is printed
`UNEVALUATED` by `--legs-for` (`tools/check-spec-tokens.py:616-618`, `:661-668`), so the trace could not
join a read to it. The directory spells no id and joins the read through `check_guard_trips`. It also
covers the case's whole input, since a second file whose name ends `-architecture-v2.md` changes the
strict case's verdict (`tools/policy/check_policy.py:1869-1872`) and now trips the leg.

On cost, measured at `591cb00d7` from `4592ab001` (2026-10-20, the commit the owner froze v2 at): 141 of
the 619 commits touched the directory, 128 of them touched no path the leg's guard already holds, so
the leg would have run on 247 of the 619 commits instead of 119. The leg's ceiling is 300 s. The
figures are PINNED to that range.

The line goes into the `policy fixtures` row's `guard` list directly after `"AGENTS.md",` and before
`"help/policy.md"` (`tools/gate-legs.json:1837-1838`). It ends in a comma, so taking it out again still
parses, and AC1's staged break depends on that. The file is edited in place, never re-dumped. The
line carries no `{prefix}` token, because the record lives under `memory/`, not under the tool root.

```
      "memory/builds/dClosedLoop/build/",
```

What the directory guard does not check: nothing compares this line with the leg's `--strict-from`
argv. If a later edit points the argv at another directory, the census still passes the old line
while it names tracked files. The guard trace reds the new directory's read on the next full run.

### What the insert can move

The builder runs each check below after S1 and acts only on what it demands.

| Gate | What it keys on | Measured on 2026-10-25 at `591cb00d7` |
|---|---|---|
| install-prefix | No waiver registry exists (`tools/check-install-prefix.sh:24-28`). Its `--offenders` keys carry no line number (`:8-12`). | The line spells no kit path. No segment of it names a directory under `tools/`, so it adds no hit. |
| spec-token waivers | The guards join's hit names a spec's first declared path that trips a leg (`tools/check-spec-tokens.py:1589-1622`). | No live spec's `policy fixtures` hit appears or re-keys. The probe covered 36 live specs, 23 of which trip the leg today. No live spec declares a path under that directory. Nothing to re-key. |
| `drift-audit records` | Signal `non_terminal_specs_cited_by_product_source` greps each non-terminal spec's own id, word-bounded, over the evidence globs (`tools/drift-audit/drift_report.py:740-741`), which hold `tools/gate-legs.json` (`tools/drift-audit/drift_signals.py:95-114`). Its offender set is shrink-only (`tools/drift-audit/drift_signals.py:373-393`, `tools/drift-audit/drift_report.py:4339-4343`, `tools/drift-audit/drift_report.py:411-451`). | The id grammar the engine builds (`_resolve_ident`, behind `_build_own_id_re` at `tools/drift-audit/drift_report.py:672-673`) finds no id in `memory/builds/dClosedLoop/build/`. In the v2 filename it finds `PLAY-dClosedLoop-1`, an INPROGRESS spec, which is the builder's divergence. No new offender. |
| kickoff manifest | Check 5 refuses a staged change to a watched path, `tools/gate-legs.json` among them, unless the staged audit block moves `last-audit` (`skills/session-kickoff/manifest-check.sh:1640-1655`). | Demanded. |
| leg join | The guards join's non-broad guards (`derive_guarded_legs`), not the first guard `--legs-for` prints per leg. | Four legs: `run-gates canary`, `run-gates gov canary`, `measure-legs selftest` and `policy fixtures`. |

The stamp moves in `memory/guides/SESSION-KICKOFF.md`, in the form `TOOL-dGroundRules-67`'s build
commit `4f76c4b39` used: `last-audit: <ISO datetime> @ <full sha of HEAD>`. No §B claim reads the
`policy fixtures` guard, so the stamp moves and the body does not. The committer adds a
`manifest-audit:` trailer to the commit message, as that commit did.

`tools/govkit/govkit.py:2611` skips `selftests` legs, and `tools/run-gates/measure_legs.py:3225` grades
only its own row's guard, so neither reads this line.

`drift-audit records` carries no guard, so it runs on every bar whatever this unit touches. It is
named on §6 because the insert sits in its evidence. The guards join does not owe it.

### Alternatives rejected

- The v2 file itself, which rev-1 picked. Its path spells `PLAY-dClosedLoop-1`, so the line becomes
  a product citation of that INPROGRESS spec. The `drift-audit records` leg then reds a new id in a
  shrink-only set.
- A glob line for the v2 suffix. `--legs-for` prints it `UNEVALUATED`, so the trace cannot join a
  read to it.
- Taking `tools/gate-legs.json` out of the drift-audit evidence globs. That would also drop the file's
  real citations, which the main loop counted at `591cb00d7`: 17 spellings of `TOOL-aSparedSpawn-13`,
  and 2 each of `TOOL-dUnstuckLanding-17`, `TOOL-dGroundRules-1` and `TOOL-aRoutedQuill-3`.
- Setting the strict operand's reads aside in the trace. That is a blind spot in the grader, and it
  lies outside this unit's non-goals besides.

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
sed -i '\#^      "memory/builds/dClosedLoop/build/",$#d' "$D/tools/gate-legs.json"
```

The leg's full run is a whole-suite form the bar join refuses in a criterion. AC1 runs the strict case
alone, which still runs the guard trace and the census check after it (`tools/policy/check_policy.py:4480-4483`).
The `policy fixtures` leg on §6 runs the whole leg at the close, through the main loop.

- **AC1** — When `python tools/policy/check_policy.py --fixture --strict-from memory/builds/dClosedLoop/build/ on-invalid-strict 2>&1 | grep -c "guard-trace.*WRONG"` runs, it prints `0`.
  The same run's `strict cell(s) in memory/builds/dClosedLoop/build/` line is present, which shows
  the case read v2 and the trace saw the read.
  Red when: the guard line is absent again. The staged break is the same command run from the root of
  `D`, which prints `1`, the `WRONG` line naming v2. At `591cb00d7` the same output follows from
  `:1875` and `:4042-4044`; this spec derived that from the code and did not run it.
- **AC2** — When `python tools/check-spec-tokens.py --legs-for memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -c "policy fixtures <-"` runs, it prints `1`.
  The same count over the v1 record, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md`,
  also prints `1`, which shows the line guards the directory and not one file. At `591cb00d7`
  both printed `0`.
  Red when: the line is left out of the guard, names only the v2 file (the v1 count reads `0`), or is
  spelled with a `{prefix}` token that resolves under `tools/`.
- **AC3** — When `git diff 591cb00d7 -- memory/guides/SESSION-KICKOFF.md | grep -c "^+last-audit: "` runs, it prints `1`.
  At `591cb00d7` it printed `0`.
  Red when: `tools/gate-legs.json` changes and the audit stamp does not move, which check 5 of
  `skills/session-kickoff/manifest-check.sh` refuses at commit.

## 6. Gates

`policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)` · `drift-audit records` · `memory hygiene`

The first four are the legs whose non-broad guard `tools/gate-legs.json` trips, as the guards join
reads them through `derive_guarded_legs`. `run-gates canary` is among them, because its guard names
`tools/gate-legs.json` beside the broad `tools/`, and `--legs-for` prints only the broad one. `recall floor` and
`recall floor arms` are the legs `memory/guides/SESSION-KICKOFF.md` trips, from `--legs-for` at
`591cb00d7`. The next four are the unguarded legs §4 "What the insert can move" names. They run on
every bar, so the guards join does not owe them, and they are named because the insert is in what
they read. The join, re-run through `derive_guarded_legs` with the directory line added, owes the
same six guarded legs as before. This unit adds no suite arm and declares no arm line.

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

- rev-2 · 2026-10-25 · §1 · S1 · §4 · AC1 · AC2 · AC3 · §6 · the builder handed back a divergence
  and committed nothing. Its patch is in the run's scratchpad, named
  TOOL-dGroundRules-69-divergence.patch. The file guard line spells `PLAY-dClosedLoop-1`, and
  `tools/gate-legs.json` sits in drift-audit's evidence globs. So the line becomes that INPROGRESS
  spec's first product citation, and the shrink-only set of signal
  `non_terminal_specs_cited_by_product_source` gains it, which reds `drift-audit records`. The
  builder also saw `gen_build_index` move dClosedLoop's Landed-unclosed column in `memory/LIVE.md`
  from 0 to 1.
  Ruling (main loop, measured at `591cb00d7`): guard the directory, rev-1's rejected alternative.
  §1, S1 and §4 "The guard line" now name the directory, with the cost restated at 141 of 619
  commits and 247 runs instead of 119. §4's table gains the `drift-audit records` row, checked with
  the engine's own id grammar, and §4's alternatives now list the file, the glob, narrowing the
  evidence globs and a trace set-aside. AC1's staged break deletes the directory line. AC2 adds the
  v1 path. The base moves to `591cb00d`, and AC1 to AC3 quote their baselines there; no watched
  file changed between `3d86915cf` and `591cb00d7`. §6 gains `drift-audit records`, an unguarded
  leg the guards join does not owe.

## 9. Reuse audit

Every seam this unit touches already exists, and it builds no new mechanism. The guard list is the
`policy fixtures` row of `tools/gate-legs.json`, the row `TOOL-dGroundRules-67` S1 extended. That row
is graded by `check_guard_trace` through `--legs-for` and by `check_guard_lines` through `git ls-files`.
The id check for the drift-audit signal reuses that engine's own grammar and adds no reader.
The stamp is the kickoff manifest's own `last-audit` key.
`python tools/codebase-map/reuse_lookup.py "add the strict case's source file to the policy fixtures gate leg guard list"`
ranked name stems only (`legs`, `leg`, `fixture`, `load_policy`), and none of them widens a guard. The
recall probe returned `TOOL-dGroundRules-37` and `TOOL-dGroundRules-33`, whose checks this line must
satisfy, and `TOOL-dGroundRules-67`, whose insert this one follows. It also returned asks
`TOOL-dGroundRules-109` and `TOOL-dGroundRules-111`, whose waiver rows this unit leaves as they stand.

Recall terms used: `python tools/memory-recall/query.py "policy fixtures guard misses the strict case's source read, on-invalid-strict traced only with --strict-from" --terms "guard-trace policy fixtures on-invalid-strict strict-from architecture-v2 gate-legs.json guard census names no file git tracks manifest-audit re-stamp"`
