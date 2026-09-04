#!/usr/bin/env bash
# pre-push.test.sh — drives a REAL git push through .githooks/pre-push in a throwaway scratch repo,
# with the gate stubbed via GOV_GATE_CMD so the bar never actually runs. Proves the hook FIRES and
# classifies correctly. Exit 0 = all cases ok.
KIT_REL="${KIT_REL:-tools}"
set -u
SRC=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "pre-push.test: not a git repo"; exit 2; }
[ -f "$SRC/.githooks/pre-push" ] || { echo "pre-push.test: .githooks/pre-push missing"; exit 1; }

tmp=$(mktemp -d) || exit 2
trap 'rm -rf "$tmp"' EXIT
fail=0
ok() { echo "  ok   — $1"; }
bad() { echo "  FAIL — $1"; fail=1; }
# The scratch repo is `git init`+`remote add` (origin/HEAD unset); pin the default so the hook's
# fail-CLOSED resolution doesn't refuse the gate cases (case 6 unsets it to test that path).
export GOV_DEFAULT_BRANCH=main

# Isolate ONLY the pre-push hook (a scratch hooks dir) so the repo's pre-commit branch-guard does not
# fire on the test's own setup commits. A clone does NOT carry core.hooksPath — set it explicitly.
mkdir -p "$tmp/hooks"
cp "$SRC/.githooks/pre-push" "$tmp/hooks/pre-push"

git init -q --bare "$tmp/remote.git"
git init -q "$tmp/work"
cd "$tmp/work" || exit 2
git config user.email t@example.com; git config user.name t
git config core.hooksPath "$tmp/hooks"
git commit -q --allow-empty -m init
git branch -M main
git remote add origin "$tmp/remote.git"

# case 0 — a raw default-branch push with NO push-main marker is refused (TOOL-aLeasedGauntlet-1).
git commit -q --allow-empty -m c0
if git push -q origin main >/dev/null 2>&1; then bad "0 raw push (no marker) must be refused"; else ok "0 raw push (no marker) refused"; fi
# The remaining cases exercise the GATE — set the marker push-main would set (the hook only CHECKS it).
touch "$(git rev-parse --git-dir)/push-main-active"

red="$tmp/red.sh";   printf '#!/usr/bin/env bash\necho "FAKE LEG failed"; exit 1\n' > "$red"
green="$tmp/green.sh"; printf '#!/usr/bin/env bash\nexit 0\n' > "$green"

# case 1 — push to main with a RED gate → blocked (non-zero push).
if GOV_GATE_CMD="bash $red" git push -q origin main >/dev/null 2>&1; then bad "1 red gate must block a main push"; else ok "1 red gate blocks a main push"; fi

# case 2 — push to main with a GREEN gate → proceeds (the gate actually ran).
if GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1; then ok "2 green gate lets a main push through"; else bad "2 green gate must let a main push through"; fi

# case 3 — push a NON-main ref → hook skips the gate, so even a RED stub proceeds.
git checkout -q -b feature
git commit -q --allow-empty -m f
if GOV_GATE_CMD="bash $red" git push -q origin feature >/dev/null 2>&1; then ok "3 non-main ref skips the gate"; else bad "3 non-main ref must skip the gate"; fi

# case 4 — push a DIFFERENTLY-NAMED local ref to main (feature:refs/heads/main) with RED → blocked.
#          Proves classification is on the remote_ref (3rd field), not the local ref name.
if GOV_GATE_CMD="bash $red" git push -q origin feature:refs/heads/main >/dev/null 2>&1; then bad "4 renamed local ref to main must be gated"; else ok "4 renamed local ref to main is gated (3rd-field classify)"; fi

# case 5 — multi-ref push including main (a new main commit + feature) with RED → blocked.
git checkout -q main
git commit -q --allow-empty -m m2
if GOV_GATE_CMD="bash $red" git push -q origin main feature >/dev/null 2>&1; then bad "5 multi-ref push incl. main must be gated"; else ok "5 multi-ref push incl. main is gated"; fi

# case 6 — fail CLOSED when the default branch is unresolvable (origin/HEAD unset AND GOV_DEFAULT_BRANCH
#          unset): the hook must REFUSE, not silently assume 'main' and BYPASS the gate on a non-main default.
git checkout -q main
msg=$( ( unset GOV_DEFAULT_BRANCH; GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"determine the default branch"*) ok "6 unresolvable default branch → fail closed" ;;
  *) bad "6 expected fail-closed refusal, got: ${msg:-<push SUCCEEDED>}" ;;
esac

# case 7 — a NON-EMPTY but meaningless GOV_DEFAULT_BRANCH must be refused, not classified against.
#          Reproduced as a live, repo-wide bypass on 2026-08-11: the loop never matched, main_local
#          stayed empty, and the hook exited 0 down the "nothing to gate" path — skipping the lander
#          refusal AND the full bar. Case 6 covers an EMPTY value; this is the worse, non-empty one.
git checkout -q main
git commit -q --allow-empty -m c7
msg=$( ( GOV_DEFAULT_BRANCH=nosuchthing GOV_GATE_CMD="bash $red" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"no branch in this clone"*) ok "7 non-empty but unresolvable default branch → refused" ;;
  *) bad "7 expected a refusal, got: ${msg:-<push SUCCEEDED — the whole bar was skipped>}" ;;
esac
# case 7c — the LIVE CONTROL for 7, one variable changed: the honest value on the same tree must reach
#           the gate and be blocked BY THE GATE, not by the classification refusal. Without this, case
#           7 would also pass against a hook that refuses everything.
# NOTE: both streams here. The hook's gate-RED line goes to STDOUT while its refusals go to stderr,
# so the stderr-only capture used above would have discarded exactly the evidence this control needs.
msg=$( ( GOV_DEFAULT_BRANCH=main GOV_GATE_CMD="bash $red" git push -q origin main 2>&1 ) )
case "$msg" in
  *"gate RED"*) ok "7c control — the honest value classifies, and the gate runs" ;;
  *) bad "7c control expected the gate to run, got: ${msg:-<push SUCCEEDED>}" ;;
esac

# case 8 — once a default branch IS observable, the environment may only AGREE with it. This is the
#          shape the real repo is in (refs/remotes/origin/HEAD is set there), and it is why the
#          reproduced bypass is closed rather than merely made harder: `feature` exists, so this is
#          refused for DISAGREEING, not for being unresolvable. Runs last: it sets origin/HEAD.
git remote set-head origin main >/dev/null 2>&1
git commit -q --allow-empty -m c8
msg=$( ( GOV_DEFAULT_BRANCH=feature GOV_GATE_CMD="bash $red" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"does not observe as the default"*) ok "8 env disagreeing with the observed default → refused" ;;
  *) bad "8 expected a refusal, got: ${msg:-<push SUCCEEDED — the whole bar was skipped>}" ;;
esac

# ============================================================================================
# THE BOUNDARY DECIDES. One arm per forcing predicate, plus the one that matters most: the arm
# proving a scoped run is EVER chosen. Without it every predicate below is satisfied by a hook
# that forces unconditionally — which is the hook this unit replaced, passing its own tests.
#
# The gate is stubbed, so what these grade is the DECISION LINE the hook prints, not a bar run.
decide() {   # -> the hook's decision line for a push of the current main
  # A COMMIT FIRST, because a push with nothing to send never invokes the hook at all — and a hook
  # that did not run is indistinguishable from one that decided nothing. Earlier cases have already
  # pushed main, so without this every arm below reads an empty line and reports a failure that is
  # really 'there was no push'.
  git commit -q --allow-empty -m "decide $RANDOM" >/dev/null 2>&1
  # BOTH streams. The refusal cases above capture stderr only, because a refusal is an error; the
  # decision line is ordinary progress output on STDOUT, and `1>/dev/null` threw it away — which
  # read as 'the hook made no decision' rather than 'the arm looked in the wrong place'.
  # GATE_SELFTESTS IS CLEARED, NOT INHERITED. It is an INPUT to the decision this function grades
  # (TOOL-dUnstalledConvoy-27's predicate 8), and the bar itself exports it — so under
  # `GATE_SELFTESTS=1 run-gates.sh` every arm below silently switched to the forcing case and the
  # control arm reported a hook bug that was really an uncontrolled input.
  ( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 ) | grep -m1 -E 'gate on main push' || true
}
stamp() {    # write a full-green record naming a sha, with a reproducible fingerprint
  # $2, when given, is the `selftests` value the record claims. OMITTED writes no key at all, which
  # is the shape of every record written before TOOL-dUnstalledConvoy-26 and is what AC4 grades.
  local sha=$1 st=${2-} gd; gd=$(git rev-parse --git-dir)
  local fp=""
  [ -x $KIT_REL/run-gates/gate-fingerprint.sh ] && fp=$(bash $KIT_REL/run-gates/gate-fingerprint.sh "$sha" 2>/dev/null)
  printf 'sha\t%s\nfingerprint\t%s\nmanifest_blob\t%s\nrun_id\ttest\n' \
    "$sha" "$fp" "$(git hash-object -- tools/gate-legs.json 2>/dev/null)" > "$gd/gate-full-green"
  [ -n "$st" ] && printf 'selftests\t%s\n' "$st" >> "$gd/gate-full-green"
  return 0
}
decide_on() {   # the hook's decision line for a push made WITH the self-test switch on
  git commit -q --allow-empty -m "decide-on $RANDOM" >/dev/null 2>&1
  ( GATE_SELFTESTS=1 GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 ) | grep -m1 -E 'gate on main push' || true
}

# --- the control FIRST: a fresh, covered record must choose SCOPED ---------------------------
stamp "$(git rev-parse HEAD)"
line=$(decide)
case "$line" in
  *"scoped gate"*) ok "9 control — a current, covered recorded green chooses a SCOPED run" ;;
  *) bad "9 a current recorded green did not produce a scoped run, so every forcing arm below is vacuous: ${line:-<no decision line>}" ;;
esac

# --- no record at all -------------------------------------------------------------------------
rm -f "$(git rev-parse --git-dir)/gate-full-green"
case "$(decide)" in
  *"FULL gate"*"no recorded full green"*) ok "10 no recorded green → FULL, and the reason says so" ;;
  *) bad "10 an absent record did not force a full run" ;;
esac

# --- a record naming a sha that is not an ancestor of the pushed tip --------------------------
stamp "0000000000000000000000000000000000000000"
case "$(decide)" in
  *"FULL gate"*) ok "11 a record naming an unreachable sha → FULL" ;;
  *) bad "11 a record naming an unreachable sha did not force" ;;
esac

# --- the record is further behind than the declared bound -------------------------------------
base_sha=$(git rev-parse HEAD)
lagbound=$(grep -m1 -oE 'GATE_FULL_MAX_LAG=[0-9]+' "$tmp/hooks/pre-push" | grep -oE '[0-9]+')
# READ FROM THE HOOK rather than pinned here: a bound written into this arm is satisfied by
# whatever the source happens to say, including a value that makes the arm unreachable.
if [ -z "$lagbound" ]; then
  bad "12 could not read GATE_FULL_MAX_LAG out of the hook, so the lag arm has no bound to grade"
else
  i=0; while [ "$i" -le "$lagbound" ]; do i=$((i+1)); echo "lag $i" >> lagfile.txt; git add -A >/dev/null 2>&1; git commit -qm "lag $i" >/dev/null 2>&1; done
  stamp "$base_sha"
  case "$(decide)" in
    *"FULL gate"*"commits behind the tip"*) ok "12 a record more than GATE_FULL_MAX_LAG=$lagbound commits back → FULL" ;;
    *) bad "12 a stale-by-lag record did not force a full run" ;;
  esac
fi

# --- the pushed diff touches the leg manifest -------------------------------------------------
stamp "$(git rev-parse HEAD)"
case "$(decide)" in *"scoped gate"*) : ;; *) bad "13 precondition — could not get back to a scoped decision" ;; esac
prev=$(git rev-parse HEAD)
mkdir -p tools
printf '%s\n' '[{"name":"x","argv":["bash","x.sh"]}]' > tools/gate-legs.json
git add -A >/dev/null 2>&1; git commit -qm "touch the manifest" >/dev/null 2>&1
stamp "$prev"
case "$(decide)" in
  *"FULL gate"*) ok "14 a diff touching the leg manifest → FULL (the scoping rules themselves moved)" ;;
  *) bad "14 a diff that moved the leg manifest did not force a full run" ;;
esac

# --- and the decision is ALWAYS announced -----------------------------------------------------
case "$(decide)" in
  *"gate on main push"*) ok "15 the boundary prints its decision and its reason on one line, every time" ;;
  *) bad "15 the boundary made a decision without announcing it" ;;
esac
# --- 19-23: THE SWITCH FIELD IS READ (TOOL-dUnstalledConvoy-27) -------------------------------
# The stamp records whether the kit-subject legs ran. Written and never read, that field is a byte
# nobody consults and the boundary trusts a partial bar as a whole one. The relation is COVERAGE,
# not equality: a record that covered MORE still satisfies a push that needs less.
cd "$tmp/work" || exit 2

# 19 — a record earned switch-OFF does not satisfy a switch-ON push. This is the only direction
#      that forces, and it is the one the whole unit is for.
stamp "$(git rev-parse HEAD)" 0
line=$(decide_on)
case "$line" in
  *"FULL gate"*) ok "19 a switch-OFF record offered for a switch-ON push → FULL" ;;
  *) bad "19 a record that never ran the kit self-tests satisfied a push that does: ${line:-<no decision line>}" ;;
esac

# 20 — and the reason NAMES the switch. A run forced for an unstated reason teaches its operator
#      nothing, and this line is the only window into the decision.
case "$line" in
  *"kit self-tests"*"HELD"*) ok "20 and the forcing reason names the switch" ;;
  *) bad "20 the boundary forced without saying the switch was why: ${line:-<no decision line>}" ;;
esac

# 21 — AC4: a record with NO switch key at all reads as OFF. Every stamp written before the parent
#      unit lacks the key, and reading its absence as 'covered everything' would make each of them
#      certify legs it never ran.
stamp "$(git rev-parse HEAD)"
case "$(decide_on)" in
  *"FULL gate"*"kit self-tests"*) ok "21 a record with NO switch key reads as OFF" ;;
  *) bad "21 a record missing the switch key was treated as covering the kit self-tests" ;;
esac

# 22 — COVERAGE, not equality: a record earned switch-ON satisfies a switch-OFF push. Equality here
#      would force a full run on every adopter's ordinary push and delete the parent unit's saving.
stamp "$(git rev-parse HEAD)" 1
case "$(decide)" in
  *"scoped gate"*) ok "22 a switch-ON record satisfies a switch-OFF push (coverage, not equality)" ;;
  *) bad "22 a STRONGER record forced a full run, which is equality wearing coverage's name" ;;
esac

# 23 — its control: switch-ON record, switch-ON push. Without this, an implementation that forced
#      on every switch-ON push would still pass 19 through 22.
stamp "$(git rev-parse HEAD)" 1
case "$(decide_on)" in
  *"scoped gate"*) ok "23 control — a switch-ON record satisfies a switch-ON push" ;;
  *) bad "23 a record that covered the kit self-tests did not satisfy a push that runs them" ;;
esac

# 24 — THE HOOK SOURCES THE REPOSITORY'S OWN GATE POLICY. TOOL-dUnstalledConvoy-28 moved gov's
#      GATE_SELFTESTS out of this hook — which ships verbatim to every push-main adopter — and into
#      `.githooks/gate-env.sh`, which no kit claims. The MECHANISM travels and the CHOICE does not,
#      and until now nothing anywhere arms the mechanism half: delete the two source lines and every
#      other arm in this file stays green while gov silently stops running its own kit self-tests.
#      Driven through the DECISION, not through the environment: the switch is only observable here
#      by what predicate 8 does with it.
mkdir -p "$tmp/work/.githooks"
printf '#!/usr/bin/env sh\nexport GATE_SELFTESTS=1\n' > "$tmp/work/.githooks/gate-env.sh"
git -C "$tmp/work" add -A >/dev/null 2>&1
stamp "$(git rev-parse HEAD)" 0
case "$(decide)" in
  *"FULL gate"*"kit self-tests"*) ok "24 the hook sources .githooks/gate-env.sh, so the repo's own switch reaches the decision" ;;
  *) bad "24 a gate-env.sh setting the switch did not reach the boundary — the sourcing is dead: $(decide)" ;;
esac
# ITS CONTROL: remove the file and the same push decides SCOPED again. Without it the arm above
# passes on a hook that forces unconditionally.
rm -f "$tmp/work/.githooks/gate-env.sh"
git -C "$tmp/work" add -A >/dev/null 2>&1
stamp "$(git rev-parse HEAD)" 0
case "$(decide)" in
  *"scoped gate"*) ok "24b control — with no gate-env.sh the same push is SCOPED" ;;
  *) bad "24b the boundary forced with no gate-env.sh present, so arm 24 proves nothing" ;;
esac

# --- 16-18: TOOL-dScrubbedConduit-1 S2/S5. A LINKED WORKTREE, because that is the shape this
# --- harness could not previously see. Every fixture above is `git init` plus `git init --bare`, and
# --- neither exports GIT_DIR into a hook — which is exactly why this class went unobserved here
# --- while an adopter hit it head-on. The fixture had to change for the RED to be observable.
SCRUB="GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX"

# 16 — the hook still CARRIES the scrub. Asserted against the hook's own bytes so that deleting the
# unset line reds this arm, rather than the arm silently testing its own inlined copy.
miss=""
for v in $SCRUB; do
  grep -qE "^unset .*\b$v\b|^ +$v\b" "$tmp/hooks/pre-push" || miss="$miss $v"
done
if [ -n "$miss" ]; then
  bad "16 the hook no longer scrubs:$miss — a leg that git-inits a scratch repo can rewrite the shared config"
else
  ok "16 the hook scrubs every injected git variable before running anything"
fi
# GIT_EXEC_PATH must SURVIVE: it locates git's own helpers and clearing it breaks git rather than
# protecting it. A scrub that over-reaches is its own defect.
if grep -qE "^unset .*GIT_EXEC_PATH|^ +GIT_EXEC_PATH\b" "$tmp/hooks/pre-push"; then
  bad "16b the hook scrubs GIT_EXEC_PATH, which breaks git instead of protecting it"
else
  ok "16b the scrub leaves GIT_EXEC_PATH alone"
fi

# 17 — the MECHANISM, in a real linked worktree: unscrubbed it poisons the shared config, scrubbed it
# does not. Both directions, because a one-sided arm cannot tell a working scrub from a fixture that
# never reproduced the bug.
wt=$(mktemp -d)
( git init -q "$wt/w" && cd "$wt/w" && git config user.email t@t && git config user.name t \
    && echo x > a && git add -A && git commit -qm init && git worktree add -q "$wt/lw" -b lw ) >/dev/null 2>&1
wtcfg="$wt/w/.git/config"
wtgd="$wt/w/.git/worktrees/lw"
if [ -d "$wtgd" ]; then
  git config --file "$wtcfg" core.bare false
  ( cd "$wt" && GIT_DIR="$wtgd" sh -c 'd=$(mktemp -d); cd "$d" && git init -q .' ) >/dev/null 2>&1
  poisoned=$(git config --file "$wtcfg" --get core.bare)
  git config --file "$wtcfg" core.bare false
  ( cd "$wt" && GIT_DIR="$wtgd" sh -c "unset $SCRUB; d=\$(mktemp -d); cd \"\$d\" && git init -q ." ) >/dev/null 2>&1
  guarded=$(git config --file "$wtcfg" --get core.bare)
  if [ "$poisoned" != true ]; then
    bad "17 the fixture did not reproduce the injection, so this arm proves nothing (git behaviour changed?)"
  elif [ "$guarded" = true ]; then
    bad "17 the scrub did not stop a scratch-repo leg rewriting the shared config"
  else
    ok "17 unscrubbed poisons the shared config and scrubbed does not (linked worktree, no submodule)"
  fi
else
  bad "17 could not build a linked-worktree fixture, so the GIT_DIR-injection class went UNTESTED"
fi

# 18 — the hook REFUSES when it cannot resolve its repo. This used to `exit 0`, and exit 0 from a
# pre-push hook means ALLOW: measured end to end, a push landed on the remote with the bar never run.
nr=$(mktemp -d)
printf 'main\nrefs/heads/main\n' > "$nr/in"
( cd "$nr" && bash "$tmp/hooks/pre-push" origin git@example:x.git < "$nr/in" ) >/dev/null 2>&1
if [ "$?" = 0 ]; then
  bad "18 the hook ALLOWED a push from a tree whose repo it could not resolve — fail-open"
else
  ok "18 the hook refuses when it cannot resolve its repo, instead of failing open"
fi
rm -rf "$wt" "$nr"


# ============================================================================================
# TOOL-dRetiredFork-11 — THE HOOK RESOLVES ITS OWN KIT ROOT.
#
# Everything above this line runs in a fixture that keeps its leg manifest at `tools/`, which is
# where gov keeps it — so every arm above would pass unchanged with the prefix hardcoded, and did.
# That is the shape of the defect: the suite could not tell a resolving hook from a hardcoded one,
# because it only ever asked in the layout the hardcoding happened to match.
#
# These arms ask in the OTHER layout, and they compare against the pre-change hook on the SAME
# fixture. A new arm that has only ever been run against the fixed code proves nothing about what
# it fixed.
pfx_home=$PWD
# `git -C "$SRC"`, NOT a bare `git show`: by this line the suite is standing inside its own scratch
# repo, where HEAD carries no .githooks/ at all. The bare form wrote an EMPTY file, the red-first
# control below hit its `[ -s ]` guard and skipped, and the suite still printed all-ok — a control
# that silently does not run is worse than no control.
# PINNED TO AN IMMUTABLE SHA, not HEAD. Reading HEAD made this control SELF-INVALIDATING: the
# moment TOOL-dRetiredFork-11 landed, "the pre-change hook" became the fixed one and the arm
# reported that it "already forced — this arm proves nothing". It was green when run before the
# commit and red immediately after, which is the worst possible timing for a control nobody re-runs.
# 05455c45 is the last commit that touched this hook BEFORE that unit.
PREPUSH_PRE=05455c45fc0fc32f7de331541daea5c57cb856e0
git -C "$SRC" show "$PREPUSH_PRE:.githooks/pre-push" > "$tmp/hooks-old-pre-push" 2>/dev/null || true
[ -s "$tmp/hooks-old-pre-push" ] || bad "AC1 red-first control unavailable — could not read the pre-change hook"

# Build a scratch repo whose kits live at $1, push once so a record can name a real sha, and leave
# the caller standing in it.
pfx_fixture() {
  local pfx=$1 hook=$2 tag=$3
  # SPLIT deliberately: `local a=$1 d="...$a..."` reads $a as unset under `set -u` here, so the
  # fixture builder died before it built anything. One name per statement.
  local d="$tmp/pfx-$pfx-$tag"
  mkdir -p "$d/hooks"; cp "$hook" "$d/hooks/pre-push"
  git init -q --bare "$d/remote.git"; git init -q "$d/work"
  cd "$d/work" || return 1
  git config user.email t@example.com; git config user.name t
  git config core.hooksPath "$d/hooks"
  mkdir -p "$pfx"
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > "$pfx/gate-legs.json"
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$d/remote.git"
  touch "$(git rev-parse --git-dir)/push-main-active"
  GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1
}
# A full-green record for a fixture at $1, naming sha $2. Deliberately NOT the `stamp` above: that
# one spells `tools/` itself, which is the very assumption under test here.
pfx_stamp() {
  local pfx=$1 sha=$2 blob=${3-} gd; gd=$(git rev-parse --git-dir)
  [ -n "$blob" ] || blob=$(git hash-object -- "$pfx/gate-legs.json" 2>/dev/null)
  printf 'sha\t%s\nfingerprint\t%s\nmanifest_blob\t%s\nrun_id\ttest\n' "$sha" "" "$blob" \
    > "$gd/gate-full-green"
}
pfx_decide() {
  git commit -q --allow-empty -m "decide $RANDOM" >/dev/null 2>&1
  ( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 ) \
    | grep -m1 -E 'gate on main push' || true
}

# --- AC1: a manifest change at a NON-tools prefix must force a full run ------------------------
for _h in new old; do
  case $_h in new) _hook="$SRC/.githooks/pre-push" ;; old) _hook="$tmp/hooks-old-pre-push" ;; esac
  [ -s "$_hook" ] || continue
  pfx_fixture scripts "$_hook" "ac1$_h" || { bad "AC1 could not build the $_h fixture"; continue; }
  pfx_stamp scripts "$(git rev-parse HEAD)"
  case "$(pfx_decide)" in
    *"scoped gate"*) [ "$_h" = new ] && ok "AC1 precondition — a scripts/ tree reaches a SCOPED decision" ;;
    *) [ "$_h" = new ] && bad "AC1 precondition — no scoped decision at a scripts/ prefix" ;;
  esac
  _prev=$(git rev-parse HEAD)
  printf '%s\n' '[{"name":"x","argv":["bash","b.sh"]},{"name":"y","argv":["bash","c.sh"]}]' \
    > scripts/gate-legs.json
  git add -A >/dev/null 2>&1; git commit -qm "move the manifest" >/dev/null 2>&1
  pfx_stamp scripts "$_prev"
  _dec=$(pfx_decide)
  case "$_h:$_dec" in
    new:*"FULL gate"*) ok "AC1 a manifest change at scripts/ FORCES a full run (predicate 6 fires)" ;;
    new:*) bad "AC1 predicate 6 did not fire at a scripts/ prefix: ${_dec:-<no decision>}" ;;
    old:*"FULL gate"*) bad "AC1 the PRE-CHANGE hook already forced — this arm proves nothing" ;;
    old:*) ok "AC1 red-first: the pre-change hook did NOT force here — it matched nothing" ;;
  esac
done

# --- AC2: a recorded manifest blob that differs, at that same prefix ---------------------------
pfx_fixture scripts "$SRC/.githooks/pre-push" ac2 || bad "AC2 could not build its fixture"
pfx_stamp scripts "$(git rev-parse HEAD)" "0000000000000000000000000000000000000000"
_dec=$(pfx_decide)
case "$_dec" in
  *"differs from the one the recorded green was earned on"*)
    ok "AC2 a differing recorded manifest blob at scripts/ FORCES (predicate 7 fires)" ;;
  *) bad "AC2 predicate 7 did not fire at a scripts/ prefix: ${_dec:-<no decision>}" ;;
esac

# --- AC3: a manifest the resolved root does NOT point at is a REFUSAL, not a non-match ---------
# The distinction the whole unit turns on. A tree that tracks a manifest somewhere the hook does not
# look must SAY SO; reading it as "no change here" is what let a manifest-wide change land scoped.
pfx_fixture nowhere "$SRC/.githooks/pre-push" ac3 >/dev/null 2>&1
git commit -q --allow-empty -m c >/dev/null 2>&1
_out=$( GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 )
case "$_out" in
  *"REFUSING"*"resolved its kit root"*)
    ok "AC3 a manifest outside the resolved root REFUSES and names the resolution" ;;
  *) bad "AC3 expected a refusal naming the failed resolution, got: ${_out:-<push SUCCEEDED>}" ;;
esac
# ANTI-VACUITY: a repo with NO manifest anywhere is a legitimate case and must NOT refuse, or the
# arm above is satisfied by a hook that refuses everything.
pfx_fixture scripts "$SRC/.githooks/pre-push" ac3b >/dev/null 2>&1
rm -f scripts/gate-legs.json; git add -A >/dev/null 2>&1
git commit -qm "no manifest at all" >/dev/null 2>&1
if GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1; then
  ok "AC3 a tree with no manifest ANYWHERE is left alone, so the refusal is not universal"
else bad "AC3 the hook refused a tree that simply has no leg manifest"; fi

cd "$pfx_home" || exit 2

[ "$fail" = 0 ] && { echo "pre-push.test: all cases ok"; exit 0; } || { echo "pre-push.test: FAILURES"; exit 1; }
