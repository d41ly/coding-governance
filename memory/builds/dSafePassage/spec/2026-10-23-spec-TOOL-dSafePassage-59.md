# TOOL-dSafePassage-59 — the spec audit of units 51 and 52, its 12 minors on TOOL-51: the link test's population and form, the `.gitmodules` link refusal, the commit-order criterion's attribution and form, and the readings that cite them

**Status:** CLOSED · rev-3 · 2026-10-28 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dSafePassage-14 · ratified 2026-10-28

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-59-deviation-105.md](../build/2026-10-23-build-TOOL-dSafePassage-59-deviation-105.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 |
| [2026-10-26-build-TOOL-dSafePassage-59-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-59-ledger.md) | journal | — |
| [2026-10-28-build-TOOL-dSafePassage-59-order-check.md](../build/2026-10-28-build-TOOL-dSafePassage-59-order-check.md) | journal | TOOL-dSafePassage-51 |
| [2026-10-23-prompt-TOOL-dSafePassage-59-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-59-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-59-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-59-hygiene-fix.md) | research | — |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 |
| [2026-10-26-prompt-TOOL-dSafePassage-59-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-59-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md) | research | TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-5 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

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
| L9 | LOW | 29 | S4, struck at rev-3 |

That is 5 MEDIUM and 7 LOW findings by raw id. Item M6 shares its defect with id 8 at HIGH, item
H3, whose promotion `TOOL-dSafePassage-56` puts the link test on every path the walk enters; S6 adds
what id 23 asks beyond it. The report refuted ids 6 and 25 and left none unverified. The skeptic
re-graded ids 13, 16, 17 and 19 from medium to low. It REJECTED the finder's fix of id 12, so S8 is
built from the skeptic's corrected fix.

At rev-3, S4, AC12 and S1's half on TOOL-dSafePassage-51 AC2 are struck, and so is AC2 by §8 F1. TOOL-dSafePassage-49 rev-6
struck the header move they graded (its §8 F1, re-resolved to (d)), and TOOL-dSafePassage-51 rev-4
struck its S2, S3 and AC2 with it. Their numbers stay, so no cross-reference dangles.

## 2. Scope (IN)

### TOOL-51 AC1's attribution and form (M1, L5, L6, L9)

- **S1** — id 2. TOOL-dSafePassage-51 AC1 grades the commit order, which no write of
  TOOL-dSafePassage-51's pass can move. It is recorded as a check of the build run: its ledger line
  sits in an `**Evidences:** TOOL-dSafePassage-51` block of a record committed with `Pass: none`.
  Observed by AC1. Its half on TOOL-dSafePassage-51 AC2 is struck at rev-3, and so is its half on
  the hand-out refusal of the struck sweep, with the retired `TOOL-dSafePassage-55` that staged its
  red case.
- **S2** — id 13. TOOL-dSafePassage-51 S1 and §7 are read with the guard that already exists:
  TOOL-dTrueNorth-16 S2's edge refusal in `tools/unattended/unattended.sh` (`:13857-13926`), which
  stops a `--dispatch` with fail 49 while a same-build producer of the dispatched unit is neither
  CLOSED nor WONTDO. TOOL-dSafePassage-4 declares `consumes-from` on TOOL-dSafePassage-7 and
  TOOL-dSafePassage-43, so its early dispatch is already refused. TOOL-dSafePassage-51 §7 names that
  refusal as the guard of AC1's commit order at its rev-4. Observed by AC9.
- **S3** — id 16. TOOL-dSafePassage-51 AC1's probe is spelled whole-line, because
  `TOOL-dSafePassage-4` is a prefix of `TOOL-dSafePassage-43` to `-49`:
  `git log --reverse --format='%(trailers:key=Pass,valueonly)' <BASE>..HEAD | grep -n -x -m1 'TOOL-dSafePassage-4'`,
  and the same `-x` form for 43, 7, 18 and 19. Observed by AC10.
- **S4** — id 29. STRUCK at rev-3, number retained. It worded the TOOL-dSafePassage-43 Rollout
  amendment that TOOL-dSafePassage-51 S3 asked, which is struck at TOOL-dSafePassage-51 rev-4.
  NOT OBSERVED: struck.

### The link test's form, positions and population (M5, M6, M7)

- **S5** — id 18. The link test is one `os.lstat`. `test_path_linked(path)`
  (`TOOL-dSafePassage-56` S1) takes `os.lstat(path)`, reads False on `FileNotFoundError`, and reads
  True when `stat.S_ISLNK(st.st_mode)` holds or `getattr(st, "st_reparse_tag", 0)` is non-zero. That
  covers a symlink on every host, a junction on Windows, and every other reparse point, which is
  refused rather than followed. S8's `.gitmodules` test reads the same two fields, so the walk and
  the file share one rule. TOOL-dSafePassage-51 S6's test is read as that function. The finding's
  premise, a 3.11 floor, is gone: `tools/lib/python-floor.txt` declares `3.15` at HEAD `10511362a`
  (§8 F1). Observed by AC3.
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
  §4 "The arm's widening", Inventory, Alternatives and §7), `tools/govkit/upgrade_steps.py`,
  where TOOL-dSafePassage-49's pass defined it at line 261, and `tools/govkit/selftest.py`, which
  reads it at lines 3934 and 3938, as the census at this revision's HEAD found
  · by value: the class arm
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
- The listing handler, the sound baseline and the link test's positions: `TOOL-dSafePassage-53`,
  `TOOL-dSafePassage-54` and `TOOL-dSafePassage-56`.
- Rewriting a built spec. An item that corrects a spec's text states the reading here.
- The report's left-shift gates and checklist entries.

### Edges

- **consumes-from** `TOOL-dSafePassage-51` — AC1, S6's link rule and plant, S9's census, S12's section probe, S15's file test, §4, §7 and §10, which S1 to S3 and S5 to S12 read
- **consumes-from** `TOOL-dSafePassage-53` — the listing's `os.scandir` call, whose entries S7 tests before any filter
- **consumes-from** `TOOL-dSafePassage-56` — `test_path_linked` and its call at the top of the walk, whose form S5 fixes and whose root position S6 plants

## 4. Design

### The link test, one lstat

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
- **`os.path.islink` or `os.path.isjunction` (S5).** Two tests where one `lstat` and its reparse
  tag answer both hosts, the same pair `read_plain_stat` reads. It also follows any reparse point
  that is neither, where the tag refuses it.
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
  runs after TOOL-dSafePassage-51's pass, it shows an `AC1` line in a record whose commit carries
  `Pass: none`, not in a commit carrying `Pass: TOOL-dSafePassage-51`.
  Red when: the commit-order check is attributed to TOOL-dSafePassage-51's pass.
- **AC2** — STRUCK at rev-3 by §8 F1, number retained so no cross-reference dangles. It grepped
  `tools/govkit/upgrade_steps.py` for `isjunction` against a 3.11 floor the tree no longer declares.
  Red when: never; its premise is gone.
- **AC3** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `test_path_linked` on a scratch junction (on Windows) or directory symlink (on POSIX), it prints
  True. On a plain scratch directory and on an absent path it prints False.
  Red when: the test follows the link, as a copy testing `S_ISLNK` alone does on a Windows junction.
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
  Red when: the guard S2 cites is gone, so nothing holds AC1's commit order at dispatch.
- **AC10** — When `printf 'TOOL-dSafePassage-43\nTOOL-dSafePassage-7\n' | grep -n -x -m1 'TOOL-dSafePassage-4'`
  runs, a history holding only TOOL-dSafePassage-43's and TOOL-dSafePassage-7's commits, it prints
  nothing and exits 1.
  Red when: the probe matches a prefix, so TOOL-dSafePassage-43's commit reads as TOOL-dSafePassage-4's.
- **AC11** — When §4's section probe runs over `help/upgrade-steps.md` and each of the seven
  criteria S12 names runs its own grep pattern over that output, each prints the line its criterion
  asserts.
  Red when: a required term sits on the page but outside the section.
- **AC12** — STRUCK at rev-3, number retained so no cross-reference dangles. It counted a phrase
  in `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-43.md`, a CLOSED spec whose
  Rollout no pass now amends.
  Red when: never; S4 is struck.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC4 AC5 AC6 · the self-test runs `test_path_linked` over a scratch link, a plain directory and an absent path, and the `submodule-modules-root-link`, `submodule-modules-link-dangling` and `gitmodules-symlink` plants; its failing cases are staged by a link-test copy testing `S_ISLNK` alone, which reads a Windows junction as no link, a walk copy that lists the root without testing it, a walk copy that filters entries by `os.path.isdir` before the link test, and a `.gitmodules` read copy that takes `os.stat` before any link test · none

What the check does not cover: the `gitmodules-symlink` refusal on a host that refuses to make a
symlink, where only its `skip —` line is seen; the `S_ISLNK`-alone copy's red on a POSIX host, where
a directory symlink still reads linked, so only Windows hosts see it; a reparse point that is neither
a symlink nor a junction, which no plant here makes; and the ledger attribution of S1 beyond the
record's commit trailer.

## 8. Open questions

- **F1 — What does S5 keep now that the Python floor is 3.15?** S5, AC2 and AC3 rest on id 18's
  premise that govkit's floor is CPython 3.11, below `os.path.isjunction`'s 3.12. At HEAD
  `10511362a`, `tools/lib/python-floor.txt` declares `3.15`, and `help/python-floor.md` says every
  kit's resolver refuses below it, so that premise is false.
  - (a) Strike S5, AC2 and AC3. TOOL-dSafePassage-51 S6's `islink or isjunction` test stands, and
    `TOOL-dSafePassage-56`'s `test_path_linked` uses it.
  - (b) Keep S5's one `os.lstat` form on its other ground: a non-zero `st_reparse_tag` also refuses
    a reparse point that is neither a symlink nor a junction, the deny-by-default direction §5
    names, and S8 already reads the same tag. Strike AC2, and restate AC3 without deleting
    `isjunction` from `os.path`.
  - (c) Keep S5, AC2 and AC3 as written. AC3's deleted-attribute probe then stages an interpreter
    the resolver refuses to run.
  - Recommendation: (b). It keeps one link test for the walk and for `.gitmodules`, and drops only
    the criteria whose premise is gone.
  - RESOLVED (agent, 2026-10-28, delegated): (b), under BUILD-METHOD M3, by the unattended run that
    decides its own forks, on this spec writer's recommendation. S5 keeps its one `os.lstat` test on
    its own ground, AC2 is struck with its number kept, and AC3 observes the test with no floor
    claim.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 51 and 52's 5 MEDIUM and 7
  LOW findings on TOOL-dSafePassage-51, one scope item per raw id.
- rev-2 · 2026-10-26 · §7 · the §7 leg line gains `policy fixtures`, whose guard a §4 Files touched path
  trips, per the spec-tokens repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.
- rev-3 · 2026-10-28 · S1 · S2 · S4 · S5 · S10 · AC1 · AC2 · AC3 · AC9 · AC12 · §1 · §3 · §4 · §7 · §8 · §10 · per
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-55-1-spec-writer.md`:
  TOOL-dSafePassage-49 rev-6 struck F1(a)'s sweep, so S4 and AC12 are struck, numbers kept, S1 and
  AC1 keep TOOL-dSafePassage-51 AC1's attribution alone, and the edge to the retired
  TOOL-dSafePassage-55 is withdrawn with its mirror; S2's citation re-read at HEAD `10511362a` as
  `:13857-13926`; S10's Readers re-read at HEAD; §8 F1 opened on S5's 3.11 floor, which
  `tools/lib/python-floor.txt` now declares `3.15`, and RESOLVED (agent, delegated) to (b), so S5
  keeps its one `os.lstat` test without the floor claim, AC2 is struck with its number kept, AC3,
  §4, §7's arm and the S5 alternative are restated.

## 10. Reuse audit

The seams extended are named per item: TOOL-dSafePassage-51's walk, file test, AC1 and section
probe, `TOOL-dSafePassage-53`'s listing and `TOOL-dSafePassage-56`'s `test_path_linked`, all
specced and unbuilt at the base. S2's guard is the existing edge refusal at
`tools/unattended/unattended.sh:13857-13926`, re-read at HEAD `10511362a`. For S8 and S5 the
census grepped `tools/` by behaviour, for `st_reparse_tag`, `S_ISREG` and `lstat`, and found
`read_plain_stat` in `tools/run-gates/measure_legs.py:1373`, whose reparse-tag test S5 copies in
form and whose module S8 names and does not import. `python tools/codebase-map/reuse_lookup.py "refuse a path that is a symlink or junction before listing it"`
ranked `before`, `CensusRefused` and `ScopeRefused`, name-token matches that miss that seam, which is
where the map and the behaviour grep disagree. So no existing seam fits beyond those specs and that
form.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted units' passes" --terms "spec audit minors batched reading hands-off walk link junction refusal order section probe"`
