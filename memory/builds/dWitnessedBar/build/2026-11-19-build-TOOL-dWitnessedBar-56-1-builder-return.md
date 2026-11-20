**Serves:** journal TOOL-dWitnessedBar-56

# TOOL-dWitnessedBar-56 — builder return 1 (run `wf_09adf362-e3e`), committed 2d0df6a24

## Why

TOOL-dWitnessedBar-56 is built from spec rev-5 and committed in two commits. 746c0416f is the pass commit: it sets the spec to CLOSED, adds the acceptance ledger and includes the index generator's rewrites. 2d0df6a24 is a portability fix that the bug-class checklist turned up. Every claim the spec makes about current code held: all nine pinned blobs matched HEAD, and every cited symbol and behaviour was there. There was no divergence.

## Summary

Built TOOL-dWitnessedBar-56 in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3, from base 01e95d21f.

**Commits**
- 746c0416f is the pass commit. It sets the spec status to CLOSED, adds the acceptance ledger memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-56-1-acceptance-ledger.md, re-stamps the kickoff manifest at the base, and includes the rewrites from `gen_build_index --write` and `gen_map --write` (memory/map/generated/symbols.json).
- 2d0df6a24 is a follow-up fix from the bug-class checklist. The hook suite's `seledit` plant used `sed -i` with `\t`, which only works on GNU sed; it now uses the suite's awk-and-move idiom. This commit also carries `Pass: TOOL-dWitnessedBar-56`, but it lands after the spec was CLOSED. If the pass-order leg objects to that, the trailer should have been `Pass: none`.

**What changed**
- **Selection (S1, S3):** in tools/run-gates/run-gates.sh, each accepted selection row is written as `selection.<n>` with its TABs kept. Only accepted rows are hashed, using the field rule of `verdict_flow.py`'s `read_selection`. Every other row is counted in a new `selection_ignored` key. In .githooks/pre-push, `read_bar_file` now reads `selection.<n>` byte for byte, and `check_tree_selection` rebuilds each row as `held<TAB>` plus that value.
- **Knob clears (S9):** the hook now clears `GATE_BASE_FROM` and `GATE_SELECTION` for every bar, including a stub.
- **`base_from` (S10):** the run header's `base_from` row gets a third field `inherited`, and the decline line names that row.
- **Tail sweep (S13, S14):** the sweep removes `tail.*` staging temps older than `TAIL_GRACE_S` and keeps fresh ones. The tail sweep and the per-tree verdict prune each carry a comment naming the reuse cache's 30-day `cut` as the seam considered and rejected.
- **Local-hook reader (S7, S8):** in tools/run-gates/verdict_backends.py, `read_local_verdict` now goes through a new `check_local_record`. It copies the hook's reuse-pair and selection checks, and runs `select --check` at the landed revision through a new `read_landed_revision`. It adds seven local-hook plants (`reused-cache`, `reused-alone`, `no-pair`, `no-selection`, `edited-selection`, `underived-selection`, `clean`). The `local-green` plant's records now carry the reuse pair and `selection none`.
- **Peer read (S15):** a bad signature (`Signature verification failed`) now reads `NONE` instead of `DEAD PROBE`. New plants: `peer-tip-missing`, `peer-no-ssh-keygen`, `peer-bad-signature`.
- **Keep (S12):** tools/run-gates/keep_tails.py now escapes C0 control bytes (CR included) and DEL as `\xHH`, then re-cuts the text to `TAIL_BYTES`. It has a new `controls` self-test case.
- **Test arms:** in .githooks/pre-push.test.sh, the plants are in TAB form, a new `dot` case covers a ` · ` inside a note, two parity arms compare the hook's decision with `read --backend local-hook`, an AC7 knob-clear arm was added, and the reason lines for both knobs were reworded. The evidence suite has new arms for AC1, AC2, AC8 and AC11, and unit 41's AC1 arm moved to the TAB form. The gov suite's plant loop has the ten new plants.
- **Floors (S19), raised by reading the arms:**
  - run-gates evidence: 302 to 309
  - run-gates gov canary: 21 to 35
  - run-gates adopter e2e: 17 to 23
  - memory-hygiene self-test: 789 to 796
  - unattended: 3408 to 3410, with `FLOOR_SHARD_3` 469 to 471
- **Docs (S20):** tools/run-gates/README.md (selection paragraph, record keys, `base_from`, tail temps, migration note, local-hook table row, peer states) and help/verdict-backends.md.

**Checks that ran (no gate, suite or `--selftest` flag ran)**
- **Runner over a scratch clone** under `%TEMP%`, standing in for the `run-gates evidence` arms (AC1, AC2, AC8, AC11): `selection.1` had 4 fields, the hash matched the LF canonical text, the LF twin gave the same hash, and `selection_ignored` read 2. The `base_from` row read `GATE_BASE…` then `inherited`. The sweep removed the 3 aged temps and kept the fresh one.
- **`verdict_backends.py --fixture --plant`** for all seven local-hook plants, `local-green` and five peer plants, standing in for the `run-gates gov canary` loop (AC6, AC13, AC14). Every scenario held.
- **The keep run in process** over a scratch repo (`run_keep` plus `check_controls_case`), standing in for the keep's `--selftest` (AC10). It reported no failures.
- **The hook's `read_bar_file` sourced alone**, standing in for `pre-push self-test`: a row's TABs were kept, including an empty last field's.
- **`guard.py --fixture --plant signers-owner-only`** (AC16) held.
- **Greps** for AC3, AC12, AC15 and AC18 all returned what the criteria expect.
- `bash -n` and `ast.parse` on every edited script; the naming lexicon passed all four new function names.

**Owed at the close**
- All of spec section 7 runs at the close.
- RED-first observation of the five `New arm:` lines: the hook suite's TAB plants, ` · ` case, parity and knob-clear arms; the evidence suite's selection, `base_from` and temp arms; the gov suite's ten plants; the verdict backends' plants; and the keep's `controls` case.
- AC1's hook adoption, AC5, AC7 and AC9 are observable only by suites.
- AC14's staged red (the principal read from standard output).
- AC17's executed counts against the raised floors.
- AC4 is not observed here; `TOOL-dWitnessedBar-58` observes it.

**Things to know**
- **Dispatch timed out:** `--dispatch --writes memory/map/generated/symbols.json` hit its 110 s bound and recorded no row. It was not re-run. Before timing out, it said that path is a generated output `--check-commit` accepts undeclared, so the file was committed. (DERIVED from the builder's probe)
- **`base_from` value bug, not fixed:** this predates the unit. Under `GATE_BASE`, the row's second field reads `GATE_BASE` immediately followed by the base sha. S10 only adds the third field, so I left it; the commit's `Decided:` line records this.
- **Branches no arm reaches:** in `check_local_record`, the `DEAD PROBE` cases (a landed revision that does not derive, a `select --check` that cannot run, a failed `hash-object`) are not reached by any arm. The spec names no plant for them.
- **Files I did not touch:** help/reference/drive.md and help/reference/units.md were already dirty before this pass and differ only in line endings; I left them unstaged.
