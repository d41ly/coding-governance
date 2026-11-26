#!/usr/bin/env bash
# pass-tree.sh — bring a parallel pass's own branch back into the run's branch, or take it away.
# TOOL-aTwinnedPass-2.
#
#   bash <kit>/pass-tree.sh --merge <slug> --pass <unit-id> --branch <branch> --from <sha>   # prints the merge commit's sha
#   bash <kit>/pass-tree.sh --remove <slug> --branch <branch>                              # prints nothing
#
# Exit 0 done · 1 a named refusal on stderr, the tree as it was · 2 misconfigured (a usage line).
#
# 1. WHAT IT IS. The main loop's tool for a build pass that ran in a worktree and on a branch of its
#    own. It runs in the RUN'S OWN TREE, the one with the run's branch checked out, by the main loop,
#    and never in a pass's worktree: both verbs refuse any other tree. It sources the driver beside it
#    for the run readers and calls `load_driver_conf`, so it answers "which tree drives this run" and
#    "which paths are generated outputs" exactly as the driver does; it never calls the driver's `main`.
#
# 2. THE ORDER, for a group the build order marks parallel:
#    a. `--dispatch` and `--brief` for each unit, on the run's branch;
#    b. one records commit carrying their rows and brief files, ending `Pass: none`;
#    c. one `unattended-unit.js` call per unit, concurrently, each with the commit key `passBase` set to
#       that records commit's sha and `writes` set to the paths that unit's `--dispatch` declared,
#       space-separated;
#    d. then, in turn, `--merge` for each pass that returned `committed: true`, with `--branch` the
#       branch its return carries and `--from` the same sha, and `--remove` for each that did not.
#
# 3. WHY THE MAIN LOOP, AND NOT THE BUILDER, RECORDS THE DISPATCH AND BRIEF ROWS. Both write the
#    run-state file, which a concurrent pass may not touch (M6 condition 3), and `--merge` refuses a
#    pass branch that changed it since its fork point.
#
# 4. WHAT `--merge` DOES. It refuses a branch whose merge base with HEAD is not `--from`: a builder
#    that skipped its reset to `passBase` forked from another line, and merging it would carry that
#    line's history in. Both verbs refuse a branch outside the runtime's two spellings,
#    `worktree-agent-<id>` and `worktree-wf_<run id>-<n>`, and a worktree holding it anywhere but
#    `<primary tree>/.claude/worktrees/<name>` for that branch's own `<name>`, the branch less
#    `worktree-`, so neither ever removes a tree it did not cut. It merges `--no-ff --no-commit`, and resolves to this side ONLY a conflicted
#    path an effective generated output covers or one the pass changed inside gen regions alone; any
#    other conflict is two passes that were not disjoint, so the merge is aborted and refused naming
#    every such path. It then runs the run-gates kit's `regen.py --write`, found as the lander finds
#    it and announced and skipped where it is not installed. The regeneration runs with HEAD on a
#    provisional commit of the merge, the index written as a tree with the merge's two parents and its
#    message, so a renderer that reads the committed revision, as the policy mirror does, reads the
#    pass's inputs; HEAD goes back on the run's branch after it, whatever its exit, as the lander's
#    `--prepare` regenerates detached on its merge. It then stages, and commits a merge whose second
#    parent is the builder's own pass commit, hooks running and never `--no-verify`. A failure after
#    the merge started and before its commit landed restores the pre-merge HEAD with nothing staged,
#    no merge in progress and no new file: the clean-tree refusal up front is what makes that exact.
#    The merge carries a `Pass: none` trailer, so `pass_commit` and check 23 skip it and read the
#    builder's commit on the second parent as the pass commit. Then the pass's worktree and branch go.
#    `--remove` takes away those of a pass that committed nothing, and refuses a branch holding a
#    commit no other branch, remote-tracking ref or tag holds, naming `--merge`.
#
# 5. WHAT IT DOES NOT CHECK.
#    - A pass's own commits: in its worktree `--check-commit` finds no run, so check 23 grades them at
#      the close. `--merge` refuses only the run-state file, a foreign fork point and an unresolvable
#      conflict.
#    - That `--branch` is the branch the harness returned for `--pass`: the main loop's word is taken.
#    - A builder that reset to the right commit and then merged or rebased other content in.
#    - A generated output no staged `[[generated]]` or `[[regenerate]]` row renders is resolved to
#      this side and not re-rendered; so is a gen region no staged item renders. A hand edit inside a
#      gen region is not told from a render.
#    - Two passes that changed one path compatibly merge with no conflict and are not looked at.
#    - A path the `merge=ours` attribute takes keeps this side's bytes without a conflict.
#    - A worktree a Windows process holds open: its removal fails, the note names it, and the branch
#      stays, since git will not delete a branch a worktree has checked out.
#    - A pass whose return carried no branch: nothing here can find its worktree.
#    - How many passes run at once.
#    - The holder comparison is textual: a worktree registered under another spelling of the same path,
#      by drive-letter case, an 8.3 short name or a link, is refused, which is the safe direction.
#    - A branch no worktree holds is deleted by `--remove` without a holder check, since there is no
#      tree to lose; the lost-commit refusal still guards its commits.
#    - A runtime that cuts passes under another name or place: each such pass is refused, never merged
#      or removed, until this tool learns the spelling.
#    - A process killed while the regeneration runs leaves HEAD detached on the provisional commit,
#      with the merge in progress. The next `--merge` refuses at the run check, since the tree no
#      longer has the run's branch checked out. The recovery is `git symbolic-ref HEAD <run ref>`,
#      then `git reset --hard` and `git clean -fd`.
#    - A generator that reads HEAD's tree for an output an earlier stage wrote reads the provisional
#      commit's bytes, from before the regeneration. The lander's `--prepare` has the same property.
#    - A generator that reads the checked-out branch's name reads none while HEAD is detached. The
#      lander's `--prepare` regenerates detached too, so such a generator already meets this at every
#      landing.
set -u
case "${BASH_SOURCE[0]}" in */*) _pt_dir=${BASH_SOURCE[0]%/*} ;; *) _pt_dir=. ;; esac
[ -f "$_pt_dir/unattended.sh" ] || {
  echo "pass-tree: the driver is missing beside this script, so the run readers it shares are unavailable: $_pt_dir/unattended.sh" >&2
  exit 2
}
# shellcheck source=unattended.sh
. "$_pt_dir/unattended.sh"
PT_USAGE="usage: pass-tree.sh --merge <slug> --pass <unit-id> --branch <branch> --from <sha> | --remove <slug> --branch <branch>"
PT_BRANCH=""; PT_FROM=""; PT_WHERE=""

print_pass_tree_refusal() { # text -> one REFUSING line on stderr
  printf 'pass-tree: REFUSING - %s\n' "$1" >&2
}

# The run check both verbs make first: the slug's run-state file exists, its RECORDED phase is live,
# and this tree has the run's branch checked out, read as `check_commit_message` reads the binding.
check_pass_tree_run() { # slug -> 0 this tree drives the run · 1 with its refusal printed; leaves HW_REF
  local rc=0 rel
  runmd_of "$1" >/dev/null; rel=$_runmd
  if [ ! -f "$rel" ]; then
    print_pass_tree_refusal "build $1 has no run-state file at $rel, so no run binds this tree; nothing was written"
    return 1
  fi
  read_recorded_phase "$rel" >/dev/null
  case "$_fact" in
    LANDED|ABORTED) print_pass_tree_refusal "the run of $1 is $_fact, so it takes no pass back; nothing was written"; return 1 ;;
  esac
  resolve_holder_worktree "$rel" || rc=$?
  case "$rc" in
    0) return 0 ;;
    2) print_pass_tree_refusal "the run-state file of $1 names no run branch (neither run-branch nor branch-ref), so no tree is known to drive it; nothing was written" ;;
    *) print_pass_tree_refusal "this tree has ${HW_HEAD:-nothing} checked out, not the run's branch $HW_REF, so it does not drive $1; run pass-tree.sh in the tree that holds $HW_REF. Nothing was written" ;;
  esac
  return 1
}

# A name git admits as a branch, compared with git's own spelling of it so `@{-1}` is not expanded
# into another branch, and never the run's own branch. Existence is each verb's own question.
check_pass_branch() { # branch -> 0 with PT_BRANCH set · 1 with its refusal printed
  local got
  PT_BRANCH=""
  case "$1" in
    ""|-*) print_pass_tree_refusal "'$1' is not a branch name git admits; nothing was written"; return 1 ;;
  esac
  got=$(GIT check-ref-format --branch "$1" 2>/dev/null) || got=""
  if [ "$got" != "$1" ]; then
    print_pass_tree_refusal "'$1' is not a branch name git admits; nothing was written"
    return 1
  fi
  if [ "refs/heads/$1" = "$HW_REF" ]; then
    print_pass_tree_refusal "$1 is the run's own branch, not a pass's; nothing was written"
    return 1
  fi
  if ! [[ $1 =~ ^worktree-(agent-[A-Za-z0-9]+|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+)$ ]]; then
    print_pass_tree_refusal "'$1' is not a branch the runtime cuts for a pass (worktree-agent-<id> or worktree-wf_<run id>-<n>), so it is not a pass's branch; nothing was written"
    return 1
  fi
  PT_BRANCH=$1
}

# The holder both verbs check before they write: a worktree holding the pass's branch must sit exactly
# where the runtime cuts that pass's, `<primary tree>/.claude/worktrees/<name>` for the branch's own
# `<name>`, the branch less `worktree-` (`agent-<id>` or `wf_<run id>-<n>`), the primary tree read from the porcelain list `derive_holder_where` reads, so both paths
# carry one spelling. An unreadable list leaves the primary empty, which fails the comparison.
check_pass_holder() { # (PT_BRANCH) -> 0 with PT_WHERE the admitted holder, empty when none holds it · 1 with its refusal printed
  local HW_REF="refs/heads/$PT_BRANCH" where primary want
  PT_WHERE=""
  where=$(derive_holder_where)
  [ -d "$where" ] || return 0
  primary=$(GIT worktree list --porcelain 2>/dev/null | awk '/^worktree /{ print substr($0, 10); exit }')
  want="$primary/.claude/worktrees/${PT_BRANCH#worktree-}"
  if [ "$where" != "$want" ]; then
    print_pass_tree_refusal "$PT_BRANCH is checked out at $where, not at $want, where the runtime cuts that pass's worktree, so that tree is not a pass's and is left as it is; nothing was written"
    return 1
  fi
  PT_WHERE=$where
}

# The resolution rule: an effective generated output, or a change the pass made inside gen regions
# alone (the merge base's blob against the branch's). Anything else is refused by the caller.
check_resolvable_path() { # path · merge base · branch -> 0 this side may be kept
  check_generated_output "$1" "$GENERATED_INDEXES" && return 0
  check_gen_region_only "$2:$1" "refs/heads/$3:$1"
}

# The regeneration, found as the lander's `run_regen` finds it: the resolved python, the run-gates kit
# beside this one, and the file under this tree. No python or no kit is announced and is not a failure.
# Both skips return before HEAD moves. The write then runs with HEAD detached on the provisional merge,
# the index as a tree with the pre-merge HEAD and the pass tip as parents and the merge's own message,
# and HEAD goes back on the run's branch, `HW_REF` as the run check left it, whatever the write's exit.
run_pass_tree_regen() { # pre-merge HEAD · pass tip · message file -> 0 regenerated or announced-skipped · 1 a provisional step or the write failed
  local py dir out rc tree prov
  if ! py=$(resolve_python 2>/dev/null); then
    echo "pass-tree: generated outputs were NOT regenerated — no usable python launcher; the merge commits what the resolution left, and the bar grades them." >&2
    return 0
  fi
  if ! dir=$(resolve_kit_dir "$py" run-gates regen.py "$KIT_DIR" 2>/dev/null) || [ ! -f "$ROOT/$dir/regen.py" ]; then
    echo "pass-tree: generated outputs were NOT regenerated — no regen.py beside this kit; the merge commits what the resolution left, and the bar grades them." >&2
    return 0
  fi
  out=$(mktemp) || { echo "pass-tree: cannot create a scratch file for the regeneration's output" >&2; return 1; }
  if ! tree=$(GIT write-tree); then
    rm -f "$out"; echo "pass-tree: the provisional merge failed at write-tree: the index could not be written as a tree" >&2; return 1
  fi
  if ! prov=$(GIT commit-tree "$tree" -p "$1" -p "$2" -F "$3"); then
    rm -f "$out"; echo "pass-tree: the provisional merge failed at commit-tree: no commit was made over tree ${tree:0:8}" >&2; return 1
  fi
  if ! GIT update-ref --no-deref HEAD "$prov"; then
    rm -f "$out"; echo "pass-tree: the provisional merge failed at the detach: HEAD could not be moved onto ${prov:0:8}" >&2; return 1
  fi
  "$py" "$ROOT/$dir/regen.py" --write >"$out" 2>&1; rc=$?
  grep -v -e ' · moved: none$' "$out" >&2 || :
  rm -f "$out"
  if ! GIT symbolic-ref HEAD "$HW_REF"; then
    echo "pass-tree: the provisional merge failed at the re-attach: HEAD is still detached on ${prov:0:8}, not on $HW_REF" >&2
    return 1
  fi
  [ "$rc" = 0 ]
}

# The restore after the merge started: exact because `--merge` required a clean tree, untracked files
# included, so every untracked file present is one this verb made. Ignored files are never touched.
# HEAD goes back on the run's branch first, so a failure while it is detached on the provisional merge
# resets to the pre-merge commit; where HEAD is already on the branch, the re-attach writes what it holds.
remove_merge_attempt() { # -> 0 the tree is at HEAD, nothing staged, no merge in progress, no new file
  GIT symbolic-ref HEAD "$HW_REF" && GIT reset -q --hard HEAD && GIT clean -qfd
}

# The pass's worktree, only the one `check_pass_holder` admitted, then the branch.
remove_pass_tree() { # (PT_BRANCH, PT_WHERE) -> 0 both gone · 1 with what is left printed
  if [ -n "$PT_WHERE" ] && ! GIT worktree remove --force "$PT_WHERE" >&2; then
    echo "pass-tree: NOTE - git could not remove the worktree $PT_WHERE, so it and branch $PT_BRANCH are left" >&2
    return 1
  fi
  if ! GIT branch -q -D "$PT_BRANCH" >&2; then
    echo "pass-tree: NOTE - git could not delete branch $PT_BRANCH, so it is left" >&2
    return 1
  fi
}

cmd_merge_tree() { # slug · unit · branch · from -> 0 merged, its sha printed · 1 refused
  local slug=$1 unit=$2 rel st head mb tip f msg p bad="" left="" rc kd
  check_pass_tree_run "$slug" || return 1
  if ! st=$(GIT status --porcelain --untracked-files=normal 2>/dev/null) || [ -n "$st" ]; then
    print_pass_tree_refusal "this tree is not clean, untracked files included, so a failed merge could not be restored exactly; commit or remove what git status lists. Nothing was written"
    return 1
  fi
  check_pass_branch "$3" || return 1
  if ! GIT rev-parse --verify -q "refs/heads/$PT_BRANCH" >/dev/null; then
    print_pass_tree_refusal "no branch $PT_BRANCH exists, so there is no pass of $unit to merge; nothing was written"
    return 1
  fi
  check_pass_holder || return 1
  head=$(GIT rev-parse --verify -q HEAD) || { print_pass_tree_refusal "HEAD does not resolve; nothing was written"; return 1; }
  if [ "$(GIT rev-list --count "HEAD..refs/heads/$PT_BRANCH" 2>/dev/null)" = 0 ]; then
    print_pass_tree_refusal "$unit's branch $PT_BRANCH holds no commit HEAD lacks, so the pass committed nothing to merge; take it away with --remove $slug --branch $PT_BRANCH. Nothing was written"
    return 1
  fi
  if ! [[ $4 =~ ^[0-9a-f]{7,64}$ ]]; then
    PT_FROM=""
    print_pass_tree_refusal "--from '$4' is not 7 to 64 lowercase hex digits, so the fork point cannot be compared; nothing was written"
    return 1
  fi
  if ! PT_FROM=$(GIT rev-parse --verify -q "$4^{commit}"); then
    PT_FROM=""
    print_pass_tree_refusal "--from '$4' names no commit here, so the fork point cannot be compared; nothing was written"
    return 1
  fi
  mb=$(GIT merge-base HEAD "refs/heads/$PT_BRANCH") || { print_pass_tree_refusal "$PT_BRANCH and HEAD share no merge base; nothing was written"; return 1; }
  if [ "$mb" != "$PT_FROM" ]; then
    print_pass_tree_refusal "$unit's branch $PT_BRANCH forks from ${mb:0:8}, not from ${PT_FROM:0:8}, the commit it was dispatched from: its builder did not reset its worktree to that commit, so the merge would carry another line's history in"
    return 1
  fi
  runmd_of "$slug" >/dev/null; rel=$_runmd
  if ! GIT diff --quiet "$mb" "refs/heads/$PT_BRANCH" -- "$rel"; then
    print_pass_tree_refusal "$unit's branch $PT_BRANCH changed the run-state file $rel since ${mb:0:8}, which only the main loop writes while passes run (M6 condition 3); nothing was written"
    return 1
  fi
  f=$(mktemp) && msg=$(mktemp) || { print_pass_tree_refusal "cannot create a scratch file; nothing was written"; return 1; }
  # Git's lines go to the scratch file, not to stderr: `-q` still prints `CONFLICT ... in <path>` for
  # a path the resolution then admits, and the refusal below must name only the paths it refused.
  GIT merge --no-ff --no-commit -q "refs/heads/$PT_BRANCH" >"$f" 2>&1; rc=$?
  if { [ "$rc" != 0 ] && [ "$rc" != 1 ]; } || ! GIT rev-parse -q --verify MERGE_HEAD >/dev/null; then
    cat "$f" >&2; remove_merge_attempt; rm -f "$f" "$msg"
    print_pass_tree_refusal "git merge of $PT_BRANCH exited $rc and left no merge in progress, as its lines above say; HEAD is ${head:0:8} as before"
    return 1
  fi
  GIT -c core.quotePath=false diff --name-only --diff-filter=U -z >"$f"
  while IFS= read -r -d '' p; do
    check_resolvable_path "$p" "$mb" "$PT_BRANCH" || bad="$bad $p"
  done <"$f"
  if [ -n "$bad" ]; then
    GIT merge --abort >&2 2>&1 || remove_merge_attempt; rm -f "$f" "$msg"
    print_pass_tree_refusal "$unit's pass and the run's branch both changed$bad, which are neither an effective generated output nor a gen-region-only change, so the two passes were not disjoint; the merge was aborted, HEAD is ${head:0:8} as before, and $PT_BRANCH is left as it was"
    return 1
  fi
  while IFS= read -r -d '' p; do
    if ! { GIT checkout -q --ours -- "$p" && GIT add -- "$p"; } >&2 2>&1; then
      remove_merge_attempt; rm -f "$f" "$msg"
      print_pass_tree_refusal "the conflicted path $p could not be resolved to this side, so the merge was undone; HEAD is ${head:0:8} as before"
      return 1
    fi
  done <"$f"
  tip=$(GIT rev-parse "refs/heads/$PT_BRANCH")
  printf "merge(%s): %s's pass tree\n\nMerges %s at %s, dispatched from %s.\n\nPass: none\n" \
    "$slug" "$unit" "$PT_BRANCH" "${tip:0:8}" "${PT_FROM:0:8}" >"$msg"
  if ! run_pass_tree_regen "$head" "$tip" "$msg"; then
    remove_merge_attempt; rm -f "$f" "$msg"
    print_pass_tree_refusal "the regeneration failed, as its lines above say, so the merge was undone; HEAD is ${head:0:8} as before"
    return 1
  fi
  GIT add -u && GIT -c core.quotePath=false ls-files --others --exclude-standard -z >"$f" || {
    remove_merge_attempt; rm -f "$f" "$msg"
    print_pass_tree_refusal "the regenerated outputs could not be staged, so the merge was undone; HEAD is ${head:0:8} as before"
    return 1
  }
  while IFS= read -r -d '' p; do
    if check_generated_output "$p" "$GENERATED_INDEXES"; then GIT add -- "$p"; else left="$left $p"; fi
  done <"$f"
  [ -z "$left" ] || echo "pass-tree: NOTE - left untracked, since no effective generated output covers them:$left" >&2
  if ! GIT commit -q -F "$msg" >&2; then
    remove_merge_attempt; rm -f "$f" "$msg"
    print_pass_tree_refusal "the merge commit was refused, as the lines above say, so the merge was undone; HEAD is ${head:0:8} as before"
    return 1
  fi
  rm -f "$f" "$msg"
  if ! remove_pass_tree; then
    kd=$(derive_self_rel "$KIT_DIR") || kd=$KIT_DIR
    echo "pass-tree: NOTE - the merge landed; take away what is left with: bash $kd/pass-tree.sh --remove $slug --branch $PT_BRANCH" >&2
  fi
  GIT rev-parse HEAD
}

cmd_remove_tree() { # slug · branch -> 0 taken away or already absent · 1 refused
  local n
  check_pass_tree_run "$1" || return 1
  check_pass_branch "$2" || return 1
  if ! GIT rev-parse --verify -q "refs/heads/$PT_BRANCH" >/dev/null; then
    echo "pass-tree: NOTE - no branch $PT_BRANCH exists, so no worktree can hold it and there is nothing to take away" >&2
    return 0
  fi
  check_pass_holder || return 1
  n=$(GIT rev-list --count "refs/heads/$PT_BRANCH" --not --exclude="$PT_BRANCH" --branches --remotes --tags 2>/dev/null) || n=""
  if [ "$n" != 0 ]; then
    print_pass_tree_refusal "$PT_BRANCH holds ${n:-an uncounted number of} commit(s) no other branch, remote-tracking ref or tag holds, so deleting it would lose the pass's work; bring it back with --merge. Nothing was written"
    return 1
  fi
  remove_pass_tree || { print_pass_tree_refusal "the pass tree of $PT_BRANCH could not be taken away whole, as the note above says"; return 1; }
}

main() { # argv -> the verb's exit
  local verb="" slug="" unit="" branch="" from="" seen=" "
  while [ $# -gt 0 ]; do
    case "$1" in
      --merge|--remove|--pass|--branch|--from)
        case "$seen" in *" $1 "*) echo "$PT_USAGE" >&2; exit 2 ;; esac
        [ $# -ge 2 ] || { echo "$PT_USAGE" >&2; exit 2; }
        seen="$seen$1 "
        case "$1" in
          --merge|--remove) [ -z "$verb" ] || { echo "$PT_USAGE" >&2; exit 2; }; verb=$1; slug=$2 ;;
          --pass) unit=$2 ;;
          --branch) branch=$2 ;;
          --from) from=$2 ;;
        esac
        shift 2 ;;
      *) echo "$PT_USAGE" >&2; exit 2 ;;
    esac
  done
  case "$verb" in
    --merge) case "$seen" in *" --pass "*) ;; *) echo "$PT_USAGE" >&2; exit 2 ;; esac
             case "$seen" in *" --branch "*) ;; *) echo "$PT_USAGE" >&2; exit 2 ;; esac
             case "$seen" in *" --from "*) ;; *) echo "$PT_USAGE" >&2; exit 2 ;; esac ;;
    --remove) case "$seen" in *" --pass "*|*" --from "*) echo "$PT_USAGE" >&2; exit 2 ;; esac
              case "$seen" in *" --branch "*) ;; *) echo "$PT_USAGE" >&2; exit 2 ;; esac ;;
    *) echo "$PT_USAGE" >&2; exit 2 ;;
  esac
  if ! check_slug_shape "$slug"; then
    echo "pass-tree: '$slug' is not a build-folder name. $PT_USAGE" >&2; exit 2
  fi
  if [ "$verb" = --merge ]; then
    local mid=${unit#*-}; mid=${mid%-*}  # census: kept slug-grammar the first and the last segment stripped
    if ! [[ $unit =~ ^${UNIT_ID_ERE}$ ]] || [ "$mid" != "$slug" ]; then
      echo "pass-tree: '$unit' is not a unit id of build $slug. $PT_USAGE" >&2; exit 2
    fi
  fi
  load_driver_conf >&2
  if [ "$verb" = --merge ]; then cmd_merge_tree "$slug" "$unit" "$branch" "$from"; exit $?; fi
  cmd_remove_tree "$slug" "$branch"; exit $?
}

main "$@"
