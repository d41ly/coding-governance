#!/usr/bin/env bash
# adopt-runlog.sh — render the runlog Skill, and check that the rendered copy has not drifted.
# gov:kit runlog@1.0
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
ROOT="$(cd "$HERE" && git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "runlog: the directory holding this script is not inside a git repository"; exit 2; }
cd "$ROOT" || exit 2
ROOT="$(pwd)"
# The kit dir as the repository spells it, RELATIVE, and computed by git so the two operands cannot
# be two spellings of one directory. A kit installed at the repository root renders as `.`.
KIT_REL="$(cd "$HERE" && git rev-parse --show-prefix)" || exit 2
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
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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
