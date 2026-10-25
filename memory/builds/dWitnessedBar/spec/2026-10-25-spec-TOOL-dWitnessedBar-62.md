# TOOL-dWitnessedBar-62 — the round-1 audit of units 52 to 57, its 39 minors batched: readers that agree on every form, arms that compare what they arm, floors and greps that can red, and contained, lossless reads

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 34 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |
| [2026-10-25-build-TOOL-dWitnessedBar-58-round3-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-58-round3-fix-return.md) | research | TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-58-round3-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-58-round3-fix-brief.md) | research | TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 |
| [2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 52 to 57
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md`)
exited CONVERGED with 43 confirmed findings. Its 4 highs are units 58 to 61, one per id. BUILD-METHOD M4
batches every MEDIUM and LOW into one unit, two only where they split into disjoint write sets by M6's
clauses; these do not (§4 "Why one unit"). Each finding is named by report id and is its own scope item,
where the report merged ids into one item too. The minors land on several units, so this unit repairs
none in particular and builds after every unit (order 34).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1, 14, 38 | S1, S2, S3 |
| M2 | MEDIUM | 2 | S4 |
| M3 | MEDIUM | 3, 18, 36 | S5, S6, S7 |
| M4 | MEDIUM | 4 | S8 |
| M5 | MEDIUM | 5, 17, 31 | S9, S10, S11 |
| M6 | MEDIUM | 6, 15 | S12, S13 |
| M7 | MEDIUM | 16 | S14 |
| L11 | LOW | 32 | S15 |
| M8 | MEDIUM | 23 | S16 |
| M9 | MEDIUM | 24 | S17 |
| M10 | MEDIUM | 29 | S18 |
| M11 | MEDIUM | 30 | S19 |
| M12 | MEDIUM | 33 | S20 |
| M13 | MEDIUM | 37 | S21 |
| M14 | MEDIUM | 39 | S22 |
| M15 | MEDIUM | 40 | S23 |
| M16 | MEDIUM | 42 | S24 |
| M17 | MEDIUM | 43 | S25 |
| L8 | LOW | 22 | S26 |
| M18 | MEDIUM | 44 | S27 |
| L1 | LOW | 7 | S28 |
| L2 | LOW | 9, 34 | S29, S30 |
| L3 | LOW | 10 | S31 |
| L4 | LOW | 11 | S32 |
| L5 | LOW | 19 | S33 |
| L6 | LOW | 20 | S34 |
| L7 | LOW | 21 | S35 |
| L9 | LOW | 25 | S36 |
| L10 | LOW | 26 | S37 |
| L12 | LOW | 41 | S38 |
| L13 | LOW | 45 | S39 |

That is 25 MEDIUM and 14 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 1. `TOOL-dWitnessedBar-54` S3's parity arm compares only rows carrying all three of
  `write`, `check` and `stage`. A row lacking them is skipped by regen before its `when` is read
  (`tools/run-gates/regen.py:180-181`) and kept by lib-unattended (`tools/unattended/lib-unattended.sh:882`);
  the arm prints such a row as `not compared <descriptor> <path>` and its docstring names that
  disagreement, which `tools/memory-tree/kit.toml:498-501` already carries, as what it does not check.
  Observed by AC1.
- **S2** — id 14. The admissible forms sit in one scratch tree: conf true, conf false, `exists:` present
  and `exists:` absent, each row carrying `write`, `check` and `stage`. `regen.build_items`' kept paths
  equal `resolve_generated_indexes`' kept pairs. Observed by AC1.
- **S3** — id 38. Each refused form sits alone in its own scratch tree beside one conf-true row: an
  unknown token, an empty path, and S21's and S22's shapes. `build_items` raises `Refusal` naming the
  row, lib-unattended prints its skip line and keeps the conf-true row, and selfcheck refuses.
  Observed by AC2.
- **S4** — id 2. `TOOL-dWitnessedBar-53`'s arm asserts that each row seeded before the commit carries the
  null SHA of `TOOL-dWitnessedBar-61` and each row of the re-seed carries the commit's HEAD; the compare
  is over the key and count columns. Observed by AC3.
- **S5** — id 3. The arm's population P is every population the first `seed --all` reports `present` or
  `armed`, each home saved before the commit; after the commit every home of P is cleared, re-seeded and
  compared, and unit 53 S2's non-empty rule holds over that union. Observed by AC3.
- **S6** — id 18. The arm's fixture adds a second registration that no adopter seeds, so a seed the first
  `seed --all` itself arms is compared too. Observed by AC4.
- **S7** — id 36. A staged break makes that registration's seed read `git ls-files` only; the arm reds on
  it. Observed by AC4.
- **S8** — id 4. At the close the main loop runs the leg `run-gates gov canary` and writes unit 43's AC1,
  AC2 and AC4 lines in its acceptance ledger in the OBSERVED form carrying that leg's name; unit 56's
  AC15 line names that observation, and its grep clause, true before unit 56's pass, is not recorded as
  evidence. Observed by AC5.
- **S9** — id 5. For each of `tools/run-gates/run-gates.evidence.test.sh`,
  `tools/run-gates/run-gates.gov.test.sh`, `tools/run-gates/adopt-run-gates.test.sh` and
  `tools/memory-tree/check-memory-hygiene.test.sh`, the floor carries one
  `RAISED <old> -> <new> by TOOL-dWitnessedBar-<n>` comment per unit among 40, 41, 42, 43, 45, 46 and
  51 whose arm lands in that suite, each raising by that unit's assertion count; this pass writes every
  one unit 56 S19's pass left out. Observed by AC6.
- **S10** — id 17. Unit 56's own arms carry their own `RAISED` line; where the executed count the close
  observes exceeds a floor, the floor rises to that count, so no floor sits below what runs.
  Observed by AC6.
- **S11** — id 31. Each floor is shown able to red: deleting one arm of a listed unit from its suite,
  one of unit 42's evidence arms among them, reds that suite on its floor line. Observed by AC7.
- **S12** — id 6. The hook takes a `selection.<n>` value as the whole line after the key's first TAB,
  read with `IFS= read -r`, so an empty note, the last field, survives the rebuild that unit 56 S1 makes;
  `IFS=$'\t' read -r k v` (`.githooks/pre-push:1425`, `tools/run-gates/run-gates.sh:2392`) strips it.
  Observed by AC8.
- **S13** — id 15. The selection fixture holds a `quarantine` row with an empty note; its record's
  `selection` hash equals the rebuilt text's and the hook adopts the record. Observed by AC8.
- **S14** — id 16. `tools/run-gates/README.md` names `selection_ignored`, `TAIL_GRACE_S` and
  `GATE_POLICY_FILE`, each grepped on its own; this pass writes whichever is missing. Observed by AC9.
- **S15** — id 32. The same README names unit 40's two declines by the phrase their lines print,
  `no gate-verdict written`, twice; `reused_cache`, present before any unit, is no part of the check.
  Observed by AC9.
- **S16** — id 23. A unit's pass commit, for `TOOL-dWitnessedBar-57` S16 and S17 and for
  `TOOL-dWitnessedBar-51` S1 and AC8, is what `build_commit` (`lib-unattended.sh:1186`) answers over
  `cdfbd1cf..HEAD` with the build folder `memory/builds/dWitnessedBar` and the conf's
  `GENERATED_INDEXES` and `SHARED_RECORDS`. Unit 57's separate `git log | awk` rule is not built; no
  answer refuses naming the id. Observed by AC10.
- **S17** — id 24. `drift_report.py`'s reading of the selection file's `quarantine` and `level` rows is
  `verdict_flow.py`'s row-acceptance function, carried inline between `# >>> selection_row` markers
  under a new `PARITY_ROWS` row in `tools/lib/resolve-python.test.sh`, as unit 51 S21 carries
  `test_held`. Observed by AC11.
- **S18** — id 29. Every `drift_report.py --gate-health` caller passes `--selection`. Unit 1's S4 write
  path passes the file `verdict_flow.py select --rev <R> --out` writes. Unit 1's AC1 to AC3 and unit 51's
  AC17, observed at the close, pass an empty file from the run's scratch where the mode holds no held
  row, and the `held` fixture's own file for unit 51's AC17; each ledger line names the argument.
  Observed by AC12.
- **S19** — id 30. Unit 57's coverage figure is 77, as `--coverage` prints it: the §4 probe below
  applies unit 50's named exclusion, `tools/unattended/lib-unattended.sh`, and prints `69 8 77`. Unit
  57's AC1 is observed against that probe's total. Observed by AC13.
- **S20** — id 33. `tools/unattended/README.md` (`:26-30`) and the reader's header comment
  (`lib-unattended.sh:830-833`) name both `when` forms, the tokens `exists:` resolves (`{prefix}`,
  `{kit}`, `{memory_root}`, `{map_root}`), the shapes S21 and S22 refuse, and that an absent path is a
  silent skip (S31). Observed by AC14.
- **S21** — id 37. lib-unattended skips, with a stderr line naming the descriptor and the `when`, a
  `when` reading `exists:` with an empty path and any `when` matching neither form; neither is kept or
  dropped silently. Observed by AC2.
- **S22** — id 39. An `exists:` path that is absolute (`/…`, `X:…`) or holds a `..` segment is refused
  by selfcheck's `_gwbad` and by `regen.check_when`, and skipped with S21's line by lib-unattended, by
  the pattern `read_gate_policy` uses (`tools/unattended/unattended.sh:9566-9567`). Observed by AC2.
- **S23** — id 40. `root_confs` (`TOOL-dWitnessedBar-52` S1) keeps each listed path once and only when it
  is a regular file in the work tree; a listed path that is absent is printed
  `not in the work tree <path>` and not read. Observed by AC15.
- **S24** — id 42. Every reader of a per-tree record or run record takes a key's value as the line after
  its first TAB: the hook's adoption (`sub(/^[^\t]*\t/, "")` in place of `print $2`,
  `.githooks/pre-push:1354-1368`), `read_local_verdict` (`split('\t', 1)`) and any reader of
  `base_from`. Observed by AC16.
- **S25** — id 43. `refuse-wrong-shell.sh --coverage` reads a call as a class: a `resolve_python` word on
  a line, with no `#` and no `function` before it on that line, and not followed by `\s*\(\s*\)`. It
  replaces unit 57 S1's list of contexts. Observed by AC17.
- **S26** — id 22. The coverage arm carries a caller in each spelling unit 57 S1 missed:
  `elif resolve_python`, `while resolve_python`, `$( resolve_python )`, a backtick call and
  `{ resolve_python; }`. The built tree's count does not move. Observed by AC17.
- **S27** — id 44. A seed home with any path component `.git`, or one that resolves to the gitlink file
  or inside `git rev-parse --git-common-dir`, is unarmed `outside the tree <path>` and nothing is
  written. Observed by AC18.
- **S28** — id 7. The `govkit selfcheck` observation over the `exists:` row has one owner, unit 54's AC2:
  at the close unit 57's AC18 line names unit 54's AC2 line, and no second run is recorded as its own
  evidence. Observed by AC19.
- **S29** — id 9. `ratchet.py`'s `untracked-conf` plant arms `conf-scalar-pins` with one row for another
  key, `OTHER_PIN`, so unit 52's AC3 exercises the unheld-pin path and not unit 57 S9's `empty seed`
  reading. Observed by AC20.
- **S30** — id 34. Unit 52's AC3 plant is run again after unit 57's pass and still exits 1 naming
  `FOO_PIN`. Observed by AC20.
- **S31** — id 10. An absent `exists:` path is a silent skip, as a false conf `when` is
  (`lib-unattended.sh:883-886`). Unit 54's AC1 clause "no line is lost silently" is observed as: no
  stderr line names a reader failure, and a sibling kit's pair is still printed (S33). Observed by AC21.
- **S32** — id 11. Every description of the conf set units 14 and 46 wrote, `ratchet.py`'s docstrings and
  the memory-tree README's adopter-receives table, reads "root confs in the working tree, ignored ones
  excluded". Observed by AC22.
- **S33** — id 19. Unit 54's AC1 negative half runs in a clone where `git rm -r -q tools/govkit` is
  committed, so `git ls-files ':(glob)tools/*/kit.toml'` lists run-gates and not govkit. Observed by AC21.
- **S34** — id 20. Unit 56's AC11 suffixless temp is planted directly: a file `<hash>.Ab3dEf9h` in the
  tails directory aged past `TAIL_GRACE_S`, then the sweep runs. Observed by AC23.
- **S35** — id 21. The seed home test resolves both sides with `os.path.realpath`, folds them with
  `os.path.normcase`, and tests containment with `os.path.commonpath`, never a string prefix.
  Observed by AC18.
- **S36** — id 25. Unit 53's arm extends unit 46's scaffold arm in the hygiene suite rather than building
  a second example-conf scaffold, so the `keys-not-scalar` `ROW_DUPLICATE_PIN` assertion is made once.
  Observed by AC3.
- **S37** — id 26. Unit 55's parity arm, with unit 59's `lone-cr` row, follows `check_conf_reader_parity`
  (`tools/govkit/selftest.py:808`): one fixture table, bash run through `G.resolve_shell_argv` with the
  sentinel row graded first, every row graded; the slice is cut by `awk '/^read_policy_key\(\)/,/^}/'`,
  as `.githooks/pre-push.test.sh:1440` and `tools/push-main.test.sh:849` cut it. Observed by AC24.
- **S38** — id 41. `witness` names a line `not an assignment` only when it matches
  `^\s*(export\s+)?INHERITED_RED\s*=` and is not an S1 assignment of unit 55; a `#`-led line and an
  `INHERITED_RED_MAX_AGE` line are neither, so gov's comment at `.githooks/gate-env.sh:74` is not named
  and `up` leaves it. Observed by AC25.
- **S39** — id 45. The allowed-signers file of unit 56 S15 is created and unlinked in one `try`/`finally`
  that covers every outcome, timeout and signal included. Observed by AC26.

## 3. Non-goals (OUT)

- Any high: units 58 to 61, one per id.
- Re-wording another unit's spec text: each item is closed by what this pass builds or observes, and a
  criterion of an earlier unit that this pass replaces is answered in that unit's ledger by name.
- The spec lints and checklist entries the report names as left-shifts: each is a gate no clause of this
  build names. S3, S7, S11 and S17 are the regression arms this batch builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-54` — S3's parity arm, the `exists:` reader and `_gwbad`, and AC1 and AC2 (ids 1, 7, 10, 14, 19, 33, 37, 38, 39)
- **consumes-from** `TOOL-dWitnessedBar-53` — the seed-across-commit arm (ids 2, 3, 18, 25, 36)
- **consumes-from** `TOOL-dWitnessedBar-61` — the null SHA on rows seeded before the first commit (id 2)
- **consumes-from** `TOOL-dWitnessedBar-46` — the hygiene suite's scaffold arm and the adopter-receives table (ids 5, 11, 25)
- **consumes-from** `TOOL-dWitnessedBar-43` — the four peer plants and the ledger lines of AC1, AC2 and AC4 (id 4)
- **consumes-from** `TOOL-dWitnessedBar-56` — the selection round trip, the floors, the README sentences, the tail sweep, the peer read and AC15 (ids 4, 5, 6, 15, 16, 17, 20, 31, 32, 42, 45)
- **consumes-from** `TOOL-dWitnessedBar-57` — the pass-commit rule, the gate-health population, the coverage predicate and figure, the seed-home containment, `empty seed` and AC18 (ids 7, 21, 22, 23, 24, 29, 30, 34, 43, 44)
- **consumes-from** `TOOL-dWitnessedBar-51` — S1, AC8, AC17 and the `PARITY_ROWS` precedent of S21 (ids 5, 23, 24, 29)
- **consumes-from** `TOOL-dWitnessedBar-1` — `--gate-health`, its write path and AC1 to AC4 (id 29)
- **consumes-from** `TOOL-dWitnessedBar-52` — `root_confs` and AC3's plant (ids 9, 11, 34, 40)
- **consumes-from** `TOOL-dWitnessedBar-14` — the `ratchet.py` docstrings that describe the conf set (id 11)
- **consumes-from** `TOOL-dWitnessedBar-55` — the parity arm and `witness` (ids 26, 41)
- **consumes-from** `TOOL-dWitnessedBar-59` — the `lone-cr` parity row, carried with the other eight (id 26)
- **hands-off** external — dTendedCadence's scheduled `--gate-health --write`, which passes `--selection` as S18 states
- **hands-off** `TOOL-dWitnessedBar-63` — the `exists:` containment on backslash forms, the cross-drive seed home, the no-TAB record line and the runner's reader, the bytes capture, the signer sweep, the generator-less row, and AC7, AC13, AC17, AC18 and AC22 re-graded (ids 4, 6, 7, 8, 10, 11, 12, 17, 19, 20, 21, 22, 25, 27, 28, 29, 30, 35)

## 4. Design

### Why one unit

M6 admits two units only when both write sets, contracts and shared records are disjoint. Here they are
not. Id 5's floors write `check-memory-hygiene.test.sh` beside the run-gates suites, and the hygiene
suite is where ids 2, 3, 18, 25 and 36 change unit 53's arm. That arm runs `legacy_ledger.py seed` and
`ratchet.py keys-not-scalar`, which ids 9, 21, 40 and 44 change, so each half would read the other's
output as an acceptance input (clause 2). One unit holds them, building after every other unit.

### Evidence

- `regen.build_items` skips a row lacking all of `write`, `check` and `stage` before it reads `when`,
  and `check_when` raises `Refusal` with no per-row catch (`regen.py:140-146`, `:178-187`).
- lib-unattended keeps any row with a path and a generator, reads the conf form only, and `continue`s
  silently on a false condition (`lib-unattended.sh:882-886`); it prints a skip line for an unresolved
  path token (`:890-891`).
- `read_gate_policy` refuses `/*|[A-Za-z]:*|..|../*|*/..|*/../*` (`unattended.sh:9566-9567`).
- The record readers split with `IFS=$'\t' read` (`run-gates.sh:2392`, `.githooks/pre-push:1425`), and
  the hook's per-record reads are `awk -F'\t' '$1=="<key>"{print $2}'` (`.githooks/pre-push:1354-1358`).
- `build_commit` matches attribution tokens from the `Pass:` trailer, else the subject, and excludes the
  build folder (`lib-unattended.sh:1145-1192`).
- `derive_temp_path` takes `mktemp -u` only when `${SRANDOM:-}` is empty (`run-gates.sh:782`).
- The floors are `-ge` checks on executed assertions (`check-memory-hygiene.test.sh:4370-4371`).
- `check_conf_reader_parity` runs bash through `G.resolve_shell_argv` with a sentinel first
  (`tools/govkit/selftest.py:808-838`).
- gov's policy file holds a commented doc line `#   INHERITED_RED=park|land` (`.githooks/gate-env.sh:74`)
  and an `INHERITED_RED_MAX_AGE=10` assignment (`:104`).

### The coverage probe (S19, S25)

Measured 2026-10-25 at `8229ea5f`, whose `tools/`, `skills/` and `.githooks/` equal `cdfbd1cf`'s
(`git diff --stat cdfbd1cf HEAD -- tools skills .githooks` prints nothing). PINNED: 69 block carriers, 8
callers, 77. Unit 57's enumerated predicate and S25's class predicate both print it.

```
git ls-files -- tools skills .githooks | python -c "
import re, sys
CLS = re.compile(r'\bresolve_python\b(?!\s*\(\s*\))')
ex = {'tools/lib/resolve-python.sh', 'tools/unattended/lib-unattended.sh'}
blk = cal = 0
for f in sys.stdin.read().split():
    if f in ex: continue
    t = open(f, encoding='utf-8', errors='replace').read()
    if not (f.endswith('.sh') or re.match(r'#!.*\b(ba)?sh\b', t.split('\n', 1)[0])): continue
    if re.search(r'(?m)^# >>> resolve_python', t): blk += 1; continue
    def call(l):
        m = CLS.search(l)
        return bool(m) and '#' not in l[:m.start()] and not re.search(r'\bfunction\s*$', l[:m.start()])
    if any(call(l) for l in t.split('\n')): cal += 1
print(blk, cal, blk + cal)"                                   # prints: 69 8 77
```

### Inventory

Minted: the arm line `not compared`; the reading `not in the work tree`; the marker stem
`selection_row` and its `PARITY_ROWS` row; the plants `deleted-conf` and `selection-with-note`; the
fixture registration of S6. Naming cells: each is asked of
`python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

None: no item changes stored data. S24 reads records written under unit 56 S1 unchanged.

### Rollout

Live at landing, after every other unit of the build. S8, S18, S28 and S30 are observed by the main loop
at the close, on the tree they grade.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `tools/govkit/govkit.py`
- `tools/govkit/steps/inherited_red.py`
- `tools/run-gates/regen.py`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/README.md`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/ratchet.py`
- `tools/memory-tree/README.md`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/adopt-run-gates.test.sh`
- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/README.md`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/drift-audit/drift_report.py`
- `tools/lib/refuse-wrong-shell.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`

### Alternatives rejected

- **Two batches split at the verdict boundary, as round 2 split.** The hygiene suite and the seed and
  ratchet modules join the halves (§4 "Why one unit").
- **Refuse an empty note at the runner (id 6's first option).** It stops a quarantine row holding its
  leg; S24's one reader rule, which id 42 needs anyway, keeps the field instead.
- **Keep unit 57's `git log | awk` pass-commit rule (id 23).** A second answer to the question
  `build_commit` already answers, and the two part on trailer-less and multi-id commits.
- **Drop the `exists:` containment from lib-unattended and refuse only in selfcheck (id 39).** An adopter
  whose selfcheck has not run would still read a path outside the tree.

## 5. Production-readiness checklist

- security — S22 and S27 contain an `exists:` path and a seed home to the work tree outside `.git`; S35
  makes the containment test correct on Windows paths; S39 leaves no signer file behind.
- perf / scale — one more parity row, two more plants, a few greps.
- error / empty / loading states — S1, S21 and S23 turn an uncompared, malformed or absent input into a
  named line, never a silent pass; S5 refuses an empty union.
- observability — each new line names its subject.
- risks — S9 to S11 raise floors to what runs, so a later deleted arm reds, which is their purpose.
- testing — AC1 to AC26 by plant, fixture and probe; the arms under §7 at the close.
- migration — none.
- user docs — S14, S15, S20 and S32 edit kit READMEs; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When the S2 tree is read through `regen.build_items` and through
  `resolve_generated_indexes`, both keep the conf-true and present-path rows only, and a row in it
  lacking `write`, `check` and `stage` is printed `not compared`.
  Red when: the two readers keep different rows, or an uncompared row passes unnamed.
  fixture: scratch trees under `%TEMP%/<short-name>`, built by the arm.
- **AC2** — When each S3 tree is read, `build_items` raises `Refusal` naming the row, lib-unattended's
  stderr names the descriptor and the `when` and its output keeps the conf-true row, and
  `govkit.py selfcheck` refuses; for the empty-path, no-colon, absolute and `..` trees alike. With
  lib-unattended's empty-path and containment tests removed, the arm reds.
  Red when: a refused form is kept, or dropped with no line.
- **AC3** — When unit 53's arm runs, it is one block with unit 46's scaffold arm
  (`grep -c 'memory-tree.conf.example' check-memory-hygiene.test.sh` does not rise), it lists every
  population the first `seed --all` printed `present` or `armed` for, the saved rows carry forty `0`
  characters in the SHA column and the re-seed's rows carry HEAD, and the key and count columns agree.
  Red when: a population the listing run armed is left out, or the arm builds a second scaffold.
- **AC4** — When the arm's fixture registration is present, it is compared after the commit; with its
  seed staged to read `git ls-files` only, the arm reds naming it.
  Red when: a tracked-only seed the listing run armed passes the arm.
- **AC5** — When `grep -rn 'run-gates gov canary' memory/builds/dWitnessedBar/build/` runs at the close,
  it names unit 43's AC1, AC2 and AC4 lines under `**Evidences:** TOOL-dWitnessedBar-43`, and unit 56's
  AC15 line names the same observation.
  Red when: unit 43 closes with its peer plants never run by a named leg.
- **AC6** — When `grep -n 'RAISED .* by TOOL-dWitnessedBar-' <suite>` runs over each of S9's four suites,
  every listed unit whose arm lands there is named on its own line, unit 56 on its own, and
  `grep -n '^FLOOR_ASSERTIONS=' <suite>` is at least the executed count the close observes.
  Red when: a unit's arms are counted by no `RAISED` line, or a floor sits below what runs.
- **AC7** — When one arm of a listed unit is deleted from each suite in a scratch copy, that suite prints
  its `FAIL executed` floor line.
  Red when: an arm can be deleted and its suite stays green.
- **AC8** — When the runner makes a full run with `GATE_SELECTION` naming a file whose `quarantine` row
  has an empty note, `.githooks/pre-push` adopts the record where R derives the row.
  Red when: the hook's rebuild drops the trailing TAB and refuses a genuine GREEN.
  fixture: a scratch clone under `%TEMP%/<short-name>`; the tree holds none.
- **AC9** — When `for t in selection_ignored TAIL_GRACE_S GATE_POLICY_FILE; do grep -q "$t" README.md || echo MISSING $t; done`
  runs in `tools/run-gates/`, it prints nothing, and `grep -c 'no gate-verdict written' README.md` prints
  at least 2.
  Red when: a promised sentence is missing while another term's lines stand in for it.
- **AC10** — When `build_commit cdfbd1cf..HEAD TOOL-dWitnessedBar-24 memory/builds/dWitnessedBar "$GENERATED_INDEXES" "$SHARED_RECORDS"`
  runs with `lib-unattended.sh` sourced at the close, it prints one SHA that is not `ad002a024`, and the
  shell-role derivation of unit 51 S1 starts from that SHA.
  Red when: a second pass-commit rule answers for a unit.
- **AC11** — When `grep -n '^selection_row|' tools/lib/resolve-python.test.sh` runs, it names the row,
  and the `# >>> selection_row` blocks of `verdict_flow.py` and `drift_report.py`, cut by
  `awk '/^# >>> selection_row/,/^# <<< selection_row/'`, are byte-identical; with one byte of the copy
  edited in a scratch tree, the two cuts differ.
  Red when: drift-audit's selection reader can drift from the runner's.
- **AC12** — When `python drift_report.py --gate-health --fixture differs --selection <empty>` runs in
  `tools/drift-audit/`, it exits 0; and `grep -rn -- '--gate-health' memory/builds/dWitnessedBar/build/`
  at the close shows every ledger line for unit 1's AC1 to AC4 and unit 51's AC17 carrying `--selection`.
  Red when: a caller is recorded running `--gate-health` without the flag.
- **AC13** — When the §4 coverage probe runs, it prints `69 8 77`, and `bash refuse-wrong-shell.sh
  --coverage` in `tools/lib/` prints a population of 77.
  Red when: the figure and the tool's count part.
  figure: 77 is PINNED at `8229ea5f`, measured 2026-10-25.
- **AC14** — When `grep -n 'exists:' tools/unattended/README.md tools/unattended/lib-unattended.sh` runs,
  it names the README's `when` paragraph and the reader's header comment.
  Red when: the kit README still says `exists:` is refused.
- **AC15** — When `python ratchet.py --fixture --plant deleted-conf` runs in `tools/memory-tree/`, a
  staged root conf removed from the work tree is printed `not in the work tree` and `keys-not-scalar`
  exits without a traceback.
  Red when: the leg opens a listed conf that is absent.
- **AC16** — When `python verdict_backends.py --fixture --plant selection-with-note` runs in
  `tools/run-gates/`, `read --backend local-hook` prints `GREEN`, and the hook adopts the same record.
  Red when: a reader takes the second TAB field alone and refuses the record.
- **AC17** — When the coverage arm's fixture holds one file per S26 spelling, `--coverage` lists each as
  a member, and the built tree's count stays 77.
  Red when: a call spelled after `elif`, in a group or in a backtick is missed.
- **AC18** — When `python legacy_ledger.py seed --home .git -- <argv>` runs inside a `git worktree add`
  fixture, and with `--home` naming the git dir of a nested repository beside it, each prints `outside the tree` and the
  gitlink is byte-identical; a relative in-tree home and an absolute in-tree home each print `armed`.
  Red when: a seed overwrites a gitlink, or a string-prefix compare refuses an in-tree home.
  fixture: a linked worktree under `%TEMP%/<short-name>`, built by the arm.
- **AC19** — When `grep -rn 'TOOL-dWitnessedBar-54' memory/builds/dWitnessedBar/build/` runs at the
  close, unit 57's AC18 line names unit 54's AC2 line and `govkit.py selfcheck`.
  Red when: one observation is recorded twice as two units' own evidence.
- **AC20** — When `python ratchet.py --fixture --plant untracked-conf` runs after unit 57's pass, its
  `conf-scalar-pins` holds the `OTHER_PIN` row and `keys-not-scalar` exits 1 naming `FOO_PIN`.
  Red when: the plant reads `empty seed` and stops naming the unheld pin.
- **AC21** — When unit 54's AC1 shell call runs in the S33 clone, the leg factory's pair is absent, the
  pair of `memory/LIVE.md` and `tools/memory-tree/gen_build_index.py`, joined by a colon, is printed,
  and stderr carries no line.
  Red when: the read saw nothing, so the absence proves nothing.
  fixture: a clone under `%TEMP%/<short-name>`; the tree holds none.
- **AC22** — When `grep -rn 'tracked root conf' tools/memory-tree/` runs on the built tree, it prints
  nothing.
  Red when: a README or docstring still describes the tracked set.
- **AC23** — When a file `<hash>.Ab3dEf9h` aged past `TAIL_GRACE_S` sits in the tails directory and the
  sweep runs, the file is unlinked; a fresh one survives.
  Red when: a suffixless temp is kept as a tail.
- **AC24** — When the govkit selftest's policy parity arm runs, its sentinel row is graded first, it
  grades all nine rows, and `grep -c "awk '/^read_policy_key" tools/govkit/selftest.py` prints 1.
  Red when: the arm compares the step with a bash that read nothing.
- **AC25** — When `python inherited_red.py witness <target>` runs over a fixture holding the comment line
  `#   INHERITED_RED=park|land` and `INHERITED_RED_MAX_AGE=10`, neither is named; an
  `export INHERITED_RED=park` line is.
  Red when: `witness` prints noise on gov's own file.
- **AC26** — When `--plant peer-no-ssh-keygen` runs, `ls <git-dir>` afterwards shows no signer temp.
  Red when: a failed peer read leaves its allowed-signers file behind.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `routed-commits selftest` · `memory-hygiene self-test` · `memory hygiene` · `kit/dogfood doc parity` · `run-gates canary` · `run-gates evidence` · `run-gates gov canary` · `run-gates adopter e2e` · `pre-push self-test` · `pre-push bar self-test` · `measure-legs selftest` · `drift-audit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest`

The unattended kit's own suites are waived for this build's landing (README rule), so S1 to S3, S21 and
S22 are observed by the govkit selftest arm, not by that kit's suites.

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC24 AC25 · the split `when` trees, the policy parity on the conf-parity pattern and the `witness` fixture, staged red by restoring lib-unattended's unchecked `exists:` test · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 AC4 · the extended scaffold arm over the present-or-armed union and a tracked-only fixture registration, staged red by listing `present` lines only · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC8 AC23 · the empty-note selection and the planted suffixless temp, staged red by reading `selection.<n>` with `IFS=$'\t'` · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/verdict_backends.py · covers AC16 AC26 · the `selection-with-note` plant and the signer temp after a failed read, staged red by unpacking two fields · none
New arm: tools/memory-tree/ratchet.py · covers AC15 AC20 · the `deleted-conf` plant and the armed `untracked-conf` plant, staged red by dropping the regular-file test · none
New arm: tools/lib/resolve-python.test.sh · covers AC11 AC17 · the `selection_row` parity row and the five coverage spellings, staged red by editing the inline copy · none
New arm: tools/lib/legacy_ledger.py · covers AC18 · the `.git` homes and the relative in-tree home, staged red by a string-prefix compare · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of each repaired unit's clause. Most repaired units are
  themselves derived and carry none, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which empty-note fix does id 6 take?** Options: (a) the runner ignores a row with an empty note;
  (b) the readers take a value as the line after its first TAB; (c) a sentinel for an empty note in the
  value. (a) makes a quarantine row stop holding its leg; (c) adds a spelling both the canonical text and
  `select --check` must learn. (b) is id 42's rule, so one change closes both. RESOLVED (agent,
  2026-10-25, delegated): (b), rung 3, the most criteria met with the fewest new spellings.
  widens: none · relaxes: none
- **F3 — Who owns the selfcheck observation id 7 names twice?** Options: (a) unit 54's AC2, with unit
  57's AC18 answered by it in the ledger; (b) unit 57's AC18, with unit 54's AC2 narrowed. (b) needs a
  re-worded criterion in a unit that lands first, which this batch does not write (§3).
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the owner that lands first.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 52 to 57: 25 MEDIUM
  and 14 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names: unit 54's parity arm for S1 to S3, unit 46's scaffold arm
for S5 and S36, `build_commit` (`tools/unattended/lib-unattended.sh:1186`) for S16, the `PARITY_ROWS`
table (`tools/lib/resolve-python.test.sh:168`) for S17, `read_gate_policy`'s containment pattern
(`tools/unattended/unattended.sh:9566-9567`) for S22, `check_conf_reader_parity`
(`tools/govkit/selftest.py:808`) and the two existing `read_policy_key` slices for S37.
`python tools/codebase-map/reuse_lookup.py "find the pass commit of a unit by its trailer"` ranked
`units`, `build_commit`, `baseline_units` and `build_unit_id_re`; `build_commit` is the seam S16 extends,
so the per-item seams above are the record.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 52 to 57 find" --terms "exists when regen build_items lib-unattended scaffold seed armed present floor RAISED selection note build_commit coverage"`
