# TOOL-dSafePassage-42 — the spec audit of units 27 to 35: its 27 minors, per-row postconditions, discriminating criteria, one blanked population and the texts that cite them

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 10 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-42-deviation-88.md](../build/2026-10-23-build-TOOL-dSafePassage-42-deviation-88.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-prompt-TOOL-dSafePassage-42-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-42-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-42-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-42-hygiene-fix.md) | research | TOOL-dSafePassage-38 TOOL-dSafePassage-39 |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-42-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-42-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-38 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 27 to 35
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`)
exited CONVERGED with 33 confirmed findings: 6 HIGH, promoted as units 36 to 41, and 27 minors. This
unit is the batch BUILD-METHOD M4 makes of the minors, every MEDIUM and every LOW, each by its report
id and each its own scope item, where the report merged ids into one item too. The minors land on
eight units, so this unit repairs none in particular and builds after every unit, order 10. Where a
minor would bite an earlier pass, the hands-off bullet the faulted unit's own §3 carries to this one
names it; where a finding's defect is the text of a spec built before this one, the item states the
superseding reading, because a built spec is not rewritten, and a criterion here observes it where
anything can.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-7 | MEDIUM | 1, 10, 31 | S1, S2, S3 |
| D-8 | MEDIUM | 2 | S4 |
| D-9 | MEDIUM | 9 | S7 |
| D-10 | MEDIUM | 27 | S8 |
| D-11 | MEDIUM | 21 | S9 |
| D-12 | MEDIUM | 24 | S10 |
| D-13 | MEDIUM | 11 | S11 |
| D-14 | MEDIUM | 18 | S12 |
| D-15 | MEDIUM | 12 | S14 |
| D-16 | MEDIUM | 25 | S15 |
| D-17 | LOW | 3, 13 | S16, S17 |
| D-18 | LOW | 19 | S18 |
| D-19 | LOW | 14, 33 | S5, S6 |
| D-20 | LOW | 4, 15 | S19, S20 |
| D-21 | LOW | 5 | S21 |
| D-22 | LOW | 6 | S22 |
| D-23 | LOW | 7 | S23 |
| D-24 | LOW | 16 | S24 |
| D-25 | LOW | 17 | S25 |
| D-26 | LOW | 20 | S26 |
| D-27 | LOW | 26 | S27 |
| D-28 | LOW | 32 | S13 |

That is 12 MEDIUM and 15 LOW findings by raw id; the report refuted none and left none unverified.
The skeptic REJECTED the finders' fixes of ids 17 and 32, so S25 and S13 are built from the skeptic's
corrected fixes; id 28's corrected fix is the high `TOOL-dSafePassage-37`.

## 2. Scope (IN)

### The prepared landing's refusals and their arm (D-7, D-8, D-19, D-14, D-28, D-27)

- **S1** — id 1. TOOL-dSafePassage-28 S3 and AC2 are read per row: the compare-and-swap row asserts
  the branch at the sha the plant moved it to, checked out, `git status --porcelain` empty and no
  `.governance/steps` or `.governance/outbox` path left; every other row keeps "at its old sha".
  Observed by AC1.
- **S2** — id 10. The `expect` column of `PREPARE_REFUSALS` (TOOL-dSafePassage-28 §4) names each row's
  expected branch value, `old` or `moved`, and the arm asserts against it. The value is read after
  `tools/push-main.sh:938`'s refused `git update-ref "refs/heads/$branch" "$t" "$oldb"` and its
  `git checkout "$branch"` at `:939`, which leave the branch where the plant moved it. Observed by AC1.
- **S3** — id 31. The compare-and-swap row keeps its clean-tree observation under the moved-branch
  expectation, so the one row that exercises that refusal still observes what it leaves behind, and
  the arm reads green on the shipped lander. Observed by AC1.
- **S4** — id 2. TOOL-dSafePassage-27 §1 is read as: the refused run's leftovers make the next
  `--prepare` refuse at its dirty-tree precondition (`tools/push-main.sh:860-865`,
  `git status --porcelain --ignore-submodules=untracked`, which lists untracked files), before the
  merge, so nothing is folded. Its AC2 is read with this clause in place of the `git ls-tree` clause:
  the retry exits 0 and does not print the "working tree has uncommitted changes or untracked files" refusal.
  Observed by AC2.
- **S5** — id 14. TOOL-dSafePassage-27 §1's cite of `--prepare`'s `git add -A` is read as `:920`;
  `:918` is `rm -f "$rgsnap"`. Observed by AC3.
- **S6** — id 33. TOOL-dSafePassage-27 AC2's red case is read as "the retry refuses at the dirty-tree
  precondition, naming a path the refused run left", observed on a lander copy whose regeneration
  refusal cleans against a snapshot taken after the walk. Observed by AC2.
- **S12** — id 18. TOOL-dSafePassage-28's derived count reuses `scan_shell_lines`
  (`tools/memory-tree/check-arms.py:305`), the blanking check-arms signature 2 applies before it reads
  a site (`:74-75`): the arm loads that module by path and counts `return 1` in the `code` column of
  `cmd_prepare`'s lines, here-document and continued lines aside. Check-arms itself is not extended,
  because its population declares `return 1` outside it (`:113-115`) for every gate in the tree, and
  widening it for one function would grade every script's `return 1`. TOOL-dSafePassage-28 §10 is read
  with this seam named. Observed by AC9.
- **S13** — id 32, the skeptic's corrected fix. The count's anchor is the call shape
  `^[[:space:]]*if ! run_gov_first`, never the first mention of the name, and a line counts when its
  code holds `return 1` as a word, so `cmd || return 1` forms count. TOOL-dSafePassage-28 §5 risks is
  read with "the anchor is the call, not the name". Observed by AC9.
- **S27** — id 26. The added fixture landings are priced: at this pass one added `--prepare` fixture
  landing is timed by direct CLI, and the `push-main self-test` row of
  `tools/run-gates/selftest-budgets.txt` (`:88`, 320 s, "worst of 11 readings 209s, x1.5") is
  re-priced as a PINNED proxy: 209 s plus the measured landing times the count TOOL-dSafePassage-27 and
  TOOL-dSafePassage-28 added, x1.5, its comment naming both units and saying it is re-priced from the
  first measured run, as `measure-legs selftest`'s row (`:74`) is priced. Observed by AC17.

### The step contract's population and keys (D-9, D-10, D-21, D-22)

- **S7** — id 9. The predicate (TOOL-dSafePassage-29 §4, widened by `TOOL-dSafePassage-37`) also keeps
  the last segments `tunnel`, `httpd` and `smtpserver`. `STEP_REFUSED_KEYS` refuses `imap.tunnel` and
  `instaweb.httpd` with any value, and `sendemail.smtpServer` when its value is an absolute path, which
  git runs as a program. TOOL-dSafePassage-29 S5's sentence is read as "the class the predicate names",
  and `TOOL-dSafePassage-37`'s §7 list loses these three. Observed by AC4.
- **S8** — id 27. TOOL-dSafePassage-30 S1's order is read as: each repository's config is read and
  graded (`config --list`, which runs nothing) and refused before any index-reading command runs in it,
  and the gitlink read runs as `git -c core.fsmonitor=false ls-files -s -z`. The `isolation` family
  gains `submodule-fsmonitor`, a nested repository whose `core.fsmonitor` names a canary. Observed by
  AC5.
- **S21** — id 5. TOOL-dSafePassage-29 S5's rewrite of "What a step can reach" keeps the literals
  TOOL-dSafePassage-24's AC5 greps, `filter.<x>.clean`, `extraheader` and `merge.<driver>.driver`, and
  TOOL-dSafePassage-29's AC5 is read with `filter.<x>.clean` and `extraheader` added to its grep.
  Observed by AC12.
- **S22** — id 6. `reached_by` for a `modules/` row (TOOL-dSafePassage-30 §4) is the path the
  worktree's `.gitmodules` maps that name to, read by
  `git config -f <worktree>/.gitmodules --get-regexp '^submodule\..*\.path$'`, and the name marked
  `by name` where no mapping exists. The `isolation` family gains `submodule-name-differs`, a submodule
  named `nm` at the path `lib/p`. Observed by AC13.

### The lander's snapshot criterion (D-16, D-17, D-18)

- **S15** — id 25. TOOL-dSafePassage-35 AC9's count is read over code lines only: comment lines are
  outside its population. Observed by AC11.
- **S16** — id 3. Its command is read as `git grep -n` filtered of comment lines, not `git grep -c`,
  which prints `tools/push-main.sh:N` rather than a bare count. Observed by AC11.
- **S17** — id 13. TOOL-dSafePassage-35 S10's rewritten comment at `tools/push-main.sh:777-783` may
  keep its phrase; no criterion depends on how a comment is worded. Observed by AC11.
- **S18** — id 19. `remove_new_untracked` (`tools/push-main.sh:788`) calls
  `write_untracked_snapshot "$now"` for its current set, so the two sets `comm -z -13` compares come
  from one writer, and AC9 is read as one code line spelling the read, inside
  `write_untracked_snapshot`. Observed by AC11.

### The rest of TOOL-dSafePassage-35, read against its sources (D-13, D-15, D-20, D-24)

- **S11** — id 11. TOOL-dSafePassage-35 AC12's population is read as the parity arm's own
  (`tools/lib/resolve-python.test.sh:218`, its exclusion at `:169`):
  `git grep -l "^# >>> resolve_python" -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md` less
  `tools/lib/resolve-python.sh`, every block in a file graded by ordinal. It held 69 files at
  `bb9a4871` on 2026-10-23 (PINNED; the report read 70 and the unanchored set 91). Observed by AC8.
- **S14** — id 12. TOOL-dSafePassage-35 S24's moved set is read as its ast closure, derived at this
  disposal over `tools/govkit/govkit.py`: `resolve_shell_argv` (`:1200`), `resolve_bash` (`:1144`),
  `resolve_tokens` (`:1233`), `target_context` (`:1436`) and `demand_safe_token` (`:1406`), which
  `target_context` calls, move; the constants `_BASH`, `TOKEN_RX`, `OPT_IN_ALL`, `PER_KIT_PATH_TOKENS`,
  `SEEDED_TOKENS`, `ANSWER_VALUE_RE`, `DRIVE_PREFIX_RE` and `TOKEN_VALUE_RE`, and the class `Refusal`,
  are each moved or copied, govkit re-importing what moves; `resolve_kit_dir` (`:197`) stays the inline
  copy S24 names. Its §5 risk line is read as five functions and eight constants. Observed by AC10.
- **S19** — id 4. TOOL-dSafePassage-35 AC18 is read as a regression guard, green before that unit's
  pass, whose failing case is a later edit to a cited spec. NOT OBSERVED: the criterion stays as
  written, and only its role in the ledger changes.
- **S20** — id 15. TOOL-dSafePassage-35 S21 is read as a recorded reading that no pass moves, its AC18
  the guard of S19. NOT OBSERVED, for S19's reason.
- **S24** — id 16. TOOL-dSafePassage-35 S9's pin is read at `tools/govkit/refusal_join.py:41`, where
  `BRANCH_PIN = 255` is defined, `:235` being its comparison; its S1 is read as: only
  `tools/govkit/govkit.py:4682-4684` applies the `missing` filter, and `:5059-5061` filters on
  `kind == "write"` alone. Observed by AC14.

### The lock record and its probes (D-12, D-25)

- **S10** — id 24. TOOL-dSafePassage-31 §4's lock record is read with `started_boot`, present only where
  `CLOCK_BOOTTIME` exists (TOOL-dSafePassage-32 S2):
  `{pid, verb, started, started_utc, started_boot, host, platform, boot_id, pid_ns}`, written by the one
  `json.dumps` of `take_write_lock` (`tools/govkit/govkit.py:7430`), and that unit is read as consuming
  TOOL-dSafePassage-32's key, which the build order already places before it. Observed by AC7.
- **S25** — id 17, the skeptic's corrected fix. TOOL-dSafePassage-31's and TOOL-dSafePassage-32's AC1
  WSL probes are spelled with the checkout's path inside the program text, never as an argument of its
  own, because Git Bash rewrites a `/mnt/c` argument to `wsl.exe` (the report's probe printed
  `C:/Program Files/Git/mnt/c/...`). Observed by AC15.

### The `ac-order` join's key and write set (D-11, D-23, D-26)

- **S9** — id 21. `cutoff_keys_armed` (`tools/drift-audit/drift_signals.py:351`, `weakens: up` at
  `:459`) rises 36 -> 37 with an in-place comment naming TOOL-dSafePassage-34's
  `SPEC_AC_ORDER_CUTOFF`, under a `memory/DECISIONS.md` row in TOOL-dTrueNorth-28's form (§8 F1).
  TOOL-dSafePassage-34 §7 is read with `drift-audit records` and `drift-audit selftest`. Between
  TOOL-dSafePassage-34's pass and this one the signal reads 37 against 36; no pass runs the bar
  (BUILD-METHOD M6), and the bar's one run at the close reads this raise. Observed by AC6.
- **S23** — id 7. TOOL-dSafePassage-34's write set is read with
  `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-8.md`, which joins its
  `--dispatch --writes` when its S3 edits that spec, as TOOL-dSafePassage-35 §4 declares its own spec
  write. NOT OBSERVED: a write set recorded at TOOL-dSafePassage-34's dispatch, before this pass; its
  §3 hands-off bullet to this unit carries the reading there.
- **S26** — id 20. TOOL-dSafePassage-34 S1 and §10 are read with `SPEC_DATE`
  (`tools/check-spec-tokens.py:896`, bound from `design_lib.SPEC_FILE_DATE`) as the date the join
  grades, matched as `SPEC_DATE.search("/" + f)` (`:1466`, `:1508`), which `TOOL-dSafePassage-41`'s join
  reads. Observed by AC16.

## 3. Non-goals (OUT)

- Every high: units 36 to 41.
- Rewriting a built spec. An item that corrects a built spec's text states the reading here.
- The report's left-shift lints: a `<path>:<line>` cite lint, an already-green-at-writing check, a
  spec-tokens join over `_CUTOFF` keys, and the checklist entries the report proposes per item.

### Edges

- **consumes-from** `TOOL-dSafePassage-27` — the one snapshot, its Goal and AC2, which S4, S5 and S6 read, and its added landings, which S27 prices
- **consumes-from** `TOOL-dSafePassage-28` — `PREPARE_REFUSALS`, its derived count and its fixture landings, which S1, S2, S3, S12, S13 and S27 amend and price
- **consumes-from** `TOOL-dSafePassage-29` — `STEP_REFUSED_KEYS` and the help section's rewrite, which S7 extends and S21 keeps whole
- **consumes-from** `TOOL-dSafePassage-30` — `read_target_repositories` and `reached_by`, which S8 reorders and S22 spells
- **consumes-from** `TOOL-dSafePassage-31` — the lock record and its WSL probe, which S10 and S25 read
- **consumes-from** `TOOL-dSafePassage-32` — the boot reading and its WSL probe, which S10 and S25 read
- **consumes-from** `TOOL-dSafePassage-34` — `SPEC_AC_ORDER_CUTOFF`, its write set and its S1, which S9, S23 and S26 price and read, S9's raise landing in that unit's pass as `TOOL-dSafePassage-46` reads it
- **consumes-from** `TOOL-dSafePassage-35` — AC9, AC12, AC18, S1, S9, S10 and S24, which S11, S14 to S20 and S24 read, and `write_untracked_snapshot`, which S18 calls
- **consumes-from** `TOOL-dSafePassage-37` — the predicate's `hook` suffix and §7 list, beside which S7 adds three names
- **consumes-from** `TOOL-dSafePassage-41` — the `ac-order` join, whose date read S26 observes
- **hands-off** `TOOL-dSafePassage-45` — S7's `sendemail.smtpServer` row read with git-send-email's absoluteness test and its identity form, S10 and AC7 read with an `ast` probe of the one writer and the fixture kept valid, S22 read with its exits and nested map, and AC3, AC14 and AC15 read as regression guards, findings 9, 22, 3, 11, 17, 23, 4 and 26 of the spec audit of units 36 to 42
- **hands-off** `TOOL-dSafePassage-46` — S9's pin raise read as landing in TOOL-dSafePassage-34's pass, and S12's arm loading `check-arms.py` from the memory-tree kit found beside the lander, with a skip where it is absent, findings 25 and 15 of the spec audit of units 36 to 42

## 4. Design

### The compare-and-swap row

```
PREPARE_REFUSALS (stage, plant, expect):
  ...
  compare-and-swap   regen.py commits on the branch, then exits 0   moved
assert per row: rc 1; branch == (oldb if expect == old else the plant's commit); branch checked out
                `git status --porcelain` empty; no .governance/steps or outbox path
```

### The derived count

```
rows  = scan_shell_lines(text of tools/push-main.sh)             # check-arms.py:305
body  = the rows of cmd_prepare, from the first matching ^[[:space:]]*if ! run_gov_first to its }
count = rows of body, not heredoc and not continued, whose code holds \breturn 1\b
```

### Inventory

Minted: the plants `submodule-fsmonitor` and `submodule-name-differs`; the `expect` values `old` and
`moved`; the `reached_by` marker `by name`. No function, conf key, gate leg or policy key; S9 raises
one drift pin and S27 re-prices one budget row. No new `raise Refusal` site: S7's rows and S8's order
use TOOL-dSafePassage-24's one site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no landed step row, lock record or receipt step exists before this build lands.

### Rollout

Live at landing. It builds at order 10, after every unit of the build, units 36 to 41 included. Its
lander items' fixtures run govkit's walk, whose code S7, S8 and S22 write, so the second half would
read the first's output as an acceptance input (M6 clause 2): the minors do not split into two
disjoint write sets, and the pass is one unit.

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/drift-audit/drift_signals.py`
- `tools/run-gates/selftest-budgets.txt`
- `memory/DECISIONS.md`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Two batch units, the lander's items apart.** M6 clause 2, as §4 "Rollout" says.
- **Extending check-arms signature 2 to `return 1` (S12).** Its population is declared tree-wide, so
  the extension would grade every script's `return 1`, not one function's.
- **Sharing one fixture clone across `PREPARE_REFUSALS`' rows (S27).** It changes two built units'
  arms to save a cost no reading has yet shown over the row; the measured proxy states it instead.
- **Folding each minor into its unit's spec.** The disposal promotes, never folds (BUILD-METHOD M4).

## 5. Production-readiness checklist

- security: S7 refuses three more executor keys; S8 runs no repository's fsmonitor before its config is
  graded.
- perf / scale: S27 measures one landing and re-prices the suite's row; S8 adds one `-c` pair per
  gitlink read.
- error / empty / loading states: S13's anchor matching nothing is a zero count, which
  TOOL-dSafePassage-28 §5 already reds.
- observability: S22's refusal spells a submodule by its path, or says it names one by its name.
- risks: S9 raises a shrink-only pin, recorded with its reason; S14's closure moves names other suites
  may monkeypatch, and govkit re-imports each.
- testing: the probes and fixtures of §6 and the arms of §7.
- migration: none.
- user docs: `help/upgrade-steps.md` (S7, S21).

## 6. Acceptance criteria

- **AC1** — When the compare-and-swap row's fixture landing `bash tools/push-main.sh --prepare --slug fx`
  runs with the planted `regen.py` that moves the branch, it exits 1, `git rev-parse refs/heads/<branch>`
  prints the plant's commit, `git symbolic-ref HEAD` names the branch and `git status --porcelain`
  prints nothing; `git grep -n "PREPARE_REFUSALS" -- tools/push-main.test.sh` shows `moved` for that row
  and `old` for every other.
  Red when: the row asserts the old sha and reds on a correct lander, or drops its clean-tree check.
  fixture: TOOL-dSafePassage-28's scratch clones under `%TEMP%`.
- **AC2** — When TOOL-dSafePassage-27's fixture retry `bash tools/push-main.sh --prepare --slug fx`
  runs after the refused run, it exits 0 and its stderr holds no "working tree has uncommitted changes
  or untracked files" line; on a lander copy whose regeneration refusal cleans against a snapshot taken
  after the walk, the retry prints that refusal naming a `.governance/steps` or `.governance/outbox`
  path.
  Red when: the retry's check cannot tell a leftover from the paths the retry makes again.
- **AC3** — When `git show "3708a705:tools/push-main.sh" | sed -n '918p;920p'` runs, it prints
  `rm -f "$rgsnap"` and the `git add -A` line.
  Red when: the cite S5 states names another line.
  figure: PINNED at `3708a705`.
- **AC4** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path, `STEP_REFUSED_KEYS`
  refuses `imap.tunnel` and `instaweb.httpd` with any value and `sendemail.smtpServer` valued
  `/usr/bin/x`, not valued `smtp.example.com`; and the predicate over `git help --config` keeps all
  three and every kept key matches one row.
  Red when: an executor key the predicate keeps by these names passes, or a host name is refused.
  figure: the kept count is DERIVED; 49 was read on node d on 2026-10-23.
- **AC5** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-fsmonitor`
  runs, the step is refused naming `core.fsmonitor` and the nested repository, the canary is absent
  after the refusal, and the run exits 1.
  Red when: the population walk's index read runs the fsmonitor before any config is graded.
- **AC6** — When `python tools/drift-audit/drift_report.py --json` runs after the pass,
  `cutoff_keys_armed` reads a value equal to its tolerance, and
  `git grep -n -e "TOOL-dSafePassage-34" -- tools/drift-audit/drift_signals.py memory/DECISIONS.md`
  prints the raise comment and the decision row.
  Red when: the armed count exceeds its pin.
  figure: DERIVED by the run; 37 of 37 expected after TOOL-dSafePassage-34's key.
- **AC7** — When a `python -c` probe calls `take_write_lock` with `read_boot_clock` stubbed to a float
  and `read_pid_namespace` to `pid:[4026532221]`, the record holds both `started_boot` and `pid_ns`, and
  `git grep -n "started_utc" -- tools/govkit` prints one record writer.
  Red when: the record drops `started_boot`.
- **AC8** — When a `bash -c` probe extracts every `resolve_python` block of the population S11 spells,
  strips CR bytes and compares each by ordinal with the canonical block, no copy differs, no file under
  `memory/` is in the population, and the probe prints the file count.
  Red when: the population takes a file that quotes the marker in prose.
  figure: the count is DERIVED; 69 was read at `bb9a4871`.
- **AC9** — When a `python -c` probe loads `tools/memory-tree/check-arms.py` by path and counts as S12
  and S13 say, the count equals the rows of `PREPARE_REFUSALS`; on a lander copy carrying a
  `# return 1` comment, an `echo "return 1"` line and a comment naming `run_gov_first` above the mint
  block, the count is unmoved.
  Red when: a comment or a quoted `return 1` is counted, or the anchor resolves above the call.
- **AC10** — When a `python -c` probe parses `tools/govkit/upgrade_steps.py` with `ast`, it defines
  `demand_safe_token` and the four functions S24 names, and each of the eight constants and `Refusal` is
  defined there or imported by govkit from there.
  Red when: a name of the closure is reached back into govkit.
- **AC11** — When `git grep -n "ls-files --others --exclude-standard -z" -- tools/push-main.sh | grep -v ':[0-9]*:[[:space:]]*#'`
  runs, it prints one code line, inside `write_untracked_snapshot`, and
  `git grep -n "write_untracked_snapshot" -- tools/push-main.sh` prints its definition and its calls,
  one inside `remove_new_untracked`.
  Red when: a second code site spells the read.
- **AC12** — When `git grep -n -e "filter.<x>.clean" -e "extraheader" -e "merge.<driver>.driver" -e "git help --config" -- help/upgrade-steps.md`
  runs, the "What a step can reach" section prints all four.
  Red when: the class sentence replaces TOOL-dSafePassage-24's named keys.
- **AC13** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-name-differs`
  runs, the refusal reads `(submodule lib/p)`; with the `.gitmodules` mapping removed it reads
  `(submodule nm, by name)`.
  Red when: the refusal spells the name where a path exists.
- **AC14** — When `grep -n "^BRANCH_PIN" tools/govkit/refusal_join.py` and
  `git show "3708a705:tools/govkit/govkit.py" | sed -n '4684p;5061p'` run, the first prints line 41 and
  only the first `govkit.py` line tests `missing`.
  Red when: either cite S24 states is wrong.
  figure: PINNED at `3708a705` and HEAD.
- **AC15** — When `wsl.exe -d Ubuntu -- python3 -c "import sys; sys.path.insert(0, '/mnt/c/<checkout>/tools/govkit'); import upgrade_steps; print(upgrade_steps.read_boot_clock())"`
  runs from Git Bash with the checkout's path written inside the program text, it prints a float, and
  the same probe of `read_pid_namespace()` prints `pid:[<digits>]`.
  Red when: the path is passed as its own argument and the import finds nothing.
  fixture: the WSL distro `Ubuntu` on node d (read 2026-10-23).
- **AC16** — When `git grep -n -e "SPEC_FILE_DATE" -e "SPEC_DATE.search" -- tools/check-spec-tokens.py`
  runs, the `ac-order` join's date read is a `SPEC_DATE.search("/" + f)` line and the file binds no
  second filename-date pattern.
  Red when: the join spells its own date regex.
- **AC17** — When `grep -n "^push-main self-test" tools/run-gates/selftest-budgets.txt` runs, the row
  names TOOL-dSafePassage-27, TOOL-dSafePassage-28 and the measured per-landing seconds, and its budget
  is the proxy S27 states.
  Red when: the row still prices the suite from the 209 s reading alone.
  figure: PINNED at the pass, from that pass's direct landing.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `drift-audit records` · `push-main self-test` · `measure-legs selftest` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC4 AC5 AC13 · the self-test runs the two plants this unit adds and the widened class arm, its failing cases staged by a walk copy that reads the index first and by a table copy missing the `imap.tunnel` row · none
New arm: tools/push-main.test.sh · covers AC1 AC9 · the compare-and-swap row under its `moved` expectation and the blanked derived count, their failing cases staged by a row expecting `old` and by a lander copy carrying a commented `return 1` · none

## 8. Open questions

- **F1 — The `cutoff_keys_armed` pin (S9).** Options: (a) raise it 36 -> 37 in place with a comment
  naming TOOL-dSafePassage-34 and a `memory/DECISIONS.md` row, as TOOL-dTrueNorth-28 raised it 34 -> 36
  under ER:388; (b) leave the pin and park the raise for the owner, which the chain's rung 5 forbids
  where a standing ruling takes it; (c) not arm `SPEC_AC_ORDER_CUTOFF`, which fails TOOL-dSafePassage-34
  and `TOOL-dSafePassage-41` outright. (a) is the only option meeting every criterion; a shrink-only pin
  is a veto-2 change outside this build's grant, which ER:388 takes. RESOLVED (agent, 2026-10-23,
  delegated): (a), on rung 5, under ER:388. widens: the drift pin `cutoff_keys_armed` 36 -> 37 ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 27 to 35's 12 MEDIUM and 15
  LOW findings, one scope item per raw id.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 36 to 42, written by the disposal stage: `TOOL-dSafePassage-45`, `TOOL-dSafePassage-46`; the existing `TOOL-dSafePassage-34` bullet names the move; no other section moved.
- rev-3 · 2026-10-26 · AC3 · AC14 · §7 · AC3's and AC14's `git show` revision paths are quoted; the §7
  leg line gains `policy fixtures`, whose guard a §4 Files touched path trips, per the spec-tokens
  repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.

## 10. Reuse audit

The seams extended are named per item: `scan_shell_lines` (`tools/memory-tree/check-arms.py:305`), the
lander's refusals (`tools/push-main.sh:860-865`, `:938-942`) and `remove_new_untracked` (`:784-793`),
the parity arm's population (`tools/lib/resolve-python.test.sh:169`, `:218`), `take_write_lock`
(`tools/govkit/govkit.py:7430`), the drift pin (`tools/drift-audit/drift_signals.py:351`), the budget
row (`tools/run-gates/selftest-budgets.txt:88`), `SPEC_DATE` (`tools/check-spec-tokens.py:896`), and the
specced seams of units 27 to 41. `python tools/codebase-map/reuse_lookup.py "carry a row field forward
when its writer rewrites the row"` and the probes of units 36 to 41 ranked name-token matches only;
`scan_shell_lines` was found by reading the lines the report cites at `check-arms.py:74-75`, and where
the report and the source disagreed, the parity population read 69 files at `bb9a4871` where the
report says 70.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's promoted repairs are placed and sequenced after the unit they repair" --terms "spec audit promoted repair unit order edges hands-off consumes-from minors batch disposal rescope"`
