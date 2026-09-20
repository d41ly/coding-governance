#!/usr/bin/env bash
# push-main.test.sh — proves tools/push-main.sh + the pre-push marker gate (TOOL-aLeasedGauntlet-1),
# against a scratch bare remote with a STUBBED gate (GOV_GATE_CMD). Exit 0 = all cases pass.
#
# Cases 1-8 are the ATTENDED landing, from a primary tree with the default branch checked out.
# Cases 9-22 are the IN-PLACE landing flags (TOOL-dDerivedDocket-2), over a second fixture that adds
# what they need: a linked worktree on a run branch, and a local default branch carrying commits
# nobody pushed. What this file does NOT check: anything about a real remote or a real bar — the
# gate is stubbed and every remote here is a path on disk.
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
if [ -f "$tmp/race2-once" ]; then rm -f "$tmp/race2-once"; git -C "$tmp/racer2" commit -q --allow-empty -m race2; git -C "$tmp/racer2" push -q origin main; fi
[ -f "$tmp/gate-fail" ] && exit 1 || exit 0
STUB
chmod +x "$tmp/stub.sh"
export GOV_GATE_CMD="bash $tmp/stub.sh"
# The scratch work repo is `git init`+`remote add` (origin/HEAD unset); pin the default so the hook's
# and lander's fail-CLOSED resolution doesn't refuse every case (that path is tested by cases 7-8).
export GOV_DEFAULT_BRANCH=main

setup_repo() {  # $1 = repo dir · $2 = its bare remote, defaulting to the first one
  local r=$1
  local rem=${2:-$tmp/remote.git}
  git init -q "$r"; cd "$r" || exit 2
  git config user.email t@e; git config user.name t
  mkdir -p tools .githooks
  cp "$SRC/tools/push-main.sh" tools/push-main.sh
  cp "$SRC/.githooks/pre-push"  .githooks/pre-push
  git config core.hooksPath .githooks
  git add -A && git commit -q -m init && git branch -M main
  git remote add origin "$rem"
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


# ---- THE IN-PLACE LANDING FLAGS — TOOL-dDerivedDocket-2 -----------------------------------------
# A SECOND fixture, because these cases need a shape the one above does not have: a bare remote, a
# primary tree with the default branch checked out, and a LINKED WORKTREE on a run branch. Every arm
# below was observed RED against a staged break of the flag it covers before it landed — the push
# spelled as the local default branch, the carry set computed as T minus that branch, a precondition
# that accepts any two-parent HEAD, an observation failure sharing exit 2 with an argument refusal,
# and an unrecognised argument falling through to the attended path.
git init -q --bare "$tmp/remote2.git"
setup_repo "$tmp/work2" "$tmp/remote2.git"
echo seed > src-seed.txt; git add src-seed.txt; git commit -q -m seed
git push -q --no-verify origin main
git -C "$tmp/remote2.git" symbolic-ref HEAD refs/heads/main
git clone -q "$tmp/remote2.git" "$tmp/racer2"
git -C "$tmp/racer2" config user.email r@e; git -C "$tmp/racer2" config user.name r
git worktree add -q "$tmp/wt" -b feat main

build_main() {  # local main back onto the remote tip; the caller adds whatever it needs on top
  git -C "$tmp/work2" fetch -q origin
  git -C "$tmp/work2" reset -q --hard origin/main
}
build_feat() {  # the run branch, off the remote tip, carrying one commit of this build
  git -C "$tmp/wt" checkout -q -B feat "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
  echo "u1 $RANDOM" > "$tmp/wt/src-u1.txt"
  git -C "$tmp/wt" add src-u1.txt
  git -C "$tmp/wt" commit -q -m "TOOL-tFix-1: unit one"
}
run_wt() { ( cd "$tmp/wt" && bash tools/push-main.sh "$@" ) ; }

# 9 — --prepare makes the merge the whole design rests on: onto the ADVERTISED tip, branch moved
build_main; build_feat
oldb=$(git -C "$tmp/wt" rev-parse HEAD)
R=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
out9=$(run_wt --prepare --slug tFix 2>&1); rc9=$?
t=$(git -C "$tmp/wt" rev-parse HEAD)
p1=$(git -C "$tmp/wt" rev-parse HEAD^1); p2=$(git -C "$tmp/wt" rev-parse HEAD^2)
subj=$(git -C "$tmp/wt" log -1 --format=%s)
[ "$rc9" = 0 ] && [ "$p1" = "$R" ] && [ "$p2" = "$oldb" ] \
  && [ "$(git -C "$tmp/wt" rev-parse refs/heads/feat)" = "$t" ] \
  && [ "$(git -C "$tmp/wt" symbolic-ref --short HEAD)" = feat ] \
  && case "$subj" in "merge: tFix — land onto origin/main at ${R:0:8}") true ;; *) false ;; esac \
  && ok "9 prepared: first parent the advertised tip, second the old tip, branch moved, subject names the slug" \
  || bad "9 rc=$rc9 subj='$subj' p1=${p1:0:8} R=${R:0:8} p2=${p2:0:8} old=${oldb:0:8} $out9"
# 9b — and NO unit id in it: build_commit joins a commit to a unit by the id as a whole token, so an
# id here would make the landing merge some unit's build commit.
case "$subj" in *TOOL-*|*PLAY-*|*KICK-*|*DEPL-*) bad "9b the merge subject names a unit id: $subj" ;;
  *) ok "9b the merge subject names no unit id" ;; esac

# 10 — --prepared agrees with that, and writes nothing
st=$(git -C "$tmp/wt" rev-parse HEAD)$(git -C "$tmp/wt" rev-parse refs/heads/feat)$(git -C "$tmp/wt" status --porcelain)
out10=$(run_wt --prepared --slug tFix 2>&1); rc10=$?
st2=$(git -C "$tmp/wt" rev-parse HEAD)$(git -C "$tmp/wt" rev-parse refs/heads/feat)$(git -C "$tmp/wt" status --porcelain)
[ "$rc10" = 0 ] && [ "$st" = "$st2" ] && ok "10 --prepared 0 on a prepared HEAD, nothing moved" \
  || bad "10 rc=$rc10 $out10"

# 11 — the unattended kit's own build_commit answers the same before and after the prepare, which is
#      what the merge subject's missing unit id buys. The library is LOCATED and never spelled: this
#      file ships to adopters who install kits at their own prefix, or who carry no such kit at all,
#      and a skip that looks like a pass is indistinguishable from coverage.
lib=$(git -C "$SRC" ls-files -- '*lib-unattended.sh' 2>/dev/null | head -1)
if [ -n "$lib" ] && [ -f "$SRC/$lib" ]; then
  ( cd "$tmp/wt" && . "$SRC/$lib"
    build_commit "$(git rev-parse HEAD^2^)..HEAD^2" TOOL-tFix-1 memory/builds/tFix "" "" > "$tmp/bc-before" )
  ( cd "$tmp/wt" && . "$SRC/$lib"
    build_commit "$(git rev-parse HEAD^1)..HEAD" TOOL-tFix-1 memory/builds/tFix "" "" > "$tmp/bc-after" )
  if [ -s "$tmp/bc-before" ] && [ "$(cat "$tmp/bc-before")" = "$(cat "$tmp/bc-after")" ]; then
    ok "11 build_commit returns the same commit before and after --prepare"
  else
    bad "11 before=$(cat "$tmp/bc-before" 2>/dev/null) after=$(cat "$tmp/bc-after" 2>/dev/null)"
  fi
else
  echo "  skip — 11 build_commit: this tree carries no unattended-kit library, so the join this case grades does not exist here"
fi

# 12 — the hook refuses an unmarked worktree push; --land is accepted; and the foreign commit
#      sitting unpushed on local main stays there, which is the defect these flags close.
git -C "$tmp/work2" commit -q --allow-empty -m "TOOL-zOther-3: another build unit"
foreign=$(git -C "$tmp/work2" rev-parse HEAD)
if ( cd "$tmp/wt" && git push -q origin HEAD:refs/heads/main 2>/dev/null ); then
  bad "12 raw worktree push must be refused (no marker)"; else ok "12 raw worktree push refused"; fi
out12=$(run_wt --land --slug tFix 2>&1); rc12=$?
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc12" = 0 ] && [ "$rem" = "$t" ] && ok "12b --land pushed exactly the prepared merge" \
  || bad "12b rc=$rc12 remote=${rem:0:8} T=${t:0:8} $out12"
if git -C "$tmp/remote2.git" merge-base --is-ancestor "$foreign" "$rem" 2>/dev/null; then
  bad "12c the foreign commit on local main reached the remote"
else ok "12c the foreign commit on local main did not reach the remote"; fi
[ -f "$(git -C "$tmp/wt" rev-parse --git-dir)/push-main-active" ] && bad "12d marker leaked" || ok "12d marker cleared"

# 13 — merged in, that same commit refuses the landing, and --carry names the sha --land names
build_main
git -C "$tmp/work2" commit -q --allow-empty -m "TOOL-zOther-4: another build unit again"
foreign2=$(git -C "$tmp/work2" rev-parse HEAD)
build_feat
git -C "$tmp/wt" merge -q --no-ff -m "merge local main" main
run_wt --prepare --slug tFix >/dev/null 2>&1
outc=$(run_wt --carry --slug tFix 2>&1); rcc=$?
outl=$(run_wt --land --slug tFix 2>&1); rcl=$?
rem2=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rcc" = 1 ] && [ "$rcl" = 1 ] && [ "$rem2" = "$rem" ] \
  && case "$outc" in *"${foreign2:0:8}"*) true ;; *) false ;; esac \
  && case "$outl" in *"${foreign2:0:8}"*zOther*) true ;; *) false ;; esac \
  && ok "13 --carry and --land both refuse, both naming ${foreign2:0:8} as zOther, remote unchanged" \
  || bad "13 rcc=$rcc rcl=$rcl carry=$outc land=$outl"

# 14 — a carry of THIS build's own commit is not foreign and lands
build_main
mkdir -p "$tmp/work2/memory/builds/tFix"
echo note > "$tmp/work2/memory/builds/tFix/NOTE.md"
git -C "$tmp/work2" add memory/builds/tFix/NOTE.md
git -C "$tmp/work2" commit -q -m "records for this build"
ownc=$(git -C "$tmp/work2" rev-parse HEAD)
build_feat
git -C "$tmp/wt" merge -q --no-ff -m "merge local main" main
run_wt --prepare --slug tFix >/dev/null 2>&1
out14=$(run_wt --carry --slug tFix 2>&1); rc14=$?
out14b=$(run_wt --land --slug tFix 2>&1); rc14b=$?
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc14" = 0 ] && [ "$rc14b" = 0 ] && [ "$rem" = "$(git -C "$tmp/wt" rev-parse HEAD)" ] \
  && case "$out14" in *"${ownc:0:8}"*tFix*) true ;; *) false ;; esac \
  && ok "14 a carry attributed to this build by its folder lands" \
  || bad "14 rc-carry=$rc14 rc-land=$rc14b carry=$out14 land=$out14b"

# 15 — and one that names no unit id and touches no build folder is `unknown`, which is foreign
build_main
echo x > "$tmp/work2/src-loose.txt"
git -C "$tmp/work2" add src-loose.txt
git -C "$tmp/work2" commit -q -m "a commit naming nothing"
unkn=$(git -C "$tmp/work2" rev-parse HEAD)
build_feat
git -C "$tmp/wt" merge -q --no-ff -m "merge local main" main
run_wt --prepare --slug tFix >/dev/null 2>&1
out15=$(run_wt --carry --slug tFix 2>&1); rc15=$?
[ "$rc15" = 1 ] && case "$out15" in *"${unkn:0:8}"*unknown*) true ;; *) false ;; esac \
  && ok "15 an unattributable carry is named unknown and refuses" || bad "15 rc=$rc15 $out15"

# 16 — a single-parent records commit on top of T is accepted, and HEAD is what gets pushed
build_main; build_feat
run_wt --prepare --slug tFix >/dev/null 2>&1
git -C "$tmp/wt" commit -q --allow-empty -m "close records"
out16p=$(run_wt --prepared --slug tFix 2>&1); rc16p=$?
out16=$(run_wt --land --slug tFix 2>&1); rc16=$?
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc16p" = 0 ] && [ "$rc16" = 0 ] && [ "$rem" = "$(git -C "$tmp/wt" rev-parse HEAD)" ] \
  && ok "16 a records commit on the prepared merge lands, HEAD and not T being what was pushed" \
  || bad "16 rc-prepared=$rc16p rc-land=$rc16 prepared=$out16p land=$out16"

# 17 — a SECOND merge on top of it is not a prepared merge, and both readers say so
build_main
git -C "$tmp/wt" checkout -q -B side "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
echo s > "$tmp/wt/src-side.txt"; git -C "$tmp/wt" add src-side.txt; git -C "$tmp/wt" commit -q -m "a side line"
build_feat
run_wt --prepare --slug tFix >/dev/null 2>&1
git -C "$tmp/wt" merge -q --no-ff -m "a second merge" side
out17p=$(run_wt --prepared --slug tFix 2>&1); rc17p=$?
out17=$(run_wt --land --slug tFix 2>&1); rc17=$?
rem2=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc17p" = 1 ] && [ "$rc17" = 1 ] && [ "$rem2" = "$rem" ] \
  && ok "17 a second merge on the prepared one is refused by --prepared and by --land alike" \
  || bad "17 rc-prepared=$rc17p rc-land=$rc17 $out17"

# 18 — the attended reconcile shape (a plain merge of the remote INTO the branch) is refused, and
#      the refusal names the flag that makes the right shape
build_main; build_feat
git -C "$tmp/racer2" pull -q; git -C "$tmp/racer2" commit -q --allow-empty -m "remote moved"
git -C "$tmp/racer2" push -q origin main
git -C "$tmp/wt" fetch -q origin main
git -C "$tmp/wt" merge -q --no-ff -m "reconcile" FETCH_HEAD
out18p=$(run_wt --prepared --slug tFix 2>&1); rc18p=$?
out18=$(run_wt --land --slug tFix 2>&1); rc18=$?
[ "$rc18p" = 1 ] && [ "$rc18" = 1 ] && case "$out18" in *--prepare*) true ;; *) false ;; esac \
  && ok "18 a plain reconcile is refused and the refusal names --prepare" \
  || bad "18 rc-prepared=$rc18p rc-land=$rc18 $out18"

# 19 — a conflicting prepare leaves the branch exactly where it was, checked out, with a clean tree
build_main; build_feat
git -C "$tmp/racer2" pull -q; echo racer > "$tmp/racer2/src-seed.txt"; git -C "$tmp/racer2" add src-seed.txt
git -C "$tmp/racer2" commit -q -m "racer edits seed"; git -C "$tmp/racer2" push -q origin main
echo mine > "$tmp/wt/src-seed.txt"; git -C "$tmp/wt" add src-seed.txt
git -C "$tmp/wt" commit -q -m "TOOL-tFix-2: mine edits seed"
before19=$(git -C "$tmp/wt" rev-parse refs/heads/feat)
out19=$(run_wt --prepare --slug tFix 2>&1); rc19=$?
[ "$rc19" = 1 ] \
  && [ "$(git -C "$tmp/wt" rev-parse refs/heads/feat)" = "$before19" ] \
  && [ "$(git -C "$tmp/wt" symbolic-ref --short HEAD 2>/dev/null)" = feat ] \
  && [ -z "$(git -C "$tmp/wt" status --porcelain)" ] \
  && case "$out19" in *"git merge origin/main"*) true ;; *) false ;; esac \
  && ok "19 conflict: branch unmoved, HEAD on it, tree clean, the reconcile to run named" \
  || bad "19 rc=$rc19 head=$(git -C "$tmp/wt" symbolic-ref --short HEAD 2>/dev/null) $out19"

# 20 — the remote advancing DURING the gate re-prepares onto the new tip and lands, with the merge
#      that was already graded still an ancestor of what is finally pushed
build_main
git -C "$tmp/wt" checkout -q -B feat "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
echo u2 > "$tmp/wt/src-u2.txt"; git -C "$tmp/wt" add src-u2.txt
git -C "$tmp/wt" commit -q -m "TOOL-tFix-3: unit three"
run_wt --prepare --slug tFix >/dev/null 2>&1
t20=$(git -C "$tmp/wt" rev-parse HEAD)
touch "$tmp/race2-once"
out20=$(run_wt --land --slug tFix 2>&1); rc20=$?
rm -f "$tmp/race2-once"
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc20" = 0 ] && [ "$rem" = "$(git -C "$tmp/wt" rev-parse HEAD)" ] \
  && git -C "$tmp/wt" merge-base --is-ancestor "$t20" "$rem" \
  && ok "20 raced, re-prepared, landed; the first prepared merge is an ancestor of the pushed tip" \
  || bad "20 rc=$rc20 $out20"

# 21 — a MISTYPED flag refuses instead of falling through to the attended path, which from this tree
#      would push the local default branch. Run where that fallthrough would actually land.
rembefore=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
out21=$( cd "$tmp/work2" && git checkout -q main && bash tools/push-main.sh --lnad 2>&1 ); rc21=$?
remafter=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc21" = 2 ] && [ "$rembefore" = "$remafter" ] && ok "21 --lnad exits 2 and pushes nothing" \
  || bad "21 rc=$rc21 $out21"
# 21b — and the no-argument invocation is still the BASE attended landing
out21b=$( cd "$tmp/work2" && bash tools/push-main.sh 2>&1 ); rc21b=$?
[ "$rc21b" = 0 ] && case "$out21b" in *"landed main on origin"*) true ;; *) false ;; esac \
  && ok "21b the no-argument invocation still lands from the primary tree" || bad "21b rc=$rc21b $out21b"

# 22 — an OBSERVATION failure exits 3 and never 2, so a driver cannot read a network fault as a
#      misdeclared flag. Two causes, one code.
git -C "$tmp/wt" symbolic-ref -d refs/remotes/origin/HEAD 2>/dev/null || true
out22=$( cd "$tmp/wt" && unset GOV_DEFAULT_BRANCH && bash tools/push-main.sh --carry --slug tFix 2>&1 ); rc22=$?
[ "$rc22" = 3 ] && ok "22 an undeterminable default branch exits 3" || bad "22 rc=$rc22 $out22"
build_main
git -C "$tmp/wt" checkout -q -B feat "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
echo u4 > "$tmp/wt/src-u4.txt"; git -C "$tmp/wt" add src-u4.txt
git -C "$tmp/wt" commit -q -m "TOOL-tFix-4: unit four"
run_wt --prepare --slug tFix >/dev/null 2>&1
remb=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
git -C "$tmp/wt" remote set-url origin "$tmp/gone.git"
out22b=$(run_wt --carry --slug tFix 2>&1); rc22b=$?
out22c=$(run_wt --prepared --slug tFix 2>&1); rc22c=$?
git -C "$tmp/wt" remote set-url origin "$tmp/remote2.git"
rema=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc22b" = 3 ] && [ "$rc22c" = 3 ] && [ "$remb" = "$rema" ] \
  && ok "22b an unreachable remote exits 3 from both read-only flags, and pushes nothing" \
  || bad "22b rc-carry=$rc22b rc-prepared=$rc22c $out22b $out22c"

[ "$fail" = 0 ] && { echo "push-main.test: all cases ok"; exit 0; } || { echo "push-main.test: FAILURES"; exit 1; }
