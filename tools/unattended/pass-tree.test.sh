#!/usr/bin/env bash
# pass-tree.test.sh — fixture self-test for pass-tree.sh. TOOL-aTwinnedPass-2.
#
#   bash <kit>/pass-tree.test.sh    # "PASS (<n> assertions)" + exit 0 = good
#
# ONE fixture repository under one `mktemp -d`, removed on exit. `main` carries the base commit and
# then `m1.txt`, the default branch moving on; `run`, checked out, is cut from the base and carries the
# records commit C, the run-state file with one dispatch row per merged unit. The base holds the conf,
# a fixture kit whose one `[[generated]]` row is `fx-out.txt`, its generator `render.sh` (the sorted
# tracked `p*.txt` files, into `fx-out.txt` and a `gen:fx` region of the README), and a copy of the
# run-gates kit's `regen.py` with what it imports, at that kit's place under this suite's tool root.
#
# A PASS IS SIMULATED, NEVER BUILT. `add_fixture_pass` does what the runtime and the builder's first
# order do, a worktree on a new branch at `main`, both in the runtime's spelling (`worktree-agent-<id>`
# at `.claude/worktrees/agent-<id>` in the primary tree), and then the hard reset to C; `noreset` stops before
# the reset. `write_fixture_pass` commits one product file there, re-rendered, with its `Pass:` trailer.
#
# NO `<prefix>/<kit>/` LITERAL: every path is derived from this file's own directory, because the
# install-prefix leg bans a kit file naming its own directory.
#
# WHAT IT DOES NOT CHECK: a run whose tree is a linked worktree of a real build; the `merge=ours`
# attribute, which this fixture does not declare; a refused merge commit, since the fixture installs
# no hook; and a Windows process holding a pass's worktree open.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TOOL="$HERE/pass-tree.sh"
# The driver is sourced for the resolvers the tool itself calls, `resolve_python`, `resolve_kit_dir`
# and `derive_self_rel`, so the fixture's copy of regen.py sits where the tool will look for it.
# shellcheck source=unattended.sh
. "$HERE/unattended.sh" || { echo "FAIL the driver did not source"; exit 2; }
# The driver exports its graft pin for its own reads; this suite's plain `git` would print git's
# graft-file deprecation hint under it, so it is dropped here. The tool sources the driver again.
unset GIT_GRAFT_FILE
KIT_REL=$(derive_self_rel "$HERE") || { echo "FAIL this suite is not inside a git repository"; exit 2; }
case "$KIT_REL" in */*) TOOL_REL="${KIT_REL%/*}" ;; *) TOOL_REL="" ;; esac
REPO=${HERE%/"$KIT_REL"}
PY=$(resolve_python 2>/dev/null) || { echo "FAIL no usable python launcher, so regen.py cannot run in the fixture"; exit 2; }
RG_REL=$(resolve_kit_dir "$PY" run-gates regen.py "$HERE" 2>/dev/null) || { echo "FAIL no run-gates kit holding regen.py beside this kit"; exit 2; }
FX_REL="${TOOL_REL:+$TOOL_REL/}fx"
export GOV_RUNLOG=0
T=$(mktemp -d) || exit 2
trap 'cd /; rm -rf "$T"' EXIT
R="$T/r"
st=0; n=0
check_has()   { n=$((n+1)); case "$2" in *"$3"*) echo "ok   $1" ;; *) echo "FAIL $1 -- output did not carry '$3': $2"; st=1 ;; esac; }
check_lacks() { n=$((n+1)); case "$2" in *"$3"*) echo "FAIL $1 -- output carried '$3' and must not: $2"; st=1 ;; *) echo "ok   $1" ;; esac; }
check_same()  { n=$((n+1)); if [ "$2" = "$3" ]; then echo "ok   $1"; else echo "FAIL $1 -- got '$2' want '$3'"; st=1; fi; }
# One tool call from the current directory: stdout in `out`, stderr in `err`, the exit in `rc`.
run_tool() { out=$(bash "$TOOL" "$@" 2>"$T/err"); rc=$?; err=$(<"$T/err"); }
measure_refusals() { grep -c '^pass-tree: REFUSING' "$T/err" || true; }
add_fixture_pass() { # n · [noreset] -> worktree $R/.claude/worktrees/agent-p<n> on branch worktree-agent-p<n>, at C unless noreset
  git -C "$R" worktree add -q -b "worktree-agent-p$1" "$R/.claude/worktrees/agent-p$1" main >/dev/null 2>&1 || return 1
  [ "${2:-}" = noreset ] && return 0
  git -C "$R/.claude/worktrees/agent-p$1" reset -q --hard "$C"
}
write_fixture_pass() { # n · product file -> one pass commit in pass n's worktree, the output re-rendered
  ( cd "$R/.claude/worktrees/agent-p$1" && printf 'pass %s\n' "$1" >"$2" && git add -- "$2" && bash "$FX_REL/render.sh" \
      && git add -A && git commit -q -m "build TOOL-tRun-$1" -m "Pass: TOOL-tRun-$1" )
}

# ---- the fixture repository -------------------------------------------------------------------------
mkdir -p "$R" "$T/hooks"
cd "$R" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t \
  && git config core.autocrlf false && git config core.hooksPath "$T/hooks" || { echo "FAIL git init"; exit 2; }
# The pass worktrees sit inside this tree, where the runtime cuts them, and are excluded as node a's
# common info/exclude excludes them, so the clean test and the untracked walk do not see them.
printf '.claude/worktrees/\n' >> .git/info/exclude
# The conf in the driver suite's `mkconf` shape, every key that NOTEs when blank declared.
cat > .unattended.conf <<'EOF'
MEMORY_ROOT=memory
UNITS_REGION_CUTOFF="2026-08-19"
SPEC_THIN_CUTOFF=""
SPEC_AUDIT_DEFAULT=""
PROMPT_BRIEF_CUTOFF="2099-01-01"
PROMPT_BRIEF_SKELETON_CUTOFF="2099-01-01"
LANDER="echo land"
LANDER_MODE="primary"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
GATE_BOUND="3600"
GATE_WALL="21600"
UNIT_STALL_BOUND="1800"
TASK_STALL_BOUND="5400"
REVIEW_ROUNDS="7"
RESUME_STALE_BOUND="5400"
WIRING_CHECK="true"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
RESUME_SCHEDULE="on"
RESUME_SCHEDULE_CREATE="TheScheduleCreate"
RESUME_SCHEDULE_DELETE="TheScheduleDelete"
RESUME_SCHEDULE_DELAY="1800"
RESUME_SCHEDULE_LIMIT="6"
RUN_CLAIMS="off"
PHASES_EXTRA=""
DOD_EXTRA=""
EOF
mkdir -p "$FX_REL" "$RG_REL"
cat > "$FX_REL/kit.toml" <<'EOF'
id = "fx"

[[generated]]
path = "fx-out.txt"
generator = "render.sh"
write = ["bash", "{kit}/render.sh"]
check = ["bash", "{kit}/render.sh", "--check"]
stage = 1
EOF
cat > "$FX_REL/render.sh" <<'EOF'
#!/usr/bin/env bash
# The fixture generator: the tracked p*.txt files, sorted, into fx-out.txt and README.md's gen:fx region.
# With FX_RENDER_FAIL set, the write first leaves fx-partial.txt behind, and both modes exit 1.
set -u
if [ -n "${FX_RENDER_FAIL:-}" ]; then
  [ "${1:-}" = --check ] || : > fx-partial.txt
  exit 1
fi
list=$(git ls-files -- 'p*.txt' | sort)
readme=$(awk -v l="$list" '/^<!-- gen:fx -->$/ { print; if (l != "") print l; s = 1; next } /^<!-- \/gen:fx -->$/ { s = 0 } !s' README.md)
if [ "${1:-}" = --check ]; then
  [ "$(<fx-out.txt)" = "$list" ] && [ "$(<README.md)" = "$readme" ]
  exit
fi
printf '%s\n' "$list" > fx-out.txt
printf '%s\n' "$readme" > README.md
EOF
printf '# fixture\n\n<!-- gen:fx -->\n<!-- /gen:fx -->\n\nprose\n' > README.md
cp "$REPO/$RG_REL/regen.py" "$REPO/$RG_REL/profile_bar.py" "$RG_REL/" || { echo "FAIL cannot copy regen.py"; exit 2; }
git add -A && bash "$FX_REL/render.sh" && git add -A && git commit -q -m base || { echo "FAIL base commit"; exit 2; }
BASE=$(git rev-parse HEAD)
git checkout -q -b run
mkdir -p memory/builds/tRun
{
  printf '# tRun — run state\n\n## Run facts\nphase: BUILDING\nrun-branch: refs/heads/run\n\n## Log\n'
  for u in 2 3 4 7; do
    printf '2026-11-15T00:00:0%sZ dispatch · item %s TOOL-tRun-%s · reason p%s.txt\n' "$u" "$BASE" "$u" "$u"
  done
} > memory/builds/tRun/RUN.md
git add -A && git commit -q -m "records" -m "Pass: none" || { echo "FAIL records commit"; exit 2; }
C=$(git rev-parse HEAD)
git checkout -q main && printf 'm1\n' > m1.txt && git add m1.txt && git commit -q -m m1 && git checkout -q run \
  || { echo "FAIL main's second commit"; exit 2; }
RUNMD=memory/builds/tRun/RUN.md

# ---- T1 (AC1, AC6): passes 2 and 3 merged in turn, the generated output and region re-rendered ---------
add_fixture_pass 2 && write_fixture_pass 2 p2.txt || { echo "FAIL pass 2"; exit 2; }
add_fixture_pass 3 && write_fixture_pass 3 p3.txt || { echo "FAIL pass 3"; exit 2; }
P2=$(git rev-parse worktree-agent-p2); P3=$(git rev-parse worktree-agent-p3)
h0=$(git rev-parse HEAD)
run_tool --merge tRun --pass TOOL-tRun-2 --branch worktree-agent-p2 --from "$C"
check_same "T1 --merge of pass 2 exits 0 (AC1)" "$rc" 0
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
M2=$out
check_same "T1 pass 2's merge prints one sha alone on stdout (AC1)" "$M2" "$(git rev-parse HEAD)"
check_same "T1 pass 2's merge has the pre-merge HEAD as its first parent" "$(git rev-parse "$M2^1")" "$h0"
check_same "T1 pass 2's merge has pass 2's commit as its second parent (AC1)" "$(git rev-parse "$M2^2")" "$P2"
run_tool --merge tRun --pass TOOL-tRun-3 --branch worktree-agent-p3 --from "$C"
check_same "T1 --merge of pass 3, whose output and region conflict, exits 0 (AC1)" "$rc" 0
M3=$out
check_same "T1 pass 3's merge prints one sha alone on stdout (AC1)" "$M3" "$(git rev-parse HEAD)"
check_same "T1 pass 3's merge has pass 3's commit as its second parent (AC1)" "$(git rev-parse "$M3^2")" "$P3"
check_same "T1 fx-out.txt lists both passes' files (AC1)" "$(<fx-out.txt)" "p2.txt
p3.txt"
bash "$FX_REL/render.sh" --check; check_same "T1 render.sh --check confirms the output and the README region fresh (AC1)" "$?" 0
check_same "T1 the second merge's subject names its unit (AC1)" "$(git log -1 --format=%s)" "merge(tRun): TOOL-tRun-3's pass tree"
check_same "T1 the merge carries the Pass: none trailer (AC1)" "$(git log -1 --format='%(trailers:key=Pass,valueonly)' | tr -d '\n')" "none"
check_has "T1 the merge body names the branch, its tip and --from" "$(git log -1 --format=%b)" "Merges worktree-agent-p3 at ${P3:0:8}, dispatched from ${C:0:8}."
wl=$(git worktree list --porcelain)
check_lacks "T1 pass 2's worktree is gone (AC1)" "$wl" "/.claude/worktrees/agent-p2"
check_lacks "T1 pass 3's worktree is gone (AC1)" "$wl" "/.claude/worktrees/agent-p3"
check_same "T1 neither pass branch remains (AC1)" "$(git branch --list 'worktree-agent-p*')" ""
check_same "T1 the tree is clean after both merges (AC1)" "$(git status --porcelain)" ""
got=$( . "$HERE/lib-unattended.sh" && pass_commit "$BASE" TOOL-tRun-2 "$RUNMD" )
check_same "T1 pass_commit names pass 2's own commit, not the merge (AC6)" "$got" "$P2"
git log -1 --format=%B > "$T/msg"
bash "$HERE/unattended.sh" --check-commit "$T/msg" >/dev/null 2>&1
check_same "T1 --check-commit over the merge's message exits 0 (AC6)" "$?" 0

# ---- T2 (AC2): pass 4 rewrites pass 2's product file; the merge is aborted and refused -----------------
add_fixture_pass 4 && write_fixture_pass 4 p2.txt || { echo "FAIL pass 4"; exit 2; }
h0=$(git rev-parse HEAD)
run_tool --merge tRun --pass TOOL-tRun-4 --branch worktree-agent-p4 --from "$C"
check_same "T2 --merge of a pass that rewrote another's product file exits 1 (AC2)" "$rc" 1
check_has "T2 the refusal names p2.txt (AC2)" "$err" "p2.txt"
check_lacks "T2 the refusal does not name fx-out.txt (AC2)" "$err" "fx-out.txt"
check_same "T2 HEAD is the pre-merge sha (AC2)" "$(git rev-parse HEAD)" "$h0"
check_same "T2 the tree is clean (AC2)" "$(git status --porcelain)" ""
git rev-parse -q --verify MERGE_HEAD >/dev/null; check_same "T2 no merge is in progress (AC2)" "$?" 1
check_same "T2 branch worktree-agent-p4 remains (AC2)" "$(git branch --list worktree-agent-p4 | tr -d ' *')" "worktree-agent-p4"
check_has "T2 pass 4's worktree remains (AC2)" "$(git worktree list --porcelain)" "/.claude/worktrees/agent-p4"

# ---- T3 (AC3): each merge refusal, with HEAD and the tree as they were --------------------------------
add_fixture_pass 5 || { echo "FAIL pass 5"; exit 2; }
add_fixture_pass 8 && ( cd "$R/.claude/worktrees/agent-p8" && printf 'stray row\n' >>"$RUNMD" && printf 'pass 8\n' > p8.txt \
  && git add -A && git commit -q -m "build TOOL-tRun-8" -m "Pass: TOOL-tRun-8" ) || { echo "FAIL pass 8"; exit 2; }
add_fixture_pass 9 noreset && write_fixture_pass 9 p9.txt || { echo "FAIL pass 9"; exit 2; }
check_merge_refused() { # label · directory · branch · from -> four assertions
  local h s
  h=$(git -C "$R" rev-parse HEAD); s=$(git -C "$R" status --porcelain)
  ( cd "$2" && run_tool --merge tRun --pass TOOL-tRun-4 --branch "$3" --from "$4"; printf '%s' "$rc" > "$T/rc" )
  rc=$(<"$T/rc"); err=$(<"$T/err")
  check_same "T3 $1: exits 1 (AC3)" "$rc" 1
  check_same "T3 $1: one REFUSING line (AC3)" "$(measure_refusals)" 1
  check_same "T3 $1: HEAD is unchanged (AC3)" "$(git -C "$R" rev-parse HEAD)" "$h"
  check_same "T3 $1: the tree's status is unchanged (AC3)" "$(git -C "$R" status --porcelain)" "$s"
}
check_merge_refused "from a tree on another branch" "$R/.claude/worktrees/agent-p5" worktree-agent-p4 "$C"
check_has "T3 the other-branch refusal names the run's branch" "$err" "refs/heads/run"
printf 'stray\n' > stray.txt
check_merge_refused "with an untracked file present" "$R" worktree-agent-p4 "$C"
check_has "T3 the untracked-file refusal names the clean test" "$err" "not clean"
rm -f stray.txt
check_merge_refused "for branch worktree-agent-none, which does not exist" "$R" worktree-agent-none "$C"
check_has "T3 the absent-branch refusal names the branch" "$err" "no branch worktree-agent-none exists"
check_merge_refused "for the run's own branch" "$R" run "$C"
check_has "T3 the run-branch refusal says so" "$err" "run is the run's own branch"
check_merge_refused "for branch -x" "$R" -x "$C"
check_has "T3 the -x refusal is the branch-name check" "$err" "'-x' is not a branch name git admits"
check_merge_refused "for pass 5, which committed nothing" "$R" worktree-agent-p5 "$C"
check_has "T3 the no-commit refusal names --remove" "$err" "--remove"
check_merge_refused "for pass 8, which wrote the run-state file" "$R" worktree-agent-p8 "$C"
check_has "T3 the run-state refusal names the file" "$err" "$RUNMD"
check_merge_refused "with --from HEAD" "$R" worktree-agent-p4 HEAD
check_has "T3 the --from refusal names the value" "$err" "--from 'HEAD' is not 7 to 64 lowercase hex digits"
check_merge_refused "for pass 9, cut from main with no reset" "$R" worktree-agent-p9 "$C"
check_has "T3 the fork-point refusal names the reset" "$err" "did not reset its worktree"
check_has "T3 the fork-point refusal names C's first eight digits" "$err" "${C:0:8}"
check_same "T3 pass 9's merge did not carry m1.txt into run (AC3)" "$(git ls-files m1.txt)" ""

# ---- T4 (AC4): a failed regeneration restores the pre-merge tree ---------------------------------------
add_fixture_pass 7 && write_fixture_pass 7 p7.txt || { echo "FAIL pass 7"; exit 2; }
h0=$(git rev-parse HEAD)
out=$(FX_RENDER_FAIL=1 bash "$TOOL" --merge tRun --pass TOOL-tRun-7 --branch worktree-agent-p7 --from "$C" 2>"$T/err"); rc=$?
check_same "T4 --merge with a failing regeneration exits 1 (AC4)" "$rc" 1
check_has "T4 the refusal is the regeneration's, so the restore ran after the merge (AC4)" "$(<"$T/err")" "the regeneration failed"
check_same "T4 HEAD is the pre-merge sha (AC4)" "$(git rev-parse HEAD)" "$h0"
check_same "T4 the tree is clean (AC4)" "$(git status --porcelain)" ""
[ -e fx-partial.txt ]; check_same "T4 fx-partial.txt is gone (AC4)" "$?" 1
git rev-parse -q --verify MERGE_HEAD >/dev/null; check_same "T4 no merge is in progress (AC4)" "$?" 1

# ---- T5 (AC5): --remove takes away an uncommitted pass and refuses a committed one ----------------------
run_tool --remove tRun --branch worktree-agent-p5
check_same "T5 --remove of pass 5, reset and never committed, exits 0 (AC5)" "$rc" 0
check_same "T5 branch worktree-agent-p5 is gone (AC5)" "$(git branch --list worktree-agent-p5)" ""
check_lacks "T5 pass 5's worktree is gone (AC5)" "$(git worktree list --porcelain)" "/.claude/worktrees/agent-p5"
add_fixture_pass 10 noreset || { echo "FAIL pass 10"; exit 2; }
run_tool --remove tRun --branch worktree-agent-p10
check_same "T5 --remove of pass 10, cut with no reset and never committed, exits 0 (AC5)" "$rc" 0
check_same "T5 branch worktree-agent-p10 is gone (AC5)" "$(git branch --list worktree-agent-p10)" ""
check_lacks "T5 pass 10's worktree is gone (AC5)" "$(git worktree list --porcelain)" "/.claude/worktrees/agent-p10"
run_tool --remove tRun --branch worktree-agent-p7
check_same "T5 --remove of pass 7, holding a commit no other ref holds, exits 1 (AC5)" "$rc" 1
check_has "T5 the refusal names --merge (AC5)" "$err" "--merge"
check_same "T5 branch worktree-agent-p7 remains (AC5)" "$(git branch --list worktree-agent-p7 | tr -d ' *')" "worktree-agent-p7"
check_has "T5 pass 7's worktree remains (AC5)" "$(git worktree list --porcelain)" "/.claude/worktrees/agent-p7"
run_tool --remove tRun --branch worktree-agent-none
check_same "T5 --remove of an absent branch exits 0 (AC5)" "$rc" 0
check_same "T5 one stderr line names worktree-agent-none (AC5)" "$(grep -c worktree-agent-none "$T/err" || true)" 1

# ---- TP4 (TOOL-aTwinnedPass-4 AC3 to AC7): a branch or holder outside the runtime's spelling ------------
# Every branch here is cut at C, which `run` holds, so none holds a commit no other ref holds and only
# the new refusals stand between `--remove` and a forced removal.
git -C "$R" worktree add -q -b worktree-agent-q1 "$T/elsewhere/agent-q1" "$C" >/dev/null 2>&1 \
  && printf 'keep\n' > "$T/elsewhere/agent-q1/keep.txt" || { echo "FAIL pass q1"; exit 2; }
run_tool --remove tRun --branch worktree-agent-q1
check_same "TP4 --remove of a branch held outside .claude/worktrees exits 1 (AC3)" "$rc" 1
check_same "TP4 the outside-holder --remove prints one REFUSING line (AC3)" "$(measure_refusals)" 1
check_has "TP4 the outside-holder refusal names the holder (AC3)" "$err" "elsewhere/agent-q1"
[ -d "$T/elsewhere/agent-q1" ]; check_same "TP4 the outside holder's directory remains (AC3)" "$?" 0
[ -f "$T/elsewhere/agent-q1/keep.txt" ]; check_same "TP4 the outside holder's keep.txt remains (AC3)" "$?" 0
git rev-parse --verify -q refs/heads/worktree-agent-q1 >/dev/null; check_same "TP4 branch worktree-agent-q1 remains (AC3)" "$?" 0
h0=$(git rev-parse HEAD); s0=$(git status --porcelain)
run_tool --merge tRun --pass TOOL-tRun-4 --branch worktree-agent-q1 --from "$C"
check_same "TP4 --merge of a branch held outside .claude/worktrees exits 1 (AC4)" "$rc" 1
check_has "TP4 the outside-holder --merge is the holder refusal (AC4)" "$err" "where the runtime cuts that pass's worktree"
check_same "TP4 HEAD is unchanged by the outside-holder --merge (AC4)" "$(git rev-parse HEAD)" "$h0"
check_same "TP4 the status is unchanged by the outside-holder --merge (AC4)" "$(git status --porcelain)" "$s0"
[ -d "$T/elsewhere/agent-q1" ]; check_same "TP4 the outside holder's directory remains after --merge (AC4)" "$?" 0
git -C "$R" worktree add -q -b agent-q2 "$R/.claude/worktrees/agent-q2" "$C" >/dev/null 2>&1 || { echo "FAIL pass q2"; exit 2; }
run_tool --remove tRun --branch agent-q2
check_same "TP4 --remove of agent-q2, outside the branch shape, exits 1 (AC5)" "$rc" 1
check_has "TP4 the agent-q2 --remove refusal is the shape's (AC5)" "$err" "is not a branch the runtime cuts for a pass"
run_tool --merge tRun --pass TOOL-tRun-4 --branch agent-q2 --from "$C"
check_same "TP4 --merge of agent-q2, outside the branch shape, exits 1 (AC5)" "$rc" 1
check_has "TP4 the agent-q2 --merge refusal is the shape's (AC5)" "$err" "is not a branch the runtime cuts for a pass"
[ -d "$R/.claude/worktrees/agent-q2" ]; check_same "TP4 agent-q2's worktree remains (AC5)" "$?" 0
git -C "$R" worktree add -q -b worktree-agent-q3 "$R/.claude/worktrees/agent-zz" "$C" >/dev/null 2>&1 || { echo "FAIL pass q3"; exit 2; }
run_tool --remove tRun --branch worktree-agent-q3
check_same "TP4 --remove of a branch held at another pass's place exits 1 (AC5)" "$rc" 1
[ -d "$R/.claude/worktrees/agent-zz" ]; check_same "TP4 the worktree at another pass's place remains (AC5)" "$?" 0
git -C "$R" worktree add -q -b worktree-agent-q4 "$R/.claude/worktrees/agent-q4" "$C" >/dev/null 2>&1 \
  && printf 'scratch\n' > "$R/.claude/worktrees/agent-q4/scratch.txt" || { echo "FAIL pass q4"; exit 2; }
run_tool --remove tRun --branch worktree-agent-q4
check_same "TP4 --remove of a confined holder with untracked scratch exits 0 (AC6)" "$rc" 0
[ -d "$R/.claude/worktrees/agent-q4" ]; check_same "TP4 the confined holder's directory is gone (AC6)" "$?" 1
run_tool --merge tRun --pass TOOL-tRun-4 --branch worktree-agent-p4 --from "$(printf '%064d' 0)"
check_same "TP4 --merge with a 64-digit --from naming nothing exits 1 (AC7)" "$rc" 1
check_has "TP4 the 64-digit --from reaches the lookup (AC7)" "$err" "names no commit"
check_lacks "TP4 the 64-digit --from passes the shape (AC7)" "$err" "is not 7 to 64"
run_tool --merge tRun --pass TOOL-tRun-4 --branch worktree-agent-p4 --from "$(printf '%065d' 0)"
check_has "TP4 a 65-digit --from is refused by the shape (AC7)" "$err" "is not 7 to 64"

[ "$st" = 0 ] && { echo "PASS ($n assertions)"; exit 0; }
echo "FAIL ($n assertions)"; exit 1
