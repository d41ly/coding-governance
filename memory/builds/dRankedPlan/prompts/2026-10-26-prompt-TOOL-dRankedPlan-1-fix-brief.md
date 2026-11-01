**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16

# Fix brief — dRankedPlan, the nine findings the main loop's checks raised over the 16 authored specs

The six writers of `unattended-build.js` run `wf_a043cc4e-f18` authored the 16 specs under
`memory/builds/dRankedPlan/spec/`, staged and not committed. The main loop then ran `tools/check-spec-tokens.py`
(14 unwaived hits, eight of them distinct spec defects; the packet hit clears when the main loop drops the README's
`status:` key) and `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` (check 12 on one spec).

Fix exactly these findings, in place, in the spec named, keeping every clause token, `**Carries:**` line, §3 edge and
§8 mark as it stands unless the finding says otherwise. The specs are uncommitted, so they stay `rev-1`: change no
status header. Write nothing else, commit nothing, and return each finding with what you changed. The spec brief,
`memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md`, still binds every rule.

## The findings

1. `2026-10-26-spec-TOOL-dRankedPlan-16.md` · check 12 · AC7 names no backticked witness. Name the observation in
   backticks: the command the arm runs and the text its refusal prints (both plan record file names).
2. `2026-10-26-spec-TOOL-dRankedPlan-16.md` · `[guards]` · §4 Files touched names `.claude/agents/gov-spec-writer.md`,
   a render, which trips the guards of the legs `check-wiring self-test` and `lexicon naming predicates`, absent from
   the §7 leg line. Name the source the unit edits (`tools/roles/agents/…`) as the edit and the render as its copy,
   and add to the §7 leg line each leg, spelled as `tools/gate-legs.json` names it, whose guard a path left in Files
   touched still trips.
3. `2026-10-26-spec-TOOL-dRankedPlan-1.md` · `[path]` · `memory/PLAN.md` (twice) and `memory/OTHER.md` are cited where
   the checker grades paths (§6), and neither is tracked. Cite the view this unit creates by basename (`PLAN.md`) in
   §6, keeping the full path in §2, §4 and Files touched; a fixture's planted file is named without a path-shaped
   token, or as a basename.
4. `2026-10-26-spec-TOOL-dRankedPlan-13.md` · `[path]` · `tools/alpha/a.py,`, `docs/x.md,` and `tools/alpha/new.py` are
   fixture paths read as untracked repository paths. Describe the planted paths so the checker does not read them as
   repository paths: a basename, or the paths outside backticks inside a quoted fixture value, and say they are
   planted in the fixture tree.
5. `2026-10-26-spec-TOOL-dRankedPlan-2.md` · `[bar]` · `bash .githooks/pre-commit.test.sh` is named as an acceptance
   observation. A suite is not one: observe the hook block on a staged break or a fixture of the unit's own code, and
   name the suite on a `New arm:` line in §7.
6. `2026-10-26-spec-TOOL-dRankedPlan-6.md` · `[bar]` · `tier2-review.test.sh` is named as an acceptance observation.
   Same remedy as finding 5: a probe of `review_pin.py` or a fixture in §6, the suite on a `New arm:` line in §7.
7. `2026-10-26-spec-TOOL-dRankedPlan-5.md` · `[guards]` · §4 Files touched names the directory `memory/builds/`, which
   trips the guards of `recall floor` and `recall floor arms`, absent from the §7 leg line. Name the exact records the
   unit writes (their path pattern under the build folders the mapping disposes) in place of the bare directory, and
   add each leg whose guard a remaining path still trips to the §7 leg line.
8. `2026-10-26-spec-TOOL-dRankedPlan-2.md` and `2026-10-26-spec-TOOL-dRankedPlan-15.md` · `[handoff]` · unit 2's §3
   hands `plan.authority` to TOOL-dRankedPlan-15, and unit 15's spec never names that token. Either unit 15 truly
   reads the ratified order `plan.authority` governs when a revision changes the plan — then name `plan.authority`
   in unit 15 where it reads it and declare the reciprocal `consumes-from` — or it does not, and unit 2's bullet is
   corrected. Say which in your return.
9. Every spec · after your edits, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no
   finding names a dRankedPlan file. The main loop re-runs `check-spec-tokens.py` after you return.
