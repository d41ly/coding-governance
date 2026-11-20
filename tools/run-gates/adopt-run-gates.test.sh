#!/usr/bin/env bash
# adopt-run-gates.test.sh — the run-gates adopter, gated on EFFECTS. the run-gates promotion spec's S7.
#
# WHY EFFECTS AND NOT EXIT CODES. The adopter READS a target's declaration and can WRITE, so an
# exit-code-only arm certifies the verb by its own report. This repo already paid for that once: a
# Tier-2 review found 4 of 7 defects, one a blocker, in the single file no leg executed. Every arm
# below asserts a MESSAGE or an on-disk state, and the refusal arms additionally assert that nothing
# was written.
#
# AC6's CONTROL LIVES HERE. `adopt-run-gates.sh --check` in gov's own tree exits 0 reporting
# NOT ADOPTED — and so would a --check that did nothing whatever. The mutation arm is what
# distinguishes them: it edits the runner's printf out from under a real declaration and asserts the
# red. Without it the criterion is satisfied by a no-op.
set -u
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "adopt-e2e: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
KIT="${KIT_REL##*/}"
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "adopt-e2e: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
KITDIR=$(cd "$(dirname "$0")" && pwd)
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
ADOPT="$KITDIR/adopt-run-gates.sh"

# The resolver, INLINE, byte-identical to the canonical blocks its marker lines name, which
# resolve-python.test.sh holds every copy to: arm 8 runs python, and `../lib/` is gov's.
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
PY=$(resolve_python) || exit 2

FLOOR_ASSERTIONS=23
# RAISED 17 -> 23 by TOOL-dWitnessedBar-56 on 2026-11-20 for TOOL-dWitnessedBar-45, whose pass left the
# floor where it was: section 8's six, the no-govkit target's one, AC1's two, AC2's two and AC3's one.
# Counted one per `ok … || nope` pair; this pass runs no suite.
n=0
bad=0
ok()   { n=$((n+1)); echo "  ok   — $1"; }
nope() { n=$((n+1)); echo "  FAIL — $1"; bad=1; }

TMP=$(mktemp -d) || { echo "adopt-e2e: cannot create a scratch dir"; exit 2; }
trap 'rm -rf "$TMP"' EXIT

# A scratch TARGET carrying the kit at a DIFFERENT prefix from gov's, so nothing here can pass by
# accidentally resolving gov's own paths.
build_target() { # <name> <prefix> -> echoes the target root
  local t="$TMP/$1" pfx="$2"
  mkdir -p "$t/$pfx/run-gates" "$t/.governance"
  ( cd "$t" && git init -q . && git config user.email e@x && git config user.name t ) >/dev/null 2>&1
  cp "$KITDIR/run-gates.sh" "$t/$pfx/${KIT}/run-gates.sh"
  cp "$ADOPT"               "$t/$pfx/${KIT}/adopt-run-gates.sh"
  printf '[]\n' > "$t/$pfx/gate-legs.json"
  ( cd "$t" && git add -A && git commit -qm init ) >/dev/null 2>&1
  printf '%s' "$t"
}
write_decl() { # <target> <prefix> <ran-head> — writes the [gate_runner] declaration AND commits it, so a
         # later `git status --porcelain` reports what the ADOPTER wrote and not the fixture.
  cat > "$1/.governance/deploy.toml" <<TOML
prefix = "$2"
[gate_runner]
kind = "manifest"
observed_ran = ["$3{name}"]
observed_failed = ["GATE FAIL  {name}"]
TOML
  ( cd "$1" && git add -A && git commit -qm decl ) >/dev/null 2>&1
}

echo "== 1. NOT ADOPTED is a real answer, and it writes nothing =="
T=$(build_target notadopted vendor)
out=$( cd "$T" && bash vendor/${KIT}/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'NOT ADOPTED' \
  && ok "no deploy.toml -> exit 0 reporting NOT ADOPTED" \
  || nope "no deploy.toml did not report NOT ADOPTED (rc=$rc): $out"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${bad:-0}" = 0 ] && echo "PASS ($n assertions)" || echo "FAIL ($n assertions)"; [ "${bad:-0}" = 0 ] && exit 0; exit 1; fi
[ -z "$( cd "$T" && git status --porcelain )" ] \
  && ok "the NOT ADOPTED path left the target byte-identical" \
  || nope "the NOT ADOPTED path wrote into the target"

echo "== 2. a matching declaration agrees, at a NON-gov prefix =="
T=$(build_target agree vendor)
write_decl "$T" vendor 'GATE ok    '
out=$( cd "$T" && bash vendor/${KIT}/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 0 ] && ok "a declaration matching the runner's printf exits 0" \
  || nope "a matching declaration did not exit 0 (rc=$rc): $out"
printf '%s' "$out" | grep -q 'observed_ran' \
  && ok "the agreeing report names the key it checked" \
  || nope "the agreeing report does not name observed_ran: $out"
[ -z "$( cd "$T" && git status --porcelain )" ] \
  && ok "--check wrote nothing on the agreeing path" \
  || nope "--check wrote into the target on the agreeing path"

echo "== 3. AC5 — the MUTATION arm, which is what makes arm 1 mean anything =="
T=$(build_target drift vendor)
write_decl "$T" vendor 'GATE ok    '
# Move the runner's output string out from under the declaration, exactly as a later unit editing
# the report verbs would. In-process `sed`, not a nested `python` heredoc: the heredoc form was
# measured SILENTLY FAILING on this host — the nested interpreter's fork dies with a cygwin
# signal-pipe error, the edit never lands, and the arm below then passes by finding the very string
# it was supposed to have removed. A mutation arm whose mutation does not happen is the
# fixture-passes-by-finding-nothing class sitting inside the arm written to prevent it, so the
# mutation is ASSERTED before the adopter is asked anything.
MUT="$T/vendor/${KIT}/run-gates.sh"
sed -i 's/GATE ok    /GATE PASSED  /g' "$MUT"
if grep -q 'GATE PASSED  ' "$MUT" && ! grep -q 'GATE ok    ' "$MUT"; then
  ok "the fixture mutation actually landed (so the arm below is not vacuous)"
else
  nope "the fixture mutation did NOT land, so the drift arm would prove nothing"
fi
out=$( cd "$T" && bash vendor/${KIT}/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 1 ] && ok "a declaration the runner no longer emits exits 1" \
  || nope "the drifted declaration did not exit 1 (rc=$rc): $out"
if printf '%s' "$out" | grep -q 'DRIFT' && printf '%s' "$out" | grep -q 'observed_ran'; then
  ok "the drift report says DRIFT and NAMES observed_ran (AC5)"
else
  nope "the drift report does not tie DRIFT to observed_ran: $out"
fi

echo "== 4. a declaration with the key ABSENT is reported, not read as agreement =="
T=$(build_target absentkey vendor)
cat > "$T/.governance/deploy.toml" <<'TOML'
prefix = "vendor"
[gate_runner]
kind = "manifest"
observed_ran = ["GATE ok    {name}"]
TOML
out=$( cd "$T" && bash vendor/${KIT}/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'observed_failed' \
  && ok "a missing observed_failed is reported by name, not read as empty-equals-empty" \
  || nope "a missing observed_failed was not reported (rc=$rc): $out"

echo "== 5. it REFUSES across two trees rather than writing a prefix the target cannot resolve =="
T=$(build_target foreign vendor)
out=$( bash "$ADOPT" --check --target "$T" 2>&1 ); rc=$?
[ "$rc" = 2 ] && printf '%s' "$out" | grep -q 'REFUSING' \
  && ok "a kit outside the named target refuses with exit 2" \
  || nope "a cross-tree adopt did not refuse (rc=$rc): $out"
[ -z "$( cd "$T" && git status --porcelain )" ] \
  && ok "the refusal left the target byte-identical" \
  || nope "the refusal wrote into the target"

echo "== 6. a --target that does not exist refuses before reading anything =="
out=$( bash "$ADOPT" --check --target "$TMP/no-such-tree" 2>&1 ); rc=$?
[ "$rc" = 2 ] && ok "an absent --target exits 2" \
  || nope "an absent --target did not exit 2 (rc=$rc): $out"

echo "== 6b. a SCALAR observed_* is refused, because the deployer's reader ITERATES it =="
T=$(build_target scalarform vendor)
cat > "$T/.governance/deploy.toml" <<'TOML'
prefix = "vendor"
[gate_runner]
kind = "manifest"
observed_ran = "GATE ok    {name}"
observed_failed = "GATE FAIL  {name}"
TOML
out=$( cd "$T" && bash vendor/${KIT}/adopt-run-gates.sh --check 2>&1 ); rc=$?
if [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'must be an ARRAY'; then
  ok "a scalar observed_* is refused by name (closing review D2/D1)"
else
  nope "a scalar observed_* was not refused (rc=$rc): $out"
fi
# ...and the control: the SAME heads in ARRAY form, with the SAME runner, must pass. Without this
# the arm above is satisfied by an adopter that refuses every declaration it is given.
T=$(build_target arrayform vendor)
write_decl "$T" vendor 'GATE ok    '
out=$( cd "$T" && bash vendor/${KIT}/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 0 ] && ok "the same heads in ARRAY form still pass (the refusal is about the shape)"   || nope "the array form did not pass (rc=$rc): $out"

echo "== 6c. --help terminates and prints usage =="
out=$( timeout 10 bash "$ADOPT" --help 2>&1 ); rc=$?
[ "$rc" = 2 ] && printf '%s' "$out" | grep -q 'usage:'   && ok "--help prints usage and exits 2 rather than spinning on an undefined function"   || nope "--help did not terminate cleanly (rc=$rc): $out"

echo "== 7. the adopter derives its own prefix — no gov path is spelled in it =="
grep -qE '^\s*KITDIR=\$\(cd "\$\(dirname "\$0"\)" && pwd\)' "$ADOPT" \
  && ok "the kit dir is derived from the script's own location" \
  || nope "the adopter does not derive its kit dir"
# ANY path head before the kit's own directory, not this install's: at a root install `${PFX}` is
# empty and the old predicate matched every bare mention of the kit (VERIFYING repair).
grep -qE '[A-Za-z0-9_.-]/'"${KIT}"'/' "$ADOPT" \
  && nope "the adopter SPELLS a gov install prefix, which lands a dead path in an adopter's tree" \
  || ok "the adopter spells no install prefix"

echo "== 8. TOOL-dWitnessedBar-45 — the leg factory where no govkit sits, as in every adopter =="
# A scratch target applied with THIS kit alone, by the deployer itself, so it holds what an adopter
# receives and no govkit. The deployer is found through the factory's own inline resolver, and the
# target's kit dir through its own index, so no kit path is spelled. Staged red by removing the
# factory row's `when` in this kit's descriptor and committing it, since apply lands committed bytes:
# regen then runs the factory's check there and `--check` exits 1.
export PYTHONDONTWRITEBYTECODE=1
KID=$(sed -n 's/^id = "\(.*\)"$/\1/p' "$KITDIR/kit.toml")
GK=$( cd "$KITDIR" && "$PY" -c 'import leg_factory as f; print((f.resolve_kit_dir(f.GOVKIT_HOME, "govkit.py", f.HERE) / "govkit.py").as_posix())' 2>&1 ) || GK=""
T="$TMP/nogovkit"
mkdir -p "$T"
( cd "$T" && git init -q . && git config user.email e@x && git config user.name t && git commit -q --allow-empty -m init ) >/dev/null 2>&1
out=$( [ -n "$GK" ] && "$PY" "$GK" intake --target "$T" --kits "$KID" 2>&1 \
  && ( cd "$T" && git add -A && git commit -qm intake ) >/dev/null 2>&1 \
  && "$PY" "$GK" apply --target "$T" --kits "$KID" 2>&1 \
  && ( cd "$T" && git add -A && git commit -qm apply ) >/dev/null 2>&1 ); rc=$?
TK=$( cd "$T" && git ls-files -- '*/leg_factory.py' ); TK=${TK%/leg_factory.py}
if [ "$rc" = 0 ] && [ -n "$TK" ] && [ -z "$( cd "$T" && git ls-files -- '*/govkit.py' )" ]; then
  ok "a target applied with $KID alone holds the factory at $TK and no govkit"
else
  nope "the no-govkit target was not built (rc=$rc, kit dir '${TK}', deployer '${GK}'): $out"
fi
out=$( cd "$T" && "$PY" "$TK/regen.py" --list 2>&1 ); rc=$?
[ "$rc" = 0 ] && printf '%s' "$out" | grep -qF 'gate-legs.json · its when exists:' \
  && printf '%s' "$out" | grep -qF 'does not hold' \
  && ok "AC1 regen --list names the factory row skipped, its when not holding" \
  || nope "AC1 regen --list did not name the factory row skipped (rc=$rc): $out"
out=$( cd "$T" && "$PY" "$TK/regen.py" --check 2>&1 ); rc=$?
[ "$rc" = 0 ] && ok "AC1 regen --check exits 0 where no govkit sits" \
  || nope "AC1 regen --check did not exit 0 where no govkit sits (rc=$rc): $out"
out=$( cd "$T/$TK" && "$PY" -c 'import leg_factory' 2>&1 ); rc=$?
[ "$rc" = 0 ] && ok "AC2 the factory module imports with no govkit" \
  || nope "AC2 the factory module did not import with no govkit (rc=$rc): $out"
out=$( cd "$T/$TK" && "$PY" leg_factory.py --write 2>&1 ); rc=$?
[ "$rc" = 2 ] && printf '%s' "$out" | grep -qF 'looked in' && ! printf '%s' "$out" | grep -q 'Traceback' \
  && ok "AC2 --write exits 2 naming the places it looked for govkit, with no traceback" \
  || nope "AC2 --write did not refuse naming the places looked (rc=$rc): $out"
out=$( cd "$T/$TK" && "$PY" leg_factory.py --conform 2>&1 ); rc=$?
[ "$rc" = 0 ] && printf '%s' "$out" | grep -qF 'fresh: not graded here — no govkit' \
  && printf '%s' "$out" | grep -qF 'enforces: not graded here — no govkit' \
  && ok "AC3 --conform exits 0 over the target's descriptors, naming fresh and enforces ungraded" \
  || nope "AC3 --conform did not grade the target's descriptors green (rc=$rc): $out"

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "adopt-e2e: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates adopter e2e, $n assertions)"
exit "$bad"
