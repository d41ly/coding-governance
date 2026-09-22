# TOOL-dBriefedPass-4 — the harness, and the two shapes a hook forced on it

**Serves:** journal TOOL-dBriefedPass-4

*Node `d`, 2026-09-01, unattended prompt-mode run under a standing mandate.*

## What shipped, and what it is honestly worth

`tools/workflows/unattended-build.js` drives SPEC then AUDIT then BUILD as stages of one program.
BUILD is unreachable except through both and except on a TERMINAL `--review` verdict. That is the
whole mechanism and it is JS control flow, so it holds across a context that compacts — which is
precisely what the prompt reports as broken.

It buys nothing else, and the file says so in its own header. A Workflow script has no filesystem, so
every observation it could make is a claim its own agent returned. The refusals live in
`TOOL-dBriefedPass-3`: `--dispatch` at the moment of the act, and the `pass-order history` leg over
the commit graph.

## Two shapes are FORCED, and both came from one denial

`tools/hooks/agent-cap.js` refuses an `agent()` inside any loop body, unconditionally — its whitelist
is closed and names no marker for the case. Measured by running the hook's own predicate over two
successive drafts; it denied every loop site, calling a strictly sequential `await agent(...)` "a
loop-built thunk array".

The conflict is exact and is PARKED for the owner: **bounded-parallel fan-out is permitted by the
hook and forbidden by the ratified `parallelism route: none`; sequential dispatch is required by that
verdict and forbidden by the hook.** A harness iterating a build's units sits in the gap.

1. **Each stage is ONE agent** holding the ordered unit list, not one per unit. Stage order stays
   structural; per-unit order moves onto `--dispatch`'s refusal, which reads the tree and is a
   stronger check than a JS loop rather than a weaker one.
2. **The convergence LOOP lives in the caller and the harness holds the GATE.** A convergence loop's
   iteration count is data-dependent, so unlike case 1 there was no bounded unroll. `CONVERGING`
   returns without reaching BUILD. The owner's ruling survives where it matters — the verdict
   decides, and no round cap exists anywhere in the file.

I did not restructure the call into a helper the loop invokes. That would be textually
indistinguishable from the evasion the rule names, and passing a checker by indirection is worse than
not passing it.

## Evidence

**Evidences:** TOOL-dBriefedPass-4
- AC1 — `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js` exits 0,
  matching the argv `tools/workflows/kit.toml` declares; `bash` on the same file exits 2, which is
  round 1's finding L1 confirmed rather than assumed. And `node tools/hooks/agent-cap.js` ADMITS the
  file when handed a Workflow call naming it — exit 0, after denying two earlier drafts.
- AC2 — `tools/workflows/unattended-build.test.sh` — five refusal arms and one PASSING arm. Two
  refusal paths are armed separately because they are different branches: unparseable prose fails at
  the parse, a JSON string carrying an object parses and then fails the `repo` check.
- AC3 — same suite — the emitted phase sequence is exactly `phase:Spec phase:Audit phase:Build`,
  asserted as a whole string so a reordering reds it.
- AC4 — same suite — no `parallel(`/`pipeline(` call anywhere in the file, plus the hook's own
  verdict as the second arm. A regex for "an `agent(` in a loop" was deliberately NOT written: the
  hook is the authority on that predicate and a second implementation would be a weaker one.
- AC5 — same suite — the audit prompt names `kind: "spec-audit"`. `tier2-review.js` defaults an
  absent kind to `diff-review`, which would prime code-shaped lenses at a spec and report it as a
  review, which is the failure M4 exists to prevent.
- AC6 — `bash tools/workflows/unattended-build.test.sh` — a run whose spec stage refused two units and whose build stage left them
  unbuilt returns `DEGRADED` and NAMES them. `degradation-known-but-unreported` is the class.
- AC7 — same suite, four arms over the driver's four states — `CONVERGING` returns `HELD AT AUDIT`
  and the Build phase never runs; `CONVERGED`, `NON-CONVERGENT` and `CEILING` each admit BUILD. The
  closing arm matters as much as the opening one: a gate tested only on the state that opens it is a
  gate nothing proved closes.
- AC8 — the harness returns `round`, and the caller's loop is bounded by convergence. The
  round-count-non-zero arm rev-4 asked for is subsumed: with the loop in the caller, an invocation
  that reaches BUILD has by construction run exactly one audit.
- AC9 — `bash tools/workflows/unattended-build.test.sh` — a dead AUDIT stage THROWS naming "must never read as CONVERGED"; a dead SPEC
  stage THROWS rather than auditing a set nothing confirmed exists.
- AC10 — `python3 tools/codebase-map/test_codebase_map.py` exits 0 with the script present. Observed
  RED first: `UNCLAIMED (new key? claim it in a feature dossier...) {'workflow-scripts':
  ['unattended-build.js']}`. Claimed in `memory/map/features/unattended.md` with its prose refreshed
  and the generated artifacts regenerated.

## Two things this pass changed that were not in the plan

**`renderRoster` exists because the map's JS layer required it.** `map_lib.scan_js_definitions`
RAISES on a JS file yielding no top-level definition rather than indexing less of it — the comment
says that is how the layer once went 30-to-3 unseen. The harness was straight-line code with only
anonymous callbacks. The verb comes from `python3 tools/lexicon/lexicon.py --suggest`, which refused
`produce` and offered the declared table; `render` is in it.

**Spec 4 went to rev-5 before either shape changed**, which is M2's route for a divergence. The spec
had specified one agent per unit and a harness-side convergence loop, and both were unbuildable
against the hook. Changing the code first and the spec after would have been the exact defect this
build exists to remove, in the unit that builds the machinery for removing it.

## What this pass did NOT verify

The harness has never RUN. Its stages are exercised through the runtime's own AsyncFunction shape
with stub hooks that record instead of spawning, which reaches every guard, the stage ordering, the
verdict gate and the degradation reporting — but not a single real agent. Driving it live is a build
of its own and is not claimed here.

No gate leg was added for `unattended-build.test.sh`. The sibling `tier2-review self-test` is one
(`chunk: selftests`, guarded to `tools/workflows/`), so the asymmetry is deliberate rather than
overlooked: spec 4 S8 asks for the arms and not for a leg, and adding one is a five-declaration act
that belongs to a unit that specced it.
