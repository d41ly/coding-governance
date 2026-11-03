#!/usr/bin/env bash
# Runnable check for the portable agent-cap.js guard on the Workflow and Agent tool calls, the rules it
# keeps since TOOL-dFairHearing-16: rule 6, the rendered handoff, and rule 7, the settings in force
# against the landed agent limit, plus the readers it exports, its refusal of every `--only=`, and
# its refusal of a spec-audit call with no opt-in pack beside it (TOOL-dFairHearing-22).
# Rules 2, 5 and 0 moved to the review kit and their arms to its suites; the retired rules' arms went
# with them.
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
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
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
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
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

# ---- the first arms ------------------------------------------------------------------------------
# TOOL-dFairHearing-16: rules 0, 2 and 5 left this hook for the review kit, and their arms went with
# them, each keeping its label, its payload and its verdict: rule 2's to the kit's
# check-verifier-fanout.test.sh, rule 5's to check-review-join.test.sh, rule 0's to
# spec-audit-optin.test.sh. What stays is what the hook still judges, rules 6 and 7, and the readers
# it EXPORTS to those homes. This arm requires the hook as a module: were `main()` to run on require it
# would read the empty stdin and exit before the line printed, and a reader missing from the exports
# prints `undefined` in its place.
exported=$(cd "$TMP" && node -e "const m=require(process.argv[1]); console.log(typeof m.runBothViews, typeof m.extractWorkflowArgs, typeof m.extractBuildSlug, typeof m.readWriterBound, m.MAX_VERIFIERS)" "$HOOK" < /dev/null 2>"$TMP/err")
if [ "$exported" = "function function function function 5" ]; then
  echo "ok   requiring the hook runs no rule, and it exports the readers its review-kit homes read"; pass=$((pass+1))
else
  echo "FAIL the hook's exports read '$exported', want 'function function function function 5'"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
fi
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi
check "non-Workflow tool → allow" 0 '{"tool_name":"Bash","tool_input":{"command":"parallel(x.map(y))"}}'
NODEDIR=$(cd "$TMP" && pwd -W 2>/dev/null || printf '%s' "$TMP")
# A `name:` run supplies no source at all. It is ALLOWED here and covered by the merge-bar leg over
# <prefix>/workflows/ instead — declared, not papered over.
check "name-only run → allow (no source reaches the hook)" 0 '{"tool_name":"Workflow","tool_input":{"name":"tier2-review"}}'

# ---- each moved rule's planted case is ADMITTED here now (TOOL-dFairHearing-16) -------------------
# The three payloads the hook DENIED at the pass's starting commit, one per rule that left: each is
# denied at its new home, by its own suite, and this hook must no longer carry the rule. A hook that
# still denied would mean the rule lives in two homes, against the move's order.
check "a verify fan over chunk(all, 1) marked gov:fixed-verifiers is admitted: rule 2 is check-verifier-fanout.js's" 0 '{"tool_name":"Workflow","tool_input":{"script":"const b = chunk(all, 1) // gov:fixed-verifiers\nconst r = await boundedParallel(b.map((g) => () => agent(g)), 5)"}}'
check "a verdict join keyed verdictByRef is admitted: rule 5 is check-review-join.js's" 0 '{"tool_name":"Workflow","tool_input":{"script":"const verdictByRef = new Map()\nverdictByRef.set(f.ref, v)"}}'
SA0="$TMP/sa0"; mkdir -p "$SA0/memory/builds/tSA/reviews"; printf -- '---\nslug: tSA\n---\n' > "$SA0/memory/builds/tSA/README.md"
# ---- the opt-in pack's presence (TOOL-dFairHearing-22) -------------------------------------------
# A spec-audit call is refused unless the review kit's pack sits beside the hook, so a hook landed
# without it (a partial update naming this kit alone) cannot admit an audit nobody judged. The arms
# copy the hook into $TMP/arms-hooks/hooks, with no workflows kit beside it, and into
# $TMP/pack-hooks/hooks, with the tree's own pack copied beside it. Against a hook with no presence
# check, the dated call and the `specAudit` call are admitted, and the first and third arms red.
PKWF=$(resolve_kit_dir "$TESTPY" workflows spec-audit-optin.js "$HERE") || PKWF=""
[ -n "$PKWF" ] && [ -z "${ROOTDIR:-}" ] && ROOTDIR=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null)
PACK_HOOKS="$TMP/pack-hooks/hooks"; mkdir -p "$PACK_HOOKS" "$TMP/pack-hooks/workflows"; cp "$KIT_HOOK" "$HERE/scratch-guard.js" "$PACK_HOOKS/"
[ -n "$PKWF" ] && cp "$ROOTDIR/$PKWF/spec-audit-optin.js" "$TMP/pack-hooks/workflows/"
run_pack() { # name expected_exit hook payload-json [text stderr must carry ...]
  local name=$1 want=$2 hk=$3 body=$4 got miss=""; shift 4
  printf '%s' "$body" | (cd "$TMP" && node "$hk") >/dev/null 2>"$TMP/err"; got=$?
  for n in "$@"; do grep -qF -- "$n" "$TMP/err" || miss="$miss '$n'"; done
  if [ "$got" = "$want" ] && [ -z "$miss" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $got, want $want${miss:+, stderr missing$miss})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
SAD="$TMP/sad"; mkdir -p "$SAD/memory/builds/tSA/reviews"; printf -- '---\nslug: tSA\nspec-audit: 2026-10-23\n---\n' > "$SAD/memory/builds/tSA/README.md"
SA_DATED="{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"spec-audit\",\"repo\":\"$NODEDIR/sad\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
run_pack "pack AC1: a dated spec-audit call with no pack beside the hook is refused, naming the pack and the update" 2 "$HOOK" "$SA_DATED" 'spec-audit-optin.js' 'govkit update --kits review-harness'
if [ -z "$PKWF" ]; then
  echo "FAIL pack AC2: no workflows kit holding spec-audit-optin.js beside this hooks kit, so the pack-present arm has no pack to copy"; fail=$((fail+1))
else
  run_pack "pack AC2: the same call with the pack beside the hook is admitted" 0 "$PACK_HOOKS/agent-cap.js" "$SA_DATED"
  run_pack "an undated spec-audit call is admitted: rule 0 is the review kit's spec-audit-optin.js" 0 "$PACK_HOOKS/agent-cap.js" "{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"spec-audit\",\"repo\":\"$NODEDIR/sa0\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
fi
run_pack "pack AC2: a diff-review call with no pack beside the hook is admitted" 0 "$HOOK" "{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"diff-review\",\"repo\":\"$NODEDIR/sad\"}}}"
run_pack "pack AC3: a specAudit call with no kind and no pack is refused, naming the pack" 2 "$HOOK" '{"tool_name":"Workflow","tool_input":{"name":"unattended-build","args":"{\"specAudit\":\"2026-10-23\",\"slug\":\"tSA\",\"repo\":\".\"}"}}' 'spec-audit-optin.js'
# ...and the selector they took with them. Every `--only=` argument is REFUSED, exit 2, naming both
# script homes, and BEFORE stdin is read: the payload here is a Bash call, which the hook admits at its
# tool-name test, so an exit 0 is a refusal that came too late. The four rule-6 arms that ran under a
# selector are this arm now; a selector left running no rule could never red (§8 F7).
for only in --only=scripts --only=join --only=bogus --only=; do
  printf '%s' '{"tool_name":"Bash","tool_input":{"command":"true"}}' | (cd "$TMP" && node "$HOOK" "$only") >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" = 2 ] && grep -qF 'check-verifier-fanout.js' "$TMP/err" && grep -qF 'check-review-join.js' "$TMP/err"; then
    echo "ok   $only is refused before stdin, naming both script homes (exit $got)"; pass=$((pass+1))
  else
    echo "FAIL $only exited $got, want 2 naming check-verifier-fanout.js and check-review-join.js"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
done

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
  printf '%s' "$payload" | (cd "$TMP" && { [ -z "$HO_PROJECT" ] || export CLAUDE_PROJECT_DIR="$HO_PROJECT"; } && node "$HOOK") >/dev/null 2>"$TMP/err"; got=$?
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
  printf '%s' "$payload" | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; got=$?
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
# The four arms that ran rule 6 under a selector left with it (TOOL-dFairHearing-16): every `--only=`
# refuses now, before any rule, and the refusal arm near the top of this file replaces them.
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
