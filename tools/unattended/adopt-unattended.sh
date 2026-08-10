#!/usr/bin/env bash
# adopt-unattended.sh — install the unattended-run kit's project-facing surface.
#
#   unattended/adopt-unattended.sh            # render .claude/skills/unattended/SKILL.md
#   unattended/adopt-unattended.sh --check    # verify the rendered Skill still matches the kit + conf
#
# Exit 0 = rendered / in sync · 1 = drift or a missing prerequisite · 2 = misconfigured.
#
# `--check` is the merge-bar arm. It renders to a temp file and DIFFS, so a hand-edited Skill reds
# instead of being quietly accepted. Both sides are CR-normalised, because a byte-comparing gate
# needs both halves: the `eol=lf` pin so the committed bytes are right, AND normalisation in the
# comparison so a Windows checkout does not report every line of an untouched file as drift.
#
# NO `fail()` HELPER, deliberately. `check-arms.py` discovers any tracked `*.sh` that defines one and
# calls `fail <n> "` as a GATE needing an armed sibling test, and an adopter is not a gate. The two
# existing adopters use plain `echo` + `exit` for the same reason; this is the third instance of a
# shape, not a new one.
set -u
MODE="${1-}"
case "$MODE" in
  ""|--check) ;;
  *) echo "usage: $0 [--check]"; exit 2 ;;
esac

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "unattended: not a git repo"; exit 2; }
ROOT="$(cd "$ROOT" && pwd)"
cd "$ROOT" || exit 2
KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE="$KIT_DIR/SKILL.template.md"
[ -f "$TEMPLATE" ] || { echo "unattended: SKILL.template.md is missing from the kit at $KIT_DIR"; exit 1; }

CONF="$ROOT/.unattended.conf"
[ -f "$CONF" ] || { echo "unattended: no .unattended.conf at the repo root — render it after adopting the project layer"; exit 1; }
MEMORY_ROOT=memory; LANDER=""; KEEPALIVE_CREATE=""; KEEPALIVE_DELETE=""
# shellcheck disable=SC1090
. "$CONF"

# The kit dir AS THE ADOPTER SEES IT, so the rendered commands are copy-pasteable. Both sides go
# through the same `cd … && pwd` chain first: under MSYS/git-bash one directory has two spellings
# and a raw prefix strip across them silently yields an absolute path, which then renders a command
# carrying a drive letter.
KIT_REL=${KIT_DIR#"$ROOT"/}
[ "$KIT_REL" != "$KIT_DIR" ] || { echo "unattended: the kit at $KIT_DIR is not inside $ROOT — refusing to render a Skill whose commands point outside the adopting repo"; exit 2; }

SKILL_DIR="$ROOT/.claude/skills/unattended"
SKILL_OUT="$SKILL_DIR/SKILL.md"

render() { # -> stdout; LF only (the render is pinned eol=lf in .gitattributes)
  sed -e "s|{{KIT_DIR}}|$KIT_REL|g" \
      -e "s|{{MEMORY_ROOT}}|$MEMORY_ROOT|g" \
      -e "s|{{LANDER}}|$LANDER|g" \
      -e "s|{{KEEPALIVE_CREATE}}|$KEEPALIVE_CREATE|g" \
      -e "s|{{KEEPALIVE_DELETE}}|$KEEPALIVE_DELETE|g" \
      "$TEMPLATE" | tr -d '\r'
}

if [ "$MODE" = "--check" ]; then
  # An UNRENDERED Skill is a named refusal, never a skip. "The file is not there" and "the file
  # matches" are different answers, and only one of them means the kit is installed.
  [ -f "$SKILL_OUT" ] || { echo "unattended: $SKILL_OUT is not rendered — run $0"; exit 1; }
  TMP=$(mktemp) || exit 2
  trap 'rm -f "$TMP"' EXIT
  render > "$TMP"
  if ! diff -q <(tr -d '\r' < "$SKILL_OUT") "$TMP" >/dev/null 2>&1; then
    echo "unattended: $SKILL_OUT is out of sync with SKILL.template.md + .unattended.conf"
    echo "  re-render with: $0"
    diff <(tr -d '\r' < "$SKILL_OUT") "$TMP" | head -20 | sed 's/^/    /'
    exit 1
  fi
  # A surviving placeholder means the conf declared nothing for it, which renders a Skill telling the
  # agent to call `{{KEEPALIVE_CREATE}}`. In sync with the template and useless.
  if grep -qE '\{\{[A-Z_]+\}\}' "$SKILL_OUT"; then
    echo "unattended: $SKILL_OUT still carries an unfilled placeholder — .unattended.conf declares no value for it"
    grep -nE '\{\{[A-Z_]+\}\}' "$SKILL_OUT" | head -5 | sed 's/^/    /'
    exit 1
  fi
  echo "unattended: in sync (skill rendered from template + .unattended.conf)"
  exit 0
fi

mkdir -p "$SKILL_DIR"
render > "$SKILL_OUT"
echo "unattended: rendered $SKILL_OUT"
cat <<EOF
unattended: next
  1. Pin the render LF in .gitattributes:  .claude/skills/unattended/SKILL.md text eol=lf
     (without it a checkout can land CRLF while git status stays clean, and the --check leg
      reports every line of an untouched file as drift)
  2. git add the render and the pin, then run: $0 --check
  3. Wire '$0 --check' and 'bash $KIT_REL/check-unattended.sh' into your gate manifest.
EOF
