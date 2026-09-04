#!/usr/bin/env bash
# unattended-build.test.sh - arms for the build harness. TOOL-dBriefedPass-4.
#
# WHAT CAN AND CANNOT BE ARMED HERE, said first because the boundary is unusual. A workflow script is
# not executable outside the Workflow runtime: it has no filesystem and its `agent`, `phase`, `log`
# and `workflow` hooks are injected by that runtime. So the GUARDS are driven by evaluating the file
# as the runtime does — the AsyncFunction shape `check-workflow-syntax.js` documents, with stub hooks
# — and the STRUCTURAL claims are asserted over the file's own text.
#
# Asserting over text is weaker than executing and is used only where executing cannot reach: whether
# an `agent(` sits inside a loop is a property of the source, and it is the property `agent-cap.js`
# itself judges from the source.
KIT_REL="${KIT_REL:-tools}"
set -u
st=0; n=0
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
F="$HERE/unattended-build.js"
[ -f "$F" ] || { echo "FAIL cannot find unattended-build.js beside this test"; exit 2; }

same() { n=$((n+1)); if [ "$2" = "$3" ]; then echo "ok   $1"; else echo "FAIL $1 -- got '$2' want '$3'"; st=1; fi }
has()  { n=$((n+1)); case "$2" in *"$3"*) echo "ok   $1" ;; *) echo "FAIL $1 -- output lacked '$3'"; st=1 ;; esac }
hasnt_(){ n=$((n+1)); case "$2" in *"$3"*) echo "FAIL $1 -- output carried '$3' and must not"; st=1 ;; *) echo "ok   $1" ;; esac }

# ---------------------------------------------------------------------------------------------
# THE RUNNER. Evaluates the script the way its runtime does, with stub hooks that RECORD rather than
# spawn. `$1` is a JS expression for `args`; `$2` is a JS object literal mapping a stage label prefix
# to the value its agent returns, or the string `null` to simulate a dead stage.
run_wf() { # args-expr · returns-expr -> prints the trace, then RESULT/THROW
  node -e '
    const fs = require("fs")
    const src = fs.readFileSync(process.argv[1], "utf8").replace(/^\s*export\s+const\s+meta\s*=/m, "const meta =")
    const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
    const trace = []
    const returns = JSON.parse(process.argv[3])
    const agent = async (prompt, opts) => {
      const label = (opts && opts.label) || "(unlabelled)"
      trace.push("agent:" + label)
      // TOOL-aStagedLane-2 - THE PROMPT IS TRACED, not just the label. The whole defect this unit
      // closes is what the agent is TOLD to run: the unattended BUILD prompt names three driver verbs
      // that refuse without a run-state file, and no gate downstream of here reads a prompt. A double
      // recording only labels cannot see the difference between the two modes at all.
      trace.push("prompt:" + label + ":" + String(prompt).replace(/\n/g, " "))
      for (const k of Object.keys(returns)) if (label.indexOf(k) === 0) return returns[k]
      return null
    }
    const phase = (t) => trace.push("phase:" + t)
    const log = (m) => trace.push("log:" + m)
    // TOOL-aStagedLane-3 - `parallel` must RUN its thunks. The stub returned [] and recorded a
    // trace line, which was harmless while nothing in this file fanned out; with a real fan it would
    // make every spec arm grade a stage that never spawned an agent, and they would all pass. A
    // double that cannot perform the thing under test is the fixture-passes-by-finding-nothing class
    // one level up, in the harness rather than in the subject.
    const parallel = async (thunks) => {
      trace.push("parallel:" + (Array.isArray(thunks) ? thunks.length : 0))
      return Promise.all((thunks || []).map((t) => t()))
    }
    const pipeline = async () => { trace.push("pipeline"); return [] }
    // TOOL-dRatifiedSeam-1. The AUDIT verdict now comes from a SUB-WORKFLOW rather than from an
    // agent, so this double has to be able to return one. It returned a bare `{}` while `workflow`
    // was unreachable, and a double that cannot produce the value under test grades nothing.
    const workflow = async (ref, wargs) => {
      trace.push("workflow:" + ((ref && ref.scriptPath) || String(ref)))
      return returns["workflow"] || {}
    }
    const budget = { total: null, spent: () => 0, remaining: () => Infinity }
    const fn = new AsyncFunction("args", "agent", "parallel", "pipeline", "phase", "log", "budget", "workflow", src)
    fn(JSON.parse(process.argv[2]), agent, parallel, pipeline, phase, log, budget, workflow)
      .then((r) => { console.log(trace.join("\n")); console.log("RESULT " + JSON.stringify(r)) })
      .catch((e) => { console.log(trace.join("\n")); console.log("THROW " + e.message) })
  ' "$F" "$1" "$2" 2>&1
}

UNITS='{"repo":"/tmp/r","slug":"tB","subjects":[{"path":"s1","blob":"abc1234"},{"path":"s2","blob":"def5678"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1"},{"id":"A-tB-2","order":1,"specPath":"s2","briefPath":"b2"},{"id":"A-tB-3","order":2,"specPath":"s3","briefPath":"b3"}]}'
SPEC_OK='{"authored":["A-tB-1"],"alreadyPresent":["A-tB-2","A-tB-3"],"refused":[],"summary":"ok"}'
BUILD_OK='{"committed":["A-tB-1","A-tB-2","A-tB-3"],"unbuilt":[],"summary":"ok"}'
# THE DOUBLE RETURNS THE CALLEE'S REAL KEYS, and the first version of it did not. It invented
# `verdict` and `reportPath`, so all 28 arms passed on two fields `tier2-review.js` has never
# returned — the harness and its callee had never met. Its actual returns carry `blockers`,
# `report`, `highs`, `note` and `precision`; there is no `verdict` anywhere but per-FINDING.
review_out() { printf '{"blockers":%s,"report":"r.md","highs":0,"precision":1,"note":"n"}' "$1"; }
# The CONVERGENCE token is the driver's, recorded by an agent, so it is a separate fixture. Keeping
# them separate is the point: a run can produce a clean review and still not converge.
rec() { printf '{"token":"%s","exitCode":0}' "$1"; }
# `audit <token> <blockers>` still reads as one thing at the call sites, but it now feeds the two
# halves their own shapes.
returns() { printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"build:":%s}' \
  "$SPEC_OK" "$(review_out "${2:-0}")" "$(rec "$1")" "$BUILD_OK"; }
audit() { printf '%s' "$1"; }

# ---- AC2: THE ARGS GUARD, BOTH DIRECTIONS. The first cut of the guard this ports from tested
# ---- `typeof a !== "object"` and refused every legitimate caller, so the PASSING case is armed.
# A PROSE STRING and a JSON-STRING-CARRYING-AN-OBJECT take DIFFERENT refusal paths, and both are
# armed: the first cannot be parsed at all, the second parses and then fails the repo check. An arm
# over only one of them would leave the other's branch unexercised.
o=$(run_wf '"just a prose string"' '{}')
has "args: unparseable prose is REFUSED at the parse" "$o" "could not parse the string given"
o=$(run_wf '"{\"slug\":\"tB\"}"' '{}')
has "args: a JSON STRING with no repo parses, then is REFUSED" "$o" "must carry an explicit \`repo\`"
o=$(run_wf '{"slug":"tB","units":[{"id":"A-tB-1"}]}' '{}')
has "args: an object with no repo is REFUSED" "$o" "must carry an explicit \`repo\`"
o=$(run_wf '{"repo":"/tmp/r","units":[{"id":"A-tB-1"}]}' '{}')
has "args: an object with no slug is REFUSED" "$o" "must carry an explicit \`slug\`"
o=$(run_wf '{"repo":"/tmp/r","slug":"tB","units":[]}' '{}')
has "args: an empty unit set is REFUSED rather than reported clean" "$o" "carries no \`units\`"
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
has "args: a VALID object is accepted — the passing case" "$o" "RESULT"

# ---- AC3: THE STAGE ORDER, asserted on the emitted sequence. A reordering reds this.
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
seq=$(printf '%s\n' "$o" | grep '^phase:' | tr '\n' ' ')
same "stage order is Spec then Audit then Build" "$seq" "phase:Spec phase:Audit phase:Build "

# ---- AC7: THE GATE ON THE VERDICT, over all four driver states. A gate tested only on the state
# ---- that OPENS it is a gate nothing proved closes.
o=$(run_wf "$UNITS" "$(returns CONVERGING 3)")
has "CONVERGING: BUILD is not reached" "$o" "HELD AT AUDIT"
n=$((n+1)); case "$o" in *"phase:Build"*) echo "FAIL CONVERGING reached the Build phase, which is the one thing this gate exists to stop"; st=1 ;; *) echo "ok   CONVERGING: the Build phase never ran" ;; esac
has "CONVERGING: the caller is told what to do next" "$o" "re-invoke this harness with round"
for v in CONVERGED NON-CONVERGENT CEILING; do
  o=$(run_wf "$UNITS" "$(returns "$v" 0)")
  n=$((n+1)); case "$o" in *"phase:Build"*) echo "ok   $v: admits BUILD" ;; *) echo "FAIL $v did not admit BUILD, so a terminal verdict cannot land a build"; st=1 ;; esac
done

# ---- TOOL-dRatifiedSeam-1. THE STAGE THAT COULD NEVER COMPLETE ------------------------------
# The AUDIT stage used to order a SIDECHAIN agent to invoke the Workflow tool, which a sidechain
# does not hold. The stage could not complete, BUILD was unreachable, and the harness named a
# route that did not run. These arms grade the fixed shape: the spawn happens in the SCRIPT.

# S1 — the sub-workflow is invoked BY THIS SCRIPT, and the trace names which one. Without this,
# every arm below could pass over a harness that reached BUILD by some other path entirely.
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
has "S1 the AUDIT stage invokes tier2-review as a SUB-WORKFLOW from the script" "$o" \
    "workflow:tools/workflows/tier2-review.js"

# S3 — CONVERGING paired with 0 blockers is REFUSED BY NAME. A loop with nothing left to
# converge on has converged, so the pairing is this repo's signature for a record no verb
# produced — and it is exactly what the dead stage returned.
o=$(run_wf "$UNITS" "$(returns CONVERGING 0)")
has "S3 CONVERGING with 0 blockers THROWS" "$o" "THROW"
has "S3 ...and the refusal names the pairing rather than a generic failure" "$o" \
    "CONVERGING paired with 0 blockers"
n=$((n+1)); case "$o" in
  *"phase:Build"*) echo "FAIL S3 the impossible pairing still reached BUILD"; st=1 ;;
  *) echo "ok   S3 ...and BUILD is not reached" ;;
esac

# S2 — A NON-INTEGER BLOCKER COUNT IS A DEGRADED RUN AND IS REPORTED AS ONE. tier2-review yields
# `null` there BY DESIGN, never 0, so reading it as 0 would make every degraded audit look clean:
# unattended.sh emits CONVERGED only on a count of 0.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":{"blockers":null,"report":"r.md"},"audit:record":%s,"build:":%s}' \
    "$SPEC_OK" "$(rec CONVERGED)" "$BUILD_OK")")
has "S2 a null blocker count THROWS rather than rounding to zero" "$o" "non-integer blocker count"
n=$((n+1)); case "$o" in
  *"phase:Build"*) echo "FAIL S2 a degraded audit reached BUILD"; st=1 ;;
  *) echo "ok   S2 ...and a degraded audit does not reach BUILD" ;;
esac

# THE SUBJECT GUARD. An unpinned subject audits whatever the file happens to say when the lens
# reads it, which is not a review of anything in particular — and tier2-review would refuse it
# downstream with a message about its own arguments rather than about which stage failed.
o=$(run_wf "${UNITS/\"blob\":\"abc1234\"/\"blob\":\"nothex\"}" "$(returns CONVERGED 0)")
has "an unpinned subject blob is REFUSED before the sub-workflow runs" "$o" "7-40 hex blob"

# ---- AC9: A DEAD AUDIT STAGE IS A REFUSAL, never a silent pass to BUILD. This is the absence that
# ---- would otherwise let the harness build on an unreviewed spec set.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"build:":%s}' "$SPEC_OK" "$BUILD_OK")")
has "a dead AUDIT stage THROWS" "$o" "THROW"
has "the throw says an absent verdict is not a convergence" "$o" "must never read as CONVERGED"
o=$(run_wf "$UNITS" "$(printf '{"workflow":%s,"audit:record":%s,"build:":%s}' "$(review_out 0)" "$(rec CONVERGED)" "$BUILD_OK")")
# The message moved with TOOL-aStagedLane-3: the stage is a FAN now, so the refusal is keyed on
# the live WRITER COUNT rather than on a falsy return. The arm follows the message rather than
# the message being frozen for the arm — `arm-literal-strands-on-message-edit`, met head on.
has "a dead SPEC stage THROWS rather than auditing nothing" "$o" "EVERY spec writer returned nothing"

# ---- AC6: A DEGRADED RUN SAYS SO. `degradation-known-but-unreported` is the class where a pipeline
# ---- computes how badly it degraded and does not report it.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"build:":%s}' \
    '{"authored":[],"alreadyPresent":["A-tB-1"],"refused":["A-tB-2","A-tB-3"],"summary":"s"}' \
    "$(review_out 0)" "$(rec CONVERGED)" \
    '{"committed":["A-tB-1"],"unbuilt":["A-tB-2","A-tB-3"],"summary":"s"}')")
has "a degraded run reports DEGRADED, not complete" "$o" "DEGRADED"
has "the refused units are NAMED, not merely counted" "$o" "A-tB-2"

# ---- AC4: NO agent() IN A LOOP AND NO FAN-OUT PRIMITIVE, asserted over the file's own text. This is
# ---- the property `agent-cap.js` judges, and the shape TOOL-cBriefedPilot-21's ratified
# ---- `parallelism route: none` requires. The hook's own verdict is the second arm.
# NO no-op arm here. A counted `n=$((n+1))` with an empty body was written first and removed: it
# incremented the total and asserted nothing, which is `memory/gotchas/fixture-passes-by-finding-
# nothing` in the very suite that grades a harness. Whether a loop encloses an `agent(` is judged by
# the hook below, which is the authority on that predicate, rather than by a regex here that would be
# a second and weaker implementation of it.
# SCOPED AT TOOL-aStagedLane-3, which made the SPEC stage a bounded fan. The blanket ban encoded
# the pre-unit-3 design. `TOOL-cBriefedPilot-21`'s ratified `parallelism route: none` is about
# BUILD DISPATCH: it failed on E4, two passes COMMITTING without racing one index, and the spec
# writers author and never commit. What must still hold is that any fan-out is MARKED and BOUNDED,
# which the hook below judges, and that BUILD dispatch stays sequential, which the next arm asserts.
n=$((n+1)); if grep -q "out.push(...(await parallel(" "$F"; then
  echo "ok   the only fan-out primitive is the marked slice inside boundedParallel"
else
  echo "FAIL a fan-out primitive is called outside the bounded helper"; st=1
fi
n=$((n+1)); if grep -q "ONE AT A TIME and IN THIS ORDER" "$F"; then
  echo "ok   BUILD dispatch is still strictly sequential"
else
  echo "FAIL the BUILD stage no longer tells its agent to work one unit at a time"; st=1
fi
if [ -f "$ROOT/tools/hooks/agent-cap.js" ]; then
  o=$(printf '{"tool_name":"Workflow","tool_input":{"scriptPath":"tools/workflows/unattended-build.js"}}' \
      | (cd "$ROOT" && node $KIT_REL/hooks/agent-cap.js 2>&1); echo "rc=$?")
  n=$((n+1)); case "$o" in *"rc=0"*) echo "ok   agent-cap ADMITS the harness" ;; *) echo "FAIL agent-cap denied the harness -- $o"; st=1 ;; esac
else
  echo "SKIP agent-cap admission — no hook at $ROOT/tools/hooks/agent-cap.js, so this arm was NOT exercised"
fi

# ---- AC5: the AUDIT stage must name the spec-audit kind. `tier2-review.js` DEFAULTS an absent kind
# ---- to `diff-review`, which primes code-shaped lenses at a spec and reports it as a review.
n=$((n+1)); grep -qE "kind: ['\"]spec-audit['\"]" "$F" \
  && echo "ok   the audit prompt names kind: \"spec-audit\"" \
  || { echo "FAIL the audit prompt does not name the spec-audit kind, so tier2-review would default to diff-review"; st=1; }

# ======================================================= TOOL-aStagedLane-2 — THE ATTENDED MODE
# The two modes differ in WHAT THEY TELL THEIR AGENTS and in which driver calls they make. Both are
# properties of the composed prompt and the call trace, which is why these arms read the trace rather
# than a return value.

# ---- AC2: the DEFAULT is unchanged. Every existing caller keeps the contract it had.
o=$(run_wf "$UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"build":{"committed":["A-tB-1"],"unbuilt":[],"summary":"b"}}')
has  "default mode: the round IS recorded through the driver" "$o" "agent:audit:record"
has  "default mode: the BUILD prompt still names --dispatch" "$o" "--dispatch"
has  "default mode: reaches BUILD" "$o" "agent:build:tB"

# ---- AC1: attended mode reaches BUILD and spawns NO recorder agent.
A_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1","planState":"READY"}]}'
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"build":{"committed":["A-tB-1"],"unbuilt":[],"summary":"b"}}')
has   "attended: reaches the build stage" "$o" "agent:build:tB"
hasnt_ "attended: no round is recorded through the driver" "$o" "agent:audit:record"
has   "attended: it SAYS the round was not recorded" "$o" "no round was recorded"

# ---- AC8: the BUILD prompt drops the verbs that refuse without a run-state file — AND still carries
# ---- the surrounding instruction. The paired positive is the point: an absence assertion passes just
# ---- as well when the whole clause is empty.
hasnt_ "attended prompt: no --dispatch INSTRUCTION" "$o" "--dispatch tB"
# The verbs are NAMED in the attended prompt, to say they are unavailable. The assertion must
# therefore target the INSTRUCTION form `--brief <slug>`, not the word — an absence arm aimed at
# the word fails on the sentence explaining the absence.
hasnt_ "attended prompt: no --brief INSTRUCTION" "$o" "--brief tB"
has   "attended prompt: the per-unit build instruction SURVIVES" "$o" "BUILD every unit below, ONE AT A TIME"
has   "attended prompt: it says why the verbs are absent" "$o" "recording verbs are unavailable"

# ---- AC9: no agent is told it holds a mandate. In this repo a mandate IS the authority to merge and
# ---- push with no owner turn, so the unattended preamble is a falsehood in attended mode.
hasnt_ "attended preamble: the word 'mandate' does not reach any agent" "$o" "under a mandate"
has   "attended preamble: it says an owner is in the loop" "$o" "OWNER in the loop"

# ---- AC10: both live verdict branches. A branch mapping a positive count to terminal would reach
# ---- BUILD over open blockers and satisfy every other criterion here.
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":2,"report":"r.md"}}')
has   "attended, 2 blockers: CONVERGING" "$o" "CONVERGING"
hasnt_ "attended, 2 blockers: BUILD is NOT reached" "$o" "agent:build:tB"

# ---- AC3: a null blocker count REFUSES in attended mode too. tier2-review.js yields null on its
# ---- degraded paths BY DESIGN, and reading it as 0 would make every degraded audit look clean.
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":null,"report":"r.md"}}')
has  "attended, null blockers: REFUSES" "$o" "THROW"
has  "attended, null blockers: names the degraded return" "$o" "DEGRADED"

# ---- AC4: a FORKED unit refuses, and the message names both the id and the state. The bare token is
# ---- supplied directly: --plan rewrites a terminal unit's grade to `DONE (FORKED)`, so a bare FORKED
# ---- and a real closed build's roster are jointly unsatisfiable.
F_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"FORKED"}]}'
o=$(run_wf "$F_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"}}')
has  "attended, FORKED unit: refuses" "$o" "THROW"
has  "attended, FORKED unit: names the id" "$o" "A-tB-1"
has  "attended, FORKED unit: names the state" "$o" "FORKED"

# ---- AC11: the terminal-unit SKIP, with the vocabulary --plan actually emits. `DONE (FORKED)` is
# ---- what a closed build reports for a unit whose underlying grade was not READY, and a five-token
# ---- allow-list halts on it — round-1's halt-at-unit-one, for the third time.
D_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"DONE (FORKED)"},{"id":"A-tB-2","order":2,"specPath":"s2","planState":"DONE"}]}'
o=$(run_wf "$D_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"build":{"committed":[],"unbuilt":[],"summary":"b"}}')
has  "attended, DONE (FORKED): SKIPPED, not refused" "$o" "SKIPPING 2 terminal unit"
has  "attended, terminal units: still reaches BUILD" "$o" "agent:build:tB"

# ---- AC13: a state outside every arm refuses BY NAME. Neither building nor skipping an unknown state
# ---- is safe, and this vocabulary has been mis-transcribed twice already.
X_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"WOBBLE"}]}'
o=$(run_wf "$X_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"}}')
has  "attended, unknown state: refuses" "$o" "THROW"
has  "attended, unknown state: names the value it did not recognise" "$o" "WOBBLE"

# ---- AC12: a missing planState refuses rather than defaulting. A defaulted state puts the refusal
# ---- predicate to work on a value nobody supplied.
M_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1"}]}'
o=$(run_wf "$M_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"}}')
has  "attended, no planState: refuses" "$o" "THROW"
has  "attended, no planState: names the field" "$o" "planState"

# ---- AC14: the FRESH-BUILD path. A unit stage 1 authors reports MISSING at entry — there is no point
# ---- between the stages at which a caller could re-run --plan — so the entry-time value is stale by
# ---- construction and the stage must not refuse the build it just specced.
N_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"MISSING"}]}'
o=$(run_wf "$N_UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"build":{"committed":["A-tB-1"],"unbuilt":[],"summary":"b"}}')
has  "attended, unit specced THIS invocation: builds despite entry-time MISSING" "$o" "agent:build:tB"
# and the control: the same MISSING state, NOT specced by stage 1, must still refuse.
o=$(run_wf "$N_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":["A-tB-1"],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"}}')
has  "attended, MISSING and NOT specced: still refuses" "$o" "THROW"

# ---- S1: the mode is a CLOSED pair. A typo must not fall back to a default that hands the caller
# ---- fewer checks than they asked for.
B_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attnded","units":[{"id":"A-tB-1","order":1}]}'
o=$(run_wf "$B_UNITS" '{}')
has  "bad mode: refuses rather than defaulting" "$o" "THROW"
has  "bad mode: names the closed set" "$o" "unattended, attended"

# ---- S7: the warning depends on a CALLER-SUPPLIED fact, because this script has no filesystem. A
# ---- caller that supplies nothing gets no warning, which is a hole the header names rather than one
# ---- a reader has to infer.
W_UNITS='{"repo":"/tmp/r","slug":"tB","mode":"attended","runStateExists":true,"subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"READY"}]}'
o=$(run_wf "$W_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"build":{"committed":["A-tB-1"],"unbuilt":[],"summary":"b"}}')
has  "attended + run-state file: WARNS" "$o" "WARNING: attended mode was requested"
has  "attended + run-state file: names the slug" "$o" "tB"
has  "attended + run-state file: CONTINUES to build" "$o" "agent:build:tB"

# ---- The run-integrity note must SAY the run was attended. A pipeline that computes how weak its own
# ---- run was and returns a bare "complete" is the degradation-known-but-unreported class, and the
# ---- caller cannot otherwise tell an attended run from an unattended one by its return.
has  "attended: the note says which guarantee the caller actually got" "$o" "NOT the guarantee an unattended run gives"
has  "attended: the return carries the mode" "$o" "\"mode\":\"attended\""

# ---- AC6: the header names all five losses separately, and does not conflate a record with a
# ---- refusal. Asserted over the file's own text, which is where the honesty statement lives.
HDR=$(sed -n '1,110p' "$F")
has "header: names the --review round record" "$HDR" "ROUND RECORD"
has "header: names dispatch's order refusal" "$HDR" "ORDER REFUSAL"
has "header: names dispatch's write-set record" "$HDR" "WRITE-SET RECORD"
has "header: names --brief" "$HDR" "--brief"
has "header: names --rescope" "$HDR" "--rescope"
has "header: says M4's disposal clause is unreachable attended" "$HDR" "UNREACHABLE HERE"
has "header: says the S7 warning is caller-supplied, not detected" "$HDR" "DEPENDS ON THE CALLER AND NOT ON DETECTION"

# ================================================== TOOL-aStagedLane-3 — THE SLICED SPEC FAN
# The spec stage fans one writer per GROUP of slices. Slices come from the caller, grouped by the
# `order` verb; the groups are what the cap bounds.

# ---- AC1: three slices at a cap of five chunk to groups of ONE, so three writers spawn and the
# ---- total never exceeds the cap.
S3='{"repo":"/tmp/r","slug":"tB","subjects":[{"path":"s1","blob":"abc1234"}],"units":[
  {"id":"A-tB-1","order":1,"specPath":"s1","specBriefPath":"bf1"},
  {"id":"A-tB-2","order":2,"specPath":"s2","specBriefPath":"bf2"},
  {"id":"A-tB-3","order":3,"specPath":"s3","specBriefPath":"bf3"}]}'
o=$(run_wf "$S3" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"build":{"committed":[],"unbuilt":[],"summary":"b"}}')
has "fan: three slices spawn three writers" "$o" "3 slice(s) -> 3 writer(s)"
has "fan: writer 0 spawned" "$o" "agent:spec:tB:g0"
has "fan: writer 2 spawned" "$o" "agent:spec:tB:g2"

# ---- AC2: a writer's prompt carries ITS OWN group's briefs and no brief from outside it.
has   "brief: writer 0 is handed its own unit's brief" "$o" "A-tB-1 -> bf1"
o0=$(printf '%s\n' "$o" | grep '^prompt:spec:tB:g0:')
hasnt_ "brief: writer 0 is NOT handed another group's brief" "$o0" "bf2"
hasnt_ "brief: writer 0 is NOT handed a third group's brief" "$o0" "bf3"

# ---- AC8: ABOVE the cap. Seven slices chunk to five groups, two of them carrying two slices, so a
# ---- writer legitimately holds MORE THAN ONE slice. AC1's three-slice case never leaves the regime
# ---- where "one writer per slice" and "one writer per group" agree, so without this arm the shape
# ---- that actually runs at the build sizes motivating the unit is untested.
S7='{"repo":"/tmp/r","slug":"tB","subjects":[{"path":"s1","blob":"abc1234"}],"units":[
  {"id":"A-tB-1","order":1,"specPath":"s1"},{"id":"A-tB-2","order":2,"specPath":"s2"},
  {"id":"A-tB-3","order":3,"specPath":"s3"},{"id":"A-tB-4","order":4,"specPath":"s4"},
  {"id":"A-tB-5","order":5,"specPath":"s5"},{"id":"A-tB-6","order":6,"specPath":"s6"},
  {"id":"A-tB-7","order":7,"specPath":"s7"}]}'
o=$(run_wf "$S7" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"build":{"committed":[],"unbuilt":[],"summary":"b"}}')
# FOUR, not five, and not seven. `chunk(x, ceil(N/K))` chunks by SIZE, so 7 slices at a cap of 5
# give groups of 2 and therefore 4 groups. The RULE is that the writer total never EXCEEDS the
# cap, not that it equals it; asserting 5 would have been asserting my arithmetic, not the bound.
has   "above cap: seven slices become four writers, never seven" "$o" "7 slice(s) -> 4 writer(s)"
hasnt_ "above cap: no writer beyond the cap is ever spawned" "$o" "agent:spec:tB:g5"
has   "above cap: one wave, and it is at or under the cap" "$o" "parallel:4"

# ---- AC3: a unit with no specBriefPath falls back, and the fallback is LOGGED. A silent fallback and
# ---- a deliberate omission are indistinguishable, and a mistyped key would hand back the old
# ---- behaviour with no signal.
has "fallback: the unit with no brief is named" "$o" "A-tB-1 has no specBriefPath"

# ---- AC4: one dead writer is REFUSED, not dropped, and its siblings still return.
o=$(run_wf "$S3" '{"spec:tB:g0":null,"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"build":{"committed":[],"unbuilt":[],"summary":"b"}}')
has "one dead writer: reported as DEGRADED" "$o" "DEGRADED — 1 of 3 writer(s) returned nothing"
has "one dead writer: its unit lands in refused" "$o" "A-tB-1"
has "one dead writer: the stage still completes" "$o" "agent:build:tB"

# ---- AC4, second half: EVERY writer dead must THROW. The old guard was `if (!specced)` on a falsy
# ---- return, and a merged object is always truthy — so without this an entirely dead spec stage
# ---- reaches AUDIT and BUILD on whatever specs already existed, with the refusal this file spends
# ---- six lines justifying silently deleted.
o=$(run_wf "$S3" '{"spec":null,"workflow":{"blockers":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"build":{"committed":[],"unbuilt":[],"summary":"b"}}')
has   "ALL writers dead: THROWS" "$o" "THROW"
has   "ALL writers dead: says every writer returned nothing" "$o" "EVERY spec writer returned nothing"
hasnt_ "ALL writers dead: BUILD is never reached" "$o" "agent:build:tB"

# ---- AC7/S3c: the writers are told to AUTHOR and never COMMIT, and not to run the generator. That is
# ---- half of clause 3 of the disjointness proof, and no gate downstream of here reads a prompt.
o=$(run_wf "$S3" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"build":{"committed":[],"unbuilt":[],"summary":"b"}}')
has "writers: told to author and NOT commit" "$o" "AUTHOR ONLY — DO NOT COMMIT"
has "writers: told the caller commits once after them" "$o" "the caller commits once after all of you"
# AC9 - S4's generator prohibition, which had no criterion at all before this arm.
has "writers: told not to run the index generator" "$o" "do not run the build-index generator"

# ---- AC10/S3d: the file's own header no longer claims every stage is one agent, and says why the
# ---- ratified `parallelism route: none` verdict does not reach this fan.
HDR3=$(sed -n '1,120p' "$F")
has "header: the one-agent claim is scoped to BUILD" "$HDR3" "THE BUILD STAGE IS ONE AGENT"
has "header: it names the ratified verdict it does not contradict" "$HDR3" "parallelism route:"
has "header: it says why — the writers do not commit" "$HDR3" "author and never commit"

echo "--- $n arms, exit $st"
exit $st
