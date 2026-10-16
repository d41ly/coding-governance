#!/usr/bin/env bash
# adopt-branch-reconcile.sh — render the /cleanup Skill, and check the rendered copy has not drifted.
# gov:kit branch-reconcile@1.5
#
#   bash <this kit>/adopt-branch-reconcile.sh --scaffold    # render .claude/skills/cleanup/SKILL.md
#   bash <this kit>/adopt-branch-reconcile.sh --check       # the gate leg: is the rendered Skill a fresh render?
#
# The Skill names the CLI by where this kit is installed, which differs per repository, so it is
# RENDERED from the template beside this script rather than shipped, and `--check` re-renders and
# compares. The kit dir is DERIVED by git from this script's own location, never spelled. The
# comparison strips CR from the on-disk copy, because the render is LF by construction and a CRLF
# working copy of an untouched file is not drift. The runlog kit's adopter is the shape this follows.
#
# BOTH MODES check the fresh render before anything is compared or written: the template spells no
# literal `tools/` path segment, the render is non-empty, no double brace survives, and the render
# names the CLI by its rendered path, which is a file here.
#
# WHAT IT DOES NOT CHECK: whether the Skill's instructions are correct. That the CLI behaves as the
# Skill says is the kit self-test's job.
#
#   Exit 0 = rendered, or in sync · 1 = drifted, unrendered, or refused · 2 = wrong invocation or not
#   a repository.
set -u

HERE=.; [[ $0 == */* ]] && HERE=${0%/*}; HERE="$(cd "$HERE" && pwd)" || exit 2
ROOT="$(unset GIT_DIR GIT_WORK_TREE; cd "$HERE" && git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "branch-reconcile: the directory holding this script is not inside a git repository"; exit 2; }
cd "$ROOT" || exit 2
ROOT="$(pwd)"
KIT_REL="$(unset GIT_DIR GIT_WORK_TREE; cd "$HERE" && git rev-parse --show-prefix)" || exit 2
KIT_REL="${KIT_REL%/}"
[ -n "$KIT_REL" ] || KIT_REL="."
USAGE="usage: bash $KIT_REL/adopt-branch-reconcile.sh --scaffold | --check"

MODE=""
for a in "$@"; do
  case "$a" in
    --scaffold|--check) [ -z "$MODE" ] || { echo "$USAGE"; exit 2; }; MODE="$a" ;;
    *) echo "$USAGE"; exit 2 ;;
  esac
done
[ -n "$MODE" ] || { echo "$USAGE"; exit 2; }

TEMPLATE="$HERE/SKILL.template.md"
SKILL_REL=".claude/skills/cleanup/SKILL.md"
SKILL="$ROOT/$SKILL_REL"

if [ ! -f "$TEMPLATE" ]; then
  if [ -f "$SKILL" ]; then
    echo "branch-reconcile: $SKILL_REL exists but $KIT_REL/SKILL.template.md does not, so its drift cannot be checked"
    exit 1
  fi
  echo "skip     cleanup skill — $KIT_REL/SKILL.template.md is not installed, so there is nothing to render"
  [ "$MODE" = "--check" ] && exit 0
  exit 1
fi

render_skill() { # -> stdout: the template with its token substituted, LF only
  # Parameter substitution, not sed: a value carrying `|` or `&` would corrupt an s||| expression.
  # The `X` sentinel keeps the trailing newlines `$( )` would strip.
  local out
  out=$( cat "$TEMPLATE" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  printf '%s' "$out"
}

check_render() { # $1 = a fresh render -> 0 when it may be written or compared, 1 with each reason
  local bad=0 hits
  hits=$(tr -d '\r' < "$TEMPLATE" | grep -nE '(^|[^A-Za-z0-9_.-])tools/' || true)
  if [ -n "$hits" ]; then
    echo "branch-reconcile: $KIT_REL/SKILL.template.md spells a literal tools/ path; name it through the kit-dir token:"
    printf '  %s\n' "${hits//$'\n'/$'\n'  }"
    bad=1
  fi
  if [ ! -s "$1" ]; then
    echo "branch-reconcile: the render is EMPTY, and an empty render compared with an equally empty Skill would pass"
    return 1
  fi
  hits=$(grep -n '{{\|}}' "$1" || true)
  if [ -n "$hits" ]; then
    echo "branch-reconcile: a double brace survives the render, so the template carries a token this script does not substitute:"
    printf '  %s\n' "${hits//$'\n'/$'\n'  }"
    bad=1
  fi
  if ! grep -qF "python $KIT_REL/branch_reconcile.py" "$1"; then
    echo "branch-reconcile: the render never names the CLI as python $KIT_REL/branch_reconcile.py"
    bad=1
  elif [ ! -f "$ROOT/$KIT_REL/branch_reconcile.py" ]; then
    echo "branch-reconcile: the render names python $KIT_REL/branch_reconcile.py, and no such file is in this tree"
    bad=1
  fi
  return "$bad"
}

TMP="$(mktemp)" || exit 2
trap 'rm -f "$TMP"' EXIT
render_skill > "$TMP" || { echo "branch-reconcile: $KIT_REL/SKILL.template.md could not be read"; exit 1; }
check_render "$TMP" || exit 1

# THE OLD RENDER (TOOL-dSweptBranches-23). The skill moved from branch-reconcile/ to cleanup/ while
# its template stayed put, and govkit's rename path keys on a row's SOURCE, so an updating adopter
# keeps the old copy beside the new one: two skills answering one ask, and nothing reading the old.
# `--scaffold` withdraws it only when it is recognisably this kit's render — its front matter names
# branch-reconcile and its body names the CLI. Anything else at that path is someone's work: named,
# kept, and the mode exits 1. `--check` withdraws nothing and reds while either stays.
OLD_REL=".claude/skills/branch-reconcile/SKILL.md"
OLD="$ROOT/$OLD_REL"
check_old_render() { # -> 0 when no old render stays (withdrawing it under --scaffold), 1 with why
  [ -e "$OLD" ] || return 0
  local front
  front=$(tr -d '\r' < "$OLD" | awk 'NR == 1 && $0 != "---" { exit } NR > 1 && $0 == "---" { exit } NR > 1')
  if ! [[ $'\n'$front$'\n' == *$'\n''name: branch-reconcile'$'\n'* ]] || ! grep -qF 'branch_reconcile.py' "$OLD"; then
    echo "branch-reconcile: $OLD_REL is not this kit's old render, so it is kept; remove it by hand once"
    echo "  nothing needs it — /cleanup at $SKILL_REL replaces the old /branch-reconcile skill"
    return 1
  fi
  if [ "$MODE" = "--check" ]; then
    echo "branch-reconcile: $OLD_REL is the old /branch-reconcile render, which /cleanup replaces."
    echo "Fix: bash $KIT_REL/adopt-branch-reconcile.sh --scaffold"
    return 1
  fi
  rm -f "$OLD" || return 1
  rmdir "${OLD%/*}" 2>/dev/null || true
  echo "withdrew $OLD_REL, the old /branch-reconcile render"
}

if [ "$MODE" = "--check" ]; then
  check_old_render || exit 1
  [ -f "$SKILL" ] || { echo "branch-reconcile: $SKILL_REL is not rendered — run bash $KIT_REL/adopt-branch-reconcile.sh --scaffold"; exit 1; }
  if diff -q <(tr -d '\r' < "$SKILL") "$TMP" >/dev/null 2>&1; then
    echo "ok       cleanup skill — $SKILL_REL is a fresh render (CLI $KIT_REL/branch_reconcile.py)"
    exit 0
  fi
  echo "branch-reconcile: $SKILL_REL has DRIFTED from a fresh render of $KIT_REL/SKILL.template.md."
  diff -u <(tr -d '\r' < "$SKILL") "$TMP" | head -40
  echo "Fix: bash $KIT_REL/adopt-branch-reconcile.sh --scaffold"
  exit 1
fi

mkdir -p "${SKILL%/*}" || exit 1
cp "$TMP" "$SKILL.tmp" && mv "$SKILL.tmp" "$SKILL" || exit 1
echo "rendered $SKILL_REL (CLI $KIT_REL/branch_reconcile.py)"
check_old_render || exit 1
echo "Next: run bash $KIT_REL/adopt-branch-reconcile.sh --check on your bar, so a template edit nobody re-rendered reds."
