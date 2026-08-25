# TOOL-dSpentCeiling-1 — build journal and acceptance ledger

**Status:** CLOSED · rev-1 · 2026-08-25 · node d · Tier-2 · base 70df24ea · streams tooling

**Serves:** journal TOOL-dSpentCeiling-1

## What was built

`READ_PATH_CEILING` and `READ_PATH_HEADROOM` are gone kit-wide. Check 16 keeps rules 3 and 4 and
loses its byte budget, and it left the armed unit entirely: `check_read_path(root, conf)` is a
top-level function that reaches neither `walk()` nor the id grammar, so it runs whenever the conf is
loadable and the memory-recall kit stays a conditional dependency. `armed()` drops to two pins and
switches to `.get`. The tracked-but-absent finding becomes rule 4 and loses its false attribution to
check 12. A conf still declaring a retired key is announced on a non-redding channel. Rules 3 and 4
report rather than gate until `READ_PATH_GATES_FROM`.

The release that ships this is memory-tree 2.43 and the grace ends at 2.44 — one release later, which is what the owner's ruling means. That pair MOVED once during the build: the closing fix changed the engine again, `check-verdict-epoch` required a second bump, and bumping onto 2.43 while the flip still read 2.43 would have ended the grace silently. The coupling is written beside `READ_PATH_GATES_FROM` so the next bump does not repeat it.

Landed across two commits on purpose: `47f9ba6b` carries the change without the version bump so
`check-verdict-epoch`'s refusal could be OBSERVED, and `8d5b8be0` carries the bump.

## Notes worth keeping

**The fixture target was wrong twice before it was right.** `memory/project/notes.md` looked like a
good uncapped rule-3 target and is not: `--print-index-set` answered with a check-3 structure failure
rather than a set, and a `grep -c` against that failure text read as a match. The kit's own rule-3
arm already used `memory/builds/tOne/spec/…`, which is structurally legal and genuinely uncapped —
reusing it was both cheaper and correct.

**The worktree copy of `corpus_ids.py` was CRLF while its blob was LF**, so every multi-line patch
needle missed. Normalising on read fixed the edits and repaired the smudge in the same move. MSYS
`grep -c $'\r'` reported CR counts for both files and was wrong about both; Python on the bytes was
the only reading that agreed with itself.

**`drift_report.py` evaluates RATCHETS only under `--check`.** The bare `--report` the charter points
sessions at does not, which is worth knowing before trusting a clean report to mean a clean ratchet.

## Acceptance ledger

**Evidences:** TOOL-dSpentCeiling-1

- AC1 — `corpus_ids.py --check` — the pre-change engine on a no-pin fixture whose charter cites an
  uncapped, tracked, present file: exit 0, no output. The control makes it stark — the same fixture
  with `READ_PATH_CEILING="100000"` exits 1 on rule 3, so a byte-budget pin was the only thing
  standing between a real defect and silence.
- AC2 — `check-memory-hygiene.sh --print-kit-version` — both halves observed. At engine 2.41 the
  finding PRINTS and the exit code is 0, with the grace announcing itself. The real constant was then
  bumped to 2.43 in place and the same fixture exited 1; a fixture citing only capped files stayed
  green at 2.43, so the rule is not merely always-red. Restored to 2.41.
- AC3 — `READ_PATH_WAIVER` — adding the cited path silenced rule 3, observed AFTER AC2's finding and
  never before.
- AC4 — `GRAMMAR_DIR` — the kit copied to a tree with no `memory-recall` sibling still fired rule 3,
  and stderr carried no `the id grammar lives in the memory-recall kit` refusal.
- AC5 — `DEAD_PATH_PIN` — with the pin set, check 15 and rule 3 both reported and the run exited 1;
  with the same tree and the pin blanked, check 15 went silent while rule 3 still reported. This is
  the arm that catches disarming 13-15 for an adopter whose only pin was the retired ceiling.
- AC6 — amended rev-2 — the criterion's stated mechanism was too narrow and §9 logs the correction.
  Both pre-change paths were observed rather than the one the spec described: with a ceiling declared
  the run printed ONE line (the `Problem`) and check 14 vanished; with no ceiling declared the mis-set
  charter was INVISIBLE because check 16 never ran at all. The post-change engine prints both findings
  in either case, which is what the criterion was reaching for.
- AC7 — `check 16 rule 4` — a charter-cited file tracked but removed from the worktree fired rule 4,
  and the message contains neither `check 12` nor `NOTE`.
- AC8 — `.memory-tree.conf` — a fixture declaring `READ_PATH_CEILING="161120"` exited with the same
  code as the same fixture without the key, plus the announcement; blank behaved identically, because
  presence is the test; the line deleted produced no announcement.
- AC9 — `govkit.py selfcheck` — dropping the key from `conditional_keys` while leaving it in
  `requires_if.when_any_key_set` redded with `requires_if names condition key 'READ_PATH_CEILING',
  which appears in none of its own config key lists`. Both moved, then green.
- AC10 — `check-method-carriers.sh` — with the conf pointer no longer naming `BUILD-METHOD.md`,
  check 4 redded on `.memory-tree.conf` as a stale declared carrier. Pointer restored, then green.
- AC11 — `check-verdict-epoch.sh` — observed as its own commit. `47f9ba6b` moved 208
  behaviour-bearing engine lines with the constant still at 2.41 and the gate refused, naming all
  three moved files. `8d5b8be0` carried the bump and the gate reports clean. The spec's wording
  described the bump-placed-too-early arm; the arm actually run was no-bump-at-all, which is the same
  refusal from the more fundamental side.
- AC12 — `kit-dogfood-parity.test.sh` — the template edited without re-rendering redded with the
  diff. Re-rendered via `--render`, then green; `memory/HYGIENE.md` was never hand-edited.
- AC13 — OBSERVED SILENCE, and recorded as such: with both keys gone from the conf and a `RATCHETS`
  row naming `READ_PATH_CEILING` restored, `drift_report.py --check` produced ZERO findings
  mentioning it. Deleting that row was therefore a manual obligation and no gate covers the class.
- AC14 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — GREEN, 85/85 legs, at
  `4b26d2b0`. It took five runs. The four that redded are the point of the criterion and are
  listed below, because a green reached on the first try would have proved only that the bar was
  not looking.

## Staged breaks, run against the shipped code

Three arms were proved to bite by breaking the real thing and watching exactly one arm fail each
time: the grace comparison made unconditional failed `at or above the flip version the same finding
GATES`; rule 4's message given back its `check 12` clause failed the misattribution arm; and the
retired ceiling put back into `armed()`'s tuple failed `a retired key alone does not arm checks
13-15`. Each was restored and the suite re-run green.

## What the DoD bar caught, across five runs

None of these were visible to the guard-scoped bar, and all four legs that matter here are
`subject: kit` and held by default — a plain green over this change really would have proved close to
nothing.

1. **`memory-hygiene self-test`** — `adopt-memory-tree.sh --scaffold` writes no `CHARTER` and no
   `AGENTS.md`, so making check 16 unconditional redded every adopter on the day they adopted. The
   grace did not cover it because the charter finding gated unconditionally. Fixed by
   `read_declared_keys()` and by moving the grace decision into `_resolve_sink()`, shared by all
   three arms.
2. **`verdict epoch`** — twice. First for the bump this build owed, which was observed deliberately.
   Then again when the closing fix moved the engine after the bump: the gate is topological, so a
   bump that is older than the change it dates is refused. Bumping to 2.43 collided with
   `READ_PATH_GATES_FROM = (2, 43)` and would have ended the grace on the release that ships the
   retirement — the flip moved to 2.44 in the same commit.
3. **`drift-audit records`** — `closed_specs_with_no_product_commit` keys on the build SLUG appearing
   in a product commit's SUBJECT. Three product commits, none naming `dSpentCeiling`. The convention
   is that a product commit says which build it serves.
4. **`install-prefix` and `dead-path carriers`** — both registries pin LINE NUMBERS, and this build
   moved lines in `corpus_ids.py` four times. Re-pinned three times for install-prefix and once for
   dead-path, in every case without the waived thing or its reason changing. Filed as
   `TOOL-dSpentCeiling-6`.
