#!/usr/bin/env bash
# The direct checks TOOL-aSparedSpawn-13's pass ran: the changed runner and the changed pre-push hook,
# each invoked directly in a hand-built fixture with its own local bare remote. No suite, no bar.
#   bash memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-13-direct-checks.sh [scratch dir]
# Prints one `ok` or `FAIL` line per observation and a count; exit 0 when every one held.
# WHAT THIS DOES NOT CHECK: a remote that moves between the two probes of one bar (a race the fixture
# cannot stage), a hook probe whose answer disagrees with the sha git hands it (git hands the hook the
# advertisement of the same connection), and AC11, which needs two whole bars on a frozen clone.
set -u
SRC=$(git rev-parse --show-toplevel) || exit 2
S=${1:-$(mktemp -d)}
mkdir -p "$S" || exit 2
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@t.test GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@t.test
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
P=0; F=0
ok()   { P=$((P + 1)); echo "ok   - $*"; }
nope() { F=$((F + 1)); echo "FAIL - $*"; }
OUT="$S/out"

# ---- the runner fixture ------------------------------------------------------------------------
R="$S/r"; O="$S/r-origin.git"
rm -rf "$R" "$O" "$S/wt"
mkdir -p "$R/tools/run-gates" "$R/tools/lib" "$R/g"
cp "$SRC/tools/run-gates/run-gates.sh" "$SRC/tools/run-gates/gate-fingerprint.sh" \
   "$SRC/tools/run-gates/gate-profiles.txt" "$R/tools/run-gates/" || exit 2
cp "$SRC/tools/lib/resolve-python.sh" "$R/tools/lib/" || exit 2
echo one > "$R/g/f"; echo x > "$R/other"
ND="$S/nd.flag"
cat > "$R/tools/gate-legs.json" <<EOF
[
  {"name": "pure", "argv": ["bash", "-c", "exit 0"], "guard": ["g/"]},
  {"name": "based", "argv": ["bash", "-c", "exit 0"], "guard": ["g/"], "reads": {"base": "fixture"}},
  {"name": "hist", "argv": ["bash", "-c", "exit 0"], "guard": ["g/"], "reads": {"history": "fixture"}},
  {"name": "clk", "argv": ["bash", "-c", "exit 0"], "guard": ["g/"], "reads": {"clock": "fixture"}},
  {"name": "rem", "argv": ["bash", "-c", "exit 0"], "guard": ["g/"], "reads": {"remote": "fixture"}},
  {"name": "legacy", "argv": ["bash", "-c", "exit 0"], "guard": ["g/"], "impure": "fixture"},
  {"name": "flip", "argv": ["bash", "-c", "[ -z \"\${FLIP:-}\" ]"], "guard": ["g/"]},
  {"name": "nd", "argv": ["bash", "-c", "if [ -e '$ND' ]; then rm -f '$ND'; exit 0; fi; : > '$ND'; exit 1"], "guard": ["g/"]},
  {"name": "red", "argv": ["bash", "-c", "[ -z \"\${RED:-}\" ]"], "guard": ["g/"]}
]
EOF
git init -q --template= -b main "$R"
git -C "$R" add -A && git -C "$R" commit -qm seed
git init -q --template= --bare "$O"
git -C "$R" remote add origin "$O"
git -C "$R" push -q -u origin main 2>/dev/null
git -C "$R" symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
E=$(git -C "$R" hash-object -w -t tree /dev/null)        # an empty tree: every guard reads changed against it
C2=$(git -C "$R" commit-tree "$E" -m alt)                 # a second base whose tree is empty too
GD="$R/.git"; CACHE="$GD/gate-cache"

run() { # VAR=value... -> rc; output in $OUT
  ( cd "$R" && env -u GATE_FULL -u GATE_REUSE -u GATE_REUSE_PUSH -u GATE_REUSE_SAMPLE -u GATE_REUSE_DAY \
      -u GATE_LEGS -u GATE_RUN_ID -u FLIP -u RED GATE_TURNSTILE=0 GATE_WALL=0 GATE_JOBS=2 GATE_BASE="$E" "$@" \
      bash tools/run-gates/run-gates.sh > "$OUT" 2>&1; echo $? )
}
verb() { # leg name -> its verb in the last output: ok, reuse, FAIL or absent
  awk -v n="$1" '$1 == "GATE" { v = $2; sub(/^GATE +[a-zA-Z]+ +/, ""); sub(/  .*/, ""); if ($0 == n) { print v; exit } }' "$OUT"
}
keyof() { # leg name -> its key in the last run record
  local c=""; IFS= read -r c < "$GD/gate-run/current"
  awk -F'\t' -v n="$1" '$1 == n { print $7 }' "$GD/gate-run/$c"/[0-9]*.leg 2>/dev/null | head -1
}
entries() { find "$CACHE" -mindepth 2 -type f 2>/dev/null | grep -c . ; }
expect() { # label · leg · want verb
  local got; got=$(verb "$2")
  [ "$got" = "$3" ] && ok "$1: $2 reads $3" || nope "$1: $2 reads '${got:-absent}', wanted $3"
}

: > "$ND"
rc=$(run)
[ "$rc" = 0 ] && ok "seed: the earning bar is green" || { nope "seed: rc=$rc"; sed 's/^/    /' "$OUT" | tail -20; }
n=$(entries)
[ "$n" = 8 ] && ok "S4: the clean green bar wrote 8 entries, every executed ok but the legacy impure leg's" \
  || nope "S4: $n entries after the earning bar, wanted 8"
k_pure=$(keyof pure)
[ -f "$CACHE/${k_pure:0:2}/$k_pure" ] && ok "S4: the entry sits at <key[0:2]>/<key>" || nope "S4: no entry at the fan-out path for pure"
IFS=$'\t' read -r e1 e2 e3 e4 e5 < "$CACHE/${k_pure:0:2}/$k_pure"
[ "$e1" = ok ] && [ "$e4" = "$(git -C "$R" rev-parse HEAD)" ] && [ "${e5:-0}" -gt 0 ] 2>/dev/null \
  && ok "S4: the entry reads ok, secs, run id, HEAD and an epoch" || nope "S4: the entry reads '$e1|$e2|$e3|$e4|$e5'"
[ -f "$GD/gate-full-green" ] && grep -q $'^reused\t0$' "$GD/gate-full-green" \
  && ok "S8: the full green carries reused 0" || nope "S8: no full green, or no reused 0 in it"

# Every reusable leg is reused, at sample 0; the legacy impure leg executes (AC10).
: > "$ND"
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
for l in pure based hist clk rem flip nd red; do expect "reuse" "$l" reuse; done
expect "AC10 a legacy impure leg is never reused" legacy ok
grep -q $'^reuse\tenv$' "$GD/gate-run/$(cat "$GD/gate-run/current")/header" && ok "header: reuse env" || nope "header: no reuse env"
[ -f "$GD/gate-full-green" ] && rm -f "$GD/gate-full-green"
# AC8, second half: a run that reused writes no full green.
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
[ ! -f "$GD/gate-full-green" ] && ok "AC8 a run that reused legs stamps no gate-full-green" || nope "AC8 a reusing run stamped a full green"
expect "AC8 control" pure reuse

# AC1: only the base moves.
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0 GATE_BASE="$C2")
expect "AC1 another GATE_BASE" based ok
expect "AC1 another GATE_BASE" pure reuse
expect "AC1 another GATE_BASE" hist reuse

# AC3: only the day moves.
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0 GATE_REUSE_DAY=1)
expect "AC3 another day" clk ok
expect "AC3 another day" pure reuse

# AC8 first half: GATE_FULL with GATE_REUSE reuses nothing.
: > "$ND"
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0 GATE_FULL=1)
[ -z "$(grep '^GATE reuse' "$OUT")" ] && ok "AC8 GATE_FULL with GATE_REUSE reuses nothing" || nope "AC8 GATE_FULL reused: $(grep -c '^GATE reuse' "$OUT")"
grep -q 'GATE_FULL is set, so nothing is reused' "$OUT" && ok "AC8 the run says why" || nope "AC8 no line names GATE_FULL"

# AC4: a fresh worktree of the same clone reuses the first tree's legs.
git -C "$R" worktree add -q "$S/wt" -b wtb 2>/dev/null
( cd "$S/wt" && env -u GATE_FULL -u GATE_REUSE_PUSH -u GATE_REUSE_DAY -u FLIP -u RED GATE_TURNSTILE=0 GATE_WALL=0 GATE_JOBS=2 \
    GATE_BASE="$E" GATE_REUSE=1 GATE_REUSE_SAMPLE=0 bash tools/run-gates/run-gates.sh > "$OUT" 2>&1 )
expect "AC4 a fresh worktree" pure reuse
expect "AC4 a fresh worktree" clk reuse
git -C "$R" worktree remove --force "$S/wt" 2>/dev/null

# AC2: a commit touching no guarded path.
echo y > "$R/other"; git -C "$R" commit -qam other
: > "$ND"
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
expect "AC2 a commit off the guard" hist ok
expect "AC2 a commit off the guard" pure reuse
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
expect "AC2 the same HEAD again" hist reuse

# AC5: a red leg, a dirty tree, a reused leg write nothing.
rm -rf "$CACHE"; : > "$ND"
rc=$(run RED=1)
k_red=$(keyof red); k_pure=$(keyof pure)
[ -n "$k_red" ] && [ ! -e "$CACHE/${k_red:0:2}/$k_red" ] && [ -f "$CACHE/${k_pure:0:2}/$k_pure" ] \
  && ok "AC5 a red leg writes no entry, and its green sibling did" || nope "AC5 red key '$k_red': entry present, or the control is missing"
before=$(entries); echo dirt > "$R/g/untracked"; : > "$ND"
rc=$(run GATE_BASE="$C2")
[ "$(entries)" = "$before" ] && ok "AC5 a run on a dirty tree writes no entry ($before before and after)" || nope "AC5 the dirty run wrote entries: $before -> $(entries)"
rm -f "$R/g/untracked"
rc=$(run); : > "$ND"
m1=$(cat "$CACHE/${k_pure:0:2}/$k_pure")
sleep 1; rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
expect "AC5 control" pure reuse
[ "$(cat "$CACHE/${k_pure:0:2}/$k_pure")" = "$m1" ] && ok "AC5 a reused leg rewrote nothing" || nope "AC5 the reused leg's entry changed"

# AC6: the sample at 1 draws every leg; flip now reds against its cached ok, nd reds then greens.
rm -f "$ND"
rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=1 FLIP=1)
[ "$rc" != 0 ] && ok "AC6 the disagreeing run reds (rc=$rc)" || nope "AC6 the run is green"
k_flip=$(keyof flip)
grep -qx "cache disagreement · flip · $k_flip" "$OUT" && ok "AC6 it prints cache disagreement · flip · <key>" || nope "AC6 no disagreement line: $(grep -i 'disagree' "$OUT")"
grep -qx "nondeterministic · nd" "$OUT" && ok "AC6 red then green prints nondeterministic · nd" || nope "AC6 no nondeterministic line"
[ ! -e "$CACHE/${k_flip:0:2}/$k_flip" ] && ok "AC6 the disagreeing entry is gone" || nope "AC6 the entry survived"
ls "$CACHE"/quarantine.* >/dev/null 2>&1 && [ "$(ls "$CACHE"/quarantine.* | grep -c .)" = 2 ] \
  && ok "AC6 both legs are quarantined" || nope "AC6 quarantine files: $(ls "$CACHE" | tr '\n' ' ')"
: > "$ND"; rc=$(run)                                       # re-earns flip's entry under the same key
[ -f "$CACHE/${k_flip:0:2}/$k_flip" ] && ok "AC6 precondition: flip's entry is earned again" || nope "AC6 flip's entry was not re-earned"
: > "$ND"; rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
expect "AC6 a quarantined leg executes although its key matches" flip ok
expect "AC6 control" pure reuse

# AC7: a leg reused on 10 runs in a row executes on the next.
age=$(ls "$CACHE"/age.* 2>/dev/null | head -1)
[ -n "$age" ] && ok "S7: reusing writes an age counter" || nope "S7: no age file"
for f in "$CACHE"/age.*; do printf '10' > "$f"; done
: > "$ND"; rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
expect "AC7 the eleventh reuse" pure ok
grep -q 'pure was reused on 10 runs in a row, so it executes' "$OUT" && ok "AC7 the run says why" || nope "AC7 no age line"
nz=""; for f in "$CACHE"/age.*; do [ "$(cat "$f")" = 0 ] || nz+=" ${f##*/}"; done
[ -z "$nz" ] && ok "AC7 execution resets every counter to 0" || nope "AC7 counters not 0:$nz"

# AC9: the prune at run end.
mkdir -p "$CACHE/zz"; printf 'ok\t1\tx\ty\t1\n' > "$CACHE/zz/zzold"; printf 'ok\t1\tx\ty\t1\n' > "$CACHE/zz/zzyoung"
touch -d '31 days ago' "$CACHE/zz/zzold"; touch -d '29 days ago' "$CACHE/zz/zzyoung"
: > "$ND"; rc=$(run GATE_REUSE=1 GATE_REUSE_SAMPLE=0)
[ ! -e "$CACHE/zz/zzold" ] && [ -e "$CACHE/zz/zzyoung" ] && ok "AC9 a 31-day entry is erased and a 29-day one remains" \
  || nope "AC9 old: $([ -e "$CACHE/zz/zzold" ] && echo kept || echo gone), young: $([ -e "$CACHE/zz/zzyoung" ] && echo kept || echo gone)"

# AC10, the key half: a legacy impure leg's key moves with the remote, a pure leg's does not.
: > "$ND"; rc=$(run); kl1=$(keyof legacy); kp1=$(keyof pure); kr1=$(keyof rem)
git -C "$R" push -q origin HEAD:refs/heads/elsewhere 2>/dev/null
: > "$ND"; rc=$(run); kl2=$(keyof legacy); kp2=$(keyof pure); kr2=$(keyof rem)
[ "$kl1" != "$kl2" ] && [ "$kr1" != "$kr2" ] && ok "AC10 a new remote head moves the legacy leg's key, as it moves the remote leg's" \
  || nope "AC10 legacy $kl1 -> $kl2, remote $kr1 -> $kr2"
[ "$kp1" = "$kp2" ] && ok "AC10 control: the pure leg's key does not move" || nope "AC10 the pure key moved"

# AC12/AC13, the runner half: GATE_REUSE_PUSH.
HEADSHA=$(git -C "$R" rev-parse HEAD)
git -C "$R" ls-remote --heads origin > "$S/adv"
TIP=$(awk -F'\t' '$2 == "refs/heads/main" { print $1 }' "$S/adv")
DIG=$(git -C "$R" hash-object --stdin < "$S/adv")
rm -f "$GD/gate-full-green"
: > "$ND"; rc=$(run GATE_REUSE_PUSH="$HEADSHA $TIP $DIG" GATE_REUSE_SAMPLE=0)
expect "AC12 push, same sha and tip" rem reuse
expect "AC12 push, same sha and tip" hist reuse
expect "AC12 push: a leg declaring neither class" pure ok
expect "AC12 push: a base leg" based ok
c=$(cat "$GD/gate-run/current")
[ "$(awk -F'\t' '$1 == "reused" { print $2 }' "$GD/gate-run/$c/verdict")" -gt 0 ] 2>/dev/null && grep -q $'^reuse\tpush$' "$GD/gate-run/$c/header" \
  && grep -q $'^full\t$' "$GD/gate-run/$c/header" && ok "AC13 the run record: reused > 0, reuse push, full empty" || nope "AC13 the run record does not say so"
[ ! -f "$GD/gate-full-green" ] && ok "AC14 the reusing push run wrote no gate-full-green" || nope "AC14 a full green was written"
: > "$ND"; rc=$(run GATE_REUSE_PUSH="$HEADSHA 0000000000000000000000000000000000000000 $DIG" GATE_REUSE_SAMPLE=0)
expect "AC12 a moved tip" rem ok
: > "$ND"; rc=$(run GATE_REUSE_PUSH="$HEADSHA $TIP 0000000000000000000000000000000000000000" GATE_REUSE_SAMPLE=0)
expect "AC12 another advertisement" rem ok
: > "$ND"; rc=$(run GATE_REUSE_PUSH="$C2 $TIP $DIG" GATE_REUSE_SAMPLE=0)
expect "AC12 another pushed sha" rem ok
expect "AC12 another pushed sha" hist ok
echo two > "$R/g/f"; git -C "$R" commit -qam guarded
HEADSHA=$(git -C "$R" rev-parse HEAD)
: > "$ND"; rc=$(run GATE_REUSE_PUSH="$HEADSHA $TIP $DIG" GATE_REUSE_SAMPLE=0)
expect "AC12 a guarded input changed" rem ok

# ---- the hook fixture --------------------------------------------------------------------------
H="$S/h"; HO="$S/h-origin.git"; rm -rf "$H" "$HO" "$S/hooks" "$S/shim"
mkdir -p "$S/hooks" "$S/shim"; cp "$SRC/.githooks/pre-push" "$S/hooks/pre-push"
git init -q --template= --bare "$HO"; git init -q --template= -b main "$H"
git -C "$H" config core.hooksPath "$S/hooks"
git -C "$H" commit -q --allow-empty -m init; git -C "$H" remote add origin "$HO"
git -C "$H" push -q --no-verify origin main 2>/dev/null; git -C "$H" remote set-head origin main >/dev/null 2>&1
: > "$H/.git/push-main-active"
printf '#!/usr/bin/env bash\nprintf "knob=%%s\\n" "${GATE_REUSE_PUSH:-}"\nexit 0\n' > "$S/stub.sh"
hpush() { # VAR=value... -> rc; output in $OUT
  git -C "$H" commit -q --allow-empty -m "c$RANDOM"
  ( cd "$H" && env GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $S/stub.sh" GOV_DEFAULT_BRANCH=main "$@" \
      git push origin main > "$OUT" 2>&1; echo $? )
}
plant_green() { printf 'sha\t%s\n%s' "$(git -C "$H" rev-parse HEAD)" "${1:-}" > "$H/.git/gate-full-green"; }

plant_green; rc=$(hpush)
want_knob="knob=$(git -C "$H" rev-parse HEAD) $(git -C "$H" rev-parse origin/main 2>/dev/null)"
grep -q 'scoped gate on main push' "$OUT" && grep -q 'reuse offered to remote and history legs' "$OUT" \
  && ok "AC13 the scoped decision line offers reuse" || nope "AC13 the decision line: $(grep 'gate on main' "$OUT")"
k=$(grep '^knob=' "$OUT" | head -1)
case "$k" in "knob=$(git -C "$H" rev-parse HEAD) "*" "*) ok "S10 the bar receives GATE_REUSE_PUSH as pushed sha, tip and digest" ;;
  *) nope "S10 the bar received '$k'" ;; esac
tip_in=$(printf '%s' "$k" | awk '{ print $2 }')
[ "$tip_in" = "$(git --git-dir="$HO" rev-parse main~1 2>/dev/null)" ] && ok "S9 the tip in the knob is what the remote advertised before the push" \
  || nope "S9 the knob's tip $tip_in is not the remote's pre-push main"

# A probe with no default-branch tip to answer with. A PATH shim for `timeout` cannot stage a failed
# probe: git runs the hook with its own directories ahead of the caller's PATH. A first push to an
# empty remote takes the same branch a failed probe takes, `_rp_tip` empty, so it is staged that way.
H2="$S/h2-origin.git"; rm -rf "$H2"; git init -q --template= --bare "$H2"
git -C "$H" remote add second "$H2"
plant_green; git -C "$H" commit -q --allow-empty -m first
( cd "$H" && env GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $S/stub.sh" GOV_DEFAULT_BRANCH=main \
    git push second main > "$OUT" 2>&1 )
grep -q 'reuse not offered: the ls-remote probe did not answer with the main tip' "$OUT" && grep -qx 'knob=' "$OUT" \
  && ok "AC12 a probe with no tip to answer offers nothing and the decision line names the probe" \
  || nope "AC12 no-tip probe: $(grep 'gate on main' "$OUT"); $(grep knob= "$OUT")"

plant_green; rc=$(hpush GATE_REUSE_PUSH=planted)
grep -q 'not honoured from the environment by this bar:.*GATE_REUSE_PUSH' "$OUT" && ok "AC15 an inherited GATE_REUSE_PUSH is named as not honoured" \
  || nope "AC15 the hook did not name the inherited knob"
grep -q '^knob=planted' "$OUT" && nope "AC15 the planted knob reached the bar" || ok "AC15 the planted knob never reaches the bar"

rm -f "$H/.git/gate-full-green"; rc=$(hpush GATE_REUSE_PUSH=planted)
grep -q 'FULL gate on main push' "$OUT" && grep -qx 'knob=' "$OUT" && ok "AC15 a FULL decision exports no knob, inherited or not" \
  || nope "AC15 FULL: $(grep 'gate on main' "$OUT"); $(grep knob= "$OUT")"

plant_green $'reused\t1\n'; rc=$(hpush)
grep -q 'FULL gate on main push.*says its run reused 1 leg(s)' "$OUT" && ok "AC14 a planted green whose reused reads 1 forces the full bar" \
  || nope "AC14 the planted record: $(grep 'gate on main' "$OUT")"
plant_green $'reused\t0\n'; rc=$(hpush)
grep -q 'scoped gate on main push' "$OUT" && ok "AC14 control: the same record with reused 0 scopes" || nope "AC14 control: $(grep 'gate on main' "$OUT")"

echo "direct checks: $P ok, $F failed"
[ "$F" = 0 ]
