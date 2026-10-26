#!/usr/bin/env bash
# adopt-runlog.sh — render the runlog Skill, and check that the rendered copy has not drifted.
# gov:kit runlog@1.13
#
#   bash <this kit>/adopt-runlog.sh --scaffold    # render .claude/skills/runlog/SKILL.md
#   bash <this kit>/adopt-runlog.sh --check       # the gate leg: is the rendered Skill a fresh render?
#
# The Skill answers an owner's questions about one unattended run, and it names two values that
# differ per repository: where this kit is installed, which is how it names the CLI, and the memory
# root, which is where a run's committed record sits. So the Skill is RENDERED from the template
# beside this script rather than shipped, and `--check` re-renders and compares, which is how a moved
# memory root or a template edit nobody re-rendered becomes a red leg instead of a Skill that sends
# an agent to a path that does not exist.
#
# BOTH MODES run the same checks on the fresh render before anything is compared or written, so a
# broken template can neither be written nor pass:
#   - the template spells no literal `tools/` or `memory/` path segment, because those two are the
#     values the tokens exist to carry, and a literal one is right only in a tree laid out like gov's;
#   - the render is non-empty, since an empty render compared with an equally empty Skill is the
#     green-by-absence shape;
#   - no double brace survives, since a token this script does not substitute would ship verbatim;
#   - the render names the CLI by its rendered path, and that path is a file here, and it names the
#     record's folder under the rendered memory root.
#
# The kit dir is DERIVED by git from this script's own location, never spelled, so the render is the
# same relative path on every node and whatever prefix the kit is installed at. The memory root is
# read by the kit's own reader, `resolve_memory_root` in the library beside this script, so the Skill
# names the folder the `record` verb writes to, and a root that reader refuses is refused here by the
# same sentence. The comparison strips CR from the on-disk copy, because the render is LF by
# construction and a CRLF working copy of an untouched file is not drift.
#
# WHAT IT DOES NOT CHECK. It proves the rendered Skill is a fresh render of the template with this
# tree's two values; it says nothing about whether the Skill's instructions are CORRECT — that the
# verbs it names behave as it says is the kit self-test's job, and that the answers an agent gives
# are right is nobody's. It reads the template's literal paths textually, so a path spelled without
# a `tools/` or `memory/` segment is invisible to it.
#
#   Exit 0 = rendered, or in sync · 1 = drifted, unrendered, or refused · 2 = wrong invocation, not a
#   repository, or no python.
set -u

# HERE before any cd: `$0` may be relative, and resolving it after moving would resolve it against
# the wrong directory.
HERE="$(cd "$(dirname "$0")" && pwd)" || exit 2
ROOT="$(unset GIT_DIR GIT_WORK_TREE; cd "$HERE" && git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "runlog: the directory holding this script is not inside a git repository"; exit 2; }
cd "$ROOT" || exit 2
ROOT="$(pwd)"
# The kit dir as the repository spells it, RELATIVE, and computed by git so the two operands cannot
# be two spellings of one directory. A kit installed at the repository root renders as `.`.
KIT_REL="$(unset GIT_DIR GIT_WORK_TREE; cd "$HERE" && git rev-parse --show-prefix)" || exit 2
KIT_REL="${KIT_REL%/}"
[ -n "$KIT_REL" ] || KIT_REL="."

MODE=""
for a in "$@"; do
  case "$a" in
    --scaffold|--check) [ -z "$MODE" ] || { echo "usage: bash $KIT_REL/adopt-runlog.sh --scaffold | --check"; exit 2; }
                        MODE="$a" ;;
    *) echo "usage: bash $KIT_REL/adopt-runlog.sh --scaffold | --check"; exit 2 ;;
  esac
done
[ -n "$MODE" ] || { echo "usage: bash $KIT_REL/adopt-runlog.sh --scaffold | --check"; exit 2; }

TEMPLATE="$HERE/SKILL.template.md"
SKILL_REL=".claude/skills/runlog/SKILL.md"
SKILL="$ROOT/$SKILL_REL"

# Three states, not two. With no template there is nothing to render and nothing that can drift, so
# `--check` SKIPS and says so. A rendered Skill with no template is the one state nothing can verify,
# and it reds.
if [ ! -f "$TEMPLATE" ]; then
  if [ -f "$SKILL" ]; then
    echo "runlog: $SKILL_REL exists but $KIT_REL/SKILL.template.md does not, so its drift cannot be checked"
    exit 1
  fi
  echo "skip     runlog skill — $KIT_REL/SKILL.template.md is not installed, so there is nothing to render"
  [ "$MODE" = "--check" ] && exit 0
  exit 1
fi

# The resolver, INLINE. This kit is copy-installed as a standalone directory, so the shared lib
# does not exist in an adopting repo. The block below is byte-identical to the canonical copy its
# own marker line names, and that copy's self-test reds if any inline copy drifts. The marker line
# is the ONE path literal this file carries, because the parity gate compares it byte for byte.
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
        # way to the direct executable where the probe named a file, so a consumer never spawns
        # the Windows App Execution Alias again; the launcher's own name otherwise.
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
    echo "resolve_python: tried:$_rp_tried"
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
  } >&2
  return 1
}
# <<< resolve_python
PY=$(resolve_python) || exit 2

# The memory root, through the kit's ONE reader of it. `-B` because a gate leg should not leave a
# bytecode cache in an adopter's kit dir. A refusal is the reader's own sentence, forwarded as is.
MEMORY_ROOT="$("$PY" -B -c '
import sys
sys.path.insert(0, sys.argv[1])
import runlog_lib
try:
    sys.stdout.write(runlog_lib.resolve_memory_root(sys.argv[2]))
except ValueError as exc:
    sys.exit(str(exc))
' "$HERE" "$ROOT")" || exit 1
MEMORY_ROOT="${MEMORY_ROOT//$'\r'/}"

render_skill() { # -> stdout: the template with both tokens substituted, LF only
  # No `sed`: a substituted value carrying `|` closes an s||| delimiter and `&` re-inserts the whole
  # match. Parameter substitution has neither, provided the replacement is quoted. The `X` sentinel
  # is because `$( )` strips every trailing newline, and `cat` exits 1 inside the substitution
  # because the substitution otherwise reports printf's status, which is always 0.
  local out
  out=$( cat "$TEMPLATE" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  out=${out//\{\{MEMORY_ROOT\}\}/"$MEMORY_ROOT"}
  printf '%s' "$out"
}

check_render() { # $1 = a fresh render -> 0 when it may be written or compared, 1 with each reason
  local bad=0 hits
  hits=$(tr -d '\r' < "$TEMPLATE" | grep -nE '(^|[^A-Za-z0-9_.-])(tools|memory)/' || true)
  if [ -n "$hits" ]; then
    echo "runlog: $KIT_REL/SKILL.template.md spells a literal tools/ or memory/ path, which is right only in a tree laid out like the kit's source; name it through the kit-dir or memory-root token:"
    printf '%s\n' "$hits" | sed 's/^/  /'
    bad=1
  fi
  if [ ! -s "$1" ]; then
    echo "runlog: the render is EMPTY, and an empty render compared with an equally empty Skill would pass"
    return 1
  fi
  hits=$(grep -n '{{\|}}' "$1" || true)
  if [ -n "$hits" ]; then
    echo "runlog: a double brace survives the render, so the template carries a token this script does not substitute:"
    printf '%s\n' "$hits" | sed 's/^/  /'
    bad=1
  fi
  if ! grep -qF "python $KIT_REL/runlog.py" "$1"; then
    echo "runlog: the render never names the CLI as python $KIT_REL/runlog.py, so the template stopped naming it through the kit-dir token"
    bad=1
  elif [ ! -f "$ROOT/$KIT_REL/runlog.py" ]; then
    echo "runlog: the render names python $KIT_REL/runlog.py, and no such file is in this tree"
    bad=1
  fi
  if ! grep -qF "$MEMORY_ROOT/builds/<slug>/build/" "$1"; then
    echo "runlog: the render never names the record's folder as $MEMORY_ROOT/builds/<slug>/build/, so the template stopped naming it through the memory-root token"
    bad=1
  fi
  return "$bad"
}

TMP="$(mktemp)" || exit 2
trap 'rm -f "$TMP"' EXIT
render_skill > "$TMP" || { echo "runlog: $KIT_REL/SKILL.template.md could not be read"; exit 1; }
check_render "$TMP" || exit 1

if [ "$MODE" = "--check" ]; then
  [ -f "$SKILL" ] || { echo "runlog: $SKILL_REL is not rendered — run bash $KIT_REL/adopt-runlog.sh --scaffold"; exit 1; }
  if diff -q <(tr -d '\r' < "$SKILL") "$TMP" >/dev/null 2>&1; then
    echo "ok       runlog skill — $SKILL_REL is a fresh render (CLI $KIT_REL/runlog.py, memory root $MEMORY_ROOT)"
    exit 0
  fi
  echo "runlog: $SKILL_REL has DRIFTED from a fresh render of $KIT_REL/SKILL.template.md."
  diff -u <(tr -d '\r' < "$SKILL") "$TMP" | head -40
  echo "Fix: bash $KIT_REL/adopt-runlog.sh --scaffold"
  exit 1
fi

mkdir -p "$(dirname "$SKILL")" || exit 1
cp "$TMP" "$SKILL.tmp" && mv "$SKILL.tmp" "$SKILL" || exit 1
echo "rendered $SKILL_REL (CLI $KIT_REL/runlog.py, memory root $MEMORY_ROOT)"
echo "Next: run bash $KIT_REL/adopt-runlog.sh --check on your bar, so a template edit or a moved memory root nobody re-rendered reds."
