# TOOL-dGroundRules-36 — a source read git ignores is set aside before the guard join, counted, and never offered to the guard

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-36-deviation-24.md](../build/2026-10-23-build-TOOL-dGroundRules-36-deviation-24.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 7 at HIGH**, which shares item **H1** with id 1
(`TOOL-dGroundRules-37`) and id 22 (`TOOL-dGroundRules-35`). Id 7 is H1 seen from grounding: the
`open` audit event fires on the attempt, so `TOOL-dGroundRules-33` S2 keeps a path git ignores on
every run, and its S4 sweep then tells the builder to put that path into `tools/gate-legs.json`. A
path git ignores never appears in the runner's `git diff`, so no guard can ever be tripped by it.
This unit is id 7's promotion: `check_guard_trace` asks git which kept paths it ignores, sets them
aside with a count, and joins only the rest to the guard. It repairs `TOOL-dGroundRules-33`, which
sits at order 11, so it builds at order 12.

## 2. Scope (IN)

- **S1** — The set-aside. Before the `--legs-for` pipe, `derive_guardable_reads(kept, top)` runs
  `git -C <source top level> check-ignore --stdin` over the kept paths and returns the kept paths
  git did not print. Exit 0 and exit 1 are both answers, exit 1 meaning none is ignored; any other
  exit, or a `git` that does not start, is a `guard-trace` `WRONG` naming `check-ignore`, never a
  pass. Observed by AC1, AC2, AC4.
- **S2** — The count. `check_guard_trace` prints
  `policy-fixture: guard-trace · <n> ignored read(s) set aside` after its count line, on every run,
  so a set-aside is visible rather than read as coverage. Observed by AC1, AC3.
- **S3** — The join's population. `TOOL-dGroundRules-33` S3's pipe and its empty-trace `WRONG` read
  the guardable paths S1 returns, and its S4 sweep adds to the `policy fixtures` row only a path that
  the join reported, so an ignored path is never offered to the guard. A tracked file that an ignore
  pattern happens to match stays guardable, because `check-ignore` without `--no-index` answers for
  untracked paths only. Observed by AC1, AC2, AC3.

## 3. Non-goals (OUT)

- Mapping a bytecode cache to its source: `TOOL-dGroundRules-35`, which keeps the warm read of
  `govkit.py` visible; this unit sets aside whatever ignored path is left.
- The source's git directory, which `check-ignore` does not report: `TOOL-dGroundRules-38`.
- A guard line that names an ignored path: `TOOL-dGroundRules-37`.
- Untracked paths that git does not ignore. A new source file a case reads before its commit is
  still joined, which is the coverage `TOOL-dGroundRules-43`'s parse of the `(not tracked at HEAD)`
  header keeps exact.

### Edges

- **consumes-from** `TOOL-dGroundRules-33` — `check_guard_trace`, its pipe to `--legs-for` and the S4 sweep, whose population S1 narrows to the paths git does not ignore
- **hands-off** `TOOL-dGroundRules-52` — `derive_guardable_reads`, whose `check-ignore` call that unit pins to `-z` and bytes (ids 13 and 33 of the round-1 spec audit of units 35 to 43)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `b9f7b5c4e`.

- `.gitignore` holds `__pycache__/` and `*.pyc`, and nothing else.
- In the main checkout, `git check-ignore --stdin -v` over `.git/index`, `.git/info/exclude`, a
  path under `tools/govkit/__pycache__/` and `README.md` printed only the `__pycache__` line and
  exited 0; over `.git/index` and `README.md` alone it printed nothing and exited 1.
- `tools/check-spec-tokens.py:637-677` `print_legs_for` still evaluates a path it marks
  ` (not tracked at HEAD)`, and refuses with exit 2 when every path given is untracked (`:659-664`).
- `TOOL-dGroundRules-33` §4 "The trace" pipes every kept path, with no filter.

### The set-aside

```text
derive_guardable_reads(kept, top):
    rc, out = run(git -C top check-ignore --stdin, stdin = "\n".join(kept))
    if git did not start or rc not in (0, 1): raise the guard-trace WRONG naming check-ignore
    ignored = set(out.splitlines())
    return [p for p in kept if p not in ignored], len(ignored)

check_guard_trace():                             # TOOL-dGroundRules-33, this unit's lines marked +
    print "policy-fixture: guard-trace · <len(kept)> source read(s)"
+   guardable, n = derive_guardable_reads(kept, source top level)
+   print "policy-fixture: guard-trace · <n> ignored read(s) set aside"
    WRONG if guardable is empty
    out = run(python <source tool root>/check-spec-tokens.py --legs-for -, stdin = guardable)
    (unit 33's per-path verdict, over guardable)
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_guardable_reads` | py.function | `tools/policy/check_policy.py` |
| `ignored read(s) set aside` | a `guard-trace` line | `tools/policy/check_policy.py` |

`lexicon.py --suggest derive_guardable_reads --as py.function` answered OK on 2026-10-23.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Keep only paths tracked at HEAD**, the review's fix. A new source file a case reads before the
  unit's commit is untracked and would go unjoined until it is committed, so a pass could verify
  with the guard blind to the file it just added. Ignored paths are the ones no guard can trip, and
  that is the set this unit names.
- **A list of ignored directories typed into `check_policy.py`.** A second carrier of the rule
  `.gitignore` and the exclude file already hold.

## 5. Production-readiness checklist

- security — N/A: one read-only `git` query over paths the process already opened.
- perf / scale — one `check-ignore` run per `--fixture` run.
- error / empty / loading states — an unreachable `check-ignore` is a named `WRONG`; a trace whose
  every read is ignored is the existing empty-trace `WRONG`.
- observability — the set-aside count line, printed on every run.
- risks — a source file a repository ignores but a case reads is set aside; the count line shows it.
- testing — AC1 to AC4.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: a gov-only leg.

## 6. Acceptance criteria

Every command runs from the repository root, in a scratch copy of the built tree. `check_policy.py`
names the policy kit's file under the kit, as `TOOL-dGroundRules-33` §6 does. Literal stagings are
spelled whole here and named by the criteria:

```text
PLANT_IGNORED = create probe.pyc at the copy's top level, and stage one open() of it, read mode,
                into the first line of build_fresh_target
UNIGNORE      = in the copy's .gitignore, the line "*.pyc" taken out
```

- **AC1** — When `PLANT_IGNORED` runs and then `python check_policy.py --fixture adopter-fresh-target`
  runs, it prints `ignored read(s) set aside` with a count of 1 or more and no `guard-trace` line
  naming `probe.pyc`.
  Red when: a path git ignores reaches the guard join and is reported as a guard miss.
- **AC2** — When `PLANT_IGNORED` and `UNIGNORE` both run and then the same command runs, it prints
  `guard-trace · WRONG probe.pyc`.
  Red when: the set-aside is decided by a name pattern of its own rather than by git's ignore rules,
  or swallows a path git does not ignore.
- **AC3** — When `python check_policy.py --fixture` runs on the built tree, it prints the
  `ignored read(s) set aside` line and no `guard-trace` `WRONG`.
  Red when: the count line is printed only when the count is non-zero, so a set-aside of nothing
  cannot be told from a step that never ran.
  figure: the count is DERIVED from the run.
- **AC4** — When `derive_guardable_reads` is staged in a copy to call a program name that does not
  resolve in place of `git`, the AC1 command prints a `guard-trace` `WRONG` naming `check-ignore`.
  Red when: a failed ignore query is read as "nothing ignored".

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the trace;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture`, the `guard-trace` join) · covers AC1 AC2 · an ignored file planted and read in process, then its ignore line staged out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 7 (HIGH, item H1) of the round-1 spec
  audit of units 33 and 34, from the review's fix narrowed to the paths git ignores, with
  `check-ignore` and `print_legs_for` read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.

## 10. Reuse audit

The seams extended are `check_guard_trace` (`TOOL-dGroundRules-33` S3) and git's own ignore
evaluation, `git check-ignore --stdin`, which reads `.gitignore`, the exclude file and
`core.excludesFile` exactly as `git status` does, so the unit spells no pattern of its own.
`python tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"`
ranked `git`, `run_git`, `read_git_output` and `build_git_env`, which run git and never ask it about
ignores: no existing seam fits the set-aside itself. The recall probe returned
`TOOL-dGroundRules-33`, this audit's H1, and `TOOL-aGraftedHelix-16`'s audit item M6, where bytecode
caches were staged into a commit; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how does a file-access trace treat bytecode
caches, ignored paths and the git directory" --terms "audit hook trace pycache bytecode gitignored
guard-trace policy fixtures legs-for git-dir worktree"`
