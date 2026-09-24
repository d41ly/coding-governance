#!/usr/bin/env bash
# push-main.test.sh — proves push-main.sh + the pre-push marker gate (TOOL-aLeasedGauntlet-1),
# against a scratch bare remote with a STUBBED gate (GOV_GATE_CMD). Exit 0 = all cases pass.
set -u
# THE SUBJECT IS FOUND FROM THIS FILE'S OWN LOCATION (TOOL-aRepatriatedFork-8 S6). This suite ships
# beside its lander to whatever prefix an adopter installs the kit at (`scripts/` at inCMS), and it
# used to spell `tools/` for both, so an adopter had to fork it to run it. KIT_REL is where the pair
# sits relative to the root, as git reports it: `tools/` here, empty at a root install.
HERE=$(cd "$(dirname "$0")" && pwd)
SRC=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 2; }
KIT_REL=$(git -C "$HERE" rev-parse --show-prefix 2>/dev/null)
[ -f "$HERE/push-main.sh" ] || { echo "push-main.sh missing beside this suite"; exit 1; }
[ -f "$SRC/.githooks/pre-push" ] || { echo ".githooks/pre-push missing"; exit 1; }
lander="${KIT_REL}push-main.sh"   # the lander's path inside every fixture, the same prefix as here

tmp=$(mktemp -d) || exit 2
trap 'rm -rf "$tmp"' EXIT
fail=0
ok()  { echo "  ok   — $1"; }
bad() { echo "  FAIL — $1"; fail=1; }

# stub gate: RED iff $tmp/gate-fail; on $tmp/race-once, advance origin behind our back, then remove it.
# A RED run prints `connection`, the word the pre-S2 lander read as an unreachable remote (case 4c).
cat > "$tmp/stub.sh" <<STUB
#!/usr/bin/env bash
if [ -f "$tmp/race-once" ]; then rm -f "$tmp/race-once"; git -C "$tmp/racer" commit -q --allow-empty -m race; git -C "$tmp/racer" push -q origin main; fi
[ -f "$tmp/gate-fail" ] && { echo "FAKE LEG: lost its connection to the test database"; exit 1; } || exit 0
STUB
chmod +x "$tmp/stub.sh"
export GOV_GATE_CMD="bash $tmp/stub.sh"
# THE DECLARED TEST ESCAPE (TOOL-aRepatriatedFork-5). The stub above lives under mktemp and is
# untracked by construction, and .githooks/pre-push refuses an untracked merge bar. This waives the
# tracked-file requirement, marks the hook's decision line 'bar: STUB', and makes push-main withhold
# the lander marker, which case 9 grades. Case 9b unsets it deliberately.
export GOV_GATE_CMD_TEST=1
# The scratch work repo is `git init`+`remote add` (origin/HEAD unset); pin the default so the hook's
# and lander's fail-CLOSED resolution doesn't refuse every case (that path is tested by cases 7-8).
export GOV_DEFAULT_BRANCH=main

setup_repo() {  # $1 = repo dir · $2 = remote name (origin) · $3 = remote path ($tmp/remote.git)
  local r=$1 name=${2:-origin} url=${3:-$tmp/remote.git}
  git init -q "$r"; cd "$r" || exit 2
  git config user.email t@e; git config user.name t
  mkdir -p "./$KIT_REL" .githooks
  cp "$HERE/push-main.sh" "$lander"
  cp "$SRC/.githooks/pre-push"  .githooks/pre-push
  git config core.hooksPath .githooks
  git add -A && git commit -q -m init && git branch -M main
  git remote add "$name" "$url"
}

git init -q --bare "$tmp/remote.git"
setup_repo "$tmp/work"
git push -q --no-verify origin main
git -C "$tmp/remote.git" symbolic-ref HEAD refs/heads/main
git clone -q "$tmp/remote.git" "$tmp/racer"
git -C "$tmp/racer" checkout -q -B main origin/main
git -C "$tmp/racer" config user.email r@e; git -C "$tmp/racer" config user.name r
cd "$tmp/work" || exit 2
gitdir=$(git rev-parse --git-dir)
read_refusal_token() { [ -s "$gitdir/pre-push-refusal" ] && cut -f1 < "$gitdir/pre-push-refusal" || echo ""; }

# 1 — hook refuses a raw default-branch push (no marker)
git commit -q --allow-empty -m c1
if git push -q origin main 2>/dev/null; then bad "1 raw push must be refused (no marker)"; else ok "1 raw push refused (no marker)"; fi
# 1b — and records WHY as a machine token the lander reads, not as prose (TOOL-aRepatriatedFork-8 S2).
[ "$(read_refusal_token)" = raw-push ] && ok "1b the refusal is recorded as the token raw-push" || bad "1b refusal token should be raw-push, got '$(read_refusal_token)'"

# 2 — push-main lands it; marker cleared after
if bash "$lander" >/dev/null 2>&1; then ok "2 push-main lands (marker + green gate)"; else bad "2 push-main should land"; fi
[ -f "$gitdir/push-main-active" ] && bad "2b marker leaked" || ok "2b marker cleared"
# 2c — case 1's token does not survive a later SUCCESSFUL push, or the lander would one day report a
#      refusal that never happened.
[ -f "$gitdir/pre-push-refusal" ] && bad "2c a stale refusal token survived a successful push" || ok "2c a successful push leaves no refusal token"

# 3 — reconcile-before-gate
git -C "$tmp/racer" pull -q; git -C "$tmp/racer" commit -q --allow-empty -m ahead; git -C "$tmp/racer" push -q origin main
git commit -q --allow-empty -m c3
if bash "$lander" >/dev/null 2>&1 && git log -1 --format=%s | grep -q 'push-main reconcile'; then ok "3 reconcile-before-gate then landed"; else bad "3 should reconcile then land"; fi

# 4 — red gate surfaced, not retried
touch "$tmp/gate-fail"; git commit -q --allow-empty -m c4
out4=$(bash "$lander" 2>&1); rc4=$?
if [ "$rc4" -eq 0 ]; then bad "4 red gate must block"; else ok "4 red gate surfaced"; fi
# 4c — reported as a bar that RAN and is red, from the hook's token. The stub printed `connection`,
#      which the pre-S2 lander, grepping the push's own output, reported as an unreachable remote.
case "$out4" in
  *"could not reach"*)      bad "4c a red bar was misreported as an unreachable remote: $out4" ;;
  *"no leg ran"*)           bad "4c a red bar was misreported as a precondition refusal: $out4" ;;
  *"bar RAN and is RED"*"gate-last-summary.txt"*) ok "4c a red bar is reported as a bar that ran, naming its summary file" ;;
  *)                        bad "4c the red-bar message is unrecognised: $out4" ;;
esac
rm -f "$tmp/gate-fail"

# 5 — mid-gate race → re-gate → land
git -C "$tmp/racer" pull -q; touch "$tmp/race-once"; git commit -q --allow-empty -m c5
if bash "$lander" >/dev/null 2>&1; then ok "5 mid-gate race recovered + landed"; else bad "5 should recover from a mid-gate race"; fi
rm -f "$tmp/race-once"

# 6 — conflicting reconcile aborts clean
git -C "$tmp/racer" pull -q; echo racer > "$tmp/racer/CONF"; git -C "$tmp/racer" add CONF; git -C "$tmp/racer" commit -q -m rc; git -C "$tmp/racer" push -q origin main
echo mine > CONF; git add CONF; git commit -q -m mc
bash "$lander" >/dev/null 2>&1
if [ -z "$(git status --porcelain)" ] && [ ! -f "$gitdir/push-main-active" ]; then ok "6 conflict aborted clean, marker gone"; else bad "6 conflict must abort clean"; fi

# 7 — a DIRTY working tree is refused early (commit/stash), NOT misreported as a reconcile conflict
echo v1 > junk; git add junk; git commit -q -m junk; echo v2 > junk
out7=$(bash "$lander" 2>&1)
case "$out7" in *"uncommitted changes"*) ok "7 dirty tree refused early (commit/stash)";; *) bad "7 dirty tree must be refused: $out7";; esac
git checkout -q -- junk 2>/dev/null || true

# 8 — the lander fails CLOSED when the default branch is unresolvable (origin/HEAD unset here)
out8=$( ( unset GOV_DEFAULT_BRANCH; bash "$lander" 2>&1 ) )
case "$out8" in *"determine the default branch"*) ok "8 unresolvable default → fail closed";; *) bad "8 expected fail-closed: $out8";; esac

# 9 — a push gated by the declared STUB is not a landing: with LANDER_MARKER declared, push-main lands
#     the push under GOV_GATE_CMD_TEST, writes NO marker, and says why. Without this, a stub-gated push
#     leaves exactly the artifact `unattended.sh --landed` accepts (TOOL-aRepatriatedFork-5).
#     Back onto origin first: case 6 left a conflicting commit that would stop the reconcile.
git fetch -q origin main && git reset -q --hard origin/main
printf 'LANDER_MARKER=unattended-landed\n' > .unattended.conf
git add .unattended.conf && git commit -q -m lander-conf
gcd=$(cd "$(git rev-parse --git-common-dir)" && pwd)
rm -f "$gcd/unattended-landed"
out9=$(bash "$lander" 2>&1); rc9=$?
if [ "$rc9" -ne 0 ]; then bad "9 push-main should land under the stub: $out9"
elif [ -f "$gcd/unattended-landed" ]; then bad "9 a STUB-gated push wrote the lander marker: $(cat "$gcd/unattended-landed")"
else
  case "$out9" in
    *"NOT writing the lander marker"*) ok "9 a STUB-gated landing writes no lander marker, and says so" ;;
    *) bad "9 the marker was withheld without saying why: $out9" ;;
  esac
fi

# 9b — ITS CONTROL: the same lander with a TRACKED bar and no escape writes the marker naming the
#      pushed commit. Without it, 9 passes on a push-main that never writes a marker at all.
#      The bar is DECLARED as the conf's GATE_CMD, since the hook refuses an undeclared one (closing
#      review round 1 M1), and the marker names it by class and path after the pushed commit.
printf '#!/usr/bin/env bash\nexit 0\n' > bar.sh
printf 'GATE_CMD="bash bar.sh"\n' >> .unattended.conf
git add bar.sh .unattended.conf && git commit -q -m tracked-bar
out9b=$( ( unset GOV_GATE_CMD_TEST; GOV_GATE_CMD="bash bar.sh" bash "$lander" 2>&1 ) ); rc9b=$?
if [ "$rc9b" -eq 0 ] && grep -q "$(git rev-parse HEAD) by push-main bar tracked bar.sh " "$gcd/unattended-landed" 2>/dev/null; then
  ok "9b control — a push gated by a tracked bar writes the lander marker naming the pushed commit and the bar"
else
  bad "9b a tracked-bar landing did not write its marker naming the bar (rc $rc9b): $out9b | $(cat "$gcd/unattended-landed" 2>/dev/null)"
fi

# H1 — ONE CHANNEL (closing review round 1 H1). The hook and this lander used to answer "was the bar a
#      stub?" from two environments, and the hook's includes whatever gate-env.sh sets. Here a
#      COMMITTED gate-env.sh sets the escape and names `true`, over a default bar that would be RED
#      (this fixture has no runner at all). The lander's own environment carries no escape, and it
#      must still withhold the marker, because the hook's verdict says `stub`.
mkdir -p .githooks
printf 'GOV_GATE_CMD_TEST=1\nGOV_GATE_CMD=true\n' > .githooks/gate-env.sh
git add .githooks/gate-env.sh && git commit -q -m h1-env
rm -f "$gcd/unattended-landed"
outh1=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; bash "$lander" 2>&1 ) ); rch1=$?
if [ -f "$gcd/unattended-landed" ]; then
  bad "H1 a stub set by a committed gate-env.sh still got the lander marker: $(cat "$gcd/unattended-landed")"
else
  case "$rch1:$outh1" in
    0:*"STUB"*"NOT writing the lander marker"*) ok "H1 a stub set by gate-env.sh lands with NO marker, read from the hook's verdict" ;;
    *) bad "H1 expected a landing with the marker withheld as a STUB (rc $rch1): $outh1" ;;
  esac
fi
git rm -q .githooks/gate-env.sh && git commit -q -m h1-env-gone

# H1b — the same file UNTRACKED and hidden by .git/info/exclude, which `git status` never reports, so
#       neither dirty check sees it. The hook must refuse to source it, so nothing lands and no marker.
printf 'GOV_GATE_CMD_TEST=1\nGOV_GATE_CMD=true\n' > .githooks/gate-env.sh
mkdir -p "$gitdir/info"; cp "$gitdir/info/exclude" "$tmp/exclude.keep" 2>/dev/null || : > "$tmp/exclude.keep"
printf '.githooks/gate-env.sh\n' >> "$gitdir/info/exclude"
before1b=$(git -C "$tmp/remote.git" rev-parse main)
outh1b=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; bash "$lander" 2>&1 ) ); rch1b=$?
if [ -f "$gcd/unattended-landed" ]; then
  bad "H1b an excluded gate-env.sh setting the escape still got the lander marker: $(cat "$gcd/unattended-landed")"
elif [ "$before1b" != "$(git -C "$tmp/remote.git" rev-parse main)" ]; then
  bad "H1b an excluded gate-env.sh was sourced and the push LANDED (rc $rch1b): $outh1b"
else
  case "$outh1b" in
    *"gate-env.sh"*"bar-refused"*) ok "H1b an excluded gate-env.sh is refused before it is sourced: no landing, no marker" ;;
    *) bad "H1b nothing landed, but not for the stated reason (rc $rch1b): $outh1b" ;;
  esac
fi
rm -f .githooks/gate-env.sh; cp "$tmp/exclude.keep" "$gitdir/info/exclude"

# 11 — an untracked file in the SUPERPROJECT blocks (S3). `-uno`, this lander's old definition of
#      dirty, passed it, and the bar then certified a file the push did not carry.
echo 'x = 1' > brand_new_module.py
out11=$(bash "$lander" 2>&1)
case "$out11" in
  *"uncommitted changes"*"brand_new_module.py"*) ok "11 an untracked superproject file blocks, and is named" ;;
  *) bad "11 an untracked superproject file must block: $out11" ;;
esac
rm -f brand_new_module.py

# 12 — no wording in the bar's output can FAKE a race or an outage (S2; inCMS's ABL-aWeighedAssay-2).
#      The remote refuses by pre-receive while the stub, GREEN, floods both poison words. The remote
#      does not move and the hook wrote no verdict, so the one correct reading is "reachable,
#      unchanged, unclaimed", reported once, after exactly one bar run. A re-gate is the regression.
cat > "$tmp/noise.sh" <<'NOISE'
#!/usr/bin/env bash
echo "  ! [rejected] some-fixture -> some-fixture (fetch first, stale info)"
echo "  worker: connection reset by peer, could not read from remote"
exit 0
NOISE
git commit -q --allow-empty -m c12
before12=$(git -C "$tmp/remote.git" rev-parse main)
printf '#!/bin/sh\nexit 1\n' > "$tmp/remote.git/hooks/pre-receive"; chmod +x "$tmp/remote.git/hooks/pre-receive"
out12=$(GOV_GATE_CMD="bash $tmp/noise.sh" bash "$lander" 2>&1); rc12=$?
rm -f "$tmp/remote.git/hooks/pre-receive"
gates12=$(printf '%s\n' "$out12" | grep -c 'gating + pushing')
if [ "$before12" != "$(git -C "$tmp/remote.git" rev-parse main)" ]; then
  bad "12 fixture broken: the remote accepted a push it was told to refuse"
else
  case "$out12" in
    *"advanced during the gate"*|*"moving faster than the gate"*) bad "12 the bar's output faked a race; the bar ran $gates12 time(s)" ;;
    *"could not reach"*) bad "12 the bar's output faked an unreachable remote: $out12" ;;
    *) if [ "$rc12" = 1 ] && [ "$gates12" = 1 ]; then ok "12 the bar's own words cannot fake a race or an outage (one run, rc 1)"
       else bad "12 expected one bar run and rc 1 (rc $rc12, runs $gates12): $out12"; fi ;;
  esac
fi

# AC5 — an unreachable remote with no verdict is reported only after a PROBE of it fails. The push
#       URL is pointed at nothing while the fetch URL still works, so the push dies before the hook.
git remote set-url --push origin "$tmp/nowhere.git"
out5u=$(bash "$lander" 2>&1); rc5u=$?
git config --unset remote.origin.pushurl
case "$rc5u:$out5u" in
  1:*"could not reach origin"*"probe"*) ok "AC5 an unreachable push URL is reported after its probe fails" ;;
  *) bad "AC5 expected the probed-unreachable verdict at rc 1, got rc $rc5u: $out5u" ;;
esac

# 13 — ONE definition of dirty, in the lander and the hook alike (S3). When they disagreed at inCMS
#      (ARCH-dWaryGatepost-1) the lander cleared a push the hook then refused. Compared as a STRING:
#      the failure this gates is a divergence in the flag.
DIRTY_PRED='git status --porcelain --ignore-submodules=untracked'
pm_hits=$(grep -cF -- "$DIRTY_PRED" "$HERE/push-main.sh" || true)
hk_hits=$(grep -cF -- "$DIRTY_PRED" "$SRC/.githooks/pre-push" || true)
if [ "${pm_hits:-0}" -ge 1 ] && [ "${hk_hits:-0}" -ge 1 ]; then
  ok "13 the lander and the hook share one dirty definition"
else
  bad "13 the dirty definition diverged: push-main.sh ${pm_hits:-0}, .githooks/pre-push ${hk_hits:-0} occurrence(s) of '$DIRTY_PRED'"
fi

# 14 — and the RETIRED spelling does not come back beside it, which is what a careless merge makes.
for f in "$HERE/push-main.sh" "$SRC/.githooks/pre-push"; do
  if grep -qE 'git status --porcelain -uno' "$f"; then bad "14 ${f##*/} carries the retired '-uno' dirty definition"
  else ok "14 ${f##*/} carries no retired dirty definition"; fi
done

# AC1 — a remote NOT named origin (inCMS's node `d` names it `incms`): the lander resolves the remote
#       first and reads ITS HEAD, and the hook reads the remote git names in $1. With no
#       GOV_DEFAULT_BRANCH exported, the pre-S1 lander exited 2 before its first fetch.
git init -q --bare "$tmp/incms.git"
setup_repo "$tmp/wi" incms "$tmp/incms.git"
git push -q --no-verify incms main
git -C "$tmp/incms.git" symbolic-ref HEAD refs/heads/main
git remote set-head incms main >/dev/null 2>&1
git commit -q --allow-empty -m ci
out1i=$( ( unset GOV_DEFAULT_BRANCH; bash "$lander" 2>&1 ) ); rc1i=$?
if [ "$rc1i" -eq 0 ] && [ "$(git -C "$tmp/incms.git" rev-parse main)" = "$(git rev-parse HEAD)" ]; then
  ok "AC1 a remote named incms lands with no GOV_DEFAULT_BRANCH"
else
  bad "AC1 a remote named incms did not land (rc $rc1i): $out1i"
fi
# ...and with SEVERAL remotes and none configured for the branch it refuses rather than guess (F2).
git remote add second "$tmp/remote.git"
out2r=$( ( unset GOV_DEFAULT_BRANCH; bash "$lander" 2>&1 ) ); rc2r=$?
case "$rc2r:$out2r" in
  2:*"GOV_REMOTE"*) ok "AC1 several remotes and none configured is refused, naming GOV_REMOTE" ;;
  *) bad "AC1 expected a refusal naming GOV_REMOTE with two remotes, got rc $rc2r: $out2r" ;;
esac
cd "$tmp" || exit 2

[ "$fail" = 0 ] && { echo "push-main.test: all cases ok"; exit 0; } || { echo "push-main.test: FAILURES"; exit 1; }
