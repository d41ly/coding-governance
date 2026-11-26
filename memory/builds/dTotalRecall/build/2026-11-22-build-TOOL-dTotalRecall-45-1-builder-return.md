**Serves:** journal TOOL-dTotalRecall-45

# TOOL-dTotalRecall-45 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `f1ddf2410` from [2026-11-22-prompt-TOOL-dTotalRecall-45-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-45-build-brief.md), recorded whole; the pass tip is `c6fcf603b`.

## Why

I built TOOL-dTotalRecall-45 from spec rev-4 as written. Every claim the spec makes about current code still held at base f1ddf2410: the four split sites, the 8 calls of render_spec_skeleton (7 self-test calls plus cmd_new_spec), backlog.ANY_FAMILY and load_id_grammar, _SLUG_GRAMMAR and load_slug_grammar, and the enclosing defs of both derive_names calls. So there was no divergence.

## Summary

Committed c6fcf603b on branch/unattended-dtotalrecall-ae256e, built from base f1ddf2410. It has the `Pass: TOOL-dTotalRecall-45` trailer, and the spec header is set to CLOSED.

**What changed**
- S1, `tools/branch-reconcile/branch_reconcile.py`: added the constant `FAMILY_CLASS` (`[A-Z][A-Z0-9]{1,9}`), which `ID_RE` now uses. `derive_names` gets each slug from `_SLUG_GRAMMAR.parse_id_parts(i, None, alt=FAMILY_CLASS)` and skips an id that raises ValueError. When `_SLUG_GRAMMAR` is None it takes the text between the first and last hyphen.
- S2, `tools/memory-tree/gen_build_index.py`: `render_spec_skeleton` has a new keyword-only `slug` and writes the node as `slug[0]`. `cmd_new_spec` passes its own `slug`, and the 7 self-test calls pass `slug="aFix"`.
- S3, `tools/memory-tree/row_grammar.py`: `scan_records` imports `backlog` inside the function and parses each row id with `parse_id_parts(rid, None, alt=backlog.ANY_FAMILY)`. A refused id keeps `""`. I also added the section 7 New arm to the row-grammar selftest: a copy-install fixture with the row `ARCH-d2026-10-26ClosedLoop-3` and a build README that records the hyphenated grammar.
- S5, `tools/policy/check_policy.py`: `derive_run_kind` compares `parse_id_parts(a, None, alt=backlog.ANY_FAMILY)[1]` with the build name. A refused ask id matches no build.
- S4: the commit's `Decided:` trailers name the four sites by file and line text at base.

The commit also has the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-45-1-acceptance-ledger.md`, the `--dispatch` rows in RUN.md, and the files `gen_build_index.py --write` rewrote. I declared those rewritten files (`memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README) with an extra `--dispatch`, and it accepted them. `gen_map.py --write` changed nothing.

**Checks that ran** (probes and fixtures only; no gate, suite or bar)
- AC1 stands in for the branch-reconcile selftest. In a flipped scratch clone (the last `_FLIPS` row plus a build README for `d2026-10-26ClosedLoop`), `derive_names` returned `d2026-10-26ClosedLoop`. Red: the base module returned `d2026`.
- AC2 stands in for the build-index selftest. `--new-spec TOOL-d2026-10-26ClosedLoop-3 --tier 2` wrote a header reading `node d`. A `python -c` probe with `spec_id="TOOL-dFoo-3"` and `slug="xFoo"` gave `node x`.
- AC3 stands in for the row-grammar selftest. `scan_records` keyed the hyphenated row `d2026-10-26ClosedLoop`; red was `d2026` on the base module. No other row's slug changed and none came out `""`. A hand copy of the new arm passed with the new module and failed with the base module (`['d2026']`).
- AC4: `git grep -nE "\.split\(['\"]-['\"]\)" -- tools` no longer lists any of the four sites. None of the remaining hits is inside unit 38's ten functions. `id_grammar.py --readers` lists nothing new in the four files.
- AC5 stands in for the policy fixtures leg. `derive_run_kind`, loaded through `load_tree_lib_or_refuse` and `load_run_readers`, answered `spec`. Red: the base module answered `build`.
- The commit hooks passed. `gotchas.py --for-diff HEAD~1..HEAD` ran and I reviewed its checklist; nothing needed acting on. I made no new functions, so no lexicon check was needed. No command hit its time limit.

**Owed to the close**
- The legs on the spec's gates section: branch-reconcile selftest, build-index selftest, row-grammar selftest, tier2-review self-test, policy fixtures, routed-commits selftest, scratch-guard self-test, recall floor, recall floor arms, memory hygiene, and the four codebase-map legs.
- The RED-first observation of the new arm in `tools/memory-tree/row_grammar.py` (covers AC3), staged by putting the split back. It must show `['d2026']` red and `['d2026-10-26ClosedLoop']` green.
