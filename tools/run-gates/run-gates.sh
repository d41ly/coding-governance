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
KIT_RUN_GATES_VERSION=1.0   # gov:kit run-gates@1.0
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
fails=0; n=0; skips=0

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
BASE=$(git rev-parse --verify -q "${GATE_BASE:-origin/${DEFBR:-main}}" 2>/dev/null) || BASE=
# GATE_FULL bypasses every guard, so the run checks the whole bar. `.githooks/pre-push` sets it: a
# guard may only ever scope a NON-authoritative run, which is what makes a too-narrow guard cost an
# early signal rather than a wrong merge verdict. Both fail-safes below keep their meaning — an
# unresolvable BASE runs everything, and so does a guard that errors.
changed() { [ -n "${GATE_FULL:-}" ] && return 0; [ -z "$BASE" ] && return 0; ! git diff --quiet "$BASE" -- "$@" 2>/dev/null; }

gd="$(git rev-parse --git-dir 2>/dev/null)"; sfile=""; TIMINGS=""
[ -n "$gd" ] && { sfile="$gd/gate-last-summary.txt"; TIMINGS="$gd/gate-timings.tsv"; }
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
  local pages pgsz kb v lim
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
if [ "$PROF_TIMEOUT" -gt 0 ] && ! timeout 1 true >/dev/null 2>&1; then
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
PROF_LINE="gate profile: $PROF_NAME  ($prof_where; width $JOBS, timeout $prof_t; $PROF_TAG)"
echo "$PROF_LINE"

WORK=$(mktemp -d) || { echo "run-gates: cannot create a scratch dir"; exit 2; }
trap 'rm -rf "$WORK"' EXIT

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
rows += [l["name"] + "\x1e" + ",".join(l.get("guard", [])) + "\x1e" + "\x1f".join(l["argv"]) for l in data]
sys.stdout.buffer.write(("\n".join(rows) + "\n").encode())   # LF bytes (Windows text stdout is CRLF); \x1e field sep is non-whitespace so an empty guard field is preserved (a tab would collapse)
' "$LEGS_FILE" "$TIMINGS") || { echo "run-gates: cannot parse $LEGS_FILE"; exit 2; }

# Rows stay 1:1 with the manifest so the dispatch indices address the same legs the reader reports.
# An empty name is the drop-sentinel: kept in the arrays to hold the index, never run and never counted.
names=(); guards=(); argvs=(); ORDER=""; first=1
while IFS= read -r line; do
  if [ "$first" = 1 ]; then ORDER=$line; first=0; continue; fi
  IFS=$'\x1e' read -r nm gd_ av <<<"$line"
  names+=("$nm"); guards+=("$gd_"); argvs+=("$av")
done <<<"$legs"
total=${#names[@]}

# Guard evaluation runs SERIALLY and up front: it is a read-only `git diff` per guarded leg, and
# deciding before dispatch keeps the skip verdict independent of scheduling.
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  [ -z "${guards[$i]}" ] && continue
  IFS=, read -ra gp <<<"${guards[$i]}"
  changed "${gp[@]}" || printf 'skip' > "$WORK/$i.rc"
done

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
  if [ "$PROF_TIMEOUT" -gt 0 ]; then timeout -k 5s "$PROF_TIMEOUT" "${argv[@]}" </dev/null >"$WORK/$i.raw" 2>&1; rc=$?
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
  printf '%s.%03d\n' "$(( (e-s)/1000000000 ))" "$(( ((e-s)/1000000)%1000 ))" > "$WORK/$i.sec"
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
    fails=$((fails+1)); printf 'GATE FAIL  %s  (no result)\n' "${names[$i]}"
    FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]}  (no result)"$'\n'; return
  fi
  rc=$(cat "$WORK/$i.rc")
  if [ "$rc" = skip ]; then
    skips=$((skips+1)); printf 'GATE skip  %s  (unchanged vs %s)\n' "${names[$i]}" "${DEFBR:-baseline}"
  elif [ "$rc" = 0 ]; then printf 'GATE ok    %s\n' "${names[$i]}"
  else fails=$((fails+1))
       # `timeout` exits 124. Reported as a timeout ONLY when one was actually in force, so a leg
       # that chooses 124 for its own reasons is still reported as the exit code it chose.
       ftail="(exit $rc)"; { [ "$rc" = 124 ] && [ "$PROF_TIMEOUT" -gt 0 ]; } && ftail="(timed out after ${PROF_TIMEOUT}s)"
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
disp=($ORDER); ndisp=${#disp[@]}; di=0; next=0
live() { jobs -rp | wc -l; }
while [ "$next" -lt "$total" ]; do
  if [ -z "${names[$next]}" ]; then next=$((next+1)); continue; fi   # drop-sentinel: holds an index, never runs
  di_before=$di
  while [ "$di" -lt "$ndisp" ] && [ "$(live)" -lt "$JOBS" ]; do
    k=${disp[$di]}; di=$((di+1))
    { [ -z "${names[$k]}" ] || [ -f "$WORK/$k.rc" ]; } && continue   # sentinel, or already decided by the guard pass
    runleg "$k" &
  done
  if [ -f "$WORK/$next.rc" ]; then report_one "$next"; next=$((next+1)); continue; fi
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
  report_one "$next"; next=$((next+1))     # genuinely no result: report it, never hang
done
wait

# Feed the next run's dispatch order. Advisory: a failed write costs wall clock, never a verdict.
if [ -n "$TIMINGS" ]; then
  new="$WORK/timings.new"; merged="$WORK/timings.merged"; : > "$new"
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.sec" ] && printf '%s\t%s\n' "${names[$i]}" "$(cat "$WORK/$i.sec")" >> "$new"
  done
  # A guard-SKIPPED leg never enters runleg(), so it produces no .sec. Rewriting the file from this
  # run's rows alone therefore DELETED the cached duration of every skipped leg — and the runs where
  # guards fire are exactly the diff-scoped ones, so a scoped run blanked the dispatch hint the next
  # full run depends on. Carry forward any cached row this run did not measure. A leg dropped from the
  # manifest falls out on its own, because the python side keys the hint on the manifest's names.
  cp "$new" "$merged" 2>/dev/null || true
  [ -s "$TIMINGS" ] && awk -F'\t' 'NR==FNR{seen[$1]=1;next} !($1 in seen)' "$new" "$TIMINGS" >> "$merged" 2>/dev/null
  cp "$merged" "$TIMINGS" 2>/dev/null || true
fi

echo "----"
skipnote=""; [ "$skips" -gt 0 ] && skipnote=" ($skips skipped)"
# TOOL-aLeasedGauntlet-1 S3: write the verdict + failing-leg rows to a durable file (worktree-safe
# gitdir) so a `| tail`/`Select-Object -Last N` can't discard which leg failed.
if [ "$fails" = 0 ]; then
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE"; printf 'gates GREEN — %s/%s legs passed%s\n' "$((n-skips))" "$((n-skips))" "$skipnote"; } >"$sfile" 2>/dev/null || true
  echo "gates GREEN — $((n-skips))/$((n-skips)) legs passed$skipnote"; exit 0
else
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE" >"$sfile"; printf '%s' "${FAILED_LEGS:-}" >>"$sfile"; printf 'gates RED — %s/%s legs failed%s\n' "$fails" "$n" "$skipnote" >>"$sfile"; } 2>/dev/null || true
  # TOOL-dNomadicAtlas-1: a SECOND copy on RED ONLY. gate-last-summary.txt is overwritten by every
  # run, so the reflexive "let me just re-run it" — which passes, when the red was a flake — erases
  # the evidence of the run that failed. This one is only ever overwritten by the next RED run.
  if [ -n "$gd" ]; then
    ffile="$gd/gate-last-failure.txt"
    { printf '%s\n' "$PROF_LINE"; printf '%s' "${FAILED_LEGS:-}"; printf 'gates RED — %s/%s legs failed%s\n' "$fails" "$n" "$skipnote"; } >"$ffile" 2>/dev/null || true
    chmod 600 "$ffile" 2>/dev/null || true
  fi
  echo "gates RED — $fails/$n legs failed$skipnote"
  [ -n "$sfile" ] && echo "gate summary saved to $sfile"
  [ -n "$gd" ] && [ -f "$gd/gate-last-failure.txt" ] && echo "gate failure record saved to $gd/gate-last-failure.txt"
  exit 1
fi
