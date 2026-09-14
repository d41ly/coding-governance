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
# THE CHILD IS IN THIS SUITE'S SCOPE, and it has no suite of its own. The parent hands out a roster
# and the child builds one unit off it, so the two halves of the mode contract — the parent PUTTING
# the mode in `dispatch.args` and the child BRANCHING on it — are one property split across two
# files. Arming only the parent's half is what let the child go mode-blind. Both paths are derived
# from `$HERE`, so nothing here spells an install prefix.
C="$HERE/unattended-unit.js"
[ -f "$C" ] || { echo "FAIL cannot find unattended-unit.js beside this test"; exit 2; }
# The driver, for the DERIVED refusal set the child arms read. `$KIT_REL` above is the one knob.
DRV="$ROOT/$KIT_REL/unattended/unattended.sh"

same() { n=$((n+1)); if [ "$2" = "$3" ]; then echo "ok   $1"; else echo "FAIL $1 -- got '$2' want '$3'"; st=1; fi }
has()  { n=$((n+1)); case "$2" in *"$3"*) echo "ok   $1" ;; *) echo "FAIL $1 -- output lacked '$3'"; st=1 ;; esac }
hasnt_(){ n=$((n+1)); case "$2" in *"$3"*) echo "FAIL $1 -- output carried '$3' and must not"; st=1 ;; *) echo "ok   $1" ;; esac }

# ---------------------------------------------------------------------------------------------
# THE RUNNER. Evaluates the script the way its runtime does, with stub hooks that RECORD rather than
# spawn. `$1` is a JS expression for `args`; `$2` is a JS object literal mapping a stage label prefix
# to the value its agent returns, or the string `null` to simulate a dead stage.
# `$3` is the SCRIPT, defaulting to the parent — the child runs on the same runtime with the same
# stubs, so pointing this at `$C` is the whole child-side harness.
run_wf() { # args-expr · returns-expr · [script] -> prints the trace, then RESULT/THROW
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
  ' "${3:-$F}" "$1" "$2" 2>&1
}

UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","subjects":[{"path":"s1","blob":"abc1234"},{"path":"s2","blob":"def5678"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1"},{"id":"A-tB-2","order":1,"specPath":"s2","briefPath":"b2"},{"id":"A-tB-3","order":2,"specPath":"s3","briefPath":"b3"}]}'
SPEC_OK='{"authored":["A-tB-1"],"alreadyPresent":["A-tB-2","A-tB-3"],"refused":[],"summary":"ok"}'
# TOOL-aHoistedPass-6 - the BUILD double is gone with the stage. What a terminal verdict now
# reaches is the DISPOSAL stage, and past it the roster hand-out, which is a return rather than an
# agent. `returns` takes an optional THIRD argument so an arm can hand back a FAILED disposal.
DISPOSE_OK='{"disposed":true,"standing":[],"promoted":0,"folded":0,"summary":"ok"}'
# THE DOUBLE RETURNS THE CALLEE'S REAL KEYS, and the first version of it did not. It invented
# `verdict` and `reportPath`, so all 28 arms passed on two fields `tier2-review.js` has never
# returned — the harness and its callee had never met. Its actual returns carry `blockers`,
# `report`, `highs`, `note`, `precision` and `confirmed`; there is no `verdict` anywhere but
# per-FINDING. TOOL-aProbedUnit-7: `confirmed` was the one real key it omitted, and the disposal
# stage now decides on it — `review_out <blockers> [confirmed] [highs]`, `confirmed` defaulting to
# the blocker count and `highs` to 0, so every existing call site keeps a return that reconciles.
review_out() { printf '{"blockers":%s,"confirmed":%s,"highs":%s,"report":"r.md","precision":1,"note":"n"}' "$1" "${2:-$1}" "${3:-0}"; }
# The CONVERGENCE token is the driver's, recorded by an agent, so it is a separate fixture. Keeping
# them separate is the point: a run can produce a clean review and still not converge.
rec() { printf '{"token":"%s","exitCode":0}' "$1"; }
# `audit <token> <blockers>` still reads as one thing at the call sites, but it now feeds the two
# halves their own shapes. The DEFAULT disposal double is built from the count it is paired with —
# `promoted` equal to the blockers, `folded` 0 — so the arms that pair `NON-CONVERGENT 2` with it
# still reconcile against the reconciling guard and still receive the full roster.
returns() { local dflt; dflt=$(printf '{"disposed":true,"standing":[],"promoted":%s,"folded":0,"summary":"ok"}' "${2:-0}")
  printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
  "$SPEC_OK" "$(review_out "${2:-0}")" "$(rec "$1")" "${3:-$dflt}"; }
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
o=$(run_wf '{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","units":[]}' '{}')
has "args: an empty unit set is REFUSED rather than reported clean" "$o" "carries no \`units\`"
# AC14 - and the refusal names the MODE that can supply a spec path. The bare `--plan` it used to
# name resolves each unit's path internally and discards it, so a caller following the message
# literally could not build the array the next line refuses it for missing.
has "args: the empty-set refusal names --plan <slug> --paths" "$o" "--plan <slug> --paths"
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
has "args: a VALID object is accepted — the passing case" "$o" "RESULT"

# ---- TOOL-aProbedUnit-4: `scratch` IS REQUIRED, refused by SHAPE, folded ONCE, and carried to every
# ---- prompt and to the hand-out. The absent and relative fixtures are `$UNITS` with the key deleted
# ---- or rewritten, so the one landed fixture is the source of all three and cannot drift from it.
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"scratch":"/tmp/s",##')" "$(returns CONVERGED 0)")
has "scratch: the parent REFUSES args with no scratch" "$o" "THROW"
has "scratch: ...and the refusal names the key" "$o" "must carry an explicit \`scratch\`"
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"scratch":"/tmp/s"#"scratch":"tmp/s"#')" "$(returns CONVERGED 0)")
has "scratch: the parent REFUSES a relative scratch" "$o" "must carry an explicit \`scratch\`"
# TWO backslashes each in the JSON, ONE each once parsed. `hasnt_` hunts the two spellings an
# unfolded value takes: bare in a prompt line, JSON-escaped in the RESULT.
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"scratch":"/tmp/s"#"scratch":"C:\\\\tmp\\\\s"#')" "$(returns CONVERGED 0)")
p=$(printf '%s\n' "$o" | grep '^prompt:spec:tB:')
has    "scratch: a backslash scratch is folded before it reaches a prompt" "$p" "goes under C:/tmp/s"
hasnt_ "scratch: no backslash spelling reaches a prompt" "$p" 'C:\tmp'
d=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"dispatch"://')
has    "scratch: the folded path is what dispatch.args carries" "$d" '"scratch":"C:/tmp/s"'
hasnt_ "scratch: no backslash spelling reaches the hand-out" "$d" 'C:\\tmp'
# THE SENTENCE IS IN GROUND, so every parent-side prompt carries it: each spec writer, the audit
# recorder, and — on the verdict that spawns it — the disposal agent. OTHER is the load-bearing
# word: the scratchpad is itself outside the repository. The rev-3 `core.longpaths` clause is armed
# ABSENT, because the exception replaced it and two clone instructions in one sentence disagree.
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
for lbl in 'prompt:spec:tB:g0:' 'prompt:spec:tB:g1:' 'prompt:audit:record:r1:'; do
  p=$(printf '%s\n' "$o" | grep "^$lbl")
  has    "scratch: $lbl names the scratch root" "$p" "goes under /tmp/s"
  has    "scratch: $lbl forbids any OTHER path outside the repository" "$p" "a bare mktemp, or any OTHER path outside the repository"
  has    "scratch: $lbl carries the clone exception" "$p" 'goes under %TEMP%/<short-name>, never inside the worktree'
  hasnt_ "scratch: $lbl does not forbid its own destination" "$p" "any path outside"
  hasnt_ "scratch: $lbl carries no longpaths clause" "$p" "core.longpaths"
done
d=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"dispatch"://')
has "scratch: dispatch.args carries the scratch root" "$d" '"scratch":"/tmp/s"'
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2 '{"disposed":false,"standing":["b1"],"summary":"x"}')")
p=$(printf '%s\n' "$o" | grep '^prompt:dispose:tB:')
has "scratch: the disposal prompt names the scratch root" "$p" "goes under /tmp/s"
has "scratch: the disposal prompt carries the clone exception" "$p" 'goes under %TEMP%/<short-name>, never inside the worktree'

# ---- AC3: THE STAGE ORDER, asserted on the emitted sequence. A reordering reds this.
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
seq=$(printf '%s\n' "$o" | grep '^phase:' | tr '\n' ' ')
same "stage order is Spec then Audit then Disposal" "$seq" "phase:Spec phase:Audit phase:Disposal "

# ---- AC7: THE GATE ON THE VERDICT, over all five driver states. A gate tested only on the state
# ---- that OPENS it is a gate nothing proved closes.
o=$(run_wf "$UNITS" "$(returns CONVERGING 3)")
has "CONVERGING: BUILD is not reached" "$o" "HELD AT AUDIT"
n=$((n+1)); case "$o" in *"phase:Disposal"*) echo "FAIL CONVERGING reached the Disposal phase, which is the one thing this gate exists to stop"; st=1 ;; *) echo "ok   CONVERGING: the Disposal phase never ran" ;; esac
has "CONVERGING: the caller is told what to do next" "$o" "re-invoke this harness with round"
for v in CONVERGED NON-CONVERGENT CEILING BOUNDED; do
  o=$(run_wf "$UNITS" "$(returns "$v" 0)")
  n=$((n+1)); case "$o" in *'"roster":[{'*) echo "ok   $v: hands out a roster" ;; *) echo "FAIL $v handed out no roster, so a terminal verdict cannot land a build"; st=1 ;; esac
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
  *"phase:Disposal"*) echo "FAIL S3 the impossible pairing still reached DISPOSAL"; st=1 ;;
  *) echo "ok   S3 ...and DISPOSAL is not reached" ;;
esac

# S2 — A NON-INTEGER BLOCKER COUNT IS A DEGRADED RUN AND IS REPORTED AS ONE. tier2-review yields
# `null` there BY DESIGN, never 0, so reading it as 0 would make every degraded audit look clean:
# unattended.sh emits CONVERGED only on a count of 0.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":{"blockers":null,"report":"r.md"},"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(rec CONVERGED)" "$DISPOSE_OK")")
has "S2 a null blocker count THROWS rather than rounding to zero" "$o" "non-integer blocker count"
n=$((n+1)); case "$o" in
  *"phase:Disposal"*) echo "FAIL S2 a degraded audit reached DISPOSAL"; st=1 ;;
  *) echo "ok   S2 ...and a degraded audit does not reach DISPOSAL" ;;
esac

# THE SUBJECT GUARD. An unpinned subject audits whatever the file happens to say when the lens
# reads it, which is not a review of anything in particular — and tier2-review would refuse it
# downstream with a message about its own arguments rather than about which stage failed.
o=$(run_wf "${UNITS/\"blob\":\"abc1234\"/\"blob\":\"nothex\"}" "$(returns CONVERGED 0)")
has "an unpinned subject blob is REFUSED before the sub-workflow runs" "$o" "7-40 hex blob"

# ---- AC9: A DEAD AUDIT STAGE IS A REFUSAL, never a silent pass to BUILD. This is the absence that
# ---- would otherwise let the harness build on an unreviewed spec set.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"dispose:":%s}' "$SPEC_OK" "$DISPOSE_OK")")
has "a dead AUDIT stage THROWS" "$o" "THROW"
has "the throw says an absent verdict is not a convergence" "$o" "must never read as CONVERGED"
o=$(run_wf "$UNITS" "$(printf '{"workflow":%s,"audit:record":%s,"dispose:":%s}' "$(review_out 0)" "$(rec CONVERGED)" "$DISPOSE_OK")")
# The message moved with TOOL-aStagedLane-3: the stage is a FAN now, so the refusal is keyed on
# the live WRITER COUNT rather than on a falsy return. The arm follows the message rather than
# the message being frozen for the arm — `arm-literal-strands-on-message-edit`, met head on.
has "a dead SPEC stage THROWS rather than auditing nothing" "$o" "EVERY spec writer returned nothing"

# ---- AC6: A DEGRADED RUN SAYS SO. `degradation-known-but-unreported` is the class where a pipeline
# ---- computes how badly it degraded and does not report it.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    '{"authored":[],"alreadyPresent":["A-tB-1"],"refused":["A-tB-2","A-tB-3"],"summary":"s"}' \
    "$(review_out 0)" "$(rec CONVERGED)" "$DISPOSE_OK")")
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
# RE-POINTED AT TOOL-aHoistedPass-6. The claim used to live in the BUILD prompt, which is deleted;
# the file's own header still carries it, and the roster's per-entry `order` is what a caller
# dispatches on. Pointing the arm at the surviving carrier is not the same as deleting it.
n=$((n+1)); if grep -q "DISPATCH IS STRICTLY SEQUENTIAL" "$F"; then
  echo "ok   dispatch is still declared strictly sequential"
else
  echo "FAIL the file no longer declares per-unit dispatch sequential"; st=1
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
o=$(run_wf "$UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"dispose":{"disposed":true,"standing":[],"summary":"d"}}')
has  "default mode: the round IS recorded through the driver" "$o" "agent:audit:record"
has  "default mode: the return names the child the caller dispatches" "$o" '"scriptPath":"tools/workflows/unattended-unit.js"'
has  "default mode: hands out a roster" "$o" '"roster":[{'

# ---- AC1: attended mode reaches BUILD and spawns NO recorder agent.
A_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1","planState":"READY"}]}'
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"dispose":{"disposed":true,"standing":[],"summary":"d"}}')
has   "attended: hands out a roster" "$o" '"roster":[{'
hasnt_ "attended: no round is recorded through the driver" "$o" "agent:audit:record"
has   "attended: it SAYS the round was not recorded" "$o" "no round was recorded"

# ---- AC8: the BUILD prompt drops the verbs that refuse without a run-state file — AND still carries
# ---- the surrounding instruction. The paired positive is the point: an absence assertion passes just
# ---- as well when the whole clause is empty.
hasnt_ "attended: NO agent prompt carries a --dispatch INSTRUCTION" "$o" "--dispatch tB"
# The verbs are NAMED in the attended preamble, to say they are unavailable. The assertion must
# therefore target the INSTRUCTION form `--brief <slug>`, not the word — an absence arm aimed at
# the word fails on the sentence explaining the absence.
hasnt_ "attended: NO agent prompt carries a --brief INSTRUCTION" "$o" "--brief tB"
# TOOL-aHoistedPass-6 - the per-unit build INSTRUCTION left with the BUILD prompt and is now the
# child's, so the arm that graded it is gone rather than re-pointed at a weaker witness. What
# survives is the preamble sentence, which is where the attended honesty statement actually lives.
has   "attended preamble: it says why the recording verbs are absent" "$o" "recording verbs are unavailable"

# ---- AC9: no agent is told it holds a mandate. In this repo a mandate IS the authority to merge and
# ---- push with no owner turn, so the unattended preamble is a falsehood in attended mode.
hasnt_ "attended preamble: the word 'mandate' does not reach any agent" "$o" "under a mandate"
has   "attended preamble: it says an owner is in the loop" "$o" "OWNER in the loop"

# ---- AC10: both live verdict branches. A branch mapping a positive count to terminal would reach
# ---- BUILD over open blockers and satisfy every other criterion here.
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":2,"confirmed":2,"highs":0,"report":"r.md"}}')
has   "attended, 2 blockers: CONVERGING" "$o" "CONVERGING"
hasnt_ "attended, 2 blockers: NO roster is handed out" "$o" '"roster":[{'

# ---- AC3: a null blocker count REFUSES in attended mode too. tier2-review.js yields null on its
# ---- degraded paths BY DESIGN, and reading it as 0 would make every degraded audit look clean.
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":null,"report":"r.md"}}')
has  "attended, null blockers: REFUSES" "$o" "THROW"
has  "attended, null blockers: names the degraded return" "$o" "DEGRADED"

# ---- AC4: a FORKED unit refuses, and the message names both the id and the state. The bare token is
# ---- supplied directly: --plan rewrites a terminal unit's grade to `DONE (FORKED)`, so a bare FORKED
# ---- and a real closed build's roster are jointly unsatisfiable.
F_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"FORKED"}]}'
o=$(run_wf "$F_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended, FORKED unit: refuses" "$o" "THROW"
has  "attended, FORKED unit: names the id" "$o" "A-tB-1"
has  "attended, FORKED unit: names the state" "$o" "FORKED"

# ---- AC11: the terminal-unit SKIP, with the vocabulary --plan actually emits. `DONE (FORKED)` is
# ---- what a closed build reports for a unit whose underlying grade was not READY, and a five-token
# ---- allow-list halts on it — round-1's halt-at-unit-one, for the third time.
D_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"DONE (FORKED)"},{"id":"A-tB-2","order":2,"specPath":"s2","planState":"READY"}]}'
o=$(run_wf "$D_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended, DONE (FORKED): SKIPPED, not refused" "$o" "SKIPPING 1 terminal unit"
has  "attended, terminal units: still hands out a roster" "$o" '"roster":[{'
# H4 - the skip must reach the ROSTER, not only the log line. It used to be read off the composed
# build prompt; the roster is now a RETURNED array and is read there. AC25: `roster` and
# `skippedTerminal` are different arrays, and a roster built from `ordered` would hand every
# already-terminal unit out for dispatch — the same defect one layer over.
ob=$(printf '%s
' "$o" | grep '^RESULT ' | sed 's/.*"roster"://; s/,"dispatch".*//')
hasnt_ "attended: a SKIPPED unit is absent from the ROSTER" "$ob" "A-tB-1"
has   "attended: a surviving unit is still IN the ROSTER" "$ob" "A-tB-2"
has   "AC25: units still counts the WHOLE ordered set, not the roster" "$o" '"units":2'
has   "AC25: the skipped unit is still reported in skippedTerminal" "$o" '"skippedTerminal":["A-tB-1"]'

# ---- AC13: a state outside every arm refuses BY NAME. Neither building nor skipping an unknown state
# ---- is safe, and this vocabulary has been mis-transcribed twice already.
X_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"WOBBLE"}]}'
o=$(run_wf "$X_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended, unknown state: refuses" "$o" "THROW"
has  "attended, unknown state: names the value it did not recognise" "$o" "WOBBLE"

# ---- AC12: a missing planState refuses rather than defaulting. A defaulted state puts the refusal
# ---- predicate to work on a value nobody supplied.
M_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1"}]}'
o=$(run_wf "$M_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended, no planState: refuses" "$o" "THROW"
has  "attended, no planState: names the field" "$o" "planState"

# ---- AC14: the FRESH-BUILD path. A unit stage 1 authors reports MISSING at entry — there is no point
# ---- between the stages at which a caller could re-run --plan — so the entry-time value is stale by
# ---- construction and the stage must not refuse the build it just specced.
N_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"MISSING"}]}'
o=$(run_wf "$N_UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended, unit AUTHORED this invocation: rostered despite entry-time MISSING" "$o" '"roster":[{'
# and the control: the same MISSING state, NOT specced by stage 1, must still refuse.
o=$(run_wf "$N_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":["A-tB-1"],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended, MISSING and NOT specced: still refuses" "$o" "THROW"
# M1 - `alreadyPresent` must NOT exempt. Those are the units the stage did NOT touch, so their
# entry-time grade is current; exempting them bypassed the THIN/FORKED refusal on an agent's
# say-so. Only `authored` is stale by construction.
o=$(run_wf "$N_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended, MISSING but only alreadyPresent: still refuses" "$o" "THROW"

# ---- S1: the mode is a CLOSED pair. A typo must not fall back to a default that hands the caller
# ---- fewer checks than they asked for.
B_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attnded","units":[{"id":"A-tB-1","order":1}]}'
o=$(run_wf "$B_UNITS" '{}')
has  "bad mode: refuses rather than defaulting" "$o" "THROW"
has  "bad mode: names the closed set" "$o" "unattended, attended"

# ---- S7: the warning depends on a CALLER-SUPPLIED fact, because this script has no filesystem. A
# ---- caller that supplies nothing gets no warning, which is a hole the header names rather than one
# ---- a reader has to infer.
W_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","runStateExists":true,"subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"READY"}]}'
o=$(run_wf "$W_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has  "attended + run-state file: WARNS" "$o" "WARNING: attended mode was requested"
has  "attended + run-state file: names the slug" "$o" "tB"
has  "attended + run-state file: CONTINUES to the hand-out" "$o" '"roster":[{'

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
has "header: says M4's disposal clause is REACHABLE attended since unit 7" "$HDR" "REACHABLE HERE SINCE"
has "header: says the S7 warning is caller-supplied, not detected" "$HDR" "DEPENDS ON THE CALLER AND NOT ON DETECTION"

# ================================================== TOOL-aStagedLane-3 — THE SLICED SPEC FAN
# The spec stage fans one writer per GROUP of slices. Slices come from the caller, grouped by the
# `order` verb; the groups are what the cap bounds.

# ---- AC1: three slices at a cap of five chunk to groups of ONE, so three writers spawn and the
# ---- total never exceeds the cap.
S3='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","subjects":[{"path":"s1","blob":"abc1234"}],"units":[
  {"id":"A-tB-1","order":1,"specPath":"s1","specBriefPath":"bf1"},
  {"id":"A-tB-2","order":2,"specPath":"s2","specBriefPath":"bf2"},
  {"id":"A-tB-3","order":3,"specPath":"s3","specBriefPath":"bf3"}]}'
o=$(run_wf "$S3" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
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
S7='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","subjects":[{"path":"s1","blob":"abc1234"}],"units":[
  {"id":"A-tB-1","order":1,"specPath":"s1"},{"id":"A-tB-2","order":2,"specPath":"s2"},
  {"id":"A-tB-3","order":3,"specPath":"s3"},{"id":"A-tB-4","order":4,"specPath":"s4"},
  {"id":"A-tB-5","order":5,"specPath":"s5"},{"id":"A-tB-6","order":6,"specPath":"s6"},
  {"id":"A-tB-7","order":7,"specPath":"s7"}]}'
o=$(run_wf "$S7" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
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
o=$(run_wf "$S3" '{"spec:tB:g0":null,"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has "one dead writer: reported as DEGRADED" "$o" "DEGRADED — 1 of 3 writer(s) returned nothing"
has "one dead writer: its unit lands in refused" "$o" "A-tB-1"
has "one dead writer: the run still reaches the hand-out" "$o" '"roster":[{'

# ---- AC4, second half: EVERY writer dead must THROW. The old guard was `if (!specced)` on a falsy
# ---- return, and a merged object is always truthy — so without this an entirely dead spec stage
# ---- reaches AUDIT and BUILD on whatever specs already existed, with the refusal this file spends
# ---- six lines justifying silently deleted.
o=$(run_wf "$S3" '{"spec":null,"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has   "ALL writers dead: THROWS" "$o" "THROW"
has   "ALL writers dead: says every writer returned nothing" "$o" "EVERY spec writer returned nothing"
hasnt_ "ALL writers dead: no roster is ever handed out" "$o" '"roster"'

# ---- AC7/S3c: the writers are told to AUTHOR and never COMMIT, and not to run the generator. That is
# ---- half of clause 3 of the disjointness proof, and no gate downstream of here reads a prompt.
o=$(run_wf "$S3" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has "writers: told to author and NOT commit" "$o" "AUTHOR ONLY — DO NOT COMMIT"
has "writers: told the caller commits once after them" "$o" "the caller commits once after all of you"
# AC9 - S4's generator prohibition, which had no criterion at all before this arm.
has "writers: told not to run the index generator" "$o" "do not run the build-index generator"

# ---- AC10/S3d: the file's own header no longer claims every stage is one agent, and says why the
# ---- ratified `parallelism route: none` verdict does not reach this fan.
HDR3=$(sed -n '1,120p' "$F")
has "header: the one-agent claim names the stage it still applies to" "$HDR3" "THE DISPOSAL STAGE IS ONE AGENT"
has "header: it names the ratified verdict it does not contradict" "$HDR3" "parallelism route:"
has "header: it says why — the writers do not commit" "$HDR3" "author and never commit"

# ============================ TOOL-aHoistedPass-6 — DISPOSAL, AND THE ROSTER HAND-OUT
# The BUILD stage is gone. What a terminal verdict now reaches is a whole-set DISPOSAL stage and
# then a RETURN carrying an ordered roster, which the caller dispatches one main-loop `Workflow`
# call per unit. Every arm below reads a return or the trace, because that is where the change is.

# ---- AC4: a CONFIRMED COUNT OF ZERO skips disposal and SAYS SO. A skip that looks like a pass is
# ---- indistinguishable from coverage, so the announcement is the arm — an absence alone would pass
# ---- over a stage that was never written at all. TOOL-aProbedUnit-7 moved the predicate off the
# ---- verdict and onto the count, so this arm now observes the count: CONVERGED with zero confirmed.
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
hasnt_ "AC4 zero confirmed: no disposal agent is spawned" "$o" "agent:dispose:"
has    "AC4 zero confirmed: the skip is ANNOUNCED in the log" "$o" "disposal: skipped"
has    "AC4 zero confirmed: and the roster is still handed out" "$o" '"roster":[{'
# V2 — the skip path carries STATED ZEROS, never a missing key standing in for one.
has    "V2 zero confirmed: the hand-out carries promoted 0 and folded 0 out loud" "$o" '"promoted":0,"folded":0'

# ======================= TOOL-aProbedUnit-7 — DISPOSAL BY SEVERITY, ON ANY CONFIRMED FINDING
# The stage ran on the VERDICT and disposed by NATURE, so a round that CONVERGED with highs, mediums
# and lows standing disposed nothing. Every arm below reads the trace or the RESULT line; each was
# observed RED against the unchanged render, one arm at a time, before the harness moved.
# ---- V1: CONVERGED with four confirmed, one of them HIGH, RUNS the stage, announces the severity
# ---- rule, spells the promotion verb with --reason, and hands out the roster with both counts.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 4 1)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":3,"summary":"d"}')")
has "V1 CONVERGED with confirmed findings: the disposal agent RUNS" "$o" "agent:dispose:tB"
has "V1 ...and the log says the rule, on CONVERGED too" "$o" "disposing by severity, on CONVERGED too"
has "V1 ...and the prompt names the one high" "$o" "1 at HIGH"
has "V1 ...and the prompt spells the promotion verb" "$o" "--rescope tB --act add --item"
has "V1 ...with --reason, which verb_rescope requires" "$o" "--reason"
has "V1 ...and the hand-out carries the stage's counts" "$o" '"promoted":1,"folded":3'
has "V1 ...and the roster is handed out" "$o" '"roster":[{'
# ---- V3: counts that do NOT reconcile — 1 + 1 + 0 standing over 3 confirmed — hand out NO roster,
# ---- carry the counts, and are never logged done. The `{disposed:true, standing:['b1']}` defect
# ---- with the contradiction moved into two integers.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 3 0)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":1,"summary":"x"}')")
has    "V3 unreconciled counts: the roster is EMPTY" "$o" '"roster":[]'
has    "V3 unreconciled counts: the note says the counts do not reconcile" "$o" "do not reconcile"
has    "V3 unreconciled counts: the counts still travel out" "$o" '"promoted":1,"folded":1'
hasnt_ "V3 unreconciled counts: disposal is NOT logged done" "$o" "disposal: done"
# ---- V4: a `confirmed` that cannot be read as the contract REFUSES, in both shapes — the key
# ---- missing, and blockers exceeding confirmed. `undefined > 0` is false, so a missing key would
# ---- otherwise skip the stage on every round, the false-clean shape.
o=$(run_wf "$UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has    "V4 no confirmed key: REFUSES" "$o" "THROW"
has    "V4 no confirmed key: the message names confirmed" "$o" "returned confirmed"
hasnt_ "V4 no confirmed key: the stage is never reached" "$o" "phase:Disposal"
o=$(run_wf "$UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":2,"confirmed":1,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has    "V4 blockers above confirmed: REFUSES" "$o" "THROW"
has    "V4 blockers above confirmed: the message names confirmed" "$o" "returned confirmed"
hasnt_ "V4 blockers above confirmed: the stage is never reached" "$o" "phase:Disposal"
# ---- V5: ATTENDED mode reaches the stage at zero blockers with two confirmed, and its prompt
# ---- promotes through the README's roster table, never through --rescope, which fail 48s with no
# ---- run-state file. The RESULT is the attended MAIN return, since A_UNITS is READY.
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":2,"highs":0,"report":"r.md"},"dispose":{"disposed":true,"standing":[],"promoted":0,"folded":2,"summary":"d"}}')
has    "V5 attended with confirmed findings: the disposal agent RUNS" "$o" "agent:dispose:tB"
has    "V5 attended: the prompt promotes through the README roster" "$o" "authored Units table"
hasnt_ "V5 attended: the prompt never orders --rescope" "$o" "--rescope tB"
has    "V5 attended: the main return carries the stage's counts" "$o" '"promoted":0,"folded":2'

# ---- AC5: a disposal that did NOT finish hands out NO roster. There is no partial hand-out: a
# ---- roster minus the units a blocker touches is a judgement this runtime cannot make, having no
# ---- filesystem.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2 '{"disposed":false,"standing":["b1"],"summary":"x"}')")
has "AC5 failed disposal: the disposal agent DID run" "$o" "agent:dispose:tB"
has "AC5 failed disposal: the roster is EMPTY" "$o" '"roster":[]'
has "AC5 failed disposal: the note is DEGRADED and says what stood" "$o" "DEGRADED — findings were not disposed"
# NAMED IN THE NOTE, not merely present in the output. A bare `b1` is satisfied by the fixture's own
# `"briefPath":"b1"`, which is the fixture-passes-by-finding-nothing class inside the arm itself —
# observed here, green against the unchanged source, before it was tightened.
has "AC5 failed disposal: the standing blocker is NAMED in the note" "$o" "were not disposed: b1"
n=$((n+1)); case "$(printf '%s\n' "$o" | grep '^agent:' | tail -1)" in
  "agent:dispose:tB") echo "ok   AC5 no agent runs after a failed disposal" ;;
  *) echo "FAIL AC5 an agent ran after the failed disposal"; st=1 ;;
esac

# ---- AC5b: a DEAD disposal stage is the same refusal as a negative one. `d.disposed !== true`
# ---- covers both, and a double returning null is how the stage dies in practice.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2 'null')")
has "AC5b dead disposal stage: the roster is EMPTY" "$o" '"roster":[]'
has "AC5b dead disposal stage: it says the stage returned nothing" "$o" "returned nothing at all"

# ---- AC6: EVERY non-throwing exit carries `roster`, so `roster.length === 0` is the caller's whole
# ---- stop condition. NEITHER of these two carried the key before this unit, and a caller reading
# ---- `roster.length` would have read a property of `undefined` and thrown.
o=$(run_wf "$UNITS" "$(returns CONVERGING 3)")
has "AC6 the CONVERGING exit carries an empty roster" "$o" '"roster":[]'
T_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"DONE"}]}'
o=$(run_wf "$T_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"}}')
has "AC6 the attended every-unit-terminal exit carries an empty roster" "$o" '"roster":[]'
has "R2F1 the attended every-unit-terminal exit says what stood" "$o" '"standing":'
# V7 (TOOL-aProbedUnit-7) — the one return no other arm reaches carries both counts as stated zeros.
has "V7 the attended every-unit-terminal exit carries promoted 0 and folded 0" "$o" '"promoted":0,"folded":0'
has "AC6 ...and still says why" "$o" "every unit was already terminal"

# ---- AC7/AC8: the hand-out itself. The roster is asserted WHOLE — key set, key order, values and
# ---- sequence in one comparison — because an arm that greps for an id passes over a roster whose
# ---- entries carry the wrong fields.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2)")
has "AC7 the roster is the ordered array of {id, order, specPath, briefPath}" "$o" \
  '"roster":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1"},{"id":"A-tB-2","order":1,"specPath":"s2","briefPath":"b2"},{"id":"A-tB-3","order":2,"specPath":"s3","briefPath":"b3"}]'
has "AC7 dispatch names the child script by its repo-relative path" "$o" \
  '"scriptPath":"tools/workflows/unattended-unit.js"'
has "AC7 dispatch names the command that resolves the rest of the paths" "$o" '--plan tB --paths'
has "AC7 the note names the hand-out" "$o" "prologue complete"
# `dispatch` is sliced out and asserted on its own: the child receives its own unit and never the
# list, which is the whole shape change.
d=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"dispatch"://')
has    "AC8 dispatch.args carries the repo" "$d" '"repo":"/tmp/r"'
has    "AC8 dispatch.args carries the slug" "$d" '"slug":"tB"'
has    "AC8 dispatch.args carries the driver" "$d" '"driver":"bash tools/unattended/unattended.sh"'
has    "AC8 dispatch.args carries the bug-class checklist" "$d" '"checklist":"python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD"'
has    "AC8 dispatch names the three per-unit fields and only those" "$d" '"perUnit":["unitId","specPath","briefPath"]'
hasnt_ "AC8 the child never receives the roster list" "$d" '"roster"'

# ---- S4: the keys the old BUILD return carried are GONE, not left reading zero. A caller that
# ---- still read `built` would see a number that means nothing.
# SINGLE-QUOTED LABELS, and that is not style. Double-quoted, the backticks below are COMMAND
# SUBSTITUTION: the shell ran `built` and `unbuilt` while composing the label, printed two
# `command not found` lines to stderr and left both verdicts naming nothing. The suite still exited
# 0, which is why it survived a landing. The same trap is recorded against `_bm31` in
# check-unattended.test.sh, where it cost a 50-minute run to find.
hasnt_ 'S4 the return no longer carries a `built` count' "$o" '"built":'
hasnt_ 'S4 the return no longer carries an `unbuilt` list' "$o" '"unbuilt":'
# ...and the run-integrity fields every return at BASE carried are still on it.
has "S4 the mode still travels on the hand-out" "$o" '"mode":"unattended"'
has "S4 skippedTerminal still travels on the hand-out" "$o" '"skippedTerminal":'


# ========================= F2 (closing review, BLOCKER) — THE MODE REACHES THE CHILD
# The child was MODE-BLIND and ordered `--dispatch` and `--brief` unconditionally, both of which
# `fail 49` without a run-state file — which is the state attended mode is DEFINED by — while
# telling the child a refusal is BINDING. So every attended dispatch halted at unit one. That is the
# failure the plan-state grading twelve screens up was moved forward to prevent, arriving one layer
# down.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2)")
d=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"dispatch"://')
has "F2 dispatch.args carries the mode — unattended" "$d" '"mode":"unattended"'
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"dispose":{"disposed":true,"standing":[],"summary":"d"}}')
d=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"dispatch"://')
has "F2 dispatch.args carries the mode — attended" "$d" '"mode":"attended"'

# THE GENERAL FORM, not a substring arm. The refusal set is DERIVED from the driver itself — every
# verb whose body refuses with `fail 4N "no run-state file` — so this keeps holding when a seventh
# verb joins it, which a hand-typed list of two would not. The needle is the INSTRUCTION form
# `--<verb> <slug>` and never the bare word: the attended text NAMES three of these verbs in the
# sentence explaining that they are unavailable, and an arm aimed at the word would fail on the
# explanation. That trap is already recorded against the attended preamble arm above.
CHILD_ARGS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","unitId":"A-tB-1","specPath":"s1","briefPath":"b1","driver":"bash drv.sh","ground":"G. goes under /tmp/s. ","checklist":"CK","mode":"%s"}'
childU=$(run_wf "$(printf "$CHILD_ARGS" unattended)" '{}' "$C")
childA=$(run_wf "$(printf "$CHILD_ARGS" attended)" '{}' "$C")
norun_verbs=''
[ -f "$DRV" ] && norun_verbs=$(awk '
  /^verb_[a-z]+\(\)/ { v = $0; sub(/^verb_/, "", v); sub(/\(\).*/, "", v); next }
  v != "" && /fail 4[0-9] "no run-state file/ { print "--" v; v = "" }
' "$DRV" | sort -u)
# A DERIVED SET THAT CAME BACK EMPTY IS NOT A CLEAN PASS. Without this the loop below iterates zero
# times and every absence arm silently ceases to exist — the vacuous-selector shape, inside the arm.
n=$((n+1)); nv=$(printf '%s\n' "$norun_verbs" | grep -c .)
if [ "$nv" -ge 3 ]; then echo "ok   F2 the no-run-state refusal set derived $nv verb(s) from the driver"
else echo "FAIL F2 the no-run-state refusal set derived $nv verb(s) — the absence arms below would be vacuous"; st=1; fi

# THE POSITIVE HALF FIRST. An absence assertion over the attended prompt passes just as well when
# the whole clause is empty, so the unattended prompt is armed for the same instructions BEING there.
has "F2 the UNATTENDED child prompt orders --dispatch" "$childU" "--dispatch tB"
has "F2 the UNATTENDED child prompt orders --brief" "$childU" "--brief tB"
has "F2 the UNATTENDED child prompt still says a refusal is BINDING" "$childU" "A REFUSAL FROM IT IS BINDING"
has "F2 the ATTENDED child prompt says the recording verbs are unavailable" "$childA" "recording verbs are unavailable"
has "F2 the ATTENDED child prompt orders the paths written down instead" "$childA" "Write down the paths"
has "aProbedUnit-1 the child prompt forbids a gate, suite or bar inside the pass" "$childU" "NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS"
has "aProbedUnit-2 the child prompt bounds every command and names a skipped one" "$childU" "YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED"
for verb in $norun_verbs; do
  hasnt_ "F2 the ATTENDED child prompt issues no $verb instruction" "$childA" "$verb tB"
done
# AND THE MODE IS A CLOSED SET IN THE CHILD TOO. A typo silently selecting the unattended text by
# default is this same defect wearing a different hat, so the child refuses rather than defaults.
o=$(run_wf '{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","unitId":"A-tB-1","specPath":"s1","briefPath":"b1","driver":"bash drv.sh","ground":"G. goes under /tmp/s. ","checklist":"CK","mode":"atttended"}' '{}' "$C")
has "F2 the child REFUSES a mode outside the closed set" "$o" "THROW"
has "F2 ...and names the value it was given" "$o" '"atttended"'
o=$(run_wf '{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","unitId":"A-tB-1","specPath":"s1","briefPath":"b1","driver":"bash drv.sh","ground":"G. goes under /tmp/s. ","checklist":"CK"}' '{}' "$C")
has "F2 the child REFUSES an absent mode rather than defaulting one" "$o" "THROW"
# TOOL-aProbedUnit-4 — the child refuses without `scratch`, and refuses a `ground` that does not
# NAME the scratch it was handed: the sentence reaches the unit agent through the parent's ground
# text, so a hand-composed dispatch that drops or swaps either key meets a refusal naming the other.
# Both fixtures derive from CHILD_ARGS, so they cannot drift from the landed one.
o=$(run_wf "$(printf "$CHILD_ARGS" unattended | sed 's#"scratch":"/tmp/s",##')" '{}' "$C")
has "scratch: the child REFUSES args with no scratch" "$o" "must carry an explicit \`scratch\`"
o=$(run_wf "$(printf "$CHILD_ARGS" unattended | sed 's#"ground":"G. goes under /tmp/s. "#"ground":"G. "#')" '{}' "$C")
has "scratch: the child REFUSES a ground that names no scratch" "$o" "names no \`/tmp/s\`"
has "scratch: the child prompt opens with the ground that names it" "$childU" "prompt:unit:A-tB-1:G. goes under /tmp/s. "

# ========================= F4 (closing review, HIGH) — DISPOSED-BUT-STANDING IS NOT DISPOSED
# `{disposed:true, standing:['b1']}` validated against DISPOSAL_SCHEMA, cleared a guard that tested
# only `disposed !== true`, logged `disposal: done` and handed out the FULL roster over an undisposed
# blocker — under a prompt whose own words are NAME in `standing` every blocker you did NOT dispose.
# Reachable on exactly the two verdicts that structurally guarantee standing blockers.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2 '{"disposed":true,"standing":["b1"],"summary":"x"}')")
has "F4 disposed:true with a standing blocker: the roster is EMPTY" "$o" '"roster":[]'
has "F4 disposed:true with a standing blocker: the note is DEGRADED" "$o" "DEGRADED — findings were not disposed"
has "F4 disposed:true with a standing blocker: the blocker is NAMED" "$o" "were not disposed: b1"
# ROUND 2, finding 1: the DEGRADED return is the ONE path where `stood` can be non-empty, and it
# carried no `standing` key at all. The arm below asserts the payload, not the empty case. The
# hand-out arm further down asserts `[]` and passes on a fixture that could not have produced
# anything else, so it proves the key is PRESENT there and nothing about its value.
has "F4 the DEGRADED return names what stood, as a key and not only in prose" "$o" '"standing":["b1"]'
hasnt_ "F4 disposed:true with a standing blocker: disposal is NOT logged done" "$o" "disposal: done"
# CEILING is the other verdict that reaches the stage, and it takes the same path.
o=$(run_wf "$UNITS" "$(returns CEILING 4 '{"disposed":true,"standing":["b2"],"summary":"x"}')")
has "F4 the same pairing under CEILING hands out no roster" "$o" '"roster":[]'
# AND WHAT STOOD TRAVELS OUT. `standing` never reached the hand-out at all, which is
# degradation-known-but-unreported — a class this harness names three times in its own comments. It
# is a REQUIRED field and never an absence: an empty list said out loud is not the same fact as a
# missing key, which is indistinguishable from a stage that never ran.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2)")
has "F4 the hand-out carries what stood, empty and explicit" "$o" '"standing":[]'

# ================================== TOOL-dPolishedVitrine-1 — THE HARNESS IS RENDERED AT INSTALL
# The harness shipped as an ENGINE file, and apply writes those verbatim, so every install path it
# spelled reached a tree installed at another prefix naming files that tree does not have: the
# driver, the bug-class checklist, the review sub-workflow it awaits and the child it hands out.
# Both adopters measured when this landed install at `scripts`, and both install the memory-tree kit
# FLAT. So the fixture carrying the weight is the flat one: a fix that derived only the prefix passes
# a nested layout and still names a checklist script the flat one does not have.
#
# EACH LAYOUT IS A REAL REPOSITORY built from this kit's own files, and it is rendered by the
# fixture's OWN copy of the parity script, which is the command the kit's `[[regenerate]]` block runs
# in an adopter. The expected values are TYPED per layout and never read back out of a render: an
# expectation derived by the same derivation it grades agrees with whatever that derivation did.
#
# ARM (v) IS THE CLASS ARM and the independent oracle. Every `.js`, `.sh` and `.py` path the harness
# emits, in its trace or its return, has to be one `git ls-files` answers for in the fixture. The
# other four arms name the four sites this unit knows about; this one catches a fifth nobody named.
#
# TWO NEGATIVE CONTROLS keep the five arms honest on every run, because an arm only ever seen to pass
# is an assertion about nothing. The harness spelled for this repo's own install — which is what
# apply wrote before this unit — reds all five. A template whose checklist is `{{TOOL_ROOT}}memory-tree/`
# reds (iv) and (v) and passes the rest, which is the prefix-only fix measured in one line.
LAY=$(mktemp -d) || exit 2
trap 'rm -rf "$LAY"' EXIT

build_layout() { # dir · kit dir · unattended dir, or '-' for none · checklist script, or '' for none -> a git repo
  local d=$1 kd=$2 ud=$3 gp=$4
  mkdir -p "$d/$kd" "$d/memory/guides"
  ( cd "$d" && git init -q -b main . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false )
  cp "$HERE/unattended-build.template.js" "$HERE/check-protocol-parity.test.sh" \
     "$HERE/REVIEW-PROTOCOL.template.md" "$HERE/tier2-review.js" "$HERE/unattended-unit.js" "$d/$kd/"
  # `-` IS A REVIEW-HARNESS-ONLY INSTALL, which `requires` permits: this kit requires agent-cap and
  # nothing else, so neither the unattended kit nor the memory-tree kit has to be there.
  if [ "$ud" != - ]; then mkdir -p "$d/$ud"; printf '#!/usr/bin/env bash\n' > "$d/$ud/unattended.sh"; fi
  if [ -n "$gp" ]; then mkdir -p "$(dirname "$d/$gp")"; printf '# a stub checklist\n' > "$d/$gp"; fi
  ( cd "$d" && git add -A )
}
run_layout() { # dir · kit dir · [--render] -> the parity script's output, then `rc=<exit>`
  ( cd "$1" && bash "$2/check-protocol-parity.test.sh" ${3:-} 2>&1; echo "rc=$?" )
}
read_field() { # json · dotted key -> the value, or an empty line
  node -e 'let v = JSON.parse(process.argv[1]); for (const k of process.argv[2].split(".")) v = v == null ? v : v[k]; console.log(v == null ? "" : v)' "$1" "$2"
}
check_layout() { # label · dir · kit dir · tool root · checklist dir · five expected verdicts, G or R
  local label=$1 d=$2 kd=$3 tr=$4 mt=$5 want=$6 o res toks tok miss="" pop got="" k g w
  o=$(run_wf "$UNITS" "$(returns CONVERGED 0)" "$d/$kd/unattended-build.js")
  res=$(printf '%s\n' "$o" | sed -n 's/^RESULT //p')
  # A HARNESS THAT DID NOT RETURN CANNOT BE GRADED. Five reds from a throw would satisfy a negative
  # control while grading nothing, which is the vacuous-selector shape one level inside the arm.
  n=$((n+1))
  if [ -z "$res" ]; then
    echo "FAIL $label -- the harness did not return: $(printf '%s\n' "$o" | tail -1)"; st=1; return
  fi
  echo "ok   $label -- the harness ran to its hand-out"
  printf '%s\n' "$o" | grep -qxF "workflow:$kd/tier2-review.js" && got="${got}G" || got="${got}R"
  [ "$(read_field "$res" dispatch.scriptPath)" = "$kd/unattended-unit.js" ] && got="${got}G" || got="${got}R"
  [ "$(read_field "$res" dispatch.args.driver)" = "bash ${tr}unattended/unattended.sh" ] && got="${got}G" || got="${got}R"
  [ "$(read_field "$res" dispatch.args.checklist)" = "python $mt/gotchas.py --for-diff HEAD~1..HEAD" ] && got="${got}G" || got="${got}R"
  # The population is every path-shaped token in the whole output, NOT the four sites above, and its
  # size is asserted: fewer than four means the extraction found nothing to grade.
  toks=$(printf '%s\n' "$o" | grep -oE '(^|[^A-Za-z0-9_./~-])[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)+\.(js|sh|py)' \
         | sed -E 's#^[^A-Za-z0-9_.-]##' | sort -u)
  pop=$(printf '%s\n' "$toks" | grep -c . || true)
  while IFS= read -r tok; do
    [ -n "$tok" ] || continue
    git -C "$d" ls-files --error-unmatch -- ":(literal)$tok" >/dev/null 2>&1 || miss="$miss $tok"
  done <<EOF
$toks
EOF
  [ "$pop" -ge 4 ] && [ -z "$miss" ] && got="${got}G" || got="${got}R"
  set -- "(i) the AUDIT stage awaits $kd/tier2-review.js" \
         "(ii) dispatch.scriptPath is $kd/unattended-unit.js" \
         "(iii) dispatch.args.driver runs ${tr}unattended/unattended.sh" \
         "(iv) dispatch.args.checklist runs $mt/gotchas.py" \
         "(v) all $pop emitted js/sh/py path(s) are tracked in the layout"
  for k in 1 2 3 4 5; do
    g=${got:k-1:1}; w=${want:k-1:1}; n=$((n+1))
    if [ "$g" = "$w" ]; then
      [ "$w" = G ] && echo "ok   $label $1" || echo "ok   $label $1 -- REDS, as this control requires"
    else
      echo "FAIL $label $1 -- got $g, want $w"; st=1
    fi
    shift
  done
  if [ "$got" != "$want" ]; then
    echo "     driver    '$(read_field "$res" dispatch.args.driver)'"
    echo "     checklist '$(read_field "$res" dispatch.args.checklist)'"
    echo "     untracked:${miss:- none}"
  fi
}

# ---- AC2: the FLAT layout, which is what both measured adopters are.
FL="$LAY/flat"; build_layout "$FL" scripts/workflows scripts/unattended scripts/gotchas.py
o=$(run_layout "$FL" scripts/workflows)
has "PV-AC5 --check before any render: a missing live copy is a red" "$o" "missing live copy scripts/workflows/unattended-build.js"
has "PV-AC5 ...and it exits 1" "$o" "rc=1"
o=$(run_layout "$FL" scripts/workflows --render)
has "PV-AC5 --render creates the missing live copy" "$o" "rendered scripts/workflows/unattended-build.js from"
has "PV-AC5 ...at exit 0" "$o" "rc=0"
check_layout "PV-AC2 flat:" "$FL" scripts/workflows scripts/ scripts GGGGG
o=$(run_layout "$FL" scripts/workflows)
has "PV-AC2 flat: the parity leg passes on its own render" "$o" "rc=0"
has "PV-AC2 flat: ...and names the directory it probed" "$o" "MEMORY_TREE_DIR 'scripts'"

# ---- AC3: the NESTED layout, and two ROOT installs, one of each memory-tree shape.
NE="$LAY/nested"; build_layout "$NE" scripts/workflows scripts/unattended scripts/memory-tree/gotchas.py
run_layout "$NE" scripts/workflows --render >/dev/null
check_layout "PV-AC3 nested:" "$NE" scripts/workflows scripts/ scripts/memory-tree GGGGG
RT="$LAY/root"; build_layout "$RT" workflows unattended memory-tree/gotchas.py  # gov:root-fixture — the ROOT-install layout PV-AC3 builds on purpose
run_layout "$RT" workflows --render >/dev/null
check_layout "PV-AC3 root:" "$RT" workflows "" memory-tree GGGGG
RF="$LAY/rootflat"; build_layout "$RF" workflows unattended gotchas.py
run_layout "$RF" workflows --render >/dev/null
check_layout "PV-AC3 root, flat memory-tree:" "$RF" workflows "" . GGGGG

# ---- AC4: no checklist script anywhere the probe looks SKIPS the harness pair out loud, and no
# ---- harness is written. rev-5: this was a whole-run exit 2 until round 1's F3 scoped it to the pair
# ---- whose template carries the token; the review-harness-only arms below are why.
NO="$LAY/none"; build_layout "$NO" scripts/workflows scripts/unattended ""
o=$(run_layout "$NO" scripts/workflows --render)
has "PV-AC4 no gotchas.py: --render skips the harness pair by name" "$o" "SKIP scripts/workflows/unattended-build.js"
has "PV-AC4 ...at exit 0, because the protocol pair still rendered" "$o" "rc=0"
has "PV-AC4 ...and names the override" "$o" "set MEMORY_TREE_DIR="
absent_harness=yes; [ -e "$NO/scripts/workflows/unattended-build.js" ] && absent_harness=no
same "PV-AC4 ...and writes no harness" "$absent_harness" "yes"
# The OVERRIDE, both directions: honoured where it names a tracked script, refused where it does not.
OV="$LAY/override"; build_layout "$OV" scripts/workflows scripts/unattended vendor/mt/gotchas.py
o=$( (cd "$OV" && MEMORY_TREE_DIR=vendor/mt bash scripts/workflows/check-protocol-parity.test.sh --render 2>&1; echo "rc=$?") )
has "PV-AC4 override: --render honours MEMORY_TREE_DIR" "$o" "rc=0"
check_layout "PV-AC4 override:" "$OV" scripts/workflows scripts/ vendor/mt GGGGG
o=$( (cd "$OV" && MEMORY_TREE_DIR=vendor/nowhere bash scripts/workflows/check-protocol-parity.test.sh --render 2>&1; echo "rc=$?") )
has "PV-AC4 override naming an untracked script is refused" "$o" "rc=2"
# A TRACKED override that holds a space still refuses: the value lands in a shell command an agent
# runs, where the space splits it. The tracked test passes first, so only the charset arm can stop it.
mkdir -p "$OV/vendor/m t" && printf '# stub\n' > "$OV/vendor/m t/gotchas.py" && ( cd "$OV" && git add -A )
o=$( (cd "$OV" && MEMORY_TREE_DIR='vendor/m t' bash scripts/workflows/check-protocol-parity.test.sh --render 2>&1; echo "rc=$?") )
has "PV-AC4 a tracked override holding a space is refused" "$o" "holds a character outside"
has "PV-AC4 ...at exit 2" "$o" "rc=2"

# ---- ROUND 1 F3: A REFUSAL THAT BELONGS TO ONE PAIR'S TOKEN NEVER BLOCKS A PAIR WITHOUT IT. This
# ---- kit requires agent-cap and nothing else, so an install with no memory-tree kit and no
# ---- unattended kit is legal, and in it nothing tracks a `gotchas.py`. The probe used to exit 2
# ---- before any pair was graded, so that install lost `REVIEW-PROTOCOL.md` too: the document that
# ---- states the concurrency cap could be neither rendered nor graded, over a harness it never runs.
RO="$LAY/review-only"; build_layout "$RO" scripts/workflows - ""
o=$(run_layout "$RO" scripts/workflows --render)
has "PV-F3 review-harness only: --render still renders the protocol" "$o" "rendered memory/guides/REVIEW-PROTOCOL.md from"
has "PV-F3 ...at exit 0" "$o" "rc=0"
has "PV-F3 ...and SKIPS the harness pair out loud, naming why" "$o" "SKIP scripts/workflows/unattended-build.js"
has "PV-F3 ...and names the override that would render it" "$o" "set MEMORY_TREE_DIR="
absent_harness=yes; [ -e "$RO/scripts/workflows/unattended-build.js" ] && absent_harness=no
same "PV-F3 ...and writes no harness" "$absent_harness" "yes"
o=$(run_layout "$RO" scripts/workflows)
has "PV-F3 --check grades the protocol and passes" "$o" "in parity"
has "PV-F3 ...at exit 0" "$o" "rc=0"
has "PV-F3 ...and the green line says a pair went ungraded" "$o" "1 pair(s) SKIPPED"
# THE PROTOCOL IS GRADED, NOT MERELY UNBLOCKED. A skip that also swallowed the protocol pair would pass
# every arm above, so its drift has to still red.
printf 'a hand edit\n' >> "$RO/memory/guides/REVIEW-PROTOCOL.md"
o=$(run_layout "$RO" scripts/workflows)
has "PV-F3 a drifted protocol still reds in that install" "$o" "DRIFT"
has "PV-F3 ...at exit 1" "$o" "rc=1"

# ---- ROUND 2 R2-3: THE REGENERATE REFRESHES AN INSTALL, IT NEVER CREATES ONE. govkit runs the argv
# ---- `kit.toml` declares on every update with GOVKIT_RERENDER=1, captures its output and prints one
# ---- line, and rows nothing it writes. So a render mode that creates a missing live copy put a
# ---- second review protocol into a consumer that keeps its own extract on purpose, and nothing named
# ---- the file. The argv is read out of `kit.toml` and run exactly as declared, because a mode this
# ---- arm chose for itself would pass while the descriptor still asked for the other one.

RG="$LAY/regenerate"; build_layout "$RG" scripts/workflows scripts/unattended scripts/gotchas.py
run_layout "$RG" scripts/workflows --render >/dev/null
( cd "$RG" && git add scripts/workflows/unattended-build.js ) && rm -f "$RG/memory/guides/REVIEW-PROTOCOL.md"
printf '// a stale render\n' >> "$RG/scripts/workflows/unattended-build.js"
rg_argv=$(sed -n '/^\[\[regenerate\]\]/,/^argv/s/^argv = //p' "$HERE/kit.toml")
rg_cmd=$(node -e 'console.log(JSON.parse(process.argv[1]).map(a => a.split("{kit}").join(process.argv[2])).join("\n"))' \
           "$rg_argv" scripts/workflows 2>/dev/null)
n=$((n+1))
if [ -n "$rg_cmd" ]; then echo "ok   PV-R2-3 LIVENESS the regenerate argv was read out of kit.toml"
else echo "FAIL PV-R2-3 LIVENESS no [[regenerate]] argv could be read out of $HERE/kit.toml, so the arms below grade nothing"; st=1; fi
mapfile -t rg_words <<EOF
$rg_cmd
EOF
o=$( (cd "$RG" && "${rg_words[@]}" 2>&1; echo "rc=$?") )
has "PV-R2-3 the declared regenerate exits 0 over an install with no protocol copy" "$o" "rc=0"
has "PV-R2-3 ...and still refreshes the harness this install tracks" "$o" "rendered scripts/workflows/unattended-build.js from"
has "PV-R2-3 ...and names the pair it would not create" "$o" "SKIP memory/guides/REVIEW-PROTOCOL.md"
absent_proto=yes; [ -e "$RG/memory/guides/REVIEW-PROTOCOL.md" ] && absent_proto=no
same "PV-R2-3 ...and writes no protocol the install never had" "$absent_proto" "yes"
hasnt_ "PV-R2-3 ...and the refreshed harness lost its stale line" "$(cat "$RG/scripts/workflows/unattended-build.js")" "a stale render"

# The same mode in --check, which the runbook's migration runs once its first step is done: an absent
# and untracked protocol is a named skip there too, and the harness it tracks is still graded.

o=$( (cd "$RG" && bash scripts/workflows/check-protocol-parity.test.sh --tracked-only 2>&1; echo "rc=$?") )
has "PV-R2-3 --check --tracked-only passes over the same install" "$o" "rc=0"
has "PV-R2-3 ...naming the protocol it skipped" "$o" "SKIP memory/guides/REVIEW-PROTOCOL.md"
has "PV-R2-3 ...and counting it in the green line" "$o" "1 pair(s) SKIPPED"
printf '// drift\n' >> "$RG/scripts/workflows/unattended-build.js"
o=$( (cd "$RG" && bash scripts/workflows/check-protocol-parity.test.sh --tracked-only 2>&1; echo "rc=$?") )
has "PV-R2-3 ...and a drifted harness still reds under it" "$o" "DRIFT"

# THE SKIP NEEDS BOTH HALVES, absent AND untracked, and each half is armed from its own side. A skip
# keyed on the index alone would pass a present untracked copy by, and one keyed on the disk alone
# would leave a tracked copy somebody deleted uninstalled; the arms above see neither.
for rg_case in tracked-deleted present-untracked; do
  RC="$LAY/regenerate-$rg_case"; build_layout "$RC" scripts/workflows scripts/unattended scripts/gotchas.py
  run_layout "$RC" scripts/workflows --render >/dev/null
  if [ "$rg_case" = tracked-deleted ]; then
    ( cd "$RC" && git add -A ) && rm -f "$RC/memory/guides/REVIEW-PROTOCOL.md"
  else
    ( cd "$RC" && git add scripts/workflows/unattended-build.js )
    printf 'an untracked copy, stale\n' > "$RC/memory/guides/REVIEW-PROTOCOL.md"
  fi
  o=$( (cd "$RC" && "${rg_words[@]}" 2>&1; echo "rc=$?") )
  has "PV-R2-3 $rg_case: the declared regenerate still renders the protocol" "$o" "rendered memory/guides/REVIEW-PROTOCOL.md from"
  hasnt_ "PV-R2-3 $rg_case: ...and does not skip it" "$o" "SKIP memory/guides/REVIEW-PROTOCOL.md"
done

# CREATION STAYS WITH THE HAND RENDER a fresh install runs, which the runbook's copy-install step
# prescribes: without the flag, the same install gets the protocol it asks for.

o=$(run_layout "$RG" scripts/workflows --render)
has "PV-R2-3 the hand --render still creates a missing protocol" "$o" "rendered memory/guides/REVIEW-PROTOCOL.md from"

# ---- AC5: the parity script catches what it exists to catch.
cp "$FL/scripts/workflows/unattended-build.js" "$LAY/flat-render.js"
# APPENDED rather than substituted. The first cut edited one path in place, and when the template it
# ran against spelled that path differently the edit matched nothing, the render stayed pristine and
# this arm reported a missing DRIFT for a break that was never staged. An appended line cannot miss.
printf '// a hand edit an adopter made in place\n' >> "$FL/scripts/workflows/unattended-build.js"
o=$(run_layout "$FL" scripts/workflows)
has "PV-AC5 a hand-edited render reds the parity leg" "$o" "DRIFT"
has "PV-AC5 ...at exit 1" "$o" "rc=1"
cp "$LAY/flat-render.js" "$FL/scripts/workflows/unattended-build.js"
cp "$FL/scripts/workflows/REVIEW-PROTOCOL.template.md" "$FL/scripts/workflows/stray.template.md"
( cd "$FL" && git add scripts/workflows/stray.template.md )
o=$(run_layout "$FL" scripts/workflows)
has "PV-AC5 a template with no pair reds the parity leg" "$o" "renders to nothing this script grades: scripts/workflows/stray.template.md"
has "PV-AC5 ...at exit 1" "$o" "rc=1"
( cd "$FL" && git rm -q --cached scripts/workflows/stray.template.md ) && rm -f "$FL/scripts/workflows/stray.template.md"
o=$(run_layout "$FL" scripts/workflows)
has "PV-AC5 control: with the render and the pairs restored the leg is green again" "$o" "rc=0"

# ---- AC6: the two NEGATIVE CONTROLS.
# The harness spelled for THIS repo's install, which is what apply shipped before this unit. The
# three values are this repo's own layout and none of them names a file, so the carried-prefix ban
# has nothing here to count.
VB="$LAY/verbatim"; build_layout "$VB" scripts/workflows scripts/unattended scripts/gotchas.py
sed -e 's|{{KIT_DIR}}|tools/workflows|g' -e 's|{{TOOL_ROOT}}|tools/|g' -e 's|{{MEMORY_TREE_DIR}}|tools/memory-tree|g' \
    "$HERE/unattended-build.template.js" > "$VB/scripts/workflows/unattended-build.js"
check_layout "PV-AC6 the verbatim spelling:" "$VB" scripts/workflows scripts/ scripts RRRRR
# The prefix-only half-fix: correct for this repo, and wrong for both measured adopters.
HF="$LAY/halffix"; build_layout "$HF" scripts/workflows scripts/unattended scripts/gotchas.py
sed -i 's|{{MEMORY_TREE_DIR}}/gotchas.py|{{TOOL_ROOT}}memory-tree/gotchas.py|' "$HF/scripts/workflows/unattended-build.template.js"
( cd "$HF" && git add -A )
run_layout "$HF" scripts/workflows --render >/dev/null
check_layout "PV-AC6 the prefix-only half-fix:" "$HF" scripts/workflows scripts/ scripts GGGRR

# ---- PV-AC12: THE TWO CARRIERS OF ONE COMMAND AGREE. The build harness hands each child the
# ---- bug-class checklist, and the unattended Skill tells the run to execute the same checklist.
# ---- Each kit derives the path with ITS OWN copy of the probe, because kits install separately and
# ---- share no code — and two copies of one derivation drift apart without anyone deciding to change
# ---- either. So this arm renders BOTH in one layout, through each kit's own renderer, and compares
# ---- the two commands they produce, rather than trusting two sources to stay alike.
UK="$ROOT/$KIT_REL/unattended"
if [ -f "$UK/adopt-unattended.sh" ]; then
  for shape in flat nested; do
    X="$LAY/carriers-$shape"
    case $shape in flat) gp=scripts/gotchas.py ;; *) gp=scripts/memory-tree/gotchas.py ;; esac
    build_layout "$X" scripts/workflows scripts/unattended "$gp"
    cp "$UK/adopt-unattended.sh" "$UK/unattended.sh" "$UK/lib-unattended.sh" "$UK/check-unattended.sh" \
       "$UK"/*.template.md "$X/scripts/unattended/"
    printf 'MEMORY_ROOT=memory\nLANDER="true"\nKEEPALIVE_CREATE="c"\nKEEPALIVE_DELETE="d"\nKEEPALIVE_INTERVAL="i"\n' \
      > "$X/.unattended.conf"
    ( cd "$X" && git add -A )
    run_layout "$X" scripts/workflows --render >/dev/null
    ( cd "$X" && bash scripts/unattended/adopt-unattended.sh >/dev/null 2>&1 )
    o=$(run_wf "$UNITS" "$(returns CONVERGED 0)" "$X/scripts/workflows/unattended-build.js")
    hc=$(read_field "$(printf '%s\n' "$o" | sed -n 's/^RESULT //p')" dispatch.args.checklist)
    sc=""
    [ -f "$X/.claude/skills/unattended/SKILL.md" ] && \
      sc=$(grep -oE 'python [^ ]*gotchas[.]py --for-diff HEAD~1[.][.]HEAD' "$X/.claude/skills/unattended/SKILL.md" | head -1)
    n=$((n+1))
    if [ -n "$hc" ] && [ "$hc" = "$sc" ]; then
      echo "ok   PV-AC12 $shape: the harness and the Skill name one checklist command -- $hc"
    else
      echo "FAIL PV-AC12 $shape: the harness hands out '$hc' and the Skill tells the run '$sc'"; st=1
    fi
  done
else
  echo "SKIP PV-AC12 -- no unattended adopter at $UK, so the two carriers were NOT compared on this run"
fi

echo "--- $n arms, exit $st"
exit $st
