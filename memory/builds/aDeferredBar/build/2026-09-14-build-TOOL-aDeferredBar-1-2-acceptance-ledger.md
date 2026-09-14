# The acceptance ledger — the instruction at five carriers

**Serves:** journal TOOL-aDeferredBar-1

Every line is OBSERVED or AMENDED, and every observation is the direct command the criterion names,
run by the build pass at rev-4 of the spec. No merge bar and no self-test suite was run for any of
them; the two leg scripts AC15 names were run by hand, once each, after the record set was staged.

**Evidences:** TOOL-aDeferredBar-1
- AC1 — `grep -c 'RUN NO MERGE BAR AND NO SELF-TEST SUITE' tools/workflows/unattended-unit.js` — `1`, and each of the four per-form greps (`not run-gates.sh in any form`, `GATE_(FULL|SELFTESTS)= prefix`, `not run-selftests.sh, not run-unattended-gates.sh`, `*.test.sh suite`) printed `1`.
- AC2 — `grep -c 'name it in .summary. and the main loop' tools/workflows/unattended-unit.js` — `1`; the `summary` rule and the hand-off sit on one source line.
- AC3 — `grep -c 'No stage of this program runs the merge bar or a self-test suite' tools/workflows/unattended-build.js` — `1`, inside `GROUND` and in no stage prompt.
- AC4 — `grep -c 'names a DIRECT observation with its command' tools/workflows/unattended-build.js` — `1`, inside the SPEC-stage writer prompt; the sentence names no gate.
- AC5 — `grep -c 'A pass runs no merge bar and no self-test suite' memory/guides/BUILD-METHOD.md` — `1`, and `grep -c 'diff-scoped' memory/guides/BUILD-METHOD.md` printed `0`.
- AC6 — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` — exit 0 at 26911 of 27648 bytes; the `sed` render of `tools/memory-tree/BUILD-METHOD.template.md` diffed empty against the live copy; `wc -l memory/guides/BUILD-METHOD.md` printed 343. The replacement stands as its own paragraph, which is the +1 byte and +2 lines over the rev-3 estimate.
- AC7 — `git grep -l 'gov:kit memory-tree@2.74' -- tools memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides` — printed nothing; the same over `2.75` printed nine paths.
- AC8 — `grep -c "version: '1.1', // gov:kit unattended-unit@1.1" tools/workflows/unattended-unit.js` — `1`, the build script's line likewise `1`, and `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-unit.js tools/workflows/unattended-build.js` exited 0 with both scripts parsed clean.
- AC9 — `bash tools/memory-tree/check-verdict-epoch.sh` — exit 0 at the build commit: the constant line and the bump are one commit, so W equals S.
- AC10 — `grep -c 'No merge bar and no self-test suite inside a pass' tools/unattended/SKILL.template.md` — `1`, the render `.claude/skills/unattended/SKILL.md` likewise `1`, and `bash tools/unattended/adopt-unattended.sh --check` reported in sync.
- AC11 — `git grep -l 'gov:kit unattended@1.19' -- tools/unattended .claude/skills/unattended memory/guides` — printed nothing; the same over `1.20` printed fifteen paths; `bash tools/check-kit-versions.sh` exited 0.
- AC12 — `grep -c 'inside a build pass run each meta-gate' memory/guides/SESSION-KICKOFF.md` — `1`, and `bash skills/session-kickoff/manifest-check.sh` exited 0. Its first run redded on C7, the 25600-byte file cap rev-3 did not price, at 25716 bytes; the duplicate traps bullet rev-4 names was deleted and the checker then passed at 25445.
- AC13 — `git log -1 --format=%B | grep -c 'manifest-audit: delta'` — `1` at the build commit; `last-audit` carries the `git merge-base origin/main HEAD` sha and `last-body-change` the sha of `HEAD~1`, each grep printing `1`.
- AC14 — `python tools/check-spec-tokens.py` — exit 0 over the tree carrying this spec, and `--list` resolved every §7 name against `tools/gate-legs.json`.
- AC15 — `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0 with the record set staged, and `bash tools/memory-tree/check-method-carriers.sh` exited 0; neither named `memory/guides/BUILD-METHOD.md` or `.claude/skills/unattended/SKILL.md`.
- AC16 — `grep -cP` over the backticked tokens of this spec's §6, through unit 2's `BAR` regex as typed there — `0`; the liveness command over `bash tools/run-gates/run-gates.sh` piped into the same regex printed `1`.
