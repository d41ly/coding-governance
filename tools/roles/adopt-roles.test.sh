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
# legacy home (arm 33). Every arm is a self-contained block below the prologue, so a
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
FLOOR_ASSERTIONS=129
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
printf '%s\n' '' '[effort.profiles.tfam]' 'match = ["tfam"]' 'default = "low"' '' \
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
printf '%s\n' '' '[effort.profiles.tven]' 'match = ["vendor"]' 'default = "low"' >> "$FX/$KREL/house/policy.toml"
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
printf '%s\n' '' '[effort.profiles.tfam]' 'match = ["tfam"]' 'default = "low"   # a21' >> "$FX/$KREL/house/policy.toml"
(cd "$FX" && bash "$FXK/adopt-roles.sh" --scaffold >/dev/null 2>&1); _rc21=$?
check_arm "arm 21 a policy that gains a profile scaffolds and checks clean" "$([ "$_rc21" = 0 ] && run_adopter --check >/dev/null && echo 1 || echo 0)"
sed -i 's/^default = "low"   # a21$/default = "max"/' "$FX/$KREL/house/policy.toml"
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
A22=$("$PY" -B -c 'import pathlib, sys
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
        print("rendered %d" % ("### brief:prompt\n\n" + lines + "\n### brief:goal\n" in task))
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
_mt=memory-tree; [[ $FXK == */* ]] && _mt=${FXK%/*}/memory-tree
A33P="$FX/$MR/builds/tFix/prompts"; A33B="$FX/$MR/builds/tFix/build"; A33R="$TMP_ROOT/a33.out"
A33H="$FX/$MR/project/work-order-legacy.txt"
mkdir -p "$FX/$_mt" "$A33P" "$A33B" && cp "$HERE/../memory-tree/legacy_ledger.py" "$FX/$_mt"/
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

[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL the suite executed $n assertions, under its floor of $FLOOR_ASSERTIONS — a block of arms was skipped"; fail=$((fail+1)); }
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ] || { echo "FAIL ($fail of $n)"; exit 1; }
