#!/usr/bin/env bash
# adopt-roles.test.sh — the roles adopter's self-test (TOOL-aOrientedCast-8 S12).
#
#   bash <prefix>/roles/adopt-roles.test.sh
#   ROLES_ADOPTER=<a copy> bash <prefix>/roles/adopt-roles.test.sh   # grade a copy, for a red observation
#
# Each arm builds its own fixture: a fresh git repository holding a copy of this kit, with the adopter
# under test as its `adopt-roles.sh`, a copy of the loop kit's definition and reader beside it, the
# governing doc and memory root this repository's conf names,
# scaffolded once. Then it stages ONE break into the fixture and asserts the adopter's refusal by exit
# code AND by the text naming it, because an exit code alone is shared by every refusal the adopter
# has: a copy with the stage binding staged out still exits 1 on the agent compare.
#
# The arms: a loop row whose order disagrees with its stage heading; a workflow of the loop
# definition no heading names; a token surviving the substitution; a byte appended to a rendered agent type; an unknown
# argument; the renderer's task part sent to the hooks kit's spawn guard (arm 6, which SKIPs out loud
# without that kit or node); an `export` conf line with a trailing comment (arm 7); the roster verb's
# one line per role and its refusal of a line past 200 characters (arm 8); the agents verb's two
# lines for a direct spawn, its tokens counted once per message id, each added to the build's agent
# ledger exactly once across two runs, a run without `--write` writing nothing, a harness run's two
# agent lines and one returned line, a prompt opening with a blank line still matching, and a
# transcript stripped of its effort printing `unknown` under the plain policy (arm 9);
# the stand-in render's refusal, R15 both ways and over eight bad rows, R13, R14, R6 over a loop row
# with no step, a misspelt one and a `stage` key in the catalogue, and R0 (arm 10);
# the roles kit's reading of a prompt's marker line and of the charter's micro-format fence
# against the hooks kit's own (arm 11, which SKIPs out loud as arm 6 does); a `--scaffold` whose
# agent render refuses, which exits 1 naming the refusal and writes no Skill (arm 13); the cited
# harnesses moved into a renamed directory behind `rendered` receipt rows, which the Skill then names
# there, and a citation extending a held one, which keeps its own plain path (arm 14); a decoy at the
# repository root for each citation that is no harness, which the Skill never names, and a receipt
# row placing the first of them, which it does (arm 15); a root install whose repository has a
# sibling directory holding each cited harness, which the citation pass lists nowhere (arm 16);
# a harness held only in the directory above the tool root with no receipt, which the Skill and the
# role index both name there (arm 17); and the handoff verbs `stage-efforts` and `role-efforts` over
# a policy that gains one profile, with no model, a model id no profile matches, one that profile
# matches, an empty or whitespace-only one, and one a second profile also matches (arm 19); one list
# of model ids read by `resolve_profile` and by the spawn guard's `resolveModelProfile` over the index
# rendered from arm 19's policy (arm 20, which SKIPs out loud as arm 6 does); and a profile level
# edited with no re-render, which the adopter's check names as a drifted index (arm 21); and the spec writer's handoff carrying the brief's `## The prompt`
# as its `brief:prompt` block, an empty prompt refusing by name (arm 22); and a role reading
# `upstream:rows?` handed the `--upstream` rows file and the row contract, the key named not supplied
# without one, and R3 refusing a bare `upstream:rows` and an `upstream:` key outside the vocabulary
# (arm 23); and the agents verb's
# session record, cold, warm, read, resumed after an append and a torn line, and keyed off by a
# transcript edit, a foreign key or an unwritable folder (arm 25); and R3 reading each `reads` entry
# in either spelling, a misspelt `field.` tag named and a bare `field.card.reuse` refused (arm 26); and the
# policy keys `roles.effort.<role>` and `roles.model.<role>.<harness>` read before the house file through a
# copied policy kit, a role's `gates` field beating its house row, the reserved `default` slot, and an
# absent house file falling to the declared effort (arm 29); and the stage rows of `workflows.toml` graded as
# R9, a two-stage mixed-role entry clean, a zero fan, an unknown effort and an unknown row kind refused with
# and without the loop kit's `kinds` verb, a cap above a committed `runtime.agents-in-flight` refused, and
# the rows' declared levels read with no house file and no key (arm 30); and the workflow shapes graded as R9, a
# kind's cap above a committed limit, an experiment table naming both, neither or a stray reruns key, a role
# outside its stage's kind, the role index's `shapes`, and an orientation tag naming no unit, resolved and
# unarmed (arm 31); and the work order's `item=` written by `--item`, a malformed tag refused, and R16 over
# a return's `**Answers:**` line, a work order planted after the seed with no `item=` or no marker, and no
# legacy home (arm 33); and the spec writer's handoff handing its spec as content under a `record:` fact line,
# and `handoff.py facts` cutting it to the same key (arm 34); and the work order rendered per item, its five blocks,
# its allowance by class, a wrong role, no allowance, an unrouted one, an undeclared item, no loop kit and a missing
# block refused (arm 35). Every arm is a self-contained block below the prologue, so a
# slice of the prologue and one block runs that arm alone; arm 20 reads arm 19's fixture, and arm 25
# arm 9's writer and lines.
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
# refusal, and R10 only as the trigger. Arm 19 does not check any profile the policy file seeds, nor
# the resolver's order inside a profile. Arm 9 does not check an agent whose model a profile
# matches, since the verb reads no profile.
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
# +1 for arm 18 (TOOL-dFoldedAudit-15).
# +4 for arm 19 (TOOL-aProfiledEffort-2).
# +1 for arm 9 and +1 for arm 19 (TOOL-aProfiledEffort-4).
# +2 for arm 21 (TOOL-aGuardedEffort-1); arm 20 and arm 6's added payload are out of the floor.
# +0 for arm 6's harness calls and rendered tables (TOOL-aGuardedEffort-2): on its SKIP path, out of the floor.
# +2 for arm 22 (TOOL-dPavedRoad-3).
# +1 for arm 10's planted `stage` key (TOOL-dDeclaredLoop-1).
# +4 for arm 23 (TOOL-dDeclaredLoop-29).
# +1 for arm 24 (TOOL-dDeclaredLoop-56).
# +8 for arm 25 (TOOL-aTrimmedWait-7).
# merged at dDeclaredLoop's reconcile of origin/main 4e6ac5f7c: 61 shared, +6 this branch's, +8 main's = 75.
# +4 for arm 26 (TOOL-dBoundRoles-14).
# +6 for arm 27 (TOOL-dBoundRoles-2).
# +3 for arm 28 (TOOL-dBoundRoles-1).
# +6 for arm 29 (TOOL-dBoundRoles-21).
# +8 for arm 30 (TOOL-dBoundRoles-22).
# +10 for arm 31 (TOOL-dBoundRoles-16).
# +8 for arm 32 (TOOL-dBoundRoles-15).
# +9 for arm 33 (TOOL-dBoundRoles-17).
# +2 for arm 34 (TOOL-dBoundRoles-13).
# +9 for arm 35 (TOOL-dBoundRoles-3).
# +6 for arm 36 (TOOL-dBoundRoles-38).
# +8 for arm 37 (TOOL-dBoundRoles-45).
# +4 for arm 38 (TOOL-dBoundRoles-48).
# +5 for arm 39 (TOOL-dBoundRoles-24).
# +3 for arm 40 (TOOL-dBoundRoles-41).
# +4 for arm 41 (TOOL-dBoundRoles-11).
# +2 for arm 42 (TOOL-dBoundRoles-47).
FLOOR_ASSERTIONS=172
n=0; fail=0
check_arm() { n=$((n+1)); if [ "$2" = 1 ]; then echo "ok   $1"; else echo "FAIL $1"; fail=$((fail+1)); fi; }
# THE LOOP KIT (TOOL-dDeclaredLoop-1): the adopter and the catalogue checker read each workflow's order
# from the loop definition, so every fixture holds a copy of the loop kit beside its roles kit, at the
# home `loop`, where the library's resolver probes. The source is the loop kit beside this one.
LOOP_SRC="$HERE/../loop"
[ -f "$LOOP_SRC/loop_lib.py" ] && [ -f "$LOOP_SRC/loop.toml" ] || { echo "adopt-roles.test: no loop kit beside this one at $LOOP_SRC, so no fixture can place its workflows"; exit 2; }
LAYERS_SRC="$HERE/../playbook"
[ -f "$LAYERS_SRC/layers.toml" ] || { echo "adopt-roles.test: no layer register beside this kit at $LAYERS_SRC, so no fixture can join a role's layer"; exit 2; }
FX=""; FXK="$KREL"; FXL=""; FXP=""
build_fixture() { # [kit path] [fixture dir] -> $FX: a repo holding this kit at the kit path, $KREL
  # unless given, with $ADOPTER as its adopter, and the loop kit beside it at $FXL, scaffolded; rc of
  # the scaffold. The fixture directory is $TMP_ROOT/fx<n> unless given, and run_adopter reads the kit
  # path the last call used.
  FXK=${1:-$KREL}; FX=${2:-$TMP_ROOT/fx$n}
  FXL=loop; [[ $FXK == */* ]] && FXL=${FXK%/*}/loop
  # TOOL-dBoundRoles-1 §8 F11: the layer register R2 joins each role's `layer` to, at the home `playbook`
  # beside the roles and loop kits, where the library's resolver probes.
  FXP=playbook; [[ $FXK == */* ]] && FXP=${FXK%/*}/playbook
  _chd=.; [[ $CH == */* ]] && _chd=${CH%/*}; mkdir -p "$FX/$FXK" "$FX/$FXL" "$FX/$FXP" "$FX/$_chd" || return 2
  git init -q "$FX" || return 2
  cp -R "$HERE"/. "$FX/$FXK"/ && cp "$ADOPTER" "$FX/$FXK/adopt-roles.sh" || return 2
  cp "$LOOP_SRC/loop_lib.py" "$LOOP_SRC/loop.toml" "$FX/$FXL"/ || return 2
  cp "$LAYERS_SRC/layers.toml" "$FX/$FXP"/ || return 2
  # TOOL-dBoundRoles-2 §4 Migration: each script a shipped role's `never` entry names, copied from this
  # repository's tool root to the same path under the fixture's, so the fixture holds the enforcers a
  # default install holds and R13 grades it as it grades one. The list is read from the role files
  # through the kit's own library, never typed here.
  _ftr=$FX; [[ $FXK == */* ]] && _ftr=$FX/${FXK%/*}
  _enf=$("$PY" -B -c 'import pathlib, sys
kit = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(kit))
import roles_lib as lib
held = set()
for slot, role in lib.load_roles(kit).items():
    for _limit, enforcer in lib.parse_never_entries(role["keys"].get("never", "")):
        first = (enforcer.split() or [""])[0]
        path = lib.resolve_enforcer_path(kit.parent, first) if lib.ENFORCER_SCRIPT_RE.match(first) else None
        if path is not None:
            held.add(path.relative_to(kit.parent).as_posix())
print("\n".join(sorted(held)))' "$HERE") || return 2
  local _ea=() _e; mapfile -t _ea <<< "$_enf"
  for _e in "${_ea[@]}"; do
    _e=${_e%$'\r'}; [ -n "$_e" ] || continue
    mkdir -p "$(dirname "$_ftr/$_e")" && cp "$HERE/../$_e" "$_ftr/$_e" || return 2
  done
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

# ---- arm 1: a loop row whose order disagrees with its stage heading --------------------------------
build_fixture; check_arm "arm 1 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
# TOOL-dDeclaredLoop-1: the order is the loop definition's, so the break is planted THERE, on the
# fixture's `reuse` row. An adopter still reading the roles catalogue never compares it.
awk '/^name = "reuse"$/{b=1} b && /^order = /{print "order = 9"; b=0; next} {print}' "$LOOP_SRC/loop.toml" > "$FX/$FXL/loop.toml"
out=$(run_adopter --check); rc=$?
check_arm "arm 1 a loop row whose order disagrees with its heading refuses, naming the entry's own order" \
   "$([ "$rc" = 1 ] && [[ $out == *'says stage 2 but the order of the entry reuse is 9 in the loop definition'* ]] && echo 1 || echo 0)"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

# ---- arm 2: a workflow of the loop definition no heading names ----------------------------------------------
build_fixture; check_arm "arm 2 the fixture scaffolds and checks clean" "$([ $? = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
sed -i '/^## Stage 2 — reuse$/d' "$FX/$KREL/SKILL.template.md"
out=$(run_adopter --check); rc=$?
check_arm "arm 2 an order-2 workflow no heading names refuses, naming it and the loop definition" \
   "$([ "$rc" = 1 ] && [[ $out == *'the entry reuse (order 2) of the loop definition is named by no ## Stage heading'* ]] && echo 1 || echo 0)"

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
  # TOOL-aGuardedEffort-1: the rendered index carries `effort`, so the hook's rule 8 grades this
  # fixture's spawns. One profile, `tfam`, is appended and the index re-rendered: it gives every role
  # `max`, and the third payload below names a transcript whose model it matches.
  printf '%s\n' '' '[effort.profiles.tfam]' 'match = ["tfam"]' 'default = "max"' >> "$FX/$KREL/house/policy.toml"
  (cd "$FX" && bash "$FXK/adopt-roles.sh" --scaffold >/dev/null 2>&1)
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
  # TOOL-dGroundRules-10: the hook's rule 7 refuses a spawn in a checkout whose settings do not hold
  # the landed agent limit, and this fixture carries no policy. The agreement this arm holds is rule
  # 6's, so it runs a copy of the hook with no policy kit beside it, where rule 7 adds no rule.
  HKC="$TMP_ROOT/hooks-copy/hooks"; mkdir -p "$HKC" && cp "$HK/agent-cap.js" "$HK/scratch-guard.js" "$HKC/"
  HK=$HKC
  # TOOL-aGuardedEffort-1: the payload names no transcript, so rule 8 reads no model and the admitted
  # spawn's stderr is exactly its not-checked line. Against a main() with rule 8 cut out, it is empty.
  A6_NOTE="agent-cap: rule 8 did not check this Agent call's effort level — the payload carries no transcript_path"
  (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR -u CLAUDE_CODE_EFFORT_LEVEL node "$HK/agent-cap.js" < "$TMP_ROOT/a6.json" >/dev/null 2>"$TMP_ROOT/a6.hook"); hrc=$?
  _a6ok=0; [ "$rc" = 0 ] && [ "$hrc" = 0 ] && [ "$(tr -d '\r' < "$TMP_ROOT/a6.hook")" = "$A6_NOTE" ] && _a6ok=1
  check_arm "arm 6 the renderer's task part, named as it printed, is admitted by the spawn guard, saying only that rule 8 read no model" "$_a6ok"
  [ "$_a6ok" = 1 ] || sed 's/^/    /' "$TMP_ROOT/a6.err" "$TMP_ROOT/a6.hook"
  # ...and the same spawn on a transcript whose model the appended profile matches, carrying no
  # `effort`, is refused over the RENDERED index: the hook is held to the renderer's shape.
  TRN=$(cd "$TMP_ROOT" && { pwd -W 2>/dev/null || pwd; })
  printf '%s\n' '{"type":"assistant","message":{"model":"vendor-tfam-9"}}' > "$TMP_ROOT/a6.tfam.jsonl"
  "$PY" -c 'import json, sys
with open(sys.argv[1], encoding="utf-8") as fh:
    d = json.load(fh)
d["transcript_path"] = sys.argv[2]
with open(sys.argv[3], "w", encoding="utf-8") as fh:
    json.dump(d, fh)' "$TMP_ROOT/a6.json" "$TRN/a6.tfam.jsonl" "$TMP_ROOT/a6e.json"
  (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR -u CLAUDE_CODE_EFFORT_LEVEL node "$HK/agent-cap.js" < "$TMP_ROOT/a6e.json" >/dev/null 2>"$TMP_ROOT/a6e.hook"); hrc=$?
  _a6e=0; [ "$hrc" = 2 ] && grep -qF 'BLOCKED by agent-cap: rule 8' "$TMP_ROOT/a6e.hook" \
     && grep -qF 'the tfam profile gives it max on the model "vendor-tfam-9"' "$TMP_ROOT/a6e.hook" && _a6e=1
  check_arm "arm 6 ...and on a profiled model's transcript with no effort it is refused over the rendered index, naming the profile's level" "$_a6e"
  [ "$_a6e" = 1 ] || sed 's/^/    /' "$TMP_ROOT/a6e.hook"
  (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR node "$HK/agent-cap.js" < "$TMP_ROOT/a6s.json" >/dev/null 2>"$TMP_ROOT/a6s.hook"); hrc=$?
  check_arm "arm 6 ...and named by the role's slot it is refused, naming the rendered name" \
     "$([ "$hrc" = 2 ] && [ "$(<"$TMP_ROOT/a6.name")" != null ] && grep -qF -- "$(<"$TMP_ROOT/a6.name")" "$TMP_ROOT/a6s.hook" && echo 1 || echo 0)"
  # TOOL-aGuardedEffort-2 S6: the `Workflow` half of rule 8 over the RENDERED index. The harness is
  # the one the index's `effort.harnesses` maps to `build`, spelled as the index spells it, and its
  # file is created where the fixture holds none, so the hook resolves it; `roles` is what
  # `harness-args` prints and `efforts` what `stage-efforts build` prints. Against a renderer keying
  # `effort.harnesses` by workflow name, the first payload is refused as no declared harness.
  printf '%s\n' '{"type":"assistant","message":{"model":"vendor-other-9"}}' > "$TMP_ROOT/a6.other.jsonl"
  "$PY" -B -c 'import json, pathlib, subprocess, sys
fx, kit, out, tfam, other = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
def verb(*a):
    return json.loads(subprocess.run([sys.executable, "-B", kit + "/handoff.py", *a], cwd=str(fx),
                                     capture_output=True, check=True).stdout.decode("utf-8"))
with open(fx / ".claude" / "roles.json", encoding="utf-8") as fh:
    runs = json.load(fh)["effort"]["harnesses"]
harness = next(h for h, names in runs.items() if "build" in names)
(fx / harness).parent.mkdir(parents=True, exist_ok=True)
(fx / harness).touch()
roles = verb("harness-args", pathlib.PurePosixPath(harness).stem)
for name, tp, efforts in (("w1", tfam, verb("stage-efforts", "build", "--model", "vendor-tfam-9")),
                          ("w2", tfam, None), ("w3", other, verb("stage-efforts", "build"))):
    args = {"roles": roles} if efforts is None else {"roles": roles, "efforts": efforts}
    with open("%s.%s.json" % (out, name), "w", encoding="utf-8") as fh:
        json.dump({"tool_name": "Workflow", "cwd": fx.as_posix(), "transcript_path": tp,
                   "tool_input": {"scriptPath": (fx / harness).as_posix(), "args": args}}, fh)
sys.stdout.buffer.write(("build: stage %s would run at " % sorted(roles)[0]).encode("utf-8"))' \
    "$FXN" "$KREL" "$TMP_ROOT/a6" "$TRN/a6.tfam.jsonl" "$TRN/a6.other.jsonl" > "$TMP_ROOT/a6.stage" 2>"$TMP_ROOT/a6w.err"; _a6w=$?
  _a6h=""
  for _w in w1 w2 w3; do
    (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR -u CLAUDE_CODE_EFFORT_LEVEL node "$HK/agent-cap.js" < "$TMP_ROOT/a6.$_w.json" >/dev/null 2>"$TMP_ROOT/a6.$_w.hook"); _a6h="$_a6h$?"
  done
  _a6ok=0; [ "$_a6w" = 0 ] && [ "$_a6h" = 020 ] && [ -s "$TMP_ROOT/a6.stage" ] && grep -qF -- "$(<"$TMP_ROOT/a6.stage")" "$TMP_ROOT/a6.w2.hook" && _a6ok=1
  check_arm "arm 6 a harness call over the rendered index is admitted at the profile's levels, refused with none naming the stage, and admitted at the default levels on an unmatched model" "$_a6ok"
  [ "$_a6ok" = 1 ] || { echo "    exits: $_a6h"; sed 's/^/    /' "$TMP_ROOT/a6w.err" "$TMP_ROOT"/a6.w?.hook; }
  # ...and the rendered tables against the verbs and the agent files, for every workflow whose entry
  # in the fixture kit's `workflows.toml` holds `[[workflow.stages]]` rows (TOOL-dBoundRoles-22), read
  # here by `tomllib` and never through the kit. Against a renderer resolving a profile's `stages` with no model, the tfam
  # table is the default one and the second comparison fails. No staged workflow fails the arm.
  out=$("$PY" -B -c 'import json, pathlib, subprocess, sys, tomllib
fx, kit = pathlib.Path(sys.argv[1]), sys.argv[2]
def verb(*a):
    return json.loads(subprocess.run([sys.executable, "-B", kit + "/handoff.py", *a], cwd=str(fx),
                                     capture_output=True, check=True).stdout.decode("utf-8"))
with open(fx / kit / "workflows.toml", "rb") as fh:
    staged = [w for w in tomllib.load(fh)["workflow"] if isinstance(w.get("stages"), list) and w["stages"]]
with open(fx / ".claude" / "roles.json", encoding="utf-8") as fh:
    e = json.load(fh)["effort"]
bad = [] if staged else ["no workflow of workflows.toml holds a stage row"]
def level(slot):
    lines = (fx / ".claude" / "agents" / (slot + ".md")).read_text(encoding="utf-8").split("\n")
    return next((ln[len("effort: "):] for ln in lines if ln.startswith("effort: ")), None)
for w in staged:
    name = w["name"]
    if e["default"]["stages"].get(name) != verb("stage-efforts", name):
        bad.append("default.stages.%s is not what stage-efforts prints" % name)
    if e["profiles"]["tfam"]["stages"].get(name) != verb("stage-efforts", name, "--model", "vendor-tfam-9"):
        bad.append("profiles.tfam.stages.%s is not what stage-efforts --model vendor-tfam-9 prints" % name)
    for key, slot in ((r["key"], r["role"]) for r in w["stages"]):
        want = level(slot)
        if want is None or e["unset"].get(name, {}).get(key) != want or e["default"]["roles"].get(slot) != want:
            bad.append("unset.%s.%s or default.roles.%s is not the effort line of %s.md, %r" % (name, key, slot, slot, want))
print("\n".join(bad))
sys.exit(1 if bad else 0)' "$FXN" "$KREL" 2>&1); rc=$?
  check_arm "arm 6 the rendered effort tables are what stage-efforts prints, with and without the profiled model, and each unset level its slot's agent file's" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
  [ "$rc" = 0 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"
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
# TOOL-aProfiledEffort-4 S1: an effort no transcript record carries prints `unknown`. It runs last
# because it rewrites the fixture's transcript. The fixture's policy is the kit's own, so this is
# the plain case and no profile is read. The last clause keeps the assertion from passing by finding
# nothing: the rendered agent type does carry a level, and the verb did not print it.
"$PY" -B -c 'import json, sys
rows = [json.loads(ln) for ln in open(sys.argv[1], encoding="utf-8") if ln.strip()]
for r in rows:
    r.pop("effort", None)
open(sys.argv[1], "w", encoding="utf-8", newline="\n").write("".join(json.dumps(r) + "\n" for r in rows))' "${A9S%.jsonl}/subagents/agent-a0000000000000001.jsonl"
out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" agents --handoff "$A9H" --session "$A9S" 2>"$TMP_ROOT/a9u.err"); rc=$?
check_arm "arm 9 an effort no transcript record carries prints unknown, never the agent type's own level" \
   "$([ "$rc" = 0 ] && [ "${out//$'\r'/}" = "${A9L1/effort medium/effort unknown}"$'\n'"$A9L2" ] \
      && grep -q 'no record answers level' "$TMP_ROOT/a9u.err" && grep -q '^effort: ' "$FX/.claude/agents/gov-builder.md" && echo 1 || echo 0)"

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
# PLAY-dOrderedCharter-21 S1, moved by TOOL-dDeclaredLoop-1: a workflow's step is the loop definition's,
# so the build row's step is dropped and then misspelt in the fixture's LOOP definition, each one R6
# line naming that definition and the row; and a `stage` key planted in the catalogue is an unknown key.
awk '/^name = "build"$/{b=1} b && /^step = /{b=0; next} {print}' "$LOOP_SRC/loop.toml" > "$FX/$FXL/loop.toml"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a loop row without step is one R6 line, naming the loop definition and the row" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R6 — ' "$A10R")" = 1 ] && grep ': R6 — ' "$A10R" | grep -F 'the loop definition does not read' | grep -qF '(build) carries no step' && echo 1 || echo 0)"
awk '/^name = "build"$/{b=1} b && /^step = /{print "step = \"step.buld\""; b=0; next} {print}' "$LOOP_SRC/loop.toml" > "$FX/$FXL/loop.toml"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a step that is no declared step tag is one R6 line, naming the loop definition, the row and the value" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R6 — ' "$A10R")" = 1 ] && grep ': R6 — ' "$A10R" | grep -F 'the loop definition does not read' | grep -F '(build)' | grep -qF "step 'step.buld'" && echo 1 || echo 0)"
cp "$LOOP_SRC/loop.toml" "$FX/$FXL/loop.toml"
cp "$FX/$KREL/workflows.toml" "$TMP_ROOT/a10.workflows"
awk '{print} /^name = "spec-write"$/{print "stage = 3"}' "$TMP_ROOT/a10.workflows" > "$FX/$KREL/workflows.toml"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A10R" 2>&1); rc=$?
check_arm "arm 10 a stage key in the catalogue is one R6 line, naming the row and the unknown key" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R6 — ' "$A10R")" = 1 ] && grep ': R6 — ' "$A10R" | grep -qF "(spec-write) has an unknown key 'stage'" && echo 1 || echo 0)"
cp "$TMP_ROOT/a10.workflows" "$FX/$KREL/workflows.toml"
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
  # A copy of the hook with no policy kit beside it, as arm 6 runs, so rule 7 adds no rule here.
  HKAC="$TMP_ROOT/a11/hooks-copy/hooks"; mkdir -p "$HKAC" && cp "$HKA/agent-cap.js" "$HKA/scratch-guard.js" "$HKAC/"
  HKA=$HKAC
  _seen=""
  for _v in v1 v2 v3 v4 v5; do
    (cd "$TMP_ROOT" && env -u CLAUDE_PROJECT_DIR node "$HKA/agent-cap.js" < "$TMP_ROOT/a11/$_v.json" >/dev/null 2>"$TMP_ROOT/a11/$_v.hook"); hrc=$?
    # The exit code alone: an admitted spawn's stderr holds rule 8's not-checked line, since the
    # rendered index carries `effort` and the payload names no transcript (TOOL-aGuardedEffort-1).
    _js=refuse; [ "$hrc" = 0 ] && _js=admit
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
[ "$rc" = 0 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"
check_arm "arm 14 ...and a citation extending the first by one character keeps its own plain path" \
   "$([ "$rc" = 0 ] && [ -n "${_a14[1]-}" ] && grep -qF -- "\`${_a14[1]}x\`" "$SK14" \
      && ! grep -qF -- "\`${_a14[0]}x\`" "$SK14" && echo 1 || echo 0)"
out=$(run_adopter --check); rc=$?
check_arm "arm 14 ...and --check over that install exits 0" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"

# ---- arm 15: a citation that is no harness never resolves above the tool root -------------------
# TOOL-dRenderedAnchor-3 S7, the closing review's M1: a citation that is not
# a `workflow`-driver harness of the workflow table resolves from the kit directory, the call
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
[ "$rc" = 0 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"
out=$(run_adopter --check); rc=$?
check_arm "arm 15 ...and --check over that install exits 0" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"
IFS=$'\t' read -r _w15 _c15 _q15 <<< "${_s15[0]-}"
mkdir -p "$FX/ci" "$FX/.governance" && printf '# placed by the receipt\n' > "$FX/ci/${_q15#*/}"
printf '{"files": [{"kit": "fixture", "source": "%s", "path": "ci/%s"}]}\n' "$_q15" "${_q15#*/}" > "$FX/.governance/install.json"
out=$(run_adopter --scaffold); rc=$?
check_arm "arm 15 ...and a receipt row placing the first of them at ci/ names it there" \
   "$([ "$rc" = 0 ] && [ -n "${_c15-}" ] && grep -qF -- "$_c15" "$SK15" && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"

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
[ "$rc" = 0 ] && [ -z "$out" ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"
out=$(run_adopter --scaffold); rc=$?
_ok=1; for _q in "${_p16[@]}"; do grep -qF -- "\`$_q\`" "$FX/.claude/skills/build/SKILL.md" || _ok=0; done
check_arm "arm 16 ...and --scaffold exits 0 naming each such harness by its plain citation" \
   "$([ "$rc" = 0 ] && [ "${#_p16[@]}" -ge 2 ] && [ "$_ok" = 1 ] && echo 1 || echo 0)"
[ "$rc" = 0 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"

# ---- arm 17: a harness held only above the tool root is named where the role index lists it ---
# TOOL-dRenderedAnchor-4 S1, the closing review's round-3 M1: the citation pass resolves a
# `workflow`-driver harness with the tool root as `here` and every other citation from the kit
# directory. With no receipt row the two values of `here` part on two layouts, which the probes of
# `resolve_kit_dir` give (TOOL-dRenderedAnchor-5, the closing review's round-4 L1): a harness held
# at `<kit>/<home>/`, which only the kit directory reaches and probes first, or one held only in the
# directory above the tool root, which only the tool root reaches. The arm builds the second and
# leaves the first unbuilt. Each pair HARNESS_PAIRS_READ lists is written there, with nothing under
# `<tool root>/<home>/` and no receipt.
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
[ "$_v17" = 1 ] || printf '    %s\n' "${out//$'\n'/$'\n'    }"

# ---- arm 18 (TOOL-dFoldedAudit-15 AC19): the render's ATTENDED bullet names every driver verb an attended
# ---- run uses. The failing case, observed at the close and not by the pass that wrote this: the old
# ---- sentence restored to the template and the render.
_v18=$(! grep -qF 'the one driver verb used' "$SK17" \
   && grep -qF 'so this run is ATTENDED: the driver verbs used are' "$SK17" \
   && grep -qF -- 'plus `--record-round` and `--chain-verdict` where a' "$SK17" && echo 1 || echo 0)
check_arm "arm 18 the render's ATTENDED bullet names the chain's two verbs" "$_v18"

# ---- arm 19 (TOOL-aProfiledEffort-2 AC9): `handoff.py stage-efforts` and `role-efforts` hand a named
# ---- model to the resolver. ONE profile, `tfam`, is appended to the fixture's policy after the
# ---- scaffold: it answers the model id `vendor-tfam-9`, and no profile answers `vendor-other-9`.
# ---- Every appended level sits at the floor `medium` or above, which R12 holds (TOOL-dBoundRoles-23 S7).
# ---- 19a's expected bytes come from A19P, an inline program that imports nothing from the kit and
# ---- reads the fixture's `[effort]` tables, its workflow table and the scaffolded role index, so
# ---- the guard shares no code with the verbs it guards. The arm reads no git revision. 19c's last
# ---- clause reds the arm where a default table already gives its two literals, which would
# ---- otherwise pass by finding nothing. The failing cases, observed at the close and not by the
# ---- pass that wrote this: the two verbs' resolver calls passing None for the model, which reds
# ---- 19c, and the shared JSON writer without its `separators`, which reds 19a and 19c.
A19P='import json, pathlib, sys, tomllib
kit, index, what = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
with open(kit / "house" / "policy.toml", "rb") as fh:
    effort = tomllib.load(fh)["effort"]
def level(slot):
    return effort.get("roles", {}).get(slot, effort["default"])
if what == "roles":
    with open(index, encoding="utf-8") as fh:
        out = {s: level(s) for s, r in json.load(fh)["roles"].items() if r["agent"]}
else:
    with open(kit / "workflows.toml", "rb") as fh:
        stages = {r["key"]: r["role"] for r in next(w["stages"] for w in tomllib.load(fh)["workflow"]
                                                     if w["name"] == what)}
    over = effort.get("stages", {}).get(what, {})
    out = {k: over.get(k, level(s)) for k, s in stages.items()}
sys.stdout.buffer.write((json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8"))'
build_fixture; _rc19=$?
printf '%s\n' '' '[effort.profiles.tfam]' 'match = ["tfam"]' 'default = "medium"' '' \
   '[effort.profiles.tfam.roles]' 'gov-builder = "max"' '' \
   '[effort.profiles.tfam.stages.closing-review]' 'synthesis = "xhigh"' >> "$FX/$KREL/house/policy.toml"
_a19=1; _b19=1; _c19=1; _d19=1; [ "$_rc19" = 0 ] || _a19=0
for _w in spec-write closing-review roles; do
  _q=(stage-efforts "$_w"); [ "$_w" = roles ] && _q=(role-efforts)
  _f="$TMP_ROOT/a19.$_w"
  (cd "$FX" && "$PY" -B "$KREL/handoff.py" "${_q[@]}") > "$_f.plain" 2>/dev/null || _a19=0
  "$PY" -B -c "$A19P" "$FX/$KREL" "$FX/.claude/roles.json" "$_w" > "$_f.want" 2>/dev/null || _a19=0
  cmp -s "$_f.plain" "$_f.want" || _a19=0
  (cd "$FX" && "$PY" -B "$KREL/handoff.py" "${_q[@]}" --model vendor-other-9) > "$_f.other" 2>/dev/null || _b19=0
  cmp -s "$_f.plain" "$_f.other" || _b19=0
  (cd "$FX" && "$PY" -B "$KREL/handoff.py" "${_q[@]}" --model vendor-tfam-9) > "$_f.tfam" 2>/dev/null || _c19=0
  for _m in "" " "; do
    out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" "${_q[@]}" --model "$_m" 2>&1 >/dev/null); rc=$?
    [ "$rc" = 2 ] && [[ $out == *'--model is empty'* ]] || _d19=0
  done
done
grep -qF '"gov-builder":"max"' "$TMP_ROOT/a19.roles.tfam" && grep -qF '"synthesis":"xhigh"' "$TMP_ROOT/a19.closing-review.tfam" \
   && ! cmp -s "$TMP_ROOT/a19.roles.plain" "$TMP_ROOT/a19.roles.tfam" \
   && ! cmp -s "$TMP_ROOT/a19.closing-review.plain" "$TMP_ROOT/a19.closing-review.tfam" || _c19=0
check_arm "arm 19 with no model both verbs print the default tables' levels, re-derived inline" "$_a19"
check_arm "arm 19 a model id no profile matches prints the no-flag bytes" "$_b19"
check_arm "arm 19 a model id the appended profile matches prints that profile's levels" "$_c19"
check_arm "arm 19 an empty or whitespace-only --model refuses with exit 2, naming the flag" "$_d19"
# 19e (TOOL-aProfiledEffort-4 S8): a second profile, `tven`, matching `vendor`, so `vendor-tfam-9`
# is a model two profiles match. Both verbs exit 1 with stdout empty and a stderr naming R12 and
# both `match` keys, and no Traceback. The append comes last: `tven` also answers `vendor-other-9`,
# which 19b reads as unmatched.
printf '%s\n' '' '[effort.profiles.tven]' 'match = ["vendor"]' 'default = "medium"' >> "$FX/$KREL/house/policy.toml"
_e19=1
for _w in roles build; do
  _q=(stage-efforts "$_w"); [ "$_w" = roles ] && _q=(role-efforts)
  (cd "$FX" && "$PY" -B "$KREL/handoff.py" "${_q[@]}" --model vendor-tfam-9) > "$TMP_ROOT/a19e.out" 2>"$TMP_ROOT/a19e.err"; rc=$?
  [ "$rc" = 1 ] && [ ! -s "$TMP_ROOT/a19e.out" ] && grep -qF 'R12' "$TMP_ROOT/a19e.err" \
     && grep -qF 'effort.profiles.tfam.match' "$TMP_ROOT/a19e.err" && grep -qF 'effort.profiles.tven.match' "$TMP_ROOT/a19e.err" \
     && ! grep -qF 'Traceback' "$TMP_ROOT/a19e.err" || _e19=0
done
check_arm "arm 19 a model two profiles match exits 1 through both verbs, naming both match keys" "$_e19"

# ---- arm 20 (TOOL-aGuardedEffort-1 AC6): the spawn guard matches a model id to a profile as the
# ---- resolver does. One list of ids, read by `roles_lib.resolve_profile` over arm 19's fixture
# ---- policy, which holds `tfam` and `tven`, and by the hooks kit's `resolveModelProfile` over the
# ---- index rendered from it: a profile's name, `-` for none, `!` for two. The list holds the empty
# ---- id, `affable-1`, `atfam-1`, which holds `tfam` inside a longer word, and the two-profile
# ---- `vendor-tfam-9`. It SKIPs as arm 6 does and stays out of the floor. The failing case, observed
# ---- at the close and not by the pass that wrote this: a substring match in the hook, which answers
# ---- `tfam` for `atfam-1`. WHAT IT DOES NOT CHECK: an id holding a letter outside ASCII.
A20_IDS=("" "affable-1" "atfam-1" "tfam9" "maker-tfam-9" "Maker-TFAM-9" "vendor-other-9" "vendor-tfam-9" "us.maker/x-tfam-9:0" "---")
if [ -z "$HK" ]; then
  echo "SKIP arm 20 — no hooks kit holding agent-cap.js was found from $KREL"
elif ! command -v node >/dev/null 2>&1; then
  echo "SKIP arm 20 — no node on PATH to run $HK/agent-cap.js"
else
  (cd "$FX" && "$PY" -B "$KREL/render_agents.py" --write >/dev/null 2>&1); _rc20=$?
  FXN=$(cd "$FX" && { pwd -W 2>/dev/null || pwd; })
  "$PY" -B -c 'import sys
sys.path.insert(0, sys.argv[1])
import roles_lib as l
p = l.load_policy(sys.argv[1], l.load_roles(sys.argv[1]), l.load_workflows(sys.argv[1]))
out = []
for m in sys.argv[2:]:
    try:
        out.append(l.resolve_profile(p, m) or "-")
    except l.RolesError:
        out.append("!")
sys.stdout.buffer.write("".join(a + "\n" for a in out).encode("utf-8"))' "$FX/$KREL" "${A20_IDS[@]}" > "$TMP_ROOT/a20.py" 2>/dev/null
  node -e 'const cap = require(process.argv[1] + "/agent-cap.js")
const e = require(process.argv[1] + "/scratch-guard.js").loadRoleIndex(process.argv[2]).effort
for (const m of process.argv.slice(3)) { const n = cap.resolveModelProfile(e.profiles, m); process.stdout.write((n.length > 1 ? "!" : n[0] || "-") + "\n") }' \
    "$HK" "$FXN" "${A20_IDS[@]}" > "$TMP_ROOT/a20.js" 2>/dev/null
  _a20=$(tr -d '\r' < "$TMP_ROOT/a20.py" | tr '\n' ' '); _j20=$(tr -d '\r' < "$TMP_ROOT/a20.js" | tr '\n' ' ')
  check_arm "arm 20 resolve_profile and resolveModelProfile give every listed model id the same answer" \
     "$([ "$_rc20" = 0 ] && [ -n "$_a20" ] && [ "$_a20" = "$_j20" ] && echo 1 || echo 0)"
  [ "$_a20" = "$_j20" ] || printf '    resolve_profile: %s\n    resolveModelProfile: %s\n' "$_a20" "$_j20"
  check_arm "arm 20 ...and the resolver's answers are none for the empty id, affable-1, atfam-1 and tfam9, a profile for four ids, and two for vendor-tfam-9" \
     "$([ "$_a20" = '- - - - tfam tfam tven ! tfam - ' ] && echo 1 || echo 0)"
fi

# ---- arm 21 (TOOL-aGuardedEffort-1 AC7): the role index carries the policy's resolved levels, so a
# ---- profile level edited with no re-render is a drifted index. A profile is appended to the
# ---- fixture's policy and scaffolded in, which checks clean; its level is then edited in place.
# ---- No agent type carries a profile's level, so the index is the one path that can drift. The
# ---- failing case, observed at the close and not by the pass that wrote this: a render that writes
# ---- no `effort` key, under which the edited policy still checks clean.
build_fixture
printf '%s\n' '' '[effort.profiles.tfam]' 'match = ["tfam"]' 'default = "high"   # a21' >> "$FX/$KREL/house/policy.toml"
(cd "$FX" && bash "$FXK/adopt-roles.sh" --scaffold >/dev/null 2>&1); _rc21=$?
check_arm "arm 21 a policy that gains a profile scaffolds and checks clean" "$([ "$_rc21" = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
sed -i 's/^default = "high"   # a21$/default = "max"/' "$FX/$KREL/house/policy.toml"
out=$(run_adopter --check); rc=$?
check_arm "arm 21 a profile level edited with no re-render is a drifted index, named" \
   "$([ "$rc" = 1 ] && [[ $out == *'drift .claude/roles.json'* ]] && [[ $out != *'drift .claude/agents/'* ]] && echo 1 || echo 0)"

# ---- arm 22 (TOOL-dPavedRoad-3 AC2): the spec writer's handoff carries the brief's `## The prompt`
# ---- as its `brief:prompt` block, and an empty prompt refuses that key by name. The keys are the
# ---- fixture kit's gov-spec-writer reads filtered to the `brief:` family, on the native key
# ---- `parse_read_key` returns since the role spells each as its `field.` tag (TOOL-dBoundRoles-14 S7), so the shipped role is
# ---- what is proved; `task:` needs the kickoff checker, which a roles-kit fixture does not hold.
# ---- The failing case, observed at the close and not by the pass that wrote this: the dispatch
# ---- reverted so `brief:prompt` reads a `### prompt` sub-head, which renders no block and passes
# ---- the empty one.
build_fixture; _rc22=$?
A22=$("$PY" -B -c 'import pathlib, re, sys
fx, kit = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
sys.path.insert(0, str(kit))
import handoff, roles_lib as lib
reads = lib.load_roles(handoff.KIT_DIR)["gov-spec-writer"]["keys"]["reads"].split(", ")
keys = {"reads": ", ".join(k for k in reads if lib.parse_read_key(k)[0].startswith("brief:"))}
brief = fx / sys.argv[3] / "builds" / "bx" / "prompts" / "2026-11-10-prompt-TOOL-bx-1-brief.md"
brief.parent.mkdir(parents=True, exist_ok=True)
heads = ("Goal", "Items", "Acceptance", "Gates", "Non-goals")
body = "".join("### %s\n\n%s text\n\n" % (h, h) for h in heads)
lines = "> owner words, verbatim\n— owner, 2026-11-10\n"
for prompt in (lines, ""):
    text = "# Brief\n\n## The prompt\n\n%s\n## The brief\n\n%s" % (prompt, body)
    brief.write_text(text, encoding="utf-8")
    try:
        task = handoff.render_handoff(fx, sys.argv[3], lib.resolve_charter_path(fx),
                                      "gov-spec-writer", keys, "bx", "TOOL-bx-1", None, {}, None)[2]
        # the fact line of the block (TOOL-dBoundRoles-13) and the fence its content sits in (TOOL-dBoundRoles-38)
        print("rendered %d" % bool(re.search(r"### brief:prompt\n\n<!-- gov:fact key=record:\S+ class=\w+ -->\n\n```\n"
                                             + re.escape(lines) + r"```\n\n### brief:goal\n", task)))
    except lib.RolesError as e:
        print("refused %d" % str(e).split("\n")[0].startswith("brief:prompt — "))
' "$FX" "$FX/$KREL" "$MR" 2>&1)
A22=${A22//$'\r'/}
check_arm "arm 22 the spec writer's handoff carries the brief's prompt verbatim" \
   "$([ "$_rc22" = 0 ] && [ "${A22%%$'\n'*}" = 'rendered 1' ] && echo 1 || echo 0)"
check_arm "arm 22 an empty prompt refuses by name" \
   "$([ "${A22#*$'\n'}" = 'refused 1' ] && echo 1 || echo 0)"
[ "$A22" = $'rendered 1\nrefused 1' ] || printf '    %s\n' "${A22//$'\n'/$'\n'    }"

# ---- arm 23 (TOOL-dDeclaredLoop-29 AC7 AC8): a role reading `upstream:rows?` is handed the rows file
# ---- `--upstream` names as its `### upstream:rows` block, the row contract after the rows, and names
# ---- the key on its `Not supplied` line without one; the catalogue checker's R3 refuses a bare
# ---- `upstream:rows` as optional-only and an `upstream:` key outside the vocabulary. The fixture kit's
# ---- gov-builder and gov-skeptic files gain the keys, so the shipped role files are what is edited,
# ---- and the render's keys are gov-builder's reads filtered to the `upstream:` family, as arm 22
# ---- filters to `brief:`. The failing case, observed at the close and not by the pass that wrote
# ---- this: `READ_KEYS` at its base, which holds no `upstream:` family, so the render has no source
# ---- for the key and R3 reads the bare key as outside the vocabulary, never as optional-only.
build_fixture; _rc23=$?
A23=$("$PY" -B -c 'import pathlib, re, subprocess, sys
fx, kit, mr = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve(), sys.argv[3]
sys.path.insert(0, str(kit))
import handoff, roles_lib as lib
def set_reads(role, old, new):
    path = kit / "agents" / (role + ".agent.md")
    text = path.read_text(encoding="utf-8")
    path.write_text(re.sub(r"(?m)^(reads:.*?)%s$" % re.escape(old), lambda m: m.group(1) + new, text, count=1),
                    encoding="utf-8", newline="")
set_reads("gov-builder", "", ", upstream:rows?")
reads = lib.load_roles(handoff.KIT_DIR)["gov-builder"]["keys"]["reads"].split(", ")
keys = {"reads": ", ".join(k for k in reads if k.startswith("upstream:"))}
(fx / sys.argv[3] / "builds" / "bx").mkdir(parents=True, exist_ok=True)
rows = ("item.design.seams#seam-1 · seam · the kit resolver finds a sibling kit\n"
        "item.design.seams#must-2 · criterion · no second copy of the ladder\n")
(fx / "rows.txt").write_text(rows, encoding="utf-8")
for up in ("rows.txt", None):
    task = handoff.render_handoff(fx, mr, lib.resolve_charter_path(fx), "gov-builder", keys, "bx", "TOOL-bx-1",
                                  None, {}, None, upstream=up)[2]
    block = task.split("### upstream:rows\n\n", 1)[1] if "### upstream:rows\n\n" in task else ""
    # past the fact line of the block (TOOL-dBoundRoles-13) and the opening line of its fence (TOOL-dBoundRoles-38)
    block = re.sub(r"\A<!-- gov:fact key=record:\S+ class=\w+ -->\n\n```\n", "", block)
    if up:
        print("rendered %d" % (block.startswith(rows) and all(w in block for w in ("## Upstream", "used", "bypassed", "not-applicable"))))
    else:
        print("absent %d" % (not block and re.search(r"Not supplied, optional: [^\n]*`upstream:rows`", task) is not None))
set_reads("gov-builder", ", upstream:rows?", ", upstream:rows")
set_reads("gov-skeptic", "", ", upstream:other?")
out = subprocess.run([sys.executable, "-B", str(kit / "check_roles.py"), "--root", str(fx)], cwd=str(fx),
                     capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.splitlines()
r3 = [ln for ln in out if ": R3 — " in ln]
print("bare %d" % any("gov-builder" in ln and "upstream:rows must be optional" in ln for ln in r3))
print("other %d" % any("gov-skeptic" in ln and "upstream:other?" in ln and "outside the vocabulary" in ln for ln in r3))
' "$FX" "$FX/$KREL" "$MR" 2>&1)
A23=${A23//$'\r'/}
check_arm "arm 23 a role reading upstream:rows? is handed the rows and the row contract under --upstream" \
   "$([ "$_rc23" = 0 ] && [[ $A23 == *'rendered 1'* ]] && echo 1 || echo 0)"
check_arm "arm 23 ...and without --upstream names the key on its Not supplied line" \
   "$([[ $A23 == *'absent 1'* ]] && echo 1 || echo 0)"
check_arm "arm 23 R3 refuses a bare upstream:rows, naming it optional-only" \
   "$([[ $A23 == *'bare 1'* ]] && echo 1 || echo 0)"
check_arm "arm 23 R3 refuses upstream:other? as outside the vocabulary" \
   "$([[ $A23 == *'other 1'* ]] && echo 1 || echo 0)"
[ "$A23" = $'rendered 1\nabsent 1\nbare 1\nother 1' ] || printf '    %s\n' "${A23//$'\n'/$'\n'    }"

# ---- arm 24 (TOOL-dDeclaredLoop-56 AC28): a fixture whose copy of the loop kit is taken away after its
# ---- scaffold: the adopter's `--check` exits non-zero naming the library's refusal, never reading the
# ---- absent kit as an empty workflow table. The failing case, observed at the close and not by the
# ---- pass that wrote this: a `read_workflow_order` answering an empty table for an absent kit.
build_fixture; rm -rf "${FX:?}/$FXL"
A24=$(run_adopter --check); _rc24=$?
check_arm "arm 24 --check with no loop kit exits non-zero naming no loop kit places the workflows: " \
   "$([ "$_rc24" != 0 ] && [[ $A24 == *'no loop kit places the workflows: '* ]] && echo 1 || echo 0)"
[ "$_rc24" != 0 ] && [[ $A24 == *'no loop kit places the workflows: '* ]] || printf '    exit %s\n    %s\n' "$_rc24" "${A24//$'\n'/$'\n'    }"
# ---- arm 25 (TOOL-aTrimmedWait-7 AC1 to AC7): the agents verb's session record. Arm 9's fixture,
# ---- written afresh, run through the CLI: cold, which writes one record under the fixture's git
# ---- common dir; warm, which writes nothing; with the record's `notified` emptied, which drops the
# ---- `returned` line and so proves the record is read; after an append and after a torn line, each
# ---- resumed from the record's offset, which only a resumed read shows: the record's bad count,
# ---- seeded to 7, prints as a note, and the returned line needs the appended result to reach the
# ---- call through the rebuilt by_id (TOOL-aTrimmedWait-9); and with the record keyed off by a
# ---- transcript edit, a foreign key or an unwritable folder, each printing the cold lines. It reads
# ---- arm 9's writer and lines. The failing case, observed at the close and not by the pass that wrote this: handoff.py
# ---- at the base, where no record is written. Not checked: timing, and a forged record.
build_fixture; _rc23=$?
A23S="$TMP_ROOT/s23/projects/p/22222222-2222-4222-8222-222222222222.jsonl"
"$PY" -B -c "$A9_WRITE" "$FX" "$A23S" "$A9H" || echo "    arm 25: the fixture writer exited non-zero"
A23D="$FX/.git/handoff-calls"; cp "$A23S" "$TMP_ROOT/a23.full"
A23_EDIT='import json, pathlib, sys
rp = next(pathlib.Path(sys.argv[1]).glob("*.json"))
rec = json.loads(rp.read_text(encoding="utf-8"))
rec["notified"], mode = {}, sys.argv[2]
if mode == "parser":
    rec["parser"] = "0" * 64
elif mode == "session":
    rec["session"] += ".other"
elif mode == "offset":
    rec["offset"] = pathlib.Path(rec["session"]).stat().st_size + 1
elif mode == "bad":
    rec["bad"] = 7
text = json.dumps(rec)
rp.write_text(text[:len(text) // 2] if mode == "truncated" else text, encoding="utf-8")'
run_agents23() { out=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" agents --handoff "$A9H" --session "$A23S" 2>"$TMP_ROOT/a23.err"); rc=$?; out=${out//$'\r'/}; }
check_cold23() { [ "$rc" = 0 ] && [ "$out" = "$A9L1"$'\n'"$A9L2" ]; }
[ ! -e "$A23D" ]; _a=$?; run_agents23
check_arm "arm 25 a cold call prints arm 9's lines and writes one record under the fixture's git common dir" \
   "$([ "$_rc23" = 0 ] && [ "$_a" = 0 ] && check_cold23 && [ "$(ls "$A23D" | grep -cE '^[0-9a-f]{16}\.json$')" = 1 ] \
      && [ "$(ls -A "$A23D" | wc -l)" = 1 ] && echo 1 || echo 0)"
touch -d '2000-01-01 00:00:00' "$A23D"/*.json; run_agents23
_w23=0; check_cold23 && [ -n "$(find "$A23D" -name '*.json')" ] \
   && [ -z "$(find "$A23D" -name '*.json' -newermt '2001-01-01')" ] && _w23=1
check_arm "arm 25 ...a warm call prints the same lines and leaves the record unwritten" "$_w23"
"$PY" -B -c "$A23_EDIT" "$A23D" poison; _e23=$?; run_agents23
check_arm "arm 25 ...a record whose notifications are emptied drops the returned line, so the record is read" \
   "$([ "$_e23" = 0 ] && [ "$rc" = 0 ] && [ "$out" = "$A9L1" ] && echo 1 || echo 0)"
head -n 1 "$TMP_ROOT/a23.full" > "$A23S"; run_agents23
"$PY" -B -c "$A23_EDIT" "$A23D" bad; _e23=$?; tail -n +2 "$TMP_ROOT/a23.full" >> "$A23S"; run_agents23
check_arm "arm 25 ...a record taken on the first line, its bad count seeded, then the rest appended, prints the cold lines and the seeded count" \
   "$([ "$_e23" = 0 ] && check_cold23 && grep -q ': 7 line(s) did not parse' "$TMP_ROOT/a23.err" && echo 1 || echo 0)"
_l1=$(head -n 1 "$TMP_ROOT/a23.full" | wc -c)
head -c $((_l1 + 40)) "$TMP_ROOT/a23.full" > "$A23S"; run_agents23
"$PY" -B -c "$A23_EDIT" "$A23D" bad; _e23=$?; tail -c +$((_l1 + 41)) "$TMP_ROOT/a23.full" >> "$A23S"; run_agents23
check_arm "arm 25 ...a torn last line, its bad count seeded, then completed, prints the cold lines and the seeded count" \
   "$([ "$_e23" = 0 ] && check_cold23 && grep -q ': 7 line(s) did not parse' "$TMP_ROOT/a23.err" && cmp -s "$A23S" "$TMP_ROOT/a23.full" && echo 1 || echo 0)"
"$PY" -B -c "$A23_EDIT" "$A23D" poison; _e23=$?; sed -i 's/async_launched/async_launchex/' "$A23S"; run_agents23
check_arm "arm 25 a transcript edited at equal length keys the record off and prints the cold lines" \
   "$([ "$_e23" = 0 ] && check_cold23 && echo 1 || echo 0)"
_f=""
for _k in parser session offset truncated; do
  "$PY" -B -c "$A23_EDIT" "$A23D" "$_k" || _f="$_f $_k(no-edit)"; run_agents23; check_cold23 || _f="$_f $_k"
done
check_arm "arm 25 a record with a foreign parser, session or offset, or truncated, prints the cold lines" \
   "$([ -z "$_f" ] && echo 1 || echo 0)"
[ -z "$_f" ] || echo "    arm 25: the record was used under:$_f"
rm -rf "$A23D"; printf x > "$A23D"; run_agents23
_w23=0; check_cold23 && [ -z "$(find "$FX/.git" -name '*.tmp')" ] && _w23=1
check_arm "arm 25 an unwritable record folder prints the cold lines and leaves no temporary file" "$_w23"

# ---- arm 26 (TOOL-dBoundRoles-14 AC6): R3 reads each `reads` entry through `parse_read_key`, so the shipped
# ---- role files' tag spelling grades clean; a fixture role whose `reads` carries the misspelt tag
# ---- `field.task.titel` is one R3 line naming it, while `field.task.title` yields none; and gov-reuse-scout's
# ---- `field.card.reuse?` without its `?` is one R3 line saying `card:reuse` must be optional. The failing
# ---- case, observed at the close and not by the pass that wrote this: R3 grading the raw entry, so every
# ---- migrated tag reads as outside the vocabulary and the tag spelling of a bare `card:reuse` passes.
build_fixture; _rc26=$?
A26=$("$PY" -B -c 'import pathlib, re, subprocess, sys
fx, kit = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
def set_reads(role, old, new):
    path = kit / "agents" / (role + ".agent.md")
    text = path.read_bytes().decode("utf-8")
    path.write_bytes(re.sub(r"(?m)^(reads:.*?)%s(\r?)$" % re.escape(old), lambda m: m.group(1) + new + m.group(2),
                            text, count=1).encode("utf-8"))
def read_r3():
    out = subprocess.run([sys.executable, "-B", str(kit / "check_roles.py"), "--root", str(fx)], cwd=str(fx),
                         capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.splitlines()
    return [ln for ln in out if ": R3 — " in ln]
print("clean %d" % (not read_r3()))
set_reads("gov-builder", "", ", field.task.titel")
got = read_r3()
print("titel %d" % (len(got) == 1 and "gov-builder" in got[0] and "field.task.titel" in got[0]
                    and "outside the vocabulary" in got[0]))
set_reads("gov-builder", ", field.task.titel", ", field.task.title")
print("title %d" % (not read_r3()))
set_reads("gov-reuse-scout", "field.card.reuse?", "field.card.reuse")
got = read_r3()
print("reuse %d" % (len(got) == 1 and "gov-reuse-scout" in got[0] and "card:reuse must be optional" in got[0]))
' "$FX" "$FX/$KREL" 2>&1)
A26=${A26//$'\r'/}
check_arm "arm 26 the shipped role files' tag-spelt reads grade clean under R3" \
   "$([ "$_rc26" = 0 ] && [[ $A26 == *'clean 1'* ]] && echo 1 || echo 0)"
check_arm "arm 26 R3 names a planted field.task.titel as outside the vocabulary, one line" \
   "$([[ $A26 == *'titel 1'* ]] && echo 1 || echo 0)"
check_arm "arm 26 ...while field.task.title yields no R3 line" \
   "$([[ $A26 == *'title 1'* ]] && echo 1 || echo 0)"
check_arm "arm 26 R3 refuses field.card.reuse without its ?, saying card:reuse must be optional" \
   "$([[ $A26 == *'reuse 1'* ]] && echo 1 || echo 0)"
[ "$A26" = $'clean 1\ntitel 1\ntitle 1\nreuse 1' ] || printf '    %s\n' "${A26//$'\n'/$'\n'    }"

# ---- arm 27 (TOOL-dBoundRoles-2 AC1 AC2 AC3 AC4 AC6): the fixture, holding the enforcers its roles' `never`
# ---- entries name, grades clean; then each plant on gov-builder is ONE line of its rule, the file restored after
# ---- it: a bare limit and a limit whose script no kit holds are R13, a body prohibition is R5 naming the line,
# ---- a template with no `outcome` is R2; and the `never` row cut from the fixture's role-schema.toml makes
# ---- every role file's `never:` an R2 unknown key, since the key set is derived from the schema. The failing
# ---- case, observed at the close and not by the pass that wrote this: any one of the plants passing.
build_fixture; _rc27=$?
A27=$("$PY" -B -c 'import pathlib, re, subprocess, sys
fx, kit = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
role, schema = kit / "agents" / "gov-builder.agent.md", kit / "role-schema.toml"
def grade():
    out = subprocess.run([sys.executable, "-B", str(kit / "check_roles.py"), "--root", str(fx)], cwd=str(fx),
                         capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.splitlines()
    return [ln for ln in out if re.search(r": R(2|5|13) — ", ln)]
def plant(path, edit):
    before = path.read_bytes()
    path.write_bytes(edit(before.decode("utf-8")).encode("utf-8"))
    try:
        return grade()
    finally:
        path.write_bytes(before)
def one(got, rule, *needles):
    return int(len(got) == 1 and (": %s — " % rule) in got[0] and all(n in got[0] for n in needles))
print("clean %d" % (not grade()))
never = lambda tail: lambda t: re.sub(r"(?m)^(never: .*?)(\r?)$", lambda m: m.group(1) + tail + m.group(2), t, count=1)
print("bare %d" % one(plant(role, never("; edits the spec")), "R13", "gov-builder", "edits the spec", "no enforcer"))
print("ghost %d" % one(plant(role, never("; writes outside ROUTED_PATHS — ghost-guard.js arm")), "R13", "ghost-guard.js"))
print("body %d" % one(plant(role, lambda t: t.rstrip() + "\n\nNever edit the spec.\n"), "R5", "Never edit the spec."))
print("outcome %d" % one(plant(role, lambda t: re.sub(r"(?m)^return: .*?(\r?)$", lambda m: "return: commit:sha?" + m.group(1), t, count=1)),
                         "R2", "outcome"))
got = plant(schema, lambda t: re.sub(r"\[\[field\]\]\r?\nkey = \"never\"\r?\n(?:[a-z]+ = .*\r?\n)*\r?\n", "", t, count=1))
roles = len(list((kit / "agents").glob("*.agent.md")))
print("schema %d" % int(roles > 0 and len(got) == roles and all("unknown front-matter key " + chr(39) + "never" + chr(39) in g for g in got)))
' "$FX" "$FX/$KREL" 2>&1)
A27=${A27//$'\r'/}
check_arm "arm 27 the fixture, holding its roles' enforcers, grades no R2, R5 or R13 line" \
   "$([ "$_rc27" = 0 ] && [[ $A27 == *'clean 1'* ]] && echo 1 || echo 0)"
check_arm "arm 27 a bare never entry is one R13 line saying it names no enforcer" \
   "$([[ $A27 == *'bare 1'* ]] && echo 1 || echo 0)"
check_arm "arm 27 a never entry naming a script no kit holds is one R13 line naming it" \
   "$([[ $A27 == *'ghost 1'* ]] && echo 1 || echo 0)"
check_arm "arm 27 a body line carrying a prohibition is one R5 line naming it" \
   "$([[ $A27 == *'body 1'* ]] && echo 1 || echo 0)"
check_arm "arm 27 a return template with no outcome is one R2 line" \
   "$([[ $A27 == *'outcome 1'* ]] && echo 1 || echo 0)"
check_arm "arm 27 the never row cut from the schema makes every role's never an R2 unknown key" \
   "$([[ $A27 == *'schema 1'* ]] && echo 1 || echo 0)"
[ "$A27" = $'clean 1\nbare 1\nghost 1\nbody 1\noutcome 1\nschema 1' ] || printf '    %s\n' "${A27//$'\n'/$'\n'    }"

# ---- arm 28 (TOOL-dBoundRoles-1 AC1): R2 joins each role's `layer` to a row of the layer register the fixture
# ---- holds at the home `playbook`, and grades `acts-as` against its two values. gov-builder planted at
# ---- `layer: layer.nowhere` and gov-skeptic at `acts-as: helper` exit 1 with exactly two R2 lines, one naming
# ---- each; restored, no R2 line. The failing case, observed at the close and not by the pass that
# ---- wrote this: `layer` graded by its shape alone, so a tag naming no row passes and one R2 line prints.
build_fixture; _rc28=$?
A28=$("$PY" -B -c 'import pathlib, re, subprocess, sys
fx, kit = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
def grade():
    p = subprocess.run([sys.executable, "-B", str(kit / "check_roles.py"), "--root", str(fx)], cwd=str(kit),
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, [ln for ln in p.stdout.splitlines() if ": R2 — " in ln]
paths = {kit / "agents" / "gov-builder.agent.md": ("layer", "layer.nowhere"),
         kit / "agents" / "gov-skeptic.agent.md": ("acts-as", "helper")}
before = {p: p.read_bytes() for p in paths}
rc, got = grade()
print("clean %d" % int(not got))
try:
    for p, (key, value) in paths.items():
        text = before[p].decode("utf-8")
        p.write_bytes(re.sub(r"(?m)^%s: .*?(\r?)$" % re.escape(key), lambda m: "%s: %s%s" % (key, value, m.group(1)),
                             text, count=1).encode("utf-8"))
    rc, got = grade()
finally:
    for p, b in before.items():
        p.write_bytes(b)
print("planted %d" % int(rc == 1 and len(got) == 2
                         and any("gov-builder" in g and "layer.nowhere" in g for g in got)
                         and any("gov-skeptic" in g and "helper" in g for g in got)))
rc, got = grade()
print("restored %d" % int(not got))
' "$FX" "$FX/$KREL" 2>&1)
A28=${A28//$'\r'/}
check_arm "arm 28 the fixture, holding the layer register at the home playbook, grades no R2 line" \
   "$([ "$_rc28" = 0 ] && [[ $A28 == *'clean 1'* ]] && echo 1 || echo 0)"
check_arm "arm 28 a layer naming no row and an acts-as outside item and cycle are two R2 lines, one naming each" \
   "$([[ $A28 == *'planted 1'* ]] && echo 1 || echo 0)"
check_arm "arm 28 restored, the fixture grades no R2 line again" "$([[ $A28 == *'restored 1'* ]] && echo 1 || echo 0)"
[ "$A28" = $'clean 1\nplanted 1\nrestored 1' ] || printf '    %s\n' "${A28//$'\n'/$'\n'    }"

# ---- arm 29 (TOOL-dBoundRoles-21 AC1 to AC6): the policy keys read before the house file, the grant a role
# ---- field. The fixture gains a copy of the policy kit at the home `policy` beside the roles kit and commits on
# ---- `main`, the branch `policy.py get` reads as the landed revision of a clone with no remote; each plant
# ---- commits its own `.governance/policy.toml`. The house file's gov-builder level is raised to `xhigh`
# ---- first, so a set key and the house level differ. The expected levels and model are read from the
# ---- fixture's files inline, never through the kit. The failing cases, observed at the close and not by
# ---- the pass that wrote this: the house file read before the keys (AC2), a stage that inherits no role
# ---- key (AC3), the model key matched by role alone (AC1), the index or the ceiling reading the house row
# ---- before the field (AC4), the `default` slot admitted (AC5), and an absent house file refusing (AC6).
# ---- WHAT IT DOES NOT CHECK: a key's `last-valid` source, a profile beside a set key, or `roles.effort.default`.
build_fixture; _rc29=$?
_pk=policy; [[ $FXK == */* ]] && _pk=${FXK%/*}/policy
mkdir -p "$FX/$_pk" && cp -R "$HERE/../policy"/. "$FX/$_pk"/ || _rc29=2
A29=$("$PY" -B -c 'import json, os, pathlib, re, subprocess, sys
fx, kit = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k != "GOV_DEFAULT_BRANCH"}
def git(*a):
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@fx", "-C", str(fx), *a], env=env,
                          capture_output=True, text=True).returncode
def commit(*lines):
    (fx / ".governance").mkdir(exist_ok=True)
    (fx / ".governance" / "policy.toml").write_text("".join(ln + "\n" for ln in lines) or "# no key\n", encoding="utf-8")
    return git("add", "-A") == 0 and git("commit", "-q", "--allow-empty", "-m", "plant") == 0
def run(*a):
    p = subprocess.run([sys.executable, "-B", *a], cwd=str(kit), env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, p.stdout.strip(), p.stderr
def front(slot, key):
    text = (kit / "agents" / (slot + ".agent.md")).read_text(encoding="utf-8")
    return re.search(r"(?m)^%s: *(.*?)\r?$" % re.escape(key), text.split("\n---", 1)[0]).group(1)
house = kit / "house" / "policy.toml"
house.write_text(re.sub(r"(?m)^gov-builder = \"high\"", "gov-builder = \"xhigh\"", house.read_text(encoding="utf-8")),
                 encoding="utf-8")
ok = git("symbolic-ref", "HEAD", "refs/heads/main") == 0 and commit()
efforts = lambda w: run("handoff.py", "stage-efforts", w)[1]
model = lambda: run("-c", "import roles_lib as l; print(l.resolve_role_model(%r, %r, %r))"
                    % ("gov-builder", "claude-code", str(fx)))[1]
ok2 = ok and commit("roles.effort.gov-builder = \"high\"") and efforts("build") == json.dumps({"builder": "high"}, separators=(",", ":"))
print("ac2 %d" % int(ok2 and commit() and efforts("build") == json.dumps({"builder": "xhigh"}, separators=(",", ":"))))
got = json.loads(efforts("spec-review") or "{}") if commit("roles.effort.gov-skeptic = \"max\"") else {}
print("ac3 %d" % int(got.get("skeptic") == "max"))
a = model() if commit("roles.model.gov-builder.codex = \"gpt-x\"") else None
b = model() if commit("roles.model.gov-builder.codex = \"gpt-x\"", "roles.model.gov-builder.claude-code = \"opus\"") else None
rendered = run("render_agents.py", "--write")[0] == 0 and re.search(
    r"(?m)^model: opus\r?$", (fx / ".claude" / "agents" / "gov-builder.md").read_text(encoding="utf-8")) is not None
print("ac1 %d" % int(a == front("gov-builder", "model") and b == "opus" and rendered))
role = kit / "agents" / "gov-builder.agent.md"
held = role.read_bytes()
def grant():
    rc = run("render_agents.py", "--write")[0]
    index = json.loads((fx / ".claude" / "roles.json").read_text(encoding="utf-8"))
    ceiling = [ln for ln in (fx / ".claude" / "agents" / "gov-builder.md").read_text(encoding="utf-8").splitlines()
               if ln.startswith("- gate legs: ")]
    return rc, index["roles"]["gov-builder"]["gates"], ceiling
commit()
house.write_text(house.read_text(encoding="utf-8") + "gov-builder = [\"memory hygiene\"]\n", encoding="utf-8")
f = grant()   # the shipped gov-builder file, whose field grants `lexicon naming predicates?`
role.write_bytes(re.sub(rb"(?m)^gates: .*\r?\n", b"", held))
h = grant()
role.write_bytes(held)
print("ac4 %d" % int(re.search(rb"(?m)^gates: lexicon naming predicates\?\r?$", held) is not None
                     and f == (0, ["lexicon naming predicates"], ["- gate legs: lexicon naming predicates"])
                     and h == (0, ["memory hygiene"], ["- gate legs: memory hygiene"])))
plant = kit / "agents" / "default.agent.md"
plant.write_bytes(re.sub(rb"(?m)^name: gov-tester(\r?)$", rb"name: default\1", (kit / "agents" / "gov-tester.agent.md").read_bytes()))
rc, out, _err = run("check_roles.py", "--root", str(fx))
plant.unlink()
said = [ln for ln in out.splitlines() if ": R2 — " in ln]
print("ac5 %d" % int(rc == 1 and len(said) == 1 and "default" in said[0] and "reserved" in said[0]))
house.unlink()
_rc, out, _err = run("check_roles.py", "--root", str(fx))
print("ac6 %d" % int(efforts("build") == json.dumps({"builder": front("gov-builder", "effort")}, separators=(",", ":"))
                     and "roles: graded " in out and " R12 " not in out and ": R12 — " not in out))
' "$FX" "$FX/$KREL" 2>&1)
A29=${A29//$'\r'/}
check_arm "arm 29 a set roles.effort.<role> key beats the house file's level, and absent the house level reads" \
   "$([ "$_rc29" = 0 ] && [[ $A29 == *'ac2 1'* ]] && echo 1 || echo 0)"
check_arm "arm 29 a stage with only its role's key set reads that key before the house stage row" \
   "$([[ $A29 == *'ac3 1'* ]] && echo 1 || echo 0)"
check_arm "arm 29 a codex model key leaves the claude-code model the declared one, and a claude-code key sets it and the agent type's model line" \
   "$([[ $A29 == *'ac1 1'* ]] && echo 1 || echo 0)"
check_arm "arm 29 a role's gates field beats its house [gates] row in the index and the ceiling, and absent the row reads" \
   "$([[ $A29 == *'ac4 1'* ]] && echo 1 || echo 0)"
check_arm "arm 29 a role file whose slot is default is one R2 line naming the reserved slot" \
   "$([[ $A29 == *'ac5 1'* ]] && echo 1 || echo 0)"
check_arm "arm 29 an absent house file falls to the declared effort and is no R12 line" \
   "$([[ $A29 == *'ac6 1'* ]] && echo 1 || echo 0)"
[ "$A29" = $'ac2 1\nac3 1\nac1 1\nac4 1\nac5 1\nac6 1' ] || printf '    %s\n' "${A29//$'\n'/$'\n'    }"

# ---- arm 30 (TOOL-dBoundRoles-22 AC2 AC4 AC5, and AC3's house-less half): the stage rows graded as R9,
# ---- and a row's declared effort read after the keys and the house file. The fixture adds the workflow
# ---- `scratch` the way the loop kit's workflow factory adds one, its name to the copied checker's
# ---- WORKFLOW_NAMES and its row to the copied loop definition, so R6 places it; its two stage rows are
# ---- `scout` as gov-reuse-scout and `judge` as gov-skeptic. A plant rewrites `judge` alone. The fixture's
# ---- loop kit holds no `upstream.py` (a01362eb0's kit answers no `kinds` verb either), so the row kinds
# ---- fall to the seg shape; a stub `upstream.py` answering `kinds` stands for the verb §8 F5 asked of
# ---- dDeclaredLoop. The policy kit is copied, and each limit committed on `main`, as arm 29 does. The
# ---- failing cases, owed at the close and not observed by the pass that wrote this: a stage map typed
# ---- per entry admitting one role (ac2), the row fields read without validation (ac4a, ac4b), the
# ---- kinds verb unread (ac4b), the cap compared with a literal (ac5d), and the row's effort read after
# ---- the role's declaration (ac3), the house file deleted last, so every plant above reads it.
# ---- WHAT IT DOES NOT CHECK: a refusing policy reader, a repeated key, a row on a non-workflow driver,
# ---- or `receives` against the kinds; nor the real loop kit's `kinds` verb, which has not landed.
# ---- `scratch` carries the shape TOOL-dBoundRoles-16 requires of an entry listing a role, `single` as the
# ---- workflow factory writes it, and its `judge` row `kind = "panel"`, the kind gov-skeptic declares.
build_fixture; _rc30=$?
_pk=policy; [[ $FXK == */* ]] && _pk=${FXK%/*}/policy
A30=$("$PY" -B -c 'import json, os, pathlib, re, shutil, subprocess, sys, tomllib
fx, kit, loop, policy_src, policy_dst = (pathlib.Path(a).resolve() for a in sys.argv[1:6])
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k != "GOV_DEFAULT_BRANCH"}
def git(*a):
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@fx", "-C", str(fx), *a], env=env,
                          capture_output=True, text=True).returncode
def run(*a):
    p = subprocess.run([sys.executable, "-B", *a], cwd=str(kit), env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, p.stdout.strip()
def check():
    rc, out = run("check_roles.py", "--root", str(fx))
    return rc, out, [ln for ln in out.splitlines() if ": R9 — " in ln]
ENTRY = """
[[workflow]]
name = "scratch"
driver = "workflow"
harness = "{prefix}/workflows/scratch.js"
roles = ["gov-reuse-scout", "gov-skeptic"]
kind = "single"
checklist = "none"
orientation = "none"
enforced-by = ["agent-cap.js spawn guard"]
trigger = "any time this arm plants it"
"""
ROW = """
[[workflow.stages]]
key = "%s"
role = "%s"
%sfan = %s
cap = %s
effort = "%s"
receives = %s
returns = %s
"""
STUB = """import sys
if sys.argv[1:] != ["kinds"]:
    sys.exit(2)
for kind in ("seam", "criterion", "interface", "fork", "finding", "repair"):
    print(kind)
"""
table, checker = kit / "workflows.toml", kit / "check_roles.py"
held = table.read_text(encoding="utf-8")
def plant(fan=1, cap=1, effort="medium", returns=("finding",)):
    table.write_text(held + ENTRY + ROW % ("scout", "gov-reuse-scout", "", 1, 1, "medium", "[]", json.dumps(["seam"]))
                     + ROW % ("judge", "gov-skeptic", "kind = \"panel\"\n", fan, cap, effort, json.dumps(["seam"]),
                              json.dumps(list(returns))),
                     encoding="utf-8")
def commit(n):
    (fx / ".governance").mkdir(exist_ok=True)
    (fx / ".governance" / "policy.toml").write_text("runtime.agents-in-flight = %d\n" % n, encoding="utf-8")
    return git("add", "-A") == 0 and git("commit", "-q", "--allow-empty", "-m", "limit %d" % n) == 0
text = checker.read_text(encoding="utf-8")
added = text.replace("WORKFLOW_NAMES = (", "WORKFLOW_NAMES = (%s, " % json.dumps("scratch"), 1)
checker.write_text(added, encoding="utf-8")
with open(loop / "loop.toml", "a", encoding="utf-8") as fh:
    fh.write("\n[[workflow]]\nname = %s\norder = 0\nstep = %s\n" % (json.dumps("scratch"), json.dumps("none")))
plant()
ok = added != text and git("symbolic-ref", "HEAD", "refs/heads/main") == 0 \
    and run("check_roles.py", "--root", str(fx), "--write")[0] == 0
rc, out, r9 = check()
args = run("handoff.py", "harness-args", "scratch")[1]
print("ac2 %d" % int(ok and rc == 0 and not r9
                     and args == json.dumps({"judge": "gov-skeptic", "scout": "gov-reuse-scout"}, separators=(",", ":"))))
plant(fan=0, effort="huge", returns=("bug",))
rc, out, r9 = check()
print("ac4a %d" % int(rc == 1 and len(r9) == 2 and all("stage judge" in ln for ln in r9)
                      and any("fan 0 " in ln for ln in r9) and any("huge" in ln for ln in r9)
                      and "seg shape alone" in out))
(loop / "upstream.py").write_text(STUB, encoding="utf-8")
rc, out, r9 = check()
(loop / "upstream.py").unlink()
print("ac4b %d" % int(rc == 1 and len(r9) == 3 and all("stage judge" in ln for ln in r9)
                      and any("bug" in ln for ln in r9) and "seg shape alone" not in out))
plant(cap=7)
rc, out, r9 = check()
print("ac5a %d" % int(rc == 0 and not r9 and "stage cap arm is unarmed" in out))
shutil.copytree(policy_src, policy_dst, dirs_exist_ok=True)
rc, out, r9 = check() if commit(6) else (None, "", [])
print("ac5b %d" % int(rc == 1 and len(r9) == 1
                      and all(s in r9[0] for s in ("stage judge", "caps 7 agents", "agents-in-flight 6"))))
plant(cap=6)
rc, out, r9 = check()
print("ac5c %d" % int(rc == 0 and not r9 and "against runtime.agents-in-flight 6," in out))
rc, out, r9 = check() if commit(5) else (None, "", [])
print("ac5d %d" % int(rc == 1 and any(all(s in ln for s in ("stage judge", "caps 6 agents", "agents-in-flight 5"))
                                      for ln in r9)))
(kit / "house" / "policy.toml").unlink()
with open(table, "rb") as fh:
    rows = next(w["stages"] for w in tomllib.load(fh)["workflow"] if w["name"] == "spec-write")
def declared(slot):
    text = (kit / "agents" / (slot + ".agent.md")).read_text(encoding="utf-8")
    return re.search(r"(?m)^effort: *(.*?)\r?$", text.split("\n---", 1)[0]).group(1)
got = json.loads(run("handoff.py", "stage-efforts", "spec-write")[1] or "{}")
print("ac3 %d" % int(got == {r["key"]: r["effort"] for r in rows}
                     and any(r["effort"] != declared(r["role"]) for r in rows)))
' "$FX" "$FX/$KREL" "$FX/$FXL" "$HERE/../policy" "$FX/$_pk" 2>&1)
A30=${A30//$'\r'/}
check_arm "arm 30 a two-stage mixed-role entry grades no R9 line, and harness-args maps both keys to their roles" \
   "$([ "$_rc30" = 0 ] && [[ $A30 == *'ac2 1'* ]] && echo 1 || echo 0)"
check_arm "arm 30 a zero fan and an unknown effort are two R9 lines naming the stage, and the seg-shape note, with no kinds verb" \
   "$([[ $A30 == *'ac4a 1'* ]] && echo 1 || echo 0)"
check_arm "arm 30 ...and beside a loop kit answering kinds, the unknown row kind is the third" \
   "$([[ $A30 == *'ac4b 1'* ]] && echo 1 || echo 0)"
check_arm "arm 30 with no policy kit a cap of 7 grades no R9 line and the cap arm prints unarmed" \
   "$([[ $A30 == *'ac5a 1'* ]] && echo 1 || echo 0)"
check_arm "arm 30 a cap of 7 over a committed limit of 6 is one R9 line naming judge, 7 and 6" \
   "$([[ $A30 == *'ac5b 1'* ]] && echo 1 || echo 0)"
check_arm "arm 30 ...a cap of 6 exits 0, the summary naming the limit" \
   "$([[ $A30 == *'ac5c 1'* ]] && echo 1 || echo 0)"
check_arm "arm 30 ...and the limit lowered to 5 reds the cap of 6" \
   "$([[ $A30 == *'ac5d 1'* ]] && echo 1 || echo 0)"
check_arm "arm 30 with the house file deleted and no key set, stage-efforts prints the rows' declared levels, one differing from its role's" \
   "$([[ $A30 == *'ac3 1'* ]] && echo 1 || echo 0)"
[ "$A30" = $'ac2 1\nac4a 1\nac4b 1\nac5a 1\nac5b 1\nac5c 1\nac5d 1\nac3 1' ] || printf '    %s\n' "${A30//$'\n'/$'\n'    }"

# ---- arm 31 (TOOL-dBoundRoles-16 AC2 AC3 AC4 AC6): the workflow shapes graded as R9. The fixture gains the
# ---- playbook kit whole over its layer register, so the unit join reads this kit's instructions.toml through
# ---- `read_units`; the workflows kit's replay_scorer.py at the home `workflows`; and the policy kit, the limit
# ---- 6 committed on `main` as arm 30 commits it, beside a tracked case file and a tracked label-key file. Each
# ---- plant is one R9 line, the file restored after it: the `panel` [[kind]] row's cap raised to 9 (ac2); the
# ---- `reuse` entry made an experiment naming both scorer and judge, neither, and a reruns key `ghost.medium`
# ---- (ac3a to ac3c), and with the scorer `scouted-seam` and every variant keyed exiting 0 (ac3d); gov-builder's
# ---- shapes cut to `single` while its stages run per-unit, one line naming both stages and the kind (ac4a),
# ---- and the role index listing each role's shapes as its file declares them after a render (ac4b);
# ---- closing-review's orientation `unit.orient.nothing` (ac6a), the four tags resolved over the fixture
# ---- (ac6b), and the join printed unarmed with the playbook kit's unit reader moved away (ac6c). The failing
# ---- cases, owed at the close and not observed by the pass that wrote this: only explicit row caps bounded
# ---- (ac2), the table read without its exactly-one rule (ac3a, ac3b), `shapes` read by no check (ac4a), and
# ---- the tag graded by its shape alone (ac6a). WHAT IT DOES NOT CHECK: a twin entry's `of`, a `merge` value,
# ---- a stage row's own `kind`, a judge file's content, or a scorer join with no workflows kit.
build_fixture; _rc31=$?
_tr31=$FX; [[ $FXK == */* ]] && _tr31=$FX/${FXK%/*}
A31=$("$PY" -B -c 'import json, os, pathlib, re, shutil, subprocess, sys
fx, kit, tool_root, src = (pathlib.Path(a).resolve() for a in sys.argv[1:5])
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k != "GOV_DEFAULT_BRANCH"}
def git(*a):
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@fx", "-C", str(fx), *a], env=env,
                          capture_output=True, text=True).returncode
def run(cwd, *a):
    p = subprocess.run([sys.executable, "-B", *a], cwd=str(cwd), env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, p.stdout
def check(*extra):
    rc, out = run(kit, "check_roles.py", "--root", str(fx), *extra)
    return rc, out, [ln for ln in out.splitlines() if ": R9 — " in ln]
homes = {}
for home in ("policy", "playbook"):
    homes[home] = tool_root / home
    shutil.copytree(src / home, homes[home], dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__"))
for home, name in (("workflows", "replay_scorer.py"),):
    (tool_root / home).mkdir(exist_ok=True)
    shutil.copy(src / home / name, tool_root / home / name)
(fx / "fx-cases.json").write_text("[]\n", encoding="utf-8")
(fx / "fx-labels.json").write_text("{}\n", encoding="utf-8")
(fx / ".governance").mkdir(exist_ok=True)
(fx / ".governance" / "policy.toml").write_text("runtime.agents-in-flight = 6\n", encoding="utf-8")
ok = git("symbolic-ref", "HEAD", "refs/heads/main") == 0 and git("add", "-A") == 0 \
    and git("commit", "-q", "--allow-empty", "-m", "limit 6") == 0
table, role = kit / "workflows.toml", kit / "agents" / "gov-builder.agent.md"
held, role_held = table.read_text(encoding="utf-8"), role.read_text(encoding="utf-8")
rc, out, r9 = check("--write")
print("ac6b %d" % int(ok and rc == 0 and not r9 and "4 unit tag(s) resolved" in out))
table.write_text(held.replace("kind = \"panel\"\nfan = 5\ncap = 5", "kind = \"panel\"\nfan = 5\ncap = 9", 1), encoding="utf-8")
rc, out, r9 = check()
print("ac2 %d" % int(rc == 1 and len(r9) == 1 and all(s in r9[0] for s in ("panel", "9", "runtime.agents-in-flight"))))
EXP = ("[workflow.experiment]\ncases = \"fx-cases.json\"\nvariants = [\"base\", \"house-index\"]\nfan = 4\n%s"
       "reruns = { \"base.medium\" = 3, \"house-index.medium\" = 3%s }\n\n")
def plant(names, extra=""):
    text = held.replace("roles = [\"gov-reuse-scout\"]\nkind = \"single\"",
                        "roles = [\"gov-reuse-scout\"]\nkind = \"experiment\"", 1)
    at = text.index("[[workflow]]", text.index("name = \"reuse\""))
    table.write_text(text[:at] + EXP % (names, extra) + text[at:], encoding="utf-8")
    return check("--write")
SCORER, JUDGE = "scorer = \"scouted-seam\"\n", "judge = \"fx-labels.json\"\n"
for case, names, extra, needle in (("ac3a", SCORER + JUDGE, "", "both scorer and judge"),
                                   ("ac3b", "", "", "neither scorer nor judge"),
                                   ("ac3c", SCORER, ", \"ghost.medium\" = 1", "ghost.medium")):
    rc, out, r9 = plant(names, extra)
    print("%s %d" % (case, int(rc == 1 and len(r9) == 1 and needle in r9[0])))
rc, out, r9 = plant(SCORER)
print("ac3d %d" % int(rc == 0 and not r9 and "no scorer factory answers" not in out))
table.write_text(held, encoding="utf-8")
check("--write")
role.write_text(role_held.replace("shapes: per-unit", "shapes: single", 1), encoding="utf-8")
rc, out, r9 = check()
print("ac4a %d" % int(rc == 1 and len(r9) == 1 and all(s in r9[0] for s in ("per-unit", "build.builder", "spec-write.builder"))))
role.write_text(role_held, encoding="utf-8")
rc, _out = run(fx, str(kit / "render_agents.py"), "--write")
index = json.loads((fx / ".claude" / "roles.json").read_text(encoding="utf-8")).get("roles", {})
declared = {}
for path in (kit / "agents").glob("*.agent.md"):
    head = path.read_text(encoding="utf-8").split("\n---", 1)[0]
    m = re.search(r"(?m)^shapes: *(.*?)\r?$", head)
    declared[path.name[:-len(".agent.md")]] = [s.strip() for s in m.group(1).split(",")] if m else []
print("ac4b %d" % int(rc == 0 and len(declared) > 1 and any(declared.values())
                      and {s: r.get("shapes") for s, r in index.items()} == declared))
table.write_text(held.replace("orientation = \"unit.orient.verifier-cold\"\nenforced-by = [\"agent-cap.js spawn guard\"]",
                              "orientation = \"unit.orient.nothing\"\nenforced-by = [\"agent-cap.js spawn guard\"]", 1),
                 encoding="utf-8")
rc, out, r9 = check()
print("ac6a %d" % int(rc == 1 and len(r9) == 1 and "unit.orient.nothing" in r9[0] and "no declared unit" in r9[0]))
table.write_text(held, encoding="utf-8")
reader = homes["playbook"].joinpath("instruction_units.py")
reader.rename(reader.with_suffix(".away"))
rc, out, r9 = check()
reader.with_suffix(".away").rename(reader)
print("ac6c %d" % int(rc == 0 and not r9 and "the unit join is unarmed" in out and "units unarmed" in out))
' "$FX" "$FX/$FXK" "$_tr31" "$HERE/.." 2>&1)
A31=${A31//$'\r'/}
check_arm "arm 31 over the fixture the four orientation and checklist tags resolve and no R9 line prints" \
   "$([ "$_rc31" = 0 ] && [[ $A31 == *'ac6b 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 the panel kind row capping 9 over a committed limit of 6 is one R9 line naming panel and the limit" \
   "$([[ $A31 == *'ac2 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 an experiment naming both scorer and judge is one R9 line" "$([[ $A31 == *'ac3a 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 ...naming neither is one R9 line" "$([[ $A31 == *'ac3b 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 ...a reruns key ghost.medium is one R9 line" "$([[ $A31 == *'ac3c 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 ...the scouted-seam scorer with every variant keyed exits 0" "$([[ $A31 == *'ac3d 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 gov-builder at shapes single under per-unit stages is one R9 line naming both stages" \
   "$([[ $A31 == *'ac4a 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 the rendered role index lists each role's shapes as its file declares them" \
   "$([[ $A31 == *'ac4b 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 an orientation naming no unit is one R9 line naming the tag" "$([[ $A31 == *'ac6a 1'* ]] && echo 1 || echo 0)"
check_arm "arm 31 with no unit reader the join prints unarmed and grades no tag" "$([[ $A31 == *'ac6c 1'* ]] && echo 1 || echo 0)"
[ "$A31" = $'ac6b 1\nac2 1\nac3a 1\nac3b 1\nac3c 1\nac3d 1\nac4a 1\nac4b 1\nac6a 1\nac6c 1' ] || printf '    %s\n' "${A31//$'\n'/$'\n'    }"

# ---- arm 32 (TOOL-dBoundRoles-15 AC1 AC2 AC3 AC7): the single carry and the budget over the whole static
# ---- block. The fixture gains the policy kit at the home `policy`, committed on `main` as arm 29 commits it,
# ---- and the playbook kit's document registry beside its layer register, so a block renders ranked. Under a
# ---- committed `instructions.task-charter = "always"` the direct render of gov-researcher exits 1 naming the
# ---- key, the value and the role, writing nothing (ac1); unset, its task holds no `### Charter rules` while its
# ---- agent type holds one (ac2a), a `--stand-in` render under the owner's waiver row holds none (ac2b) and
# ---- under `always` refuses naming the charter file (ac2c), and gov-session, an `agent: false` role rendered in
# ---- process with its reads cut to the families a roles-kit fixture answers, does both (ac2d). With the
# ---- policy kit moved away the render exits 0 with the note naming the key and `when-not-static` (ac7), and
# ---- a practice of 1100 bytes, or one byte past gov-reuse-scout's headroom where that is larger, cited by its
# ---- `rules` is one R5 line naming the role and its budget (ac3a), exit 0 with the rule taken out (ac3b). The
# ---- failing cases, owed at the close and not observed by the pass that wrote this: the key ignored, so
# ---- `always` renders (ac1, ac2c, ac2d); a stand-in read as `inline`, its task carrying the charter (ac2b); an
# ---- absent policy kit read as `always` (ac7); and R5 measuring the base body alone (ac3a). WHAT IT DOES NOT
# ---- CHECK: the `inline` kind, which no route derives, a reader exit 2, or the `warn` mode's BUDGET WARN line.
build_fixture; _rc32=$?
_pk=policy; [[ $FXK == */* ]] && _pk=${FXK%/*}/policy
mkdir -p "$FX/$_pk" && cp -R "$HERE/../policy"/. "$FX/$_pk"/ || _rc32=2
cp "$LAYERS_SRC/documents.toml" "$FX/$FXP"/ || _rc32=2
A32=$("$PY" -B -c 'import os, pathlib, re, shutil, subprocess, sys
fx, kit, pk, mr, ch = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve(), *sys.argv[3:6]
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k != "GOV_DEFAULT_BRANCH"}
def git(*a):
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@fx", "-C", str(fx), *a], env=env,
                          capture_output=True, text=True).returncode
def commit(*lines):
    (fx / ".governance").mkdir(exist_ok=True)
    (fx / ".governance" / "policy.toml").write_text("".join(ln + "\n" for ln in lines) or "# no key\n", encoding="utf-8")
    return git("add", "-A") == 0 and git("commit", "-q", "--allow-empty", "-m", "plant") == 0
def run(cwd, *a):
    p = subprocess.run([sys.executable, "-B", *a], cwd=str(cwd), env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, p.stdout, p.stderr
prompts = fx / mr / "builds" / "tFix" / "prompts"
prompts.mkdir(parents=True, exist_ok=True)
(fx / mr / "project").mkdir(parents=True, exist_ok=True)
made = lambda: sorted(p for p in prompts.iterdir())
render = ["handoff.py", "render", "--role", "gov-researcher", "--build", "tFix", "--unit", "TOOL-tFix-1",
          "--input", "question=q"]
always = "instructions.task-charter = \"always\""
ok = git("symbolic-ref", "HEAD", "refs/heads/main") == 0 and commit(always)
rc, out, err = run(kit, *render, "--stdout")
print("ac1 %d" % int(ok and rc == 1 and all(w in err for w in ("instructions.task-charter", "always", "gov-researcher"))
                     and not made()))
commit()
rc, out, err = run(kit, *render, "--stdout")
agent = (fx / ".claude" / "agents" / "gov-researcher.md").read_text(encoding="utf-8")
print("ac2a %d" % int(rc == 0 and "### Charter rules" not in out.split("\n## Task\n", 1)[-1]
                      and len(re.findall(r"(?m)^### Charter rules\r?$", agent)) == 1))
waiver = fx / mr / "project" / "role-stand-in-waiver.txt"
waiver.write_text("2026-11-22\towner a\tgov-researcher\ttFix\tthis tool exposes no sub-agent primitive\n", encoding="utf-8")
commit()
rc, out, err = run(kit, *render, "--stand-in")
held = made()
text = held[0].read_text(encoding="utf-8") if len(held) == 1 else "### Charter rules"
print("ac2b %d" % int(rc == 0 and "### Charter rules" not in text.split("\n## Task\n", 1)[-1]))
for p in held:
    p.unlink()
commit(always)
rc, out, err = run(kit, *render, "--stand-in")
print("ac2c %d" % int(rc == 1 and "instructions.task-charter" in err and ch in err and not made()))
session = "\n".join(["import pathlib, sys", "import roles_lib as lib, handoff",
    "fx, mr = pathlib.Path(sys.argv[1]), sys.argv[2]",
    "keys = dict(lib.load_roles(handoff.KIT_DIR)[\"gov-session\"][\"keys\"], reads=\"field.input.question\")",
    "try:",
    "    task = handoff.render_handoff(fx, mr, lib.resolve_charter_path(fx), \"gov-session\", keys, \"tFix\",",
    "                                  \"TOOL-tFix-1\", None, {\"question\": \"q\"}, None, [])[2]",
    "    print(\"rendered\", \"### Charter rules\" in task)",
    "except lib.RolesError as e:",
    "    print(\"refused\", e)"])
_rc, refused, _err = run(kit, "-c", session, str(fx), mr)
commit()
_rc, rendered, _err = run(kit, "-c", session, str(fx), mr)
print("ac2d %d" % int(rendered.strip() == "rendered False" and refused.startswith("refused")
                      and "gov-session" in refused and ch in refused))
waiver.unlink()
commit()
shutil.move(str(fx / pk), str(fx / "policy.away"))
rc, out, err = run(kit, *render, "--stdout")
print("ac7 %d" % int(rc == 0 and any("instructions.task-charter" in ln and "when-not-static" in ln for ln in err.splitlines())
                     and "### Charter rules" not in out.split("\n## Task\n", 1)[-1]))
sys.path.insert(0, str(kit))
import roles_lib as lib
role = kit / "agents" / "gov-reuse-scout.agent.md"
budget = lib.read_role_budget(lib.load_roles(kit)["gov-reuse-scout"])
charter, scout = (fx / ch).read_text(encoding="utf-8"), role.read_bytes()
cat = lib.parse_charter(charter, ch)
block = lib.render_static_block(kit, "gov-reuse-scout", lib.load_roles(kit)["gov-reuse-scout"], mr, cat, None, (), (),
                                lib.load_document_registry(kit), ch)
head = "- [bigrule] "
rule = head + "y" * (max(1100, budget - len(block.encode("utf-8")) + 1) - len(head)) + "\n"
at = charter.index("<!-- /one-line -->", charter.index("<!-- gov:practices -->"))
(fx / ch).write_text(charter[:at] + rule + charter[at:], encoding="utf-8")
role.write_bytes(re.sub(rb"(?m)^rules: ", b"rules: bigrule, ", scout))
rc, out, err = run(kit, "check_roles.py", "--root", str(fx))
r5 = [ln for ln in out.splitlines() if ": R5 — " in ln]
print("ac3a %d" % int(rc == 1 and len(r5) == 1 and "gov-reuse-scout" in r5[0] and "%d-byte ceiling" % budget in r5[0]))
(fx / ch).write_text(charter, encoding="utf-8")
role.write_bytes(scout)
rc, out, err = run(kit, "check_roles.py", "--root", str(fx))
print("ac3b %d" % int(rc == 0))
shutil.move(str(fx / "policy.away"), str(fx / pk))
' "$FX" "$FX/$FXK" "$_pk" "$MR" "$CH" 2>&1)
A32=${A32//$'\r'/}
check_arm "arm 32 under a committed instructions.task-charter always the direct render exits 1 naming the key, the value and the role" \
   "$([ "$_rc32" = 0 ] && [[ $A32 == *'ac1 1'* ]] && echo 1 || echo 0)"
check_arm "arm 32 unset, the task carries no charter rules and the agent type carries them once" \
   "$([[ $A32 == *'ac2a 1'* ]] && echo 1 || echo 0)"
check_arm "arm 32 a stand-in render under the owner's waiver row carries no charter in its task" \
   "$([[ $A32 == *'ac2b 1'* ]] && echo 1 || echo 0)"
check_arm "arm 32 ...and under always refuses naming the charter file, writing nothing" \
   "$([[ $A32 == *'ac2c 1'* ]] && echo 1 || echo 0)"
check_arm "arm 32 an agent: false role's render carries no charter, and under always refuses naming the charter file" \
   "$([[ $A32 == *'ac2d 1'* ]] && echo 1 || echo 0)"
check_arm "arm 32 with no policy kit the render exits 0 with the note naming the key and when-not-static" \
   "$([[ $A32 == *'ac7 1'* ]] && echo 1 || echo 0)"
check_arm "arm 32 a cited rule past gov-reuse-scout's headroom is one R5 line naming the role and its budget" \
   "$([[ $A32 == *'ac3a 1'* ]] && echo 1 || echo 0)"
check_arm "arm 32 ...and with the rule taken out the catalogue checks clean" "$([[ $A32 == *'ac3b 1'* ]] && echo 1 || echo 0)"
[ "$A32" = $'ac1 1\nac2a 1\nac2b 1\nac2c 1\nac2d 1\nac7 1\nac3a 1\nac3b 1' ] || printf '    %s\n' "${A32//$'\n'/$'\n'    }"

# ---- arm 33 (TOOL-dBoundRoles-17 AC1 AC3 AC4 AC6): the work order's `item=` and the return's `**Answers:**`
# ---- line, graded as R16 after the fixture's seed. The fixture gains the memory-tree kit's `legacy_ledger.py`
# ---- at the home `memory-tree`, where the library's resolver probes, and is committed, so a `--scaffold`
# ---- seeds `work-order-legacy.txt` from an empty population: its header and no row. A render with `--item
# ---- item.build.unit` writes that tag into its marker and `handoff.py check` passes it; `--item Item.Build`
# ---- exits 1 naming `--item` and writes nothing; no `--item` writes `item=-`. A `research` return naming the
# ---- first work order with a matching `**Answers:**` line checks clean; without the line it is one R16 line
# ---- naming the record, and with its `task-sha` one digit off one naming the mismatch. A work order planted
# ---- after the seed whose marker carries no `item=`, and one with no marker line, are each one R16 line. With
# ---- the home removed, one `R16 unarmed` note names the seed command and nothing is graded. The failing
# ---- cases, owed at the close and not observed by the pass that wrote this: a stale `task-sha` passing
# ---- because the line is graded on presence alone, and the legacy home read as a pattern so a planted
# ---- unmarked work order passes. WHAT IT DOES NOT CHECK: a return naming two work orders, or a seed over
# ---- an unborn HEAD, which leaves the home unarmed.
build_fixture
# TOOL-dBoundRoles-3 S1: an item's work order reads the item's declaration from the loop kit, so the fixture's
# definition declares `item.build.unit` for the role this arm renders, gov-researcher.
printf '\n[[item]]\ntag = "item.build.unit"\nstep = "step.build"\nactor = "role:gov-researcher"\nneeds = []\noutcomes = ["picked"]\nwitness = { class = "history", by = "the return" }\nowner = "tFix"\nroutes = { picked = "transition" }\n' >> "$FX/$FXL/loop.toml"
_mt=memory-tree; [[ $FXK == */* ]] && _mt=${FXK%/*}/memory-tree
A33P="$FX/$MR/builds/tFix/prompts"; A33B="$FX/$MR/builds/tFix/build"; A33R="$TMP_ROOT/a33.out"
A33H="$FX/$MR/project/work-order-legacy.txt"
_mtsrc="$HERE/../memory-tree"
mkdir -p "$FX/$_mt" "$A33P" "$A33B" && cp "$_mtsrc/legacy_ledger.py" "$FX/$_mt"/
(cd "$FX" && unset GIT_DIR GIT_WORK_TREE && git add -A && git -c user.name=fx -c user.email=fx@fx commit -qm fx) >/dev/null 2>&1
run_adopter --scaffold > "$A33R"
A33W=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --item item.build.unit --input "question=q" 2>/dev/null); A33W=${A33W%$'\r'}
_mk=$(grep -m1 '^<!-- gov:handoff ' "$FX/$A33W" 2>/dev/null)
(cd "$FX" && "$PY" -B "$KREL/handoff.py" check "$A33W") >/dev/null 2>&1; rc=$?
check_arm "arm 33 --item item.build.unit is the marker's item= and handoff.py check passes the work order" \
   "$([ -n "$A33W" ] && [[ $_mk == *' unit=TOOL-tFix-1 item=item.build.unit path='* ]] && [ "$rc" = 0 ] && echo 1 || echo 0)"
_ls=$(ls -A "$A33P")
(cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --item Item.Build --input "question=q") > /dev/null 2>"$TMP_ROOT/a33.err"; rc=$?
check_arm "arm 33 --item Item.Build exits 1 naming --item and writes nothing" \
   "$([ "$rc" = 1 ] && grep -qF -- '--item' "$TMP_ROOT/a33.err" && [ "$(ls -A "$A33P")" = "$_ls" ] && echo 1 || echo 0)"
_dash=$(cd "$FX" && "$PY" -B "$KREL/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --input "question=q" 2>/dev/null); _dash=${_dash%$'\r'}
check_arm "arm 33 with no --item the marker reads item=-" \
   "$([ -n "$_dash" ] && grep -q '^<!-- gov:handoff .* unit=TOOL-tFix-1 item=- path=' "$FX/$_dash" && echo 1 || echo 0)"
_sha=$(printf '%s\n' "$_mk" | sed -n 's/.* task-sha=\([0-9a-f]\{12\}\) -->.*/\1/p')
A33A="$A33B/2026-11-22-build-TOOL-tFix-1-findings.md"
_ans="**Answers:** $A33W task-sha=$_sha"
printf '**Serves:** research TOOL-tFix-1\n%s\n\n# findings\n\nAnswering ../prompts/%s.\n' "$_ans" "${A33W##*/}" > "$A33A"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A33R" 2>&1); rc=$?
check_arm "arm 33 after the seed's empty home a return with a matching Answers line checks clean, both graded" \
   "$([ "$rc" = 0 ] && [ -n "$_sha" ] && [ "$(grep -vc '^#' "$A33H" 2>/dev/null)" = 0 ] && ! grep -q ': R16 — ' "$A33R" \
      && grep -qF 'R16 2 handoff(s) and 1 return(s) graded, 0 legacy row(s)' "$A33R" && echo 1 || echo 0)"
[ "$rc" = 0 ] || sed 's/^/    /' "$A33R"
printf '**Serves:** research TOOL-tFix-1\n\n# findings\n\nAnswering ../prompts/%s.\n' "${A33W##*/}" > "$A33A"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A33R" 2>&1); rc=$?
check_arm "arm 33 the Answers line removed is one R16 line naming the record" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R16 — ' "$A33R")" = 1 ] && grep ': R16 — ' "$A33R" | grep -qF "${A33A##*/}" && echo 1 || echo 0)"
_bad=${_sha%?}; [ "${_sha: -1}" = 0 ] && _bad=${_bad}1 || _bad=${_bad}0
printf '**Serves:** research TOOL-tFix-1\n%s\n\n# findings\n\nAnswering ../prompts/%s.\n' "${_ans% *} task-sha=$_bad" "${A33W##*/}" > "$A33A"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A33R" 2>&1); rc=$?
check_arm "arm 33 a task-sha one digit off is one R16 line naming the mismatch" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R16 — ' "$A33R")" = 1 ] && grep ': R16 — ' "$A33R" | grep -F "$_bad" | grep -qF "$_sha" && echo 1 || echo 0)"
printf '**Serves:** research TOOL-tFix-1\n%s\n\n# findings\n\nAnswering ../prompts/%s.\n' "$_ans" "${A33W##*/}" > "$A33A"
A33U="$A33P/2026-11-22-prompt-TOOL-tFix-2-1-builder.md"
sed 's/ item=item\.build\.unit / /' "$FX/$A33W" > "$A33U"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A33R" 2>&1); rc=$?
check_arm "arm 33 a work order planted after the seed with no item= is one R16 line naming it" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R16 — ' "$A33R")" = 1 ] && grep ': R16 — ' "$A33R" | grep -qF "${A33U##*/}" && echo 1 || echo 0)"
printf '# no marker\n\n## Role\n\n## Task\n' > "$A33U"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A33R" 2>&1); rc=$?
check_arm "arm 33 ...and one with no marker line at all is refused the same way" \
   "$([ "$rc" = 1 ] && [ "$(grep -c ': R16 — ' "$A33R")" = 1 ] && grep ': R16 — ' "$A33R" | grep -qF "${A33U##*/}" && echo 1 || echo 0)"
rm -f "$A33U" "$A33H"
(cd "$FX" && "$PY" -B "$KREL/check_roles.py" > "$A33R" 2>&1); rc=$?
check_arm "arm 33 with no home one R16 unarmed note names the seed command and no handoff is graded" \
   "$([ "$rc" = 0 ] && [ "$(grep -c '^roles: note: R16 unarmed' "$A33R")" = 1 ] \
      && grep '^roles: note: R16 unarmed' "$A33R" | grep -qF 'legacy_ledger.py seed --home' \
      && grep -qF 'R16 unarmed, 0 handoff(s)' "$A33R" && echo 1 || echo 0)"

# ---- arm 34 (TOOL-dBoundRoles-13 AC1 AC4): the spec writer's handoff hands its spec as content, under a
# ---- fact line keyed `record:<path>@<sha12>` and classed `claimed`, with no line that is the path alone;
# ---- and `handoff.py facts` cuts the same spec, with its brief, to the same key. The keys are the fixture
# ---- kit's gov-spec-writer reads filtered to the `brief:` and `input:` families, as arm 22 filters them:
# ---- `task:` needs the kickoff checker and `card:` the session's card, which a roles-kit fixture lacks.
# ---- The spec is written with CRLF endings, so a key over the raw bytes differs from the verb's only
# ---- where the two cut differently. The failing case, observed at the close and not by the pass that
# ---- wrote this: `render_handoff` handing the spec's path string again, as before this unit.
build_fixture; _rc34=$?
A34=$("$PY" -B -c 'import json, pathlib, subprocess, sys
fx, kit, mr = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve(), sys.argv[3]
sys.path.insert(0, str(kit))
import handoff, roles_lib as lib
role = lib.load_roles(handoff.KIT_DIR)["gov-spec-writer"]["keys"]
keys = dict(role)
keys["reads"] = ", ".join(k for k in role["reads"].split(", ") if lib.parse_read_key(k)[0].startswith(("brief:", "input:")))
build = fx / mr / "builds" / "tFix"
(build / "prompts").mkdir(parents=True, exist_ok=True)
(build / "spec").mkdir(parents=True, exist_ok=True)
brief = build / "prompts" / "2026-11-22-prompt-TOOL-tFix-1-brief.md"
heads = ("Goal", "Items", "Acceptance", "Gates", "Non-goals")
brief.write_text("# Brief\n\n## The prompt\n\n> owner words\n\n## The brief\n\n" + "".join(
    "### %s\n\n%s text\n\n" % (h, h) for h in heads), encoding="utf-8")
spec = build / "spec" / "2026-10-25-spec-TOOL-tFix-1.md"
spec.write_bytes(b"# TOOL-tFix-1\r\n\r\nThe spec line one.\r\n")
srel, brel = spec.relative_to(fx).as_posix(), brief.relative_to(fx).as_posix()
task = handoff.render_handoff(fx, mr, lib.resolve_charter_path(fx), "gov-spec-writer", keys, "tFix",
                              "TOOL-tFix-1", None, {"spec": srel}, None)[2]
block = task.split("### input:spec\n\n", 1)[-1].split("\n### ", 1)[0]
fact = lib.FACT_RE.search(block)
print("render %d" % (fact is not None and fact.group("key").startswith("record:%s@" % srel)
                     and fact.group("class") == "claimed" and "The spec line one." in block.split("\n")
                     and srel not in [ln.strip() for ln in block.split("\n")]))
r = subprocess.run([sys.executable, "-B", str(kit / "handoff.py"), "facts", "--build", "tFix", "--unit", "TOOL-tFix-1",
                    "--input", "spec=" + srel, "--input", "prompt=" + brel], cwd=fx, capture_output=True, encoding="utf-8")
got = json.loads(r.stdout) if r.returncode == 0 else []
shaped = [f["name"] for f in got] == ["input:spec", "input:prompt"] and all(set(f) == {"name", "key", "class", "text"} for f in got)
print("facts %d" % (shaped and fact is not None and got[0]["key"] == fact.group("key")))
' "$FX" "$FX/$KREL" "$MR" 2>&1)
A34=${A34//$'\r'/}
check_arm "arm 34 the spec writer's handoff hands its spec as content under a claimed record: fact line" \
   "$([ "$_rc34" = 0 ] && [ "${A34%%$'\n'*}" = 'render 1' ] && echo 1 || echo 0)"
check_arm "arm 34 handoff.py facts cuts the same spec to the same key, beside its brief" \
   "$([ "${A34#*$'\n'}" = 'facts 1' ] && echo 1 || echo 0)"
[ "$A34" = $'render 1\nfacts 1' ] || printf '    %s\n' "${A34//$'\n'/$'\n'    }"

# ---- arm 35 (TOOL-dBoundRoles-3 AC1 AC2 AC3 AC4 AC6 AC7): the work order rendered per item. The fixture's loop
# ---- definition gains three rows: `item.build.unit` for gov-builder, whose `product` class takes the granted
# ---- paths, and `item.design.tspec` and `item.design.tnone` for gov-spec-writer, the second narrowed to `none`;
# ---- the fixture's gov-spec-writer reads `field.input.spec?` alone, since `task:` needs the kickoff checker and
# ---- `brief:` a brief record, which a roles-kit fixture lacks. Its conf routes the kit's own folder. The builder's
# ---- render through the CLI writes the five blocks inside `## Task`, its allowance the one granted path, its marker
# ---- `item=item.build.unit`, and `handoff.py check` passes it; the same render naming gov-spec-writer, granting no
# ---- path, granting one beside the memory root's README, naming an undeclared item, or with the loop kit taken
# ---- away each exits 1 naming the actor, the class and the flag, the path, the tag or the loop kit, and writes
# ---- nothing; the spec item's allowance is the build's `spec/` folder and the narrowed one reads `none`; the
# ---- work order without its `### witness` block, its marker re-hashed, fails `check` naming the block. The failing
# ---- cases, owed at the close and not observed by the pass that wrote this: `render_handoff` with its item
# ---- step cut out, which renders the work order with no block and passes every refusal, and `derive_allowance`
# ---- admitting every granted path. WHAT IT DOES NOT CHECK: a work order spawned, which the hooks kit's
# ---- agent-cap.test.sh binds to the session's card.
build_fixture; _rc35=$?
printf '\n[[item]]\ntag = "item.build.unit"\nstep = "step.build"\nactor = "role:gov-builder"\nneeds = []\noutcomes = ["committed", "diverged"]\nwitness = { class = "history", by = "the unit'"'"'s commit, its Pass: trailer naming the unit" }\nowner = "tFix"\nroutes = { committed = "transition", diverged = "transition" }\n' >> "$FX/$FXL/loop.toml"
for _t in tspec tnone; do
  _al=""; [ "$_t" = tnone ] && _al='allowance = "none"'$'\n'
  printf '\n[[item]]\ntag = "item.design.%s"\nstep = "step.design"\nactor = "role:gov-spec-writer"\nneeds = []\n%soutcomes = ["done"]\nwitness = { class = "history", by = "the spec" }\nowner = "tFix"\nroutes = { done = "transition" }\n' \
    "$_t" "$_al" >> "$FX/$FXL/loop.toml"
done
sed 's/^reads: .*/reads: field.input.spec?/' "$FX/$FXK/agents/gov-spec-writer.agent.md" > "$TMP_ROOT/a35.role" \
  && cp "$TMP_ROOT/a35.role" "$FX/$FXK/agents/gov-spec-writer.agent.md"
printf 'ROUTED_PATHS="%s/"\n' "$FXK" >> "$FX/.memory-tree.conf"
A35P="$FX/$MR/builds/tFix/prompts"; A35S="$MR/builds/tFix/spec/2026-11-22-spec-TOOL-tFix-1.md"; A35E="$TMP_ROOT/a35.err"
mkdir -p "$A35P" "$FX/$MR/builds/tFix/spec" && printf '# TOOL-tFix-1\n\nThe spec line one.\n' > "$FX/$A35S"
render35() { (cd "$FX" && "$PY" -B "$FXK/handoff.py" render --build tFix --unit TOOL-tFix-1 "$@" 2>"$A35E"); }
A35W=$(render35 --role gov-builder --item item.build.unit --allowance "$FXK/handoff.py" --input "spec=$A35S"); _rc=$?
A35W=${A35W%$'\r'}
A35=$("$PY" -B -c 'import pathlib, re, sys
text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
task = text[text.index("\n## Task\n"):]
heads = ["### item", "### inputs", "### allowance", "### return", "### witness"]
at = [task.find("\n%s\n" % h) for h in heads]
print("blocks %d" % (all(a > 0 for a in at) and at == sorted(at)))
print("allow %s" % task.split("\n### allowance\n\n", 1)[-1].split("\n\n", 1)[0].replace("\n", "|"))
print("item %d" % bool(re.search(r"^<!-- gov:handoff .* item=item\.build\.unit path=", text, re.M)))
' "$FX/$A35W" 2>&1); A35=${A35//$'\r'/}
(cd "$FX" && "$PY" -B "$FXK/handoff.py" check "$A35W") >/dev/null 2>&1; _ck=$?
check_arm "arm 35 AC1 the builder's item work order holds the five blocks in ## Task, its allowance the granted path, and check passes" \
   "$([ "$_rc35" = 0 ] && [ "$_rc" = 0 ] && [ "$_ck" = 0 ] && [ "$A35" = "blocks 1"$'\n'"allow - $FXK/handoff.py"$'\n'"item 1" ] && echo 1 || echo 0)"
[ "$_rc" = 0 ] && [ "$_ck" = 0 ] || { printf '    exit %s check %s\n' "$_rc" "$_ck"; sed 's/^/    /' "$A35E"; }
[ "$A35" = "blocks 1"$'\n'"allow - $FXK/handoff.py"$'\n'"item 1" ] || printf '    %s\n' "${A35//$'\n'/$'\n'    }"
_ls=$(ls -A "$A35P")
check_refused35() { # name needle render-args...: exit 1, the needle on stderr, nothing written
  local name=$1 needle=$2; shift 2
  render35 "$@" >/dev/null; local rc=$?
  check_arm "$name" "$([ "$rc" = 1 ] && grep -qF -- "$needle" "$A35E" && [ "$(ls -A "$A35P")" = "$_ls" ] && echo 1 || echo 0)"
  [ "$rc" = 1 ] && grep -qF -- "$needle" "$A35E" || { printf '    exit %s, want 1 naming %s\n' "$rc" "$needle"; sed 's/^/    /' "$A35E"; }
}
check_refused35 "arm 35 AC2 a render naming gov-spec-writer exits 1 naming the item's actor role:gov-builder and writes nothing" \
  'role:gov-builder' --role gov-spec-writer --item item.build.unit --allowance "$FXK/handoff.py" --input "spec=$A35S"
check_refused35 "arm 35 AC3 with no --allowance the product item exits 1 naming the class and the flag" \
  'product class, which takes only the paths the dispatch grants: pass --allowance' --role gov-builder --item item.build.unit --input "spec=$A35S"
check_refused35 "arm 35 AC4 a granted path under no ROUTED_PATHS entry exits 1 naming it" \
  "--allowance $MR/notes.md sits under no ROUTED_PATHS entry" --role gov-builder --item item.build.unit --allowance "$MR/notes.md" --input "spec=$A35S"
check_refused35 "arm 35 AC6 an item the loop does not declare exits 1 naming the tag" \
  'no [[item]] row declares item.build.nothing' --role gov-builder --item item.build.nothing --allowance "$FXK/handoff.py" --input "spec=$A35S"
for _t in tspec tnone; do
  _w=$(render35 --role gov-spec-writer --item "item.design.$_t" --input "spec=$A35S"); _w=${_w%$'\r'}
  _a=$([ -n "$_w" ] && "$PY" -B -c 'import pathlib, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
print(t.split("\n### allowance\n\n", 1)[-1].split("\n\n", 1)[0].replace("\n", "|"))' "$FX/$_w"); _a=${_a%$'\r'}
  [ "$_t" = tspec ] && _want="- $MR/builds/tFix/spec/" || _want=none
  check_arm "arm 35 AC3 the $_t item's allowance block reads $_want" "$([ "$_a" = "$_want" ] && echo 1 || { printf '    %s\n' "$_a" >&2; echo 0; })"
  rm -f "$FX/$_w"
done
A35K="$A35P/2026-11-22-prompt-TOOL-tFix-1-9-builder.md"
"$PY" -B -c 'import pathlib, re, sys, hashlib
src, dst, rel = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
text = src.read_text(encoding="utf-8").split("\n### witness\n", 1)[0] + "\n"
m = re.search(r"^<!-- gov:handoff .* path=(\S+) role-sha=\S+ task-sha=([0-9a-f]{12}) -->$", text, re.M)
sha = hashlib.sha256(text[text.index("\n## Task\n") + 1:].encode("utf-8")).hexdigest()[:12]
line = m.group(0).replace("path=" + m.group(1), "path=" + rel).replace("task-sha=" + m.group(2), "task-sha=" + sha)
dst.write_text(text.replace(m.group(0), line), encoding="utf-8", newline="\n")' "$FX/$A35W" "$A35K" "$MR/builds/tFix/prompts/${A35K##*/}"
_ck=$(cd "$FX" && "$PY" -B "$FXK/handoff.py" check "$MR/builds/tFix/prompts/${A35K##*/}" 2>&1); _rc=$?
check_arm "arm 35 AC7 the work order without its ### witness block, re-hashed, fails check naming the block" \
   "$([ "$_rc" = 1 ] && [[ $_ck == *"lacks its '### witness' block"* ]] && echo 1 || echo 0)"
rm -f "$A35K"; _ls=$(ls -A "$A35P")
mv "$FX/$FXL" "$TMP_ROOT/a35-loop"
check_refused35 "arm 35 AC6 with the loop kit taken away the render exits 1 naming no loop kit" \
  'no loop kit' --role gov-builder --item item.build.unit --allowance "$FXK/handoff.py" --input "spec=$A35S"
mv "$TMP_ROOT/a35-loop" "$FX/$FXL"

# ---- arm 36 (TOOL-dBoundRoles-38 AC1 AC2 AC4): handed content fenced, and every reader of a fact or marker line
# ---- skipping what a fence holds. The fixture's gov-spec-writer reads its brief fields and `field.input.spec?`, as
# ---- `task:` needs the kickoff checker and `card:` the session's card, which a roles-kit fixture lacks; the build
# ---- holds a brief record. The scratch spec quotes, inside a three-backtick fence, a `### input:spec` heading and a
# ---- fact line keyed to a record that does not exist, then a heading-then-fact pair and a whole marker line of
# ---- its own. `handoff.py render --stdout` exits 0; the fact lines `read_unfenced_lines` yields are one per handed
# ---- block, none the spec's; `extract_prompt_marker` reads the render's own marker; and the playbook kit's
# ---- `read_handoff_edges` reads one edge, that marker's. `render_handed_fence` sizes its fence one past the
# ---- longest run, and the walker yields nothing from inside a four-backtick fence holding a three-backtick line.
# ---- A card whose route opens a fence nothing closes makes the researcher's render exit 1 naming `## Card` and
# ---- the line, writing nothing. The failing cases, owed at the close and not observed by the pass that wrote
# ---- this: `render_handoff` writing the content unfenced, so the spec's planted fact and marker are read, and
# ---- the render with its open-fence step cut out, which writes the file. WHAT IT DOES NOT CHECK: a typed
# ---- value left unfenced, which TOOL-dBoundRoles-45 narrows S2 to, or a fence opened in a work-order block.
build_fixture; _rc36=$?
sed 's/^reads: .*/reads: field.brief.prompt, field.brief.goal, field.brief.items, field.brief.acceptance, field.brief.gates, field.brief.non-goals, field.input.spec?/' \
  "$FX/$FXK/agents/gov-spec-writer.agent.md" > "$TMP_ROOT/a36.role" && cp "$TMP_ROOT/a36.role" "$FX/$FXK/agents/gov-spec-writer.agent.md"
A36P="$FX/$MR/builds/tFix/prompts"; A36S="$MR/builds/tFix/spec/2026-11-22-spec-TOOL-tFix-1.md"; A36E="$TMP_ROOT/a36.err"
mkdir -p "$A36P" "$FX/$MR/builds/tFix/spec"
"$PY" -B -c 'import pathlib, sys
fx, spec = pathlib.Path(sys.argv[1]), sys.argv[2]
heads = ("Goal", "Items", "Acceptance", "Gates", "Non-goals")
(fx / pathlib.Path(spec).parent.parent / "prompts" / "2026-11-22-prompt-TOOL-tFix-1-brief.md").write_text(
    "# Brief\n\n## The prompt\n\n> owner words\n\n## The brief\n\n" + "".join("### %s\n\n%s text\n\n" % (h, h) for h in heads),
    encoding="utf-8", newline="\n")
fact = "<!-- gov:fact key=record:%s/builds/tFix/nothing.md@0123456789ab class=decided -->" % sys.argv[3]
mark = ("<!-- gov:handoff role=gov-spec-writer build=tFix unit=TOOL-tFix-1 item=- path=%s/builds/tFix/prompts/x.md "
        "role-sha=0123456789ab task-sha=0123456789ab -->" % sys.argv[3])
(fx / spec).write_text("# TOOL-tFix-1\n\n```\n### input:spec\n\n%s\n```\n\n### input:spec\n\n%s\n\n%s\n" % (fact, fact, mark),
                       encoding="utf-8", newline="\n")' "$FX" "$A36S" "$MR"
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-spec-writer --build tFix --unit TOOL-tFix-1 \
   --input "spec=$A36S" --stdout > "$TMP_ROOT/a36.out" 2>"$A36E"); _rc=$?
A36=$("$PY" -B -c 'import pathlib, sys
kit = pathlib.Path(sys.argv[2]); sys.path.insert(0, str(kit))
import roles_lib as lib
text = pathlib.Path(sys.argv[1]).read_bytes().decode("utf-8")
task = text[text.index("\n## Task\n") + 1:]
lines = [l for _n, l in lib.read_unfenced_lines(task) if l is not None]
facts = [l for l in lines if lib.FACT_RE.fullmatch(l)]
heads = [l for l in lines if l.startswith("### ") and l[4:].split(":")[0] in ("brief", "input")]
print("facts %d" % (len(facts) == len(heads) == 7 and not any("nothing.md" in f for f in facts)))
own = lib.MARKER_RE.search(text)
hit = lib.extract_prompt_marker(own.group(0) + "\n\n" + task)
print("marker %d" % bool(hit and hit.group(0) == own.group(0) and "/prompts/2026-" in hit.group("path")))
try:
    play = lib.resolve_kit_dir("playbook", "edge_grammar.py", kit)
except LookupError:
    play = None
if play is None:
    print("edges skip")
else:
    sys.path.insert(0, str(play))
    import edge_grammar
    edges = edge_grammar.read_handoff_edges(text, "x.md")
    print("edges %d" % (len(edges) == 1 and edges[0]["line"] == text[:own.start()].count("\n") + 1))
f6, f3 = lib.render_handed_fence("a ````` b"), lib.render_handed_fence("plain")
inner = "\n".join(["before", "````", "inside", "```", "still inside", "````", "after"])
print("fence %d" % (f6 == "``````\na ````` b\n``````" and f3 == "```\nplain\n```"
                    and [l for _n, l in lib.read_unfenced_lines(inner)] == ["before", "after"]))
' "$TMP_ROOT/a36.out" "$HERE" 2>&1); A36=${A36//$'\r'/}
check_arm "arm 36 AC1 the spec writer's render handing a spec that quotes facts and a marker exits 0" \
   "$([ "$_rc36" = 0 ] && [ "$_rc" = 0 ] && echo 1 || { sed 's/^/    /' "$A36E" >&2; echo 0; })"
check_arm "arm 36 AC1 ...the unfenced fact lines are one per handed block, none of them the spec's" \
   "$([[ $A36 == *"facts 1"* ]] && echo 1 || echo 0)"
check_arm "arm 36 AC1 ...extract_prompt_marker reads the render's own marker" "$([[ $A36 == *"marker 1"* ]] && echo 1 || echo 0)"
if [[ $A36 == *"edges skip"* ]]; then
  echo "SKIP arm 36 edges — no playbook kit holding edge_grammar.py was found from $KREL"; FLOOR_ASSERTIONS=$((FLOOR_ASSERTIONS-1))
else
  check_arm "arm 36 AC1 ...read_handoff_edges reads one edge, the render's own marker's" "$([[ $A36 == *"edges 1"* ]] && echo 1 || echo 0)"
fi
check_arm "arm 36 AC2 render_handed_fence runs one past the longest backtick run, and a shorter run closes no fence" \
   "$([[ $A36 == *"fence 1"* ]] && echo 1 || echo 0)"
[[ $A36 == *"facts 1"*"marker 1"* && $A36 == *"fence 1"* ]] || printf '    %s\n' "${A36//$'\n'/$'\n'    }"
mkdir -p "$FX/.claude" && printf '%s\n' '[.claude/orientation-card.md · Level 1 · the card]' '## route' '- build: tFix' '````' \
  '- unit: TOOL-tFix-1' '[/.claude/orientation-card.md]' > "$FX/.claude/orientation-card.md"
_ls=$(ls -A "$A36P")
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --input "question=which mechanism fits" >/dev/null 2>"$A36E"); _rc=$?
check_arm "arm 36 AC4 a card route opening a fence nothing closes exits 1 naming ## Card and the line, writing nothing" \
   "$([ "$_rc" = 1 ] && grep -qF -- '## Card — a fence opened at line' "$A36E" && [ "$(ls -A "$A36P")" = "$_ls" ] && echo 1 || echo 0)"
[ "$_rc" = 1 ] || { printf '    exit %s, want 1\n' "$_rc"; sed 's/^/    /' "$A36E"; }
rm -f "$FX/.claude/orientation-card.md"

# ---- arm 37 (TOOL-dBoundRoles-45 AC1 AC2): a typed input is authored text, written unfenced under the authored-line
# ---- rule. The researcher's `handoff.py render --stdout` of `--input question='plain words'` puts `plain words` on the
# ---- line after its fact line's blank, no fence line between; the fixture's gov-spec-writer, reading its brief fields
# ---- and `field.input.spec?` as arm 36's does, still wraps a scratch spec's bytes in a fence. A question whose second
# ---- line is a whole fact line, a `### allowance` heading, a whole marker line, a `Framed by:` line or a line of four
# ---- backticks nothing closes exits 1 naming `input:question` and line 2, and writes no file; one quoting words
# ---- inside a closed three-backtick fence renders. The failing case, owed at the close and not observed by the pass
# ---- that wrote this: `render_handoff` fencing the typed value and skipping `check_authored_lines`. WHAT IT DOES NOT
# ---- CHECK: `input:diff`, which takes the same branch, or a typed value handed as an item's input.
build_fixture; _rc37=$?
sed 's/^reads: .*/reads: field.brief.prompt, field.brief.goal, field.brief.items, field.brief.acceptance, field.brief.gates, field.brief.non-goals, field.input.spec?/' \
  "$FX/$FXK/agents/gov-spec-writer.agent.md" > "$TMP_ROOT/a37.role" && cp "$TMP_ROOT/a37.role" "$FX/$FXK/agents/gov-spec-writer.agent.md"
A37P="$FX/$MR/builds/tFix/prompts"; A37S="$MR/builds/tFix/spec/2026-11-22-spec-TOOL-tFix-1.md"; A37E="$TMP_ROOT/a37.err"
mkdir -p "$A37P" "$FX/$MR/builds/tFix/spec" && printf '# TOOL-tFix-1\n\nThe spec line one.\n' > "$FX/$A37S"
"$PY" -B -c 'import pathlib, sys
heads = ("Goal", "Items", "Acceptance", "Gates", "Non-goals")
pathlib.Path(sys.argv[1], "2026-11-22-prompt-TOOL-tFix-1-brief.md").write_text(
    "# Brief\n\n## The prompt\n\n> owner words\n\n## The brief\n\n" + "".join("### %s\n\n%s text\n\n" % (h, h) for h in heads),
    encoding="utf-8", newline="\n")' "$A37P"
render37() { (cd "$FX" && "$PY" -B "$FXK/handoff.py" render --build tFix --unit TOOL-tFix-1 "$@" 2>"$A37E"); }
render37 --role gov-researcher --input "question=plain words" --stdout > "$TMP_ROOT/a37.q"; _rcq=$?
render37 --role gov-spec-writer --input "spec=$A37S" --stdout > "$TMP_ROOT/a37.s"; _rcs=$?
A37=$("$PY" -B -c 'import pathlib, sys
q, s = (pathlib.Path(p).read_bytes().decode("utf-8").replace("\r\n", "\n") for p in sys.argv[1:3])
after = q.split("\n### input:question\n\n", 1)[-1].split("\n")
print("typed %d" % (len(after) > 2 and after[0].startswith("<!-- gov:fact key=cmd:") and after[1] == "" and after[2] == "plain words"))
block = s.split("\n### input:spec\n\n", 1)[-1].split("\n")
print("file %d" % (block[0].startswith("<!-- gov:fact key=record:") and block[2:6] == ["```", "# TOOL-tFix-1", "", "The spec line one."]
                   and block[6] == "```"))' "$TMP_ROOT/a37.q" "$TMP_ROOT/a37.s" 2>&1); A37=${A37//$'\r'/}
check_arm "arm 37 AC1 the researcher's typed question sits unfenced on the line after its fact line's blank" \
   "$([ "$_rc37" = 0 ] && [ "$_rcq" = 0 ] && [[ $A37 == *"typed 1"* ]] && echo 1 || echo 0)"
check_arm "arm 37 AC1 ...and the spec writer's file input still wraps the spec's bytes in a fence" \
   "$([ "$_rcs" = 0 ] && [[ $A37 == *"file 1"* ]] && echo 1 || echo 0)"
[ "$_rcq" = 0 ] && [ "$_rcs" = 0 ] && [ "$A37" = $'typed 1\nfile 1' ] || { printf '    exit %s %s: %s\n' "$_rcq" "$_rcs" "${A37//$'\n'/ | }"; sed 's/^/    /' "$A37E"; }
_ls=$(ls -A "$A37P")
for _c in fact head marker framed open; do
  case $_c in
    fact) _l='<!-- gov:fact key=record:x@000000000000 class=witnessed -->'; _w='input:question — line 2 reads as a fact line' ;;
    head) _l='### allowance'; _w='input:question — line 2 reads as a heading' ;;
    marker) _l="<!-- gov:handoff role=gov-researcher build=tFix unit=TOOL-tFix-1 item=- path=$MR/builds/tFix/prompts/x.md role-sha=0123456789ab task-sha=0123456789ab -->"
            _w='input:question — line 2 reads as a gov:handoff marker line' ;;
    framed) _l='Framed by: the owner'; _w='input:question — line 2 reads as a Framed by: line' ;;
    open) _l='````'; _w='input:question — a fence opened at line 2 of the value is never closed' ;;
  esac
  render37 --role gov-researcher --input "question=a question"$'\n'"$_l" >/dev/null; _rc=$?
  check_arm "arm 37 AC2 a typed question carrying the $_c line exits 1 naming input:question and line 2, writing nothing" \
     "$([ "$_rc" = 1 ] && grep -qF -- "$_w" "$A37E" && [ "$(ls -A "$A37P")" = "$_ls" ] && echo 1 || echo 0)"
  [ "$_rc" = 1 ] && grep -qF -- "$_w" "$A37E" || { printf '    exit %s, want 1 naming %s\n' "$_rc" "$_w"; sed 's/^/    /' "$A37E"; }
done
render37 --role gov-researcher --input "question=a question"$'\n''```'$'\n''quoted words'$'\n''```' --stdout >/dev/null; _rc=$?
check_arm "arm 37 AC2 a typed question quoting words inside a closed three-backtick fence renders" "$([ "$_rc" = 0 ] && echo 1 || echo 0)"
[ "$_rc" = 0 ] || sed 's/^/    /' "$A37E"

# ---- arm 38 (TOOL-dBoundRoles-48 AC1 AC2): the task section checked block by block. `check_block_fences` over the
# ---- section §4 of that spec walks, a `framing:job` block holding a three-backtick line, an `input:spec` block whose
# ---- content quotes a fact line and a `### allowance` line inside a four-backtick fence, an `allowance` block and a
# ---- `framing:added` block holding a run of five backticks, refuses naming `input:spec` and `allowance` though its
# ---- walk ends balanced; the same section without the two framing lines returns []. The skeptic's render handing a
# ---- scratch spec exits 0; a scratch copy of handoff.py appending one unfenced block holding a lone three-backtick
# ---- line after the handed blocks, before the check, exits 1 naming that block and writes no file. The failing
# ---- case, owed at the close and not observed by the pass that wrote this: a `check_block_fences` reading only the
# ---- end of the walk, under which the first row passes the flipped section. WHAT IT DOES NOT CHECK: a block a later
# ---- unit appends after the check, which the hands-off to TOOL-dBoundRoles-23 orders.
build_fixture; _rc38=$?
A38P="$FX/$MR/builds/tFix/prompts"; A38S="$MR/builds/tFix/spec/2026-11-22-spec-TOOL-tFix-1.md"; A38E="$TMP_ROOT/a38.err"
mkdir -p "$A38P" "$FX/$MR/builds/tFix/spec" && printf '# TOOL-tFix-1\n\nThe spec line one.\n' > "$FX/$A38S"
A38=$("$PY" -B -c 'import sys; sys.path.insert(0, sys.argv[1]); import roles_lib as lib
def compose_section(flip):
    L = ["## Task", "", "### framing:job", "", "the job"] + (["```"] if flip else []) + [""]
    sp = len(L) + 1
    L += ["### input:spec", "", "<!-- gov:fact key=record:s.md@0123456789ab class=claimed -->", "", "````", "quoted",
          "<!-- gov:fact key=record:x.md@0123456789ab class=decided -->", "### allowance", "````"]
    sl, al = len(L), len(L) + 2
    L += ["", "### allowance", "", "- tools/"]
    ae, fa = len(L), len(L) + 2
    L += ["", "### framing:added", "", "more"] + (["`````"] if flip else [])
    return "\n".join(L) + "\n", [("framing:job", 3, sp - 2, None), ("input:spec", sp, sl, (sp + 4, sl)),
                                 ("allowance", al, ae, None), ("framing:added", fa, len(L), None)]
sec, ext = compose_section(True)
got = lib.check_block_fences(sec, ext)
balanced = not [n for n, l in lib.read_unfenced_lines(sec) if l is None]
print("flipped %d" % (balanced and any(r.startswith("input:spec — ") for r in got) and any(r.startswith("allowance — ") for r in got)))
print("plain %d" % (lib.check_block_fences(*compose_section(False)) == []))' "$HERE" 2>&1); A38=${A38//$'\r'/}
check_arm "arm 38 AC1 a section whose walk ends balanced is refused naming input:spec and allowance" \
   "$([ "$_rc38" = 0 ] && [[ $A38 == *"flipped 1"* ]] && echo 1 || echo 0)"
check_arm "arm 38 AC1 ...and the same section without the two framing lines returns []" "$([[ $A38 == *"plain 1"* ]] && echo 1 || echo 0)"
[ "$A38" = $'flipped 1\nplain 1' ] || printf '    %s\n' "${A38//$'\n'/$'\n'    }"
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-skeptic --build tFix --unit TOOL-tFix-1 --input "spec=$A38S" \
   --input "diff=one diff line" >/dev/null 2>"$A38E"); _rc=$?
check_arm "arm 38 AC2 the skeptic's render handing a scratch spec exits 0" "$([ "$_rc" = 0 ] && echo 1 || echo 0)"
[ "$_rc" = 0 ] || sed 's/^/    /' "$A38E"
"$PY" -B -c 'import pathlib, sys
kit = pathlib.Path(sys.argv[1]); src = (kit / "handoff.py").read_text(encoding="utf-8")
anchor = "    if declaration is not None:\n        # TOOL-dBoundRoles-3 S2"
(kit / "handoff_a38.py").write_text(src.replace(anchor, sys.argv[2] + "\n" + anchor, 1), encoding="utf-8", newline="\n")' \
  "$FX/$FXK" $'    blocks.append(("added", "### framing:added\\n\\n```", None, "### framing:added\\n\\n```"))'
_ls=$(ls -A "$A38P")
(cd "$FX" && "$PY" -B "$FXK/handoff_a38.py" render --role gov-skeptic --build tFix --unit TOOL-tFix-1 --input "spec=$A38S" \
   --input "diff=one diff line" >/dev/null 2>"$A38E"); _rc=$?
check_arm "arm 38 AC2 a handoff.py appending an unfenced block holding a lone fence line exits 1 naming it, writing nothing" \
   "$([ "$_rc" = 1 ] && grep -qF -- '### framing:added — a fence opened at line' "$A38E" && [ "$(ls -A "$A38P")" = "$_ls" ] && echo 1 || echo 0)"
[ "$_rc" = 1 ] || { printf '    exit %s, want 1\n' "$_rc"; sed 's/^/    /' "$A38E"; }
rm -f "$FX/$FXK/handoff_a38.py"

# ---- arm 39 (TOOL-dBoundRoles-24 AC1 AC2 AC4): every anchor the rendered task points at resolves to a fact the work
# ---- order hands. `check_anchors` over a scratch file holding one backticked `blob:` key names it as resolving to no
# ---- fact this work order hands, and returns [] with that key in the set; over a text holding the span `blob:nothing`
# ---- and, inside a fenced block, a `cmd:` example, it returns one line, marked malformed. The researcher's render of a
# ---- question carrying a backticked `record:` key the order does not hand exits 1 naming the anchor and writes no file,
# ---- and exits 0 with the anchor removed; the skeptic's render whose typed diff anchors the key of the spec it is
# ---- handed exits 0. The failing case, owed at the close and not observed by the pass that wrote this: the
# ---- `check_anchors` call removed from `render_handoff`, under which the planted render exits 0 and writes its file.
# ---- WHAT IT DOES NOT CHECK: that the fact behind a resolving anchor says what the task claims of it, or a reference
# ---- without the key shape, which is prose.
build_fixture; _rc39=$?
A39P="$FX/$MR/builds/tFix/prompts"; A39S="$MR/builds/tFix/spec/2026-11-23-spec-TOOL-tFix-1.md"; A39E="$TMP_ROOT/a39.err"
mkdir -p "$A39P" "$FX/$MR/builds/tFix/spec" && printf '# TOOL-tFix-1\n\nThe spec line one.\n' > "$FX/$A39S"
printf 'See `blob:roles_lib.py@%s:1-4` for it.\n' 0123456789ab > "$TMP_ROOT/anchor-nothing.md"
A39=$("$PY" -B -c 'import pathlib, sys; sys.path.insert(0, sys.argv[1]); import roles_lib as lib
text = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8")
span = "blob:roles_lib.py@" + "0123456789ab:1-4"
got = lib.check_anchors(text, set())
print("nothing %d" % (len(got) == 1 and span in got[0] and got[0].endswith("resolves to no fact this work order hands")
                      and lib.check_anchors(text, {span}) == []))
got = lib.check_anchors("one `blob:nothing` here\n```\nthe `cmd:000000000000:000000000000` example\n```\n", set())
print("malformed %d" % (len(got) == 1 and "`blob:nothing`" in got[0] and "malformed" in got[0]))
print("key %s" % lib.derive_fact_key("record", sys.argv[4], (pathlib.Path(sys.argv[3]) / sys.argv[4]).read_bytes()))' \
  "$HERE" "$TMP_ROOT/anchor-nothing.md" "$FX" "$A39S" 2>&1); A39=${A39//$'\r'/}
check_arm "arm 39 AC1 an anchor to nothing is named as resolving to no handed fact, and [] once its key is handed" \
   "$([ "$_rc39" = 0 ] && [[ $A39 == *"nothing 1"* ]] && echo 1 || echo 0)"
check_arm "arm 39 AC4 a prefix-shaped span failing its form is one malformed line, and a fenced example is not graded" \
   "$([[ $A39 == *"malformed 1"* ]] && echo 1 || echo 0)"
[[ $A39 == *"nothing 1"*"malformed 1"* ]] || printf '    %s\n' "${A39//$'\n'/$'\n'    }"
_ls=$(ls -A "$A39P")
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --input 'question=which mechanism fits; see `record:memory/nowhere.md@0123456789ab`' >/dev/null 2>"$A39E"); _rc=$?
check_arm "arm 39 AC2 a question planting an anchor the order does not hand exits 1 naming it, writing nothing" \
   "$([ "$_rc" = 1 ] && grep -qF -- 'anchor `record:memory/nowhere.md@0123456789ab` — resolves to no fact' "$A39E" \
      && [ "$(ls -A "$A39P")" = "$_ls" ] && echo 1 || echo 0)"
[ "$_rc" = 1 ] || { printf '    exit %s, want 1\n' "$_rc"; sed 's/^/    /' "$A39E"; }
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-researcher --build tFix --unit TOOL-tFix-1 \
   --input 'question=which mechanism fits' --stdout >/dev/null 2>"$A39E"); _rc=$?
check_arm "arm 39 AC2 ...and the same render with the anchor removed exits 0" "$([ "$_rc" = 0 ] && echo 1 || echo 0)"
[ "$_rc" = 0 ] || sed 's/^/    /' "$A39E"
_key=$(printf '%s\n' "$A39" | sed -n 's/^key //p')
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-skeptic --build tFix --unit TOOL-tFix-1 --input "spec=$A39S" \
   --input "diff=the diff answers \`$_key\`" --stdout >/dev/null 2>"$A39E"); _rc=$?
check_arm "arm 39 AC2 ...and a typed diff anchoring the key of the spec the order hands renders" \
   "$([ "$_rc" = 0 ] && [[ $_key == record:* ]] && echo 1 || echo 0)"
[ "$_rc" = 0 ] || { printf '    key %s\n' "$_key"; sed 's/^/    /' "$A39E"; }

# ---- arm 40 (TOOL-dBoundRoles-41 AC1 AC2): the anchor check grades the text a work order authors, never the content
# ---- it hands. A scratch spec whose prose, outside any fence, quotes the backticked spans `cmd:<command>` and a
# ---- well-formed example key: the builder's render handing it as `input:spec` exits 0 and writes its prompt file;
# ---- the same render under a card whose route quotes the same two spans, its card block handed unfenced at the
# ---- head of the task, exits 0; the orienter's render handing the spec as `input:prompt` beside a typed question
# ---- holding a backticked `record:` anchor the order does not hand exits non-zero naming it and writes no file. The
# ---- failing cases, owed at the close and not observed by the pass that wrote this: `render_handoff` passing the
# ---- whole section to `check_anchors`, under which the card render exits 1 naming both spans, and a graded text
# ---- dropping the typed value, under which the orienter's render exits 0. The spec's own spans sit inside its
# ---- handed fence (TOOL-dBoundRoles-38), which the check's fence walk skips with or without the graded text. WHAT
# ---- IT DOES NOT CHECK: a practices block, which a fixture with no playbook kit never renders, an item's excerpts,
# ---- and the marker's task-sha, which the pass compared against a render before the change.
build_fixture; _rc40=$?
A40P="$FX/$MR/builds/tFix/prompts"; A40S="$MR/builds/tFix/spec/2026-11-23-spec-TOOL-tFix-1.md"; A40E="$TMP_ROOT/a40.err"
mkdir -p "$A40P" "$FX/$MR/builds/tFix/spec" \
  && printf '# TOOL-tFix-1\n\nThe spec quotes `cmd:<command>` and `blob:roles_lib.py@%s:1-4` in its prose.\n' 0123456789ab > "$FX/$A40S"
_ls=$(ls -A "$A40P")
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-builder --build tFix --unit TOOL-tFix-1 --input "spec=$A40S" \
   >/dev/null 2>"$A40E"); _rc=$?
check_arm "arm 40 AC1 the builder's render handing a spec quoting the key grammar in its prose exits 0, writing its file" \
   "$([ "$_rc40" = 0 ] && [ "$_rc" = 0 ] && [ -z "$_ls" ] && [ -n "$(ls -A "$A40P")" ] && echo 1 || echo 0)"
[ "$_rc" = 0 ] || sed 's/^/    /' "$A40E"
mkdir -p "$FX/.claude" && printf '[.claude/orientation-card.md · Level 1 · the card]\n## route\n- build: tFix\n- quotes `cmd:<command>` and `blob:roles_lib.py@%s:1-4`\n[/.claude/orientation-card.md]\n' \
  0123456789ab > "$FX/.claude/orientation-card.md"
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-builder --build tFix --unit TOOL-tFix-1 --input "spec=$A40S" \
   --stdout >/dev/null 2>"$A40E"); _rc=$?
check_arm "arm 40 AC1 ...and under a card whose route quotes both spans, its block handed at the task's head, exits 0" \
   "$([ "$_rc" = 0 ] && echo 1 || echo 0)"
[ "$_rc" = 0 ] || sed 's/^/    /' "$A40E"
rm -f "$FX/.claude/orientation-card.md"
_ls=$(ls -A "$A40P")
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-orienter --build tFix --unit TOOL-tFix-1 --input "prompt=$A40S" \
   --input 'question=which seam fits; see `record:memory/nowhere.md@0123456789ab`' >/dev/null 2>"$A40E"); _rc=$?
check_arm "arm 40 AC2 the orienter's typed question planting an anchor the order does not hand exits non-zero naming it" \
   "$([ "$_rc" != 0 ] && grep -qF -- 'anchor `record:memory/nowhere.md@0123456789ab` — resolves to no fact' "$A40E" \
      && [ "$(ls -A "$A40P")" = "$_ls" ] && echo 1 || echo 0)"
[ "$_rc" != 0 ] || { printf '    exit %s, want non-zero\n' "$_rc"; sed 's/^/    /' "$A40E"; }

# ---- arm 41 (TOOL-dBoundRoles-11 AC5): `handoff.py owner-question`, the shell door of `resolve_owner_question`, which
# ---- reads `run.on-owner-question` through `read_policy_setting`. The fixture gains a copy of the policy kit beside the
# ---- roles kit, as arm 29's does, and commits each plant's `.governance/policy.toml` on `main`, the landed revision
# ---- `policy.py get` reads in a clone with no remote. With no key a fork prints `resolve`; under each of the four
# ---- values a fork and an owner gate print the value, `best-effort-recorded` as `resolve`; a ratification, an
# ---- owner write and an attended fork print `owner` under every value; an unknown kind exits 2 naming it. The
# ---- failing case, owed at the close and not observed by the pass that wrote this: the reader answering the key's
# ---- value for a ratification, under which the owner row reds. WHAT IT DOES NOT CHECK: a refused policy read, or
# ---- no policy kit beside the roles kit, each a RolesError the door prints and exits 2 on.
build_fixture; _rc41=$?
_pk=policy; [[ $FXK == */* ]] && _pk=${FXK%/*}/policy
mkdir -p "$FX/$_pk" && cp -R "$HERE/../policy"/. "$FX/$_pk"/ || _rc41=2
A41=$("$PY" -B -c 'import os, pathlib, subprocess, sys
fx, kit = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k != "GOV_DEFAULT_BRANCH"}
def git(*a):
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@fx", "-C", str(fx), *a], env=env,
                          capture_output=True, text=True).returncode
def commit(*lines):
    (fx / ".governance").mkdir(exist_ok=True)
    (fx / ".governance" / "policy.toml").write_text("".join(ln + "\n" for ln in lines) or "# no key\n", encoding="utf-8")
    return git("add", "-A") == 0 and git("commit", "-q", "--allow-empty", "-m", "plant") == 0
def ask(*a):
    p = subprocess.run([sys.executable, "-B", "handoff.py", "owner-question", *a], cwd=str(kit), env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, p.stdout.strip(), p.stderr
ok = git("symbolic-ref", "HEAD", "refs/heads/main") == 0 and commit()
print("default %d" % int(ok and ask("--kind", "fork")[:2] == (0, "resolve") and ask("--kind", "owner-gate")[1] == "resolve"))
held, owner = [], []
for value, want in (("park-item", "park-item"), ("park-build", "park-build"), ("stop-run", "stop-run"),
                    ("best-effort-recorded", "resolve")):
    planted = commit("run.on-owner-question = \"%s\"" % value)
    held.append(planted and ask("--kind", "fork")[1] == want and ask("--kind", "owner-gate")[1] == want)
    owner.append(planted and [ask("--kind", k)[1] for k in ("ratification", "owner-write")] == ["owner", "owner"]
                 and ask("--kind", "fork", "--attended")[1] == "owner")
print("value %d" % int(all(held)))
print("owner %d" % int(all(owner)))
rc, out, err = ask("--kind", "nonsense")
print("unknown %d" % int(rc == 2 and out == "" and "nonsense" in err))
' "$FX" "$FX/$KREL" 2>&1)
A41=${A41//$'\r'/}
check_arm "arm 41 AC5 with no run.on-owner-question set, a fork and an owner gate each print resolve" \
   "$([ "$_rc41" = 0 ] && [[ $A41 == *'default 1'* ]] && echo 1 || echo 0)"
check_arm "arm 41 AC5 under each value a fork and an owner gate print it, best-effort-recorded as resolve" \
   "$([[ $A41 == *'value 1'* ]] && echo 1 || echo 0)"
check_arm "arm 41 AC5 a ratification, an owner write and an attended fork print owner under every value" \
   "$([[ $A41 == *'owner 1'* ]] && echo 1 || echo 0)"
check_arm "arm 41 AC5 an unknown kind exits 2 naming it" \
   "$([[ $A41 == *'unknown 1'* ]] && echo 1 || echo 0)"
[ "$A41" = $'default 1\nvalue 1\nowner 1\nunknown 1' ] || printf '    %s\n' "${A41//$'\n'/$'\n'    }"

# ---- arm 42 (TOOL-dBoundRoles-47 AC1): one criterion across the fence, the strip and the graded text. One backticked
# ---- `record:` span the order does not hand, planted in a typed `--input question=` and in the prose of the scratch
# ---- spec the orienter's render hands as `--input prompt=`: the render exits non-zero, names the span once and writes
# ---- no file, and with the question in plain words it exits 0 and writes its prompt file. Its producers, read
# ---- together: TOOL-dBoundRoles-38 fences handed content, TOOL-dBoundRoles-45 writes a typed value raw,
# ---- TOOL-dBoundRoles-24 refuses an anchor the order does not hand and skips fenced spans, TOOL-dBoundRoles-41 keeps
# ---- a typed value in the graded text and leaves a handed block's content out. A refusal naming the span once is the
# ---- typed copy graded; a clean second render is the handed copy not graded. The failing case, owed at the close
# ---- and not observed by the pass that wrote this: a `render_handoff` that wraps the typed value in
# ---- `render_handed_fence`, as TOOL-dBoundRoles-38 S2 first specified, under which the planted render exits 0. WHAT
# ---- IT DOES NOT CHECK: a typed diff on another role, or an anchor that resolves, which arm 39 grades.
build_fixture; _rc42=$?
A42P="$FX/$MR/builds/tFix/prompts"; A42S="$MR/builds/tFix/spec/2026-11-23-spec-TOOL-tFix-1.md"; A42E="$TMP_ROOT/a42.err"
A42K="record:TOOL-tFix-9@$(printf '%012d' 0)"
mkdir -p "$A42P" "$FX/$MR/builds/tFix/spec" \
  && printf '# TOOL-tFix-1\n\nThe spec quotes `%s` in its prose.\n' "$A42K" > "$FX/$A42S"
_ls=$(ls -A "$A42P")
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-orienter --build tFix --unit TOOL-tFix-1 --input "prompt=$A42S" \
   --input "question=which seam fits; see \`$A42K\`" >/dev/null 2>"$A42E"); _rc=$?
check_arm "arm 42 AC1 the orienter's span planted in its typed question and its handed prompt exits non-zero naming it once" \
   "$([ "$_rc42" = 0 ] && [ "$_rc" != 0 ] && [ "$(grep -oF -- "$A42K" "$A42E" | wc -l | tr -d ' ')" = 1 ] \
      && [ "$(ls -A "$A42P")" = "$_ls" ] && echo 1 || echo 0)"
[ "$_rc" != 0 ] || { printf '    exit %s, want non-zero\n' "$_rc"; sed 's/^/    /' "$A42E"; }
(cd "$FX" && "$PY" -B "$FXK/handoff.py" render --role gov-orienter --build tFix --unit TOOL-tFix-1 --input "prompt=$A42S" \
   --input 'question=which seam fits' >/dev/null 2>"$A42E"); _rc=$?
check_arm "arm 42 AC1 ...and with the question in plain words it exits 0 and writes its prompt file" \
   "$([ "$_rc" = 0 ] && [ -z "$_ls" ] && [ -n "$(ls -A "$A42P")" ] && echo 1 || echo 0)"
[ "$_rc" = 0 ] || sed 's/^/    /' "$A42E"

[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL the suite executed $n assertions, under its floor of $FLOOR_ASSERTIONS — a block of arms was skipped"; fail=$((fail+1)); }
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ] || { echo "FAIL ($fail of $n)"; exit 1; }
