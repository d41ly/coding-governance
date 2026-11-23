**Serves:** journal TOOL-dTotalRecall-51
**Caused-by:** TOOL-dTotalRecall-51

# TOOL-dTotalRecall-51 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `8138bb587` from [2026-11-22-prompt-TOOL-dTotalRecall-51-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-51-build-brief.md), recorded whole; the pass tip is `30d1901d6`.

## Why

TOOL-dTotalRecall-51 was built as its rev-3 spec states, with no divergence. Everything is in one pass commit, 30d1901d6, which ends with the `Pass: TOOL-dTotalRecall-51` and `Co-Authored-By` trailers and moves the spec header to CLOSED, 2026-11-23. Every acceptance criterion was observed with a fixture or a probe of the changed code. Whatever only a gate can show is listed in the summary as owed to the close.

## Summary

Built TOOL-dTotalRecall-51 in commit 30d1901d6 (base 8138bb587). All paths were inside the declared write set, so no extra `--dispatch` was needed. The brief was already recorded (`--brief` said "already recorded, unchanged").

**What changed**
- **S1 and S2**, in tools/memory-tree/tree_lib.py:
  - `BIND_PREFIX` is now the one place the optional comment marker (`#`, `//` or `;`) is spelled, as the named group `prefix`. `BIND_RE` and the new `HEAD_EDGE_RE` (Made-by or Caused-by) both use it.
  - `read_header_edges` now reads an untyped record's made-by and cause lines behind the prefix its first Serves line uses. It raises `ValueError` naming the record and both lines when the two prefixes differ.
  - The old `HEADER_EDGE_RE` is deleted; nothing else used it.
- **S3**, in tools/memory-tree/record_causes.py:
  - `read_grading` now grades, besides Markdown records, each non-Markdown record whose first Serves line is behind a comment marker. The check for that is a helper nested inside it, `read_serves_prefix`, which the lexicon accepted.
  - Record keys stay Markdown file stems, and `--measure` is unchanged.
  - The `--check` count line now reads `N Markdown record(s) · M comment-headed · K legacy`.
  - New fixture plants: `script-cause-prefixed`, `script-cause-bare` and `script-causeless`.
- **S4**: one `ratchet.py widen legacy-records` call admitted 139 records. It wrote memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-51-widen-7.md and added 139 rows to memory/project/legacy-records.txt, removing none. No existing record was rewritten.
- **S5**: one sentence added to the Record bindings section of tools/memory-tree/HYGIENE.template.md, rendered into memory/HYGIENE.md with `adopt-memory-tree.sh --render`.
- **Test arm**: added to tools/memory-tree/check-memory-hygiene.test.sh for AC1 to AC3. I checked its syntax with `bash -n` and ran its reader-probe part on its own (3 checks, all passed). I did not run the suite.
- **Other files in the commit**: the acceptance ledger (memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-51-1-acceptance-ledger.md), RUN.md, and the files `gen_build_index.py --write` regenerated (memory/LIVE.md, memory/backlog/TOOL.md, the build README, and the spec's records table). `gen_map.py --write` changed nothing.

**Checks that ran, and the gate each stands in for**
- **AC1**: a `python -c` probe of `read_header_edges` over a `.py` text with a `#`-prefixed cause line returned the `caused-by` edge to `TOOL-dFix-1`. The `script-cause-prefixed` plant reported `1 comment-headed`, `0 causeless · 0 orphan(s)` and green. Stands in for the memory-hygiene self-test.
- **AC2**: a bare cause line under a `#` Serves line in a `.sh` record, and a `#` cause line under a bare Serves line in a `.md` record, each raised the `ValueError` naming both lines. The `script-cause-bare` plant reported the record's header as refused. A probe of every tracked record in the tree raised 0 times. Stands in for the memory-hygiene self-test.
- **AC3**: the `script-causeless` plant reported the `.sh` record under `causes` and never mentioned `atlas.html`. Stands in for the memory-hygiene self-test.
- **AC4**: a probe of `read_grading` at the base found 139 graded non-Markdown records, none already in the legacy list, matching the spec's 139. A probe of the list then counted 139 rows marked `widened:` with the widen-7 record's name. The commit adds no non-Markdown file under memory/builds. Stands in for the `record causes` and `memory hygiene` legs.

**Owed to the close (not run here)**
- `record_causes.py --check` at the tip (AC4's first clause). The hook refused it to this role because it is the `record causes` leg.
- The legs `memory hygiene`, `memory-hygiene self-test`, `kit/dogfood doc parity`, `recall floor`, `recall floor arms` and `lexicon naming predicates`.
- The RED-first observation of the new arm in check-memory-hygiene.test.sh (AC1 AC2 AC3). Its staged breaks: reading only the bare form at the start of the line (the prefixed plant then reds), and grading only Markdown records (the `comment-headed` and `.sh` checks then fail).

**Choices the spec left open** (each is a `Decided:` trailer in the commit)
- `HEADER_EDGE_RE` was deleted rather than kept beside `HEAD_EDGE_RE`.
- A record with no Serves line in its first lines expects the bare form.
- The plants' records name the fixture's own unit, TOOL-fRoot-1, rather than AC1's TOOL-dFix-1, because the fixture does not define TOOL-dFix-1 and the cause would fail to resolve.

**Bug-class checklist**: I ran `gotchas.py --for-diff HEAD~1..HEAD` and went through it.
- `HEADER_EDGE_RE` has no remaining reader anywhere.
- "Amendment leaves its other half standing" turned up prose outside this unit's write set that is now out of date. I left it for the main loop rather than widen the write set:
  - tools/memory-tree/README.md, the paragraph opening "The causes check reds a tracked Markdown record" (its plant list was already out of date before this pass).
  - tools/playbook/README.md and tools/playbook/edge_grammar.py's docstring, which describe the bare cause line "at column 0". That is still true for Markdown records, the only kind the edge grammar reads.

No command timed out or was skipped.
