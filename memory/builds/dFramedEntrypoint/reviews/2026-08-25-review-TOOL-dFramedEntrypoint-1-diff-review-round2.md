**Serves:** diff-review TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8

# Diff review round 2 — the cumulative diff landing on main

**Reviewed range: `beb5fce43e2680983f01732975ae005b004eb980...HEAD` (HEAD = `54bb627690f3de6d05dc0c84d17def9e06baf775`). ROUND 2.**

*Node d, 2026-08-25. Two commits, 22 files, +557/-109. This round reviews the FIXES round 1 asked for, not the build again: `2b6b2e62` (the verb-table rename over `gen_build_index.py`) and `54bb6276` (the three blockers round 1 found, plus the data loss one of them caused). Adversarial finder fan, then skeptics prompted to REFUTE, then this synthesis. Every finding below was reproduced in this worktree, not reasoned about.*

## Verdict: BLOCKED

### Review shape

Raw 14 · confirmed 12 · refuted 2 · unverified 0 · precision 0.86.

The 12 confirmed findings collapse to **5 distinct defects**: **1 BLOCKER · 1 HIGH · 3 MEDIUM**. Four separate finder lenses reached the blocker and four more reached the high, which is why the raw count is nearly triple the defect count. Each defect below names every finding id that reached it, so nothing is lost in the merge.

### The shape of what was found

Round 1's through-line was **a check that cannot fail**, and both top defects of this round are that same class *reintroduced by the fixes for it*. The blocker is a guard that never takes its true branch on any node in this repo's registry — the fix is inert on the platform it was written on, and the only branch it has ever been observed taking is the one that does nothing. The high is the left-shift arm for round 1's data-corruption defect: it names two functions in its label and calls neither, so the exact regression it was added to catch passes the suite unchallenged.

Both were proven by reproduction — the guard by running the scaffolder, the arm by reverting the buggy filter and watching `--selftest` print `PASS`. Neither fix shipped with its failing case observed. That is the §7 rule the two of them break together, and it is why the verdict is BLOCKED rather than CLEAN WITH FIXES.

---

## BLOCKER

### B1 — the ceiling-strip guard compares two different spellings of the same path, so it is dead on every node

**`tools/memory-tree/adopt-memory-tree.sh:155`** *(finders 1, 4, 7, 10 — four lenses, one defect)*

The new guard reads `case "$HERE/" in "$ROOT"/*)`. `ROOT` is set at line 8 from `git rev-parse --show-toplevel`; `HERE` is set at line 10 from `cd "$(dirname "$0")" && pwd`. Under MSYS those are two different spellings of one directory, so the prefix test never matches.

Measured in this worktree, from `tools/memory-tree/`:

```
ROOT   = C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea
HERE   = /c/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea/tools/memory-tree
ROOT_N = /c/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea

case "$HERE/" in "$ROOT"/*)    ->  NO-MATCH
case "$HERE/" in "$ROOT_N"/*)  ->  MATCH
```

The script's own header at lines 11-16 documents this exact trap — under MSYS one directory has two spellings, a drive-letter one from `git rev-parse` and a mount-point one from `pwd`, and a raw strip across those flavors silently yields an absolute path that substitutes nothing and looks like it worked. It computes `ROOT_N` at line 16 precisely to avoid that, and `KIT_REL` at line 17 uses `ROOT_N` correctly. The new guard is the one comparison in the file that regressed to the raw `$ROOT`.

**Consequences, all four reproduced.**

1. **The in-tree strip never runs.** A fresh repo with the kit copied to `tools/memory-tree/` inside it, scaffolded from inside it, keeps gov's ceilings verbatim: `900 / 500 / 500 / 1800 / 1800`. Every node in the AGENTS.md registry is Windows, so this is every adopter following `WIRE-INTO-PROJECT.md`'s copy-then-run order.
2. **The stderr line is false and actively misleading.** The `*)` arm prints `memory-tree: kit dir is outside $ROOT — leaving its build-readme-slot-limits.txt alone; copy the kit into the target tree first` on the normal in-tree run. It instructs the operator to do what they have already done.
3. **A declared measurement hole silently discharges itself.** `tools/memory-tree/kit.toml`'s `slot-budget-ceilings` hole states the file ships with its canonical rows and no ceiling values, because a pin measured against gov's corpus and shipped into a tree that never measured it is either vacuous or permanently red — the invariant `build-readme-slot-limits.txt:24` spells as `ADOPTERS DO NOT INHERIT THESE`. The hole's discharge probe, an `awk` scan asserting every `## ` row's second field is a bare integer, then sees the inherited integers and exits 0. Govkit reports the hole DISCHARGED in a tree that measured nothing.
4. **The fix has only ever been observed taking the no-op branch.** Nothing tests the strip: a grep for `build-readme-slot` across `tools/memory-tree/*.test.sh` returns zero hits, and the only adopter invocation in the suite (`check-memory-hygiene.test.sh:1168`) runs from gov's own kit dir against a temp repo, where `*)` is the correct arm.

It fails safe for gov only by accident — the else branch happens to be the non-destructive one.

**Fix.** One token: `case "$HERE/" in "$ROOT_N"/*)`. Better, stop spelling the inside/outside decision two incompatible ways in one file. The script already derived that fact twenty lines earlier, where the kit is inside the tree exactly when `[ "$KIT_REL" != "$HERE" ]`. Set a `KIT_INSIDE` flag in those two branches and test it here, so the two answers cannot disagree.

**Left-shift gate.** Arm the POSITIVE branch, which has never been observed. In `check-memory-hygiene.test.sh`, beside the existing scaffold arm: copy the kit into the temp repo, run `--scaffold` from that copy, and assert every `## ` row in *that copy's* `build-readme-slot-limits.txt` has an empty second field. Add the mirror arm for the out-of-tree case asserting gov's own file is byte-identical after the run. Confirm the positive arm REDs against the current `$ROOT` spelling before landing it.

---

## HIGH

### H1 — the left-shift arm for round 1's data-corruption defect is a tautology over four string literals

**`tools/memory-tree/gen_build_index.py:1900`** *(finders 2, 5, 8, 11 — four lenses, one defect)*

The arm is labelled `read_slot_table and do_bump agree on what a comment is`. Its lambda calls neither function:

```python
lambda: str(all(("\t" in l) != (l.strip().startswith("#") and "\t" not in l)
                or not l.strip()
                for l in ["# c", "## S\t9", "", "## T\t"]))
```

A closed boolean over four hardcoded literals, referencing no module state. Evaluated standalone, without importing the module at all, it returns `True`, and every element satisfies it independently — so the arm's expected value `"True"` is satisfied by arithmetic, not by the code under test. Grepping `do_bump` across the file confirms exactly three references: its definition (1574), this arm's *label* (1900), and the dispatch in `main()` (2251). No arm anywhere drives it.

**Proven by mutation.** Reverting the keep-filter at line 1586 to the exact buggy predicate the comment names — `if not l.strip() or l.lstrip().startswith("#")` — and running `--selftest` prints:

```
arm ok    read_slot_table and do_bump agree on what a comment is
PASS — gen_build_index: all arms held
```

exit 0. That mutation *is* round 1's D4 regression: the buggy filter retains tab-bearing `## Slot A` rows, so `keep + rows` duplicates all five high-water rows on every `--bump` — 5, then 10, then 15, in a tracked data file. It now has **zero** regression cover and would land green through the merge bar.

The harness is otherwise armed, which is the control that makes this a real defect rather than a broken runner: mutating the D2 duplicate-detection block reds exactly one arm and exits 1.

The comment at lines 1583-1585 asserts that the agreement "is now armed". It is not. The label reads as verified coverage to every later reviewer of this file, which is worse than no arm at all — §7's "a gate you have only ever seen pass is an assertion about nothing", reintroduced by the fix for it.

**Fix.** Make the arm run the code. Two shapes, either acceptable.

- **Single-source the grammar.** Extract a named predicate — a comment row is a line with no tab — and have both `read_slot_table` and `do_bump`'s keep-filter call it. There is then one answer to the question, and the arm can test the predicate directly.
- **Arm end-to-end.** Write a high-water fixture into a temp root, holding the header comment lines plus one row per canonical slot. Call `do_bump` twice against a fixture tree. Then assert the tab-bearing row count is exactly `len(SLOT_CANON)` after each run, that the two written byte-strings are identical, and that the `# ` header comment survived.

**Left-shift gate.** Whichever shape lands, the arm is not done until it has been observed RED against the reverted line-1586 filter. Generalise beyond this one arm: add a meta-arm asserting that every arm whose label names a module function actually references that function in its body. This is the second time in two rounds that a label has claimed coverage its lambda does not deliver, so the class is established and gateable.

---

## MEDIUM

### M1 — the adopter arm that caused the data loss still asserts nothing about what the adopter writes

**`tools/memory-tree/check-memory-hygiene.test.sh:1168`** *(finder 9)*

Line 15 sets `HERE="$(cd "$(dirname "$0")" && pwd)"` — the real kit dir — and line 1168 is the suite's only `bash "$HERE/adopt-memory-tree.sh" --scaffold`. Its assertions at 1176, 1182 and 1186 cover only the scaffolded tree's `memory/project/*` contents and its hygiene rc. Nothing asserts the integrity of the kit copy the scaffolder just wrote into.

This is the run that blanked the tracked ceilings in `beb5fce4`. The commit shows exactly the five values emptied in a landed commit, and the arm did that on every invocation while the leg printed clean. `54bb6276` touched 11 files and this test file is **not** among them: the guard shipped with no assertion behind it.

Combined with B1, the suite is byte-identical whether the new guard works, is inverted, or is deleted outright. Any future write under `$HERE` — not only this one — is again undetectable. A grep for `build-readme-slot` across the kit's test files returns zero hits.

The only adjacent control is `run-gates.sh:1151-1153`'s `tree_moved`, which merely suppresses the full-green stamp. It does not red the run, does not name the mutated file, and did not prevent the blanked ceilings from being committed.

**Fix.** Add the class-level invariant, three lines. Before invoking the adopter, snapshot the kit directory into a sorted checksum file. After it returns, take the same snapshot and diff them, failing with the name of any file the scaffolder modified.

**Left-shift gate.** That snapshot-and-diff IS the gate, and it catches the class rather than the instance: it reds on any write under `$HERE`, not just to the ceilings file. It is also the only assertion that makes B1's `case` guard testable at all, so land it together with B1's positive arm.

### M2 — round 1's own record is false on arrival, and its still-open fixes name symbols that same commit deleted

**`memory/builds/dFramedEntrypoint/reviews/2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md:23`** *(finder 13)*

Line 23 states the verb-table rename "is uncommitted and outside the reviewed range". The name-only listing for `2b6b2e62` contains the review record AND `tools/memory-tree/gen_build_index.py` AND the regenerated `memory/map/generated/symbols.json`, in that one commit. The record's path has no amendment in its history, so this is self-inflicted at authoring time, not drift. The commit message even corrects the attribution — the lexicon regression was the same session's — while leaving "a concurrent session is mid-rename in this worktree" standing.

The caveat's translation list names three renames. The record cites three more symbols with no bridge at all, and none of them exists at HEAD: `assert_contract_registry` (2 citations), `_canon_violations` (3), `budget_findings` (2), plus bare `slot_sizes` (2). All return zero hits under `tools/` at HEAD.

This is live work, not history. Round 1's still-open items instruct against dead names:

| record line | instruction | spelling at HEAD |
|---|---|---|
| 221 | compare `lines[i].rstrip()` against `heads` in `slot_sizes` | `measure_slot_sizes` |
| 310 | call `assert_contract_registry(root, conf, tracked)` | `check_contract_registry` |

Both defects are still open — `gen_build_index.py:1042` is still `if lines[i] in heads:` (D8), and `do_report` and `do_bump` still call `read_contract_registry` bare (D13) — so a later pass acting on the open items greps for symbols the same commit deleted. Only the "outside the reviewed range" half of line 23 survives, since the range is pinned to `beb5fce4`.

**Fix.** Treat the findings as frozen evidence and add ONE dated addendum block at the top of the record: correct line 23 to say the rename landed in `2b6b2e62`, then map old spelling to HEAD spelling for every renamed symbol the record cites, including the three the original caveat omitted. The open items stay actionable without rewriting the findings themselves.

**Left-shift gate.** A review record's backticked symbol citations are machine-checkable against the tree. Add a check that every backticked identifier in a `diff-review` record which looks like a Python function name resolves either in `memory/map/generated/symbols.json` or in a rename line of that record's own addendum block. Scope it forward-only by a cutoff date, exactly as hygiene check 22 is, because a landed review is not rewritten.

### M3 — the duplicate-heading scan runs over every heading, so a repeated non-canonical one is reported as a duplicated canonical slot

**`tools/memory-tree/gen_build_index.py:1178`** *(finders 6 and 12 — rated low and medium respectively; taken at the higher)*

In `scan_canon`, `seen` accumulates every line starting with `## ` at line 1169, canonical or not. The duplicate loop at 1176-1178 counts over that unfiltered list and emits `canonical slot heading appears more than once` without testing membership in `SLOT_CANON`. The early return at 1179-1180 then fires on that hit, so the `heading outside the canon` branch never runs.

Measured against the live module:

| README | what `slot_violations(..., canon=True)` returns |
|---|---|
| one `## Afterword` | `[(29, 'heading outside the canon: ## Afterword')]` |
| `## Afterword` twice | `[(29, 'canonical slot heading appears more than once: ## Afterword'), (33, same)]` |

Two rows both asserting `## Afterword` is a canonical slot, which `SLOT_CANON` does not declare, and the correct diagnosis gone. Not by design: the D2 comment and the arm at 1894 scope the fix to a repeated CANONICAL heading.

The file still reds either way, so this costs a wrong *reason* rather than a missed failure, which is why it is medium and not higher. But the wrong reason is the harder one to act on. The operator is told to de-duplicate a slot that should simply be deleted, and §7 requires a failure to name the row truthfully.

**Fix.** Scope the duplicate scan to the canon. Compute the canonical heading set before the loop and guard the count with membership in it. A repeated out-of-canon heading then falls through to the existing `heading outside the canon` branch, which already names each occurrence correctly.

**Left-shift gate.** An arm on the two-`## Afterword` fixture asserting the emitted string contains `outside the canon` and does NOT contain `more than once`. The negative half is the load-bearing half: this defect is a message appearing where it should not, so an arm checking only for the presence of the right text would pass today.

---

## Refuted

Two of the fourteen raw findings did not survive a skeptic and are recorded as refuted, not carried. Precision 0.86 is comfortably above the ~0.5 floor §8 sets for tightening scope before adding agents, and the four-way convergence on both top defects says the lens fan was correctly primed for this diff rather than over-wide.

## What this round did NOT cover

- Round 1's remaining open findings are **not** re-verified here. This round reviews `beb5fce4...HEAD`, which is the fix commits only. The round-1 record remains the live list for everything it left open, subject to M2's symbol-name caveat.
- No gate was run as part of this review. The claims above come from direct reproduction — the guard by running the scaffolder into a fresh repo, the arm by mutation and rerun — not from a bar verdict.
- `2b6b2e62`'s rename itself was reviewed only for the record-consistency fallout in M2. The changed lines of `gen_build_index.py` in that commit were not re-reviewed as a behavioural change, on the ground that a pure rename with `symbols.json` regenerated in the same commit is Tier-1 shaped.
