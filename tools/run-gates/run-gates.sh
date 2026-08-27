#!/usr/bin/env bash
# run-gates.sh — the coding-governance merge bar: run every gate this repo dogfoods, report per leg.
# The full bar green at the push boundary; earlier runs scoped. Exit 0 = all passed · 1 = one or more failed · 2 = must run from the repo.
#   bash <prefix>/run-gates/run-gates.sh             # legs run CONCURRENTLY, at the width
#                                                    # <prefix>/run-gates/gate-profiles.txt declares
#                                                    # for the detected cores and RAM
#   GATE_JOBS=1 bash <prefix>/run-gates/run-gates.sh # one worker — the serial bar, through this same pool
#   GATE_PROFILE=<row> bash …                        # select a table row by name, skipping detection
#   GATE_PROFILES=<path> bash …                      # read a different table; an absent path falls
#                                                    # back to the built-in formula (the rollback)
# Legs live in the manifest DERIVED below as this kit dir's sibling (single source); this runner is
# a thin iterator over it and holds no leg command of its own.
#
# Legs run through a bounded worker pool. They are safe to run together
# because each heavy leg is already hermetic — it builds its own `mktemp -d` scratch repo, sets git
# config only inside it, and never writes into the real tree. Execution order is a scheduling detail;
# REPORTING is always manifest order, so the output is byte-stable whatever the width.
set -u
KIT_RUN_GATES_VERSION=1.1   # gov:kit run-gates@1.1
# 1.0 -> 1.1: the manifest gained `subject`, and the canary's pinned key set gained it with
# the runner. A target below 1.1 REDS on a leg row carrying the key, so govkit withholds it
# there rather than breaking a bar it was only passing through. TOOL-dUnstalledConvoy-26.
# THIS SCRIPT'S OWN DIRECTORY, RESOLVED BEFORE THE `cd`. A relative `$0` is relative to the caller's
# cwd, so deriving it after `cd "$ROOT"` resolves it against the repo root instead: invoked as
# `bash ../tools/run-gates/run-gates.sh` from a subdirectory the kit dir collapsed to the root, the
# manifest to `./gate-legs.json`, and the runner ran ZERO legs. Captured here, used below.
KITDIR=$(cd "$(dirname "$0")" && pwd)
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "run-gates: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
# The python-launcher resolver, INLINED byte-identically from tools/lib/resolve-python.sh. This
# kit is deployable (the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/`), and tools/lib/ is gov-internal and never travels:
# sourcing it made this runner exit 2 with zero legs run in any tree that did not have it.
# The resolver parity gate derives its copy population by grepping for the marker below, so this
# copy enrols itself. Do not edit it here. (That gate's own script path is deliberately NOT
# spelled in this file: the canary forbids a leg's script path appearing in the runner, and it
# is right to — a comment naming one is one edit away from an inlined leg command.)
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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
PYBIN=$(resolve_python) || { echo "run-gates: no usable python — required to parse the leg manifest"; exit 2; }
fails=0; n=0; skips=0; ondemands=0

# The leg manifest, overridable so a fixture can drive this runner without re-running the real bar.
# Without a seam here the only way to exercise run-gates.sh is to invoke it against the repo, which
# re-runs the whole bar recursively and clobbers the live gate-last-summary.txt mid-run -- so the
# evidence guarantee below had no way to be tested at all (TOOL-dNomadicAtlas-1).
# The manifest is the kit dir's SIBLING, derived rather than spelled: this kit installs at
# <prefix>/run-gates/ and a hardcoded "tools/gate-legs.json" resolves to nothing at any other
# prefix. GATE_LEGS still outranks the derivation (the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` S3).
# Both sides are normalised through the SAME `cd ... && pwd` chain before the strip. Under MSYS one
# directory has two spellings — `git rev-parse --show-toplevel` answers `C:/...` and `pwd` answers
# `/c/...` — and a prefix strip across the two flavours silently leaves an ABSOLUTE path, which then
# resolves to nothing. Never compare path strings across flavours.
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"

# ---- durable per-leg evidence (TOOL-dNomadicAtlas-1) --------------------------------------------
# leg() already holds every leg's merged output in $out and PRINTS it on failure, then keeps only the
# ROW for the durable summary. The reason is in scope at the exact line the durable record is built,
# and dropped there -- so a `| tail` still loses the WHY while keeping the WHICH. inCMS hit this for
# real: a red leg inside a push piped through `tail -45`, unidentifiable afterwards, and the
# reflexive re-run passed, so the evidence was gone for good.
#
# Resolved ONCE, and a path is never composed from an empty root: `git rev-parse --git-dir` yields
# nothing outside a repo, and composing "/gate-logs/<leg>.log" from that would write outside the tree.
GD="$(git rev-parse --git-dir 2>/dev/null)" || GD=""
LOGDIR=""
if [ -n "$GD" ] && mkdir -p "$GD/gate-logs" 2>/dev/null; then
  LOGDIR="$GD/gate-logs"
  chmod 700 "$LOGDIR" 2>/dev/null || true
else
  echo "run-gates: evidence capture OFF (no usable git dir) — leg output is stdout-only this run" >&2
fi

leg_log() {   # NAME -> the log path, or rc 1 when capture is off
  [ -n "$LOGDIR" ] || return 1
  printf '%s/%s.log' "$LOGDIR" "$(printf '%s' "$1" | tr -c 'A-Za-z0-9._-' '_')"
}
# A leg's output can carry an operator-exported credential; mask URL userinfo before it becomes
# durable. Terminal output was ephemeral, a file is not.
redact() { sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g'; }

# Baseline for conditional legs: the mainline tip we gate against. Override with GATE_BASE.
# Unresolvable (no remote / shallow / detached) → empty, and changed() fails safe to "run".
DEFBR=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null); DEFBR=${DEFBR#origin/}
# THE BASE IS THE BRANCH POINT, not the remote tip, so a branch is graded on what IT changed
# rather than on everything that landed while it was open. The merge-base is used only where it
# is a PROPER ANCESTOR of HEAD; otherwise the origin tip stands.
#
# That fallback is not a nicety. An earlier draft REFUSED the base whenever the merge-base equalled
# HEAD, on the reasoning that the merge-base is degenerate on the default branch itself. The
# refusal cannot tell that case from a fresh branch cut off a fast-forwarded `main` — which is the
# commonest scoped-run state in this repository — and in both it fell back to running all 86 legs.
# Worse, it would have red the shipped canary on landing: that harness points its fixture remote at
# HEAD, so merge-base == HEAD there and the arm expecting `GATE skip  guarded` would have lost its
# skip. The origin tip handles both correctly, because `changed()` diffs BASE against the WORKING
# TREE and therefore still sees uncommitted edits.
BASE=
if [ -n "${GATE_BASE:-}" ]; then
  # An explicit base OUTRANKS the derivation, unchanged. It is the escape hatch for exactly the
  # cases no derivation gets right.
  BASE=$(git rev-parse --verify -q "$GATE_BASE" 2>/dev/null) || BASE=
else
  _tip=$(git rev-parse --verify -q "origin/${DEFBR:-main}" 2>/dev/null) || _tip=
  if [ -n "$_tip" ]; then
    _mb=$(git merge-base HEAD "$_tip" 2>/dev/null) || _mb=
    _head=$(git rev-parse --verify -q HEAD 2>/dev/null) || _head=
    if [ -n "$_mb" ] && [ "$_mb" != "$_head" ]; then BASE=$_mb; else BASE=$_tip; fi
  fi
fi
# GATE_FULL bypasses every guard, so the run checks the whole bar. `.githooks/pre-push` sets it: a
# guard may scope ANY run now, including the authoritative one — and the property that used to make
# that safe was `.githooks/pre-push` forcing GATE_FULL=1 on every push. That force is gone; what
# replaces it is a BOUNDED, RECORDED obligation in the hook, which forces a total run when no
# recorded full green covers the pushed tip, when it is more than a declared number of commits
# behind, when its tree fingerprint does not reproduce at the sha it names, or when the leg
# manifest itself moved. So a too-narrow guard costs an early signal for at most that many
# commits, rather than never being caught — and it is the hook, not this line, that is now the
# thing to read. Both fail-safes below keep their meaning: an unresolvable BASE runs everything,
# early signal rather than a wrong merge verdict. Both fail-safes below keep their meaning — an
# unresolvable BASE runs everything, and so does a guard that errors.
changed() { [ -n "${GATE_FULL:-}" ] && return 0; [ -z "$BASE" ] && return 0; ! git diff --quiet "$BASE" -- "$@" 2>/dev/null; }

# ONE git-dir resolution for the whole runner. `GD` above and a second `gd` here used to resolve the
# same thing twice; the run record adds four more git-dir-rooted paths, and four paths hanging off
# whichever of two variables an author happened to reach for is how a record ends up half in one
# place. `gd` survives as the name the surrounding code already reads.
gd="$GD"; sfile=""; LEDGER=""
[ -n "$gd" ] && { sfile="$gd/gate-last-summary.txt"; LEDGER="$gd/gate-ledger.tsv"; }
# The dispatch hint is READ from the ledger and no longer from a separate timing cache. Field 2 is
# still the duration, which is what keeps the manifest parser below unchanged.
TIMINGS="$LEDGER"
# MERGE NOTE: `leg()` is gone — the pool replaced it with runleg() (the worker) and report_one() (the
# reporter). TOOL-dNomadicAtlas-1's durable per-leg evidence is PORTED into both rather than dropped:
# the log write lives in runleg(), which is where $out and $rc are in scope, and the `log:` pointer
# lives in report_one(), which is where FAILED_LEGS is built. Writing from the worker is strictly
# better here — the writes are per-leg files and now happen concurrently.

# ---- hardware profiles (the profile-table unit) --------------------------------------------------
# The knobs are DECLARED in a table beside this runner rather than computed from core count alone: a
# 16-core / 8 GB VM used to select width 8 and thrash, because cores were the only question asked.
# Grammar and reasoning live in the table itself; this block reads it, selects a row, and applies it.
#
# THE GOVERNING INVARIANT: no knob may ever turn a leg into a PASS or a SKIP. A knob may make the bar
# slower, and it may turn an unbounded hang into a bounded RED. It may never make the bar check less.
# KNOWN_KNOBS is the whole implemented set; the canary PINS the same set separately, which is what
# stops a coverage knob being added without an author reading this paragraph.
KNOWN_KNOBS="width timeout"
PROFILES="${GATE_PROFILES:-$KITREL/gate-profiles.txt}"
prof_die() { echo "run-gates: $*" >&2; exit 2; }

# LENGTH-BOUNDED BEFORE ANY ARITHMETIC. Both `[ "$v" -gt 0 ]` and `$(( ))` ERROR on an int64 overflow
# instead of comparing, which is how a 20-digit width value once span the dispatch loop forever
# having executed ZERO legs. 15 digits admits every real reading below (a byte count on a 900 TB box)
# and cannot overflow int64 even after one multiply. Zero is "unknown", never a valid reading.
num_ok() { case "$1" in ''|*[!0-9]*) return 1 ;; esac; [ ${#1} -le 15 ] || return 1; [ "$1" -gt 0 ]; }

# Every source is RUN and its output validated, never probed for existence — being on PATH is not
# evidence, the lesson tools/lib/resolve-python.sh records. Measured on node `a`: the three core
# sources all report 16, the page arithmetic and /proc/meminfo agree within 1 MB, and `sysctl` exits
# 127, which is the case the chain must survive and does. CORE_SRC/RAM_SRC accumulate what was TRIED,
# so the visibility line names the chain whether it answered on the first source or the third.
DET_CORES=0; DET_RAM=0; CORE_SRC=""; RAM_SRC=""
det_cores() {
  local v
  DET_CORES=0
  if [ -n "${GATE_CORES+x}" ]; then CORE_SRC="seam"; num_ok "${GATE_CORES}" && DET_CORES=${GATE_CORES}; return; fi
  CORE_SRC="nproc"
  v=$(nproc 2>/dev/null); if num_ok "$v"; then DET_CORES=$v; return; fi
  CORE_SRC="$CORE_SRC,getconf"
  v=$(getconf _NPROCESSORS_ONLN 2>/dev/null); if num_ok "$v"; then DET_CORES=$v; return; fi
  CORE_SRC="$CORE_SRC,env"
  v=${NUMBER_OF_PROCESSORS:-}; if num_ok "$v"; then DET_CORES=$v; return; fi
}
# The cgroup root, seamed so a fixture can drive the container path. Without a seam this source is
# untestable on a host that is not in a container, and an untestable source rots.
CGROUP_ROOT="${GATE_CGROUP_ROOT:-/sys/fs/cgroup}"
cgroup_ram_mb() {   # -> prints the ENFORCED limit in MB, or nothing
  local f v
  for f in "$CGROUP_ROOT/memory.max" "$CGROUP_ROOT/memory/memory.limit_in_bytes"; do
    [ -r "$f" ] || continue
    v=$(head -c 32 "$f" 2>/dev/null | tr -d '[:space:]')
    # `max` (v2's no-limit spelling) and v1's 9223372036854771712 sentinel are both UNKNOWN, not
    # readings. num_ok's 15-digit bound rejects the sentinel for us, which is the bound doing a second
    # job rather than a coincidence — a 19-digit byte count is not a memory size anybody has.
    num_ok "$v" || continue
    v=$(( v / 1048576 )); num_ok "$v" || continue
    printf '%s' "$v"; return 0
  done
  return 1
}
det_ram() {   # -> DET_RAM in MB
  local pages pgsz kb v
  DET_RAM=0
  if [ -n "${GATE_RAM_MB+x}" ]; then RAM_SRC="seam"; num_ok "${GATE_RAM_MB}" && DET_RAM=${GATE_RAM_MB}; return; fi
  RAM_SRC="getconf"
  pages=$(getconf _PHYS_PAGES 2>/dev/null); pgsz=$(getconf PAGESIZE 2>/dev/null)
  if num_ok "$pages" && num_ok "$pgsz"; then
    # Divide the PAGE SIZE first so the product stays small. A page under 1 KB truncates that divisor
    # to zero, which would report NO MEMORY — a reading, and a wrong one. Guarded, so it reports
    # UNKNOWN and falls through to the next source instead.
    kb=$(( pgsz / 1024 ))
    if [ "$kb" -gt 0 ]; then v=$(( pages * kb / 1024 )); if num_ok "$v"; then DET_RAM=$v; return; fi; fi
  fi
  RAM_SRC="$RAM_SRC,meminfo"
  v=$(awk '/^MemTotal:/ { print int($2 / 1024); exit }' /proc/meminfo 2>/dev/null)
  if num_ok "$v"; then DET_RAM=$v; return; fi
  RAM_SRC="$RAM_SRC,sysctl"
  v=$(sysctl -n hw.memsize 2>/dev/null)
  if num_ok "$v"; then v=$(( v / 1048576 )); if num_ok "$v"; then DET_RAM=$v; return; fi; fi
}
# THE ENFORCED LIMIT WINS OVER THE HOST READING, and the RAM guard is the reason. Every source above
# reports HOST physical memory, which inside a memory-capped container is not the number that decides
# whether eight scratch repos fit: a 4 GB CI runner on a 512 GB host reads 512 GB, selects the widest
# row, and thrashes — the exact case the table was written for, in the environment this bar is
# scheduled to move to. MIN rather than replace, so a bogus limit can only ever make the bar SLOWER,
# which is the fail-safe direction this whole block is built on.
det_ram_capped() {
  det_ram
  local lim
  # THE SEAM WINS. `det_ram` returns early with RAM_SRC=seam precisely to signal a bypass, and capping
  # it here handed the deciding vote back to ambient container state — in the arms written so the box
  # could not decide, and against the runner's own documented promise that the seam overrides the
  # reading. It also silently replaced the deliberate UNKNOWN of `GATE_RAM_MB=0`. The container guard
  # still covers every genuinely DETECTED reading, which is the only population it was argued for.
  [ "$RAM_SRC" = seam ] && return 0
  lim=$(cgroup_ram_mb) || return 0
  [ "$DET_RAM" = 0 ] && { DET_RAM=$lim; RAM_SRC="$RAM_SRC,cgroup"; return 0; }
  [ "$lim" -lt "$DET_RAM" ] && { DET_RAM=$lim; RAM_SRC="$RAM_SRC,cgroup"; }
  return 0
}

PROF_NAME=""; PROF_WIDTH=""; PROF_TIMEOUT=0; PROF_TAG=""; PROF_WHERE=""
if [ -f "$PROFILES" ]; then
  # GATE_PROFILE names a row and SKIPS detection; otherwise the first row both thresholds satisfy.
  if [ -n "${GATE_PROFILE:-}" ]; then PROF_WHERE="detection skipped"
  else det_cores; det_ram_capped; fi
  ln=0; declared=""; sel=""; selknobs=""
  # Every row is validated even after one is selected: a malformed row is an operator error wherever
  # it sits, and a refusal that depended on position would pass on the tables most likely to be wrong.
  while IFS=$'\t' read -r pname pcores pram pknobs || [ -n "$pname" ]; do
    ln=$((ln+1))
    # LEADING BLANKS STRIPPED BEFORE THE TEST, because the canary's own comment filter strips them
    # and this parser did not: an INDENTED comment — which this file's header explicitly invites, and
    # which the shipped table itself is full of — refused the whole bar with a message about field
    # counts. Two readers of one file disagreeing about which lines are even rows is the drift this
    # joins shut; the looser of the two wins, since no verdict can turn on a comment.
    case "${pname#"${pname%%[![:space:]]*}"}" in ''|'#'*) continue ;; esac
    case "$pknobs" in *$'\t'*) prof_die "$PROFILES:$ln: malformed profile row (more than four tab-separated fields)" ;; esac
    [ -n "$pcores" ] && [ -n "$pram" ] && [ -n "$pknobs" ] \
      || prof_die "$PROFILES:$ln: malformed profile row (expected name, min cores, min RAM MB, knobs)"
    case "$pcores$pram" in *[!0-9]*) prof_die "$PROFILES:$ln: malformed profile row (thresholds must be digits: '$pcores', '$pram')" ;; esac
    # THE DECLARED HALF OF THE COMPARISON, bounded exactly as num_ok bounds the detected half. Digits
    # alone are not enough: `[ "$DET_CORES" -ge "$pcores" ]` ERRORS on an int64 overflow rather than
    # comparing, so a twenty-digit threshold silently matched nothing and dropped the run to the
    # catch-all with no refusal at all. A bound on one side of a comparison is not a bound.
    { [ ${#pcores} -le 15 ] && [ ${#pram} -le 15 ]; } \
      || prof_die "$PROFILES:$ln: threshold too long to compare (max 15 digits): '$pcores', '$pram'"
    # A silently ignored knob is a knob the operator believes they set, so an unknown key REFUSES.
    IFS=, read -ra kv <<<"$pknobs"
    for k in "${kv[@]}"; do
      case "$k" in *=*) ;; *) prof_die "$PROFILES:$ln: malformed knob '$k' (expected key=value)" ;; esac
      case " $KNOWN_KNOBS " in *" ${k%%=*} "*) ;; *) prof_die "$PROFILES:$ln: unknown knob key '${k%%=*}' (known: $KNOWN_KNOBS)" ;; esac
      case "${k#*=}" in ''|*[!0-9]*) prof_die "$PROFILES:$ln: knob '${k%%=*}' has a non-numeric value '${k#*=}'" ;; esac
      # Same bound, same reason, and here the symptom was worse than a wrong width: an over-long
      # `timeout=` made every later `[ "$PROF_TIMEOUT" -gt 0 ]` error instead of compare, so the knob
      # was silently dropped AND the INERT warning that would have said so was disabled by the same
      # failing test. The visibility line then reported `timeout off` beside a table declaring one.
      case "${k#*=}" in ????????????????*) prof_die "$PROFILES:$ln: knob '${k%%=*}' value too long to compare (max 15 digits): '${k#*=}'" ;; esac
    done
    declared="$declared $pname"
    [ -n "$sel" ] && continue
    if [ -n "${GATE_PROFILE:-}" ]; then
      [ "$pname" = "${GATE_PROFILE}" ] && { sel=$pname; selknobs=$pknobs; }
    elif [ "$DET_CORES" -ge "$pcores" ] && [ "$DET_RAM" -ge "$pram" ]; then
      sel=$pname; selknobs=$pknobs
    fi
  done < "$PROFILES"
  if [ -z "$sel" ]; then
    [ -n "${GATE_PROFILE:-}" ] \
      && prof_die "$PROFILES: GATE_PROFILE='${GATE_PROFILE}' names no row. Declared rows:$declared"
    # Unmatchable is not the same state as ABSENT, and only one of them is an operator error: the
    # catch-all row is what makes a match unconditional, so a table with none was declared wrong.
    prof_die "$PROFILES: no row matches cores $DET_CORES / ram $DET_RAM MB — the table declares no catch-all row. Declared rows:$declared"
  fi
  PROF_NAME=$sel
  IFS=, read -ra kv <<<"$selknobs"
  for k in "${kv[@]}"; do
    case "${k%%=*}" in width) PROF_WIDTH=${k#*=} ;; timeout) PROF_TIMEOUT=${k#*=} ;; esac
  done
  [ -n "$PROF_WIDTH" ] || prof_die "$PROFILES: row '$sel' declares no width knob"
  PROF_TAG="detected"
  [ -n "${GATE_PROFILE:-}" ] && PROF_TAG="GATE_PROFILE"
  [ -z "$PROF_WHERE" ] && { [ "$DET_CORES" = 0 ] || [ "$DET_RAM" = 0 ]; } && PROF_TAG="detection failed"
else
  # ABSENT is a FALLBACK, not a refusal: this kit deploys, and an adopter may take it without the
  # table. Deleting the table is therefore also the documented rollback for this whole mechanism, and
  # the arm that drives this branch is what proves the rollback rather than hoping for it.
  # The 8 here is the SAME value the table's top row declares, and its measurement is argued THERE,
  # beside the number. Restating the argument in both places is how the two copies drift apart while
  # still agreeing loudly enough that nobody checks.
  det_cores; det_ram_capped
  bi=$DET_CORES; [ "$bi" -gt 0 ] || bi=4
  PROF_NAME="built-in"; PROF_WIDTH=$(( bi < 8 ? bi : 8 )); PROF_TIMEOUT=0; PROF_TAG="built-in default"
  # A pin the operator set and this branch cannot honour. WARNED, not refused: refusing would block
  # the documented rollback for anyone carrying GATE_PROFILE in their environment. Silence is the one
  # option ruled out — the same typo is FATAL against a present table, so staying quiet here turns a
  # refusal into an invisible no-op, which is the rule the row validator above states in as many words.
  if [ -n "${GATE_PROFILE:-}" ]; then
    echo "run-gates: GATE_PROFILE='${GATE_PROFILE}' is set but no profile table exists at $PROFILES — the built-in formula is in force and the request is IGNORED" >&2
    PROF_TAG="$PROF_TAG, GATE_PROFILE ignored"
  fi
fi

# A knob the operator set and the host cannot honour is worse than no knob: say so rather than run
# inert. `timeout` is RUN, not probed — the same rule the detection chain follows.
# PROBED WITH THE OPTION SET THE RUN ACTUALLY USES. A bare `timeout 1 true` passes on a build that
# rejects `-k`, so the probe cleared a path the leg exec then failed on — the probe and the subject
# were two different commands, which is the shape a probe exists to rule out.
# PROBED ONCE, READ TWICE. The profile knob and the per-leg ceilings need the same fact -- does
# `timeout -k` actually RUN here -- and probing it per consumer would cost a spawn each and could
# answer differently. RUN, never `command -v`: the lesson tools/lib/resolve-python.sh records.
CEILINGS_LIVE=1
timeout -k 1s 1 true >/dev/null 2>&1 || CEILINGS_LIVE=0
if [ "$PROF_TIMEOUT" -gt 0 ] && [ "$CEILINGS_LIVE" = 0 ]; then
  echo "run-gates: profile '$PROF_NAME' asks for a ${PROF_TIMEOUT}s per-leg timeout but timeout does not run here — the knob is INERT this run" >&2
  PROF_TIMEOUT=0
fi

# A non-numeric or <1 width is clamped to 1 rather than refused — this knob only schedules work, it
# can never skip a leg. GATE_JOBS overrides the width ONLY: the row is still selected and still
# supplies the timeout, which is what keeps the override from disabling the rest of the profile.
JOBS=${GATE_JOBS:-$PROF_WIDTH}
# Bound by LENGTH before any numeric test touches the value. Both `[ "$JOBS" -lt 1 ]` and `$(( JOBS < 1 ))`
# ERROR on an int64 overflow instead of comparing, so a 20-digit value used to sail past the clamp into a
# dispatch loop whose own `[ "$(live)" -lt "$JOBS" ]` errored identically: the runner spun forever having
# executed ZERO legs and printed no verdict, which on the push boundary is a hang rather than a red.
# `:-` substitutes the default for null as well as unset, so JOBS is never empty and an '' alternative here
# would be dead — the arm that "covered" it was measuring the default width, not the clamp.
case "$JOBS" in *[!0-9]*) JOBS=1 ;; ?????*) JOBS=64 ;; esac
[ "$JOBS" -lt 1 ] && JOBS=1

# ONE visibility line, before the first leg verdict and copied into the durable records — a profile
# nobody can see is a knob nobody can debug. The parenthesised tail follows the report's two-space
# contract: `<head>  (<tail>)`, so a reader splits on the double space and gets the bare name back.
# It reports the EFFECTIVE width (post-clamp, post-GATE_JOBS) and the sources the chain TRIED, so a
# run that fell through to its second source says so instead of looking like a first-source hit.
prof_n() { if [ "$1" = 0 ]; then printf '?'; else printf '%s' "$1"; fi; }
[ -n "${GATE_JOBS:-}" ] && PROF_TAG="$PROF_TAG, GATE_JOBS"
if [ -n "$PROF_WHERE" ]; then prof_where=$PROF_WHERE
else prof_where="cores $(prof_n "$DET_CORES") via $CORE_SRC, ram $(prof_n "$DET_RAM") MB via $RAM_SRC"; fi
prof_t=off; [ "$PROF_TIMEOUT" -gt 0 ] && prof_t="${PROF_TIMEOUT}s"
# THE CEILING REGIME IS ITS OWN FIELD, and deliberately not folded into `timeout`. That field names
# the PROFILE knob, which every shipped row sets to 0, and the canary asserts it reads `off` on a
# host that cannot honour it -- overloading it made an INERT run read as a live bound. But leaving
# the line saying only `timeout off` while 85 legs carried a ceiling was the opposite lie, so the
# regime is reported beside the knob rather than instead of it. TOOL-aBoundedCeiling-1.
prof_c=live; [ "$CEILINGS_LIVE" = 1 ] || prof_c=INERT
# ON STDERR, and independent of PROF_TIMEOUT. The pre-existing INERT notice at the profile probe is
# gated on a knob every shipped row sets to 0, so it can never fire; without this line the only
# signal that all 85 ceilings are dead would be a stdout suffix nobody reads for warnings.
if [ "$CEILINGS_LIVE" != 1 ]; then
  echo "run-gates: NOTE - this host has no runnable 'timeout -k', so EVERY leg's declared ceiling is INERT and every leg runs unbounded this run" >&2
fi
PROF_LINE="gate profile: $PROF_NAME  ($prof_where; width $JOBS, timeout $prof_t, ceilings $prof_c; $PROF_TAG)"
echo "$PROF_LINE"


# ---- the turnstile: one bar per repository at a time (the turnstile unit) -------------------------
# Nothing coordinated two bars before this. `git worktree list` reports well into double figures on
# this node, and the sibling profiling build measured three full bars running at once with CPU at
# 39 %, both queues empty, and width 24 running 26 % SLOWER than width 8. The contended resource does
# not parallelise, so two concurrent bars are worse than two sequential ones and serializing them is
# the right shape for this machine rather than merely the polite one.
#
# THE KEY IS THE GIT COMMON DIR, resolved absolutely. Every worktree of one repository shares it, and
# two different repositories never do — so "one bar per repo" falls out of the key derivation instead
# of needing a predicate. The runner's per-worktree `$gd` resolutions above are deliberate and are
# left exactly as they are: evidence is per-worktree, contention is per-repository.
TS_COMMON=""; TS_DIR=""; TS_TICKET=""; TS_NONCE=""; TS_WAITED=0; TS_HELD=0
if [ "${GATE_TURNSTILE:-1}" != 0 ]; then
  TS_COMMON=$(git rev-parse --git-common-dir 2>/dev/null) || TS_COMMON=""
  [ -n "$TS_COMMON" ] && TS_COMMON=$(cd "$TS_COMMON" 2>/dev/null && pwd) || TS_COMMON=""
fi

# THE TTL IS DERIVED, never a wall clock copied out of a timing cache. What has to be outlasted is
# the gap between two heartbeat refreshes, and S4 refreshes at one site: a leg COMPLETING. So the
# bound is "how long can one leg take", and the runner already has a declared answer for that when
# the selected profile row sets one — `timeout=<s>`. When it does not, no number here is derivable
# from anything, and the fallback is deliberately large and says so.
#
# ponytail: a single leg longer than TS_TTL with no per-leg deadline configured is reaped mid-run.
# That is the named ceiling of the fallback, and the fix is to set `timeout=` on the profile row
# rather than to raise this constant — a bigger fallback only moves the same cliff further out.
if [ "${PROF_TIMEOUT:-0}" -gt 0 ]; then TS_TTL=$(( PROF_TIMEOUT * 3 ))
else TS_TTL=${GATE_TURNSTILE_TTL:-1800}; fi
# The bounded wait is a DECLARED MULTIPLE OF THE TTL, so it moves with the one number this unit
# derives and is never sized against a bar's wall clock. Four: long enough that a queue three deep
# behind a stalled holder still drains rather than stampeding, short enough that a wedged node
# releases within an hour.
TS_MAXWAIT=$(( TS_TTL * 4 ))
TS_TICK=${GATE_TURNSTILE_TICK:-2}

ts_now()  { date +%s; }
ts_hb()   { [ -n "$TS_DIR" ] && printf '%s' "$(ts_now)" > "$TS_DIR/heartbeat.tmp" 2>/dev/null && mv -f "$TS_DIR/heartbeat.tmp" "$TS_DIR/heartbeat" 2>/dev/null || true; }
ts_alive(){ kill -0 "$1" 2>/dev/null; }

# RELEASE IS NONCE-GUARDED. A run whose beacon was reaped for being stale must never delete its
# successor's: without the nonce, a slow holder that comes back to life removes a directory it no
# longer owns and two bars run anyway — the exact failure this unit exists to prevent, arriving
# through its own cleanup path.
ts_release() {
  [ -n "$TS_DIR" ] || return 0
  if [ "$(cat "$TS_DIR/nonce" 2>/dev/null)" = "$TS_NONCE" ]; then rm -rf "$TS_DIR" 2>/dev/null || true; fi
  TS_DIR=""
}
ts_drop_ticket() { [ -n "$TS_TICKET" ] && rm -f "$TS_TICKET" 2>/dev/null; TS_TICKET=""; }

# Reap a holder that cannot still be holding. TWO independent signals, because each covers a case the
# other cannot: a dead PID is immediate and certain, and a stale heartbeat catches the holder whose
# PID was recycled or which is alive but wedged.
ts_try_reap() {
  local hpid hb age
  [ -d "$TS_DIR_C" ] || return 1
  hpid=$(cat "$TS_DIR_C/pid" 2>/dev/null)
  hb=$(cat "$TS_DIR_C/heartbeat" 2>/dev/null)
  if [ -n "$hpid" ] && ! ts_alive "$hpid"; then
    printf 'run-gates: reaping the beacon of a dead holder (pid %s)\n' "$hpid" >&2
    rm -rf "$TS_DIR_C" 2>/dev/null; return 0
  fi
  case "$hb" in ''|*[!0-9]*) hb=0 ;; esac
  age=$(( $(ts_now) - hb ))
  if [ "$hb" != 0 ] && [ "$age" -gt "$TS_TTL" ]; then
    printf 'run-gates: reaping the beacon of a stalled holder (heartbeat %ss old, ttl %ss)\n' "$age" "$TS_TTL" >&2
    rm -rf "$TS_DIR_C" 2>/dev/null; return 0
  fi
  return 1
}

if [ -n "$TS_COMMON" ]; then
  TS_DIR_C="$TS_COMMON/gate-bar-beacon"
  TS_Q="$TS_COMMON/gate-bar-queue"
  TS_NONCE="$$-$(ts_now)-$RANDOM"
  mkdir -p "$TS_Q" 2>/dev/null || true
  # EVERY RUN TAKES A TICKET, including an uncontended one. A ticket whose name sorts by time is all
  # the ordering there is: every waiter reads the same listing and derives the same total order
  # independently, so there is no counter file to corrupt and no coordinator to elect.
  TS_TICKET="$TS_Q/$(date -u +%Y%m%dT%H%M%S)-$$-$RANDOM"
  : > "$TS_TICKET" 2>/dev/null || TS_TICKET=""
  ts_start=$(ts_now); ts_lastpos=""; ts_announced=0
  while :; do
    # THE CLAIM IS A DIRECTORY CREATE, which is atomic on every filesystem this runs on and needs no
    # `flock` — which does not exist on this platform. The heartbeat is written FIRST on winning, so
    # a just-claimed holder is never mistaken by a waiter for one with no clock.
    # REAP DEAD WAITERS BEFORE READING THE HEAD. The beacon has always had a liveness test --
    # `ts_alive`, ten lines up, and the runner even prints "reaping the beacon of a dead
    # holder". The QUEUE had none, and the acquire predicate below is only "my ticket sorts
    # first". So a killed bar left a ticket that sorts first FOREVER and wedged every later bar
    # in the repository, reporting nothing at all: no legs, no per-leg log, just a position
    # number that never moves.
    #
    # MEASURED 2026-08-27: a `push-main.sh` landing sat 6858 s at "queued at position 4" with
    # ZERO legs run, behind three dead tickets from bars killed earlier that session. Deleting
    # them by hand advanced it 4 -> 3 -> 1 and it acquired at once. Second wedge that day.
    # TOOL-aBoundedCeiling-12.
    #
    # A ticket is `<utc>-<pid>-<nonce>`, so the pid is field 2. A name that does not parse is
    # LEFT ALONE rather than guessed at: deleting a ticket we cannot read is how a live bar
    # loses its place, which is a worse failure than the one being fixed.
    for _tk in "$TS_Q"/*; do
      [ -e "$_tk" ] || continue
      _tb=$(basename "$_tk")
      [ "$_tb" = "$(basename "${TS_TICKET:-}")" ] && continue
      _tp=$(printf %s "$_tb" | cut -d- -f2)
      case "$_tp" in ""|*[!0-9]*) continue ;; esac
      ts_alive "$_tp" || rm -f "$_tk" 2>/dev/null || true
    done
    if [ -n "$TS_TICKET" ] && [ "$(ls -1 "$TS_Q" 2>/dev/null | LC_ALL=C sort | head -1)" = "$(basename "$TS_TICKET")" ] \
       && mkdir "$TS_DIR_C" 2>/dev/null; then
      TS_DIR="$TS_DIR_C"
      printf '%s' "$(ts_now)" > "$TS_DIR/heartbeat" 2>/dev/null || true
      printf '%s' "$$"        > "$TS_DIR/pid" 2>/dev/null || true
      printf '%s' "$TS_NONCE" > "$TS_DIR/nonce" 2>/dev/null || true
      TS_HELD=1
      # THE RELEASE TRAP GOES ON HERE, at the instant the beacon becomes ours, and not with the
      # scratch-dir trap further down. Everything between this line and there — the manifest
      # parse, the fingerprint, the whole run-record setup — is time during which the beacon is
      # HELD and, without this, no trap would release it. A signal in that window killed the run
      # and left the repository queueing behind nobody until the TTL expired.
      #
      # Measured, and it is the reason this is not merely tidy: the turnstile arms passed three
      # times in a row run alone and failed on TERM and HUP the moment they ran after another
      # harness. Under that load the window is seconds wide — process creation on this platform
      # has been measured 25x slower under contention — so the window is not theoretical and it is
      # widest exactly when two bars are most likely to collide.
      trap 'ts_release; ts_drop_ticket' EXIT INT TERM HUP
      # S4 (TOOL-aShardedFloor-1), and the GUARD is the whole of it. `TS_WAITED` is refreshed at
      # the BOTTOM of this loop and this path breaks above it, so a contended acquire records the
      # previous tick's value and understates the wait by up to one `TS_TICK`.
      #
      # Refreshing unconditionally — which is the obvious fix and the one first specced — breaks
      # the UNCONTENDED case instead: `ts_now` is `date +%s` and truncates, the five processes
      # above (`ls`, `sort`, `head`, `basename`, `mkdir`) sometimes straddle a second boundary,
      # and the line below then prints `waited 1s` where `run-gates.turnstile.test.sh` asserts
      # `^gate queue: waited 0s$`. Measured on node a: 4 of 60 first-iteration acquires crossed,
      # on an idle box, in a leg that normally runs inside a concurrent bar where process
      # creation is 25x slower. `ts_announced` is 1 only once the loop has reported a position,
      # which is exactly the predicate "this run actually queued".
      #
      # RESIDUAL, named rather than left to be rediscovered: `ts_try_reap && continue` above
      # skips both this refresh AND the announce, so a run that reaps a stale holder on its first
      # iteration still records the stale value. Closing that needs a second predicate and is
      # deliberately not in this unit.
      [ "$ts_announced" = 1 ] && TS_WAITED=$(( $(ts_now) - ts_start ))
      break
    fi
    ts_try_reap && continue
    TS_WAITED=$(( $(ts_now) - ts_start ))
    if [ "$TS_WAITED" -ge "$TS_MAXWAIT" ]; then
      # FAILS OPEN, LOUDLY. A turnstile that can wedge a bar is worse than two bars: the run drops
      # its ticket and proceeds unqueued rather than becoming the outage. It contributes nothing to
      # the exit code, ever.
      echo "run-gates: turnstile WAIT EXPIRED after ${TS_WAITED}s (bound ${TS_MAXWAIT}s) — running UNQUEUED alongside whatever holds the beacon" >&2
      ts_drop_ticket
      break
    fi
    pos=$(ls -1 "$TS_Q" 2>/dev/null | LC_ALL=C sort | grep -n "^$(basename "${TS_TICKET:-none}")$" | cut -d: -f1)
    [ -n "$pos" ] || pos="?"
    if [ "$pos" != "$ts_lastpos" ] || [ "$ts_announced" = 0 ]; then
      echo "run-gates: another bar holds this repository — queued at position $pos (waited ${TS_WAITED}s)" >&2
      [ -n "$gd" ] && printf 'position\t%s\nwaited\t%s\n' "$pos" "$TS_WAITED" > "$gd/gate-queue-status" 2>/dev/null || true
      ts_lastpos=$pos; ts_announced=1
    fi
    sleep "$TS_TICK"
  done
  ts_drop_ticket
  [ -n "$gd" ] && rm -f "$gd/gate-queue-status" 2>/dev/null || true
  # A LINEAGE MARKER for any future nested caller. The primary path needs no exemption predicate —
  # a nested run in a scratch repo resolves a different common dir and therefore a different beacon —
  # but a caller that one day nests inside the SAME repo would deadlock against its own parent, and a
  # marker it can read is cheaper than the incident.
  export GATE_TURNSTILE_HELD="${GATE_TURNSTILE_HELD:-}${GATE_TURNSTILE_HELD:+,}$TS_NONCE"
fi

# THE QUEUE FACTS, resolved ONCE here and emitted at three sites — the same shape as `PROF_LINE`,
# which is built once and echoed to stdout, to `gate-last-summary.txt` and to the RED-only durable
# copy. `PROF_LINE` cannot absorb the wait: it is echoed BEFORE this block, and folding the wait
# into it would delay the profile line by the entire queue wait.
#
# THE VALUE IS A DASH WHEN IT IS UNMEASURABLE, which is this file's own idiom for an input it could
# not measure (see `input_key`). A `0` recorded for a run whose turnstile was DISABLED is a
# reassuring number about a probe that never ran, and this repo's rule is that such a probe says so.
#
# `queued_from` earns its place on a TWO-way ambiguity, not a three-way one. With `-` emitted for
# `off` and `unresolved`, a `queued 0` can only mean held-and-uncontended — an `expired` run has
# burned at least `TS_MAXWAIT`, which is `TS_TTL * 4` and therefore never 0. What the second key
# carries that a bare integer cannot is the `held`/`expired` split, and the `off`/`unresolved` one.
#
# WHAT THIS DOES NOT CHECK, stated here because a reader will assume otherwise: `unresolved` is
# UNARMED. Reaching it needs `git rev-parse --git-common-dir` to fail while the runner is already
# past its own repo guard, and breaking a linked worktree's `commondir` makes `--show-toplevel` fail
# too, so the runner exits 2 before this line. No fixture in the turnstile suite can produce it.
QUEUED="-"; QUEUED_FROM=off
if [ "${GATE_TURNSTILE:-1}" != 0 ]; then
  if   [ -z "$TS_COMMON" ]; then QUEUED_FROM=unresolved
  elif [ "$TS_HELD" = 1 ];  then QUEUED="$TS_WAITED"; QUEUED_FROM=held
  else                            QUEUED="$TS_WAITED"; QUEUED_FROM=expired
  fi
fi
QUEUE_SUMMARY="gate queue: queued $QUEUED from $QUEUED_FROM"

# ONE PARSEABLE LINE, always, zero when uncontended. A wrapper that brackets a wall clock around this
# runner — `profile_bar.py` is exactly one — cannot otherwise tell waiting from working, and a queue
# wait folded into a measured wall clock can push a packing ratio below 1.0, which that tool correctly
# refuses as arithmetically impossible. This unit ships the line; who consumes it is a separate
# question.
#
# ITS BYTES ARE PINNED by two consumers — `profile_bar.py`'s `$`-anchored regex and
# `run-gates.turnstile.test.sh` — so the state word above is NOT appended here. It goes to the
# header and the summary file, which is why `QUEUE_SUMMARY` is a separate string.
echo "gate queue: waited ${TS_WAITED}s"

WORK=$(mktemp -d) || { echo "run-gates: cannot create a scratch dir"; exit 2; }
# THE TRAP COVERS THE SCRATCH DIR AND THE BEACON, AND NOTHING ELSE. That exclusion is load-bearing:
# the run record below lives under the git dir and is DURABLE, so a trap that swept it would erase
# the record on every ordinary exit and on every caught signal — which is every path except the
# crash the record exists to make readable.
#
# WIDENED past EXIT because a bar is routinely interrupted, and a beacon that only releases on a
# clean exit turns every Ctrl-C into a repository that queues behind a run nobody is doing until
# the TTL expires. The signal arms re-exit with the conventional 128+n so the caller still sees
# what killed it. `cleanup` is idempotent: EXIT fires after them and must not undo a release.
# SUPERSEDES the claim-time trap above with the same release plus the scratch dir. `trap` replaces
# rather than appends, which is what makes this safe: there is never a moment with no handler, and
# never two handlers racing to remove the same directory.
cleanup() { rm -rf "$WORK" 2>/dev/null || true; ts_release; ts_drop_ticket; }
trap cleanup EXIT
trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM
trap 'cleanup; exit 129' HUP

# ---- the run record (the run-record unit) --------------------------------------------------------
# The runner used to forget everything on exit: the per-leg results lived in $WORK, which the trap
# above deletes, and the three files that survived were prose for a human. The record is a directory
# of small append-once files another session can read DURING the run and after a crash.
#
# PER-RUN, never a fixed path, and that is a correctness property rather than tidiness. The `.rc`
# file is the DISPATCH SUPPRESSOR — the loop below skips any leg that already has one — so a
# leftover at a fixed path makes the runner skip a leg and print it green. Per-run uniqueness is what
# makes that impossible; nothing is cleared at the start of a run, because a start-of-run clear can
# partially fail on this platform against an open handle or an AV lock and inherit the previous run's
# verdicts, which is the same defect wearing a different hat.
GATE_RUN_KEEP=${GATE_RUN_KEEP:-5}
# DECLARED with its reasoning, not an unnamed number. Five is enough that a crashed run's record —
# the one with a header and no verdict — survives the two or three ordinary runs an operator does
# before they come back to look at it, and small enough that a header, one row per leg and a verdict
# cannot grow the git dir without practical limit.
RUNROOT=""; RUNDIR=""; RUNID=""
# THE COMPLETION FILE STAYS IN THE SCRATCH DIR, and the durable record does not hold one. This is
# the one place this unit's spec asked for something its own reasoning argues against, and the
# arm for it is what found the disagreement rather than a reading of the text.
#
# The spec asked for the completion files to MOVE into the run directory, on the reasoning that
# the file is the DISPATCH SUPPRESSOR and not a log — the loop below skips any leg that already
# has one, so a leftover makes the runner skip a leg and print it green. That reasoning is right,
# and it is an argument for keeping the suppressor OUT of the durable record: a `mktemp -d` name
# nothing outside this process can predict cannot be planted, while a run directory has a
# NAMEABLE path, and this runner accepts a pinned id through `GATE_RUN_ID`. Moving the suppressor
# somewhere addressable re-opened the hole the move was meant to close.
#
# The two jobs the file was doing come apart cleanly: suppression is per-run and must be
# unforgeable, durability is per-leg and must survive the process. The `.leg` row below is the
# durable half and it is written before the completion signal, so the record loses nothing.
# Measured: with the suppressor in the run directory, a planted `<i>.rc` suppressed its leg and
# the run reported the plant's verdict as the leg's own.
if [ -n "$gd" ]; then
  # The id is seamed for the ARM, not for the runner: an arm that plants a stale completion file has
  # to know which directory the run will open, and without the seam the plant lands somewhere the run
  # never looks and the arm passes by finding nothing.
  RUNID="${GATE_RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)-$$}"
  RUNROOT="$gd/gate-run"
  RUNDIR="$RUNROOT/$RUNID"
  if mkdir -p "$RUNDIR" 2>/dev/null; then
    chmod 700 "$RUNDIR" 2>/dev/null || true
    RC="$RUNDIR"
    printf '%s' "$RUNID" > "$RUNROOT/current.tmp" 2>/dev/null && mv -f "$RUNROOT/current.tmp" "$RUNROOT/current" 2>/dev/null || true
  else
    # Creating the run directory fails the run the way the `mktemp -d` it sits beside already does.
    echo "run-gates: cannot create the run record at $RUNDIR" >&2; exit 2
  fi
fi

FPRINT="$KITREL/gate-fingerprint.sh"
fingerprint() { [ -f "$FPRINT" ] || { printf ''; return; }; bash "$FPRINT" "$@" 2>/dev/null; }
FPRINT_START=$(fingerprint)
# CLEAN means `git status --porcelain` EMPTY, untracked-and-unignored files included — the same
# predicate the fingerprint's own porcelain component is computed from. The obvious `git diff
# --quiet` pair ignores untracked files, and a record written from a tree with a `??` line in it
# carries a digest whose porcelain component is non-empty, which the at-a-rev form cannot reproduce
# at any sha. The push boundary would then mismatch on every later push and force the full bar
# forever while printing that the record describes a different tree — safe, permanent, and it reads
# as caution rather than as the defect it is.
# ONE PORCELAIN WALK, read by everything that needs it. Three separate `git status --porcelain`
# calls accumulated here — one for the clean test, one for the per-leg input keys, and one inside
# the fingerprint helper — and a status walk over a real tree is the expensive part of this
# runner's startup. Measured before this fold: 2136 ms from process start to the header being on
# disk, in a scratch repo with two files. The helper keeps its own walk because it is a separate
# executable a git hook calls directly and must be self-contained; the other two are the same
# question asked twice.
PORCELAIN_START=$(LC_ALL=C git status --porcelain 2>/dev/null | LC_ALL=C sort)
# CLEAN means this listing EMPTY, untracked-and-unignored files included — not `git diff --quiet`,
# which is blind to a `??` line and would stamp a green over a tree the at-a-rev fingerprint form
# cannot reproduce at any sha.
TREE_CLEAN=no
[ -z "$PORCELAIN_START" ] && TREE_CLEAN=yes

# Read the leg manifest as name<RS>guard(comma-joined)<RS>argv(joined by <US>) per line, where
# RS=\x1e and US=\x1f (non-whitespace, so an empty guard field survives `read`; a tab would collapse).
# Line 1 is the advisory DISPATCH ORDER: leg indices longest-first from the timing cache the previous
# run wrote. A leg the cache does not know scores 0 and sorts last; an absent or unreadable cache
# yields manifest order. It is a scheduling hint only — it can never change a verdict.
# Command-substitution surfaces a parse failure (a `< <()` process-sub would swallow it).
legs=$("$PYBIN" -c '
import json, os, sys
try:
    data = json.load(open(sys.argv[1]))
except Exception as e:
    sys.stderr.write("parse error: %s\n" % e); sys.exit(3)
if not isinstance(data, list) or not data:
    sys.stderr.write("gate-legs.json empty or not a list\n"); sys.exit(3)
durs = {}
cache = sys.argv[2] if len(sys.argv) > 2 else ""   # argv[1] is the MANIFEST; the cache is argv[2]
if cache and os.path.exists(cache):
    try:
        for line in open(cache, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 2: durs[p[0]] = float(p[1])
    except Exception:
        durs = {}          # a corrupt cache is a missing cache, never a failed run
order = sorted(range(len(data)), key=lambda i: -durs.get(data[i]["name"], 0.0))
rows = [" ".join(str(i) for i in order)]
# The fourth field is the `impure` declaration, carried through as a PRESENCE rather than as its
# text: the reason string is for a human reading the manifest, and the runner only ever asks whether
# there is one. Newlines and the field separators cannot appear in it because it is reduced to a flag
# here, which is what keeps a prose reason from being able to corrupt the wire format.
# The SIXTH field is `subject`, appended AFTER chunk so the chunk position is unchanged — a field
# inserted before it would be parsed as chunk by any reader that had not moved in the same commit.
# Defaulted to `repo`: a leg that has not declared is on the bar, because the other default silently
# removes an undeclared leg from every run. NOTE: this program is inside a single-quoted shell block,
# so a comment here may carry no apostrophe. TOOL-dUnstalledConvoy-26.
#
# THE CRITERION, and it is the ONE statement of it. Ask what a FAILURE of this leg MEANS:
#
#   "the kit source is broken"          -> subject = kit   (held; the owner asks for it)
#   "this repository is misconfigured"  -> subject = repo  (on the bar, every run)
#
# Asking instead what a leg TESTS is the wording that does not decide, and it decided four legs
# wrongly before this sentence replaced it. A kit whose product is a repository configuration —
# the push and commit boundaries are the case — has a self-test that reads BOTH the kit source and
# the live hook installed here, so "what does it test" has two true answers and the failure question
# has one. Those four legs are `repo`: a broken boundary in THIS repository cannot wait for somebody
# to remember a variable. TOOL-dUnstalledConvoy-30.
rows += [l["name"] + "\x1e" + ",".join(l.get("guard", [])) + "\x1e" + "\x1f".join(l["argv"])
         + "\x1e" + ("1" if l.get("impure") else "")
         + "\x1e" + str(l.get("chunk", "") or "")
         + "\x1e" + (l.get("subject") or "repo")
         # THE SEVENTH FIELD, appended after `subject` for exactly the reason `subject` was appended
         # after `chunk`: a field inserted before an existing one is parsed AS that one by any reader
         # that has not moved in the same commit. EMPTY when the leg declares none, which is legal and
         # is what an adopter emitted manifest carries until the deployer learns the key
         # (TOOL-aBoundedCeiling-5). A non-integer or non-positive value reads as absent rather than
         # as zero: `timeout 0` means NO timeout, so coercing junk to 0 would silently unbound the one
         # leg whose declaration was malformed.
         + "\x1e" + (str(l["ceiling"]) if isinstance(l.get("ceiling"), int)
                            and not isinstance(l.get("ceiling"), bool) and l["ceiling"] > 0 else "")
         for l in data]
sys.stdout.buffer.write(("\n".join(rows) + "\n").encode())   # LF bytes (Windows text stdout is CRLF); \x1e field sep is non-whitespace so an empty guard field is preserved (a tab would collapse)
' "$LEGS_FILE" "$TIMINGS") || { echo "run-gates: cannot parse $LEGS_FILE"; exit 2; }

# Rows stay 1:1 with the manifest so the dispatch indices address the same legs the reader reports.
# An empty name is the drop-sentinel: kept in the arrays to hold the index, never run and never counted.
names=(); guards=(); argvs=(); impures=(); chunks=(); subjects=(); ceilings=(); ORDER=""; first=1
while IFS= read -r line; do
  if [ "$first" = 1 ]; then ORDER=$line; first=0; continue; fi
  IFS=$'\x1e' read -r nm gd_ av im ch sj ce <<<"$line"
  names+=("$nm"); guards+=("$gd_"); argvs+=("$av"); impures+=("${im:-}"); chunks+=("${ch:-default}")
  subjects+=("${sj:-repo}"); ceilings+=("${ce:-}")
done <<<"$legs"
total=${#names[@]}

# UNBOUNDED LEGS ARE REPORTED, NEVER REFUSED. TOOL-aBoundedCeiling-1 S6. The runner cannot know
# whether a row with no ceiling is a gov leg somebody forgot or an adopter leg the deployer has no
# business bounding, and a refusal it cannot justify is a refusal that reds a tree for a field it
# has no way to supply -- the class the shipped canary header names. So this is a COUNT on the
# profile line, which is where an operator already reads this run's knobs. The DECLARATION
# requirement over gov's own corpus is S9, in run-gates.gov.test.sh, which is the suite allowed to
# hold a claim about this repository.
# Guard evaluation runs SERIALLY and up front: it is a read-only `git diff` per guarded leg, and
# deciding before dispatch keeps the skip verdict independent of scheduling.
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  # SUBJECT FIRST, and in this pass rather than in the dispatch loop. A kit-subject leg tests the
  # KIT'S OWN SOURCE and has no job in a repo that copy-installs the kit and never edits it, so it
  # runs only when asked. `GATE_FULL` deliberately does NOT ask: it means "ignore every guard", and
  # conflating it with "run the kit's own tests" would leave no way to request a complete bar
  # without them — and it is the very bypass that made `guard = ["{kit}/"]` ineffective here.
  # Deciding in the dispatch loop instead would leave an index with no result, which the reporting
  # pass reports as `(no result)`. TOOL-dUnstalledConvoy-26.
  #
  # THE CHUNK IS HELD TOO, by owner ruling 2026-08-26: EVERY self-test is on demand, not just the
  # kit-subject ones. The `subject = kit` predicate alone left SIX legs in the `selftests` chunk
  # running on every bar, because they carry `subject = repo` — the two hook self-tests, the
  # push-main self-test, the recall floor arms and the two run-gates canaries. Each is a `.test.sh`
  # or `test_*.py` that exercises a checker's own source, which is the thing this hold is for, and
  # the split by subject was grading WHOSE source rather than WHAT KIND of leg it is.
  #
  # WHAT THIS COSTS, stated rather than discovered later: the two run-gates canaries are the bar's
  # own liveness assertion — the arms that catch a guard naming an untracked path, which would
  # otherwise skip forever and silently. Holding them means a default bar no longer proves it can
  # move. That is a real reduction in what a green means, it is the owner's call, and
  # `GATE_SELFTESTS=1` remains the way to ask for it. The push boundary is where it matters, and
  # `.githooks/pre-push` decides there against a recorded green whose `selftests` key says whether
  # the recorded run had them held.
  if { [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; } \
     && [ -z "${GATE_SELFTESTS:-}" ]; then
    printf 'ondemand' > "$WORK/$i.rc"; continue
  fi
  [ -z "${guards[$i]}" ] && continue
  IFS=, read -ra gp <<<"${guards[$i]}"
  changed "${gp[@]}" || printf 'skip' > "$WORK/$i.rc"
done

# UNBOUNDED LEGS ARE REPORTED, NEVER REFUSED, and counted over the legs that will actually RUN.
# The runner cannot tell a leg somebody forgot from an adopter leg the deployer has no business
# bounding, so a refusal it cannot justify would red a tree for a field it has no way to supply.
# Counted HERE rather than at parse time: before the hold and guard passes the count is a fact about
# the manifest, and this line claims to be a fact about the run. TOOL-aBoundedCeiling-1 S6.
unbounded=0; willrun=0
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  [ -f "$WORK/$i.rc" ] && continue          # already held, skipped or reuse-marked: it will not run
  willrun=$((willrun + 1))
  [ -n "${ceilings[$i]:-}" ] || unbounded=$((unbounded + 1))
done
[ "$unbounded" -gt 0 ] && printf 'run-gates: %s of %s legs that will run declare no ceiling and run unbounded\n' "$unbounded" "$willrun" >&2

# The per-leg INPUT KEY: "what did this leg's verdict depend on". Written here and CONSUMED by
# the reuse unit, which is what makes the two units' authority explicit rather than assumed —
# that unit defines what the key means, this one is where the value is in scope to compute.
#
# A guarded leg is keyed on its own guard pathspecs; an unguarded leg declares by its silence
# that it reads everything, so it is keyed on the whole-tree fingerprint. Both also take the
# argv and the resolved base, because the same paths run by a different command, or diffed
# against a different baseline, are not the same question.
#
# INDEX-AND-STATUS rather than a hash of every file: `ls-files -s` is one cheap git call per leg
# and reads no file content, and the porcelain slice below is taken from the ONE whole-tree
# status the run already ran. Hashing each guarded file per leg would have re-read most of the
# tree fifty times to produce a key nothing yet consumes.
#
# Empty fingerprint means we could not measure the tree, and an unmeasurable input is NOT a
# reusable one: the key is a dash, which the reuse unit must treat as "never matches".
input_key() { # leg index -> the key, or a dash
  local i=$1 gp comp dirt
  [ -n "$FPRINT_START" ] || { printf '%s' -; return; }
  if [ -n "${guards[$i]}" ]; then
    IFS=, read -ra gp <<<"${guards[$i]}"
    comp=$(git ls-files -s -- "${gp[@]}" 2>/dev/null | LC_ALL=C sort) || comp=""
    # The guard's share of the dirt. Without it a guarded leg's key would not move when a
    # guarded file is edited but not committed, which is most of the edits a developer makes.
    dirt=$(printf '%s\n' "$PORCELAIN_START" | LC_ALL=C grep -F -e "${gp[0]}" 2>/dev/null) || dirt=""
    local g; for g in "${gp[@]:1}"; do
      dirt="$dirt$(printf '%s\n' "$PORCELAIN_START" | LC_ALL=C grep -F -e "$g" 2>/dev/null)"
    done
    comp="$comp
$dirt"
  else
    comp="$FPRINT_START"
  fi
  printf '%s\n---\n%s\n---\n%s\n' "${argvs[$i]}" "$BASE" "$comp" \
    | git hash-object --stdin 2>/dev/null || printf '%s' -
}

# THE HEADER, written before the first leg dispatches, in a key-per-line grammar. It is what a
# concurrent reader resolves through `gate-run/current` while the run is in flight, and what
# survives a crash to say what the run WAS when the verdict never arrived.
if [ -n "$RUNDIR" ]; then
  {
    printf 'schema\t1\n'
    printf 'run_id\t%s\n' "$RUNID"
    printf 'started\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'head\t%s\n' "$(git rev-parse HEAD 2>/dev/null)"
    printf 'base\t%s\n' "$BASE"
    printf 'base_from\t%s\n' "${GATE_BASE:+GATE_BASE}${GATE_BASE:-origin/${DEFBR:-main}}"
    printf 'fingerprint\t%s\n' "$FPRINT_START"
    printf 'tree_clean\t%s\n' "$TREE_CLEAN"
    printf 'manifest\t%s\n' "$LEGS_FILE"
    printf 'manifest_blob\t%s\n' "$(git hash-object -- "$LEGS_FILE" 2>/dev/null)"
    printf 'full\t%s\n' "${GATE_FULL:+1}"
    printf 'full_from\t%s\n' "${GATE_FULL:+GATE_FULL}"
    # THE RUN ENVELOPE IS FOUR KEYS, NOT ONE. The width alone was what an earlier draft recorded,
    # written when the width was a number this script computed. It is now a DECLARED row, so a
    # later reader comparing two runs needs the row NAME, the resolved width, the per-leg timeout
    # and the detection source to tell a re-detected row from a GATE_JOBS override. These are the
    # components of PROF_LINE rather than a second derivation of the same four values.
    printf 'profile_row\t%s\n' "$PROF_NAME"
    printf 'width\t%s\n' "$JOBS"
    printf 'leg_timeout\t%s\n' "$PROF_TIMEOUT"
    # THE REGIME the legs actually ran under, beside the profile knob rather than instead of it: the
    # knob is an input a later reader may want, and the regime is what the run did.
    printf 'leg_ceilings\t%s\n' "$([ "$CEILINGS_LIVE" = 1 ] && echo live || echo inert)"
    printf 'profile_from\t%s\n' "$PROF_TAG"
    printf 'legs\t%s\n' "$total"
    printf 'worktree\t%s\n' "$(git rev-parse --show-toplevel 2>/dev/null)"
    # THE QUEUE WAIT, paired value and source, in the header's own `value`/`_from` grammar —
    # `base`/`base_from`, `full`/`full_from`, `profile_row`/`profile_from`. Fourth instance.
    # DELIBERATELY OUTSIDE the run-envelope block above: `run-gates.evidence.test.sh` asserts that
    # block is four keys and selects them BY NAME, so a key added inside would leave that arm green
    # and only its comment lying. `schema` does not bump — every reader selects by key name, so an
    # additive key breaks none, and a bump could not be armed because nothing reads the field.
    printf 'queued\t%s\n'      "$QUEUED"
    printf 'queued_from\t%s\n' "$QUEUED_FROM"
    # The RESOLVED dispatch order, recorded here because this is the point at which it is in
    # scope. The chunking unit's ordering criteria read it from the record rather than
    # re-deriving it, which is what keeps the record's key set single-sourced.
    printf 'dispatch\t%s\n' "$ORDER"
  } > "$RUNDIR/header.tmp" 2>/dev/null && mv -f "$RUNDIR/header.tmp" "$RUNDIR/header" 2>/dev/null || true
  chmod 600 "$RUNDIR/header" 2>/dev/null || true
fi

# ---- reuse a proven green (the reuse unit) -------------------------------------------------
# OPT-IN, and that is the boundary rule rather than caution: an advisory input may cause LESS work
# only on a run that is not authoritative. `.githooks/pre-push` never sets this, so the run that
# decides a landing always executes every leg it did not guard away.
#
# A leg is reused when ALL of: reuse is asked for, the leg is not declared `impure`, its ledger row
# says `ok`, that row carries a key, and the key equals the one computed THIS run. Any missing term
# means execute — every failure mode of this block is "did more work", never "checked less".
reuses=0
if [ -n "${GATE_REUSE:-}" ] && [ -n "$LEDGER" ] && [ -s "$LEDGER" ]; then
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.rc" ] && continue                 # already decided by the guard pass
    # An IMPURE leg is never reused, on any tree, however identical. Its verdict is a function of
    # something outside the tree, so a byte-identical tree is not the same question twice.
    [ -n "${impures[$i]}" ] && continue
    _row=$(LC_ALL=C grep -m1 -F "${names[$i]}"$'\t' "$LEDGER" 2>/dev/null) || _row=
    [ -n "$_row" ] || continue
    IFS=$'\t' read -r _n _sec _st _key _end <<<"$_row"
    [ "$_n" = "${names[$i]}" ] || continue
    [ "$_st" = ok ] || continue                      # a RED row is never reusable
    [ -n "$_key" ] && [ "$_key" != "-" ] || continue # no key recorded is not a match, it is a gap
    [ "$_key" = "$(input_key "$i")" ] || continue
    printf 'reuse' > "$WORK/$i.rc"
  done
fi

runleg() { # leg index — writes .out, then .sec, then ATOMICALLY .rc (the completion signal)
  local i=$1 s e out rc
  local argv; IFS=$'\x1f' read -ra argv <<<"${argvs[$i]}"
  case "${argv[0]}" in python|python3) argv[0]=$PYBIN ;; esac   # the manifest stores the canonical python3; run under the resolved PYBIN
  s=$(date +%s%N)
  # legs never read stdin — deny it so a stray reader can't hang the bar. The profile's per-leg
  # timeout wraps the exec when the selected row asks for one: a leg that outlives it exits 124 and
  # is reported RED naming itself, never skipped and never green. That is a COVERAGE improvement, not
  # a carve-out — an unbounded hang wedges the whole bar and names nothing.
  #
  # CAPTURED THROUGH A FILE, NOT A PIPE, and that is the whole difference between a bound and a
  # decoration. `out=$(timeout N cmd)` reads until EOF, and EOF arrives only when the LAST inherited
  # write end closes — so a surviving grandchild holds the pipe and the worker blocks for the entire
  # hang while `timeout` cheerfully reports 124. MEASURED on the first landing of this knob: 51.4 s
  # wall against a 1 s bound, indistinguishable from the same fixture with the timeout off. The
  # verdict was bounded and the clock was not, which is the one property the knob exists for.
  # `-k` follows for the child that ignores SIGTERM; the file read cannot block on anybody.
  # THE LEG'S OWN CEILING WINS, and the two bounds NEVER wrap one leg together: nested deadlines
  # both exit 124 and the verdict cannot then say which fired. `PROF_TIMEOUT` stays the fallback for
  # a leg that declares none, which is every leg in a manifest the deployer has not yet taught the
  # key. `bound` is also what report_one reads, so the number in the verdict is the number that
  # fired rather than a second lookup that could disagree with it. TOOL-aBoundedCeiling-1.
  local bound=${ceilings[$i]:-}
  [ -n "$bound" ] || bound=$PROF_TIMEOUT
  # CEILINGS_LIVE is the liveness gate: with no runnable `timeout` a declared ceiling is INERT, and
  # the leg runs UNBOUNDED rather than being skipped. A knob may cost speed and may turn a hang into
  # a RED; it may never turn a leg into a pass or a skip (gate-profiles.txt, the governing invariant).
  [ "$CEILINGS_LIVE" = 1 ] || bound=0
  printf '%s' "$bound" > "$WORK/$i.bound"
  if [ "${bound:-0}" -gt 0 ]; then timeout -k 5s "$bound" "${argv[@]}" </dev/null >"$WORK/$i.raw" 2>&1; rc=$?
  else "${argv[@]}" </dev/null >"$WORK/$i.raw" 2>&1; rc=$?; fi
  out=$(cat "$WORK/$i.raw" 2>/dev/null)
  e=$(date +%s%N)
  # TOOL-dNomadicAtlas-1, ported into the worker: persist EVERY leg, not only the failing one — a
  # passing leg's output is what a later bisect reads, and the bytes are already in memory. Redacted,
  # because a terminal line is ephemeral and a file is not.
  local lf; lf="$(leg_log "${names[$i]}")" || lf=""
  if [ -n "$lf" ]; then
    { printf '# run-gates | leg %s | exit %s\n' "${names[$i]}" "$rc"; printf '%s\n' "$out"; } | redact >"$lf" 2>/dev/null || true
    chmod 600 "$lf" 2>/dev/null || true
  fi
  printf '%s\n' "$out" > "$WORK/$i.out"
  local secs; secs=$(printf '%s.%03d' "$(( (e-s)/1000000000 ))" "$(( ((e-s)/1000000)%1000 ))")
  printf '%s\n' "$secs" > "$WORK/$i.sec"
  # THE DURABLE HALF. One TSV row per leg and one copy of its output, both inside the run
  # directory, and both written BEFORE the completion signal so a concurrent reader that sees
  # `.rc` sees a complete row rather than a half-written one.
  if [ -n "$RUNDIR" ]; then
    # The output copy takes the SAME redaction and the SAME restrictive mode its `gate-logs`
    # sibling already has. It is the same bytes with a longer life, and a durable copy that skips
    # the masking its sibling applies is a credential leak the old scratch-dir lifetime was
    # merely hiding.
    { printf '# run-gates | leg %s | exit %s\n' "${names[$i]}" "$rc"; printf '%s\n' "$out"; } \
      | redact >"$RUNDIR/$i.out" 2>/dev/null || true
    chmod 600 "$RUNDIR/$i.out" 2>/dev/null || true
    local st; case "$rc" in 0) st=ok ;; *) st=fail ;; esac
    # TAB-SEPARATED and NEWLINE-FREE by construction: every field is a leg name, a token, a
    # number or a digest. The leg name is the only one an author controls, and the canary
    # already forbids a tab inside one.
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "${names[$i]}" "$st" "$rc" "$secs" "$s" "$e" "$(input_key "$i")" \
      > "$RUNDIR/$i.leg.tmp" 2>/dev/null \
      && mv -f "$RUNDIR/$i.leg.tmp" "$RUNDIR/$i.leg" 2>/dev/null || true
  fi
  # THE ONE HEARTBEAT SITE, and it is here rather than in the reader loop because this is the
  # event the TTL is sized against: S4 refreshes at a leg COMPLETING, so "can the holder still be
  # holding" and "has a leg finished lately" are the same question. A second site in the reader
  # loop would refresh while no leg was making progress, which is the state the reaper exists to
  # detect.
  ts_hb
  printf '%s' "$rc" > "$WORK/$i.rc.tmp" && mv -f "$WORK/$i.rc.tmp" "$WORK/$i.rc"
}

# THE TAIL CONTRACT (the run-gates promotion spec's S5). Every tailed line is `<verb>  <leg name>  <tail>`:
# TWO spaces before the parenthesised tail, on every verb, so a reader splits the remainder on a
# double space and gets the bare leg name back. A single space made that split return a TRUNCATED
# name for any leg whose name contains a space, which is most of them, and the deployer reads a
# target's verdicts exactly that way. The canary forbids a double space INSIDE a leg NAME, which is
# what keeps the split unambiguous rather than merely usually right. Every verb the sibling units
# add conforms: two spaces before any parenthesised tail.
report_one() { # leg index — emits exactly the line the serial bar has always emitted
  local i=$1 rc ftail
  n=$((n+1))
  if [ ! -f "$WORK/$i.rc" ]; then
    fails=$((fails+1)); c_ran=$((c_ran+1)); c_fail=$((c_fail+1)); printf 'GATE FAIL  %s  (no result)\n' "${names[$i]}"
    FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]}  (no result)"$'\n'; return
  fi
  rc=$(cat "$WORK/$i.rc")
  if [ "$rc" = ondemand ]; then
    # THE FIFTH VERB, and it is NOT `skip`. Two reasons, both load-bearing. `skip`'s tail says
    # `unchanged vs <branch>`, which is false here — the leg is not unchanged, it is out of subject —
    # and `skips` is conjoined into the `gate-full-green` stamp, so counting an on-demand skip there
    # would silence the stamp and pin `.githooks/pre-push` into forcing a full run forever.
    ondemands=$((ondemands+1)); c_ondemand=$((c_ondemand+1))
    printf 'GATE held  %s  (self-test, set GATE_SELFTESTS=1 to run)\n' "${names[$i]}"
  elif [ "$rc" = skip ]; then
    skips=$((skips+1)); c_skip=$((c_skip+1)); printf 'GATE skip  %s  (unchanged vs %s)\n' "${names[$i]}" "${DEFBR:-baseline}"
  elif [ "$rc" = reuse ]; then
    # THE FOURTH VERB, padded to the same column as the other three and following the two-space tail
    # contract: a reader splits the remainder on a double space and gets the bare leg name back.
    reuses=$((reuses+1)); c_reuse=$((c_reuse+1)); printf 'GATE reuse %s  (proven green, inputs unchanged)\n' "${names[$i]}"
  elif [ "$rc" = 0 ]; then c_ran=$((c_ran+1)); printf 'GATE ok    %s\n' "${names[$i]}"
  else fails=$((fails+1)); c_ran=$((c_ran+1)); c_fail=$((c_fail+1))
       # `timeout` exits 124 on the TERM, and 137 once `-k` escalates to KILL — which is exactly the
       # leg the kill-after exists for, so mapping only 124 left the worst case reported as a bare
       # exit code. Both stay behind the PROF_TIMEOUT guard, so a leg that chooses either for its own
       # reasons is still reported as the code it chose.
       # THE BOUND THAT ACTUALLY FIRED, read from what runleg recorded rather than re-derived. The
       # old spelling read `PROF_TIMEOUT` for both the guard and the number, so once a leg carried
       # its own ceiling and PROF_TIMEOUT stayed 0 -- which is every shipped profile row -- a killed
       # leg reported a bare `(exit 124)` naming nothing. TOOL-aBoundedCeiling-1.
       local fired; fired=$(cat "$WORK/$i.bound" 2>/dev/null || printf 0)
       ftail="(exit $rc)"
       { [ "$rc" = 124 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s)"
       { [ "$rc" = 137 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s, killed)"
       printf 'GATE FAIL  %s  %s\n' "${names[$i]}" "$ftail"; sed 's/^/    /' "$WORK/$i.out"
       FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]}  $ftail"$'\n'   # TOOL-aLeasedGauntlet-1 S3: keep for the durable summary
       # TOOL-dNomadicAtlas-1: a POINTER at the leg's own output, so the durable summary answers WHY
       # and not only WHICH. A pointer, never the bytes — this file is what an operator quotes.
       lf="$(leg_log "${names[$i]}")" && [ -n "$lf" ] && FAILED_LEGS="${FAILED_LEGS}    log: $lf"$'\n'; fi
}

# Dispatch and report from ONE shell, so this shell owns every worker and can BLOCK on `wait -n`
# rather than poll for results. That is not a style preference: a poll tick costs a `sleep` PROCESS,
# measured at ~75ms for a 50ms sleep on this platform, and an earlier revision that polled every 50ms
# spent ~317s of a 617s serial run doing nothing but spawning them.
# Dispatch order is the advisory longest-first hint; REPORTING walks the manifest, so a leg prints
# only once every leg before it has printed.
# ---- CHUNKS BOUND REPORTING, NEVER DISPATCH (the chunking unit) --------------------------------
# The bar is FLOOR-bound: one leg is most of the wall clock, so no ordering of the other eighty-odd
# moves it. Reordering dispatch was specced and then CUT on that measurement, and what survives is
# the half the measurement supports — a reviewable verdict per chunk instead of one verdict at the
# end, on a bar where the first line used to appear minutes in.
#
# So legs run at full pool width in whatever order the longest-first hint gives, across chunk lines
# freely. Only the READER'S walk changes: from the raw index range to a flattened chunk-then-manifest
# list. Chunk ORDER is order of FIRST APPEARANCE in the manifest — no second declaration file, no
# order field, and a leg with no key falls into `default`.
#
# The manifest is deliberately NOT grouped, so this flattening is a real permutation rather than an
# identity. That is what makes the grouping observable at all, and it is why the whole-manifest
# reorder could be cut without costing this unit anything.
CHUNK_ORDER=""
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  case " $CHUNK_ORDER " in *" ${chunks[$i]} "*) ;; *) CHUNK_ORDER="$CHUNK_ORDER ${chunks[$i]}" ;; esac
done
WALK=()
for c in $CHUNK_ORDER; do
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ "${chunks[$i]}" = "$c" ] && WALK+=("$i")
  done
done
nwalk=${#WALK[@]}

disp=($ORDER); ndisp=${#disp[@]}; di=0; wi=0; next=0
[ "$nwalk" -gt 0 ] && next=${WALK[0]}
# per-chunk tallies, reset at each boundary
cur_chunk=""; c_ran=0; c_fail=0; c_skip=0; c_reuse=0; c_ondemand=0; c_t0=$(date +%s)
CHUNK_ROLLUP=""
chunk_close() {   # emit the verdict for the chunk just finished
  [ -n "$cur_chunk" ] || return 0
  local secs=$(( $(date +%s) - c_t0 )) verdict
  if   [ "$c_fail" -gt 0 ]; then verdict="RED"
  # A CHUNK IN WHICH EVERY LEG WAS SKIPPED REPORTS AS SKIPPED, never as green. On a scoped run the
  # guard pre-pass decides those legs before dispatch, so the chunk closes at once — and calling that
  # green would be the loudest possible green-by-absence, one altitude above a single leg.
  # A HELD LEG IS A LEG THAT DID NOT RUN, so it satisfies this rule exactly as a guard-skip does.
  # The rule above was already correct and already stated; what it lacked was reachability from the
  # newer skip kind, which is worse than a missing rule because the comment asserts it. A chunk of
  # nothing but kit self-tests closed GREEN on every switch-off bar. TOOL-dUnstalledConvoy-32.
  elif [ "$c_ran" = 0 ] && [ "$c_reuse" = 0 ] && { [ "$c_skip" -gt 0 ] || [ "${c_ondemand:-0}" -gt 0 ]; }; then verdict="skipped"
  else verdict="green"; fi
  # HELD IS ITS OWN TALLY and not folded into `skipped`, for the reason the leg verb is its own verb:
  # the two have different remedies. A guard-skip runs again when its path moves; a held leg runs
  # when somebody sets the variable, and a reader who cannot tell them apart waits for the wrong one.
  printf -- '---- chunk %s: %s  (%s ran, %s failed, %s skipped, %s reused, %s held)\n' \
    "$cur_chunk" "$verdict" "$c_ran" "$c_fail" "$c_skip" "$c_reuse" "${c_ondemand:-0}"
  # PER-CHUNK WALL TIME goes to the durable records and NOT to stdout: a wall clock on a terminal
  # line invites comparison between runs that are not comparable, which is the whole reason the
  # profiling verb records an envelope.
  CHUNK_ROLLUP="${CHUNK_ROLLUP}chunk\t${cur_chunk}\t${verdict}\t${c_ran}\t${c_fail}\t${c_skip}\t${c_reuse}\t${c_ondemand:-0}\t${secs}\n"
  cur_chunk=""; c_ran=0; c_fail=0; c_skip=0; c_reuse=0; c_ondemand=0; c_t0=$(date +%s)
}
live() { jobs -rp | wc -l; }
while [ "$wi" -lt "$nwalk" ]; do
  next=${WALK[$wi]}
  # THE CHUNK BOUNDARY. The walk is grouped, so a change of chunk here is the end of the previous
  # one — every leg of it has printed, because the reader never advances past a leg with no result.
  if [ "${chunks[$next]}" != "$cur_chunk" ]; then chunk_close; cur_chunk=${chunks[$next]}; fi
  di_before=$di
  while [ "$di" -lt "$ndisp" ] && [ "$(live)" -lt "$JOBS" ]; do
    k=${disp[$di]}; di=$((di+1))
    { [ -z "${names[$k]}" ] || [ -f "$WORK/$k.rc" ]; } && continue   # sentinel, or already decided by the guard pass
    runleg "$k" &
  done
  if [ -f "$WORK/$next.rc" ]; then report_one "$next"; wi=$((wi+1)); continue; fi
  if [ "$(live)" -gt 0 ]; then wait -n 2>/dev/null || true; continue; fi
  # Nothing running. That is NOT yet evidence this leg has no result: `jobs -rp` counts only RUNNING
  # jobs, so a worker that finished between the file check and the count is invisible, and with
  # instant legs the pool can drain faster than the reader walks. Exhaust dispatch, reap everything,
  # and re-check before declaring a leg dead — an earlier revision skipped this and reported a
  # perfectly healthy leg as "(no result)" roughly one run in three.
  if [ "$di" -lt "$ndisp" ]; then
    # Nothing is running and legs remain. Normally the pass above dispatched one; if it dispatched
    # NOTHING, force one here so every iteration makes progress and the loop can never spin.
    # Falling through to the report instead would declare an UNDISPATCHED leg dead, and that is not
    # hypothetical: guarding on "did this pass advance?" did exactly that. The window is a worker
    # that is live when the dispatch pass looks (so nothing dispatches) and finished by the liveness
    # check (so nothing is waited on), and the timing cache makes it common by decoupling dispatch
    # order from manifest order — measured at 6 of 30 legs falsely reported, on the second run only,
    # because the first run is the one with no cache.
    if [ "$di" -eq "$di_before" ]; then
      k=${disp[$di]}; di=$((di+1))
      if [ -n "${names[$k]}" ] && [ ! -f "$WORK/$k.rc" ]; then runleg "$k" & fi
    fi
    continue
  fi
  wait                                     # everything dispatched and nothing running: reap, look once more
  [ -f "$WORK/$next.rc" ] && continue
  report_one "$next"; wi=$((wi+1))         # genuinely no result: report it, never hang
done
wait
chunk_close                                # the last chunk has no successor to close it

# THE LEDGER. It replaces the old `gate-timings.tsv` rather than sitting beside it: two stores of
# one fact, with the older one read by the only tool that grades the newer, is exactly the shape
# this record exists to remove. Field 2 is still the duration, which is what lets the manifest
# parser above read it as a dispatch hint with no edit at all.
#
# Rows: name, seconds, status, input key, ended-at. Advisory for dispatch, DURABLE for the reuse
# unit that reads the key — a failed write costs wall clock, never a verdict.
if [ -n "$LEDGER" ]; then
  new="$WORK/ledger.new"; merged="$WORK/ledger.merged"; : > "$new"
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.sec" ] || continue
    lst=ok; lkey=-; lend=""
    if [ -n "$RUNDIR" ] && [ -f "$RUNDIR/$i.leg" ]; then
      IFS=$'\t' read -r _ lst _ _ _ lend lkey < "$RUNDIR/$i.leg" 2>/dev/null || { lst=ok; lkey=-; }
    fi
    # A RED leg is never reusable, and the ledger says so in the field the reuse unit reads
    # rather than leaving that rule to be re-implemented there. A key on a failed row would be a
    # true statement about the inputs and a dangerous one about the verdict.
    [ "$lst" = ok ] || lkey=-
    printf '%s\t%s\t%s\t%s\t%s\n' "${names[$i]}" "$(cat "$WORK/$i.sec")" "$lst" "$lkey" "$lend" >> "$new"
  done
  # A guard-SKIPPED leg never enters runleg(), so it produces no .sec. Rewriting the file from this
  # run's rows alone therefore DELETED the cached duration of every skipped leg — and the runs where
  # guards fire are exactly the diff-scoped ones, so a scoped run blanked the dispatch hint the next
  # full run depends on. Carry forward any cached row this run did not measure. A leg dropped from the
  # manifest falls out on its own, because the python side keys the hint on the manifest's names.
  cp "$new" "$merged" 2>/dev/null || true
  [ -s "$LEDGER" ] && awk -F'\t' 'NR==FNR{seen[$1]=1;next} !($1 in seen)' "$new" "$LEDGER" >> "$merged" 2>/dev/null
  # ATOMIC rather than a copy in place. A reader that opens the ledger while the bar is mid-write
  # got a truncated file before; a rename is the only way this file is ever replaced now.
  mv -f "$merged" "$LEDGER" 2>/dev/null || cp "$merged" "$LEDGER" 2>/dev/null || true
fi

echo "----"
skipnote=""; [ "$skips" -gt 0 ] && skipnote=" ($skips skipped)"
[ "${reuses:-0}" -gt 0 ] && skipnote="$skipnote (${reuses} reused)"
# THE HELD LEGS ARE NAMED, exactly as a guard-skip and a reuse are, and for the same reason: a
# total that shrank silently reads as a bar that shrank for reasons nobody recorded. Naming the
# population is what keeps the smaller number from being a smaller lie. TOOL-dUnstalledConvoy-31.
[ "${ondemands:-0}" -gt 0 ] && skipnote="$skipnote (${ondemands} held: every self-test, GATE_SELFTESTS=1 runs them)"

# THE COUNT THAT RAN, computed ONCE and read by the verdict record, the durable summary and stdout.
# Three call sites recomputing one figure is how two of them end up disagreeing, and this figure is
# the one a reader quotes. A leg that was held did not run, so counting it in the total is the
# green-by-absence class stated as arithmetic. TOOL-dUnstalledConvoy-31.
ran=$((n-skips-${ondemands:-0}))

# A BAR THAT RAN NOTHING BECAUSE EVERYTHING WAS HELD IS NOT A GREEN BAR. It is the loudest possible
# green-by-absence: a repository whose whole manifest is kit-subject would print `gates GREEN` on
# every run forever while executing not one leg, and the record it stamps would say so too.
# NARROW ON PURPOSE — guard-skips and reuses are ORDINARY reasons for a leg not to run, and a scoped
# run over an untouched tree legitimately executes nothing. This fires only when the on-demand hold
# is the SOLE reason: nothing ran, nothing was skipped, nothing was reused, and something was held.
# Exit 2, the runner's own configuration-refusal code, never 0 and never 1. TOOL-dUnstalledConvoy-26.
if [ "$fails" = 0 ] && [ "$ran" -le 0 ] && [ "${ondemands:-0}" -gt 0 ] \
   && [ "$skips" = 0 ] && [ "${reuses:-0}" = 0 ]; then
  echo "run-gates: every leg in this manifest is subject=kit and the self-tests were not asked for,"
  echo "run-gates: so this run executed NOTHING. Refusing to report a green over an empty population."
  echo "run-gates: run it as GATE_SELFTESTS=1, or give this manifest at least one repo-subject leg."
  # A VERDICT IS WRITTEN BEFORE THE EXIT. The run record's ABSENCE is this runner's crash signal —
  # a directory with a header and no verdict means the process died — so exiting between the two
  # manufactures that signature for a deliberate refusal, and leaves the PREVIOUS run's `gates
  # GREEN` standing in gate-last-summary.txt for anyone who reads the durable record instead of the
  # terminal. Both records say REFUSED instead. TOOL-dUnstalledConvoy-26.
  if [ -n "$RUNDIR" ]; then
    { printf 'ended\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
      printf 'verdict\tREFUSED\n'
      printf 'ran\t0\n'
      printf 'failed\t0\n'
      printf 'skipped\t%s\n' "$skips"
      printf 'held\t%s\n' "${ondemands:-0}"
      printf 'reused\t0\n'
    } > "$RUNDIR/verdict.tmp" 2>/dev/null && mv -f "$RUNDIR/verdict.tmp" "$RUNDIR/verdict" 2>/dev/null || true
    chmod 600 "$RUNDIR/verdict" 2>/dev/null || true
  fi
  [ -n "$sfile" ] && printf 'gates REFUSED — every leg is a held kit self-test, so this run executed nothing\n' >"$sfile" 2>/dev/null || true
  exit 2
fi

# ---- the verdict, the full-green stamp, and the sweep --------------------------------------
# `reuses` is the fourth full-green precondition, counted by the reuse verb above. A run that reused
# ANY leg has not proven the whole bar this time, so it cannot stamp a full green — which is what
# keeps the push boundary from ever resting on a verdict that was copied rather than earned.
reuses=${reuses:-0}
FPRINT_END=$(fingerprint)
tree_moved=no
[ -n "$FPRINT_START" ] && [ -n "$FPRINT_END" ] && [ "$FPRINT_START" != "$FPRINT_END" ] && tree_moved=yes
gate_verdict=GREEN; [ "$fails" = 0 ] || gate_verdict=RED

if [ -n "$RUNDIR" ]; then
  # WRITTEN LAST, and its ABSENCE is the crash signal — the only one needed. A run that dies
  # anywhere between the header and here leaves a directory with a header and no verdict, which
  # is unambiguous and costs no watchdog, no heartbeat and no second mechanism.
  {
    printf 'ended\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'verdict\t%s\n' "$gate_verdict"
    printf 'ran\t%s\n' "$ran"
    printf 'failed\t%s\n' "$fails"
    printf 'skipped\t%s\n' "$skips"
    printf 'held\t%s\n' "${ondemands:-0}"
    printf 'reused\t%s\n' "$reuses"
    printf 'fingerprint_end\t%s\n' "$FPRINT_END"
    printf 'tree_moved\t%s\n' "$tree_moved"
  } > "$RUNDIR/verdict.tmp" 2>/dev/null && mv -f "$RUNDIR/verdict.tmp" "$RUNDIR/verdict" 2>/dev/null || true
  chmod 600 "$RUNDIR/verdict" 2>/dev/null || true
fi

# THE FULL-GREEN STAMP, and its five preconditions are the whole of what makes its name true.
# An implementation that forgets ONE of them still passes every arm written for the others, which
# is why each has its own negative control in the evidence harness.
#
#   failed nothing  · skipped nothing  · reused nothing  · the tree did not move  · the tree was
#   CLEAN when the run started
#
# The last one is the one a spec audit found missing. A developer's ordinary full run on a dirty
# tree would otherwise stamp a green that the push boundary later treats as proof about a tree
# nobody ever tested.
if [ -n "$gd" ] && [ "$fails" = 0 ] && [ "$skips" = 0 ] && [ "$reuses" = 0 ] \
   && [ "$tree_moved" = no ] && [ "$TREE_CLEAN" = yes ] && [ -n "$FPRINT_START" ]; then
  {
    printf 'sha\t%s\n' "$(git rev-parse HEAD 2>/dev/null)"
    printf 'fingerprint\t%s\n' "$FPRINT_START"
    printf 'manifest_blob\t%s\n' "$(git hash-object -- "$LEGS_FILE" 2>/dev/null)"
    # WHAT THIS GREEN COVERED. Without it a record named `gate-full-green` cannot say
    # whether the kit-subject legs ran, and the push boundary would trust a partial bar as
    # a whole one. The READER of this field is TOOL-dUnstalledConvoy-27; written without
    # that reader it is an inert byte, which is what a spec audit caught rev-2 shipping.
    printf 'selftests\t%s\n' "${GATE_SELFTESTS:+1}"
    printf 'run_id\t%s\n' "$RUNID"
    printf 'stamped\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  } > "$gd/gate-full-green.tmp" 2>/dev/null \
    && mv -f "$gd/gate-full-green.tmp" "$gd/gate-full-green" 2>/dev/null || true
fi

# THE SWEEP runs AFTER the verdict is written and NEVER before the first leg dispatches. Both
# halves matter: sweeping at the start would delete the crashed run's record an operator came
# back to read, and it can partially fail on this platform against an open handle, which is how a
# start-of-run clear inherits the previous run's verdicts.
if [ -n "$RUNROOT" ] && [ -d "$RUNROOT" ]; then
  ls -1t "$RUNROOT" 2>/dev/null | grep -v '^current$' | tail -n "+$((GATE_RUN_KEEP+1))" | while IFS= read -r old; do
    [ -n "$old" ] && [ "$old" != "$RUNID" ] && rm -rf "$RUNROOT/$old" 2>/dev/null || true
  done
fi
# TOOL-aLeasedGauntlet-1 S3: write the verdict + failing-leg rows to a durable file (worktree-safe
# gitdir) so a `| tail`/`Select-Object -Last N` can't discard which leg failed.
if [ "$fails" = 0 ]; then
  # THE CHUNK ROLL-UP, with per-chunk wall time, goes into the DURABLE records and never to stdout.
  # A wall clock on a terminal line invites comparison between two runs that are not comparable —
  # the profiling verb exists precisely because a duration without its envelope is not a
  # measurement.
  # `QUEUE_SUMMARY` rides beside `PROF_LINE` on every path — green, red, and the durable RED copy —
  # UNCONDITIONALLY. A line that is present on some runs and absent on others means two things.
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf 'gates GREEN — %s/%s legs passed%s\n' "$ran" "$ran" "$skipnote"; } >"$sfile" 2>/dev/null || true
  echo "gates GREEN — $ran/$ran legs passed$skipnote"; exit 0
else
  # THE SAME DENOMINATOR THE GREEN LINE USES. `$n` is the whole manifest, so a red bar that held
  # 42 legs reported `1/85 legs failed` — a ratio against a population it never ran. The two lines
  # are read by the same person in the same terminal and a figure that changes meaning between them
  # is worse than either. TOOL-dUnstalledConvoy-31.
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE" >"$sfile"; printf '%s\n' "$QUEUE_SUMMARY" >>"$sfile"; printf '%b' "${CHUNK_ROLLUP:-}" >>"$sfile"; printf '%s' "${FAILED_LEGS:-}" >>"$sfile"; printf 'gates RED — %s/%s legs failed%s\n' "$fails" "$ran" "$skipnote" >>"$sfile"; } 2>/dev/null || true
  # TOOL-dNomadicAtlas-1: a SECOND copy on RED ONLY. gate-last-summary.txt is overwritten by every
  # run, so the reflexive "let me just re-run it" — which passes, when the red was a flake — erases
  # the evidence of the run that failed. This one is only ever overwritten by the next RED run.
  if [ -n "$gd" ]; then
    ffile="$gd/gate-last-failure.txt"
    { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf '%s' "${FAILED_LEGS:-}"; printf 'gates RED — %s/%s legs failed%s\n' "$fails" "$n" "$skipnote"; } >"$ffile" 2>/dev/null || true
    chmod 600 "$ffile" 2>/dev/null || true
  fi
  echo "gates RED — $fails/$ran legs failed$skipnote"
  [ -n "$sfile" ] && echo "gate summary saved to $sfile"
  [ -n "$gd" ] && [ -f "$gd/gate-last-failure.txt" ] && echo "gate failure record saved to $gd/gate-last-failure.txt"
  exit 1
fi
