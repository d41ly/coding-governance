# TOOL-dSafePassage-59 — the spec audit of units 51 and 52, its 12 minors on TOOL-51: the link test's population and form, the `.gitmodules` link refusal, the sweep's own criteria, and the readings that cite them

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-59-deviation-105.md](../build/2026-10-23-build-TOOL-dSafePassage-59-deviation-105.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-59-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-59-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-59-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-59-hygiene-fix.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 51 and 52
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`)
exited BOUNDED with 22 minors. BUILD-METHOD M4 batches them, and they split into two disjoint write
sets by M6's clauses. `TOOL-dSafePassage-58` batches the ten on TOOL-dSafePassage-52, whose writes
are the lander's suite and the spec template. This unit batches the other 12, 5 MEDIUM and 7 LOW,
all on TOOL-dSafePassage-51, whose writes are the step module, its self-test and its help page. Each
is named by its report id and is its own scope item, including where the report merged ids into one
item.

All 12 land on TOOL-dSafePassage-51, so this unit repairs that unit and builds one above it, at
order 15, after the unit's other repairs by the driver's id tie-break. Where a minor would bite
TOOL-dSafePassage-51's pass, that unit's own §3 hands-off bullet to this unit names it, so that pass
may build it.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2 | S1 |
| M3 | MEDIUM | 12 | S8 |
| M5 | MEDIUM | 18 | S5 |
| M6 | MEDIUM | 23 | S6 |
| M7 | MEDIUM | 24 | S7 |
| L1 | LOW | 4, 17 | S9, S10 |
| L2 | LOW | 5 | S11 |
| L5 | LOW | 13 | S2 |
| L6 | LOW | 16 | S3 |
| L7 | LOW | 19 | S12 |
| L9 | LOW | 29 | S4 |

That is 5 MEDIUM and 7 LOW findings by raw id. Item M6 shares its defect with id 8 at HIGH, item
H3, whose promotion `TOOL-dSafePassage-56` puts the link test on every path the walk enters; S6 adds
what id 23 asks beyond it. The report refuted ids 6 and 25 and left none unverified. The skeptic
re-graded ids 13, 16, 17 and 19 from medium to low. It REJECTED the finder's fix of id 12, so S8 is
built from the skeptic's corrected fix.

## 2. Scope (IN)

### The sweep's own criteria (M1, L5, L6, L9)

- **S1** — id 2. TOOL-dSafePassage-51 AC1 and AC2 grade the sweep's work and the commit order, which
  no write of TOOL-dSafePassage-51's pass can move. They are recorded as checks of the build run's
  sweep: their ledger lines sit in an `**Evidences:** TOOL-dSafePassage-51` block of a record
  committed with `Pass: none`. The hand-out refusal they lean on is seen to refuse by
  `TOOL-dSafePassage-55` AC3, over a copy whose TOOL-dSafePassage-4 header still reads `order 2`.
  Observed by AC1.
- **S2** — id 13. TOOL-dSafePassage-51 S1 and §7 are read with the guard that already exists:
  TOOL-dTrueNorth-16 S2's edge refusal in `tools/unattended/unattended.sh` (`:13691`), which stops a
  `--dispatch` with fail 49 while a same-build producer of the dispatched unit is neither CLOSED nor
  WONTDO. TOOL-dSafePassage-4 declares `consumes-from` on TOOL-dSafePassage-7 and
  TOOL-dSafePassage-43, so its early dispatch is already refused. §7's "which only S1's hand-out step
  guards" is read as: the edge refusal guards it at TOOL-dSafePassage-4's dispatch, and
  `TOOL-dSafePassage-55`'s probe guards the header order the driver sorts by, before any pass.
  Observed by AC9.
- **S3** — id 16. TOOL-dSafePassage-51 AC1's probe is spelled whole-line, because
  `TOOL-dSafePassage-4` is a prefix of `TOOL-dSafePassage-43` to `-49`:
  `git log --reverse --format='%(trailers:key=Pass,valueonly)' <BASE>..HEAD | grep -n -x -m1 'TOOL-dSafePassage-4'`,
  and the same `-x` form for 43, 7, 18 and 19. Observed by AC10.
- **S4** — id 29. TOOL-dSafePassage-51 S3 is read with S2's "in these words and on one line", so
  the amended TOOL-dSafePassage-43 Rollout holds `TOOL-dSafePassage-4 builds at order 3` on one line,
  which TOOL-dSafePassage-51 AC2's line-local `git grep -c` counts. Observed by AC12.

### The link test's form, positions and population (M5, M6, M7)

- **S5** — id 18. The link test needs no call newer than govkit's floor, CPython 3.11
  (`tools/govkit/govkit.py:104-112`). `test_path_linked(path)` (`TOOL-dSafePassage-56` S1) takes
  `os.lstat(path)`, reads False on `FileNotFoundError`, and reads True when
  `stat.S_ISLNK(st.st_mode)` holds or `getattr(st, "st_reparse_tag", 0)` is non-zero. That covers a
  symlink on every host and a junction on Windows. `os.path.isjunction`, added in 3.12, appears
  nowhere in `tools/govkit/upgrade_steps.py`. TOOL-dSafePassage-51 S6's test is read as that
  function. TOOL-dSafePassage-51 §5 states the floor. Observed by AC2 and AC3.
- **S6** — id 23. The plant `submodule-modules-root-link`: `<git_dir>/modules` itself is a junction
  or directory symlink to a scratch directory. The step is refused naming `.git/modules`, with no
  `Traceback`, and exits 1 within 60 seconds. In `submodule-modules-link-loop`, `.git/modules/a` is a
  plain directory and no repository, a name segment. So `loop` is a listed child the walk tests.
  Were `a` a repository, only `a/modules` would be entered and `loop` never listed. Observed by AC4.
- **S7** — id 24. The listing's population is every entry `os.scandir(d)` yields, with no type
  filter (`TOOL-dSafePassage-53`'s listing). `test_path_linked` runs on each entry first, and a hit
  is the refusal. Only then are the rest filtered to directories by
  `DirEntry.is_dir(follow_symlinks=False)`. So a dangling link, or a link to a file, under `modules/`
  is refused by name before any filter sees it. The `isolation` family gains
  `submodule-modules-link-dangling`: a junction or symlink under `.git/modules/` whose target path is
  absent. Observed by AC5.

### The `.gitmodules` link refusal (M3)

- **S8** — id 12, the skeptic's corrected fix. TOOL-dSafePassage-51 S15's type test is read as one
  `os.lstat` of `<worktree>/.gitmodules`. `FileNotFoundError` means missing. `stat.S_ISLNK` or a
  non-zero `st_reparse_tag` is a refusal naming the path. Anything not `stat.S_ISREG` is a refusal
  naming the path. Only then does TOOL-dSafePassage-45 S13's read run, so a linked `.gitmodules` is
  never followed, and the `os.stat` S15 names is not taken. TOOL-dSafePassage-51 AC9 is read with
  `os.lstat` alone. TOOL-dSafePassage-51 §4 "Alternatives rejected" is read as naming
  `read_plain_stat` in `tools/run-gates/measure_legs.py:1373`, not reused because it lives in the
  run-gates kit, from which no `tools/govkit/*.py` imports, and its `st_nlink == 1` rule is written
  for files a run made itself. TOOL-dSafePassage-51 §10's conclusion is read as naming that seam. The
  `isolation` family gains `gitmodules-symlink`, made by `os.symlink`, which prints a `skip —` line
  and exits 0 where the host refuses to make a symlink. Observed by AC6.

### The retired key list's readers (L1)

- **S9** — id 4. TOOL-dSafePassage-29's §3 hands-off bullet to TOOL-dSafePassage-49, which says
  "keeping `UNLISTED_EXECUTOR_KEYS`", is read with TOOL-dSafePassage-51 S9 like TOOL-dSafePassage-49's
  own sections: the expected unlisted executor keys live as the selftest literal, and the module
  defines no such constant. TOOL-dSafePassage-51 S9's list of texts read that way gains it.
  Observed by AC7.
- **S10** — id 17. TOOL-dSafePassage-51 S9 retires `UNLISTED_EXECUTOR_KEYS`, and its census is taken
  at the tree its pass builds on, after TOOL-dSafePassage-49's order-13 pass, with
  `git grep -n UNLISTED_EXECUTOR_KEYS -- tools help`. TOOL-dSafePassage-51 §4 Inventory is read as
  listing the retirement, and its AC6 grep as reaching `-- tools help`. Observed by AC7.
  **Readers:** by name: `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-29.md`
  (its §3 bullet), `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md` (S8,
  §4 "The arm's widening", Inventory, Alternatives and §7), `tools/govkit/selftest.py` where
  TOOL-dSafePassage-49's pass mints it, and READER NOT IN TREE for `tools/govkit/upgrade_steps.py`,
  because TOOL-dSafePassage-1 creates that module and is unbuilt at the base, so no tracked file is
  that reader yet · by value: the class arm
  in `tools/govkit/selftest.py`, which reads the selftest literal in its place.

### The section probe (L2, L7)

- **S11** — id 5. TOOL-dSafePassage-51 §4 "The section probe" toggles its fence state on both fence
  forms, `/^(```|~~~)/`, so a tilde fence holding a `# ` line neither ends nor opens the section.
  Observed by AC8.
- **S12** — id 19. TOOL-dSafePassage-51 S12's "the one probe for the section" binds every criterion
  that asserts what the section names. TOOL-dSafePassage-7 AC8, TOOL-dSafePassage-24 AC5,
  TOOL-dSafePassage-29 AC5, TOOL-dSafePassage-36 AC3, TOOL-dSafePassage-37 AC4, TOOL-dSafePassage-38
  AC4 and TOOL-dSafePassage-42 AC12 are each read as their own grep run over that probe's output in
  place of the whole page. Observed by AC11.

## 3. Non-goals (OUT)

- The lander's suite and the spec template: `TOOL-dSafePassage-58`.
- The listing handler, the sound baseline, the hand-out probe and the link test's positions:
  `TOOL-dSafePassage-53`, `TOOL-dSafePassage-54`, `TOOL-dSafePassage-55` and `TOOL-dSafePassage-56`.
- Rewriting a built spec. An item that corrects a spec's text states the reading here.
- The report's left-shift gates and checklist entries.

### Edges

- **consumes-from** `TOOL-dSafePassage-51` — S1's sweep criteria, S3's Rollout, S6's link rule and plant, S9's census, S12's section probe, S15's file test, §4, §7 and §10, which S1 to S12 read
- **consumes-from** `TOOL-dSafePassage-53` — the listing's `os.scandir` call, whose entries S7 tests before any filter
- **consumes-from** `TOOL-dSafePassage-55` — AC3's staged hand-out refusal, which S1 names as the red case of TOOL-dSafePassage-51's sweep criteria
- **consumes-from** `TOOL-dSafePassage-56` — `test_path_linked` and its call at the top of the walk, whose form S5 fixes and whose root position S6 plants

## 4. Design

### The link test, on Python 3.11

```
test_path_linked(path):
  try: st = os.lstat(path)
  except FileNotFoundError: return False
  return stat.S_ISLNK(st.st_mode) or getattr(st, "st_reparse_tag", 0) != 0
```

This unit's probe on node d, Python 3.14.5, 2026-10-23: a junction made with `mklink /J` read
`st_reparse_tag` `0xa0000003` and `S_ISLNK` False, so the tag is what finds it. A junction whose
target was then removed still answered `os.lstat` with the same tag; `os.scandir` listed it and
`DirEntry.is_dir(follow_symlinks=False)` read True, while `os.path.isdir` read False. So an
`os.path.isdir` filter before the test drops a dangling junction, which S7 forbids.

### The section probe, both fences

```
awk '/^(```|~~~)/{c=!c} !c&&/^#+ What a step can reach/{l=index($0," ");f=1;next} !c&&f&&/^#+ /&&index($0," ")<=l{f=0} f' help/upgrade-steps.md
```

Over a scratch page holding the section, a `~~~` fence with `# x` inside it, a line `b` and then
`## End`, it printed `a`, the fence, `# x` and `b`, and stopped at `## End` (node d, 2026-10-23).

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the `isolation` plants `submodule-modules-root-link`,
`submodule-modules-link-dangling` and `gitmodules-symlink`. No function, constant, conf key, gate leg
or policy key. Retired by reading: `UNLISTED_EXECUTOR_KEYS`, S10. The refusals of S6, S7 and S8 are
TOOL-dSafePassage-24's one `raise Refusal` site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN`
does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 15, after `TOOL-dSafePassage-53` to `TOOL-dSafePassage-56` by the
driver's id tie-break, and shares `tools/govkit/upgrade_steps.py`, `tools/govkit/selftest.py` and
`help/upgrade-steps.md` with `TOOL-dSafePassage-53`, `TOOL-dSafePassage-54` and
`TOOL-dSafePassage-56`, so the build run sequences those passes by M6's first clause. That set does
not meet `TOOL-dSafePassage-58`'s, which is the lander's suite.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Admitting a linked `.gitmodules` and reading through it (S8).** The skeptic's second option. Git
  refuses to index a symlinked `.gitmodules` (finding 25's skeptic measured `error: invalid path
  '.gitmodules'`), so a linked one in a worktree was planted, never checked out. The charter's
  deny-by-default rule then refuses it.
- **`getattr(os.path, "isjunction", None)` with a fallback per host (S5).** The report's fix. It is
  two tests where one `lstat` and its reparse tag answer both hosts, the same pair
  `read_plain_stat` reads.
- **Narrowing S12's claim to the three criteria it names (S12).** The report's second option. Seven
  criteria would keep grading the whole page.
- **Folding each minor into TOOL-dSafePassage-51.** The disposal promotes, never folds
  (BUILD-METHOD M4).

## 5. Production-readiness checklist

- security: a linked `.gitmodules` and a dangling or file link under `modules/` are refused, never
  followed or dropped.
- perf / scale: one `lstat` per entry under `modules/` and one per `.gitmodules`.
- error / empty / loading states: every refusal names its path; an absent path reads False to the
  link test and stays `TOOL-dSafePassage-53`'s absent class.
- observability: each refusal names the path it refused.
- risks: a reparse point that is neither a symlink nor a junction now reads as linked and is
  refused, the safe direction.
- testing: the probes and plants of §6, through §7's arm.
- migration: none.
- user docs: `help/upgrade-steps.md`, the section S11's probe reads, which names the linked
  `.gitmodules` refusal.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -A6 '^\*\*Evidences:\*\* TOOL-dSafePassage-51' -- memory/builds/dSafePassage/`
  runs after the sweep, it shows `AC1` and `AC2` lines in a record whose commit carries `Pass: none`,
  not in a commit carrying `Pass: TOOL-dSafePassage-51`.
  Red when: the sweep's checks are attributed to TOOL-dSafePassage-51's pass.
- **AC2** — When `git grep -n isjunction -- tools/govkit/upgrade_steps.py` runs, it prints nothing.
  Red when: the module calls a function newer than its 3.11 floor.
- **AC3** — When a `python -c` probe deletes `isjunction` from `os.path`, then imports
  `tools/govkit/upgrade_steps.py` by path and calls `test_path_linked` on a scratch junction or
  directory symlink, it prints True and raises no `AttributeError`.
  Red when: the test reaches `os.path.isjunction` on an interpreter without it.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-modules-root-link`
  runs, the step is refused naming `.git/modules`, the output holds no `Traceback`, and the run exits
  1 within 60 seconds.
  Red when: the root is listed through its link.
- **AC5** — When the same family runs with `--plant submodule-modules-link-dangling`, the step is
  refused naming the dangling path and the run exits 1.
  Red when: a type filter drops the dangling link before the link test, so the run exits 0.
- **AC6** — When a `python -c` probe walks `tools/govkit/upgrade_steps.py` with `ast`, the function
  that reads `<worktree>/.gitmodules` tests `S_ISLNK` on its `os.lstat` result on a line before its
  `config -f` spawn and before any `open`. When the same family runs with `--plant gitmodules-symlink`,
  the step is refused naming the `.gitmodules` path and exits 1, or prints a `skip —` line naming the
  plant and exits 0 where the host cannot make a symlink.
  Red when: a symlinked `.gitmodules` is followed and read.
- **AC7** — When `git grep -n UNLISTED_EXECUTOR_KEYS -- tools help` runs after TOOL-dSafePassage-51's
  pass, it prints nothing.
  Red when: the constant TOOL-dSafePassage-29's bullet asked to keep survives in code or on a page.
- **AC8** — When §4's section probe runs over a scratch page holding a `~~~` fence with a `# ` line
  inside the section, its output holds the lines after the fence and none after the next `##`
  heading.
  Red when: the probe ends the section at a `# ` line inside a tilde fence.
- **AC9** — When `grep -n 'TOOL-dTrueNorth-16 S2, THE EDGE REFUSAL' tools/unattended/unattended.sh`
  runs, it prints one line.
  Red when: the guard S2 cites is gone, so TOOL-dSafePassage-55's probe is again the only one.
- **AC10** — When `printf 'TOOL-dSafePassage-43\nTOOL-dSafePassage-7\n' | grep -n -x -m1 'TOOL-dSafePassage-4'`
  runs, a history holding only TOOL-dSafePassage-43's and TOOL-dSafePassage-7's commits, it prints
  nothing and exits 1.
  Red when: the probe matches a prefix, so TOOL-dSafePassage-43's commit reads as TOOL-dSafePassage-4's.
- **AC11** — When §4's section probe runs over `help/upgrade-steps.md` and each of the seven
  criteria S12 names runs its own grep pattern over that output, each prints the line its criterion
  asserts.
  Red when: a required term sits on the page but outside the section.
- **AC12** — When `git grep -c 'TOOL-dSafePassage-4 builds at order 3'` runs over the
  TOOL-dSafePassage-43 spec after the sweep, it prints at least `1`.
  Red when: the amended Rollout wraps the phrase across two lines.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC4 AC5 AC6 · the self-test runs `test_path_linked` with `os.path.isjunction` absent, and the `submodule-modules-root-link`, `submodule-modules-link-dangling` and `gitmodules-symlink` plants; its failing cases are staged by a link-test copy calling `os.path.isjunction`, a walk copy that lists the root without testing it, a walk copy that filters entries by `os.path.isdir` before the link test, and a `.gitmodules` read copy that takes `os.stat` before any link test · none

What the check does not cover: the `gitmodules-symlink` refusal on a host that refuses to make a
symlink, where only its `skip —` line is seen, and the ledger attribution of S1 beyond the record's
commit trailer.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 51 and 52's 5 MEDIUM and 7
  LOW findings on TOOL-dSafePassage-51, one scope item per raw id.

## 10. Reuse audit

The seams extended are named per item: TOOL-dSafePassage-51's walk, file test, sweep criteria and
section probe, `TOOL-dSafePassage-53`'s listing, `TOOL-dSafePassage-55`'s probe and
`TOOL-dSafePassage-56`'s `test_path_linked`, all specced and unbuilt at the base. For S8 and S5 the
census grepped `tools/` by behaviour, for `st_reparse_tag`, `S_ISREG` and `lstat`, and found
`read_plain_stat` in `tools/run-gates/measure_legs.py:1373`, whose reparse-tag test S5 copies in
form and whose module S8 names and does not import. `python tools/codebase-map/reuse_lookup.py "refuse a path that is a symlink or junction before listing it"`
ranked `before`, `CensusRefused` and `ScopeRefused`, name-token matches that miss that seam, which is
where the map and the behaviour grep disagree. So no existing seam fits beyond those specs and that
form.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted units' passes" --terms "spec audit minors batched reading hands-off walk link junction refusal order section probe"`
