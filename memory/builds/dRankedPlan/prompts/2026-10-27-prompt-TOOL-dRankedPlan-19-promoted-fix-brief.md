**Serves:** research TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29

# Promoted-fix brief — dRankedPlan, the check-spec-tokens hits on the round-1 promotions

The round-1 spec audit's disposal (run `wf_c40b3689-b08`) authored `TOOL-dRankedPlan-19` to `-29` and folded a
hands-off edge into each roster spec it closes findings on. The main loop then ran `tools/check-spec-tokens.py`: the
hits below, every one on a promoted spec. Fix exactly these, in place, in the spec named, keeping every `**Carries:**`
line, §3 edge and §8 mark as it stands. The promoted specs are uncommitted: change no status header. Commit nothing,
and return each hit with what you changed. The spec brief,
`memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md`, still binds every rule.

## The hits

`[path]` — the checker grades every path a §6 criterion names against `git ls-files`, and none of these is tracked at
HEAD: each is a file this build or a parent will CREATE. Cite it by basename in §6 (`ratify.py`, `plan.md`), keeping the
full path in §2, §4 and Files touched; a command that reads a file takes it as an argument rather than a path in a
quoted literal; a fixture's planted file is named by basename and said to be planted.

- 2026-10-26-spec-TOOL-dRankedPlan-19.md [path] `help/plan.md` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-19.md [path] `tools/loop/ratify.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-20.md [path] `help/loop.md` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-20.md [path] `tools/loop/scenario.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-21.md [path] `help/plan.md` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-21.md [path] `tools/loop/ratify.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-22.md [path] `tools/loop/README.md` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-22.md [path] `tools/loop/ratify.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-22.md [path] `tools/memory-tree/triage.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-23.md [path] `help/loop.md` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-23.md [path] `tools/loop/plan_revision.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-24.md [path] `tools/loop/ratify.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-25.md [path] `help/plan.md` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-25.md [path] `tools/loop/ratify.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-26.md [path] `tools/loop/ratify.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-28.md [path] `tools/memory-tree/record_kinds.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-29.md [bar] `tools/drift-audit/selftest.py` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- 2026-10-26-spec-TOOL-dRankedPlan-29.md [path] `memory/PLAN.md` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-29.md [path] `tools/loop/loop.toml` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-29.md [path] `tools/ok.py` — not tracked by git ls-files
- 2026-10-26-spec-TOOL-dRankedPlan-29.md [path] `tools/workflows/review_pin.py` — not tracked by git ls-files

`[bar]` — `tools/drift-audit/selftest.py` in unit 29 is named as an acceptance observation. A suite is not one: observe
the unit's own code on a staged break or a fixture in §6, and name the suite on a `New arm:` line in §7.

`tools/ok.py` in unit 29 is a planted fixture path: name it as planted, by basename.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file. The main loop re-runs `check-spec-tokens.py` after you return.
