**Serves:** journal TOOL-dWitnessedBar-5

# TOOL-dWitnessedBar-5 — builder return 1 (run `wf_f155de9c-57a`), a divergence, nothing committed

## Why

BLOCKED AT THE COMMIT, NOT A SPEC DIVERGENCE. The commit has to carry a path that `--dispatch` refuses to declare, so nothing was committed.

1. The pre-commit hook refused the pass commit with `MANIFEST check 5 FAILED`. `tools/run-gates/run-gates.sh` is on the `watch:` list in memory/guides/SESSION-KICKOFF.md, so the hook requires the manifest's `last-audit` re-stamp in the same commit.
2. memory/guides/SESSION-KICKOFF.md is not in the declared write set. I ran `bash tools/unattended/unattended.sh --dispatch dWitnessedBar --pass TOOL-dWitnessedBar-5 --writes ...` twice. Both runs were refused by `UNATTENDED check 49 FAILED`: the spec-token checker is red over the live tree because `chain-packet.py --check dWitnessedBar` reports `byte compare red`. The packet pins the as-built view memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md at blob d951c621 (as at c9b50206). Sibling commit acd04756e (TOOL-dWitnessedBar-44) moved that file to ec1fdfea and did not re-pin the packet.
3. The same refusal also blocked two other paths I meant to add: tools/playbook/kit.toml and a deviation record under build/.

That refusal is binding, and `--no-verify` would route around the hook, so I stopped.

What the main loop needs to do:
- Re-pin or re-render the dWitnessedBar packet so check 49 goes green.
- Re-dispatch this unit with memory/guides/SESSION-KICKOFF.md added to its writes (plus the deviation record, and tools/playbook/kit.toml if wanted), or commit the staged pass itself with the re-stamp bundled in.

I put the spec header back to INPROGRESS so the driver's `--plan` does not read this unit as finished.

## Summary

TOOL-dWitnessedBar-5 is NOT committed. The whole build is in the shared working tree, uncommitted and unstaged. The pre-commit hook needs a kickoff-manifest re-stamp in the same commit, and `--dispatch` refused to declare that file because of a packet red introduced by sibling commit acd04756e (details in `why`). Base: c9b50206fdd4df08a52f6cddbd0ee9594525cb05.

**Left in the working tree, all inside the declared write set:**
- `.githooks/pre-push`: reads `verdict.held` at R next to `verdict.blocks`. Under `push-selected`, when the pusher set no `GATE_SELFTESTS`, it exports `GATE_SELFTESTS=changed` before the recorded greens are read. Before admitting a bar whose run record holds a `selection`, it runs `verdict_flow.py select --check`.
- `.githooks/pre-push.test.sh`: `GATE_SELECTION` added to `BAR_INERT_KNOBS` with its reason line, plus the new SEL arms for AC5 and AC6.
- `tools/run-gates/run-gates.sh`:
  - one predicate, `derive_hold_source`, now called from all three old sites and from `report_one`;
  - `GATE_SELECTION` is read once and unset, and the file is copied into the run record as `selection`;
  - one held-line format; the summary counts held legs by source;
  - `held.<n>` keys in all three verdict writers.
- `tools/run-gates/run-gates.test.sh`: the selection canary arm (AC2, AC3), and the summary and `(kit, unchanged since` patterns updated.
- `tools/run-gates/verdict_flow.py`: `select`, `select --check`, `read_held_keys`, `read_selection`, `SELECT_SOURCES`, and fixtures `selection-rows`, `held-keys`, `select`, `held-policy`.
- `tools/run-gates/leg_factory.py`: the `held guard` arm, `· <h> held · <u> unguarded` on the count line, and selftest cases for it.
- The 36 descriptor or registry rows each gain an `unguarded_why`. The held-halves and review-replay comment reasons moved into that key.
- `verdict.held` documented: summary and usage in `tools/policy/catalogue.toml`, drained from `tools/policy/unsummarised-keys.txt`, and a section on `help/reference/policy.md`.
- `tools/run-gates/README.md` updated; `memory/map/generated/symbols.json` regenerated.
- The ledger `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-5-1-acceptance-ledger.md` is written.

The spec header and the files `gen_build_index.py --write` rewrote (`memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README) are back at HEAD. The commit message is ready at `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/msg5.txt`. `gotchas.py --for-diff` was not run, because there is no commit.

**Checks that ran (each stands in for the named leg, not for the gate itself):**
- AC1, AC3, AC7 (README part), AC8, AC9: greps over the built tree, compared with c9b50206. Each read green now and red at c9b50206. These stand in for `spec tokens` and `help reference pages`.
- AC2, AC4, AC5, AC6: `verdict_flow.py --fixture` for selection-rows, held-keys, select and held-policy all exited 0, and `route` and `red-route` stay green. At c9b50206 the same fixture names are refused with a usage line. These stand in for the `run-gates canary`.
- Runner hold block and `report_one`: extracted and run over planted arrays. This stands in for `run-gates canary` and `run-gates gov canary`.
- Hook admission and export blocks: extracted and run over a planted repo at `%TEMP%/v5h`. This stands in for `pre-push self-test`.
- `check_knob_classes`, extracted, was clean over the built runner.
- `check_declarations` with planted held declarations: flagged neither, an empty reason, and both; silent on a guard alone and on a reason alone.
- `run_check` shows the manifest is unchanged.
- The naming lexicon `--suggest` was OK for every new name.

**Owed at the close:**
- The three `New arm:` lines, each needing its RED-first observation: `run-gates.test.sh` (AC2, AC3), the `held guard` cases in `leg_factory.py --selftest` (AC7), and the SEL arms in `.githooks/pre-push.test.sh` (AC5, AC6).
- Every leg in spec §7 (merge bar).
- AC7's scratch-clone run.
- `.governance/policy.json` needs `policy.py mirror --write` after the pass, as the spec says.

**Found while building:**
- `leg_factory --conform` on the landed tree exits 1 on a `name` finding that is not this unit's: unit 24's leg `encoding posture (an entry point writes stdout as UTF-8)`. AC7's exit 0 can't be observed until that leg is renamed.
- `playbook render selftest` is guarded only under `[gate_leg.gov]`. The adopter form of `--conform` will flag it until its descriptor gets an `unguarded_why`; that file was refused.
- AC6's export rule is spelled twice: once in `verdict_flow.py#derive_held_export`, which the fixture observes, and once in the hook, which the pre-push arm observes.
- A deviation record for these choices is owed. Its path was refused, so the choices are on the message's `Decided:` lines for now.
