# TOOL-dGroundRules-52 — the round-1 audit of units 35 to 43, its minors: twenty-five findings closed in the code and the observations those units leave, one scope item each

**Status:** DEFERRED · rev-6 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 16 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-52-deviation-40.md](../build/2026-10-23-build-TOOL-dGroundRules-52-deviation-40.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-52-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-52-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-51-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-51-staleness-probe-brief.md) | research | TOOL-dGroundRules-51 |
| [2026-10-24-prompt-TOOL-dGroundRules-52-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-52-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-52-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-52-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-52-3-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-52-3-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-52-edge-repair-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-52-edge-repair-brief.md) | research | TOOL-dGroundRules-45 TOOL-dGroundRules-60 TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-57 TOOL-dGroundRules-58 |
| [2026-10-24-prompt-TOOL-dGroundRules-52-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-52-probe-fix-brief.md) | research | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with 33 confirmed findings. Its BLOCKER and seven HIGH ids are promoted one unit each,
`TOOL-dGroundRules-44` to `TOOL-dGroundRules-51`. BUILD-METHOD M4 promotes the other twenty-five,
sixteen MEDIUM and nine LOW, batched into one unit, and this is that unit. They land on units 35 to
41 and 43. They do not split into two disjoint write sets by M6's clauses: every item that changes
code writes `tools/policy/check_policy.py`, and the rest write nothing. It repairs no unit in
particular. It builds at order 16, the one unit at that step: after `TOOL-dGroundRules-43` at order
14, whose S9 event filter and S10 forwarding S20 and S16 need, and before the steps at orders 17,
18 and 20.

Units 1 to 41 are built at `8eab342e0`, so most items here are closed already, by the unit they land
on or by a sibling, and each is recorded with the observation that confirms it. The code items left
are S6 with S14, S15, S20 and S25, all in `tools/policy/check_policy.py`.

Ids 30, 31, 3, 12 and 25 are the medium halves of H1, H2 and H3, and ids 7 and 14 are one defect at
two grades; the review keeps each apart only by its binding grade. Each still takes its own scope
item. Each finding is taken at the binding severity the report gives it.

| Finding id | Severity | Review item | Unit it lands on | Scope item | Criterion |
|---|---|---|---|---|---|
| 3 | MEDIUM | M3 | 43 | S1 | AC1 |
| 4 | MEDIUM | M4 | 35 | S2 | AC2 |
| 5 | MEDIUM | M7 | 38 | S3 | AC3 |
| 6 | MEDIUM | M8 | 34 to 39, 41 | S4 | AC4 |
| 12 | MEDIUM | M3 | 43 | S5 | AC1, AC5 |
| 13 | MEDIUM | M6 | 36 | S6 | AC6 |
| 14 | MEDIUM | M5 | 43 | S7 | AC7 |
| 15 | MEDIUM | M9 | 38 | S8 | AC8 |
| 19 | MEDIUM | M10 | 37 | S9 | AC9 |
| 25 | MEDIUM | M3 | 43 | S10 | AC1 |
| 26 | MEDIUM | M11 | 39 | S11 | AC10 |
| 30 | MEDIUM | M1 | 40, 43 | S12 | AC5 |
| 31 | MEDIUM | M2 | 41 | S13 | AC11 |
| 33 | MEDIUM | M6 | 36 | S14 | AC12 |
| 35 | MEDIUM | M12 | 35 | S15 | AC13 |
| 36 | MEDIUM | M13 | 43 | S16 | AC14 |
| 7 | LOW | L1 | 43 | S17 | AC7 |
| 8 | LOW | L2 | 38 | S18 | AC15 |
| 9 | LOW | L3 | 37 | S19 | AC16 |
| 16 | LOW | L4 | 35 | S20 | AC17 |
| 17 | LOW | L5 | 40 | S21 | AC5 |
| 18 | LOW | L6 | 43 | S22 | AC18 |
| 34 | LOW | L7 | 35 | S23 | AC19 |
| 37 | LOW | L8 | 37 | S24 | AC20 |
| 38 | LOW | L9 | 35 | S25 | AC21 |

Each item's fix is the one the skeptic judged sound; for id 16 and id 35 it is the skeptic's
corrected fix. For id 19 the run kept `check_guard_lines` (S9), and for id 36 the §4 Evidence shows
the relative value already resolving against the source (S16).

## 2. Scope (IN)

- **S1** — Finding 3. Closed by `TOOL-dGroundRules-43` rev-5 (`6e8863f43`), whose `EVIDENCE` reads
  the build README whole, so that unit's AC3 is observed through the file the build-order region
  sits in. S1 owes no code. Observed by AC1.
- **S2** — Finding 4. Built by `TOOL-dGroundRules-35` (`764a8a282`): the cache mapping is observed
  directly, not through the absence of a `WRONG` that `TOOL-dGroundRules-36`'s set-aside can hide.
  `KEPT_PROBE` feeds `add_source_read` a cache read, an `.opt-1` cache read and importlib's
  temporary write, and prints `SOURCE_READS`. Observed by AC2.
- **S3** — Finding 5. `TOOL-dGroundRules-38` S3's claim about `TOOL-dGroundRules-34`'s in-process
  read of the exclude file is observed in a primary clone with the git-directory rule staged out:
  the trace names the clone's exclude file. Both units are built, so S3 owes no code. Observed by AC3.
- **S4** — Finding 6. Closed by `derive_parallel_step` in `tools/memory-tree/gen_build_index.py`,
  built by `TOOL-dGroundRules-25` (`b663756ca`): steps 12, 13 and 14 of the build-order region, each
  holding four or more units, render `no`. S4 owes no code. Observed by AC4.
- **S5** — Finding 12. Its AC3 half is closed as S1 says; its AC1 half is `TOOL-dGroundRules-43`
  AC1, observed through `PAIRS_PY` and `PAIRS_SH` of `TOOL-dGroundRules-40` §6. Observed by AC1,
  AC5.
- **S6** — Finding 13. `derive_guardable_reads` (`TOOL-dGroundRules-36`, `cc4b4e53b`) already sends
  bytes to `git check-ignore --stdin`. This unit adds the rest: `-z`, each kept path `os.fsencode`d
  and NUL-terminated, the output split on NUL and each path `os.fsdecode`d, and a count that is the
  number of kept paths matching an output path, not the number of output lines. Observed by AC6.
- **S7** — Finding 14. Closed by `TOOL-dGroundRules-43` rev-5's `ORDER_SHIFT`, which picks a unit of
  a step holding two or more units (step 1 holds two), the observation that unit's AC6 makes. S7
  owes no code. Observed by AC7.
- **S8** — Finding 15. `TOOL-dGroundRules-38` AC1 is observed in `CLONE_AT`, a clone checked out at
  the commit under test, so the clone grades committed bytes of the unit and not the source's default
  branch. That unit is built (`8b50fc8bb`), so S8 owes no code. Observed by AC8.
- **S9** — Finding 19. `check_guard_lines` (`TOOL-dGroundRules-37`, `7a600abf5`) stays whole in
  `tools/policy/check_policy.py`, with its one call in `run_fixture`, because
  `TOOL-dGroundRules-43` rev-5 AC8, AC9, AC11 and AC12 rest on its finding no dead guard entry. Arm
  1b of `tools/run-gates/run-gates.test.sh` holds the same rule under the `run-gates canary` guard;
  S9 takes out no part of either and owes no code. Observed by AC9.
  **Readers:** by name: `run_fixture`, the one caller, in `tools/policy/check_policy.py`.
  by value: NO VALUE READERS — the lines it prints are parsed by no code, only read by criteria.
- **S10** — Finding 25. Closed as S1 says. Observed by AC1.
- **S11** — Finding 26. `TOOL-dGroundRules-39` AC2 and AC3 are observed in `CLONE_AT`, a git
  repository, and each requires a `WRONG` line naming `census-window-edge` and no `WRONG` line naming
  `rev-parse`, `check-ignore` or `policy fixtures`. Unit 39 is built, so S11 owes no code.
  Observed by AC10.
- **S12** — Finding 30. `TOOL-dGroundRules-40` AC2 and `TOOL-dGroundRules-43` AC1 are observed
  through `PAIRS_PY` and `PAIRS_SH` of `TOOL-dGroundRules-40` §6, built at `942581c64`. S12 owes no
  code. Observed by AC5.
- **S13** — Finding 31. `TOOL-dGroundRules-41` AC4 and AC5 are observed through that unit's own
  `INSTALL_LINES` and `HELP_LEGS` (rev-4, built at `277c9e37f`), each spelling the page whole as
  `help/policy.md`. S13 owes no code. Observed by AC11.
- **S14** — Finding 33. S6's `-z` output is never C-quoted, so a gitignored path holding a non-ASCII
  byte, a double quote or a backslash is matched and set aside like any other. Observed by AC12.
- **S15** — Finding 35. When `sys.pycache_prefix` is set, `--fixture` prints
  `policy-fixture: guard-trace · WRONG sys.pycache_prefix is set` and runs no case, because a cache
  read under a prefix has no `__pycache__` parent to map from. Observed by AC13.
- **S16** — Finding 36. Closed without code once `TOOL-dGroundRules-43` S10 is built: the snapshot's
  `add -A` runs with the source as its work tree, and git reads a relative `core.excludesFile`
  against the work tree's top level (§4 Evidence), so the value that unit forwards already resolves
  against the source. Observed by AC14.
- **S17** — Finding 7. The same closure as S7, taken at the grade the review binds for id 7.
  Observed by AC7.
- **S18** — Finding 8. Built by `TOOL-dGroundRules-38` (`8b50fc8bb`): `read_source_git_dirs`
  raises naming `rev-parse` when git does not answer both directories, and `run_fixture` prints
  that as a `guard-trace` `WRONG` and runs no case. S18 owes no code. Observed by AC15.
- **S19** — Finding 9. A manifest that does not parse is a `guard-trace` `WRONG` twice over:
  `check_guard_lines` says so, and the trace's `--legs-for` call fails, which `check_guard_trace`
  prints as a `WRONG`. Both are built, so S19 owes no code. Observed by AC16.
- **S20** — Finding 16. The `.pyc` digit-tail cut of `TOOL-dGroundRules-35` S1 is taken out of
  `add_source_read`, because `TOOL-dGroundRules-43` S9 skips importlib's temporary write, a mode-None
  `open` carrying `O_CREAT`, before the path steps, so the cut sees no input. The cold case is
  observed with bytecode writing on. Observed by AC17.
- **S21** — Finding 17. Closed by `TOOL-dGroundRules-40`'s arm in `tools/check-spec-tokens.test.sh`,
  which grades `check_writes_intersect` and `overlaps` over `OVERLAP_PAIRS`; `TOOL-dGroundRules-40`
  §3's "both answer correctly today" is now graded for both rules. S21 owes no code. Observed by AC5.
- **S22** — Finding 18. `TOOL-dGroundRules-43` AC13 is paired with its staged break: a local-state
  file tracked in a scratch copy makes the count 1. Observed by AC18.
- **S23** — Finding 34. Built by `TOOL-dGroundRules-33` (`eb67e2cc8`): `add_source_read`, the audit
  hook whose reads `check_guard_trace` joins, reads the `open` event's path with `os.fsdecode`, so a
  str, a bytes and a path-like path are one spelling. S23 owes no code. Observed by AC19.
- **S24** — Finding 37. A `policy fixtures` row whose guard list is empty makes the trace print a
  `guard-trace` `WRONG` for every traced read, since no read trips the leg. This is built, so S24
  owes no code. Observed by AC20.
- **S25** — Finding 38. A cache name that `source_from_cache` refuses is kept as spelled, which
  `TOOL-dGroundRules-35` built (`764a8a282`). This unit adds the line: such a read is also kept in
  `UNMAPPED_READS`, and `check_guard_trace` prints
  `policy-fixture: guard-trace · unmapped cache read <path>` for each before
  `TOOL-dGroundRules-36`'s set-aside, so the read is named rather than counted. Observed by AC21.

## 3. Non-goals (OUT)

- The BLOCKER and HIGH ids: `TOOL-dGroundRules-44` to `TOOL-dGroundRules-51`.
- Rewriting any reviewed spec's text. Each defect a spec stated is closed here in the code and the
  observation it governs, and each repaired unit's §3 names this unit; nothing is folded
  (BUILD-METHOD M4).
- Renumbering any unit's `order`, and adding edges among units 34 to 41. S4 observes the order the
  render derives; dispatch is sequential within a step (`tools/workflows/unattended-build.js`, its
  `DISPATCH IS STRICTLY SEQUENTIAL` comment).
- Taking `check_guard_lines` out in favour of arm 1b of `tools/run-gates/run-gates.test.sh`: the
  criteria of `TOOL-dGroundRules-43` named in S9 rest on it.
- Any literal of `TOOL-dGroundRules-51`, `-53`, `-54`, `-57`, `-58` or `-59`; no criterion here
  consumes one.

### Edges

- **consumes-from** `TOOL-dGroundRules-32` — `check_writes_intersect`, which S21 observes graded by `TOOL-dGroundRules-40`'s arm, and `derive_parallel_step`, which calls it and whose rendering of steps 12 to 14 S4 observes
- **consumes-from** `TOOL-dGroundRules-33` — `add_source_read`, `check_guard_trace` and its `--legs-for` failure `WRONG`, which S19, S23 to S25 amend or observe
- **consumes-from** `TOOL-dGroundRules-35` — the cache mapping and its digit-tail cut, which S2, S15, S20, S23 and S25 observe or amend
- **consumes-from** `TOOL-dGroundRules-36` — `derive_guardable_reads`, whose call S6 and S14 pin to `-z`, `os.fsencode` and a matched count
- **consumes-from** `TOOL-dGroundRules-37` — `check_guard_lines`, which S9 keeps and S19 observes
- **consumes-from** `TOOL-dGroundRules-38` — `read_source_git_dirs`, `UNEXCLUDE`, its S3 claim and its AC1, which S3, S8 and S18 observe
- **consumes-from** `TOOL-dGroundRules-39` — `census-window-edge`, `DEPTH3_LIVE`, `TOPLEVEL` and the criteria AC2 and AC3, which S11 observes in a git clone
- **consumes-from** `TOOL-dGroundRules-40` — `PAIRS_PY`, `PAIRS_SH`, `RAW_BOTH` and the arm over `OVERLAP_PAIRS`, through which S5, S12 and S21 observe
- **consumes-from** `TOOL-dGroundRules-41` — `INSTALL_LINES`, `HELP_LEGS` and `HELP_MOVED`, through which S13 observes that unit's AC4 and AC5
- **consumes-from** `TOOL-dGroundRules-43` — `build_source_snapshot`, the S9 event filter, `EVIDENCE`, `ORDERS`, `ORDER_SHIFT`, `EXCLUDES_REPO`, `SNAP_PROBE` and the criteria AC1, AC3, AC6 and AC13, which S1, S5, S7, S10, S16, S17, S20 and S22 amend or observe
- **hands-off** `TOOL-dGroundRules-60` — S21 and AC5, which that unit observes through `TOOL-dGroundRules-45`'s `PAIRS_TABLE`

`TOOL-dGroundRules-34`'s exclude-file read, which S3 observes, is reached through
`TOOL-dGroundRules-38`'s own edge to it, and `ORDER_ROWS`, which AC7 reads, through
`TOOL-dGroundRules-43`'s.

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at `8eab342e0`.

- `importlib.util.source_from_cache` raised `ValueError` for a cache file x.pyc
  ("expected only 2 or 3 dots") and for govkit.cpython-314.pyc.123 ("optimization portion of
  filename does not start with 'opt-'") (read 2026-10-23).
- `add_source_read` decodes with `os.fsdecode(path)`, maps a cache read under
  `contextlib.suppress(ValueError)`, and cuts a `.pyc.<digits>` tail with `re.sub` before it;
  `KEPT_PROBE` printed a list holding `tools/govkit/govkit.py` alone.
- `derive_guardable_reads` runs `git -C <top> check-ignore --stdin` with
  `"\n".join(kept).encode("utf-8")` and returns `len(ignored)`, the output lines. `GUARDABLE_PROBE`
  over a scratch `IGNORE_LOG` printed `(['keep', 'ig\xf6'], 2)` and then a `UnicodeEncodeError`
  for the lone surrogate; the S6 call, run as a scratch script, printed `(['keep'], 2)` and
  `(['keep'], 1)`. `git config --get core.quotePath` printed nothing on this node.
- `run_fixture` calls `read_source_git_dirs` before any case and, on its `RuntimeError`, prints a
  `guard-trace` `WRONG` and returns 1; it then runs `check_guard_trace` and `check_guard_lines` after
  the cases. `check_guard_lines` prints a `WRONG` for a manifest that does not parse.
- `print_legs_for` trips a leg only through a guard entry, so a row with an empty guard is tripped by
  no path. `help/policy.md` and no `README.md` sit in the `policy fixtures` guard.
- `INSTALL_LINES` printed `1`; `HELP_LEGS` named `policy fixtures`; `LOCAL_COUNT` printed `0`.
- In a scratch repository with secret.local listed in an untracked excl.txt, `git add -A` run
  with `GIT_DIR` set to a second repository, `GIT_WORK_TREE` set to the first and
  `-c core.excludesFile=` given the relative value excl.txt, from the first's top level and from a
  directory outside it, staged excl.txt and kept.txt and not secret.local.
- `git check-ignore --stdin` answered exit 1 for the paths .git/info/exclude and .git/index.
- `RENDERED_STEPS` printed steps 12, 13 and 14, of five, four and eight units, each ending `| no |`.

### The trace after this unit

```text
--fixture start:
+   if sys.pycache_prefix is not None: print the S15 WRONG; return 1, no case run   # S15
add_source_read(event, args):              # units 33, 35, 38 and 43; this unit's lines marked +
    (43 S9's event and mode filter)
    p = os.fsdecode(args[0])                                                       # built by 33
+   refused = False
+   if parent name of p == "__pycache__" and p ends in ".pyc":                    # S20: no digit tail
        try: p = importlib.util.source_from_cache(p)
+       except ValueError: refused = True                                          # S25; p kept
    (units 33 and 38's resolve, top-level, temporary and git-directory steps)
    SOURCE_READS.add(rel)
+   if refused: UNMAPPED_READS.add(rel)                                            # S25

derive_guardable_reads(kept, top):         # TOOL-dGroundRules-36, S6 and S14
+   out = run(git -C top check-ignore --stdin -z, input = b"".join(os.fsencode(p) + b"\0" for p in kept))
+   ignored = {os.fsdecode(b) for b in out.split(b"\0") if b}
+   return [p for p in kept if p not in ignored], sum(p in ignored for p in kept)

check_guard_trace():
    print the source read(s) count line
+   for p in sorted(UNMAPPED_READS): print "policy-fixture: guard-trace · unmapped cache read <p>"   # S25
    (units 36 and 43's set-asides, then the --legs-for join)
```

The exit-code and `RuntimeError` handling of `derive_guardable_reads` stay as built.

### Per-item changes, by file

| File | Items |
|---|---|
| `tools/policy/check_policy.py` | S6, S14, S15, S20, S25 |

The other items change no code: each is the observation this unit owes for a defect in a criterion
or a stated outcome, made against the code units 25 to 43 build.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `UNMAPPED_READS` | a module-level set beside `SOURCE_READS` | `tools/policy/check_policy.py` |
| `unmapped cache read` | a `guard-trace` line | `tools/policy/check_policy.py` |

### Files touched (estimate)

- `tools/policy/check_policy.py`

### Alternatives rejected

- **`check_guard_lines` taken out, arm 1b its one carrier (rev-4).** `TOOL-dGroundRules-43` rev-5
  AC8, AC9, AC11 and AC12 rest on its finding no dead guard entry, and arm 1b runs only when its
  leg's guard trips.
- **The digit-tail cut taken out in unit 35 itself.** Before unit 43's filter the temporary would
  reach `source_from_cache`, be kept as spelled, and red that unit's AC1 (the skeptic's note on
  id 16); at order 16, unit 43's filter is built.
- **S16's relative value joined to the source's top level in code (rev-4).** Git already reads it
  there (§4 Evidence), so the join would be a line no observation can tell apart.
- **Two batch units.** Every code item writes `tools/policy/check_policy.py`, so M6's first clause
  fails.

## 5. Production-readiness checklist

- security — no item widens a write surface; S16 leaves the forwarded path as git reads it.
- perf / scale — S6 changes one subprocess call's encoding; S25 adds one set.
- error / empty / loading states — S15 refuses rather than tracing blind; S25 names an unmappable
  read; S19 and S24 observe that a bad or empty guard is still a `WRONG`.
- observability — the `unmapped cache read` line and the S15 refusal.
- risks — a `--fixture` run under a cache prefix now refuses; no gov leg sets one.
- testing — the cases under `--fixture` and AC1 to AC21.
- migration — none: no function is added or taken out, so the codebase map does not move.
- user docs — N/A: gov-only legs and probes.

## 6. Acceptance criteria

Every command runs from the repository root. `ORDER_ROWS` is the expression `TOOL-dGroundRules-34`
§6 defines; `EVIDENCE`, `ORDERS`, `ORDER_SHIFT`, `EXCLUDES_REPO` and `SNAP_PROBE` are
`TOOL-dGroundRules-43` §6's; `UNEXCLUDE` is `TOOL-dGroundRules-38` §6's; `DEPTH3_LIVE` and
`TOPLEVEL` are `TOOL-dGroundRules-39` §6's; `PAIRS_PY`, `PAIRS_SH` and `RAW_BOTH` are
`TOOL-dGroundRules-40` §6's; `INSTALL_LINES`, `HELP_LEGS` and `HELP_MOVED` are
`TOOL-dGroundRules-41` §6's. `FIX <case>` stands for
`python tools/policy/check_policy.py --fixture <case>`, as `TOOL-dGroundRules-43` §6 spells it. The
copy is the clone `CLONE_AT` makes at `$TEMP/gr52`, a staging is an edit of its working tree, and a
command run in the copy is spelled `(cd "$TEMP/gr52" && <command>)`. A fixture repository is a
`git init` repository under `%TEMP%/<short name>`. Literal commands and stagings are spelled whole
here, once, and the criteria name them:

```text
CLONE_AT        = sha=$(git rev-parse HEAD); git clone -q "$PWD" "$TEMP/gr52" && git -C "$TEMP/gr52" checkout -q "$sha"
KEPT_PROBE      = python -c probe with tools/policy on sys.path that imports check_policy, sets TRACE_ROOTS[:]
                  to [top, None, read_source_git_dirs(top)], top the realpath of derive_source_top(), as
                  run_fixture does, calls add_source_read("open", (path, mode, flags)) for
                  <top>/tools/govkit/__pycache__/govkit.cpython-314.pyc mode "rb",
                  <top>/tools/govkit/__pycache__/govkit.cpython-314.opt-1.pyc mode "rb", and
                  <top>/tools/govkit/__pycache__/govkit.cpython-314.pyc.123 mode None with flags
                  os.O_CREAT | os.O_WRONLY, and prints sorted(SOURCE_READS)
NO_MAP          = in the copy, add_source_read's source_from_cache call staged out, the cache path kept
RENDERED_STEPS  = awk '/<!-- gen:build-order -->/,/<!-- \/gen:build-order -->/' memory/builds/dGroundRules/README.md | grep -E '^\| 1[234] \|'
NO_STEP_RULE    = in the copy, derive_parallel_step staged to return "yes" for a step of two or more
                  units, and the build README re-rendered there by tools/memory-tree/gen_build_index.py --write
IGNORE_LOG      = a fixture repository <r> whose .gitignore lists ig*, core.quotePath unset
GUARDABLE_PROBE = python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; print(ascii(c.derive_guardable_reads(['keep', 'ig\u00f6', 'igx'], sys.argv[1]))); print(ascii(c.derive_guardable_reads(['keep', 'ig\udcff'], sys.argv[1])))" <r>
PLANT_NONASCII  = in the copy, tools/gövkit/__pycache__/x.pyc created and a read-mode open() of it
                  staged into the first line of run_fresh_target, the case runner in
                  tools/policy/check_policy.py
PREFIXED        = PYTHONPYCACHEPREFIX="$TEMP/gr52pfx" python tools/policy/check_policy.py --fixture budgets-ships-join
EXCLUDES_REL    = EXCLUDES_REPO with its core.excludesFile set to the relative value excl.txt, and
                  <r>/excl.txt listing secret.local
NO_FORWARD      = in the copy, build_source_snapshot's -c core.excludesFile forwarding
                  (TOOL-dGroundRules-43 S10) staged out
NO_GIT          = in the copy, the policy.run_git call inside read_source_git_dirs staged to the value
                  None, git's no-answer, every other policy.run_git caller left whole
DENY_OFF        = in the copy, read_source_git_dirs's raise staged to return ()
BAD_JSON        = in the copy, one comma inserted before the closing bracket of tools/gate-legs.json
COLD_WRITING    = env -u PYTHONDONTWRITEBYTECODE python -c "import shutil; shutil.rmtree('tools/govkit/__pycache__', ignore_errors=True)" &&
                  env -u PYTHONDONTWRITEBYTECODE python tools/policy/check_policy.py --fixture budgets-ships-join
LOCAL_COUNT     = git ls-files .claude | grep -cE '^\.claude/(worktrees/|scheduled_tasks\.lock|mailbox/)'
TRACK_LOCAL     = in the copy, .claude/mailbox/x created and added with git add -f
PLANT_BYTES     = in the copy, open(b'README.md') staged into run_fresh_target's first line
STR_PATH        = in the copy, add_source_read's os.fsdecode(path) staged to str(path)
EMPTY_GUARD     = in the copy, the "policy fixtures" row's guard list set to []
PLANT_REFUSED   = in the copy, tools/govkit/__pycache__/x.pyc created and a read-mode open() of it
                  staged into run_fresh_target's first line
```

- **AC1** — When `EVIDENCE` runs, it prints lines `165` and `179`, as it does before this unit; the
  same query over the build README at HEAD prints other lines, `242` and `265` at `8eab342e0`.
  Red when: the evidence cites lines its stated revision does not hold in the build README.
  figure: `165` and `179` PINNED, the revision being fixed; the HEAD pair DERIVED at observation time.
- **AC2** — When `KEPT_PROBE` runs on the built tree, it prints a list holding one path,
  `tools/govkit/govkit.py`, as it does before this unit; after `NO_MAP`, `KEPT_PROBE` in the copy
  prints `.pyc` paths.
  Red when: a cache read is kept as a `.pyc` path, or the mapping is absent and only the absence of a `WRONG` would show it.
- **AC3** — When `CLONE_AT` and `UNEXCLUDE` run and `FIX adopter-fresh-target` runs in the copy, it
  prints a `guard-trace` `WRONG` naming the exclude file under .git/, as it does before this unit.
  Red when: unit 38's claim about unit 34's exclude-file read is certified by no observation.
  fixture: the clone carries the exclude file git's default template writes.
- **AC4** — When `RENDERED_STEPS` runs on the built tree, it prints three rows, each ending `| no |`,
  as it does before this unit; after `NO_STEP_RULE`, `RENDERED_STEPS` in the copy prints them ending `| yes |`.
  Red when: a step whose units' write sets intersect renders as parallel.
- **AC5** — When `PAIRS_PY` and `PAIRS_SH` run on the built tree, they print `True` then `False`,
  and `0` then `1`, as they do before this unit; after `RAW_BOTH`, they print `True` twice and `0` twice in the copy.
  Red when: either overlap rule, the Python one included, misreads a directory over a file or a shared string prefix.
- **AC6** — When `GUARDABLE_PROBE` runs over `IGNORE_LOG`, it prints `(['keep'], 2)` then
  `(['keep'], 1)`; before this unit it prints a list keeping the non-ASCII path, then a traceback.
  Red when: a quoted output path is counted but not set aside, or a path `os.fsencode` takes is refused by a narrower encoding.
  fixture: a git whose `core.quotePath` is unset or true; this node's is unset.
- **AC7** — When `ORDER_SHIFT` runs, `ORDERS` over that copy prints one more than
  `ORDER_ROWS | wc -l` does there, as it does before this unit.
  Red when: the staging picks a sole holder of its order, so the comparison cannot see the step.
- **AC8** — When `CLONE_AT` runs, `git -C "$TEMP/gr52" rev-parse HEAD` prints the sha it checked
  out, and `FIX adopter-fresh-target` in the copy prints no `guard-trace` line naming .git/, as it
  does before this unit; after `UNEXCLUDE` the same run names the exclude file, AC3's observation.
  Red when: the primary case grades bytes other than the commit under test.
- **AC9** — When `FIX budgets-ships-join` runs on the built tree, it prints a `guard line(s) checked`
  line, as it does before this unit; this unit's diff writes `run_fixture`, so the run at its close is the one that can red.
  Red when: `check_guard_lines` or its call leaves the run, and the criteria of `TOOL-dGroundRules-43` that rest on it lose their check.
- **AC10** — When `CLONE_AT` and then `DEPTH3_LIVE` run, and `FIX census-window-edge` runs in the
  copy, it prints a `WRONG` line naming `census-window-edge` and no `WRONG` line naming `rev-parse`,
  `check-ignore` or `policy fixtures`; the same holds with `TOPLEVEL` in place of `DEPTH3_LIVE`. It
  holds before this unit, unit 39 being built.
  Red when: a `WRONG` from a broken copy passes for the window's own.
- **AC11** — When `INSTALL_LINES` and `HELP_LEGS` run on the built tree, the first prints `1` or more
  and the second names `policy fixtures`, as before this unit; after `HELP_MOVED`, `INSTALL_LINES` in the copy prints `0`.
  Red when: either criterion of unit 41 is observed through a bare page name.
- **AC12** — When `PLANT_NONASCII` runs and `FIX adopter-fresh-target` runs in the copy, it prints no
  `guard-trace` `WRONG` naming x.pyc.
  Red when: git's quoted spelling of a non-ASCII ignored path is compared with the kept path.
- **AC13** — When `PREFIXED` runs, it prints a `WRONG` naming `pycache_prefix`.
  Red when: a warm load under a cache prefix records nothing and the trace reads silent as covered.
- **AC14** — When `SNAP_PROBE` runs over `EXCLUDES_REL` on a tree carrying `TOOL-dGroundRules-43`
  S10, `git -C <s> ls-tree -r --name-only HEAD` on the root it prints lists the fixture's kept.txt
  and not its secret.local, as it does before this unit; after `NO_FORWARD`, `SNAP_PROBE` in the copy lists secret.local.
  Red when: a relative excludes file is read against the snapshot rather than the source.
- **AC15** — When `NO_GIT` runs and `FIX adopter-fresh-target` runs in the copy, it prints a `WRONG`
  naming `rev-parse` and no `source read(s)` count line, as it does before this unit; after `DENY_OFF` too, it prints the count line.
  Red when: a failed `rev-parse` turns the git-directory rule off and the case runs.
- **AC16** — When `BAD_JSON` runs and `FIX adopter-fresh-target` runs in the copy, it prints a
  `guard-trace` `WRONG`, as it does before this unit; this unit's diff writes `check_guard_trace`, so the run at its close is the one that can red.
  Red when: an unparsable manifest reads as a trace with no miss.
- **AC17** — When `COLD_WRITING` runs on the built tree, it prints no `guard-trace` `WRONG` and no
  `guard-trace` line naming `.pyc`; it holds before this unit, and the run at its close, the cut gone and S25's line printing, is the one that can red.
  Red when: importlib's temporary write reaches the path steps once the digit-tail cut is gone.
  fixture: bytecode writing on for the run; this node's shell sets `PYTHONDONTWRITEBYTECODE`, which `env -u` unsets.
- **AC18** — When `LOCAL_COUNT` runs on the built tree, it prints `0`, as it does before this unit;
  after `TRACK_LOCAL`, `LOCAL_COUNT` in the copy prints `1`.
  Red when: the count cannot see a tracked local-state file.
- **AC19** — When `PLANT_BYTES` runs and `FIX adopter-fresh-target` runs in the copy, it prints
  `guard-trace · WRONG README.md`, as it does before this unit; after `STR_PATH` too, no such line.
  Red when: a bytes path is kept under its `b'...'` spelling and lost.
- **AC20** — When `EMPTY_GUARD` runs and `FIX adopter-fresh-target` runs in the copy, it prints a
  `guard-trace` `WRONG`, as it does before this unit; this unit's diff writes `check_guard_trace`, so the run at its close is the one that can red.
  Red when: a guard holding nothing reads as clean.
- **AC21** — When `PLANT_REFUSED` runs and `FIX adopter-fresh-target` runs in the copy, it prints an
  `unmapped cache read` line naming x.pyc.
  Red when: a cache name the stdlib refuses is counted by the set-aside and never named.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `policy fixtures`

`policy fixtures`, a leg in `tools/gate-legs.json`, runs `tools/policy/check_policy.py --fixture`,
the arm below.

New arm: tools/policy/check_policy.py --fixture · covers AC12 AC13 AC21 · a non-ASCII ignored read, a cache prefix and an unmappable cache read, each staged in a primary clone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the sixteen MEDIUM and nine LOW findings of the
  round-1 spec audit of units 35 to 43 in one batch, from the skeptic's sound fixes and its corrected
  fixes for ids 16 and 35, with each cited line read at `0ced625e1`.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-60`, the reciprocal end of the round-1 closing diff
  review's promotions; no scope or criterion moved.
- rev-3 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.
- rev-4 · 2026-10-24 · §6 · a criterion code span rejoined onto one line so hygiene check 23 reads the criterion's tokens; no meaning change.
- rev-5 · 2026-10-24 · §1 to §7, §10 · every item restated against `8eab342e0`, units 1 to 41 built
  and units 51, 53, 54, 57, 58 and 59 WONTDO. Disagreements and the run's rulings: §1 put order 16
  above every unit (it is the one step-16 unit, before 17, 18 and 20); S1, S5's AC3 half and S10 are
  closed by -43 rev-5's `EVIDENCE`, S7 and S17 by its `ORDER_SHIFT`, in place of -51's literal; S4's
  rule is -25's `derive_parallel_step`, its steps of four or more; S6 owes only `-z`, `os.fsencode`
  and the matched count, AC6 now a probe of those; S8, S18, S23 and S25's suppress half are built,
  the set `SOURCE_READS` and `kept` a local, so the new set is `UNMAPPED_READS`; S9 keeps
  `check_guard_lines`, which -43 rev-5 AC8, AC9, AC11 and AC12 rest on, and the arm 1b `New arm:`
  line goes; S13 and AC11 read -41's `INSTALL_LINES` and `HELP_LEGS`; S21 is graded by -40's arm;
  AC5 reads -40's `PAIRS_PY`/`PAIRS_SH`; stagings name `run_fresh_target`; `NO_GIT` targets
  `read_source_git_dirs`'s `policy.run_git` call alone; every literal spells
  `tools/policy/check_policy.py`; the §7 claim that the policy legs do not exist is gone; each
  green-before criterion names the staging or close run that can red it. Found by this pass: git
  reads a relative `core.excludesFile` against the work tree's top level, so S16 owes no code. The
  `TOOL-dGroundRules-60` hands-off narrows to S21 and AC5 through `PAIRS_TABLE`, per -60 rev-2.
- rev-6 · 2026-10-24 · §3 · the consumes-from edge on `TOOL-dGroundRules-25`, CLOSED and declaring no hands-off back,
  gives way to one on `TOOL-dGroundRules-32` naming `check_writes_intersect` and `derive_parallel_step`, the reciprocal
  of that unit's hands-off line; S4 still names the rule in its prose. No scope, design or criterion moved.

## 10. Reuse audit

Each item extends a seam already named in its row: `add_source_read` and `check_guard_trace`
(`TOOL-dGroundRules-33`), `derive_guardable_reads` (`TOOL-dGroundRules-36`), `read_source_git_dirs`
(`TOOL-dGroundRules-38`), `build_source_snapshot` (`TOOL-dGroundRules-43` S10), the standard
library's `os.fsdecode` and `os.fsencode`, and the probes `TOOL-dGroundRules-40`, `-41` and `-43`
spell. `python tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"`
ranked `run_git` and `read_git_output`, which run git but do not choose its encoding, so S6 amends
the call that exists; the other seams were found by reading the files the review cites. The recall
probe returned the prior minors batches `TOOL-dGroundRules-34` and `TOOL-dGroundRules-43`, whose
one-item-per-finding table this unit follows.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
