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
      for (const k of Object.keys(returns)) if (label.indexOf(k) === 0) return schemaShaped(returns[k], opts && opts.schema)
      return null
    }
    // TOOL-dMergedTally-1 - `RUN_WF_SCHEMA=strict` makes the double answer AS ITS SCHEMA ALLOWS: a
    // value missing a key the schema requires comes back null, which is how a validation failure in
    // the runtime reaches a script, and a top-level key the schema does not declare is dropped. Without
    // it a double returns a field the callee never asked for, and an arm passes over a schema that
    // was reverted (closing review, T1). Opt-in, because older fixtures predate the schemas they meet.
    const schemaShaped = (v, schema) => {
      if (process.env.RUN_WF_SCHEMA !== "strict" || !schema || !v || typeof v !== "object") return v
      if ((schema.required || []).some((k) => !(k in v))) return null
      const out = {}
      for (const k of Object.keys(v)) if (schema.properties && k in schema.properties) out[k] = v[k]
      return out
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
    // THE ARGS ARE TRACED TOO (closing review round 2, cluster E). The double recorded `ref` alone,
    // so nothing could see which ROUND the callee was handed; the harness passed the invocation
    // round and every promoted-spec audit was primed as a fold review of a spec nobody had read.
    const workflow = async (ref, wargs) => {
      trace.push("workflow:" + ((ref && ref.scriptPath) || String(ref)))
      trace.push("wargs:" + JSON.stringify(wargs))
      return returns["workflow"] || {}
    }
    const budget = { total: null, spent: () => 0, remaining: () => Infinity }
    const fn = new AsyncFunction("args", "agent", "parallel", "pipeline", "phase", "log", "budget", "workflow", src)
    fn(JSON.parse(process.argv[2]), agent, parallel, pipeline, phase, log, budget, workflow)
      .then((r) => { console.log(trace.join("\n")); console.log("RESULT " + JSON.stringify(r)) })
      .catch((e) => { console.log(trace.join("\n")); console.log("THROW " + e.message) })
  ' "${3:-$F}" "$1" "$2" 2>&1
}

UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","subjects":[{"path":"s1","blob":"abc1234"},{"path":"s2","blob":"def5678"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1"},{"id":"A-tB-2","order":1,"specPath":"s2","briefPath":"b2"},{"id":"A-tB-3","order":2,"specPath":"s3","briefPath":"b3"}]}'
SPEC_OK='{"authored":["A-tB-1"],"alreadyPresent":["A-tB-2","A-tB-3"],"refused":[],"summary":"ok"}'
# TOOL-aHoistedPass-6 - the BUILD double is gone with the stage. What a terminal verdict now
# reaches is the DISPOSAL stage, and past it the roster hand-out, which is a return rather than an
# agent. `returns` takes an optional THIRD argument so an arm can hand back a FAILED disposal.
DISPOSE_OK='{"disposed":true,"standing":[],"promoted":0,"folded":0,"promotedIds":[],"edges":[],"placements":[],"summary":"ok"}'
# THE DOUBLE RETURNS THE CALLEE'S REAL KEYS, and the first version of it did not. It invented
# `verdict` and `reportPath`, so all 28 arms passed on two fields `tier2-review.js` has never
# returned — the harness and its callee had never met. Its actual returns carry `blockers`,
# `report`, `highs`, `note`, `precision` and `confirmed`; there is no `verdict` anywhere but
# per-FINDING. TOOL-aProbedUnit-7: `confirmed` was the one real key it omitted, and the disposal
# stage now decides on it — `review_out <blockers> [confirmed] [highs] [unverified]`, `confirmed`
# defaulting to the blocker count and `highs` and `unverified` to 0, so every existing call site
# keeps a return that reconciles. `unverified` joined at the closing review's cluster F, because the
# harness now refuses a synthesis return without it and disposes it beside `confirmed`.
review_out() { printf '{"blockers":%s,"confirmed":%s,"highs":%s,"unverified":%s,"report":"r.md","precision":1,"note":"n"}' "$1" "${2:-$1}" "${3:-0}" "${4:-0}"; }
# The CONVERGENCE token is the driver's, recorded by an agent, so it is a separate fixture. Keeping
# them separate is the point: a run can produce a clean review and still not converge.
rec() { printf '{"token":"%s","exitCode":0}' "$1"; }
# `audit <token> <blockers>` still reads as one thing at the call sites, but it now feeds the two
# halves their own shapes. The DEFAULT disposal double is built from the count it is paired with —
# `promoted` equal to the blockers, `folded` 0, and one `promotedIds` entry whenever it promoted —
# so the arms that pair `NON-CONVERGENT 2` with it still reconcile against the reconciling guard,
# in sum and in severity split, and still receive the full roster.
returns() { local dflt ids='[]' places='[]'
  # A PROMOTING DEFAULT PLACES ITS UNIT, because TOOL-cMendedVintage-19 refuses a promotion that
  # declares no placement. `A-tB-3` is the last unit of `$UNITS` at order 2, so a repair of it sits
  # at 3 — one above, the rule's own arithmetic rather than a number picked to pass.
  [ "${2:-0}" -gt 0 ] && { ids='["A-tB-p"]'; places='[{"unit":"A-tB-p","repairs":"A-tB-3","order":3}]'; }
  dflt=$(printf '{"disposed":true,"standing":[],"promoted":%s,"folded":0,"promotedIds":%s,"edges":[],"placements":%s,"summary":"ok"}' "${2:-0}" "$ids" "$places")
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
# A POSITIVE COUNT FOR THE THREE EXITS THE DRIVER ONLY REACHES ON ONE. `review_state` returns
# CONVERGED for a count of 0 and for nothing else, so NON-CONVERGENT, CEILING and BOUNDED beside 0
# was a pairing no driver prints; the harness refuses it both ways since closing review round 2,
# cluster B, and this fixture used to hand the harness the impossible shape.
for v in CONVERGED NON-CONVERGENT CEILING BOUNDED; do
  o=$(run_wf "$UNITS" "$(returns "$v" "$([ "$v" = CONVERGED ] && echo 0 || echo 1)")")
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
o=$(run_wf "$UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"},"dispose":{"disposed":true,"standing":[],"summary":"d"}}')
has  "default mode: the round IS recorded through the driver" "$o" "agent:audit:record"
has  "default mode: the return names the child the caller dispatches" "$o" '"scriptPath":"tools/workflows/unattended-unit.js"'
has  "default mode: hands out a roster" "$o" '"roster":[{'

# ---- AC1: attended mode reaches BUILD and spawns NO recorder agent.
A_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1","planState":"READY"}]}'
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"dispose":{"disposed":true,"standing":[],"summary":"d"}}')
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
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":2,"confirmed":2,"highs":0,"unverified":0,"report":"r.md"}}')
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
F_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"FORKED"}]}'
o=$(run_wf "$F_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
has  "attended, FORKED unit: refuses" "$o" "THROW"
has  "attended, FORKED unit: names the id" "$o" "A-tB-1"
has  "attended, FORKED unit: names the state" "$o" "FORKED"

# ---- AC11: the terminal-unit SKIP, with the vocabulary --plan actually emits. `DONE (FORKED)` is
# ---- what a closed build reports for a unit whose underlying grade was not READY, and a five-token
# ---- allow-list halts on it — round-1's halt-at-unit-one, for the third time.
D_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"DONE (FORKED)"},{"id":"A-tB-2","order":2,"specPath":"s2","planState":"READY"}]}'
o=$(run_wf "$D_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
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
X_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"WOBBLE"}]}'
o=$(run_wf "$X_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
has  "attended, unknown state: refuses" "$o" "THROW"
has  "attended, unknown state: names the value it did not recognise" "$o" "WOBBLE"

# ---- AC12: a missing planState refuses rather than defaulting. A defaulted state puts the refusal
# ---- predicate to work on a value nobody supplied.
M_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1"}]}'
o=$(run_wf "$M_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
has  "attended, no planState: refuses" "$o" "THROW"
has  "attended, no planState: names the field" "$o" "planState"

# ---- AC14: the FRESH-BUILD path. A unit stage 1 authors reports MISSING at entry — there is no point
# ---- between the stages at which a caller could re-run --plan — so the entry-time value is stale by
# ---- construction and the stage must not refuse the build it just specced.
N_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"MISSING"}]}'
o=$(run_wf "$N_UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
has  "attended, unit AUTHORED this invocation: rostered despite entry-time MISSING" "$o" '"roster":[{'
# and the control: the same MISSING state, NOT specced by stage 1, must still refuse.
o=$(run_wf "$N_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":["A-tB-1"],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
has  "attended, MISSING and NOT specced: still refuses" "$o" "THROW"
# M1 - `alreadyPresent` must NOT exempt. Those are the units the stage did NOT touch, so their
# entry-time grade is current; exempting them bypassed the THIN/FORKED refusal on an agent's
# say-so. Only `authored` is stale by construction.
o=$(run_wf "$N_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
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
W_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","runStateExists":true,"subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"READY"}]}'
o=$(run_wf "$W_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
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
S3='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","subjects":[{"path":"s1","blob":"abc1234"}],"units":[
  {"id":"A-tB-1","order":1,"specPath":"s1","specBriefPath":"bf1"},
  {"id":"A-tB-2","order":2,"specPath":"s2","specBriefPath":"bf2"},
  {"id":"A-tB-3","order":3,"specPath":"s3","specBriefPath":"bf3"}]}'
o=$(run_wf "$S3" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
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
S7='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","subjects":[{"path":"s1","blob":"abc1234"}],"units":[
  {"id":"A-tB-1","order":1,"specPath":"s1"},{"id":"A-tB-2","order":2,"specPath":"s2"},
  {"id":"A-tB-3","order":3,"specPath":"s3"},{"id":"A-tB-4","order":4,"specPath":"s4"},
  {"id":"A-tB-5","order":5,"specPath":"s5"},{"id":"A-tB-6","order":6,"specPath":"s6"},
  {"id":"A-tB-7","order":7,"specPath":"s7"}]}'
o=$(run_wf "$S7" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
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
o=$(run_wf "$S3" '{"spec:tB:g0":null,"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has "one dead writer: reported as DEGRADED" "$o" "DEGRADED — 1 of 3 writer(s) returned nothing"
has "one dead writer: its unit lands in refused" "$o" "A-tB-1"
has "one dead writer: the run still reaches the hand-out" "$o" '"roster":[{'

# ---- AC4, second half: EVERY writer dead must THROW. The old guard was `if (!specced)` on a falsy
# ---- return, and a merged object is always truthy — so without this an entirely dead spec stage
# ---- reaches AUDIT and BUILD on whatever specs already existed, with the refusal this file spends
# ---- six lines justifying silently deleted.
o=$(run_wf "$S3" '{"spec":null,"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has   "ALL writers dead: THROWS" "$o" "THROW"
has   "ALL writers dead: says every writer returned nothing" "$o" "EVERY spec writer returned nothing"
hasnt_ "ALL writers dead: no roster is ever handed out" "$o" '"roster"'

# ---- AC7/S3c: the writers are told to AUTHOR and never COMMIT, and not to run the generator. That is
# ---- half of clause 3 of the disjointness proof, and no gate downstream of here reads a prompt.
o=$(run_wf "$S3" '{"spec":{"authored":["x"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
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
    "$SPEC_OK" "$(review_out 0 4 1)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":3,"promotedIds":["A-tB-4"],"edges":[],"placements":[{"unit":"A-tB-4","repairs":"A-tB-3","order":3}],"summary":"d"}')")
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
o=$(run_wf "$UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":2,"confirmed":1,"highs":0,"unverified":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has    "V4 blockers above confirmed: REFUSES" "$o" "THROW"
has    "V4 blockers above confirmed: the message names confirmed" "$o" "returned confirmed"
hasnt_ "V4 blockers above confirmed: the stage is never reached" "$o" "phase:Disposal"
# ---- V5: ATTENDED mode reaches the stage at zero blockers with two confirmed, and its prompt
# ---- promotes through the README's roster table, never through --rescope, which fail 48s with no
# ---- run-state file. The RESULT is the attended MAIN return, since A_UNITS is READY.
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":2,"highs":0,"unverified":0,"report":"r.md"},"dispose":{"disposed":true,"standing":[],"promoted":0,"folded":2,"edges":[],"placements":[],"summary":"d"}}')
has    "V5 attended with confirmed findings: the disposal agent RUNS" "$o" "agent:dispose:tB"
has    "V5 attended: the prompt promotes through the README roster" "$o" "authored Units table"
hasnt_ "V5 attended: the prompt never orders --rescope" "$o" "--rescope tB"
has    "V5 attended: the main return carries the stage's counts" "$o" '"promoted":0,"folded":2'

# ======================= TOOL-dMergedTally-1 — THE SEVERITY SPLIT IS COUNTED IN THE UNIT `confirmed` IS
# The guard computes `mustFold = confirmed - (blockers + highs)`. `confirmed` counts RAW findings, and
# the synthesis typed `blockers` and `highs` over the ITEMS it merged raw findings into. Measured on
# dLoggedFlight's round-1 spec audit of units 14 and 15: 48 raw, 13 confirmed, merged into 10 items —
# 1 BLOCKER and 5 HIGH by item, 3 and 6 by raw finding, 4 MEDIUM either way. The harness got blockers
# 1 and highs 5, demanded 7 folds of 4 MEDIUMs, and refused the only honest disposal, 9 promoted and
# 4 folded. Every `review_out` fixture above hands the harness integers it chose, which is why no arm
# could see this: the two numbers were never produced by the callee. So these arms RUN the callee,
# with only its agents doubled, and feed the harness the callee's own RESULT line. The SYNTHESIS
# double merges the way the measured one did and carries both halves of what it could return: the
# two integers the old schema demanded, as the measured synthesis typed them, and the item list the
# new one demands. One fixture therefore runs against either revision — observed RED on every arm
# below against the unchanged render and callee, GREEN after.
MT_T2="$HERE/tier2-review.js"
MT_ARGS='{"repo":"/tmp/r","kind":"spec-audit","subjects":[{"path":"s1","blob":"abc1234"}],"round":1,"reviewDir":"r/"}'
# `build_merged_returns <items-json|absent> [judged] [shape-json]`: four lenses of twelve findings each
# are ids 1-48; the skeptic double judges ids 1 to `judged` (default 48), confirming the thirteen below
# and refuting the rest, so an id above `judged` comes back UNVERIFIED; the synthesis double returns
# the given items, or no `items` key at all for `absent`. `shape` replaces the measured audit the
# double replays: `confirmed` ids, `lenses` as label prefix to finding count in the order the double
# matches them, `typed` as the blockers and highs that audit's synthesis typed, and its `summary`.
# `run_merged_review <returns>` runs the callee with its doubles answering as their SCHEMAS allow, so
# a synthesis schema that stopped requiring `items` drops the key and reds the counting arms.
build_merged_returns() {
  node -e '
    const shape = process.argv[3] ? JSON.parse(process.argv[3]) : {
      confirmed: [1, 4, 7, 9, 11, 14, 16, 20, 22, 26, 30, 33, 40],
      lenses: { "find:": 12 }, typed: [1, 5], summary: "13 confirmed in 10 items" }
    const confirmed = new Set(shape.confirmed)
    const finding = { file: "s1", where: "section 2", severity: "high", claim: "c", impact: "i", fix: "f" }
    const verdicts = Array.from({ length: Number(process.argv[2]) }, (_, i) =>
      ({ id: i + 1, verdict: confirmed.has(i + 1) ? "confirmed" : "refuted", reason: "r" }))
    const out = {}
    for (const [prefix, count] of Object.entries(shape.lenses))
      out[prefix] = { lens: "l", findings: Array.from({ length: count }, () => finding) }
    out["verify:"] = { verdicts }
    out.synth = { path: "r/merged.md", summary: shape.summary, blockers: shape.typed[0], highs: shape.typed[1],
      items: process.argv[1] === "absent" ? undefined : JSON.parse(process.argv[1]) }
    console.log(JSON.stringify(out))
  ' "$1" "${2:-48}" "${3:-}"
}
# The measured record's two merges are B1 (14, 26, 40) and H2 (16, 4); every other item holds one id.
MT_MERGED='[{"severity":"BLOCKER","ids":[14,26,40]},{"severity":"HIGH","ids":[1]},{"severity":"HIGH","ids":[16,4]},{"severity":"HIGH","ids":[7]},{"severity":"HIGH","ids":[9]},{"severity":"HIGH","ids":[11]},{"severity":"MEDIUM","ids":[20]},{"severity":"MEDIUM","ids":[22]},{"severity":"MEDIUM","ids":[30]},{"severity":"MEDIUM","ids":[33]}]'
# Every promoted unit is PLACED (TOOL-cMendedVintage-19): `A-tB-3` is the last roster unit at order 2,
# so a repair of it sits at 3 — the doubles below were written before that rule and never re-fed it.
MT_DISPOSE='{"disposed":true,"standing":[],"promoted":9,"folded":4,"refuted":0,"promotedIds":["A-tB-16","A-tB-17","A-tB-18","A-tB-19"],"edges":[],"placements":[{"unit":"A-tB-16","repairs":"A-tB-3","order":3},{"unit":"A-tB-17","repairs":"A-tB-3","order":3},{"unit":"A-tB-18","repairs":"A-tB-3","order":3},{"unit":"A-tB-19","repairs":"A-tB-3","order":3}],"summary":"9 promoted into 4 units, 4 folded"}'
run_merged_review() { RUN_WF_SCHEMA=strict run_wf "$MT_ARGS" "$1" "$MT_T2"; }
run_merged_build() { # callee RESULT json · [driver token] · [disposal double] -> the build harness run over it
  run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "${1:-null}" "$(rec "${2:-BOUNDED}")" "${3:-$MT_DISPOSE}")"
}
t2=$(run_merged_review "$(build_merged_returns "$MT_MERGED")")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
# LIVENESS FIRST. Without it a fixture that broke into an empty review would skip the disposal stage
# and hand out a roster, and the roster arm below would pass over a stage that never ran.
has    "MT the callee ran over the measured shape — 48 raw, 13 confirmed" "$au" '"raw":48,"confirmed":13'
has    "MT the callee counts blockers and highs over RAW confirmed findings, not over items" "$au" '"blockers":3,"highs":6'
o=$(run_merged_build "$au")
has    "MT the disposal stage RAN over the callee's counts" "$o" "agent:dispose:tB"
has    "MT promoted 9 and folded 4, by raw id, is ACCEPTED" "$o" "disposal: done — promoted 9 · folded 4"
hasnt_ "MT ...and is not refused as a bad severity split" "$o" "do not split by severity"
has    "MT ...and the roster is handed out" "$o" '"roster":[{'
# THE REFUSAL, both ways. A confirmed id the item list places nowhere, or in two items, leaves the
# raw split unknowable; the callee returns NEITHER count and names the id, and the harness refuses
# the null as a degraded run rather than reading it as zero.
t2=$(run_merged_review "$(build_merged_returns "$(printf '%s' "$MT_MERGED" | sed 's/,{"severity":"MEDIUM","ids":\[33\]}//')")")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
has    "MT a confirmed id in NO item returns neither count" "$au" '"blockers":null,"highs":null'
has    "MT ...and the note names the id" "$au" "confirmed id(s) 33 sit in no item"
t2=$(run_merged_review "$(build_merged_returns "$(printf '%s' "$MT_MERGED" | sed 's/"ids":\[20\]/"ids":[20,4]/')")")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
has    "MT a confirmed id in TWO items returns neither count" "$au" '"blockers":null,"highs":null'
has    "MT ...and the note names the id" "$au" "confirmed id(s) 4 sit in more than one item"
o=$(run_merged_build "$au")
has    "MT the harness REFUSES the null count" "$o" "non-integer blocker count"
hasnt_ "MT ...before the disposal stage" "$o" "phase:Disposal"
# AND ONLY CONFIRMED IDS ARE COUNTED. The prompt lets the synthesis list an UNVERIFIED id, which the
# disposal stage adjudicates itself, so id 48 left unjudged and listed at BLOCKER moves neither count.
t2=$(run_merged_review "$(build_merged_returns "$(printf '%s' "$MT_MERGED" | sed 's/\[14,26,40\]/[14,26,40,48]/')" 47)")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
has    "MT an UNVERIFIED id listed in an item is left uncounted" "$au" '"unverified":1,'
has    "MT ...so the raw counts stay 3 and 6" "$au" '"blockers":3,"highs":6'
# A SEVERITY OUTSIDE THE CLOSED FOUR places nothing, and a lowercase one is the same word: the
# finders' schema spells all four that way.
t2=$(run_merged_review "$(build_merged_returns "$(printf '%s' "$MT_MERGED" | sed 's/"MEDIUM","ids":\[33\]/"CRITICAL","ids":[33]/')")")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
has    "MT a severity outside the closed four leaves its ids unplaced" "$au" "confirmed id(s) 33 sit in no item"
t2=$(run_merged_review "$(build_merged_returns "$(printf '%s' "$MT_MERGED" | sed 's/"HIGH","ids":\[1\]/"high","ids":[1]/')")")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
has    "MT a lowercase severity is the same word" "$au" '"blockers":3,"highs":6'
# THE SCHEMA IS ASKED FOR, and the strict runner is live (closing review T1). The synthesis prompt
# names `items`, and a synthesis double with no `items` key is refused the way the runtime refuses a
# return missing a required key: the callee reads a dead synthesis, so neither count is invented.
t2=$(run_merged_review "$(build_merged_returns "$MT_MERGED")")
has    "MT the synthesis prompt asks for the item list" "$(printf '%s\n' "$t2" | grep '^prompt:synth:')" 'Return JSON {path, items, summary}'
t2=$(run_merged_review "$(build_merged_returns absent)")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
has    "MT a synthesis return without items is refused by its schema" "$au" 'the synthesis agent died'
has    "MT ...and neither count is invented" "$au" '"blockers":null,"highs":null'
# NOTHING CONFIRMED, EVERYTHING UNVERIFIED (closing review T3). The counts are derived here too, and
# an empty item list over an empty confirmed set is a RESULT at 0, never a fault: the harness must
# reach the disposal stage for the 48 findings no skeptic judged, record the round after it, and
# accept a disposal that folds them all.
t2=$(run_merged_review "$(build_merged_returns '[]' 0)")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
has    "MT zero confirmed and 48 unverified reaches the synthesis" "$au" '"confirmed":0,"refuted":0,"unverified":48'
has    "MT ...and an empty item list counts 0 and 0, not null" "$au" '"blockers":0,"highs":0'
o=$(run_merged_build "$au" CONVERGED '{"disposed":true,"standing":[],"promoted":0,"folded":48,"refuted":0,"promotedIds":[],"edges":[],"placements":[],"summary":"s"}')
has    "MT ...and the harness disposes the unverified population" "$o" "disposal: done — promoted 0 · folded 48"
# THE SECOND MEASURED AUDIT, dLoggedFlight's round-1 spec audit of units 14, 16 and 20, ran on the
# unfixed harness and failed the same way with a wider gap. 46 raw, 16 confirmed, merged into 9 items:
# 2 BLOCKER, 3 HIGH, 3 MEDIUM and 1 LOW by item, 4, 6, 5 and 1 by raw finding. The synthesis typed
# blockers 2 and highs 3, so the guard demanded 11 folds where only 6 raw findings sit at MEDIUM or
# LOW, and no honest disposal passed, by raw id (10 and 6) or by item (5 and 4). The arms below replay
# that record's own merges, B1 (38, 29), B2 (39, 30), H1 (1, 20, 43), H3 (40, 31), M1 (25, 9) and
# M2 (41, 6), with H2, M3 and L1 one id each. One lens returns 10 findings and three return 12.
MT20_SHAPE='{"confirmed":[1,2,6,9,10,16,20,25,29,30,31,38,39,40,41,43],"lenses":{"find:underspecification":10,"find:":12},"typed":[2,3],"summary":"16 confirmed in 9 items"}'
MT20_MERGED='[{"severity":"BLOCKER","ids":[38,29]},{"severity":"BLOCKER","ids":[39,30]},{"severity":"HIGH","ids":[1,20,43]},{"severity":"HIGH","ids":[2]},{"severity":"HIGH","ids":[40,31]},{"severity":"MEDIUM","ids":[25,9]},{"severity":"MEDIUM","ids":[41,6]},{"severity":"MEDIUM","ids":[16]},{"severity":"LOW","ids":[10]}]'
MT20_DISPOSE='{"disposed":true,"standing":[],"promoted":10,"folded":6,"refuted":0,"promotedIds":["A-tB-21","A-tB-22","A-tB-23","A-tB-24"],"summary":"10 promoted into 4 units, 6 folded"}'
t2=$(run_merged_review "$(build_merged_returns "$MT20_MERGED" 46 "$MT20_SHAPE")")
au=$(printf '%s\n' "$t2" | sed -n 's/^RESULT //p')
# LIVENESS, and the MERGE is part of it: a double that put one id in each item would count 4 and 6
# too, and would reproduce nothing the record measured.
has    "MT20 the callee ran over the measured shape — 46 raw, 16 confirmed, 30 refuted" "$au" '"raw":46,"confirmed":16,"refuted":30,"unverified":0'
has    "MT20 ...over nine items that split differently by item and by raw finding" "$t2" "by item 2/3/3/1, by raw confirmed finding 4/6/5/1"
has    "MT20 the callee counts blockers and highs over RAW confirmed findings, not over items" "$au" '"blockers":4,"highs":6'
# THE MEASURED REFUSAL, reproduced as a control: the same RESULT carrying the integers that audit's
# synthesis typed refuses the raw-id disposal, so the arms after it can tell the counts apart.
o=$(run_merged_build "$(printf '%s' "$au" | sed 's/"blockers":4,"highs":6/"blockers":2,"highs":3/')" BOUNDED "$MT20_DISPOSE")
has    "MT20 control: item-typed counts refuse the raw-id disposal, as measured" "$o" "folded 6 is below the 11 confirmed at MEDIUM or LOW"
o=$(run_merged_build "$au" BOUNDED "$MT20_DISPOSE")
has    "MT20 the disposal stage RAN over the callee's counts" "$o" "agent:dispose:tB"
has    "MT20 promoted 10 and folded 6, by raw id, is ACCEPTED" "$o" "disposal: done — promoted 10 · folded 6"
hasnt_ "MT20 ...and is not refused as a bad severity split" "$o" "do not split by severity"
has    "MT20 ...and the roster is handed out" "$o" '"roster":[{'
# ONE BASIS BOTH WAYS. A disposal counted by ITEM no longer reconciles, and one that promotes the item
# count while folding the rest has folded raw HIGH or BLOCKER findings into prose.
o=$(run_merged_build "$au" BOUNDED '{"disposed":true,"standing":[],"promoted":5,"folded":4,"refuted":0,"promotedIds":["A-tB-21"],"summary":"by item"}')
has    "MT20 a disposal counted by item is REFUSED" "$o" "promoted 5 + folded 4 + refuted 0 + standing 0 is not confirmed 16 + unverified 0"
o=$(run_merged_build "$au" BOUNDED '{"disposed":true,"standing":[],"promoted":5,"folded":11,"refuted":0,"promotedIds":["A-tB-21"],"summary":"item promotions"}')
has    "MT20 promoting only the item count is REFUSED by the raw floor" "$o" "promoted 5 is below blockers 4 + highs 6"
hasnt_ "MT20 ...and hands out no roster" "$o" '"roster":[{'

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
T_UNITS='{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","specAudit":"2026-09-20","mode":"attended","subjects":[{"path":"s1","blob":"abc1234"}],"units":[{"id":"A-tB-1","order":1,"specPath":"s1","planState":"DONE"}]}'
o=$(run_wf "$T_UNITS" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"}}')
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
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"unverified":0,"report":"r.md"},"dispose":{"disposed":true,"standing":[],"summary":"d"}}')
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
# Reachable on any confirmed finding since TOOL-aProbedUnit-7; these arms keep the NON-CONVERGENT shape.
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

# ==================== CLOSING REVIEW ROUND 1 — CLUSTERS B, C, D, E, F (spec 7 rev-4)
# Every arm below was observed RED against a frozen copy of the base render, one arm at a time, with
# this suite's preamble sourced, before the harness moved.

# ---- B (ids 10, 5): the review subject is keyed per spec-set GENERATION, so a promoted unit has an
# ---- audit route. The literal `<slug>-spec-set` was terminal after its one round and `verb_review`
# ---- refused a second; the promoted spec was built unaudited.
o=$(run_wf "$UNITS" "$(returns BOUNDED 1)")
p=$(printf '%s\n' "$o" | grep '^prompt:audit:record:r1:')
has    "B round 1 records under the generation key" "$p" "--subject tB-spec-set-r1 --verdict"
hasnt_ "B ...and never under the bare literal" "$p" "--subject tB-spec-set --verdict"
has    "B a BOUNDED exit with a promotion carries promotedIds out" "$o" '"promotedIds":["A-tB-p"]'
has    "B ...and orders the audit of the promoted specs BEFORE any is dispatched" "$o" "AUDIT the promoted specs before any of them is dispatched"
has    "B ...naming the re-invocation's round and auditIds" "$o" 'round: 2, auditIds: [\"A-tB-p\"] and no subjectRound'
has    "B ...and still hands out the roster" "$o" '"roster":[{'
# The round-2 re-invocation over the promoted id: a fresh subject, no throw, and the resolver sees
# ONLY the promoted unit. `subjects` is stripped because the harness REFUSES the pair (closing
# review round 2, cluster C, armed below): this fixture used to strip it "so the resolver stage
# actually runs", which was the arm working around a seam the code let through.
NOSUBJ=$(printf '%s' "$UNITS" | sed 's#"subjects":\[[^]]*\],##' | sed 's#"slug":"tB",#"slug":"tB","round":2,"auditIds":["A-tB-3"],#')
# TOOL-aWokenSentinel-15 - the stubbed RESOLVER return carries a full 40-hex `blob` and an equal
# `tree`, because the resolver branch refuses anything shorter by name before it compares the two.
# The supplied-subject fixtures in `$UNITS` keep their 7-hex blobs: they never enter that branch.
B40=0123456789abcdef0123456789abcdef01234567
T40=fedcba9876543210fedcba9876543210fedcba98
o=$(run_wf "$NOSUBJ" "$(printf '{"spec:":%s,"audit:subjects":{"subjects":[{"path":"s3","blob":"%s","tree":"%s"}]},"workflow":%s,"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$B40" "$B40" "$(review_out 0)" "$(rec CONVERGED)" "$DISPOSE_OK")")
has    "B round 2 over the promoted id does not throw" "$o" "RESULT"
p=$(printf '%s\n' "$o" | grep '^prompt:audit:record:r2:')
has    "B round 2 records under its own generation key" "$p" "--subject tB-spec-set-r2 --verdict"
p=$(printf '%s\n' "$o" | grep '^prompt:audit:subjects:r2:')
has    "B round 2 the resolver is scoped to the promoted unit" "$p" "A-tB-3"
hasnt_ "B round 2 ...and sees no unit outside auditIds" "$p" "A-tB-1"
has    "B round 2 the scoping is logged with the subject" "$o" "scoped to 1 promoted unit(s) — A-tB-3 · subject tB-spec-set-r2"
# A fold re-invoke keeps the SAME subject: `subjectRound` names the generation's first round, and
# the CONVERGING return hands it back so the caller copies rather than derives it.
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":3,"subjectRound":2,#')" "$(returns CONVERGING 3)")
p=$(printf '%s\n' "$o" | grep '^prompt:audit:record:r3:')
has    "B a fold re-invoke at round 3 with subjectRound 2 records under -r2" "$p" "--subject tB-spec-set-r2 --verdict"
has    "B ...and the CONVERGING return carries subjectRound" "$o" '"subjectRound":2'
has    "B ...and its nextAction names it" "$o" "round: 4, subjectRound: 2"
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":2,"subjectRound":3,#')" "$(returns CONVERGED 0)")
has    "B a subjectRound above round is REFUSED" "$o" "is above \`round\`"
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":2,"auditIds":["A-tB-9"],#')" "$(returns CONVERGED 0)")
has    "B an auditIds entry outside units is REFUSED by name" "$o" 'names A-tB-9, which `units` does not carry'
# The terminal-subject refusal is its own outcome, and the throw names the remedy.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":{"terminalSubject":true,"exitCode":1,"stderr":"fail 37"},"dispose:":%s}' "$SPEC_OK" "$(review_out 0)" "$DISPOSE_OK")")
has    "B a terminal-subject refusal THROWS by name" "$o" "the subject is terminal, re-key it"
has    "B ...naming the subject it refused" "$o" '`tB-spec-set-r1` already carries a terminal review round'
hasnt_ "B ...and not as an unrecorded round" "$o" "the round was not recorded"
# The prompt's promise is now routed: `auditIds` is a line of the program.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2)")
p=$(printf '%s\n' "$o" | grep '^prompt:dispose:tB:')
hasnt_ "B the disposal prompt no longer promises an audit nothing routes" "$p" "audited once as a spec"
has    "B ...and names the route that does" "$p" 'audits it as a spec, under `auditIds`, before it is built'
has    "B ...and asks for promotedIds" "$p" 'name every promoted unit id in `promotedIds`'

# ---- C (harness end): `--disposition promote` rides the record command at a CONVERGED exit with
# ---- highs, so the merge bar demands the units the highs became.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 4 1)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":3,"promotedIds":["A-tB-4"],"edges":[],"placements":[{"unit":"A-tB-4","repairs":"A-tB-3","order":3}],"summary":"d"}')")
p=$(printf '%s\n' "$o" | grep '^prompt:audit:record:r1:')
has    "C zero blockers with a high: the record command appends --disposition promote" "$p" "--blockers 0 --disposition promote"
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 3 0)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":0,"folded":3,"promotedIds":[],"edges":[],"placements":[],"summary":"d"}')")
p=$(printf '%s\n' "$o" | grep '^prompt:audit:record:r1:')
hasnt_ "C zero blockers, no high: the first command carries no disposition" "$p" "--blockers 0 --disposition promote"
has    "C ...but the retry instruction for a terminal refusal stays" "$p" "run the SAME command once more with --disposition promote"

# ---- D (id 2): the reconciliation SPLITS by severity, not only sums. `promoted 0, folded 5` over
# ---- confirmed 5 with two blockers and three highs reconciled, and two blockers went out as prose.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 2 5 3)" "$(rec BOUNDED)" '{"disposed":true,"standing":[],"promoted":0,"folded":5,"promotedIds":[],"summary":"x"}')")
has    "D promoted 0 beside 2 blockers + 3 highs: the roster is EMPTY" "$o" '"roster":[]'
has    "D ...and the note says the counts do not split" "$o" "do not split by severity — promoted 0 is below blockers 2 + highs 3"
has    "D ...and the disposal is NOT done" "$o" "disposal: NOT done"
# THREE since closing review round 2, cluster F: `refuted` joined `promoted` and `folded`.
n=$((n+1)); if [ "$(grep -c "type: 'integer', minimum: 0" "$F")" = 3 ]; then echo "ok   D promoted, folded and refuted carry minimum 0 in DISPOSAL_SCHEMA"; else echo "FAIL D DISPOSAL_SCHEMA does not pin minimum 0 on all three counts"; st=1; fi
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 1 1 0)" "$(rec BOUNDED)" '{"disposed":true,"standing":[],"promoted":1,"folded":0,"promotedIds":[],"summary":"x"}')")
has    "D a promotion naming no unit is REFUSED" "$o" 'promoted 1 beside promotedIds []'
has    "D ...with an empty roster" "$o" '"roster":[]'

# ---- P (TOOL-cMendedVintage-19): AN EDGE IS A PAIR, AND A REPAIR SITS BESIDE WHAT IT REPAIRS.
# The round-1 audit of `cMendedVintage` promoted seven findings into units, appended every one past
# the whole roster, and wrote consumes-from bullets whose reciprocals the hygiene join then named.
# Two orders and seven bullets were repaired by hand. Both halves are now the stage's own return and
# both refuse the hand-out, so the arms below stage each break and watch it red.
#
# `$UNITS` is A-tB-1 and A-tB-2 at order 1 and A-tB-3 at order 2, so a repair of A-tB-1 belongs at
# order 2 and the end of this roster is anything above 2. Those two numbers are what make the
# beside-it case and the past-the-end case distinguishable at all; picking a repair target at the
# END of the roster would have made them the same integer and graded nothing.
build_dispose() { # edges-json · placements-json
  printf '{"disposed":true,"standing":[],"promoted":1,"folded":0,"promotedIds":["A-tB-4"],"edges":%s,"placements":%s,"summary":"d"}' "$1" "$2"
}
PAIRED='[{"from":"A-tB-4","verb":"consumes-from","to":"A-tB-1"},{"from":"A-tB-1","verb":"hands-off","to":"A-tB-4"}]'
ONEWAY='[{"from":"A-tB-4","verb":"consumes-from","to":"A-tB-1"}]'
BESIDE='[{"unit":"A-tB-4","repairs":"A-tB-1","order":2}]'
run_dispose() { # dispose-json -> the trace and the RESULT
  run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 1 1)" "$(rec CONVERGED)" "$1")"
}

# THE PASSING CASE FIRST, so every refusal below is known to differ from it by one field.
o=$(run_dispose "$(build_dispose "$PAIRED" "$BESIDE")")
has "P paired edge + a repair at one above its target: the roster is handed out" "$o" '"roster":[{'
has "P ...and the log names the pairing and the placement" "$o" "edges 2 paired · placed A-tB-4 at order 2"

# ONE END ONLY. The mirror is dropped and nothing else changes.
o=$(run_dispose "$(build_dispose "$ONEWAY" "$BESIDE")")
has "P a one-way §3 edge: the roster is EMPTY" "$o" '"roster":[]'
has "P ...and the note NAMES the unpaired bullet" "$o" 'A-tB-4 **consumes-from** A-tB-1'
has "P ...and the disposal is NOT done" "$o" "disposal: NOT done"
# A MALFORMED BULLET JOINS THE SAME BUCKET, because an edge naming no verb is unpaired in the only
# sense this stage can see.
o=$(run_dispose "$(build_dispose '[{"from":"A-tB-4","verb":"depends-on","to":"A-tB-1"}]' "$BESIDE")")
has "P an edge carrying a verb outside the two: the roster is EMPTY" "$o" '"roster":[]'
# ASSERTED ON THE NOTE'S OWN PAYLOAD, never on the phrase alone: the prompt two screens up carries
# the words "written at one end only" verbatim, so an arm matching those bytes passes while the
# guard is disarmed — the gate-satisfied-by-its-own-prose class, in a test file.
has "P ...and it is reported as written at one end only" "$o" 'A-tB-4 **depends-on** A-tB-1'
# AN ABSENT LIST IS NOT A DECLARED EMPTY ONE.
o=$(run_dispose '{"disposed":true,"standing":[],"promoted":1,"folded":0,"promotedIds":["A-tB-4"],"placements":'"$BESIDE"',"summary":"d"}')
has "P no edges key at all: the roster is EMPTY" "$o" '"roster":[]'
has "P ...and the note says the list itself is missing" "$o" 'returned no `edges` list'

# THE PLACEMENT HALF. Same fixture, only the order moves.
o=$(run_dispose "$(build_dispose "$PAIRED" '[{"unit":"A-tB-4","repairs":"A-tB-1","order":3}]')")
has "P a repair appended PAST the roster end: the roster is EMPTY" "$o" '"roster":[]'
has "P ...and the note names the unit, its order and its target" "$o" 'A-tB-4 at order 3 repairing "A-tB-1"'
# SHARING the target's own order is not "after" it — units at one order are a parallel group.
o=$(run_dispose "$(build_dispose "$PAIRED" '[{"unit":"A-tB-4","repairs":"A-tB-1","order":1}]')")
has "P a repair sharing its target's order is REFUSED" "$o" 'not placed beside the unit it repairs'
# `none` IS THE ONLY ROUTE PAST THE END, and it has to actually be past it.
o=$(run_dispose "$(build_dispose "$PAIRED" '[{"unit":"A-tB-4","repairs":"none","order":3}]')")
has "P a promotion repairing none, above every unit: the roster is handed out" "$o" '"roster":[{'
o=$(run_dispose "$(build_dispose "$PAIRED" '[{"unit":"A-tB-4","repairs":"none","order":2}]')")
has "P ...but one repairing none INSIDE the roster is REFUSED" "$o" '"roster":[]'
# A TARGET THIS ROSTER DOES NOT CARRY is the `auditIds` stray, one stage later.
o=$(run_dispose "$(build_dispose "$PAIRED" '[{"unit":"A-tB-4","repairs":"A-tB-99","order":2}]')")
has "P a repairs naming no unit of this roster is REFUSED" "$o" 'A-tB-4 at order 2 repairing "A-tB-99"'
# AND THE TWO LISTS NAME THE SAME UNITS, in both directions.
o=$(run_dispose "$(build_dispose "$PAIRED" '[{"unit":"A-tB-5","repairs":"none","order":3}]')")
has "P promotedIds and placements naming different units: REFUSED" "$o" 'name different units (A-tB-4, A-tB-5)'

# THE INSTRUCTION, not just the guard. A stage told nothing about either rule would return a
# compliant-looking answer only by accident, and the guard alone would grade the accident.
p=$(printf '%s\n' "$o" | grep '^prompt:dispose:tB:')
has "P the disposal prompt carries the placement rule" "$p" "IMMEDIATELY AFTER THE UNIT IT REPAIRS"
has "P ...and names the append-past-the-end default for a promotion repairing nothing" "$p" "ABOVE EVERY unit in this build"
has "P the disposal prompt carries the both-ends rule" "$p" "EVERY §3 EDGE YOU WRITE GETS BOTH OF ITS ENDS"
has "P ...and asks for both lists back" "$p" "Return in \`placements\` one \`{unit, repairs, order}\` per promoted unit"

# ---- E (id 11): BOUNDED is a by-design exit, not a degradation.
o=$(run_wf "$UNITS" "$(returns BOUNDED 1)")
nt=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"note":"//')
hasnt_ "E the BOUNDED hand-out's note does not open DEGRADED" "$nt" "DEGRADED"
has    "E ...and still reads prologue complete" "$nt" "prologue complete"
o=$(run_wf "$UNITS" "$(returns CEILING 1)")
nt=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"note":"//')
has    "E the CEILING hand-out's note still opens DEGRADED" "$nt" "DEGRADED — 0 spec(s) refused, verdict CEILING"
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 1)")
nt=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"note":"//')
has    "E ...and so does NON-CONVERGENT" "$nt" "DEGRADED — 0 spec(s) refused, verdict NON-CONVERGENT"

# ---- F (ids 14, 15): the callee's two null-blocker RESULTS are read as clean rounds, its unverified
# ---- population is disposed, and the dead-lens shape keeps the throw.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":{"confirmed":[],"report":null,"blockers":null,"highs":null,"lensesRun":4,"lensesDead":0,"skepticsDead":0,"unverified":0,"note":"all findings adjudicated and refuted"},"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$(rec CONVERGED)" "$DISPOSE_OK")")
has    "F all-refuted: a RESULT, not a throw" "$o" "RESULT"
has    "F all-refuted: read as a clean round at 0" "$o" "a clean round at 0"
has    "F all-refuted: the round is recorded CLEAN at 0" "$o" '--verdict "CLEAN" --blockers 0'
has    "F all-refuted: the disposal skip is announced" "$o" "disposal: skipped"
has    "F all-refuted: unverified travels out as a stated 0" "$o" '"unverified":0'
# ROUND 2, CLUSTER D (ids 3, 15): the clean round used to hand out the roster — this arm asserted
# `"roster":[{` here — and the callee writes no `**Serves:** spec-audit` record on either clean path,
# so every unit built after it failed `specs-audited` at --close with nothing to point the override
# at. Unattended mode now WITHHOLDS the roster and names, in nextAction, the ids the record must
# carry, the path grammar at the SUBJECT's round, and the resume route; `dispatch` stays on the
# return so the caller can take it. Attended mode keeps the hand-out: an owner is in the loop.
has    "D all-refuted, unattended: the roster is WITHHELD" "$o" '"roster":[]'
has    "D ...and nextAction demands the record BEFORE any dispatch" "$o" "WRITE the spec-audit record this clean round left unwritten, BEFORE any unit is dispatched"
# ROUND 3, CLUSTER B (ids 1, 6): OWED is what the callee READ — the units whose spec path is among the
# subjects it was handed — never the roster. `s3` is no subject in UNITS, so A-tB-3 is NOT named on
# the demanded line and is called out as uncovered instead.
has    "D ...naming the ids the binding line must carry — the AUDITED set" "$o" '**Serves:** spec-audit A-tB-1 A-tB-2`'
hasnt_ "D ...and never a unit no subject covered" "$o" 'spec-audit A-tB-1 A-tB-2 A-tB-3'
has    "D ...and the uncovered unit is named as owing a later audit" "$o" 'NOT covered by this round and NOT to be named on that line: A-tB-3'
# ROUND 3, CLUSTER C (id 10): the record hygiene check 22 reads needs a `## Verdict:` heading, and the
# hand-out prescribes the callee's own opening order so the file it demands is one the bar accepts.
has    "D ...and the demanded record carries the Verdict heading check 22 reads" "$o" '## Verdict: CLEAN'
has    "D ...and the record path at the subject round" "$o" 'memory/builds/tB/reviews/<date>-review-A-tB-1-spec-audit-round1.md'
has    "D ...and the resume route" "$o" 'dispatch every unit `bash tools/unattended/unattended.sh --plan tB --paths` lists as READY'
has    "D ...and the note opens HELD" "$o" '"note":"HELD AT HAND-OUT — a clean round with no tracked spec-audit record'
has    "D ...and dispatch still travels, for the resume route" "$o" '"dispatch":{"scriptPath":"tools/workflows/unattended-unit.js"'
has    "D ...and the withholding is logged" "$o" "hand-out: WITHHELD"
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":{"confirmed":[],"report":null,"root":"/tmp/r","blockers":null,"highs":null,"lensesRun":4,"lensesDead":0,"note":"clean: 0 findings"},"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$(rec CONVERGED)" "$DISPOSE_OK")")
has    "F zero findings, no unverified key: a RESULT too" "$o" "RESULT"
has    "D zero findings, unattended: the roster is WITHHELD too" "$o" '"roster":[]'
has    "D ...and the callee's note is quoted into the demand" "$o" "the callee said: clean: 0 findings"
o=$(run_wf "$A_UNITS" '{"spec":{"authored":[],"alreadyPresent":["A-tB-1"],"refused":[],"summary":"s"},"workflow":{"confirmed":[],"report":null,"blockers":null,"highs":null,"lensesRun":4,"lensesDead":0,"skepticsDead":0,"unverified":0,"note":"all findings adjudicated and refuted"}}')
has    "D attended clean round: the roster is still handed out — an owner is in the loop" "$o" '"roster":[{'
hasnt_ "D ...and nothing is withheld" "$o" "hand-out: WITHHELD"
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":{"confirmed":[],"report":null,"blockers":null,"highs":null,"lensesRun":0,"lensesDead":4,"note":"UNVERIFIED: no lens completed"},"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$(rec CONVERGED)" "$DISPOSE_OK")")
has    "F every lens dead: still THROWS" "$o" "non-integer blocker count"
has    "F ...naming the lens deaths" "$o" "lensesDead 4"
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":{"confirmed":[],"report":null,"blockers":null,"highs":null,"lensesRun":3,"lensesDead":1,"skepticsDead":0,"unverified":0,"note":"all findings refuted, but 1/4 lenses died"},"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$(rec CONVERGED)" "$DISPOSE_OK")")
has    "F all-refuted beside a dead lens: THROWS" "$o" "non-integer blocker count"
# id 14: unverified findings are OUTSTANDING and run the stage.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 0 0 2)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":0,"folded":2,"promotedIds":[],"edges":[],"placements":[],"summary":"d"}')")
has    "F 0 confirmed + 2 unverified: the disposal agent RUNS" "$o" "agent:dispose:tB"
has    "F ...and the prompt hands it the unverified population" "$o" "and 2 unverified. Open the report"
has    "F ...and says an unverified finding is OUTSTANDING, not cleared" "$o" "OUTSTANDING, not cleared"
has    "F ...and the hand-out carries unverified 2" "$o" '"unverified":2'
has    "F ...and the roster is handed out" "$o" '"roster":[{'
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 1 1 1)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":1,"promotedIds":["A-tB-4"],"edges":[],"placements":[{"unit":"A-tB-4","repairs":"A-tB-3","order":3}],"summary":"d"}')")
has    "F confirmed 1 + unverified 1: reconciles against their sum" "$o" '"roster":[{'
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 1 1 1)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":0,"promotedIds":["A-tB-4"],"summary":"d"}')")
has    "F ...and one short of the sum is refused naming both populations" "$o" "is not confirmed 1 + unverified 1"
o=$(run_wf "$UNITS" '{"spec":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"},"workflow":{"blockers":0,"confirmed":0,"highs":0,"report":"r.md"},"audit:record":{"token":"CONVERGED"}}')
has    "F a synthesis return with no unverified key is REFUSED" "$o" "THROW"
has    "F ...and the message names unverified" "$o" "unverified undefined"
hasnt_ "F ...and the stage is never reached" "$o" "phase:Disposal"

# ==================== CLOSING REVIEW ROUND 2 — CLUSTERS B, C, E, F, G (spec 7 rev-5)
# Every arm below was observed RED against a frozen copy of the round-1 render, one arm at a time,
# with this suite's preamble sourced, before the harness moved. Cluster D's arms sit with the
# round-1 F arms above, because they flip the two clean-round hand-out arms in place.

# ---- B (ids 2, 7, 11, 17): the CONVERGED disposition is derived from what was PROMOTED, not
# ---- predicted from `auHighs`. `blockers 0, highs 0, unverified 2` and a disposal that promotes
# ---- one of the unverified findings used to record a bare CONVERGED row the merge bar reads as
# ---- demanding nothing. At zero blockers with something outstanding the DISPOSAL stage now runs
# ---- FIRST and the record carries `promote` iff `promotedIds` is non-empty.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 0 0 2)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":1,"promotedIds":["A-tB-9"],"edges":[],"placements":[{"unit":"A-tB-9","repairs":"A-tB-3","order":3}],"summary":"d"}')")
p=$(printf '%s\n' "$o" | grep '^prompt:audit:record:r1:')
has    "R2-B zero blockers, zero highs, a promoted UNVERIFIED finding: the record carries --disposition promote" "$p" "--blockers 0 --disposition promote"
ag=$(printf '%s\n' "$o" | grep '^agent:' | tr '\n' ' ')
has    "R2-B ...because the disposal ran BEFORE the record" "$ag" "agent:dispose:tB agent:audit:record:r1"
has    "R2-B ...and the log says the record follows the disposal" "$o" "the driver records this exit AFTER the disposal"
has    "R2-B ...and the hand-out still carries the promoted unit" "$o" '"promotedIds":["A-tB-9"]'
# The control: at a POSITIVE count the driver decides whether the loop even ended, so the record
# comes first and the disposal after it — the order every existing NON-CONVERGENT arm was written to.
o=$(run_wf "$UNITS" "$(returns NON-CONVERGENT 2)")
ag=$(printf '%s\n' "$o" | grep '^agent:' | tr '\n' ' ')
has    "R2-B control: at two blockers the record precedes the disposal" "$ag" "agent:audit:record:r1 agent:dispose:tB"
# The pairing guard runs BOTH ways: CONVERGED beside a positive count is a token no driver printed.
o=$(run_wf "$UNITS" "$(returns CONVERGED 3)")
has    "R2-B CONVERGED paired with 3 blockers THROWS" "$o" "returned CONVERGED paired with 3 blockers"
hasnt_ "R2-B ...and DISPOSAL is not reached" "$o" "phase:Disposal"
# A disposal that does not finish at zero blockers has nothing to record yet, and says so rather than
# writing a bare CONVERGED row over findings nobody disposed.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 3 0)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":1,"folded":1,"summary":"x"}')")
hasnt_ "R2-B a DEGRADED disposal at zero blockers records NO round" "$o" "agent:audit:record"
has    "R2-B ...and the note says so, with the hand-record command" "$o" 'The round was NOT recorded: at zero blockers the driver'
# The needle carries the RESULT line's JSON-escaped quotes, one backslash each.
has    "R2-B ...naming the subject the caller records under" "$o" '--review tB --subject tB-spec-set-r1 --verdict \"CLEAN\" --blockers 0`'

# ---- C (ids 8, 12, 13): `auditIds` beside a caller-supplied `subjects` is REFUSED by name. The
# ---- supplied set skipped the resolver, which is the only place the scoping applies, while the
# ---- log claimed the scoping happened; the promoted unit was rostered with its spec never audited.
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":2,"auditIds":["A-tB-3"],#')" "$(returns CONVERGED 0)")
has    "R2-C auditIds beside subjects: THROWS" "$o" "THROW"
has    "R2-C ...naming the pair" "$o" 'pass `auditIds` OR `subjects`, never both'
has    "R2-C ...and why a runtime with no filesystem cannot intersect them" "$o" "cannot be scoped to the promoted units by a runtime that cannot read their specs"
hasnt_ "R2-C ...and the scoping is NOT logged as applied" "$o" "scoped to 1 promoted unit(s)"
hasnt_ "R2-C ...and no agent was spawned before the refusal" "$o" "agent:"
o=$(run_wf "$UNITS" "$(returns BOUNDED 1)")
has    "R2-C the post-disposal nextAction names subjects among what NOT to pass" "$o" 'and no subjectRound and no `subjects`, so they take a fresh subject'

# ---- E (id 14): the callee is handed the SUBJECT's round, not the invocation's. Under the kit
# ---- default every promoted-spec audit lands at invocation round 2, and `tier2-review.js` primed
# ---- it as a FOLD review of a spec nobody had reviewed.
o=$(run_wf "$NOSUBJ" "$(printf '{"spec:":%s,"audit:subjects":{"subjects":[{"path":"s3","blob":"%s","tree":"%s"}]},"workflow":%s,"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$B40" "$B40" "$(review_out 0)" "$(rec CONVERGED)" "$DISPOSE_OK")")
w=$(printf '%s\n' "$o" | grep '^wargs:')
has    "R2-E a post-disposal re-invoke at round 2 hands the callee round 1" "$w" '"round":1'
has    "R2-E ...as a spec-audit" "$w" '"kind":"spec-audit"'
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":3,"subjectRound":2,#')" "$(returns CONVERGING 3)")
w=$(printf '%s\n' "$o" | grep '^wargs:')
has    "R2-E a fold re-invoke at round 3 on a subject first audited at 2 hands the callee round 2" "$w" '"round":2'
has    "R2-E ...while the harness keeps its own round for the record" "$o" "prompt:audit:record:r3:"

# ---- TOOL-aWokenSentinel-15: the resolver pins at a blob and the lenses read the tree, so the
# ---- stage compares the two hashes the resolver returned and refuses to dispatch over a dirty
# ---- subject. INSIDE the resolver branch only: the supplied-subject fixtures above carry no
# ---- `tree` and never enter it. Each arm read RED first against the render at 12513c25, where
# ---- the first and third proceed to the sub-workflow and the second finds no `tree` to strip.
o=$(run_wf "$NOSUBJ" "$(printf '{"spec:":%s,"audit:subjects":{"subjects":[{"path":"s3","blob":"%s","tree":"%s"}]},"workflow":%s,"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$B40" "$T40" "$(review_out 0)" "$(rec CONVERGED)" "$DISPOSE_OK")")
has    "WS15 a resolved subject whose tree differs from its blob THROWS" "$o" "THROW"
has    "WS15 ...naming the path and both hashes" "$o" "s3 HEAD $B40 tree $T40"
has    "WS15 ...and the remedy" "$o" "Commit the fold"
same   "WS15 ...and no lens was dispatched" "$(printf '%s\n' "$o" | grep -c '^workflow:')" "0"
o=$(run_wf "$NOSUBJ" "$(printf '{"spec:":%s,"audit:subjects":{"subjects":[{"path":"s3","blob":"%s","tree":"%s"}]},"workflow":%s,"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$B40" "$B40" "$(review_out 0)" "$(rec CONVERGED)" "$DISPOSE_OK")")
same   "WS15 an agreeing pair reaches the sub-workflow" "$(printf '%s\n' "$o" | grep -c '^workflow:')" "1"
w=$(printf '%s\n' "$o" | grep '^wargs:')
has    "WS15 ...handed {path, blob}" "$w" "\"subjects\":[{\"path\":\"s3\",\"blob\":\"$B40\"}]"
same   "WS15 ...with tree stripped" "$(printf '%s' "$w" | grep -c '"tree"')" "0"
o=$(run_wf "$NOSUBJ" "$(printf '{"spec:":%s,"audit:subjects":{"subjects":[{"path":"s3","blob":"%s"}]},"workflow":%s,"audit:record":%s,"dispose:":%s}' "$SPEC_OK" "$B40" "$(review_out 0)" "$(rec CONVERGED)" "$DISPOSE_OK")")
has    "WS15 a resolved subject with no tree THROWS naming the field" "$o" "40-hex tree"
hasnt_ "WS15 ...and not as a dirty tree" "$o" "Commit the fold"

# ---- F (id 16): an UNVERIFIED finding the stage judges not a defect has a route. `refuted` is
# ---- optional, bounded by `unverified`, in the sum, and the severity floors stand.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 2 0 1)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":0,"folded":2,"refuted":1,"promotedIds":[],"edges":[],"placements":[],"summary":"r1 refuted: not reachable"}')")
has    "R2-F promoted 0 + folded 2 + refuted 1 over confirmed 2 + unverified 1: the roster is handed out" "$o" '"roster":[{'
has    "R2-F ...and refuted travels out" "$o" '"folded":2,"refuted":1'
has    "R2-F ...and the log counts it" "$o" "promoted 0 · folded 2 · refuted 1"
p=$(printf '%s\n' "$o" | grep '^prompt:dispose:tB:')
has    "R2-F the prompt permits refuting an UNVERIFIED finding" "$p" "You may REFUTE an UNVERIFIED finding — never a CONFIRMED one"
has    "R2-F ...with a one-line reason in summary" "$p" "with a one-line reason per refuted finding in \`summary\`, and count it in \`refuted\`"
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"audit:record":%s,"dispose:":%s}' \
    "$SPEC_OK" "$(review_out 0 2 0 1)" "$(rec CONVERGED)" '{"disposed":true,"standing":[],"promoted":0,"folded":1,"refuted":2,"promotedIds":[],"summary":"x"}')")
has    "R2-F refuted 2 above unverified 1 is REFUSED by name" "$o" "refuted 2 is above the 1 unverified"
has    "R2-F ...with an empty roster" "$o" '"roster":[]'
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
has    "R2-F the skip path carries refuted 0 out loud" "$o" '"folded":0,"refuted":0'

# ---- G (id 9): a present-but-wrong-typed `round`, `subjectRound` or `auditIds` REFUSES by name
# ---- with the received JSON, like `mode`, `scratch` and `units`, instead of folding to a default.
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":2,"subjectRound":"2",#')" "$(returns CONVERGED 0)")
has    "R2-G a string subjectRound is REFUSED" "$o" "THROW"
has    "R2-G ...naming the field and the received JSON" "$o" '`subjectRound` must be a positive integer when present, got "2"'
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"subjects":\[[^]]*\],##' | sed 's#"slug":"tB",#"slug":"tB","round":2,"auditIds":"A-tB-3",#')" "$(returns CONVERGED 0)")
has    "R2-G a string auditIds is REFUSED" "$o" '`auditIds` must be an array of unit ids when present, got "A-tB-3"'
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":"2",#')" "$(returns CONVERGED 0)")
has    "R2-G a string round is REFUSED too — the same class, one guard" "$o" '`round` must be a positive integer when present, got "2"'
hasnt_ "R2-G ...before any agent is spawned" "$o" "agent:"

# ==================================== TOOL-aBlindedTrial-3 — THE SPEC AUDIT IS OPT-IN
# The AUDIT stage runs only when `specAudit` is declared. Absent, the stage announces itself OFF by
# declaration, awaits no sub-workflow, spawns no resolver and no disposal agent, and hands the roster
# out on SPEC completion with a verdict that says NOT-OWED — never a zero it did not count and never a
# clean bill. `UNITS` carries the key, so every arm above stays on the ON branch; the OFF fixture is
# `UNITS` minus the key AND minus `subjects`, because a caller-pinned subject set beside no audit is
# the re-invoke pairing AC5 refuses. Every OFF arm was observed RED against the pre-edit render.
OFF_UNITS=$(printf '%s' "$UNITS" | sed 's#"specAudit":"2026-09-20",##; s#"subjects":\[[^]]*\],##')
# ---- AC2: no `workflow` double at all, so a harness that still awaits the sub-workflow gets `{}`
# ---- back and throws; the OFF harness never asks. A RESOLVER double IS supplied, on purpose: without
# ---- one the pre-edit harness threw at the resolver before it could await the sub-workflow, and the
# ---- `workflow:` absence arm passed over a harness that had not been reached — the vacuous pass,
# ---- observed here. With subjects on offer, the pre-edit harness awaits and the arm reds.
o=$(run_wf "$OFF_UNITS" "$(printf '{"spec:":%s,"audit:subjects":{"subjects":[{"path":"s1","blob":"abc1234"}]}}' "$SPEC_OK")")
has    "BT3-AC2 OFF: the audit stage announces itself OFF by declaration" "$o" "log:audit stage: OFF by declaration"
hasnt_ "BT3-AC2 OFF: the sub-workflow is never awaited" "$o" "workflow:"
hasnt_ "BT3-AC2 OFF: ...and its args are never composed" "$o" "wargs:"
hasnt_ "BT3-AC2 OFF: no subject resolver is spawned" "$o" "agent:audit:"
# ---- AC3: the roster follows SPEC completion; DISPOSAL still runs, over nothing, and says why.
has    "BT3-AC3 OFF: the run completes with a RESULT" "$o" "RESULT"
has    "BT3-AC3 OFF: the roster is handed out" "$o" '"roster":[{'
hasnt_ "BT3-AC3 OFF: the roster is not withheld for a spec-audit record" "$o" "HELD AT HAND-OUT"
has    "BT3-AC3 OFF: the DISPOSAL phase still runs" "$o" "phase:Disposal"
seq=$(printf '%s\n' "$o" | grep '^phase:' | tr '\n' ' ')
same   "BT3-AC3 OFF: the stage order is unchanged" "$seq" "phase:Spec phase:Audit phase:Disposal "
has    "BT3-AC3 OFF: the disposal skip names the real reason" "$o" "disposal: skipped — the spec audit is OFF by declaration"
hasnt_ "BT3-AC3 OFF: no disposal agent is spawned" "$o" "agent:dispose:"
# ---- AC4: the return says the audit was NOT OWED, with stated nulls, and the note reads neither
# ---- DEGRADED nor clean.
has    "BT3-AC4 OFF: the verdict is NOT-OWED" "$o" '"verdict":"NOT-OWED"'
has    "BT3-AC4 OFF: the audit object says it did not run" "$o" '"audit":{"ran":false,"verdict":"NOT-OWED","blockers":null,"highs":null,"unverified":null}'
has    "BT3-AC4 OFF: blockers travel out as a stated null" "$o" '"blockers":null'
hasnt_ "BT3-AC4 OFF: never a blocker count of zero on a path that reviewed nothing" "$o" '"blockers":0'
hasnt_ "BT3-AC4 OFF: never a clean round at 0 either" "$o" "a clean round at 0"
nt=$(printf '%s\n' "$o" | grep '^RESULT ' | sed 's/.*"note":"//')
hasnt_ "BT3-AC4 OFF: the note does not read DEGRADED" "$nt" "DEGRADED"
has    "BT3-AC4 OFF: ...and does not read clean — it says the audit was off" "$nt" "spec audit OFF by declaration"
has    "BT3-AC4 OFF: ...and still hands out the prologue" "$nt" "prologue complete"
# ---- AC1: a present-but-wrong-typed `specAudit` refuses by name, with the date shape, before any
# ---- agent runs. A truthy non-string must never switch the audit on.
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"specAudit":"2026-09-20"#"specAudit":1#')" "$(returns CONVERGED 0)")
has    "BT3-AC1 specAudit 1: THROWS" "$o" "THROW"
has    "BT3-AC1 ...naming the key and the date shape" "$o" '`specAudit` must be a YYYY-MM-DD date string when present, got 1'
hasnt_ "BT3-AC1 ...before any agent is spawned" "$o" "agent:"
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"specAudit":"2026-09-20"#"specAudit":true#')" "$(returns CONVERGED 0)")
has    "BT3-AC1 specAudit true: THROWS rather than switching the audit on" "$o" "THROW"
hasnt_ "BT3-AC1 ...and the sub-workflow never ran" "$o" "wargs:"
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"specAudit":"2026-09-20"#"specAudit":"2026-9-1"#')" "$(returns CONVERGED 0)")
has    "BT3-AC1 a malformed date string is refused by the same row" "$o" 'got "2026-9-1"'
# ---- AC5: an audit-shaped argument beside no `specAudit` is a re-invoke of an audit that never
# ---- ran, refused by name like every other impossible pairing in the file.
o=$(run_wf "$(printf '%s' "$UNITS" | sed 's#"specAudit":"2026-09-20",##')" "$(returns CONVERGED 0)")
has    "BT3-AC5 subjects beside no specAudit: THROWS" "$o" "THROW"
has    "BT3-AC5 ...naming the pairing" "$o" '`subjects` is present beside no `specAudit`'
hasnt_ "BT3-AC5 ...before any agent is spawned" "$o" "agent:"
o=$(run_wf "$(printf '%s' "$OFF_UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":2,"auditIds":["A-tB-3"],#')" "$(returns CONVERGED 0)")
has    "BT3-AC5 auditIds beside no specAudit: THROWS by the same guard" "$o" '`auditIds` and `round` is present beside no `specAudit`'
o=$(run_wf "$(printf '%s' "$OFF_UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":2,"subjectRound":2,#')" "$(returns CONVERGED 0)")
has    "BT3-AC5 subjectRound beside no specAudit: THROWS by the same guard" "$o" '`subjectRound` and `round` is present beside no `specAudit`'
# ---- ...and `round > 1` ALONE (closing review of units 2–5, F6): the fourth audit-shaped argument.
# ---- Only an audit re-invoke is ever told to pass it, so beside no declaration it names a round that
# ---- never ran; before this arm the OFF path handed the roster out under `"round":2` without a word.
o=$(run_wf "$(printf '%s' "$OFF_UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":2,#')" "$(returns CONVERGED 0)")
has    "BT3-AC5 round 2 beside no specAudit: THROWS by the same guard" "$o" "THROW"
has    "BT3-AC5 ...naming round" "$o" '`round` is present beside no `specAudit`'
hasnt_ "BT3-AC5 ...before any agent is spawned" "$o" "agent:"
o=$(run_wf "$(printf '%s' "$OFF_UNITS" | sed 's#"slug":"tB",#"slug":"tB","round":1,#')" "$(returns CONVERGED 0)")
hasnt_ "BT3-AC5 round 1 beside no specAudit is the first round and is NOT refused" "$o" "THROW"
# ---- AC6: the DECLARED build keeps its audit exactly as before — the control for every arm above.
o=$(run_wf "$UNITS" "$(returns CONVERGED 0)")
has    "BT3-AC6 declared: the sub-workflow is awaited" "$o" "workflow:"
has    "BT3-AC6 declared: ...as a spec-audit" "$o" '"kind":"spec-audit"'
has    "BT3-AC6 declared: the audit object says it ran, with the counts it read" "$o" '"audit":{"ran":true,"verdict":"CONVERGED","blockers":0,"highs":0,"unverified":0}'
hasnt_ "BT3-AC6 declared: nothing announces the audit off" "$o" "OFF by declaration"
# The attended every-unit-terminal exit is the one other return the OFF path can reach, and it says so.
o=$(run_wf "$(printf '%s' "$T_UNITS" | sed 's#"specAudit":"2026-09-20",##; s#"subjects":\[[^]]*\],##')" '{"spec":{"authored":[],"alreadyPresent":[],"refused":[],"summary":"s"}}')
has    "BT3 attended, OFF, every unit terminal: the exit carries the audit object" "$o" '"audit":{"ran":false,"verdict":"NOT-OWED"'
has    "BT3 ...with an empty roster, by filtering" "$o" '"roster":[]'
# ---- AC7: both carriers read 1.2 — the render is byte-compared to the template by the parity leg,
# ---- so the marker moving in one file and not the other reds there; this arm reads the render.
has    "BT3-AC7 the render carries the engine version 1.2" "$(sed -n '3p' "$F")" "version: '1.2', // gov:kit unattended-build@1.2"

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
# ---- `kit.toml` declares on every update unless GOVKIT_RERENDER=0, captures its output and prints one
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

# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Authored from a
# static count of the `same`/`has`/`hasnt_` sites in this file — `grep -cE '^\s*(same|has|hasnt_) '`
# over it, 326 at 1d8530e7 (TOOL-aWokenSentinel-21) — at ~10 % headroom, rounded down, because the
# pass that wrote this line may not run the suite; the first green under GATE_SELFTESTS=1 or
# run-selftests.sh --kit tools/workflows confirms the executed count against it. The inline
# `n=$((n+1))` sites — the PV-AC12 branch's among them, the one region that can SKIP — are not in
# the static count, so it is a LOWER bound on what a green run executes. Lower it in a reviewed
# diff or not at all.
FLOOR_ASSERTIONS=293
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
# NOTHING RUNS AFTER THE TERMINAL EXIT (TOOL-dUnstalledConvoy-19): the floor cannot see an arm
# appended past `exit $st`, and neither can check-arms.py or the summary line. One grep can. The
# range starts at the exit line itself, so a suite with nothing after it reads exactly 1; a comment
# or a blank line after it is not counted.
[ "$(sed -n '/^exit \$st$/,$p' "$0" | grep -cvE '^\s*(#|$)')" = 1 ] || { echo "FAIL a line follows the terminal exit and can never run"; st=1; }

echo "--- $n arms, exit $st"
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit $st
