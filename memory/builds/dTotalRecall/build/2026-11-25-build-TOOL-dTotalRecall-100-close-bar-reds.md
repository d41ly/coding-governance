**Serves:** log TOOL-dTotalRecall-100
**Caused-by:** TOOL-dTotalRecall-100

# The close's first bar, its reds and what each one is

The plain bar ran at the main loop over `e5b7ee15b`, the run branch with `origin/main` `3d6c1702a` reconciled in
(`ffa0dcf2d`). It returned RED on 25 legs (DERIVED 2026-11-25, that run), two of them on their serial retry. The units ran the pass legs alone, so most of these
legs had not graded this build before. Each red is read below; "ours" is a red a unit of this build made, "merge" one the
reconcile made. Beside them stand reds the scoped self-tests showed (DERIVED 2026-11-25, main loop, a scratch clone).

## Reds and causes

- `drift-audit records` · ours (unit 16): `record-kinds.toml`'s purposes cite design records by path, which
  `non_terminal_specs_cited_by_product_source` reads as shipped evidence. `drift_signals.py#EVIDENCE_GLOBS` excludes the
  size registries and `unscanned-readers.txt` for that reason.
- `marker contracts` · ours (unit 5): `marker-contract.test.sh` names its fixture slugs `tMark<n>`, and the slug grammar
  admits no digit there, so check 12 grades none of them.
- `routed commits name a specced unit` · `d0e02120b`, a `Red-fix:` commit of 2 routed paths and 69 lines (DERIVED 2026-11-25, that leg) against the
  lane's bound of 3 and 60 (PINNED 2026-11-23, `routed_commits.py#RED_FIX_MAX_LINES`). The RANGE half at the push
  boundary reads no waiver. This one is the landing's, below.
- `remote literals (kit code names no remote)` · ours (units 3, 7, 19): five lines (DERIVED 2026-11-25, that leg) in
  `build_records.py` and `gen_build_index.py` fixtures.
- `govkit selfcheck` · merge: `memory_measure.py`'s marker reads runlog 1.18 against main's 1.19.
- `govkit acceptance matrix` · the scratch install's `playbook render selftest` arm "a map past MAP_CAP_BYTES refuses"
  reads `hold 'PLAY-fx-0 F1' is not <unit id> F<n>`: `documents.toml`'s fixture id `PLAY-fx-0` under the slug grammar.
- `transition-audit arms` · ours (unit 5): AC15, an absent `id_grammar.py` is not refused by name and a shards-mode tree
  without it is not dormant. `backlog.py` and siblings import `id_grammar` at import time.
- `layer dependencies (the core never depends on an expansion)` · ours (units 9, 12, 17, 18): eleven edges (DERIVED 2026-11-25,
  that leg) from memory-tree and review-harness to memory-recall and runlog with no optional row naming the file.
- `core meta-check` · ours (unit 19's leg): the pending row `principle.p35` of `core-pending.txt` is stale, the principle
  being enforced now.
- `docs` and `help reference pages` · merge: `help/reference/policy.md` took main's side, so `asks.acceptance`,
  `builds.slug-words`, `builds.slug-style`, `builds.slug-date` and `memory.map-purpose` are anchored on no page; the
  render is `render_playbook.py --reference`.
- `python reads (a name never bound, an import outside its guard)` · ours: suites now import the loop, playbook, memory-recall,
  memory-tree, policy, roles and runlog kits outside their guards, and eight parameters (DERIVED 2026-11-25, that leg) are read
  nowhere: `build_records.py#render_text` rel, `design_lib.py#extract_spec_head` arg, `record_kinds.py#render_template`
  typed_kinds, `tree_lib.py#extract_head_lines` arg, `record_extract.py#extract_feature` and `#extract_marker` ctx and
  path, `memory_measure.py#read_slice_bytes` agent_path.
- `ratchet (never gains)` · `positional-refs` gained rows of `RUN.LANDED.bc313f97.md`, the archived run record.
- `ratchet (both ways)` · ours (unit 20): four upgrade steps (DERIVED 2026-11-25, that leg) have no `landed-steps` row.
- `shell hygiene (a location probe asked from a moved directory)` · ours (unit 2): one site in
  `check-memory-hygiene.test.sh`.
- `shell hygiene (a fork spent on builtin work)` · ours: sites in `check-memory-hygiene.test.sh`, `gov-claim.sh` and
  `push-main.test.sh`, seven findings in all (DERIVED 2026-11-25, that leg).
- `shell hygiene (a fixed-name temp renamed into place)` and `shell hygiene (a quoting hazard)` · ours (unit 3):
  `gov-claim.sh`.
- `portability (shell lines only shrink)` · 24 findings (DERIVED 2026-11-25, that leg), ours and merge: rows over or under their
  `shell-role` count and `gov-claim.sh` with none.
- `spawn budget (forks per hot entrypoint)` · four entrypoints (DERIVED 2026-11-25, that leg) over their `fork-ceilings` row.
- `cleanup posture (a tree removal that swallows its error)` · ours: five sites (DERIVED 2026-11-25, that leg), the leg main
  added since this build's base.
- `kickoff-manifest ratchet` · merge: the reconcile's re-stamp names the merge's first parent, and main's watched commits
  sit past it.
- `memory hygiene` · check 15 refuses two citations, `gov-ref.sh#remove_gov_ref` and `id_grammar.py#derive_slug_grammar`
  (DERIVED 2026-11-25, that leg), though both symbols exist.

- `tags (the resolver's checks)` · ours (units 9, 10): the `section` namespace unit 9 registers puts every derived heading
  anchor before `check_tag_shape`, and 13202 (DERIVED 2026-11-25, `gov_tag.py check`) are over its 64 bytes; 41 more (DERIVED 2026-11-25, the same run)
  are `owned`, a `marker` tag an expansion kit's file mints in a core namespace; the rest are in the log.
- `edges (every declared edge parses, is registered and resolves)` · ours (unit 9): the `feature` namespace is registered and
  holds no anchor, so each `tests=feature.<seg>` edge of `gate-legs.json` resolves to no row, 216 (DERIVED 2026-11-25, that leg); the
  remaining one named this unit's id before its spec existed.

## Self-test arms red on the clean tree

- `check-memory-hygiene.test.sh`: `hit` and `miss` hand grep a pattern without `--`, so the arms whose pattern opens with
  a hyphen can never hold; `PASS door-header — 8 cases` is 12 since unit 43 (DERIVED 2026-11-25, the plant's own line); `findings 1`
  and `findings-2 1` are `findings causes` and `findings-2 causes` since the population's third key, and the paired `miss`
  is vacuous.
- `row_grammar.py --selftest`: four arms (DERIVED 2026-11-25) red on `from id_grammar import SlugPattern` at import, and
  `scan_engine_imports` lists the function-body imports of `build_records.py`, `gov_record.py`, `record_causes.py` and
  `record_kinds.py`.

Drafts of six repairs (DERIVED 2026-11-25) ran in the scratch clone: `check-remote-literals.sh` read clean and
`row_grammar.py --selftest` read whole green with them.

## The landing

`d0e02120b` blocks the landing whatever else is green. The RANGE half of `routed_commits.py` grades every pushed commit and
reads no waiver, so the push is refused while that commit sits in the range. dWitnessedBar met the same refusal and rewrote
its range by `2026-11-22-build-TOOL-dWitnessedBar-1-replay.py`, on the owner's own words. This run holds no such word, so
it repairs what it can and holds the landing for the owner.
