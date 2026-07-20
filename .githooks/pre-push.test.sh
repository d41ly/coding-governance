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

[ "$fail" = 0 ] && { echo "pre-push.test: all cases ok"; exit 0; } || { echo "pre-push.test: FAILURES"; exit 1; }
