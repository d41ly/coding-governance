# Census — NicoCares (C:/projects/nicocares/main)

**Serves:** journal DEPL-dRetiredFork-7

- adopter: `C:/projects/nicocares/main`
- gov index: 25837 objects with a path label, 1406 blobs at HEAD
- register: `.governance/install.json`, gov_commit `14e21399f7dd0559224837a2754fcbf9fc4a754b`
- mapped: 160 files
- IN-SYNC: 85
- DRIFT: 43
- FORK: 31
- UNMAPPED: 1

- carve-out tags: 23 distinct sites across scripts/,.claude/hooks/,.claude/workflows/,.githooks/,tools/unattended/

## Declared in the receipt, absent from the second register

- `.claude/SESSION-KICKOFF.md` — FORK, role `seed`
- `.claude/hooks/scratch-guard.js` — DRIFT, role `engine`
- `.claude/skills/drift-audit/SKILL.md` — FORK, role `rendered`
- `.claude/skills/memory-recall/SKILL.md` — FORK, role `rendered`
- `.claude/skills/unattended/SKILL.md` — FORK, role `rendered`
- `CLAUDE.md` — FORK, role `seed`
- `memory/HYGIENE.md` — FORK, role `rendered`
- `memory/TEMPLATE-SPEC.md` — FORK, role `rendered`
- `memory/guides/BUILD-METHOD.md` — FORK, role `rendered`
- `memory/guides/PLAYBOOK-TEMPLATE.md` — DRIFT, role `rendered`
- `memory/guides/REVIEW-PROTOCOL.md` — FORK, role `rendered`
- `memory/guides/UNATTENDED-PROTOCOL.md` — DRIFT, role `rendered`
- `scripts/.memory-tree.conf.example` — DRIFT, role `engine`
- `scripts/BUILD-METHOD.template.md` — DRIFT, role `engine`
- `scripts/README.md` — FORK, role `engine`
- `scripts/REVIEW-PROTOCOL.template.md` — DRIFT, role `engine`
- `scripts/SPEC-TEMPLATE.template.md` — DRIFT, role `engine`
- `scripts/check-install-prefix.sh` — DRIFT, role `engine`
- `scripts/check-method-carriers.sh` — DRIFT, role `engine`
- `scripts/check-review-join.test.sh` — DRIFT, role `engine`
- `scripts/codebase-map/map_extractors.py` — FORK, role `project-owned`
- `scripts/codebase-map/map_lib.py` — DRIFT, role `engine`
- `scripts/codebase-map/reuse_lookup.py` — DRIFT, role `engine`
- `scripts/codebase-map/selftest.py` — DRIFT, role `engine`
- `scripts/drift-audit/README.md` — DRIFT, role `engine`
- `scripts/drift-audit/adopt-drift-audit.sh` — DRIFT, role `engine`
- `scripts/drift-audit/drift_report.py` — DRIFT, role `engine`
- `scripts/drift-audit/drift_signals.py` — FORK, role `project-owned`
- `scripts/drift-audit/drift_signals.template.py` — DRIFT, role `engine`
- `scripts/drift-audit/kit.toml` — DRIFT, role `engine`
- `scripts/drift-audit/selftest.py` — DRIFT, role `engine`
- `scripts/hooks/README.md` — DRIFT, role `engine`
- `scripts/hooks/scratch-guard.js` — DRIFT, role `engine`
- `scripts/hooks/scratch-guard.test.sh` — DRIFT, role `engine`
- `scripts/install-prefix-carried.txt` — DRIFT, role `generated`
- `scripts/manifest-check.sh` — DRIFT, role `engine`
- `scripts/memory-recall/README.md` — DRIFT, role `engine`
- `scripts/memory-recall/extract.py` — DRIFT, role `forked`
- `scripts/memory-recall/recall_conf.py` — DRIFT, role `engine`
- `scripts/playbook/playbook.kit.toml` — DRIFT, role `engine`
- `scripts/playbook/registry.toml` — DRIFT, role `engine`
- `scripts/playbook/render_playbook.py` — DRIFT, role `engine`
- `tools/unattended/.unattended.conf.example` — DRIFT, role `engine`
- `tools/unattended/PLAYBOOK-TEMPLATE.template.md` — DRIFT, role `engine`
- `tools/unattended/PROTOCOL.template.md` — DRIFT, role `engine`
- `tools/unattended/SKILL.template.md` — DRIFT, role `engine`
- `tools/unattended/adopt-unattended.sh` — DRIFT, role `engine`
- `tools/unattended/check-playbook.sh` — DRIFT, role `engine`
- `tools/unattended/check-unattended.sh` — DRIFT, role `engine`
- `tools/unattended/check-unattended.test.sh` — DRIFT, role `engine`
- `tools/unattended/kit.toml` — DRIFT, role `engine`
- `tools/unattended/lib-unattended.sh` — DRIFT, role `engine`
- `tools/unattended/run-unattended-gates.sh` — DRIFT, role `engine`
- `tools/unattended/unattended.test.sh` — DRIFT, role `engine`

## In NO register at all, but named like a gov file (11)

Neither register mentions these. The class is this census's own verdict.

- `.githooks/README.md` — FORK
- `.githooks/pre-commit` — FORK
- `.githooks/pre-push.test.sh` — IN-SYNC
- `scripts/check-kit-versions.sh` — DRIFT
- `scripts/check-placeholders.sh` — DRIFT
- `scripts/check-placeholders.test.sh` — DRIFT
- `scripts/check-wiring.sh` — FORK
- `scripts/gate-legs.json` — FORK
- `scripts/manifest-check.test.sh` — DRIFT
- `scripts/push-main.sh` — DRIFT
- `scripts/push-main.test.sh` — DRIFT

## UNDECLARED FORK — in no gov commit ever (31)

- `.claude/SESSION-KICKOFF.md` — role `seed`, kit `kickoff-manifest`, gov `skills/session-kickoff/MANIFEST-TEMPLATE.md`
- `.claude/hooks/agent-cap.js` — role `engine`, kit `agent-cap`, gov `tools/hooks/agent-cap.js`
- `.claude/skills/drift-audit/SKILL.md` — role `rendered`, kit `drift-audit`, gov `tools/drift-audit/SKILL.template.md`
- `.claude/skills/memory-recall/SKILL.md` — role `rendered`, kit `memory-recall`, gov `tools/memory-recall/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md` — role `rendered`, kit `unattended`, gov `tools/unattended/SKILL.template.md`
- `CLAUDE.md` — role `seed`, kit `playbook`, gov `coding-governance-agents.template.md`
- `memory/HYGIENE.md` — role `rendered`, kit `memory-tree`, gov `tools/memory-tree/HYGIENE.template.md`
- `memory/TEMPLATE-SPEC.md` — role `rendered`, kit `memory-tree`, gov `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/guides/BUILD-METHOD.md` — role `rendered`, kit `memory-tree`, gov `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/REVIEW-PROTOCOL.md` — role `rendered`, kit `review-harness`, gov `tools/workflows/REVIEW-PROTOCOL.template.md`
- `scripts/HYGIENE.template.md` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/HYGIENE.template.md`
- `scripts/README.md` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/README.md`
- `scripts/check-memory-hygiene.sh` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/check-memory-hygiene.sh`
- `scripts/check-memory-hygiene.test.sh` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/check-memory-hygiene.test.sh`
- `scripts/check-review-join.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/check-review-join.sh`
- `scripts/check-verifier-fanout.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/check-verifier-fanout.sh`
- `scripts/check-workflow-syntax.js` — role `engine`, kit `review-harness`, gov `tools/workflows/check-workflow-syntax.js`
- `scripts/codebase-map/map_extractors.py` — role `seed`, kit `codebase-map`, gov `tools/codebase-map/map_extractors.template.py`
- `scripts/codebase-map/map_extractors.py` — role `project-owned`, kit `codebase-map`, gov `tools/codebase-map/map_extractors.py`
- `scripts/corpus_ids.py` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/corpus_ids.py`
- `scripts/drift-audit-code.js` — role `engine`, kit `review-harness`, gov `tools/workflows/drift-audit-code.js`
- `scripts/drift-audit-state.js` — role `engine`, kit `review-harness`, gov `tools/workflows/drift-audit-state.js`
- `scripts/drift-audit/drift_signals.py` — role `seed`, kit `drift-audit`, gov `tools/drift-audit/drift_signals.template.py`
- `scripts/drift-audit/drift_signals.py` — role `project-owned`, kit `drift-audit`, gov `tools/drift-audit/drift_signals.py`
- `scripts/gen_build_index.py` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/gen_build_index.py`
- `scripts/hooks/agent-cap.js` — role `engine`, kit `agent-cap`, gov `tools/hooks/agent-cap.js`
- `scripts/hooks/agent-cap.test.sh` — role `engine`, kit `agent-cap`, gov `tools/hooks/agent-cap.test.sh`
- `scripts/memory-recall/selftest.py` — role `engine`, kit `memory-recall`, gov `tools/memory-recall/selftest.py`
- `scripts/tier2-review.js` — role `engine`, kit `review-harness`, gov `tools/workflows/tier2-review.js`
- `scripts/tier2-review.test.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/tier2-review.test.sh`
- `tools/unattended/unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/unattended.sh`

## DRIFT — a gov vintage, not gov's HEAD (43)

- `.claude/hooks/scratch-guard.js` — role `engine`, kit `agent-cap`, gov `tools/hooks/scratch-guard.js` — gov's label for this blob is .claude/hooks/scratch-guard.js
- `memory/guides/PLAYBOOK-TEMPLATE.md` — role `rendered`, kit `unattended`, gov `tools/unattended/PLAYBOOK-TEMPLATE.template.md` — gov's label for this blob is memory/guides/PLAYBOOK-TEMPLATE.md
- `memory/guides/UNATTENDED-PROTOCOL.md` — role `rendered`, kit `unattended`, gov `tools/unattended/PROTOCOL.template.md` — gov's label for this blob is memory/guides/UNATTENDED-PROTOCOL.md
- `scripts/.memory-tree.conf.example` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/.memory-tree.conf.example`
- `scripts/BUILD-METHOD.template.md` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/BUILD-METHOD.template.md`
- `scripts/REVIEW-PROTOCOL.template.md` — role `engine`, kit `review-harness`, gov `tools/workflows/REVIEW-PROTOCOL.template.md`
- `scripts/SPEC-TEMPLATE.template.md` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `scripts/check-install-prefix.sh` — role `engine`, kit `check-install-prefix`, gov `tools/check-install-prefix.sh`
- `scripts/check-method-carriers.sh` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/check-method-carriers.sh`
- `scripts/check-review-join.test.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/check-review-join.test.sh`
- `scripts/codebase-map/map_lib.py` — role `engine`, kit `codebase-map`, gov `tools/codebase-map/map_lib.py`
- `scripts/codebase-map/reuse_lookup.py` — role `engine`, kit `codebase-map`, gov `tools/codebase-map/reuse_lookup.py`
- `scripts/codebase-map/selftest.py` — role `engine`, kit `codebase-map`, gov `tools/codebase-map/selftest.py`
- `scripts/drift-audit/README.md` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/README.md`
- `scripts/drift-audit/adopt-drift-audit.sh` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/adopt-drift-audit.sh`
- `scripts/drift-audit/drift_report.py` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/drift_report.py`
- `scripts/drift-audit/drift_signals.template.py` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/drift_signals.template.py`
- `scripts/drift-audit/kit.toml` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/kit.toml`
- `scripts/drift-audit/selftest.py` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/selftest.py`
- `scripts/hooks/README.md` — role `engine`, kit `agent-cap`, gov `tools/hooks/README.md`
- `scripts/hooks/scratch-guard.js` — role `engine`, kit `agent-cap`, gov `tools/hooks/scratch-guard.js` — gov's label for this blob is .claude/hooks/scratch-guard.js
- `scripts/hooks/scratch-guard.test.sh` — role `engine`, kit `agent-cap`, gov `tools/hooks/scratch-guard.test.sh`
- `scripts/install-prefix-carried.txt` — role `generated`, kit `check-install-prefix`, gov `tools/install-prefix-carried.txt`
- `scripts/kit.toml` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/kit.toml` — gov's label for this blob is tools/workflows/kit.toml
- `scripts/manifest-check.sh` — role `engine`, kit `kickoff-manifest`, gov `skills/session-kickoff/manifest-check.sh`
- `scripts/memory-recall/README.md` — role `engine`, kit `memory-recall`, gov `tools/memory-recall/README.md`
- `scripts/memory-recall/extract.py` — role `forked`, kit `memory-recall`, gov `tools/memory-recall/extract.py`
- `scripts/memory-recall/recall_conf.py` — role `engine`, kit `memory-recall`, gov `tools/memory-recall/recall_conf.py`
- `scripts/playbook/playbook.kit.toml` — role `engine`, kit `playbook-render`, gov `tools/govkit/entries/playbook.kit.toml`
- `scripts/playbook/registry.toml` — role `engine`, kit `playbook-render`, gov `tools/govkit/registry.toml`
- `scripts/playbook/render_playbook.py` — role `engine`, kit `playbook-render`, gov `tools/playbook/render_playbook.py`
- `tools/unattended/.unattended.conf.example` — role `engine`, kit `unattended`, gov `tools/unattended/.unattended.conf.example`
- `tools/unattended/PLAYBOOK-TEMPLATE.template.md` — role `engine`, kit `unattended`, gov `tools/unattended/PLAYBOOK-TEMPLATE.template.md` — gov's label for this blob is memory/guides/PLAYBOOK-TEMPLATE.md
- `tools/unattended/PROTOCOL.template.md` — role `engine`, kit `unattended`, gov `tools/unattended/PROTOCOL.template.md` — gov's label for this blob is memory/guides/UNATTENDED-PROTOCOL.md
- `tools/unattended/SKILL.template.md` — role `engine`, kit `unattended`, gov `tools/unattended/SKILL.template.md`
- `tools/unattended/adopt-unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/adopt-unattended.sh`
- `tools/unattended/check-playbook.sh` — role `engine`, kit `unattended`, gov `tools/unattended/check-playbook.sh`
- `tools/unattended/check-unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh` — role `engine`, kit `unattended`, gov `tools/unattended/check-unattended.test.sh`
- `tools/unattended/kit.toml` — role `engine`, kit `unattended`, gov `tools/unattended/kit.toml`
- `tools/unattended/lib-unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/lib-unattended.sh`
- `tools/unattended/run-unattended-gates.sh` — role `engine`, kit `unattended`, gov `tools/unattended/run-unattended-gates.sh`
- `tools/unattended/unattended.test.sh` — role `engine`, kit `unattended`, gov `tools/unattended/unattended.test.sh`

## UNMAPPED — no gov path derivable (1)

- `.gitattributes` — role `attributes`, kit `(govkit)`

## IN-SYNC (85)

Named only in aggregate: a file identical to gov HEAD is the uninteresting case, and
listing all of them would bury the 75 that are not.
