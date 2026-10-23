# TOOL-dGroundRules-37 — every `policy fixtures` guard entry names a file git tracks, so the trace's sweep cannot widen the guard with a path no diff carries

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-37-deviation-25.md](../build/2026-10-23-build-TOOL-dGroundRules-37-deviation-25.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 1 at HIGH**, which shares item **H1** with id 7
(`TOOL-dGroundRules-36`) and id 22 (`TOOL-dGroundRules-35`). Id 1 is H1 seen from coherence:
`TOOL-dGroundRules-33` AC3 cannot pass on a correct build, and S4's only remedy is to add the
reported path to the `policy fixtures` row of `tools/gate-legs.json`, where an interpreter-tagged,
gitignored `.pyc` guards nothing, because a guard is a pathspec over the runner's `git diff` and git
never lists that file. This unit is id 1's promotion, and it closes the remedy rather than the
report: `check_guard_lines` holds every entry of the `policy fixtures` guard to the files git
tracks, so a guard line that matches nothing git lists is a `WRONG`, whichever unit wrote it. It
repairs `TOOL-dGroundRules-33`, which sits at order 11, so it builds at order 12.

## 2. Scope (IN)

- **S1** — The check. After `check_guard_trace` (`TOOL-dGroundRules-33` S3), `check_guard_lines`
  reads the `policy fixtures` row of the source's `<tool root>/gate-legs.json`, resolves `{prefix}`
  in each guard entry to the source's tool root, and runs
  `git -C <source top level> ls-files -- <entry>` for each. An entry that lists no file prints
  `policy-fixture: guard-trace · WRONG guard <entry> · names no file git tracks`.
  Observed by AC1, AC3.
- **S2** — The count. `check_guard_lines` prints `policy-fixture: guard-trace · <n> guard line(s)
  checked` first, and a manifest that does not parse or holds no `policy fixtures` row is a `WRONG`
  naming that row, never zero lines read as a pass. Observed by AC2, AC4.
- **S3** — The index, not the disk. `ls-files` reads the index, so a file that is on disk and
  ignored is a `WRONG` however often a warm cache rewrites it, and a new source file the builder has
  staged passes before its commit. This is the rule `TOOL-dGroundRules-33` S4's sweep now meets: a
  path it adds is one git tracks. Observed by AC1, AC3.

## 3. Non-goals (OUT)

- Keeping cache and ignored paths out of the trace: `TOOL-dGroundRules-35` and
  `TOOL-dGroundRules-36`. This unit holds the guard whatever reaches it.
- Any leg's guard but `policy fixtures`. The same rule over every row of `tools/gate-legs.json` is a
  manifest-wide lint with its own population, and no other row's sweep is fed by a trace.
- `govkit.py`'s own "matches no tracked path in the target" rule (`tools/govkit/govkit.py:4390`),
  which drops a kit descriptor's leg guard at install. The policy kit may not import a sibling kit.

### Edges

- **consumes-from** `TOOL-dGroundRules-33` — `check_guard_trace` and the S4 sweep's additions to the `policy fixtures` row, which S1 holds to the files git tracks

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `b9f7b5c4e`.

- `tools/check-spec-tokens.py:486-487` `read_tracked` is `git ls-files`, the index, and
  `print_legs_for` joins guards against that set.
- `git check-ignore -v` printed `.gitignore:1:__pycache__/` for a path under
  `tools/govkit/__pycache__/`, and `git ls-files` lists no `.pyc`.
- `TOOL-dGroundRules-33` S4: "each reported path is added to the `policy fixtures` row in this
  unit's commit"; its review id 1 found that a correct build reports the `.pyc`.
- `tools/govkit/govkit.py:4383-4392` drops a kit descriptor's leg guard that "matches no tracked
  path in the target" at install, the same rule in the deployer, which the policy kit cannot import
  (`tools/codebase-map/map_lib.py:1505`).

### The check

```text
check_guard_lines(top, troot):                 # after check_guard_trace, --fixture mode only
    rows = json.loads(<top>/<troot>/gate-legs.json)   WRONG naming "policy fixtures" if it fails
    row  = the row whose name is "policy fixtures"    WRONG naming it if absent
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
- **AC4** — When `NO_ROW` runs and then the same command runs, it prints a `guard-trace` `WRONG`
  naming `policy fixtures`.
  Red when: a guard the check cannot find reads as zero dead lines.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the check;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture`, the `guard-trace` join) · covers AC1 AC3 AC4 · a cache path, then an unstaged new file, appended to a scratch copy's `policy fixtures` guard, then the row's name respelled · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (HIGH, item H1) of the round-1 spec
  audit of units 33 and 34, closing the remedy its S4 names, with `read_tracked`, the ignore rules
  and govkit's own guard refusal read on 2026-10-23.

## 10. Reuse audit

The seams extended are `check_guard_trace` (`TOOL-dGroundRules-33` S3) and `git ls-files`, the same
index read `read_tracked` (`tools/check-spec-tokens.py:486-487`) joins guards against, so a guard
entry is held to the set the guard is evaluated over. govkit's "matches no tracked path in the
target" rule (`tools/govkit/govkit.py:4390`) states the same rule for a descriptor's leg guards at
install and cannot be imported across kits (§3).
`python tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"`
ranked `git`, `run_git` and `read_git_output`, none of which grades a guard: no existing seam fits
the check itself. The recall probe returned `TOOL-dGroundRules-33` and this audit's H1; both agree
with source.

Recall terms used: `python tools/memory-recall/query.py "how does a file-access trace treat bytecode
caches, ignored paths and the git directory" --terms "audit hook trace pycache bytecode gitignored
guard-trace policy fixtures legs-for git-dir worktree"`
