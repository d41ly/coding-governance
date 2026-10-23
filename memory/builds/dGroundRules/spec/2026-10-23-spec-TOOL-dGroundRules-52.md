# TOOL-dGroundRules-52 — the round-1 audit of units 35 to 43, its minors: twenty-five findings closed in the code and the observations those units leave, one scope item each

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 16 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-52-deviation-40.md](../build/2026-10-23-build-TOOL-dGroundRules-52-deviation-40.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-52-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-52-build-brief.md) | journal | — |
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
particular, so it builds at order 16, above every unit of this build, `TOOL-dGroundRules-51` at
order 15 included.

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
corrected fix, and for id 19 it is the first form the skeptic gives, the check taken out.

## 2. Scope (IN)

- **S1** — Finding 3. `TOOL-dGroundRules-43` AC3 is observed at this unit's close through
  `EVIDENCE_WHOLE` of `TOOL-dGroundRules-51` §5, which names the build README whole.
  Observed by AC1.
- **S2** — Finding 4. `TOOL-dGroundRules-35`'s mapping is observed directly, not through the absence
  of a `WRONG` that `TOOL-dGroundRules-36`'s set-aside can hide: `KEPT_PROBE` feeds
  `add_source_read` a cache read, an `.opt-1` cache read and importlib's temporary write, and prints
  the kept set. Observed by AC2.
- **S3** — Finding 5. `TOOL-dGroundRules-38` S3's claim about `TOOL-dGroundRules-34`'s in-process
  read of the exclude file is observed here, after both units are built: with the git-directory rule
  staged out in a primary clone, the trace names `.git/info/exclude`. Observed by AC3.
- **S4** — Finding 6. Steps 12, 13 and 14 of this build's build-order region render `no` once
  `TOOL-dGroundRules-32`'s `derive_parallel_step` is built and the region is re-rendered, because
  each step holds two units whose Files touched intersect. Observed by AC4.
- **S5** — Finding 12. `TOOL-dGroundRules-43` AC3 is observed as S1 says, and its AC1 through
  `PAIRS_TABLE` of `TOOL-dGroundRules-45` §6. Observed by AC1, AC5.
- **S6** — Finding 13. `derive_guardable_reads` (`TOOL-dGroundRules-36` S1) writes the kept paths to
  `git -C <top> check-ignore --stdin -z` as bytes, each `os.fsencode`d and NUL-terminated, splits the
  output on NUL, and decodes each path with `os.fsdecode`. Its count is the number of kept paths that
  matched an output path, not a count of output lines. Observed by AC6.
- **S7** — Finding 14. `TOOL-dGroundRules-43` AC6 is observed with `ORDER_SHIFT_11`, which names its
  target: `TOOL-dGroundRules-11`, whose order 1 `TOOL-dGroundRules-1` also holds. Observed by AC7.
- **S8** — Finding 15. `TOOL-dGroundRules-38` AC1 is observed in `CLONE_AT`, a clone checked out at
  the commit under test, so the clone grades committed bytes of the unit and not the source's default
  branch. Observed by AC8.
- **S9** — Finding 19. `check_guard_lines` (`TOOL-dGroundRules-37` S1 to S3) and its call are taken
  out of `tools/policy/check_policy.py`. The rule it carried, every `policy fixtures` guard entry
  matching a tracked path at a component boundary with `{prefix}` resolved by the canonical
  `resolve_prefix_token`, is carried by arm 1b of `tools/run-gates/run-gates.test.sh:619-660`, which
  the `run-gates canary` leg runs on every edit of `tools/gate-legs.json`. The `New arm:` line of
  `TOOL-dGroundRules-37` §7 is observed at the close on that arm, staged with the same `PYC_GUARD`.
  Observed by AC9.
  **Readers:** by name: READER NOT IN TREE — the function is minted by TOOL-dGroundRules-37, which is
  unbuilt at this spec's base, and its one caller is the --fixture run in the same file.
  by value: NO VALUE READERS — the lines it prints are parsed by nothing.
- **S10** — Finding 25. `TOOL-dGroundRules-43` AC3 is observed as S1 says. Observed by AC1.
- **S11** — Finding 26. `TOOL-dGroundRules-39` AC2 and AC3 are observed in `CLONE_AT`, a git
  repository, and each requires a `WRONG` line naming `census-window-edge` and no `WRONG` line naming
  `rev-parse`, `check-ignore` or `policy fixtures`. Observed by AC10.
- **S12** — Finding 30. `TOOL-dGroundRules-40` AC2 and `TOOL-dGroundRules-43` AC1 are observed at
  this unit's close through `PAIRS_TABLE` of `TOOL-dGroundRules-45` §6. Observed by AC5.
- **S13** — Finding 31. `TOOL-dGroundRules-41` AC4 and AC5 are observed at this unit's close through
  `INSTALL_LINES_WHOLE` of `TOOL-dGroundRules-48` §5 and `HELP_LEGS_WHOLE` of
  `TOOL-dGroundRules-49` §5. Observed by AC11.
- **S14** — Finding 33. S6's `-z` output is never C-quoted, so a gitignored path holding a non-ASCII
  byte, a double quote or a backslash is matched and set aside like any other. Observed by AC12.
- **S15** — Finding 35. When `sys.pycache_prefix` is set, `--fixture` prints
  `policy-fixture: guard-trace · WRONG sys.pycache_prefix is set` and runs no case, because a cache
  read under a prefix has no `__pycache__` parent to map from. Observed by AC13.
- **S16** — Finding 36. `build_source_snapshot` (`TOOL-dGroundRules-43` S10) resolves a relative
  `core.excludesFile` value against the source's top level before it passes
  `-c core.excludesFile=<absolute>` to the snapshot's `add -A`. Observed by AC14.
- **S17** — Finding 7. The same observation as S7, taken at the grade the review binds for id 7.
  Observed by AC7.
- **S18** — Finding 8. `TOOL-dGroundRules-38` S1's deny branch is staged: `read_source_git_dirs`
  calling a program that does not resolve makes `--fixture` print a `WRONG` naming `rev-parse` and
  run no case. Observed by AC15.
- **S19** — Finding 9. The unparsable-manifest branch S9 takes out with `check_guard_lines` is
  observed where it now lands: a manifest that does not parse makes the guard trace's
  `--legs-for` call fail, and `TOOL-dGroundRules-33` S3 prints that as a `guard-trace` `WRONG`.
  Observed by AC16.
- **S20** — Finding 16. The `.pyc` digit-tail cut of `TOOL-dGroundRules-35` S1 is taken out of
  `add_source_read`, because `TOOL-dGroundRules-43` S9 skips importlib's temporary write, a mode-None
  `open` carrying `O_CREAT`, before the path steps, so the cut sees no input. The cold case is
  observed with bytecode writing on. Observed by AC17.
- **S21** — Finding 17. `TOOL-dGroundRules-40` §3's "both answer correctly today" holds for
  `overlaps` only; `check_writes_intersect` is `TOOL-dGroundRules-32` S9's and is first graded here,
  by `PAIRS_TABLE`'s Python column. Observed by AC5.
- **S22** — Finding 18. `TOOL-dGroundRules-43` AC13 is paired with its staged break: a local-state
  file tracked in a scratch copy makes the count 1. Observed by AC18.
- **S23** — Finding 34. `add_source_read` reads the `open` event's path with `os.fsdecode`, so a str,
  a bytes and a path-like path are one spelling, in place of `str(path)` (`TOOL-dGroundRules-35` §4).
  Observed by AC19.
- **S24** — Finding 37. The empty-guard reading S9 takes out with `check_guard_lines` is observed
  where it now lands: a `policy fixtures` row whose guard list is empty makes the trace print a
  `guard-trace` `WRONG` for every traced read. Observed by AC20.
- **S25** — Finding 38. A cache name that `source_from_cache` refuses is still kept as spelled, and
  `check_guard_trace` also prints `policy-fixture: guard-trace · unmapped cache read <path>` for it
  before `TOOL-dGroundRules-36`'s set-aside, so the read is named rather than counted.
  Observed by AC21.

## 3. Non-goals (OUT)

- The BLOCKER and HIGH ids: `TOOL-dGroundRules-44` to `TOOL-dGroundRules-51`.
- Rewriting any reviewed spec's text. Each defect a spec stated is closed here in the code and the
  observation it governs, and each repaired unit's §3 names this unit; nothing is folded
  (BUILD-METHOD M4).
- Renumbering any unit's `order`, and adding edges among units 34 to 41. S4 observes the order the
  render derives; the dispatch is sequential within a step (`tools/workflows/unattended-build.js:76`).
- A second carrier of the guard-liveness rule. S9 leaves arm 1b as its one carrier.

### Edges

- **consumes-from** `TOOL-dGroundRules-32` — `derive_parallel_step`, whose rendering of steps 12 to 14 S4 observes
- **consumes-from** `TOOL-dGroundRules-33` — `add_source_read`, `check_guard_trace` and its `--legs-for` failure `WRONG`, which S19, S23 to S25 amend or observe
- **consumes-from** `TOOL-dGroundRules-35` — the cache mapping and its digit-tail cut, which S2, S15, S20, S23 and S25 observe or amend
- **consumes-from** `TOOL-dGroundRules-36` — `derive_guardable_reads`, whose call S6 and S14 pin to `-z` and bytes
- **consumes-from** `TOOL-dGroundRules-37` — `check_guard_lines` and its arm line, which S9 takes out and moves to arm 1b, and whose branches S19 and S24 observe where they land
- **consumes-from** `TOOL-dGroundRules-38` — `read_source_git_dirs`, its S3 claim and its criteria AC1, which S3, S8 and S18 observe
- **consumes-from** `TOOL-dGroundRules-39` — `census-window-edge` and the criteria AC2 and AC3, which S11 observes in a git clone
- **consumes-from** `TOOL-dGroundRules-40` — the criteria AC2 and the §3 claim, which S12 and S21 observe
- **consumes-from** `TOOL-dGroundRules-41` — the criteria AC4 and AC5, which S13 observes
- **consumes-from** `TOOL-dGroundRules-43` — `build_source_snapshot`, the S9 event filter and the criteria AC1, AC3, AC6 and AC13, which S1, S5, S7, S10, S16, S17, S20 and S22 amend or observe
- **consumes-from** `TOOL-dGroundRules-45` — `PAIRS_TABLE`, through which S5, S12 and S21 observe
- **consumes-from** `TOOL-dGroundRules-48` — `INSTALL_LINES_WHOLE`, through which S13 observes
- **consumes-from** `TOOL-dGroundRules-49` — `HELP_LEGS_WHOLE`, through which S13 observes
- **consumes-from** `TOOL-dGroundRules-51` — `EVIDENCE_WHOLE`, through which S1, S5 and S10 observe
- **hands-off** `TOOL-dGroundRules-60` — S5, S12, S21 and AC5, which that unit observes through `PAIRS_TABLE_WHOLE` in place of `PAIRS_TABLE` (id 20 of the closing diff review, round 1)

`TOOL-dGroundRules-34`'s exclude-file read, which S3 observes, is reached through
`TOOL-dGroundRules-38`'s own edge to it; unit 34's spec sits within bytes of the spec size ceiling.

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `0ced625e1`.

- `importlib.util.source_from_cache` raised `ValueError` for `tools/govkit/__pycache__/x.pyc`
  ("expected only 2 or 3 dots") and for `govkit.cpython-314.pyc.123` ("optimization portion of
  filename does not start with 'opt-'").
- `os.fsdecode` returned `README.md` for `b'README.md'` and `a/b` for a `PurePosixPath`.
- `tools/run-gates/run-gates.test.sh:619-660` is arm 1b: it inlines `resolve_prefix_token`, resolves
  every `guard` and `doc_reads` entry, and fails naming any entry that matches no `git ls-files`
  path at a component boundary. `tools/gate-legs.json` gives the `run-gates canary` leg the guard
  `{prefix}/`, `{prefix}/gate-legs.json` and `{prefix}/lib/` (review id 19).
- `tools/workflows/unattended-build.js:76` states dispatch is strictly sequential within a shared
  order, and `:608-613` sorts a shared order by unit id.
- The status lines of this build's specs hold order 1 for `TOOL-dGroundRules-1` and
  `TOOL-dGroundRules-11`, and no unit holds order 99.
- `TOOL-dGroundRules-43` S9 and its pseudocode skip a mode-None `open` whose flags carry `O_WRONLY`,
  `O_RDWR` or `O_CREAT` before any path step; `TOOL-dGroundRules-35` §4 Evidence records importlib's
  temporary as a mode-None `open`.

### The trace after this unit

```text
--fixture start:
+   if sys.pycache_prefix is not None: print the S15 WRONG; run no case          # S15
add_source_read(event, args):              # units 33, 35, 38 and 43; this unit's lines marked +
    (43 S9's event and mode filter)
+   p = os.fsdecode(args[0])                                                       # S23
    if parent name of p == "__pycache__" and p ends in ".pyc":                    # S20: no digit tail
        try: p = importlib.util.source_from_cache(p)
+       except ValueError: unmapped.add(p relative to top)                         # S25; p kept
    (units 33 and 38's resolve, top-level, temporary and git-directory steps)

derive_guardable_reads(kept, top):         # TOOL-dGroundRules-36, S6 and S14
+   out = run(git -C top check-ignore --stdin -z, input = b"".join(os.fsencode(p) + b"\0" for p in kept))
+   ignored = {os.fsdecode(b) for b in out.split(b"\0") if b}
    return [p for p in kept if p not in ignored], sum(p in ignored for p in kept)

check_guard_trace():
+   for p in sorted(unmapped): print "policy-fixture: guard-trace · unmapped cache read <p>"   # S25
    (units 36 and 43's set-asides, then the --legs-for join; check_guard_lines is not called)  # S9

build_source_snapshot(source):             # TOOL-dGroundRules-43 S10, S16
    v = git -C source config --type=path --get core.excludesFile
+   if v and not os.path.isabs(v): v = os.path.join(source top level, v)
```

### Per-item changes, by file

| File | Items |
|---|---|
| `tools/policy/check_policy.py` | S6, S9, S14 to S16, S20, S23, S25 |
| the codebase map | S9, by regeneration |

The other items change no code: each is the observation this unit owes for a defect in a criterion
or a stated outcome, made against the code units 32 to 51 build.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `unmapped` | a module-level set beside `kept` | `tools/policy/check_policy.py` |
| `unmapped cache read` | a `guard-trace` line | `tools/policy/check_policy.py` |

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **`check_guard_lines` kept, with the canonical `resolve_prefix_token` inlined.** It would agree
  with arm 1b and still be a second carrier of one rule, which the review's reuse lens names; arm 1b
  already runs on every manifest edit.
- **The digit-tail cut taken out in unit 35 itself.** Between orders 12 and 14 the temporary would
  reach `source_from_cache`, be kept as spelled, and red that unit's AC1 (the skeptic's note on
  id 16); at order 16, unit 43's filter is built.
- **Two batch units.** Every code item writes `tools/policy/check_policy.py`, so M6's first clause
  fails.

## 5. Production-readiness checklist

- security — S16 resolves a forwarded path inside the source; no item widens a write surface.
- perf / scale — S6 changes one subprocess call's encoding; S25 adds one set.
- error / empty / loading states — S15 refuses rather than tracing blind; S25 names an unmappable
  read; S19 and S24 observe that a bad or empty guard is still a `WRONG`.
- observability — the `unmapped cache read` line and the S15 refusal.
- risks — S9 leaves the guard-liveness rule to arm 1b alone, which runs only under its leg's guard;
  that guard holds `tools/gate-legs.json`, the file the S4 sweep of unit 33 writes.
- testing — the cases under `--fixture` and AC1 to AC21.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: gov-only legs and probes.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. `check_policy.py` names the
policy kit's file under the kit, as `TOOL-dGroundRules-43` §6 does, and `ORDERS`, `ORDER_ROWS`,
`EXCLUDES_REPO`, `UNEXCLUDE`, `DEPTH3_LIVE`, `TOPLEVEL` and `PYC_GUARD` are the expressions units 43,
34, 38, 39 and 37 define. A fixture repository is a `git init` repository under `%TEMP%/<short
name>`. Literal commands and stagings are spelled whole here, once, and the criteria name them:

```text
CLONE_AT        = sha=$(git rev-parse HEAD); git clone -q <this repository> "$TEMP/gr52" &&
                  git -C "$TEMP/gr52" checkout -q "$sha" && cd "$TEMP/gr52"
KEPT_PROBE      = python -c probe, the kit directory on sys.path, that imports check_policy, sets the
                  source top level as --fixture sets it, calls add_source_read("open", ...) for
                  <top>/tools/govkit/__pycache__/govkit.cpython-314.pyc mode "rb",
                  <top>/tools/govkit/__pycache__/govkit.cpython-314.opt-1.pyc mode "rb", and
                  <top>/tools/govkit/__pycache__/govkit.cpython-314.pyc.123 mode None with flags
                  os.O_CREAT | os.O_WRONLY, and prints sorted(kept)
RENDERED_STEPS  = awk '/<!-- gen:build-order -->/,/<!-- \/gen:build-order -->/' memory/builds/dGroundRules/README.md | grep -E '^\| 1[234] \|'
ORDER_SHIFT_11  = in a scratch copy, "· order 1" changed to "· order 99" on the status line of
                  memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-11.md, the README
                  not re-rendered
PLANT_TWO       = in CLONE_AT, probe.pyc and probe2.pyc created at the top level and one read-mode
                  open() of each staged into build_fresh_target's first line
PLANT_NONASCII  = in CLONE_AT, tools/gövkit/__pycache__/x.pyc created and a read-mode open() of it
                  staged into build_fresh_target's first line
GUARD_LINES_GONE = grep -c "check_guard_lines" check_policy.py
PREFIXED        = PYTHONPYCACHEPREFIX="$TEMP/gr52pfx" python check_policy.py --fixture budgets-ships-join
EXCLUDES_REL    = EXCLUDES_REPO with its core.excludesFile set to the relative value excl.txt, and
                  excl.txt at that repository's top level listing secret.local
NO_GIT          = in CLONE_AT, read_source_git_dirs staged to call a program named git-absent in
                  place of git
BAD_JSON        = in CLONE_AT, one comma inserted before the closing bracket of tools/gate-legs.json
COLD_WRITING    = env -u PYTHONDONTWRITEBYTECODE python -c "import shutil; shutil.rmtree('tools/govkit/__pycache__', ignore_errors=True)" &&
                  env -u PYTHONDONTWRITEBYTECODE python check_policy.py --fixture budgets-ships-join
LOCAL_COUNT     = git ls-files .claude | grep -cE '^\.claude/(worktrees/|scheduled_tasks\.lock|mailbox/)'
TRACK_LOCAL     = in CLONE_AT, .claude/mailbox/x created and added with git add -f
PLANT_BYTES     = in CLONE_AT, open(b'README.md') staged into build_fresh_target's first line
EMPTY_GUARD     = in CLONE_AT, the "policy fixtures" row's guard list set to []
PLANT_REFUSED   = in CLONE_AT, tools/govkit/__pycache__/x.pyc created and a read-mode open() of it
                  staged into build_fresh_target's first line
```

- **AC1** — When `EVIDENCE_WHOLE` of `TOOL-dGroundRules-51` §5 runs, it prints lines `165` and `179`.
  Red when: the evidence cites lines its stated revision does not hold.
  figure: PINNED, the revision being fixed; this is a check on evidence, not on the build.
- **AC2** — When `KEPT_PROBE` runs on the built tree, it prints a list holding one
  path, `tools/govkit/govkit.py`.
  Red when: a cache read is kept as a `.pyc` path, or the mapping is absent and only the absence of a
  `WRONG` would show it.
- **AC3** — When `CLONE_AT` and `UNEXCLUDE` run and `python check_policy.py --fixture adopter-fresh-target`
  runs in the clone, it prints a `guard-trace` `WRONG` naming `.git/info/exclude`.
  Red when: unit 38's claim about unit 34's exclude-file read is certified by no observation.
  fixture: the clone carries the `.git/info/exclude` git's default template writes.
- **AC4** — When `RENDERED_STEPS` runs on the built tree, it prints three rows, each ending `| no |`.
  Red when: a step whose units' write sets intersect renders as parallel.
- **AC5** — When `PAIRS_TABLE` of `TOOL-dGroundRules-45` §6 runs on the built tree, on each line the
  last two fields are `True 0` for `intersect` and `False 1` for `disjoint`.
  Red when: either overlap rule, the Python one included, disagrees with the table.
- **AC6** — When `PLANT_TWO` runs and the AC3 command runs in the clone, it prints
  `ignored read(s) set aside` with a count of 2 or more and no `guard-trace` line naming `probe.pyc`
  or `probe2.pyc`.
  Red when: every ignored path but the last is joined, as a text-mode newline-joined input does.
- **AC7** — When `ORDER_SHIFT_11` runs, `ORDERS` over that copy prints one more than
  `ORDER_ROWS | wc -l` does there.
  Red when: the staging picks a sole holder of its order, so the comparison cannot see the step.
- **AC8** — When `CLONE_AT` runs, `git -C "$TEMP/gr52" rev-parse HEAD` prints the sha it checked out,
  and the AC3 command, without `UNEXCLUDE`, prints no `guard-trace` line naming `.git/`.
  Red when: the primary case grades bytes other than the commit under test.
- **AC9** — When `GUARD_LINES_GONE` runs on the built tree, it prints `0`, and the AC3 command prints
  no `guard line(s) checked` line.
  Red when: the guard-liveness rule has two carriers.
- **AC10** — When `CLONE_AT` and then `DEPTH3_LIVE` run, and `python check_policy.py --fixture census-window-edge`
  runs in the clone, it prints a `WRONG` line naming `census-window-edge` and no `WRONG` line naming
  `rev-parse`, `check-ignore` or `policy fixtures`; the same holds with `TOPLEVEL` in place of
  `DEPTH3_LIVE`.
  Red when: a `WRONG` from a broken copy passes for the window's own.
- **AC11** — When `INSTALL_LINES_WHOLE` of `TOOL-dGroundRules-48` §5 and `HELP_LEGS_WHOLE` of
  `TOOL-dGroundRules-49` §5 run on the built tree, the first prints `1` or more and the second names
  `policy fixtures`.
  Red when: either criterion of unit 41 is observed through a bare page name.
- **AC12** — When `PLANT_NONASCII` runs and the AC3 command runs in the clone, it prints no
  `guard-trace` `WRONG` naming `x.pyc`.
  Red when: git's quoted spelling of a non-ASCII ignored path is compared with the kept path.
- **AC13** — When `PREFIXED` runs, it prints a `WRONG` naming `pycache_prefix`.
  Red when: a warm load under a cache prefix records nothing and the trace reads silent as covered.
- **AC14** — When `build_source_snapshot` runs over `EXCLUDES_REL`,
  `git -C <s> ls-tree -r --name-only HEAD` lists `kept.txt` and not `secret.local`.
  Red when: a relative excludes file is read against the snapshot rather than the source.
- **AC15** — When `NO_GIT` runs and the AC3 command runs in the clone, it prints a `WRONG` naming
  `rev-parse` and no `guard-trace` count line.
  Red when: a failed `rev-parse` turns the git-directory rule off and the case runs.
- **AC16** — When `BAD_JSON` runs and the AC3 command runs in the clone, it prints a `guard-trace`
  `WRONG`.
  Red when: an unparsable manifest reads as a trace with no miss.
- **AC17** — When `COLD_WRITING` runs on the built tree, it prints no `guard-trace` `WRONG` and no
  `guard-trace` line naming `.pyc`.
  Red when: importlib's temporary write reaches the path steps once the digit-tail cut is gone.
  fixture: bytecode writing on for the run; this node's shell sets `PYTHONDONTWRITEBYTECODE`, which
  `env -u` unsets.
- **AC18** — When `LOCAL_COUNT` runs on the built tree, it prints `0`; after `TRACK_LOCAL`, run in
  the clone, it prints `1`.
  Red when: the count cannot see a tracked local-state file.
- **AC19** — When `PLANT_BYTES` runs and the AC3 command runs in the clone, it prints
  `guard-trace · WRONG README.md`.
  Red when: a bytes path is kept under its `b'...'` spelling and lost.
- **AC20** — When `EMPTY_GUARD` runs and the AC3 command runs in the clone, it prints a `guard-trace`
  `WRONG`.
  Red when: a guard holding nothing reads as clean.
- **AC21** — When `PLANT_REFUSED` runs and the AC3 command runs in the clone, it prints
  an `unmapped cache read` line naming `x.pyc`.
  Red when: a cache name the stdlib refuses is counted by the set-aside and never named.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `run-gates canary`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the cases;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py --fixture · covers AC6 AC12 AC13 AC15 AC19 AC21 · two ignored reads, a non-ASCII ignored read, a cache prefix, the git-directory query broken, a bytes read and an unmappable cache read, each staged in a primary clone · none
New arm: tools/run-gates/run-gates.test.sh (arm 1b) · covers none · `PYC_GUARD` appended to a scratch copy's `policy fixtures` guard, the case `TOOL-dGroundRules-37` §7 declared, moved to the arm that carries the rule · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the sixteen MEDIUM and nine LOW findings of the
  round-1 spec audit of units 35 to 43 in one batch, from the skeptic's sound fixes and its corrected
  fixes for ids 16 and 35, with each cited line read at `0ced625e1`.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-60`, the reciprocal end of the round-1 closing diff
  review's promotions; no scope or criterion moved.

## 10. Reuse audit

Each item extends a seam already named in its row: `add_source_read` and `check_guard_trace`
(`TOOL-dGroundRules-33`), `derive_guardable_reads` (`TOOL-dGroundRules-36`), `read_source_git_dirs`
(`TOOL-dGroundRules-38`), `build_source_snapshot` (`TOOL-dGroundRules-43` S10), the standard
library's `os.fsdecode` and `os.fsencode`, arm 1b of `tools/run-gates/run-gates.test.sh:619-660` for
S9, and the probes `TOOL-dGroundRules-45`, `-48`, `-49` and `-51` spell. `python
tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"` ranked
`run_git` and `read_git_output`, which run git but do not choose its encoding, so S6 amends the call
that exists; the other seams were found by reading the files the review cites. The recall probe
returned the prior minors batches `TOOL-dGroundRules-34` and `TOOL-dGroundRules-43`, whose
one-item-per-finding table this unit follows.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
