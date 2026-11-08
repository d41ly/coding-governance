# Acceptance ledger — TOOL-dFairHearing-23

**Serves:** journal TOOL-dFairHearing-23

Built against spec rev-6 in pass commit `7ff570cfa`, whose parent is `a3de6015f`. The main loop drafted this ledger at the close from the builder return and that commit's message. No suite, gate or bar ran in the pass: the scratch probes stood in for the legs, and the spec's gate legs and the RED-first observations of its five `New arm:` lines are owed to the close. A line that says "not recorded" names a half of its criterion no record on disk shows. The eight criteria that had no line were observed at the close, each at the commit it names.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-23
- AC1 — `def extract_tag_ref` — `git merge-base --is-ancestor` found the landing `af3831a6c` present in the parent. The `extract_tag_ref` probes returned the expected values, and an `ast` walk found one `def extract_tag_ref`
- AC2 — `replay_scorer.py --experiment` — over a scratch review-replay manifest it printed 4 of 4, then 3 of 4 with one appendix cut, and an unknown key exited 2
- AC3 — `python review_pin.py --subject $DREC --design-record-preset whole-design --design-audit-runs 3 --design-audit-seed synthetic` — at the tip `948e4141b` it printed three lines, each `"preset": "whole-design"` with `walk` `runs` 3, `seed` `synthetic` and `run` 1, 2, 3. `--design-audit-runs 4` exited 2 naming the flag, and with no `whole-design` no line carried `walk`
- AC4 — `legCount` — the counts read `legCount` 5/5 and `a pipe written as` 1/1
- AC5 — `git merge-base --is-ancestor` — `ef757de0c` and `4a0e73da6` are present in the parent. Not recorded: the `review_pin.py` lines, which the return lists among its checks with no output
- AC6 — `git diff -U0 <unit>~1 <unit> -- tools/hooks tools/roles .claude/skills/build tools/workflows/tier2-review.template.js | grep -E '^[-+].*(KIT_[A-Z_]+_VERSION = |gov:kit [a-z-]+@)'` — over `7ff570cfa` it counts 0 lines, and the same `grep` over the `git log -p` of this build's `tool(dFairHearing)` commits to that unit counts 0, from base `8bec4cefd`, this run's base, where the spec names `3708a705`
- AC7 — `git merge-base --is-ancestor 9ce7710ab <unit>~1` — the landing is present in the parent. Not recorded: the `render_lenses.py` result, which the return lists among its probes with no output
- AC8 — `bash check-verifier-fanout.sh tier2-review.js` — `b21501741` is present in the parent, and a scratch copy of the gate over the render counted 4 marked literals of 5. The greps ran with no printed line recorded. Not recorded: the prelude preset probe, which the return says had no dedicated run
- AC9 — `git merge-base --is-ancestor 886c11fea <unit>~1` — the landing is present in the parent. The return says the label census had no dedicated run here: that half is superseded, see below. Not recorded: the marker-count figures of the half that stands
- AC10 — `git show-ref refs/replay/fhr` — the README recipe with `fhr` at `3708a705` gave a `rev-list` of 6545 and left no `refs/replay/fhr`, and the clone was removed. Not recorded: the `grep -c "clone --branch"` count, an absence check unit 27's AC2 restates
- AC11 — `git merge-base --is-ancestor 3745b407a <unit>~1` — the landing is present in the parent. The greps ran with no printed line recorded. Not recorded: the `deriveRoundState([4, 3, 2], 1, 3)` call, which the return says had no dedicated run
- AC12 — `check_ungated` — a probe at the tip `948e4141b` read the first body gated and the other two ungated, and an `ast` walk found `check_invariant`'s body calling `check_gate_token`
- AC13 — `node spec-audit-optin.js < "$SCRATCH/replay1.json"` — over the replay clone it exited 0 with the replay `reviewDir`, and exited 2 naming `authorized-by: prompt` with dClosedLoop's. Not recorded: the README placement count
- AC14 — `mkfix` — the grep printed 1. An `mkfix`-shaped fixture passed whole-tree with exit 0, and exited 1 naming the missing marker once its literal was cut
- AC15 — `grep -n "render_lenses.py" unattended-build.test.sh` — at the tip `948e4141b` it printed `build_layout`'s copy line beside `lenses.toml`, at :2182. A scratch directory of that copy set rendered `tier2-review.template.js`, exit 0, and exited 2 with `lenses.toml` removed
- AC16 — `replay_scorer.scan_pairing_sites` — neither root call returned a site under `memory/`
- AC17 — `grep -n "spec-audit opt-in pack self-test" tools/govkit/registry.toml tools/run-gates/selftest-budgets.txt tools/run-gates/foreign-prefix.gov.test.sh` — at the tip `948e4141b` it prints the `[[exempt_leg]]` name line and the budget row, and no `WHOLE_RUN` row: unit 27's `e3bd1ad45` took that row out. The row existed at `7ff570cfa`, per `git log -p`
- AC18 — `check-verifier-fanout.js` — the two copy greps printed 3 and 5 and the expected-line grep printed 1. A scratch gate copy with no `check-verifier-fanout.js` beside it exited 2 naming the file
- AC19 — `grep -n "gotchas.py --for-diff" memory/guides/SESSION-KICKOFF.md` — at the tip `948e4141b` it prints line 100, which says the review harness acquires the checklist on the diff kind
- AC20 — `git merge-base --is-ancestor` — `e21580aac`, `9ce7710ab` and `c70d6a020` are present in the parent. Not recorded: the `grep -c "3708a705"` count and the three arms' comparison. Unit 27's AC22 re-reads the base-sha half
- AC21 — `tier2-review.js` — a stub runner over the render passed the `grades` cases at the tip and failed them over the parent render
- AC22 — `legCount` — a stub runner over the render passed the resume-probe cases at the tip and failed them over the parent render
- AC23 — `a pipe written as` — the count over the render is 1, and a stub runner passed the piped-reason case at the tip and failed it over the parent render
- AC24 — `git merge-base --is-ancestor af3831a6c <unit>~1` — the landing is present in the parent. Not recorded: the `read_raw_output` result, which the return lists among its probes with no output
- AC25 — `topLevelArgs` — a scratch copy of the fan-out gate read five `deriveSlotLens` calls as 5, and with `topLevelArgs` staged to split on every comma it read 15
- AC26 — `render_lenses.py --markers` — over a comment naming the marker it printed the literal's line alone. Not recorded: the fan-out leg's exit over that file
- AC27 — `checklistError` — a stub runner over the render passed the truncated-checklist cases at the tip and failed them over the parent render
- AC28 — `git merge-base --is-ancestor 7b2153c28 <unit>~1` — the landing is present in the parent. Not recorded: the `resume:checklist` and `const STAGE_OPTS = ` greps
- AC29 — `git merge-base --is-ancestor 4a0e73da6 <unit>~1` — the landing is present in the parent. Not recorded: the `tomllib` result, which the return lists among its probes with no output
- AC30 — `git merge-base --is-ancestor c70d6a020 <unit>~1` — the landing is present in the parent. Not recorded: `gotchas.py --report`, which the return says had no dedicated run, and `gotchas.py --for-paths`
- AC31 — `DESIGN_RECORD_PRESET` — unit 25's verdict record, at that unit's later commit, reads `DESIGN_RECORD_PRESET` at `tools/workflows/review_pin.py:47` and the template default `'unit-spec'` at `tools/workflows/tier2-review.template.js:330`. Not recorded at this commit: the probe's output and the count of `replay 1` lines
- AC32 — `git merge-base --is-ancestor af3831a6c <unit>~1` — the landing is present in the parent, and the return records the `extract_tag_ref` probe returning the expected value
- AC33 — `grep -c "LENS_SLOTS = " check-verifier-fanout.js` — it printed 1, and the `measureSlots` and `MAX_LENSES` greps printed 0 and 0
- AC34 — `git merge-base --is-ancestor b21501741 <unit>~1` — the landing is present in the parent. Not recorded: the `measure_design_recall` result, which the return lists among its probes with no output
- AC35 — `grep -c "legManifest" tier2-review.js` — it printed 0. Not recorded: the `gateManifest:` key line in the args header
- AC36 — `git grep -n "run before a review\|Before a review, run\|Hand a reviewer the classes" -- tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/guides/MERGE-BAR.md memory/guides/SESSION-KICKOFF.md` — at the tip `948e4141b` it prints nothing. `memory/HYGIENE.md` and its template name the harness acquiring the classes at :775, and the kickoff manifest at :100. The merge bar guide says at :94 that the review harness acquires the checklist on the diff kind
- AC37 — `python review_pin.py --subject 'memory\builds\dX\spec\2026-01-01-spec-TOOL-dX-1.md'` — at the tip `948e4141b` it exits 2 and its stderr names the backslash
- AC38 — `git merge-base --is-ancestor c70d6a020 <unit>~1` — the landing is present in the parent. Not recorded: the `lensNotes` prelude probe, which the return says had no dedicated run
- AC39 — `deriveAddressKey` — a stub runner over the render passed the address-key cases at the tip and failed them over the parent render
- AC40 — `walks` — a stub runner over the render passed the grid-ceiling cases at the tip and failed them over the parent render
- AC41 — `build_merged_returns` — sliced and read for `MT_MERGED`, it gave 13 dispositions with every item graded. Not recorded: the `build_merged_returns '[]' 0` and `build_merged_returns absent` cases

## Supersessions

Each one is named by the later unit's spec and recorded here in `TOOL-dFairHearing-23`'s own supersession form.

- `TOOL-dFairHearing-23` AC9 — the label half is answered by `TOOL-dFairHearing-26` AC1 to AC3. The marker-count half, over `gov:fixed-verifiers` and `gov:sequential-agents`, stands
- `TOOL-dFairHearing-23` S26 and AC17 — the `WHOLE_RUN` row and AC17's foreign-prefix half are superseded by `TOOL-dFairHearing-27` S4
- `TOOL-dFairHearing-23` S35 — the sentence "every line matching the renderer's own anchored marker regex" is superseded by `TOOL-dFairHearing-27` S1
- `TOOL-dFairHearing-23` Design — the middle row of the tag-reader table is superseded by `TOOL-dFairHearing-27` S6, and "lifted unchanged" by its S9
- `TOOL-dFairHearing-23` S12 and AC6 — "restored to base `3708a705`'s value" and AC6's base are superseded by `TOOL-dFairHearing-27` S15
- `TOOL-dFairHearing-23` S18 — the `rev-list --count` check is superseded by `TOOL-dFairHearing-27` S22
- `TOOL-dFairHearing-23` S21 — the single physical line is superseded by `TOOL-dFairHearing-27` S11
