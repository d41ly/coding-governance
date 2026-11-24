#!/usr/bin/env bash
# pass-tree.test.sh — fixture self-test for pass-tree.sh. TOOL-aTwinnedPass-2.
#
#   bash <kit>/pass-tree.test.sh    # "PASS (<n> assertions)" + exit 0 = good
#
# ONE fixture repository under one `mktemp -d`, removed on exit. `main` carries the base commit and
# then `m1.txt`, the default branch moving on; `run`, checked out, is cut from the base and carries the
# records commit C, the run-state file with one dispatch row per merged unit. The base holds the conf,
# a fixture kit whose stage-1 `[[generated]]` rows, `fx-out.txt` and `fx-new.txt`, share one generator
# `render.sh` (the sorted tracked `p*.txt` files, into `fx-out.txt` and a `gen:fx` region of the
# README), and a copy of the run-gates kit's `regen.py` with what it imports, at that kit's place under
# this suite's tool root. `render.sh` takes three switches, each off unless a block sets it:
# `FX_RENDER_FAIL` (T4), and `FX_RENDER_NEW` and `FX_RENDER_STRAY` (T7), which make the write create
# `fx-new.txt`, a generated output never tracked before, and `fx-stray.txt`, which no row covers.
# The kit's third row, `fx-rev.txt` at stage 2, is written by `rev.sh` (KICK-dKeptSession-67), a
# renderer of the committed revision modelled on the policy mirror's: each tracked `in-*.txt` with its
# blob id at HEAD, and in both modes a refusal, exit 2, while an input differs from its blob at HEAD.
# The base carries `in-0.txt`, and its commit is amended with the render, since a root commit has no
# HEAD to render from.
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
# no hook; and a Windows process holding a pass's worktree open. Nor (TOOL-aTwinnedPass-5) `--remove`'s
# own path through the run check, which shares it with `--merge` and is not armed; that the generic
# four assertions of a T3 run-check case come from the run check rather than the clean-tree refusal
# after it, which only each case's text arm tells; regen.py's reading of the two fixture rows as ONE
# item, which T7 relies on and cannot tell from two renders; and which stream the T7 NOTE goes to.
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
write_fixture_pass() { # n · product file · [worktree's last segment, default agent-p<n>] -> one pass commit in that worktree, the output re-rendered
  ( cd "$R/.claude/worktrees/${3:-agent-p$1}" && printf 'pass %s\n' "$1" >"$2" && git add -- "$2" && bash "$FX_REL/render.sh" \
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

[[generated]]
path = "fx-new.txt"
generator = "render.sh"
write = ["bash", "{kit}/render.sh"]
check = ["bash", "{kit}/render.sh", "--check"]
stage = 1

[[generated]]
path = "fx-rev.txt"
generator = "rev.sh"
write = ["bash", "{kit}/rev.sh"]
check = ["bash", "{kit}/rev.sh", "--check"]
stage = 2
EOF
cat > "$FX_REL/render.sh" <<'EOF'
#!/usr/bin/env bash
# The fixture generator: the tracked p*.txt files, sorted, into fx-out.txt and README.md's gen:fx region.
# With FX_RENDER_FAIL set, the write first leaves fx-partial.txt behind, and both modes exit 1.
# With FX_RENDER_NEW set the write also creates fx-new.txt, and with FX_RENDER_STRAY fx-stray.txt;
# --check reads neither.
set -u
if [ -n "${FX_RENDER_FAIL:-}" ]; then
  [ "${1:-}" = --check ] || : > fx-partial.txt
  exit 1
fi
[ -z "${FX_RENDER_NEW:-}" ] || [ "${1:-}" = --check ] || printf 'new\n' > fx-new.txt
[ -z "${FX_RENDER_STRAY:-}" ] || [ "${1:-}" = --check ] || printf 'stray\n' > fx-stray.txt
list=$(git ls-files -- 'p*.txt' | sort)
readme=$(awk -v l="$list" '/^<!-- gen:fx -->$/ { print; if (l != "") print l; s = 1; next } /^<!-- \/gen:fx -->$/ { s = 0 } !s' README.md)
if [ "${1:-}" = --check ]; then
  [ "$(<fx-out.txt)" = "$list" ] && [ "$(<README.md)" = "$readme" ]
  exit
fi
printf '%s\n' "$list" > fx-out.txt
printf '%s\n' "$readme" > README.md
EOF
cat > "$FX_REL/rev.sh" <<'EOF'
#!/usr/bin/env bash
# The fixture's renderer of a committed revision, as the policy mirror is one: each tracked in-*.txt
# with its blob id at HEAD, sorted, into fx-rev.txt. In both modes, while an input's bytes differ from
# its blob at HEAD, an input absent at HEAD included, it exits 2 naming the input; --check compares.
set -u
list=$(git ls-files -- 'in-*.txt' | sort | while IFS= read -r p; do
  h=$(git rev-parse -q --verify "HEAD:$p" 2>/dev/null) || h=""
  if [ -z "$h" ] || [ "$h" != "$(git hash-object -- "$p" 2>/dev/null)" ]; then
    printf 'fx-rev: refused · %s · uncommitted changes; the render reads a revision, commit first\n' "$p" >&2
    exit 2
  fi
  printf '%s %s\n' "$p" "$h"
done) || exit 2
if [ "${1:-}" = --check ]; then
  [ "$(cat fx-rev.txt 2>/dev/null)" = "$list" ]
  exit
fi
printf '%s\n' "$list" > fx-rev.txt
EOF
printf '# fixture\n\n<!-- gen:fx -->\n<!-- /gen:fx -->\n\nprose\n' > README.md
printf 'in 0\n' > in-0.txt
cp "$REPO/$RG_REL/regen.py" "$REPO/$RG_REL/profile_bar.py" "$RG_REL/" || { echo "FAIL cannot copy regen.py"; exit 2; }
git add -A && bash "$FX_REL/render.sh" && git add -A && git commit -q -m base \
  && bash "$FX_REL/rev.sh" && git add -A && git commit -q --amend --no-edit || { echo "FAIL base commit"; exit 2; }
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
# L1 (TOOL-aTwinnedPass-5 S6): the admission arm below has a negative control on the same tree and
# HEAD, so its exit 0 is the hook grading here and not a hook that binds no run. Units 4 and 7 have
# rows and no pass commit yet. Staged break: `check_commit_message`'s binding loop given an empty
# list admits every message, and both control arms go red.
printf 'build TOOL-tRun-4\n' > "$T/msg4"
cc=$(bash "$HERE/unattended.sh" --check-commit "$T/msg4" 2>&1); rc=$?
check_same "T1 --check-commit over a trailerless subject naming open pass 4 exits 1, so the hook grades in this tree" "$rc" 1
check_has "T1 ...with check 49's subject refusal" "$cc" "this commit's subject names TOOL-tRun-4, an open dispatched pass of tRun"
git log -1 --format=%B > "$T/msg"
bash "$HERE/unattended.sh" --check-commit "$T/msg" >/dev/null 2>&1
check_same "T1 --check-commit over the merge's message exits 0 (AC6)" "$?" 0

# ---- T2 (AC2): pass 4 rewrites pass 2's product file; the merge is aborted and refused -----------------
add_fixture_pass 4 && write_fixture_pass 4 p2.txt || { echo "FAIL pass 4"; exit 2; }
P4=$(git rev-parse worktree-agent-p4)
h0=$(git rev-parse HEAD)
run_tool --merge tRun --pass TOOL-tRun-4 --branch worktree-agent-p4 --from "$C"
check_same "T2 --merge of a pass that rewrote another's product file exits 1 (AC2)" "$rc" 1
check_has "T2 the refusal names p2.txt (AC2)" "$err" "p2.txt"
check_lacks "T2 the refusal does not name fx-out.txt (AC2)" "$err" "fx-out.txt"
check_same "T2 HEAD is the pre-merge sha (AC2)" "$(git rev-parse HEAD)" "$h0"
check_same "T2 the tree is clean (AC2)" "$(git status --porcelain)" ""
git rev-parse -q --verify MERGE_HEAD >/dev/null; check_same "T2 no merge is in progress (AC2)" "$?" 1
# The ref itself against its captured tip, never `git branch --list`, which prints git's `+` marker for
# a branch a worktree holds (TOOL-aTwinnedPass-5 S2). Staged break: `remove_pass_tree` called in the
# not-disjoint refusal deletes the branch, and this arm reads the empty string.
check_same "T2 branch worktree-agent-p4 remains at its tip (AC2)" "$(git rev-parse --verify -q refs/heads/worktree-agent-p4)" "$P4"
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
# M4 (TOOL-aTwinnedPass-5 S3): the run check's other refusals. The run-state file is edited in the
# work tree only and restored after each case. The run check precedes the clean-tree refusal, so each
# edit leaves the tree dirty on purpose, and the generic four assertions stay green under a break that
# skips the run check, because the dirty RUN.md is refused next: ONLY THE TEXT ARM tells the run's
# refusal from that one. Staged breaks, one at a time: the LANDED|ABORTED case deleted reds both phase
# arms; it reading LANDED alone reds the ABORTED arm; the rc-2 case folded into `*)` reds the
# no-run-branch arm; the file test deleted reds the missing-file arm. `--remove`'s path is not armed.
for ph in LANDED ABORTED; do
  sed -i "s/^phase: BUILDING\$/phase: $ph/" "$RUNMD"
  check_merge_refused "for a run recorded $ph" "$R" worktree-agent-p4 "$C"
  check_has "T3 the $ph refusal names the phase" "$err" "the run of tRun is $ph, so it takes no pass back"
  git checkout -q -- "$RUNMD"
done
sed -i '/^run-branch: /d' "$RUNMD"
check_merge_refused "for a run-state file naming no run branch" "$R" worktree-agent-p4 "$C"
check_has "T3 the no-run-branch refusal says so" "$err" "names no run branch (neither run-branch nor branch-ref)"
git checkout -q -- "$RUNMD"
mv "$RUNMD" "$T/runmd.away"
check_merge_refused "with no run-state file" "$R" worktree-agent-p4 "$C"
check_has "T3 the missing-file refusal names the file" "$err" "build tRun has no run-state file at $RUNMD"
mv "$T/runmd.away" "$RUNMD"

# ---- T4 (AC4): a failed regeneration restores the pre-merge tree ---------------------------------------
add_fixture_pass 7 && write_fixture_pass 7 p7.txt || { echo "FAIL pass 7"; exit 2; }
P7=$(git rev-parse worktree-agent-p7)
h0=$(git rev-parse HEAD)
out=$(FX_RENDER_FAIL=1 bash "$TOOL" --merge tRun --pass TOOL-tRun-7 --branch worktree-agent-p7 --from "$C" 2>"$T/err"); rc=$?
check_same "T4 --merge with a failing regeneration exits 1 (AC4)" "$rc" 1
check_has "T4 the refusal is the regeneration's, so the restore ran after the merge (AC4)" "$(<"$T/err")" "the regeneration failed"
check_same "T4 HEAD is the pre-merge sha (AC4)" "$(git rev-parse HEAD)" "$h0"
check_same "T4 the tree is clean (AC4)" "$(git status --porcelain)" ""
[ -e fx-partial.txt ]; check_same "T4 fx-partial.txt is gone (AC4)" "$?" 1
git rev-parse -q --verify MERGE_HEAD >/dev/null; check_same "T4 no merge is in progress (AC4)" "$?" 1
# KICK-dKeptSession-67 AC3: the regeneration ran with HEAD detached on the provisional merge, so the
# restore put it back on the run's branch. Staged break: the restore's re-attach replaced by a
# `reset --hard` to the pre-merge sha leaves HEAD detached, and this arm alone reds.
check_same "T4 HEAD is back on the run's branch (KICK-dKeptSession-67 AC3)" "$(git symbolic-ref -q HEAD)" "refs/heads/run"

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
# As T2's: the ref against pass 7's tip captured in T4. Staged break: `--remove`'s lost-commit test
# made `false` deletes the branch.
check_same "T5 branch worktree-agent-p7 remains at its tip (AC5)" "$(git rev-parse --verify -q refs/heads/worktree-agent-p7)" "$P7"
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

# ---- T6 (TOOL-aTwinnedPass-5 S4): every exit-2 path of main, each before load_driver_conf, HEAD as it was --
# Pass 4's branch is every call's operand: it holds a commit nothing else holds and does not merge
# cleanly, so a call that slips past its usage exit reaches a verb that refuses with exit 1 and loses
# nothing. Staged breaks, one at a time, each redding its call's exit and text arms: the `--from`
# requirement deleted; the duplicate-flag test deleted; `--remove`'s `--pass`/`--from` test deleted;
# `check_slug_shape` returning 0; the `$mid` test deleted. Not checked: an exit-2 path a later edit
# adds, which no arm here names.
check_usage_refused() { # label · stderr needle · tool argv... -> three assertions
  local l=$1 w=$2 h
  shift 2
  h=$(git rev-parse HEAD)
  run_tool "$@"
  check_same "T6 $l: exits 2" "$rc" 2
  check_same "T6 $l: HEAD is unchanged" "$(git rev-parse HEAD)" "$h"
  check_has "T6 $l: stderr names the refusal" "$err" "$w"
}
check_usage_refused "--merge without --from" "usage: pass-tree.sh" --merge tRun --pass TOOL-tRun-4 --branch worktree-agent-p4
check_usage_refused "a second --branch" "usage: pass-tree.sh" --merge tRun --pass TOOL-tRun-4 --branch worktree-agent-p4 --branch worktree-agent-p4 --from "$C"
check_usage_refused "--remove carrying --pass" "usage: pass-tree.sh" --remove tRun --branch worktree-agent-p4 --pass TOOL-tRun-4
check_usage_refused "slug ../x" "'../x' is not a build-folder name" --remove ../x --branch worktree-agent-p4
check_usage_refused "a unit of another build" "'TOOL-other-2' is not a unit id of build tRun" --merge tRun --pass TOOL-other-2 --branch worktree-agent-p4 --from "$C"

# ---- T7 (TOOL-aTwinnedPass-5 S5): the regeneration creates a generated file and leaves a stray one ------
# Only the first is committed. Pass 11 conflicts on fx-out.txt and the README region as pass 3 did, and
# the tool resolves both. The NOTE needle carries the colon and the one space before the first path, so
# a path git lists before fx-stray.txt, such as an unignored pass worktree, reds it: a fixture fault
# this arm names. Staged breaks: the staging loop's `check_generated_output` made `false` leaves
# fx-new.txt out and the NOTE naming it (arms 2, 4, 5 red); made `true` commits fx-stray.txt (arms 3, 5
# red); the loop deleted stages neither (arms 2, 4 red).
add_fixture_pass 11 && write_fixture_pass 11 p11.txt || { echo "FAIL pass 11"; exit 2; }
out=$(FX_RENDER_NEW=1 FX_RENDER_STRAY=1 bash "$TOOL" --merge tRun --pass TOOL-tRun-11 --branch worktree-agent-p11 --from "$C" 2>"$T/err"); rc=$?; err=$(<"$T/err")
check_same "T7 --merge whose regeneration creates fx-new.txt and leaves fx-stray.txt exits 0" "$rc" 0
check_same "T7 the merge commit carries fx-new.txt, a generated output the render created fresh" "$(git ls-tree --name-only "$out" -- fx-new.txt)" "fx-new.txt"
check_same "T7 the merge commit does not carry fx-stray.txt" "$(git ls-tree --name-only "$out" -- fx-stray.txt)" ""
check_has "T7 the NOTE names fx-stray.txt as left untracked" "$err" "no effective generated output covers them: fx-stray.txt"
check_same "T7 fx-stray.txt is the one path the tree's status lists" "$(git status --porcelain)" "?? fx-stray.txt"
rm -f fx-stray.txt

# ---- TP11 (TOOL-aTwinnedPass-11 AC4, AC5): the Workflow runtime's spelling, `worktree-wf_<run id>-<n>` --
# Each tree is cut by hand at C, as TP4's are. Pass 12 conflicts on fx-out.txt and the README region as
# T1's second merge does, and the tool resolves both; unit 12 has no dispatch row, as unit 11 has none
# in T7, since `--merge` reads no row. The two refused branches hold no commit no other ref holds, so
# only the new refusals stand between `--remove` and a forced removal. Staged breaks: check_pass_branch's
# test put back to `^worktree-agent-[A-Za-z0-9]+$` reds the merge arm; check_pass_holder's comparison
# widened to a `$primary/.claude/worktrees/` prefix reds the other-wf_-name arm; the tool's wf_
# alternative written `wf_[A-Za-z0-9_-]+` reds the off-structure arm.
git -C "$R" worktree add -q -b worktree-wf_0d688c69-edb-1 "$R/.claude/worktrees/wf_0d688c69-edb-1" "$C" >/dev/null 2>&1 \
  && write_fixture_pass 12 p12.txt wf_0d688c69-edb-1 || { echo "FAIL pass wf_0d688c69-edb-1"; exit 2; }
P12=$(git rev-parse worktree-wf_0d688c69-edb-1)
run_tool --merge tRun --pass TOOL-tRun-12 --branch worktree-wf_0d688c69-edb-1 --from "$C"
check_same "TP11 --merge of a wf_ pass exits 0 (AC4)" "$rc" 0
check_same "TP11 the wf_ merge prints one sha alone on stdout (AC4)" "$out" "$(git rev-parse HEAD)"
check_same "TP11 the wf_ merge has the pass commit as its second parent (AC4)" "$(git rev-parse "$out^2")" "$P12"
check_lacks "TP11 the wf_ pass's worktree is gone (AC4)" "$(git worktree list --porcelain)" "/.claude/worktrees/wf_0d688c69-edb-1"
git rev-parse --verify -q refs/heads/worktree-wf_0d688c69-edb-1 >/dev/null; check_same "TP11 branch worktree-wf_0d688c69-edb-1 is gone (AC4)" "$?" 1
git -C "$R" worktree add -q -b worktree-wf_0d688c69-edb-2 "$R/.claude/worktrees/wf_0d688c69-edb-3" "$C" >/dev/null 2>&1 || { echo "FAIL pass wf_0d688c69-edb-2"; exit 2; }
run_tool --remove tRun --branch worktree-wf_0d688c69-edb-2
check_same "TP11 --remove of a wf_ branch held at another wf_ name exits 1 (AC5)" "$rc" 1
check_has "TP11 the other-wf_-name refusal is the holder's (AC5)" "$err" "where the runtime cuts that pass's worktree"
[ -d "$R/.claude/worktrees/wf_0d688c69-edb-3" ]; check_same "TP11 the tree at the other wf_ name remains (AC5)" "$?" 0
git rev-parse --verify -q refs/heads/worktree-wf_0d688c69-edb-2 >/dev/null; check_same "TP11 branch worktree-wf_0d688c69-edb-2 remains (AC5)" "$?" 0
git -C "$R" worktree add -q -b worktree-wf_x "$R/.claude/worktrees/wf_x" "$C" >/dev/null 2>&1 || { echo "FAIL pass wf_x"; exit 2; }
run_tool --remove tRun --branch worktree-wf_x
check_same "TP11 --remove of a wf_ name off the runtime's structure exits 1 (AC5)" "$rc" 1
check_has "TP11 the off-structure refusal is the shape's (AC5)" "$err" "is not a branch the runtime cuts for a pass"
[ -d "$R/.claude/worktrees/wf_x" ]; check_same "TP11 the off-structure tree remains (AC5)" "$?" 0

# ---- K67 (KICK-dKeptSession-67 AC1, AC2): the regeneration renders over the merge as committed -------
# Pass 13 adds in-13.txt in one commit and carries rev.sh's re-render in a second; pass 14 adds
# in-14.txt and carries the base's fx-rev.txt unrendered. Neither conflicts. rev.sh refuses an input
# HEAD lacks, so a regeneration with HEAD on the pre-merge commit fails on pass 13's merge: the staged
# break, and the block's RED-first reading, is pass-tree.sh at ce776cccc, where that merge exits 1.
add_fixture_pass 13 && ( cd "$R/.claude/worktrees/agent-p13" && printf 'in 13\n' > in-13.txt && git add -- in-13.txt \
  && git commit -q -m "build TOOL-tRun-13" -m "Pass: TOOL-tRun-13" && bash "$FX_REL/rev.sh" && git add -- fx-rev.txt \
  && git commit -q -m "build TOOL-tRun-13: the render" -m "Pass: TOOL-tRun-13" ) || { echo "FAIL pass 13"; exit 2; }
add_fixture_pass 14 && ( cd "$R/.claude/worktrees/agent-p14" && printf 'in 14\n' > in-14.txt && git add -- in-14.txt \
  && git commit -q -m "build TOOL-tRun-14" -m "Pass: TOOL-tRun-14" ) || { echo "FAIL pass 14"; exit 2; }
P13=$(git rev-parse worktree-agent-p13); R13=$(git show worktree-agent-p13:fx-rev.txt); R14=$(git show worktree-agent-p14:fx-rev.txt)
h0=$(git rev-parse HEAD)
run_tool --merge tRun --pass TOOL-tRun-13 --branch worktree-agent-p13 --from "$C"
check_same "K67 --merge of pass 13, which changed an input of a renderer of HEAD, exits 0 (AC1)" "$rc" 0
check_same "K67 pass 13's merge prints one sha alone on stdout (AC1)" "$out" "$(git rev-parse HEAD)"
check_lacks "K67 pass 13's merge prints no REFUSING line (AC1)" "$err" "pass-tree: REFUSING"
check_same "K67 pass 13's merge has the pre-merge HEAD as its first parent (AC1)" "$(git rev-parse "$out^1")" "$h0"
check_same "K67 pass 13's merge has pass 13's tip as its second parent (AC1)" "$(git rev-parse "$out^2")" "$P13"
check_same "K67 the merge's fx-rev.txt is pass 13's render (AC1)" "$(git show HEAD:fx-rev.txt)" "$R13"
bash "$FX_REL/rev.sh" --check; check_same "K67 rev.sh --check reads the merge's render fresh (AC1)" "$?" 0
check_same "K67 HEAD is on the run's branch after the merge (AC1)" "$(git symbolic-ref HEAD)" "refs/heads/run"
run_tool --merge tRun --pass TOOL-tRun-14 --branch worktree-agent-p14 --from "$C"
check_same "K67 --merge of pass 14, carrying the base's render, exits 0 (AC2)" "$rc" 0
check_same "K67 pass 14's merge prints one sha alone on stdout (AC2)" "$out" "$(git rev-parse HEAD)"
[ "$(git show HEAD:fx-rev.txt)" != "$R14" ]; check_same "K67 the merge's fx-rev.txt differs from pass 14's stale bytes (AC2)" "$?" 0
check_same "K67 fx-rev.txt lists in-14.txt at its blob in the merge (AC2)" "$(grep -c "^in-14.txt $(git rev-parse HEAD:in-14.txt)\$" fx-rev.txt)" 1
bash "$FX_REL/rev.sh" --check; check_same "K67 rev.sh --check reads pass 14's merge fresh (AC2)" "$?" 0

[ "$st" = 0 ] && { echo "PASS ($n assertions)"; exit 0; }
echo "FAIL ($n assertions)"; exit 1
