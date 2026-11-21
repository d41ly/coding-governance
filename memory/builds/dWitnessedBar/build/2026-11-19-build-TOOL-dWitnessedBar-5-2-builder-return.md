**Serves:** journal TOOL-dWitnessedBar-5

# TOOL-dWitnessedBar-5 — builder return 2 (run `wf_b08bb6c4-c96`), committed eef75404f33bd8d97d096a7593e2171114c2e624

## Why

TOOL-dWitnessedBar-5 is built and committed as one pass commit. Its subject names the unit, and it carries `Pass: TOOL-dWitnessedBar-5` beside `Co-Authored-By: Claude Opus 5`. The spec header is now CLOSED · rev-8 · 2026-11-20, and that edit changes nothing else in the spec. The first builder's work was checked against the spec, not rebuilt. One defect was fixed: the `held guard` arm would have flagged `playbook render selftest` in every adopter, or in gov once that leg got a reason; deviation 52 records the fix. This pass also wrote the deviations, the kickoff manifest re-stamp and the ledger update the earlier pass could not commit. There is no spec divergence. (DERIVED from the builder's probe)

## Summary

Base 30160e0c; commit eef75404f (30 files). This pass resumed the first builder's uncommitted work (run wf_f155de9c-57a) and finished it.

**Checked against the spec and kept:**
- `tools/run-gates/run-gates.sh`: one `derive_hold_source` with `kit`, `quarantine` and `level` as sources; `GATE_SELECTION` read once and unset, the file copied into the run record; one held-line format; the summary counts by source; `held.<n>` keys in all three verdict writers.
- `tools/run-gates/verdict_flow.py`: `select`, `select --check`, `SELECT_SOURCES`, and four fixtures.
- `.githooks/pre-push`: reads `verdict.held` at R, does the `push-selected` export, and runs `select --check` before admitting a bar whose run record holds a selection.
- `.githooks/pre-push.test.sh`: `GATE_SELECTION` in `BAR_INERT_KNOBS`, plus the SEL arms.
- `tools/run-gates/run-gates.test.sh`: the canary arm and the updated held-tail patterns.
- The 36 `unguarded_why` keys, the `verdict.held` catalogue summary and usage, `help/reference/policy.md`, and `tools/run-gates/README.md`.

**Changed in this pass:**
- `tools/run-gates/leg_factory.py#check_declarations`: the "both" case now refuses a reason only when the leg has a guard in every form (its own row and gov's render). As it was, the arm flagged `playbook render selftest` for carrying neither in the adopter form; with an `unguarded_why` added it would have flagged the same leg for carrying both in gov. The selftest case wording follows the new message.
- `tools/playbook/kit.toml`: `playbook render selftest` gains an `unguarded_why`.
- New records: `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-5-deviation-52.md` (the split-guard rule) and `-deviation-53.md` (the push-selected export spelled in both the hook and `derive_held_export`).
- `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped at 30160e0c, with one body change on the `GATE_SELFTESTS=1` line.
- The acceptance ledger updated for AC7.
- The files `gen_build_index` rewrote: `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README, the spec's records rows, and the dClosedLoop as-built view (2228 to 2230 deviation records).

**Write set:** my extra `--dispatch` for the as-built view replaced the declaration at 30160e0c. The pre-commit check (check 49) then refused the commit and printed the exact widening command, which I ran with the paths already declared at bf873d18. The second commit went through every hook.

**Checks that ran (none is a gate):**
- AC1, AC3, AC7's README grep, AC8 and AC9: greps over the built tree, all green. They stand in for `spec tokens`, `help reference pages` and `pre-push self-test`'s knob-class arm.
- `verdict_flow.py --fixture` for route, red-route, selection-rows, held-keys, select and held-policy: all exit 0. They stand in for `run-gates canary` and `pre-push self-test` on AC2 and AC4 to AC6.
- The runner's hold block, extracted and run over a planted selection file: the quarantine and level rows are held, the unknown and `kit` rows are refused, and the file is copied byte-equal. Stands in for `run-gates canary` and `run-gates gov canary`.
- `check_declarations` probes: neither, an empty reason, a blank reason, and a guard in every form are each refused; a split guard and a guard alone pass.
- `leg_factory.py --conform` prints `101 held · 36 unguarded` with no `held guard` finding. The adopter form shows no `held guard` finding. `--check` reports the manifest fresh.
- `bash -n` over the four edited shell files: syntax clean.
- The naming lexicon `--suggest` passes every new name.
- `gotchas.py --for-diff HEAD~1..HEAD` selected 63 classes. I acted on these: the old `(self-test,` spelling has no reader left; TAB fields collapsing when empty only ever run the leg; the duplicated rule is recorded as deviation 53.

**Owed at the close:**
- Every §7 leg.
- RED-first observation of the three `New arm:` lines: the `run-gates.test.sh` selection arm (AC2, AC3), the `held guard` cases in `leg_factory.py --selftest` (AC7), and the `.githooks/pre-push.test.sh` SEL arms (AC5, AC6).
- AC7's scratch-clone run. AC7's exit 0 also stays red until unit 24's leg `encoding posture (an entry point writes stdout as UTF-8)` is renamed; that red was already there at base and is not this unit's.
- `.governance/policy.json` needs `policy.py mirror --write` in the commit after the pass, as the spec's Rollout says.

**For the main loop:**
- Re-pin the dWitnessedBar packet's pin of the as-built view, which this commit moved (the same thing that happened at bf873d18c).
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-44.md` has a generated records row I left unstaged, because it is unit 44's file. `help/reference/drive.md` and `help/reference/units.md` differ only in line endings and were left alone.

No command hit its time limit and nothing was skipped.
