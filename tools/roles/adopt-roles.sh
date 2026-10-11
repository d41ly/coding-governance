#!/usr/bin/env bash
# adopt-roles.sh — install the role catalogue's project-facing surface: the `/build` Skill.
#
#   <prefix>/roles/adopt-roles.sh --scaffold   # render .claude/skills/build/SKILL.md and print its path
#   <prefix>/roles/adopt-roles.sh --check      # render in memory and byte-compare with the file on disk
#
# Exit 0 = rendered / in sync · 1 = stale, absent, a surviving token or a stage disagreement, each
# named · 2 = usage, a failed derivation, an absent conf or a dead catalogue probe.
#
# The shape is the unattended kit's adopter (KICK-aOrientedCast-2): the same `.git` walk derives the
# kit's repo-relative path and the tool root, every `{{TOKEN}}` is substituted literally, and both
# sides of the compare are CR-normalised. NO `fail()` HELPER, for that adopter's reason: check-arms
# grades a script defining one as a gate, and an adopter is not a gate.
#
# THE STAGE BINDING. Each `## Stage <n> — <workflow>` heading of the template must name a
# `[[workflow]]` of the catalogue whose `stage` is <n>, the headings run in strictly ascending stage
# order, and every workflow of stage 1 or more is named by exactly one heading. It runs inside
# `render_skill`, so `--check` grades exactly what `--scaffold` would write.
#
# WHAT THIS DOES NOT CHECK: what a stage's body says, whether the commands it names exist, or any
# catalogue key but `name` and `stage`. The catalogue is read with awk over `[[workflow]]` blocks, so
# an inline-table reformat reads zero workflows and refuses as a dead probe rather than passing.
set -u
MODE="${1-}"
case "$MODE" in
  --scaffold|--check) ;;
  *) echo "usage: $0 --scaffold | --check"; exit 2 ;;
esac

KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "roles: not a git repo"; exit 2; }

# A LOGICAL upward walk from the kit dir to the first `.git` (a file in a linked worktree, hence -e),
# building the kit's repo-relative path from basenames. adopt-unattended.sh says why no path string is
# compared and why the walk is not physical.
KIT_REL=""; _p="$KIT_DIR"
while : ; do
  _parent="$(dirname "$_p")"
  [ "$_parent" = "$_p" ] && { KIT_REL=""; break; }
  KIT_REL="$(basename "$_p")${KIT_REL:+/$KIT_REL}"
  [ -e "$_parent/.git" ] && break
  _p="$_parent"
done
[ -n "$KIT_REL" ] || { echo "roles: KIT_DIR derived empty — no .git above the kit at $KIT_DIR"; exit 2; }
TOOL_ROOT=${KIT_REL%/*}; [ "$TOOL_ROOT" = "$KIT_REL" ] && TOOL_ROOT=""
[ -z "$TOOL_ROOT" ] || TOOL_ROOT="$TOOL_ROOT/"

cd "$ROOT" || exit 2
CONF=".memory-tree.conf"
[ -f "$CONF" ] || { echo "roles: no $CONF at the repo root, so MEMORY_ROOT cannot be read"; exit 2; }
MEMORY_ROOT=$(sed -n 's/^MEMORY_ROOT=//p' "$CONF" | tail -1 | tr -d '\r"'"'")
[ -n "$MEMORY_ROOT" ] || { echo "roles: MEMORY_ROOT is blank or absent in $CONF"; exit 2; }

TEMPLATE="$KIT_DIR/SKILL.template.md"
CATALOGUE="$KIT_DIR/workflows.toml"
OUT=".claude/skills/build/SKILL.md"

render_skill() { # -> the render on stdout; 1 a stage disagreement or a surviving token, 2 a dead probe
  [ -f "$TEMPLATE" ] && [ -f "$CATALOGUE" ] || { echo "roles: $KIT_REL lacks SKILL.template.md or workflows.toml" >&2; return 2; }
  local bind rc out left
  bind=$(awk -v cat="$KIT_REL/workflows.toml" -v tpl="$KIT_REL/SKILL.template.md" '
    function close_blk() {
      if (blk) {
        if (name == "" || stage == "") { print "roles: catalogue block at " cat ":" blk " carries no " (name == "" ? "name" : "stage") " line"; bad = 1 }
        else { n++; st[name] = stage }
      }
      blk = 0; name = ""; stage = ""
    }
    function switch_file() { switched = 1; close_blk(); if (n == 0) { print "roles: dead probe — " cat " parsed zero [[workflow]] blocks"; dead = 1; exit 2 } }
    { sub(/\r$/, "") }
    FILENAME == ARGV[1] {
      if ($0 ~ /^\[\[workflow\]\][ \t]*$/) { close_blk(); blk = FNR; next }
      if (blk && $0 ~ /^name = "/) { v = $0; sub(/^name = "/, "", v); sub(/".*/, "", v); name = v }
      if (blk && $0 ~ /^stage = [0-9]+/) { v = $0; sub(/^stage = /, "", v); sub(/[^0-9].*/, "", v); stage = v + 0 }
      next
    }
    !switched { switch_file() }
    /^## Stage / {
      h = "heading \"" $0 "\" at " tpl ":" FNR
      if (NF != 5 || $4 != "—" || $3 !~ /^[0-9]+$/) { print "roles: " h " is not of the form ## Stage <n> — <workflow>"; bad = 1; next }
      num = $3 + 0; wf = $5
      if (!(wf in st)) { print "roles: " h " names no [[workflow]] entry of " cat; bad = 1; next }
      if (st[wf] != num) { print "roles: " h " says stage " num " but the entry " wf " is stage " st[wf]; bad = 1 }
      if (seen[wf]++) { print "roles: " h " names the entry " wf " a second time"; bad = 1 }
      if (num <= last) { print "roles: " h " does not ascend past stage " last; bad = 1 }
      last = num
    }
    END {
      if (dead) exit 2
      if (!switched) switch_file()
      if (dead) exit 2
      for (w in st) if (st[w] >= 1 && !(w in seen)) { print "roles: the entry " w " (stage " st[w] ") of " cat " is named by no ## Stage heading"; bad = 1 }
      exit bad
    }' "$CATALOGUE" "$TEMPLATE"); rc=$?
  [ "$rc" -eq 0 ] || { printf '%s\n' "$bind" >&2; return "$rc"; }
  # The `X` sentinel keeps trailing newlines `$( )` would strip. The replacements are QUOTED, because
  # bash 5.1+ reads an unquoted `&` in one as the matched text.
  out=$(cat "$TEMPLATE" && printf X) || return 2
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOL_ROOT"}
  out=${out//\{\{MEMORY_ROOT\}\}/"$MEMORY_ROOT"}
  if left=$(printf '%s' "$out" | grep -nF '{{'); then
    echo "roles: a token survived the render of $KIT_REL/SKILL.template.md:" >&2
    printf '%s\n' "$left" | sed 's/^/    line /' >&2
    return 1
  fi
  printf '%s' "$out"
}

body=$(render_skill && printf X) || exit $?
body=${body%X}

if [ "$MODE" = "--check" ]; then
  [ -f "$OUT" ] || { echo "roles: $OUT is not rendered — run $0 --scaffold"; exit 1; }
  disk=$(tr -d '\r' < "$OUT" && printf X); disk=${disk%X}
  [ "$disk" = "$body" ] || { echo "roles: $OUT is out of sync with $KIT_REL/SKILL.template.md — re-render with $0 --scaffold"; exit 1; }
  exit 0
fi

new=""; [ -f "$OUT" ] || new=1
mkdir -p "${OUT%/*}" || exit 2
printf '%s' "$body" > "$OUT" || exit 2
echo "$OUT"
# Whether a running session lists a Skill written after it started is UNVERIFIED on this CLI; the
# line states the conservative rule.
[ -z "$new" ] || echo "roles: a session started before this write may not list /build until it restarts"
exit 0
