# TOOL-dGroundRules-37 — every `policy fixtures` guard entry names a file git tracks, so the trace's sweep cannot widen the guard with a path no diff carries

**Status:** CLOSED · rev-4 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-37-deviation-25.md](../build/2026-10-23-build-TOOL-dGroundRules-37-deviation-25.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-37-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-37-ledger.md) | journal | — |
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-23-prompt-TOOL-dGroundRules-37-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-37-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-36-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-36-staleness-probe-brief.md) | research | TOOL-dGroundRules-36 TOOL-dGroundRules-38 |
| [2026-10-24-prompt-TOOL-dGroundRules-37-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-37-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-37-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-37-probe-fix-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-32-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-32-close-arms-brief.md) | research | TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-43 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-65 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 1 at HIGH**, which shares item **H1** with id 7
(`TOOL-dGroundRules-36`) and id 22 (`TOOL-dGroundRules-35`). Id 1 is H1 seen from coherence:
`TOOL-dGroundRules-33` AC3 could not pass on a correct build, and its sweep's only remedy was to add
the reported path to the `policy fixtures` row of `tools/gate-legs.json`, where an
interpreter-tagged, gitignored `.pyc` guards nothing, because a guard is a pathspec over the
runner's `git diff` and git never lists that file.

On the branch after `TOOL-dGroundRules-35` (commit 764a8a282) a warm load records
`tools/govkit/govkit.py`, not its `.pyc`, so a correct build reports that path no more; only a cache
name `source_from_cache` refuses still reaches the join as spelled. The remedy is unchanged: the
sweep writes each reported path into the row, and nothing holds an entry to the files git tracks.
The trace's own join cannot, because a guard trips by its literal spelling, tracked or not (§4).
Deviation 78 of `TOOL-dGroundRules-33` puts that sweep at the close: the first `--fixture` run over
the built tree is the close's `policy fixtures` leg, and the paths it reports are added to the row
there. This unit is id 1's promotion, and it closes the remedy rather than the report:
`check_guard_lines` holds every entry of the `policy fixtures` guard to the files git tracks, so a
guard line that matches nothing git lists is a `WRONG`, whether the close's sweep or any unit wrote
it. It repairs `TOOL-dGroundRules-33`, which sits at order 11, so it builds at order 12.

## 2. Scope (IN)

- **S1** — The check. After `check_guard_trace` (`TOOL-dGroundRules-33` S3), `check_guard_lines`
  reads the `policy fixtures` row of the source's `<tool root>/gate-legs.json`, resolves `{prefix}`
  in each guard entry to the source's tool root, and runs
  `git -C <source top level> ls-files -- <entry>` for each. An entry that lists no file prints
  `policy-fixture: guard-trace · WRONG guard <entry> · names no file git tracks`.
  Observed by AC1, AC3.
- **S2** — The count. `check_guard_lines` prints `policy-fixture: guard-trace · <n> guard line(s) checked`
  ahead of its entry lines. A manifest that does not parse prints
  `policy-fixture: guard-trace · WRONG: the manifest did not parse: <error>, so no guard line was checked`,
  and one with no row of that name prints
  `policy-fixture: guard-trace · WRONG: the manifest holds no policy fixtures row, so no guard line was checked`,
  never zero lines read as a pass. Observed by AC2, AC4.
- **S3** — The index, not the disk. `ls-files` reads the index, so a file that is on disk and
  ignored is a `WRONG` however often a warm cache rewrites it, and a new source file the builder has
  staged passes before its commit. This is the rule the close's sweep meets, the one deviation 78 of
  `TOOL-dGroundRules-33` hands to the close's first `policy fixtures` run: each path it adds to the
  row is one git tracks, and the leg's next run reds one that is not. Observed by AC1, AC3.

## 3. Non-goals (OUT)

- Keeping cache and ignored paths out of the trace: `TOOL-dGroundRules-35` and
  `TOOL-dGroundRules-36`. This unit holds the guard whatever reaches it.
- Any leg's guard but `policy fixtures`. The same rule over every row of `tools/gate-legs.json` is a
  manifest-wide lint with its own population, and no other row's sweep is fed by a trace.
- `govkit.py`'s own "matches no tracked path in the target" rule (`tools/govkit/govkit.py:4390`),
  which drops a kit descriptor's leg guard at install. The policy kit may not import a sibling kit.

### Edges

- **consumes-from** `TOOL-dGroundRules-33` — `check_guard_trace`, and the additions the close's sweep (that unit's deviation 78) makes to the `policy fixtures` row, which S1 holds to the files git tracks
- **hands-off** `TOOL-dGroundRules-52` — `check_guard_lines`, which that unit takes out in favour of arm 1b of `tools/run-gates/run-gates.test.sh`, where this unit's arm line is then observed (ids 19, 9 and 37 of the round-1 spec audit of units 35 to 43)

## 4. Design

### Evidence

Every line below was read on 2026-10-24 at 7106e5abc, the branch after `TOOL-dGroundRules-35`,
except the ignore probe, run on 2026-10-23 at b9f7b5c4e.

- The join as built. `print_legs_for` (`tools/check-spec-tokens.py:592`) takes the set
  `read_tracked` (`tools/check-spec-tokens.py:479`) builds from `git ls-files`, the index, and uses
  it only to mark a path ` (not tracked at HEAD)` and to refuse an input none of whose paths is
  tracked. The trips come from `derive_tripped_legs` (`tools/check-spec-tokens.py:580`), which
  tests each literal guard through `check_guard_trips` and never reads that set. So a guard entry
  spelled as the path it covers trips that path, tracked or not, and `check_guard_trace`
  (`tools/policy/check_policy.py:3777`) reads the path as covered: its join cannot see a dead entry.
- `read_legs_for` (`tools/policy/check_policy.py:3656`) strips the ` (not tracked at HEAD)` mark from
  each path line and raises on a non-zero exit, so the mark reaches no caller and an all-untracked
  input arrives as a checker failure.
- `TOOL-dGroundRules-35`: `add_source_read` (`tools/policy/check_policy.py:3748`) keeps a
  `__pycache__` read as the source `importlib.util.source_from_cache` names, so a warm load records
  `tools/govkit/govkit.py`; a cache name that call refuses is kept as spelled. Review id 1's premise,
  that a correct build reports the `.pyc`, holds no more on this branch; the unchecked remedy holds.
- Deviation 78 of `TOOL-dGroundRules-33`
  (`memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-33-deviation-78.md`): that
  unit's commit adds `{prefix}/govkit/selftest.py` alone, and the paths the close's first
  `policy fixtures` run reports are added to the row there, after units 35 to 38. That sweep is the
  writer this check holds.
- `git check-ignore -v` printed `.gitignore:1:__pycache__/` for a path under
  `tools/govkit/__pycache__/`, and `git ls-files` lists no `.pyc`.
- `tools/govkit/govkit.py:4383-4392` drops a kit descriptor's leg guard that "matches no tracked
  path in the target" at install, the same rule in the deployer, which the policy kit cannot import
  (`tools/codebase-map/map_lib.py:1505`).

### The check

```text
check_guard_lines(top, troot):                 # after check_guard_trace, --fixture mode only
    rows = json.loads(<top>/<troot>/gate-legs.json)   WRONG "the manifest did not parse: <error>" if it fails
    row  = the row whose name is "policy fixtures"    WRONG "the manifest holds no policy fixtures row" if absent
    print "policy-fixture: guard-trace · <len(row guard)> guard line(s) checked"
    for entry in row guard:
        spec = entry with "{prefix}" as troot
        if git -C top ls-files -- spec prints nothing:
            print "policy-fixture: guard-trace · WRONG guard <entry> · names no file git tracks"
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_guard_lines` | py.function | `tools/policy/check_policy.py` |
| `WRONG guard` | a `guard-trace` line | `tools/policy/check_policy.py` |

`lexicon.py --suggest check_guard_lines --as py.function` answered OK on 2026-10-23.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The `--legs-for` mark as the judge.** `read_legs_for` strips it, and a guard of dead entries
  alone is refused whole, so the dead entries would read as a checker failure, never by name.
- **The sweep told in prose not to add a cache path.** A rule in one unit's §2 binds that pass only;
  the next unit that reads a new kind of path meets the same remedy with nothing to stop it.
- **An entry held to a path that exists on disk.** The warm cache exists, so the `.pyc` would pass.
- **Every row of the manifest.** Outside this build's scope (§3).

## 5. Production-readiness checklist

- security — N/A: read-only `git ls-files` queries and one manifest read.
- perf / scale — one `ls-files` run per guard entry of one row, once per `--fixture` run.
- error / empty / loading states — an unreadable manifest or a missing row is a named `WRONG`.
- observability — the checked-lines count and one `WRONG guard` line per dead entry.
- risks — an entry for a file the builder has not staged reds until it is staged; the line says why.
- testing — AC1 to AC4.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: a gov-only leg.

## 6. Acceptance criteria

Every command runs from the repository root, in a scratch copy of the built tree. `check_policy.py`
names the policy kit's file under the kit, as `TOOL-dGroundRules-33` §6 does. Literal stagings are
spelled whole here and named by the criteria:

```text
WARM_CACHE  = python -c "import py_compile; py_compile.compile('tools/govkit/govkit.py')"
PYC_GUARD   = in the copy's tools/gate-legs.json, "{prefix}/govkit/__pycache__/govkit.cpython-314.pyc"
              appended to the "policy fixtures" row's guard list
NEW_GUARD   = tools/govkit/probe_new.py created in the copy, and "{prefix}/govkit/probe_new.py"
              appended to the same guard list
STAGE_NEW   = git add tools/govkit/probe_new.py, in the copy
NO_ROW      = the "policy fixtures" row's name respelled in the copy's tools/gate-legs.json
```

- **AC1** — When `WARM_CACHE` and `PYC_GUARD` run and then
  `python check_policy.py --fixture budgets-ships-join` runs, it prints a `WRONG guard` line naming
  `__pycache__` and `names no file git tracks`.
  Red when: the sweep's remedy writes a gitignored, interpreter-tagged path into the guard silently.
- **AC2** — When the same command runs in an unmodified copy, it prints the `guard line(s) checked`
  line with a count above zero and no `WRONG guard` line.
  Red when: a live guard entry is reported dead, or the check reads no entry at all.
  figure: the count is DERIVED from the manifest at observation time.
- **AC3** — When `NEW_GUARD` runs and then the same command runs, it prints a `WRONG guard` line
  naming `probe_new.py`; when `STAGE_NEW` runs and the command runs again, it prints no
  `WRONG guard` line.
  Red when: the check reads the disk rather than the index git diffs.
- **AC4** — When `NO_ROW` runs and then the same command runs, it prints a `guard-trace` line
  holding `WRONG: the manifest holds no policy fixtures row`.
  Red when: a guard the check cannot find reads as zero dead lines; `check_guard_trace`'s own
  `not under the policy fixtures guard` lines do not hold that text, so they cannot pass it.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the check;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture`, the `guard-trace` join) · covers AC1 AC3 AC4 · a cache path, then an unstaged new file, appended to a scratch copy's `policy fixtures` guard, then the row's name respelled · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (HIGH, item H1) of the round-1 spec
  audit of units 33 and 34, closing the remedy its S4 names, with `read_tracked`, the ignore rules
  and govkit's own guard refusal read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.
- rev-3 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.
- rev-4 · 2026-10-24 · §1 §2 §3 §4 §6 §10 · four disagreements a read-only probe of 7106e5abc found,
  each ruled to the source. §4 had `print_legs_for` joining guards against the tracked set; trips
  come from `derive_tripped_legs` and the set only marks and refuses, so §4 and §10 restate the join
  and the reuse claim by symbol. §1 and §4 held that a correct build reports the `.pyc`, which
  `TOOL-dGroundRules-35` ended; the premise is restated as the unchecked remedy. S3 bound
  `TOOL-dGroundRules-33` S4's sweep, which that unit's deviation 78 puts at the close; §1, S3, §4 and
  the edge bind the close's sweep. AC4 was green at HEAD on `check_guard_trace`'s own line; S2 now
  spells this unit's no-row line and AC4 matches it.

## 10. Reuse audit

The seams extended are `check_guard_trace` (`TOOL-dGroundRules-33` S3) and `git ls-files`, the
index `read_tracked` (`tools/check-spec-tokens.py:479`) reads. The legs join holds no guard entry to
that index: `print_legs_for` uses the set only to mark and to refuse, and `derive_tripped_legs`
trips by the literal guard alone (§4). This check adds the hold the join lacks, over the set the
runner's `git diff` draws from, and the join's own mark is not reused as its judge (§4, Alternatives
rejected). govkit's "matches no tracked path in the target" rule (`tools/govkit/govkit.py:4390`)
states the same rule for a descriptor's leg guards at install and cannot be imported across kits
(§3).
`python tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"`
ranked `git`, `run_git` and `read_git_output`, none of which grades a guard: no existing seam fits
the check itself. The recall probe returned `TOOL-dGroundRules-33` and this audit's H1; both agree
with source.

Recall terms used: `python tools/memory-recall/query.py "how does a file-access trace treat bytecode
caches, ignored paths and the git directory" --terms "audit hook trace pycache bytecode gitignored
guard-trace policy fixtures legs-for git-dir worktree"`
