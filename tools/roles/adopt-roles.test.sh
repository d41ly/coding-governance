#!/usr/bin/env bash
# adopt-roles.test.sh — the roles adopter's self-test (TOOL-aOrientedCast-8 S12).
#
#   bash <prefix>/roles/adopt-roles.test.sh
#   ROLES_ADOPTER=<a copy> bash <prefix>/roles/adopt-roles.test.sh   # grade a copy, for a red observation
#
# Each arm builds its own fixture: a fresh git repository holding a copy of this kit, with the adopter
# under test as its `adopt-roles.sh`, the governing doc and memory root this repository's conf names,
# scaffolded once. Then it stages ONE break into the fixture and asserts the adopter's refusal by exit
# code AND by the text naming it, because an exit code alone is shared by every refusal the adopter
# has: a copy with the stage binding staged out still exits 1 on the agent compare.
#
# The arms: a stage heading naming a workflow at the wrong stage; a catalogue workflow no heading
# names; a token surviving the substitution; a byte appended to a rendered agent type; an unknown
# argument. Every arm is a self-contained block below the prologue, so a slice of the prologue and one
# block runs that arm alone.
#
# WHAT THIS DOES NOT CHECK: what the rendered Skill or an agent type SAYS, which the catalogue checker
# and the renderer's own self-test grade; the `--scaffold` restart notice's wording; or an adopter run
# at another install prefix, since the fixture mirrors this repository's own.
#
# Withheld from the payload by the kit's descriptor (`project-owned`): its subject is the adopter in
# this directory, so it has a job only where that source changes.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ADOPTER="${ROLES_ADOPTER:-$HERE/adopt-roles.sh}"
REPO=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "adopt-roles.test: not inside a git repository"; exit 2; }
KREL=$(git -C "$HERE" rev-parse --show-prefix 2>/dev/null) || exit 2
KREL=${KREL%/}
[ -n "$KREL" ] || { echo "adopt-roles.test: the kit's directory derived empty"; exit 2; }
MR=$(sed -n 's/^MEMORY_ROOT=//p' "$REPO/.memory-tree.conf" | tail -1 | tr -d '\r"'"'")
CH=$(sed -n 's/^CHARTER=//p' "$REPO/.memory-tree.conf" | tail -1 | tr -d '\r"'"'")
[ -n "$MR" ] && [ -n "$CH" ] && [ -f "$REPO/$CH" ] || { echo "adopt-roles.test: $REPO/.memory-tree.conf names no MEMORY_ROOT or no CHARTER file"; exit 2; }
[ -f "$ADOPTER" ] || { echo "adopt-roles.test: no adopter at $ADOPTER"; exit 2; }
TMP_ROOT=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP_ROOT"' EXIT
FLOOR_ASSERTIONS=10
n=0; fail=0
check_arm() { n=$((n+1)); if [ "$2" = 1 ]; then echo "ok   $1"; else echo "FAIL $1"; fail=$((fail+1)); fi; }
FX=""
build_fixture() { # -> $FX: a repo holding this kit with $ADOPTER as its adopter, scaffolded; rc of the scaffold
  FX="$TMP_ROOT/fx$n"
  mkdir -p "$FX/$KREL" "$FX/$(dirname "$CH")" || return 2
  git init -q "$FX" || return 2
  cp -R "$HERE"/. "$FX/$KREL"/ && cp "$ADOPTER" "$FX/$KREL/adopt-roles.sh" || return 2
  printf 'MEMORY_ROOT=%s\nCHARTER=%s\n' "$MR" "$CH" > "$FX/.memory-tree.conf"
  cp "$REPO/$CH" "$FX/$CH" || return 2
  (cd "$FX" && bash "$KREL/adopt-roles.sh" --scaffold >/dev/null 2>&1)
}
run_adopter() { (cd "$FX" && bash "$KREL/adopt-roles.sh" "$@" 2>&1); }

# ---- arm 1: a stage heading naming a workflow at the wrong stage --------------------------------
build_fixture; check_arm "arm 1 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
sed -i 's/^## Stage 2 — reuse$/## Stage 3 — reuse/' "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --check); rc=$?
check_arm "arm 1 a heading at the wrong stage refuses, naming the entry's own stage" \
   "$([ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'says stage 3 but the entry reuse is stage 2' && echo 1 || echo 0)"

# ---- arm 2: a catalogue workflow no heading names ----------------------------------------------
build_fixture; check_arm "arm 2 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
sed -i '/^## Stage 2 — reuse$/d' "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --check); rc=$?
check_arm "arm 2 a stage-2 workflow no heading names refuses, naming it" \
   "$([ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'the entry reuse (stage 2) of .* is named by no ## Stage heading' && echo 1 || echo 0)"

# ---- arm 3: a token surviving the substitution --------------------------------------------------
build_fixture; check_arm "arm 3 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
printf '{{UNKNOWN_TOKEN}}\n' >> "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --scaffold); rc=$?
check_arm "arm 3 a surviving token refuses the scaffold, naming its line" \
   "$([ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'a token survived the render' \
      && printf '%s' "$out" | grep -q '{{UNKNOWN_TOKEN}}' && echo 1 || echo 0)"

# ---- arm 4: a byte appended to a rendered agent type --------------------------------------------
build_fixture; check_arm "arm 4 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
_a=""; for _a in "$FX"/.claude/agents/*.md; do break; done
printf 'x' >> "$_a"
out=$(run_adopter --check); rc=$?
check_arm "arm 4 an agent type with one byte appended is stale, named with the scaffold remedy" \
   "$([ "$rc" = 1 ] && printf '%s' "$out" | grep -qF "drift .claude/agents/${_a##*/}" \
      && printf '%s' "$out" | grep -q 'adopt-roles.sh --scaffold$' && echo 1 || echo 0)"

# ---- arm 5: an unknown argument -----------------------------------------------------------------
build_fixture; check_arm "arm 5 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
out=$(run_adopter --render); rc=$?
check_arm "arm 5 an unknown argument is the usage refusal, exit 2" \
   "$([ "$rc" = 2 ] && printf '%s' "$out" | grep -q '^usage: ' && echo 1 || echo 0)"

[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL the suite executed $n assertions, under its floor of $FLOOR_ASSERTIONS — a block of arms was skipped"; fail=$((fail+1)); }
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ] || { echo "FAIL ($fail of $n)"; exit 1; }
