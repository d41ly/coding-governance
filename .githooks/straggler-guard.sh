#!/usr/bin/env bash
# straggler-guard.sh — the shards-to-builds STRAGGLER predicates, sourced by the tracked hooks
# beside it. TOOL-dDerivedDocket-13.
#
# A STRAGGLER is a branch that predates the per-build backlog and still edits the authored shards.
# Merging one after the default branch has flipped can lose a row change with nobody watching: the
# shards side edits a file the builds side no longer authors, so a clean three-way merge takes
# either side and neither outcome is a conflict. The transition audit (hygiene check 26) finds that
# AFTERWARDS. These hooks are the layer that instructs the branch BEFORE the merge, at each moment
# its own node can see it — a commit, a rebase, a push.
#
# WHY A LIBRARY BESIDE THE HOOKS, AND NOT INSIDE A KIT. A pre-flip branch's own tree carries the OLD
# kit and no straggler rule, so a rule living in any kit the hook resolves through the committing
# tree would never reach the branch it is about. The hooks that run are whatever `core.hooksPath`
# resolves to, which is a checkout rather than a commit — so the rule is reachable there and is
# sourced through the CALLING HOOK's own directory, never through the tree being committed.
#
# WHICH HOOK FILES RUN. The shared `core.hooksPath` applies unless a worktree's config.worktree sets
# its own, and the value in effect decides which hook files run: an ABSOLUTE value runs the hooks of
# the checkout it names, the relative `.githooks` check-wiring writes runs each worktree's own. So
# this library reaches a straggler checked out in a linked worktree only under an ABSOLUTE value.
# Under the relative one that worktree runs its own pre-flip hook files and this layer is inert
# there — the documented inert case. `<prefix>/check-wiring.sh` marks such a straggler `hooks own-tree`
# from any post-flip session tree, the drift signal lists it from any node, and hygiene check 26 at
# the merge bar is what GUARANTEES. These layers instruct; the bar decides.
#
# WHAT IT READS. Git objects and the staged name list, and nothing else. No python, no kit module,
# no file in the working tree. Two reads on a repository that has not flipped: the default branch's
# committed `.memory-tree.conf` blob, and (only when that first spelling misses) whatever it takes
# to tell "no default branch" from "the kit is not adopted here".
#
# WHAT THIS DOES NOT CHECK, said out loud because a structural check reads as a semantic one to
# everybody who did not write it:
#   * It never decides whether a row change is ACCOUNTED. That is the transition audit's judgement
#     and the relocation engine's inventory; this file counts nothing and prints instructions.
#   * It reads `.memory-tree.conf` at the repository root. A memory tree installed under a prefix
#     would need the prefix derivation `transition_audit.derive_conf_rel` makes, and this file does
#     not make it: it would read as not-flipped there and stay dormant, which is a silent skip and
#     is stated rather than closed.
#   * A refusal is bypassed by `--no-verify`, the deliberate bypass every other refusal here uses.
#   * A node that has not pulled the default branch runs old hook files and never reaches this at
#     all, which is the same hole `memory/gotchas/hookspath-resolves-into-another-checkout.md` owns.
#
# LIVENESS. Every predicate below answers from something it read. An unresolvable default branch
# prints a NAMED line and allows rather than returning a reassuring "nothing to do": a probe that
# cannot move says so.

# The kit directory name and the conf basename, as VALUES. Assembled rather than spelled, the same
# rule `.githooks/commit-msg` follows: a tracked hook is graded for install-prefix literals and a
# spelled kit path is one, and the prefix an adopter installs at is not this file's to guess.
STRAGGLER_KIT_NAME=memory-tree
STRAGGLER_CONF_REL=.memory-tree.conf
STRAGGLER_SAY=straggler-guard
STRAGGLER_READY=0
STRAGGLER_DEF_REF=""
STRAGGLER_DEF_SHA=""
STRAGGLER_MEMORY_ROOT=memory
STRAGGLER_WATCHED=()

read_blob_at() { # $1 = a `<rev>:<path>` spec -> the blob's text · rc 1 when it does not resolve
  # THE SPEC GOES IN ON STDIN, never in argv, and that is not a style choice. A POSIX-emulation
  # shell on Windows rewrites an ARGUMENT that looks like a path list: `refs/remotes/origin/HEAD:
  # .memory-tree.conf` arrives at git as `refs\remotes\origin\HEAD;.memory-tree.conf` and git
  # reports "not a valid object name" — measured in this unit's own scratch fixture, where every
  # predicate below read as dormant against a repository that had flipped. `git cat-file --batch`
  # reads its specs from stdin, which nothing converts, and it costs ONE process.
  local raw first
  raw=$(printf '%s\n' "$1" | git cat-file --batch 2>/dev/null)
  first=$(printf '%s\n' "$raw" | head -n 1)
  case "$first" in *" blob "*) ;; *) return 1 ;; esac
  printf '%s' "$raw" | tail -n +2
}

read_conf_value() { # $1 = conf blob text · $2 = key -> its value as the kit's parser reads it · rc 1 when no line declares it
  # THE KIT'S ONE LINE PARSER, PORTED RULE FOR RULE — `parse_conf_line` in the memory-tree kit's
  # `tree_lib.py`, applied the way its `parse_conf` applies it: every line, the LAST declaration
  # wins. The pipeline this replaces (grep, tr, sed) was a second reader of one file, and it kept
  # `BACKLOG_MODE=builds   # flipped` as `builds   # flipped` and read `export BACKLOG_MODE=builds`
  # as no declaration at all. Both spellings are legal — the hygiene gate SOURCES this file — so a
  # flipped repository spelling either read as unflipped here and every straggler layer went dormant
  # in silence (closing diff review round 1, F6).
  #
  # WHY A PORT AND NOT A CALL. The subjects are git OBJECTS — the default branch's conf, a merge
  # base's, a straggler's own commits' — and this file neither executes one (sourcing a blob would
  # run whatever a fetched commit wrote) nor starts python on every commit (unit 13's spec rules the
  # library python-free). A deliberate re-parse is only safe beside something asserting it agrees,
  # so `straggler-guard.test.sh` runs THIS function and the kit's `parse_conf` over one table of
  # spellings and reds on any difference.
  #
  # NOT MODELLED, as the kit's own docstring says of itself: command substitution, expansion, line
  # continuations. Whitespace here is the ASCII set; python's `strip` also takes Unicode spaces.
  printf '%s\n' "$1" | awk -v want="$2" -v sq="'" '
    function trim(s) { sub(/^[ \t\r\v\f]+/, "", s); sub(/[ \t\r\v\f]+$/, "", s); return s }
    function peel(s, c) {
      while (length(s) > 0 && substr(s, 1, 1) == c) s = substr(s, 2)
      while (length(s) > 0 && substr(s, length(s), 1) == c) s = substr(s, 1, length(s) - 1)
      return s
    }
    {
      line = trim($0)
      if (line == "" || substr(line, 1, 1) == "#") next
      eq = index(line, "="); if (eq == 0) next
      k = trim(substr(line, 1, eq - 1)); v = substr(line, eq + 1)
      if (k ~ /^export[ \t]/) k = trim(substr(k, 7))
      if (k == "" || k != want) next
      found = 1
      # The WORD rule: whitespace right after `=` ends the assignment, so the value is empty.
      if (v ~ /^[ \t\r\v\f]/) { val = ""; next }
      v = trim(v)
      q = substr(v, 1, 1)
      if (q == "\"" || q == sq) {
        e = index(substr(v, 2), q)
        if (e > 0) { val = substr(v, 2, e - 1); next }
        # An unterminated quote falls through to the unquoted scan, as the kit parser does.
      }
      # Unquoted: a `#` that FOLLOWS whitespace begins a comment; one glued to a word is data.
      for (i = 2; i <= length(v); i++)
        if (substr(v, i, 1) == "#" && substr(v, i - 1, 1) ~ /[ \t\r\v\f]/) { v = trim(substr(v, 1, i - 1)); break }
      val = peel(peel(v, "\""), sq)
    }
    END { if (!found) exit 1; printf "%s", val }'
}

read_conf_modes() { # $@ = commits -> one mode token per DISTINCT conf blob among them
  # ONE `cat-file --batch-check` for every commit, then one read per DISTINCT blob. A history
  # re-uses one conf blob for hundreds of commits at a time, so this costs a handful of objects
  # however long the lineage is — the shape `transition_audit.read_modes` uses, in shell.
  #
  # A commit whose tree has NO conf declares nothing, which reads as `shards`. That is the same
  # default the kit's own parser takes, and it is the safe direction here: it can only make this
  # layer instruct where it need not, never stay silent where it must not.
  [ "$#" -gt 0 ] || return 0
  local sha specs="" check blob
  for sha in "$@"; do specs="$specs$sha:$STRAGGLER_CONF_REL
"; done
  check=$(printf '%s' "$specs" | git cat-file --batch-check 2>/dev/null)
  printf '%s\n' "$check" | grep -qvE ' blob [0-9]+$' && echo shards
  printf '%s\n' "$check" | sed -n 's/^\([0-9a-f]\{7,\}\) blob [0-9]*$/\1/p' | sort -u |
  while read -r blob; do
    [ -n "$blob" ] || continue
    if [ "$(read_conf_value "$(git cat-file -p "$blob" 2>/dev/null)" BACKLOG_MODE 2>/dev/null || true)" = builds ]; then
      echo builds
    else
      echo shards
    fi
  done
}

# The remote ladder (TOOL-dLadderedRemote-2), INLINED byte-identically from the canonical copy
# named on its marker line and gated by the resolve-python self-test.
# >>> remote_ladder_sh -- canonical copy: resolve-remote.sh in the gov lib dir (byte-identical; gated)
# resolve_remote_sh -> RR_REMOTE RR_BRANCH RR_OBSERVED RR_WHY, rc 0; rc 1 with RR_WHY on a refusal.
# The ladder, row for row, is resolve_remote.py in the gov lib dir: GOV_REMOTE, else the current
# branch remote unless it is ".", else the ONLY remote; several and none chosen, or a name that is
# no remote here, refuses naming GOV_REMOTE; no remote at all is RR_REMOTE="" and rc 0. RR_OBSERVED
# is what <remote>/HEAD names; RR_BRANCH is GOV_DEFAULT_BRANCH, else RR_OBSERVED. Fetches nothing.
# RR_GIT names the git command, so a caller holding a pinned wrapper function passes it.
resolve_remote_sh() {
  local _rr_git=${RR_GIT:-git} _rr_names _rr_n _rr_list _rr_cur _rr_where _rr_how=GOV_REMOTE _rr_head _rr_bad
  RR_REMOTE=${GOV_REMOTE:-}; RR_BRANCH=""; RR_OBSERVED=""; RR_WHY=""
  _rr_names=$("$_rr_git" remote 2>/dev/null) || _rr_names=""
  _rr_n=$(printf "%s" "$_rr_names" | grep -c . || true)
  _rr_list=$(printf "%s" "$_rr_names" | tr "\n" " ")
  [ -n "$_rr_list" ] || _rr_list=none
  # FULL refs, never `--short`: a tag or branch sharing the name makes the short form ambiguous.
  _rr_cur=$("$_rr_git" symbolic-ref --quiet HEAD 2>/dev/null) || _rr_cur=""
  case "$_rr_cur" in refs/heads/?*) _rr_cur=${_rr_cur#refs/heads/} ;; *) _rr_cur="" ;; esac
  if [ -z "$RR_REMOTE" ] && [ -n "$_rr_cur" ]; then
    RR_REMOTE=$("$_rr_git" config "branch.$_rr_cur.remote" 2>/dev/null) || RR_REMOTE=""
    _rr_how="branch.$_rr_cur.remote"
    [ "$RR_REMOTE" != . ] || RR_REMOTE=""
  fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -eq 1 ]; then RR_REMOTE=$_rr_names; fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -gt 1 ]; then
    _rr_where="a detached HEAD"; [ -z "$_rr_cur" ] || _rr_where="branch $_rr_cur"
    RR_WHY="cannot choose a remote: GOV_REMOTE is unset, $_rr_where has no configured remote, and this repository has $_rr_n remotes ($_rr_list). Name it: export GOV_REMOTE=<remote>."
    return 1
  fi
  # A name holding whitespace is no remote: `grep -F` would split it into several patterns.
  case "$RR_REMOTE" in *[[:space:]]*) _rr_bad=1 ;; *) _rr_bad=0 ;; esac
  if [ -n "$RR_REMOTE" ] && { [ "$_rr_bad" = 1 ] || ! printf "%s\n" "$_rr_names" | grep -qxF -- "$RR_REMOTE"; }; then
    RR_WHY="$_rr_how names $RR_REMOTE, which is no remote of this repository ($_rr_list). Name one that is: export GOV_REMOTE=<remote>."
    RR_REMOTE=""
    return 1
  fi
  if [ -n "$RR_REMOTE" ]; then
    _rr_head=$("$_rr_git" symbolic-ref --quiet "refs/remotes/$RR_REMOTE/HEAD" 2>/dev/null) || _rr_head=""
    case "$_rr_head" in "refs/remotes/$RR_REMOTE"/?*) RR_OBSERVED=${_rr_head#"refs/remotes/$RR_REMOTE"/} ;; esac
  fi
  RR_BRANCH=${GOV_DEFAULT_BRANCH:-$RR_OBSERVED}
  return 0
}
# <<< remote_ladder_sh
init_straggler_guard() { # 0 = FLIPPED and the globals are set · 1 = nothing to do here
  # THE DEFAULT BRANCH'S OWN CONF, and the flip is observed WHERE IT LANDS. The remote-tracking
  # default is read first, so a node whose local `main` was never fast-forwarded is not dormant on
  # a flip the fleet has already taken. `.githooks/pre-push` resolves the same way and for the same
  # reason: the OBSERVED default wins and `GOV_DEFAULT_BRANCH` is a cross-check that can warn and
  # never select — `TOOL-aStandingWrit-5` records an environment value that disabled the
  # primary-tree branch guard by naming a branch nobody was pushing.
  STRAGGLER_READY=0
  STRAGGLER_WATCHED=()
  # THE REMOTE IS THE LADDER'S above (TOOL-dLadderedRemote-2). This read a literal remote name, so
  # on a node whose remote is named after the project it never observed the flip at all. A ladder
  # refusal is announced and checks nothing, as a clone observing no default branch always was.
  local text="" ref="" def="" mode="" fam famdecl pair obs rhead=""
  if ! resolve_remote_sh; then
    echo "$STRAGGLER_SAY: this clone observes no default branch — $RR_WHY — so the backlog-mode question cannot be asked and NOTHING was checked here."
    return 1
  fi
  [ -z "$RR_REMOTE" ] || rhead="refs/remotes/$RR_REMOTE/HEAD"
  if [ -n "$rhead" ] && text=$(read_blob_at "$rhead:$STRAGGLER_CONF_REL"); then
    ref=$rhead
  else
    def=${GOV_DEFAULT_BRANCH:-main}
    if git rev-parse --verify --quiet "refs/heads/$def" >/dev/null 2>&1; then
      ref="refs/heads/$def"
      # The branch is there and carries no conf: the memory-tree kit is not adopted in this
      # repository, which is a legal state and not this layer's business. Silent.
      text=$(read_blob_at "$ref:$STRAGGLER_CONF_REL") || return 1
    elif [ -n "$rhead" ] && git rev-parse --verify --quiet "$rhead" >/dev/null 2>&1; then
      return 1
    else
      echo "$STRAGGLER_SAY: this clone observes no default branch — ${rhead:-a remote HEAD} is unset and '$def' is no local branch — so the backlog-mode question cannot be asked and NOTHING was checked here. Fix once: ${RR_REMOTE:+git remote set-head $RR_REMOTE -a, or }export GOV_DEFAULT_BRANCH=<a branch that exists>."
      return 1
    fi
  fi
  mode=$(read_conf_value "$text" BACKLOG_MODE 2>/dev/null || true)
  [ "$mode" = builds ] || return 1

  STRAGGLER_DEF_REF="$ref"
  STRAGGLER_DEF_SHA=$(git rev-parse --verify --quiet "$ref^{commit}" 2>/dev/null || true)
  if [ -z "$STRAGGLER_DEF_SHA" ]; then
    echo "$STRAGGLER_SAY: '$ref' declares the per-build backlog but resolves to no commit, so no lineage question can be asked against it and NOTHING was checked here."
    return 1
  fi
  STRAGGLER_MEMORY_ROOT=$(read_conf_value "$text" MEMORY_ROOT 2>/dev/null || true)
  [ -n "$STRAGGLER_MEMORY_ROOT" ] || STRAGGLER_MEMORY_ROOT=memory
  STRAGGLER_MEMORY_ROOT=${STRAGGLER_MEMORY_ROOT%/}

  # THE WATCHED PATHS: the backlog shards, plus the FAMILY-NAMED rotated archives and NOT the
  # archive directory as a whole. `archive/` also holds the rotated decision log, the retired
  # ledger shards and the frozen charter snapshots; rotating the decision log is routine and has
  # NOTHING to relocate, so a branch that only rotated one must never draw a relocation recipe.
  # Unit 9's check 26 was narrowed to this same population, so the two layers read one archive set.
  STRAGGLER_WATCHED=("$STRAGGLER_MEMORY_ROOT/backlog/")
  # THE FAMILIES ARE SPLIT IN THIS SHELL, word by word, and never read back out of a here-string over
  # a function's substitution: that feed waits on a grandchild's pipe under MSYS, the shell-hygiene
  # leg's class. A `<stream>:<FAMILY>` pair yields what follows its first colon; a word with nothing
  # there yields nothing, as the sed this replaces printed an empty line the loop then skipped.
  famdecl=$(read_conf_value "$text" FAMILIES 2>/dev/null || true)
  # Deliberately unquoted: the declaration is a space-separated list and the split is the parse.
  # shellcheck disable=SC2086
  for pair in $famdecl; do
    case "$pair" in *:?*) ;; *) continue ;; esac
    fam=${pair#*:}
    STRAGGLER_WATCHED+=("$STRAGGLER_MEMORY_ROOT/archive/$fam.*.md")
  done

  if [ -n "${GOV_DEFAULT_BRANCH:-}" ] && [ -n "$rhead" ] && [ "$ref" = "$rhead" ]; then
    obs=$RR_OBSERVED
    if [ -n "$obs" ] && [ "$obs" != "$GOV_DEFAULT_BRANCH" ]; then
      echo "$STRAGGLER_SAY: GOV_DEFAULT_BRANCH names '$GOV_DEFAULT_BRANCH' and this clone observes '$obs' as its default. The OBSERVED branch decides here; the environment value is a cross-check that warns and never selects."
    fi
  fi
  STRAGGLER_READY=1
  return 0
}

check_preflip() { # $1 = subject commit · $2 = base, default the default branch -> 0 = pre-flip
  # PRE-FLIP IS NOT THE TIP'S OWN CONF, and that is the whole predicate. A straggler that pulled the
  # new conf early blinds a tip read while its lineage still holds every old shard commit — the
  # blocker the bypass hunt found. This asks instead whether the branch has INTEGRATED the flip,
  # through its MERGE BASES: once a builds-mode commit is merged in, the merge base IS that commit
  # and the branch is no longer pre-flip, however old the rest of its lineage is.
  local sha="${1:-}" base="${2:-$STRAGGLER_DEF_SHA}" bases m
  [ -n "$sha" ] && [ -n "$base" ] || return 1
  bases=$(git merge-base --all "$base" "$sha" 2>/dev/null || true)
  # No common history at all: nothing has been integrated, so nothing has been integrated FROM the
  # flip either. Pre-flip, and the caller's other predicates decide whether there is anything to say.
  [ -n "$bases" ] || return 0
  # shellcheck disable=SC2086
  for m in $(read_conf_modes $bases); do
    [ "$m" = builds ] && return 1
  done
  return 0
}

check_has_delta() { # $1 = subject commit · $2 = base, default the default branch -> 0 = has a delta
  # IS THERE ANYTHING TO RELOCATE: a commit in the lineage whose OWN tree is in shards mode and
  # which touches a watched path. The mode test is per commit rather than per branch because this
  # is also asked of a tip that has already integrated the flip, where the newest commits are
  # builds-mode and the shards-mode ones are the question.
  local sha="${1:-}" base="${2:-$STRAGGLER_DEF_SHA}" cands m
  [ -n "$sha" ] && [ -n "$base" ] || return 1
  [ "${#STRAGGLER_WATCHED[@]}" -gt 0 ] || return 1
  cands=$(git rev-list "$base..$sha" -- "${STRAGGLER_WATCHED[@]}" 2>/dev/null || true)
  [ -n "$cands" ] || return 1
  # shellcheck disable=SC2086
  for m in $(read_conf_modes $cands); do
    [ "$m" = shards ] && return 0
  done
  return 1
}

check_staged_backlog() { # 0 when the INDEX carries a watched path
  [ "${#STRAGGLER_WATCHED[@]}" -gt 0 ] || return 1
  git diff --cached --name-only -- "${STRAGGLER_WATCHED[@]}" 2>/dev/null | grep -q .
}

check_merge_head_builds() { # 0 when a pending MERGE_HEAD names a builds-mode commit
  # THE RELOCATION MERGE ITSELF is concluded by `git commit` with the restored views staged, so it
  # stages watched paths on a pre-flip branch — exactly the shape pre-commit refuses. It carries a
  # builds-mode MERGE_HEAD, which is what tells the two apart, and `commit-msg` then audits it.
  local gd heads m
  gd=$(git rev-parse --git-dir 2>/dev/null) || return 1
  [ -f "$gd/MERGE_HEAD" ] || return 1
  heads=$(tr -d '\r' < "$gd/MERGE_HEAD")
  [ -n "$heads" ] || return 1
  # shellcheck disable=SC2086
  for m in $(read_conf_modes $heads); do
    [ "$m" = builds ] && return 0
  done
  return 1
}

read_kit_rel() { # the memory-tree kit's directory, DERIVED — never spelled
  # From the DEFAULT BRANCH's own tree first: the recipe names commands the operator runs AFTER
  # merging it, and a pre-flip tree may not carry the engine at all. The committing tree is the
  # fallback, for a repository whose default branch this clone cannot list.
  local hit
  hit=$(git ls-tree -r --name-only "$STRAGGLER_DEF_SHA" 2>/dev/null |
        grep -m 1 -E "(^|/)$STRAGGLER_KIT_NAME/migrate_backlog\.py$" || true)
  [ -n "$hit" ] || hit=$(git ls-files -- "*$STRAGGLER_KIT_NAME/migrate_backlog.py" 2>/dev/null | head -n 1)
  [ -n "$hit" ] || return 1
  printf '%s' "${hit%/migrate_backlog.py}"
}

print_recipe() { # $1 = optional line prefix
  # THE CANONICAL TEXT, rendered at THIS install's prefix and memory root. The relocation engine's
  # `--recipe` prints the same bytes from the one constant that owns them, and the suite beside this
  # file compares the two — so a drift in either is a red rather than two operators reading two
  # different instructions. The substitutions are DERIVED here exactly as they are there.
  local pre="${1:-}" kit m
  m="$STRAGGLER_MEMORY_ROOT"
  kit=$(read_kit_rel || true)
  echo "${pre}This branch predates the per-build backlog. Its edits to $m/backlog/<F>.md must be relocated, not merged."
  if [ -z "$kit" ]; then
    # An empty derivation REFUSES to spell a command: `python /migrate_backlog.py` is worse than no
    # instruction, because it looks like one.
    echo "${pre}The relocation engine is in neither this tree nor the default branch's, so its commands cannot be spelled here. Merge the default branch first, then read the memory-tree kit's README."
    return 0
  fi
  echo "${pre}  git merge <default>       # MERGE, never rebase or squash: those leave no merge to audit"
  echo "${pre}  python $kit/migrate_backlog.py --relocate --as <your-slug>"   # gov:literal-python — a remedy line printed for the operator, never run; its bytes are the engine's --recipe constant
  echo "${pre}  git add $m/ && git commit"
  echo "${pre}Already landed without this? Any node:  python $kit/migrate_backlog.py --repair <merge-sha>"
  echo "${pre}A branch nobody will revisit? From the default branch:  python $kit/migrate_backlog.py --ingest <ref>"
}

true
