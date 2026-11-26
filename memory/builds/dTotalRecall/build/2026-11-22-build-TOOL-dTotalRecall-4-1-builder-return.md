**Serves:** journal TOOL-dTotalRecall-4

# TOOL-dTotalRecall-4 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `94e17798f` from [2026-11-22-prompt-TOOL-dTotalRecall-4-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-4-build-brief.md), recorded whole; the pass tip is `dcd8b10f7`.

## Why

Every claim the spec makes about current code held when checked against the tree. The README census came out as pinned: 223 READMEs and the same key counts. With the code in place, the derivation printed 26 disagreement lines (18 streams, 7 roster, 1 node), as section 4 states. One thing could not be built exactly as written. S2's four-argument grader `check_front_matter_value(key, value, conf, grammar)` has no tree to pass to `build_id_token_re` and `_expand_ids`, which section 4 says it matches ids for. It therefore takes a fifth, optional `root=None`. The four-argument call still behaves as the spec says. This and the other builder discoveries are recorded in deviation 42 ("builder discovery", author-recorded), not returned as a divergence. All criteria were observed by probes or are named below as owed. Unit 4 is committed with its spec header set to CLOSED.

## Summary

TOOL-dTotalRecall-4 is built and committed as dcd8b10f7 (base 94e17798f). The spec header is CLOSED, and the commit carries the `Pass: TOOL-dTotalRecall-4` trailer and `Co-Authored-By: Claude Opus 5`. No gate, suite or bar ran; the closing checks the main loop still owes are listed at the end.

**What landed**
- `tools/memory-tree/gen_build_index.py`:
  - `FRONT_MATTER_KEYS` declares every front-matter key once; `REQUIRED_KEYS` is now derived from it as slug, opened and ids.
  - `parse_front_matter` refuses an undeclared key, naming the key, its line and the declared set. It grades the types that need no tree through `check_front_matter_value`.
  - `collect` grades the tree-bound types (ids, slugs, families, streams) in place of its two old checks.
  - `derive_front_matter` derives node, roster and streams. The roster comes from the build's ids, then its asks, then its parents' rosters, then the conf's first FAMILIES pair. The result is written over each build's front matter, so the derived values win in every render.
  - The legacy population `build-readme-typed-derived` is read, armed and unarmed. A typed derived key outside it is refused. Disagreements and the unarmed state each print one stderr line.
  - New flags `--print-front-matter <slug>` and `--print-typed-derived` (the seed).
  - New `build-routes` region with `render_routes`, which names at most two records per purpose.
  - `derive_defined_ids` feeds `--print-bindings`, so a design-only build's `ids:` defines its units.
  - Both scaffolds stop writing node, roster and streams.
  - New selftest arm `test_front_matter_schema`, and two existing scaffold oracles updated.
- `tools/govkit/registry.toml` registers the population. Its home `memory/project/build-readme-typed-derived.txt` was seeded with 223 rows (DERIVED, the builder's seed at `dcd8b10f7`), and `.memory-tree.conf` admits it under `PROJECT_REGISTRY_EXTRA`.
- `tools/memory-tree/record-kinds.toml` gains the `build-readme` row. The registry region and check 9's prose are re-rendered in `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` (their changed lines are identical).
- `tools/roles/handoff.py` gains `read_agent_root`, and the task opening now states the agent's root. `tools/roles/render_agents.py` gains arm 21, `check_agent_root_arms`.
- `tools/unattended/unattended.sh`'s `read_roster_family` now runs `--print-front-matter`. Its slice in `unattended.test.sh` stubs `resolve_index_generator`.
- `tools/loop/claim.py`'s `read_anchor_unit` now calls `read_derived_front_matter`.
- Also in the commit: the regenerated `symbols.json`, the kickoff manifest re-stamped (because `.memory-tree.conf` is on its watch list), and the 225 re-rendered READMEs plus `LIVE.md`, the 2026-11 ledger shard, `backlog/TOOL.md` and the as-built view.
- Records: the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-4-1-acceptance-ledger.md` and deviation 42 at `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-4-deviation-42.md`.

**Checks that ran (probes of this unit's own code, standing in for the gates named in brackets)**
- AC1 [build-index selftest, memory hygiene check 9]: in a scratch clone at $TEMP/tr4w, `--write` reached a fixed point (an empty porcelain on the second run). Adding `parent: dTrueNorth` made it exit 1, naming the key, line 4 and the declared set. In the worktree, `--check` was clean after `--write`.
- AC2: fixture probes raised StaleHeader for `opened: 2026-13-45` and `pieces: 0`; `collect` refused `depends-on: d!bad` as a slugs value.
- AC3: `--print-front-matter dTotalRecall` printed `node: d`, `roster: TOOL`, `streams: tooling` in about 7 s (DERIVED, the builder's probe at `dcd8b10f7`). Neither scaffold writes the three keys. In a fixture whose first FAMILIES pair is ARCH, a placed patch of a TOOL origin derived TOOL. `read_roster_family` returned TOOL; `read_anchor_unit` returned `TOOL-dTotalRecall-1`.
- AC4 (in the clone): a typed `streams: playbook` printed the disagreement line and rendered tooling; a new README typing `node: d` exited 1; with the home deleted the run exited 0 and printed the unarmed line.
- AC5: the dTrueNorth routes region shows two reviews plus "and 3 more under reviews/", and the card ref row. The longest region line across the tree is 226 characters.
- AC6: the real tree renders the work-order line. A clone committing `agent-root = "readme"` renders the README line. A repo with no commit renders the work-order line plus a refusal note.
- AC7: the fixture printed a B row only for TOOL-xDesign-2; with `spec_ids` alone it printed both.
- AC8: tomllib finds the row, and `read_schema_source` lists the same 20 keys as its fields.
- `gotchas.py --for-diff HEAD~1..HEAD` ran over the commit and was acted on: no control bytes in the added lines, and no stranded message literals.

**Owed to the close**
- `record_kinds.py --check` for AC8: the role hook refused it here.
- These legs: `build-index selftest`, `memory hygiene`, `memory-hygiene self-test`, `build README slot contract`, `kit/dogfood doc parity`, `record-kinds`, `roles render selftest`, `roles adopter self-test`, `roles catalogue`, `unattended kit gate`, the four loop fixture legs, `loop claim fixtures`, `govkit selftest`, `ratchet (never gains)`, `ratchet (both ways)`, `policy check`, `policy fixtures`, `lexicon naming predicates`, `python reads`, `spec tokens`, and the rest of section 7.
- Both `New arm:` RED-first observations:
  - `gen_build_index.py` `test_front_matter_schema`, staged by restoring the open-world parse.
  - `render_agents.py` arm 21, staged by dropping the policy read.

**Risks for the close to watch**
- `read_roster_family` and `read_anchor_unit` now run a full `collect`. Driver or claim fixture trees that reach them without an owner id need a tree `collect` accepts, including the stale-header waiver file. This affects `unattended kit gate` and `loop claim fixtures`.
- `check-memory-hygiene.sh` still prices only four regions as generated, so the routes region bills to each README's 25600-byte cap. dSafePassage now measures 24501 authored bytes.
- Refusal branches with no arm: an unreadable ledger registration, a home holding the unarmed line, the `--print-front-matter` usage error, and an out-of-catalogue agent-root value.
- `AGENT_ROOT_DEFAULT` repeats the catalogue's `work-order` default in a second place.

**Shared worktree**
- `memory/builds/dTotalRecall/README.md` was staged with only this pass's rows. Six DEFERRED unit rows (40, 44, 45, 6, 63, 64) that another unit's spec writer changed in the working tree were left at HEAD's text.
- Those spec edits and their untracked records stay uncommitted in the worktree.
