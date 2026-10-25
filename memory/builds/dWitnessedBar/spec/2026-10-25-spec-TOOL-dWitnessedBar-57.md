# TOOL-dWitnessedBar-57 — the round-1 audit of units 40 to 51, resolver, ledger and adopter minors batched: one stated wrong-shell predicate, contained seed homes, readers that see what the runner holds, and observations that can red

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 32 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 |
| [2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 to 51
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`)
exited CONVERGED with 48 confirmed findings; its 4 highs are units 52 to 55. BUILD-METHOD M4 batches
every MEDIUM and LOW, and they split into two disjoint write sets by M6's clauses
(`TOOL-dWitnessedBar-56` §4 states the three). This unit holds the 24 of the resolver, the ledger, the
adopters, the step script, the run log and the build's close-time derivations; unit 56 holds the
verdict boundary's 20. Each finding is named by report id and is its own scope item, where the report
merged ids into one item too. The minors land on several units, so this unit repairs none in particular
and builds after every unit (order 32), concurrent with unit 56.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M6, L7 | MEDIUM, LOW | 5; 19, 51 | S1; S2, S3 |
| L1 | LOW | 6 | S4 |
| M7 | MEDIUM | 17 | S5 |
| M15 | MEDIUM | 36 | S6 |
| L13 | LOW | 29 | S7 |
| L3 | LOW | 9 | S8 |
| M1 | MEDIUM | 44 | S9 |
| L11 | LOW | 25 | S10 |
| M18 | MEDIUM | 45 | S11 |
| L2 | LOW | 7, 21 | S12, S13 |
| M8 | MEDIUM | 18 | S14 |
| M11 | MEDIUM | 31 | S15 |
| M17 | MEDIUM | 39 | S16 |
| M19 | MEDIUM | 46 | S17 |
| M9 | MEDIUM | 26 | S18 |
| M13 | MEDIUM | 34 | S19 |
| M10 | MEDIUM | 30 | S20 |
| L4 | LOW | 10 | S21 |
| L6 | LOW | 12 | S22 |
| L9 | LOW | 22 | S23 |
| L14 | LOW | 38 | S24 |

That is 12 MEDIUM and 12 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 5. `refuse-wrong-shell.sh --coverage` (`TOOL-dWitnessedBar-50` S1, S4) reads a call as
  `$(resolve_python` anywhere, or `resolve_python` as the first word of a command after optional
  whitespace, a `;`, `&`, `|`, `!`, `if`, `then`, `do` or `else`, not followed by `()`; a
  `resolve_python()` definition is not a call. A member "sources `refuse-wrong-shell.sh`" when a line
  matches `^\s*(\.|source)\s+\S*refuse-wrong-shell\.sh`. Observed by AC1.
- **S2** — id 19. The population figure is re-pinned by the §4 probe, stated verbatim: 69 block carriers
  and 9 callers, 78, at `cdfbd1cf`; the whitespace-tolerant reading that keeps definitions would give 10.
  Observed by AC1.
- **S3** — id 51. `tools/push-main.test.sh:915`, the indented stub `resolve_python() { echo bash; }`, is a
  non-member, and the coverage arm carries it as a fixture case. Observed by AC2.
- **S4** — id 6. `tools/lib/resolve-python.sh` is not a member: it is only ever sourced. `--coverage` names
  it beside unit 50's named exclusion as `TOOL-dWitnessedBar-27`'s listed member the predicate excludes,
  with that reason, and the file carries no `refuse_wrong_shell || exit 2` line; if unit 27's pass added one,
  this pass takes that line out. Observed by AC3.
- **S5** — id 17. `regen.run_command` (`tools/run-gates/regen.py:279`) raises `Refusal` naming the
  resolver's refusal when `run[0] == "bash"` and no bash resolved, and never looks `bash` up on `PATH`;
  `scan_bare_bash` shape 4 (`TOOL-dWitnessedBar-49` S1) also matches a `shutil.which(<expr>)` whose
  argument is not a constant inside an expression comparing that argument to `"bash"`.
  Observed by AC4.
- **S6** — id 36. The row-grammar adapter (`TOOL-dWitnessedBar-48` S1) appends the block's `found` to
  `shell_used` before it returns the ERE (`tools/memory-tree/row_grammar.py:2005`, read at `:2047`), and
  returns `None` on the block's refusal; this unit's §7 names `row-grammar selftest`. Observed by AC5.
- **S7** — id 29. The `resolve_bash_py` block is carried once in `tools/memory-tree/tree_lib.py`, under its
  parity row, and `row_grammar.resolve_shell_ere` and `corpus_ids.py`'s adapter import it, as
  `row_grammar.py` already imports its shared helpers from `tree_lib` (`:81-84`). Observed by AC6.
- **S8** — id 9. Shape 2's count at the base is stated by the §4 probe, which reads blobs at `cdfbd1cf`
  and prints 8, `tools/govkit/govkit.py:1210`'s membership test among them; `TOOL-dWitnessedBar-51`'s
  AC15 second clause is answered by that command. Observed by AC7.
- **S9** — id 44. `keys-not-scalar` over an armed `conf-scalar-pins` holding zero rows, while a root conf
  assigns a scalar pin, exits 1 printing `empty seed conf-scalar-pins` and the re-seed remedy, removing
  the home and running `legacy_ledger.py seed --population conf-scalar-pins`, in place of an unheld-pin
  line that points at a widen record. Observed by AC8.
- **S10** — id 25. `keys-not-scalar`'s unarmed test calls the function behind `ratchet.py unarmed`
  (`TOOL-dWitnessedBar-14` S7), scoped to `conf-scalar-pins`, and carries no reader of the unarmed line
  of its own. Observed by AC9.
- **S11** — id 45. A seed home (`TOOL-dWitnessedBar-47` S1) is admitted only when, resolved with symlinks
  followed, it lies under `git rev-parse --show-toplevel`, outside the git dir, and `git check-ignore`
  does not match it; otherwise it is unarmed `outside the tree <path>` or `ignored <path>` and nothing is
  written. An absolute path resolving inside the work tree is admitted. Observed by AC10.
- **S12** — id 7. Unit 47's arm in `tools/codebase-map/adopt-codebase-map.test.sh` takes the exempt
  file's basename from the seed-if-absent guard of `adopt-codebase-map.sh` (`:198` today), so it follows
  `TOOL-dWitnessedBar-16` S6's rename, and fails when no name is found. Observed by AC11.
- **S13** — id 21. After units 16 and 51, no line of `adopt-codebase-map.test.sh` spells the exempt file's
  pre-rename `.toml` basename, whose readers unit 16 S6 answers for. Observed by AC11.
- **S14** — id 18. `inherited_red.py up` edits each file as bytes, removes only the lines
  `TOOL-dWitnessedBar-55` S3 deletes, and keeps every other byte, line ends included. Observed by AC12.
- **S15** — id 31. `tools/runlog/record.py` gains `EXCLUDED_KINDS_BEFORE_FIX_OF`, the excluded set less
  `fix-of`; `EXCLUDED_KINDS_BEFORE_HOLD` leaves `fix-of` out as well; the `excluded rows` fact admits the
  three templates (`record.py:115-119`, `:284-285`). Observed by AC13.
- **S16** — id 39. At the close, the shell-role derivation of `TOOL-dWitnessedBar-51` S1 runs on the
  `push-main.sh --prepare` merge: `grown` is measured there, a member grown by a unit's pass takes its
  row as S1 says, and a member grown only by commits reached through the merge's default-branch parent
  takes one reconcile widen record whose `Caused-by:` is the merge. Observed by AC14.
- **S17** — id 46. A unit's pass commit, for S16 and for unit 51's S1 and AC8, is the oldest commit in
  `cdfbd1cf..HEAD` whose `Pass` trailer equals the unit id and whose subject begins
  `tool(dWitnessedBar): <id> `; none found refuses naming the id. Observed by AC15.
- **S18** — id 26. `measure_gate_health`'s bar legs (`TOOL-dWitnessedBar-51` S21) are the manifest's legs
  less the `kit` holds of the inline `test_held` and less the `quarantine` and `level` rows of the
  selection file named by `--selection <path>`; `verdict_flow.py flakes` passes the file
  `select --rev <R> --out` writes. With no `--selection`, `--gate-health` exits 2 naming the flag.
  Observed by AC16.
- **S19** — id 34. `tools/check-spec-tokens.py` gains the canonical sides of unit 51's two parity rows,
  `# >>> acceptance_reader` holding `TICK`, `AC_HEAD` and `extract_acceptance` as one contiguous block
  and `# >>> arm_walk` holding `scan_arm_covers`' walk; this unit's §7 names `spec-tokens self-test`; and
  unit 51's pass commit touches no path outside its Files touched and the three it omits,
  `tools/memory-tree/merge-rows.py`, `tools/memory-tree/merge-rows.test.sh` and
  `tools/run-gates/keep_tails.py`. Observed by AC17.
- **S20** — id 30. `govkit.py selfcheck` reports no `[[generated]]` failure on the built tree with the
  factory row's `exists:` `when`, and fails on a scratch copy whose `when` reads `exists:` with no path,
  the leg unit 45's §7 never names. Observed by AC18.
- **S21** — id 10. `TOOL-dWitnessedBar-51`'s AC36 is answered by its carriers: every commit in
  `cdfbd1cf..HEAD` editing `memory/HYGIENE.md` or `memory/guides/BUILD-METHOD.md` carries a `Decided:`
  trailer citing `grants: PLAY-dClosedLoop-3`. Observed by AC19.
- **S22** — id 12. The order-2 passes of units 27, 48 and 49, which all write
  `tools/lib/resolve-python.test.sh`, land in sequence: no merge commit in the build range touches it.
  Observed by AC20.
- **S23** — id 22. Unit 51's S13 is observed on gov's own conf: `.memory-tree.conf` names none of the
  five homes. Observed by AC21.
- **S24** — id 38. Unit 51's AC35 prints, per pack `portability` and `product-tests`, its row count and
  names, and reds when either count is 0 as well as on any mismatch. Observed by AC22.

## 3. Non-goals (OUT)

- Any high: units 52 to 55, one per id.
- The verdict-boundary minors: `TOOL-dWitnessedBar-56`.
- The spec lints and checklist entries the report names as left-shifts: each is a gate no clause of this
  build names.
- Re-wording another unit's spec text: each item is closed by what this pass builds or observes.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-50` — the derived population and `--coverage` (ids 5, 6, 19, 51)
- **consumes-from** `TOOL-dWitnessedBar-27` — `refuse-wrong-shell.sh` and its listed population (ids 6, 12)
- **consumes-from** `TOOL-dWitnessedBar-49` — shape 4 of `scan_bare_bash` (id 17)
- **consumes-from** `TOOL-dWitnessedBar-26` — the `resolve_bash_py` block and its parity row (ids 17, 29)
- **consumes-from** `TOOL-dWitnessedBar-48` — the row-grammar adapter and its inline copy (ids 12, 29, 36)
- **consumes-from** `TOOL-dWitnessedBar-46` — `keys-not-scalar` over the seeded population (id 44)
- **consumes-from** `TOOL-dWitnessedBar-14` — the `unarmed` verb (id 25)
- **consumes-from** `TOOL-dWitnessedBar-47` — the directory admission rule and its adopter arm (ids 7, 45)
- **consumes-from** `TOOL-dWitnessedBar-16` — the exempt file's rename (ids 7, 21)
- **consumes-from** `TOOL-dWitnessedBar-44` — the step script `inherited_red.py` (id 18)
- **consumes-from** `TOOL-dWitnessedBar-55` — the lines `up` deletes (id 18)
- **consumes-from** `TOOL-dWitnessedBar-51` — S1, S13, S21, S23, AC8, AC15, AC35, AC36 and its two parity rows (ids 9, 10, 22, 26, 31, 34, 38, 39, 46)
- **consumes-from** `TOOL-dWitnessedBar-45` — the factory row's `exists:` `when` (id 30)
- **consumes-from** `TOOL-dWitnessedBar-54` — the widened `_gwbad` (id 30)
- **consumes-from** `TOOL-dWitnessedBar-7` — its HYGIENE and BUILD-METHOD carrier edits (id 10)
- **consumes-from** `TOOL-dWitnessedBar-24` — the `portability` legs and the five homes (ids 22, 38)
- **consumes-from** `TOOL-dWitnessedBar-9` — the `product-tests` legs (id 38)
- **hands-off** `TOOL-dWitnessedBar-62` — the pass-commit rule, the gate-health population, the coverage predicate and figure, the seed-home containment, `empty seed` and AC18, which the minors batch builds on `build_commit`, holds to parity, widens to a class and contains (ids 7, 21, 22, 23, 24, 29, 30, 34, 43, 44)
- **hands-off** `TOOL-dWitnessedBar-63` — AC12's byte preservation in `up`, by which the minors batch answers unit 59's AC2 byte half (id 3)

## 4. Design

### Evidence

- `resolve_python` callers: `check-line-length.sh:86` and `adopt-playbook.sh:48` call `$(resolve_python`
  and define it at `:57` and `:18`; `tools/push-main.test.sh:915` holds only the indented stub.
- `regen.py:279`: `run[0] = (BASH if run[0] == "bash" else "") or shutil.which(run[0]) or run[0]`, and
  `resolve_bash` returns `''` when the resolver cannot load or no candidate answers (`:232-245`); the only
  other non-constant `shutil.which` call is `branch_reconcile.py:996`'s `RM_NAME`.
- `held_halves.test_held` returns `subject == "kit" or chunk == "selftests"` (`held_halves.py:75-77`).
- `EXCLUDED_KINDS` and `EXCLUDED_KINDS_BEFORE_HOLD` feed the two `excluded rows` templates
  (`tools/runlog/record.py:115-119`, `:284-285`).
- `ad002a024`, the build's spec commit, names every unit id in its subject and carries `Pass: none`, so a
  subject search resolves to it and S17's rule does not.

### The two pinned probes (S2, S8)

Measured 2026-10-25 at `00cd80dd`, whose `tools/`, `skills/` and `.githooks/` equal `cdfbd1cf`'s:

```
git ls-files -- tools skills .githooks | python -c "
import re, sys
CALL = re.compile(r'\\\$\(resolve_python\b|(^|[;&|]|\b(if|then|do|else)\b|!)\s*resolve_python\b(?!\s*\(\s*\))')
blk = cal = 0
for f in sys.stdin.read().split():
    if f == 'tools/lib/resolve-python.sh': continue
    t = open(f, encoding='utf-8', errors='replace').read()
    if not (f.endswith('.sh') or re.match(r'#!.*\b(ba)?sh\b', t.split('\n', 1)[0])): continue
    if re.search(r'(?m)^# >>> resolve_python', t): blk += 1; continue
    if any(CALL.search(l) for l in t.split('\n')): cal += 1
print(blk, cal, blk + cal)"                                   # prints: 69 9 78

git ls-tree -r --name-only cdfbd1cf | grep '\.py$' | python -c "
import ast, subprocess, sys
n = 0
for f in sys.stdin.read().split():
    src = subprocess.run(['git', 'show', 'cdfbd1cf:' + f], capture_output=True, text=True, encoding='utf-8').stdout
    try: t = ast.parse(src)
    except SyntaxError: continue
    for x in ast.walk(t):
        if isinstance(x, (ast.List, ast.Tuple)):
            v = [e.value for e in x.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
            if 'bash' in v and 'bash.exe' in v: n += 1
print(n)"                                                     # prints: 8
```

### The pass-commit rule (S17)

```
git log --reverse --format='%H%x09%s%x09%(trailers:key=Pass,valueonly,separator=%x2C)' cdfbd1cf..HEAD \
  | awk -F'\t' -v id=<unit id> '$3 == id && index($2, "tool(dWitnessedBar): " id " ") == 1 { print $1; exit }'
```

### Inventory

Minted: `EXCLUDED_KINDS_BEFORE_FIX_OF`; the readings `empty seed`, `outside the tree` and `ignored`; the
flag `--selection` of `drift_report.py --gate-health`; the marker stems `acceptance_reader` and
`arm_walk` in `tools/check-spec-tokens.py`. Naming cells: each is asked of
`python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

S15 keeps every committed runlog record valid under its own template. S16 writes at most one reconcile
widen record per close. No other item changes stored data.

### Rollout

Live at landing, after every other unit of the build, concurrent with `TOOL-dWitnessedBar-56`. S16 and
S21 to S24 are observed by the main loop at the close, on the tree they grade.

### Files touched (estimate)

- `tools/lib/refuse-wrong-shell.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/lib/resolve-python.sh`
- `tools/run-gates/regen.py`
- `tools/run-gates/measure_legs.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/ratchet.py`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/codebase-map/adopt-codebase-map.test.sh`
- `tools/govkit/steps/inherited_red.py`
- `tools/govkit/selftest.py`
- `tools/runlog/record.py`
- `tools/drift-audit/drift_report.py`
- `tools/check-spec-tokens.py`
- `memory/project/shell-role.txt`
- `memory/builds/dWitnessedBar/build/<date>-build-TOOL-dWitnessedBar-57-widen-<n>.md`

### Alternatives rejected

- **Column-0 calls only (id 5's first reading).** It misses a future indented call; the definition
  exclusion keeps the stub out with the wider reading, and both give 9 today.
- **Skip regen's fallback without widening shape 4 (id 17's second option alone).** The next variable
  lookup of `bash` would pass the scan.
- **Run `verdict_flow.py select` from drift-audit (id 26).** drift-audit imports no run-gates module and
  forks none today; it reads the file its caller derives.

## 5. Production-readiness checklist

- security — S11 confines seed writes to the work tree outside `.git` and ignored paths; S5 removes a
  path to WSL's launcher.
- perf / scale — one `check-ignore` per seed home; the rest are reads.
- error / empty / loading states — S9, S11 and S18 turn an empty, outside or missing input into a named
  reading, never a silent pass.
- observability — each refusal names its subject.
- risks — S16 writes a widen record at the close, outside any dispatched pass, recorded in its commit.
- testing — AC1 to AC22 by plant, fixture and probe; the arms under §7 at the close.
- migration — §4.
- user docs — the docstrings S4, S11 and S18 change; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When `bash refuse-wrong-shell.sh --coverage` runs in `tools/lib/` on the built tree, it prints a
  population whose count the §4 probe re-derives, and in a scratch clone where a member indents its
  `resolve_python` call under `if`, it still names that member.
  Red when: an indented call is missed, or a definition is counted as a call.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
- **AC2** — When the coverage arm's fixture case holding `  resolve_python() { echo bash; }` alone runs,
  `--coverage` does not list that file.
  Red when: a test stub becomes a member and `--coverage` exits 1 on it.
- **AC3** — When `bash refuse-wrong-shell.sh --coverage` runs, it names `tools/lib/resolve-python.sh` as
  dropped with its reason, and `grep -c 'refuse_wrong_shell || exit 2' tools/lib/resolve-python.sh`
  prints 0.
  Red when: the sourced canonical carries an exit its sourcer would run.
- **AC4** — When `python measure_legs.py --selftest` runs in `tools/run-gates/` with a fixture holding
  `x = (B if a == "bash" else "") or shutil.which(a)`, the bare-bash arm names that line; and
  `regen.run_command` over a `bash` argv with the resolver stubbed to refuse raises `Refusal`.
  Red when: a variable PATH lookup of `bash` passes, or regen launches a PATH bash.
- **AC5** — When `python tools/memory-tree/row_grammar.py --selftest` runs on a node with Git bash, the
  readers-agree arm passes; with the adapter's append removed, it fails rather than raising `IndexError`.
  Red when: `shell_used` stays empty and `shell_used[0]` raises.
- **AC6** — When `grep -c '^# >>> resolve_bash_py' tools/memory-tree/tree_lib.py tools/memory-tree/row_grammar.py tools/memory-tree/corpus_ids.py`
  runs, it prints 1, 0 and 0, and both modules import the block's function from `tree_lib`.
  Red when: the kit carries two inline copies.
- **AC7** — When the §4 shape-2 probe runs, it prints 8.
  Red when: the pinned figure has no command that re-derives it.
  figure: 8 is PINNED at `cdfbd1cf`, measured 2026-10-25.
- **AC8** — When `python ratchet.py --fixture --plant empty-seed` runs in `tools/memory-tree/`, an armed
  empty `conf-scalar-pins` beside a conf assigning `ROW_DUPLICATE_PIN="0"` makes `keys-not-scalar` exit
  1 printing `empty seed conf-scalar-pins` and the re-seed command.
  Red when: an empty seed reads as an unheld pin owed a widen record.
- **AC9** — When `grep -n '# unarmed' ratchet.py` runs in `tools/memory-tree/`, it names one reader, the
  `unarmed` verb's, and `keys-not-scalar` over an unarmed home exits 1 printing `unarmed conf-scalar-pins`.
  Red when: two functions read the unarmed line.
- **AC10** — When `python legacy_ledger.py seed --home ../outside/x -- <argv>` runs in `tools/lib/`'s fixture
  repository, and with an absolute path outside the tree, and with a home under an ignored directory,
  each writes nothing and prints `outside the tree` or `ignored`; an absolute in-tree home prints `armed`.
  Red when: a seed writes outside the work tree or into an ignored path.
- **AC11** — When the codebase-map adopter arm runs, it names the exempt basename it took from the
  adopter's guard, and `git grep -n 'affordance-exempt\.toml' -- tools/codebase-map/adopt-codebase-map.test.sh`
  prints nothing on the built tree.
  Red when: the arm keeps a retired literal, so it reds after the rename or passes vacuously.
- **AC12** — When `python inherited_red.py up <target>` runs over an LF fixture and a CRLF fixture, every
  line it keeps is byte-identical to the before-image and each file keeps its line ends.
  Red when: a text-mode write turns an LF file CRLF.
- **AC13** — When `python tools/runlog/runlog.py check-records` runs on the built tree, it exits 0 over
  the committed records, and `grep -n 'EXCLUDED_KINDS_BEFORE_FIX_OF' tools/runlog/record.py` names it.
  Red when: adding `fix-of` refuses every committed record.
- **AC14** — When `python sh_hygiene.py --shell-role <ledger> .` runs on the `push-main.sh --prepare`
  merge, `<ledger>` being the shell-role ledger `shell-role.txt` (its path in §4 Files touched), it prints
  nothing, and each `widened:` row grown only through the
  default branch names a reconcile widen record.
  Red when: a shell file main grew exceeds its row on the merge the bar grades.
- **AC15** — When the §4 pass-commit rule runs for `TOOL-dWitnessedBar-24` before that unit's pass, it
  prints nothing and the derivation refuses naming the id; after the pass, it prints one SHA that is not
  `ad002a024`.
  Red when: a subject search resolves to the spec commit.
- **AC16** — When `python drift_report.py --gate-health --fixture held --selection <fixture>` runs in
  `tools/drift-audit/`, a leg held by a `quarantine` row and one held as `kit` are neither a bar leg; with
  no `--selection` it exits 2 naming the flag.
  Red when: the population omits the runner's quarantine holds.
- **AC17** — When `grep -c '^# >>> acceptance_reader\|^# >>> arm_walk' tools/check-spec-tokens.py` runs, it
  prints 2, and `git show --name-only --format= <unit 51's pass commit>` lists no path outside that
  spec's Files touched and S19's three.
  Red when: a parity row's canonical side lacks its markers, or a fourth unlisted write lands.
- **AC18** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, it reports no
  `[[generated]]` failure; on a scratch copy whose factory row reads `when = "exists:"`, it fails.
  Red when: selfcheck reds gov's tree, or admits a pathless `exists:`.
- **AC19** — When `git log --format='%H%x09%(trailers:key=Decided,valueonly,separator=%x7C)' cdfbd1cf..HEAD -- memory/HYGIENE.md memory/guides/BUILD-METHOD.md`
  runs at the close, every line carries `grants: PLAY-dClosedLoop-3`.
  Red when: unit 7's carrier edits land with no recorded grant.
- **AC20** — When `git log --merges --oneline cdfbd1cf..HEAD -- tools/lib/resolve-python.test.sh` runs at
  the close, it prints nothing, and the file's log names the passes of units 27, 48 and 49.
  Red when: two order-2 passes edited the file concurrently.
- **AC21** — When `grep -cE 'encoding-stdout-sites|encoding-js-sites|path-literal-sites|quoting-sites|shell-role' .memory-tree.conf`
  runs at gov's root on the built tree, it prints 0.
  Red when: a home stays admitted through `PROJECT_REGISTRY_EXTRA` too.
- **AC22** — When unit 51's AC35 probe runs on the built tree, it prints each pack's count and names, both
  above 0, and no mismatch; over a manifest with the `pack` keys removed, it reds.
  Red when: the check grades zero rows green.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `measure-legs selftest` · `run-gates canary` · `row-grammar selftest` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `shell-hygiene selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `drift-audit selftest` · `build-index selftest` · `spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 AC6 · the indented caller, the stub definition, the dropped canonical and the moved block row, staged red by matching column 0 only · none
New arm: tools/run-gates/measure_legs.py · covers AC4 · the variable `shutil.which` fixture, staged red by matching constant arguments only · none
New arm: tools/memory-tree/ratchet.py · covers AC8 AC9 · the plants `empty-seed` and an unarmed home, staged red by reading the unarmed line locally · none
New arm: tools/lib/legacy_ledger.py · covers AC10 · the outside, absolute and ignored homes, staged red by restoring the directory-exists test alone · none
New arm: tools/govkit/selftest.py · covers AC12 · the LF and CRLF step fixtures, staged red by a text-mode write · none
New arm: tools/drift-audit/drift_report.py · covers AC16 · the `held` fixture with a quarantine row, staged red by reading `test_held` alone · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of each repaired unit's clause, splitting clauses the
  roster units carry whole. (b) reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which call predicate does `--coverage` take, given M6 says column 0 and L7 says first word
  (ids 5, 19, 51)?** Options: (a) `$(resolve_python` or `^resolve_python\b` at column 0; (b) the first
  word of a command after whitespace or a command separator, definitions excluded. Both give 9 today; (a)
  misses an indented call a later edit writes. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3, the
  reading that meets every criterion both items name. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51: 12 MEDIUM and
  12 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-62's
  consumes-from edge, promoted by the round-1 spec audit of units 52 to 57; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names: unit 50's `--coverage` for S1 to S4, `regen.resolve_bash`
and `scan_bare_bash` for S5, `tree_lib.py` as the kit's shared-helper module for S7, the `unarmed`
verb for S10, unit 47's admission rule for S11, `record.py`'s legacy-template precedent
(`EXCLUDED_KINDS_BEFORE_HOLD`) for S15, the commit `Pass` trailer the driver already writes for S17, and
`check-spec-tokens.py`'s existing functions for S19. `python tools/codebase-map/reuse_lookup.py "find the
pass commit of a unit by its trailer"` ranked `units`, `build_commit`, `baseline_units` and
`build_unit_id_re`, none of which locates a pass by trailer, so the per-item seams above are the record.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 40 to 51 find in the resolver and ledger units" --terms "resolve_python coverage refuse_wrong_shell scan_bare_bash shutil.which seed home check-ignore shell-role widen Pass trailer gate-health"`
