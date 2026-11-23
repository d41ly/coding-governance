**Serves:** journal TOOL-dTotalRecall-19
**Caused-by:** TOOL-dTotalRecall-19

# TOOL-dTotalRecall-19 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `9d7afdc6a` from [2026-11-22-prompt-TOOL-dTotalRecall-19-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-19-build-brief.md), recorded whole; the pass commits are `6ea003891` and `e2a4eb84a`.

## Why

TOOL-dTotalRecall-19 is built and committed in two commits, both carrying `Pass: TOOL-dTotalRecall-19`. The pass commit is 6ea0038917b88da100410fad7c6831935375fb5d: all the code, the seeded population, the leg, the records, and the spec header set to CLOSED · rev-9 · 2026-11-23. The second commit, e2a4eb84a9aed42118c1dec397dcf7437caa9097, holds only the policy mirror. It has to be separate because `policy.py mirror --write` renders the catalogue as committed at HEAD, which is what spec S11 says. The spec was buildable as written, with two small departures. First, the `legacy-records` table also needs `verbatim = ["section"]`, because 7 heading anchors are bare numbers that the ledger would refuse as line numbers. That is recorded in deviation record 1002. Second, AC1 and AC2 leave out `--title`, which the door has required since unit 2. The door now checks for a cause before it checks its flags, so AC1 as written is still refused naming `Caused-by`, and AC2 was observed with `--title` added.

## Summary

TOOL-dTotalRecall-19 is built and committed. No gate, suite or merge bar ran in this pass. Everything below was checked with fixtures and probes of the new code, and the gate runs are listed as owed to the close.

**What was built**
- **Header reader:** `tools/memory-tree/tree_lib.py` gains `read_header_edges` and `RECORD_KEY_RE`. The reader handles both header forms (column-0 lines for ordinary records, `- **…:**` fields for typed kinds) and refuses a key given twice, naming both lines.
- **Record door:** `tools/memory-tree/build_records.py#write_new_record` and `tools/memory-tree/gov_record.py` gain `--caused-by` and `--edge`, which work as follows:
  - Every kind except a root refuses a missing cause, and the door refuses a cause that does not resolve.
  - `Made-by` is `lease-<slug>` when this session holds the build lease, else `owner`. It comes from the new `read_mint_authority`, which `check_mint_authority` now wraps.
  - Edge lines go under their heading, and the door's output is read back through the header reader and the edge parser before anything is written.
  - `Made-by` is left out of the content key, so a replay still reads as the same write.
- **Checks:** `tools/memory-tree/record_causes.py` (new) holds `check_causes`, `check_orphans`, `read_legacy_anchors`, `STAND_IN_RE` and the five modes. It also has six fixture plants: `legacy`, `causeless`, `typed-causeless`, `orphan`, `claim-root` and `none`.
- **Registry:** the `root` column is set true on `build-readme` and `claim`, and `record_kinds.py#check_row` reds a value that is not a boolean.
- **Edge registry:** two new native classes in `tools/playbook/namespaces.toml`, `made-by-stand-in` and `record-key`. `tools/playbook/edges.toml`'s `made-by` row now admits the first.
- **Population and leg:** the `legacy-records` ledger in `tools/govkit/registry.toml` is seeded into `memory/project/legacy-records.txt` with 10,657 record rows and 56,828 section rows (11.5 MB). The new exempt leg `record causes (causes and orphans over the legacy population)` enforces `principle.p35`, is rendered into `tools/gate-legs.json`, and is claimed in the memory-tree-hygiene feature dossier. Its evidence row was written with `derive-ceilings --observed`.
- **Policy and docs:** `memory.legacy-anchors` now has its summary and usage and has left the unsummarised list. The policy mirror is in the second commit, and the kit README documents the header and both checks.
- **Suite edits:** `check-memory-hygiene.test.sh` gains the door-header and record_causes arms. Its existing record-door arms now pass a resolving cause, and its seed defines TOOL-xLeased-2 so those arms still resolve.
- **Pass records:** the acceptance ledger and deviation record 1002, written through the door under this run's lease.

**Checks run, and the gates they stand in for**
- **AC1–AC3, AC5** (the memory-hygiene self-test's door arms): `build_records.py --fixture --plant door-header` passed all 8 cases. A scratch-clone probe showed a held lease writes `Made-by: lease-dTotalRecall`.
- **AC4, AC6–AC8** (the new leg and its suite arms): all six record_causes plants gave the expected output. The `claim-root` plant goes red with the claim read removed, so it is not passing by finding nothing.
- **AC6 on the real tree:** `--check` after the seed printed `0 causeless · 0 orphan(s)`, with the record-row count equal to the 10,657 Markdown records. It took 11.7 s in one run, measured before the leg was declared.
- **AC5** (record-kinds): a probe of `check_row` named `root = "yes"`.
- **AC9** (policy fixtures): `policy.py get memory.legacy-anchors --explain` printed `derived` with its reason.
- **AC10** (the edges leg): `edge_grammar.run_parse` with resolution resolved a real record stem and `owner`, and named an unknown stem as unresolved. A probe found no record stem outside `RECORD_KEY_RE`.
- **Naming lexicon:** `lexicon.py --measure` left `VERB_OFFENDER_PIN` at 1448.
- The pre-commit hook passed on the second try. The first try failed only because the new leg was unclaimed in the codebase map, which I fixed.

**Owed to the main loop at the close**
- The legs on the spec's gates section, including the new leg itself and `edges (every declared edge parses, is registered and resolves)`.
- The first `New arm:`, in `check-memory-hygiene.test.sh`: see it go red with the cause refusal cut, and with the walk seeded from the records instead of the roots.
- The second `New arm:`, the leg itself: see it go red in a scratch worktree with a new record that has no `Caused-by`.
- The memory-hygiene self-test's time budget should be re-measured, since the suite gained the door-header plant (several minutes) and six fixture runs.

**Things the main loop should know**
- From this commit on, any record written by hand without a resolving `**Caused-by:**` turns the new leg red. That includes the briefs and builder returns the loop writes, and the untracked unit 14 and 15 reground records another session has in this worktree. Unit 36 is the one that makes every code writer emit the line.
- In the build README I staged only this unit's rows. The rows for units 9, 14 and 15, and that session's unstaged spec edits, are left in the working tree.
- The as-built view, MAP.md and inventories.json are generated outputs. I declared them with a second `--dispatch`, along with the dossier and the deviation record. The first dispatch hit the builder's 110 s command limit and was re-run once with a 590 s limit (both DERIVED, the builder's own timeouts), because writing those paths depended on it.
- The bug-class checklist over HEAD~2..HEAD was run and acted on (the claim-root probe, a control-byte scan, the budget item above).
