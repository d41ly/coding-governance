#!/usr/bin/env bash
# Runnable check for the roles kit's spawn guard, `spawn-guard.js`, on the Workflow and Agent tool calls
# (TOOL-dBoundRoles-25): every rule the hooks kit's retired agent limit hook ran, moved with its arms,
# each retargeted at the pack and its deny prefix `BLOCKED by spawn-guard:` — rule 6, the rendered
# handoff, with harness admission held to the landed blob (S3), rule 8, the effort level a call runs at
# against its model's (TOOL-aGuardedEffort-1), and rule 7, the settings in force against the landed agent
# limit, plus the readers the pack exports, its refusal of every `--only=`, and its refusal of a
# spec-audit call with no opt-in pack beside it (TOOL-dFairHearing-22). Every arm runs a COPY of the
# pack beside a copy of the hooks kit's scratch-guard.js, the layout `build_pack` builds, since the pack
# reads that file's exports. The arms over the retired hook's own copies and its frozen script views
# did not move: the views are the review kit's script-views.js now, and their arm is its suite's.
# Run from the kit directory: bash ./spawn-guard.test.sh   (exit 0 = all pass)
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "spawn-guard.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
# ROOTPFX is a ROOT install's prefix, empty by definition: a fixture that models a root install,
# or a key relative to the tool root, is spelled through it rather than bare (TOOL-aRepatriatedFork-28 S2).
ROOTPFX=""
KIT_HOOK="$HERE/spawn-guard.js"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
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
  # THE BAR'S OWN RESOLUTION, taken with no spawn (TOOL-aMeasuredDrag-11). The run-gates runner
  # exports GATE_RESOLVED_PY as four lines: the version, the launcher it resolved, and GOV_PYTHON and
  # PATH as it saw them. With no caller override the loop below is decided by GOV_PYTHON, PATH and the
  # floor, so a memo matching both byte for byte, at or above THIS floor, is what the loop would print.
  # Anything else, malformed or partial included, is ignored and the loop runs. Only an absolute
  # launcher is admitted (TOOL-aMeasuredDrag-12): a relative one names another file once a leg
  # changes directory, and a bare name does too under a PATH holding `.`.
  _rp_re=$'^([0-9]+)\\.([0-9]+)\n(/[^\n]*|[A-Za-z]:/[^\n]*|[A-Za-z]:\\\\[^\n]*)\n([^\n]*)\n(.*)$'
  if [ -z "${1:-}" ] && [[ ${GATE_RESOLVED_PY:-} =~ $_rp_re ]] \
    && [ "${BASH_REMATCH[4]}" = "${GOV_PYTHON:-}" ] && [ "${BASH_REMATCH[5]}" = "$PATH" ] \
    && [ $(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} )) -ge "$_rp_fv" ]; then
    printf '%s\n' "${BASH_REMATCH[3]}"
    return 0
  fi
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
# >>> refuse_wrong_shell — canonical copy: refuse-wrong-shell.sh in gov's lib dir (byte-identical; gated)
wrong_shell_at() {   # <abs path> <wsl 0|1>; returns 0 when the path is a Windows checkout under WSL
  [ "$2" = 1 ] || return 1
  case "$1" in /mnt/[a-z]/*) return 0 ;; esac
  return 1
}
refuse_wrong_shell() {
  _rws_wsl=0
  { [ -n "${WSL_DISTRO_NAME:-}" ] || [ -e /proc/sys/fs/binfmt_misc/WSLInterop ]; } && _rws_wsl=1
  _rws_p=${BASH_SOURCE[0]:-$0}
  case "$_rws_p" in /*) ;; *) _rws_p=$PWD/$_rws_p ;; esac
  wrong_shell_at "$_rws_p" "$_rws_wsl" || return 0
  echo "refuse_wrong_shell: WSL's bash is running $_rws_p from a Windows checkout under /mnt/;" >&2
  echo "refuse_wrong_shell: run it with Git's bash (C:/Program Files/Git/bin/bash.exe)." >&2
  return 1
}
# <<< refuse_wrong_shell
refuse_wrong_shell || exit 2
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
TESTPY=$(resolve_python) || { echo "spawn-guard.test: no usable python"; exit 2; }
# THE PACK'S LAYOUT: the hooks kit's scratch-guard.js, found the way the pack finds it, read from its kit.
ROOTDIR=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null)
SG_DIR=$(resolve_kit_dir "$TESTPY" hooks scratch-guard.js "$HERE") || { echo "spawn-guard.test: no hooks kit holding scratch-guard.js beside this kit"; exit 2; }
SG_SRC="$ROOTDIR/$SG_DIR/scratch-guard.js"
# Kit directory names, read from where each kit sits and never typed (the install-prefix ban).
RKN=${KIT_REL##*/}; HKN=${SG_DIR##*/}; WKN=workflows; LBW="${PFX}$WKN"
build_pack() { # <kits dir> -> prints the pack copied into <kits dir>, beside a copy of the hooks kit's scratch-guard.js
  mkdir -p "$1/$RKN" "$1/$HKN" && cp "$KIT_HOOK" "$1/$RKN/" && cp "$SG_SRC" "$1/$HKN/" && printf '%s\n' "$1/$RKN/spawn-guard.js"
}
# THE ARMS RUN A COPY (TOOL-dGroundRules-21 S38): rule 7 refuses a payload cwd that lies in no checkout
# wherever a policy kit sits beside the pack, and every arm below runs from "$TMP", which no checkout
# holds. The copy sits beside scratch-guard.js and no policy kit, where rule 7 adds no rule, so each arm
# judges the rule it names; the sections that arm rule 7 or admit a harness build their own copies beside
# a policy kit, since a declared harness is admitted only at its landed blob, which the policy kit reads.
HOOK=$(build_pack "$TMP/arms-kits")
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
# spec-audit-optin.test.sh. What stays is what the hook still judges, rules 6, 8 and 7, and the readers
# it EXPORTS to those homes. This arm requires the hook as a module: were `main()` to run on require it
# would read the empty stdin and exit before the line printed, and a reader missing from the exports
# prints `undefined` in its place.
exported=$(cd "$TMP" && node -e "const m=require(process.argv[1]); console.log(typeof m.resolveModelProfile, typeof m.checkEffortLevel, typeof m.resolvePromptsAuthor, typeof m.checkHarnessLanded, Array.isArray(m.TYPED_INPUTS))" "$HOOK" < /dev/null 2>"$TMP/err")
if [ "$exported" = "function function function function true" ]; then
  echo "ok   requiring the pack runs no rule, and it exports the readers the roles kit's suites read"; pass=$((pass+1))
else
  echo "FAIL the pack's exports read '$exported', want 'function function function function true'"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
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
PACK_HOOK=$(build_pack "$TMP/pack-kits"); mkdir -p "$TMP/pack-kits/workflows"
[ -n "$PKWF" ] && cp "$ROOTDIR/$PKWF/spec-audit-optin.js" "$TMP/pack-kits/workflows/"
run_pack() { # name expected_exit hook payload-json [text stderr must carry ...]
  local name=$1 want=$2 hk=$3 body=$4 got miss=""; shift 4
  printf '%s' "$body" | (cd "$TMP" && node "$hk") >/dev/null 2>"$TMP/err"; got=$?
  for n in "$@"; do grep -qF -- "$n" "$TMP/err" || miss="$miss '$n'"; done
  if [ "$got" = "$want" ] && [ -z "$miss" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $got, want $want${miss:+, stderr missing$miss})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
SAD="$TMP/sad"; mkdir -p "$SAD/memory/builds/tSA/reviews"; printf -- '---\nslug: tSA\nspec-audit: 2026-10-23\n---\n' > "$SAD/memory/builds/tSA/README.md"
SA_DATED="{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"spec-audit\",\"repo\":\"$NODEDIR/sad\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
# TOOL-dFairHearing-27 S13: this hook copy has no receipt above it, so the remedy is `apply`, which installs a kit;
# `update` refuses one the receipt does not claim.
run_pack "pack AC1: a dated spec-audit call with no pack beside the hook is refused, naming the pack and the apply" 2 "$HOOK" "$SA_DATED" 'spec-audit-optin.js' 'govkit apply --kits review-harness'
# ---- TOOL-dFairHearing-27 AC8, AC15: the remedy by receipt state, and the pack found through the receipt ----------
# A layout with a `.git` marker, the hook under `.claude/hooks/` and the pack under a per-kit prefix the probe
# beside the hook never reaches. RED against the hook at TOOL-dFairHearing-22's commit, which read no receipt:
# it named `update` for an unclaimed kit and denied the pack the receipt names.
RWK=workflows
RCP="$TMP/rcpt/p"; mkdir -p "$RCP/.git" "$RCP/.governance" "$RCP/tools/$RWK"
RCP_HOOK=$(build_pack "$RCP/.claude")
RCP_ROW="{\"path\":\"tools/$RWK/spec-audit-optin.js\",\"kit\":\"review-harness\",\"role\":\"engine\",\"source\":\"tools/$RWK/spec-audit-optin.js\"}"
printf '{"kits":["agent-cap"],"files":[]}' > "$RCP/.governance/install.json"
run_pack "FH27 AC8: a receipt claiming agent-cap alone names the apply remedy" 2 "$RCP_HOOK" "$SA_DATED" 'govkit apply --kits review-harness'
grep -qF 'update --kits review-harness' "$TMP/err" && { echo "FAIL FH27 AC8: the unclaimed receipt's deny still names the update remedy"; fail=$((fail+1)); }
printf '{"kits":["agent-cap","review-harness"],"files":[]}' > "$RCP/.governance/install.json"
run_pack "FH27 AC8: a receipt claiming both names the update remedy" 2 "$RCP_HOOK" "$SA_DATED" 'govkit update --kits review-harness'
: > "$RCP/tools/$RWK/spec-audit-optin.js"
printf '{"kits":["agent-cap","review-harness"],"files":[%s]}' "$RCP_ROW" > "$RCP/.governance/install.json"
run_pack "FH27 AC15: the pack under a per-kit prefix the receipt names is admitted" 0 "$RCP_HOOK" "$SA_DATED"
# TOOL-dFairHearing-32 AC15: `resolveKitDir`'s rungs. A row naming a missing path is SKIPPED, so the pack beside the
# hook admits; only the resolver's refusal denies, naming the receipt and both probes, and a `..` row is skipped
# even where it names a file. RED against the hook at TOOL-dFairHearing-27's commit, which denied the stale row
# whatever sat beside the hook. The paths are matched by their tails: node spells the scratch root its own way.
printf '{"kits":["agent-cap","review-harness"],"files":[%s]}' "${RCP_ROW//tools\/$RWK\/spec-audit-optin.js\",\"kit/tools/gone/spec-audit-optin.js\",\"kit}" > "$RCP/.governance/install.json"
mkdir -p "$RCP/.claude/workflows"; : > "$RCP/.claude/workflows/spec-audit-optin.js"
run_pack "FH32 AC15: a stale receipt row with the pack beside the hook is admitted" 0 "$RCP_HOOK" "$SA_DATED"
rm -f "$RCP/.claude/workflows/spec-audit-optin.js"
run_pack "FH32 AC15: ...and with the pack removed too, refused naming the receipt and both probes" 2 "$RCP_HOOK" "$SA_DATED" \
  'rcpt/p/.governance/install.json' 'rcpt/p/.claude/roles/workflows and ' 'rcpt/p/.claude/workflows. '
printf '{"kits":["agent-cap","review-harness"],"files":[%s]}' "${RCP_ROW//\"path\":\"tools\/$RWK/\"path\":\"tools/x/../$RWK}" > "$RCP/.governance/install.json"
run_pack "FH32 AC15: a receipt row whose path holds .. is skipped though it names the pack, refused the same way" 2 "$RCP_HOOK" "$SA_DATED" \
  'rcpt/p/.governance/install.json' 'rcpt/p/.claude/roles/workflows and ' 'rcpt/p/.claude/workflows. '
printf '{"kits":["agent-cap","review-harness"],"files":[]}' > "$RCP/.governance/install.json"
run_pack "FH27 AC15: with the row left out, the probe beside the hook misses and the call is refused" 2 "$RCP_HOOK" "$SA_DATED" 'spec-audit-optin.js'
if [ -z "$PKWF" ]; then
  echo "FAIL pack AC2: no workflows kit holding spec-audit-optin.js beside this hooks kit, so the pack-present arm has no pack to copy"; fail=$((fail+1))
else
  run_pack "pack AC2: the same call with the pack beside the hook is admitted" 0 "$PACK_HOOK" "$SA_DATED"
  run_pack "an undated spec-audit call is admitted: rule 0 is the review kit's spec-audit-optin.js" 0 "$PACK_HOOK" "{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"spec-audit\",\"repo\":\"$NODEDIR/sa0\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
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
LIMHOOK=$(build_pack "$TMP/limit-kits")
LIMREPO="$TMP/limitrepo"; mkdir -p "$LIMREPO/.git" "$LIMREPO/sub"
LIMJ="$NODEDIR/limitrepo/sub"
run_limit_call() { # name expected_exit payload-json [hook] [text stderr must carry]
  local got
  printf '%s' "$3" | (cd "$TMP" && node "${4:-$LIMHOOK}") >/dev/null 2>"$TMP/err"; got=$?
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
if [ -z "$LIMPK" ] || [ -z "$ROOTDIR" ]; then
  echo "FAIL limit: no policy kit beside this hooks kit, so rule 7 has nothing to arm with"; fail=$((fail+1))
else
  R7="$TMP/r7"; mkdir -p "$R7/.governance" "$R7/kits/policy" "$R7/.claude" "$R7/$LBW"
  R7_HOOK=$(build_pack "$R7/kits")
  # The harness rule 8's order arm names below, committed so its blob is the landed one (S3).
  printf 'const s = await agent("one")\n' > "$R7/$LBW/h.js"
  for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do cp "$ROOTDIR/$LIMPK/$f" "$R7/kits/policy/"; done
  printf '[runtime]\nagents-in-flight = 2\n' > "$R7/.governance/policy.toml"
  ( cd "$R7" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
      && git config user.name t && git add -A && git commit -qm limit --no-verify )
  R7_WF='{"tool_name":"Workflow","cwd":"'"$NODEDIR/r7"'","tool_input":{"script":"const r = await agent(1)"}}'
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"3","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"3"}}\n' > "$R7/.claude/settings.json"
  run_limit_call "rule7: settings at 3 over a landed limit of 2 -> deny, naming the variable" 2 "$R7_WF" "$R7_HOOK" 'CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS'
  # TOOL-dBoundRoles-25 AC7: the moved rule names the file and both numbers.
  run_limit_call "rule7 BR25 AC7: ...naming the file, the value and the landed limit" 2 "$R7_WF" "$R7_HOOK" '.claude/settings.json: env.CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS is 3, above runtime.agents-in-flight 2'
  run_limit_call "rule7 BR25 AC7: ...and its stderr opens with the pack's prefix" 2 "$R7_WF" "$R7_HOOK" 'BLOCKED by spawn-guard: rule 7'
  run_limit_call "rule7: ...and naming the render" 2 "$R7_WF" "$R7_HOOK" 'policy.py settings --write'
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R7/.claude/settings.json"
  run_limit_call "rule7: settings at the limit -> allow (control)" 0 "$R7_WF" "$R7_HOOK"
  # TOOL-dGroundRules-61: a settings file GOV_SETTINGS_JSON declares outside the checkout is one more
  # layer, never the project file's replacement, and every layer that sets a variable holds the limit.
  R7D="$TMP/r7-declared.json"; R7DN="$NODEDIR/r7-declared.json"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R7D"
  printf '{"env":{"CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"3"}}\n' > "$R7/.claude/settings.json"
  GOV_SETTINGS_JSON="$R7DN" run_limit_call "rule7: declared at 2, the project file at 3 -> deny, naming the project file" 2 "$R7_WF" "$R7_HOOK" '.claude/settings.json: env.CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS is 3'
  rm -f "$R7/.claude/settings.json"
  GOV_SETTINGS_JSON="$R7DN" run_limit_call "rule7: declared only, at 2 -> allow" 0 "$R7_WF" "$R7_HOOK"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R7/.claude/settings.json"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"3","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"3"}}\n' > "$R7D"
  GOV_SETTINGS_JSON="$R7DN" run_limit_call "rule7: declared at 3, the project file at 2 -> deny, naming the declared file" 2 "$R7_WF" "$R7_HOOK" 'r7-declared.json: env.CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS is 3'
fi
# ---- TOOL-dBoundRoles-10 AC4 (S3): rule 6 reads prompts.author, and its refusal names the value --------
# A real repository, the hook copy beside a copy of the policy kit, as rule 7's armed section builds it,
# and a role index with one agent-true role. Its primary branch `main` commits a policy file setting
# prompts.author to requesting-worker-rendered; `pa-unset`, which GOV_DEFAULT_BRANCH names for two rows,
# commits none, so the key reads its default. The author-requesting plant is a freeform Agent prompt piped
# to the hook from the fixture, refused by rule 6, the refusal naming the key and the value in force. Staged
# against a rule 6 that reads no key, the author-requesting row and its unset twin red: no such line.
# WHAT THIS DOES NOT CHECK: the prompt writer's framing under prompt-writer, which is TOOL-dBoundRoles-4's.
if [ -z "$LIMPK" ] || [ -z "$ROOTDIR" ]; then
  echo "FAIL prompts.author: no policy kit beside this hooks kit, so rule 6 has no key to read"; fail=$((fail+1))
else
  PA="$TMP/pa"; mkdir -p "$PA/.governance" "$PA/kits/policy" "$PA/.claude"
  PA_HOOK=$(build_pack "$PA/kits")
  PA_NODE_HOOK="$(cd "$PA/kits/roles" && pwd -W 2>/dev/null || printf '%s' "$PA/kits/roles")/spawn-guard.js"
  for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do cp "$ROOTDIR/$LIMPK/$f" "$PA/kits/policy/"; done
  printf '[prompts]\nauthor = "requesting-worker-rendered"\n' > "$PA/.governance/policy.toml"
  printf '%s\n' '{"roles":{"gov-researcher":{"agent":true,"workflow":"research","writes":"none"}},"harnesses":[]}' > "$PA/.claude/roles.json"
  ( cd "$PA" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
      && git config user.name t && git add -A && git commit -qm author --no-verify \
      && git update-ref refs/heads/pa-unset "$(git commit-tree "$(git mktree </dev/null)" -m 'no policy file')" )
  pa_got=$(cd "$TMP" && GOV_DEFAULT_BRANCH=pa-unset node -e 'console.log(require(process.argv[1]).resolvePromptsAuthor(process.argv[2]))' "$PA_NODE_HOOK" "$NODEDIR/pa" 2>&1)
  if [ "$pa_got" = prompt-writer ]; then echo "ok   AC4 resolvePromptsAuthor with prompts.author unset reads prompt-writer"; pass=$((pass+1))
  else echo "FAIL AC4 resolvePromptsAuthor with prompts.author unset read: $pa_got"; fail=$((fail+1)); fi
  pa_got=$(cd "$TMP" && node -e 'console.log(require(process.argv[1]).resolvePromptsAuthor(process.argv[2]))' "$PA_NODE_HOOK" "$NODEDIR/pa" 2>&1)
  if [ "$pa_got" = requesting-worker-rendered ]; then echo "ok   AC4 resolvePromptsAuthor reads the landed requesting-worker-rendered"; pass=$((pass+1))
  else echo "FAIL AC4 resolvePromptsAuthor with prompts.author set read: $pa_got"; fail=$((fail+1)); fi
  PA_FREE='{"tool_name":"Agent","cwd":"'"$NODEDIR/pa"'","session_id":"pa","tool_input":{"subagent_type":"gov-researcher","prompt":"Research this freely.","description":"x"}}'
  run_limit_call "AC4 author-requesting: a freeform prompt under requesting-worker-rendered -> deny by rule 6" 2 "$PA_FREE" "$PA_HOOK" 'rule 6 (TOOL-aOrientedCast-7) refused'
  run_limit_call "AC4 author-requesting: ...naming prompts.author and the value in force" 2 "$PA_FREE" "$PA_HOOK" 'prompts.author is requesting-worker-rendered'
  GOV_DEFAULT_BRANCH=pa-unset run_limit_call "AC4 a freeform prompt with prompts.author unset -> deny naming the default prompt-writer" 2 "$PA_FREE" "$PA_HOOK" 'prompts.author is prompt-writer'
fi
# ---- TOOL-dBoundRoles-4 AC3 (S4): under prompts.author = prompt-writer a spawn carries the prompt writer's framing
# A real repository, the hook copy beside a copy of the policy kit, as the section above builds it; its main branch
# commits prompts.author = requesting-worker-rendered, and `pf-unset`, which GOV_DEFAULT_BRANCH names for the
# default's rows, commits no policy file. Its settings hold the default agent limit, so rule 7 admits, and its index
# carries no `effort`, so rule 8 adds no rule. The prompt files under memory/builds/bx/prompts/ are written as the
# renderer defines them, each section hashed as `roles_lib.derive_section_sha` hashes it: the prompt writer's work
# order, a researcher's, and three builder tasks, one with no framing and two whose `### framing:job` block closes
# with a `Framed by:` line naming the first or the second. The plants: `spawn-unframed`, denied under the default
# naming the key and the route and admitted under requesting-worker-rendered; `spawn-framed`, admitted;
# `spawn-framed-by-researcher`, denied naming the researcher's role; `spawn-prompt-writer`, admitted unframed.
# Staged against a rule 6 whose framing check is cut, `spawn-unframed` and `spawn-framed-by-researcher` are admitted
# under the default and their rows red. WHAT THIS DOES NOT CHECK: that the framing is the prompt writer's return,
# which `handoff.py render --framed-by` reads and the roles kit's render self-test holds.
if [ -z "$LIMPK" ] || [ -z "$ROOTDIR" ]; then
  echo "FAIL prompt framing: no policy kit beside this hooks kit, so rule 6 has no prompts.author to read"; fail=$((fail+1))
else
  PF="$TMP/pf"; mkdir -p "$PF/.governance" "$PF/kits/policy" "$PF/.claude" "$PF/memory/builds/bx/prompts"
  PF_HOOK=$(build_pack "$PF/kits")
  for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do cp "$ROOTDIR/$LIMPK/$f" "$PF/kits/policy/"; done
  printf '[prompts]\nauthor = "requesting-worker-rendered"\n' > "$PF/.governance/policy.toml"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$PF/.claude/settings.json"
  "$TESTPY" -c '
import hashlib, json, os, sys
root, cwd, out = sys.argv[1], sys.argv[2], sys.argv[3]
h = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]
pre = "memory/builds/bx/prompts/"
role = {r: "## Role\n\nYou are %s.\n\n" % r for r in ("gov-builder", "gov-prompt-writer", "gov-researcher")}
opening = "## Task\n\nThis handoff is for build `bx`, unit `T-1`.\n"
def write_prompt_file(rel, r, task):
    m = "<!-- gov:handoff role=%s build=bx unit=T-1 item=- path=%s role-sha=%s task-sha=%s -->" % (r, rel, h(role[r]), h(task))
    with open(os.path.join(root, rel), "w", newline="\n", encoding="utf-8") as f:
        f.write("**Serves:** journal T-1\n\n# %s handoff - T-1\n\n%s\n\n%s%s" % (r, m, role[r], task))
    return m, h(task)
pw = pre + "2026-11-23-prompt-T-1-1-prompt-writer.md"
rs = pre + "2026-11-23-prompt-T-1-2-researcher.md"
pw_mark, pw_sha = write_prompt_file(pw, "gov-prompt-writer", opening + "\n### input:question\n\nWhat does T-1 build?\n")
_m, rs_sha = write_prompt_file(rs, "gov-researcher", opening + "\n### input:question\n\nWhich seam fits?\n")
def framed(path, sha):
    return opening + "\n### framing:job\n\nBuild T-1 as its spec says.\n\nFramed by: %s task-sha=%s\n\n### framing:no-stop\n\nStop once it is committed.\n" % (path, sha)
plants = {"spawn-unframed": ("gov-builder", opening, "build"),
          "spawn-framed": ("gov-builder", framed(pw, pw_sha), "build"),
          "spawn-framed-by-researcher": ("gov-builder", framed(rs, rs_sha), "build")}
# TOOL-dBoundRoles-92 - one plant per refusal of checkFraming, each the framed task with one thing moved.
whole, named = framed(pw, pw_sha), "Framed by: %s task-sha=%s\n\n" % (pw, pw_sha)
for rel, text in (("plain.md", "no marker\n"), ("twice.md", pw_mark + "\n\n" + pw_mark + "\n")):
    with open(os.path.join(root, pre + rel), "w", newline="\n", encoding="utf-8") as f:
        f.write(text)
plants.update({"frame-" + k: ("gov-builder", task, "build") for k, task in {
    "two-blocks": whole + "\n### framing:job\n\nAgain.\n", "no-line": whole.replace(named, ""),
    "two-lines": whole.replace(named, named + named), "before": whole.replace(named, "").replace("\n### framing:job", "\n" + named + "### framing:job"),
    "after": whole.replace(named, "") + "\n" + named, "misspelt": framed(pw, "no-sha"),
    "outside": framed("memory/builds/bx/spec/x.md", pw_sha), "dotdot": framed(pre + "../prompts/" + pw[len(pre):], pw_sha),
    "no-file": framed(pre + "none.md", pw_sha), "no-marker": framed(pre + "plain.md", pw_sha),
    "two-markers": framed(pre + "twice.md", pw_sha), "other-sha": framed(pw, "0123456789ab")}.items()})
index = {"roles": {r: {"agent": True, "role-sha": h(role[r]), "workflow": w, "writes": c} for r, w, c in (
    ("gov-builder", "build", "product"), ("gov-prompt-writer", "handoff", "none"), ("gov-researcher", "research", "none"))},
    "harnesses": []}
with open(os.path.join(root, ".claude", "roles.json"), "w", newline="\n", encoding="utf-8") as f:
    json.dump(index, f)
calls = {}
for k, (name, (r, task, wf)) in enumerate(plants.items()):
    m, _s = write_prompt_file(pre + "2026-11-23-prompt-T-1-%d-builder.md" % (3 + k), r, task)
    calls[name] = (r, m + "\n\n" + task, wf)
calls["spawn-prompt-writer"] = ("gov-prompt-writer", pw_mark + "\n\n" + opening + "\n### input:question\n\nWhat does T-1 build?\n", "handoff")
for name, (r, prompt, wf) in calls.items():
    with open(os.path.join(out, name + ".json"), "w", encoding="utf-8") as f:
        json.dump({"tool_name": "Agent", "cwd": cwd, "session_id": "pf", "tool_input": {
            "subagent_type": r, "prompt": prompt, "description": "bx · T-1 · " + wf}}, f)
' "$PF" "$NODEDIR/pf" "$TMP"
  ( cd "$PF" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
      && git config user.name t && git add -A && git commit -qm framing --no-verify \
      && git update-ref refs/heads/pf-unset "$(git commit-tree "$(git mktree </dev/null)" -m 'no policy file')" )
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR4 AC3 spawn-unframed: a builder task with no framing:job under the default prompt-writer -> deny naming prompts.author" 2 "$(cat "$TMP/spawn-unframed.json")" "$PF_HOOK" 'prompts.author is prompt-writer, so a gov-builder task carries the prompt writer'"'"'s framing'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR4 AC3 spawn-unframed: ...naming the three-call route, --for then --framed-by" 2 "$(cat "$TMP/spawn-unframed.json")" "$PF_HOOK" '--for gov-builder --build bx --unit T-1'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR4 AC3 spawn-framed: its Framed by: line names the prompt writer's work order and task-sha -> allow" 0 "$(cat "$TMP/spawn-framed.json")" "$PF_HOOK"
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR4 AC3 spawn-framed-by-researcher: its Framed by: line names a role=gov-researcher work order -> deny" 2 "$(cat "$TMP/spawn-framed-by-researcher.json")" "$PF_HOOK" 'marker names role=gov-researcher, not gov-prompt-writer'
  run_limit_call "rule6 BR4 AC3 spawn-unframed: under requesting-worker-rendered the unframed builder task -> allow" 0 "$(cat "$TMP/spawn-unframed.json")" "$PF_HOOK"
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR4 AC3 spawn-prompt-writer: the prompt writer's own task, unframed, under the default -> allow" 0 "$(cat "$TMP/spawn-prompt-writer.json")" "$PF_HOOK"
  # TOOL-dBoundRoles-92 AC14: every refusal of checkFraming past the role's, each by its own text; with one of
  # them cut, its plant is admitted or refused by another text. The line count, the placement test, the path check
  # and the marker count take two plants each.
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-two-blocks: two framing:job blocks -> deny" 2 "$(cat "$TMP/frame-two-blocks.json")" "$PF_HOOK" 'the task carries 2 `### framing:job` blocks'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-no-line: no Framed by: line -> deny" 2 "$(cat "$TMP/frame-no-line.json")" "$PF_HOOK" 'the task carries 0 `Framed by:` lines'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-two-lines: two Framed by: lines -> deny" 2 "$(cat "$TMP/frame-two-lines.json")" "$PF_HOOK" 'the task carries 2 `Framed by:` lines'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-before: the line before its block -> deny" 2 "$(cat "$TMP/frame-before.json")" "$PF_HOOK" 'line sits outside its `### framing:job` block'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-after: the line in the block after its own -> deny" 2 "$(cat "$TMP/frame-after.json")" "$PF_HOOK" 'line sits outside its `### framing:job` block'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-misspelt: a task-sha of no hex -> deny" 2 "$(cat "$TMP/frame-misspelt.json")" "$PF_HOOK" 'is not `Framed by: <path> task-sha=<12 hex>`'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-outside: a path outside prompts/ -> deny" 2 "$(cat "$TMP/frame-outside.json")" "$PF_HOOK" 'path memory/builds/bx/spec/x.md is not a repo-relative file under builds/bx/prompts/'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-dotdot: a path holding .. -> deny" 2 "$(cat "$TMP/frame-dotdot.json")" "$PF_HOOK" '/prompts/../prompts/2026-11-23-prompt-T-1-1-prompt-writer.md is not a repo-relative file under builds/bx/prompts/'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-no-file: a path naming no file -> deny" 2 "$(cat "$TMP/frame-no-file.json")" "$PF_HOOK" 'prompts/none.md names no file under'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-no-marker: a file holding no marker -> deny" 2 "$(cat "$TMP/frame-no-marker.json")" "$PF_HOOK" 'prompts/plain.md holds 0 gov:handoff marker lines'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-two-markers: a file holding two markers -> deny" 2 "$(cat "$TMP/frame-two-markers.json")" "$PF_HOOK" 'prompts/twice.md holds 2 gov:handoff marker lines'
  GOV_DEFAULT_BRANCH=pf-unset run_limit_call "rule6 BR92 AC14 frame-other-sha: a task-sha of another render -> deny" 2 "$(cat "$TMP/frame-other-sha.json")" "$PF_HOOK" 'and the `Framed by:` line names 0123456789ab: the framing was cut from another render of it'
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
HOOK=$(build_pack "$TMP/rule6-hooks")
HOREPO="$TMP/horepo"
HO_WF=workflows
mkdir -p "$HOREPO/.claude" "$HOREPO/.governance" "$HOREPO/sub" "$HOREPO/tools/$HO_WF" \
  "$HOREPO/memory/builds/bx/prompts" "$HOREPO/memory/builds/bx/spec"
HOJ="$NODEDIR/horepo"
printf 'const s = await agent("one")\n' > "$HOREPO/tools/$HO_WF/h.js"
printf 'const s = await agent("one")\n' > "$HOREPO/tools/$HO_WF/other.js"
# TOOL-dBoundRoles-25 S3 - A HARNESS IS ADMITTED ONLY AT ITS LANDED BLOB. The checkout is a real repository whose
# `main`, the landed revision where it has no remote, commits every harness the index below declares, a policy
# file holding the agent limit, and settings at it; `HOOKL` is a copy of the pack beside the policy kit, inside
# the checkout as rule 7's own fixtures place it, and every Workflow call that reaches the harness match runs
# through it, so each arm judges the rule it names after the harness is admitted. The Agent arms keep the copy
# with no policy kit beside it.
for _h in h2 h3 h4; do printf 'const s = await agent("one")\n' > "$HOREPO/tools/$HO_WF/$_h.js"; done
printf '[runtime]\nagents-in-flight = 2\n' > "$HOREPO/.governance/policy.toml"
printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$HOREPO/.claude/settings.json"
HOOKL=$(build_pack "$HOREPO/kits"); mkdir -p "$HOREPO/kits/policy"
for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do [ -n "$LIMPK" ] && cp "$ROOTDIR/$LIMPK/$f" "$HOREPO/kits/policy/"; done
( cd "$HOREPO" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
    && git config user.name t && git add -A && git commit -qm landed --no-verify )
# TOOL-dBoundRoles-6 S6: the researcher's `role-sha` is the hash of the role section write_handoff gives
# every handoff below; HO_RSHA2 is that section with one more line, the role text after a body change.
HO_RSHA=$("$TESTPY" -c 'import hashlib; print(hashlib.sha256(b"## Role\n\nYou research.\n\n").hexdigest()[:12])' | tr -d '\r')
HO_RSHA2=$("$TESTPY" -c 'import hashlib; print(hashlib.sha256(b"## Role\n\nYou research.\n\nOne more line.\n\n").hexdigest()[:12])' | tr -d '\r')
HO_ROLES='{"roles":{"gov-researcher":{"agent":true,"role-sha":"'"$HO_RSHA"'","workflow":"research","writes":"none"},"gov-builder":{"agent":true,"workflow":"build","writes":"product"},"gov-session":{"agent":false,"workflow":"handoff","writes":"none"}},"harnesses":["tools/'"$HO_WF"'/h.js"]}'
# TOOL-dBoundRoles-3 S5: the session's card, read through scratch-guard's `readCard`, whose path is the kickoff
# checker's `--card --path --session <sid>` answer. A stub checker sits where the hook copy's kit resolver probes,
# `<hooks dir>/../session-kickoff/`, and names `cards/<sid>.md` under the checkout it runs in; `ho-c1`'s card
# routes T-1, `ho-c2`'s routes T-2 only, and no other session has one.
mkdir -p "$TMP/rule6-hooks/session-kickoff" "$HOREPO/cards"
printf '%s\n' '#!/bin/bash' '[ "$1" = --card ] && [ "$2" = --path ] && [ "$3" = --session ] || exit 2' \
  'printf "%s\n" "$PWD/cards/$4.md"' > "$TMP/rule6-hooks/session-kickoff/manifest-check.sh"
printf '## route\n- build: bx\n- unit: T-1 · spec memory/builds/bx/spec/x.md\n' > "$HOREPO/cards/ho-c1.md"
printf '## route\n- build: bx\n- unit: T-2 · spec memory/builds/bx/spec/x.md\n' > "$HOREPO/cards/ho-c2.md"
printf '## route\n- build: bx\n' > "$HOREPO/cards/ho-c4.md"   # the card a handed fact is cut over (TOOL-dBoundRoles-92)
HO_CWD=""
HO_PROJECT=""
# TOOL-dBoundRoles-50 S16: spec 13 of the tree this suite runs in, the one `write_handoff` hands whole as its
# `s13` variant; its build is spelled from parts, and the memory root is the tree's own conf's.
_b50=dBound; _b50=${_b50}Roles
SG50_MR=$(sed -n 's/^MEMORY_ROOT=//p' "$ROOTDIR/.memory-tree.conf" 2>/dev/null | tr -d '\r' | head -n 1)
SG50_S13=$(ls "$ROOTDIR/${SG50_MR:-memory}/builds/$_b50/spec/"*"-spec-TOOL-$_b50-13.md" 2>/dev/null | head -n 1)
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
def render_marker(p, sec, r="gov-researcher", unit="T-1", item=None, r_sec=None):
    # TOOL-dBoundRoles-17: `item=` sits between `unit=` and `path=` where given; every other variant
    # keeps the six-field marker, the legacy shape the guard still admits.
    tag = " item=%s" % item if item else ""
    return "<!-- gov:handoff role=%s build=bx unit=%s%s path=%s role-sha=%s task-sha=%s -->" % (r, unit, tag, p, h(r_sec or role), h(sec))
def write_prompt_file(rel, m, sec, r_sec=None):
    with open(os.path.join(root, rel), "w", newline="\n") as f:
        f.write("**Serves:** journal T-1\n\n# gov-researcher handoff - T-1\n\n" + m + "\n\n" + (r_sec or role) + sec)
ok, stale, spec = pre + "2026-10-11-prompt-T-1-researcher.md", pre + "2026-10-11-prompt-T-2-researcher.md", "memory/builds/bx/spec/x.md"
M = render_marker(ok, task)
write_prompt_file(ok, M, task)
# TOOL-aOrientedCast-27 - a handoff rendered with no --unit: its marker unit is `-`, its name has no unit part.
nounit = pre + "2026-10-11-prompt-bx-researcher.md"
MN = render_marker(nounit, task, unit="-")
write_prompt_file(nounit, MN, task)
write_prompt_file(stale, render_marker(stale, task), task.replace("rule 4", "rule 5"))
# TOOL-dBoundRoles-17 - a handoff whose marker carries `item=`, as the renderer now writes every one.
itemed = pre + "2026-10-11-prompt-T-1-2-researcher.md"
MI = render_marker(itemed, task, item="item.build.unit")
write_prompt_file(itemed, MI, task)
# TOOL-dBoundRoles-3 - a handoff whose marker carries `item=-`, cut for no item, which no card binds.
dashed = pre + "2026-10-11-prompt-T-1-5-researcher.md"
MD = render_marker(dashed, task, item="-")
write_prompt_file(dashed, MD, task)
write_prompt_file(spec, render_marker(spec, task), task)
# TOOL-dBoundRoles-6 - the handoff re-rendered after the role body gained one line: its role section and
# the role-sha of its marker is the new text; the `ok` handoff above is the one rendered before.
rerendered = pre + "2026-10-11-prompt-T-1-3-researcher.md"
MR = render_marker(rerendered, task, r_sec=role + "One more line.\n\n")
write_prompt_file(rerendered, MR, task, role + "One more line.\n\n")
# TOOL-dBoundRoles-13 - a handoff handing a spec as content under its record: key, the git blob id of the
# spec bytes as they stand when this runs, CRLF folded, so a call after the spec moved cuts it fresh. The content
# sits inside its fence, as the unit 38 render writes it, since TOOL-dBoundRoles-48 S3 denies a handed block
# whose next non-blank line after its fact line opens no fence.
fspec = "memory/builds/bx/spec/fact.md"
fpath = os.path.join(root, fspec)
if not os.path.exists(fpath):
    with open(fpath, "w", newline="\n") as f:
        f.write("The spec line.\n")
with open(fpath, "rb") as f:
    raw = f.read().replace(b"\r\n", b"\n")
fblob = hashlib.sha1(b"blob %d\0" % len(raw) + raw).hexdigest()[:12]
ftask = task + "\n### input:spec\n\n<!-- gov:fact key=record:%s@%s class=claimed -->\n\n```\n%s```\n" % (fspec, fblob, raw.decode("utf-8"))
faced = pre + "2026-10-11-prompt-T-1-4-researcher.md"
MF = render_marker(faced, ftask)
write_prompt_file(faced, MF, ftask)
# TOOL-dBoundRoles-92 - a fact under each other source form: the card of the session ho-c4, cut over its bytes as
# they stand, and one of a session with no card; a key escaping the checkout, spelled four ways; and a spec written
# here for the arm to remove. Each handed block is a fenced line no check reads.
def read_blob(path):
    with open(path, "rb") as f:
        held = f.read().replace(b"\r\n", b"\n")
    return hashlib.sha1(b"blob %d\0" % len(held) + held).hexdigest()[:12]
gone = "memory/builds/bx/spec/gone.md"
with open(os.path.join(root, gone), "w", newline="\n") as f:
    f.write("A spec line.\n")
srcs = {"kcard": "card/ho-c4@" + read_blob(os.path.join(root, "cards", "ho-c4.md")), "kcardless": "card/ho-c8@0123456789ab",
        "kslash": "memory/../../out.md@0123456789ab", "kback": "memory\\..\\..\\out.md@0123456789ab",
        "kroot": "/out.md@0123456789ab", "kdrive": "C:out.md@0123456789ab", "kgone": "%s@%s" % (gone, read_blob(os.path.join(root, gone)))}
forms = {}
for k, (name, src) in enumerate(srcs.items()):
    rel = pre + "2026-11-24-prompt-T-1-%d-researcher.md" % (60 + k)
    sec = task + "\n### input:spec\n\n<!-- gov:fact key=record:%s class=claimed -->\n\n```\nA line.\n```\n" % src
    forms[name] = (render_marker(rel, sec), sec)
    write_prompt_file(rel, *forms[name])
# TOOL-dBoundRoles-38 - handed content fenced: a spec quoting a three-backtick fence that holds a heading and a
# fact line keyed to no file, then a whole marker line, handed under its own record: key inside a four-backtick
# fence; `moved` is that handoff with the quoted marker hand-moved below the fence, `open` one whose task section
# ends inside the fence, each re-hashed so its digest holds.
qspec = "memory/builds/bx/spec/quoted.md"
qmark = render_marker(pre + "2026-10-11-prompt-T-1-9-researcher.md", task)
qraw = ("```\n### input:spec\n\n<!-- gov:fact key=record:memory/builds/tFix/nothing.md@0123456789ab class=claimed -->\n"
        "```\n" + qmark + "\n").encode("utf-8")
with open(os.path.join(root, qspec), "wb") as f:
    f.write(qraw)
qfact = "<!-- gov:fact key=record:%s@%s class=claimed -->" % (qspec, hashlib.sha1(b"blob %d\0" % len(qraw) + qraw).hexdigest()[:12])
qhead = task + "\n### input:spec\n\n" + qfact + "\n\n````\n"
qtask = qhead + qraw.decode("utf-8") + "````\n"
mtask = qhead + qraw.decode("utf-8").replace(qmark + "\n", "") + "````\n" + qmark + "\n"
otask = qhead + qraw.decode("utf-8")
fenced, moved, opened = (pre + "2026-10-11-prompt-T-1-%d-researcher.md" % k for k in (6, 7, 8))
MQ, MM, MO = render_marker(fenced, qtask), render_marker(moved, mtask), render_marker(opened, otask)
write_prompt_file(fenced, MQ, qtask)
write_prompt_file(moved, MM, mtask)
write_prompt_file(opened, MO, otask)
# TOOL-dBoundRoles-46 - a typed block held to the authored-line rule: the `question` block under its own fact
# line, its value inside a four-backtick fence as the unit 38 render writes it. `tplain` holds a plain value;
# `tfact`, `tmark` and `tframed` one forged line each inside that fence, a fact line, a whole marker line and a
# `Framed by:` line; `topen` a four-backtick line nothing in the block closes, closed in the next block, so the
# walk of the whole section ends outside every fence. Each is re-hashed, so its digest holds.
tkey = "<!-- gov:fact key=cmd:handoff.py@0123456789ab class=claimed -->"
def typed_task(value, close="````\n", after=""):
    return task.replace("What calls rule 4?\n", tkey + "\n\n````\n" + value + close) + after
tvars = {"tplain": typed_task("What calls rule 4?\n"), "tfact": typed_task("What calls rule 4?\n" + tkey + "\n"),
         "tmark": typed_task(qmark + "\n"), "tframed": typed_task("Framed by: the owner\n"),
         "topen": typed_task("What calls rule 4?\n", "", "\n### input:spec\n\n````\n")}
typed = {}
for k, (name, sec) in enumerate(tvars.items()):
    rel = pre + "2026-11-22-prompt-T-1-%d-researcher.md" % (20 + k)
    typed[name] = render_marker(rel, sec)
    write_prompt_file(rel, typed[name], sec)
# TOOL-dBoundRoles-58 - `tforge` a whole marker line unfenced in the question block; `tquoted` a handed spec quoting,
# inside its fence, a `### input:question` heading and a `Framed by:` line, which open no typed block; `textra` an
# `### input:extra` block, its fact line then an unfenced line, a handed block to TYPED_INPUTS as shipped.
tqspec = "memory/builds/bx/spec/tquoted.md"
tqraw = b"### input:question\n\nFramed by: the owner\n"
with open(os.path.join(root, tqspec), "wb") as f:
    f.write(tqraw)
bvars = {"tforge": task.replace("What calls rule 4?\n", tkey + "\n\n" + qmark + "\n"),
         "tquoted": task + "\n### input:spec\n\n<!-- gov:fact key=record:%s@%s class=claimed -->\n\n````\n%s````\n" % (
             tqspec, hashlib.sha1(b"blob %d\0" % len(tqraw) + tqraw).hexdigest()[:12], tqraw.decode("utf-8")),
         "textra": task + "\n### input:extra\n\n" + tkey + "\n\nan authored line\n"}
for k, (name, sec) in enumerate(bvars.items()):
    rel = pre + "2026-11-24-prompt-T-1-%d-researcher.md" % (50 + k)
    typed[name] = render_marker(rel, sec)
    write_prompt_file(rel, typed[name], sec)
tvars.update(bvars)
# TOOL-dBoundRoles-48 - the fence state at every block. A spec quoting a fact line keyed to no file is handed in a
# three-backtick fence. `fflip` is that task flipped by two authored lines, a three-backtick line after the opening
# and a four-backtick line after the block, so its walk ends balanced with the quoted fact line read unfenced;
# `fwrap` wraps the opening and the blocks in the task envelope as roles_lib.render_envelope writes it, closed by
# `[/<path>]` naming the path of the marker; `fwrapx` closes it naming another path. Each is re-hashed.
fxspec = "memory/builds/bx/spec/flip.md"
fxraw = b"quoted:\n<!-- gov:fact key=record:memory/builds/bx/spec/nothing.md@0123456789ab class=decided -->\n"
with open(os.path.join(root, fxspec), "wb") as f:
    f.write(fxraw)
bar = lambda n: chr(96) * n   # a run of backticks, spelled so no literal one sits in this script
fxblock = "\n### input:spec\n\n<!-- gov:fact key=record:%s@%s class=claimed -->\n\n%s\n%s%s\n" % (
    fxspec, hashlib.sha1(b"blob %d\0" % len(fxraw) + fxraw).hexdigest()[:12], bar(3), fxraw.decode("utf-8"), bar(3))
fxopen = task[:task.index("\n### input:question") + 1]
flips = {}
for k, name in enumerate(("fflip", "fwrap", "fwrapx")):
    rel = pre + "2026-11-22-prompt-T-1-%d-researcher.md" % (30 + k)
    body = (task + fxblock)[len(fxopen):]
    sec = (fxopen + bar(3) + "\n" + body + "\n" + bar(4) + "\n" if name == "fflip" else
           "## Task\n\n[%s · Level 6 · The task]\n%s%s[/%s]\n" % (rel, fxopen[len("## Task\n\n"):], body,
                                                               rel if name == "fwrap" else pre + "other.md"))
    flips[name] = (render_marker(rel, sec), sec)
    write_prompt_file(rel, *flips[name])
# TOOL-dBoundRoles-50 S16 - spec 13 of the tree this suite runs in, handed whole as the render hands a spec: its
# bytes, CRLF folded, copied into the checkout and keyed by their blob, inside a fence one backtick longer than
# the longest run they hold and at least three, the rule of render_handed_fence. The spec quotes a three-backtick
# fence holding a fact line, so its fence is four long. The variant is written only where argv names the spec.
s13 = {}
if len(sys.argv) > 3 and sys.argv[3] and os.path.isfile(sys.argv[3]):
    import re
    with open(sys.argv[3], "rb") as f:
        sraw = f.read().replace(b"\r\n", b"\n")
    sspec = "memory/builds/bx/spec/s13.md"
    with open(os.path.join(root, sspec), "wb") as f:
        f.write(sraw)
    stext = sraw.decode("utf-8")
    sbar = bar(max([3] + [len(run) + 1 for run in re.findall(bar(1) + "+", stext)]))
    stask = task + "\n### input:spec\n\n<!-- gov:fact key=record:%s@%s class=claimed -->\n\n%s\n%s%s%s\n" % (
        sspec, hashlib.sha1(b"blob %d\0" % len(sraw) + sraw).hexdigest()[:12], sbar, stext,
        "" if stext.endswith("\n") else "\n", sbar)
    srel = pre + "2026-11-23-prompt-T-1-40-researcher.md"
    s13["s13"] = render_marker(srel, stask) + "\n\n" + stask
    write_prompt_file(srel, render_marker(srel, stask), stask)
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
    "item": MI + "\n\n" + task,
    "dash": MD + "\n\n" + task,
    "rerendered": MR + "\n\n" + task,
    "fact": MF + "\n\n" + ftask,
    "fenced": MQ + "\n\n" + qtask,
    "moved": MM + "\n\n" + mtask,
    "open": MO + "\n\n" + otask,
}

prompts.update({name: typed[name] + "\n\n" + sec for name, sec in tvars.items()})
prompts.update({name: mark + "\n\n" + sec for name, (mark, sec) in (*flips.items(), *forms.items())})
prompts.update(s13)
for k, v in prompts.items():
    with open(out + "." + k, "w", newline="") as f:
        f.write(v)
' "$HOREPO" "$TMP/ho" "${SG50_S13:-}"
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
  printf '%s' "$payload" | (cd "$TMP" && node "$HOOKL") >/dev/null 2>"$TMP/err"; got=$?
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
# TOOL-dBoundRoles-17 AC2 — a marker carrying `item=` between `unit=` and `path=` is admitted, its path read
# by name; the six-field cases above are the legacy shape. Against the six-group regex it carries 0 markers.
# Its session's card routes the marker's unit, which TOOL-dBoundRoles-3 S5 requires of an item's work order.
run_spawn "rule6 TOOL-dBoundRoles-17 AC2: a marker carrying item= is admitted" 0 gov-researcher item "" ho-c1
# TOOL-dBoundRoles-3 AC5 — an item's work order bound to its act: it spawns only in a session whose card, named
# by the stub kickoff checker, routes the marker's unit; a handoff whose `item=` is `-` keeps today's exit
# either way. Against checkHandoffSpawn with its binding step cut out, the three refusals are admitted.
run_spawn "rule6 BR3 AC5: an item work order in a session whose card routes T-2 only refused, naming T-1" 2 gov-researcher item "cut for unit T-1" ho-c2
run_spawn "rule6 BR3 AC5: ...and naming the card and the unit it routes" 2 gov-researcher item "cards/ho-c2.md routes T-2" ho-c2
run_spawn "rule6 BR3 AC5: ...and a session with no card refused, naming where readCard looked" 2 gov-researcher item "card does not read" ho-c9
run_spawn "rule6 BR3 AC5: the same work order in a session whose card routes T-1 admitted" 0 gov-researcher item "" ho-c1
run_spawn "rule6 BR3 AC5: an item=- handoff keeps today's exit in the session routing T-2 only" 0 gov-researcher dash "" ho-c2
run_spawn "rule6 BR3 AC5: ...and in the session routing T-1" 0 gov-researcher dash "" ho-c1
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
# TOOL-dBoundRoles-13 AC3 — a handed fact re-cut at the spawn. The `fact` handoff hands the spec fact.md
# under its record: key; the spec then gains one line, so the key the handoff carries moved, and
# write_handoff cuts it fresh. Against checkHandoffSpawn with its fact step cut out, both refusals admit.
write_roles "$HO_ROLES"
run_spawn "rule6 BR13 AC3: a handoff whose handed spec is unchanged is admitted" 0 gov-researcher fact ""
printf 'One more line.\n' >> "$HOREPO/memory/builds/bx/spec/fact.md"
run_spawn "rule6 BR13 AC3: the spec moved after rendering refused, naming its record: key" 2 gov-researcher fact "fact: record:memory/builds/bx/spec/fact.md@"
run_spawn "rule6 BR13 AC3: ...and naming the re-render that cuts it fresh" 2 gov-researcher fact "re-render the handoff, which cuts it fresh"
write_handoff
run_spawn "rule6 BR13 AC3: ...and the handoff re-rendered after the move admitted" 0 gov-researcher fact ""
# TOOL-dBoundRoles-92 AC15 - the other three source forms of the re-cut: the card, read through readCard, a key that
# leaves the checkout, spelled under a slash, a backslash, a leading slash and a drive letter, and a source removed.
# Against checkFactKeys with the card branch cut the first row is refused; with the escape branch, or one test of
# it, cut, a row reads another text; with a missing source read as held, the last is admitted.
run_spawn "rule6 BR92 AC15: a card fact whose card is unchanged is admitted" 0 gov-researcher kcard ""
printf -- '- unit: T-1 · spec memory/builds/bx/spec/x.md\n' >> "$HOREPO/cards/ho-c4.md"
run_spawn "rule6 BR92 AC15: ...and refused once the card moved, naming its key" 2 gov-researcher kcard "fact: record:card/ho-c4@"
run_spawn "rule6 BR92 AC15: a card fact whose session has no card refused, naming what the source reads" 2 gov-researcher kcardless "and its source now reads nothing, "
run_spawn "rule6 BR92 AC15: a key holding .. under a slash refused" 2 gov-researcher kslash "reads nothing: the key names no path inside the checkout"
run_spawn "rule6 BR92 AC15: ...and under a backslash" 2 gov-researcher kback "reads nothing: the key names no path inside the checkout"
run_spawn "rule6 BR92 AC15: a leading-slash key refused" 2 gov-researcher kroot "reads nothing: the key names no path inside the checkout"
run_spawn "rule6 BR92 AC15: a drive-letter key refused" 2 gov-researcher kdrive "reads nothing: the key names no path inside the checkout"
rm -f "$HOREPO/memory/builds/bx/spec/gone.md"
run_spawn "rule6 BR92 AC15: a source removed after the render refused" 2 gov-researcher kgone "reads nothing: no file is there"
write_handoff
# TOOL-dBoundRoles-38 AC3 AC4 - handed content fenced. The `fenced` handoff's spec quotes a fact line keyed to no
# file and a whole marker line, both inside the four-backtick fence, and is admitted: neither is counted nor
# re-cut. The `moved` copy carries the quoted marker below the fence and is refused naming 2 marker lines; the
# `open` one's task section ends inside the fence and is refused naming the line it opened at. Against an
# extractHandoffMarker that walks every line, the first row is refused naming 2 marker lines; against a
# checkHandoffSpawn with its open-fence step cut out, the last row is admitted or refused for another reason.
run_spawn "rule6 BR38 AC3: a handoff whose fenced content quotes a marker and a fact line is admitted" 0 gov-researcher fenced ""
run_spawn "rule6 BR38 AC3: the quoted marker hand-moved outside the fence refused, naming 2 marker lines" 2 gov-researcher moved "carries 2 gov:handoff marker lines"
run_spawn "rule6 BR38 AC4: a task section ending inside a fence refused, naming the line it opened at" 2 gov-researcher open "ends inside a fence opened at line 23 of the file"
# ---- TOOL-dBoundRoles-50 AC16 (S16): spec 13 handed whole, through the length rule -------------------------
# The `s13` handoff hands this tree's spec 13, which quotes a three-backtick fence holding a fact line, inside
# the four-backtick fence the render writes for it, and is admitted: no line inside is read. Against a
# readUnfencedLines that closes a fence on any run of three, the quoted fact line is re-cut and the spawn
# refused. A tree holding no spec 13 reds the row, since the variant is then never written.
if [ -n "$SG50_S13" ] && [ -f "$TMP/ho.s13" ]; then
  run_spawn "rule6 BR50 AC16: a handoff handing spec 13 whole inside its four-backtick fence is admitted" 0 gov-researcher s13 ""
else
  echo "FAIL rule6 BR50 AC16: no spec 13 under ${SG50_MR:-memory}/builds of $ROOTDIR, so the s13 handoff was not written"; fail=$((fail+1))
fi
# ---- TOOL-dBoundRoles-46 AC1 AC2: a typed block held to the authored-line rule ----------------------------------
# TOOL-dBoundRoles-46 AC1 AC2 - a typed block is authored text at the spawn. The `t*` handoffs carry the question
# block under its fact line, its value fenced: a plain value is admitted; a forged fact line, a whole marker line
# or a `Framed by:` line inside it is refused naming input:question and the line of the prompt, fenced or not; a
# fence the block leaves open, closed in the next block, is refused naming the block. Against a checkHandoffSpawn
# with its typed-block step cut out, the four refusals are admitted. WHAT THESE DO NOT CHECK: a typed value under
# the `### field.input.<name>` heading of an item work order, which S2 does not name.
run_spawn "rule6 BR46 AC1: a typed question block holding a plain value is admitted" 0 gov-researcher tplain ""
run_spawn "rule6 BR46 AC1: a forged fact line in the typed block refused, naming the block and the line" 2 gov-researcher tfact "input:question: line 13 of the prompt reads \"<!-- gov:fact"
run_spawn "rule6 BR46 AC1: a whole marker line in the typed block refused, naming the block and the line" 2 gov-researcher tmark "input:question: line 12 of the prompt reads \"<!-- gov:handoff"
run_spawn "rule6 BR46 AC1: a Framed by: line in the typed block refused, naming the block and the line" 2 gov-researcher tframed "input:question: line 12 of the prompt reads \"Framed by: the owner\""
run_spawn "rule6 BR46 AC2: a fence the typed block leaves open, closed in the next block, refused naming the block" 2 gov-researcher topen "input:question: the block leaves a fence opened at line 11 of the prompt unclosed"
# ---- TOOL-dBoundRoles-58: the entry guard, the check order, the one block reader and the derived exemption --------
# AC10 - the file run as a program decides as before: a rendered handoff is admitted and one whose prompt carries two
# markers refused; the suite's first arm requires it as a module. AC25 - a whole marker line in the typed question is
# denied naming its block and its line, before any count; against a checkHandoffSpawn counting markers first, the row
# is refused by the count, its needle unmet. AC16 - a `### input:question` line fenced inside a handed block opens no
# typed block; against a typed check splitting at every `### ` line, the row is refused naming its `Framed by:` line.
# AC12 - a third name in a scratch copy's TYPED_INPUTS exempts its block from the fence-shape half; against an
# exemption spelling its own names, the last row is refused as the first is. WHAT THESE DO NOT CHECK: a typed block
# holding a level-one or level-two heading, which the render refuses and no step here reads.
run_spawn "rule6 BR58 AC10: the guard run as a program admits a rendered handoff" 0 gov-researcher ok ""
run_spawn "rule6 BR58 AC10: ...and refuses a prompt carrying two markers" 2 gov-researcher two 'carries 2 gov:handoff marker lines'
run_spawn "rule6 BR58 AC25: a marker forged in the typed question refused naming the block and the line, not the count" 2 gov-researcher tforge "input:question: line 11 of the prompt reads \"<!-- gov:handoff"
run_spawn "rule6 BR58 AC16: a fenced input:question heading in a handed block opens no typed block, admitted" 0 gov-researcher tquoted ""
run_spawn "rule6 BR58 AC12: an input:extra block holding an unfenced line refused as a handed block" 2 gov-researcher textra "input:extra: line 23 of the file is not the opening line of the handed block's fence"
HOOKX=$(build_pack "$TMP/rule6-typed")
sed "s/^const TYPED_INPUTS = \[/&'extra', /" "$KIT_HOOK" > "$HOOKX"
HOOK="$HOOKX" run_spawn "rule6 BR58 AC12: ...and admitted where a scratch copy's TYPED_INPUTS names extra" 0 gov-researcher textra ""
# TOOL-dBoundRoles-48 AC3 - every block opens outside a fence and a handed block's content lies inside its own. The
# `fflip` handoff, flipped by two authored lines around its handed block so its walk ends balanced, is refused
# naming the quoted fact line it surfaced; the wrapped `fwrap`, ending on the task envelope's closer naming the
# marker's path, is admitted, and `fwrapx`, whose closer names another path, is refused naming that line. Against a
# checkHandoffSpawn without its block-fence step, the first row is refused by the fact re-cut instead, its needle
# unmet, and the last row admitted. WHAT THESE DO NOT CHECK: a flipped section whose surfaced content carries no
# fact line, which S3's rules do not name.
run_spawn "rule6 BR48 AC3: a section flipped around its handed block refused, naming the surfaced fact line" 2 gov-researcher fflip "opening: line 26 of the file reads a fact line no unfenced"
run_spawn "rule6 BR48 AC3: the handoff wrapped in the task envelope, closed naming its own path, admitted" 0 gov-researcher fwrap ""
run_spawn "rule6 BR48 AC3: ...and closed naming another path refused, naming that line" 2 gov-researcher fwrapx "input:spec: line 28 of the file sits between the handed block's fence and the next block"
# AC3 - the pack's TYPED_INPUTS equals handoff.py's INPUT_NAMES less its PATH_INPUTS, both read at run time from
# the roles kit beside this one. Against a TYPED_INPUTS missing a name, or a typed input added to handoff.py
# alone, the row reds; with no roles kit beside this one, it reds, as nothing could be compared.
HO_RK=$(resolve_kit_dir "$TESTPY" roles handoff.py "$HERE") || HO_RK=""
HO_JS=$(cd "$TMP" && node -e 'console.log(require(process.argv[1]).TYPED_INPUTS.slice().sort().join(" "))' "$HOOK" < /dev/null 2>&1 | tr -d '\r')
HO_PY=$([ -n "$HO_RK" ] && "$TESTPY" -c 'import sys; sys.path.insert(0, sys.argv[1]); import handoff
print(" ".join(sorted(n for n in handoff.INPUT_NAMES if n not in handoff.PATH_INPUTS)))' "$ROOTDIR/$HO_RK" 2>&1 | tr -d '\r')
if [ -n "$HO_RK" ] && [ -n "$HO_JS" ] && [ "$HO_JS" = "$HO_PY" ]; then echo "ok   rule6 BR46 AC3: TYPED_INPUTS equals the typed names of handoff.py ($HO_JS)"; pass=$((pass+1))
else echo "FAIL rule6 BR46 AC3: TYPED_INPUTS [$HO_JS] against the typed names of handoff.py [${HO_PY:-no roles kit beside this one}]"; fail=$((fail+1)); fi
# TOOL-dBoundRoles-6 AC4 — role-sha compared at spawn. The index is re-rendered after the researcher's
# body gained one line, so it carries HO_RSHA2; the `ok` handoff was rendered before it and carries
# HO_RSHA. Against checkHandoffSpawn with its role-sha step cut out, the first row is admitted.
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); d["roles"]["gov-researcher"]["role-sha"]=sys.argv[2]; print(json.dumps(d))' "$HO_ROLES" "$HO_RSHA2")"
run_spawn "rule6 BR6 AC4: a handoff rendered before the role body changed refused, naming role-sha" 2 gov-researcher ok "role-sha: the handoff was rendered from role text $HO_RSHA, and gov-researcher was rendered from $HO_RSHA2; re-render the handoff"
run_spawn "rule6 BR6 AC4: ...and the handoff re-rendered from the new text admitted" 0 gov-researcher rerendered ""
# AC5 — an index row without `role-sha` refuses naming the index's re-render; a malformed one is a
# broken index. Against a guard admitting on a missing key, the first row is admitted; against a
# loadRoleIndex passing the key unread, the second is refused by the comparison, not as broken.
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); del d["roles"]["gov-researcher"]["role-sha"]; print(json.dumps(d))' "$HO_ROLES")"
run_spawn "rule6 BR6 AC5: an index holding no role-sha for the type refused, naming the index's re-render" 2 gov-researcher ok 'holds no role-sha for gov-researcher; re-render the index'
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); d["roles"]["gov-researcher"]["role-sha"]="XYZ"; print(json.dumps(d))' "$HO_ROLES")"
run_spawn "rule6 BR6 AC5: a role-sha of XYZ is a broken index, refusing the spawn" 2 gov-researcher ok "role gov-researcher's role-sha is not 12 lowercase hex digits"
# AC3 — an absent index in a governed tree, one whose .claude/agents/ keeps a rendered role agent,
# refuses both tools naming the re-render; the arms of AC5 above, with no agents folder, still admit.
# Against a rule 6 reading an absent index as no rule, both rows are admitted.
write_roles none
mkdir -p "$HOREPO/.claude/agents"
printf -- '---\nname: gov-researcher\ndescription: d\nworkflow: research\nwrites: none\n---\nbody\n' > "$HOREPO/.claude/agents/gov-researcher.md"
run_spawn "rule6 BR6 AC3: no index beside a rendered agent file refuses the spawn, naming the re-render" 2 general-purpose none 'is absent while this tree carries rendered role agents; re-render it with render_agents.py --write'
run_harness "rule6 BR6 AC3: ...and the harness call" 2 "$HO_INLINE" 'is absent while this tree carries rendered role agents'
printf -- '---\nname: adopter-own\ndescription: d\n---\nbody\n' > "$HOREPO/.claude/agents/gov-researcher.md"
run_spawn "rule6 BR6 AC3: an agents folder holding only an adopter's own file is no governed tree, admitted" 0 general-purpose none ""
rm -rf "$HOREPO/.claude/agents"
write_roles "$HO_ROLES"
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

# ---- rule 8: the level a call runs at is its model's (TOOL-aGuardedEffort-1) ----------------------
# Over rule 6's checkout and hook copy, with a hand-written index carrying an `effort` key: the role
# and the one stage are `high` in the default tables and `medium` under the profile `tfam`, and a
# second profile, `tven`, matches `vendor`, so `vendor-tfam-9` is a model two profiles match. Every
# payload is a call rule 6 admits, so rule 8 is what decides. The first transcript ends on a
# sidechain entry, a `<synthetic>` one and a line that is no JSON, which the read walks past.
# CLAUDE_CODE_EFFORT_LEVEL is unset for every arm but the two that name it in E8_LEVEL.
# Against a `main()` with its rule 8 block cut out, every refusal below exits 0 and every
# not-checked line is gone. WHAT THESE DO NOT CHECK: the rendered index, which arm 6 of the roles
# kit's adopter suite runs through this hook, and the word match, which its arm 20 holds.
# TOOL-aGuardedEffort-2 — THE INDEX GREW, and no payload of the arms above the `aGuardedEffort-2`
# line below did: `h.js` still serves `build` alone with its one stage, and those arms keep their
# verdicts. Added: a third agent-true role, `gov-skeptic`, at `medium` where `gov-builder` is `high`;
# `h2.js`, serving `closing` and `spec`, which share the keys `finder` and `synthesis` at different
# levels, the policy's slots being `gov-skeptic` and `gov-builder`, so `spec.synthesis` is `medium`
# in the default stage table while its role's level, and its `unset` level, is `high`; `h3.js`,
# serving `build` and the unkeyed `bare`; and `h4.js`, serving `bare` alone. The tfam transcript
# opens on another model's main-chain entry and holds a `user` record naming that model after the
# tfam entry, so a read walking forward, or one with no `type` test, grades the AC1 arms as unmatched.
E8_ROLES=$("$TESTPY" -c 'import json,sys
d=json.loads(sys.argv[1]); wf="tools/%s/" % sys.argv[2]
d["roles"]["gov-skeptic"]={"agent":True,"workflow":"review","writes":"none"}
d["harnesses"]=[wf+n for n in ("h.js","h2.js","h3.js","h4.js")]
def table(r,s,b,cf,cs,sf,ss):
    return {"roles":{"gov-researcher":r,"gov-builder":r,"gov-skeptic":s},
            "stages":{"build":{"builder":b},"closing":{"finder":cf,"synthesis":cs},"spec":{"finder":sf,"synthesis":ss},"bare":{}}}
d["effort"]={"default":table("high","medium","high","low","high","medium","medium"),
  "profiles":{"tfam":dict(table("medium","medium","medium","medium","medium","low","low"),match=["tfam"]),
              "tven":dict(table("low","low","low","low","low","low","low"),match=["vendor"])},
  "harnesses":{wf+"h.js":["build"],wf+"h2.js":["closing","spec"],wf+"h3.js":["bare","build"],wf+"h4.js":["bare"]},
  "unset":{"build":{"builder":"high"},"closing":{"finder":"medium","synthesis":"high"},"spec":{"finder":"medium","synthesis":"high"},"bare":{}}}
print(json.dumps(d))' "$HO_ROLES" "$HO_WF")
write_roles "$E8_ROLES"
printf '%s\n' '{"type":"assistant","message":{"model":"maker-other-9"}}' \
  '{"type":"assistant","message":{"model":"maker-tfam-9"}}' \
  '{"type":"user","message":{"model":"maker-other-9"}}' \
  '{"type":"assistant","isSidechain":true,"message":{"model":"maker-other-9"}}' \
  '{"type":"assistant","message":{"model":"<synthetic>"}}' 'not json' > "$TMP/e8.tfam.jsonl"
printf '%s\n' '{"type":"assistant","message":{"model":"maker-other-9"}}' > "$TMP/e8.other.jsonl"
printf '%s\n' '{"type":"assistant","message":{"model":"vendor-tfam-9"}}' > "$TMP/e8.two.jsonl"
printf '%s\n' '{"type":"user","message":{"content":"hi"}}' > "$TMP/e8.empty.jsonl"
E8_LEVEL=""
# The knobs of TOOL-aGuardedEffort-2's arms, each empty for the default: E8_H the harness a Workflow
# call names, E8_R its `args.roles` as JSON, E8_TYPE an Agent call's subagent_type, E8_NOT a text
# stderr must not hold, and E8_CWD with E8_HOOK the checkout and the hook copy of the armed rule 7.
E8_H=""; E8_R=""; E8_TYPE=""; E8_NOT=""; E8_CWD=""; E8_HOOK=""
run_effort() { # name expected_exit tool transcript(- for none) extra-json needle(empty: an allow with an empty stderr) [more needles]
  # `extra` is merged into an Agent call's tool_input, and is a Workflow call's `args.efforts` unless null.
  local payload got name=$1 want=$2 miss="" n roles=$E8_R
  [ -n "$roles" ] || roles='{"builder":"gov-builder"}'
  payload=$("$TESTPY" -c 'import json,sys
cwd,tool,tp,extra,pf,h,roles,kind=sys.argv[1:9]
extra=json.loads(extra)
if tool=="Agent":
    ti={"subagent_type":kind,"description":"bx · T-1 · research","prompt":open(pf,newline="").read()}
    ti.update(extra)
else:
    ti={"scriptPath":h,"args":{"roles":json.loads(roles)}}
    if extra is not None: ti["args"]["efforts"]=extra
d={"tool_name":tool,"cwd":cwd,"tool_input":ti}
if tp!="-": d["transcript_path"]=tp
print(json.dumps(d))' "${E8_CWD:-$HOJ/sub}" "$3" "$4" "$5" "$TMP/ho.ok" "${E8_H:-$HO_H}" "$roles" "${E8_TYPE:-gov-researcher}")
  local hk=$HOOK; [ "$3" = Workflow ] && hk=$HOOKL   # a harness call is admitted only at its landed blob (S3)
  printf '%s' "$payload" | (cd "$TMP" && unset CLAUDE_CODE_EFFORT_LEVEL && { [ -z "$E8_LEVEL" ] || export CLAUDE_CODE_EFFORT_LEVEL="$E8_LEVEL"; } && node "${E8_HOOK:-$hk}") >/dev/null 2>"$TMP/err"; got=$?
  shift 5
  if [ -z "$1" ]; then [ ! -s "$TMP/err" ] || miss=" an empty stderr"
  else for n in "$@"; do grep -qF -- "$n" "$TMP/err" || miss="$miss '$n'"; done; fi
  [ -z "$E8_NOT" ] || ! grep -qF -- "$E8_NOT" "$TMP/err" || miss="$miss no '$E8_NOT'"
  if [ "$got" = "$want" ] && [ -z "$miss" ]; then
    echo "ok   $name (exit $got)"; pass=$((pass+1))
  else
    echo "FAIL $name (exit $got, want $want${miss:+, stderr missing$miss})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
}
E8_T="$NODEDIR/e8.tfam.jsonl"; E8_O="$NODEDIR/e8.other.jsonl"
# AC1 — a matched model: no `effort` and the default level are refused, the profile's level admitted.
run_effort "rule8 AC1: no effort on a profiled model refused, naming the profile's level" 2 Agent "$E8_T" '{}' 'and the tfam profile gives it medium on the model "maker-tfam-9" (read from the transcript)'
run_effort "rule8 AC1: ...opening as rule 8 and naming the agent type's level" 2 Agent "$E8_T" '{}' "BLOCKED by spawn-guard: rule 8 (TOOL-aGuardedEffort-1) refused this Agent call — gov-researcher would run at high (its agent type's level"
run_effort "rule8 AC1: ...and the verb that prints the right value" 2 Agent "$E8_T" '{}' 'handoff.py role-efforts --model "maker-tfam-9"'
run_effort "rule8 AC1: the default level passed as effort refused" 2 Agent "$E8_T" '{"effort":"high"}' "would run at high (the call's own"
run_effort "rule8 AC1: the profile's level passed as effort admitted" 0 Agent "$E8_T" '{"effort":"medium"}' ""
# AC2 — an unmatched model is graded against the default tables.
run_effort "rule8 AC2: no effort on an unmatched model admitted" 0 Agent "$E8_O" '{}' ""
run_effort "rule8 AC2: another level on an unmatched model refused, naming the default" 2 Agent "$E8_O" '{"effort":"medium"}' 'the default tables give it high'
# AC3 — a harness call: a stage with no value runs at its agent type's level.
run_effort "rule8 AC3: no efforts on a profiled model refused, naming the stage" 2 Workflow "$E8_T" null 'build: stage builder would run at high'
run_effort "rule8 AC3: ...and the verb that prints the right value" 2 Workflow "$E8_T" null 'handoff.py stage-efforts build --model "maker-tfam-9"'
run_effort "rule8 AC3: the default level passed in efforts refused" 2 Workflow "$E8_T" '{"builder":"high"}' 'expected medium'
run_effort "rule8 AC3: the profile's level passed in efforts admitted" 0 Workflow "$E8_T" '{"builder":"medium"}' ""
run_effort "rule8 AC3: efforts that is a list refused, saying so" 2 Workflow "$E8_T" '["medium"]' 'is present and not a plain object'
# AC4 — the call's own model wins over the transcript's.
run_effort "rule8 AC4: model tfam on another model's transcript graded as tfam" 2 Agent "$E8_O" '{"model":"tfam"}' 'on the model "tfam" (read from the call)'
run_effort "rule8 AC4: ...and admitted at the profile's level" 0 Agent "$E8_O" '{"model":"tfam","effort":"medium"}' ""
run_effort "rule8 AC4: an unmatched model on a tfam transcript admitted with no effort" 0 Agent "$E8_T" '{"model":"other"}' ""
# AC5 — no model read admits with its own line; an index with no `effort` key is not graded.
run_effort "rule8 AC5: no transcript_path admitted, saying so" 0 Agent - '{}' "rule 8 did not check this Agent call's effort level — the payload carries no transcript_path"
run_effort "rule8 AC5: an unreadable transcript admitted, saying so" 0 Agent "$NODEDIR/e8.absent.jsonl" '{}' 'is unreadable (ENOENT)'
run_effort "rule8 AC5: a transcript naming no model admitted, saying so" 0 Agent "$NODEDIR/e8.empty.jsonl" '{}' 'holds no main-chain assistant entry naming a model'
run_effort "rule8 AC5: a harness call with no transcript_path admitted, saying so" 0 Workflow - null "rule 8 did not check this Workflow call's effort level"
# AC11 — a model two profiles match, and a set CLAUDE_CODE_EFFORT_LEVEL on each tool.
run_effort "rule8 AC11: a model two profiles match admitted, naming both" 0 Agent "$NODEDIR/e8.two.jsonl" '{}' 'matches the profiles tfam and tven'
E8_LEVEL=high
run_effort "rule8 AC11: a set CLAUDE_CODE_EFFORT_LEVEL admits an Agent call, naming the variable" 0 Agent "$E8_T" '{}' 'CLAUDE_CODE_EFFORT_LEVEL is set'
run_effort "rule8 AC11: ...and a Workflow call is graded all the same" 2 Workflow "$E8_T" null 'rule 8 (TOOL-aGuardedEffort-1) refused this Workflow call'
E8_LEVEL=""
# ---- TOOL-aGuardedEffort-2: an unset stage is graded at the level of the role the call names -----
# Item 1 — the call's own `roles`, never the policy's slot. Against a loop reading an unset stage's
# level from the `unset` map, the first, third and fourth rows flip their exit and the second names
# `medium` for `finder`, not `high`.
E8_H2="$HOJ/tools/$HO_WF/h2.js"; E8_H3="$HOJ/tools/$HO_WF/h3.js"; E8_H4="$HOJ/tools/$HO_WF/h4.js"
E8_R='{"builder":"gov-skeptic"}'
run_effort "rule8 GE2 item 1: a role swapped for one at another level, no efforts, refused naming the role and its level" 2 Workflow "$E8_O" null "build: stage builder would run at medium (gov-skeptic, its agent type's level; the call's \`efforts\` names no builder), expected high"
run_effort "rule8 GE2 item 1: a role swapped for one at the profile's level, no efforts, admitted" 0 Workflow "$E8_T" null ""
E8_H=$E8_H2 E8_R='{"finder":"gov-builder","synthesis":"gov-builder"}'
run_effort "rule8 GE2 item 1: ...and a swapped role on the two-workflow harness refused, naming it in both workflows" 2 Workflow "$E8_O" null 'closing: stage finder would run at high (gov-builder,' 'spec: stage finder would run at high (gov-builder,'
E8_H="" E8_R='{"other":"gov-builder"}'
run_effort "rule8 GE2 item 1: roles under a key no stage has, no efforts, refused as untyped" 2 Workflow "$E8_O" null "stage builder would run untyped at the session's level (the call's \`roles\` and \`efforts\` name no builder), expected high"
run_effort "rule8 GE2 item 1: ...and admitted with the key's level in efforts" 0 Workflow "$E8_O" '{"builder":"high"}' ""
E8_H=$E8_H2
run_effort "rule8 GE2 item 1: the same omission on the two-workflow harness refused, a line per workflow" 2 Workflow "$E8_O" null 'closing: stage finder would run untyped' 'name no synthesis), expected medium'
run_effort "rule8 GE2 item 1: ...and admitted with one workflow's levels in efforts" 0 Workflow "$E8_O" '{"finder":"medium","synthesis":"medium"}' ""
# Item 2 — the policy's own roles: `spec.synthesis` runs at its role's `high`, and the default stage
# table gives it `medium`. Against a loop reading the default stage table, the refusal is admitted.
E8_R='{"finder":"gov-skeptic","synthesis":"gov-builder"}'
run_effort "rule8 GE2 item 2: the policy's roles, no efforts, a stage whose role level is not its stage level refused" 2 Workflow "$E8_O" null "spec: stage synthesis would run at high (gov-builder, its agent type's level; the call's \`efforts\` names no synthesis), expected medium"
run_effort "rule8 GE2 item 2: ...and admitted with that stage's level in efforts" 0 Workflow "$E8_O" '{"synthesis":"medium"}' ""
# Item 4 — the any-of rule over two workflows, whole workflow by whole workflow. Against a loop
# returning its first workflow's verdict, the first row is refused.
run_effort "rule8 GE2 item 4: efforts right for the second workflow only admitted" 0 Workflow "$E8_O" '{"finder":"medium","synthesis":"medium"}' ""
run_effort "rule8 GE2 item 4: efforts right for neither refused, a line per workflow and both verbs" 2 Workflow "$E8_O" '{"finder":"high","synthesis":"low"}' 'closing: stage finder would run at high' 'spec: stage finder would run at high' '`handoff.py stage-efforts closing --model "maker-other-9"` or `handoff.py stage-efforts spec --model "maker-other-9"`'
run_effort "rule8 GE2 item 4: efforts taking one key's level from each workflow refused" 2 Workflow "$E8_O" '{"finder":"low","synthesis":"medium"}' 'closing: stage synthesis would run at medium' 'spec: stage finder would run at low'
# Item 3 — a workflow with no stage key never admits beside a keyed one, and alone it is the
# not-checked line. Against the empty-object default with the loop over the table's keys, the
# first row is admitted and the second says nothing.
E8_H=$E8_H3 E8_R=""
run_effort "rule8 GE2 item 3: a keyed and an unkeyed workflow, levels wrong for the keyed one, refused naming it alone" 2 Workflow "$E8_O" '{"builder":"low"}' 'build: stage builder would run at low' 'Pass `efforts` as `handoff.py stage-efforts build --model "maker-other-9"` prints it'
E8_H=$E8_H4
run_effort "rule8 GE2 item 3: a harness whose only workflow is unkeyed admitted, saying so" 0 Workflow "$E8_O" null "rule 8 did not check this Workflow call's effort level — the effort tables of" 'hold no stage key for bare, which the harness'
E8_H=""
# Item 7 — the order. A spawn rule 6 refuses, whose role the effort tables also lack, is answered
# by rule 6. Against a main() running rule 8's block first, the refusal is rule 8's throw.
E8_TYPE=general-purpose E8_NOT='rule 8'
run_effort "rule8 GE2 item 7: a general-purpose spawn over the effort index is refused by rule 6, with no rule 8 text" 2 Agent "$E8_T" '{}' 'is not an agent-true role'
if [ "$(head -c 30 "$TMP/err")" = 'BLOCKED by spawn-guard: rule 6' ]; then echo "ok   rule8 GE2 item 7: ...and its stderr opens as rule 6's, under the pack's prefix (BR25 AC1)"; pass=$((pass+1))
else echo "FAIL rule8 GE2 item 7: the refusal does not open 'BLOCKED by spawn-guard: rule 6'"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
E8_TYPE="" E8_NOT=""
# ...and a harness call whose level differs, in the armed rule 7 section's checkout, whose settings
# are put above the landed limit: rule 8 answers, before rule 7. The index is written there after
# that section's arms. Against a main() running rule 8's block after rule 7's, the refusal is rule 7's.
if [ -z "${R7:-}" ]; then
  echo "FAIL rule8 GE2 item 7: no policy kit beside this hooks kit, so no checkout arms rule 7 for the order arm"; fail=$((fail+1))
else
  printf '%s' "$E8_ROLES" > "$R7/.claude/roles.json"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"3","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"3"}}\n' > "$R7/.claude/settings.json"
  E8_CWD="$NODEDIR/r7" E8_HOOK="$R7_HOOK" E8_H="$NODEDIR/r7/tools/$HO_WF/h.js" E8_NOT='rule 7'
  run_effort "rule8 GE2 item 7: settings above the limit and a level that differs are refused by rule 8, with no rule 7 text" 2 Workflow "$E8_T" null 'rule 8 (TOOL-aGuardedEffort-1) refused'
  E8_CWD="" E8_HOOK="" E8_H="" E8_NOT=""
  rm -f "$R7/.claude/roles.json"
fi
# Item 3 — the tables agree on one population of stage keys. A matched table with no `stages` entry
# for a workflow, and an `unset` lacking one key, each throw, and main() names a re-render. Against
# the empty-object default with the loop over the table's keys, both calls are admitted.
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); del d["effort"]["default"]["stages"]["build"]; print(json.dumps(d))' "$E8_ROLES")"
run_effort "rule8 GE2 item 3: a matched table with no stages entry for the workflow refused, naming a re-render" 2 Workflow "$E8_O" '{"builder":"high"}' 'disagree on stage builder of build' 'render_agents.py --write'
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); del d["effort"]["unset"]["build"]["builder"]; print(json.dumps(d))' "$E8_ROLES")"
run_effort "rule8 GE2 item 3: an unset map lacking one stage key refused, naming a re-render" 2 Workflow "$E8_O" '{"builder":"high"}' 'disagree on stage builder of build' 'render_agents.py --write'
# A role the effort tables do not hold: the rule throws and main() refuses, naming a re-render.
write_roles "$("$TESTPY" -c 'import json,sys; d=json.loads(sys.argv[1]); del d["effort"]["default"]["roles"]["gov-researcher"]; print(json.dumps(d))' "$E8_ROLES")"
run_effort "rule8: a role the effort tables lack refused, naming a re-render" 2 Agent "$E8_T" '{}' 'render_agents.py --write'
# An index with no `effort` key adds no rule: the call AC1 refuses is admitted with an empty stderr.
write_roles "$HO_ROLES"
run_effort "rule8 AC5: an index with no effort key grades nothing" 0 Agent "$E8_T" '{}' ""
# AC8 — an `effort` that is not the shape is a broken index, which refuses both tools. Against a
# loadRoleIndex returning the key unread, neither refusal is the broken index's.
write_roles "${HO_ROLES%\}},\"effort\":[]}"
run_effort "rule8 AC8: an effort that is a list refuses the spawn as a broken index" 2 Agent "$E8_T" '{"effort":"medium"}' 'effort is not'
run_effort "rule8 AC8: ...and the harness call" 2 Workflow "$E8_T" '{"builder":"medium"}' 'effort is not'
# TOOL-aGuardedEffort-2 item 9 — the four keys, each a plain object. Against a loader holding the
# outer plain-object test alone, each index is read as ok and the refusal is rule 8's throw.
write_roles "${HO_ROLES%\}},\"effort\":{\"default\":{},\"profiles\":{},\"harnesses\":{}}}"
run_effort "rule8 GE2 item 9: an effort holding three of its four keys refuses as a broken index" 2 Agent "$E8_T" '{"effort":"medium"}' 'effort is not'
write_roles "${HO_ROLES%\}},\"effort\":{\"default\":[],\"profiles\":{},\"harnesses\":{},\"unset\":{}}}"
run_effort "rule8 GE2 item 9: an effort whose default is a list refuses as a broken index" 2 Agent "$E8_T" '{"effort":"medium"}' 'effort is not'
write_roles none


# ---- TOOL-dBoundRoles-25 AC4 AC5 AC6: a declared harness is admitted only at its landed blob ------------
# A repository with a bare remote whose `main` holds the declared harness, the pack and its kits committed
# inside it as rule 7's fixtures place them, its policy file holding the agent limit and its settings at it.
# The landed revision is `origin/main`, which `readLandedRevision` reads through the policy kit's shim. The
# harness edited in the working tree is refused naming the path and the landed sha's first eight digits;
# the edit committed and not pushed is refused the same way; the landed bytes restored are admitted. A
# second declared harness present in the working tree and absent at the landed revision is refused as not
# landed. Against an admission that compares with HEAD, the committed edit is admitted; against one that
# matches the path alone, every edited row is admitted; against one reading a missing blob as equal, the
# not-landed row is admitted. WHAT THESE DO NOT CHECK: a harness whose landed bytes differ only by a filter
# the repository does not declare, which `git hash-object` reads as the repository does.
if [ -z "$LIMPK" ] || [ -z "$ROOTDIR" ]; then
  echo "FAIL BR25 AC4: no policy kit beside this kit, so no landed revision can be read"; fail=$((fail+1))
else
  LB="$TMP/lb"; LBR="$TMP/lb-remote.git"; LBJ="$NODEDIR/lb"
  mkdir -p "$LB/.claude" "$LB/.governance" "$LB/$LBW"
  LB_HOOK=$(build_pack "$LB/kits"); mkdir -p "$LB/kits/policy"
  for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do cp "$ROOTDIR/$LIMPK/$f" "$LB/kits/policy/"; done
  printf '[runtime]\nagents-in-flight = 2\n' > "$LB/.governance/policy.toml"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$LB/.claude/settings.json"
  printf '%s\n' '{"roles":{"gov-builder":{"agent":true,"workflow":"build","writes":"product"}},"harnesses":["'"$LBW"'/h.js","'"$LBW"'/h5.js"]}' > "$LB/.claude/roles.json"
  printf 'const s = await agent("one")\n' > "$LB/$LBW/h.js"
  git init -q --bare "$LBR"
  ( cd "$LB" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
      && git config user.name t && git config core.autocrlf false && git add -A && git commit -qm landed --no-verify \
      && git remote add origin "$LBR" && git push -q origin main 2>/dev/null )
  LB_L8=$(git -C "$LB" rev-parse origin/main | cut -c1-8)
  run_landed_call() { # harness path from the checkout root; its stderr in $TMP/err, its exit the hook's
    printf '%s' '{"tool_name":"Workflow","cwd":"'"$LBJ"'","tool_input":{"scriptPath":"'"$LBJ/$1"'","args":{"roles":{"builder":"gov-builder"}}}}' \
      | (cd "$TMP" && node "$LB_HOOK") >/dev/null 2>"$TMP/err"
  }
  run_landed() { # name expected_exit harness-file [text stderr must carry ...]
    local name=$1 want=$2 h=$3 got miss="" n; shift 3
    run_landed_call "$LBW/$h"; got=$?
    for n in "$@"; do grep -qF -- "$n" "$TMP/err" || miss="$miss '$n'"; done
    if [ "$got" = "$want" ] && [ -z "$miss" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
    else echo "FAIL $name (exit $got, want $want${miss:+, stderr missing$miss})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
  }
  run_landed "BR25 AC4 LIVENESS the landed harness is admitted" 0 h.js
  printf 'const s = await agent("two")\n' > "$LB/$LBW/h.js"
  run_landed "BR25 AC4 the harness edited in the working tree is refused, naming the path and the landed sha" 2 h.js \
    'BLOCKED by spawn-guard: rule 6' "harness $LBW/h.js differs from its blob at the landed revision $LB_L8"
  ( cd "$LB" && git commit -qam edit --no-verify )
  run_landed "BR25 AC4 ...and the edit committed and not pushed is refused all the same" 2 h.js "differs from its blob at the landed revision $LB_L8"
  ( cd "$LB" && git reset -q --hard origin/main )
  run_landed "BR25 AC4 ...and the landed bytes restored are admitted" 0 h.js
  printf 'const s = await agent("five")\n' > "$LB/$LBW/h5.js"
  run_landed "BR25 AC5 a declared harness in the working tree and absent at the landed revision is refused as not landed" 2 h5.js \
    "harness $LBW/h5.js is not landed at $LB_L8"

  # ---- TOOL-dBoundRoles-88: every declared harness a landed harness nests is held to its landed blob too ----
  # One landing holds every fixture: h.js, h5.js and h6.js nest one another in a cycle; h7.js nests by a
  # variable, h8.js a path outside the index, h9.js spells a nested call on a comment line alone; and every
  # harness gov's own index declares sits at its path with its bytes. Against a hold that runs
  # checkHarnessLanded on the entry alone, the edited-callee, transitive and real-held rows are admitted;
  # against a scan that returns no callee, those and the two unplaced rows are; against one that reads comment
  # lines, the comment row and the real liveness row are refused. The real-held row derives its pairs with its
  # own grep, never through the guard's reader. WHAT THESE DO NOT CHECK: a nested call the text scan cannot see
  # (the pack's NESTED CEILING), and a nested file edited after admission.
  BR88_REAL=$("$TESTPY" -c 'import json,sys; print("\n".join(json.load(open(sys.argv[1], encoding="utf-8"))["harnesses"]))' "$ROOTDIR/.claude/roles.json" | tr -d '\r')
  printf 'const s = await workflow({ scriptPath: "%s/h5.js" }, {})\n' "$LBW" > "$LB/$LBW/h.js"
  printf "const s = await workflow(\n  { scriptPath: './%s/h6.js', },\n  {},\n)\n" "$LBW" > "$LB/$LBW/h5.js"
  printf 'const s = await workflow({ scriptPath: "%s/h.js" }, {})\n' "$LBW" > "$LB/$LBW/h6.js"
  printf 'const p = "%s/h.js"\n// a comment\nconst s = await workflow({ scriptPath: p })\n' "$LBW" > "$LB/$LBW/h7.js"
  printf 'const s = await workflow({ scriptPath: "%s/elsewhere.js" })\n' "$LBW" > "$LB/$LBW/h8.js"
  printf '  // the runtime provides workflow({scriptPath}, args)\nconst s = await agent("nine")\n' > "$LB/$LBW/h9.js"
  for h in $BR88_REAL; do mkdir -p "$LB/$(dirname "$h")"; cp "$ROOTDIR/$h" "$LB/$h"; done
  "$TESTPY" -c 'import json,sys
p, w, real = sys.argv[1], sys.argv[2], sys.argv[3].split()
i = json.load(open(p, encoding="utf-8"))
i["harnesses"] = [f"{w}/h{n}.js" for n in ("", 5, 6, 7, 8, 9)] + real
json.dump(i, open(p, "w", encoding="utf-8"))' "$LB/.claude/roles.json" "$LBW" "$BR88_REAL"
  ( cd "$LB" && git add -A && git commit -qm nested --no-verify && git push -q origin main 2>/dev/null )
  LB_L8=$(git -C "$LB" rev-parse origin/main | cut -c1-8)
  run_landed "BR88 LIVENESS three landed harnesses that nest one another in a cycle are admitted, and the walk ends" 0 h.js
  printf '// edited\n' >> "$LB/$LBW/h5.js"
  run_landed "BR88 a landed harness whose callee is edited is refused, naming the callee, the landed sha and the caller" 2 h.js \
    "harness $LBW/h5.js differs from its blob at the landed revision $LB_L8" "Harness $LBW/h.js runs it"
  ( cd "$LB" && git reset -q --hard origin/main )
  printf '// edited\n' >> "$LB/$LBW/h6.js"
  run_landed "BR88 ...and one whose callee's callee is edited, naming that callee and its own caller" 2 h.js \
    "harness $LBW/h6.js differs from its blob at the landed revision $LB_L8" "Harness $LBW/h5.js runs it"
  ( cd "$LB" && git reset -q --hard origin/main )
  run_landed "BR88 a nested call whose path is no literal is refused, naming the line" 2 h7.js "harness $LBW/h7.js line 3 nests workflow("
  run_landed "BR88 a nested call naming no declared harness is refused, naming the path" 2 h8.js \
    "harness $LBW/h8.js line 1 nests $LBW/elsewhere.js, which is not a declared harness"
  run_landed "BR88 a comment line spelling the nested call is no nested call" 0 h9.js
  br88_bad=""
  for h in $BR88_REAL; do run_landed_call "$h" || br88_bad="$br88_bad $h($(head -1 "$TMP/err" | cut -c1-200))"; done
  if [ -n "$BR88_REAL" ] && [ -z "$br88_bad" ]; then echo "ok   BR88 LIVENESS every harness gov's index declares, landed, is admitted"; pass=$((pass+1))
  else echo "FAIL BR88 LIVENESS every harness gov's index declares, landed, is admitted (refused:${br88_bad:- the index declares none})"; fail=$((fail+1)); fi
  # Each `workflow(` line of a declared harness that opens no comment owes a pair: the scriptPath literal on it
  # or the two lines under it, edited in the fixture, refuses a call to the harness holding the line.
  br88_bad=""; br88_pairs=0
  for h in $BR88_REAL; do
    for ln in $(grep -nE '\bworkflow[[:space:]]*\(' "$ROOTDIR/$h" | grep -vE '^[0-9]+:[[:space:]]*//' | cut -d: -f1); do
      callee=$(sed -n "$ln,$((ln+2))p" "$ROOTDIR/$h" | sed -nE "s/.*scriptPath[[:space:]]*:[[:space:]]*['\"]([^'\"]+)['\"].*/\1/p" | head -1)
      if [ -z "$callee" ] || [ ! -f "$LB/$callee" ]; then br88_bad="$br88_bad $h:$ln(no pair)"; continue; fi
      br88_pairs=$((br88_pairs+1))
      printf '// edited\n' >> "$LB/$callee"
      run_landed_call "$h"; got=$?
      if [ "$got" != 2 ] || ! grep -qF -- "harness $callee differs from its blob at the landed revision $LB_L8" "$TMP/err"; then br88_bad="$br88_bad $h->$callee(exit $got)"; fi
      ( cd "$LB" && git reset -q --hard origin/main )
    done
  done
  if [ "$br88_pairs" -gt 0 ] && [ -z "$br88_bad" ]; then echo "ok   BR88 each harness gov's declared harnesses nest, edited, refuses its landed caller"; pass=$((pass+1))
  else echo "FAIL BR88 each harness gov's declared harnesses nest, edited, refuses its landed caller ($br88_pairs pairs;$br88_bad)"; fail=$((fail+1)); fi

  # AC6 (gap-roles-25): an adopter layout at prefix `scripts`, its index naming gov's review harness there,
  # landed, is admitted; so is a CRLF checkout of the same LF blob, read through the repository's clean filter.
  AD="$TMP/ad"; ADR="$TMP/ad-remote.git"; ADJ="$NODEDIR/ad"
  mkdir -p "$AD/.claude" "$AD/.governance" "$AD/scripts/$WKN"
  AD_HOOK=$(build_pack "$AD/scripts"); mkdir -p "$AD/scripts/policy"
  for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do cp "$ROOTDIR/$LIMPK/$f" "$AD/scripts/policy/"; done
  printf '[runtime]\nagents-in-flight = 2\n' > "$AD/.governance/policy.toml"
  printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$AD/.claude/settings.json"
  printf '%s\n' '{"roles":{"gov-reviewer":{"agent":true,"workflow":"review","writes":"none"}},"harnesses":["scripts/'"$WKN"'/tier2-review.js"]}' > "$AD/.claude/roles.json"
  printf 'const a = 1\nconst b = await agent("x")\n' > "$AD/scripts/$WKN/tier2-review.js"
  git init -q --bare "$ADR"
  ( cd "$AD" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
      && git config user.name t && git config core.autocrlf false && git add -A && git commit -qm landed --no-verify \
      && git remote add origin "$ADR" && git push -q origin main 2>/dev/null )
  run_adopter_call() { # name expected_exit
    local got
    printf '%s' '{"tool_name":"Workflow","cwd":"'"$ADJ"'","tool_input":{"scriptPath":"'"$ADJ/scripts/$WKN/tier2-review.js"'","args":{"roles":{"finder":"gov-reviewer"}}}}' \
      | (cd "$TMP" && node "$AD_HOOK") >/dev/null 2>"$TMP/err"; got=$?
    if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
    else echo "FAIL $1 (exit $got, want $2)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
  }
  run_adopter_call "BR25 AC6 an adopter at prefix scripts calling its landed tier2-review.js is admitted" 0
  git -C "$AD" config core.autocrlf true
  printf 'const a = 1\r\nconst b = await agent("x")\r\n' > "$AD/scripts/$WKN/tier2-review.js"
  run_adopter_call "BR25 AC6 ...and a CRLF checkout of the same LF blob is admitted, through the clean filter" 0
fi

n=$((pass+fail))
# 187 (TOOL-dBoundRoles-43), the base: that unit owed the suite a floor and pinned none, so TOOL-dBoundRoles-62
# counted it, every assertion but those of the terms below. A shrink-only pin on the EXECUTED count: an arm stranded
# past an early exit leaves the suite green with no floor. Base and terms are DERIVED by reading each assertion call
# site from source, one per execution, so a site in a loop counts once per item of its literal list, and every helper
# here asserts once per call. No arm of this suite skips: a missing kit is a FAIL. The comparison reads `$pass`, since
# a failed assertion reds the run on its own (TOOL-dBoundRoles-66). The close's run is the executed observation. It
# does NOT CHECK that an executed arm can fail.
# +1 for spec 13 handed whole to the guard (TOOL-dBoundRoles-50).
# +6 for the entry guard, the check order, the one block reader and the derived exemption (TOOL-dBoundRoles-58).
# +8 for the nested harnesses held to their landed blobs, one per row (TOOL-dBoundRoles-88).
# +20 for the twelve framing refusals and the eight rows of the other fact sources (TOOL-dBoundRoles-92).
# The pin sits alone on its line because the testsuite-counts leg reads it anchored.
FLOOR_ASSERTIONS=222
[ "$pass" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL $pass assertions passed against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]
