**Serves:** research TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37

# Promoted-units fix brief, round four — one writer per unit, each its own files only

The round-4 spec audit (`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`) promoted five units; `memory/builds/dFairHearing/RUN.md` carries their `rescope · item add` rows. Do YOUR unit's row, the unit your handoff names, and touch no other file. The specs are uncommitted at rev-1 and unaudited: edit in place, with no rev bump. Do not commit, stage, or run the build-index generator or any gate.

## Every unit — one departure record

Write it in the grammar of `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-28-deviation-281.md`, the same fixed fields:

- **Departs from:** `dFairHearing [roster]`
- **Hand-off:** `design-to-spec`
- **Cause:** `review finding`
- **Risk:** `additive`
- **Approver:** the spec writer, under `author-recorded` (`PLAY-dClosedLoop-4`)
- **Follow-through:** `new unit <id>`
- **Caused-by:** `PLAY-dClosedLoop-2`
- **Reason:** names the round-4 finding(s) it closes, and says this is a spec run, so the unit is carried forward once (`UNATTENDED-STOPS.md` §15).
- **Evidence:** the round-4 audit record, the rescope add row, and the spec.
- **Before:** names only specced units (1 to 18, 20 to 23 and 25 to 32): there is no unit 19 spec and no unit 24.

File it as `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<n>1.md`, that is `-331`, `-341`, `-351`, `-361` or `-371`.

## Per unit

- **TOOL-dFairHearing-33, -34, -35** — the departure record only.
- **TOOL-dFairHearing-36** — `check-spec-tokens.py` reports two `[bar]` hits in its §6: it names `tools/workflows/check-review-join.test.sh` and `spec-audit-optin.test.sh` as acceptance observations. A suite is never one: observe the checker on a staged break, a `--selftest` flag or a fixture, refer to each suite by a short name §2 defines (as `TOOL-dFairHearing-26` did), and name each suite on a `New arm:` line in §7. Then the departure record.
- **TOOL-dFairHearing-37** — one `[path]` hit in §6: `tools/workflows/replay_scorer.py` is not tracked by `git ls-files`. Cite it by basename in §6; the full path stays in §2 and §4. Then the departure record.

Report each edit verbatim.
