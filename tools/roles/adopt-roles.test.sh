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
# one line per role and its refusal of a line past 200 characters (arm 8); the agents verb's two
# lines for a direct spawn, its tokens counted once per message id, each added to the build's agent
# ledger exactly once across two runs, a run without `--write` writing nothing, a harness run's two
# agent lines and one returned line, and a prompt opening with a blank line still matching (arm 9);
# the stand-in render's refusal, R15 both ways and over eight bad rows, R13, R14 and R0 (arm 10);
# the roles kit's reading of a prompt's marker line and of the charter's micro-format fence
# against the hooks kit's own (arm 11, which SKIPs out loud as arm 6 does); a `--scaffold` whose
# agent render refuses, which exits 1 naming the refusal and writes no Skill (arm 13); the cited
# harnesses moved into a renamed directory behind `rendered` receipt rows, which the Skill then names
# there, and a citation extending a held one, which keeps its own plain path (arm 14); a decoy at the
# repository root for each citation that is no harness, which the Skill never names, and a receipt
# row placing the first of them, which it does (arm 15); a root install whose repository has a
# sibling directory holding each cited harness, which the citation pass lists nowhere (arm 16); and
# a harness held only in the directory above the tool root with no receipt, which the Skill and the
# role index both name there (arm 17). Every arm is a self-contained block below the prologue, so a
# slice of the prologue and one block runs that arm alone.
#
# WHAT THIS DOES NOT CHECK: what the rendered Skill or an agent type SAYS beyond the citation paths
# of arms 14 to 17, which the catalogue checker and the renderer's own self-test grade; the
# `--scaffold` restart notice's wording; or an adopter run at another install prefix, since the
# fixture mirrors this repository's own, arm 16's root install aside. Arms 14 to 17 read only the
# citations the shipped template holds, so a harness the table lists and the template does not cite
# is in none of them, and arm 15 reads only a citation inside backticks. Arm 16 does not check what
# the role index lists at its root install, where the index's own probe names each sibling harness
# as `../<home>/<file>`, outside the repository (TOOL-dRenderedAnchor-3 section 3). The kit path
# needs two or more segments for arm 17, which does not run `--check` over its install and places
# nothing for `unattended-unit.js`, which the template does not cite (TOOL-dRenderedAnchor-4).
# Arm 11 does not compare a refusal's wording, any marker field beyond the whole line, or any
# micro-format head but `agent` and `returned`. Arm 13 does not check which rule refused: any
# non-zero exit of the agent render takes the same branch, so it grades the adopter's handling of a
# refusal, and R10 only as the trigger.
#
# Withheld from the payload by the kit's descriptor (`project-owned`): its subject is the adopter in
# this directory, so it has a job only where that source changes.
set -u
HERE=.; [[ $0 == */* ]] && HERE=${0%/*}; HERE="$(cd "$HERE" && pwd)"
ADOPTER="${ROLES_ADOPTER:-$HERE/adopt-roles.sh}"
REPO=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "adopt-roles.test: not inside a git repository"; exit 2; }
KREL=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-prefix 2>/dev/null) || exit 2
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
# +3 for arm 8 (TOOL-aOrientedCast-17). +3 for arm 9 (TOOL-aOrientedCast-20). +4 for arm 9 and +10
# for arm 10 (TOOL-aOrientedCast-25); arm 11 is out of the floor, as arm 6 is. +1 for arm 6's named
# spawn and +4 for arm 12 (TOOL-aOrientedCast-27): arm 6's one floored assertion is taken back off the
# floor by the SKIP that announces the arm unrun, so a skip still cannot red it.
# +2 for arm 13 (TOOL-dRedressedBar-6). +3 for arm 14 (TOOL-dRenderedAnchor-2). +1 for arm 14, +3
# for arm 15 and +2 for arm 16 (TOOL-dRenderedAnchor-3). +1 for arm 17 (TOOL-dRenderedAnchor-4).
FLOOR_ASSERTIONS=50
n=0; fail=0
check_arm() { n=$((n+1)); if [ "$2" = 1 ]; then echo "ok   $1"; else echo "FAIL $1"; fail=$((fail+1)); fi; }
FX=""; FXK="$KREL"
build_fixture() { # [kit path] [fixture dir] -> $FX: a repo holding this kit at the kit path, $KREL
  # unless given, with $ADOPTER as its adopter, scaffolded; rc of the scaffold. The fixture directory
  # is $TMP_ROOT/fx<n> unless given, and run_adopter reads the kit path the last call used.
  FXK=${1:-$KREL}; FX=${2:-$TMP_ROOT/fx$n}
  _chd=.; [[ $CH == */* ]] && _chd=${CH%/*}; mkdir -p "$FX/$FXK" "$FX/$_chd" || return 2
  git init -q "$FX" || return 2
  cp -R "$HERE"/. "$FX/$FXK"/ && cp "$ADOPTER" "$FX/$FXK/adopt-roles.sh" || return 2
  printf 'MEMORY_ROOT=%s\nCHARTER=%s\n' "$MR" "$CH" > "$FX/.memory-tree.conf"
  cp "$REPO/$CH" "$FX/$CH" || return 2
  (cd "$FX" && bash "$FXK/adopt-roles.sh" --scaffold >/dev/null 2>&1)
}
run_adopter() { (cd "$FX" && bash "$FXK/adopt-roles.sh" "$@" 2>&1); }
# THE CITED HARNESS PAIRS, read by this suite and never through `roles_lib` (TOOL-dRenderedAnchor-3
# S5): the `harness` of each `[[workflow]]` entry of `<kit>/workflows.toml` whose `driver` is
# `workflow`, split after a literal `{prefix}/` into home and file, kept when `<kit>/SKILL.template.md`
# holds `{{TOOL_ROOT}}<home>/<file>`; one `<home>/<file>` line per distinct pair, in table order. An
# arm guarding the citation pass never takes its population from the pattern that pass reads, so a
# pattern that stops matching a harness reds the arm rather than shrinking it.
HARNESS_PAIRS_READ='import pathlib, sys, tomllib
kit = pathlib.Path(sys.argv[1])
with open(kit / "workflows.toml", "rb") as fh:
    table = tomllib.load(fh).get("workflow") or []
text = (kit / "SKILL.template.md").read_text(encoding="utf-8")
pairs = []
for w in table:
    harness = w.get("harness") if isinstance(w, dict) and w.get("driver") == "workflow" else None
    if not isinstance(harness, str) or not harness.startswith("{prefix}/"):
        continue
    pair = harness[len("{prefix}/"):]
    home, _, name = pair.partition("/")
    if home and name and "/" not in name and "{{TOOL_ROOT}}" + pair in text and pair not in pairs:
        pairs.append(pair)
sys.stdout.buffer.write("".join(p + "\n" for p in pairs).encode("utf-8"))'

# ---- arm 1: a stage heading naming a workflow at the wrong stage --------------------------------
build_fixture; check_arm "arm 1 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
sed -i 's/^## Stage 2 — reuse$/## Stage 3 — reuse/' "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --check); rc=$?
check_arm "arm 1 a heading at the wrong stage refuses, naming the entry's own stage" \
   "$([ "$rc" = 1 ] && [[ $out == *'says stage 3 but the entry reuse is stage 2'* ]] && echo 1 || echo 0)"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

# ---- arm 2: a catalogue workflow no heading names ----------------------------------------------
build_fixture; check_arm "arm 2 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
sed -i '/^## Stage 2 — reuse$/d' "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --check); rc=$?
check_arm "arm 2 a stage-2 workflow no heading names refuses, naming it" \
   "$([ "$rc" = 1 ] && _re2=$'the entry reuse \\(stage 2\\) of [^\n]* is named by no ## Stage heading' && [[ $out =~ $_re2 ]] && echo 1 || echo 0)"

# ---- arm 3: a token surviving the substitution --------------------------------------------------
build_fixture; check_arm "arm 3 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
printf '{{UNKNOWN_TOKEN}}\n' >> "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --scaffold); rc=$?
check_arm "arm 3 a surviving token refuses the scaffold, naming its line" \
   "$([ "$rc" = 1 ] && [[ $out == *'a token survived the render'* ]] \
      && [[ $out == *'{{UNKNOWN_TOKEN}}'* ]] && echo 1 || echo 0)"

# ---- arm 4: a byte appended to a rendered agent type --------------------------------------------
build_fixture; check_arm "arm 4 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
_a=""; for _a in "$FX"/.claude/agents/*.md; do break; done
printf 'x' >> "$_a"
out=$(run_adopter --check); rc=$?
check_arm "arm 4 an agent type with one byte appended is stale, named with the scaffold remedy" \
   "$([ "$rc" = 1 ] && [[ $out == *"drift .claude/agents/${_a##*/}"* ]] \
      && [[ $'\n'$out$'\n' == *$'\n'"roles: remedy — bash $KREL/adopt-roles.sh --scaffold"$'\n'* ]] && echo 1 || echo 0)"

# ---- arm 5: an unknown argument -----------------------------------------------------------------
build_fixture; check_arm "arm 5 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
out=$(run_adopter --render); rc=$?
check_arm "arm 5 an unknown argument is the usage refusal, exit 2" \
   "$([ "$rc" = 2 ] && [[ $'\n'$out == *$'\n''usage: '* ]] && echo 1 || echo 0)"

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
  echo "SKIP arm 6 — no hooks kit holding agent-cap.js was found from $KREL"; FLOOR_ASSERTIONS=$((FLOOR_ASSERTIONS-1))
elif ! command -v node >/dev/null 2>&1; then
  echo "SKIP arm 6 — no node on PATH to run $HK/agent-cap.js"; FLOOR_ASSERTIONS=$((FLOOR_ASSERTIONS-1))
else
  build_fixture
  printf -v _a6day '%(%F)T' -1; A6P="$MR/builds/bx/prompts/$_a6day-prompt-TOOL-bx-1-1-researcher.md"
  mkdir -p "$FX/$MR/builds/bx/prompts"
  (cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build bx --unit TOOL-bx-1 \
     --input "question=which mechanism fits" --out "$A6P" --part task) > "$TMP_ROOT/a6.task" 2>"$TMP_ROOT/a6.err"; rc=$?
  FXN=$(cd "$FX" && { pwd -W 2>/dev/null || pwd; })
  # TOOL-aOrientedCast-27: the payload's `description` is the name the render printed on stderr after
  # `handoff: description — `, and a second payload carries the role's slot name in its place. The
  # rendered name, JSON-quoted as the hook's refusal spells it, goes to a6.name.
  "$PY" -c 'import json, sys
err = open(sys.argv[4], encoding="utf-8").read().replace("\r", "").split("\n")
name = next((l[len("handoff: description — "):] for l in err if l.startswith("handoff: description — ")), None)
for out, desc in ((sys.argv[5], name), (sys.argv[6], "bx · TOOL-bx-1 · researcher")):
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"tool_name": "Agent", "cwd": sys.argv[1], "session_id": "a6-s", "prompt_id": "a6-p-" + sys.argv[3],
                   "tool_use_id": "a6-u", "tool_input": {"subagent_type": "gov-researcher", "description": desc,
                   "prompt": open(sys.argv[2], newline="", encoding="utf-8").read()}}, fh)
sys.stdout.buffer.write(json.dumps(name, ensure_ascii=False).encode("utf-8"))' \
    "$FXN" "$TMP_ROOT/a6.task" "$$" "$TMP_ROOT/a6.err" "$TMP_ROOT/a6.json" "$TMP_ROOT/a6s.json" > "$TMP_ROOT/a6.name"
  (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR node "$HK/agent-cap.js" < "$TMP_ROOT/a6.json" >/dev/null 2>"$TMP_ROOT/a6.hook"); hrc=$?
  check_arm "arm 6 the renderer's task part, named as it printed, is admitted by the spawn guard" \
     "$([ "$rc" = 0 ] && [ "$hrc" = 0 ] && [ ! -s "$TMP_ROOT/a6.hook" ] && echo 1 || echo 0)"
  [ "$rc" = 0 ] && [ "$hrc" = 0 ] && [ ! -s "$TMP_ROOT/a6.hook" ] || sed 's/^/    /' "$TMP_ROOT/a6.err" "$TMP_ROOT/a6.hook"
  (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR node "$HK/agent-cap.js" < "$TMP_ROOT/a6s.json" >/dev/null 2>"$TMP_ROOT/a6s.hook"); hrc=$?
  check_arm "arm 6 ...and named by the role's slot it is refused, naming the rendered name" \
     "$([ "$hrc" = 2 ] && [ "$(<"$TMP_ROOT/a6.name")" != null ] && grep -qF -- "$(<"$TMP_ROOT/a6.name")" "$TMP_ROOT/a6s.hook" && echo 1 || echo 0)"
  msha=$(tr -d '\r' < "$TMP_ROOT/a6.task" | sed -n '1s/.* task-sha=\([0-9a-f]\{12\}\) -->$/\1/p')
  out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" check "$A6P" 2>&1); rc=$?; out=${out//$'\r'/}
  check_arm "arm 6 check re-derives the marker's task-sha" \
     "$([ "$rc" = 0 ] && [ -n "$msha" ] && [[ $out$'\n' == *" task-sha=$msha"$'\n'* ]] && echo 1 || echo 0)"
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
out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" roster 2>/dev/null); rc=$?; mapfile -t _l8 <<< "$out"
_re8='^- `[a-z-]*`: '; _nl=0; for _x8 in "${_l8[@]}"; do [[ $_x8 =~ $_re8 ]] && _nl=$((_nl+1)); done
check_arm "arm 8 roster exits 0 with one backticked-slot line per role file" \
   "$([ "$rc" = 0 ] && [ "$_nr" -gt 0 ] && [ "$_nl" = "$_nr" ] && _nb=${out//[!$'\n']/} && [ "$(( ${#_nb} + 1 ))" = "$_nr" ] && echo 1 || echo 0)"
_pad=$(printf '%200s' '' | tr ' ' 'x')
sed -i "s/^description: \(.*\)\.\(\r\{0,1\}\)\$/description: \1$_pad.\2/" "$FX/$KREL/agents/gov-builder.agent.md"
(cd "$FX" && "$PY" -B "$KREL/handoff.py" roster) > "$TMP_ROOT/a8.out" 2>"$TMP_ROOT/a8.err"; rc=$?
check_arm "arm 8 a gov-builder line lengthened by 200 characters refuses, naming it, with stdout empty" \
   "$([ "$rc" = 1 ] && grep -q 'gov-builder' "$TMP_ROOT/a8.err" && [ ! -s "$TMP_ROOT/a8.out" ] && echo 1 || echo 0)"

# ---- arm 9: the agents verb's two lines for a direct spawn, each added to the ledger once ------
# TOOL-aOrientedCast-20 S6: a build folder and a session tree, the unit's section 6 fixture: an
# `Agent` call whose prompt opens with the handoff's marker line, its notification, and a transcript
# whose two records sharing one message id count once, at the larger output, so a per-record sum
# reads 1.9k where the line says 1.6k. Arm 9 asks git nothing about its own location.
A9_WRITE='import json, pathlib, sys
fx, sess, hrel = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
def put(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = rows if isinstance(rows, str) else "".join(json.dumps(r) + "\n" for r in rows)
    path.write_text(text, encoding="utf-8", newline="\n")
marker = "<!-- gov:handoff role=gov-builder build=tFix unit=TOOL-tFix-1 path=%s role-sha=%s task-sha=%s -->" % (
    hrel, "0" * 12, "1" * 12)
put(fx / hrel.split("/prompts/")[0] / "spec" / "2026-10-13-spec-TOOL-tFix-1.md", "# TOOL-tFix-1 — t\n")
put(fx / hrel, marker + "\n\n## Task\n\nt\n")
def use(tid, name, inp):
    return {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": tid, "name": name, "input": inp}]}}
def res(tid, result):
    return {"type": "user", "toolUseResult": result, "message": {"content": [{"type": "tool_result", "tool_use_id": tid}]}}
put(sess, [use("toolu_A", "Agent", {"subagent_type": "gov-builder", "prompt": marker + "\n\n## Task\n"}),
           res("toolu_A", {"status": "async_launched", "agentId": "a0000000000000001", "resolvedModel": "claude-test-1"}),
           use("toolu_W", "Workflow", {"scriptPath": "harness/unit.js",
                                       "args": {"slug": "tFix", "briefPath": hrel}}),
           res("toolu_W", {"runId": "wf_00000001-aaa"}),
           {"type": "user", "message": {"content": "<task-notification>\n<tool-use-id>toolu_A</tool-use-id>\n"
                                                   "<status>completed</status>\n</task-notification>"}}])
def turn(at, model, effort, mid, tokens, writes=()):
    return {"type": "assistant", "timestamp": "2026-10-13T%s.000Z" % at, "effort": effort,
            "message": {"model": model, "id": mid, "usage": {"output_tokens": tokens},
                        "content": [{"type": "tool_use", "name": n, "input": {"file_path": p}} for n, p in writes]}}
sub = sess.with_suffix("") / "subagents"
# The Claude Code session directory holding one subdirectory per Workflow run, not the review-harness kit.
WORKFLOW_RUNS_DIR = "workflows"
put(sub / "agent-a0000000000000001.jsonl", [{"type": "user", "timestamp": "2026-10-13T10:00:00.000Z"},
    turn("10:00:05", "claude-test-1", "medium", "m1", 300, [("Write", "a.txt")]),
    turn("10:00:06", "claude-test-1", "medium", "m1", 700, [("Write", "b.txt")]),
    turn("10:07:47", "claude-test-1", "medium", "m2", 900, [("Edit", "a.txt")])])
put(sub / "agent-a0000000000000001.meta.json", json.dumps({"agentType": "gov-builder", "description": "build one"}))
wf = sub / WORKFLOW_RUNS_DIR / "wf_00000001-aaa"
put(wf / "journal.jsonl", [{"type": "started", "agentId": "a0000000000000002", "label": "unit:TOOL-tFix-1"},
    {"type": "result", "agentId": "a0000000000000002", "result": {"committed": True, "sha": "abc123def"}},
    {"type": "started", "agentId": "a0000000000000003", "label": "commit:specs:tFix"}])
put(wf / "agent-a0000000000000002.jsonl", [turn("10:00:00", "claude-test-2", "xhigh", "m3", 1000),
                                           turn("10:00:45", "claude-test-2", "xhigh", "m4", 500)])
put(wf / "agent-a0000000000000002.meta.json", json.dumps({"agentType": "gov-builder"}))
put(wf / "agent-a0000000000000003.jsonl", [turn("10:01:00", "claude-test-2", "high", "m5", 10)])
put(wf / "agent-a0000000000000003.meta.json", json.dumps({"agentType": "workflow-subagent"}))'
build_fixture; check_arm "arm 9 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
A9H="$MR/builds/tFix/prompts/2026-10-13-prompt-TOOL-tFix-1-1-builder.md"
A9S="$TMP_ROOT/s9/projects/p/11111111-1111-4111-8111-111111111111.jsonl"
"$PY" -B -c "$A9_WRITE" "$FX" "$A9S" "$A9H" || echo "    arm 9: the fixture writer exited non-zero"
A9L1="- agent — gov-builder · effort medium · model claude-test-1 · TOOL-tFix-1 · prompt [${A9H##*/}]($A9H) · writes product · gates lexicon naming predicates · run direct/a0000000000000001"
A9L2="- returned — gov-builder · wrote 2 files · 7m47s · 1.6k out · run direct/a0000000000000001"
out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" agents --handoff "$A9H" --session "$A9S" --write 2>"$TMP_ROOT/a9.err"); rc=$?; out=${out//$'\r'/}
check_arm "arm 9 agents prints a direct spawn's agent and returned lines, its tokens the per-message-id maximum" \
   "$([ "$rc" = 0 ] && [ "$out" = "$A9L1"$'\n'"$A9L2" ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || sed 's/^/    /' "$TMP_ROOT/a9.err"
(cd "$FX" && "$PY" -B "$KREL/handoff.py" agents --handoff "$A9H" --session "$A9S" --write >/dev/null 2>&1)
_lg=$(ls "$FX/$MR/builds/tFix/build/"*-agent-ledger.md 2>/dev/null)
_ll1=${A9L1/"($A9H)"/"(../prompts/${A9H##*/})"}
check_arm "arm 9 ...and after a second run the build's one agent ledger holds each line, its link re-rooted, once" \
   "$([[ -n $_lg && $_lg != *$'\n'* ]] && [ "$(tr -d '\r' < "$_lg" | grep -cxF -e "$_ll1")" = 1 ] \
      && [ "$(tr -d '\r' < "$_lg" | grep -cxF -e "$A9L2")" = 1 ] && echo 1 || echo 0)"
# TOOL-aOrientedCast-25 S13: a call without --write writes nothing, so one made mid-pass leaves the
# tree as it found it. It runs BEFORE the run's lines are written, so a verb that wrote anyway would
# add them here and move the hash.
_h0=$(git hash-object "$_lg"); _d0=$(ls -A "$FX/$MR/builds/tFix/build")
(cd "$FX" && "$PY" -B "$KREL/handoff.py" agents --run wf_00000001-aaa --session "$A9S" >/dev/null 2>"$TMP_ROOT/a9n.err"); rc=$?
check_arm "arm 9 agents without --write leaves the ledger and the build folder unchanged, naming --write" \
   "$([ "$rc" = 0 ] && [ "$(git hash-object "$_lg")" = "$_h0" ] && [ "$(ls -A "$FX/$MR/builds/tFix/build")" = "$_d0" ] \
      && grep -q -e '--write' "$TMP_ROOT/a9n.err" && echo 1 || echo 0)"
# TOOL-aOrientedCast-25 S4: the journal branch, over the same fixture. a0000000000000003 has no
# `result`, so it prints no returned line.
A9L3="- agent — gov-builder · effort xhigh · model claude-test-2 · TOOL-tFix-1 · prompt [${A9H##*/}]($A9H) · writes product · gates lexicon naming predicates · run wf_00000001-aaa/a0000000000000002"
A9L4="- returned — gov-builder · committed abc123def · 45s · 1.5k out · run wf_00000001-aaa/a0000000000000002"
A9L5="- agent — workflow-subagent · effort high · model claude-test-2 · commit:specs:tFix · prompt [${A9H##*/}]($A9H) · writes none · gates none · run wf_00000001-aaa/a0000000000000003"
out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" agents --run wf_00000001-aaa --session "$A9S" --write 2>"$TMP_ROOT/a9r.err"); rc=$?
check_arm "arm 9 agents --run prints the run's two agent lines and its one returned line" \
   "$([ "$rc" = 0 ] && [ "${out//$'\r'/}" = "$A9L3"$'\n'"$A9L4"$'\n'"$A9L5" ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || sed 's/^/    /' "$TMP_ROOT/a9r.err"
_r=0
for _l in "$_ll1" "$A9L2" "${A9L3/"($A9H)"/"(../prompts/${A9H##*/})"}" "$A9L4" "${A9L5/"($A9H)"/"(../prompts/${A9H##*/})"}"; do
  [ "$(tr -d '\r' < "$_lg" | grep -cxF -e "$_l")" = 1 ] && _r=$((_r+1))
done
check_arm "arm 9 ...and the ledger gains exactly those three" \
   "$([ "$(tr -d '\r' < "$_lg" | grep -c '^- ')" = 5 ] && [ "$_r" = 5 ] && echo 1 || echo 0)"
# TOOL-aOrientedCast-25 S2: the spawn guard admits a prompt opening with a blank line, so the verb
# matches it too.
"$PY" -B -c 'import json, sys
rows = [json.loads(ln) for ln in open(sys.argv[1], encoding="utf-8") if ln.strip()]
for r in rows:
    for c in (r.get("message") or {}).get("content") or []:
        if isinstance(c, dict) and c.get("id") == "toolu_A":
            c["input"]["prompt"] = "\n" + c["input"]["prompt"]
open(sys.argv[1], "w", encoding="utf-8", newline="\n").write("".join(json.dumps(r) + "\n" for r in rows))' "$A9S"
out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" agents --handoff "$A9H" --session "$A9S" 2>"$TMP_ROOT/a9b.err"); rc=$?
check_arm "arm 9 a prompt opening with a blank line still matches its handoff" \
   "$([ "$rc" = 0 ] && [ "${out//$'\r'/}" = "$A9L1"$'\n'"$A9L2" ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || sed 's/^/    /' "$TMP_ROOT/a9b.err"

# ---- arm 10: the stand-in refusal, R15 both ways and over eight bad rows, R13, R14 and R0 --------
# TOOL-aOrientedCast-25 S3: the rules TOOL-aOrientedCast-17 and TOOL-aOrientedCast-19 added, each
# answered by the shipped checker over the shipped role files, charter and renderer the fixture
# copies. Step 1 is the liveness half: a fixture that is not clean reds there, before any staged
# break is read.
build_fixture
A10W="$FX/$MR/project/role-stand-in-waiver.txt"
A10P="$FX/$MR/builds/tFix/prompts"
A10R="$TMP_ROOT/a10.out"
_t=$'\t'
A10G="2026-10-13${_t}owner a${_t}gov-researcher${_t}tFix${_t}this tool exposes no sub-agent primitive"
mkdir -p "$A10P" "$FX/$MR/project"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 the fixture's catalogue checks clean, with no stand-in waiver or declaration" \
   "$([ "$rc" = 0 ] && grep -qF '0 stand-in waiver(s), 0 stand-in declaration(s)' "$A10R" && echo 1 || echo 0)"
[ "$rc" = 0 ] || sed 's/^/    /' "$A10R"
(cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --input "question=q" --stand-in) > "$TMP_ROOT/a10.render" 2>"$TMP_ROOT/a10.err"; rc=$?
_ls=$(ls -A "$A10P")
check_arm "arm 10 a stand-in render with no registry refuses, naming it, and writes nothing" \
   "$([ "$rc" = 1 ] && grep -qF "role-stand-in-waiver.txt" "$TMP_ROOT/a10.err" && [ -z "$_ls" ] && echo 1 || echo 0)"
printf '%s\n' "$A10G" > "$A10W"
A10D=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --input "question=q" --stand-in 2>/dev/null); rc=$?
A10D=${A10D%$'\r'}
check_arm "arm 10 ...and with the owner's row it writes the declaration, named -researcher-stand-in.md" \
   "$([ "$rc" = 0 ] && [[ "$A10D" == *-researcher-stand-in.md ]] && [ -f "$FX/$A10D" ] && echo 1 || echo 0)"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 the row and its declaration join: one waiver note, exit 0" \
   "$([ "$rc" = 0 ] && [ "$(grep -c '^roles: note: stand-in waiver' "$A10R")" = 1 ] \
      && grep -qF '1 stand-in waiver(s), 1 stand-in declaration(s)' "$A10R" && echo 1 || echo 0)"
mv "$A10W" "$TMP_ROOT/a10.waiver"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a declaration no row covers is one R15 line, naming it, its role and its build" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R15 — ' "$A10R")" = 1 ] \
      && grep ': R15 — ' "$A10R" | grep -F "$A10D" | grep -F 'gov-researcher' | grep -qF 'tFix' && echo 1 || echo 0)"
mv "$TMP_ROOT/a10.waiver" "$A10W"; mv "$FX/$A10D" "$TMP_ROOT/a10.decl"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a row covering no declaration is one R15 line, stale" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R15 — ' "$A10R")" = 1 ] && grep ': R15 — ' "$A10R" | grep -qF 'stale' && echo 1 || echo 0)"
# The eight bad rows of TOOL-aOrientedCast-19's AC1, each otherwise the good row: four fields, a
# date that is no calendar date, an attribution that is not the owner's, a role with no file, the
# catalogue's one agent: false role, a build that is not a slug, an empty reason after a fifth TAB,
# and a second copy of the good row. They are registry lines 2 to 9.
mv "$TMP_ROOT/a10.decl" "$FX/$A10D"
printf '%s\n' "2026-10-13${_t}owner a${_t}gov-researcher${_t}tFix" \
  "2026-13-01${A10G#2026-10-13}" \
  "2026-10-13${_t}agent a${A10G#*owner a}" \
  "${A10G/gov-researcher/gov-ghost}" \
  "${A10G/gov-researcher/gov-session}" \
  "${A10G/tFix/t-Fix}" \
  "2026-10-13${_t}owner a${_t}gov-researcher${_t}tFix${_t}" \
  "$A10G" >> "$A10W"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
_r=0
for _i in 2 3 4 5 6 7 8 9; do
  [ "$(grep -cF "role-stand-in-waiver.txt:$_i: R15 — " "$A10R")" = 1 ] && _r=$((_r+1))
done
check_arm "arm 10 eight bad rows are eight R15 lines, naming registry lines 2 to 9 once each" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R15 — ' "$A10R")" = 8 ] && [ "$_r" = 8 ] && echo 1 || echo 0)"
printf '%s\n' "$A10G" > "$A10W"
cp "$FX/$KREL/agents/gov-orienter.agent.md" "$TMP_ROOT/a10.orienter"
sed -i 's/^mandatory: .*/mandatory: for every session/' "$FX/$KREL/agents/gov-orienter.agent.md"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a mandatory role whose workflow no hook enforces is one R13 line, naming its file" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R13 — ' "$A10R")" = 1 ] && grep ': R13 — ' "$A10R" | grep -qF 'gov-orienter.agent.md' && echo 1 || echo 0)"
cp "$TMP_ROOT/a10.orienter" "$FX/$KREL/agents/gov-orienter.agent.md"
cp "$FX/$KREL/agents/gov-spec-writer.agent.md" "$TMP_ROOT/a10.writer"
sed -i 's/^output: .*/output: specs/' "$FX/$KREL/agents/gov-spec-writer.agent.md"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a spec writer whose output lacks its folder is one R14 line, naming the folder" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R14 — ' "$A10R")" = 1 ] && grep ': R14 — ' "$A10R" | grep -qF '{{MEMORY_ROOT}}/builds/<slug>/spec/' && echo 1 || echo 0)"
cp "$TMP_ROOT/a10.writer" "$FX/$KREL/agents/gov-spec-writer.agent.md"
printf 'CHARTER=%s\n' "$CH" > "$FX/.memory-tree.conf"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a conf with its CHARTER line alone is unarmed, exit 2 naming MEMORY_ROOT" \
   "$([ "$rc" = 2 ] && grep -qF 'MEMORY_ROOT' "$A10R" && echo 1 || echo 0)"

# ---- arm 11: the roles kit reads a prompt's marker and the charter's fence as the hooks kit does --
# TOOL-aOrientedCast-25 S2 and S6, after arm 6's idiom: the hooks kit is found the derived way, and
# with no hooks kit or no node the arm SKIPs, naming what is absent. It stays out of the floor. Part A
# feeds five prompt variants to roles_lib.extract_prompt_marker and to the spawn guard; part B three
# charter copies to roles_lib.extract_microformat_shapes and to format-guard's readCharterShapes.
# WHAT IT DOES NOT COMPARE: a refusal's wording, any marker field beyond the whole line, and any head
# but `agent` and `returned`.
HK11=$("$PY" -B -c 'import sys
sys.path.insert(0, sys.argv[1])
import roles_lib
found = []
for anchor in ("agent-cap.js", "format-guard.js"):
    try:
        found.append(roles_lib.resolve_kit_dir("hooks", anchor, sys.argv[1]).as_posix())
    except LookupError:
        found.append("")
sys.stdout.write("|".join(found))' "$HERE")
HKA=${HK11%%|*}; HKF=${HK11#*|}
if [ -z "$HKA" ] || [ -z "$HKF" ]; then
  echo "SKIP arm 11 — no hooks kit holding agent-cap.js and format-guard.js was found from $KREL"
elif ! command -v node >/dev/null 2>&1; then
  echo "SKIP arm 11 — no node on PATH to run $HKA/agent-cap.js and $HKF/format-guard.js"
else
  build_fixture
  printf -v _d '%(%Y-%m-%d)T' -1
  A11P="$MR/builds/bx/prompts/$_d-prompt-TOOL-bx-1-1-researcher.md"
  mkdir -p "$FX/$MR/builds/bx/prompts" "$TMP_ROOT/a11"
  (cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build bx --unit TOOL-bx-1 \
     --input "question=which mechanism fits" --out "$A11P" --part task) > "$TMP_ROOT/a11/task" 2>"$TMP_ROOT/a11/err"
  FXN=$(cd "$FX" && { pwd -W 2>/dev/null || pwd; })
  # Each variant's bytes written exact, then its two answers: `admit` or `refuse`, one line per variant.
  # Every payload carries the name the render printed as its `description` (TOOL-aOrientedCast-27).
  "$PY" -B -c 'import json, pathlib, sys
sys.path.insert(0, sys.argv[1])
import roles_lib
out, fxn, pid = pathlib.Path(sys.argv[2]), sys.argv[3], sys.argv[4]
err = (out / "err").read_bytes().decode("utf-8").replace("\r", "").split("\n")
desc = next((l[len("handoff: description — "):] for l in err if l.startswith("handoff: description — ")), None)
t = (out / "task").read_bytes().decode("utf-8")
m = t.replace("\r", "").split("\n", 1)[0]
head, rest = t.split("\n", 1)
variants = {"v1": t, "v2": "\n" + t, "v3": t.replace("\r\n", "\n").replace("\n", "\r\n"),
            "v4": head.rstrip("\r") + " \n" + rest, "v5": "  " + t}
for name, text in variants.items():
    with open(out / (name + ".json"), "w", encoding="utf-8", newline="") as fh:
        json.dump({"tool_name": "Agent", "cwd": fxn, "session_id": "a11-s-" + name,
                   "prompt_id": "a11-p-%s-%s" % (name, pid), "tool_use_id": "a11-u-" + name,
                   "tool_input": {"subagent_type": "gov-researcher", "description": desc, "prompt": text}}, fh)
    hit = roles_lib.extract_prompt_marker(text)
    with open(out / (name + ".py"), "w", encoding="utf-8", newline="") as fh:
        fh.write("admit" if hit and hit.group(0) == m else "refuse")' "$HERE" "$TMP_ROOT/a11" "$FXN" "$$"
  _seen=""
  for _v in v1 v2 v3 v4 v5; do
    (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR node "$HKA/agent-cap.js" < "$TMP_ROOT/a11/$_v.json" >/dev/null 2>"$TMP_ROOT/a11/$_v.hook"); hrc=$?
    _js=refuse; [ "$hrc" = 0 ] && [ ! -s "$TMP_ROOT/a11/$_v.hook" ] && _js=admit
    _py=$(<"$TMP_ROOT/a11/$_v.py")
    _seen+=" $_js"
    check_arm "arm 11 prompt variant $_v: the spawn guard and extract_prompt_marker both $_js" \
       "$([ "$_js" = "$_py" ] && echo 1 || echo 0)"
  done
  check_arm "arm 11 ...and the five answers hold both an admit and a refuse" \
     "$([[ "$_seen" == *admit* && "$_seen" == *refuse* ]] && echo 1 || echo 0)"
  # Part B: three charter copies, each written as AGENTS.md in its own folder, the name format-guard reads.
  "$PY" -B -c 'import pathlib, sys
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
text = src.read_bytes().decode("utf-8").replace("\r\n", "\n")
d2 = "- `agent — <role> · run <run-id|direct>/<agent-id>`"
copies = {"c1": text, "c2": text.replace("\n<!-- /microformats -->\n", "\n%s\n<!-- /microformats -->\n" % d2, 1),
          "c3": text.replace("\n<!-- microformats -->\n", "\nx <!-- microformats -->\n", 1)}
for name, body in copies.items():
    (out / name).mkdir(parents=True, exist_ok=True)
    with open(out / name / "AGENTS.md", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)' "$REPO/$CH" "$TMP_ROOT/a11"
  _nn=0; _nd=0; _defs=$'\n'
  for _c in c1 c2 c3; do
    _cn=$(cd "$TMP_ROOT/a11/$_c" && { pwd -W 2>/dev/null || pwd; })
    _js=$(node -e 'const r = require(process.argv[1]).readCharterShapes(process.argv[2])
const s = r.shapes || {}
process.stdout.write(["agent", "returned"].map((h) => s[h] ? s[h].def : "none").join("\n"))' "$HKF/format-guard.js" "$_cn")
    _py=$("$PY" -B -c 'import sys
sys.path.insert(0, sys.argv[1])
import roles_lib
s = roles_lib.extract_microformat_shapes(roles_lib.load_text(sys.argv[2]))
sys.stdout.buffer.write("\n".join(s.get(h, "none") for h in ("agent", "returned")).encode("utf-8"))' "$HERE" "$TMP_ROOT/a11/$_c/AGENTS.md")
    _a=${_js%%$'\n'*}
    if [ "$_a" = none ]; then _nn=$((_nn+1))
    elif [[ "$_defs" != *$'\n'"$_a"$'\n'* ]]; then _nd=$((_nd+1)); _defs+="$_a"$'\n'; fi
    check_arm "arm 11 charter copy $_c: readCharterShapes and extract_microformat_shapes read the same agent and returned" \
       "$([ "$_js" = "$_py" ] && echo 1 || echo 0)"
  done
  check_arm "arm 11 ...and the three agent answers hold two distinct definitions and one none" \
     "$([ "$_nd" = 2 ] && [ "$_nn" = 1 ] && echo 1 || echo 0)"
fi

# ---- arm 12: a harness agent's unit is the one unit id its label names ---------------------------
# TOOL-aOrientedCast-27 S4: a spec writer serving a group names several ids and so no one unit, and a
# label written before the unit's labels still yields its unit. Against extract_label_unit staged back
# to the first id a label holds, the group label reads as its first unit and the second row reds.
_a12=$("$PY" -B -c 'import sys
sys.path.insert(0, sys.argv[1])
import handoff
sys.stdout.buffer.write("\n".join(str(handoff.extract_label_unit(x)) for x in sys.argv[2:]).encode("utf-8"))' "$HERE" \
  "aOrientedCast · TOOL-aOrientedCast-27 · build" "aOrientedCast · TOOL-aOrientedCast-26 TOOL-aOrientedCast-27 · spec-write" \
  "aOrientedCast · diff-review round 1 · find:security" "unit:TOOL-tFix-1"); _a12=${_a12//$'\r'/}
_i=0
for _w in "TOOL-aOrientedCast-27|a builder's label names its one unit" "None|a spec writer's group label names no one unit" \
          "None|a review label names no unit" "TOOL-tFix-1|a label written before the new shape still yields its unit"; do
  _i=$((_i+1))
  check_arm "arm 12 ${_w#*|}" "$([ "$(printf '%s\n' "$_a12" | sed -n "${_i}p")" = "${_w%%|*}" ] && echo 1 || echo 0)"
done

# ---- arm 13: a --scaffold whose agent render refuses stops before the Skill ----------------------
# TOOL-dRedressedBar-6 S2: the adopter runs the agent render before it writes the Skill, so a refused
# render exits 1, names the refusal, and leaves the Skill unwritten. The break is arm 3's token idiom
# appended to a house overlay, which roles_lib.render_role refuses as R10 whatever the overlay held;
# the Skill is unlinked first, so a scaffold that went on to write it is seen.
build_fixture; check_arm "arm 13 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
rm -f "$FX/.claude/skills/build/SKILL.md"
printf '{{UNKNOWN_TOKEN}}\n' >> "$FX/$KREL/house/gov-builder.md"
out=$(run_adopter --scaffold); rc=$?
check_arm "arm 13 a refused agent render stops the scaffold, naming the refusal, and writes no Skill" \
   "$([ "$rc" = 1 ] \
      && [[ $out == *'roles: the agent render refused, so nothing more was written — fix what it named and re-run'* ]] \
      && [[ $out == *'{{UNKNOWN_TOKEN}}'* ]] && [ ! -e "$FX/.claude/skills/build/SKILL.md" ] && echo 1 || echo 0)"

# ---- arm 14: the Skill names each cited harness where the install holds it ----------------------
# TOOL-dRenderedAnchor-2 S12: the shape govkit leaves when it lands a kit under its id rather than
# its home. Each harness the template cites sits in a renamed directory behind one `rendered`
# receipt row whose `source` is its template under the cited home, and `render_skill` resolves each
# citation through the kit resolver before the plain `{{TOOL_ROOT}}` substitution. The population is
# HARNESS_PAIRS_READ's (TOOL-dRenderedAnchor-3 S5): the asserted count must equal the cited count and
# be at least 2, PINNED from the template's two harness citations at TOOL-dRenderedAnchor-3's base,
# and each path is matched with its backticks, the form the template cites it in. One line appended
# to the template cites the first pair with `x` added to its file name, which nothing holds, and it
# must keep its own plain path (S6). Red against an adopter with the citation pass taken out, whose
# Skill names each harness under the home the template cites; against a citation pattern narrowed
# so a harness drops out of it; and against held citations applied as unanchored substrings, which
# write the extended citation under the renamed directory.
build_fixture; check_arm "arm 14 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
A14P=$("$PY" -B -c "$HARNESS_PAIRS_READ" "$FX/$KREL"); A14P=${A14P//$'\r'/}; A14P=${A14P%$'\n'}
_p14=(); [ -z "$A14P" ] || mapfile -t _p14 <<< "$A14P"
A14=$("$PY" -B -c 'import json, pathlib, sys
fx, tool = pathlib.Path(sys.argv[1]), pathlib.PurePosixPath(sys.argv[2]).parent
rows, said = [], []
for pair in sys.argv[3:]:
    home, name = pair.split("/", 1)
    held = tool / "renamed" / name
    (fx / held).parent.mkdir(parents=True, exist_ok=True)
    (fx / held).write_text("// harness\n", encoding="utf-8")
    stem, ext = name.rsplit(".", 1)
    rows.append({"role": "rendered", "kit": "fixture", "path": held.as_posix(),
                 "source": (tool / home / ("%s.template.%s" % (stem, ext))).as_posix()})
    said += [held.as_posix(), (tool / home / name).as_posix()]
(fx / ".governance").mkdir(exist_ok=True)
(fx / ".governance" / "install.json").write_text(json.dumps({"files": rows}), encoding="utf-8")
sys.stdout.buffer.write("\n".join(said).encode("utf-8"))' "$FX" "$KREL" "${_p14[@]}")
printf '`{{TOOL_ROOT}}%sx`\n' "${_p14[0]-}" >> "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --scaffold); rc=$?
SK14="$FX/.claude/skills/build/SKILL.md"
mapfile -t _a14 <<< "${A14//$'\r'/}"
_ok=1; _i=0
while [ "$_i" -lt "${#_a14[@]}" ]; do
  [ -n "${_a14[$_i]}" ] || { _ok=0; break; }
  grep -qF -- "\`${_a14[$_i]}\`" "$SK14" || _ok=0
  grep -qF -- "\`${_a14[$((_i+1))]:-x}\`" "$SK14" && _ok=0
  _i=$((_i+2))
done
check_arm "arm 14 a --scaffold names each cited harness under the renamed directory, and none under its cited home" \
   "$([ "$rc" = 0 ] && [ "${#_p14[@]}" -ge 2 ] && [ "$((_i / 2))" = "${#_p14[@]}" ] && [ "$_ok" = 1 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '%s\n' "$out" | sed 's/^/    /'
check_arm "arm 14 ...and a citation extending the first by one character keeps its own plain path" \
   "$([ "$rc" = 0 ] && [ -n "${_a14[1]-}" ] && grep -qF -- "\`${_a14[1]}x\`" "$SK14" \
      && ! grep -qF -- "\`${_a14[0]}x\`" "$SK14" && echo 1 || echo 0)"
out=$(run_adopter --check); rc=$?
check_arm "arm 14 ...and --check over that install exits 0" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '%s\n' "$out" | sed 's/^/    /'

# ---- arm 15: a citation that is no harness never resolves above the tool root -------------------
# TOOL-dRenderedAnchor-3 S7, the closing review's M1: a citation that is
# no `workflow`-driver harness of the workflow table resolves from the kit directory, the call
# `derive_kit_paths` makes, so at a prefixed install, this arm's fixture, a file of its name at the
# repository root is never named. The arm finds each backticked span of the template holding
# `{{TOOL_ROOT}}` with its own pattern, skips each whose `<home>/<file>` HARNESS_PAIRS_READ lists,
# writes a decoy at `<repo>/<home>/<file>` for every other one, and the Skill must carry each such
# span under the plain prefix: at least 2, PINNED from the merge bar's and `unattended.sh`'s
# citations at TOOL-dRenderedAnchor-3's base. A receipt row then places the first one at
# `ci/<file>`, and the Skill must name it there, as `derive_kit_paths` does. Red against a library
# that resolves every citation with the tool root as `here`, whose Skill names each decoy.
build_fixture; _rc15=$?
A15P=$("$PY" -B -c "$HARNESS_PAIRS_READ" "$FX/$KREL"); A15P=${A15P//$'\r'/}
A15=$("$PY" -B -c 'import pathlib, re, sys
fx, krel, pairs = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3].split("\n")
tool = krel.rpartition("/")[0]
tool = tool + "/" if tool else ""
text = (fx / krel / "SKILL.template.md").read_text(encoding="utf-8")
said = []
for span in re.findall(r"`([^`\n]*)`", text):
    if "{{TOOL_ROOT}}" not in span:
        continue
    cite = re.split(r"[ `]", span.split("{{TOOL_ROOT}}", 1)[1], maxsplit=1)[0]
    home, _, name = cite.partition("/")
    plain = "`%s`" % span.replace("{{TOOL_ROOT}}", tool)
    if not home or not name or cite in pairs or any(plain == s[0] for s in said):
        continue
    (fx / home).mkdir(parents=True, exist_ok=True)
    (fx / home / name).write_text("# a decoy at the repository root\n", encoding="utf-8")
    placed = "`%s`" % span.replace("{{TOOL_ROOT}}" + cite, "ci/" + name).replace("{{TOOL_ROOT}}", tool)
    said.append((plain, placed, cite))
sys.stdout.buffer.write("".join("%s\t%s\t%s\n" % s for s in said).encode("utf-8"))' "$FX" "$KREL" "$A15P")
_s15=(); [ -z "$A15" ] || mapfile -t _s15 <<< "${A15//$'\r'/}"
out=$(run_adopter --scaffold); rc=$?
SK15="$FX/.claude/skills/build/SKILL.md"
_ok=1; _k=0
for _l in "${_s15[@]}"; do
  [ -n "$_l" ] || continue
  _k=$((_k+1)); grep -qF -- "${_l%%$'\t'*}" "$SK15" || _ok=0
done
check_arm "arm 15 a --scaffold with a decoy at the repository root for each citation that is no harness names each under the plain prefix" \
   "$([ "$_rc15" = 0 ] && [ "$rc" = 0 ] && [ "$_k" -ge 2 ] && [ "$_ok" = 1 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '%s\n' "$out" | sed 's/^/    /'
out=$(run_adopter --check); rc=$?
check_arm "arm 15 ...and --check over that install exits 0" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '%s\n' "$out" | sed 's/^/    /'
IFS=$'\t' read -r _w15 _c15 _q15 <<< "${_s15[0]-}"
mkdir -p "$FX/ci" "$FX/.governance" && printf '# placed by the receipt\n' > "$FX/ci/${_q15#*/}"
printf '{"files": [{"kit": "fixture", "source": "%s", "path": "ci/%s"}]}\n' "$_q15" "${_q15#*/}" > "$FX/.governance/install.json"
out=$(run_adopter --scaffold); rc=$?
check_arm "arm 15 ...and a receipt row placing the first of them at ci/ names it there" \
   "$([ "$rc" = 0 ] && [ -n "${_c15-}" ] && grep -qF -- "$_c15" "$SK15" && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '%s\n' "$out" | sed 's/^/    /'

# ---- arm 16: a harness a sibling of the repository holds is listed nowhere at a root install -----
# TOOL-dRenderedAnchor-3 S8, the closing review's L6: with the kit at `<repo>/roles` the tool root is
# the repository, so a harness citation's second probe is `<repo>/../<home>/<file>`. A directory
# beside the repository holding each pair HARNESS_PAIRS_READ lists makes the path's `relative_to`
# raise, and `resolve_cited_paths` must list nothing rather than fail the pass, so `--scaffold` exits
# 0 with each citation plain. Red against a library whose `except` names `LookupError` alone: the
# call raises, and the adopter exits 2 naming the citation pass.
build_fixture roles "$TMP_ROOT/a16/repo"; _rc16=$?
A16P=$("$PY" -B -c "$HARNESS_PAIRS_READ" "$FX/roles"); A16P=${A16P//$'\r'/}; A16P=${A16P%$'\n'}
_p16=(); [ -z "$A16P" ] || mapfile -t _p16 <<< "$A16P"
for _q in "${_p16[@]}"; do mkdir -p "$TMP_ROOT/a16/${_q%/*}" && printf '// harness\n' > "$TMP_ROOT/a16/$_q"; done
out=$("$PY" -B -c 'import pathlib, sys
sys.path.insert(0, sys.argv[1])
import roles_lib
kit = pathlib.Path(sys.argv[1]).absolute()
text = (kit / "SKILL.template.md").read_text(encoding="utf-8")
for cite, rel in roles_lib.resolve_cited_paths(text, kit, kit.parent, roles_lib.load_workflows(kit)):
    print(cite, rel)' "$FX/roles" 2>&1); rc=$?
check_arm "arm 16 at a root install, resolve_cited_paths lists no harness a sibling of the repository holds" \
   "$([ "$_rc16" = 0 ] && [ "${#_p16[@]}" -ge 2 ] && [ "$rc" = 0 ] && [ -z "$out" ] && echo 1 || echo 0)"
[ "$rc" = 0 ] && [ -z "$out" ] || printf '%s\n' "$out" | sed 's/^/    /'
out=$(run_adopter --scaffold); rc=$?
_ok=1; for _q in "${_p16[@]}"; do grep -qF -- "\`$_q\`" "$FX/.claude/skills/build/SKILL.md" || _ok=0; done
check_arm "arm 16 ...and --scaffold exits 0 naming each such harness by its plain citation" \
   "$([ "$rc" = 0 ] && [ "${#_p16[@]}" -ge 2 ] && [ "$_ok" = 1 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '%s\n' "$out" | sed 's/^/    /'

# ---- arm 17: a harness held only above the tool root is named where the role index lists it ---
# TOOL-dRenderedAnchor-4 S1, the closing review's round-3 M1: the citation pass resolves a
# `workflow`-driver harness with the tool root as `here` and every other citation from the kit
# directory, and the two values of `here` part on one layout only: a harness held only in the
# directory above the tool root, with no receipt row. The arm builds that layout. Each pair
# HARNESS_PAIRS_READ lists is written there, with nothing under `<tool root>/<home>/` and no receipt.
# After `--scaffold` the Skill must name each pair there, backticked, never under the tool root, and
# the `harnesses` list of the role index must hold the same path. The expected path is built from
# the pair and the kit path, never read from either output the arm grades. The fixture's
# preconditions are in the assertion: a kit path of two or more segments, nothing under the tool
# root's home, no receipt, and at least 2 pairs, PINNED from the template's two harness citations,
# so a fixture that drifts toward a layout both values of `here` reach reds the arm. Red against
# `roles_lib.py` line 626 staged as `here = kit`, the C2 break TOOL-dRenderedAnchor-3's spec
# rejected, whose Skill names each pair under the tool root while the role index does not move.
build_fixture; _rc17=$?
A17P=$("$PY" -B -c "$HARNESS_PAIRS_READ" "$FX/$KREL"); A17P=${A17P//$'\r'/}; A17P=${A17P%$'\n'}
_p17=(); [ -z "$A17P" ] || mapfile -t _p17 <<< "$A17P"
_t17=${KREL%/*}; _u17=""; [[ $_t17 == */* ]] && _u17=${_t17%/*}/
_ok=1
for _q in "${_p17[@]}"; do
  [ -e "$FX/$_t17/${_q%%/*}" ] && _ok=0
  mkdir -p "$FX/$_u17${_q%/*}" && printf '// harness\n' > "$FX/$_u17$_q"
done
out=$(run_adopter --scaffold); rc=$?
SK17="$FX/.claude/skills/build/SKILL.md"
IX17=$("$PY" -B -c 'import json, sys
with open(sys.argv[1], encoding="utf-8") as fh:
    held = json.load(fh).get("harnesses") or []
sys.stdout.buffer.write("".join(h + "\n" for h in held if isinstance(h, str)).encode("utf-8"))' \
   "$FX/.claude/roles.json" 2>/dev/null); IX17=${IX17//$'\r'/}
for _q in "${_p17[@]}"; do
  grep -qF -- "\`$_u17$_q\`" "$SK17" || _ok=0
  grep -qF -- "\`$_t17/$_q\`" "$SK17" && _ok=0
  grep -qxF -- "$_u17$_q" <<< "$IX17" || _ok=0
done
_v17=$([[ $KREL == */* ]] && [ "$_rc17" = 0 ] && [ "$rc" = 0 ] && [ "${#_p17[@]}" -ge 2 ] \
   && [ ! -e "$FX/.governance/install.json" ] && [ "$_ok" = 1 ] && echo 1 || echo 0)
check_arm "arm 17 a harness held only above the tool root is named there by the Skill and by roles.json" "$_v17"
[ "$_v17" = 1 ] || printf '%s\n' "$out" | sed 's/^/    /'

[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL the suite executed $n assertions, under its floor of $FLOOR_ASSERTIONS — a block of arms was skipped"; fail=$((fail+1)); }
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ] || { echo "FAIL ($fail of $n)"; exit 1; }
