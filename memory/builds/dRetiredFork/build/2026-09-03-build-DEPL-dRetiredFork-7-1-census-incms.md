# Census — inCMS (C:/projects/incms/main)

**Serves:** journal DEPL-dRetiredFork-7

- adopter: `C:/projects/incms/main`
- gov index: 25837 objects with a path label, 1406 blobs at HEAD
- register: `.governance/install.json`, gov_commit `14e21399f7dd0559224837a2754fcbf9fc4a754b`
- mapped: 95 files
- IN-SYNC: 36
- DRIFT: 11
- FORK: 47
- UNMAPPED: 1

- carve-out tags: 0 distinct sites across scripts/,.claude/,.githooks/

## Declared in the receipt, absent from the second register

- `.claude/SESSION-KICKOFF.md` — FORK, role `seed`

## In NO register at all, but named like a gov file (7)

Neither register mentions these. The class is this census's own verdict.

- `.claude/skills/session-kickoff/SKILL.md` — FORK
- `scripts/corpus-path-unresolved.txt` — FORK
- `scripts/curation-debt.txt` — FORK
- `scripts/gate-legs.json` — FORK
- `scripts/legacy-files.txt` — FORK
- `scripts/memory-reorg/rekey/README.md` — FORK
- `scripts/unarmed-branches.txt` — FORK

## UNDECLARED FORK — in no gov commit ever (47)

- `.claude/SESSION-KICKOFF.md` — role `seed`, kit `kickoff-manifest`, gov `skills/session-kickoff/MANIFEST-TEMPLATE.md`
- `.claude/hooks/agent-cap.js` — role `engine`, kit `agent-cap`, gov `tools/hooks/agent-cap.js`
- `.claude/hooks/agent-cap.test.sh` — role `engine`, kit `agent-cap`, gov `tools/hooks/agent-cap.test.sh`
- `.claude/skills/drift-audit/SKILL.md` — role `rendered`, kit `drift-audit`, gov `tools/drift-audit/SKILL.template.md`
- `.claude/skills/memory-recall/SKILL.md` — role `rendered`, kit `memory-recall`, gov `tools/memory-recall/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md` — role `rendered`, kit `unattended`, gov `tools/unattended/SKILL.template.md`
- `.githooks/pre-push` — role `engine`, kit `push-main`, gov `.githooks/pre-push`
- `memory/HYGIENE.md` — role `rendered`, kit `memory-tree`, gov `tools/memory-tree/HYGIENE.template.md`
- `memory/TEMPLATE-SPEC.md` — role `rendered`, kit `memory-tree`, gov `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/guides/BUILD-METHOD.md` — role `rendered`, kit `memory-tree`, gov `tools/memory-tree/BUILD-METHOD.template.md`
- `scripts/check-arms.py` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/check-arms.py`
- `scripts/check-wiring.sh` — role `engine`, kit `check-wiring`, gov `tools/check-wiring.sh`
- `scripts/check-wiring.test.sh` — role `engine`, kit `check-wiring`, gov `tools/check-wiring.test.sh`
- `scripts/codebase-map/map_extractors.py` — role `seed`, kit `codebase-map`, gov `tools/codebase-map/map_extractors.template.py`
- `scripts/codebase-map/map_extractors.py` — role `project-owned`, kit `codebase-map`, gov `tools/codebase-map/map_extractors.py`
- `scripts/codebase-map/selftest.py` — role `engine`, kit `codebase-map`, gov `tools/codebase-map/selftest.py`
- `scripts/corpus_ids.py` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/corpus_ids.py`
- `scripts/drift-audit/drift_signals.py` — role `seed`, kit `drift-audit`, gov `tools/drift-audit/drift_signals.template.py`
- `scripts/drift-audit/drift_signals.py` — role `project-owned`, kit `drift-audit`, gov `tools/drift-audit/drift_signals.py`
- `scripts/gen_build_index.py` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/gen_build_index.py`
- `scripts/gotchas.py` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/gotchas.py`
- `scripts/hygiene-parity.test.sh` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/hygiene-parity.test.sh`
- `scripts/merge-rows.py` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/merge-rows.py`
- `scripts/merge-rows.test.sh` — role `engine`, kit `memory-tree`, gov `tools/memory-tree/merge-rows.test.sh`
- `scripts/push-main.sh` — role `engine`, kit `push-main`, gov `tools/push-main.sh`
- `scripts/push-main.test.sh` — role `engine`, kit `push-main`, gov `tools/push-main.test.sh`
- `scripts/recall/README.md` — role `engine`, kit `memory-recall`, gov `tools/memory-recall/README.md`
- `scripts/recall/extract.py` — role `forked`, kit `memory-recall`, gov `tools/memory-recall/extract.py`
- `scripts/recall/query.py` — role `forked`, kit `memory-recall`, gov `tools/memory-recall/query.py`
- `scripts/recall/selftest.py` — role `engine`, kit `memory-recall`, gov `tools/memory-recall/selftest.py`
- `scripts/unattended/.unattended.conf.example` — role `engine`, kit `unattended`, gov `tools/unattended/.unattended.conf.example`
- `scripts/unattended/adopt-unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/adopt-unattended.sh`
- `scripts/unattended/adopt-unattended.test.sh` — role `engine`, kit `unattended`, gov `tools/unattended/adopt-unattended.test.sh`
- `scripts/unattended/check-playbook.test.sh` — role `engine`, kit `unattended`, gov `tools/unattended/check-playbook.test.sh`
- `scripts/unattended/check-unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/check-unattended.sh`
- `scripts/unattended/check-unattended.test.sh` — role `engine`, kit `unattended`, gov `tools/unattended/check-unattended.test.sh`
- `scripts/unattended/cross-component.test.sh` — role `engine`, kit `unattended`, gov `tools/unattended/cross-component.test.sh`
- `scripts/unattended/lib-unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/lib-unattended.sh`
- `scripts/unattended/playbook.fixture.md` — role `engine`, kit `unattended`, gov `tools/unattended/playbook.fixture.md`
- `scripts/unattended/run-unattended-gates.sh` — role `engine`, kit `unattended`, gov `tools/unattended/run-unattended-gates.sh`
- `scripts/unattended/unattended.sh` — role `engine`, kit `unattended`, gov `tools/unattended/unattended.sh`
- `scripts/unattended/unattended.test.sh` — role `engine`, kit `unattended`, gov `tools/unattended/unattended.test.sh`
- `scripts/workflows/check-review-join.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/check-review-join.sh`
- `scripts/workflows/check-review-join.test.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/check-review-join.test.sh`
- `scripts/workflows/check-verifier-fanout.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/check-verifier-fanout.sh`
- `scripts/workflows/check-verifier-fanout.test.sh` — role `engine`, kit `review-harness`, gov `tools/workflows/check-verifier-fanout.test.sh`
- `scripts/workflows/check-workflow-syntax.js` — role `engine`, kit `review-harness`, gov `tools/workflows/check-workflow-syntax.js`

## DRIFT — a gov vintage, not gov's HEAD (11)

- `memory/guides/PLAYBOOK-TEMPLATE.md` — role `rendered`, kit `unattended`, gov `tools/unattended/PLAYBOOK-TEMPLATE.template.md` — gov's label for this blob is memory/guides/PLAYBOOK-TEMPLATE.md
- `memory/guides/UNATTENDED-PROTOCOL.md` — role `rendered`, kit `unattended`, gov `tools/unattended/PROTOCOL.template.md` — gov's label for this blob is memory/guides/UNATTENDED-PROTOCOL.md
- `scripts/codebase-map/map_lib.py` — role `engine`, kit `codebase-map`, gov `tools/codebase-map/map_lib.py`
- `scripts/drift-audit/README.md` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/README.md`
- `scripts/drift-audit/drift_report.py` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/drift_report.py`
- `scripts/drift-audit/drift_signals.template.py` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/drift_signals.template.py`
- `scripts/drift-audit/selftest.py` — role `engine`, kit `drift-audit`, gov `tools/drift-audit/selftest.py`
- `scripts/manifest-check.sh` — role `engine`, kit `kickoff-manifest`, gov `skills/session-kickoff/manifest-check.sh`
- `scripts/unattended/PLAYBOOK-TEMPLATE.template.md` — role `engine`, kit `unattended`, gov `tools/unattended/PLAYBOOK-TEMPLATE.template.md` — gov's label for this blob is memory/guides/PLAYBOOK-TEMPLATE.md
- `scripts/unattended/PROTOCOL.template.md` — role `engine`, kit `unattended`, gov `tools/unattended/PROTOCOL.template.md` — gov's label for this blob is memory/guides/UNATTENDED-PROTOCOL.md
- `scripts/unattended/SKILL.template.md` — role `engine`, kit `unattended`, gov `tools/unattended/SKILL.template.md`

## UNMAPPED — no gov path derivable (1)

- `.gitattributes` — role `attributes`, kit `(govkit)`

## UNDECLARED FORK, still declared `engine` (11)

kits.json calls each of these gov's bytes. None is in any gov commit, ever.

- `.claude/hooks/recall-opened.js` — kit `memory-recall` — not in install.json at all
- `.claude/hooks/recall-opened.test.sh` — kit `memory-recall` — not in install.json at all
- `scripts/check-arms.py` — kit `memory-tree`
- `scripts/gotchas.py` — kit `memory-tree`
- `scripts/recall/extract.py` — kit `memory-recall`
- `scripts/unattended/.unattended.conf.example` — kit `unattended`
- `scripts/unattended/adopt-unattended.sh` — kit `unattended`
- `scripts/unattended/cross-component.test.sh` — kit `unattended`
- `scripts/unattended/fixture-records/scripts~unattended~fixture-pieces~one~piece.md.md` — kit `unattended` — not in install.json at all
- `scripts/unattended/fixture-records/scripts~unattended~fixture-pieces~two~piece.md.md` — kit `unattended` — not in install.json at all
- `scripts/workflows/check-verifier-fanout.test.sh` — kit `review-harness`

## The adopter's two registers disagree (30 paths)

- `.claude/hooks/agent-cap.js` — kits.json `diverged`, install.json `engine`
- `.claude/hooks/agent-cap.test.sh` — kits.json `diverged`, install.json `engine`
- `.githooks/pre-push` — kits.json `project-owned`, install.json `engine`
- `scripts/check-wiring.sh` — kits.json `diverged`, install.json `engine`
- `scripts/check-wiring.test.sh` — kits.json `diverged`, install.json `engine`
- `scripts/codebase-map/selftest.py` — kits.json `diverged`, install.json `engine`
- `scripts/corpus_ids.py` — kits.json `project-owned`, install.json `engine`
- `scripts/gen_build_index.py` — kits.json `diverged`, install.json `engine`
- `scripts/hygiene-parity.test.sh` — kits.json `project-owned`, install.json `engine`
- `scripts/merge-rows.py` — kits.json `project-owned`, install.json `engine`
- `scripts/merge-rows.test.sh` — kits.json `project-owned`, install.json `engine`
- `scripts/push-main.sh` — kits.json `diverged`, install.json `engine`
- `scripts/push-main.test.sh` — kits.json `diverged`, install.json `engine`
- `scripts/recall/README.md` — kits.json `project-owned`, install.json `engine`
- `scripts/recall/extract.py` — kits.json `engine`, install.json `forked`
- `scripts/recall/query.py` — kits.json `project-owned`, install.json `forked`
- `scripts/recall/selftest.py` — kits.json `project-owned`, install.json `engine`
- `scripts/unattended/adopt-unattended.test.sh` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/check-playbook.test.sh` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/check-unattended.sh` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/check-unattended.test.sh` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/lib-unattended.sh` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/playbook.fixture.md` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/run-unattended-gates.sh` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/unattended.sh` — kits.json `diverged`, install.json `engine`
- `scripts/unattended/unattended.test.sh` — kits.json `diverged`, install.json `engine`
- `scripts/workflows/check-review-join.sh` — kits.json `diverged`, install.json `engine`
- `scripts/workflows/check-review-join.test.sh` — kits.json `diverged`, install.json `engine`
- `scripts/workflows/check-verifier-fanout.sh` — kits.json `diverged`, install.json `engine`
- `scripts/workflows/check-workflow-syntax.js` — kits.json `diverged`, install.json `engine`

## PROFILE — `scripts/gen_build_index.py` against gov `tools/memory-tree/gen_build_index.py`

- census class: FORK
- kits.json role: diverged
- gov `tools/memory-tree/gen_build_index.py`: 2785 lines, 63 top-level symbols
- adopter `scripts/gen_build_index.py`: 518 lines, 14 top-level symbols
- shared top-level names: 3 — `_fixture`, `collect`, `main`

## IN-SYNC (36)

Named only in aggregate: a file identical to gov HEAD is the uninteresting case, and
listing all of them would bury the 59 that are not.

## RECOMMENDATION handed to inCMS — `scripts/gen_build_index.py`

*This section is a RECOMMENDATION, not an edit. The row lives in inCMS's own `kits.json` and gov
owns none of it; this census records the measurement and hands the disposition to the adopter.*

> `scripts/gen_build_index.py` is declared `diverged` — a fork of gov's
> `tools/memory-tree/gen_build_index.py`. The measurement does not support that reading. gov's file
> is 2785 lines carrying 63 top-level symbols; inCMS's is 518 lines carrying 14, and the two share
> exactly three names, all of them generic: `_fixture`, `collect`, `main`. That is not a fork that
> drifted. It is a second program that was written to do a similar job under the same filename.
>
> **Recommendation: reclassify the row `project-owned`.** Two things follow, and the second is why
> this is worth doing rather than leaving alone. A `diverged` row asserts a convergence debt that
> nobody is ever going to pay, so it will sit in every retirement report forever as work that is
> permanently outstanding. And its 2764-line diff is counted into every metric computed over that
> registry, which inflates the divergence figure the whole programme is sized against — one row
> dominating a number meant to describe fourteen kits.
>
> inCMS already carries the precedent: `kits.json` has an `owned_why` block, and its existing entry
> for `scripts/recall/selftest.py` makes exactly this argument — "two independently-written programs
> sharing a filename, not a fork" — with the same kind of symbol evidence. This row wants the same
> treatment and the same block.

**Status: RECORDED, not applied.** Nothing in inCMS was edited by this unit.
