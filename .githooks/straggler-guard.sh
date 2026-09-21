#!/usr/bin/env bash
# straggler-guard.sh — the shards-to-builds STRAGGLER predicates, sourced by the tracked hooks
# beside it. TOOL-dDerivedDocket-13.
#
# A STRAGGLER is a branch that predates the per-build backlog and still edits the authored shards.
# Merging one after the default branch has flipped can lose a row change with nobody watching: the
# shards side edits a file the builds side no longer authors, so a clean three-way merge takes
# either side and neither outcome is a conflict. The transition audit (hygiene check 25) finds that
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
# there — the documented inert case. `tools/check-wiring.sh` marks such a straggler `hooks own-tree`
# from any post-flip session tree, the drift signal lists it from any node, and hygiene check 25 at
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

read_conf_value() { # $1 = conf blob text · $2 = key -> its value, quotes and edge blanks stripped
  local line
  line=$(printf '%s\n' "$1" | grep -E "^[[:space:]]*$2[[:space:]]*=" | tail -n 1)
  [ -n "$line" ] || return 1
  line=${line#*=}
  line=$(printf '%s' "$line" | tr -d "\"'\r")
  printf '%s' "$line" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

read_families() { # $1 = conf blob text -> one FAMILY token per line, from `<stream>:<FAMILY>` pairs
  local raw
  raw=$(read_conf_value "$1" FAMILIES) || return 1
  # Deliberately unquoted: the declaration is a space-separated list and the split is the parse.
  # shellcheck disable=SC2086
  printf '%s\n' $raw | sed -n 's/^[^:]*:\(.*\)$/\1/p'
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

init_straggler_guard() { # 0 = FLIPPED and the globals are set · 1 = nothing to do here
  # THE DEFAULT BRANCH'S OWN CONF, and the flip is observed WHERE IT LANDS. The remote-tracking
  # default is read first, so a node whose local `main` was never fast-forwarded is not dormant on
  # a flip the fleet has already taken. `.githooks/pre-push` resolves the same way and for the same
  # reason: the OBSERVED default wins and `GOV_DEFAULT_BRANCH` is a cross-check that can warn and
  # never select — `TOOL-aStandingWrit-5` records an environment value that disabled the
  # primary-tree branch guard by naming a branch nobody was pushing.
  STRAGGLER_READY=0
  STRAGGLER_WATCHED=()
  local text="" ref="" def="" mode="" fam obs
  if text=$(read_blob_at "refs/remotes/origin/HEAD:$STRAGGLER_CONF_REL"); then
    ref=refs/remotes/origin/HEAD
  else
    def=${GOV_DEFAULT_BRANCH:-main}
    if git rev-parse --verify --quiet "refs/heads/$def" >/dev/null 2>&1; then
      ref="refs/heads/$def"
      # The branch is there and carries no conf: the memory-tree kit is not adopted in this
      # repository, which is a legal state and not this layer's business. Silent.
      text=$(read_blob_at "$ref:$STRAGGLER_CONF_REL") || return 1
    elif git rev-parse --verify --quiet refs/remotes/origin/HEAD >/dev/null 2>&1; then
      return 1
    else
      echo "$STRAGGLER_SAY: this clone observes no default branch — origin/HEAD is unset and '$def' is no local branch — so the backlog-mode question cannot be asked and NOTHING was checked here. Fix once: git remote set-head origin -a, or export GOV_DEFAULT_BRANCH=<a branch that exists>."
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
  # Unit 9's check 25 was narrowed to this same population, so the two layers read one archive set.
  STRAGGLER_WATCHED=("$STRAGGLER_MEMORY_ROOT/backlog/")
  while read -r fam; do
    [ -n "$fam" ] || continue
    STRAGGLER_WATCHED+=("$STRAGGLER_MEMORY_ROOT/archive/$fam.*.md")
  done <<< "$(read_families "$text" 2>/dev/null || true)"

  if [ -n "${GOV_DEFAULT_BRANCH:-}" ] && [ "$ref" = refs/remotes/origin/HEAD ]; then
    obs=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null || true); obs=${obs#origin/}
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
  echo "${pre}  python $kit/migrate_backlog.py --relocate --as <your-slug>"
  echo "${pre}  git add $m/ && git commit"
  echo "${pre}Already landed without this? Any node:  python $kit/migrate_backlog.py --repair <merge-sha>"
  echo "${pre}A branch nobody will revisit? From the default branch:  python $kit/migrate_backlog.py --ingest <ref>"
}

true
