#!/usr/bin/env bash
# push-main.test.sh — proves tools/push-main.sh + the pre-push marker gate (TOOL-aLeasedGauntlet-1),
# against a scratch bare remote with a STUBBED gate (GOV_GATE_CMD). Exit 0 = all cases pass.
set -u
SRC=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 2; }
[ -f "$SRC/tools/push-main.sh" ] || { echo "tools/push-main.sh missing"; exit 1; }
[ -f "$SRC/.githooks/pre-push" ] || { echo ".githooks/pre-push missing"; exit 1; }

tmp=$(mktemp -d) || exit 2
trap 'rm -rf "$tmp"' EXIT
fail=0
ok()  { echo "  ok   — $1"; }
bad() { echo "  FAIL — $1"; fail=1; }

# stub gate: RED iff $tmp/gate-fail; on $tmp/race-once, advance origin behind our back, then remove it.
cat > "$tmp/stub.sh" <<STUB
#!/usr/bin/env bash
if [ -f "$tmp/race-once" ]; then rm -f "$tmp/race-once"; git -C "$tmp/racer" commit -q --allow-empty -m race; git -C "$tmp/racer" push -q origin main; fi
[ -f "$tmp/gate-fail" ] && exit 1 || exit 0
STUB
chmod +x "$tmp/stub.sh"
export GOV_GATE_CMD="bash $tmp/stub.sh"
# The scratch work repo is `git init`+`remote add` (origin/HEAD unset); pin the default so the hook's
# and lander's fail-CLOSED resolution doesn't refuse every case (that path is tested by cases 7-8).
export GOV_DEFAULT_BRANCH=main

setup_repo() {  # $1 = repo dir
  local r=$1
  git init -q "$r"; cd "$r" || exit 2
  git config user.email t@e; git config user.name t
  mkdir -p tools .githooks
  cp "$SRC/tools/push-main.sh" tools/push-main.sh
  cp "$SRC/.githooks/pre-push"  .githooks/pre-push
  git config core.hooksPath .githooks
  git add -A && git commit -q -m init && git branch -M main
  git remote add origin "$tmp/remote.git"
}

git init -q --bare "$tmp/remote.git"
setup_repo "$tmp/work"
git push -q --no-verify origin main
git -C "$tmp/remote.git" symbolic-ref HEAD refs/heads/main
git clone -q "$tmp/remote.git" "$tmp/racer"
git -C "$tmp/racer" checkout -q -B main origin/main
git -C "$tmp/racer" config user.email r@e; git -C "$tmp/racer" config user.name r
cd "$tmp/work" || exit 2

# 1 — hook refuses a raw default-branch push (no marker)
git commit -q --allow-empty -m c1
if git push -q origin main 2>/dev/null; then bad "1 raw push must be refused (no marker)"; else ok "1 raw push refused (no marker)"; fi

# 2 — push-main lands it; marker cleared after
if bash tools/push-main.sh >/dev/null 2>&1; then ok "2 push-main lands (marker + green gate)"; else bad "2 push-main should land"; fi
[ -f "$(git rev-parse --git-dir)/push-main-active" ] && bad "2b marker leaked" || ok "2b marker cleared"

# 3 — reconcile-before-gate
git -C "$tmp/racer" pull -q; git -C "$tmp/racer" commit -q --allow-empty -m ahead; git -C "$tmp/racer" push -q origin main
git commit -q --allow-empty -m c3
if bash tools/push-main.sh >/dev/null 2>&1 && git log -1 --format=%s | grep -q 'push-main reconcile'; then ok "3 reconcile-before-gate then landed"; else bad "3 should reconcile then land"; fi

# 4 — red gate surfaced, not retried
touch "$tmp/gate-fail"; git commit -q --allow-empty -m c4
if bash tools/push-main.sh >/dev/null 2>&1; then bad "4 red gate must block"; else ok "4 red gate surfaced"; fi
rm -f "$tmp/gate-fail"

# 5 — mid-gate race → re-gate → land
git -C "$tmp/racer" pull -q; touch "$tmp/race-once"; git commit -q --allow-empty -m c5
if bash tools/push-main.sh >/dev/null 2>&1; then ok "5 mid-gate race recovered + landed"; else bad "5 should recover from a mid-gate race"; fi
rm -f "$tmp/race-once"

# 6 — conflicting reconcile aborts clean
git -C "$tmp/racer" pull -q; echo racer > "$tmp/racer/CONF"; git -C "$tmp/racer" add CONF; git -C "$tmp/racer" commit -q -m rc; git -C "$tmp/racer" push -q origin main
echo mine > CONF; git add CONF; git commit -q -m mc
bash tools/push-main.sh >/dev/null 2>&1
if [ -z "$(git status --porcelain)" ] && [ ! -f "$(git rev-parse --git-dir)/push-main-active" ]; then ok "6 conflict aborted clean, marker gone"; else bad "6 conflict must abort clean"; fi

# 7 — a DIRTY working tree is refused early (commit/stash), NOT misreported as a reconcile conflict
echo v1 > junk; git add junk; git commit -q -m junk; echo v2 > junk
out7=$(bash tools/push-main.sh 2>&1)
case "$out7" in *"uncommitted changes"*) ok "7 dirty tree refused early (commit/stash)";; *) bad "7 dirty tree must be refused: $out7";; esac
git checkout -q -- junk 2>/dev/null || true

# 8 — the lander fails CLOSED when the default branch is unresolvable (origin/HEAD unset here)
out8=$( ( unset GOV_DEFAULT_BRANCH; bash tools/push-main.sh 2>&1 ) )
case "$out8" in *"determine the default branch"*) ok "8 unresolvable default → fail closed";; *) bad "8 expected fail-closed: $out8";; esac

[ "$fail" = 0 ] && { echo "push-main.test: all cases ok"; exit 0; } || { echo "push-main.test: FAILURES"; exit 1; }
