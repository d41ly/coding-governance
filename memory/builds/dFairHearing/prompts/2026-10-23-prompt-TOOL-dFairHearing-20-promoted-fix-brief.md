**Serves:** research TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23

# Promoted-units fix brief — tokens, size and departures for the four units the round-1 spec audit added

The round-1 spec audit's disposal promoted four units (`memory/builds/dFairHearing/RUN.md`'s four `rescope · item add` rows; the audit record `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`). Before the round-2 audit pins them, three things are owed. The specs are uncommitted at rev-1 and unaudited: edit in place, no rev bump.

## 1. The spec-token hits

Fix every hit below so `python tools/check-spec-tokens.py` reports none in these four specs, changing no meaning.
- A `[path]` hit is a backticked path-shaped token in §6 that `git ls-files` does not track.
- A file the build run creates, a `rev:path`, or an example literal is cited in §6 by BASENAME or without a slash.
- Full paths stay in §2 and §4.

## 2. The size ceiling

`TOOL-dFairHearing-23` is 51082 bytes against the 49152 spec ceiling (`tools/template-size-limits.txt`).

- **First, bring it under by moving nothing out of scope.** Tighten prose and drop repetition, keeping every finding id, criterion and seen-red case.
- **Only if that cannot reach the ceiling, split it in two.** Build method M4 admits a second batch unit ONLY when the minors split into two disjoint write sets. The new unit is a second batch unit under the next free id, at `memory/builds/dFairHearing/spec/2026-10-23-spec-a second batch unit under the next free id.md`, in the same shape. Name in your report exactly which finding ids and which product paths each half holds, so the main loop records the `rescope add`.

## 3. One departure record per added unit

Each unit this spec run added is a departure (README rule 1), written in the grammar of `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-23-deviation-22.md`:

- **Departs from:** `dFairHearing [roster]`
- **Hand-off:** `design-to-spec`
- **Cause:** `review finding`
- **Risk:** `additive`
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** `new unit <id>`
- **Caused-by:** `PLAY-dClosedLoop-2`
- **Reason:** that this is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Before / After:** the roster before and after.
- **Evidence:** the audit record, the rescope add row and the unit's spec.

File each as `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<n>1.md`, so unit 20's is `-deviation-201`, unit 21's `-deviation-211`, and so on.

## Rules for this pass

- Change nothing else in any spec.
- Do not commit, do not stage, and do not run the build-index generator or any gate; the main loop runs them.
- Report every edit, the new byte size of `TOOL-dFairHearing-23`, and whether you split it.

## The token hits, verbatim

- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-21.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-22.md [path] `tools/workflows/spec-audit-optin.js` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/review_pin.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `memory/builds/dX/build/d.md` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/render_lenses.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `3708a705:tools/hooks/agent-cap.test.sh` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/spec-audit-optin.test.sh` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `no/such/path.sh` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/spec-audit-optin.js` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `HEAD:tools/workflows/README.md` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/render_lenses.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `d=tomllib.load(open('tools/workflows/kit.toml','rb'));` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `memory/gotchas/portability-sweep.md` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `memory/gotchas/topology-sweep.md` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `memory/gotchas/adopter-migration-sweep.md` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/review_pin.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `('/x.md',` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/check-verifier-fanout.js` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/check-verifier-fanout.js` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [path] `tools/workflows/review_pin.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md [size] `size <- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md` — 51082 bytes, 1930 over the spec ceiling 49152; split the spec or move history out of it
