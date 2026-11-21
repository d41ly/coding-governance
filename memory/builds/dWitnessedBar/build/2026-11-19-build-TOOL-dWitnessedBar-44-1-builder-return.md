**Serves:** journal TOOL-dWitnessedBar-44

# TOOL-dWitnessedBar-44 — builder return 1 (run `wf_d566f269-487`), committed acd04756e3efbb052507d628da0055ae44f992eb

## Why

TOOL-dWitnessedBar-44 is built to spec rev-4 and its spec status is now CLOSED in the same pass commit. The spec's claims about the code held when I checked them. The step row still reads `unlanded` (`upgrade_steps.py list`) and 930a5289d is on neither main nor origin/main, so the widening could go into inherited_red.py itself instead of shipping as a new step.

## Summary

Commit acd04756e (base c9b50206f) has the `Pass: TOOL-dWitnessedBar-44` trailer.

**The change:**
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/govkit/steps/inherited_red.py now reads `INHERITED_RED` from two files: `.githooks/gate-env.sh` and the file `.unattended.conf`'s `GATE_POLICY_FILE` names. A blank or absent key, or no conf, means the gate file is read once.
- `land` maps to `own-mixed-contended`. Every other non-blank value (`Park`, `LAND`, `bogus`) maps to `every-red`, and the old refusal of off-table values is gone.
- A `GATE_POLICY_FILE` that leaves the tree, by the driver's own case patterns, counts as `every-red` and is neither read nor edited.
- Where the two files disagree the stricter value is written. The existing conflict refusal applies to that value.
- `up` takes the key out of every file that held it, and `down` restores each file from the before-image.
- `witness` prints one line per file read (file, value found, value written; after an `up` it reads the found value from the before-image) and exits 0 only when neither file assigns the key.
- tools/govkit/selftest.py gains `check_inherited_red_step`, wired after `check_review_rounds_step`.
- help/upgrade-steps.md gains a section for the step: both files, the mapping table, the stricter-of-two rule, the conflict refusal, and the three verbs in a `run: no` fence.
- The commit also carries the acceptance ledger memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-44-1-acceptance-ledger.md, RUN.md, the regenerated symbols.json, and what `gen_build_index --write` rewrote.

**Changes the spec did not state** (both declared with `--dispatch`, each with a deviation record):
- Deviation 442: tools/govkit/usage.toml gains `[[usage]]` rows for `inherited_red.py#up`, `#witness` and `#down`. Without them the `docs` leg reds `UNROWED` on the section's fence. Fingerprints `7d308cd4`, `79b2b797` and `14a9242d` were computed with `docs_leg.derive_usage_fingerprint`, which reproduces review_rounds' existing anchors.
- Deviation 443: a `GATE_POLICY_FILE` that names `.governance/policy.toml` now refuses. One path cannot hold both the gate edit and the policy edit.
- I also declared `...-44-change-1.md` but did not write it.

**How I committed, and why:** in the shared worktree the pre-commit `codebase-map` leg reported `symbols.json` STALE. I confirmed this comes from unit 5's uncommitted code: a regenerate there adds only symbols from `run-gates.sh` and `verdict_flow.py`. So I:
1. Regenerated the map in a clean clone (`%TEMP%/m44`) at the base plus only this pass's files.
2. Exported the staged blobs into a second clean clone (`%TEMP%/c44`) and checked that `git write-tree` matched this worktree's index exactly.
3. Committed there through the same hooks path, with no `--no-verify`. Every hook passed; the hygiene hook re-rendered `memory/LIVE.md` back to HEAD's bytes, so LIVE.md is not in the commit.
4. Fast-forwarded this branch to that commit and reset the stale staged LIVE.md to HEAD.

Unit 5's working files were not touched, and both clones are deleted.

**Checks run here:**
- A scratch probe (C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe44.py) ran the step's verbs under `-I` over fixture repos in `%TEMP%/p44`. All 31 cases passed: AC1, AC2 (including off-tree `/etc/x`, `C:/x`, `../x`, `a/../b` and `..`), AC3 (two witness lines and a byte-for-byte `down`), the conflict, non-UTF-8, an absent named file, a converging re-run, and the gate file named twice. This stands in for the `govkit selftest` arm.
- The same probe against the step at c9b50206 failed on AC1, AC2 and AC3, so the probe can fail.
- AC4 by grep: `inherited_red.py` counts 4 and `GATE_POLICY_FILE` counts 2 on the new page, both 0 at base.
- I ran the naming lexicon `--suggest` on each new function name, and `gen_map --check`/`--write` only inside the clean clone.

**Owed to the main loop at the close:**
- Running `check_inherited_red_step` and its RED-first observation (staged break: restore the `.githooks/gate-env.sh`-only read).
- The §7 legs: `govkit selftest`, `govkit acceptance matrix`, `govkit refusal join` (one refusal site removed and one added, so the count should be unchanged against `BRANCH_PIN = 335`), `memory hygiene`, `recall floor arms`, `policy fixtures`, `step-rows-frozen`. (DERIVED from the builder's probe)
- The `docs` leg over the new anchors and usage rows.

**Gotchas checklist** (`gotchas.py --for-diff HEAD~1..HEAD`) ran over the commit and changed nothing:
- `line-claim-matched-over-the-whole-output`: the AC3 arm checks per line. AC1 matches `ops/gate-policy.sh` over the whole output, but only that file's own row can print the name.
- `pipe-in-a-code-span-splits-a-table-cell`: no `|` inside the new table's code spans.
- `ledger-token-wrapped-across-a-line-joins-nothing`: every ledger token sits on one line.
- `insert-after-a-key-that-occurs-twice`: the `usage.toml` anchor I inserted after was unique.
- `fixture-passes-by-finding-nothing`: the probe's red run shows the fixtures can fail.

No command timed out, and nothing was skipped.
