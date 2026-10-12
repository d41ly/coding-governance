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
# argument; the renderer's task part sent to the hooks kit's spawn guard (arm 6, which SKIPs out loud
# without that kit or node); an `export` conf line with a trailing comment (arm 7); the roster verb's
# one line per role and its refusal of a line past 200 characters (arm 8). Every arm is a
# self-contained block below the prologue, so a slice of the prologue and one
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
# The python launcher, by an inline candidate loop RUN per candidate: this suite defines no helper
# for it (TOOL-aOrientedCast-15 S4), and being on PATH is not evidence of a launcher that runs.
PY=""; for _c in "${GOV_PYTHON:-}" python3 python py; do [ -n "$_c" ] && "$_c" -c 'import sys' >/dev/null 2>&1 && { PY=$_c; break; }; done
[ -n "$PY" ] || { echo "adopt-roles.test: no python launcher ran (GOV_PYTHON, python3, python, py)"; exit 2; }
# MR and CH through the library's one conf grammar, as the adopter reads them (S6), never a `sed`.
CONF_READ='import pathlib, sys
sys.path.insert(0, sys.argv[1])
import roles_lib
print(roles_lib.read_conf_key(pathlib.Path(sys.argv[2]), sys.argv[3]) or "")'
MR=$("$PY" -B -c "$CONF_READ" "$HERE" "$REPO/.memory-tree.conf" MEMORY_ROOT); MR=${MR%$'\r'}
CH=$("$PY" -B -c "$CONF_READ" "$HERE" "$REPO/.memory-tree.conf" CHARTER); CH=${CH%$'\r'}
[ -n "$MR" ] && [ -n "$CH" ] && [ -f "$REPO/$CH" ] || { echo "adopt-roles.test: $REPO/.memory-tree.conf names no MEMORY_ROOT or no CHARTER file"; exit 2; }
[ -f "$ADOPTER" ] || { echo "adopt-roles.test: no adopter at $ADOPTER"; exit 2; }
TMP_ROOT=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP_ROOT"' EXIT
# 10, then +3 for arm 7 (TOOL-aOrientedCast-15). Arm 6 is NOT in the floor: it SKIPs out loud on a
# host with no hooks kit or no node, and a skip must not red the floor.
# +3 for arm 8 (TOOL-aOrientedCast-17).
FLOOR_ASSERTIONS=16
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

# ---- arm 6: the renderer's task part, sent as an Agent prompt, is admitted by the spawn guard ----
# TOOL-aOrientedCast-15 S4: the renderer and the hooks kit's rule 6 hash the same `## Task` bytes, and
# nothing but this arm runs the one against the other. The hooks kit is found the derived way the
# renderer finds the kickoff kit; with no hooks kit or no node the arm SKIPs, naming what is absent.
HK=$("$PY" -B -c 'import sys
sys.path.insert(0, sys.argv[1])
import roles_lib
try:
    print(roles_lib.resolve_kit_dir("hooks", "agent-cap.js", sys.argv[1]).as_posix())
except LookupError:
    pass' "$HERE"); HK=${HK%$'\r'}
if [ -z "$HK" ]; then
  echo "SKIP arm 6 — no hooks kit holding agent-cap.js was found from $KREL"
elif ! command -v node >/dev/null 2>&1; then
  echo "SKIP arm 6 — no node on PATH to run $HK/agent-cap.js"
else
  build_fixture
  A6P="$MR/builds/bx/prompts/$(date +%F)-prompt-TOOL-bx-1-1-researcher.md"
  mkdir -p "$FX/$MR/builds/bx/prompts"
  (cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build bx --unit TOOL-bx-1 \
     --input "question=which mechanism fits" --out "$A6P" --part task) > "$TMP_ROOT/a6.task" 2>"$TMP_ROOT/a6.err"; rc=$?
  FXN=$(cd "$FX" && { pwd -W 2>/dev/null || pwd; })
  "$PY" -c 'import json, sys
print(json.dumps({"tool_name": "Agent", "cwd": sys.argv[1], "session_id": "a6-s", "prompt_id": "a6-p-" + sys.argv[3],
                  "tool_use_id": "a6-u", "tool_input": {"subagent_type": "gov-researcher",
                  "prompt": open(sys.argv[2], newline="", encoding="utf-8").read()}}))' \
    "$FXN" "$TMP_ROOT/a6.task" "$$" > "$TMP_ROOT/a6.json"
  (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR node "$HK/agent-cap.js" < "$TMP_ROOT/a6.json" >/dev/null 2>"$TMP_ROOT/a6.hook"); hrc=$?
  check_arm "arm 6 the renderer's task part is admitted by the spawn guard" \
     "$([ "$rc" = 0 ] && [ "$hrc" = 0 ] && [ ! -s "$TMP_ROOT/a6.hook" ] && echo 1 || echo 0)"
  [ "$rc" = 0 ] && [ "$hrc" = 0 ] && [ ! -s "$TMP_ROOT/a6.hook" ] || sed 's/^/    /' "$TMP_ROOT/a6.err" "$TMP_ROOT/a6.hook"
  msha=$(tr -d '\r' < "$TMP_ROOT/a6.task" | sed -n '1s/.* task-sha=\([0-9a-f]\{12\}\) -->$/\1/p')
  out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" check "$A6P" 2>&1); rc=$?
  check_arm "arm 6 check re-derives the marker's task-sha" \
     "$([ "$rc" = 0 ] && [ -n "$msha" ] && printf '%s' "$out" | tr -d '\r' | grep -q " task-sha=$msha\$" && echo 1 || echo 0)"
fi

# ---- arm 7: an `export` conf line with a trailing comment ---------------------------------------
# TOOL-aOrientedCast-15 S6: the adopter reads MEMORY_ROOT with the library's conf grammar. The base
# adopter's bare `sed` read the `export` form as absent and exited 2.
build_fixture; mkdir -p "$TMP_ROOT/a7" && cp -R "$FX/.claude/skills" "$FX/.claude/agents" "$TMP_ROOT/a7"/
printf 'export MEMORY_ROOT=%s  # note\nCHARTER=%s\n' "$MR" "$CH" > "$FX/.memory-tree.conf"
out=$(run_adopter --scaffold); rc=$?
out2=$(run_adopter --check); rc2=$?
check_arm "arm 7 an export conf line with a trailing comment scaffolds and checks clean" \
   "$([ "$rc" = 0 ] && [ "$rc2" = 0 ] && echo 1 || echo 0)"
check_arm "arm 7 ...the rendered Skill carries no comment" \
   "$([ -f "$FX/.claude/skills/build/SKILL.md" ] && ! grep -q '# note' "$FX/.claude/skills/build/SKILL.md" && echo 1 || echo 0)"
check_arm "arm 7 ...and the Skill and every agent type name the root the plain conf rendered, byte for byte" \
   "$(diff -r -q "$TMP_ROOT/a7/skills" "$FX/.claude/skills" >/dev/null && diff -r -q "$TMP_ROOT/a7/agents" "$FX/.claude/agents" >/dev/null && echo 1 || echo 0)"

# ---- arm 8: the roster verb prints one line per role, and refuses an over-long one --------------
# TOOL-aOrientedCast-17 S8: `handoff.py roster` is what the playbook's derived placeholder reads, so
# a line past the one-line region's 200 characters must refuse with nothing on stdout.
build_fixture; check_arm "arm 8 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
_nr=$(ls "$FX/$KREL/agents/"*.agent.md | wc -l | tr -d ' ')
out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" roster 2>/dev/null); rc=$?
_nl=$(printf '%s\n' "$out" | tr -d '\r' | grep -c '^- `[a-z-]*`: ')
check_arm "arm 8 roster exits 0 with one backticked-slot line per role file" \
   "$([ "$rc" = 0 ] && [ "$_nr" -gt 0 ] && [ "$_nl" = "$_nr" ] && [ "$(printf '%s\n' "$out" | wc -l | tr -d ' ')" = "$_nr" ] && echo 1 || echo 0)"
_pad=$(printf '%200s' '' | tr ' ' 'x')
sed -i "s/^description: \(.*\)\.\(\r\{0,1\}\)\$/description: \1$_pad.\2/" "$FX/$KREL/agents/gov-builder.agent.md"
(cd "$FX" && "$PY" -B "$KREL/handoff.py" roster) > "$TMP_ROOT/a8.out" 2>"$TMP_ROOT/a8.err"; rc=$?
check_arm "arm 8 a gov-builder line lengthened by 200 characters refuses, naming it, with stdout empty" \
   "$([ "$rc" = 1 ] && grep -q 'gov-builder' "$TMP_ROOT/a8.err" && [ ! -s "$TMP_ROOT/a8.out" ] && echo 1 || echo 0)"

[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL the suite executed $n assertions, under its floor of $FLOOR_ASSERTIONS — a block of arms was skipped"; fail=$((fail+1)); }
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ] || { echo "FAIL ($fail of $n)"; exit 1; }
