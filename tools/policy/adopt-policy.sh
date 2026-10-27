#!/usr/bin/env bash
# adopt-policy.sh — scaffold a repository's policy file, and check it against the policy catalogue.
#
#   bash <this kit>/adopt-policy.sh --scaffold [--target <repo>]   # write .governance/policy.toml if absent
#   bash <this kit>/adopt-policy.sh --check [--target <repo>]      # every policy arm over <repo>
#
# <repo> defaults to the git top level of the working directory.
#
# `--scaffold` writes the starter file `policy.py scaffold` prints, and ONLY when no file is there:
# a policy file is the repository's own from its first write, so an existing one is kept byte for
# byte and the script says "kept". Then, kept or written, it renders the harness's two concurrency
# settings from the agent limit at HEAD, `policy.py settings --write`, whenever HEAD resolves, so an
# adopter spawns on install day without running the render by hand, and then the JSON mirror,
# `policy.py mirror --write` (TOOL-dGroundRules-25 S7); with no commit yet it prints one line naming
# the re-run, and while an input of the mirror is uncommitted, as on install day, one line deferring
# the mirror to the re-run after the commit, unless `check_policy.py`'s `arm_schema` finds the policy
# file invalid, which exits 2 printing its findings (TOOL-dGroundRules-34 S20). `[[regenerate]]` in
# kit.toml runs this same verb on every update unless GOVKIT_RERENDER=0 is exported
# (TOOL-dGroundRules-21 S37). `--check` is `check_policy.py --repo <repo>`, whose exit it returns.
#
# The kit dir is this script's own directory, never spelled, so the adopter runs from wherever the
# kit is installed. Its refusals are armed by `adopt-policy.test.sh` beside it.
#
#   Exit 0 = written, kept or green · 1 = red, or a write failed · 2 = wrong invocation, no
#   repository, no python, or an invalid policy file on install day.
set -u

HERE=.; [[ $0 == */* ]] && HERE=${0%/*}; HERE="$(cd "$HERE" && pwd)" || exit 2
USAGE="usage: bash <this kit>/adopt-policy.sh --scaffold | --check [--target <repo>]"

MODE=""
TARGET=""
while [ $# -gt 0 ]; do
  case "$1" in
    --scaffold|--check) [ -z "$MODE" ] || { echo "$USAGE"; exit 2; }
                        MODE="$1" ;;
    --target) [ $# -ge 2 ] || { echo "$USAGE"; exit 2; }
              TARGET="$2"; shift ;;
    *) echo "$USAGE"; exit 2 ;;
  esac
  shift
done
[ -n "$MODE" ] || { echo "$USAGE"; exit 2; }
if [ -z "$TARGET" ]; then
  TARGET="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "policy: the working directory is in no git repository; name one with --target <repo>"; exit 2; }
fi
[ -d "$TARGET" ] || { echo "policy: --target $TARGET is not a directory"; exit 2; }

# The resolver, INLINE. This kit is copy-installed as a standalone directory, so the shared lib
# does not exist in an adopting repo. The block below is byte-identical to the canonical copy its
# own marker line names, and that copy's self-test reds if any inline copy drifts.
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
PY=$(resolve_python) || exit 2

if [ "$MODE" = "--check" ]; then
  "$PY" -B "$HERE/check_policy.py" --repo "$TARGET"
  exit $?
fi

FILE="$TARGET/.governance/policy.toml"
if [ -e "$FILE" ]; then
  echo "kept     $FILE — a policy file is the repository's own, and the scaffold never overwrites it"
else
  if ! mkdir -p "$TARGET/.governance" 2>/dev/null; then
    echo "policy: the directory .governance could not be made in $TARGET"
    exit 1
  fi
  _tmp=$(mktemp -u "$FILE.XXXXXXXX")
  if ! { "$PY" -B "$HERE/policy.py" scaffold > "$_tmp" && mv "$_tmp" "$FILE"; } 2>/dev/null; then
    rm -f "$_tmp" 2>/dev/null
    echo "policy: the scaffold could not be written to $FILE"
    exit 1
  fi
  echo "wrote    $FILE"
fi

# The harness's settings, rendered from the agent limit at HEAD wherever HEAD resolves.
if ! git -C "$TARGET" rev-parse --verify -q HEAD >/dev/null 2>&1; then
  echo "policy: $TARGET has no commit yet, so the harness settings are not rendered; re-run --scaffold after the first commit"
  exit 0
fi
if ! (cd "$TARGET" && "$PY" -B "$HERE/policy.py" settings --write); then
  echo "policy: the harness settings could not be rendered in $TARGET; the line above says why"
  exit 1
fi
# Then the JSON mirror the hooks read, rendered at HEAD the same way (TOOL-dGroundRules-25 S7), so an
# adopter's bar finds it fresh at its preflight. On install day every input it records differs from
# HEAD, so its `uncommitted changes` refusal, and only that one, is deferred to the re-run after the
# first commit, naming the input the refusal names (TOOL-dGroundRules-31); the scaffold compares no
# input itself. Every other refusal stands.
OUT=$(cd "$TARGET" && "$PY" -B "$HERE/policy.py" mirror --write 2>&1)
RC=$?
if [ "$RC" = 2 ] && [[ "$OUT" == *"uncommitted changes"* ]]; then
  # An invalid policy file is never deferred (TOOL-dGroundRules-34 S20): `check_policy.py`'s
  # `arm_schema` grades the working-tree file first, and a finding stops the scaffold, exit 2.
  SCHEMA=$("$PY" -B "$HERE/check_policy.py" --repo "$TARGET" 2>&1 |
    awk '/^policy-check: arm_schema · /{f=1; print; next} f && /^  /{print; next} {f=0}')
  case "$SCHEMA" in
    "policy-check: arm_schema · "[1-9]*)
      echo "policy: $TARGET/.governance/policy.toml is invalid, so the mirror is not deferred; fix it, then re-run --scaffold"
      printf '%s\n' "$SCHEMA"
      exit 2 ;;
  esac
  INPUT=${OUT#*refused · }
  echo "adopt-policy: mirror deferred · ${INPUT%%:[0-9]* · uncommitted changes*} has uncommitted changes · commit, then re-run --scaffold"
elif [ "$RC" != 0 ]; then
  echo "policy: the policy mirror could not be rendered in $TARGET; the line below says why"
  printf '%s\n' "$OUT"
  exit 1
else
  printf '%s\n' "$OUT"
fi
exit 0
