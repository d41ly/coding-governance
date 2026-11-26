**Serves:** journal TOOL-dTotalRecall-39
**Caused-by:** TOOL-dTotalRecall-39

# TOOL-dTotalRecall-39 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `fe7630e5e` from [2026-11-22-prompt-TOOL-dTotalRecall-39-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-39-build-brief.md), recorded whole; the pass tip is `d65380330`.

## Why

TOOL-dTotalRecall-39 is built and committed as d65380330, and the spec could be built as written. Before writing anything I checked the spec's claims against the tree. Unit 19's `tree_lib.read_header_edges` exists with the signature and ValueError the spec describes. The landed adapter `edge_grammar.py#read_header_edges` and `HEADER_RE` had exactly the two callers named (`read_tree_edges` and `read_site_edges`). `check_site_targets` and `EdgeRefusal` are as cited, the `caused-by` row had `pin = "none"`, and the dFurnishedOrders-19 deviation record carries `cl-dClosedLoop-0210@c44de500`. In the same commit the spec header moved to CLOSED, dated 2026-11-23, and nothing else in the spec was edited.

## Summary

**What changed**
- `tools/playbook/edge_grammar.py` no longer has its own `read_header_edges` or `HEADER_RE`. It gains `check_header_edges(text, path, binding=None)`, which:
  - looks up `tree_lib.read_header_edges` through `ti.load_memory_tree()` at each call;
  - turns that reader's ValueError into one `EdgeRefusal`, with the reader's message on line 2;
  - returns `check_site_targets` over the edges.
- `read_tree_edges` and `read_site_edges` now call it. The module docstring's grammar and sites paragraphs are updated.
- `tools/playbook/edges.toml`: the `caused-by` row is now `pin = "clause"`.
- `tools/playbook/README.md` and `help/tags.md` are updated: the help table row now ends `| clause |`, plus its pinned-forms paragraph and "Where edges are read".
- `tools/memory-tree/record_causes.py` gains two plants, `bulleted-cause` and `bulleted-twice`, and a helper `check_plant_walk`. Each plant runs both the causes check and the playbook kit's `read_tree_edges`, which it reaches through `gen_build_index.load_edge_grammar(resolve_kit_dir(...))`, the same route `build_records` uses. Each prints a PASS or FAIL line and exits 0 only on PASS.
- `tools/memory-tree/check-memory-hygiene.test.sh` has the new §7 arm for those two plants.
- Also in the commit: the acceptance ledger, the regenerated outputs (`memory/map/generated/symbols.json`, `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README, the spec's records region) and `RUN.md`. The commit message ends with `Pass: TOOL-dTotalRecall-39` beside `Co-Authored-By: Claude Opus 5`.

**What I checked** (fixtures and probes only; no merge bar, suite, gate leg or `--selftest` ran)
- **AC1:** a `python -c` probe wrapping `tree_lib.read_header_edges` printed `False False 1`, and `git grep "def read_header_edges" -- tools` finds only `tree_lib.py`.
- **AC2:** `--plant bulleted-cause` printed `0 causeless · 0 orphan(s)`, the walk's `caused-by` edge to `TOOL-tFix-1`, and PASS, then exited 0.
- **AC3:** `--plant bulleted-twice` printed no edge for the record and one walk refusal, `Caused-by is given twice, at lines 5 and 6`; the causes check reported the same header refused; it printed PASS and exited 0.
- **AC4:** `--parse` on the typed scratch file holding `a,b` exited 1 with "matches no address form"; on `bare.md` it exited 0 and printed `caused-by · TOOL-tFix-1`.
- **AC5:** `--parse` on the dFurnishedOrders-19 deviation printed its `caused-by · cl-dClosedLoop-0210@c44de500` row and green, with exit 0. `--list` shows `pin clause`, and the grep of `help/tags.md` finds line 218 ending `| clause |`.
- A probe of `read_tree_edges` plus `check_edges` over this tree read 2791 header `caused-by` edges with 0 refusals and 0 reds. It did not resolve the edges.

These probes stand in for `playbook render selftest`, `memory hygiene` and the tags-pack `edges` leg.

**Owed to the close**
- The legs on the spec's gates section: `playbook render selftest`, `govkit acceptance matrix`, `policy fixtures`, `memory hygiene`, `recall floor`, `recall floor arms`, plus the `edges` leg's resolution pass.
- The RED-first observation of the new arm in `check-memory-hygiene.test.sh` (it covers AC2 and AC3). Staging the old column-0-only adapter should make both plants FAIL: no edge in the first, no refusal in the second.
- S6's departure from PLAY-dOrderedCharter-28 S5 is the close's `deviations.py` report to record. S5's prose is for the diff review to read.

**Choices recorded as `Decided:` trailers**
- The AC4 scratch file sits under a `builds/tFix/build/` folder, because `derive_record_name` only treats a file as typed under a build's `build/` folder.
- The bulleted plants add a fixture `deviation` row whose fields include `Caused-by`, and a rooted `tFix` build. Without them the causes check never reads the field, and `TOOL-tFix-1` is neither defined nor reached.
- One sentence in `tree_lib.read_header_edges`' docstring still says the edge grammar's own adapter "stays until TOOL-dTotalRecall-39 binds this one". `tree_lib.py` was outside the declared write set, so I left it for the diff review.

**After the commit**
- `gotchas.py --for-diff HEAD~1..HEAD` returned 0 and selected 41 classes; I went through the ones that apply. Both plants assert a positive result, so each can turn red. A grep found no reader of the retired names outside build records. No source was written through a heredoc, and no fence or table pipe was added.
- The build status rendered as DEFERRED, which is derived: no unit is INPROGRESS now.
- Nothing timed out, so nothing was skipped.
