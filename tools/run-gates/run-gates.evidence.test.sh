#!/usr/bin/env bash
# run-gates.evidence.test.sh — fixture harness for DURABLE LEG EVIDENCE (TOOL-dNomadicAtlas-1).
# Exit 0 = all cases pass.
#
# What this gates that nothing else can: when a leg goes red, its own output must survive on disk, so
# a caller who pipes/backgrounds/scrolls away the runner can still name the failing test without
# re-running the whole bar. leg() already held every leg's merged output in $out and printed it, then
# kept only the ROW for the durable summary — the reason was in scope at the exact line the durable
# record was built, and dropped there.
#
# This is a FIXTURE harness, not a canary: run-gates.test.sh is static (it parses the manifest and
# greps the runner) and never executes run-gates.sh. Executing the real runner in place would re-run
# the whole bar recursively and clobber the live gate-last-summary.txt mid-run, so every case here
# drives it through GATE_LEGS with its own scratch GIT_DIR.
set -u

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "evidence-test: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
RUNNER="$ROOT/tools/run-gates/run-gates.sh"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
bad=0
# the run-gates promotion spec's S11. The count is INCREMENTED where the assertions actually happen -- in the
# two helpers every arm routes through -- so it can never drift from the arms the way a hardcoded
# literal does. That drift is the recorded failure this leg exists for: a suite printed a fixed
# `PASS (130 assertions)` for its whole life with no counter behind it.
FLOOR_ASSERTIONS=51
n=0
ok()   { n=$((n+1)); echo "  ok   — $1"; }
nope() { n=$((n+1)); echo "  FAIL — $1"; bad=1; }

# mk_legs <file> <json-array-body>
mk_legs() { printf '[%s]\n' "$2" > "$1"; }

# fresh_gitdir <n> — a scratch GIT_DIR per case, so cases cannot read each other's logs and the real
# gate-last-summary.txt is never touched
fresh_gitdir() {
  local d="$tmp/gd$1"; rm -rf "$d"; git init -q --bare "$d" 2>/dev/null || mkdir -p "$d"
  printf '%s' "$d"
}
# GIT_WORK_TREE is required, not decoration: the runner resolves ROOT with `--show-toplevel`,
# which refuses a bare GIT_DIR outright. Without it every case dies at line 7 with exit 2.
run() { GIT_DIR="$1" GIT_WORK_TREE="$ROOT" GATE_LEGS="$2" bash "$RUNNER" 2>&1; }

# ---------------------------------------------------------------------------------------------
# 1. a failing leg's own output survives on disk, and the caller's stdout is irrelevant to that
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 1)"
mk_legs "$tmp/l1.json" '{"name":"red-leg","argv":["bash","-c","echo NEEDLE_UP_4c1; exit 1"]}'
run "$gd" "$tmp/l1.json" > /dev/null 2>&1
log="$gd/gate-logs/red-leg.log"
if [ -f "$log" ] && grep -q NEEDLE_UP_4c1 "$log"; then
  ok "a red leg's output survives on disk"
else
  nope "a red leg's output is NOT on disk (looked in $log)"
fi

# the durable summary must POINT at it — a pointer, never the bytes: this file is what an operator
# is told to read after a refused push
sum="$gd/gate-last-summary.txt"
if [ -f "$sum" ] && grep -q 'red-leg.log' "$sum"; then
  ok "the durable summary points at the failing leg's log"
else
  nope "the durable summary does not name the failing leg's log"
fi
if [ -f "$sum" ] && grep -q NEEDLE_UP_4c1 "$sum"; then
  nope "raw leg bytes leaked into gate-last-summary.txt (must be a POINTER only)"
else
  ok "gate-last-summary.txt carries a pointer, not raw leg output"
fi

# ---------------------------------------------------------------------------------------------
# 2. a PASSING leg is captured too — a later bisect reads the green run's output, and the bytes are
#    already in memory
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 2)"
mk_legs "$tmp/l2.json" '{"name":"green-leg","argv":["bash","-c","echo NEEDLE_GREEN_88; exit 0"]}'
run "$gd" "$tmp/l2.json" > /dev/null 2>&1
if grep -q NEEDLE_GREEN_88 "$gd/gate-logs/green-leg.log" 2>/dev/null; then
  ok "a passing leg's output is captured as well"
else
  nope "a passing leg's output was not captured"
fi

# ---------------------------------------------------------------------------------------------
# 3. gate-last-failure.txt is written on RED and SURVIVES a later green run. gate-last-summary.txt is
#    overwritten by every run, so the reflexive re-run would otherwise erase the failing evidence.
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 3)"
mk_legs "$tmp/l3red.json"   '{"name":"r","argv":["bash","-c","echo NEEDLE_KEEP_d2; exit 1"]}'
mk_legs "$tmp/l3green.json" '{"name":"r","argv":["bash","-c","echo fine; exit 0"]}'
run "$gd" "$tmp/l3red.json"   > /dev/null 2>&1
run "$gd" "$tmp/l3green.json" > /dev/null 2>&1
if [ -f "$gd/gate-last-failure.txt" ] && grep -q 'gates RED' "$gd/gate-last-failure.txt"; then
  ok "gate-last-failure.txt survives a subsequent GREEN run"
else
  nope "gate-last-failure.txt was erased by the green re-run"
fi
if grep -q 'gates GREEN' "$gd/gate-last-summary.txt" 2>/dev/null; then
  ok "gate-last-summary.txt still reflects the LATEST run"
else
  nope "gate-last-summary.txt did not follow the latest run"
fi

# ---------------------------------------------------------------------------------------------
# 4. THE CAPTURE PATH MUST NEVER DECIDE WHETHER A LEG RUNS.
#
# Two distinct states, and only one of them is reachable through GIT_DIR. An absent GIT_DIR is
# refused at line 7 by `git rev-parse --show-toplevel` — before any capture code — so the evidence
# layer can never compose a path from an empty root that way. The capture-off branch is reached by a
# gate-logs that cannot be CREATED, which a plain file in its place produces exactly.
# ---------------------------------------------------------------------------------------------
mk_legs "$tmp/l4.json" '{"name":"fine","argv":["bash","-c","echo hi; exit 0"]}'
out="$(GIT_DIR="$tmp/nope.git" GIT_WORK_TREE="$ROOT" GATE_LEGS="$tmp/l4.json" bash "$RUNNER" 2>&1)"; rc=$?
if [ "$rc" -eq 2 ] && printf '%s' "$out" | grep -q 'not a git repo'; then
  ok "an absent git dir is refused at the repo guard, before any capture"
else
  nope "an absent git dir was not refused cleanly (rc=$rc)"
fi

gd="$(fresh_gitdir 4)"; : > "$gd/gate-logs"   # a FILE where the directory must go
out="$(run "$gd" "$tmp/l4.json")"; rc=$?
if [ "$rc" -eq 0 ] && printf '%s' "$out" | grep -q 'gates GREEN'; then
  ok "an uncreatable log dir does not change the verdict"
else
  nope "an uncreatable log dir changed the verdict (rc=$rc)"
fi
if printf '%s' "$out" | grep -qi 'evidence capture OFF'; then
  ok "capture-off is STATED, not silent"
else
  nope "capture was disabled silently — green-by-absence"
fi

# ---------------------------------------------------------------------------------------------
# 5. REDACTION — a leg can echo an operator-exported credential, and a file outlives a terminal
# ---------------------------------------------------------------------------------------------
gd="$(fresh_gitdir 5)"
mk_legs "$tmp/l5.json" '{"name":"secret","argv":["bash","-c","echo using postgresql://carol:topsecret@db.example/x; exit 1"]}'
run "$gd" "$tmp/l5.json" > /dev/null 2>&1
sl="$gd/gate-logs/secret.log"
if [ -f "$sl" ] && ! grep -q 'topsecret' "$sl" && grep -q 'db.example' "$sl"; then
  ok "URL userinfo is redacted, the rest of the line is kept"
else
  nope "a credential survived into a durable log"
fi

# ---------------------------------------------------------------------------------------------
# 6. the GATE_LEGS seam itself: without it this harness cannot exist, so it is part of the contract
# ---------------------------------------------------------------------------------------------
out="$(GIT_DIR="$(fresh_gitdir 6)" GIT_WORK_TREE="$ROOT" GATE_LEGS="$tmp/definitely-absent.json" bash "$RUNNER" 2>&1)"; rc=$?
if [ "$rc" -eq 2 ] && printf '%s' "$out" | grep -q 'definitely-absent.json'; then
  ok "an unreadable GATE_LEGS exits 2 and names the file it could not parse"
else
  nope "an unreadable GATE_LEGS did not fail cleanly (rc=$rc)"
fi

# =================================================================================================
# THE RUN RECORD (the run-record unit). Every arm below drives the real runner inside its OWN scratch
# repository, because the record lives in the git dir and these arms have to make trees dirty, kill
# runs, and plant files. The bare-GIT_DIR fixtures above cannot do that: they borrow this repo's
# working tree, so "make the tree dirty" would mean dirtying the tree under test.
#
# WHY SO MANY NEGATIVE ARMS. The full-green stamp has five preconditions, and an implementation that
# forgets exactly one of them passes every arm written for the other four. Each therefore gets its
# own control, and the two that historically had none — the red run and the untracked-only dirty
# tree — get theirs first.

REC_OUT=$(mktemp)   # runner stdout goes OUTSIDE the repo under test: writing it inside makes the
                    # tree untracked-dirty before the runner starts, which silently turns every
                    # full-green arm into a no-op. Measured while building this suite.

rec_repo() {  # -> sets REC_T (worktree) and REC_GD (git dir)
  REC_T=$(mktemp -d)
  mkdir -p "$REC_T/tools/run-gates" "$REC_T/tools/lib" "$REC_T/fx"
  cp "$ROOT/tools/run-gates/run-gates.sh" "$ROOT/tools/run-gates/gate-fingerprint.sh" \
     "$ROOT/tools/run-gates/gate-profiles.txt" "$REC_T/tools/run-gates/" || return 1
  cp "$ROOT/tools/lib/resolve-python.sh" "$REC_T/tools/lib/" 2>/dev/null || true
  ( cd "$REC_T" && git init -q -b main . && git config user.email rec@test.invalid \
      && git config user.name rec-test ) >/dev/null 2>&1 || return 1
  printf '#!/usr/bin/env bash\necho hello\nexit 0\n' > "$REC_T/fx/a.sh"
  printf '#!/usr/bin/env bash\necho boom\nexit 3\n'  > "$REC_T/fx/red.sh"
  printf '#!/usr/bin/env bash\nsleep 6\nexit 0\n'    > "$REC_T/fx/slow.sh"
  printf '#!/usr/bin/env bash\necho "https://u:p@example.com"\nexit 0\n' > "$REC_T/fx/leak.sh"
  printf '%s\n' '[' \
    '  {"name": "one", "argv": ["bash", "fx/a.sh"]},' \
    '  {"name": "guarded", "argv": ["bash", "fx/a.sh"], "guard": ["fx/"]}' \
    ']' > "$REC_T/tools/gate-legs.json"
  ( cd "$REC_T" && git add -A && git commit -qm seed ) >/dev/null 2>&1 || return 1
  # A resolvable origin, so guards can compute a BASE and a skip is actually reachable. Without it
  # BASE is empty, changed() fails safe to "run", and every skip arm passes by finding nothing.
  ( cd "$REC_T" && git update-ref refs/remotes/origin/main HEAD \
      && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
  REC_GD="$REC_T/.git"
}
rec_run()  { ( cd "$REC_T" && env "$@" bash tools/run-gates/run-gates.sh >"$REC_OUT" 2>&1; echo $? ); }
rec_legs() { printf '%s\n' "$1" > "$REC_T/tools/gate-legs.json"
             ( cd "$REC_T" && git add -A && git commit -qm legs ) >/dev/null 2>&1; }
rec_dir()  { printf '%s/gate-run/%s' "$REC_GD" "$(cat "$REC_GD/gate-run/current" 2>/dev/null)"; }
rec_done() { rm -rf "$REC_T"; }

# --- the header is readable BY A LEG while the run is in flight ----------------------------------
rec_repo || { echo "evidence-test: cannot build a record scratch"; exit 2; }
printf '%s\n' '#!/usr/bin/env bash' \
  'gd=$(git rev-parse --git-dir)' \
  'id=$(cat "$gd/gate-run/current" 2>/dev/null)' \
  '[ -n "$id" ] || { echo "no current"; exit 1; }' \
  'grep -q "^run_id	$id$" "$gd/gate-run/$id/header" || { echo "header does not name this run"; exit 1; }' \
  'echo "read the header of run $id"' > "$REC_T/fx/reader.sh"
rec_legs '[ {"name": "reader", "argv": ["bash", "fx/reader.sh"]} ]'
rc=$(rec_run GATE_FULL=1)
if [ "$rc" = 0 ] && grep -q 'GATE ok    reader' "$REC_OUT"; then
  ok "a leg resolved gate-run/current and read this run's header WHILE the run was in flight"
else
  nope "a leg could not read the in-flight header (rc=$rc)"; sed 's/^/      /' "$REC_OUT"
fi
rec_done

# --- a hard kill leaves a header and NO verdict ---------------------------------------------------
# THE KILL LANDS AT 5s AGAINST A 6s LEG, and the margin is deliberate on both sides. It was 2s,
# which measured 2136 ms to write the header on this platform — so the arm was grading the
# runner's STARTUP BUDGET, and reported the crash case as unreadable whenever startup lost a
# race it was never meant to be in. Too wide and the leg finishes first and there is no crash to
# observe; the leg sleeps 6s, so 5s is mid-run with room on both sides.
rec_repo
rec_legs '[ {"name": "slow", "argv": ["bash", "fx/slow.sh"]} ]'
( cd "$REC_T" && timeout -s KILL 5 env GATE_FULL=1 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1
d=$(rec_dir)
[ -f "$d/header" ] && ok "the header survived a hard kill" \
                   || nope "no header after a hard kill — the crash case is unreadable"
[ -f "$d/verdict" ] && nope "a verdict exists after a hard kill, so its absence is not the crash signal" \
                    || ok "no verdict after a hard kill (absence IS the crash signal)"
rec_done

# --- the failed leg's ledger row, and the control that stops it passing by finding nothing --------
rec_repo
rec_legs '[ {"name": "red", "argv": ["bash", "fx/red.sh"]}, {"name": "one", "argv": ["bash", "fx/a.sh"]} ]'
rec_run GATE_FULL=1 >/dev/null
if awk -F'\t' '$1=="red" && $3=="fail" && $4=="-" {f=1} END{exit !f}' "$REC_GD/gate-ledger.tsv" 2>/dev/null; then
  ok "a failed leg's ledger row is status fail with no reusable input key"
else
  nope "the failed leg's ledger row is wrong"; sed 's/^/      /' "$REC_GD/gate-ledger.tsv" 2>/dev/null
fi
if awk -F'\t' '$1=="one" && $3=="ok" && $4!="-" && length($4)>=7 {f=1} END{exit !f}' "$REC_GD/gate-ledger.tsv" 2>/dev/null; then
  ok "control: a PASSING leg does carry an input key, so the dash above is a verdict and not a default"
else
  nope "no leg carries an input key at all — the dash assertion above proves nothing"
fi
rec_done

# --- a corrupt ledger is survived ------------------------------------------------------------------
rec_repo
printf 'not\ta\tnumber\n\x00garbage\n' > "$REC_GD/gate-ledger.tsv"
rc=$(rec_run GATE_FULL=1)
[ "$rc" = 0 ] && ok "a corrupt ledger did not change the verdict" \
              || nope "a corrupt ledger failed the run (rc=$rc)"
rec_done

# --- the full-green stamp, and its five preconditions, each with a control -------------------------
rec_repo
rc=$(rec_run GATE_FULL=1)
if [ -f "$REC_GD/gate-full-green" ]; then
  ok "control: a clean, fully-green, nothing-skipped run DOES stamp gate-full-green"
  blob=$( cd "$REC_T" && git hash-object -- tools/gate-legs.json )
  grep -q "^manifest_blob	$blob$" "$REC_GD/gate-full-green" \
    && ok "the stamp's manifest_blob is the hash of the manifest THAT RUN READ" \
    || { nope "the stamp's manifest_blob does not match the manifest the run read"; sed 's/^/      /' "$REC_GD/gate-full-green"; }
  stamp_before=$(cat "$REC_GD/gate-full-green")
  # a RED run must neither write nor UPDATE it — the arm that distinguishes the two
  printf '#!/usr/bin/env bash\necho boom\nexit 3\n' > "$REC_T/fx/a.sh"
  ( cd "$REC_T" && git add -A && git commit -qm red ) >/dev/null 2>&1
  rc=$(rec_run GATE_FULL=1)
  [ "$rc" = 1 ] || nope "control: the red fixture did not red (rc=$rc)"
  [ "$(cat "$REC_GD/gate-full-green")" = "$stamp_before" ] \
    && ok "a RED run neither wrote nor updated an existing full-green stamp" \
    || nope "a RED run rewrote the full-green stamp"
else
  nope "the control failed: a clean fully-green run did not stamp, so every arm below proves nothing"
fi
rec_done

rec_repo
rc=$(rec_run GATE_FULL=)     # guards live: the guarded leg is unchanged vs origin/main
if grep -q 'GATE skip' "$REC_OUT"; then
  ok "control: a leg actually skipped, so the skip precondition has something to grade"
  [ -f "$REC_GD/gate-full-green" ] && nope "full-green stamped despite a skipped leg" \
                                   || ok "a skipped leg defeats the full-green stamp"
else
  nope "nothing skipped, so the skip precondition arm would pass by finding nothing"
fi
rec_done

rec_repo
echo scribble >> "$REC_T/fx/a.sh"
rec_run GATE_FULL=1 >/dev/null
[ -f "$REC_GD/gate-full-green" ] && nope "full-green stamped from a tracked-dirty tree" \
                                 || ok "a tracked modification at start defeats the full-green stamp"
rec_done

rec_repo
touch "$REC_T/scratch.tmp"
rec_run GATE_FULL=1 >/dev/null
# THE FIXTURE THAT SEPARATES THE TWO READINGS OF "CLEAN". `git diff --quiet` is blind to an untracked
# file, so an implementation using it passes every other dirty-tree arm and stamps a green here.
[ -f "$REC_GD/gate-full-green" ] \
  && nope "full-green stamped from a tree whose only dirt is UNTRACKED — CLEAN is being read as git diff --quiet" \
  || ok "untracked-only dirt defeats the stamp (CLEAN means porcelain EMPTY, not diff --quiet)"
rec_done

rec_repo
rec_legs '[ {"name": "slow", "argv": ["bash", "fx/slow.sh"]} ]'
# THE EDIT WAITS FOR A FACT, NOT A CLOCK. `sleep 2` raced the runner's startup: the fingerprint is
# taken before the first leg dispatches, so under an 8-wide bar the edit could land BEFORE it and
# there was nothing to detect. Measured — this arm passed alone and failed inside a full bar run.
# The run record's own header is the observable that says "the fingerprint has been taken".
( for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    c="$REC_GD/gate-run/current"
    [ -f "$c" ] && [ -f "$REC_GD/gate-run/$(cat "$c")/header" ] && break
    sleep 1
  done
  echo moved >> "$REC_T/fx/a.sh" ) &
rec_run GATE_FULL=1 >/dev/null
wait
grep -q '^tree_moved	yes' "$(rec_dir)/verdict" 2>/dev/null \
  && ok "a tree that moved mid-run is recorded as moved in the verdict" \
  || { nope "mid-run tree movement was not recorded"; cat "$(rec_dir)/verdict" 2>/dev/null | sed 's/^/      /'; }
[ -f "$REC_GD/gate-full-green" ] && nope "full-green stamped although the tree moved mid-run" \
                                 || ok "a tree that moved mid-run defeats the stamp"
rec_done

# --- a planted completion file cannot suppress a leg ----------------------------------------------
# The run id is pinned through its seam so the plant lands in the directory this run actually opens.
# Without the pin the plant goes somewhere the run never looks and the arm passes by finding nothing,
# which is the exact shape it exists to rule out.
rec_repo
mkdir -p "$REC_GD/gate-run/PINNED"
printf '0' > "$REC_GD/gate-run/PINNED/1.rc"
printf '0' > "$REC_GD/gate-run/1.rc"
rec_run GATE_FULL=1 GATE_RUN_ID=PINNED >/dev/null
[ -f "$REC_GD/gate-run/PINNED/1.leg" ] \
  && ok "a completion file planted in this run's own directory did NOT suppress its leg" \
  || nope "a planted completion file suppressed a leg — a leftover reads as a green verdict"
rec_done

# --- retention, and the control that proves the sweep runs after the verdict ----------------------
rec_repo
for i in 1 2 3 4 5 6 7 8; do mkdir -p "$REC_GD/gate-run/old$i"; sleep 0.05; done
rec_run GATE_FULL=1 >/dev/null
left=$(ls -1 "$REC_GD/gate-run" 2>/dev/null | grep -cv '^current$')
keep=$(grep -m1 -oE 'GATE_RUN_KEEP:-[0-9]+' "$ROOT/tools/run-gates/run-gates.sh" | grep -oE '[0-9]+')
# GRADED AGAINST THE CONSTANT BY NAME, read out of the runner. A bound written only into this arm is
# satisfied by whatever a builder picked, including one above the fixture's size, which passes by
# finding nothing.
[ -n "$keep" ] || nope "could not read GATE_RUN_KEEP out of the runner, so this arm has no bound to grade"
[ "$left" = "${keep:-x}" ] && ok "the sweep left exactly GATE_RUN_KEEP=$keep run directories" \
                           || nope "the sweep left $left run directories, expected ${keep:-?}"
rec_done

rec_repo
for i in 1 2 3 4 5 6 7 8; do mkdir -p "$REC_GD/gate-run/old$i"; done
rec_legs '[ {"name": "slow", "argv": ["bash", "fx/slow.sh"]} ]'
( cd "$REC_T" && timeout -s KILL 5 env GATE_FULL=1 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1
left=$(ls -1 "$REC_GD/gate-run" 2>/dev/null | grep -cv '^current$')
[ "$left" -ge 9 ] && ok "a run KILLED before its verdict swept nothing (the sweep is after the verdict)" \
                  || nope "a killed run swept $((9-left)) record(s) — the sweep is running before the verdict"
rec_done

# --- the durable output copy is redacted and restrictive, with a control --------------------------
rec_repo
rec_legs '[ {"name": "leak", "argv": ["bash", "fx/leak.sh"]} ]'
rec_run GATE_FULL=1 >/dev/null
d=$(rec_dir)
if grep -rq 'u:p@example.com' "$d" 2>/dev/null; then
  nope "the DURABLE per-leg output copy carries an unmasked credential"
else
  ok "the durable per-leg output copy is redacted"
fi
if grep -rq '\*\*\*:\*\*\*@example.com' "$d" 2>/dev/null; then
  ok "control: the masked form IS present, so the arm above is not passing on an empty file"
else
  nope "neither the raw nor the masked credential is in the record — the redaction arm proves nothing"
fi
rec_done

# --- the fingerprint helper's two forms ------------------------------------------------------------
rec_repo
FP="$REC_T/tools/run-gates/gate-fingerprint.sh"
a=$( cd "$REC_T" && bash "$FP" ); b=$( cd "$REC_T" && bash "$FP" HEAD )
[ -n "$a" ] && [ "$a" = "$b" ] \
  && ok "on a clean tree the no-argument and at-a-rev forms agree" \
  || nope "the two fingerprint forms disagree on a clean tree ('$a' vs '$b')"
echo second > "$REC_T/fx/a.sh"; ( cd "$REC_T" && git add -A && git commit -qm second ) >/dev/null 2>&1
c=$( cd "$REC_T" && bash "$FP" HEAD ); p=$( cd "$REC_T" && bash "$FP" HEAD~1 )
[ -n "$p" ] && [ "$p" != "$c" ] \
  && ok "the helper at HEAD~1 differs from the helper at HEAD (the argument is LIVE)" \
  || nope "the helper returns the same digest for two different revs — the argument is dead, and the push boundary would take the digest at the tip"
( cd "$REC_T" && git checkout -q HEAD~1 )
q=$( cd "$REC_T" && bash "$FP" )
[ "$q" = "$p" ] \
  && ok "the at-a-rev digest equals the no-argument digest measured with that rev checked out clean" \
  || nope "the at-a-rev form does not reproduce the working-tree form at the same rev"
( cd "$REC_T" && git checkout -q main )
echo dirty >> "$REC_T/fx/a.sh"
e=$( cd "$REC_T" && bash "$FP" ); f=$( cd "$REC_T" && bash "$FP" HEAD )
{ [ "$e" != "$f" ] && [ "$f" = "$c" ]; } \
  && ok "on a dirty tree the forms differ and the at-a-rev form is unmoved" \
  || nope "the dirty-tree behaviour is wrong (worktree '$e', rev '$f', clean-rev '$c')"
rec_done

# --- the header's run envelope is FOUR keys, across two fixtures with different profile rows -------
# One fixture cannot separate a header that records the envelope from one that hardcodes the
# catch-all row's values.
for prof in capable minimal; do
  rec_repo
  rec_run GATE_FULL=1 GATE_PROFILE="$prof" >/dev/null
  h=$(rec_dir)/header
  pl=$(grep -m1 '^gate profile: ' "$REC_OUT")
  hrow=$(awk -F'\t' '$1=="profile_row"{print $2}' "$h" 2>/dev/null)
  hw=$(awk -F'\t' '$1=="width"{print $2}' "$h" 2>/dev/null)
  ht=$(awk -F'\t' '$1=="leg_timeout"{print $2}' "$h" 2>/dev/null)
  hf=$(awk -F'\t' '$1=="profile_from"{print $2}' "$h" 2>/dev/null)
  if [ "$hrow" = "$prof" ] && [ -n "$hw" ] && [ -n "$ht" ] && [ -n "$hf" ] \
     && printf '%s' "$pl" | grep -q "^gate profile: $prof " \
     && printf '%s' "$pl" | grep -q "width $hw"; then
    ok "the header's four envelope keys match the PROF_LINE this run printed (row $prof)"
  else
    nope "the header envelope disagrees with PROF_LINE for row $prof (row='$hrow' width='$hw' timeout='$ht' from='$hf' line='$pl')"
  fi
  rec_done
done
rm -f "$REC_OUT"

# =================================================================================================
# REUSE A PROVEN GREEN (the reuse unit). Every arm drives the real runner in its own scratch repo,
# for the reason the record arms above give: these have to make trees dirty and re-run over a ledger.
#
# EVERY POSITIVE ARM CARRIES ITS CONTROL. "Nothing was reused" is the state a cold ledger, a broken
# key and a correct refusal all produce, so an arm that only checks for the absence of the reuse verb
# passes on all three. Each one below therefore also proves that reuse WOULD have fired.

ru_repo() {   # -> RU_T, RU_GD
  RU_T=$(mktemp -d)
  mkdir -p "$RU_T/tools/run-gates" "$RU_T/tools/lib" "$RU_T/fx" "$RU_T/ga" "$RU_T/gb"
  cp "$ROOT/tools/run-gates/run-gates.sh" "$ROOT/tools/run-gates/gate-fingerprint.sh" \
     "$ROOT/tools/run-gates/gate-profiles.txt" "$RU_T/tools/run-gates/" || return 1
  cp "$ROOT/tools/lib/resolve-python.sh" "$RU_T/tools/lib/" 2>/dev/null || true
  ( cd "$RU_T" && git init -q -b main . && git config user.email ru@test.invalid \
      && git config user.name ru-test ) >/dev/null 2>&1 || return 1
  printf '#!/usr/bin/env bash\necho a\nexit 0\n' > "$RU_T/fx/a.sh"
  printf '#!/usr/bin/env bash\necho b\nexit 0\n' > "$RU_T/fx/b.sh"
  echo x > "$RU_T/ga/f"; echo y > "$RU_T/gb/f"
  printf '%s\n' '[' \
    '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
    '  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]}' \
    ']' > "$RU_T/tools/gate-legs.json"
  ( cd "$RU_T" && git add -A && git commit -qm seed ) >/dev/null 2>&1 || return 1
  ( cd "$RU_T" && git update-ref refs/remotes/origin/main HEAD \
      && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
  RU_GD="$RU_T/.git"
}
ru_run() { ( cd "$RU_T" && env "$@" bash tools/run-gates/run-gates.sh >"$REC_OUT" 2>&1; echo $? ); }
ru_done() { rm -rf "$RU_T"; }

REC_OUT=${REC_OUT:-$(mktemp)}

ru_repo || { echo "evidence-test: cannot build a reuse scratch"; exit 2; }
ru_run GATE_FULL=1 >/dev/null
ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
[ "$(grep -c '^GATE reuse ' "$REC_OUT")" = 2 ] \
  && ok "with GATE_REUSE set, an unchanged tree reuses every pure leg" \
  || { nope "reuse did not fire on an unchanged tree"; grep '^GATE ' "$REC_OUT" | sed 's/^/      /'; }
grep -qE 'reused\)' "$REC_OUT" && ok "the verdict line reports a non-zero reused count" \
                               || nope "the verdict does not name the reused count"
ru_done

# THE OPT-IN DEFAULT, with the precondition that makes the arm mean something. An advisory input may
# cause LESS work only on a run that is not authoritative, and this is the one criterion guarding
# that boundary — so it first proves the rows WOULD have matched, then proves they were not used.
ru_repo
ru_run GATE_FULL=1 >/dev/null
ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
[ "$(grep -c '^GATE reuse ' "$REC_OUT")" = 2 ] \
  && ok "precondition: those ledger rows WOULD match this run's keys" \
  || nope "the rows do not match, so the opt-in arm below would pass by finding nothing"
ru_run GATE_FULL=1 >/dev/null
ru_a=$(grep -E '^GATE ' "$REC_OUT")
grep -q '^GATE reuse ' "$REC_OUT" && nope "a leg was reused with GATE_REUSE unset — the default leaked" \
                                  || ok "no leg is reused with GATE_REUSE unset"
rm -f "$RU_GD/gate-ledger.tsv"; ru_run GATE_FULL=1 >/dev/null
ru_b=$(grep -E '^GATE ' "$REC_OUT")
[ "$ru_a" = "$ru_b" ] && ok "stdout with a matching ledger is byte-identical to the same tree with no ledger" \
                      || nope "stdout differs from the ledger-removed control — something advisory reached the default path"
ru_done

# A CHANGE INSIDE ONE GUARD, and its control: the arm has to show the OTHER leg still reusing, or a
# runner that simply stopped reusing altogether passes it.
ru_repo
ru_run GATE_FULL=1 >/dev/null
echo moved > "$RU_T/ga/f"; ( cd "$RU_T" && git add -A && git commit -qm move ) >/dev/null 2>&1
ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
grep -q '^GATE ok    pa' "$REC_OUT" && ok "a leg whose guarded input moved is NOT reused" \
                                    || nope "a leg was reused although a file inside its guard changed"
grep -q '^GATE reuse pb' "$REC_OUT" && ok "control: the untouched leg on the same run WAS reused" \
                                    || nope "no leg reused on that run, so the arm above proves nothing"
ru_done

# AN IMPURE LEG IS NEVER REUSED. Fixture-declared: this tree's own corpus is not the subject, and a
# harness that ships must not assert which of an adopter's legs are impure.
ru_repo
printf '%s\n' '[' \
  '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"], "impure": "reads a remote"},' \
  '  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]}' \
  ']' > "$RU_T/tools/gate-legs.json"
( cd "$RU_T" && git add -A && git commit -qm impure ) >/dev/null 2>&1
ru_run GATE_FULL=1 >/dev/null
ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
grep -q '^GATE ok    pa' "$REC_OUT" && ok "a leg declared impure executes even on a byte-identical tree" \
                                    || nope "an impure leg was reused"
grep -q '^GATE reuse pb' "$REC_OUT" && ok "control: a pure sibling WAS reused on that same run" \
                                    || nope "nothing was reused, so the impure arm proves nothing"
ru_done

# A RED ROW IS NEVER REUSABLE, and the ledger says so in the field rather than leaving the rule to be
# re-implemented by every reader.
ru_repo
printf '#!/usr/bin/env bash\necho boom\nexit 3\n' > "$RU_T/fx/a.sh"
( cd "$RU_T" && git add -A && git commit -qm red ) >/dev/null 2>&1
ru_run GATE_FULL=1 >/dev/null
ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
grep -q '^GATE FAIL  pa' "$REC_OUT" && ok "a leg whose recorded row is a failure runs again" \
                                    || nope "a red leg was reused"
grep -q '^GATE reuse pb' "$REC_OUT" && ok "control: the green sibling WAS reused on that run" \
                                    || nope "nothing was reused, so the red arm proves nothing"
ru_done

# REUSE DEFEATS THE FULL-GREEN STAMP. This is the join the push boundary rests on: a stamp must never
# be able to describe a run that copied a verdict instead of earning it.
ru_repo
ru_run GATE_FULL=1 >/dev/null
[ -f "$RU_GD/gate-full-green" ] && ok "control: the earning run stamped a full green" \
                                || nope "the earning run did not stamp, so the arm below proves nothing"
rm -f "$RU_GD/gate-full-green"
ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
[ -f "$RU_GD/gate-full-green" ] && nope "a run that reused legs stamped a full green" \
                               || ok "a run that reused ANY leg does not stamp a full green"
ru_done

# THE PROFILER STILL SEES A REUSED LEG. Without this the new verb is dropped by that tool's verdict
# grammar and the bar is under-counted in silence — the same class as a leg that stops being
# collected.
if [ -f "$ROOT/tools/run-gates/profile_bar.py" ]; then
  ru_repo
  cp "$ROOT/tools/run-gates/profile_bar.py" "$RU_T/tools/run-gates/"
  ru_run GATE_FULL=1 >/dev/null
  ru_out=$( cd "$RU_T" && "${PYBIN:-python}" tools/run-gates/profile_bar.py --width 2 2>&1 )
  # Matched on the word the tool uses for a REFUSAL, not on 'executed leg' — which appears in its
  # ordinary success line ('across N executed leg(s)') and made this arm fail on a healthy run.
  if printf '%s' "$ru_out" | grep -qi 'refus'; then
    nope "the profiler refused on the earning run, so its reuse grammar cannot be reached here"
    printf '%s
' "$ru_out" | tail -3 | sed 's/^/      /'
  else
    ok "control: the profiler records a run of this fixture without refusing"
  fi
  ru_done
else
  ok "no profiler ships beside the runner here, so its reuse grammar is not gradeable (stated)"
fi

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "run-gates evidence: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates evidence durability, $n assertions)"
exit "$bad"
