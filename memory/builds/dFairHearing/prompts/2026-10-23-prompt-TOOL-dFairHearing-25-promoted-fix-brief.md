**Serves:** research TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27

# Promoted-units fix brief, round two — one writer per unit, each its own files only

The round-2 spec audit (`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md`) promoted three units; `memory/builds/dFairHearing/RUN.md` carries their `rescope · item add` rows. Before the round-3 audit pins them, do YOUR unit's work, the unit your handoff names. Touch no other unit's files. The specs are uncommitted at rev-1 and unaudited: edit them in place, with no rev bump. Do not commit, stage, or run the build-index generator or any gate.

## 1. The spec-token hits (your unit's lines, verbatim below)

- **A `[path]` hit** is a backticked path-shaped token in §6 that `git ls-files` does not track. Cite a file the build run creates by BASENAME, or without a slash, in §6; full paths stay in §2 and §4. An adopter-side path such as `.governance/install.json` or `{prefix}/…` is written without a slash in §6, or moved to §4.
- **A `[bar]` hit** names a suite as an acceptance observation. Observe the checker on a staged break, a `--selftest` flag or a fixture instead, and name the suite on a `New arm:` line in §7.
- **A `[guards]` hit** means §4 Files touched names `tools/gate-legs.json`, whose guard trips legs your §7 leg line does not name. Either name each listed leg on the §7 leg line, or, if the unit does not need to touch `tools/gate-legs.json`, take it out of Files touched. Read `tools/gate-legs.json`'s guards to decide.

## 2. One departure record

Write it in the grammar of `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-20-deviation-201.md`:

- **Departs from:** `dFairHearing [roster]`
- **Hand-off:** `design-to-spec`
- **Cause:** `review finding`
- **Risk:** `additive`
- **Approver:** the spec writer, under `author-recorded` (`PLAY-dClosedLoop-4`)
- **Follow-through:** `new unit <id>`
- **Caused-by:** `PLAY-dClosedLoop-2`
- **Reason:** this is a spec run, so the unit is carried forward once (`UNATTENDED-STOPS.md` §15).
- **Evidence:** the round-2 audit record, its rescope add row, and its spec.

File it as `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<n>1.md`, that is `-deviation-251`, `-261` or `-271`.

Report every edit, and your spec's final byte size.

## The hits, verbatim
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md [path] `tools/workflows/spec-audit-optin.js` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md [path] `tools/workflows/review_pin.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-26.md [path] `tools/workflows/spec-audit-optin.test.sh` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-26.md [bar] `tools/workflows/spec-audit-optin.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-26.md [bar] `tools/workflows/check-review-join.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-26.md [bar] `tools/hooks/agent-cap.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md [path] `.governance/install.json` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md [path] `{prefix}/workflows/spec-audit-optin.js` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md [bar] `tier2-review.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md [bar] `tier2-review.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md [guards] `run-gates gov canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates gov canary', absent from the §7 leg line
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md [guards] `measure-legs selftest <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'measure-legs selftest', absent from the §7 leg line
