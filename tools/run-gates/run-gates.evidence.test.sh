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
KIT_REL="${KIT_REL:-tools/run-gates}"
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
FLOOR_ASSERTIONS=70
n=0
ok()   { n=$((n+1)); echo "  ok   — $1"; }
nope() { n=$((n+1)); echo "  FAIL — $1"; bad=1; }
# A SKIP THAT ANNOUNCES ITSELF. This file had `ok` and `nope` and nothing else, so an arm that could
# not be exercised had only two ways to end: claim a pass it had not earned, or accuse the subject of
# a defect it had not observed. It chose the second, which is worse. `skipped` counts toward the same
# floor as the other two, so an arm that stops running still cannot vanish quietly.
skipped() { n=$((n+1)); echo "  SKIP — $1"; }

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
  printf '#!/usr/bin/env bash\nsleep 60\nexit 0\n'    > "$REC_T/fx/slow.sh"
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
# THE AMBIENT SCOPING ENV IS CLEARED, and this is load-bearing rather than tidy. This fixture builds
# a scratch repo and drives a nested runner to grade what that runner RECORDS — including whether a
# guard fired. `.githooks/pre-push` exports GATE_BASE before it runs the bar, so when this leg runs
# at the push boundary the nested runner inherits a sha that does not exist in the scratch repo,
# resolves an EMPTY base, and falls back to running everything. Nothing is skipped, and the arm whose
# whole subject is a skipped leg refuses — correctly, and for a reason outside its own repo.
#
# This is the `inputs-inside-the-subjects-reach` class: the harness measuring the subject shares an
# input with it. Every call site's own `KEY=VALUE` still wins, because `-u` is applied first.
rec_run()  { ( cd "$REC_T" && env -u GATE_BASE -u GATE_FULL -u GATE_REUSE -u GATE_JOBS -u GATE_PROFILES "$@" bash $KIT_REL/run-gates.sh >"$REC_OUT" 2>&1; echo $? ); }
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
# BRACKETED, because the hard-kill arm below needs to know how slow THIS host is rather than assume
# it. This arm already drives a full run to completion, so the measurement is free.
REC_T0=$(date +%s)
rc=$(rec_run GATE_FULL=1)
REC_STARTUP=$(( $(date +%s) - REC_T0 ))
[ "$REC_STARTUP" -ge 1 ] 2>/dev/null || REC_STARTUP=1
if [ "$rc" = 0 ] && grep -q 'GATE ok    reader' "$REC_OUT"; then
  ok "a leg resolved gate-run/current and read this run's header WHILE the run was in flight"
else
  nope "a leg could not read the in-flight header (rc=$rc)"; sed 's/^/      /' "$REC_OUT"
fi
rec_done

# --- a hard kill leaves a header and NO verdict ---------------------------------------------------
# THE KILL LANDS AT 20s AGAINST A 60s LEG, and the margin is wide on purpose. It was 2s, which
# measured 2136 ms to write the header on this platform, so the arm was grading the runner's STARTUP
# BUDGET; widening to 5s against a 6s leg fixed that STANDALONE and left a one-second window that
# ambient load closes. Measured 2026-08-21: this arm passed alone and failed inside the concurrent
# 90-leg bar on the same tree, twice, because startup under that load exceeds 5s — the same defect
# the 2s note describes, one order of magnitude up.
#
# Widening the KILL alone would let the leg finish first and leave no crash to observe, so the leg
# sleeps 60s and the kill lands at 20s: any startup under 20s is mid-run with room on both sides.
# The file's own better idiom is at the sweep arm below — "THE EDIT WAITS FOR A FACT, NOT A CLOCK" —
# and it is not used here because `timeout -s KILL` is what makes the descendants die; polling for
# the header and then killing a backgrounded pipeline leaks the nested legs, which is the orphan
# class this repo catalogues under bounded-through-a-pipe-is-unbounded.
# ...AND THE DEADLINE IS DERIVED NOW, because a fourth hand-widening buys margin without removing
# the class. Startup here was measured at 5, 6, 14, 15 and 17 seconds inside ten minutes with no code
# change — a 3.4x spread straddling a fixed 20. Three times the run measured above, floored at the 20
# this arm already used so no host gets a TIGHTER deadline than before, and capped at 50 so the 60s
# leg still cannot finish first and leave no crash to observe.
REC_KILL=$(( REC_STARTUP * 3 ))
[ "$REC_KILL" -lt 20 ] && REC_KILL=20
[ "$REC_KILL" -gt 50 ] && REC_KILL=50
rec_repo
rec_legs '[ {"name": "slow", "argv": ["bash", "fx/slow.sh"]} ]'
( cd "$REC_T" && timeout -s KILL "$REC_KILL" env GATE_FULL=1 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1
d=$(rec_dir)
# A MISSING HEADER IS NOT AUTOMATICALLY A DEFECT, and this arm used to say it was. The header is
# written late in startup — after the fingerprint, the porcelain walk, python resolution and the
# manifest parse — while `gate-run/current` is written well before it. A kill landing DURING startup
# therefore leaves `current` present and `header` absent: a run that was never graded, not a runner
# that loses its header on a crash. Measured on this platform, `current` at 7.65s and 12.13s against
# headers at 15.53s and 18.04s. Printing "the crash case is unreadable" for that state is a starved
# host manufacturing a defect claim about code it never exercised. `nope` survives for the genuine
# shape only.
if [ -f "$d/header" ]; then
  ok "the header survived a hard kill"
elif [ -f "$REC_GD/gate-run/current" ]; then
  skipped "the kill at ${REC_KILL}s landed during startup (a full run here measured ${REC_STARTUP}s) — the run never reached its header, so the crash case went UNEXERCISED rather than failing"
else
  nope "no header and no run directory after a hard kill — the crash case is unreadable"
fi
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
( cd "$REC_T" && timeout -s KILL 20 env GATE_FULL=1 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1
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
ru_run() { ( cd "$RU_T" && env "$@" bash $KIT_REL/run-gates.sh >"$REC_OUT" 2>&1; echo $? ); }
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
  ru_out=$( cd "$RU_T" && "${PYBIN:-python}" $KIT_REL/profile_bar.py --width 2 2>&1 )
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

# =================================================================================================
# THE ADMISSION RULE (TOOL-aLeakedHandle-2). `derive-ceilings.py` built its evidence from `ok` rows
# only, so a leg that never finishes inside the retained window acquired no row at all and its
# ceiling was held above nothing — the gate that exists to catch an unsafe ceiling passing green on
# the very bar where that ceiling fired. A failing row is now admitted when its seconds land in the
# CLOSED window `[ceiling, ceiling + CEILING_WINDOW_S]`, and not otherwise.
#
# EVERY ARM RUNS AGAINST A COPY. `--write` writes to the SCRIPT's own directory, so an arm that
# reached the installed file would rewrite the tracked `ceiling-evidence.txt` — a self-test that
# edits the artifact its own merge-bar leg reads.
DC_T=$(mktemp -d)
mkdir -p "$DC_T/tools/run-gates"
cp "$ROOT/tools/run-gates/derive-ceilings.py" "$ROOT/tools/run-gates/ceiling-margin.txt" \
   "$DC_T/tools/run-gates/" || { echo "evidence-test: cannot copy the ceiling kit"; exit 2; }
( cd "$DC_T" && git init -q -b main . ) >/dev/null 2>&1 \
  || { echo "evidence-test: cannot init the ceiling fixture repo"; exit 2; }
DC_SCRIPT="$DC_T/tools/run-gates/derive-ceilings.py"
DC_EV="$DC_T/tools/run-gates/ceiling-evidence.txt"
# The launcher is RESOLVED, not assumed: this suite's other python arm falls back to a bare
# `python`, and on Windows that name can be the Store stub that answers `command -v` and exits 9009.
# An arm that dies on the launcher would print FAIL and accuse the subject of a defect it never saw.
DC_PY="${PYBIN:-}"
if [ -z "$DC_PY" ] && [ -f "$ROOT/tools/lib/resolve-python.sh" ]; then
  . "$ROOT/tools/lib/resolve-python.sh"
  DC_PY=$(resolve_python 2>/dev/null)
fi
[ -n "$DC_PY" ] || DC_PY=python
# Three legs, ONE ceiling, three failing readings: AT it, well BELOW it, and at FOUR TIMES it. The
# third is the class the window's upper edge refuses. It is not decoration — `run-gates.sh` sets
# `bound=0` and runs every leg UNBOUNDED when its CEILINGS_LIVE probe fails, and the `.leg` row
# carries no bound field, so an implementation spelling the predicate `secs >= ceiling` admits a
# leg that failed on its own at 4x its ceiling as though a bound had stopped it. That is the
# failure-duration-as-floor case the `ok`-only filter existed to prevent, and it enters a MONOTONE
# file. This arm gates that CLASS, not the 900.240 s instance the unit was written from.
#
# A FOURTH LEG CARRIES THE KILL-PATH OVERSHOOT AT A REALISTIC MAGNITUDE. `kill-overhead`'s ceiling
# and reading are sized from the elapsed-above-bound figure `run-gates.sh`'s rc=124 block records
# under load — read it THERE; this comment cites the source rather than copying its number, which is
# the defect this same commit removes from `derive-ceilings.py`. Nothing here re-verifies that
# figure: a different one would leave the fixture a valid clamp test, so the citation is provenance
# for the choice and never a parity claim. Two things need this leg and neither is served by the
# existing 100/100.4 pair:
# the window has to actually ADMIT the worst overshoot this repo has measured, and the clamp arm
# below needs a fixture where raw elapsed and the ceiling are far enough apart that reading one for
# the other is unmistakable rather than a rounding argument.
printf '%s\n' '[' \
  '  {"name": "at-ceiling",    "argv": ["true"], "ceiling": 100},' \
  '  {"name": "below-ceiling", "argv": ["true"], "ceiling": 100},' \
  '  {"name": "way-over",      "argv": ["true"], "ceiling": 100},' \
  '  {"name": "kill-overhead", "argv": ["true"], "ceiling": 2}' \
  ']' > "$DC_T/tools/gate-legs.json"
mkdir -p "$DC_T/.git/gate-run/r1"
{ printf 'at-ceiling\tfail\t124\t100.4\t0\t0\t-\n'
  printf 'below-ceiling\tfail\t1\t40.0\t0\t0\t-\n'
  printf 'way-over\tfail\t137\t400.0\t0\t0\t-\n'
  printf 'kill-overhead\tfail\t124\t12.0\t0\t0\t-\n'; } > "$DC_T/.git/gate-run/r1/1.leg"

dc_out=$("$DC_PY" "$DC_SCRIPT" --report 2>&1)
printf '%s\n' "$dc_out" | awk -F'\t' '$1=="at-ceiling" && $2=="100.0" {f=1} END{exit !f}' \
  && ok "a fail row AT its leg's ceiling is admitted as evidence" \
  || { nope "the row at the ceiling was not admitted — the change is absent"; printf '%s\n' "$dc_out" | sed 's/^/      /'; }
printf '%s\n' "$dc_out" | awk -F'\t' 'NF>=4 && $1=="below-ceiling" {f=1} END{exit !f}' \
  && nope "a fail row BELOW its ceiling was admitted — the ceiling comparison is gone" \
  || ok "a fail row below its ceiling stays excluded"
printf '%s\n' "$dc_out" | awk -F'\t' 'NF>=4 && $1=="way-over" {f=1} END{exit !f}' \
  && nope "a fail row at FOUR TIMES its ceiling was admitted — the window's upper edge is gone, which is the unbounded-run case" \
  || ok "a fail row at four times its ceiling stays excluded (the window is closed at the top)"
# THE CONTROL. A report that printed no table at all satisfies both exclusions above by finding
# nothing, which is the shape those two arms exist to rule out.
printf '%s\n' "$dc_out" | grep -q 'UNBACKED' \
  && printf '%s\n' "$dc_out" | grep 'UNBACKED' | grep -q 'below-ceiling' \
  && printf '%s\n' "$dc_out" | grep 'UNBACKED' | grep -q 'way-over' \
  && ok "control: both excluded legs are NAMED on the UNBACKED line, so the exclusions above are verdicts and not an empty report" \
  || { nope "the UNBACKED line does not name both excluded legs"; printf '%s\n' "$dc_out" | sed 's/^/      /'; }

# --- the WRITE path reads the ceilings too ---------------------------------------------------------
# The defaulted-parameter case, and it is the reason this arm drives `--write` rather than trusting
# the report. Give `read_runs` the ceilings map with a DEFAULT, pass it at `cmd_report` and forget
# `cmd_write`, and the only path that produces the tracked artifact keeps its `ok`-only behaviour
# while every arm above stays green. The merge-bar leg cannot see it either: it runs `--check`,
# which reads the two tracked files and no run file.
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
awk -F'\t' '$1=="at-ceiling" && $2=="100.0" {f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "--write records the ceiling-reaching leg's FAILING reading" \
  || { nope "--write wrote no row for the ceiling-reaching leg — the write path still filters on ok"; sed 's/^/      /' "$DC_EV" 2>/dev/null; }
awk -F'\t' '$1=="below-ceiling" || $1=="way-over" {f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && { nope "--write recorded a row for a leg the window excludes"; sed 's/^/      /' "$DC_EV"; } \
  || ok "--write records neither excluded leg"

# --- AN ADMITTED FAILING ROW IS CLAMPED TO ITS CEILING (TOOL-aLeakedHandle-1 F6) -------------------
# Only the ceiling is a provable lower bound on the work: `timeout` killed the leg there, and the
# elapsed value on that path is the ceiling PLUS kill-path overhead, which `run-gates.sh`'s own
# rc=124 block states. The artifact is MONOTONE, so an entry carrying that overhead never comes back
# down and permanently inflates the headroom `--check` demands above it. An EQUALITY, not a bound:
# `< 12.0` is satisfied by the row being absent, which is the shape the `ok`-only filter this unit
# removed would produce.
awk -F'\t' '$1=="kill-overhead" && $2=="2.0" {f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "an admitted rc=124 row enters the artifact at its ceiling (2.0), not at its 12.0 elapsed" \
  || { nope "the admitted rc=124 row did not enter at its ceiling — kill-path teardown is being recorded as work, permanently"; sed 's/^/      /' "$DC_EV" 2>/dev/null; }

# --- the check-time sentence -----------------------------------------------------------------------
# Written by hand rather than chained off the `--write` above, so a defect there cannot make this
# arm fail for a reason that is not its own.
printf 'at-ceiling\t100.4\t1\ta\t2026-09-10\n' > "$DC_EV"
dc_chk=$("$DC_PY" "$DC_SCRIPT" --check 2>&1); dc_rc=$?
if [ "$dc_rc" != 0 ] && printf '%s\n' "$dc_chk" | grep -q 'REACHED in a recorded run'; then
  ok "--check exits non-zero and says the ceiling was REACHED in a recorded run"
else
  nope "--check did not report the reached ceiling (rc=$dc_rc)"; printf '%s\n' "$dc_chk" | sed 's/^/      /'
fi
printf '%s\n' "$dc_chk" | grep -q 'does not clear its evidenced maximum' \
  && nope "a REACHED ceiling still reports the headroom arithmetic, which invites sizing a new ceiling from a lower bound" \
  || ok "a reached ceiling does not report the headroom sentence"

# --- THE TWO READERS OF ONE ARTIFACT AGREE (TOOL-aLeakedHandle-1 F5) -------------------------------
# A PARITY arm, not two per-reader assertions, and the difference is the whole point. `--check` was
# amended to withdraw the headroom sentence from a ceiling-reaching reading; `--report` — the table
# an operator actually sizes a ceiling FROM — was left calling the same reading UNDER and printing a
# `need` target beside it. Two readers of one artifact get one arm that joins them, or the next
# amendment lands on one side again. Graded on the SAME two values both readers derive from.
dc_rep_state=$(printf '%s\n' "$dc_out" | awk -F'\t' '$1=="at-ceiling"{print $7}')
dc_rep_need=$(printf '%s\n' "$dc_out" | awk -F'\t' '$1=="at-ceiling"{print $6}')
if printf '%s\n' "$dc_chk" | grep -q 'REACHED in a recorded run' \
   && [ "$dc_rep_state" = "REACHED" ] && [ "$dc_rep_need" = "-" ]; then
  ok "--report and --check agree on a ceiling-reaching reading: both say REACHED, and the table offers no need target to size a ceiling from"
else
  nope "--report and --check disagree on a ceiling-reaching reading (report state='$dc_rep_state' need='$dc_rep_need') — the human-facing reader is the one still inviting a sizing"
fi
# THE CONTROL for the arm above: the headroom sentence must still exist for the row it was written
# for, or its absence is a default rather than a verdict.
printf 'below-ceiling\t40.0\t1\ta\t2026-09-10\n' > "$DC_EV"
"$DC_PY" "$DC_SCRIPT" --check 2>&1 | grep -q 'does not clear its evidenced maximum' \
  && ok "control: a row BELOW its ceiling still gets the headroom sentence" \
  || nope "no row gets the headroom sentence at all, so the arm above proves nothing"

# --- the admitted failing row must reach the number the gate consumes ------------------------------
# An `ok` reading BELOW the ceiling, alongside the failing one at it: admission that never reaches
# the maximum is admission that changed nothing.
printf 'at-ceiling\tok\t0\t20.0\t0\t0\t-\n' >> "$DC_T/.git/gate-run/r1/1.leg"
dc_out=$("$DC_PY" "$DC_SCRIPT" --report 2>&1)
printf '%s\n' "$dc_out" | awk -F'\t' '$1=="at-ceiling" && $2=="100.0" && $3=="2" {f=1} END{exit !f}' \
  && ok "with an ok row below the ceiling too, the reported max is the FAILING row's seconds over both readings" \
  || { nope "the reported maximum is not the failing row's"; printf '%s\n' "$dc_out" | sed 's/^/      /'; }

# --- `--write --reset <leg>` ACTUALLY LOWERS, WITH THE OFFENDING RUN STILL RETAINED (F4) -----------
# The docstring rests the entire mitigation of the monotone-floor hazard on this escape, so the
# escape is EXERCISED rather than read. `--reset` bypassed the monotone hold and nothing else, which
# is inert for the whole GATE_RUN_KEEP window: `max(vals)` was re-derived from the same retained
# `.leg` rows and the identical value went straight back. That window is the only one an operator
# reaches for it in — the offending run is what put the row there — so the promise was falsifiable
# exactly where it was made and never falsified.
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
dc_before=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
"$DC_PY" "$DC_SCRIPT" --write --reset at-ceiling >/dev/null 2>&1
dc_after=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
# THE CONTROL FIRST: a reset that lowered nothing and a reset with nothing to lower produce the same
# `dc_after`, so the row it has to clear is proved present before the lowering is graded.
# Graded as a PROPERTY (the row is a ceiling-reaching reading) rather than against a literal, so it
# does not silently couple to whatever the block above last wrote into the evidence file.
awk -v a="$dc_before" 'BEGIN{exit !(a != "" && a+0 >= 100)}' \
  && ok "control: the pre-reset row ($dc_before) is a ceiling-reaching reading, so the reset has something to lower" \
  || nope "the pre-reset row is '$dc_before', below its 100s ceiling — the reset arm below would grade nothing"
if [ -n "$dc_before" ] && [ -n "$dc_after" ] \
   && awk -v a="$dc_before" -v b="$dc_after" 'BEGIN{exit !(b<a)}'; then
  ok "--write --reset LOWERED the row while the run that produced the reading was still retained ($dc_before -> $dc_after)"
else
  nope "--write --reset left the row at '$dc_after' — the documented escape from an admitted killed reading is inert for the whole retention window"
fi
# THE ARM THAT ACTUALLY GRADES THE ESCAPE, and the one the arm above cannot be (TOOL-aLeakedHandle-1
# D1). A reset that lowers the row for exactly ONE invocation satisfies every assertion up to here:
# the second revision of this escape filtered the killed reading per-process and left it sitting in
# the retention window, so the next ordinary `--write` re-admitted it, `max(vals)` handed the cleared
# value back, and the summary said `1 raised`. 100.0 -> 20.0 -> 100.0, all three greens. What
# separates a discard from a filter is therefore what the row READS one ordinary write later, and
# nothing shorter than that write can ask it.
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
dc_later=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
if [ -n "$dc_later" ] \
   && awk -v a="$dc_after" -v b="$dc_later" 'BEGIN{exit !(a != "" && b+0 == a+0)}'; then
  ok "the reset value ($dc_after) SURVIVES the next ordinary --write, with the run that produced the killed reading still retained"
else
  nope "an ordinary --write put the row back to '$dc_later' from the same retained killed reading — the reset lasted one invocation, not the retention window"
fi
# THE SUMMARY LINE IS GRADED TOO, because it is the only feedback `--write` gives and it was
# reporting the opposite of what happened (D4). A reset re-deriving the value already stored was
# forced out of the monotone hold by its own `name not in reset` clause and counted as a RAISE.
# TWO RESETS BACK TO BACK, deliberately: the equal-value case is only reachable on the SECOND, and
# re-running the reset is exactly the gesture an operator makes when the first appeared not to
# stick. Graded on the COUNTER against the row's own movement, not on the row alone — the row is
# unchanged either way, which is what made this invisible.
"$DC_PY" "$DC_SCRIPT" --write --reset at-ceiling >/dev/null 2>&1
dc_noop_pre=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
dc_noop=$("$DC_PY" "$DC_SCRIPT" --write --reset at-ceiling 2>&1)
dc_noop_row=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
dc_raised=$(printf '%s\n' "$dc_noop" | grep -o '[0-9]* raised' | head -1 | cut -d' ' -f1)
if awk -v r="$dc_noop_row" -v p="$dc_noop_pre" 'BEGIN{exit !(r != "" && p != "" && r+0 == p+0)}' \
   && [ "$dc_raised" = 0 ]; then
  ok "a repeated reset re-derives the identical value ($dc_noop_pre -> $dc_noop_row) and reports no movement (raised=$dc_raised)"
else
  nope "a repeated reset left the row at '$dc_noop_row' from '$dc_noop_pre' and printed '$dc_raised raised' — a count of work nobody did, in the only line --write prints"
fi

# AND WHEN NOTHING SURVIVES THE RESET, THE ROW GOES. `kill-overhead` has only the killed reading, so
# a reset leaves it nothing to re-derive from. Carrying the previous row forward there would hand
# back the exact value the operator asked to clear while printing that the reset ran, which is worse
# than doing nothing because it looks like it worked. UNBACKED is `--check`'s reported, non-failing
# state, and the next ordinary `--write` re-derives the leg once a finished run is in the window.
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
awk -F'\t' '$1=="kill-overhead"{f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "control: the ordinary write restored kill-overhead's row, so its absence below is the reset's doing" \
  || nope "kill-overhead has no row before the drop arm, so that arm would pass by finding nothing"
"$DC_PY" "$DC_SCRIPT" --write --reset kill-overhead >/dev/null 2>&1
awk -F'\t' '$1=="kill-overhead"{f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && { nope "a reset leg with no surviving reading kept its old row — the reset silently restored the value it was asked to clear"; sed 's/^/      /' "$DC_EV" 2>/dev/null; } \
  || ok "a reset leg with no surviving reading loses its row rather than carrying the cleared value forward"
awk -F'\t' '$1=="at-ceiling"{f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "control: the untouched leg kept its row on that same write, so the drop above is a verdict and not an emptied file" \
  || nope "no row survived that write at all — the drop arm above proves nothing"
# THE DROP HAS THE IDENTICAL LIFETIME QUESTION, so it gets the identical arm. A dropped row whose
# killed reading is still retained comes straight back on the next ordinary write, at the value the
# operator cleared, and the absence asserted above would have been true for one invocation only.
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
dc_ko_later=$(awk -F'\t' '$1=="kill-overhead"{print $2}' "$DC_EV" 2>/dev/null)
[ -z "$dc_ko_later" ] \
  && ok "the dropped row STAYS dropped across the next ordinary --write, rather than being re-derived from the killed reading it was cleared of" \
  || nope "an ordinary --write re-derived kill-overhead at '$dc_ko_later' from the reading the reset discarded — the drop lasted one invocation"

# --- THE RESET LEG IS THE ONLY LEG WITH A READING (TOOL-aLeakedHandle-1 D3) ------------------------
# The state the DEAD-PROBE return was preempting: `cmd_write` asked "what survives the reset" and
# printed the answer to "was anything measured at all", so a reset naming the only leg with a
# retained reading exited 2 saying nothing was measured — of readings it had just excluded itself —
# and the stale row it was asked to clear survived. Reachable without contrivance: GATE_LEGS
# produces a one-leg bar, guards scope a run to a handful, and resetting every leg that currently
# has a retained reading is the plain case. The fixture above cannot see it, because `at-ceiling`
# keeps an `ok` row there and `runs` is never empty.
printf 'at-ceiling\tfail\t124\t100.4\t0\t0\t-\n' > "$DC_T/.git/gate-run/r1/1.leg"
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
dc_lonely_pre=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
awk -v a="$dc_lonely_pre" 'BEGIN{exit !(a != "" && a+0 >= 100)}' \
  && ok "control: the sole-reading leg holds a ceiling-reaching row ($dc_lonely_pre) before the reset, so the arm below has something to clear" \
  || nope "the sole-reading leg reads '$dc_lonely_pre' before the reset — the arm below would grade an absence"
dc_lonely=$("$DC_PY" "$DC_SCRIPT" --write --reset at-ceiling 2>&1); dc_lonely_rc=$?
dc_lonely_row=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
if [ "$dc_lonely_rc" = 0 ] && [ -z "$dc_lonely_row" ] \
   && ! printf '%s\n' "$dc_lonely" | grep -q 'DEAD PROBE'; then
  ok "resetting the only leg with a reading runs the drop path: exit 0, the row gone, and no DEAD PROBE misdiagnosis"
else
  nope "resetting the only leg with a reading exited $dc_lonely_rc leaving the row at '$dc_lonely_row' — the liveness return fired above the drop path it was supposed to let through"
  printf '%s\n' "$dc_lonely" | sed 's/^/      /'
fi
# THE LIVENESS CONTROL FOR THAT SPLIT. Asking the emptiness question without the reset filter must
# not stop it being asked: with the run record genuinely empty, DEAD PROBE still fires, or the arm
# above is satisfied by a check that was deleted rather than moved.
rm -f "$DC_T/.git/gate-run/r1/1.leg"
dc_dead=$("$DC_PY" "$DC_SCRIPT" --write 2>&1); dc_dead_rc=$?
if [ "$dc_dead_rc" = 2 ] && printf '%s\n' "$dc_dead" | grep -q 'DEAD PROBE'; then
  ok "control: with no retained reading at all, --write still exits 2 with DEAD PROBE"
else
  nope "control: an empty run record no longer reports DEAD PROBE (rc=$dc_dead_rc) — the liveness assertion was removed, not relocated"
fi

# --- the docstring is the only written statement of any of this ------------------------------------
# §5 rests the whole mitigation of the monotone-floor hazard on it, so it is OBSERVED rather than
# assumed. The substrings are named by the criterion, not chosen here, so the arm grades content
# rather than a builder's choice of grep.
dc_doc=$("$DC_PY" -c 'import ast,sys
for n in ast.parse(open(sys.argv[1],encoding="utf-8").read()).body:
    if isinstance(n, ast.FunctionDef) and n.name == "read_runs":
        print(ast.get_docstring(n) or "")' "$DC_SCRIPT" 2>&1)
dc_miss=""
for dc_w in ceiling slow contended hung; do
  printf '%s\n' "$dc_doc" | grep -q -- "$dc_w" || dc_miss="$dc_miss $dc_w"
done
[ -z "$dc_miss" ] \
  && ok "read_runs's docstring states the ceiling comparison and names slow, contended and hung as the causes it cannot tell apart" \
  || nope "read_runs's docstring omits:$dc_miss — a rule with no written statement, or a statement of what it cannot distinguish that omits it"
printf '%s\n' "$dc_doc" | grep -q -- '--reset' \
  && ok "read_runs's docstring names the --write --reset <leg> escape, which is the half a reader ACTS on" \
  || nope "read_runs's docstring omits --reset, so the entire mitigation of the monotone-floor hazard ships undocumented"
rm -rf "$DC_T"

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "run-gates evidence: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates evidence durability, $n assertions)"
exit "$bad"
