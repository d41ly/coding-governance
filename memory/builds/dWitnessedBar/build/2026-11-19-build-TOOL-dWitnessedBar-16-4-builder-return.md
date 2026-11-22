**Serves:** journal TOOL-dWitnessedBar-16

# TOOL-dWitnessedBar-16 — builder return 4 (run `wf_59b77b58-240`), a divergence, nothing committed

## Why

DIVERGENCE: the spec's S10 and its §4/§8 F3 homes conflict with its own §7 leg `install-prefix (shipped surface)`. The brief tells this pass to fix that leg. That leg has no waiver, and as written the spec leaves no spelling that both passes the leg and still runs under the landed factory and step runner.

(1) S10 argv. S10 spells every `[[upgrade]]` argv as `["python", "{gov}/memory-tree/convert_registry.py", ...]`. That is 33 argv elements: 6 in `tools/codebase-map/kit.toml`, 6 in `tools/drift-audit/kit.toml` and 21 in `tools/memory-tree/kit.toml`. Rule 3 of `tools/check-install-prefix.sh` (KSEG) counts kit/file under any prefix, and `{gov}/` is not on its DRAINED list (`{prefix}/`, `{kit}/`, `{{TOOL_ROOT}}`, `<prefix>/`, `<tool-root>/`). The other spellings all fail:
- `check_argv` in `tools/govkit/upgrade_steps.py` admits only `{gov}`, `{target}` and `{prefix}`.
- `{prefix}/` does pass the gate, but in a step `derive_step_context` resolves it to the target's install prefix with its slashes stripped (relative, e.g. `tools`). `run_step_isolated` spawns with `cwd=gov_root`, so at any other prefix the program path names nothing. The step contract (`read_steps`, `check_frozen`) also keys on `{gov}/` programs that gov tracks.
- `{target}/{prefix}/memory-tree/...` runs the target's own copy, not gov's tracked program. That changes what S10 runs.
- The gate-clean route is a gov step program on a path that is not kit/file, e.g. `tools/govkit/steps/<name>.py`, as `review_rounds.py` sits. That route is a new file, which Files touched does not list, and a different argv from the one S10 spells.
So S10 (with Files touched) has to name the program and spelling. Respelling it here would be building against S10.

(2) Four `[[ledger]]` homes under gov's tool root:
- `tools/drift-audit/drift-pins.txt` and `tools/drift-audit/drift-baselines.txt`: §4 Drift; `tools/drift-audit/kit.toml` lines 193 and 203.
- `tools/dead-path-waivers.txt` and `tools/playbook-kit-waivers.txt`: §4 table and F3; `tools/govkit/registry.toml` lines 2460 and 2470.

Rule 2 counts all four. `tools/lib/legacy_ledger.py#read_registrations` / `check_home` read `home` literally, with no token resolution, and unit 51 S32 resolves tokens only in seed argv. So no spelling of these homes both passes the leg and is read by the factory. That is the case the brief says to report, not route around. The leg is also right on the merits: a shipped drift-audit descriptor naming `tools/drift-audit/...` names nothing at an adopter installed at another prefix. Fixing this needs either token resolution of `home` in the factory (unit 13's per §3, or unit 51 S32 widened) or homes outside the tool root. §3's 'no population moves' and §4 Drift both need restating for that.

The drift-audit rows' `surfaces = ["file:tools/drift-audit/..."]` (lines 212 and 220) and their `--home` argv follow whichever answer (2) gets.

Nothing was written; the tree is clean at base. `--brief` reported the brief already recorded and unchanged.

## Summary

No commit: this is a divergence report. The spec can't be built as written. Its S10 step argv (`{gov}/memory-tree/convert_registry.py`) and four `[[ledger]]` homes under `tools/` keep the §7 leg `install-prefix (shipped surface)` red. That leg takes no waiver, and the landed step runner and ledger factory leave no spelling that passes it.

Feasibility checks I ran (reading code and the pass-1 log only; I ran no gate, suite or self-test):

1. **S12 / AC14** – can be built. The transitional read is at `read_contract_rows` in `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/memory-tree/gen_build_index.py` (`import convert_registry` / `read_legacy_rows`, about lines 2639-2645). Its fixture arm is "a legacy home reads through the transitional read" (about line 6611). Once the read is deleted, a home with no header should raise `Problem` from the `parse_header` ValueError.

2. **verdict epoch** – deleting S12's read removes the only importer of `convert_registry.py`. No other file under `tools/` imports it, so this red clears on its own. Adding it to DELEGATES in `check-verdict-epoch.sh` would list a module no delegate imports.

3. **install-prefix** – the divergence, in two parts:
   - The `{gov}/memory-tree/...` argv appears 6 times in the codebase-map kit.toml, 6 in the drift-audit kit.toml and 21 in the memory-tree kit.toml. `{prefix}/` passes the gate, but `run_step_isolated` runs at cwd `gov_root` and resolves `{prefix}` to the target's relative prefix, so the program isn't found at other prefixes.
   - The four homes are drift-audit kit.toml lines 193 and 203 and govkit `registry.toml` lines 2460 and 2470. `read_registrations` reads homes literally.
   - These can be fixed in code without touching the spec: the `convert_registry.py` table strings and `TOOLS / "govkit"` (lines 197-222 and 353), `tools/drift-audit/selftest.py` lines 395-398, and the `lib/` sourcing at lines 223-226 of `tools/check-dead-paths.sh`.
   - The carried unit-14 seed at memory-tree kit.toml line 719 stays until unit 51.

4. **dead-path carriers** – can be fixed:
   - Waiver rows naming TOOL-dWitnessedBar-51 S5 for the `.gitattributes` lines 260-261, AGENTS.md, `.governance/instructions.toml`, WIRE-INTO-PROJECT.md, the gotcha record, the codebase-map dossier, `test_codebase_map(.template).py` and the `check-spec-tokens.test.sh` fixture.
   - Repoint `tools/codebase-map/selftest.py` line 1607.
   - The codebase-map kit.toml `[[upgrade]]` lines naming `memory/map/*.toml` depend on how S10 is revised.

5. **shell hygiene and lexicon** – can be fixed. Shell hygiene: `<<<` loops in `check-dead-paths.sh` and `fork-count.sh`, plus count drops (check-memory-hygiene.sh 8 to 7, check-method-carriers.sh 2 to 1). Lexicon: pin 1410 against 1418.

Owed to the close regardless: the two `New arm:` lines (`tools/drift-audit/selftest.py` for AC7 and AC8, `tools/memory-tree/ratchet.py` for AC12), each to be observed RED then GREEN, and AC14 after S12's pass.

Not done because nothing was committed: the `gotchas.py --for-diff` checklist, `positional.py` and `writing_practice.py`.

No command hit its time limit.
