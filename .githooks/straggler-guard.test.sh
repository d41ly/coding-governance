#!/usr/bin/env bash
# straggler-guard.test.sh — the arms for the shards-to-builds straggler layer.
#
#   bash .githooks/straggler-guard.test.sh                    # "PASS (n assertions)" + exit 0 = good
#   bash .githooks/straggler-guard.test.sh --topology <repo> <branch>
#
# WHAT IT GRADES. `straggler-guard.sh` and the three hook bodies that source it: the commit refusal
# and its two notices, the rebase refusal, the per-ref push layer, the recipe's parity with the one
# constant that owns it, and the session step's `hooks own-tree` mark. Every arm builds a throwaway
# git repository, installs the real hooks and the real kits into it, writes a history whose SHAPE is
# the question, and runs the real hook. Nothing here re-implements the subject.
#
# WHY IT IS A REPO-SUBJECT LEG AND NOT A HELD SELF-TEST. The recipe-parity arm grades two tracked
# TEXTS — the library's rendering and the relocation engine's `--recipe` — which drift with nobody
# editing a hook. That is the repository-state class the merge bar keeps, so the leg is unguarded by
# chunk and guarded by path, and the suite itself is WITHHELD from adopters: the library and
# `pre-rebase` are gov-only and an adopter wires its own carriers.
#
# THE FIXTURES INSTALL THE KITS AT `scripts/`, deliberately, and it is not arbitrary. Every path in
# the subject is DERIVED, so a fixture built at THIS tree's own prefix would pass a hook that had the
# prefix spelled back in. It also keeps `.githooks/pre-commit`'s hygiene and manifest legs from
# resolving at all, so an arm's verdict is the straggler layer's and never another gate's.
#
# THE STRAGGLER BRANCHES LIVE IN LINKED WORKTREES, for the same reason this project's charter says
# they should: `pre-commit`'s branch guard refuses a commit in the PRIMARY tree while parked off the
# default branch, so a straggler committed there would be refused by the wrong rule. It also puts
# every arm on the topology where `core.hooksPath` actually decides which hook files run.
#
# WHAT IT DOES NOT GRADE, said out loud because a structural check reads as a semantic one. It never
# asserts the hygiene engine's overall verdict over a fixture — a scratch tree is not a conforming
# memory tree. It does not grade the transition audit's own judgement, which is unit 9's suite; it
# grades only that this layer CALLS it at the right sha and routes its three exits correctly. And it
# cannot see a rebase made with `--no-verify`, a squash, or a cherry-pick: those leave no hook call
# and no merge, and that hole is pinned as absence rather than closed.
set -u
# The fixture kits are imported by the real engines, and CPython writes their bytecode beside the
# SOURCE — inside a tree the arms then check out into a linked worktree, where the untracked `.pyc`
# files abort the checkout. Measured, in this unit's own scratch fixture.
export PYTHONDONTWRITEBYTECODE=1

ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
HOOKDIR="$(cd "$(dirname "$0")" && pwd)"
SELF="$HOOKDIR/$(basename "$0")"

# ---------------------------------------------------------------------------- the topology helper
# THE LINKED-WORKTREE TOPOLOGY, IN ONE PLACE. AC12's arms build their worktree through this, and the
# deployer build's scratch clone runs the `--topology` mode, so the two cannot build two topologies
# that drift. It sets NO `core.hooksPath`: each caller sets the value it means to measure, which is
# the whole variable under test.
add_topology_worktree() { # $1 = repo dir · $2 = branch -> prints the new linked worktree's path
  local repo="$1" branch="$2" wt
  [ -n "$repo" ] && [ -n "$branch" ] || { echo "topology: need <repo> and <branch>" >&2; return 2; }
  [ -d "$repo/.git" ] || { echo "topology: '$repo' is no primary tree" >&2; return 2; }
  wt="$repo-wt-$(printf '%s' "$branch" | tr '/' '-')"
  rm -rf "$wt"
  git -C "$repo" worktree prune >/dev/null 2>&1
  git -C "$repo" worktree add -q "$wt" "$branch" || return 2
  printf '%s\n' "$wt"
}

if [ "${1:-}" = "--topology" ]; then
  add_topology_worktree "${2:-}" "${3:-}" || exit 2
  exit 0
fi

# ------------------------------------------------------------------------ this tree's own sources
ENGINE_REL=$(git ls-files -- '*memory-tree/migrate_backlog.py' | head -n 1)
[ -n "$ENGINE_REL" ] || { echo "FAIL the relocation engine is not tracked here, so the recipe has no canonical text to grade against"; exit 2; }
KIT_MT=$(dirname "$ENGINE_REL")
TOOL_ROOT=$(dirname "$KIT_MT")
KIT_MR="$TOOL_ROOT/memory-recall"
KIT_LIB="$TOOL_ROOT/lib"
WIRING="$TOOL_ROOT/check-wiring.sh"
[ -f "$KIT_MR/extract.py" ] || { echo "FAIL the memory-recall sibling is not beside the memory-tree kit at $KIT_MR, and the transition audit keys every row through its grammar"; exit 2; }
[ -f "$WIRING" ] || { echo "FAIL the wiring checker is not at $WIRING, so the session step cannot be exercised"; exit 2; }
# shellcheck source=/dev/null
. "$KIT_LIB/resolve-python.sh"
PY=$(resolve_python) || { echo "FAIL no usable python launcher"; exit 2; }

FLOOR_ASSERTIONS=57

TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT
n=0; st=0
ok()  { n=$((n+1)); }
bad() { echo "FAIL $1"; st=1; n=$((n+1)); }
has() { printf '%s' "$1" | grep -qF -- "$2"; }

# ------------------------------------------------------------------------------ fixture machinery
# The fixture's own kit prefix. `scripts` rather than this tree's, for the reason the header gives.
FX_ROOT=scripts
FX_MT="$FX_ROOT/memory-tree"

write_conf() { # $1 = repo dir, $2 = mode
  { printf 'MEMORY_ROOT=memory\n'
    printf 'DISCIPLINES="tooling"\n'
    printf 'FAMILIES="tooling:TOOL"\n'
    printf 'ROTATION_MODE="cut"\n'
    printf 'BACKLOG_MODE="%s"\n' "$2"
  } > "$1/.memory-tree.conf"
}
write_shard() { # $1 = repo dir, $2 = the text of row 1
  { printf '# TOOL backlog\n\n'
    printf -- '- TOOL-aSeed-1 \xc2\xb7 filed 2026-01-01 \xc2\xb7 %s\n' "$2"
    printf -- '- TOOL-aSeed-2 \xc2\xb7 filed 2026-01-02 \xc2\xb7 the second ask\n'
  } > "$1/memory/backlog/TOOL.md"
}
write_hooks() { # $1 = repo dir — the POST-flip hook files, outside the tree, plus a pre-flip copy in it
  mkdir -p "$1/hk" "$1/.githooks"
  cp "$HOOKDIR/pre-commit" "$HOOKDIR/pre-push" "$HOOKDIR/pre-rebase" \
     "$HOOKDIR/straggler-guard.sh" "$1/hk/"
  chmod +x "$1/hk/pre-commit" "$1/hk/pre-push" "$1/hk/pre-rebase"
  # A pre-flip branch's OWN hook files carry no straggler rule. This is what a linked worktree runs
  # under the relative value `check-wiring.sh --fix` writes, and it is the inert case AC12 measures.
  printf '#!/usr/bin/env bash\nexit 0\n' > "$1/.githooks/pre-commit"
  chmod +x "$1/.githooks/pre-commit"
}
write_kits() { # $1 = repo dir — the real engines, at the fixture's own prefix
  mkdir -p "$1/$FX_ROOT/run-gates"
  printf 'the kit-root probe reads this directory, never a spelled prefix\n' > "$1/$FX_ROOT/run-gates/.keep"
  cp -r "$ROOT/$KIT_MT" "$1/$FX_MT"
  cp -r "$ROOT/$KIT_MR" "$1/$FX_ROOT/memory-recall"
  cp -r "$ROOT/$KIT_LIB" "$1/$FX_ROOT/lib"
  cp "$ROOT/$WIRING" "$1/$FX_ROOT/check-wiring.sh"
  rm -rf "$1/$FX_MT/__pycache__" "$1/$FX_ROOT/memory-recall/__pycache__"
}
init_repo() { # $1 = repo dir — a shards-mode base commit, a bare origin, and the hooks wired
  mkdir -p "$1/memory/backlog" "$1/memory/archive" "$1/memory/builds/aSeed"
  write_hooks "$1"
  printf '__pycache__/\n' > "$1/.gitignore"
  printf '# the seed build\n' > "$1/memory/builds/aSeed/README.md"
  printf '# decisions\n\n- TOOL-aSeed-9 - a decision\n' > "$1/memory/DECISIONS.md"
  printf 'notes\n' > "$1/README.md"
  write_conf "$1" shards
  write_shard "$1" "the first ask"
  git init -q -b main "$1"
  git -C "$1" config user.email arms@example.invalid
  git -C "$1" config user.name arms
  git -C "$1" config commit.gpgsign false
  git -C "$1" config core.autocrlf false
  git -C "$1" add -A >/dev/null 2>&1
  git -C "$1" commit -q --no-verify -m base
  git init -q --bare -b main "$1.git"
  git -C "$1" remote add origin "$1.git"
}
add_origin_head() { # $1 = repo dir — publish main and make origin/HEAD observable
  git -C "$1" push -q --no-verify origin main
  git -C "$1" remote set-head origin -a >/dev/null 2>&1
}
set_builds_mode() { # $1 = repo dir — the commit that switches the default branch
  write_conf "$1" builds
  mkdir -p "$1/memory/builds/aFlip"
  printf '# aFlip\n\n## Asks\n\n## Dispositions\n' > "$1/memory/builds/aFlip/BACKLOG.md"
  git -C "$1" add -A >/dev/null 2>&1
  git -C "$1" commit -q --no-verify -m "flip to builds"
}
write_relocated() { # $1 = repo dir/worktree, $2 = id, $3 = sha
  mkdir -p "$1/memory/builds/aFlip"
  { printf '# aFlip\n\n## Asks\n\n## Dispositions\n\n'
    printf -- '- RELOCATED \xc2\xb7 %s \xc2\xb7 by %s \xc2\xb7 kept: carried forward across the transition\n' "$2" "$3"
  } > "$1/memory/builds/aFlip/BACKLOG.md"
}
run_in() { # $1 = dir, rest = argv — run with the CALLER's cwd inside the fixture
  local d="$1"; shift
  ( cd "$d" && "$@" 2>&1 )
}
read_lib_recipe() { # $1 = repo dir, $2 = hooks dir relative to it -> the library's own rendering
  ( cd "$1" && bash -c ". \"$2/straggler-guard.sh\"; init_straggler_guard >/dev/null 2>&1; print_recipe" 2>/dev/null ) | tr -d '\r'
}

# ============================================================== F1 — a builds default and a straggler
F1="$TMP/f1"
init_repo "$F1"
write_kits "$F1"
git -C "$F1" add -A >/dev/null 2>&1; git -C "$F1" commit -q --no-verify -m "the kits"
F1_BASE=$(git -C "$F1" rev-parse HEAD)
git -C "$F1" checkout -q -b strag
write_shard "$F1" "the first ask, REWORDED by the straggler"
git -C "$F1" commit -q --no-verify -am "the straggler edits a row"
F1_STRAG=$(git -C "$F1" rev-parse HEAD)
git -C "$F1" checkout -q main
set_builds_mode "$F1"
add_origin_head "$F1"
git -C "$F1" config core.hooksPath "$F1/hk"
WT=$(add_topology_worktree "$F1" strag)

# ---- AC1 — a staged shard edit on a pre-flip branch is refused, and --no-verify overrides --------
printf -- '- TOOL-aSeed-3 \xc2\xb7 filed 2026-03-01 \xc2\xb7 a late ask\n' >> "$WT/memory/backlog/TOOL.md"
git -C "$WT" add memory/backlog/TOOL.md
out=$(run_in "$WT" git commit -m "the straggler stages a shard edit"); rc=$?
[ "$rc" != 0 ] || bad "AC1: a staged shard edit on a pre-flip branch was COMMITTED (rc=$rc)"; ok
has "$out" "migrate_backlog.py --relocate --as <your-slug>" \
  || bad "AC1: the refusal does not print the relocation recipe"; ok
out=$(run_in "$WT" git commit --no-verify -m "the straggler stages a shard edit"); rc=$?
[ "$rc" = 0 ] || bad "AC1: --no-verify did not override the refusal (rc=$rc): $out"; ok

# ---- AC2 — a non-backlog commit gets ONE notice and is never refused -----------------------------
printf 'more\n' >> "$WT/README.md"
git -C "$WT" add README.md
out=$(run_in "$WT" git commit -m "a non-backlog commit"); rc=$?
[ "$rc" = 0 ] || bad "AC2: a non-backlog commit on a pre-flip branch was refused (rc=$rc): $out"; ok
notices=$(printf '%s\n' "$out" | grep -c '^pre-commit: note — ')
[ "$notices" = 1 ] || bad "AC2: a non-backlog commit printed $notices notice lines, not exactly one"; ok
has "$out" "still owes a relocation" || bad "AC2: the notice does not say the branch owes a relocation"; ok

# ---- AC1/AC2 — the RELOCATION MERGE stages watched paths and is NOT refused ----------------------
run_in "$WT" git merge --no-ff --no-commit --no-edit main >/dev/null 2>&1
write_shard "$WT" "the first ask, as the RESTORED view renders it"
write_relocated "$WT" TOOL-aSeed-1 "$F1_STRAG"
git -C "$WT" add memory/ >/dev/null 2>&1
out=$(run_in "$WT" git commit -m "conclude the relocation merge"); rc=$?
[ "$rc" = 0 ] || bad "AC2: the relocation merge — watched paths staged under a builds-mode MERGE_HEAD — was REFUSED, so the recipe's own last step cannot complete (rc=$rc): $out"; ok
has "$out" "REFUSING" && bad "AC2: the relocation merge drew the straggler refusal"; ok

# ============================================== F2 — the rebase arms, on an un-merged straggler ----
git -C "$F1" branch -q strag2 "$F1_STRAG"
WT2=$(add_topology_worktree "$F1" strag2)
out=$(run_in "$WT2" git rebase main); rc=$?
[ "$rc" != 0 ] || bad "AC3: a rebase of a HAS-DELTA pre-flip branch onto the builds-mode default was allowed"; ok
has "$out" "migrate_backlog.py --relocate --as <your-slug>" \
  || bad "AC3: the rebase refusal does not print the relocation recipe"; ok
has "$out" "MERGE, never rebase or squash" || bad "AC3: the recipe's first step does not say merge and never rebase"; ok
out=$(run_in "$WT2" git pull --rebase origin main); rc=$?
[ "$rc" != 0 ] || bad "AC3: 'git pull --rebase' passes no branch argument and rebased the straggler anyway"; ok
out=$(run_in "$WT2" git rebase --no-verify main); rc=$?
[ "$rc" = 0 ] || bad "AC3: 'git rebase --no-verify' did not bypass the hook (rc=$rc): $out"; ok

# ---- AC3 — a DECISION-LOG rotation is not a backlog delta ----------------------------------------
# The archive population is the FAMILY-named one. A branch that only rotated the decision log has
# nothing to relocate, so it must draw the merge-first notice and never the recipe, and it rebases.
git -C "$F1" branch -q rot "$F1_BASE"
WT3=$(add_topology_worktree "$F1" rot)
printf '# rotated decisions\n\n- TOOL-aSeed-9 - a decision\n' > "$WT3/memory/archive/DECISIONS.2026-05-01.md"
git -C "$WT3" add memory/archive >/dev/null 2>&1
out=$(run_in "$WT3" git commit -m "rotate the decision log"); rc=$?
[ "$rc" = 0 ] || bad "AC3: a decision-log rotation on a pre-flip branch was refused (rc=$rc): $out"; ok
has "$out" "merge it before filing a new ask" \
  || bad "AC3: a branch with no backlog delta did not draw the merge-first notice: $out"; ok
has "$out" "migrate_backlog.py --relocate" && bad "AC3: a decision-log rotation drew the relocation recipe"; ok
out=$(run_in "$WT3" git rebase main); rc=$?
[ "$rc" = 0 ] || bad "AC3: a branch whose only archive change is a decision-log rotation was refused a rebase (rc=$rc): $out"; ok

# ---- AC4 — a PRE-FLIP, HAS-DELTA feature push gets the recipe and LANDS --------------------------
# Its OWN branch: AC3 rebased strag2 past the flip, so pushing that one would measure the
# other row of the table.
git -C "$F1" branch -q strag4 "$F1_STRAG"
out=$(run_in "$F1" git push origin strag4); rc=$?
[ "$rc" = 0 ] || bad "AC4: a pre-flip feature push was refused, which strands the straggler's only off-node copy (rc=$rc): $out"; ok
has "$out" "migrate_backlog.py --relocate --as <your-slug>" \
  || bad "AC4: the feature push printed no relocation recipe"; ok
git -C "$F1.git" rev-parse --verify --quiet refs/heads/strag4 >/dev/null \
  || bad "AC4: the pre-flip feature branch did not reach the remote"; ok

# ---- AC10 — the recipe is the ONE canonical text ------------------------------------------------
# CR-normalised on both sides: the engine prints through python, whose text-mode stdout emits CRLF
# on Windows, and the library prints through `echo`. The bytes under test are the TEXT, and a
# comparison that reds on a platform's newline is a comparison nobody can keep.
canon=$(run_in "$F1" "$PY" "$FX_MT/migrate_backlog.py" --recipe | tr -d '\r')
mine=$(read_lib_recipe "$F1" hk)
[ -n "$canon" ] || bad "AC10: the relocation engine printed no recipe, so the parity arm would compare two empty strings"; ok
[ "$canon" = "$mine" ] || bad "AC10: the library's recipe differs from the engine's --recipe:
--- engine ---
$canon
--- library ---
$mine"; ok
# The one-byte flip: a copy of the library with a single character changed must NOT compare equal.
mkdir -p "$F1/hkflip"; cp "$F1/hk/straggler-guard.sh" "$F1/hkflip/straggler-guard.sh"
sed -i 's/never rebase or squash/never rebase or squashh/' "$F1/hkflip/straggler-guard.sh"
flipped=$(read_lib_recipe "$F1" hkflip)
[ "$canon" != "$flipped" ] || bad "AC10: a one-byte change to the library's recipe still compared equal to the engine's, so the parity arm grades nothing"; ok

# ============================== F3 — a tip that has INTEGRATED the flip, pushed to a bare remote ---
git -C "$F1" checkout -q -b feat "$F1_STRAG"
git -C "$F1" merge -q --no-ff --no-verify -m "merge the flipped default" main
F3_MERGE=$(git -C "$F1" rev-parse HEAD)
git -C "$F1" checkout -q main
out=$(run_in "$F1" git push origin feat); rc=$?
[ "$rc" != 0 ] || bad "AC5: a feature branch holding an UNACCOUNTED transition merge was pushed (rc=$rc)"; ok
has "$out" "$F3_MERGE" || bad "AC5: the push refusal does not name the transition merge sha"; ok
has "$out" "--repair" || bad "AC5: the push refusal does not name the repair verb"; ok

git -C "$F1" checkout -q feat
write_relocated "$F1" TOOL-aSeed-1 "$F1_STRAG"
git -C "$F1" add -A >/dev/null 2>&1; git -C "$F1" commit -q --no-verify -m "account for the relocation"
git -C "$F1" checkout -q main
out=$(run_in "$F1" git push origin feat); rc=$?
[ "$rc" = 0 ] || bad "AC5: a feature branch whose RELOCATED rows are committed was still refused (rc=$rc): $out"; ok

# The audit module ABSENT from both trees: one skip line naming the ref, and the push lands.
git -C "$F1" checkout -q feat
printf -- '- TOOL-aSeed-5 \xc2\xb7 filed 2026-04-01 \xc2\xb7 another ask\n' >> "$F1/memory/backlog/TOOL.md"
git -C "$F1" commit -q --no-verify -am "another shard edit after the merge"
git -C "$F1" checkout -q main
mv "$F1/$FX_MT/transition_audit.py" "$TMP/ta.bak"
out=$(run_in "$F1" git push origin feat); rc=$?
mv "$TMP/ta.bak" "$F1/$FX_MT/transition_audit.py"
[ "$rc" = 0 ] || bad "AC5: an unresolvable audit module refused the push instead of announcing a skip (rc=$rc): $out"; ok
{ has "$out" "refs/heads/feat" && has "$out" "did NOT run"; } \
  || bad "AC5: an unresolvable audit module printed no skip line naming the ref: $out"; ok

# The module's conf reader BROKEN: a DEAD PROBE line naming the ref, and the push lands.
git -C "$F1" checkout -q feat
printf -- '- TOOL-aSeed-6 \xc2\xb7 filed 2026-04-02 \xc2\xb7 yet another ask\n' >> "$F1/memory/backlog/TOOL.md"
git -C "$F1" commit -q --no-verify -am "one more shard edit"
git -C "$F1" checkout -q main
cp "$F1/$FX_MT/transition_audit.py" "$TMP/ta.orig"
sed -i 's/^def read_mode(/def read_mode_BROKEN(/' "$F1/$FX_MT/transition_audit.py"
out=$(run_in "$F1" git push origin feat); rc=$?
cp "$TMP/ta.orig" "$F1/$FX_MT/transition_audit.py"
[ "$rc" = 0 ] || bad "AC5: a DEAD PROBE refused a feature push, stranding its only off-node copy (rc=$rc): $out"; ok
{ has "$out" "DEAD PROBE" && has "$out" "refs/heads/feat"; } \
  || bad "AC5: a dead audit printed no DEAD PROBE line naming the ref: $out"; ok

# ============================================== AC12 — the two hooks-path values, one topology -----
# Under the RELATIVE value `check-wiring.sh --fix` writes, the linked worktree runs its OWN pre-flip
# hook files and the commit is not refused. That is the documented inert case, and the session step
# is what names it.
git -C "$F1" config core.hooksPath .githooks
# Its OWN branch: `strag` concluded a relocation merge above and is no longer pre-flip.
git -C "$F1" branch -q wt12 "$F1_STRAG"
WT4=$(add_topology_worktree "$F1" wt12)
printf -- '- TOOL-aSeed-8 \xc2\xb7 filed 2026-07-01 \xc2\xb7 an ask under the relative value\n' >> "$WT4/memory/backlog/TOOL.md"
git -C "$WT4" add memory/backlog/TOOL.md
out=$(run_in "$WT4" git commit -m "a shard edit under the relative hooks path"); rc=$?
[ "$rc" = 0 ] || bad "AC12: under the relative core.hooksPath the worktree's own pre-flip hooks did not run, so the arm measured the primary tree's (rc=$rc): $out"; ok
has "$out" "REFUSING" && bad "AC12: the documented inert case was refused"; ok
sess=$(run_in "$F1" bash "$FX_ROOT/check-wiring.sh" --session); rc=$?
[ "$rc" = 0 ] || bad "AC12: check-wiring --session exited $rc on a tree holding a straggler"; ok
line=$(printf '%s\n' "$sess" | grep '^note     straggler')
has "$line" "refs/heads/wt12" || bad "AC12: the session note does not name the local straggler: $sess"; ok
has "$line" "hooks own-tree" || bad "AC12: the session note does not mark a straggler whose worktree runs its own hooks: $line"; ok
# And under an ABSOLUTE value naming the primary tree's post-flip hooks, the same worktree IS refused.
git -C "$F1" config core.hooksPath "$F1/hk"
printf -- '- TOOL-aSeed-9 \xc2\xb7 filed 2026-07-02 \xc2\xb7 an ask under the absolute value\n' >> "$WT4/memory/backlog/TOOL.md"
git -C "$WT4" add memory/backlog/TOOL.md
out=$(run_in "$WT4" git commit -m "a shard edit under the absolute hooks path"); rc=$?
[ "$rc" != 0 ] || bad "AC12: under an absolute core.hooksPath naming the primary tree's hooks the shard edit was committed"; ok
has "$out" "migrate_backlog.py --relocate --as <your-slug>" \
  || bad "AC12: the absolute-value refusal does not print the recipe"; ok

# ================================================== AC11 — where the default branch is READ from ---
# The REMOTE default carries the flip while the local branch is still in shards mode: a node whose
# local `main` was never fast-forwarded must not stay dormant on a flip the fleet has taken.
git -C "$F1" update-ref refs/heads/main "$F1_BASE"
git -C "$F1" branch -q rs "$F1_STRAG"
WT5=$(add_topology_worktree "$F1" rs)
printf -- '- TOOL-aSeed-7 \xc2\xb7 filed 2026-06-01 \xc2\xb7 a late ask\n' >> "$WT5/memory/backlog/TOOL.md"
git -C "$WT5" add memory/backlog/TOOL.md
out=$(run_in "$WT5" git commit -m "a shard edit while the local default is still shards"); rc=$?
[ "$rc" != 0 ] || bad "AC11: with origin/HEAD in builds mode and the local default still in shards, the shard edit was committed"; ok
has "$out" "migrate_backlog.py --relocate --as <your-slug>" \
  || bad "AC11: the remote-default refusal does not print the recipe"; ok

# No default branch this clone can resolve at all: a NAMED line, and the commit proceeds.
U="$TMP/nodef"
mkdir -p "$U/memory/backlog"
write_hooks "$U"
printf 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\nBACKLOG_MODE="builds"\n' > "$U/.memory-tree.conf"
printf '# TOOL backlog\n\n- TOOL-x-1 - a row\n' > "$U/memory/backlog/TOOL.md"
git init -q -b trunk "$U"
git -C "$U" config user.email arms@example.invalid; git -C "$U" config user.name arms
git -C "$U" config core.autocrlf false; git -C "$U" config commit.gpgsign false
git -C "$U" config core.hooksPath "$U/hk"
git -C "$U" add -A >/dev/null 2>&1; git -C "$U" commit -q --no-verify -m base
UW=$(git -C "$U" worktree add -q -b side "$U-wt" >/dev/null 2>&1; printf '%s' "$U-wt")
printf -- '- TOOL-x-2 - another row\n' >> "$UW/memory/backlog/TOOL.md"
git -C "$UW" add memory/backlog/TOOL.md
out=$(run_in "$UW" git commit -m "a commit with no default branch anywhere"); rc=$?
[ "$rc" = 0 ] || bad "AC11: an unresolvable default branch REFUSED a commit (rc=$rc): $out"; ok
has "$out" "observes no default branch" \
  || bad "AC11: an unresolvable default branch printed no named line, so the layer is silently off: $out"; ok

# ================================================== AC7 — dormancy, and the library-absent adopter -
S="$TMP/shards"
mkdir -p "$S/memory/backlog"
write_hooks "$S"
printf 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\nBACKLOG_MODE="shards"\n' > "$S/.memory-tree.conf"
printf '# TOOL backlog\n\n- TOOL-x-1 - a row\n' > "$S/memory/backlog/TOOL.md"
git init -q -b main "$S"
git -C "$S" config user.email arms@example.invalid; git -C "$S" config user.name arms
git -C "$S" config core.autocrlf false; git -C "$S" config commit.gpgsign false
git -C "$S" config core.hooksPath "$S/hk"
git -C "$S" add -A >/dev/null 2>&1; git -C "$S" commit -q --no-verify -m base
git init -q --bare -b main "$S.git"; git -C "$S" remote add origin "$S.git"
add_origin_head "$S"
printf -- '- TOOL-x-2 - another row\n' >> "$S/memory/backlog/TOOL.md"
git -C "$S" add memory/backlog/TOOL.md
out=$(run_in "$S" git commit -m "a shard edit on a shards-mode default"); rc=$?
[ "$rc" = 0 ] || bad "AC7: a shards-mode default refused a shard edit (rc=$rc): $out"; ok
printf '%s' "$out" | grep -q 'straggler-guard\|pre-commit: note\|pre-commit: REFUSING' \
  && bad "AC7: the dormant path printed a line in a repository that has not flipped: $out"; ok
git -C "$S" checkout -q -b featshards
printf -- '- TOOL-x-3 - a third row\n' >> "$S/memory/backlog/TOOL.md"
git -C "$S" commit -q --no-verify -am "a feature commit"
out=$(run_in "$S" git push origin featshards); rc=$?
[ "$rc" = 0 ] || bad "AC7: a shards-mode default refused a feature push (rc=$rc): $out"; ok
printf '%s' "$out" | grep -q 'pre-push: note\|pre-push: REFUSING\|straggler-guard' \
  && bad "AC7: the dormant push path printed a line in a repository that has not flipped: $out"; ok

# The library ABSENT beside a shipped pre-push, on a builds-mode default: the block is inert, the
# push lands, and the hook's exit is BASE's 0 for a feature ref. This is every adopter that took the
# push-main kit and not the gov-only library, and no other arm exercises it.
N="$TMP/nolib"
mkdir -p "$N/hk" "$N/memory/backlog" "$N/memory/builds/aFlip"
cp "$HOOKDIR/pre-push" "$N/hk/pre-push"; chmod +x "$N/hk/pre-push"
printf 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\nBACKLOG_MODE="builds"\n' > "$N/.memory-tree.conf"
printf '# aFlip\n' > "$N/memory/builds/aFlip/BACKLOG.md"
printf '# TOOL backlog\n\n- TOOL-x-1 - a row\n' > "$N/memory/backlog/TOOL.md"
git init -q -b main "$N"
git -C "$N" config user.email arms@example.invalid; git -C "$N" config user.name arms
git -C "$N" config core.autocrlf false; git -C "$N" config commit.gpgsign false
git -C "$N" config core.hooksPath "$N/hk"
git -C "$N" add -A >/dev/null 2>&1; git -C "$N" commit -q --no-verify -m base
git init -q --bare -b main "$N.git"; git -C "$N" remote add origin "$N.git"
add_origin_head "$N"
[ -f "$N/hk/straggler-guard.sh" ] && bad "AC7: the library-absent fixture carries the library, so its arm proves nothing"; ok
git -C "$N" checkout -q -b featn
printf -- '- TOOL-x-9 - a feature row\n' >> "$N/memory/backlog/TOOL.md"
git -C "$N" commit -q --no-verify -am "a feature commit"
out=$(run_in "$N" git push origin featn); rc=$?
[ "$rc" = 0 ] || bad "AC7: with no straggler-guard.sh beside it the shipped pre-push refused a feature push — every push-main adopter (rc=$rc): $out"; ok
printf '%s' "$out" | grep -q 'pre-push:' \
  && bad "AC7: the library-absent block printed a line: $out"; ok
git -C "$N.git" rev-parse --verify --quiet refs/heads/featn >/dev/null \
  || bad "AC7: the library-absent feature push did not reach the remote"; ok

# ================================================== AC14 — the topology helper is ONE definition ---
T="$TMP/topo"
init_repo "$T"
git -C "$T" branch -q side
before=$(git -C "$T" config --get core.hooksPath || true)
tout=$(bash "$SELF" --topology "$T" side); trc=$?
after=$(git -C "$T" config --get core.hooksPath || true)
[ "$trc" = 0 ] || bad "AC14: --topology exited $trc"; ok
[ "$(printf '%s\n' "$tout" | grep -c .)" = 1 ] || bad "AC14: --topology printed more or fewer than one line: $tout"; ok
git -C "$T" worktree list | grep -qF "$tout" || bad "AC14: the path --topology printed is not a worktree of the fixture: $tout"; ok
printf '%s' "$tout" | grep -q PASS && bad "AC14: --topology printed a PASS line, so the mode reads as a suite run"; ok
[ "$before" = "$after" ] || bad "AC14: --topology changed core.hooksPath from '$before' to '$after'"; ok
hits=$(grep -c 'add_topology_worktree' "$SELF")
[ "$hits" -ge 3 ] || bad "AC14: the topology helper is named $hits times in this suite, so its definition, the mode's dispatch and AC12's call are not all routed through it"; ok
grep -qE '^add_topology_worktree\(\) \{' "$SELF" || bad "AC14: the topology helper has no definition line in this suite"; ok

# ---------------------------------------------------------------------------------------- verdict
if [ "$n" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL executed $n assertions, below the declared floor of $FLOOR_ASSERTIONS — a block of arms"
  echo "     is stranded past an exit, and a suite that reports success over half of itself is the"
  echo "     green-by-absence shape this floor exists to catch."
  st=1
fi
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
