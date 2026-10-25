#!/usr/bin/env bash
# Runnable check for the portable agent-cap.js guard on the Workflow and Agent tool calls, the rules it
# keeps since TOOL-dGroundRules-10: rule 2, a verify stage that spawns one agent per item; rule 5,
# the ref-keyed verdict join; rule 0, the spec-audit opt-in; rule 6, the rendered handoff; and rule 7,
# the settings in force against the landed agent limit. The retired rules' arms went with them.
# Run from the kit directory: bash ./agent-cap.test.sh   (exit 0 = all pass)
set -u
# A suite run from inside a session inherits the session's directory, which would arm rule 6 over a
# fixture whose cwd lies in no checkout (TOOL-aOrientedCast-14 S7); an arm that needs one names it.
unset CLAUDE_PROJECT_DIR
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "agent-cap.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
# ROOTPFX is a ROOT install's prefix, empty by definition: a fixture that models a root install,
# or a key relative to the tool root, is spelled through it rather than bare (TOOL-aRepatriatedFork-28 S2).
ROOTPFX=""
KIT_HOOK="$HERE/agent-cap.js"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
# THE ARMS RUN A COPY (TOOL-dGroundRules-21 S38): rule 7 refuses a payload cwd that lies in no checkout
# wherever a policy kit sits beside the hook, and every arm below runs from "$TMP", which no checkout
# holds. The copy sits beside scratch-guard.js and no policy kit, where rule 7 adds no rule, so each arm
# judges the rule it names; the sections that arm rule 7 build their own copies beside a policy kit.
ARMS_HOOKS="$TMP/arms-hooks/hooks"; mkdir -p "$ARMS_HOOKS"; cp "$KIT_HOOK" "$HERE/scratch-guard.js" "$ARMS_HOOKS/"
HOOK="$ARMS_HOOKS/agent-cap.js"
pass=0; fail=0
# The one resolver, not the retired `command -v python3 || python` idiom this repo banned — which the
# ban could not see here, because it matches only `command -v`.
# TOOL-aRepatriatedFork-46: the resolver is carried INLINE. It was sourced from a probe of the
# library directory beside this kit, which ships nowhere, with a bare launcher as the fallback.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
TESTPY=$(resolve_python) || { echo "agent-cap.test: no usable python"; exit 2; }
check() { # name expected_exit json
  # FROM "$TMP", not from wherever the suite was launched: a payload with no `cwd` judges the
  # caller's checkout, whose roles index arms rule 6 and whose settings rule 7 reads. The scratch dir
  # has no checkout, so neither rule arms.
  printf '%s' "$3" | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; local got=$?
  if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
# js <name> <expected_exit> — the script body arrives on stdin, so a fixture can be written as real
# multi-line JavaScript instead of a \n-spliced one-liner. Every rule-2 fixture below is a SHAPE, and
# a shape squeezed onto one line stops being the shape that was written last time.
js() { # name expected_exit  (script on stdin)
  local name=$1 want=$2
  local payload
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  # An EMPTY payload makes every ALLOW arm pass for the wrong reason — the hook exits 0 on
  # unparseable input by design. A fixture that produced nothing is a failure, not a silent green.
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  check "$name" "$want" "$payload"
}

# ---- the first arms ------------------------------------------------------------------------------
# Rule 1, the ban on raw `parallel`/`pipeline`, retired in TOOL-dGroundRules-10 with its corpus:
# the harness's own concurrency settings bound how many run at once. This first arm still DENIES, by
# rule 2, because the raw primitive fans an agent over an unbounded receiver.
check "a raw parallel fanning an agent over an unbounded map → deny (rule 2)" 2 '{"tool_name":"Workflow","tool_input":{"script":"const r = await parallel(D.map(d => () => agent(d.p)))"}}'
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi
check "non-Workflow tool → allow" 0 '{"tool_name":"Bash","tool_input":{"command":"parallel(x.map(y))"}}'
# The helper line itself is sanctioned, and its fan-out receiver is now BOUNDED — the old fixture
# fanned `D.map(d=>()=>agent(d.p))`, which rule 2 correctly denies. A fixture that the gate must
# reject cannot double as the fixture proving it accepts.
check "boundedParallel + marker → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"async function boundedParallel(t,cap=5){const o=[];for(let i=0;i<t.length;i+=cap)o.push(...await parallel(t.slice(i,i+cap))); // gov:bounded-fanout\nreturn o}\nconst LENSES = [1,2,3]\nconst r = await boundedParallel(LENSES.map(d=>()=>agent(d)),5)"}}'

# ---- the LOOP KEYWORD SET (TOOL-aWeldedTribunal-1) ----------------------------------------------
# Every loop-recognition path must see the SAME keyword set. Six sites in agent-cap.js used to hold
# their own `for|while` regex, and two ordinary spellings matched none of them: `for await (` puts an
# identifier between the keyword and the paren, and a `do { … } while (…)` block's opening line
# carries no keyword at all. Both were MEASURED at exit 0 against the shipped hook before this unit.
#
# ARMS PER WALK, NOT PER KEYWORD. The same fan expressed as `for await (` must deny whether it is
# reached through the BRACE walk or the OPENER walk — those are different predicates and the opener
# walk needs the end-of-text form, so a single arm would certify coverage it does not have.
check "for-await thunk array (brace walk) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const th = []\nfor await (const f of allFindings) { th.push(() => agent(f.claim)) }\nawait Promise.all(th.map(t=>t()))"}}'
check "do-while thunk array (brace walk) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const th = []\nlet i = 0\ndo { th.push(() => agent(allFindings[i].claim)); i++ } while (i < allFindings.length)\nawait Promise.all(th.map(t=>t()))"}}'
check "for-await inline agent (opener walk) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"for await (const f of allFindings) await agent(f.claim)"}}'
check "do-block inline agent → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"let i = 0\ndo { await agent(allFindings[i].claim); i++ } while (i < allFindings.length)"}}'
# THE NEGATIVE DIRECTION. A widened predicate that denies innocent files is the failure this pair
# exists to catch; measured over all eight tracked *.js, ZERO lines match the widened form and not
# the old one, so nothing legal may change verdict.
check "bounded fan, no loop → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const LENSES = [1,2,3]\nawait boundedParallel(LENSES.map(L=>()=>agent(L)), 5)"}}'
check "the words for-await inside a string → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const note = \"we never write for await (x of y) here\"\nawait boundedParallel(T, 5)"}}'

# ---- a GROWN receiver loses its bound (TOOL-aWeldedTribunal-2) ----------------------------------
# `const batches = []` counts zero elements and is blessed by the array-literal case; a later
# `batches.push(...)` grows it to one entry per finding with the bound still standing. The arms
# assert on the refusal TEXT, not just the exit code: an arm checking non-zero alone cannot tell
# this rule's denial from the loop ban's, and a criterion that could not was this unit's own blocker.
#
# THE ADJACENCY IS THE POINT. The hook judges only lines containing `agent(`, and `push` is not an
# ITER_CALL — so the agent call must sit lexically INSIDE the map receiver's parens for the iter arm
# to be reached at all. `push` on one line and a detached `.map` on another is LEGAL and stays 0.
check "grown-by-push receiver → deny, naming the mutation" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.push(f)\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
check "grown-by-unshift receiver → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.unshift(f)\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
check "grown-by-splice receiver → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.splice(0, 0, f)\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
# THE NEGATIVES. An empty literal nobody grows is legal, and so is a growth whose fan is not
# adjacent — a non-mutating `.concat`/`.flat`/`.flatMap` must NOT take a bound back, which is what
# the pre-wiring run over this tree refuted the first vocabulary for.
check "empty literal never grown → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
check "grown but the fan is not adjacent → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const batches = []\nbatches.push(f)\nconst out = batches.map((b) => b())\nawait agent(\"one call\")"}}'
check "concat does not grow the receiver → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nconst more = LENSES.concat(extra)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# ---- the closing diff review's fold. Every arm below FAILED before its fix, and each was
# ---- reproduced by running the shipped hook rather than argued.
# THE ACCEPTED RESIDUAL, and the arm states it as such rather than hiding it. A BLOCK comment
# mentioning a growth REVOKES the bound and denies the script. Four review rounds went into trying
# to strip comments out of the take-back view and each attempt bought a FAIL-OPEN instead, because
# this file models no regex literal and every strip inherits that blindness in a new shape. The
# strip is gone; the false deny is accepted, which is the fail-closed direction and the behaviour
# that shipped before this build. Cost: one reworded comment. The alternative cost an agent burst.
check "a block comment naming a push DENIES (accepted residual, fail-closed)" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n/* never do LENSES.push(x) here */\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# A LINE comment is different and still allows: the lexed view breaks on `//` itself, so no strip
# of ours is involved. Kept as an arm because the two comment forms now diverge, and a reader who
# assumes they behave alike would be wrong.
check "a line comment naming a push does not take the bound back → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n// never do LENSES.push(x)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# A MEMBER CHAIN IS NOT THE TOP-LEVEL NAME. Without a left guard the regex captured the LAST segment,
# so `state.lenses.push(x)` denied a script naming a variable nothing had touched.
check "a member-chain push does not revoke an unrelated name → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst lenses = [1,2,3]\nstate.lenses.push(x)\nawait boundedParallel(lenses.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# A REMOVAL-ONLY SPLICE SHRINKS. Denying it states "was GROWN" about an array that got smaller.
check "removal-only splice does not take the bound back → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3,4,5]\nLENSES.splice(0, 2)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
check "a 3-argument splice INSERTS, so it still takes the bound back → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nLENSES.splice(0, 0, extra)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# THE TAKE-BACK CASCADES. A derivation is bounded only because its SOURCE was; when the source loses
# its bound the derived name must lose it too, or an unbounded fan is admitted one `.filter()` away.
# Two arms, one per sweep — the reassignment sweep had this hole before this build and now does not.
check "push-then-derive: the derived name loses its bound too → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.push(f)\nconst groups = batches.filter(Boolean) // gov:fixed-verifiers\nawait boundedParallel(groups.map((g) => () => agent(g)), MAX_VERIFIERS)"}}'
check "reassign-then-derive: the derived name loses its bound too → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nlet items = [1, 2]\nitems = allFindings\nconst groups = items.filter(Boolean) // gov:fixed-verifiers\nawait boundedParallel(groups.map((g) => () => agent(g)), MAX_VERIFIERS)"}}'
check "derive from a source that KEEPS its bound → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nconst groups = LENSES.filter(Boolean) // gov:fixed-verifiers\nawait boundedParallel(groups.map((g) => () => agent(g)), MAX_VERIFIERS)"}}'

# ---- THE FROZEN DENY CORPUS (TOOL-aWeldedTribunal-2, round 2 of the closing review) -------------
# WHY THIS EXISTS, and it is the most useful thing in this file. The fold that fixed round 1's
# false-DENY findings traded them for four fail-OPEN bound escapes, and this suite was 196 passed,
# 0 failed while it happened — because every arm above pins the exact script a review reported and
# none pins the CLASS. A green leg over a broken control is the shape the charter names, and it
# happened here, in the file that enforces the fan-out cap.
#
# So: ONE GROWTH, spelled every way legal JavaScript allows, all of which must DENY. Adding a
# spelling is one line; a view change or a regex tightening that blinds any of them reds. That is
# the difference between gating an instance and gating a class.
#
# `LENSES` is bounded by its literal; each line grows it; the fan is bounded-looking and must
# therefore be refused because the receiver is not.
arm_growth_denies() { # $1 = label, $2 = the mutation line
  check "deny-corpus: $1" 2 "$(node -e '
    const m = process.argv[1]
    const s = "export const meta={name:\"x\",description:\"y\"}\nconst MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n"
            + m + "\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)\n"
    process.stdout.write(JSON.stringify({tool_name:"Workflow",tool_input:{script:s}}))' "$2")"
}
arm_growth_denies "a plain push"                    'LENSES.push(x)'
arm_growth_denies "an unshift"                      'LENSES.unshift(x)'
arm_growth_denies "an inserting splice"             'LENSES.splice(0, 0, x)'
arm_growth_denies "a splice with a spread"          'LENSES.splice(...more)'
arm_growth_denies "inside a template interpolation" 'const s = `${LENSES.push(x)}`'
arm_growth_denies "after a closing paren"           'if (x) LENSES.push(y)'
arm_growth_denies "nested in another call"          'sink.push(LENSES.push(9))'
arm_growth_denies "after a semicolon"               'let i = 0; LENSES.push(x)'
arm_growth_denies "inside an arrow body"            'const f = () => LENSES.push(x)'
arm_growth_denies "as an expression statement"      '(LENSES.push(x))'
# THE VIEW AXIS, which is the one every fold of this build broke and the first corpus did not reach.
# Round 3's blocker: the take-back view stripped block comments over the JOINED text, so a `/*` in a
# regex literal — this file models none, by standing decision — opened a phantom comment that ate
# every take-back down to the next real `*/`. Ten spellings of the MUTATION could not see it,
# because the mutation was never what changed.
arm_growth_denies "below a regex literal containing a comment opener" 'const re = /[/*]/
LENSES.push(x)
const t = 1 /* a later real closer */'
arm_growth_denies "between two regex literals"      'const a = /[/*]/
LENSES.push(x)
const b = /[*/]/'
arm_growth_denies "on the same line as a closed block comment" '/* note */ LENSES.push(x)'
# ROUND 4's blocker: a regex literal and a REAL closer on the SAME line. Every strip this build
# tried paired the two; there is no strip now, so the growth is simply visible.
arm_growth_denies "regex literal and a real closer on one line" 'if (/[/*]/.test(s)) LENSES.push(x) /* ok */'
arm_growth_denies "regex literal, growth and closer, all one line" 'const re = /[/*]/; LENSES.push(x); const t = 1 /* pad */'
# ROUND 4's high: a comment in the argument list hid a top-level spread from the arity test. An
# argument list carrying a comment is no longer graded at all.
arm_growth_denies "a comment hiding a spread in splice args" 'LENSES.splice(0, /*
*/ ...rest)'
# The reassignment half of the same view, which round 3 found this fold had newly broken.
check "deny-corpus: a reassignment below a regex-literal comment opener" 2 "$(node -e '
  const s = "export const meta={name:\"x\",description:\"y\"}\nconst MAX_VERIFIERS = 5\nlet LENSES = [1,2,3]\n"
          + "const re = /[/*]/\nLENSES = allFindings\nconst t = 1 /* closer */\n"
          + "await boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)\n"
  process.stdout.write(JSON.stringify({tool_name:"Workflow",tool_input:{script:s}}))')"
# AND THE NEGATIVE HALF OF THE VIEW AXIS. A comment that MENTIONS a growth grows nothing, and a
# spread NESTED in a removal-only splice's argument is not a spread argument.
check "view axis: a single-line block comment mentioning a push DENIES (residual)" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n/* never do LENSES.push(x) here */\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
check "view axis: a spread nested in a removal-only splice → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nLENSES.splice(0, Math.min(...ns))\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'

# ---- the blanked view reports an unterminated scan (TOOL-aWeldedTribunal-3) ---------------------
# The blanked view carries its mode ACROSS lines, correctly, because a template literal spans them.
# That is also how one unterminated backtick blanked every line below it and the two rules reading
# that view went blind under it. Both now fall back to a PER-LINE blanked render.
#
# Rule 3 read the same view and retired in TOOL-dGroundRules-10 with its two arms here; rule 5's
# remain.
check "rule5: a ref-keyed join below an unterminated backtick → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const note = `an unterminated template\nconst m = new Map()\nm.set(f.ref, v)"}}'
# THE NARROWING SURVIVES THE FALLBACK. `TOOL-dTieredTribunal-14 S2` chose the blanked view for rule 5
# so a banned pattern inside a STRING would not match; falling back to a view that keeps template
# contents would regain that false-positive class, and `runBothViews` unions the views so either one
# denying is a denial. The fallback is the same scan reset per line, so the narrowing holds.
check "rule5: banned text in a single-line terminated template → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const p = `we never key a map by verdictByRef here`\nawait boundedParallel(T, 5)"}}'
# THE RESIDUAL, pinned rather than left unstated. A per-line view cannot know a line CONTINUES a
# template opened above it, so banned text on a continuation line reads as code and denies. It needs
# an unterminated backtick AND banned text, and it errs fail-CLOSED. Measured 0 before this unit and
# 2 after — an arm asserting the residual is how a trade stays priced instead of becoming folklore.
check "rule5: banned text on a continuation line → deny (stated residual)" 2 '{"tool_name":"Workflow","tool_input":{"script":"const note = `an unterminated template\nwe never key a map by verdictByRef here"}}'
check "rule5: a legal join under a terminated multi-line literal → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const p = `line one\nline two`\nconst m = new Map()\nm.set(f.id, v)"}}'
check "a legal multi-line prompt with a bounded fan → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const LENSES = [1,2,3]\nconst prompt = `line one\nline two\nline three`\nawait boundedParallel(LENSES.map((L) => () => agent(prompt)), 5)"}}'

# ---- rule 5: the ref-keyed verdict join -----------------------------------------------------------
# TOOL-dTieredTribunal-14's section 4 declared these ten arms as what "the failing case has been
# observed" means for that unit, and the unit landed WITHOUT them: `git show --stat fb2d692e` never
# touched this file, and no arm here named `join`, `.ref` or `--only`. Rule 5 was covered only
# INDIRECTLY, through check-review-join.sh delegating to this hook — so the hook's own suite could
# not tell whether its own rule worked. Written now, from that table, against the shipped rule.
#
# jso <name> <expected_exit> <flag> — like `js`, but passes a selector flag, which the three
# selector arms need and which `check`/`js` cannot express.
jso() { # name expected_exit flag  (script on stdin)
  local name=$1 want=$2 flag=$3 payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" | (cd "$TMP" && node "$HOOK" "$flag") >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" = "$want" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}

# The three bans. Each fires with NO raw primitive anywhere in the fixture, which is the whole point
# of the port: the file gate could only ever see files, and the modality where this defect actually
# happens is an inline `script` string on a Workflow call.
js "rule5: the bracket ban fires with no raw primitive present" 2 <<'EOF'
const verdicts = {}
verdicts[v.ref] = v
EOF
js "rule5: the Map ban fires" 2 <<'EOF'
const m = new Map()
m.set(f.ref, v)
EOF
js "rule5: the retired identifier fires" 2 <<'EOF'
const verdictByRef = new Map()
EOF

# Prose is NOT code. This is the narrowing the port deliberately took over the awk it replaced, and
# it is load-bearing: `<prefix>/workflows/tier2-review.js` carries a comment that necessarily spells the
# banned expression while documenting the retired join, and a whole-file-text ban reds on it.
js "rule5: a comment documenting the join is prose" 0 <<'EOF'
// never key the join on m[f.ref] = v again; use the integer id
const r = 1
EOF
js "rule5: a string mentioning the join is prose" 0 <<'EOF'
const s = "do not write m[f.ref] = v"
EOF
js "rule5: a template mentioning the join is prose" 0 <<'EOF'
const prompt = `Never key a verdict join on verdictByRef; use the integer id.`
EOF

# The integer-keyed join is the SANCTIONED shape, and an arm that only proves denial is satisfied by
# a rule that denies everything.
js "rule5: the integer-keyed join is untouched" 0 <<'EOF'
const verdictById = new Map()
verdictById.set(f.id, v)
EOF

# The selector, as ONE arm set of three. The eighth alone proves only that the fixture is harmless;
# the ninth is what shows the flag actually narrowed something; the tenth is what stops the flag
# being a silent switch that disables the cap whenever it is misspelled.
jso "rule5: --only=join passes a rule-2 breach that carries no join" 0 --only=join <<'EOF'
const r = await parallel(D.map((d) => () => agent(d.p)))
EOF
js "rule5: the same script unfiltered still denies" 2 <<'EOF'
const r = await parallel(D.map((d) => () => agent(d.p)))
EOF
jso "rule5: an unrecognised selector refuses" 2 --only=bogus <<'EOF'
const r = 1
EOF

# ---- rule 2: verifier arity ---------------------------------------------------------------------
# THE PROVENANCE OF THESE FIXTURES: the first is the verify stage of the bespoke closing-review
# workflow written in this repo's own session on 2026-08-09, reconstructed from the transcript. It is
# not a synthetic approximation of the mistake; it is the mistake. The nine after it are the evasions
# a reviewer proposed when asked to defeat the rule — each was ALLOWED by an earlier cut of this hook
# and each is here because it was, not because it was imagined.
js "rule2: one agent per finding → deny" 2 <<'EOF'
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(`Adversarially verify: ${f.title}`, { label: `verify:${f.id}` })))
EOF
js "rule2: fan-out wrapped over many lines → deny" 2 <<'EOF'
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(
    `line one
line two
line three
line four
line five
line six`,
    { label: `verify:${f.id}` })), 5)
EOF
js "rule2: flatMap → deny" 2 <<'EOF'
const r = await boundedParallel(all.flatMap((f) => [() => agent(f.claim)]), 5)
EOF
js "rule2: Array.from → deny" 2 <<'EOF'
const r = await boundedParallel(Array.from(all, (f) => () => agent(f.claim)), 5)
EOF
js "rule2: loop-built thunks → deny" 2 <<'EOF'
const th = []
for (const f of all) {
  th.push(() => agent(f.claim))
}
const r = await boundedParallel(th, 5)
EOF
js "rule2: forEach-built thunks → deny" 2 <<'EOF'
const th = []
all.forEach((f) => th.push(() => agent(f.claim)))
const r = await boundedParallel(th, 5)
EOF
js "rule2: renamed receiver → deny" 2 <<'EOF'
const groups = all
const r = await boundedParallel(groups.map((f) => () => agent(f.claim)), 5)
EOF
# The marker is a CLAIM; these three make it falsely and must still red, or the whitelist degenerates
# into "write the magic comment".
js "rule2: marker over chunk(all,1) → deny" 2 <<'EOF'
const b = chunk(all, 1) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marker over splitInto(all, all.length) → deny" 2 <<'EOF'
const b = splitInto(all, all.length) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marker with a literal above the cap → deny" 2 <<'EOF'
const b = splitInto(all, 9) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF

# ---- gov:sequential-agents (TOOL-dFoldedVerdict-4) ----------------------------------------------
# THE ONE LOOP SHAPE THE HOOK ADMITS. Owner-ratified spelling, 2026-09-01. It exists because a
# ratified `parallelism route: none` verdict forbids the bounded PARALLEL fan this hook permits while
# this hook forbade the strictly sequential dispatch that verdict requires — a harness iterating a
# build's units sat in the gap and could not be written at all.
#
# The ADMIT arm first, then one arm per clause. Each refusal names the FIRST clause that failed, so
# a fixture breaking two clauses proves only the earlier one — which is why C8's fixture keeps its
# `await` and breaks the function boundary instead.
js "seq: marked, bounded receiver, awaited, one call → ALLOW" 0 <<'EOF'
const MAX = 5
const units = [1, 2, 3, 4, 5]
const out = []
for (const u of units) { // gov:sequential-agents(MAX)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
js "seq: an array LITERAL receiver is bounded too → ALLOW" 0 <<'EOF'
const units = ['a', 'b', 'c']
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C3 — a bare marker claims concurrency one and says nothing about the TOTAL, which is the half the
# owner ruling insists on. Two rules, not one.
js "seq: a bare marker with no bound → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C4 — the number is CHECKED, through the same resolver every other consumer uses.
js "seq: a bound above the cap → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(9)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# AC6 — a bound the file cannot RESOLVE, in the two shapes that look resolved and are not. An
# `<expr> || <int>` right-hand side is a caller-settable knob wearing a constant's clothes, which is
# how two shipped harnesses raised their own verifier count past the cap while every gate stayed
# green; a `.length` is a number nobody wrote down.
js "seq: an or-bound K → deny" 2 <<'EOF'
const K = (args && args.cap) || 5
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(K)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
js "seq: a .length K → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(units.length)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C6 — THE CLAUSE THAT CARRIES THE WEIGHT. Without it the marker's number is an author's assertion
# over an array of any size, which is the shape the owner ruling names as the thing to refuse.
js "seq: marked, but the receiver is not proven bounded → deny" 2 <<'EOF'
const units = findings.map((f) => f.id)
const out = []
for (const u of units) { // gov:sequential-agents(5)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C7 — AWAIT-ADJACENCY on THIS occurrence. A loop that collects unawaited calls is building a thunk
# array with extra steps.
js "seq: marked and bounded but the call is not awaited → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(agent('do ' + u, { label: 'u' }))
}
EOF
# C8 — awaited, but through a function boundary, which is the evasion the ban exists for. This
# fixture keeps the `await` deliberately: break C7 as well and the refusal names C7 and proves
# nothing about C8.
js "seq: awaited THROUGH a function boundary → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  const run = async () => out.push(await agent('do ' + u, { label: 'u' }))
  await run()
}
EOF
# THE NINTH CONDITION, judged after the scan. Two awaited calls in one marked body spend twice the
# bound, so the marker would name a number the loop does not obey.
js "seq: TWO awaited calls in one marked body → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(await agent('a ' + u, { label: 'u' }))
  out.push(await agent('b ' + u, { label: 'u' }))
}
EOF
# NESTED LOOPS FAIL CLOSED with no extra clause: the walk stops at the first enclosing loop, so an
# unmarked inner loop inside a marked outer one is refused at the inner header.
js "seq: an unmarked inner loop inside a marked outer one → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  for (const p of u.parts) {
    out.push(await agent('do ' + p, { label: 'p' }))
  }
}
EOF
# AND THE UNMARKED LOOP STILL DENIES WITH ITS ORIGINAL SENTENCE. This is the arm that proves the
# marker is an affordance and not a weakening: no claim, no change.
js "seq: an unmarked loop is denied exactly as before → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) {
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF

# ---- THE CLOSING REVIEW'S FOLD. Four refusals, every one of them a bypass that was EXECUTED against
# ---- the shipped hook before it existed. All four are the same shape one level up: the predicate
# ---- read a LINE where the rule is about a CONSTRUCT, or bounded a BODY where the charter bounds a
# ---- TOTAL.
# The receiver clause used to take the FIRST `of <ident>)` anywhere on the header line, so a block
# comment supplied a bounded token for a loop iterating caller-sized data. One agent per element.
js "seq fold: a bounded token from a BLOCK COMMENT does not bless the loop -> deny" 2 <<'EOF'
const OK = ['a', 'b', 'c']
async function run(args) {
  for (/* of OK) */ const f of args.findings) await agent(f) // gov:sequential-agents(5)
}
EOF
# ...and from a guard clause on the same line.
js "seq fold: a bounded token from a GUARD clause does not bless the loop -> deny" 2 <<'EOF'
const OK = ['a', 'b', 'c']
async function run(args) {
  if ('probe' in OK) for (const f of args.findings) await agent(f) // gov:sequential-agents(5)
}
EOF
# A `while` has no iteration source this scan can size, so a bound over one is a claim about nothing.
js "seq fold: a marked while loop -> deny" 2 <<'EOF'
const OK = ['a', 'b', 'c']
async function run(args) {
  const queue = args.findings.slice()
  while (queue.length && ('probe' in OK)) { // gov:sequential-agents(5)
    await agent(queue.pop())
  }
}
EOF
# Two openers on one line: the brace walk stops at the shared header and the inner loop never gets
# its own. This is the fixture that refuted the old "nested loops fail closed" comment.
js "seq fold: two loop openers on one header line -> deny" 2 <<'EOF'
const OK = ['a', 'b']
async function run(args) {
  const ALL = args.findings
  for (const g of OK) for (const f of ALL) await agent(f) // gov:sequential-agents(5)
}
EOF
# THE SWEEP COUNTED LINES, NOT CALLS. Five awaited calls on one line contributed one entry, so the
# group stayed at 1 and 25 spawns landed under a marker naming 5.
js "seq fold: five awaited calls on ONE line -> deny" 2 <<'EOF'
const UNITS = ['a', 'b', 'c', 'd', 'e']
async function run() {
  for (const u of UNITS) { // gov:sequential-agents(5)
    await agent(u); await agent(u); await agent(u); await agent(u); await agent(u)
  }
}
EOF
# TWO HONEST MARKERS MULTIPLY. Every clause satisfied, 5 x 5 = 25 spawns. The bound is a TOTAL and
# the sweep relates no two headers.
js "seq fold: two nested marked loops -> deny" 2 <<'EOF'
const UNITS = ['a', 'b', 'c', 'd', 'e']
async function run() {
  for (const u of UNITS) { // gov:sequential-agents(5)
    for (const v of UNITS) { // gov:sequential-agents(5)
      await agent(u + v)
    }
  }
}
EOF
# ...and an UNMARKED outer loop does it unboundedly, while never being evaluated itself because no
# agent( line is attributed to it.
js "seq fold: a marked loop inside an UNMARKED loop -> deny" 2 <<'EOF'
const UNITS = ['a', 'b', 'c', 'd', 'e']
async function run(args) {
  for (const x of args.findings) {
    for (const u of UNITS) { // gov:sequential-agents(5)
      await agent(u)
    }
  }
}
EOF

# THE BYPASSES. Every one of these was ALLOWED by the first cut of rule 2 and reported "clean" by the
# merge-bar leg that delegates to it — found by an adversarial review of the commit that introduced
# the rule, each reproduced against this tree before it was fixed. They are here because a whitelist
# is only as good as the spellings it refuses, and the ones it has never seen are the ones that get
# written. The root cause was a single line: an unrecognised receiver fell through to ALLOW.
js "bypass: the marker on the agent() line itself → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.map((f) => () => agent(f.claim)), 5) // gov:fixed-verifiers
EOF
js "bypass: a .filter().map() chain → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.filter(Boolean).map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a call-result receiver → deny" 2 <<'EOF'
const r = await boundedParallel(Object.values(byId).map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a spread literal → deny" 2 <<'EOF'
const items = [...allFindings]
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: [].concat(x) → deny" 2 <<'EOF'
const items = [].concat(allFindings)
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a reassigned receiver → deny" 2 <<'EOF'
let items = [1, 2]
items = allFindings
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a braceless for-of body → deny" 2 <<'EOF'
const out = []
for (const f of allFindings) out.push(await agent(f.claim))
EOF
js "bypass: a braceless while body → deny" 2 <<'EOF'
let i = 0
while (i < all.length) out.push(await agent(all[i++].claim))
EOF
js "bypass: a marked .concat() derivation → deny" 2 <<'EOF'
const LENSES = [{ k: 1 }, { k: 2 }]
const more = LENSES.concat(allFindings) // gov:fixed-verifiers
const r = await boundedParallel(more.map((f) => () => agent(f.k)), 5)
EOF
js "bypass: .reduce() instead of .map() → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.reduce((a, f) => a.concat([() => agent(f.claim)]), []), 5)
EOF

# ---- rule 2: the shapes that MUST pass ----------------------------------------------------------
# Without these the rule could be satisfied by denying everything, which is a gate that stops work
# rather than stopping a defect.
js "rule2: bounded group count + marker → allow" 0 <<'EOF'
const MAX_VERIFIERS = 5
const batches = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(batches.map((g) => () => agent(g)), 5)
EOF
js "rule2: a fixed lens literal → allow" 0 <<'EOF'
const LENSES = [{ k: 'security' }, { k: 'correctness' }, { k: 'seams' }, { k: 'dead-code' }]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
# THE LENS ALLOWANCE IS THE SAME 5 AS EVERYTHING ELSE, and these three arms are why it can be. It
# read as 6 for one release and that was never a decision: the counter scored `1 + every top-level
# comma`, so a prettier-formatted 5-element array measured 6 and the constant had been raised to fit
# the error. Both drift-audit waves ship exactly this shape, so without the trailing-comma arm below
# lowering the number would deny two shipped harnesses — and the arm that proves the count is fixed
# has to be the multi-line, trailing-comma form, because the single-line one never mis-measured.
js "rule2: five lenses, prettier-formatted with a trailing comma → allow" 0 <<'EOF'
const LENSES = [
  { k: 'dead-code' },
  { k: 'unwired' },
  { k: 'duplication' },
  { k: 'inefficient' },
  { k: 'instruments' },
]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: six lenses → deny (the allowance is 5)" 2 <<'EOF'
const LENSES = [{ k: 'a' }, { k: 'b' }, { k: 'c' }, { k: 'd' }, { k: 'e' }, { k: 'f' }]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: six lenses with a trailing comma → deny (the comma is not a sixth escape)" 2 <<'EOF'
const LENSES = [
  { k: 'a' },
  { k: 'b' },
  { k: 'c' },
  { k: 'd' },
  { k: 'e' },
  { k: 'f' },
]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a marked derivation from a bounded literal → allow" 0 <<'EOF'
const ALL_LENSES = [{ s: 'a' }, { s: 'b' }, { s: 'c' }]
const LENSES = a.lenses ? ALL_LENSES.filter((L) => a.lenses.includes(L.s)) : ALL_LENSES // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.s)), 5)
EOF
# TOOL-dTieredTribunal-13 S5 — the marked branch now judges EVERY top-level value branch. THREE of
# these five DENY arms are the reproduced holes: before this unit each PASSED, because either accept
# could return on a single arm while the other stayed caller-supplied. The other two are the guards
# inside the new predicate, which had no arm at all — and a guard nobody has watched fail is an
# assertion about nothing. Every one was run against the shipped file and its verdict recorded.
js "rule2: marked ternary whose OTHER arm is caller-supplied → deny" 2 <<'EOF'
const SPEC = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.kind === 'spec' ? SPEC : args.customLenses // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: marked .filter ROOTED on a caller value → deny" 2 <<'EOF'
const ALL = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.lenses.filter((L) => ALL.includes(L)) // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: bounded split in one arm, caller value in the other → deny" 2 <<'EOF'
const MAX_VERIFIERS = 5
const items = [1, 2, 3]
const b = cond ? chunk(items, Math.ceil(items.length / MAX_VERIFIERS)) : args.custom // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marked line whose right-hand side yields NO branch → deny" 2 <<'EOF'
const LENSES = // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
EOF
js "rule2: marked ternary whose : is not on the line → deny" 2 <<'EOF'
const SPEC = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.kind === 'spec' ? SPEC // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a marked ternary between two sibling literals → allow" 0 <<'EOF'
const SPEC_LENSES = [{ k: 'a' }, { k: 'b' }]
const DIFF_LENSES = [{ k: 'c' }, { k: 'd' }]
const LENSES = kind === 'spec-audit' ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a single synthesis agent → allow" 0 <<'EOF'
const synth = await agent('synthesize the confirmed findings', { label: 'synth' })
EOF
# The synthesis stage builds its PROMPT with a .map over every finding. A proximity-based scan read
# that as a fan-out and denied a one-agent call — measured on <prefix>/workflows/tier2-review.js:290.
js "rule2: a synth prompt that quotes a .map → allow" 0 <<'EOF'
const synth = await agent(
  'findings:\n' + allFindings.map((f) => f.claim).join('\n'),
  { label: 'synth' })
EOF

# ---- scriptPath: a saved script is a FILE, and a node hook has fs -------------------------------
# Exiting 0 here made both rules unenforceable the moment anyone wrote the offending script to disk.
# NODE'S VIEW OF THE PATH, not the shell's. Under MSYS/git-bash one directory has two spellings and
# `mktemp -d` hands back the POSIX one (`/tmp/tmp.X`), which node cannot open. The first cut of these
# three arms passed for the wrong reason: the "offending file denied" arm was green because the read
# FAILED, not because the rule fired — a fixture that proves nothing while looking like proof.
NODEDIR=$(cd "$TMP" && pwd -W 2>/dev/null || printf '%s' "$TMP")
GOOD="$TMP/good.js"; printf 'const s = await agent("one")\n' > "$GOOD"
BAD="$TMP/bad.js";   printf 'const r = await boundedParallel(all.map((f) => () => agent(f.c)), 5)\n' > "$BAD"
GOOD="$NODEDIR/good.js"; BAD="$NODEDIR/bad.js"
check "scriptPath → clean file allowed" 0 "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\"}}"
check "scriptPath → offending file denied" 2 "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$BAD\"}}"
check "scriptPath → unreadable path refused, not waved through" 2 '{"tool_name":"Workflow","tool_input":{"scriptPath":"/no/such/workflow.js"}}'
# A `name:` run supplies no source at all. It is ALLOWED here and covered by the merge-bar leg over
# <prefix>/workflows/ instead — declared, not papered over.
check "name-only run → allow (no source reaches the hook)" 0 '{"tool_name":"Workflow","tool_input":{"name":"tier2-review"}}'

# ---- rule 0: a spec audit is OPT-IN, declared in the build README's front matter ----------------
# TOOL-aBlindedTrial-4. The rule reads `tool_input.args` ONLY — never the script text, which both
# shipped harnesses fill with the word `spec-audit` — so every arm here carries the CLEAN script
# above and differs from its neighbour in args alone. Every deny arm asserts its own branch text,
# since every rule exits 2; `check_spec_audit` runs each payload TWICE, args as an OBJECT and as a JSON STRING,
# because the Workflow tool delivers both and the first cut of tier2-review's own guard refused one.
SAREPO="$TMP/sarepo"; mkdir -p "$SAREPO/memory/builds/tSA/reviews"
SAJ="$NODEDIR/sarepo"; SAREADME="$SAREPO/memory/builds/tSA/README.md"
check_spec_audit() { # name expected_exit needles(;;-joined, empty for an allow) args-json
  local name=$1 want=$2 needles=$3 args=$4 form payload got n miss
  for form in object string; do
    payload=$("$TESTPY" -c 'import json,sys
g,a,form=sys.argv[1:4]
args=json.loads(a)
print(json.dumps({"tool_name":"Workflow","tool_input":{"scriptPath":g,"args":args if form=="object" else json.dumps(args)}}))' "$GOOD" "$args" "$form")
    printf '%s' "$payload" | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; got=$?
    if [ "$got" != "$want" ]; then
      echo "FAIL $name [args as $form] (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); continue
    fi
    miss=""
    if [ -n "$needles" ]; then
      # Split on `;;` alone — a needle may carry spaces ("not a date"), so no word-splitting here.
      # Fed from a scratch FILE, never a here-string holding a command substitution: the
      # shell-hygiene leg reds that shape because a failed substitution leaves the read at EOF.
      # WITH a trailing newline (TOOL-aBlindedTrial-7): `read` returns non-zero on the final
      # unterminated line, so `printf '%s'` left every arm's LAST needle unchecked and a
      # single-needle arm checking nothing - observed when a needle absent from the deny passed.
      printf '%s\n' "$needles" | sed 's/;;/\n/g' > "$TMP/needles"
      while IFS= read -r n; do
        [ -n "$n" ] && ! grep -qF -- "$n" "$TMP/err" && miss="$miss [$n]"
      done < "$TMP/needles"
    fi
    # A deny that spells a kit-install path strands every adopter that installed the kit elsewhere
    # — the shipped-surface ratchet holds this hook at its current count, and this arm holds the text.
    if [ "$want" = 2 ] && grep -q 'tools[/]' "$TMP/err"; then miss="$miss <a-kit-path-literal>"; fi
    if [ -z "$miss" ]; then echo "ok   $name [args as $form]"; pass=$((pass+1))
    else echo "FAIL $name [args as $form] (exit $got as wanted, but the message misses:$miss)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
  done
}
# AC1 — the README exists and carries no key: denied, naming the decision, the key and the README.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
check_spec_audit "rule0: spec-audit, README without the key → deny naming id + key + README" 2 \
  "TOOL-aBlindedTrial-6;;spec-audit:;;builds/tSA/README.md" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
# S5 — the rule sits ABOVE the script read, so a `name:`-only invocation is judged too.
check "rule0: spec-audit by NAME only, README without the key → deny" 2 \
  "{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
# AC4 — a diff review, and an absent kind, are not this rule's business; the same undeclared README.
check_spec_audit "rule0: kind diff-review on the same undeclared README → allow" 0 "" \
  "{\"kind\":\"diff-review\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
check_spec_audit "rule0: no kind at all → allow" 0 "" "{\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# CONTROL — script TEXT spelling the kind, args carrying none: the rule keys on args, never on text.
check "rule0: control, 'spec-audit' in the script text with no such args → allow" 0 \
  '{"tool_name":"Workflow","tool_input":{"script":"// kind: '"'"'spec-audit'"'"' — prose only\nconst s = await agent(\"one\")"}}'
# STATED LIMIT — an args string that does not parse shows the hook no kind; the harness throws on it.
check "rule0: unparseable args string → allow (stated limit: no kind is visible)" 0 \
  "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\",\"args\":\"{kind: spec-audit, not json\"}}"
# AC2 — the key in the front matter, dated: allowed.
printf -- '---\nslug: tSA\nspec-audit: 2026-09-20\n---\n' > "$SAREADME"
check_spec_audit "rule0: spec-audit, README declares spec-audit: <date> → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC3 — a non-date value is a claim with no owner date behind it; a body-only key is not front matter.
printf -- '---\nslug: tSA\nspec-audit: yes\n---\n' > "$SAREADME"
check_spec_audit "rule0: spec-audit: yes → deny, not a date" 2 "not a date;;spec-audit: yes" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf -- '---\nslug: tSA\n---\n\n```\nspec-audit: 2026-09-20\n```\n' > "$SAREADME"
check_spec_audit "rule0: key only inside a fenced BODY block → deny (front matter only)" 2 "front matter" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC5 — an unplaceable call fails CLOSED, naming the field: a numeric repo, a reviewDir outside
# any builds/<slug>/ folder, and no reviewDir at all.
printf -- '---\nslug: tSA\nspec-audit: 2026-09-20\n---\n' > "$SAREADME"
check_spec_audit "rule0: repo is a number → deny naming repo" 2 '`repo`' \
  "{\"kind\":\"spec-audit\",\"repo\":7,\"reviewDir\":\"memory/builds/tSA/reviews\"}"
check_spec_audit "rule0: reviewDir outside builds/<slug>/ → deny naming reviewDir" 2 '`reviewDir`;;docs/reviews' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"docs/reviews\"}"
check_spec_audit "rule0: reviewDir absent → deny naming reviewDir" 2 '`reviewDir`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\"}"
# AC6 — a README this hook cannot READ is a deny, never a stack trace at exit 1 (which admits).
mkdir -p "$SAREPO/memory/builds/tDir/reviews" "$SAREPO/memory/builds/tDir/README.md"
check_spec_audit "rule0: README path is a DIRECTORY → deny (exit 2, not a crash at 1)" 2 "could not be read;;spec-audit:" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tDir/reviews\"}"
check_spec_audit "rule0: README absent → deny naming the path tried" 2 "builds/tNone/README.md;;could not be read" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tNone/reviews\"}"
# F1 (closing review of units 2–5, round 1) — the guard and its callee must agree on WHAT a spec-audit
# call IS. `tier2-review.js` derives `kind` as `String(a.kind)`, so `["spec-audit"]` runs a full audit
# there; the hook's strict equality ADMITTED it. Both delivery forms, on the undeclared README.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
check_spec_audit "rule0: kind [\"spec-audit\"] (an array) on the undeclared README → deny" 2 "TOOL-aBlindedTrial-6;;spec-audit:" \
  "{\"kind\":[\"spec-audit\"],\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# ...and the CLASS: one payload set fed to the hook AND to the callee's own `kind` line — the one line
# of tier2-review.js that decides `isSpec` — asserting the two agree. An edit to either side reds
# here until the other follows. The harness sits beside this kit in this repo; an adopter layout
# without it gets an ANNOUNCED skip, never a silent green.
T2R=""; _wf_dir=$(resolve_kit_dir "$TESTPY" workflows tier2-review.js "$HERE" 2>/dev/null) && T2R="$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)/$_wf_dir/tier2-review.js"
if [ -f "$T2R" ]; then
  kind_line=$(grep -m1 '^const kind = ' "$T2R")
  for k in '"spec-audit"' '["spec-audit"]' '"diff-review"' '"SPEC-AUDIT"' '{"k":"spec-audit"}' '7'; do
    callee=$(node -e "const a={kind:$k}; $kind_line; console.log(kind==='spec-audit'?2:0)" 2>/dev/null)
    printf '%s' "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\",\"args\":{\"kind\":$k,\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}" \
      | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; got=$?
    if [ -n "$callee" ] && [ "$got" = "$callee" ]; then echo "ok   rule0: pair — hook and tier2-review agree on kind $k (exit $got)"; pass=$((pass+1))
    else echo "FAIL rule0: pair — hook exit $got, tier2-review isSpec says exit-equivalent '$callee' for kind $k"; fail=$((fail+1)); fi
  done
else
  echo "skip rule0: pair arm — tier2-review.js is not beside this kit (adopter layout); the class arm did NOT run"
fi
# F2 — the declaration is read from where the RECORD lands (`reviewDir`), so the SUBJECTS must sit
# under that same `builds/<slug>/`, else naming a declared build's reviews folder audits an
# undeclared build's specs. And a `reviewDir` that climbs through `..` is not placed by its own text.
printf -- '---\nslug: tSA\nspec-audit: 2026-09-20\n---\n' > "$SAREADME"
mkdir -p "$SAREPO/memory/builds/tOther/reviews"; printf -- '---\nslug: tOther\n---\n' > "$SAREPO/memory/builds/tOther/README.md"
check_spec_audit "rule0: declared reviewDir, one subject under ANOTHER build → deny naming subjects + the path" 2 '`subjects`;;builds/tOther/spec/s.md' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"},{\"path\":\"memory/builds/tOther/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: declared reviewDir, every subject under the SAME build → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"},{\"path\":\"memory/builds/tSA/spec/t.md\",\"blob\":\"abc1235\"}]}"
check_spec_audit "rule0: declared reviewDir, a subject with NO builds/<slug> segment → deny naming subjects" 2 '`subjects`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"docs/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: declared reviewDir, a subject re-routed through .. → deny naming subjects" 2 '`subjects`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/../tOther/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: reviewDir climbing through .. into a declared build → deny naming reviewDir" 2 '`reviewDir`;;..' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ/memory/builds/tOther\",\"reviewDir\":\"../../builds/tSA/reviews\"}"
# F5 — an MSYS-form `repo` (`/c/...`) is a spelling this node's corpus carries and the harness's own
# `git -C` accepts; `path.resolve` on win32 made it `C:\c\...` and denied a DECLARED build with ENOENT.
# Derived from $SAJ, so on a host where `pwd -W` is not a thing the arm feeds the unchanged POSIX path.
SAM=$(printf '%s' "$SAJ" | sed 's|^\([A-Za-z]\):/|/\L\1/|')
check_spec_audit "rule0: declared build, repo in MSYS /<drive>/ form → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAM\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# R1 (round 2) — containment must hold on the ROOT axis, not only the slug axis. A SECOND checkout
# beside the first, same slug, no declaration: an ABSOLUTE or `~`-rooted subject spelling it was
# admitted, because the walk found `builds/tSA` somewhere in the string and never asked whether the
# path sits under `repo`. A direct spec-audit subject is repo-relative by the harness's own contract,
# so every other spelling is denied by the same `subjects` sentence. The repo-relative allow above
# is the control.
SAREPO2="$TMP/sarepo2"; mkdir -p "$SAREPO2/memory/builds/tSA/spec"; printf -- '---\nslug: tSA\n---\n' > "$SAREPO2/memory/builds/tSA/README.md"
SAJ2="$NODEDIR/sarepo2"; SAM2=$(printf '%s' "$SAJ2" | sed 's|^\([A-Za-z]\):/|/\L\1/|')
check_spec_audit "rule0: declared reviewDir, an ABSOLUTE subject into a same-slug second checkout → deny naming subjects" 2 '`subjects`;;sarepo2/memory/builds/tSA/spec/s.md' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"$SAJ2/memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: ...the same subject in MSYS /<drive>/ form → deny naming subjects" 2 '`subjects`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"$SAM2/memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: declared reviewDir, a ~-rooted subject → deny naming subjects" 2 '`subjects`;;~/memory/builds/tSA/spec/s.md' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"~/memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
# R2 (round 2) — the F5 fold corrects a WIN32 rule and must run there alone: on POSIX `/w/repo` is a
# real root and the fold turned it into a cwd-relative `w:/repo` that ENOENTs. The hook exports
# nothing, so the fold line is read out of the source and run under an overridden platform — the F1
# pair arm's trick. A line that stops matching is a loud FAIL, never a silent pass.
fold_line=$(grep -m1 '^[[:space:]]*const repo = ' "$HOOK")
for plat_in_want in 'linux|/w/repo|/w/repo' 'win32|/w/repo|w:/repo' 'linux|C:/x/y|C:/x/y' 'win32|/tmp/x|/tmp/x'; do
  IFS='|' read -r plat rin rwant <<<"$plat_in_want"
  rgot=$(node -e "Object.defineProperty(process,'platform',{value:'$plat'}); const a={repo:'$rin'}; $fold_line; console.log(repo)" 2>/dev/null)
  if [ -n "$fold_line" ] && [ "$rgot" = "$rwant" ]; then echo "ok   rule0: fold — on $plat repo $rin folds to $rwant"; pass=$((pass+1))
  else echo "FAIL rule0: fold — on $plat repo $rin folded to '$rgot', want $rwant"; fail=$((fail+1)); fi
done
# ...and what the fold cannot reach ANNOUNCES itself: a repo under any other MSYS mount (`/tmp/…`)
# used to resolve to `C:\tmp\…` and deny as a README that does not exist, hiding the spelling that
# was tried. Win32 only — on POSIX `/tmp/x` is a real path and there is nothing to announce.
if [ "$(node -p process.platform)" = win32 ]; then
  case "$TMP" in /tmp/*) SAMOUNT="$TMP/sarepo" ;; *) SAMOUNT="/tmp/sarepo-msys-mount" ;; esac
  check_spec_audit "rule0: declared build, repo under an MSYS mount other than /<drive>/ → deny naming repo + MSYS" 2 '`repo`;;MSYS' \
    "{\"kind\":\"spec-audit\",\"repo\":\"$SAMOUNT\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
else
  echo "skip rule0: MSYS-mount deny arm — not win32 (the fold and its residual are win32-only); the arm did NOT run"
fi
# TOOL-aBlindedTrial-7 — a PROJECT-WIDE default. When the README carries NO key, the hook reads
# `SPEC_AUDIT_DEFAULT` from `<repo>/.unattended.conf` (the WORKTREE copy — this hook guards a session
# with an owner present; the driver reads BASE). Node cannot source shell, so the read is a deliberate
# re-parse, and the three spellings the two-readers gotcha names are each an arm: single quotes, a
# trailing comment, and a last-wins pair. The value is ARMED: a non-date DENIES by name rather than
# reading as absent. The README, present with any value, wins — a malformed key beside a dated
# default is still the not-a-date deny, never a silent fall-back.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
SACONF="$SAREPO/.unattended.conf"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
check_spec_audit "rule0/U7: README without the key, conf SPEC_AUDIT_DEFAULT=\"<date>\" → allow by project default" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf "SPEC_AUDIT_DEFAULT='2026-09-21'\n" > "$SACONF"
check_spec_audit "rule0/U7: the single-quoted spelling → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21" # the day the owner ruled\n' > "$SACONF"
check_spec_audit "rule0/U7: a trailing comment after the value → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# closing review of units 7/8, R8 — a `#` GLUED to a bare word is part of the word to the shell, not a
# comment: `2026-09-21#c` is fail 54 in the driver, and rev-1's regex stopped the word at `#` and
# admitted the date. Observed RED-first on that hook. Its sibling, the `;`-joined line, reads as NO
# assignment here (the README deny, the safe direction) while the shell reads the date — a stated
# limit of this reader, pinned so it cannot drift into the permissive direction unnoticed.
printf 'SPEC_AUDIT_DEFAULT=2026-09-21#note\n' > "$SACONF"
check_spec_audit "rule0/U7: a glued #note on a bare value is part of the value → deny, not a date" 2 "SPEC_AUDIT_DEFAULT;;not a date" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"; X=1\n' > "$SACONF"
check_spec_audit "rule0/U7: a ;-joined second command reads as no assignment → the README deny (documented limit)" 2 "TOOL-aBlindedTrial-6;;spec-audit:;;builds/tSA/README.md" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="yes"\nSPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
check_spec_audit "rule0/U7: two assignments, the LAST a date → allow (last wins, as the shell reads it)" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\nSPEC_AUDIT_DEFAULT="yes"\n' > "$SACONF"
check_spec_audit "rule0/U7: two assignments, the LAST a non-date → deny naming the key" 2 "SPEC_AUDIT_DEFAULT;;not a date" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="yes"\n' > "$SACONF"
check_spec_audit "rule0/U7: conf SPEC_AUDIT_DEFAULT=\"yes\" → deny naming the key, not a date" 2 "SPEC_AUDIT_DEFAULT;;not a date" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT=""\n' > "$SACONF"
check_spec_audit "rule0/U7: conf SPEC_AUDIT_DEFAULT=\"\" (blank) → the README deny, unchanged" 2 "TOOL-aBlindedTrial-6;;spec-audit:;;builds/tSA/README.md" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# ...the deny's REMEDY names both routes, so an adopter learns the project-wide one from the refusal.
check_spec_audit "rule0/U7: the README deny names SPEC_AUDIT_DEFAULT as the other remedy" 2 "SPEC_AUDIT_DEFAULT" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
printf -- '---\nslug: tSA\nspec-audit: yes\n---\n' > "$SAREADME"
check_spec_audit "rule0/U7: README spec-audit: yes beside a dated default → deny, not a date (README wins)" 2 "not a date;;spec-audit: yes" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
check_spec_audit "rule0/U7: dated conf, README absent → still could-not-be-read (fail-closed unchanged)" 2 "builds/tNone/README.md;;could not be read" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tNone/reviews\"}"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
rm -f "$SACONF"
check_spec_audit "rule0/U7: conf removed, README without the key → deny (no conf is no default)" 2 "TOOL-aBlindedTrial-6;;spec-audit:" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"

# ---- TOOL-aWardedAudit-2 — the opt-in is the OWNER's. Each deny below was observed admitting
# ---- against the base hook first: it read the worktree key whoever wrote it.
SARUN="$SAREPO/memory/builds/tSA/RUN.md"
# AC3 — no run-state file, a prompt-mode README carrying a dated key → deny naming the mode.
printf -- '---\nslug: tSA\nauthorized-by: prompt\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
check_spec_audit "rule0/aWardedAudit: prompt README with a dated key → deny naming the mode" 2 "authorized-by: prompt;;admits nothing;;TOOL-aWardedAudit-4" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC1 — a live run that pinned no fact, beside a slug README carrying a dated key → deny naming RUN.md.
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nslug: tSA\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: live run with no spec-audit fact, worktree key → deny" 2 "builds/tSA/RUN.md;;live unattended run;;phase BUILDING" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC2 — the same live run pinning a dated fact, beside a README with NO key → allow.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: 2026-10-05\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: live run pinning a dated fact → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# ...and a non-date fact is no fact: deny.
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: yes\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: live run pinning a non-date fact → deny" 2 "live unattended run" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC4 — a FINISHED run's file decides nothing: a LANDED record beside a slug README's dated key → allow.
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: LANDED\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: LANDED run-state file, slug README key → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
rm -f "$SARUN"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"

# ---- TOOL-aWardedAudit-2 S4 — the BUILD HARNESS's `specAudit` is judged by the same predicate: its
# ---- nested audit is a runtime `workflow()` call no hook sees, so this is the one tool call there is.
# ---- The base hook admitted every one of these, because it judged `kind` alone.
SAH="{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\"}"
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: BUILDING\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: harness specAudit, live run pinning no fact → deny" 2 "builds/tSA/RUN.md;;live unattended run" "$SAH"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: 2026-10-05\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: harness specAudit equal to the pinned fact → allow" 0 "" "$SAH"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: 2026-09-01\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: harness specAudit differing from the pinned fact → deny" 2 "pins \`spec-audit: 2026-09-01\`;;the pinned date or nothing" "$SAH"
check_spec_audit "rule0/aWardedAudit: harness specAudit with an unplaceable slug → deny" 2 "is not one path segment" \
  "{\"repo\":\"$SAJ\",\"slug\":\"../x\",\"specAudit\":\"2026-10-05\"}"
check_spec_audit "rule0/aWardedAudit: harness call with no specAudit → not this rule's business" 0 "" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\"}"
rm -f "$SARUN"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"

# ---- TOOL-aWardedAudit-6 — the closing review's minors on rule 0. Each changed verdict was observed
# ---- against the base hook first.
SAOTH="$SAREPO/memory/builds/tOth"; mkdir -p "$SAOTH"
printf -- '---\nslug: tOth\nspec-audit: 2026-10-05\n---\n' > "$SAOTH/README.md"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\nphase: BUILDING\n' > "$SARUN"
# S1 / AC1 — a harness call for tSA is placed in tSA: another build's reviewDir or spec path → deny.
check_spec_audit "rule0/aWardedAudit-6: harness reviewDir under another build → deny" 2 "under another build;;memory/builds/tOth/reviews" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\",\"reviewDir\":\"memory/builds/tOth/reviews\"}"
check_spec_audit "rule0/aWardedAudit-6: harness units[].specPath under another build → deny" 2 "units[].specPath;;memory/builds/tOth/spec/a.md" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\",\"units\":[{\"id\":\"x\",\"specPath\":\"memory/builds/tOth/spec/a.md\"},{\"id\":\"y\"}]}"
# S5 / AC1 — an EMPTY reviewDir defaults as the harness does, so the live run's file decides.
check_spec_audit "rule0/aWardedAudit-6: harness reviewDir \"\" → placed in builds/tSA, the live run denies" 2 "builds/tSA/RUN.md;;live unattended run" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\",\"reviewDir\":\"\"}"
# S2 / AC2 — only `## Run facts` is read, and LANDING is no live run.
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\nphase: BUILDING\n\n## Run facts\nphase: LANDING\n\n## Parked\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit-6: a stray phase above Run facts, LANDING inside → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf '# run\nspec-audit: 2026-10-05\n\n## Run facts\nphase: BUILDING\n\n## Parked\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit-6: a spec-audit line outside Run facts is no fact → deny" 2 "live unattended run" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf '# run\n\n## Run facts\nphase: ABORTED\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit-6: an ABORTED record decides nothing → allow on the slug key" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
rm -f "$SARUN"
# S3 / AC3 — a harness call with NO run-state file reads the README and the conf as an attended call.
check_spec_audit "rule0/aWardedAudit-6: harness call, no run-state file, slug README key → allow" 0 "" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\"}"
printf -- '---\nslug: tSA\nauthorized-by: prompt\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
check_spec_audit "rule0/aWardedAudit-6: harness call, no run-state file, prompt README key → deny" 2 "authorized-by: prompt;;admits nothing" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\"}"
# ...and the mode deny needs a KEY: a prompt README with none, beside a dated default → allow.
printf -- '---\nslug: tSA\nauthorized-by: prompt\n---\n' > "$SAREADME"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
check_spec_audit "rule0/aWardedAudit-6: prompt README with no key, dated worktree default → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
rm -f "$SACONF"
rm -rf "$SAOTH"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"

# ---- rule 2: the marked K and a reassigned receiver, each refusal asserting its own text ----------
# Rule 3, which resolved every concurrency width, retired in TOOL-dGroundRules-10 with its arms.
# These three were filed beside it and are rule 2's: the marker's K resolves through the one binder,
# and an `<expr> || <int>` fallback or a reassignment takes the bound back. Each asserts its message,
# because every rule exits 2.
msg() { # name expected_exit needle   (script on stdin)
  local name=$1 want=$2 needle=$3 payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" != "$want" ]; then
    echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); return
  fi
  if grep -qF "$needle" "$TMP/err"; then echo "ok   $name"; pass=$((pass+1))
  else echo "FAIL $name (exit $got as wanted, but no branch named: $needle)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}

msg "rule2: a marked K bound by an || fallback → deny" 2 \
  'which this file does not show to be bounded' <<'EOF'
const MAX_VERIFIERS = (args && args.maxVerifiers) || 5
const b = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
# A BARE REASSIGNMENT invalidates the NUMBER, not just the receiver: `let K = 5; K = 500` published a 5.
msg "rule2: a reassigned K → deny" 2 \
  'which this file does not show to be bounded' <<'EOF'
let K = 5
K = 500
const b = chunk(all, Math.ceil(all.length / K)) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF

# D10 - a REASSIGNED receiver must SAY so. The reason map is written by both scan passes and was
# never cleared on accept, so a name refused on pass 1 for declaration order and then accepted on
# pass 2 kept the pass-1 text; the sweep below took the name back and the refusal printed an
# explanation of a branch pass 2 had just blessed. This arm asserts the TEXT, because an exit-code
# arm cannot tell a right reason from a wrong one.
msg "rule2: a reassigned marked receiver -> deny NAMING the reassignment" 2   'was REASSIGNED after its bounded assignment' <<'EOF'
let LENSES = ALL.filter((L) => L.on) // gov:fixed-verifiers
const ALL = [1, 2, 3]
LENSES = args.custom
const r = await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
EOF

# ---- a set AGENT_CAP is read by nothing (TOOL-dGroundRules-10) ------------------------------------
# The refusal of a set `AGENT_CAP` retired in TOOL-dGroundRules-10 with the clamp it guarded: the agent limit is the
# policy kit's `runtime.agents-in-flight`, and this hook reads no ceiling from the environment.
printf '%s' '{"tool_name":"Workflow","tool_input":{"script":"const r = await agent(1)"}}' > "$TMP/envpayload"
(cd "$TMP" && AGENT_CAP=50 node "$HOOK") < "$TMP/envpayload" >/dev/null 2>"$TMP/env.err"; envrc=$?
if [ "$envrc" = 0 ] && [ ! -s "$TMP/env.err" ]; then
  echo "ok   a set AGENT_CAP over a clean script is admitted, silently"; pass=$((pass+1))
else
  echo "FAIL a set AGENT_CAP was not admitted (exit $envrc)"; sed 's/^/     /' "$TMP/env.err"; fail=$((fail+1))
fi

# The rule-2 remediation text names the number it enforces, and the constant it lives in.
if grep -qF "verify-stage agents at 5 TOTAL, this hook's MAX_VERIFIERS" <(printf '%s' '{"tool_name":"Workflow","tool_input":{"script":"const r = await boundedParallel(all.map((f) => () => agent(f.c)), 5)"}}' | (cd "$TMP" && node "$HOOK") 2>&1); then
  echo "ok   rule-2 deny text names the 5-verifier cap"; pass=$((pass+1))
else echo "FAIL rule-2 deny text does not name the cap"; fail=$((fail+1)); fi

# ---- the agent limit (TOOL-dGroundRules-10) -------------------------------------------------------
# Rule 4, the per-prompt slot ledger, and the 1-to-5 clamp read from `.agent-cap.conf` retired in TOOL-dGroundRules-10:
# the harness counts agents in flight under the two settings the policy kit renders. The arms below
# run a COPY of the hook beside a copy of scratch-guard.js and nothing else, so rule 7 finds no policy
# kit and adds no rule, in a checkout that is a bare `.git` directory, which is all the root walk
# looks for. The last arm puts a policy kit beside the copy, in a real repository, and rule 7 arms.
LIMHK="$TMP/limit-hooks/hooks"; mkdir -p "$LIMHK"; cp "$HERE/agent-cap.js" "$HERE/scratch-guard.js" "$LIMHK/"
LIMREPO="$TMP/limitrepo"; mkdir -p "$LIMREPO/.git" "$LIMREPO/sub"
LIMJ="$NODEDIR/limitrepo/sub"
run_limit_call() { # name expected_exit payload-json [hook] [text stderr must carry]
  local got
  printf '%s' "$3" | (cd "$TMP" && node "${4:-$LIMHK/agent-cap.js}") >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" = "$2" ] && { [ -z "${5:-}" ] || grep -qF -- "$5" "$TMP/err"; }; then
    echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else
    echo "FAIL $1 (exit $got, want $2${5:+, stderr carrying '$5'})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
}
LIM_WF='{"tool_name":"Workflow","cwd":"'"$LIMJ"'","tool_input":{"script":"const r = await agent(1)"}}'
# A conf above the retired clamp's five is no refusal: the hook reads no conf.
printf 'FANOUT_CAP=8\n' > "$LIMREPO/.agent-cap.conf"
run_limit_call "limit: FANOUT_CAP=8 in .agent-cap.conf, a Workflow call -> allow" 0 "$LIM_WF"
run_limit_call "limit: FANOUT_CAP=8 in .agent-cap.conf, an Agent call -> allow" 0 '{"tool_name":"Agent","cwd":"'"$LIMJ"'","session_id":"s8","prompt_id":"p8","tool_use_id":"u8"}'
rm -f "$LIMREPO/.agent-cap.conf"
# Six direct spawns in one prompt: the slot ledger that refused the sixth is gone, and so is its directory.
for i in 1 2 3 4 5 6; do
  run_limit_call "limit: direct spawn $i of one prompt -> allow" 0 '{"tool_name":"Agent","cwd":"'"$LIMJ"'","session_id":"s6","prompt_id":"p6","tool_use_id":"u'"$i"'"}'
done
if [ -e "$LIMREPO/.git/agent-cap" ]; then
  echo "FAIL limit: a slot ledger directory appeared under $LIMREPO/.git"; fail=$((fail+1))
else
  echo "ok   limit: no slot ledger directory under the git dir"; pass=$((pass+1))
fi
# A raw primitive with no agent fan, and a width of 50: rules 1 and 3 retired, so each is admitted.
check "limit: a raw parallel over items.map -> allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const items = [1, 2]\nconst r = await parallel(items.map((i) => () => i))"}}'
check "limit: boundedParallel(thunks, 50) -> allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const r = await boundedParallel(thunks, 50)"}}'
# RULE 7, armed: a real repository whose policy lands a limit of 2, the hook copy with a copy of the
# policy kit beside it, and the settings the harness would start from first above the limit, then at it.
LIMPK=$(resolve_kit_dir "$TESTPY" policy policy.py "$HERE") || LIMPK=""
ROOTDIR=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null)
if [ -z "$LIMPK" ] || [ -z "$ROOTDIR" ]; then
  echo "FAIL limit: no policy kit beside this hooks kit, so rule 7 has nothing to arm with"; fail=$((fail+1))
else
  R7="$TMP/r7"; R7_HOOKS="$R7/kits/hooks"; mkdir -p "$R7/.governance" "$R7_HOOKS" "$R7/kits/policy" "$R7/.claude"
  cp "$HERE/agent-cap.js" "$HERE/scratch-guard.js" "$R7_HOOKS/"
  for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do cp "$ROOTDIR/$LIMPK/$f" "$R7/kits/policy/"; done
  printf '[runtime]\nagents-in-flight = 2\n' > "$R7/.governance/policy.toml"
  ( cd "$R7" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
      && git config user.name t && git add -A && git commit -qm limit --no-verify )
  R7_WF='{"tool_name":"Workflow","cwd":"'"$NODEDIR/r7"'","tool_input":{"script":"const r = await agent(1)"}}'
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"3","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"3"}}\n' > "$R7/.claude/settings.json"
  run_limit_call "rule7: settings at 3 over a landed limit of 2 -> deny, naming the variable" 2 "$R7_WF" "$R7_HOOKS/agent-cap.js" 'CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS'
  run_limit_call "rule7: ...and naming the render" 2 "$R7_WF" "$R7_HOOKS/agent-cap.js" 'policy.py settings --write'
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R7/.claude/settings.json"
  run_limit_call "rule7: settings at the limit -> allow (control)" 0 "$R7_WF" "$R7_HOOKS/agent-cap.js"
  # TOOL-dGroundRules-61: a settings file GOV_SETTINGS_JSON declares outside the checkout is one more
  # layer, never the project file's replacement, and every layer that sets a variable holds the limit.
  R7D="$TMP/r7-declared.json"; R7DN="$NODEDIR/r7-declared.json"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R7D"
  printf '{"env":{"CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"3"}}\n' > "$R7/.claude/settings.json"
  GOV_SETTINGS_JSON="$R7DN" run_limit_call "rule7: declared at 2, the project file at 3 -> deny, naming the project file" 2 "$R7_WF" "$R7_HOOKS/agent-cap.js" '.claude/settings.json: env.CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS is 3'
  rm -f "$R7/.claude/settings.json"
  GOV_SETTINGS_JSON="$R7DN" run_limit_call "rule7: declared only, at 2 -> allow" 0 "$R7_WF" "$R7_HOOKS/agent-cap.js"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R7/.claude/settings.json"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"3","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"3"}}\n' > "$R7D"
  GOV_SETTINGS_JSON="$R7DN" run_limit_call "rule7: declared at 3, the project file at 2 -> deny, naming the declared file" 2 "$R7_WF" "$R7_HOOKS/agent-cap.js" 'r7-declared.json: env.CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS is 3'
fi
# TOOL-dGroundRules-18 — rule 2 judges a `gov:fixed-writers` split against the agent limit and a
# `gov:fixed-verifiers` split against MAX_VERIFIERS whatever the limit. The copy sits beside a STUB
# policy-mirror.js answering the limit, which arms rule 7, so the arms run in a scratch checkout whose
# settings hold both variables at 4, at or under each stub limit below (TOOL-dGroundRules-68): rule 7
# admits, rule 6 finds no role index there, and each arm judges rule 2. With no stub, rule 7 adds no
# rule.
WS="$TMP/writer-split"; WS_HOOKS="$WS/hooks" WS_POLICY="$WS/policy"; mkdir -p "$WS_HOOKS" "$WS_POLICY" "$WS/.claude"; cp "$HERE/agent-cap.js" "$HERE/scratch-guard.js" "$WS_HOOKS/"
printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"4","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"4"}}\n' > "$WS/.claude/settings.json"
( unset GIT_DIR GIT_WORK_TREE; cd "$WS" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
    && git config user.name t && git add -A && git commit -qm writer-split --no-verify )
write_limit_stub() { # limit
  printf 'class PolicyRefusal extends Error {}\nmodule.exports = { PolicyRefusal, readPolicy: () => ({ value: %s, source: "stub", reason: "stub" }) }\n' "$1" > "$WS_POLICY/policy-mirror.js"
}
WS_WRITER='{"tool_name":"Workflow","cwd":"'"$NODEDIR/writer-split"'","tool_input":{"script":"const SPEC_WRITERS = 6\nconst g = chunk(s, Math.ceil(s.length / SPEC_WRITERS)) // gov:fixed-writers\nconst r = await boundedParallel(g.map((x) => () => agent(x)), SPEC_WRITERS)"}}'
WS_VERIFIER='{"tool_name":"Workflow","cwd":"'"$NODEDIR/writer-split"'","tool_input":{"script":"const K = 6\nconst g = chunk(all, Math.ceil(all.length / K)) // gov:fixed-verifiers\nconst r = await boundedParallel(g.map((x) => () => agent(x)), 5)"}}'
write_limit_stub 4
run_limit_call "writer split: K 6 above a stub limit of 4 -> deny, naming the marker" 2 "$WS_WRITER" "$WS_HOOKS/agent-cap.js" 'gov:fixed-writers but its bounded split'
run_limit_call "writer split: ...and the K it read against that limit" 2 "$WS_WRITER" "$WS_HOOKS/agent-cap.js" 'resolves to 6, above the bound 4: runtime.agents-in-flight'
write_limit_stub 6
run_limit_call "writer split: K 6 at a stub limit of 6 -> allow (control)" 0 "$WS_WRITER" "$WS_HOOKS/agent-cap.js"
run_limit_call "verifier split: K 6 under a stub limit of 6 -> deny, against MAX_VERIFIERS" 2 "$WS_VERIFIER" "$WS_HOOKS/agent-cap.js" 'above the bound 5: MAX_VERIFIERS'
rm -f "$WS_POLICY/policy-mirror.js"
run_limit_call "writer split: no policy kit beside the hooks kit -> deny, against MAX_VERIFIERS" 2 "$WS_WRITER" "$WS_HOOKS/agent-cap.js" 'above the bound 5: MAX_VERIFIERS, as no policy kit'

# ---- the two copies ------------------------------------------------------------------------------
# `.claude/hooks/agent-cap.js` is the WIRED copy and `<prefix>/hooks/agent-cap.js` is the kit's. Nothing
# gated them: check-wiring.sh asserts the hook is wired, never that the wired one is this one. A
# stale wired copy enforces yesterday's rules while the kit documents today's.
# The arm used to sit inside `if BOTH files exist`, so a DELETED wired copy satisfied it by absence —
# the parity assertion's own failure mode. Inside the governance repo the pair is REQUIRED; in an
# adopting tree with no <prefix>/hooks/ the arm skips loudly instead of vanishing.
# The kit copy is LOCATED, never assumed at one prefix. Gating on the literal `<prefix>/hooks/` made
# this arm disarm itself in every tree that installs the kit anywhere else: measured in a scratch
# repo with the kit at `<root>/hooks/` and NO wired copy at all, this file reported "39 passed, 0
# failed", exit 0. A stale wired hook enforcing yesterday's fan-out rules was undetectable there.
# Finding nothing is still a legitimate skip — an adopting tree need not carry the kit — but finding
# the kit and then not checking it is not.
ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
KITJS=""
if [ -n "$ROOT" ]; then
  for c in "$ROOT/$KIT_REL/agent-cap.js" "$ROOT/${KIT_REL##*/}/agent-cap.js"; do
    [ -f "$c" ] && { KITJS="$c"; break; }
  done
  # Last resort: ask git where it is, so a prefix nobody listed still arms the arm.
  if [ -z "$KITJS" ]; then
    # The two globs sit in variables so the marked line carries no line continuation: a trailing
    # backslash would escape the space before a comment rather than the newline, and the resulting
    # break is valid shell that silently drops the rest of the command.
    _g_prefixed="*/${KIT_REL##*/}/agent-cap.js"
    _g_root="${ROOTPFX}${KIT_REL##*/}/agent-cap.js"   # a root install is half of what this searches
    rel=$(git -C "$ROOT" ls-files -- "$_g_prefixed" "$_g_root" 2>/dev/null \
          | grep -v '^\.claude/' | head -1)
    [ -n "$rel" ] && KITJS="$ROOT/$rel"
  fi
fi
# SELF-ARMING ON THE RESOLVED COPY COUNT — TOOL-dRetiredFork-14.
# This arm asserted TWO copies and hard-FAILED when the second was absent. That became the CORRECT
# state the moment the kit stopped shipping a second destination, so the arm failed on the shipped
# layout: not a parity check any more, just a stale assumption with a test around it.
#
# It now grades the population it actually finds:
#   0 copies  -> REFUSE. A parity arm with no subject proves nothing, and saying "skip" there is the
#                green-by-absence shape this repo has a catalogue entry for.
#   1 copy    -> the single-copy layout. There is nothing to drift FROM, and that is a pass.
#   2 or more -> the historical dual-ship. Every extra copy must match the kit copy byte for byte.
if [ -n "$KITJS" ]; then
  ac_extra=""
  for ac_c in "$ROOT/.claude/hooks/agent-cap.js"; do
    [ -f "$ac_c" ] && ac_extra="$ac_extra $ac_c"
  done
  ac_n=$(printf '%s' "$ac_extra" | wc -w | tr -d ' ')
  if [ "$ac_n" = 0 ]; then
    echo "ok   single-copy layout: ${KITJS#"$ROOT/"} is the only tracked copy, so there is nothing to drift from"
    pass=$((pass+1))
  else
    ac_drift=0
    for ac_c in $ac_extra; do
      if ! diff -q <(sed 's/\r$//' "$ac_c") <(sed 's/\r$//' "$KITJS") >/dev/null; then
        echo "FAIL ${ac_c#"$ROOT/"} has drifted from ${KITJS#"$ROOT/"}"
        echo "     fix: cp ${KITJS#"$ROOT/"} ${ac_c#"$ROOT/"}"
        ac_drift=1
      fi
    done
    if [ "$ac_drift" = 0 ]; then
      echo "ok   all $((ac_n+1)) tracked copies of agent-cap.js agree"; pass=$((pass+1))
    else
      fail=$((fail+1))
    fi
  fi
else
  echo "FAIL the parity arm found NO copy of agent-cap.js anywhere (looked for ${PFX}hooks/, hooks/, then any */hooks/ outside .claude/) — an arm with no subject cannot pass"
  fail=$((fail+1))
fi


# ---- rule 2: LENS PROSE IS NOT CODE (TOOL-aLexedStripper-2) --------------------------------------
# Every arm below is the SAME correct five-element lens array, fanned through the sanctioned helper.
# Only the English inside one prompt differs, and every one of them must ADMIT.
#
# THE PROVENANCE: five of these spellings DENIED against `agent-cap` 1.8, measured across both array
# shapes before the fix was wired — a literal `...` read as a spread by the array-literal guard, and
# an unmatched `[`, `]`, `)` or `}` read as bracket structure by the join-forward walk or by
# `topLevelArgs`. An adopter hit this and filed it as a gov ask; their diagnosis blamed apostrophes
# and prescribed U+2019, and both of those admit at 1.8 — which is why the apostrophe and U+2019 rows
# are here too, as the negative result.
#
# The ADMIT direction is the whole point of this group. A fixture set that only ever asserts denials
# cannot catch a guard that has become a blanket.

js "rule2 prose: a literal ... in a prompt is not a spread" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows ... then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched [ in a prompt is not an array" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows [see the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched ] in a prompt does not close the array" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows], then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched ) in a prompt does not shift the depth" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows), then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched } in a prompt does not close the element" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows}, then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: apostrophes and an em dash, the adopter's stale diagnosis" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `check S2's rows and the table's keys — then stop` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: SIX lenses still deny, whatever the prose" 2 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `list the rows ... then the table` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
  { key: "f", prompt: `six` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# ---- rule 2: an interpolation holds CODE, and both directions are checked ------------------------
# `blankLiterals` blanks `${…}` bodies. Rule 2 may not, or an `agent(` written inside one becomes
# invisible to the only rule that bounds it. The multi-line shape is the one a per-line span view
# cannot reach: its `}` is not on its opening line.

js "rule2 interp: an unbounded fan inside a single-line interpolation denies" 2 <<'EOF'
const all = args.everything
const r = `x: ${await Promise.all(all.map((f) => agent(f.p)))}`
return r
EOF

js "rule2 interp: an unbounded fan inside a MULTI-line interpolation denies" 2 <<'EOF'
const all = args.everything
const report = `results: ${await Promise.all(
  all.map((f) => agent(f.prompt))
)}`
return report
EOF

js "rule2 interp: a BOUNDED fan inside an interpolation still admits" 0 <<'EOF'
const L = [{a:1},{a:2},{a:3},{a:4},{a:5}]
const r = `res: ${await boundedParallel(L.map((x) => () => agent(x)), 5)}`
return r
EOF

# ---- rule 2: template-literal edges (TOOL-aLexedStripper-2 S2, TOOL-aLexedStripper-5) ------------
# A nested template must BALANCE, or the fallback path fires on a legal script. A backtick that this
# file cannot model — inside a regex literal, a string, or a comment — must not change a verdict:
# the fallback returns the pre-change view, so these are the shipped hook's own answers.

js "rule2 edges: a nested template balances and admits" 0 <<'EOF'
const n = `a${`b`}c`
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a regex literal admits a legal harness" 0 <<'EOF'
const re = /`/
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick in a regex character class admits" 0 <<'EOF'
const re = /[`~]/g
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a quoted string admits" 0 <<'EOF'
const s = "a ` b"
const t = 'c ` d'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a comment admits" 0 <<'EOF'
// a stray ` in a line comment
/* and one ` in a block comment */
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# THE FAIL-OPEN THIS GROUP EXISTS FOR. An unterminated template literal blanks everything below it
# under a naive template-aware view, hiding the fan entirely. The fallback denies it because the
# shipped hook denies it — which is the property, not a coincidence.
js "rule2 edges: an unbounded fan below an unterminated backtick still denies" 2 <<'EOF'
const stray = `an unterminated template literal
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF


# The same class in the OTHER field-count regime. A stray `)` drives topLevelArgs' depth negative and
# every comma AFTER it then counts at top level, so denial depends on how many commas follow -- i.e.
# on how many fields each element has. A one-field array is denied only when the prose sits in the
# LAST element; a two-field one is denied wherever it sits. Both regimes are here because a fixture
# in one of them measures the other wrongly, which is how two independent grids disagreed on `)`.
js "rule2 prose: one-field element, stray ) in the LAST element" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { prompt: `one` },
  { prompt: `two` },
  { prompt: `three` },
  { prompt: `four` },
  { prompt: `list the rows), then the table` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# The other end of the same rule: a `)` with no comma after it inside its element was ALWAYS harmless,
# so this arm admits at BASE too. It is here to pin the boundary, not the fix -- without it the group
# only ever asserts the denying side and cannot notice the guard becoming a blanket.
js "rule2 prose: a stray ) at the very end of the prose was never a denial" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `the rows, then the table)` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF


# ---- renderCodeView: the FAIL-OPEN arms (TOOL-aLexedStripper-5) ----------------------------------
# Every arm here is a script the SHIPPED hook denies, and each one was ADMITTED by some revision of
# renderCodeView before it reached this file. They exist because two closing-review rounds found a
# fail-open in this view and the first repair was measured insufficient for the second shape. A view
# that blanks anything can hide a fan-out; these are the shapes that proved it.

js "renderCodeView: an unbounded fan below an unterminated block-comment opener denies" 2 <<'EOF'
const x = 1 /* never closed
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF

js "renderCodeView: a regex-borne /* closed by a later ordinary */ denies" 2 <<'EOF'
const re = /\/*/
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
const d = a */ b
EOF

# The apostrophe inside a regex literal. The view used to run to end of line and synthesize a closer
# the source never had, taking the fan on that line with it.
js "renderCodeView: an apostrophe in a regex does not swallow the fan on its line" 2 <<'EOF'
const all = args.everything
if (/won't/.test(args.s)) await Promise.all(all.map((f) => agent(f.prompt)))
EOF

js "renderCodeView: the same line without the apostrophe denies too (control)" 2 <<'EOF'
const all = args.everything
if (/wont/.test(args.s)) await Promise.all(all.map((f) => agent(f.prompt)))
EOF

js "renderCodeView: an unpaired double quote does not swallow the fan on its line" 2 <<'EOF'
const all = args.everything
if (x === 5") await Promise.all(all.map((f) => agent(f.prompt)))
EOF



# ---- TOOL-dMispairedQuote-1: a quote pairs with the WRONG partner ---------------------------------
# Every arm below was staged RED against the tip before it landed. The defect: each of this file's
# string views pairs a quote with the next quote of the same kind on the line, so an apostrophe in
# prose earlier on that line pairs with the quote opening `agent('a'` and the span blanked between
# them carries the fan-out. `addc6169` already demanded a matching PAIR; a pair exists, and it is the
# wrong one. The construct holding the apostrophe is not the mechanism -- these arms carry a regex, a
# double-quoted string, a block comment and a template literal, and the shipped hook admitted all
# four. The CONTROL beside each is the same line with the apostrophe removed.

# Rule 1's seven arms here, a raw `parallel` beside a prose apostrophe, retired with that rule in TOOL-dGroundRules-10
# (TOOL-dGroundRules-10); the defect they pinned is a view's, and rule 2's and rule 5's arms keep it.
js "mispaired quote: rule 2 counter loses the agent( -> deny" 2 <<'EOF'
const re = /won't/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)
EOF

js "mispaired quote: rule 2 control, no apostrophe -> deny" 2 <<'EOF'
const re = /wont/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)
EOF

# Rule 5, the ref-keyed-join ban, is defeated by the same apostrophe and nobody had named it. Both
# of these ADMIT at the tip and deny after.
js "mispaired quote: rule 5 join hidden by an apostrophe -> deny" 2 <<'EOF'
const re = /won't/; m.get(f.ref); const s = 'x'
EOF

js "mispaired quote: rule 5 verdictByRef hidden by an apostrophe -> deny" 2 <<'EOF'
const re = /won't/; const verdictByRef = {}; const s = 'x'
EOF

js "mispaired quote: rule 5 control, no apostrophe -> deny" 2 <<'EOF'
const re = /wont/; m.get(f.ref); const s = 'x'
EOF

# ---- and the ADMIT direction, which is half the class -------------------------------------------
# A fixture group that only ever asserts denials cannot catch a fail-closed that has become a
# fail-open. Each of these passes at the tip and must keep passing.

js "mispaired quote: aLexedStripper-5's own fixture stays legal -> allow" 0 <<'EOF'
const SEP = /[`]/
const all = ['a','b']
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF

# ---- TOOL-dMispairedQuote-3: no denial may be LOST ------------------------------------------------
# Correcting what counts as a string literal does not only un-hide fan-outs; it un-hides every other
# character the old mispairing was blanking, and rules 2, 3 and 5 walk brackets and balance parens
# ACROSS lines. Three DENY-to-ADMIT moves were reproduced against unit 1 alone. Each has a fixture
# here, and each was ALSO closed by the property arm below -- which is what makes the property worth
# its bytes: the next repair to these views inherits it without knowing these three shapes.

# Its four fixtures here hit rule 3 (a width of 50) and rule 1 (a raw primitive), which retired in TOOL-dGroundRules-10
# (TOOL-dGroundRules-10); three of them stay in the property's population below as expected losses.

# ---- TOOL-aRepatriatedFork-7 S3: the NESTED-INTERPOLATION matrix ---------------------------------
# A nested `${` zeroed the ONE depth counter the lexed view kept, so a brace open around an inner
# template -- an object literal, a block, an arrow body -- closed the OUTER interpolation at its own
# `}` and every fan-out after it left the view. a7c78ad2 admitted four of these five nested forms at
# exit 0 through the sanctioned helper, where the raw-text rule has no reason to fire. `depth-two`
# opens no brace and is the class's control. Every nested form and its flat control must be denied
# BY THE VERIFY-STAGE RULE, asserted on its text: an exit code alone cannot tell rules apart. The
# files also join the S9 property population below (F3), so no BASE denial among them can be lost.
mkdir -p "$TMP/nest"
NEST_HELPER='async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}'
NEST_FAN='await boundedParallel(findings.map((g) => () => agent(g)), 5)'
write_nest_pair() { # name nested-script flat-script, FAN standing for the unbounded verify stage
  printf '%s\n%s\n' "$NEST_HELPER" "${2//FAN/$NEST_FAN}" > "$TMP/nest/$1.js"
  printf '%s\n%s\n' "$NEST_HELPER" "${3//FAN/$NEST_FAN}" > "$TMP/nest/$1-flat.js"
}
write_nest_pair depth-two 'const s = `a ${ `b ${ x } c` + FAN } d`' 'const s = `a ${ 1 + FAN } d`'
write_nest_pair depth-three 'const s = `a ${ f({ k: `b ${ g({ m: `c ${ y } d` }) } e` }) + FAN } z`' 'const s = `a ${ f({ k: 1 }) + FAN } z`'
write_nest_pair object-before-inner 'const s = `a ${ f({ k: `b ${ x } c` }) + FAN } d`' 'const s = `a ${ f({ k: 1 }) + FAN } d`'
write_nest_pair arrow-body 'const s = `a ${ [1].map((v) => { return `b ${ v } c` }).join("") + FAN } d`' 'const s = `a ${ [1].map((v) => { return v }).join("") + FAN } d`'
write_nest_pair multi-line 'const s = `a ${ f({ k: `b ${ x } c` })
  + FAN
} d`' 'const s = `a ${ f({ k: 1 })
  + FAN
} d`'
nest_n=0
for f in "$TMP"/nest/*.js; do
  [ -f "$f" ] || continue
  nest_n=$((nest_n+1))
  n=$(basename "$f" .js)
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":open(sys.argv[1],encoding="utf-8").read()}}))' "$f")
  printf '%s' "$payload" | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; rc=$?
  if [ "$rc" = 2 ] && grep -qF 'spawns one agent per item' "$TMP/err"; then
    echo "ok   nesting matrix: $n -> denied by the verify-stage rule"; pass=$((pass+1))
  else
    echo "FAIL nesting matrix: $n exited $rc without the verify-stage denial"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
done
if [ "$nest_n" = 10 ]; then
  echo "ok   nesting matrix: all 10 fixtures were written and judged"; pass=$((pass+1))
else
  echo "FAIL nesting matrix: $nest_n fixture(s) judged, want 10 -- a matrix that judged fewer certifies shapes it never saw"; fail=$((fail+1))
fi

# ---- S10: `verbatim` is CHECKED, not asserted ----------------------------------------------------
# The three renderShipped* bodies must equal their counterparts in the BASE blob. Only the name line
# differs. A tree where that blob does not resolve -- every adopter -- gets an announced SKIP.
GOV_BASE_SHA=${GOV_BASE_SHA:-d65da7ab}
# DERIVED, never spelled: a `<prefix>/hooks/` literal is gov's own install prefix and resolves to
# nothing in a target that installed this kit elsewhere, which is what the shipped-surface ratchet
# refuses. `git ls-files --full-name` answers where THIS hook actually lives in THIS tree.
HOOKREL=$(git -C "$HERE" ls-files --full-name -- "$KIT_HOOK" 2>/dev/null | head -1)
if [ -n "$HOOKREL" ] && git -C "$HERE" show "$GOV_BASE_SHA:$HOOKREL" > "$TMP/base-hook.js" 2>/dev/null; then
  cat > "$TMP/byte.py" <<'PYEOF'
import sys, pathlib
base = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n")
cur = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").replace("\r\n", "\n")
PAIRS = [("function stripStrings(line) {", "function renderShippedLine(line) {"),
         ("function renderCodeView(script) {", "function renderShippedView(script) {"),
         ("function blankLiterals(script) {", "function renderShippedBlanks(script) {")]
def block(text, header):
    ls = text.split("\n")
    s = ls.index(header)
    e = s
    while ls[e] != "}":
        e += 1
    return "\n".join(ls[s + 1:e + 1])
bad = 0
for b, c in PAIRS:
    try:
        if block(base, b) != block(cur, c):
            print("DRIFT %s is not the BASE bytes of %s" % (c, b)); bad += 1
    except ValueError as e:
        print("MISSING %s or %s (%s)" % (b, c, e)); bad += 1
print("bodies-compared 3 drifted %d" % bad)
sys.exit(1 if bad else 0)
PYEOF
  "$TESTPY" "$TMP/byte.py" "$TMP/base-hook.js" "$HOOK" > "$TMP/byte.out" 2>&1
  if [ $? = 0 ]; then
    echo "ok   no-regress: the three renderShipped* bodies are the BASE bytes"; pass=$((pass+1))
  else
    echo "FAIL no-regress: a renderShipped* body has drifted from BASE"; sed 's/^/     /' "$TMP/byte.out"; fail=$((fail+1))
  fi
else
  echo "skip no-regress byte arm — $GOV_BASE_SHA:${HOOKREL:-<this hook is not tracked here>} does not resolve in this tree, so there is nothing to compare the frozen bodies against"
fi

# ---- S9: THE PROPERTY. No script this hook denied at BASE may be admitted now. --------------------
# The population is every tracked file PLUS the fixtures below. The second half is not padding:
# unit 1 alone flips ZERO tracked files, because every reproduced shape is synthetic. A property arm
# whose population holds no instance of the class it guards can only ever pass.
if [ -s "$TMP/base-hook.js" ]; then
  mkdir -p "$TMP/nrfix"
  # TOOL-dGroundRules-10: `backtick-in-regex.js` and `exposed-backtick.js` (rule 3, a width of 50) and
  # `template-borne-comment.js` (rule 1) are denied at BASE by rules TOOL-dGroundRules-10 retired, so each prints a
  # `RETIRED rule <n>` line and is never counted as lost.
  # TOOL-dFoldedVerdict-4 S7. The FIRST is the ratified path: BASE denies it, this hook admits it, and
  # deleting the marker restores the denial — which is what makes the loss marker-attributed rather
  # than merely tolerated. The SECOND is the control: an unmarked braceless loop that BOTH hooks deny,
  # so the affordance is proven scoped to the marker and not to loops in general.
  cat > "$TMP/nrfix/seq-marked-bounded.js" <<'EOF'
const MAX = 5
const units = [1, 2, 3, 4, 5]
const out = []
for (const u of units) { // gov:sequential-agents(MAX)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
  cat > "$TMP/nrfix/seq-unmarked-braceless.js" <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) out.push(await agent('do ' + u, { label: 'u' }))
EOF
  cat > "$TMP/nrfix/backtick-in-regex.js" <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /it's`don't/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF
  cat > "$TMP/nrfix/exposed-backtick.js" <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /a'b`c/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF
  cat > "$TMP/nrfix/template-borne-comment.js" <<'EOF'
const p = `see 'http://x' now`; await parallel(all.map(f))
EOF
  # TOOL-aRepatriatedFork-7 F3: the nesting matrix joins the population, so no fixture of it that BASE
  # denied -- every flat control, and `depth-two` -- may be admitted now.
  cp "$TMP"/nest/*.js "$TMP/nrfix/" 2>/dev/null || true
  # ONE NODE FOR THE WHOLE PROPERTY (TOOL-aSparedSpawn-11 S1, owner ruling F1 (a)). The loop below
  # used to be Python starting `node` per population file and per hook, about 3700 processes and
  # most of this suite's wall clock. The runner compiles each hook ONCE as a `vm.Script` and runs every
  # payload in a FRESH context with the hook's own CommonJS arguments: the real `require`, except that
  # `fs.readFileSync(0)` returns the payload; a `process` whose `exit` records the FIRST code and
  # throws a sentinel; and an `argv` naming the hook as `node <hook>` would. An uncaught throw is 1,
  # as real node exits, and a return with no exit is 0. The cwd and environment are this shell's, as
  # the Python loop's were. What it reads is unchanged: every `git ls-files` path split on
  # whitespace, plus the fixtures; each body decoded as UTF-8 with universal newlines, as Python's
  # `read_text` did; admission is `exit != 2`; the ratification re-run strips every marker token;
  # zero denials or zero ratifications red. The parity arm after it is the guard against the one
  # risk this buys: an in-process verdict that real node would not give.
  cat > "$TMP/nr.js" <<'JSEOF'
'use strict'
const fs = require('fs')
const path = require('path')
const vm = require('vm')
const Module = require('module')
const cp = require('child_process')
const [mode, baseHook, curHook, root, fixdir, strideArg] = process.argv.slice(2)
const BOUND_MS = 120000
const STOP = { stop: 'process.exit' }
// The rules TOOL-dGroundRules-10 retired, by the opening text of their BASE denial.
const RETIRED = [[1, 'raw parallel()/pipeline()'], [3, 'a bound is written here that this file cannot resolve']]

function loadHook(file) {
  const abs = path.resolve(file)
  // A hashbang is legal only at the very start of a script, and the wrapper below is not the start.
  // Blanking the line keeps every line number the hook's own.
  const src = fs.readFileSync(abs, 'utf8').replace(/^#!.*/, '')
  const wrapped = '(function (exports, require, module, __filename, __dirname, process, console) {' + src +
    '\n}).apply(__nrArgs[0], __nrArgs)'
  return { abs, script: new vm.Script(wrapped, { filename: abs }), req: Module.createRequire(abs) }
}

function runInProcess(hook, payload, flags = []) {
  let code = null
  let err = ''
  // Both views proxy an EMPTY target and read the real object inside the trap, so no proxy invariant
  // ties a returned value to a non-configurable property of the real `fs` or `process`.
  const fsView = new Proxy({}, {
    get: (_t, k) => (k === 'readFileSync'
      ? (fd, ...rest) => (fd === 0 ? payload : fs.readFileSync(fd, ...rest))
      : fs[k]),
    has: (_t, k) => k in fs,
  })
  const req = (id) => (id === 'fs' || id === 'node:fs' ? fsView : hook.req(id))
  const sink = { write: () => true }
  // STDERR IS RECORDED (TOOL-dGroundRules-10): a BASE denial is named by its opening text.
  const errSink = { write: (t) => { err += String(t); return true } }
  const proc = new Proxy({}, {
    get: (_t, k) => {
      if (k === 'exit') return (c) => { if (code === null) code = c === undefined ? 0 : c; throw STOP }
      if (k === 'argv') return [process.execPath, hook.abs, ...flags]
      if (k === 'stdout') return sink
      if (k === 'stderr') return errSink
      const v = process[k]
      return typeof v === 'function' ? v.bind(process) : v
    },
    has: (_t, k) => k in process,
  })
  const quiet = { log() {}, error() {}, warn() {}, info() {}, debug() {} }
  const mod = { exports: {} }
  const ctx = vm.createContext({ __nrArgs: [mod.exports, req, mod, hook.abs, path.dirname(hook.abs), proc, quiet] })
  try {
    hook.script.runInContext(ctx, { timeout: BOUND_MS })
  } catch (e) {
    if (e !== STOP && code === null) {
      if (e && e.code === 'ERR_SCRIPT_EXECUTION_TIMEOUT') throw new Error('TIMEOUT after ' + BOUND_MS + ' ms')
      code = 1
    }
  }
  return { code: code === null ? 0 : code, err }
}

function runSpawned(hook, payload) {
  const r = cp.spawnSync(process.execPath, [hook.abs], { input: payload, timeout: BOUND_MS, stdio: ['pipe', 'ignore', 'ignore'] })
  return r.status === null ? 'killed' : r.status
}

function readBody(p) {
  try {
    return fs.readFileSync(p, 'utf8').replace(/\r\n?/g, '\n')
  } catch {
    return null
  }
}

// THE PAYLOAD CWD IS THE FIXTURE DIR, which no checkout holds (TOOL-aSweptBar-1 S3). With no `cwd` the
// hook falls back to this checkout, whose `.claude/roles.json` arms rule 6 against every inline script,
// so every BASE denial read as a rule 6 denial and nothing was ratified. Under no checkout rule 6 stays
// unarmed, and so does rule 7 (TOOL-dGroundRules-10), and the property compares the script rules with
// BASE, which predates both.
function buildPayload(body) {
  return JSON.stringify({ tool_name: 'Workflow', cwd: path.resolve(fixdir), tool_input: { script: body } })
}

const tracked = cp.execFileSync('git', ['-C', root, 'ls-files'], { encoding: 'utf8', maxBuffer: 1 << 28 })
  .split(/\s+/).filter(Boolean).map((f) => path.join(path.resolve(root), f))
const fixtures = fs.readdirSync(fixdir).filter((f) => f.endsWith('.js')).sort().map((f) => path.join(fixdir, f))
const base = loadHook(baseHook)
const cur = loadHook(curHook)

try {
  if (mode === 'property') {
    const lost = []
    const ratified = []
    const retired = []
    let denied = 0
    let n = 0
    for (const p of tracked.concat(fixtures)) {
      const body = readBody(p)
      if (body === null) continue
      const payload = buildPayload(body)
      const a = runInProcess(base, payload)
      n += 1
      if (a.code !== 2) continue
      denied += 1
      const b = runInProcess(cur, payload).code
      // ADMISSION IS `exit != 2`, not `exit == 0`: the hook BLOCKS only on 2, so a crash is an admission too.
      if (b !== 2) {
        // AN EXPECTED LOSS (TOOL-dGroundRules-10): BASE denied it by a rule this unit retired, named by the
        // denial's opening text. BASE runs rule 2 before both, so that text means rule 2 admitted it
        // there, and BASE under `--only=join` must admit it too, so a rule-5 denial is never hidden
        // behind a retired one. Never counted as lost.
        const rule = RETIRED.find(([, text]) => a.err.startsWith('BLOCKED by agent-cap: ' + text))
        if (rule && runInProcess(base, payload, ['--only=join']).code !== 2) {
          retired.push('RETIRED rule ' + rule[0] + ': ' + p)
          continue
        }
        // CLASS-SCOPED RATIFICATION (TOOL-dFoldedVerdict-4): denial restored by stripping every marker
        // token means the marker bought the loss; anything else is a regression.
        const r = runInProcess(cur, buildPayload(body.split('gov:sequential-agents').join(''))).code
        if (r === 2) ratified.push(p + ' (exit ' + b + ', denial restored by removing the marker)')
        else lost.push(p + ' (exit ' + b + ')')
      }
    }
    for (const f of retired) console.log(f)
    for (const f of lost) console.log('LOST a denial: ' + f)
    for (const f of ratified) console.log('RATIFIED a marker-attributed loss: ' + f)
    console.log('population ' + n + ' scanned, ' + denied + ' denied at BASE, ' + lost.length +
      ' denial(s) lost, ' + ratified.length + ' ratified, ' + retired.length + ' retired-rule loss(es) excluded')
    process.exitCode = lost.length || denied === 0 || ratified.length === 0 ? 1 : 0
  } else if (mode === 'parity') {
    // ponytail: a fixed stride over the sorted tracked list keeps the sample a handful of spawns; a
    // narrower stride buys coverage at about a second per spawn on a Windows node.
    const stride = Number(strideArg)
    const sample = fixtures.slice()
    const sorted = tracked.slice().sort()
    for (let i = 0; i < sorted.length; i += stride) sample.push(sorted[i])
    const bad = []
    let compared = 0
    let denies = 0
    for (const p of sample) {
      const body = readBody(p)
      if (body === null) continue
      const payload = buildPayload(body)
      for (const [name, hook] of [['BASE', base], ['current', cur]]) {
        const inProc = runInProcess(hook, payload).code
        const real = runSpawned(hook, payload)
        compared += 1
        if (real === 2) denies += 1
        if (inProc !== real) bad.push(name + ' hook on ' + p + ': in-process exit ' + inProc + ', node exit ' + real)
      }
    }
    for (const b of bad) console.log('DISAGREE ' + b)
    console.log('parity ' + compared + ' verdict(s) compared over ' + sample.length + ' payload(s), ' +
      denies + ' deny verdict(s) from real node, ' + bad.length + ' disagreement(s)')
    process.exitCode = bad.length || denies === 0 ? 1 : 0
  } else {
    console.log('nr.js: unknown mode ' + mode)
    process.exitCode = 2
  }
} catch (e) {
  console.log('nr.js: ' + (e && e.message ? e.message : String(e)))
  process.exitCode = 1
}
JSEOF
  node "$TMP/nr.js" property "$TMP/base-hook.js" "$HOOK" "$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)" "$TMP/nrfix" > "$TMP/nr.out" 2>&1
  if [ $? = 0 ]; then
    echo "ok   no-regress: no denial lost against BASE ($(tail -1 "$TMP/nr.out"))"; pass=$((pass+1))
  else
    echo "FAIL no-regress: a denial the BASE hook made is gone"; sed 's/^/     /' "$TMP/nr.out"; fail=$((fail+1))
  fi
  # S2 — PARITY: every fixture above plus every 400th tracked path, through the in-process runner AND
  # through a real `node` per hook. Any disagreement reds naming the payload, and so does a sample in
  # which real node denied nothing, since a parity over admissions alone cannot see an exit stub that
  # drops its code.
  node "$TMP/nr.js" parity "$TMP/base-hook.js" "$HOOK" "$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)" "$TMP/nrfix" 400 > "$TMP/nrp.out" 2>&1
  if [ $? = 0 ]; then
    echo "ok   no-regress parity: the in-process runner agrees with real node ($(tail -1 "$TMP/nrp.out"))"; pass=$((pass+1))
  else
    echo "FAIL no-regress parity: the in-process runner and real node disagree"; sed 's/^/     /' "$TMP/nrp.out"; fail=$((fail+1))
  fi
else
  echo "skip no-regress property arm — the BASE blob does not resolve in this tree, so there is no shipped hook to compare verdicts against"
fi


# ---- closing-review folds: a guard that times out, or crashes, does not guard --------------------
# A PreToolUse hook is NON-BLOCKING when it times out AND when it exits 1. Both were reachable.

# F1. `checkLiteralOpen` copied the whole line prefix per quote, so cost was quadratic in LINE
# length and every ordinary `return 'x'` paid it. Measured before the fix: 253 KB on one line took
# 33.8 s against 62 ms at BASE. This arm is a RATIO against a CONTROL, never a typed ceiling
# (TOOL-aSparedSpawn-15 S1): the same 8000 literals ONE PER LINE are timed first, in this process,
# and the one-line run may take at most four times that plus 2 s, both read from EPOCHREALTIME. A
# loaded host slows both runs alike, so the verdict stops being a function of the box, while a walk
# that is quadratic in LINE length grows the one-line run only. The typed 10 s it replaced redded on
# a loaded node `a`, where one spawn costs 632 to 818 ms. The absolute hook timeout is NOT this arm's
# question: a slowdown linear in both runs is not the defect it guards. Both runs must ADMIT (exit
# 0), so a hook that crashed fast on either cannot pass the ratio by doing no work. EVERY LITERAL
# FOLLOWS `void`: the walk runs only for a quote glued to an identifier, and the `f(a1, 'lit1')`
# this arm used to time put a comma there, so the restored per-quote copy never ran and the arm
# could not fail on the regression it names. Measured on node `a`: with the copy restored the
# one-line run took 19 to 23 s against 0.9 to 1.3 s one per line; shipped, 0.3 to 0.9 s both ways.
long_one=$("$TESTPY" -c "
import json
n = 8000
line = 'const x = [' + ','.join(\"f(a%d, void 'lit%d')\" % (i, i) for i in range(n)) + ']'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': line}}))
")
long_ctl=$("$TESTPY" -c "
import json
n = 8000
body = 'const x = [' + chr(10) + (',' + chr(10)).join(\"f(a%d, void 'lit%d')\" % (i, i) for i in range(n)) + chr(10) + ']'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': body}}))
")
c0=${EPOCHREALTIME//[.,]/}
printf '%s' "$long_ctl" | (cd "$TMP" && node "$HOOK") >/dev/null 2>&1; ctl_rc=$?
c1=${EPOCHREALTIME//[.,]/}
printf '%s' "$long_one" | (cd "$TMP" && node "$HOOK") >/dev/null 2>&1; one_rc=$?
c2=${EPOCHREALTIME//[.,]/}
ctl_ms=$(( (10#$c1 - 10#$c0) / 1000 )); one_ms=$(( (10#$c2 - 10#$c1) / 1000 )); lim_ms=$(( 4 * ctl_ms + 2000 ))
if [ "$ctl_rc" != 0 ] || [ "$one_rc" != 0 ]; then
  echo "FAIL quadratic ratio: the hook exited $one_rc on ONE line and $ctl_rc one per line, not 0 for both, so the timing compares runs that did not do the work"; fail=$((fail+1))
elif [ "$one_ms" -le "$lim_ms" ]; then
  echo "ok   quadratic ratio: 8000 literals on ONE line in ${one_ms} ms against ${ctl_ms} ms one per line (<= 4x + 2000 = ${lim_ms} ms)"; pass=$((pass+1))
else
  echo "FAIL quadratic ratio: 8000 literals on ONE line took ${one_ms} ms against ${ctl_ms} ms one per line (> 4x + 2000 = ${lim_ms} ms) — a walk quadratic in line length is back, and a hook that times out is NON-BLOCKING"; fail=$((fail+1))
fi

# F2. A throw in the corrected views must not become an admission. This script drives
# `parseBranches` past its recursion limit, which is PRE-EXISTING: the BASE hook exits 1 on it and
# therefore does not block. Denying is stricter than BASE and is this file's stated posture.
deep=$("$TESTPY" -c "
import json
k = ' ? args.big : '.join('c%d' % i for i in range(9000))
sc = 'const K = ' + k + ' : args.big // gov:fixed-verifiers\nawait boundedParallel(K.map((g) => () => agent(g)), 5)'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': sc}}))
")
printf '%s' "$deep" | (cd "$TMP" && node "$HOOK") >/dev/null 2>&1; deeprc=$?
if [ "$deeprc" = 2 ]; then
  echo "ok   crash posture: a script neither view can scan is DENIED, not admitted at exit 1"; pass=$((pass+1))
else
  echo "FAIL crash posture: a script neither view can scan exited $deeprc — only 2 blocks"; fail=$((fail+1))
fi


# ---- rule 6: every agent prompt is a rendered handoff (TOOL-aOrientedCast-7) ----------------------
# Armed by `.claude/roles.json` at the checkout root of the payload `cwd`. Every arm above runs with
# no index, which is the absent case; the arms below build their own checkout, whose index the
# `write_roles` calls move between the absent, broken, unarmed and armed states. Each payload stands in
# a subdirectory so the root walk is exercised. Every deny asserts its own reason, since every rule
# exits 2; every allow asserts an empty stderr.
# THE SECTION RUNS A COPY OF THE HOOK (TOOL-dGroundRules-10): its checkout is a bare `.git` directory
# with no settings, which rule 7 would refuse, so the copy sits beside scratch-guard.js and no policy
# kit, where rule 7 adds no rule. Its refusal arms are rule 6's, which decides before rule 7.
HO6="$TMP/rule6-hooks/hooks"; mkdir -p "$HO6"; cp "$HERE/agent-cap.js" "$HERE/scratch-guard.js" "$HO6/"
HOOK="$HO6/agent-cap.js"
HOREPO="$TMP/horepo"
HO_WF=workflows
mkdir -p "$HOREPO/.git" "$HOREPO/.claude" "$HOREPO/sub" "$HOREPO/tools/$HO_WF" \
  "$HOREPO/memory/builds/bx/prompts" "$HOREPO/memory/builds/bx/spec"
HOJ="$NODEDIR/horepo"
printf 'const s = await agent("one")\n' > "$HOREPO/tools/$HO_WF/h.js"
printf 'const s = await agent("one")\n' > "$HOREPO/tools/$HO_WF/other.js"
HO_ROLES='{"roles":{"gov-researcher":{"agent":true,"workflow":"research","writes":"none"},"gov-builder":{"agent":true,"workflow":"build","writes":"product"},"gov-session":{"agent":false,"workflow":"handoff","writes":"none"}},"harnesses":["tools/'"$HO_WF"'/h.js"]}'
HO_FLAG=""
HO_CWD=""
HO_PROJECT=""
write_roles() { # the index body, or `none` to remove it
  if [ "$1" = none ]; then rm -f "$HOREPO/.claude/roles.json"; else printf '%s' "$1" > "$HOREPO/.claude/roles.json"; fi
}
# The handoff files and one prompt file per variant under $TMP/ho.<variant>. The marker and digest are
# computed here as the renderer defines them; arm 6 of the roles kit's adopt-roles.test.sh, the
# agreement arm, holds the renderer itself against the hook (TOOL-aOrientedCast-15).
write_handoff() {
  "$TESTPY" -c '
import hashlib, os, sys
root, out = sys.argv[1], sys.argv[2]
h = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]
role = "## Role\n\nYou research.\n\n"
task = "## Task\n\nThis handoff is for build `bx`, unit `T-1`.\n\n### input:question\n\nWhat calls rule 4?\n"
pre = "memory/builds/bx/prompts/"
def render_marker(p, sec, r="gov-researcher", unit="T-1"):
    return "<!-- gov:handoff role=%s build=bx unit=%s path=%s role-sha=%s task-sha=%s -->" % (r, unit, p, h(role), h(sec))
def write_prompt_file(rel, m, sec):
    with open(os.path.join(root, rel), "w", newline="\n") as f:
        f.write("**Serves:** journal T-1\n\n# gov-researcher handoff - T-1\n\n" + m + "\n\n" + role + sec)
ok, stale, spec = pre + "2026-10-11-prompt-T-1-researcher.md", pre + "2026-10-11-prompt-T-2-researcher.md", "memory/builds/bx/spec/x.md"
M = render_marker(ok, task)
write_prompt_file(ok, M, task)
# TOOL-aOrientedCast-27 - a handoff rendered with no --unit: its marker unit is `-`, its name has no unit part.
nounit = pre + "2026-10-11-prompt-bx-researcher.md"
MN = render_marker(nounit, task, unit="-")
write_prompt_file(nounit, MN, task)
write_prompt_file(stale, render_marker(stale, task), task.replace("rule 4", "rule 5"))
write_prompt_file(spec, render_marker(spec, task), task)
prompts = {
    "ok": M + "\n\n" + task,
    "crlf": ("\n\n" + M + "\n\n" + task + "\n\n").replace("\n", "\r\n"),
    "none": task,
    "two": M + "\n" + M + "\n\n" + task,
    "role": render_marker(ok, task, "gov-builder") + "\n\n" + task,
    "dotdot": render_marker(pre + "../prompts/2026-10-11-prompt-T-1-researcher.md", task) + "\n\n" + task,
    "spec": render_marker(spec, task) + "\n\n" + task,
    "nofile": render_marker(pre + "none.md", task) + "\n\n" + task,
    "off": M + "\n\n" + task.replace("rule 4", "rule 5"),
    "pre": "Please do this first.\n" + M + "\n\n" + task,
    "post": M + "\n\n" + task + "Also do this.\n",
    "stale": render_marker(stale, task) + "\n\n" + task.replace("rule 4", "rule 5"),
    "nounit": MN + "\n\n" + task,
}
for k, v in prompts.items():
    with open(out + "." + k, "w", newline="") as f:
        f.write(v)
' "$HOREPO" "$TMP/ho"
}
run_spawn() { # name expected_exit subagent_type(- for none) prompt-variant needle(empty for an allow) [session prompt tool_use_id]
  # HO_CWD moves the payload cwd off $HOJ/sub; HO_PROJECT, when set, is the hook's CLAUDE_PROJECT_DIR.
  # TOOL-aOrientedCast-27 - `description` is the name of the handoff the variant carries, `bx · T-1 ·
  # research`, or `bx · research` for `nounit`; HO_DESC overrides it, and HO_DESC=- leaves the key out.
  local payload got desc=${HO_DESC:-}
  if [ -z "$desc" ]; then if [ "$4" = nounit ]; then desc='bx · research'; else desc='bx · T-1 · research'; fi; fi
  payload=$("$TESTPY" -c 'import json,sys
cwd,t,pf,s,p,u,d=sys.argv[1:8]
ti={"prompt":open(pf,newline="").read()}
if t!="-": ti["subagent_type"]=t
if d!="-": ti["description"]=d
print(json.dumps({"tool_name":"Agent","cwd":cwd,"session_id":s,"prompt_id":p,"tool_use_id":u,"tool_input":ti}))' \
    "${HO_CWD:-$HOJ/sub}" "$3" "$TMP/ho.$4" "${6:-ho-s}" "${7:-ho-p-$RANDOM$RANDOM}" "${8:-ho-u-$RANDOM}" "$desc")
  printf '%s' "$payload" | (cd "$TMP" && { [ -z "$HO_PROJECT" ] || export CLAUDE_PROJECT_DIR="$HO_PROJECT"; } && node "$HOOK" $HO_FLAG) >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" = "$2" ] && { if [ -z "$5" ]; then [ ! -s "$TMP/err" ]; else grep -qF -- "$5" "$TMP/err"; fi; }; then
    echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else
    echo "FAIL $1 (exit $got, want $2${5:+, stderr carrying '$5'})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
}
run_harness() { # name expected_exit tool_input-json needle(empty for an allow)
  local payload got
  payload=$("$TESTPY" -c 'import json,sys
print(json.dumps({"tool_name":"Workflow","cwd":sys.argv[1],"tool_input":json.loads(sys.argv[2])}))' "$HOJ/sub" "$3")
  printf '%s' "$payload" | (cd "$TMP" && node "$HOOK" $HO_FLAG) >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" = "$2" ] && { if [ -z "$4" ]; then [ ! -s "$TMP/err" ]; else grep -qF -- "$4" "$TMP/err"; fi; }; then
    echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else
    echo "FAIL $1 (exit $got, want $2${4:+, stderr carrying '$4'})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
}
write_handoff
write_roles "$HO_ROLES"
HO_H="$HOJ/tools/$HO_WF/h.js"
# AC1 — the rendered handoff is admitted; CRLF and blank ends do not move it.
run_spawn "rule6 AC1: a rendered handoff is admitted" 0 gov-researcher ok "" ho-s ho-ac1 ho-ac1-u
run_spawn "rule6 AC1: CRLF endings and blank ends are admitted" 0 gov-researcher crlf ""
# AC2 — every type that is not an agent-true role, and every malformed prompt, is refused by name.
run_spawn "rule6 AC2: general-purpose refused" 2 general-purpose ok '"general-purpose" is not an agent-true role'
run_spawn "rule6 AC2: Explore refused, naming the researcher" 2 Explore ok 'as the gov-researcher role'
run_spawn "rule6 AC2: no subagent_type refused" 2 - ok 'subagent_type null is not an agent-true role'
run_spawn "rule6 AC2: the agent-false gov-session refused" 2 gov-session ok '"gov-session" is not an agent-true role'
run_spawn "rule6 AC2: a type refusal lists gov-researcher" 2 general-purpose ok 'gov-builder, gov-researcher'
run_spawn "rule6 AC2: a type refusal names the render route" 2 Explore ok 'handoff.py render --role <name> --build <slug> --part task'
run_spawn "rule6 AC2: no marker refused" 2 gov-researcher none 'carries 0 gov:handoff marker lines'
run_spawn "rule6 AC2: two markers refused" 2 gov-researcher two 'carries 2 gov:handoff marker lines'
run_spawn "rule6 AC2: a marker role unlike the type refused" 2 gov-researcher role 'is not the subagent_type'
run_spawn "rule6 AC2: a path holding .. refused" 2 gov-researcher dotdot 'is not a repo-relative file under builds/bx/prompts/'
run_spawn "rule6 AC2: a path outside prompts/ refused" 2 gov-researcher spec 'is not a repo-relative file under builds/bx/prompts/'
run_spawn "rule6 AC2: a path naming no file refused" 2 gov-researcher nofile 'names no file'
run_spawn "rule6 AC2: a section one character off refused" 2 gov-researcher off "differs from"
run_spawn "rule6 AC2: a freeform line before the marker refused" 2 gov-researcher pre 'prompt line 1 is not the marker line'
run_spawn "rule6 AC2: a freeform line after the section refused" 2 gov-researcher post 'differs from'
run_spawn "rule6 AC2: a file edited after rendering refused" 2 gov-researcher stale 'edited after rendering'
# AC3 — five refusals, then the call that is admitted.
for i in 1 2 3 4 5; do run_spawn "rule6 AC3: refused spawn $i" 2 general-purpose ok 'not an agent-true role' ho-s3 ho-p3 "ho-r$i"; done
run_spawn "rule6 AC3: the spawn after five refusals is admitted" 0 gov-researcher ok "" ho-s3 ho-p3 ho-ac3-u
# AC4 — a declared harness with known roles passes, as an object and as a JSON string; nothing else.
run_harness "rule6 AC4: the harness with roles as an object" 0 "{\"scriptPath\":\"$HO_H\",\"args\":{\"roles\":{\"builder\":\"gov-builder\"}}}" ""
run_harness "rule6 AC4: the harness with roles in a JSON string" 0 "{\"scriptPath\":\"$HO_H\",\"args\":\"{\\\"roles\\\":{\\\"builder\\\":\\\"gov-builder\\\"}}\"}" ""
run_harness "rule6 AC4: an inline script refused" 2 '{"script":"const s = await agent(\"one\")\n","args":{"roles":{"builder":"gov-builder"}}}' 'an inline `script`'
run_harness "rule6 AC4: a name-only call refused" 2 '{"name":"tier2-review"}' 'names no `scriptPath`'
run_harness "rule6 AC4: a scriptPath not in harnesses refused" 2 "{\"scriptPath\":\"$HOJ/tools/$HO_WF/other.js\",\"args\":{\"roles\":{\"builder\":\"gov-builder\"}}}" 'is not a declared harness'
run_harness "rule6 AC4: args that do not parse refused" 2 "{\"scriptPath\":\"$HO_H\",\"args\":\"{nope\"}" '`args` is not a plain object'
run_harness "rule6 AC4: the harness with no roles refused" 2 "{\"scriptPath\":\"$HO_H\",\"args\":{\"repo\":\".\"}}" 'handoff.py harness-args'
run_harness "rule6 AC4: the harness with roles {} refused" 2 "{\"scriptPath\":\"$HO_H\",\"args\":{\"roles\":{}}}" 'handoff.py harness-args'
run_harness "rule6 AC4: an unknown role refused" 2 "{\"scriptPath\":\"$HO_H\",\"args\":{\"roles\":{\"builder\":\"gov-nobody\"}}}" '"gov-nobody", not an agent-true role'
run_harness "rule6 AC4: an agent-false role refused" 2 "{\"scriptPath\":\"$HO_H\",\"args\":{\"roles\":{\"builder\":\"gov-session\"}}}" '"gov-session", not an agent-true role'
# AC5 — absent adds no rule; broken refuses both tools; unarmed refuses that tool; a selector skips it.
HO_INLINE='{"script":"const s = await agent(\"one\")\n"}'
write_roles none
run_spawn "rule6 AC5: no index, a general-purpose spawn admitted as at base" 0 general-purpose none "" ho-s5 ho-p5 ho-ac5-u
run_harness "rule6 AC5: no index, an inline script admitted as at base" 0 "$HO_INLINE" ""
write_roles '{'
run_spawn "rule6 AC5: a broken index refuses the spawn" 2 general-purpose none 'roles.json is not JSON'
run_harness "rule6 AC5: a broken index refuses the harness call" 2 "$HO_INLINE" 'roles.json is not JSON'
HO_FLAG=--only=join
run_spawn "rule6 AC5: --only=join never meets rule 6 (Agent)" 0 general-purpose none ""
run_harness "rule6 AC5: --only=join never meets rule 6 (Workflow)" 0 "$HO_INLINE" ""
# S11 — `scripts` is the fan-out gate's selector: the script rules run, the call rules do not.
HO_FLAG=--only=scripts
run_harness "rule6 AC5: --only=scripts never meets rule 6" 0 "$HO_INLINE" ""
run_harness "rule6 AC5: --only=scripts still runs the fan-out rules" 2 '{"script":"const r = await boundedParallel(all.map((f) => () => agent(f)), 5)\n"}' 'spawns one agent per item'
HO_FLAG=""
write_roles '{"roles":{"gov-session":{"agent":false,"workflow":"handoff","writes":"none"}},"harnesses":["tools/'"$HO_WF"'/h.js"]}'
run_spawn "rule6 AC5: no agent-true role refuses the spawn as UNARMED" 2 gov-session ok 'UNARMED'
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); d["harnesses"]=[]; print(json.dumps(d))' "$HO_ROLES")"
run_harness "rule6 AC5: no harness refuses the harness call as UNARMED" 2 "{\"scriptPath\":\"$HO_H\",\"args\":{\"roles\":{\"builder\":\"gov-builder\"}}}" 'UNARMED'
# TOOL-aOrientedCast-27 — the spawn's name. Every admitted spawn above carries its handoff's name by
# default; these pass a stale, freeform or misderived one, and one the index cannot derive. Against
# checkHandoffSpawn with its description step cut out, every refusal below is admitted.
write_roles "$HO_ROLES"
run_spawn "rule6 OC27: the unit-less handoff with its unit-less name is admitted" 0 gov-researcher nounit ""
HO_DESC=- run_spawn "rule6 OC27: no description refused, naming the expected name" 2 gov-researcher ok '"bx · T-1 · research"'
HO_DESC=- run_spawn "rule6 OC27: ...and naming the missing one as null" 2 gov-researcher ok 'description null is not'
HO_DESC='Fold two specs, spec three units' run_spawn "rule6 OC27: a freeform description refused" 2 gov-researcher ok '"bx · T-1 · research"'
HO_DESC='bx · T-1 · build' run_spawn "rule6 OC27: a wrong-action description refused" 2 gov-researcher ok '"bx · T-1 · research"'
HO_DESC='bx · T-2 · research' run_spawn "rule6 OC27: a wrong-unit description refused" 2 gov-researcher ok '"bx · T-1 · research"'
HO_DESC='bx · - · research' run_spawn "rule6 OC27: a dash unit part on the unit-less handoff refused" 2 gov-researcher nounit '"bx · research"'
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); del d["roles"]["gov-researcher"]["workflow"]; print(json.dumps(d))' "$HO_ROLES")"
run_spawn "rule6 OC27: an index role with no workflow refused, naming the key" 2 gov-researcher ok 'declares no workflow for gov-researcher'
# TOOL-aOrientedCast-14 AC4 — the anchor: a cwd under no checkout falls back to CLAUDE_PROJECT_DIR, a
# cwd in a checkout keeps it, and neither resolving says so. $TMP itself lies in no checkout. Against
# a rule 6 reading the payload cwd alone, the first row exits 0 and the third says nothing.
write_roles "$HO_ROLES"
mkdir -p "$TMP/horepo2/.git" "$TMP/noco"
HO_CWD="$NODEDIR" HO_PROJECT="$HOJ"
run_spawn "rule6 OC14 AC4: cwd under no checkout, CLAUDE_PROJECT_DIR armed -> Explore refused" 2 Explore ok 'as the gov-researcher role'
HO_CWD="$NODEDIR/horepo2"
run_spawn "rule6 OC14 AC4: cwd in an index-less checkout keeps it over CLAUDE_PROJECT_DIR -> admitted" 0 Explore ok ""
HO_CWD="$NODEDIR" HO_PROJECT="$NODEDIR/noco"
run_spawn "rule6 OC14 AC4: cwd and CLAUDE_PROJECT_DIR under no checkout -> admitted, naming rule 6 unarmed" 0 Explore ok 'rule 6 unarmed'
HO_CWD="" HO_PROJECT=""
write_roles none

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
