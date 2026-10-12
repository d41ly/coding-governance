# Acceptance ledger — TOOL-aSparedSpawn-32

**Serves:** journal TOOL-aSparedSpawn-32

Node `a`, 2026-10-12, the second attempt at the reconcile. origin/main had moved past the spec's
37200355d to fcba06009 when the unit was dispatched, and to 6e8f8b1da, one records commit later, by
the time the merge was taken; the merge commit `51beae61f` takes 6e8f8b1da, 222 commits past the
build's parent `01ba3a815`, merge-base 69e0ff0f5. The extra commit touches four records and none of
the conflicted files. The same 16 files conflicted as in the driver's trial. The first attempt's
partial resolutions were reused where origin had not moved the file since 37200355d (`agent-cap`,
the hygiene suite and the turnstile suite) and ported onto origin's later delta with
`git merge-file` elsewhere (`.memory-tree.conf`, the run-gates dossier, the pre-push suite); the
runner, hook, evidence suite, README and `push-main.test.sh` were resolved afresh. Every observation
ran beside other sessions' bars on this host, so a fixture push took about ten minutes.

Commits: the merge `51beae61f` (`Pass: none`), carrying both reuse designs side by side; the spec
rev-4 `764b145d1` (`Pass: none`); and the pass commit after it, which composes the two designs per
§4 and closes the unit.

**Evidences:** TOOL-aSparedSpawn-32
- AC1 — the two-parent diff over the staged merge (`git diff -U0 69e0ff0f5 6e8f8b1da -- F`, every
  added line searched for in the index) — 11 files; origin's added lines absent from the result: 4 in
  the runner, 5 in the hook, 4 in the evidence suite, 1 in the README, 1 in `.memory-tree.conf`, 1 in
  `agent-cap.test.sh`, 1 in the hygiene suite, 2 in the dossier, 0 elsewhere. Each is a line both
  sides rewrote, kept as its composite: `HEAD_SHA=$RG_HEAD` (origin's read, this build's no-spawn
  fact), the nine-field ledger row with the builtin seconds read, `read_green_file` and the two
  scoped decision lines carrying both sides' fields, `lineage_reuses=0` initialised beside this
  build's `reuses=0`, the summed `FLOOR_ASSERTIONS` (evidence 208 + 26 = 234, hygiene 613 + 5 = 618),
  the `ARMS_FLOORS` line with both pairs, `agent-cap`'s `node nr.js` calls with origin's
  `unset GIT_DIR GIT_WORK_TREE`, and dossier prose condensed to its 20480-byte cap.
- AC2 — the same diff from `01ba3a815` — this build's absent lines: 1 in the runner, 13 in the
  hook, 3 in the evidence suite, 1 in the README, 1 in `.memory-tree.conf`, 2 in `agent-cap`, 1 in
  the hygiene suite, 12 in the dossier. Each is the same composite seen from this side, plus
  `check_green_record`'s reused argument, which moved into `check_green_reuse` because origin's
  signature gained a manifest path and a bar pair, and the probe's `if`, which gained the `--decide`
  guard when the probe moved after origin's cover pass. `push-main.test.sh` case 26 keeps origin's
  `core.hooksPath` line and drops its identity line, which this build's suite sets through the
  environment. The dossier lost a paragraph of reuse prose to the cap and points at the README.
- AC3 — `gen_map.py --check` exit 0 at the staged merge and on the pass tree; `gen_build_index.py
  --write` left no diff after its own re-render at the merge.
- AC4 — `grep -n 'last-audit\|last-body-change' memory/guides/SESSION-KICKOFF.md` — the merge took
  origin's stamps (`last-audit … @ 37e7b1da`); MANIFEST check 5 refused the pass commit until it
  carried the re-stamp, so the pass commit re-stamps `last-audit` at `764b145d1`, its parent and a
  descendant of the merge, neither parent's stamp. `last-body-change` stays origin's: no manifest body
  line moved.
- AC5 — `grep -c` of conflict markers — 0 in `.memory-tree.conf` and in the dossier; every key of
  either parent's conf is present (the conf's two-parent diff shows only the `ARMS_FLOORS`
  composite absent).
- AC6 — direct, at the merge and again on the pass tree: `bash -n` on the eight conflicted shell
  files 0; `govkit.py selfcheck` 0; `check-arms.py --check` 0; `check-spec-tokens.py` 0;
  `gen_map.py --check` 0; `check-memory-hygiene.sh --staged` 0 at the merge, after the dossier
  was condensed from 22192 to 20394 bytes (origin left it at exactly 20480). `sh_hygiene.py
  --spawn-idioms` redded at the merge on 29 rows, every one a site origin's code brought to this
  build's new registry (`post-merge.sh`, the turnstile suite's 20 `beacon`/`queue` substitutions,
  among them); the rows were re-measured and the leg reads 2188 sites in 302 rows, both readings in
  the merge commit's diff. `fork-count.sh --only run-gates-1leg` measured 53 three times against a
  ceiling of 51; the row was raised to 53, and the 2-leg row stayed at 55 of 55. On the pass tree
  the evidence suite's new arm added one `cat-file` site, converted to `$(<file)`, and both fork rows
  read 53 and 55.
- AC7 — `2026-10-12-build-TOOL-aSparedSpawn-32-fixtures.sh` (real runner and hook, a local bare
  remote) — RED at the merge: the runner died on `impures[$i]: unbound variable` in origin's ledger
  block, so the fix push stamped nothing and the next push was FULL. GREEN on the pass tree: the
  fix push was FULL with `reuse: lineage`, reused `pa`, and stamped `reused 1` and `reused_cache 0`;
  the next push, over a moved tree, was `scoped gate`. An empty commit is taken by origin's cover
  pass before any decision line, so the fixture moves the tree.
- AC8 — the same fixture with a stub bar — at the merge a stamp with `reused_cache 1` scoped and a
  lineage stamp (`reused 2`, `reused_cache 0`) was forced FULL; on the pass tree `reused_cache 1`
  forces FULL naming `reused 1 leg(s) from the cache`, an unlabelled `reused 2` forces FULL, and the
  lineage stamp scopes.
- AC9 — the fixture's runner section — RED at the merge (the runner died, header `reuse` written
  twice as `off,off`); RED on the first composed tree too, which found a red the merge produced:
  origin's host turnstile exports `GATE_TURNSTILE_HOLDER` before the reuse digest, so every key
  moved on every run with the turnstile on and nothing was ever reused. With the nonce left out of
  the digest, GREEN: `GATE reuse pa` and `reuse env`.
- AC10 — the same — RED at the merge; GREEN on the pass tree: a cached `ok` beside a ledger row
  with an empty `full`, and `GATE_FULL=1 GATE_REUSE_LINEAGE=1` executes `pa` and records `lineage`.
- AC11 — `grep -c 'WHAT LINEAGE REUSE DOES NOT CHECK' tools/run-gates/README.md` prints 1, the
  precedence table's header row occurs once, and the cache's not-checked sentence once.
- AC12 — the fixture's runner section — RED at the merge; GREEN on the pass tree: full with both
  knobs records `lineage` and prints `not used: GATE_REUSE`, and without the full flag records `env`
  and prints `GATE_REUSE_LINEAGE is not used without GATE_FULL`.

## Arms written and owed at VERIFYING

No suite ran in this pass. Written, checked with `bash -n` and by reading, and owed to the close:
the evidence suite's AC9, AC10 and AC12 arms, the lineage stamp's `reused_cache 0` arm, origin's
lineage arms re-staged on `GATE_REUSE_LINEAGE` and their opt-in controls on the cache's env mode,
and the floor raised to 240; the pre-push suite's AC7 arm in the LIN scratch, the AC8 pair beside
the predicate-9 arm, which now plants `reused_cache 1`, and the non-runner bar arm reading both
knobs.

## Found after the pass commit, and the records commit after it

- `manifest-check.sh memory/guides/SESSION-KICKOFF.md` redded check 9 at `ba16f0f6d`: the merge
  took origin's whole manifest, so `last-body-change` was origin's 31cf2f4c and counted this build's
  17 watched commits. Taking the whole file also dropped this build's one surviving body line, the
  bar command's `--calibrate-width` wording, which git had auto-merged; origin had deleted the
  other line this build reworded, the ceiling line, which stays deleted. The records commit restores
  the line, advances `last-body-change` and `last-audit` to `ba16f0f6d`, and the check exits 0.
- The pre-push suite's H49 class arm, replayed read-only over the runner and the hook: it reds at the
  build's parent `01ba3a815` on seven knobs this build's earlier units added to the runner
  (`GATE_REUSE_PUSH`, `GATE_REUSE_SAMPLE`, `GATE_REUSE_DAY`, `GATE_CALIBRATION_RATES`,
  `GATE_PUSH_BASE`, `GATE_SELFTESTS_MAX_LAG`, `GATE_SPAWN_NOW`) and is clean at origin 6e8f8b1da. The
  composition adds `GATE_REUSE_LINEAGE`, in `GATE_REUSE_PUSH`'s class: cleared by the hook for every
  bar, which none of the arm's three classes names. Owed with the seven, at VERIFYING.

## Announced gaps

- `tools/run-gates/post-merge.sh` and the unattended driver's `_gknobs` scrub `GATE_REUSE` from the
  bars they run and not `GATE_REUSE_LINEAGE`, so an exported lineage knob reaches a post-merge or
  close bar. Both run with the full flag, so such a bar would take lineage. Outside this unit's
  write set; spec §4 (f) records it as owed.
- The fork ceiling's +2 is attributed to origin's runner changes as a whole: a `--sites` diff
  against the build's parent could not be taken, because an archived tree outside git measured 72.
