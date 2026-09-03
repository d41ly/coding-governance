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
      for (const k of Object.keys(returns)) if (label.indexOf(k) === 0) return returns[k]
      return null
    }
    const phase = (t) => trace.push("phase:" + t)
    const log = (m) => trace.push("log:" + m)
    const parallel = async () => { trace.push("parallel"); return [] }
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
audit() { printf '{"verdict":"%s","blockers":%s,"reportPath":"r.md","summary":"s"}' "$1" "$2"; }
returns() { printf '{"spec:":%s,"workflow":%s,"build:":%s}' "$SPEC_OK" "$1" "$BUILD_OK"; }

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
o=$(run_wf "$UNITS" "$(returns "$(audit CONVERGED 0)")")
has "args: a VALID object is accepted — the passing case" "$o" "RESULT"

# ---- AC3: THE STAGE ORDER, asserted on the emitted sequence. A reordering reds this.
o=$(run_wf "$UNITS" "$(returns "$(audit CONVERGED 0)")")
seq=$(printf '%s\n' "$o" | grep '^phase:' | tr '\n' ' ')
same "stage order is Spec then Audit then Build" "$seq" "phase:Spec phase:Audit phase:Build "

# ---- AC7: THE GATE ON THE VERDICT, over all four driver states. A gate tested only on the state
# ---- that OPENS it is a gate nothing proved closes.
o=$(run_wf "$UNITS" "$(returns "$(audit CONVERGING 3)")")
has "CONVERGING: BUILD is not reached" "$o" "HELD AT AUDIT"
n=$((n+1)); case "$o" in *"phase:Build"*) echo "FAIL CONVERGING reached the Build phase, which is the one thing this gate exists to stop"; st=1 ;; *) echo "ok   CONVERGING: the Build phase never ran" ;; esac
has "CONVERGING: the caller is told what to do next" "$o" "re-invoke this harness with round"
for v in CONVERGED NON-CONVERGENT CEILING; do
  o=$(run_wf "$UNITS" "$(returns "$(audit "$v" 0)")")
  n=$((n+1)); case "$o" in *"phase:Build"*) echo "ok   $v: admits BUILD" ;; *) echo "FAIL $v did not admit BUILD, so a terminal verdict cannot land a build"; st=1 ;; esac
done

# ---- TOOL-dRatifiedSeam-1. THE STAGE THAT COULD NEVER COMPLETE ------------------------------
# The AUDIT stage used to order a SIDECHAIN agent to invoke the Workflow tool, which a sidechain
# does not hold. The stage could not complete, BUILD was unreachable, and the harness named a
# route that did not run. These arms grade the fixed shape: the spawn happens in the SCRIPT.

# S1 — the sub-workflow is invoked BY THIS SCRIPT, and the trace names which one. Without this,
# every arm below could pass over a harness that reached BUILD by some other path entirely.
o=$(run_wf "$UNITS" "$(returns "$(audit CONVERGED 0)")")
has "S1 the AUDIT stage invokes tier2-review as a SUB-WORKFLOW from the script" "$o" \
    "workflow:tools/workflows/tier2-review.js"

# S3 — CONVERGING paired with 0 blockers is REFUSED BY NAME. A loop with nothing left to
# converge on has converged, so the pairing is this repo's signature for a record no verb
# produced — and it is exactly what the dead stage returned.
o=$(run_wf "$UNITS" "$(returns "$(audit CONVERGING 0)")")
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
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":{"verdict":"CONVERGED","blockers":null},"build:":%s}' \
    "$SPEC_OK" "$BUILD_OK")")
has "S2 a null blocker count THROWS rather than rounding to zero" "$o" "non-integer blocker count"
n=$((n+1)); case "$o" in
  *"phase:Build"*) echo "FAIL S2 a degraded audit reached BUILD"; st=1 ;;
  *) echo "ok   S2 ...and a degraded audit does not reach BUILD" ;;
esac

# THE SUBJECT GUARD. An unpinned subject audits whatever the file happens to say when the lens
# reads it, which is not a review of anything in particular — and tier2-review would refuse it
# downstream with a message about its own arguments rather than about which stage failed.
o=$(run_wf "${UNITS/\"blob\":\"abc1234\"/\"blob\":\"nothex\"}" "$(returns "$(audit CONVERGED 0)")")
has "an unpinned subject blob is REFUSED before the sub-workflow runs" "$o" "7-40 hex blob"

# ---- AC9: A DEAD AUDIT STAGE IS A REFUSAL, never a silent pass to BUILD. This is the absence that
# ---- would otherwise let the harness build on an unreviewed spec set.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"build:":%s}' "$SPEC_OK" "$BUILD_OK")")
has "a dead AUDIT stage THROWS" "$o" "THROW"
has "the throw says an absent verdict is not a convergence" "$o" "must never read as CONVERGED"
o=$(run_wf "$UNITS" "$(printf '{"workflow":%s,"build:":%s}' "$(audit CONVERGED 0)" "$BUILD_OK")")
has "a dead SPEC stage THROWS rather than auditing nothing" "$o" "SPEC stage returned nothing"

# ---- AC6: A DEGRADED RUN SAYS SO. `degradation-known-but-unreported` is the class where a pipeline
# ---- computes how badly it degraded and does not report it.
o=$(run_wf "$UNITS" "$(printf '{"spec:":%s,"workflow":%s,"build:":%s}' \
    '{"authored":[],"alreadyPresent":["A-tB-1"],"refused":["A-tB-2","A-tB-3"],"summary":"s"}' \
    "$(audit CONVERGED 0)" \
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
n=$((n+1)); grep -qE '\bparallel\s*\(|\bpipeline\s*\(' "$F" \
  && { echo "FAIL the harness calls a fan-out primitive, which the ratified parallelism verdict forbids"; st=1; } \
  || echo "ok   no parallel()/pipeline() call anywhere in the harness"
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

echo "--- $n arms, exit $st"
exit $st
