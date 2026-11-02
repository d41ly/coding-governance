#!/usr/bin/env bash
# Fixture self-test for check-testsuite-counts.sh — every refusal armed by a POSITIVE assertion
# naming its own failure text, each paired with a green control. A check that was never reached is
# silent for the same reason a passing one is.
#
#   bash <prefix>/check-testsuite-counts.test.sh    # "PASS (N assertions)" + exit 0 = good
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-testsuite-counts.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
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
_rkd_py=$(resolve_python) || { echo "check-testsuite-counts.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
LIB_DIR=$(resolve_kit_dir "$_rkd_py" lib lib-selftest.sh "$HERE") || exit 2
LIB="${LIB_DIR##*/}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
st=0; n=0
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }

cd "$TMP" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t
mkdir -p "./${PFX}" memory/project
cp "$HERE/check-testsuite-counts.sh" "./${PFX}"
SCRIPT="$TMP/${PFX}check-testsuite-counts.sh"
run() { bash "$SCRIPT" 2>&1; }

# A COMPLIANT suite: the agreed count line plus a pinned floor.
build_ok()  { printf 'FLOOR_ASSERTIONS=3
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || st=1
echo "PASS ($n assertions)"
' > "$1"; }
# SILENT: no count at all, which is the state 12 of 27 suites were in when the leg was written.
build_bad() { printf 'echo done\n' > "$1"; }
# A floor pinned with nothing printing a count to compare it against.
build_floor_only() { printf 'FLOOR_ASSERTIONS=3\necho done\n' > "$1"; }
# A count and a floor that never MEET — the shape the reference suite actually had for its whole life.
build_uncompared() { printf 'FLOOR_ASSERTIONS=3
echo "PASS ($n assertions)"
' > "$1"; }
# A floor of ZERO: pinned, compared, and unable to bite.
build_zero() { printf 'FLOOR_ASSERTIONS=0
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || st=1
echo "PASS ($n assertions)"
' > "$1"; }

# ---- THE HARNESS SPELLING. A suite on `<prefix>/lib/lib-selftest.sh` prints no count of its own and
# ---- compares no floor of its own: `run_arms` does both. These three fixtures are the same three
# ---- states as the classic ones above, in that spelling.
build_harness_ok()    { printf '. "$HERE/'"$LIB"'/lib-selftest.sh"
SELFTEST_FLOOR=3
run_arms t
' > "$1"; }
build_harness_zero()  { printf '. "$HERE/'"$LIB"'/lib-selftest.sh"
SELFTEST_FLOOR=0
run_arms t
' > "$1"; }
build_harness_inert() { printf '. "$HERE/'"$LIB"'/lib-selftest.sh"
SELFTEST_FLOOR=3
echo done
' > "$1"; }

manifest() { # one argv entry per named suite
  { echo '['
    sep=""
    for f in "$@"; do printf '%s  { "name": "%s", "argv": ["bash", "%s"] }\n' "$sep" "$f" "$f"; sep=","; done
    echo ']'
  } > ${PFX}gate-legs.json
}
: > memory/project/testsuite-count-waivers.txt

# ---- GREEN CONTROL first. Every red arm below is worthless if a conforming tree is not silent.
build_ok ${PFX}a.test.sh; manifest ${PFX}a.test.sh
out=$(run); rc=$?
same "a conforming tree exits 0" "$rc" "0"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS ($n assertions)" || echo "FAIL ($n assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
same "a conforming tree prints nothing" "$out" ""

# ---- a suite printing NO count, and not waived.
build_bad ${PFX}b.test.sh; manifest ${PFX}a.test.sh ${PFX}b.test.sh
out=$(run)
hit "$out" "a self-test on the bar prints no executed assertion count against a floor, so a block of its arms could be stranded past an exit and the suite would still report success: ${PFX}b.test.sh"
same "and it exits non-zero" "$(run >/dev/null 2>&1; echo $?)" "1"

# ...WAIVED, it is silent — that is what lets the leg land green over a real tree and ratchet.
printf ''"${PFX}b.test.sh"'\n' > memory/project/testsuite-count-waivers.txt
same "a waived suite is silent" "$(run)" ""

# ---- a STALE waiver: the suite now complies, so the row hides nothing and must red. Without this
# ---- the list only ever grows, which is the opposite of a ratchet.
build_ok ${PFX}b.test.sh
hit "$(run)" "a testsuite-count waiver names a suite that now complies, so the list has stopped shrinking and the row hides nothing: ${PFX}b.test.sh"

# ---- a waiver naming a suite the manifest does not run at all.
build_bad ${PFX}b.test.sh
printf ''"${PFX}b.test.sh"'\n'"${PFX}ghost.test.sh"'\n' > memory/project/testsuite-count-waivers.txt
hit "$(run)" "a testsuite-count waiver names a suite the gate manifest does not run, so it waives nothing and outlives what it was written for: ${PFX}ghost.test.sh"

# ---- a floor with no count line to compare it to. Distinct message, because the fix is different.
: > memory/project/testsuite-count-waivers.txt
build_floor_only ${PFX}c.test.sh; manifest ${PFX}a.test.sh ${PFX}c.test.sh
hit "$(run)" "or never compares the two, so nothing reads the pin: ${PFX}c.test.sh"

# ...a count AND a floor that never meet — a pin nothing reads is the same nothing as no pin.
build_uncompared ${PFX}e.test.sh; manifest ${PFX}a.test.sh ${PFX}e.test.sh
hit "$(run)" "or never compares the two, so nothing reads the pin: ${PFX}e.test.sh"

# ...a floor of ZERO, which nothing can fall below.
build_zero ${PFX}g.test.sh; manifest ${PFX}a.test.sh ${PFX}g.test.sh
hit "$(run)" "a self-test pins a floor of ZERO, which nothing can fall below"

# ---- THE DERIVED-POPULATION ARM. Adding a suite to the manifest reds the leg with NO edit to the
# ---- leg itself; a hand-kept list would have stayed green and that is the defect being prevented.
manifest ${PFX}a.test.sh
same "one compliant suite, silent" "$(run)" ""
build_bad ${PFX}d.test.sh; manifest ${PFX}a.test.sh ${PFX}d.test.sh
hit "$(run)" "${PFX}d.test.sh"

# ---- THE HARNESS SPELLING, all three states. Added when TOOL-aQuenchedHarness-6 ported the first
# ---- suite onto the harness and every ported suite tripped this leg: the property is unchanged,
# ---- the spelling is not.
build_harness_ok ${PFX}h.test.sh; manifest ${PFX}h.test.sh
out=$(run); rc=$?
same "a harness-form suite is compliant" "$rc" "0"
same "and a tree holding only harness-form suites is silent" "$out" ""

build_harness_zero ${PFX}hz.test.sh; manifest ${PFX}h.test.sh ${PFX}hz.test.sh
hit "$(run)" "a harness self-test pins SELFTEST_FLOOR of ZERO, which nothing can fall below — a pin that cannot bite is the decoration this leg exists to remove: ${PFX}hz.test.sh"

build_harness_inert ${PFX}hi.test.sh; manifest ${PFX}h.test.sh ${PFX}hi.test.sh
hit "$(run)" "a harness self-test pins SELFTEST_FLOOR but never reaches run_arms, or does not source the harness, so nothing prints its executed count and nothing reads the pin: ${PFX}hi.test.sh"

# ---- a git PATHSPEC in an argv is not a suite. A leg excluding the suites from its own population
# ---- spells `:!*.test.sh`, which ends like a suite path and names no file (TOOL-aGraftedHelix-45).
build_ok ${PFX}a.test.sh; manifest ${PFX}a.test.sh ':!*.test.sh'
out=$(run); rc=$?
same "a pathspec excluding the suites is not read as a suite" "$rc" "0"
miss "$out" "cannot read"

# ---- a manifest naming a suite that is not on disk must NOT be skipped silently.
manifest ${PFX}a.test.sh ${PFX}gone.test.sh
hit "$(run)" "the gate manifest names a self-test this leg cannot read, and skipping it silently removes it from the population: ${PFX}gone.test.sh"

# ---- an EMPTY population is a refusal, not a pass. This is the vacuous-selector shape the leg
# ---- exists to prevent, applied to the leg itself.
manifest
hit "$(run)" "the gate manifest names no *.test.sh, so this leg would grade an empty population"

FLOOR_ASSERTIONS=20
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
