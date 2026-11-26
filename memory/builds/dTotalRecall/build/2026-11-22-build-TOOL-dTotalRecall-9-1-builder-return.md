**Serves:** journal TOOL-dTotalRecall-9
**Caused-by:** TOOL-dTotalRecall-9

# TOOL-dTotalRecall-9 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `e1321ce78` from [2026-11-22-prompt-TOOL-dTotalRecall-9-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-9-build-brief.md), recorded whole; the pass commits are `29b39e572` and `300ee1243`.

## Why

TOOL-dTotalRecall-9 is built from its spec at rev-7, which I did not change. I checked the spec against the code before writing anything: every symbol, path and flag it cites exists at the base, so there was no divergence to report. There are two commits, each with the trailer `Pass: TOOL-dTotalRecall-9`. The pass commit 29b39e57245237223e3ce27112cc73f6ef547c89 holds the code and records, and flips the spec header to CLOSED · 2026-11-23 with no other spec edit. Commit 300ee124303ef8683eb22e6faf34fd267dfed25b holds only `.governance/policy.json`, re-rendered with `policy.py mirror --write` from the catalogue the first commit landed. Spec section S10 asks for that second commit.

## Summary

Built and committed TOOL-dTotalRecall-9 in two commits: 29b39e572 (code, records, spec CLOSED) and 300ee1243 (the policy mirror). No gate, suite or bar ran; only the naming lexicon did. Every check below is a probe or fixture of the changed code. Results are in `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-9-1-acceptance-ledger.md`; choices the spec left open are in `memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-9-deviation-1006.md`.

**What was built**
- Five new tag namespaces (`record`, `section`, `feature`, `class`, `marker`). Their extractors are in `tools/playbook/record_extract.py` and their rows in `tools/playbook/namespaces.toml`.
- A `sections` column on the spec row of `tools/memory-tree/record-kinds.toml`, read by `read_sections` and checked by `check_sections` in `tools/memory-tree/record_kinds.py`. `cmd_new_spec` in `tools/memory-tree/gen_build_index.py` now refuses a new spec whose skeleton lacks a required section, before writing.
- `tools/memory-tree/record_find.py` holds the `find`, `show` and `budget` verbs, reached through `gov_record.py`. The search ranking moved there unchanged from `tools/memory-recall/query.py`, which imports it back. `check-recall.py` now grades through it, and both recall gate rows watch the new file (`tools/govkit/registry.toml`, regenerated `tools/gate-legs.json`).
- `<id>#<tag>` addresses now resolve in `edge_grammar.resolve_edge` and in `gov_tag.py show`, through the same section reader `record show` uses.
- `handoff.py render --read <key>` runs `gov_record.py budget` before rendering and writes a `reads:` list. A refusal exits 2 and writes no file.
- A `memory-slices` row in `tools/policy/caps.toml` (the first `exempt` row) and its test case in `check_policy.CAP_CASES`.
- The session card's `memory —` cell now reports the card's bytes and the auto-memory index's bytes, each against the budget (`memory_index.py --card-bytes`, wired in `manifest-check.sh`).
- Summary and usage lines for the four memory policy keys; those keys left `unsummarised-keys.txt`.
- Docs: `help/tags.md`, `help/size-caps.md`, the memory-tree and playbook READMEs. Also `SESSION-KICKOFF.md` `last-audit` re-stamped and the code map regenerated.

**What I verified (each stands in for the gate named after it)**
- **AC1** (`tags` resolver checks and the playbook render selftest): a probe of the live index counted record 51, section 109854, feature 0, class 174 and marker 3078. The 51 and 174 match the `git grep` counts the criterion names. `gov_tag.py show record.witness` printed that kind's registry row. A cold rebuild of the index took 1m43s, under the 420 s ceiling. (figures DERIVED, the builder's probes and timings)
- **AC2** (playbook render selftest): the new `gov_tag.py --fixture --plant memory-records` plant served the second of two repeated `## Findings` sections and keyed the record by its file stem. It also printed `tags: unarmed feature`.
- **AC3, AC4, AC5, AC7, AC8, AC9** (memory-hygiene self-test): all ten `record_find.py --fixture --plant` cases behaved as the criteria say. In this repo, `find --build dClosedLoop` printed 40 rows plus a total line, and `find --kind deviation --build dTotalRecall` reported 142, matching `git ls-files`. `show` with `#section.nope` exited 2 naming it, `resolve_edge` returned resolved, and `handoff --read` produced the `reads:` list. (figures DERIVED, the builder's probes and timings)
- **AC10** (policy fixtures): `run_cap_case('budgets-cap-memory-slices')` passed under both `warn` and `refuse` with identical output.
- **AC11** (manifest-check self-test): a real `--card --write` against a 9,000-byte index wrote `card 2949 B within · MEMORY.md 9000 B over · each its own 8000 B budget`.
- **AC12** (policy fixtures): `policy.py get <key> --explain` printed `measured`, `report`, `refuse` and `8k`, and the criterion's `grep -c` printed 0.
- **AC6** (recall floor): `git grep "def run_fusion"` finds one line, in `record_find.py`. A probe showed the functions the moved search code now calls are the same objects as before (`bench.terms is id_grammar.terms`, and likewise for the others). The new floor arm's body passed when run inline.
- The lexicon offender count stays at 1435, checked with `--offenders` at HEAD and at the pass: `query_expr`, `search` and `rrf` left `query.py` and arrived in `record_find.py`. A shell helper I had first named `rf_plant` was renamed to `run_find_plant` to pass.

**Owed to the close**
- See each new test RED-first on its staged break (the spec's three `New arm:` lines):
  - `tools/memory-tree/check-memory-hygiene.test.sh`: the 40-row cap line cut, `memory.superseded-slices` read and ignored, `check_sections` skipped.
  - `tools/playbook/adopt-playbook.sh`, the `memory-records` rows: `extract_section` folding headings without `derive_anchor`.
  - `tools/memory-recall/test_recall_floor.py`: a second copy of the search function left in `query.py`.
- Run as legs: `recall floor` (`check-recall.py --data-dir` against the base's rows), `leg_factory.py --check`, policy fixtures, manifest-check self-test, `tags`, the docs leg, and the spec's full section-7 list.
- Re-measure test-time ceilings. About ten hygiene fixtures at roughly 8 s each, six `adopt-playbook` rows at roughly 12 s each, and a policy case of about 20 s were added. The `memory-hygiene self-test`, `playbook render selftest` and `policy fixtures` legs were not re-measured. (figures DERIVED, the builder's probes and timings)
- The playbook render selftest's guard does not list the memory-tree files the `memory-records` plant reads, and the memory-hygiene self-test's guard does not list the playbook, memory-recall and policy kits its fixtures copy. A change to those files alone will not re-run these legs.
- A cold `find` takes about 1m30s and a warm one about 20s, mostly spent filling recall's served set. (figures DERIVED, the builder's probes and timings)
- The memory-tree kit's undeclared `requires_if` reach into the other kits is TOOL-dTotalRecall-43 S10, by the spec.

**Not built**
- S6's per-role `memory.item-budget` value, because the catalogue's allowed values cannot express one.

**Checklist and working tree**
- I ran `gotchas.py --for-diff HEAD~2..HEAD`. The shell heredoc did corrupt `gov_tag.py` (the `heredoc-escape-reaches-the-regex` class); I fixed it with a scratch script, then scanned every changed file for control bytes and parsed every `.py` file: all clean. The `move-inventory` class found no stale callers of the moved functions. The test-time ceilings and the two guard gaps above came out of the same checklist.
- I left the spec writer's unit-43 work unstaged: the spec-43 edit, three untracked files, and its row in the regenerated build README (I staged the README without that row).
