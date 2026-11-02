# Build brief — TOOL-dFoldedAudit-6

**Serves:** research TOOL-dFoldedAudit-6

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-6.md`, its latest rev, and nothing else. The design it derives from is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`; where the two differ the spec wins.

- Run no gate leg, no suite and no bar. Stage a new refusal's RED with the one test file you write, directly, only if the spec's arm is yours to observe; every `New arm:` is otherwise owed to the main loop at the close.
- Closing DIFF review behaviour stays byte-identical. Every change sits on the spec subject's branch.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
- A live run claim on dRankedPlan, dFurnishedOrders or dDeclaredLoop at this pass is a park, not a write. Read `unattended.sh --claims` first.
- Leave `memory/LIVE.md` and `memory/ledger/` out of `--writes`, and stage their `--write` render undeclared. This unit writes their generator, so declaring them is the pairing `--dispatch` refuses. They are declared generated indexes, so check 23 does not count them as undeclared writes: `tools/memory-tree/kit.toml:460-464`, with `TOOL-dTrueNorth-26`'s commit `dc0b801d3` as the precedent. This answers the stopped dispatch recorded at `build/2026-11-02-build-TOOL-dFoldedAudit-6-1-builder-return.md`.
- The selftest at `gen_build_index.py:5877` calls `render_region` on a `collect()` dict with no `root` key, so the pass-through must read `build.get("root")`.
