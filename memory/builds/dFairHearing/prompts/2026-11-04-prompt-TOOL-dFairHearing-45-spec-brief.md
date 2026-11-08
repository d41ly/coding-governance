# Spec brief — TOOL-dFairHearing-45: the bar's own reds in the kits

**Serves:** research TOOL-dFairHearing-45

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Write the spec for `TOOL-dFairHearing-45` at `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-45.md`. The close ran the bar's lint legs on this branch and on a frozen clone of BASE `8bec4cefd`. These legs pass at BASE and fail here, so the reds are this build's own and must clear before the full bar. This unit repairs every one of them outside `tools/workflows/replay_scorer.py`, which unit 46 owns. It builds after unit 43, which writes several of the same files, so ground it on unit 43's spec as well as on today's tree. Commit nothing; the main loop commits.

### Items
Run each leg's command from `tools/gate-legs.json` read-only to see its current output, then scope a fix for each:
1. **install-prefix (shipped surface):** kit-path spellings in `tools/hooks/README.md`, `tools/hooks/agent-cap.test.sh`, `tools/workflows/README.md`, `tools/workflows/check-verifier-fanout.test.sh`, `tools/workflows/lenses.toml`, `tools/workflows/tier2-review.template.js` and its render, and `tools/workflows/tier2-review.test.sh`. Prefer the install-prefix form. Waive only where the leg's waiver file is the right home, and remember those waivers are line-keyed.
2. **hook destinations:** `tools/workflows/spec-audit-optin.fragment.json` declares a hook path no `kit.toml` rule ships.
3. **docs:** `hook:spec-audit-optin` is anchored on no page under `help/`. Document it; do not list it as undocumented.
4. **shell hygiene (a fork spent on builtin work):** the counts risen in `tools/workflows/check-review-join.sh`, `tools/workflows/check-verifier-fanout.sh`, `tools/workflows/check-verifier-fanout.test.sh` and `tools/lib/resolve-python.test.sh`, and the unregistered sites in `tools/workflows/spec-audit-optin.test.sh`. Convert to the no-fork form where that is the honest fix.
5. **lexicon naming predicates and lexicon wiring:** 1220 verb offenders over a pin of 1211. Nine names are new and ten keys moved with unit 16's split of `agent-cap.js`. Rename the new ones with `tools/lexicon/lexicon.py --suggest`, and bring the count to the pin or below by the route the lexicon kit declares for moved keys, never by raising the pin.
6. **drift-audit records:** `tools/workflows/README.md` cites `PLAY-dClosedLoop-1`, a non-terminal spec, from product source. The set is shrink-only: remove the cause, never list it.
7. **playbook parity selftest:** the leg guard omits `{prefix}/workflows/check-verifier-fanout.js`, which its suite now reads.
8. **brief-recorded:** units 10 to 14 and 16 to 18 have build commits with no brief row, or a row whose hash no longer matches, in `memory/builds/dFairHearing/RUN.md`. Read the leg and `memory/project/brief-recorded-waiver.txt`, and scope the honest record. Those commits cannot change.

A `New arm:` line for any gate this unit adds or changes; each must name a break that reds on today's code. Check any generated file and its generator against the dispatch rule that refuses them together, and split the scope if they pair. Write the unit's departure record the way unit 43's deviation record was written, and carry `order 30`, no ask clause, as unit 43's design explains. Bump no kit version by hand unless the kit-epoch leg demands it, and say which.

### Acceptance
A spec conforming to `memory/TEMPLATE-SPEC.md`, with one criterion per leg that names the leg's own command and goes green on a correct build. Every criterion must be one a correct build can pass after unit 43. Check the acceptance section's backticked words against `tools/check-spec-tokens.py`'s `BAR` pattern (lines 419 to 424). Every change-log line names a section, a scope id or an acceptance id. New text cites no check, section or method rule by a bare number.

### Gates
None you run beyond those read-only leg commands.

### Non-goals
No code, no other spec, and nothing in `tools/workflows/replay_scorer.py`. Not the kickoff-manifest re-stamp, which the main loop does last.
