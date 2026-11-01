**Serves:** journal TOOL-dSafePassage-102

# TOOL-dSafePassage-102 — acceptance ledger

The unit as built, at spec rev-2. Product writes: `memory/project/fork-ceilings.txt` (S1) and
`tools/run-gates/ceiling-evidence.txt` (S2), nothing else. Neither file moved between the spec's
`4f7ba0a30` and this pass's parent `699d6376f` (`git log 4f7ba0a30..HEAD` over both printed nothing).

THE FIFTEEN READINGS, taken at the parent `699d6376f` before any edit, from the worktree root on
node a under GNU bash 5.3.9 (cygwin), with
`bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only <id>`, each the
number after `measured`, in the order taken:

| Row | Readings | Bar's count at `5fe2c7e34` | Ceiling before -> after |
|---|---|---|---|
| `run-gates-1leg` | 56, 56, 56 | 56 | 55 -> 56 |
| `run-gates-2leg` | 58, 58, 58 | 58 | 57 -> 58 |
| `memory-hygiene` | 190, 190, 190 | 190 | 189 -> 190 |
| `manifest-check` | 76, 76, 76 | 76 | 74 -> 76 |
| `check-wiring` | 45, 45, 45 | 45 | 44 -> 45 |

Every reading equals the bar's count, so each ceiling is the largest reading, at the bar's count and
inside every reading's margin, and §4's halt did not trigger.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC2, AC4 and AC5 are the
legs' own argv, which scratch-guard's row G1 refuses to this role, so all three are owed at the
close. In AC2's place the counter ran with `--only` once per raised row after the edit.

**Evidences:** TOOL-dSafePassage-102
- AC1 — `grep -v '^#' memory/project/fork-ceilings.txt | cut -f1,3,4` printed seven lines in order: `unattended-status` 47 57, `check-unattended` 684 709, `run-gates-1leg` 56 72, `run-gates-2leg` 58 97, `memory-hygiene` 190 219, `manifest-check` 76 108, `check-wiring` 45 55. Each ceiling sits in its band.
- AC2 — owed at the close: `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .` under bash 5.3, to `fork-count: 7 passed · 0 red · 0 skipped — a skipped row is not a pass`. In its place `--only` per raised row printed `fork-count: ok` for each: `run-gates-1leg · measured 56 · ceiling 56`, `run-gates-2leg · measured 58 · ceiling 58`, `memory-hygiene · measured 190 · ceiling 190`, `manifest-check · measured 76 · ceiling 76`, `check-wiring · measured 45 · ceiling 45`. Before the edit the same five printed RED, as the readings above record.
- AC3 — the five pipelines over `git diff -U0 4f7ba0a30 -- memory/project/fork-ceilings.txt` printed (a) `0`, (b) `5` and `5`, (c) `check-wiring`, `manifest-check`, `memory-hygiene`, `run-gates-1leg`, `run-gates-2leg`, (d) nothing, and (e) `5`. Each clause's readings are the ledger's table above.
- AC4 — owed at the close: `bash tools/check-install-prefix.sh` exits 0 and names `tools/run-gates/ceiling-evidence.txt` on no line. Derived, not run: no respelled word carries a literal `tools/` lead (AC6).
- AC5 — owed at the close: `python tools/run-gates/derive-ceilings.py --check` exits 0, its out-of-band line opening with 7 ceilings and naming the three legs at 253.0 s, 366.0 s and 7177.0 s with the respelled words.
- AC6 — `git diff -U0 --word-diff=porcelain 4f7ba0a30 -- tools/run-gates/ceiling-evidence.txt | grep -E '^[-+][^-+]'` printed exactly six lines: `-tools/memory-tree/routed_commits.py` `+<prefix>/memory-tree/routed_commits.py`, `-tools/check-spec-tokens.py` `+<prefix>/check-spec-tokens.py`, `-tools/govkit/upgrade_walk.py,` `+<prefix>/govkit/upgrade_walk.py,`. The field-join pipeline over `4f7ba0a30` printed nothing.

The three criteria scratch-guard G1 refuses to a role agent were observed by the main loop at `50852889a`. AC2: `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .` exited 0 in 99 s, printing `fork-count: 7 passed · 0 red · 0 skipped`. AC4: `bash tools/check-install-prefix.sh` exited 0, printing `install-prefix: clean — 450 tracked file(s) graded, 7 render(s) left out as matching their template, 0 kit-path spelling(s) on 0 line(s)`, no line naming `ceiling-evidence.txt`. AC5: `python tools/run-gates/derive-ceilings.py --check` exited 0, printing `derive-ceilings: 7 ceiling(s) backed by a reading taken OUTSIDE the runner`, with the three respelled readings `<prefix>/memory-tree/routed_commits.py` 253s, `<prefix>/check-spec-tokens.py` 366s and `<prefix>/govkit/upgrade_walk.py` 7177s.
