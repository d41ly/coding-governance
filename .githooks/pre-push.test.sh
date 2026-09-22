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

# case 9 — THE RED IS ATTRIBUTED AGAINST THE LANDING BASE (TOOL-dDerivedDocket-23 AC7). The runner is
#          handed GATE_ATTRIBUTE = the REMOTE sha git feeds the hook on stdin, never the local one: a
#          red attributed against the tree that has it reads every red as inherited. The hook is
#          driven DIRECTLY with a hand-fed stdin line, because only then are both shas known to the
#          arm, and a fake runner prints its environment and exits 3 so the hook's exit is visible.
git checkout -q main
git commit -q --allow-empty -m c9
_c9r=$(git ls-remote origin refs/heads/main | cut -f1)
_c9l=$(git rev-parse HEAD)
envr="$tmp/envr.sh"
printf '#!/usr/bin/env bash\nprintf "ATTR=%%s\\n" "${GATE_ATTRIBUTE:-}"\nexit %s\n' 3 > "$envr"
msg=$( GATE_ATTRIBUTE= GOV_GATE_CMD="bash $envr" bash "$tmp/hooks/pre-push" origin "$tmp/remote.git" \
       <<<"refs/heads/main $_c9l refs/heads/main $_c9r" 2>&1 ); _c9rc=$?
if [ -z "$_c9r" ] || [ "$_c9r" = "$_c9l" ]; then
  bad "9 precondition — the remote and local shas must both exist and differ, or the arm grades nothing"
else
  case "$msg" in
    *"ATTR=$_c9r"*) ok "9 the runner is handed GATE_ATTRIBUTE = the remote sha fed on stdin" ;;
    *"ATTR=$_c9l"*) bad "9 the hook exported its LOCAL sha, which attributes a red against the tree that has it" ;;
    *) bad "9 GATE_ATTRIBUTE did not reach the runner as the remote sha: ${msg:-<no output>}" ;;
  esac
  [ "$_c9rc" = 3 ] && ok "9 the hook's exit is the runner's (3)" || bad "9 the hook exited $_c9rc where the runner exited 3"
fi
# 9b — THE CONTROL: a remote sha of all zeroes is a branch the remote does not have, and exports nothing.
_c9z=0000000000000000000000000000000000000000
msg=$( GATE_ATTRIBUTE= GOV_GATE_CMD="bash $envr" bash "$tmp/hooks/pre-push" origin "$tmp/remote.git" \
       <<<"refs/heads/main $_c9l refs/heads/main $_c9z" 2>&1 )
case "$msg" in
  *"ATTR=$_c9z"*) bad "9b an all-zero remote sha was exported as a base to attribute against" ;;
  *"ATTR="*) ok "9b an all-zero remote sha exports no GATE_ATTRIBUTE" ;;
  *) bad "9b the runner did not run, so the control grades nothing: ${msg:-<no output>}" ;;
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

# ---- TOOL-dDerivedDocket-24: THE INHERITED-RED POLICY, READ AT R ---------------------------------
# A scratch repo whose `.githooks/gate-env.sh` at the pushed remote tip R declares the policy under
# test, and a stub gate that writes the run record a real runner would: a RED verdict and one
# attribution row in the nine-column order, reading `GATE_RUN_ID` and `GATE_ATTRIBUTE` from the hook.
# The stub also records the policy the hook exported, so an arm can grade what reached the runner.
ir_env="$tmp/ir-env.txt"
irstub="$tmp/irstub.sh"
cat > "$irstub" <<'IRSTUB'
#!/usr/bin/env bash
d="$(git rev-parse --git-dir)/gate-run/$GATE_RUN_ID"; mkdir -p "$d"
printf 'verdict\tRED\nfailed\t1\ntree_moved\t%s\n' "${IR_MOVED:-no}" > "$d/verdict"
printf 'x\t%s\t1\t0\t%s\t%s\t-\t-\tstub\n' "${IR_VERDICT:-INHERITED}" "${GATE_ATTRIBUTE:-none}" "${IR_AGE:-3}" > "$d/attribution"
printf 'policy=%s age=%s attr=%s\n' "${GATE_INHERITED_RED:-}" "${GATE_INHERITED_RED_MAX_AGE:-}" "${GATE_ATTRIBUTE:-}" > "$IR_ENV"
echo "FAKE LEG failed"; exit 1
IRSTUB
build_ir_fixture() { # tag · gate-env body (printf %b) -> a pushed main whose R carries that body; sets IR_R
  local tag=$1 body=$2
  local d="$tmp/ir-$tag"
  mkdir -p "$d/hooks"; cp "$SRC/.githooks/pre-push" "$d/hooks/pre-push"
  git init -q --bare "$d/remote.git"; git init -q "$d/work"
  cd "$d/work" || return 1
  git config user.email t@example.com; git config user.name t
  git config core.hooksPath "$d/hooks"
  mkdir -p .githooks tools
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > tools/gate-legs.json
  printf '%b' "$body" > .githooks/gate-env.sh
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$d/remote.git"
  touch "$(git rev-parse --git-dir)/push-main-active"
  GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1
  IR_R=$(git rev-parse HEAD)
}
run_ir_push() { # [env assignments…] -> the push's merged output, then `rc=<n>` on its own line
  git commit -q --allow-empty -m "ir $RANDOM" >/dev/null 2>&1
  local o r
  o=$( env GATE_SELFTESTS= IR_ENV="$ir_env" GOV_GATE_CMD="bash $irstub" "$@" git push origin main 2>&1 ); r=$?
  printf '%s\nrc=%s\n' "$o" "$r"
}
write_ir_stamp() { # sha · base · max_age -> a planted gate-inherited-green
  printf 'sha\t%s\nfingerprint\t\nmanifest_blob\t\nselftests\t\nbase\t%s\nmax_age\t%s\nlegs\tx\nrun_id\ttest\n' \
    "$1" "$2" "$3" > "$(git rev-parse --git-dir)/gate-inherited-green"
}

# AC1, the hook's half: R says park and the pushed branch commits `land` into its OWN copy. The policy
# line reads park, and an inherited-only red is blocked. A reader of the working tree would land it.
build_ir_fixture ac1 'INHERITED_RED=park\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC1 could not build its fixture"
printf 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' > .githooks/gate-env.sh
git add -A >/dev/null 2>&1; git commit -q -m "the branch grants itself land" >/dev/null 2>&1
_o=$(run_ir_push)
case "$_o" in
  *"inherited-red policy at ${IR_R:0:8} reads park"*"rc=1") ok "IR AC1 a branch-committed land is not read: R's park binds and the red is blocked" ;;
  *) bad "IR AC1 expected R's park and a blocked push, got: $_o" ;;
esac

# AC2: under land at R, a red whose one leg reads INHERITED and not aged lands, naming the leg; the
# same bar with the leg MIXED is blocked. The export reaches the runner too.
build_ir_fixture ac2 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC2 could not build its fixture"
_o=$(run_ir_push)
case "$_o" in
  *"red on inherited legs only — landing under INHERITED_RED=land: x"*"rc=0") ok "IR AC2 an inherited-only red within its age lands under land" ;;
  *) bad "IR AC2 expected the landing line and exit 0, got: $_o" ;;
esac
case "$(cat "$ir_env" 2>/dev/null)" in
  "policy=land age=10 attr=${IR_R}") ok "IR AC2 the runner is handed land, the bound 10 and R" ;;
  *) bad "IR AC2 the runner was handed: $(cat "$ir_env" 2>/dev/null)" ;;
esac
_o=$(run_ir_push IR_VERDICT=MIXED)
case "$_o" in
  *"this red does not land under INHERITED_RED=land — x reads MIXED"*"rc=1") ok "IR AC2 a MIXED leg is blocked under land" ;;
  *) bad "IR AC2 a MIXED leg must block, got: $_o" ;;
esac

# AC15: the same inherited-only record on a bar whose verdict reads tree_moved yes is blocked, naming it.
_o=$(run_ir_push IR_MOVED=yes)
case "$_o" in
  *"the tree moved while the bar ran, so no verdict describes the pushed commit"*"rc=1") ok "IR AC15 a moved tree blocks an inherited-only red" ;;
  *) bad "IR AC15 a moved tree must block, got: $_o" ;;
esac

# AC17: an aged row blocks under land; land beside a blank, zero or non-numeric bound reads park.
_o=$(run_ir_push IR_AGE=aged)
case "$_o" in
  *"x reads INHERITED with age 'aged'"*"rc=1") ok "IR AC17 an aged inherited leg is blocked under land" ;;
  *) bad "IR AC17 an aged leg must block, got: $_o" ;;
esac
for _b in "" 0 ten; do
  build_ir_fixture "ac17$_b" "INHERITED_RED=land\nINHERITED_RED_MAX_AGE=$_b\n" || bad "IR AC17 could not build its fixture"
  _o=$(run_ir_push)
  case "$_o" in
    *"reads park — INHERITED_RED=land with no positive INHERITED_RED_MAX_AGE beside it, which reads park"*"rc=1")
      ok "IR AC17 land with the bound '$_b' reads park, announced, and blocks" ;;
    *) bad "IR AC17 land with the bound '$_b' must read park, got: $_o" ;;
  esac
done

# AC4: an inherited green whose base IS the remote sha selects the scoped gate and names itself; once
# the remote moves past that base, the same stamp forces FULL.
build_ir_fixture ac4 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC4 could not build its fixture"
git commit -q --allow-empty -m c1 >/dev/null 2>&1
write_ir_stamp "$(git rev-parse HEAD)" "$IR_R" 10
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c2 && git push origin main' 2>&1 )
case "$_o" in
  *"scoped gate on main push"*"inherited green"*"at base ${IR_R:0:8}"*) ok "IR AC4 an inherited green at the remote sha scopes the gate" ;;
  *) bad "IR AC4 expected a scoped gate naming the inherited green, got: $_o" ;;
esac
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c3 && git push origin main' 2>&1 )
case "$_o" in
  *"FULL gate on main push"*"the inherited green was earned against base ${IR_R:0:8}"*) ok "IR AC4 a moved remote sha forces FULL past the inherited green" ;;
  *) bad "IR AC4 expected FULL naming the stale base, got: $_o" ;;
esac

# AC14: a stamp written under max_age 50 while the bound at R is 10 forces FULL, naming both.
build_ir_fixture ac14 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC14 could not build its fixture"
write_ir_stamp "$(git rev-parse HEAD)" "$IR_R" 50
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c && git push origin main' 2>&1 )
case "$_o" in
  *"FULL gate on main push"*"written under max_age 50 and the bound at ${IR_R:0:8} is 10"*) ok "IR AC14 a stamp's wider window is not trusted" ;;
  *) bad "IR AC14 expected FULL naming both bounds, got: $_o" ;;
esac

# AC16: a STALE full green that predicate 2 refuses does not hide a usable inherited green.
build_ir_fixture ac16 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC16 could not build its fixture"
git checkout -q -b elsewhere; git commit -q --allow-empty -m off >/dev/null 2>&1; _off=$(git rev-parse HEAD); git checkout -q main
printf 'sha\t%s\nfingerprint\t\nmanifest_blob\t\nrun_id\ttest\n' "$_off" > "$(git rev-parse --git-dir)/gate-full-green"
write_ir_stamp "$(git rev-parse HEAD)" "$IR_R" 10
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c && git push origin main' 2>&1 )
case "$_o" in
  *"scoped gate on main push"*"inherited green"*"is not an ancestor of the pushed tip"*) ok "IR AC16 a stale full green still reaches the inherited green" ;;
  *) bad "IR AC16 expected a scoped gate over a stale full green, got: $_o" ;;
esac

# AC11, the hook's half: its own reader, sliced out of the SHIPPED hook, run over this repository at
# HEAD, resolves land with a bound of 10.
_ir_fns=$(awk '/^read_policy_key\(\)/,/^}/; /^read_policy_at\(\)/,/^}/' "$SRC/.githooks/pre-push")
_o=$( cd "$SRC" && _gate_env_rel=".githooks/gate-env.sh" && def=main && eval "$_ir_fns" \
      && read_policy_at "$(git rev-parse HEAD)" && printf '%s %s' "$PP_POLICY" "$PP_MAX_AGE" )
case "$_o" in
  "land 10") ok "IR AC11 this repository at HEAD reads land with an age bound of 10" ;;
  *) bad "IR AC11 this repository at HEAD read: ${_o:-<nothing>}" ;;
esac

cd "$pfx_home" || exit 2

# ---- TOOL-dDerivedDocket-26: AN EXIT 0 IS NOT A VERDICT UNTIL THE RUN RECORD SAYS SO ------------------
# A STUB RUNNER at the hook's DEFAULT command, with GOV_GATE_CMD unset, because an override command is
# announced and not checked. It exits 0 in every mode; the variable is what it writes into the run
# record of the id the hook pinned. The GREEN mode is the control: without it a hook that blocked
# every push would pass the two arms that expect a block.
build_vr_fixture() { # tag -> a pushed main whose tree carries the stub runner; cwd moves into its work tree
  local d="$tmp/vr-$1"
  mkdir -p "$d/hooks"; cp "$SRC/.githooks/pre-push" "$d/hooks/pre-push"
  git init -q --bare "$d/remote.git"; git init -q "$d/work"
  cd "$d/work" || return 1
  git config user.email t@example.com; git config user.name t
  git config core.hooksPath "$d/hooks"
  mkdir -p "$KIT_REL/run-gates"
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > "$KIT_REL/gate-legs.json"
  cat > "$KIT_REL/run-gates/run-gates.sh" <<'VRSTUB'
#!/usr/bin/env bash
[ -n "${VR_IDS:-}" ] && printf '%s\n' "$GATE_RUN_ID" >> "$VR_IDS"
d="$(git rev-parse --git-dir)/gate-run/$GATE_RUN_ID"
case "${VR_MODE:-none}" in
  green) mkdir -p "$d" && printf 'verdict\tGREEN\n' > "$d/verdict" ;;
  red)   mkdir -p "$d" && printf 'verdict\tRED\n' > "$d/verdict" ;;
esac
exit 0
VRSTUB
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$d/remote.git"
  touch "$(git rev-parse --git-dir)/push-main-active"
  GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1
}
run_vr_push() { # [env assignments…] -> VR_OUT and VR_RC, the push's merged output and its status
  git commit -q --allow-empty -m "vr $RANDOM" >/dev/null 2>&1
  VR_OUT=$( env -u GOV_GATE_CMD -u GATE_RUN_ID GATE_SELFTESTS= "$@" git push origin main 2>&1 ); VR_RC=$?
}
build_vr_fixture ac5 || bad "VR could not build its fixture"
# AC5, the hook's half: a runner that exits 0 and writes NO record is blocked — the
# TOOL-aSurfacedLexicon-25 shape, where the status alone let a push through with no bar run.
run_vr_push VR_MODE=none
case "$VR_RC|$VR_OUT" in
  1*"left no verdict in its run record"*) ok "VR AC5 an exit 0 with no run record is blocked, naming the missing verdict" ;;
  *) bad "VR AC5 an exit 0 with no run record must block, got rc $VR_RC: $VR_OUT" ;;
esac
git reset -q --hard origin/main
run_vr_push VR_MODE=red
case "$VR_RC|$VR_OUT" in
  1*"reads verdict 'RED', not GREEN"*) ok "VR AC5 an exit 0 over a RED record is blocked" ;;
  *) bad "VR AC5 an exit 0 over a RED record must block, got rc $VR_RC: $VR_OUT" ;;
esac
git reset -q --hard origin/main
run_vr_push VR_MODE=green
[ "$VR_RC" = 0 ] && ok "VR control: an exit 0 over its own GREEN record lands" \
  || bad "VR control: an exit 0 over its own GREEN record must land, got rc $VR_RC: $VR_OUT"
# AC15: an inherited GATE_RUN_ID naming a pre-planted GREEN record buys nothing, because the hook pins
# and clears its OWN id; and two consecutive pushes pin two different ids.
_vgd=$(git rev-parse --git-dir)
mkdir -p "$_vgd/gate-run/planted"; printf 'verdict\tGREEN\n' > "$_vgd/gate-run/planted/verdict"
run_vr_push VR_MODE=none GATE_RUN_ID=planted
[ "$VR_RC" = 1 ] && ok "VR AC15 an inherited id naming a planted GREEN record is not honoured" \
  || bad "VR AC15 a planted GREEN record under an inherited id satisfied the boundary: rc $VR_RC: $VR_OUT"
git reset -q --hard origin/main
: > "$tmp/vr-ids"
run_vr_push VR_MODE=green VR_IDS="$tmp/vr-ids"; run_vr_push VR_MODE=green VR_IDS="$tmp/vr-ids"
case "$(sort -u "$tmp/vr-ids" | grep -c .)|$(grep -c '^planted$' "$tmp/vr-ids")" in
  "2|0") ok "VR AC15 two pushes pin two different ids, neither the inherited one" ;;
  *) bad "VR AC15 the stub runner saw these ids: $(tr '\n' ' ' < "$tmp/vr-ids")" ;;
esac
# S6's announcement: an override command is not the runner and writes no record, so it is not checked.
git commit -q --allow-empty -m "vr override" >/dev/null 2>&1
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" git push origin main 2>&1 ); _r=$?
case "$_r|$_o" in
  0*"its run record is not checked for an override command"*) ok "VR an override command lands and the skipped record check is announced" ;;
  *) bad "VR an override command must land with the skip announced, got rc $_r: $_o" ;;
esac
cd "$pfx_home" || exit 2

[ "$fail" = 0 ] && { echo "pre-push.test: all cases ok"; exit 0; } || { echo "pre-push.test: FAILURES"; exit 1; }
