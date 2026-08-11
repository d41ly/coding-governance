#!/usr/bin/env bash
# pre-push.test.sh — drives a REAL git push through .githooks/pre-push in a throwaway scratch repo,
# with the gate stubbed via GOV_GATE_CMD so the bar never actually runs. Proves the hook FIRES and
# classifies correctly. Exit 0 = all cases ok.
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

[ "$fail" = 0 ] && { echo "pre-push.test: all cases ok"; exit 0; } || { echo "pre-push.test: FAILURES"; exit 1; }
