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
#
# It also carries the post-merge bar's arms (TOOL-aFrugalTurnstile-6 AC1-AC10, between the
# `post-merge arms` markers near the end): a bare remote and a clone, the kit's `post-merge.sh` run on
# landed red and green commits, and the remote ref, the two records and the refusals read back.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "evidence-test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
KIT="${KIT_REL##*/}"   # this kit's own directory NAME (TOOL-aRepatriatedFork-46)

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "evidence-test: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
RUNNER="$ROOT/${PFX}${KIT}/run-gates.sh"
# The launcher is RESOLVED, not assumed, ONCE, for every python arm below: on Windows the bare name
# `python` can be the Store stub that answers `command -v` and exits 9009, and an arm that dies on
# the launcher would print FAIL and accuse the subject of a defect it never saw. `PYBIN=` overrides.
# TOOL-aRepatriatedFork-46: the resolver is carried INLINE; it was sourced from the library
# directory, which ships nowhere.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
DC_PY="${PYBIN:-}"
[ -n "$DC_PY" ] || DC_PY=$(resolve_python 2>/dev/null)
# NO BARE FALLBACK. The idiom ban this repo's own bar carries reads `DC_PY=python` as a launcher
# invoked without being resolved, and it was right: on the Store-stub machine that name is the
# one launcher guaranteed NOT to run. A resolver that answered nothing is a refusal, said aloud.
[ -n "$DC_PY" ] || { echo "evidence-test: no python launcher resolves, so the ceiling arms cannot run"; exit 2; }
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME. This
# suite's own NAME is bound beside PFX, above, because RUNNER reads it before this point.
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
LIB_DIR=$(resolve_kit_dir "$DC_PY" lib resolve-python.sh "$HERE") || exit 2
LIB="${LIB_DIR##*/}"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
# THE HOST TURNSTILE IS THIS SUITE'S OWN (TOOL-aFrugalTurnstile-5 S7): on the host default a fixture bar
# queues behind every real bar, and inside a real bar's leg it nests and never holds, which AC14's
# `queued_from held` control would read as the turnstile not running.
export GATE_TURNSTILE_DIR="$tmp/gate-turnstile"
# THE MEMORY PAUSE IS OFF for every bar here (TOOL-aGraftedHelix-7): the shipped table turns it on and
# it reads the HOST's memory, so a box above its threshold would narrow these bars' pools and move the
# census and timing arms for a reason that is the box's. The canary drives the pause over fixtures.
export GATE_MEMPAUSE=0
bad=0
# the run-gates promotion spec's S11. The count is INCREMENTED where the assertions actually happen -- in the
# two helpers every arm routes through -- so it can never drift from the arms the way a hardcoded
# literal does. That drift is the recorded failure this leg exists for: a suite printed a fixed
# `PASS (130 assertions)` for its whole life with no counter behind it.
FLOOR_ASSERTIONS=136
# RAISED 116 -> 136 by TOOL-aFrugalTurnstile-6: the post-merge bar's twenty assertions.
# RAISED 115 -> 116 by TOOL-aFrugalTurnstile-1: the control stamp's `manifest` key.
# MERGED 112 / 87 -> 115 at the reconcile with origin/main 290d0d2d5: base 84, plus this branch's 28, plus main's 3.
# RAISED 110 -> 112 by TOOL-aGraftedHelix-7: AC10's two assertions over a reading taken during a memory pause.
# RAISED 84 -> 87 by TOOL-dThriftyLanding-2: the shared-stamp control and its two assertions.
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
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${bad:-0}" = 0 ] && echo "PASS ($n assertions)" || echo "FAIL ($n assertions)"; [ "${bad:-0}" = 0 ] && exit 0; exit 1; fi

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
  mkdir -p "$REC_T/${PFX}${KIT}" "$REC_T/${PFX}${LIB}" "$REC_T/fx"
  cp "$ROOT/${PFX}${KIT}/run-gates.sh" "$ROOT/${PFX}${KIT}/gate-fingerprint.sh" \
     "$ROOT/${PFX}${KIT}/gate-profiles.txt" "$REC_T/${PFX}${KIT}/" || return 1
  cp "$ROOT/${LIB_DIR}/resolve-python.sh" "$REC_T/${PFX}${LIB}/" 2>/dev/null || true
  ( cd "$REC_T" && git init -q -b main . && git config user.email rec@test.invalid \
      && git config user.name rec-test ) >/dev/null 2>&1 || return 1
  printf '#!/usr/bin/env bash\necho hello\nexit 0\n' > "$REC_T/fx/a.sh"
  printf '#!/usr/bin/env bash\necho boom\nexit 3\n'  > "$REC_T/fx/red.sh"
  printf '#!/usr/bin/env bash\nsleep 60\nexit 0\n'    > "$REC_T/fx/slow.sh"
  printf '#!/usr/bin/env bash\necho "https://u:p@example.com"\nexit 0\n' > "$REC_T/fx/leak.sh"
  printf '%s\n' '[' \
    '  {"name": "one", "argv": ["bash", "fx/a.sh"]},' \
    '  {"name": "guarded", "argv": ["bash", "fx/a.sh"], "guard": ["fx/"]}' \
    ']' > "$REC_T/${PFX}gate-legs.json"
  ( cd "$REC_T" && git add -A && git commit -qm seed ) >/dev/null 2>&1 || return 1
  # A resolvable origin, so guards can compute a BASE and a skip is actually reachable. Without it
  # BASE is empty, changed() fails safe to "run", and every skip arm passes by finding nothing. The
  # remote is CONFIGURED, because the runner's remote ladder reads configuration (TOOL-dLadderedRemote-2).
  ( cd "$REC_T" && git remote add origin ../origin.git && git update-ref refs/remotes/origin/main HEAD \
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
rec_run()  { ( cd "$REC_T" && env -u GATE_BASE -u GATE_FULL -u GATE_REUSE -u GATE_JOBS -u GATE_PROFILES -u GATE_DOCS_BASE "$@" bash $KIT_REL/run-gates.sh >"$REC_OUT" 2>&1; echo $? ); }
rec_legs() { printf '%s\n' "$1" > "$REC_T/${PFX}gate-legs.json"
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
  blob=$( cd "$REC_T" && git hash-object -- ${PFX}gate-legs.json )
  grep -q "^manifest_blob	$blob$" "$REC_GD/gate-full-green" \
    && ok "the stamp's manifest_blob is the hash of the manifest THAT RUN READ" \
    || { nope "the stamp's manifest_blob does not match the manifest the run read"; sed 's/^/      /' "$REC_GD/gate-full-green"; }
  # WHICH manifest, repo-relative (TOOL-aFrugalTurnstile-1 AC6): the pre-push hook refuses a record
  # whose `manifest` is not the kit sibling, so an absolute or `./`-prefixed spelling costs a full bar.
  [ "$(awk -F'\t' '$1=="manifest"{print $2}' "$REC_GD/gate-full-green")" = "${PFX}gate-legs.json" ] \
    && ok "the stamp's manifest names the kit sibling ${PFX}gate-legs.json, repo-relative" \
    || { nope "the stamp's manifest is not ${PFX}gate-legs.json"; sed 's/^/      /' "$REC_GD/gate-full-green"; }
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

# --- TOOL-dThriftyLanding-2: a green earned in a LINKED worktree is shared through the common dir ---
# Its own git dir keeps its stamp, the common dir gains `gate-full-green.shared` carrying the same sha,
# and the common dir's OWN stamp, which is the primary tree's, is never written from a worktree.
rec_repo
# autocrlf OFF before the checkout: on a host that converts, the worktree's copy of the profile table
# reads CRLF and the runner refuses it, so the control would fail for a reason outside this unit.
( cd "$REC_T" && git config core.autocrlf false && git worktree add -q "$REC_T.wt" -b side ) >/dev/null 2>&1
( cd "$REC_T.wt" && env -u GATE_BASE -u GATE_REUSE -u GATE_JOBS -u GATE_PROFILES -u GATE_DOCS_BASE GATE_FULL=1 \
    bash $KIT_REL/run-gates.sh >"$REC_OUT" 2>&1 )
_wgd=$( cd "$REC_T.wt" && git rev-parse --git-dir 2>/dev/null )
_ws1=$(awk -F'\t' '$1=="sha"{print $2}' "$_wgd/gate-full-green" 2>/dev/null)
_ws2=$(awk -F'\t' '$1=="sha"{print $2}' "$REC_GD/gate-full-green.shared" 2>/dev/null)
if [ -n "$_ws1" ]; then
  ok "control: a fully-green run in a linked worktree stamps its own git dir"
  [ "$_ws1" = "$_ws2" ] && ok "the common dir's gate-full-green.shared carries the worktree green's sha" \
                        || nope "no shared stamp, or one naming another sha ([$_ws1] vs [$_ws2])"
  [ -f "$REC_GD/gate-full-green" ] && nope "a linked worktree's green wrote the primary tree's own stamp" \
                                   || ok "the primary tree's own stamp is untouched by a worktree's green"
else
  nope "the control failed: the linked worktree's run stamped nothing, so the sharing arms prove nothing"
fi
rm -rf "$REC_T.wt"; rec_done

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
keep=$(grep -m1 -oE 'GATE_RUN_KEEP:-[0-9]+' "$ROOT/${PFX}${KIT}/run-gates.sh" | grep -oE '[0-9]+')
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
FP="$REC_T/${PFX}${KIT}/gate-fingerprint.sh"
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

# =================================================================================================
# THE FOREIGN-LOAD CENSUS (TOOL-aGraftedHelix-5). Every arm drives the real runner in its own scratch
# repo and reads what it recorded: the run's `census` file and the eighth field of its `.leg` rows,
# `foreign`. NO ARM ASSERTS A TOTAL: another session's suite on this host is foreign gate work, so an
# arm reading the census's count would red on a busy host for a reason that is not its own. The arms
# assert ROOTS BY PID, a process the arm started or one it must never see, and the fields a census
# that could not see must write.
#
# load.sh sleeps its first argument, after touching its second when one is given, and takes its
# sleep down with it on TERM, so an arm that stops its outside load leaves no orphan behind.
write_load_fixture() { printf '%s\n' '#!/usr/bin/env bash' '[ -n "${2:-}" ] && : > "$2"' 'trap "kill \$! 2>/dev/null; exit 0" TERM' \
              'sleep "${1:-5}" & wait' 'exit 0' > "$REC_T/fx/load.sh"; }
# check_census_root <census file> <pid:token> [<first line to read>] — rc 0 when a sample names that root
check_census_root() { awk -F'\t' -v w="$2" -v from="${3:-1}" 'NR >= from { n = split($3, r, " "); for (i = 1; i <= n; i++) if (r[i] == w) f = 1 } END { exit !f }' "$1" 2>/dev/null; }
read_foreign_field() { awk -F'\t' 'NR == 1 { print $8 }' "$1" 2>/dev/null; }
# The stub `ps` dirs go FIRST on PATH, and PATH is colon-separated, so a drive-letter spelling of the
# scratch dir (`C:/...`, which `mktemp` returns under a Windows-spelled TMPDIR) would split the stub
# dir in two and put no stub first.
cn_pd=$(cygpath -u "$tmp" 2>/dev/null) || cn_pd=$tmp

# --- AC1: an outside run of the leg's own script, alive beside the bar, is a foreign root ----------
# STARTED THROUGH `exec`, so the pid the arm holds is the process the census sees: a subshell that
# did not exec would be a fork of this harness, whose own line ends `.test.sh`.
rec_repo; write_load_fixture
rec_legs '[ {"name": "loaded", "argv": ["bash", "fx/load.sh", "5"]} ]'
( cd "$REC_T" && exec bash fx/load.sh 120 ) & cn_out=$!
rc=$(rec_run GATE_FULL=1)
d=$(rec_dir); cn_f=$(read_foreign_field "$d/0.leg")
case "$cn_f" in ''|*[!0-9]*) cn_n=0 ;; *) cn_n=$cn_f ;; esac
[ "$rc" = 0 ] && [ "$cn_n" -ge 1 ] \
  && ok "AC1 a leg run beside an outside run of its own script records foreign $cn_f" \
  || { nope "AC1 the leg's foreign field reads '$cn_f' (rc=$rc) with an outside run of its script alive"; sed 's/^/      /' "$d/census" 2>/dev/null; }
check_census_root "$d/census" "$cn_out:fx/load.sh" \
  && ok "AC1 the census names the outside process as a root, by pid $cn_out and the leg's script as its token" \
  || { nope "AC1 no census line names $cn_out:fx/load.sh — the outside process was not a root"; sed 's/^/      /' "$d/census" 2>/dev/null; }
kill "$cn_out" 2>/dev/null; wait "$cn_out" 2>/dev/null
rec_done

# --- AC2: the runner's ancestors and descendants are never foreign --------------------------------
# The wrapper is a `bash -c` whose argv names the runner's path, which is exactly what an agent
# session's wrapper looks like; the leg runs nest.sh, which starts a nested nest.sh, so both match
# a manifest token and both are descendants. Sampled every second so a snapshot holds them.
rec_repo
printf '#!/usr/bin/env bash\nif [ "${1:-}" = outer ]; then echo $$ > .git/cn-leg.pid; bash fx/nest.sh inner & echo $! > .git/cn-nested.pid; sleep 5; wait; else sleep 6; fi\nexit 0\n' > "$REC_T/fx/nest.sh"
rec_legs '[ {"name": "nest", "argv": ["bash", "fx/nest.sh", "outer"]} ]'
( cd "$REC_T" && env -u GATE_BASE -u GATE_REUSE -u GATE_JOBS -u GATE_PROFILES GATE_FULL=1 GATE_CENSUS_EVERY=1 \
    bash -c 'echo $$ > .git/cn-wrapper.pid; bash "$1"; true' _ "$REC_T/$KIT_REL/run-gates.sh" ) >"$REC_OUT" 2>&1
d=$(rec_dir); cn_id=$(cat "$REC_GD/gate-run/current" 2>/dev/null)
cn_lines=$(wc -l < "$d/census" 2>/dev/null | tr -d ' ')
[ "${cn_lines:-0}" -ge 2 ] \
  && ok "AC2 control: the census took $cn_lines samples, so a snapshot held the leg and its nested run" \
  || nope "AC2 the census holds ${cn_lines:-0} line(s), so no snapshot ever held the leg — the arm below would pass by finding nothing"
cn_bad=""
for cn_p in "$(cat "$REC_GD/cn-wrapper.pid" 2>/dev/null)" "${cn_id##*-}" "$(cat "$REC_GD/cn-leg.pid" 2>/dev/null)" "$(cat "$REC_GD/cn-nested.pid" 2>/dev/null)"; do
  [ -n "$cn_p" ] || { cn_bad="$cn_bad (a pid file is missing)"; continue; }
  awk -F'\t' -v p="$cn_p" '{ n = split($3, r, " "); for (i = 1; i <= n; i++) if (r[i] ~ "^" p ":") f = 1 } END { exit !f }' "$d/census" 2>/dev/null \
    && cn_bad="$cn_bad $cn_p"
done
[ -z "$cn_bad" ] \
  && ok "AC2 no root is the wrapper's, the runner's, the leg's or its nested run's pid" \
  || { nope "AC2 the census counted an ancestor or descendant of the runner as foreign:$cn_bad"; sed 's/^/      /' "$d/census" 2>/dev/null; }
rec_done

# --- AC3 and AC6: a census that cannot see writes `unknown`, never `0`, and moves no verdict --------
rec_repo
rec_legs '[ {"name": "one", "argv": ["bash", "fx/a.sh"]}, {"name": "two", "argv": ["bash", "fx/a.sh"]} ]'
rc=$(rec_run GATE_FULL=1)
cn_v0=$(grep '^gates ' "$REC_OUT")
# AC6 rides this control run: the ledger block's read of a `.leg` row takes field 7 alone.
# Nine fields since TOOL-aFrugalTurnstile-4 S1 added run, full, manifest_blob and head after ended-at.
[ "$(grep -c . "$REC_GD/gate-ledger.tsv" 2>/dev/null)" = 2 ] && [ -z "$(awk -F'\t' 'NF != 9' "$REC_GD/gate-ledger.tsv" 2>/dev/null)" ] \
  && ok "AC6 every gate-ledger row stays nine fields, so no key absorbed the eighth" \
  || { nope "AC6 the ledger lost its nine-field shape"; cat -A "$REC_GD/gate-ledger.tsv" 2>/dev/null | sed 's/^/      /'; }
mkdir -p "$tmp/ps-fail" "$tmp/ps-nocol" "$tmp/ps-noself"
printf '#!/bin/sh\nexit 1\n' > "$tmp/ps-fail/ps"
printf '#!/bin/sh\necho "  UID  TTY  STIME COMMAND"\necho "  u    ?    10:00 bash fx/a.sh"\n' > "$tmp/ps-nocol/ps"
printf '#!/bin/sh\necho "  UID   PID  PPID  TTY  STIME COMMAND"\necho "  u       7     1  ?    10:00 bash fx/a.sh"\n' > "$tmp/ps-noself/ps"
chmod +x "$tmp/ps-fail/ps" "$tmp/ps-nocol/ps" "$tmp/ps-noself/ps"
for cn_s in fail nocol noself; do
  rc=$(rec_run GATE_FULL=1 PATH="$cn_pd/ps-$cn_s:$PATH")
  d=$(rec_dir)
  cn_rows=$(awk -F'\t' '{ print $8 }' "$d"/*.leg 2>/dev/null | sort -u | tr '\n' ' ')
  [ "$cn_rows" = "unknown " ] && [ "$(grep '^gates ' "$REC_OUT")" = "$cn_v0" ] \
    && ok "AC3 with a ps that $cn_s, every leg's foreign field reads unknown and the verdict is the stub-free one" \
    || { nope "AC3 with a ps that $cn_s the foreign fields read '$cn_rows' and the verdict '$(grep '^gates ' "$REC_OUT")' against '$cn_v0'"; sed 's/^/      /' "$d/census" 2>/dev/null; }
  if [ "$cn_s" = fail ]; then
    [ "$(cut -f2 "$d/census" 2>/dev/null | sort -u)" = unknown ] && [ "$(grep -c 'run-gates: NOTE.*census' "$REC_OUT")" = 1 ] \
      && ok "AC3 every census line reads unknown, and stderr carries one NOTE naming the census" \
      || { nope "AC3 the census lines or the NOTE are wrong under a failing ps"; sed 's/^/      /' "$d/census" "$REC_OUT" 2>/dev/null; }
  fi
done
rec_done

# --- AC4: the sampler is no live job and holds no caller's stdout ---------------------------------
# The WALL IS OFF: its own watcher holds a captured stdout for up to its 30 s poll, a defect that is
# not the census's, and with it off the census sampler is the only sleeper this bound can measure.
# Bounded, because a sampler counted by `live()` wedges a serial pool for good.
rec_repo
rec_legs '[ {"name": "one", "argv": ["bash", "fx/a.sh"]}, {"name": "two", "argv": ["bash", "fx/a.sh"]} ]'
cn_cap=$( cd "$REC_T" && env -u GATE_BASE -u GATE_REUSE -u GATE_PROFILES -u GATE_CENSUS_EVERY GATE_FULL=1 GATE_JOBS=1 GATE_WALL=0 \
            timeout -k 5s 240 bash $KIT_REL/run-gates.sh 2>&1 ); cn_back=$(date +%s)
cn_end=$(awk -F'\t' '$1 == "ended" { print $2 }' "$(rec_dir)/verdict" 2>/dev/null)
cn_ende=""; [ -n "$cn_end" ] && cn_ende=$(date -d "$cn_end" +%s 2>/dev/null)
if [ -z "$cn_end" ]; then
  nope "AC4 the runner wrote no verdict inside its 240 s bound — a sampler counted as a live job wedged the serial pool"
  printf '%s\n' "$cn_cap" | grep '^GATE\|^gates' | sed 's/^/      /'
elif [ -z "$cn_ende" ]; then
  skipped "AC4 this host's date cannot read the verdict's ended stamp '$cn_end', so the stdout hold went UNMEASURED"
else
  printf '%s\n' "$cn_cap" | grep -q '^GATE ok    one$' && printf '%s\n' "$cn_cap" | grep -q '^GATE ok    two$' \
    && [ $(( cn_back - cn_ende )) -le 30 ] \
    && ok "AC4 at GATE_JOBS=1 both legs report and the capture returns $(( cn_back - cn_ende ))s after the runner ended" \
    || { nope "AC4 the serial pool or the capture wedged: returned $(( cn_back - cn_ende ))s after the runner ended"; printf '%s\n' "$cn_cap" | grep '^GATE\|^gates' | sed 's/^/      /'; }
fi
rec_done

# --- AC5: load arriving mid-leg is sampled ---------------------------------------------------------
# THE OUTSIDE LOAD WAITS FOR A FACT, the leg's start marker, never a clock: the runner's startup here
# varies by seconds, so a clock could start it before the first sample and leave the loop ungraded.
rec_repo; write_load_fixture
rec_legs '[ {"name": "long", "argv": ["bash", "fx/load.sh", "15", ".git/cn-started"]} ]'
( cd "$REC_T" && i=0; while [ ! -f .git/cn-started ] && [ "$i" -lt 1200 ]; do sleep 0.1; i=$((i + 1)); done
  exec bash fx/load.sh 8 ) & cn_out=$!
rc=$(rec_run GATE_FULL=1 GATE_CENSUS_EVERY=2)
wait "$cn_out" 2>/dev/null
d=$(rec_dir); cn_lines=$(wc -l < "$d/census" 2>/dev/null | tr -d ' '); cn_f=$(read_foreign_field "$d/0.leg")
case "$cn_f" in ''|*[!0-9]*) cn_n=0 ;; *) cn_n=$cn_f ;; esac
[ "${cn_lines:-0}" -ge 4 ] && check_census_root "$d/census" "$cn_out:fx/load.sh" 2 && [ "$cn_n" -ge 1 ] \
  && ok "AC5 $cn_lines samples, a line after the first names the mid-leg load $cn_out, and the leg records foreign $cn_f" \
  || { nope "AC5 load arriving mid-leg was missed: $cn_lines samples, foreign '$cn_f'"; sed 's/^/      /' "$d/census" 2>/dev/null; }
rec_done

# --- AC11: the first sample precedes a sub-second first wave --------------------------------------
# Each leg looks for the census AS IT STARTS. The runner writes the first sample before it dispatches
# anything, so a correct runner can never fail this; one that left the first sample to the detached
# loop races its own legs. The race is made one a loaded host loses: `ps` takes two seconds here, as
# a loaded `ps -ef` has been measured to, so an asynchronous first sample lands after the legs ended.
# A census that can see prints no NOTE, which is the other half of keeping the first sample's NOTE
# in the runner's shell: a NOTE written from a file the loop has not filled yet would print always.
rec_repo
printf '%s\n' '#!/usr/bin/env bash' 'id=$(cat .git/gate-run/current 2>/dev/null)' \
  'if [ -s ".git/gate-run/$id/census" ]; then echo seen; else echo unseen; fi > ".git/cn-peek-$1"' 'exit 0' > "$REC_T/fx/peek.sh"
rec_legs '[ {"name": "one", "argv": ["bash", "fx/peek.sh", "one"]}, {"name": "two", "argv": ["bash", "fx/peek.sh", "two"]} ]'
cn_ps=$(command -v ps); mkdir -p "$tmp/ps-slow"
printf '#!/bin/sh\nsleep 2\nexec "%s" "$@"\n' "$cn_ps" > "$tmp/ps-slow/ps"; chmod +x "$tmp/ps-slow/ps"
rc=$(rec_run GATE_FULL=1 GATE_JOBS=2 PATH="$cn_pd/ps-slow:$PATH")
d=$(rec_dir); cn_first=$(awk -F'\t' 'NR == 1 { print $1 }' "$d/census" 2>/dev/null); cn_bad=""
for cn_p in one two; do
  [ "$(cat "$REC_GD/cn-peek-$cn_p" 2>/dev/null)" = seen ] || cn_bad="$cn_bad $cn_p:census-not-yet-written-at-start"
done
[ "$(grep -c 'run-gates: NOTE.*census' "$REC_OUT")" = 0 ] || cn_bad="$cn_bad a-census-NOTE-on-a-host-it-can-see"
for cn_l in "$d/0.leg" "$d/1.leg"; do
  cn_f=$(read_foreign_field "$cn_l"); cn_s=$(awk -F'\t' '{ print $5 }' "$cn_l" 2>/dev/null)
  case "$cn_f" in ''|*[!0-9]*) cn_bad="$cn_bad ${cn_l##*/}:foreign=$cn_f" ;; esac
  case "$cn_first$cn_s" in ''|*[!0-9]*) cn_bad="$cn_bad ${cn_l##*/}:unstamped" ;;
    *) [ "$cn_first" -le $(( cn_s / 1000000000 )) ] || cn_bad="$cn_bad ${cn_l##*/}:first-sample-after-start" ;; esac
done
[ -z "$cn_bad" ] \
  && ok "AC11 both first-wave legs found the census already written, carry a numeric foreign field, and start no earlier than its first stamp" \
  || { nope "AC11 a first-wave leg went uncensused:$cn_bad"; sed 's/^/      /' "$d/census" 2>/dev/null; }
rec_done

# --- AC12: a retried leg's row is eight fields, and a positive count outranks `unknown` -----------
# The fixture is the canary's contended pair: a leg that hangs while the spinner holds its flag and
# passes once it is gone, so its first attempt times out beside the spinner and its retry is green.
if command -v timeout >/dev/null 2>&1; then
  rec_repo
  export HV_FLAG="$tmp/cn-spinner"; rm -f "$HV_FLAG" "$HV_FLAG.done" "$HV_FLAG.hung"
  printf '#!/usr/bin/env bash\n: > "$HV_FLAG"\ni=0; while [ ! -f "$HV_FLAG.hung" ] && [ "$i" -lt 600 ]; do sleep 0.1; i=$((i + 1)); done\nsleep 3\nrm -f "$HV_FLAG"\n: > "$HV_FLAG.done"\n' > "$REC_T/fx/spin.sh"
  printf '#!/usr/bin/env bash\nwhile [ ! -f "$HV_FLAG" ] && [ ! -f "$HV_FLAG.done" ]; do sleep 0.1; done\nif [ -f "$HV_FLAG" ]; then : > "$HV_FLAG.hung"; sleep 60; fi\nexit 0\n' > "$REC_T/fx/contended.sh"
  rec_legs '[ {"name": "spinner", "argv": ["bash", "fx/spin.sh"]}, {"name": "contended", "argv": ["bash", "fx/contended.sh"], "ceiling": 2} ]'
  rc=$(rec_run GATE_FULL=1)
  d=$(rec_dir)
  if grep -q '^GATE ok    contended  (retried after timeout)$' "$REC_OUT"; then
    awk -F'\t' 'NF == 8 && ($8 == "unknown" || $8 ~ /^[0-9]+$/) { f = 1 } END { exit !f }' "$d/1.retry.leg" 2>/dev/null \
      && ok "AC12 the serial retry's row holds eight fields with a census verdict in the eighth" \
      || { nope "AC12 the retry row is not eight fields with a census verdict"; cat -A "$d/1.retry.leg" 2>/dev/null | sed 's/^/      /'; }
  else
    nope "AC12 control: the contended leg did not pass on its serial retry, so no retry row was graded"; grep '^GATE\|^gates' "$REC_OUT" | sed 's/^/      /'
  fi
  unset HV_FLAG
  rec_done
else
  skipped "AC12 no runnable timeout here, so no ceiling fires and the retry row went UNEXERCISED"
fi
# `derive_foreign`, SLICED out of the runner, over a census of one `unknown` and one `2` inside the
# window; the zeros-only and unknown-only controls are what stop a constant answer passing. The
# fourth census holds its one sample 15 s BEFORE the leg starts, inside the three-period reach at a
# 10 s period, which is the sample a short leg with no sample of its own depends on.
awk '/^derive_foreign\(\) \{/,/^}/' "$RUNNER" > "$tmp/cn-derive.sh"
cn_got=$( RUNDIR="$tmp/cn-rec"; CENSUS_EVERY=10; mkdir -p "$RUNDIR"; . "$tmp/cn-derive.sh"
  printf '1000\tunknown\t\n1010\t2\t7:fx/a.sh\n' > "$RUNDIR/census"; derive_foreign 1005000000000 1030000000000; printf '%s ' "$FOREIGN"
  printf '1000\t0\t\n1010\t0\t\n' > "$RUNDIR/census"; derive_foreign 1005000000000 1030000000000; printf '%s ' "$FOREIGN"
  printf '1000\tunknown\t\n1010\t0\t\n' > "$RUNDIR/census"; derive_foreign 1005000000000 1030000000000; printf '%s ' "$FOREIGN"
  printf '1000\t2\t7:fx/a.sh\n' > "$RUNDIR/census"; derive_foreign 1015000000000 1016000000000; printf '%s' "$FOREIGN" )
[ "$cn_got" = "2 0 unknown 2" ] \
  && ok "AC12 derive_foreign stamps 2 over an unknown and a 2, 0 over zeros, unknown over an unknown and a 0, and reaches back three periods" \
  || nope "AC12 derive_foreign read '$cn_got' for (unknown+2, zeros, unknown+0, a sample 15 s before the leg), want '2 0 unknown 2'"

# --- AC14: neither the turnstile ticker nor the census sampler outlives the bar --------------------
# The DEFAULT TTL on purpose: its ticker sleeps a sixth of it, so a ticker the exit does not stop is
# still alive when this looks. The snapshot is taken to a file first, so the pattern grep reads is
# not on the command line the snapshot lists.
rec_repo
rc=$(rec_run GATE_FULL=1 GATE_TURNSTILE=1 GATE_CENSUS_EVERY=60)
sleep 2
ps -ef > "$tmp/cn-ps.txt" 2>/dev/null
cn_left=$(grep -F -- "${REC_T##*/}/$KIT_REL/run-gates.sh" "$tmp/cn-ps.txt")
# THE CONTROL: the bar HELD the turnstile, so it started a ticker, and an absence below is a verdict.
cn_held=$(awk -F'\t' '$1 == "queued_from" { print $2 }' "$(rec_dir)/header" 2>/dev/null)
if [ ! -s "$tmp/cn-ps.txt" ]; then
  skipped "AC14 ps -ef printed nothing here, so a lingering ticker went UNSEEN"
elif [ "$cn_held" != held ]; then
  nope "AC14 control: the bar's turnstile reads '$cn_held', not held, so no ticker started and the absence below would grade nothing"
elif [ -z "$cn_left" ]; then
  ok "AC14 no process naming the finished bar's runner path remains (rc=$rc)"
else
  nope "AC14 the finished bar left processes the next bar's census would count as foreign:"; printf '%s\n' "$cn_left" | cut -c1-160 | sed 's/^/      /'
fi
rec_done

# --- S2's override refusal: a period that is not a positive integer is announced and not used -----
# AC5 shows a valid override is honoured (four samples in a 15 s leg cannot come from 60 s); this is
# the other branch, which no criterion reads: one NOTE naming the value, and the header keeping 60.
rec_repo
rc=$(rec_run GATE_FULL=1 GATE_CENSUS_EVERY=abc)
[ "$(grep -c "run-gates: NOTE - GATE_CENSUS_EVERY='abc'" "$REC_OUT")" = 1 ] \
  && [ "$(awk -F'\t' '$1 == "census_every" { print $2 }' "$(rec_dir)/header" 2>/dev/null)" = 60 ] \
  && ok "S2 a GATE_CENSUS_EVERY that is not a positive integer prints one NOTE and the run samples every 60 s" \
  || { nope "S2 an invalid GATE_CENSUS_EVERY was not announced once, or the header does not keep 60 (rc=$rc)"; grep 'NOTE' "$REC_OUT" | sed 's/^/      /'; }
rec_done
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
  mkdir -p "$RU_T/${PFX}${KIT}" "$RU_T/${PFX}${LIB}" "$RU_T/fx" "$RU_T/ga" "$RU_T/gb"
  cp "$ROOT/${PFX}${KIT}/run-gates.sh" "$ROOT/${PFX}${KIT}/gate-fingerprint.sh" \
     "$ROOT/${PFX}${KIT}/gate-profiles.txt" "$RU_T/${PFX}${KIT}/" || return 1
  cp "$ROOT/${LIB_DIR}/resolve-python.sh" "$RU_T/${PFX}${LIB}/" 2>/dev/null || true
  ( cd "$RU_T" && git init -q -b main . && git config user.email ru@test.invalid \
      && git config user.name ru-test ) >/dev/null 2>&1 || return 1
  printf '#!/usr/bin/env bash\necho a\nexit 0\n' > "$RU_T/fx/a.sh"
  printf '#!/usr/bin/env bash\necho b\nexit 0\n' > "$RU_T/fx/b.sh"
  echo x > "$RU_T/ga/f"; echo y > "$RU_T/gb/f"
  printf '%s\n' '[' \
    '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
    '  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]}' \
    ']' > "$RU_T/${PFX}gate-legs.json"
  ( cd "$RU_T" && git add -A && git commit -qm seed ) >/dev/null 2>&1 || return 1
  ( cd "$RU_T" && git remote add origin ../origin.git && git update-ref refs/remotes/origin/main HEAD \
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
  ']' > "$RU_T/${PFX}gate-legs.json"
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

# OPT-IN REUSE DEFEATS THE FULL-GREEN STAMP. This is the join the push boundary rests on: a stamp must
# never describe a run that copied a verdict no full run earned. The `lineage` mode, whose reuses a
# full run on a clean tree did earn, is the one exception, and its arms follow the profiler's below.
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
if [ -f "$ROOT/${PFX}${KIT}/profile_bar.py" ]; then
  ru_repo
  cp "$ROOT/${PFX}${KIT}/profile_bar.py" "$RU_T/${PFX}${KIT}/"
  ru_run GATE_FULL=1 >/dev/null
  ru_out=$( cd "$RU_T" && "$DC_PY" $KIT_REL/profile_bar.py --width 2 2>&1 )
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
# LINEAGE REUSE (TOOL-aFrugalTurnstile-4). `GATE_REUSE=lineage` reuses only a row that a FULL run on a
# CLEAN tree earned, on this manifest blob, at an ancestor of HEAD, and a run whose every reuse is of
# that kind may still stamp. The scratch is ru_repo's plus an unguarded leg `pu`, which writes the
# GATE_REUSE it sees into the git dir, and a `pb` that stays red until `gb/f` says fixed.
# EVERY REFUSAL ARM CARRIES ITS CONTROL ON THE SAME LEDGER: it is saved before the lineage run and put
# back before a GATE_REUSE=1 run, which must reuse `pa`. Without that, a key that never matched would
# pass the refusal arm as well as the lineage term it names.
build_lin_repo() {
  ru_repo || return 1
  printf '#!/usr/bin/env bash\ngrep -q fixed gb/f\n' > "$RU_T/fx/b.sh"
  printf '#!/usr/bin/env bash\nprintf "%%s" "${GATE_REUSE-unset}" > .git/reuse-leak\n' > "$RU_T/fx/u.sh"
  echo broken > "$RU_T/gb/f"
  printf '%s\n' '[' \
    '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
    '  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]},' \
    '  {"name": "pu", "argv": ["bash", "fx/u.sh"]}' \
    ']' > "$RU_T/${PFX}gate-legs.json"
  ( cd "$RU_T" && git add -A && git commit -qm lineage && git update-ref refs/remotes/origin/main HEAD ) >/dev/null 2>&1
}
write_lin_fix() { echo fixed > "$RU_T/gb/f"; ( cd "$RU_T" && git add -A && git commit -qm fix ) >/dev/null 2>&1; }
read_lin_header() { awk -F'\t' -v k="$1" '$1 == k { print $2 }' "$RU_GD/gate-run/$(cat "$RU_GD/gate-run/current" 2>/dev/null)/header" 2>/dev/null; }
read_lin_stamp() { awk -F'\t' '$1 == "reused" { print $2 }' "$RU_GD/gate-full-green" 2>/dev/null; }
check_lin_control() { # <AC label> — restore the saved ledger and prove GATE_REUSE=1 reuses pa from it
  cp "$tmp/ru.led" "$RU_GD/gate-ledger.tsv"; ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
  grep -q '^GATE reuse pa  ' "$REC_OUT" && ok "$1 control: the same ledger under GATE_REUSE=1 reuses pa, so the key matched" \
                                        || nope "$1 control: GATE_REUSE=1 did not reuse pa either, so the refusal above proves nothing"
}

# AC1, AC2, AC8 and AC6 share one scratch: the red full run, the fix, the lineage run, the opt-in run.
build_lin_repo || { echo "evidence-test: cannot build the lineage scratch"; exit 2; }
ru_run GATE_FULL=1 >/dev/null
ru_bad=$(awk -F'\t' -v r="$(read_lin_header run_id)" -v m="$(read_lin_header manifest_blob)" -v h="$(cd "$RU_T" && git rev-parse HEAD)" \
  'NF != 9 || $6 != r || $7 != "1" || $8 != m || $9 != h' "$RU_GD/gate-ledger.tsv" 2>/dev/null)
[ "$(grep -c . "$RU_GD/gate-ledger.tsv" 2>/dev/null)" = 3 ] && [ -n "$(read_lin_header run_id)" ] && [ -z "$ru_bad" ] \
  && ok "AC1 a full run on a clean tree writes nine-field rows naming its run, full 1, its manifest_blob and its head" \
  || { nope "AC1 the ledger rows do not carry the run, full, manifest_blob and head fields"; cat -A "$RU_GD/gate-ledger.tsv" 2>/dev/null | sed 's/^/      /'; }
write_lin_fix; rm -f "$RU_GD/gate-full-green"
ru_run GATE_FULL=1 GATE_REUSE=lineage >/dev/null
grep -q '^GATE reuse pa  ' "$REC_OUT" && grep -q '^GATE ok    pb$' "$REC_OUT" && grep -q '^GATE ok    pu$' "$REC_OUT" \
  && [ "$(read_lin_stamp)" = 1 ] \
  && ok "AC2 after a red full run and a fix, a lineage run reuses pa, runs pb and pu, and stamps reused 1" \
  || { nope "AC2 the lineage run after a fix did not reuse pa alone and stamp reused 1 (stamp '$(read_lin_stamp)')"; grep '^GATE ' "$REC_OUT" | sed 's/^/      /'; }
[ "$(cat "$RU_GD/reuse-leak" 2>/dev/null)" = unset ] && [ "$(read_lin_header reuse)" = lineage ] \
  && ok "AC8 a leg never inherits the reuse mode, and the header records reuse lineage" \
  || nope "AC8 the leg saw '$(cat "$RU_GD/reuse-leak" 2>/dev/null)' and the header reuse reads '$(read_lin_header reuse)'"
rm -f "$RU_GD/gate-full-green"
ru_run GATE_FULL=1 GATE_REUSE=1 >/dev/null
grep -q '^GATE reuse pa  ' "$REC_OUT" && [ ! -f "$RU_GD/gate-full-green" ] \
  && ok "AC6 over lineage-qualifying rows, GATE_REUSE=1 reuses and still writes no full green" \
  || nope "AC6 the opt-in run did not reuse pa, or it stamped a full green"
touch "$RU_T/untracked"; ru_run GATE_FULL=1 >/dev/null
[ "$(grep -c . "$RU_GD/gate-ledger.tsv" 2>/dev/null)" = 3 ] && [ -z "$(awk -F'\t' '$7 != ""' "$RU_GD/gate-ledger.tsv" 2>/dev/null)" ] \
  && ok "AC1 a full run over an untracked file writes every row with an empty full" \
  || nope "AC1 a dirty full run wrote a row with full set"
ru_done

# AC3: rows earned WITHOUT the full flag are not lineage-qualifying. The touch commit makes every leg
# execute on the earning run, so each one has a row.
build_lin_repo
echo x2 > "$RU_T/ga/f"; echo broken2 > "$RU_T/gb/f"; ( cd "$RU_T" && git add -A && git commit -qm touch ) >/dev/null 2>&1
ru_run >/dev/null; write_lin_fix; cp "$RU_GD/gate-ledger.tsv" "$tmp/ru.led"
ru_run GATE_FULL=1 GATE_REUSE=lineage >/dev/null
grep -q '^GATE reuse ' "$REC_OUT" && nope "AC3 lineage reused a row a run without the full flag earned" \
                                  || ok "AC3 lineage reuses nothing from rows with an empty full"
check_lin_control AC3
ru_done

# AC4: a row earned on another manifest blob.
build_lin_repo
ru_run GATE_FULL=1 >/dev/null; write_lin_fix
sed 's#"guard": \["gb/"\]},#"guard": ["gb/"]}, {"name": "pd", "argv": ["bash", "fx/a.sh"], "guard": ["gd/"]},#' \
  "$RU_T/${PFX}gate-legs.json" > "$tmp/ru.legs" && cp "$tmp/ru.legs" "$RU_T/${PFX}gate-legs.json"
( cd "$RU_T" && git add -A && git commit -qm leg4 ) >/dev/null 2>&1; cp "$RU_GD/gate-ledger.tsv" "$tmp/ru.led"
ru_run GATE_FULL=1 GATE_REUSE=lineage >/dev/null
grep -q '^GATE ok    pd$' "$REC_OUT" || nope "AC4 fixture: the fourth leg did not run, so the manifest did not move"
grep -q '^GATE reuse ' "$REC_OUT" && nope "AC4 lineage reused a row earned on another manifest blob" \
                                  || ok "AC4 lineage reuses nothing once the manifest blob moved"
check_lin_control AC4
ru_done

# AC5: a row whose head is a SIBLING of HEAD, with the same ga/ bytes and the same base.
build_lin_repo
ru_first=$(cd "$RU_T" && git rev-parse HEAD)
echo sib > "$RU_T/other"; ( cd "$RU_T" && git add -A && git commit -qm sibling ) >/dev/null 2>&1
ru_run GATE_FULL=1 >/dev/null
( cd "$RU_T" && git reset -q --hard "$ru_first" ) >/dev/null 2>&1; write_lin_fix; cp "$RU_GD/gate-ledger.tsv" "$tmp/ru.led"
ru_run GATE_FULL=1 GATE_REUSE=lineage >/dev/null
grep -q '^GATE reuse ' "$REC_OUT" && nope "AC5 lineage reused a row whose head is not an ancestor of HEAD" \
                                  || ok "AC5 lineage reuses nothing from a sibling's rows"
check_lin_control AC5
ru_done

# AC7: an impure leg runs under lineage, and the run still stamps over the two legs it reused.
build_lin_repo
sed 's#"guard": \["ga/"\]}#"guard": ["ga/"], "impure": "reads a remote"}#' "$RU_T/${PFX}gate-legs.json" > "$tmp/ru.legs" \
  && cp "$tmp/ru.legs" "$RU_T/${PFX}gate-legs.json"
( cd "$RU_T" && git add -A && git commit -qm impure && git update-ref refs/remotes/origin/main HEAD ) >/dev/null 2>&1
write_lin_fix; ru_run GATE_FULL=1 >/dev/null; rm -f "$RU_GD/gate-full-green"
ru_run GATE_FULL=1 GATE_REUSE=lineage >/dev/null
grep -q '^GATE ok    pa$' "$REC_OUT" && grep -q '^GATE reuse pb  ' "$REC_OUT" && grep -q '^GATE reuse pu  ' "$REC_OUT" \
  && [ "$(read_lin_stamp)" = 2 ] \
  && ok "AC7 lineage runs the impure pa, reuses pb and pu, and stamps reused 2" \
  || { nope "AC7 lineage over an impure leg did not run it and stamp reused 2 (stamp '$(read_lin_stamp)')"; grep '^GATE ' "$REC_OUT" | sed 's/^/      /'; }
ru_done
rm -f "$tmp/ru.led" "$tmp/ru.legs"

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
mkdir -p "$DC_T/${PFX}${KIT}"
cp "$ROOT/${PFX}${KIT}/derive-ceilings.py" "$ROOT/${PFX}${KIT}/ceiling-margin.txt" \
   "$DC_T/${PFX}${KIT}/" || { echo "evidence-test: cannot copy the ceiling kit"; exit 2; }
( cd "$DC_T" && git init -q -b main . ) >/dev/null 2>&1 \
  || { echo "evidence-test: cannot init the ceiling fixture repo"; exit 2; }
DC_SCRIPT="$DC_T/${PFX}${KIT}/derive-ceilings.py"
DC_EV="$DC_T/${PFX}${KIT}/ceiling-evidence.txt"
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
  ']' > "$DC_T/${PFX}gate-legs.json"
mkdir -p "$DC_T/.git/gate-run/r1"
# EVERY RUN ROW IN THIS FIXTURE CARRIES AN EIGHTH FIELD OF `0`, the census's faithful value
# (TOOL-aGraftedHelix-5). A seven-field row is `uncensused` and set aside, so without it every arm
# below would grade the census rather than the rule it names.
{ printf 'at-ceiling\tfail\t124\t100.4\t0\t0\t-\t0\n'
  printf 'below-ceiling\tfail\t1\t40.0\t0\t0\t-\t0\n'
  printf 'way-over\tfail\t137\t400.0\t0\t0\t-\t0\n'
  printf 'kill-overhead\tfail\t124\t12.0\t0\t0\t-\t0\n'; } > "$DC_T/.git/gate-run/r1/1.leg"

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
printf 'at-ceiling\tok\t0\t20.0\t0\t0\t-\t0\n' >> "$DC_T/.git/gate-run/r1/1.leg"
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
dc_ac_later=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
# ITS OWN CONTROL, because the arm below grades an ABSENCE and an absence is what an empty file, a
# failed write and a working drop all look like. The untouched leg proves this write produced rows.
[ -n "$dc_ac_later" ] \
  && ok "control: the untouched leg still reads $dc_ac_later after that write, so the absence graded below is a verdict and not an empty file" \
  || nope "no row at all survived the write before the drop-lifetime arm, so that arm would pass by finding nothing"
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
printf 'at-ceiling\tfail\t124\t100.4\t0\t0\t-\t0\n' > "$DC_T/.git/gate-run/r1/1.leg"
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

# --- A READING TAKEN OUTSIDE THE RUNNER (TOOL-cMendedVintage-17) -----------------------------------
# The circularity the flag breaks: a ceiling is raised from the evidence of a COMPLETED run, a leg
# killed at its ceiling completes none, and its killed reading enters the monotone file AT that
# ceiling — so the declared mechanism cannot reach exactly the legs whose bounds fire. Two healthy
# legs were raised by hand from quiet re-runs during the build that filed this row, and the hand-edit
# is what these arms grade the replacement of.
#
# THE RUN RECORD IS EMPTY HERE, left that way by the DEAD-PROBE control above, and that is the
# fixture rather than an accident: the state this flag exists for is one where nothing admissible
# was recorded for the leg being raised, and an implementation whose liveness return fires above the
# flag refuses the only case it was built for. That return has already been repaired once for this
# exact shape one section up.
dc_obs=$(GOV_NODE=z "$DC_PY" "$DC_SCRIPT" --write --observed 'at-ceiling=853' \
           --how 'quiet re-run, nothing else on the box' 2>&1); dc_obs_rc=$?
dc_obs_row=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
if [ "$dc_obs_rc" = 0 ] && awk -v v="$dc_obs_row" 'BEGIN{exit !(v != "" && v+0 == 853)}'; then
  ok "--write --observed admits a reading taken outside the runner with the run record EMPTY ($dc_obs_row), which is the state a leg killed at its ceiling is in"
else
  nope "--write --observed exited $dc_obs_rc leaving the row at '$dc_obs_row' — the out-of-band reading was refused in the one state it exists for"
  printf '%s\n' "$dc_obs" | sed 's/^/      /'
fi
# DISTINGUISHABLE OR IT IS WORTHLESS. An out-of-band number that reads like an in-band one is how a
# ceiling becomes a number nobody chose, which is the failure the margin file's header already names.
# Both halves the ruling requires are graded here: the NODE it was taken on and HOW it was taken.
awk -F'\t' '$1=="at-ceiling" && $4=="z" && $6=="quiet re-run, nothing else on the box" {f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "the out-of-band row carries the node it was taken on and the operator's account of how, in the artifact itself" \
  || { nope "the out-of-band row does not carry its node and conditions — the reading is indistinguishable from one the runner produced"; sed 's/^/      /' "$DC_EV" 2>/dev/null; }
# THE CONTROL, and the arm above is a claim about nothing without it: a source column that said the
# same thing on every row would satisfy that grep and tell two kinds of reading apart for nobody.
printf 'below-ceiling\tok\t0\t30.0\t0\t0\t-\t0\n' > "$DC_T/.git/gate-run/r1/1.leg"
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
awk -F'\t' '$1=="below-ceiling" && $6=="runner" {f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "control: a row this tool derived from the run record spells a different source, so the column separates the two kinds" \
  || { nope "a runner-derived row does not spell its own source — the column cannot tell the two kinds apart"; sed 's/^/      /' "$DC_EV" 2>/dev/null; }
# AND IT SURVIVES AN ORDINARY WRITE, provenance included. A source that reverted to the runner's on
# the next refresh would relabel a typed number as an observed one, silently, one command later.
awk -F'\t' '$1=="at-ceiling" && $2=="853.0" && $6=="quiet re-run, nothing else on the box" {f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "the out-of-band row and its stated provenance SURVIVE an ordinary --write that measured nothing for that leg" \
  || { nope "an ordinary --write lost the out-of-band row or relabelled its source — a typed number would be read as an observed one"; sed 's/^/      /' "$DC_EV" 2>/dev/null; }
# AND AGAIN WITH THE KILLED READING BACK IN THE WINDOW, which is a DIFFERENT code path and the only
# one the real case takes. Above, the leg had no retained reading at all and its row was carried by
# the carry-forward for legs this run measured nothing for. A leg raised out-of-band because its
# bound fired still HAS its killed reading in the retention window — that is what put the row there
# — so the row is carried by the monotone hold instead, which is where a rebuilt tuple can quietly
# relabel a typed number as a runner's. Staging exactly that relabel left every arm here green until
# this fixture line existed, which is the could-not-fail shape one level up.
printf 'at-ceiling\tfail\t124\t100.4\t0\t0\t-\t0\n' >> "$DC_T/.git/gate-run/r1/1.leg"
"$DC_PY" "$DC_SCRIPT" --write >/dev/null 2>&1
awk -F'\t' '$1=="at-ceiling" && $2=="853.0" && $6=="quiet re-run, nothing else on the box" {f=1} END{exit !f}' "$DC_EV" 2>/dev/null \
  && ok "the out-of-band row outranks the leg's own killed reading and keeps its source through the monotone hold" \
  || { nope "the killed reading displaced the out-of-band row or relabelled its source — the ceiling is held above the bound that fired again"; sed 's/^/      /' "$DC_EV" 2>/dev/null; }
# A READING THAT RAISES NOTHING IS REFUSED, not absorbed. The file is monotone, so admitting a lower
# number writes a fresh row and moves no value — the operator's gesture answered by a report of work
# that did not happen, which is the shape this whole artifact is arranged against.
dc_lo=$(GOV_NODE=z "$DC_PY" "$DC_SCRIPT" --write --observed 'at-ceiling=100' --how 'quiet' 2>&1); dc_lo_rc=$?
dc_lo_row=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
if [ "$dc_lo_rc" != 0 ] && awk -v v="$dc_lo_row" 'BEGIN{exit !(v+0 == 853)}'; then
  ok "an --observed reading at or under the recorded maximum is REFUSED and writes nothing (row still $dc_lo_row)"
else
  nope "a non-raising --observed reading exited $dc_lo_rc leaving the row at '$dc_lo_row' — a silent no-op reported as a write"
fi
# EVERY MISSING HALF OF THE CLAIM IS A REFUSAL. A reading with no stated conditions, one naming a leg
# that does not exist, and one whose node was defaulted rather than stated are all the hand-edit this
# flag replaces wearing a command's clothes; the fourth is the gesture made on a read-only verb,
# where accepting the ordinary output back would read as acceptance of a reading stored nowhere.
dc_ref_i=0
while [ "$dc_ref_i" -lt 4 ]; do
  case "$dc_ref_i" in
    0) dc_ref_out=$(GOV_NODE=z "$DC_PY" "$DC_SCRIPT" --write --observed 'at-ceiling=9999' 2>&1)
       dc_ref_rc=$?; dc_ref_what="a reading with no --how account of the conditions" ;;
    1) dc_ref_out=$(GOV_NODE=z "$DC_PY" "$DC_SCRIPT" --write --observed 'no-such-leg=9999' --how 'quiet' 2>&1)
       dc_ref_rc=$?; dc_ref_what="a reading for a leg the manifest does not carry" ;;
    2) dc_ref_out=$(GOV_NODE="" "$DC_PY" "$DC_SCRIPT" --write --observed 'at-ceiling=9999' --how 'quiet' 2>&1)
       dc_ref_rc=$?; dc_ref_what="a reading whose node would have to be defaulted" ;;
    # `--report` RATHER THAN `--check`, and the choice is the difference between an arm and a
    # decoration: this fixture's ceilings fail, so `--check` exits non-zero with the guard gone as
    # readily as with it there, and the arm would pass over a deleted refusal. `--report` exits 0
    # on the same fixture, so only the refusal can make this case non-zero.
    3) dc_ref_out=$(GOV_NODE=z "$DC_PY" "$DC_SCRIPT" --report --observed 'at-ceiling=9999' --how 'quiet' 2>&1)
       dc_ref_rc=$?; dc_ref_what="a reading handed to a read-only verb" ;;
  esac
  dc_ref_row=$(awk -F'\t' '$1=="at-ceiling"{print $2}' "$DC_EV" 2>/dev/null)
  if [ "$dc_ref_rc" != 0 ] && awk -v v="$dc_ref_row" 'BEGIN{exit !(v+0 == 853)}'; then
    ok "REFUSED: $dc_ref_what (rc=$dc_ref_rc, row untouched at $dc_ref_row)"
  else
    nope "$dc_ref_what exited $dc_ref_rc and left the row at '$dc_ref_row' — it was admitted, or admitted quietly"
    printf '%s\n' "$dc_ref_out" | sed 's/^/      /'
  fi
  dc_ref_i=$((dc_ref_i+1))
done
# THE SECOND HALF OF THE RULING. `--check` called an unbacked ceiling REPORTED-and-not-a-failure, so
# a never-measured bound and a trusted one read the same to anyone scanning the output. UNBACKED is
# left alone — a leg that has never run still has nothing to be measured against, and a way to type a
# reading in does not change that. What changed is the word "backed", which now covers a duration
# this tool watched the runner produce AND one an operator measured elsewhere. The second kind is
# named, with the node and the conditions it was taken under.
dc_chk=$("$DC_PY" "$DC_SCRIPT" --check 2>&1)
printf '%s\n' "$dc_chk" | grep -q 'OUTSIDE the' \
  && printf '%s\n' "$dc_chk" | grep 'OUTSIDE the' | grep -q 'at-ceiling' \
  && printf '%s\n' "$dc_chk" | grep 'OUTSIDE the' | grep -q 'quiet re-run, nothing else on the box' \
  && ok "--check names the out-of-band-backed leg with its node and stated conditions, rather than counting it as backed and saying nothing" \
  || { nope "--check does not separate an out-of-band-backed ceiling from one the runner measured"; printf '%s\n' "$dc_chk" | sed 's/^/      /'; }
printf '%s\n' "$dc_chk" | grep 'OUTSIDE the' | grep -q 'below-ceiling' \
  && nope "--check named a runner-derived leg on its out-of-band line — the line reports every backed leg and separates nothing" \
  || ok "control: the runner-derived leg is absent from that line, so naming above is a verdict and not a roll-call"
# THE REACHED SENTENCE IS A CLAIM ABOUT PROVENANCE, and it is false over an out-of-band row. It says
# the reading is a LOWER BOUND on the work and that no new ceiling may be sized from it, which holds
# of a duration `timeout` cut short and of nothing else. Said over a quiet measurement an operator
# took to completion, it withdraws the invitation in the exact case this flag exists to extend it.
# The failing verdict is unchanged either way — the ceiling is under the evidenced maximum — so what
# is graded here is which sentence the operator is handed, and whether it carries the floor.
dc_reach=$(printf '%s\n' "$dc_chk" | grep 'at-ceiling' | grep 'REACHED')
[ -z "$dc_reach" ] \
  && ok "an out-of-band reading above its ceiling is NOT called a reached bound, because nothing killed it" \
  || { nope "an out-of-band reading is reported as a reached ceiling and a lower bound on the work — the operator is told not to size a ceiling from the one reading this flag exists to let them size one from"; printf '%s\n' "$dc_reach" | sed 's/^/      /'; }
printf '%s\n' "$dc_chk" | grep 'at-ceiling' | grep -q 'does not clear its evidenced maximum' \
  && ok "it gets the headroom sentence instead, which states the floor such a ceiling has to clear" \
  || { nope "an out-of-band reading above its ceiling produced neither sentence — the row fails with no target to raise the ceiling to"; printf '%s\n' "$dc_chk" | sed 's/^/      /'; }
rm -rf "$DC_T"

# --- ONLY A CENSUSED-CLEAN READING ARGUES A CEILING (TOOL-aGraftedHelix-5) -------------------------
# A fixture of its own, for the reason the one above gives: `--write` writes beside the script. One
# run holds four `ok` readings of L, one per census state — 10 s at foreign 0, 50 s at 2, 60 s at
# `unknown`, 70 s as a seven-field row — and one of M at foreign 1, so every count below is PINNED.
CN_T=$(mktemp -d)
mkdir -p "$CN_T/${PFX}${KIT}" "$CN_T/.git/gate-run/r1"
cp "$ROOT/${PFX}${KIT}/derive-ceilings.py" "$ROOT/${PFX}${KIT}/ceiling-margin.txt" "$CN_T/${PFX}${KIT}/" \
  || { echo "evidence-test: cannot copy the ceiling kit for the census arms"; exit 2; }
( cd "$CN_T" && git init -q -b main . ) >/dev/null 2>&1
CN_SCRIPT="$CN_T/${PFX}${KIT}/derive-ceilings.py"; CN_EV="$CN_T/${PFX}${KIT}/ceiling-evidence.txt"
printf '%s\n' '[' '  {"name": "L", "argv": ["true"], "ceiling": 100},' '  {"name": "M", "argv": ["true"], "ceiling": 100}' ']' \
  > "$CN_T/${PFX}gate-legs.json"
{ printf 'L\tok\t0\t10.0\t0\t0\t-\t0\n'
  printf 'L\tok\t0\t50.0\t0\t0\t-\t2\n'
  printf 'L\tok\t0\t60.0\t0\t0\t-\tunknown\n'
  printf 'L\tok\t0\t70.0\t0\t0\t-\n'
  printf 'M\tok\t0\t30.0\t0\t0\t-\t1\n'; } > "$CN_T/.git/gate-run/r1/1.leg"
cn_rep=$( cd "$CN_T" && "$DC_PY" "$CN_SCRIPT" --report 2>&1 )
# AC7. The `aside` column is LAST, so a reason a later unit inserts leaves it where it is read.
printf '%s\n' "$cn_rep" | awk -F'\t' '$1 == "L" && $2 == "10.0" && $3 == "1" && $NF == "3" { f = 1 } END { exit !f }' \
  && ok "AC7 L argues from its one faithful reading, max 10.0, with 3 readings set aside" \
  || { nope "AC7 L's row admits a contended or uncensused reading"; printf '%s\n' "$cn_rep" | sed 's/^/      /'; }
# The two counts asserted APART, so a reason inserted between them leaves this arm standing.
cn_set=$(printf '%s\n' "$cn_rep" | grep '^# set aside:')
printf '%s' "$cn_set" | grep -q '[^0-9]2 contended' && printf '%s' "$cn_set" | grep -q '[^0-9]2 uncensused' \
  && ok "AC7 the set-aside line names 2 contended and 2 uncensused" \
  || { nope "AC7 the set-aside line reads '$cn_set'"; printf '%s\n' "$cn_rep" | sed 's/^/      /'; }
printf '%s\n' "$cn_rep" | grep 'SET ASIDE' | grep -qw M && ! printf '%s\n' "$cn_rep" | grep 'UNBACKED' | grep -qw M \
  && ok "AC7 M, every reading set aside, is named on its own line and not as UNBACKED" \
  || { nope "AC7 M is reported as UNBACKED, or not at all"; printf '%s\n' "$cn_rep" | sed 's/^/      /'; }
# AC8. A set-aside reading moves no row, and the summary line counts it.
printf '# hdr\nL\t40.0\t1\ta\t2026-09-10\trunner\nM\t25.0\t1\ta\t2026-09-10\trunner\n' > "$CN_EV"
cn_w=$( cd "$CN_T" && "$DC_PY" "$CN_SCRIPT" --write 2>&1 )
awk -F'\t' '$1 == "L" && $2 == "40.0" { f = 1 } END { exit !f }' "$CN_EV" 2>/dev/null \
  && printf '%s' "$cn_w" | grep -q '[^0-9]2 contended' && printf '%s' "$cn_w" | grep -q '[^0-9]2 uncensused' \
  && ok "AC8 L's row holds at 40.0 and the summary names 2 contended and 2 uncensused" \
  || { nope "AC8 a set-aside reading moved L's row, or the summary does not count them"; printf '%s\n' "$cn_w" | sed 's/^/      /'; sed 's/^/      /' "$CN_EV"; }
# AC9 reads the header that write rendered: the tracked artifact's must be the same bytes.
[ "$(grep '^#' "$CN_EV")" = "$(grep '^#' "$ROOT/${PFX}${KIT}/ceiling-evidence.txt")" ] \
  && ok "AC9 the tracked evidence file carries the header --write renders" \
  || nope "AC9 the tracked ceiling-evidence.txt header differs from the one --write renders — re-render it"
awk '/^## The run record/ { s = 1; next } /^## / { s = 0 } s && /foreign/ && /key · foreign/ { f = 1 } END { exit !f }' "$ROOT/${PFX}${KIT}/README.md" \
  && ok "AC9 the README's run-record section lists the eighth field, foreign" \
  || nope "AC9 the README's run-record section does not list foreign among the .leg fields"
printf 'M\tok\t0\t30.0\t0\t0\t-\t1\n' > "$CN_T/.git/gate-run/r1/1.leg"
cn_rows=$(grep -v '^#' "$CN_EV"); cn_w=$( cd "$CN_T" && "$DC_PY" "$CN_SCRIPT" --write 2>&1 ); cn_rc=$?
[ "$cn_rc" = 0 ] && ! printf '%s' "$cn_w" | grep -q 'DEAD PROBE' && [ "$(grep -v '^#' "$CN_EV")" = "$cn_rows" ] \
  && ok "AC8 with every reading set aside --write exits 0, says no DEAD PROBE, and holds every row" \
  || { nope "AC8 a record of set-aside readings read as DEAD PROBE or moved a row (rc=$cn_rc)"; printf '%s\n' "$cn_w" | sed 's/^/      /'; }
# AC13. The manual route stays admitted, and the header it renders says it is uncensused.
cn_w=$( cd "$CN_T" && GOV_NODE=z "$DC_PY" "$CN_SCRIPT" --write --observed 'L=55' --how 'quiet host, no other session' 2>&1 ); cn_rc=$?
[ "$cn_rc" = 0 ] && awk -F'\t' '$1 == "L" && $2 == "55.0" && $6 == "quiet host, no other session" { f = 1 } END { exit !f }' "$CN_EV" 2>/dev/null \
  && grep '^#' "$CN_EV" | grep -q 'admitted uncensused' \
  && ok "AC13 --observed still writes L from its reading, and the rendered header says that route is admitted uncensused" \
  || { nope "AC13 the manual route was refused, or no header line says it is uncensused (rc=$cn_rc)"; printf '%s\n' "$cn_w" | sed 's/^/      /'; }
awk '/^## Every leg may declare a `ceiling`/ { s = 1; next } /^## / { s = 0 } s && /TOOL-cMendedVintage-17/ && /uncensused/ { f = 1 } END { exit !f }' "$ROOT/${PFX}${KIT}/README.md" \
  && ok "AC13 the README's ceiling section names the --observed route uncensused under TOOL-cMendedVintage-17" \
  || nope "AC13 the README's ceiling section does not say the --observed route is uncensused"
# THE LIVENESS CONTROL: a record holding no reading at all is still a DEAD PROBE.
rm -f "$CN_T/.git/gate-run/r1/1.leg"
cn_w=$( cd "$CN_T" && "$DC_PY" "$CN_SCRIPT" --write 2>&1 ); cn_rc=$?
[ "$cn_rc" = 2 ] && printf '%s' "$cn_w" | grep -q 'DEAD PROBE' \
  && ok "AC8 control: a record holding no reading still exits 2 with DEAD PROBE" \
  || nope "AC8 control: an empty record no longer reports DEAD PROBE (rc=$cn_rc)"
rm -rf "$CN_T"

# --- A READING TAKEN DURING A MEMORY PAUSE ARGUES NO CEILING (TOOL-aGraftedHelix-7 AC10) -----------
# One run, one `pauses` episode from epoch 1000 to 1010, and three `ok` readings of L at foreign 0:
# 10 s from 995 to 1005 (inside the episode), 20 s from 1020 to 1040 (after it), 30 s from 970 to 1000
# (it TOUCHES the episode's start, which is the instant a held leg dispatched). Every count PINNED.
PZ_T=$(mktemp -d)
mkdir -p "$PZ_T/${PFX}${KIT}" "$PZ_T/.git/gate-run/r1"
cp "$ROOT/${PFX}${KIT}/derive-ceilings.py" "$ROOT/${PFX}${KIT}/ceiling-margin.txt" "$PZ_T/${PFX}${KIT}/" \
  || { echo "evidence-test: cannot copy the ceiling kit for the pause arms"; exit 2; }
( cd "$PZ_T" && git init -q -b main . ) >/dev/null 2>&1
printf '%s\n' '[' '  {"name": "L", "argv": ["true"], "ceiling": 300}' ']' > "$PZ_T/${PFX}gate-legs.json"
printf '1000\t1010\t10\t95\t90\tfell\n' > "$PZ_T/.git/gate-run/r1/pauses"
{ printf 'L\tok\t0\t10.0\t995000000000\t1005000000000\t-\t0\n'
  printf 'L\tok\t0\t20.0\t1020000000000\t1040000000000\t-\t0\n'
  printf 'L\tok\t0\t30.0\t970000000000\t1000000000000\t-\t0\n'; } > "$PZ_T/.git/gate-run/r1/1.leg"
pz_rep=$( cd "$PZ_T" && "$DC_PY" "$PZ_T/${PFX}${KIT}/derive-ceilings.py" --report 2>&1 )
printf '%s\n' "$pz_rep" | awk -F'\t' '$1 == "L" && $2 == "30.0" && $3 == "2" && $NF == "1" { f = 1 } END { exit !f }' \
  && ok "AC10 L reads a max of 30.0 from 2 readings with 1 set aside: the overlapping one, not the one touching the edge" \
  || { nope "AC10 L's row admits the reading taken during the pause, or sets aside the one touching its start"; printf '%s\n' "$pz_rep" | sed 's/^/      /'; }
printf '%s\n' "$pz_rep" | grep '^# set aside:' | grep -q '[^0-9]1 paused' \
  && ok "AC10 the set-aside line names 1 paused" \
  || { nope "AC10 the set-aside line does not name 1 paused"; printf '%s\n' "$pz_rep" | sed 's/^/      /'; }
rm -rf "$PZ_T"

# --- THE POST-MERGE BAR (TOOL-aFrugalTurnstile-6 AC1-AC10) -----------------------------------------
# A bare remote and a clone carrying this kit's runner, its post-merge script and a one-leg manifest
# whose leg reads `verdict.txt`. c1 is green, c2 red, c3 green, each a child of the one before, all
# landed. Remotes are named through variables; the turnstile is this suite's own, exported above.
# >>> post-merge arms
PM_T=$(mktemp -d); PM_B="$PM_T/b.git"; PM_B2="$PM_T/b2.git"; PM_C="$PM_T/c"; PM_K="${PFX}${KIT}"
PM_R=up; PM_R2=second; PM_OUT="$PM_T/out"; PM_PROBE="$PM_T/probe"; PM_REF=refs/gov/bar-red
mkdir -p "$PM_C/$PM_K"
cp "$ROOT/$PM_K/run-gates.sh" "$ROOT/$PM_K/gate-fingerprint.sh" "$ROOT/$PM_K/gate-profiles.txt" \
   "$ROOT/$PM_K/lib-attribute.sh" "$ROOT/$PM_K/post-merge.sh" "$PM_C/$PM_K/" \
  || { echo "evidence-test: cannot copy the kit for the post-merge arms"; exit 2; }
git init -q --bare -b main "$PM_B" && git init -q --bare -b main "$PM_B2" \
  || { echo "evidence-test: cannot make the post-merge remotes"; exit 2; }
# `core.autocrlf false`: the scratch worktree is a fresh CHECKOUT, and a host-wide autocrlf would hand
# the bar CRLF scripts the fixture never wrote (measured on node a: every bar red on a `\r`).
( cd "$PM_C" && git init -q -b main . && git config user.email pm@test.invalid && git config user.name pm-test \
    && git config core.autocrlf false && git remote add "$PM_R" "$PM_B" ) >/dev/null 2>&1 \
  || { echo "evidence-test: cannot make the post-merge clone"; exit 2; }
printf '%s\n' '[' '  {"name": "verdict", "argv": ["bash", "-c", "cat verdict.txt; grep -qx green verdict.txt"]}' ']' \
  > "$PM_C/${PFX}gate-legs.json"
printf '#!/usr/bin/env bash\n{ env; git rev-parse HEAD; pwd; } > "$PM_PROBE"\n' > "$PM_C/bar.sh"
pm_commit() { # verdict word · [gate-env text, printf-interpreted] -> prints the new sha, landed on main
  printf '%s\n' "$1" > "$PM_C/verdict.txt"
  mkdir -p "$PM_C/.githooks"
  if [ -n "${2:-}" ]; then printf "$2" > "$PM_C/.githooks/gate-env.sh"; else rm -f "$PM_C/.githooks/gate-env.sh"; fi
  ( cd "$PM_C" && git add -A && git commit -qm "$1" && git push -q "$PM_R" HEAD:main \
      && git symbolic-ref "refs/remotes/$PM_R/HEAD" "refs/remotes/$PM_R/main" && git rev-parse HEAD ) 2>/dev/null
}
pm_run() { ( cd "$PM_C" && env -u GATE_FULL -u GATE_JOBS -u GATE_PROFILES -u GOV_REMOTE PM_PROBE="$PM_PROBE" ${PM_X:-} \
               bash "$PM_K/post-merge.sh" "$@" >"$PM_OUT" 2>&1; echo $? ); }
pm_key() { awk -F'\t' -v k="$2" '$1 == k { print $2; exit }' "$1" 2>/dev/null; }
pm_red() { git ls-remote "${1:-$PM_B}" "$PM_REF" 2>/dev/null | cut -f1; }
pm_show() { sed 's/^/      /' "$PM_OUT"; }
PM_GD="$PM_C/.git"; PM_REC="$PM_GD/gate-post-merge"
pm_c1=$(pm_commit green); pm_c2=$(pm_commit red); pm_c3=$(pm_commit green)
[ -n "$pm_c1" ] && [ -n "$pm_c2" ] && [ -n "$pm_c3" ] || { echo "evidence-test: cannot land the post-merge commits"; exit 2; }

# AC1 — a red landing publishes the ref, records RED pushed, and its run record survives the worktree.
pm_rc=$(pm_run "$pm_c2"); pm_id=$(pm_key "$PM_REC" run_id)
[ "$pm_rc" = 1 ] && [ "$(pm_red)" = "$pm_c2" ] && [ "$(pm_key "$PM_REC" verdict)" = RED ] && [ "$(pm_key "$PM_REC" published)" = pushed ] \
  && ok "AC1 a red post-merge exits 1, refs/gov/bar-red names c2, and gate-post-merge reads verdict RED, published pushed" \
  || { nope "AC1 a red post-merge did not publish (rc=$pm_rc, ref=$(pm_red))"; pm_show; }
[ -n "$pm_id" ] && grep -rqx red "$PM_GD/gate-run/$pm_id" 2>/dev/null && ! git -C "$PM_C" worktree list | grep -q 'gate-pm\.' \
  && ok "AC1 gate-run/<run_id>/ in the common dir holds the failing leg's output after the scratch worktree is gone" \
  || { nope "AC1 the run record went with the worktree, or the worktree survived (id=$pm_id)"; git -C "$PM_C" worktree list | sed 's/^/      /'; }

# AC2 — a green descendant clears it and writes D3's record, by post-merge.
pm_rc=$(pm_run "$pm_c3"); git ls-remote --exit-code "$PM_B" "$PM_REF" >/dev/null 2>&1; pm_lr=$?
[ "$pm_rc" = 0 ] && [ "$pm_lr" = 2 ] \
  && ok "AC2 a green descendant exits 0 and git ls-remote --exit-code of refs/gov/bar-red exits 2" \
  || { nope "AC2 the green did not clear the ref (rc=$pm_rc, ls-remote rc=$pm_lr)"; pm_show; }
PM_BG="$PM_GD/gate-bar-green.shared"
[ "$(cut -f1 "$PM_BG" 2>/dev/null | tr '\n' ' ')" = "sha tree bar bar_paths kind base selftests run_id by stamped " ] \
  && [ "$(pm_key "$PM_BG" kind)" = full ] && [ "$(pm_key "$PM_BG" by)" = post-merge ] && [ "$(pm_key "$PM_BG" sha)" = "$pm_c3" ] \
  && [ "$(pm_key "$PM_BG" bar)" = "bash $PM_K/run-gates.sh" ] \
  && ok "AC2 gate-bar-green.shared carries exactly D3's keys, kind full, by post-merge, and the default bar string" \
  || { nope "AC2 gate-bar-green.shared differs from D3's grammar"; sed 's/^/      /' "$PM_BG" 2>/dev/null; }
[ -f "$PM_GD/gate-full-green.shared" ] && ! git -C "$PM_C" worktree list | grep -q 'gate-pm\.' \
  && ok "AC2 the runner's gate-full-green.shared is present and no gate-pm. worktree is left" \
  || nope "AC2 gate-full-green.shared is absent, or a gate-pm. worktree survived"

# AC3 — a green that does not descend from the red keeps it.
git -C "$PM_C" push -q "$PM_R" "$pm_c2:$PM_REF" 2>/dev/null
pm_rc=$(pm_run "$pm_c1")
[ "$pm_rc" = 0 ] && [ "$(pm_red)" = "$pm_c2" ] && [ "$(pm_key "$PM_REC" published)" = kept ] \
  && ok "AC3 a green on c2's parent exits 0, the ref still names c2, and the record reads published kept" \
  || { nope "AC3 a non-descendant green moved the ref (rc=$pm_rc, ref=$(pm_red))"; pm_show; }

# AC4 — a red never moves the ref backwards.
git -C "$PM_C" push -q -f "$PM_R" "$pm_c3:$PM_REF" 2>/dev/null
pm_rc=$(pm_run "$pm_c2")
[ "$pm_rc" = 1 ] && [ "$(pm_red)" = "$pm_c3" ] && [ "$(pm_key "$PM_REC" published)" = kept ] \
  && ok "AC4 a red on c2 with the ref at c3 exits 1, keeps c3, and reads published kept" \
  || { nope "AC4 the ref moved backwards (rc=$pm_rc, ref=$(pm_red))"; pm_show; }
git -C "$PM_C" push -q "$PM_R" ":$PM_REF" 2>/dev/null

# AC5 — a declared bar runs inside the hold verb, full, in the scratch worktree, with no reuse.
pm_c4=$(pm_commit green 'GOV_GATE_CMD="bash bar.sh"\n'); rm -f "$PM_PROBE"
pm_rc=$(PM_X="GATE_REUSE=lineage" pm_run "$pm_c4")
[ "$pm_rc" = 0 ] && grep -qx 'GATE_FULL=1' "$PM_PROBE" 2>/dev/null && grep -q '^GATE_TURNSTILE_HOLDER=.' "$PM_PROBE" \
  && ! grep -q '^GATE_REUSE=' "$PM_PROBE" && grep -qx "$pm_c4" "$PM_PROBE" && grep -q 'gate-pm\.[0-9]*$' "$PM_PROBE" \
  && ok "AC5 the declared bar saw GATE_FULL=1, a holder, no GATE_REUSE, HEAD at the sha and a gate-pm. cwd" \
  || { nope "AC5 the declared bar ran outside the hold verb, unfull, with reuse, or elsewhere (rc=$pm_rc)"; pm_show; }
[ "$(pm_key "$PM_BG" bar)" = "bash bar.sh" ] \
  && ok "AC5 the green record's bar reads bash bar.sh" || nope "AC5 the green record's bar reads '$(pm_key "$PM_BG" bar)'"

# AC6 — a remote that rejects the ref fails the publication, loudly, and the record still lands.
printf '#!/bin/sh\nwhile read o n r; do case "$r" in refs/gov/*) echo "no gov refs here"; exit 1 ;; esac; done\nexit 0\n' \
  > "$PM_B/hooks/pre-receive"; chmod +x "$PM_B/hooks/pre-receive"; rm -f "$PM_REC"
git -C "$PM_B" update-ref -d "$PM_REF" 2>/dev/null
pm_rc=$(pm_run "$pm_c2")
[ "$pm_rc" = 1 ] && grep -q 'post-merge: publish FAILED — .*rejected' "$PM_OUT" && [ "$(pm_key "$PM_REC" published)" = failed ] \
  && [ -n "$(pm_key "$PM_REC" why)" ] \
  && ok "AC6 a rejected publication exits 1, prints publish FAILED naming the rejection, and records published failed with a why" \
  || { nope "AC6 a rejected publication was not reported or not recorded (rc=$pm_rc)"; pm_show; }
rm -f "$PM_B/hooks/pre-receive"

# AC7 — a commit that never landed is refused before any bar.
( cd "$PM_C" && git checkout -q -b feat && printf 'x\n' > feat.txt && git add feat.txt && git commit -qm feat ) >/dev/null 2>&1
pm_c5=$(git -C "$PM_C" rev-parse HEAD); git -C "$PM_C" checkout -q main 2>/dev/null; rm -f "$PM_PROBE"
git -C "$PM_B" update-ref -d "$PM_REF" 2>/dev/null
pm_rc=$(pm_run "$pm_c5")
[ "$pm_rc" = 2 ] && grep -q 'post-merge: REFUSING' "$PM_OUT" && [ ! -f "$PM_PROBE" ] && [ -z "$(pm_red)" ] \
  && ok "AC7 an unlanded commit exits 2 with REFUSING, no bar ran and no ref was pushed" \
  || { nope "AC7 an unlanded commit was not refused before the bar (rc=$pm_rc)"; pm_show; }

# AC8 — the export form is refused; the hook's accepted forms all read bash bar.sh.
pm_c6=$(pm_commit green 'export GOV_GATE_CMD="bash bar.sh"\n'); rm -f "$PM_PROBE"
pm_rc=$(pm_run "$pm_c6")
[ "$pm_rc" = 2 ] && grep -q 'export GOV_GATE_CMD' "$PM_OUT" && [ ! -f "$PM_PROBE" ] \
  && ok "AC8 export GOV_GATE_CMD= exits 2 naming the line, and no bar ran" \
  || { nope "AC8 the export form was not refused (rc=$pm_rc)"; pm_show; }
for pm_form in "GOV_GATE_CMD='bash bar.sh'\\n" 'GOV_GATE_CMD="bash bar.sh" # the bar\n' 'GOV_GATE_CMD="bash bar.sh"\r\n' \
               'GOV_GATE_CMD=bash nothing.sh\nGOV_GATE_CMD="bash bar.sh"\n'; do
  pm_c=$(pm_commit green "$pm_form"); rm -f "$PM_BG"
  pm_rc=$(pm_run "$pm_c")
  [ "$pm_rc" = 0 ] && [ "$(pm_key "$PM_BG" bar)" = "bash bar.sh" ] \
    && ok "AC8 the accepted form $(printf '%q' "$pm_form") resolves to bash bar.sh" \
    || { nope "AC8 the accepted form $(printf '%q' "$pm_form") resolved to '$(pm_key "$PM_BG" bar)' (rc=$pm_rc)"; pm_show; }
done

# AC9 — two remotes and a detached HEAD: refused unless named, and --remote publishes there alone.
git -C "$PM_B" update-ref -d "$PM_REF" 2>/dev/null
( cd "$PM_C" && git remote add "$PM_R2" "$PM_B2" && git push -q "$PM_R2" main \
    && git symbolic-ref "refs/remotes/$PM_R2/HEAD" "refs/remotes/$PM_R2/main" && git checkout -q --detach ) >/dev/null 2>&1
pm_rc=$(pm_run "$pm_c2")
[ "$pm_rc" = 2 ] && grep -q GOV_REMOTE "$PM_OUT" \
  && ok "AC9 two remotes, a detached HEAD and no GOV_REMOTE exit 2 naming GOV_REMOTE" \
  || { nope "AC9 the script chose a remote nobody named (rc=$pm_rc)"; pm_show; }
pm_rc=$(pm_run "$pm_c2" --remote "$PM_R2")
[ "$pm_rc" = 1 ] && [ "$(pm_red "$PM_B2")" = "$pm_c2" ] && [ -z "$(pm_red)" ] \
  && ok "AC9 --remote second publishes the red on the second remote and the first shows none" \
  || { nope "AC9 --remote did not publish on the named remote alone (rc=$pm_rc)"; pm_show; }
git -C "$PM_C" checkout -q main 2>/dev/null

# AC10 — no argument, or a sha that names nothing, is a usage refusal and runs no bar.
pm_rc=$(pm_run)
[ "$pm_rc" = 2 ] && grep -q 'post-merge: usage:' "$PM_OUT" && ! grep -q 'gate queue' "$PM_OUT" \
  && ok "AC10 no argument exits 2 with a usage line and no bar" || { nope "AC10 no argument did not refuse (rc=$pm_rc)"; pm_show; }
pm_rc=$(pm_run 0123456789abcdef0123456789abcdef01234567)
[ "$pm_rc" = 2 ] && grep -q 'post-merge: usage:' "$PM_OUT" && ! grep -q 'gate queue' "$PM_OUT" \
  && ok "AC10 a sha naming no commit exits 2 with a usage line and no bar" || { nope "AC10 an unknown sha did not refuse (rc=$pm_rc)"; pm_show; }
rm -rf "$PM_T"
# <<< post-merge arms

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "run-gates evidence: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates evidence durability, $n assertions)"
exit "$bad"
