# lib-unattended.sh — the predicates the driver and the gate leg must answer IDENTICALLY.
#
# SOURCED, never executed. It defines functions and nothing else: a file that did work on source
# would do it twice, once per caller, at whatever moment each happened to source it.
#
# WHY THIS FILE EXISTS. `unattended.sh` decides at declaration time whether two passes collide;
# `check-unattended.sh` decides after the fact whether a pass wrote what it declared. Both questions
# reduce to "has this pass committed yet", and both were written by hand, separately, in one sitting.
# The driver's copy carried a comment saying it read the question "the same way the leg reads it".
# It did not — it counted the run-state bookkeeping commit that carries a pass's own declaration, so
# every pass closed the instant it was declared and the disjointness proof found nobody to collide
# with. A closing review reproduced that with two controls: a pass whose ONLY commit was its own
# declaration read CLOSED to the driver and OPEN to the leg, and adding one product commit made both
# read closed. So the two spellings disagreed exactly on the case the disjointness proof depends on,
# and agreed everywhere else — which is why reading them side by side had not shown it.
# Pointer, not evidence: TOOL-dUnstalledConvoy-22.
#
# The lesson is not "be more careful". Two spellings of one rule is [[two-answers-to-one-question]],
# and the fix for it is one spelling, which is this file.
#
# WHAT IT HOLDS: `GIT` and its two pins; `resolve_sidecar_dir`, the one derivation of the sidecar
# root the driver and the resume tick both read; `read_bound_key`, the one reader of a bound conf
# key both of them call; `read_host_name`, `read_pid_image` and `check_pid_alive`, the one reading
# of "which node, which process" the lease writer and both pid probes share; `parse_gate_profile` and
# `check_gate_wall`, the one reading of the gate runner's profile the driver and the leg both ask; the
# anchored id tests; path containment; and "has this pass committed yet". The same rule admits the
# resume tick as a third sourcer.

# --------------------------------------------------------------------------------- git, once
# Replace refs and graft advice are both OFF: a leg that reads history must see the history that is
# there, and a repo-local replace ref would silently rewrite what every predicate below answers.
# NAMED, so `GIT` and the bounded remote observation cannot drift apart. The observation cannot call
# GIT - it wraps git in `timeout` and needs the pins as argv - so the two spelled the same two
# options independently until one of them was named. The pins live HERE rather than in either
# caller, because the driver and the gate leg both source this file and a pin in one of them is a
# pin the other does not have.
GIT_PIN_REPLACE=core.useReplaceRefs=false
GIT_PIN_GRAFTADV=advice.graftFileDeprecated=false
# NO MEMO LIVES HERE, and the attempt is recorded because it looked obviously right.
# TOOL-aQuenchedHarness-10 cached this wrapper on argv, having measured that 436 of the leg's
# 1008 git calls are byte-identical repeats. It bought almost nothing: about twenty call sites
# invoke `GIT` inside `$( )`, and whole functions — `pass_commit`, `next_anchor`,
# `baseline_units`, `pinned_units` — are themselves called through command substitution, so
# every cache entry they filled died with the subshell that filled it. `rev-parse HEAD` still
# cost 39 spawns with the cache active.
#
# It also RED-ED check 28, which is the better reason it is gone: that check reads this
# definition LINE and requires the replace-ref pin on it, so a wrapper whose body carries the
# pin while its signature does not is exactly the unpinned-wrapper shape it exists to catch.
# The lesson the measurement actually supports: fill tables ONCE in the main shell before the
# loops, which is what `is_published` now does, rather than caching a wrapper that is mostly
# called from subshells.
GIT() { git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" "$@"; }

# THE SIDECAR ROOT, derived ONCE, HERE and nowhere else: `<git-dir>/unattended`, the WORKTREE's git
# dir — where `gate-logs/` already lives — never the common dir, because a run lives in one
# worktree and one sidecar per worktree is the whole point. Every reader of a sidecar file (the
# stall log at `--liveness`, the stop log at `--landed`, the resume log in the tick) calls this
# rather than respelling it; the driver and the tick both source this file, so a second spelling in
# either would be two answers to one question, and the kit gate counts the literal on exactly one
# code line across the three. An empty answer is a DEAD PROBE for the caller, never a path composed
# from an empty root — the caller refuses, it does not default. Moved from the driver, where unit 2
# defined it, by TOOL-aWokenSentinel-20; the body is unit 2's, unchanged.
resolve_sidecar_dir() { # -> <git-dir>/unattended, or nothing when the git dir cannot be derived
  local g; g=$(GIT rev-parse --git-dir 2>/dev/null) || g=""
  [ -n "$g" ] || return 1
  printf '%s/unattended\n' "$g"
}

# ------------------------------------------------------------------------------ bounds, once
# MOVED from the driver by TOOL-aWokenSentinel-5, body unchanged: the resume tick reads its two
# knobs through this function, and the driver its four, so it lives where both source it. THE
# CALLING-SHELL CONTRACT, on the function line and ASSERTED by its first line (TOOL-aWokenSentinel-18):
# `${!name}` reads the calling shell, and the NOTE interpolates `$CONF`, so a caller that named no
# conf would be handed a default announced with nowhere to change it — `Declare one in  to change
# it`, the empty path — or, under `set -u`, a shell error naming neither contract nor remedy. That
# is a refusal here, in the one function every caller shares, so the next script that sources this
# library from an unsourced shell refuses on its first run instead of taking the defaults silently.
# A BOUND KEY: DEFAULTED, VALIDATED, AND ANNOUNCED. TOOL-aBoundedCeiling-6, hoisted at its second
# instance by TOOL-aProbedUnit-3 — the charter's section 12 extracts the shared contract when the
# second caller arrives, and the third (`REVIEW_ROUNDS`) is a call, never a third `case`.
#
# A conf that declares nothing still gets a bound, because the population that produced the observed
# 3h19m hang is exactly the one that never edits this key. What it does NOT get is silence: the line
# below says which number is in force and where it came from, so a defaulted pin is never invisible.
#
# A malformed value is a REFUSAL rather than a silent fallback. "0" would mean no bound at all to
# `timeout`, so accepting junk and coercing it would unbound the one project whose declaration was
# wrong -- the failure landing on whoever tried hardest to configure it.
#
# <UNIT> is an argument because a caller may count rounds rather than seconds, and a refusal that
# says `seconds` about a round count is a false sentence. No `fail` branch here: this runs before
# `fail()` exists and refuses with exit 2, the misconfiguration code, exactly as the block it replaces.
read_bound_key() { # NAME · DEFAULT · UNIT · NOTE — the caller sourced the conf into THIS shell and named it in CONF
  [ -n "${CONF:-}" ] && [ -f "$CONF" ] || {
    echo "unattended: REFUSING - read_bound_key was called with CONF unset or naming no file, so its NOTE could name nowhere to declare the key and a default would be taken from nowhere; set CONF to the sourced conf before the call" >&2
    RUNLOG_CLEAN=1; exit 2; }
  local _bk_name="$1" _bk_default="$2" _bk_unit="$3" _bk_note="$4" _bk_val
  _bk_val="${!_bk_name:-}"
  case "$_bk_val" in
    "") printf -v "$_bk_name" '%s' "$_bk_default"
        echo "unattended: NOTE - this project declares no $_bk_name, so $_bk_note. Declare one in $CONF to change it." >&2 ;;
    *[!0-9]*|0)
        echo "unattended: REFUSING - $_bk_name is declared as '$_bk_val', which is not a positive integer of $_bk_unit. A bound that cannot be parsed is a bound nobody set, and 0 means no bound at all." >&2
        RUNLOG_CLEAN=1; exit 2 ;;
  esac
}

# ------------------------------------------------------------------------ the gate profile, once
# TOOL-dDerivedDocket-27 S2, S3 and S6. The runner prints its resolved profile as TAB-separated
# key/value lines, and two readers need three of those keys: the driver bounds its bar by `wall`
# plus `queue`, and both the driver's `--preflight` and the gate leg compare the effective wall with
# `ceiling_max`. One parse and one comparison here, because a threshold spelled in both callers is
# two answers to one question, and the leg is the second opinion on a number the driver acts on.
#
# THE KEYS ARE READ, NEVER GUESSED. A key the profile did not print, or printed as anything but a
# plain integer, is MISSING and named in GPF_MISSING, so a caller can say which one it lacked. A
# `wall` of 0 counts as missing too: the runner prints 0 for NO wall, and a bound derived from it
# would be the margin alone, which kills a healthy bar. A `queue` of 0 is a real value, a turnstile
# that never waits. `ceiling_max` may read `-`, the runner's word for a manifest declaring no
# ceiling, and that is an answer rather than a missing key.
#
# NORMALISED WITH `10#`, because a value that arrives as `08` is otherwise read as a broken octal
# literal by the first arithmetic that touches it.
GPF_WALL=""; GPF_QUEUE=""; GPF_CEILING_MAX=""; GPF_MISSING=""
parse_gate_profile() { # the profile command's stdout -> GPF_WALL, GPF_QUEUE, GPF_CEILING_MAX, GPF_MISSING; rc 1 when a key is missing
  local _gp_k _gp_v _gp_w="" _gp_q="" _gp_c=""
  GPF_WALL=""; GPF_QUEUE=""; GPF_CEILING_MAX=""; GPF_MISSING=""
  while IFS=$'\t' read -r _gp_k _gp_v || [ -n "$_gp_k" ]; do
    _gp_v=${_gp_v%$'\r'}
    case "$_gp_k" in
      wall) _gp_w=$_gp_v ;;
      queue) _gp_q=$_gp_v ;;
      ceiling_max) _gp_c=$_gp_v ;;
    esac
  done <<< "$1"
  case "$_gp_w" in ''|*[!0-9]*) GPF_MISSING="wall" ;; *) GPF_WALL=$((10#$_gp_w)); [ "$GPF_WALL" -gt 0 ] || { GPF_WALL=""; GPF_MISSING="wall"; } ;; esac
  case "$_gp_q" in ''|*[!0-9]*) GPF_MISSING="${GPF_MISSING:+$GPF_MISSING }queue" ;; *) GPF_QUEUE=$((10#$_gp_q)) ;; esac
  case "$_gp_c" in
    -) GPF_CEILING_MAX=- ;;
    ''|*[!0-9]*) GPF_MISSING="${GPF_MISSING:+$GPF_MISSING }ceiling_max" ;;
    *) GPF_CEILING_MAX=$((10#$_gp_c)) ;;
  esac
  [ -z "$GPF_MISSING" ]
}

# THE CONF CHECK, one predicate for both readers, called after `parse_gate_profile`. The EFFECTIVE
# wall is the declared GATE_WALL, else the profile's own `wall`, because a blank GATE_WALL leaves the
# runner's row in force. It may not sit below the largest leg ceiling the profile reports: a wall
# below it fires on a healthy bar that dispatches that leg. rc 0 when it clears, 1 when it is below,
# naming both numbers in GW_WHY, and 2 when there is nothing to compare, saying why. The caller
# decides what each means; the leg announces a 2 and never reds on one.
GW_EFFECTIVE=""; GW_WHY=""
check_gate_wall() { # the declared GATE_WALL, blank or a positive integer -> rc 0 clears · 1 below the ceiling · 2 cannot compare
  local _gw_w=$1 _gw_src="the declared GATE_WALL"
  GW_EFFECTIVE=""; GW_WHY=""
  if [ -z "$_gw_w" ]; then
    _gw_w=$GPF_WALL; _gw_src="the profile's own wall, GATE_WALL being blank"
    if [ -z "$_gw_w" ]; then
      GW_WHY="GATE_WALL is blank and the profile printed no usable wall, so there is no wall to compare with the largest leg ceiling"
      return 2
    fi
  fi
  GW_EFFECTIVE=$_gw_w
  if [ -z "$GPF_CEILING_MAX" ]; then
    GW_WHY="the profile printed no usable ceiling_max, so the ${_gw_w}s wall cannot be compared with the largest leg ceiling"
    return 2
  fi
  if [ "$GPF_CEILING_MAX" = - ]; then
    GW_WHY="the profile reports that no leg declares a ceiling, so the ${_gw_w}s wall has no ceiling to clear"
    return 2
  fi
  if [ "$_gw_w" -lt "$GPF_CEILING_MAX" ]; then
    GW_WHY="the effective wall, $_gw_src, is ${_gw_w}s, below the largest declared leg ceiling of ${GPF_CEILING_MAX}s"
    return 1
  fi
  GW_WHY="the effective wall, $_gw_src, is ${_gw_w}s and clears the largest declared leg ceiling of ${GPF_CEILING_MAX}s"
  return 0
}

# --------------------------------------------------------------------------- processes, once
# THE LEASE NAMES A PROCESS, NOT A NUMBER (TOOL-aWokenSentinel-5, folding the closing review's id 2).
# A pid alone proves that SOME process holds the number: a reboot mid-run — a recorded event on
# this fleet — recycles it to whatever the owner starts next, and a run branch checked out on a
# second node carries the first node's pid into the second's process table. So the lease records
# the node and the image beside the pid, and the aliveness probe matches all it was given — the
# image, and the lease's own UTC as a bound the holder's start time may not pass. Four functions,
# in the library because the driver WRITES the facts and the resume tick READS the launched pid
# back through the same probe; a spelling in each would be two answers to one question.

# THE NODE, one spelling: `COMPUTERNAME` where Windows sets it, `hostname` elsewhere, LOWERCASED
# because the two disagree on case for one machine (measured on node `a`, 2026-09-21: `COMPUTERNAME`
# upper, `hostname` lower). Empty when neither answers; the caller records `absent` for that.
read_host_name() { # -> the node's name, lowercased, or nothing
  local h="${COMPUTERNAME:-}"
  [ -n "$h" ] || h=$(hostname 2>/dev/null) || h=""
  [ -n "$h" ] || return 1
  printf '%s\n' "$h" | tr '[:upper:]' '[:lower:]'
}

# THE IMAGE HOLDING A PID. Prints the image name and returns 0 when a process holds the pid; 1 when
# none does; 2 when the probe could not look — an absent or non-numeric pid, a missing tool, a tool
# that exited non-zero — because a tool that answered nothing is not a `no`. Under MSYS the probe is
# `tasklist` and its OUTPUT decides: MEASURED on node `a`, 2026-09-16, it exits 0 for a live pid AND
# for a dead one (printing `INFO: No tasks are running`), so the exit code decides nothing; and
# `kill -0` on a live Windows pid reports `No such process` there, so the POSIX arm alone would read
# every live run on this fleet as dead. The row is `<image> <pid> <session> <session#> <mem>`, and
# the image is every field BEFORE the one equal to the pid, so an image with a space survives.
# Elsewhere `kill -0` decides existence and `ps -o comm=` names the image, UNVERIFIED (no registered
# node is POSIX).
read_pid_image() { # pid -> image on stdout; 0 held · 1 no such process · 2 the probe answered nothing
  local pid="$1" out img
  case "$pid" in ""|absent|*[!0-9]*) return 2 ;; esac
  case "$(uname -s 2>/dev/null)" in
    MINGW*|MSYS*|CYGWIN*)
      command -v tasklist >/dev/null 2>&1 || return 2
      out=$(tasklist //FI "PID eq $pid" //NH 2>/dev/null) || return 2
      img=$(printf '%s\n' "$out" | tr -s '\r\t ' '   ' | awk -v p="$pid" '{ for (i = 2; i <= NF; i++) if ($i == p) { s = $1; for (j = 2; j < i; j++) s = s " " $j; print s; exit } }')
      [ -n "$img" ] || return 1
      printf '%s\n' "$img" ;;
    *)
      kill -0 "$pid" 2>/dev/null || return 1
      img=$(ps -o comm= -p "$pid" 2>/dev/null | sed 's/^ *//; s/ *$//'); printf '%s\n' "${img:-unknown}" ;;
  esac
}

# WHEN THE HOLDER OF A PID STARTED, as a UTC stamp at second precision. Under MSYS a PowerShell
# `Get-CimInstance Win32_Process` read (`wmic` is gone from this fleet's Windows 11; `Get-Process`
# hands back a null `StartTime` for a process it cannot open, `System` included), invariant `s`
# format so no culture's time separator leaks in; MEASURED on node `a`, 2026-09-21: 300-450 ms a
# call, and a pid nothing holds prints nothing. Elsewhere `ps -o lstart=` re-read by `date -u`,
# UNVERIFIED (no registered node is POSIX). Returns 2 and prints nothing when the probe answered
# nothing, because a start time nobody read is not a start time.
read_pid_start() { # pid -> the holder's start as a UTC stamp on stdout; 0 read · 2 the probe answered nothing
  local pid="$1" out=""
  case "$pid" in ""|absent|*[!0-9]*) return 2 ;; esac
  case "$(uname -s 2>/dev/null)" in
    MINGW*|MSYS*|CYGWIN*)
      command -v powershell.exe >/dev/null 2>&1 || return 2
      out=$(powershell.exe -NoProfile -NonInteractive -Command "(Get-CimInstance Win32_Process -Filter 'ProcessId=$pid').CreationDate.ToUniversalTime().ToString('s')" </dev/null 2>/dev/null | tr -d '\r')
      [ -z "$out" ] || out="${out}Z" ;;
    *)
      out=$(ps -o lstart= -p "$pid" 2>/dev/null) && [ -n "$out" ] && out=$(date -u -d "$out" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null) ;;
  esac
  case "$out" in
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z) printf '%s\n' "$out" ;;
    *) return 2 ;;
  esac
}

# DOES THE RECORDED PID EXIST, AND IS IT THE RECORDED PROCESS. `yes`, `no` or `unknown`: `unknown`
# when the probe could not look; `no` when nothing holds the pid, OR when something does and the
# recorded image does not match it — the recycled-pid case, and a tree kill aimed there lands on the
# owner's new interactive session, an IDE, or `explorer.exe` and every child — OR when the holder
# STARTED AFTER the stamp the caller recorded it under (the closing review's round 2, defect E): a
# same-image recycle — a second `claude.exe` on a node whose job is running them, a second
# `bash.exe` on a bash-heavy one — passes the image and fails this, because the process that wrote
# a lease, or that a launch recorded, existed before the stamp, and any later holder of its number
# started after it. An image of `absent` or none at all matches anything, and so does an absent
# stamp: a lease written before either was recorded, or by a harness whose pid the probe could not
# see, keeps the pid-only reading it always had, and the header says so rather than pretending that
# lease is guarded. A start time the probe cannot read keeps the image reading — the compare is
# additive, never a `no` manufactured from a dead probe. Existence is not progress: a hung process
# is `yes`. MOVED from the driver by TOOL-aWokenSentinel-5's fold of the closing review; the pid half
# is unit 2's, unchanged in its verdicts.
check_pid_alive() { # pid · [image] · [not-after-utc] -> yes | no | unknown
  local img rc st
  img=$(read_pid_image "$1"); rc=$?
  case "$rc" in 2) echo unknown; return 0 ;; 1) echo no; return 0 ;; esac
  case "${2:-}" in ""|absent|"$img") ;; *) echo no; return 0 ;; esac
  case "${3:-}" in ""|absent) ;; *) if st=$(read_pid_start "$1") && [ "$st" \> "$3" ]; then echo no; return 0; fi ;; esac
  echo yes
}

# ------------------------------------------------------------------------------- ids, anchored
# An id compared as a SUBSTRING joins `-1` to `-10`, and the joined pair is always the wrong one:
# `TOOL-x-1` is a prefix of every `TOOL-x-1N` a build with ten units will mint. The trailing class
# must exclude digits — that IS the `-1`/`-10` case — and excluding `-` keeps a hyphenated suffix
# from matching. `grep -w` is not enough: `-` is a word character to some greps and not others.
id_rows() {  # haystack-text · id  -> the lines carrying that id as a whole token
  printf '%s\n' "$1" | grep -E "(^|[^A-Za-z0-9-])$2([^A-Za-z0-9-]|\$)" || true
}
# PURE BASH, AND THIS ONE IS THE HOT PATH. `id_rows` forks a subshell and spawns a `grep` per
# call, and `pass_commit` calls this once per commit in its window -- 1528 calls in one run of
# `check-unattended.sh`, measured on node `a` 2026-09-07, which was the largest single spawn
# population left in the leg after the `git log -1` removal above it.
#
# THE PATTERN IS `id_rows`'S, and the two are EQUIVALENT on a multi-line haystack even though
# grep anchors per LINE and bash anchors per STRING: a newline is itself a member of the
# negated class each anchor alternates with, so every position where grep's `^` or `$` would
# match is a position where the character-class branch matches instead. That is the kind of
# claim that is obviously true and occasionally false, so it was checked differentially over
# seventeen cases -- both anchors, both multi-line edges, the `-1`/`-10` trap and the
# hyphenated suffix -- before this landed, and the leg's whole stdout is byte-identical
# across the change. TOOL-aQuenchedHarness-7.
#
# `id_rows` KEEPS its grep: it returns the matching LINES, which is a different job, and it is
# not called per commit.
id_in() {    # haystack-text · id  -> 0 when the id appears as a whole token
  [[ $1 =~ (^|[^A-Za-z0-9-])"$2"([^A-Za-z0-9-]|$) ]]
}

# --------------------------------------------------------------------------- paths, normalised
# `memory`, `memory/` and `./memory` are ONE path. Compared as raw strings they are three, and a
# containment question answered on the strings reports two names of the same directory as disjoint —
# which turns every refusal built on it into a spelling test that one trailing slash passes.
normpath() {  # path -> the same path in one spelling
  _np=$1
  # REPEATED SLASHES COLLAPSE FIRST. Stripping the leading `./` before collapsing turns `.//x` into
  # the ABSOLUTE `/x` — a path in a different tree — and every containment answer after that is about
  # somewhere else. Found by the arm written for this function, which is the argument for writing it.
  while :; do case "$_np" in *//*) _np=$(printf '%s' "$_np" | sed 's|//*|/|g') ;; *) break ;; esac; done
  while :; do case "$_np" in ./?*) _np=${_np#./} ;; *) break ;; esac; done
  # THE DOT SEGMENTS, interior and trailing. `a/./b`, `a/b/.` and `a/b/./` all name what `a/b` names,
  # and every containment answer in this kit is built on this function — so a declaration spelled with
  # a dot segment was compared as a different string and the guards judged one path while the leg
  # graded another. Both spellings are broken by ONE missing step, which is why fixing only the
  # interior one would have left the class open with an instance closed.
  while :; do case "$_np" in */./*) _np="${_np%%/./*}/${_np#*/./}" ;; *) break ;; esac; done
  while :; do case "$_np" in ?*/.) _np=${_np%/.} ;; *) break ;; esac; done
  while :; do case "$_np" in ?*/) _np=${_np%/} ;; *) break ;; esac; done
  printf '%s' "$_np"
}
# `covers a b` — b is a, or sits under it. DIRECTIONAL, and what a "may this pass write here"
# question wants. `overlaps` is what every DISJOINTNESS question wants, and disjointness is what the
# dispatch refusals are actually asking: testing one direction only refuses the narrow declarations
# and admits the one that claims everything, because the widest path is under nothing.
covers() {
  _ca=$(normpath "$1"); _cb=$(normpath "$2")
  case "$_cb" in "$_ca"|"$_ca"/*) return 0 ;; esac
  return 1
}
overlaps() { covers "$1" "$2" || covers "$2" "$1"; }
# The whole-repository spellings, which normalise to something no containment test can express: `.`
# covers everything and is under nothing, and an empty path is not a path. Named here so the driver
# and any later reader refuse the same set.
is_repo_root() {
  case "$(normpath "$1")" in ""|"."|"./") return 0 ;; esac
  return 1
}

# ------------------------------------------------ condition 3's two keys, resolved and compared once
# TOOL-dDerivedDocket-20 S1. `SHARED_RECORDS` and `GENERATED_INDEXES` are the two halves of the build
# method's condition 3, and `--dispatch` answers each by its own rule: a shared record may never be
# declared, a generated index may be declared alone. One path under BOTH keys is answered by whichever
# rule the verb reaches first, and makes the other declaration mean nothing. So the pair is refused at
# conf load by the driver AND by the gate leg, through the one predicate below — the driver alone would
# let the bar pass a conf no run has read yet, and the leg alone would let a run start on one.
#
# THE DEFAULT IS RESOLVED HERE TOO, and that is half the point. An UNDECLARED `SHARED_RECORDS` means a
# memory tree at its conventional layout, `<memory root>/DECISIONS.md <memory root>/backlog`; a DECLARED
# blank means the empty set, which is why both callers initialise the key to the sentinel below rather
# than to blank. The driver used to resolve that default inline while the leg read the key as blank, so
# a conf leaving it undeclared would have been refused by one reader and passed by the other — two
# readers of one config, one of them re-deriving it (memory/gotchas/two-readers-of-one-config-one-re-derived.md).
# The sentinel itself, spelled ONCE. Both callers initialise the key to it before the conf is read,
# and a second spelling in either would be a sentinel this comparison never recognises.
SHARED_RECORDS_UNDECLARED="__kit-default__"
resolve_shared_records() { # declared value · memory root -> the effective set
  if [ "$1" = "$SHARED_RECORDS_UNDECLARED" ]; then
    printf '%s' "$2/DECISIONS.md $2/backlog"
  else
    printf '%s' "$1"
  fi
}
# One `<shared record><TAB><index>` line per pair that overlaps, on `overlaps` — CONTAINMENT, in either
# direction, never string equality: `memory` shared beside a `memory/LIVE.md` index is the same
# contradiction as the two spelled alike, and so is the reverse nesting. Only the INDEX half of a
# `GENERATED_INDEXES` pair is compared, because the generator is product code a pass may write. Read
# into arrays rather than word-split, so a glob character in a value is compared as written rather than
# expanded against the working tree. Prints nothing when the keys agree; it reads no memory-tree state.
scan_shared_index_overlaps() { # shared-records · generated-indexes -> the overlapping pairs
  local -a _so_shared=() _so_pairs=()
  local _so_s _so_p _so_i
  read -ra _so_shared <<<"$1"
  read -ra _so_pairs <<<"$2"
  for _so_s in "${_so_shared[@]}"; do
    [ -n "$_so_s" ] || continue
    for _so_p in "${_so_pairs[@]}"; do
      _so_i=${_so_p%%:*}
      [ -n "$_so_i" ] || continue
      # A whole-repository spelling contains everything and is under nothing, so `overlaps` cannot
      # say so; it is a contradiction with every index there is.
      if is_repo_root "$_so_s" || is_repo_root "$_so_i" || overlaps "$_so_s" "$_so_i"; then
        printf '%s\t%s\n' "$_so_s" "$_so_i"
      fi
    done
  done
  return 0
}

# --------------------------------------------------- the paths a unit's brief rows name, once
# Prints, one per line and normalised, every path a ` brief · item <unit> · reason ` row names in
# the run-state file AS IT STANDS AT <commit>. Two consumers, one parser: `pass_commit` subtracts
# this set before it calls a commit a pass commit, and check 23 subtracts the same set before it
# grades what that commit carried. When the exclusion lived in check 23 alone, a `{run-state,
# brief}` bookkeeping commit naming the unit — the ordinary shape, since `--brief` requires the
# brief TRACKED and stages the run-state file beside it — was SELECTED as the pass commit, graded
# clean once the brief was forgiven, and the pass's real commit was never read. The closing diff
# review of aRatifiedRulings, finding 7. Only the leg was fooled: the driver's condition 1 also
# requires an `overlaps` hit against the declared set before it closes a pass, and a brief overlaps
# nothing an ordinary pass declares.
#
# THE TREE AT THE COMMIT, never the working copy: a row appended after the commit is outside it by
# construction, which is what keeps a post-hoc `--brief` from excusing a stray write. Selected on
# the whole field with both separators, so `-1` is not a prefix of `-10`; parsed with
# `check-brief-recorded.sh`'s own expansions, so a grammar change breaks every reader the same way.
# A FILE, NEVER A COMMAND SUBSTITUTION, for the reason `pass_commit`'s header states in full twenty
# lines below. The blob used to land in a VARIABLE the loop then read through a heredoc, and the
# variable was assigned from `$(GIT show …)`: a substitution reads until EOF, EOF arrives when the
# LAST inherited write end closes, and `GIT` is a shell FUNCTION — so the substitution forks a
# subshell which forks `git`, and the reader waits on a grandchild's write end. Same class, same
# file, one function apart. `pass_commit` calls this once per commit in its window, so `--dispatch`
# on this build's run inherited it a hundred-odd times per row and stopped completing at all: four
# runs died without writing a row, the last on a one-hour bound at 11350 s. The walk therefore runs
# in the CURRENT shell with its stdout redirected to a scratch file and the loop reads that file by
# redirect. No pipe exists, so no EOF has to arrive.
# `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` is the class. TOOL-cMendedVintage-12.
#
# WHY THE GATE DID NOT SEE IT, which is the half worth carrying: the `shell hygiene` leg refuses a
# loop fed by a substitution repo-wide, and this loop was fed by a heredoc over a VARIABLE assigned
# from one on the line above. The predicate did not follow the assignment, so the instance sat in
# the blind spot of the check written to catch it. That predicate now follows one assignment.
#
# A SCRATCH FILE THAT CANNOT BE CREATED IS A NAMED REFUSAL, `pass_commit`'s rule for its reason: an
# empty answer here MEANS "this pass declared no brief paths", which is a legitimate and common
# state, so a broken TMPDIR answered with silence would read as a correct answer and forgive a write
# nothing declared. The stderr line is the only thing that makes it visible.
#
# THREE CONDITIONS, AND A ROW MEETING TWO OF THEM COVERS NOTHING. TOOL-dDerivedDocket-30 S1, which
# finishes what TOOL-aLeakedHandle-7 ruled and TOOL-aRatifiedRulings-2 built as the first of them.
#   * THE UNIT: the row names THIS unit, so a pass cannot carry a sibling's brief unreported.
#   * THE DIRECTORY: the path lies under the build's own `prompts/`, the folder beside the run-state
#     file, so a row cannot name a product file and excuse it. The folder itself is not under itself.
#   * THE BLOB: the path's blob AT <commit> starts with the row's twelve-hex hash, so a brief EDITED
#     after `--brief` hashed it is not excused — that edit is exactly the write the declare-before-
#     dispatch rule exists to see. A hash that is not twelve lowercase hex digits matches nothing.
# All three are applied HERE and nowhere else, because this function's two consumers must excuse one
# set: narrowed in check 23 alone, `pass_commit` would still skip a commit carrying an edited brief as
# bookkeeping, and the commit that edited it would never be the one graded. The blob is read from
# the COMMIT, never the working copy, because the question is what that commit wrote; it goes through
# a scratch file for the substitution reason stated above, the same file reused per row.
read_brief_paths() {  # commit · unit · run-state-path
  _rb_f=$(mktemp) || { printf 'lib-unattended: read_brief_paths cannot create a scratch file, so it cannot say which paths a brief row declared\n' >&2; return 2; }
  _rb_b=$(mktemp) || { rm -f "$_rb_f"; printf 'lib-unattended: read_brief_paths cannot create a scratch file, so it cannot say which paths a brief row declared\n' >&2; return 2; }
  GIT show "$1:$3" >"$_rb_f" 2>/dev/null || :
  _rb_d=$(normpath "$3"); _rb_d=${_rb_d%/*}/prompts/
  # THE `|| [ -n … ]` REPLACES A GUARANTEE THE HEREDOC GAVE FREE. Command substitution stripped the
  # trailing newlines and the heredoc put exactly one back, so every line was terminated; a FILE may
  # end without one, and a bare `read` drops that last line. Without this the repair would silently
  # return a smaller path set than the shape it replaced — which is the one way this change could
  # move a disjointness verdict while claiming to fix a stall.
  while IFS= read -r _rb_r || [ -n "$_rb_r" ]; do
    case "$_rb_r" in *" brief · item $2 · reason "*) ;; *) continue ;; esac
    _rb_r=${_rb_r#* · reason }
    _rb_h=${_rb_r%% *}; _rb_p=$(normpath "${_rb_r#* }")
    case "$_rb_h" in [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]) ;; *) continue ;; esac
    case "$_rb_p" in "$_rb_d"?*) ;; *) continue ;; esac
    GIT rev-parse --verify --quiet "$1:$_rb_p" </dev/null >"$_rb_b" 2>/dev/null || continue
    _rb_o=""; IFS= read -r _rb_o <"$_rb_b" || :
    case "$_rb_o" in "$_rb_h"*) printf '%s\n' "$_rb_p" ;; esac
  done <"$_rb_f"
  rm -f "$_rb_f" "$_rb_b"
}

# ------------------------------------------------------------- has this pass committed yet, once
# Prints the FIRST pass commit after <anchor> and returns 0; prints nothing and returns 1 while the
# pass is still open. Three callers need this and each spelled it separately before: the driver's
# condition 1, the driver's re-declaration rule, and the leg's write-set grading.
#
# A RUN-STATE BOOKKEEPING COMMIT IS NOT A PASS COMMIT, and the skip is the load-bearing half.
# `--dispatch` STAGES the run-state file, so the run commits that declaration itself — and that
# commit's subject names the unit, because it is about that unit. Counting it closes a pass before
# the pass has written a byte, and the whole disjointness proof then runs over an empty sibling set.
# THE BRIEF `--brief` STAGED IS THE SAME KIND OF BOOKKEEPING: a commit whose touch set minus the
# run-state file minus the paths its brief rows name is EMPTY moved nothing the pass wrote, and the
# walk continues to the commit that did (`read_brief_paths` above).
#
# The window is `<anchor>..HEAD` and the answer is the FIRST qualifying commit, never a later one: a
# pass's own review fold or spec bump lands after its group has ended and is not the commit that
# closed it.
#
# THE UPPER BOUND is optional and defaults to HEAD. A unit legitimately owns several dispatch rows at
# several anchors — M6 defines five pass kinds — and with an unbounded window row one is graded
# against row two's commit, which is another pass's work. The bound does not change what counts as a
# pass commit; it changes which commits are even offered. TOOL-dUnstalledConvoy-23 S3.
pass_commit() {  # anchor · unit · run-state-path · [upper-bound, default HEAD]
  _pa=$1; _pu=$2; _prel=$3; _pto=${4:-HEAD}
  GIT rev-parse --verify --quiet "$_pa^{commit}" >/dev/null 2>&1 || return 1
  # THE SUBJECT COMES OUT OF THE SAME WALK AS THE SHA. It used to cost a `git log -1` per
  # commit in the window, on every call, and this function is called once per (anchor, unit)
  # pair -- so the same commits were re-read once per pair. Profiled on node `a` 2026-09-07
  # over a full run of `bash tools/unattended/check-unattended.sh`: 1528 of that run's 2513
  # git spawns were this one line, against 31 for the `--follow` walk everyone assumes is the
  # expensive one. `%H%x09%s` gets both out of one walk. TOOL-aQuenchedHarness-7.
  #
  # A FILE, NEVER A PIPE AND NO LONGER A HEREDOC. The heredoc was here for a real reason and the
  # reason still stands: a piped `while` runs in a subshell and this loop RETURNS from the function,
  # so the `return 0` below would exit the subshell and the function would fall through. What the
  # heredoc solved in one direction it broke in the other, because its body was a COMMAND
  # SUBSTITUTION: `$( )` reads until EOF, EOF arrives when the LAST inherited write end closes, and
  # `GIT` is a shell FUNCTION — so the substitution forks a subshell which forks `git`, and the
  # reader waits on a grandchild's write end. On 2026-09-10 that never closed: the `unattended kit
  # gate` leg sat at zero CPU for 63 minutes, with the forked subshell holding both ends of its own
  # pipe on fd 3 and fd 4 and no descendant alive, until an operator killed it.
  #
  # The walk therefore runs in the CURRENT shell with its stdout redirected to a scratch file, and
  # the loop reads that file by redirect. No pipe exists, so no EOF has to arrive; a redirect from a
  # file creates no subshell, so `return 0` still returns from `pass_commit`. Both properties at
  # once, which is what the heredoc could not do.
  # `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` is the class; the `shell hygiene (a loop
  # fed by a command substitution)` merge-bar leg now refuses it repo-wide. TOOL-aLeakedHandle-1.
  #
  # A SCRATCH FILE THAT CANNOT BE CREATED IS A NAMED REFUSAL, not a fall-through to `return 1`.
  # `return 1` already MEANS "this pass has not committed yet", so answering a broken TMPDIR with it
  # would report every open pass as open forever and read as a correct answer. Both callers spell
  # `$(pass_commit … || true)`, so rc 2 reaches them as the same empty answer rc 1 does — the
  # difference is the stderr line, which is the only thing that makes a broken TMPDIR visible.
  _pf=$(mktemp) || { printf 'lib-unattended: pass_commit cannot create a scratch file, so it cannot say whether this pass committed\n' >&2; return 2; }
  GIT log --reverse --format="%H%x09%s" "$_pa..$_pto" >"$_pf" 2>/dev/null || :
  # It reads LINES rather than word-splitting because a subject holds spaces, and the possibly-empty
  # field is LAST for the reason memory/gotchas/empty-field-collapses-unless-it-is-last.md states.
  while IFS=$'\t' read -r _pc _psub; do
    [ -n "$_pc" ] || continue
    id_in "$_psub" "$_pu" || continue
    _ptouch=$(GIT diff-tree --no-commit-id --name-only -r "$_pc" 2>/dev/null | grep -vxF -- "$_prel" || true)
    [ -n "$_ptouch" ] || continue
    # EXACT membership against the newline-wrapped set, deliberately not `covers`: a row naming a
    # directory must forgive nothing under it. Same test check 23 makes, on the same set.
    _pnl=$'\n'; _pbrief="$_pnl$(read_brief_paths "$_pc" "$_pu" "$_prel")$_pnl"
    _pleft=""
    for _pp in $_ptouch; do
      case "$_pbrief" in *"$_pnl$_pp$_pnl"*) ;; *) _pleft=1; break ;; esac
    done
    [ -n "$_pleft" ] || continue
    printf '%s\n' "$_pc"
    rm -f "$_pf"
    return 0
  done <"$_pf"
  rm -f "$_pf"
  return 1
}

# ------------------------------------------------------------- which commit BUILT this unit, once
# ONE PREDICATE, TWO WINDOWS. This is the whole build-commit definition and every caller passes its
# own window rather than its own copy. A second copy would be two answers to one question, and the
# copy would be the one that drifts.
#
# LIFTED OUT OF `check-pass-order.sh` BY TOOL-aHoistedPass-7, and the lift is the work rather than
# the bookkeeping. It lived there as `_find_build_commit`, INDENTED inside that leg's per-unit loop
# together with the only other function that file has, so neither existed until the block ran and no
# sibling could source the file and call either. The symbol was reusable and the SEAM was not, which
# a grep for the name cannot tell apart. Sourcing the file and invoking the name can, and that is the
# test this move owes.
#
# THE WINDOW ARGUMENTS ARE OPTIONAL AND DEFAULT TO THE IN-RANGE WALK — unbounded, `--reverse` —
# because that is the question every caller but one asks. Dropping them to fit a five-argument
# signature would have deleted the pre-anchor violation class rather than moved it.
#
# THE EXCLUSION IS THE BUILD'S WHOLE FOLDER PLUS THE GENERATED INDEXES AND THE SHARED RECORDS, and
# getting this wrong made a CONFORMING run unlandable, twice. It was `spec/` and `reviews/` alone,
# and a spec pass legitimately writes more than those two: the regenerated index, the build README,
# the run-state file and the month ledger all sit outside them. So a SPEC commit naming the unit id
# won the selection and its caller then graded ITS parent — where, correctly, no spec exists yet.
# `SHARED_RECORDS` was omitted after that and it is not a corner. A backlog row is owed only by a
# unit planned before its spec, and a run that plans one writes that row in the same commit as the
# spec, which put the commit back outside the exclusion and redded a run that followed the method
# exactly. So the exclusion is whatever the project DECLARES, in either backlog mode: every
# `SHARED_RECORDS` path, and the index half of every `GENERATED_INDEXES` pair, whether the row lands
# in a shared shard or as an ask in the run's own build. `GENERATED_INDEXES` arrives as
# `index:generator` pairs; the generator half is never excluded, because a commit touching the
# GENERATOR is touching product code.
build_commit() {  # rev-range · unit-id · build-dir · generated-indexes · shared-records · [cap] · [order]
  _bc_range=$1; _bc_id=$2; _bc_dir=$3; _bc_gen=$4; _bc_shared=$5
  _bc_cap=${6:-}
  # `$#` AND NOT `${7:-...}`: the pre-anchor caller passes an EMPTY order deliberately, meaning
  # newest-first, and a `:-` default cannot tell that from an absent argument.
  if [ "$#" -ge 7 ]; then _bc_ord=$7; else _bc_ord=--reverse; fi
  _bc_ex=""
  for _bc_i in $_bc_gen; do
    _bc_p=${_bc_i%%:*}
    [ -n "$_bc_p" ] && _bc_ex="$_bc_ex -e ^$_bc_p"
  done
  for _bc_s in $_bc_shared; do
    [ -n "$_bc_s" ] && _bc_ex="$_bc_ex -e ^$_bc_s"
  done
  # THE CAP BOUNDS THE ENUMERATION, not only the loop body. `for _c in $(rev-list ...)` runs the
  # whole traversal in a command substitution BEFORE the first iteration, so a loop-only cap bounds
  # the VERDICT and not the WORK — the `bounded-through-a-pipe-is-unbounded` class. The pre-anchor
  # window is the entire history behind an anchor, so `--max-count` is what bounds it.
  #
  # THE TWO WINDOWS WALK IN OPPOSITE DIRECTIONS, and getting that wrong is what made the pre-anchor
  # probe unable to see its own target. The IN-RANGE walk wants the EARLIEST build commit, so it is
  # `--reverse`. The PRE-ANCHOR probe wants ANY violating commit behind the anchor, and the nearest
  # is both the likeliest and the one that must survive truncation — so it walks NEWEST-FIRST and
  # truncates the FAR end.
  #
  # WHAT WENT WRONG, because it is worth one reader's minute. `rev-list --reverse --max-count=N`
  # applies the count during traversal and reverses AFTER, so the anchor is the LAST element of the
  # window, not the first. The probe was written `--reverse` for both windows on the belief that it
  # yielded the commits nearest the anchor; it yields the farthest. So the one commit the probe
  # exists to reach was dropped by the cap whenever the history behind it was deeper — and the
  # truncation arm could not see that, because it used the record-only fixture, where the correct and
  # the broken behaviour give the same verdict.
  #
  # Truncation is therefore reported AFTER the walk, on the count actually emitted.
  #
  # `cap+1` FETCHED, `cap` GRADED, so truncation is EXACT. With `--max-count=$cap` a complete walk of
  # an exactly-cap-deep window is indistinguishable from a truncated one, and the caller reported
  # TRUNCATED for a probe that had in fact seen everything. Fetching one extra is the only way to
  # know there was more.
  # Does the caller carry a subject cache? Asked ONCE, outside the walk.
  if declare -p _SUBJ >/dev/null 2>&1; then _bc_cache=1; else _bc_cache=0; fi
  _bc_n=0; _bc_mc=""
  [ -n "$_bc_cap" ] && _bc_mc="--max-count=$((_bc_cap+1))"
  for _bc_c in $(GIT rev-list $_bc_ord $_bc_mc $_bc_range 2>/dev/null); do
    _bc_n=$((_bc_n+1))
    # the (cap+1)-th commit is the SENTINEL: proof that more exists, never graded.
    if [ -n "$_bc_cap" ] && [ "$_bc_n" -gt "$_bc_cap" ]; then printf 'TRUNCATED'; return 0; fi
    # FROM THE CALLER'S SUBJECT CACHE WHEN THERE IS ONE, and this is not an optimisation you may drop.
    # `check-pass-order.sh` builds `_SUBJ` in one `git log` over all of HEAD and asserts its size
    # against `rev-list --count`, then walks 10,811 commits through here. Reading a subject per commit
    # instead costs a `git log` AND a `printf|tr` on every one of them, and the leg's own ledger prices
    # the difference at 591 s cached against 3977-5401 s uncached — the second of which straddles its
    # own 5400 s ceiling, so the leg stops being able to answer at all.
    #
    # IT WAS ORPHANED BY THE LIFT THAT CREATED THIS FUNCTION. The cache and its reader were one
    # inline block; the reader moved here and the read did not come with it, so `_SUBJ` was still
    # BUILT and size-asserted by the caller and consulted by nothing. Caught at the push boundary by
    # a 6.7x leg-level regression, not by anything that reads the code.
    #
    # THE PROBE IS DECLARED-ONCE, not per commit: `declare -p` is a builtin but this loop runs tens of
    # thousands of times, and a caller that declares no `_SUBJ` must not error under `set -u`.
    if [ "$_bc_cache" = 1 ]; then _bc_subj=${_SUBJ[$_bc_c]-}; else _bc_subj=""; fi
    # A cached value is ALREADY tokenised and space-padded on both ends, so an empty read is a MISS
    # and nothing else — an empty subject caches as two spaces. A miss falls back to the pair of
    # processes the cache replaced rather than reading as "this commit does not name the id", which
    # would grade the unit unbuilt and report a clean bill.
    #
    # THE WHOLE-TOKEN MATCH is `memory/gotchas/id-matched-as-a-substring`: every id ending in a 1-up
    # sequence is a prefix of nine others, so an unanchored `TOOL-x-1` matches `TOOL-x-19`'s commit.
    [ -n "$_bc_subj" ] || _bc_subj=" $(GIT log -1 --format=%s "$_bc_c" 2>/dev/null | tr -c 'A-Za-z0-9-' ' ') "
    case "$_bc_subj" in *" $_bc_id "*) ;; *) continue ;; esac
    # Did it touch anything outside this build's own record surface?
    if GIT show --pretty=format: --name-only "$_bc_c" 2>/dev/null \
       | grep -v '^$' | grep -qv -e "^$_bc_dir/" $_bc_ex; then
      printf '%s' "$_bc_c"; return 0
    fi
  done
  return 1
}

# ------------------------------------------------------------------- the run's OWN commits
# TOOL-dDerivedDocket-17 S2/section 8 F5. The commits reachable from an ENDPOINT, not reachable from
# a BASE, and not reachable from any of the one or more EXCLUSION TIPS it is handed.
#
# WHY THE EXCLUSIONS EXIST AT ALL, because `base..endpoint` looks like the whole answer. Under
# `in-place` landing `--close` runs on a PREPARED MERGE whose first parent is the advertised tip, so
# every default-branch commit landed since the base is reachable from the endpoint too — and a
# foreign build's row landed in that window would be read as something this run wrote. Excluding the
# advertised tip is what leaves exactly the run's own commits; the alternative that was rejected,
# excluding the first parent of the first two-parent commit, misreads a run branch that merged the
# default branch plainly.
#
# MORE THAN ONE TIP, because unit 19's terminal walk excludes one parent at each merge it reads. The
# T4 caller passes exactly one and the arity costs it nothing.
#
# IT REFUSES RATHER THAN NARROWING. An endpoint or a base this clone cannot resolve would make
# `rev-list` print nothing, and an empty list here reads as "this run wrote no commits" — the exact
# reassuring zero a dead probe must never produce. An exclusion tip that does not resolve is refused
# for the mirror reason: dropping it WIDENS the set silently, which is the direction that grades
# somebody else's commit as this run's.
read_run_commits() {  # endpoint · base · exclusion-tip…
  _rrc_end=$1; _rrc_base=$2; shift 2
  _rrc_ex=""
  [ -n "$_rrc_end" ] && GIT rev-parse --verify --quiet "$_rrc_end^{commit}" >/dev/null 2>&1 || return 1
  [ -n "$_rrc_base" ] && GIT rev-parse --verify --quiet "$_rrc_base^{commit}" >/dev/null 2>&1 || return 1
  for _rrc_t in "$@"; do
    [ -n "$_rrc_t" ] || continue
    GIT rev-parse --verify --quiet "$_rrc_t^{commit}" >/dev/null 2>&1 || return 1
    _rrc_ex="$_rrc_ex ^$_rrc_t"
  done
  GIT rev-list "$_rrc_end" "^$_rrc_base" $_rrc_ex 2>/dev/null
}

# ----------------------------------------------- is a commit touching a path reachable from here
# TOOL-dDerivedDocket-54. Given a COMMIT, a BASE and a PATH: is a commit since BASE that touched PATH
# reachable from COMMIT? The terminal-record exclusion asks it once per PARENT of each merge on a
# witness's tail and reads the pair of answers, so the subject is always a parent - and a parent may
# itself be a merge, which is the one subject at which the two spellings of this walk disagree.
#
# THREE ANSWERS, AND THE THIRD IS NOT THE SECOND. Status 0 is yes. Status 1 is no: the walk ran to
# completion and reached none, which is the answer the caller's fail-closed rule trusts. Status 2 is
# CANNOT ANSWER, with one stderr line naming the commit and the path - the channel `pass_commit`
# uses for the same shape - and stdout stays empty on every answer. A caller that folds 2 into 1
# turns a broken probe into a confident negative, so read the status with `case`, never with `if`.
#
# THE WALK IS UNSIMPLIFIED ON PURPOSE, and the path restriction does not make the flag redundant: a
# path-limited walk prunes every other side of a merge that is TREESAME to one side for that path,
# so a parent that is itself a merge resolving the path back to one side's content answers NO for a
# touching commit it does reach - and what comes back is EXISTENCE only, never which commit, and
# never who wrote either side.
# Measured in a scratch repo on git 2.54.0: from such a nested-merge parent the simplified walk
# prints nothing and `--full-history` prints the merge, while from a plain parent the two agree, so
# the flag changes the answer only where the pruning does. The drift report's product-commit walk
# records the same class for the same flag.
#
# BASE IS REFUSED BEFORE THE WALK unless it RESOLVES TO A COMMIT, and a non-empty test is not that
# test. The caller reads BASE out of the record being graded, so the run supplies it. An empty BASE
# under the range spelling is `HEAD..<commit>`, which exits 0 printing nothing - byte-identical to an
# honest no. A blob or tree sha is a legal object, so `^<object>` excludes no commit and the walk
# answers a confident YES over the whole history. The two fail in OPPOSITE directions, which is why
# one refusal in front of the walk covers both and neither is left to whatever the walk prints.
#
# IT CHECKS THAT BASE IS A COMMIT, NEVER THAT IT IS THE RIGHT ONE. A run-written BASE naming another
# real commit moves the range, and this answers faithfully over the moved range; whether the record
# pins the commit it should is the leg's check 9, not a question this predicate can ask.
#
# A SHALLOW CLONE CANNOT ANSWER. Both ends of the range are computed over grafted roots there: the
# walk from COMMIT can stop short of a touching commit, and "not reachable from BASE" can hold for a
# commit that is BASE's ancestor through history the clone does not have - a wrong answer of either
# sign, so neither is given.
#
# THE PATH IS ONE PATH. A pathspec is a pattern language, and a glob or `:(exclude)` in the value
# would widen or invert the question, so the walk runs under `--literal-pathspecs`.
#
# `--max-count=1` prints one commit at most, so a yes never enumerates the range into this shell. A
# no walks the whole range, and a bound on that belongs to the caller's budget.
check_touching_commit_reachable() { # commit · base · path -> status 0 yes · 1 no · 2 cannot answer
  _tc_c=$1; _tc_b=$2; _tc_p=$3
  _tc_why="lib-unattended: check_touching_commit_reachable cannot answer for commit [$_tc_c] and path [$_tc_p]"
  case $_tc_b in
    *[![:space:]]*) ;;
    *) printf '%s: the BASE is empty or blank, so no walk was started over a range nobody resolved\n' "$_tc_why" >&2
       return 2 ;;
  esac
  _tc_bs=$(GIT rev-parse --verify --quiet "$_tc_b^{commit}" 2>/dev/null) || _tc_bs=""
  if [ -z "$_tc_bs" ]; then
    printf '%s: the BASE [%s] does not resolve to a commit, and a BASE that is not one excludes nothing from the walk\n' "$_tc_why" "$_tc_b" >&2
    return 2
  fi
  _tc_cs=""
  [ -n "$_tc_c" ] && { _tc_cs=$(GIT rev-parse --verify --quiet "$_tc_c^{commit}" 2>/dev/null) || _tc_cs=""; }
  if [ -z "$_tc_cs" ]; then
    printf '%s: the commit does not resolve to a commit in this history\n' "$_tc_why" >&2
    return 2
  fi
  case $_tc_p in
    *[![:space:]]*) ;;
    *) printf '%s: the path is empty or blank, and an empty pathspec is not a path\n' "$_tc_why" >&2
       return 2 ;;
  esac
  case $(GIT rev-parse --is-shallow-repository 2>/dev/null) in
    false) ;;
    true) printf '%s: this clone is shallow, so both ends of the range are computed over grafted history\n' "$_tc_why" >&2
          return 2 ;;
    *) printf '%s: this repository could not say whether it is shallow\n' "$_tc_why" >&2
       return 2 ;;
  esac
  _tc_hit=$(GIT --literal-pathspecs rev-list --full-history --max-count=1 "$_tc_cs" "^$_tc_bs" -- "$_tc_p" 2>/dev/null) || {
    printf '%s: the walk itself failed, so its empty output is not a completed walk\n' "$_tc_why" >&2
    return 2
  }
  [ -n "$_tc_hit" ] && return 0
  return 1
}

# ------------------------------------------------------------------------ the grant grammar
# TOOL-dDerivedDocket-19 S3. A build README may carry ONE front-matter key, `may:`, whose value is one
# physical line of space-separated GRANTS or the single word `none`. A grant is a decision id in the
# grammar `expand_id_runs` reads, or a repo-relative PATH: no leading `/`, no `..` segment, no
# backslash, and a `/` or a file extension somewhere in it. Either may be bare or wrapped in
# backticks, the form an ask row's `may` clause uses, so an owner copying a proposal verbatim and one
# typing it bare pin the SAME bytes.
#
# ONE FUNCTION, TWO CALLERS, and that is why it is here. `--preflight` normalises the README's line
# into the pinned `may:` fact and the leg normalises the same line again to compare against that
# fact. Two spellings would make the comparison depend on how the owner copied the grant, and the leg
# would then red an honest record or pass a forged one according to a backtick.
#
# STATUS 0 prints the grants, backticks stripped and one space apart, or `none`. STATUS 1 prints the
# ONE token it refused, as written, so the refusal can name it — nothing when the value is empty.
# `none` beside a grant is refused like any other token that is neither an id nor a path: a value
# that says both "nothing" and "this" has no honest reading.
#
# WHAT IT DOES NOT CHECK: that an id RESOLVES in the decision log, or that a path EXISTS. It is a typo
# guard over shape, and whether a grant covers a given change is the run's M3 judgement, which no
# code here observes. Split by `read -a`, never by an unquoted expansion, so a token that happens to
# be a glob is refused as the token it is rather than expanded into file names.
parse_grants() { # may: value -> status 0 the grants (or `none`) · status 1 the refused token
  local _pg_w _pg_t _pg_s _pg_out=""
  read -r -a _pg_w <<<"$1"
  [ "${#_pg_w[@]}" -gt 0 ] || return 1
  if [ "${#_pg_w[@]}" = 1 ] && [ "${_pg_w[0]}" = none ]; then printf 'none'; return 0; fi
  for _pg_t in "${_pg_w[@]}"; do
    _pg_s=$_pg_t
    case $_pg_s in \`?*\`) _pg_s=${_pg_s#\`}; _pg_s=${_pg_s%\`} ;; esac
    if ! [[ $_pg_s =~ ^[A-Z]+-[A-Za-z0-9]+-[0-9]+$ ]]; then
      case $_pg_s in
        /*|*\\*|*\`*|..|../*|*/..|*/../*) printf '%s' "$_pg_t"; return 1 ;;
        */*|*?.?*) ;;
        *) printf '%s' "$_pg_t"; return 1 ;;
      esac
    fi
    _pg_out="$_pg_out${_pg_out:+ }$_pg_s"
  done
  printf '%s' "$_pg_out"
}

# ------------------------------------------- the terminal record's exclusions, read by content
# TOOL-dDerivedDocket-19 section 4 and section 8 F8. Given a terminal record's WITNESS, its BASE and
# its RUN-STATE PATH: the tips `read_run_commits` must exclude so that what is left is the commits the
# run itself made. Unit 22's S17 applies the same function to a landing commit.
#
# THE RUN SIDE OF A MERGE IS READ BY CONTENT, never by parent order and never from a default-branch
# tip. At every two-parent commit on the witness's tail, the witness included, the parent from which
# a commit since BASE touching the run-state path is reachable is the run's side: the other parent is
# printed as an exclusion and the walk descends the run side, so nested merges are read in turn. That
# one rule reads unit 2's prepared merge, a plain reconcile on the run branch, the primary lander's
# `--no-ff` landing merge and push-main's own reconcile on the default branch, whichever parent each
# puts the run on. A single-parent commit passes the walk to its parent.
#
# THE RUN-STATE PATH IS THE BUILD FOLDER'S `RUN.md`, even for an archived record: every record commit
# the run made touched that path, and rotation happens after them.
#
# IT STOPS, ADDING NOTHING, where it cannot tell — the fail-closed direction, because an exclusion
# nobody earned removes a run commit from the arm's range. That is a merge where neither parent or
# both reach such a commit, a commit BASE holds, a root, and a commit with more than two parents.
# The walk is bounded by the witness's history since BASE, read ONCE with `rev-list --parents` into
# this shell rather than one git call per step.
#
# STATUS 0 is a completed walk; the exclusions are on stdout, one per line. STATUS 2 is CANNOT
# ANSWER: the witness or BASE does not resolve, or a reachability probe could not answer — its own
# reason line is on stderr — and whatever was printed before that point stands, fewer exclusions
# rather than invented ones. It makes no remote observation, so a stale tip moves no terminal range.
#
# STATED RESIDUAL: it tells a merge's sides by where the record's commits are, not by who made the
# other commits. A side carrying run commits but no commit touching the run-state path since BASE
# reads as default-branch content, and only a branch forked outside the run's history has that shape.
read_run_exclusions() { # witness · base · run-state path -> the exclusion tips, one per line · status 0 read · 2 cannot answer
  local _re_w="${1:-}" _re_b="${2:-}" _re_p="${3:-}" _re_ws _re_bs _re_map _re_cur _re_par _re_p1 _re_p2 _re_rest _re_r1 _re_r2
  _re_ws=$(GIT rev-parse --verify --quiet "$_re_w^{commit}" 2>/dev/null) || _re_ws=""
  _re_bs=$(GIT rev-parse --verify --quiet "$_re_b^{commit}" 2>/dev/null) || _re_bs=""
  if [ -z "$_re_w" ] || [ -z "$_re_b" ] || [ -z "$_re_ws" ] || [ -z "$_re_bs" ]; then
    printf 'lib-unattended: read_run_exclusions cannot answer for witness [%s] and base [%s]: one of them does not resolve to a commit\n' "$_re_w" "$_re_b" >&2
    return 2
  fi
  _re_map=$(GIT rev-list --parents "$_re_ws" "^$_re_bs" 2>/dev/null) || {
    printf 'lib-unattended: read_run_exclusions cannot answer for witness [%s]: the walk of its history since BASE failed\n' "$_re_w" >&2
    return 2
  }
  _re_map=$'\n'"$_re_map"$'\n'
  _re_cur=$_re_ws
  while :; do
    # A COMMIT OUTSIDE THE MAP IS ONE BASE HOLDS, because the map is exactly the witness's history
    # not reachable from BASE. The line is `<commit> <parent>…`, so a match on "\n<commit>" is a
    # match at the start of that commit's own line and never inside another's parent list.
    case $_re_map in *$'\n'"$_re_cur"*) ;; *) break ;; esac
    _re_par=${_re_map#*$'\n'"$_re_cur"}
    _re_par=${_re_par%%$'\n'*}
    read -r _re_p1 _re_p2 _re_rest <<<"$_re_par"
    if [ -z "$_re_p1" ] || [ -n "$_re_rest" ]; then break; fi
    if [ -z "$_re_p2" ]; then _re_cur=$_re_p1; continue; fi
    check_touching_commit_reachable "$_re_p1" "$_re_bs" "$_re_p"; _re_r1=$?
    check_touching_commit_reachable "$_re_p2" "$_re_bs" "$_re_p"; _re_r2=$?
    if [ "$_re_r1" = 2 ] || [ "$_re_r2" = 2 ]; then return 2; fi
    if [ "$_re_r1" = 0 ] && [ "$_re_r2" = 1 ]; then
      printf '%s\n' "$_re_p2"; _re_cur=$_re_p1
    elif [ "$_re_r1" = 1 ] && [ "$_re_r2" = 0 ]; then
      printf '%s\n' "$_re_p1"; _re_cur=$_re_p2
    else
      break
    fi
  done
  return 0
}

# ------------------------------------------------------------ the derived terminal (unit 22)
# TOOL-dDerivedDocket-22, owner ruling D12-i2. A LANDING record whose OWN commit is reachable from
# the tip the remote advertises is landed, and that is DERIVED by the readers rather than written by
# a verb after the push. These four answer the parts both the driver and the gate leg must agree on.
#
# THE LANDING COMMIT, found by CONTENT and never by subject or by walking back. The in-place close
# commits under a fixed subject and a primary close under whatever the agent wrote, so a subject key
# finds one mode's records. And the run-state path is REUSED after a rotation, so walking the path's
# history back to the newest LANDING copy passes a staged, uncommitted LANDING and finds an EARLIER
# run's landing commit - which is on the remote, and would derive the new run landed.
#
# So: the record must be byte-identical to HEAD's copy, and HEAD's copy must read `phase: LANDING`;
# then the answer is the commit that last changed the path, as HEAD's history simplifies it. A staged
# LANDING has no landing commit and cannot derive, which is right: no history a remote could carry
# holds it. An unreadable HEAD copy is NOT LANDING, never read as one. Status 1 prints nothing.
read_landing_commit() { # run-state file -> the commit that carries it at LANDING, or status 1
  local _lc_f="${1:-}" _lc_ph _lc_c
  [ -n "$_lc_f" ] || return 1
  GIT diff --quiet HEAD -- "$_lc_f" 2>/dev/null || return 1
  _lc_ph=$(GIT show "HEAD:$_lc_f" 2>/dev/null | sed -n 's/^phase: *//p' | head -1 | tr -d '\r')
  [ "$_lc_ph" = LANDING ] || return 1
  _lc_c=$(GIT log -1 --format=%H HEAD -- "$_lc_f" 2>/dev/null)
  [ -n "$_lc_c" ] || return 1
  printf '%s\n' "$_lc_c"
}

# THE DATE A RECORD'S OWN RUN BEGAN, for a cutoff that grandfathers by age. It answers a DATE, never
# a sha: `resolve_introducing_commit` in the leg answers the sha a re-derivation needs and refuses
# `--follow` for it, which is a different question with a different ruling (TOOL-dDerivedDocket-52).
#
# `--follow` IS WHAT KEEPS A ROTATION FROM RE-DATING A RECORD. Without it an archived record dates to
# the rotation commit that added its archived name, which moves a pre-cutoff record into the graded
# set: aPacedTurnstile's `RUN.LANDED.a1fd98d8.md` reads 2026-08-20 without it and 2026-08-18 with it.
#
# WHAT `--follow` DOES NOT DO, and the direction of its error. It takes the OLDEST add along the
# followed history, so an archive in a folder that rotated more than once can date to an EARLIER
# run's first commit. That errs toward grandfathering and never toward a frozen red.
#
# THE FLOOR, for the LIVE path. A live `RUN.md` in a folder that has rotated is recorded `M` at the
# rotation and never re-added, so its oldest add is the PREVIOUS run's preflight and the record would
# grade older than it is. Its tenancy of the path began at the newest FIRST TOUCH of an archived
# sibling in the same folder - the rotation - so the date is floored there. First touch rather than
# an add search, because a rotation landing inside a merge records no add at all.
#
# `nofloor` SKIPS THE FLOOR, for a cutoff that predates it. Flooring moves a live record YOUNGER,
# into a graded set it was never graded by, and where that record is already terminal no verb may
# add what the cutoff asks for; the caller that passes it says which record that would be.
#
# `--follow` ALSO FOLLOWS COPIES: at a record's first commit it may continue into another file that
# shares more than half its lines, and date by that one's add. On a real history the source is the
# older file, so the error is again toward grandfathering.
#
# NOTHING PRINTED is "this path has no committed history", which a caller reads as NEW - the one
# thing a record with no first commit certainly is.
read_first_commit_date() { # record path · [nofloor] -> YYYY-MM-DD, or nothing
  local _fd_p="${1:-}" _fd_d _fd_s _fd_t _fd_floor=""
  [ -n "$_fd_p" ] || return 0
  _fd_d=$(GIT log --follow --diff-filter=A --format=%cs -- "$_fd_p" 2>/dev/null | tail -1)
  if [ "${_fd_p##*/}" = RUN.md ] && [ "${2:-}" != nofloor ]; then
    while IFS= read -r _fd_s; do
      [ -n "$_fd_s" ] || continue
      _fd_t=$(GIT log --full-history --format=%cs -- "$_fd_s" 2>/dev/null | tail -1)
      [ -n "$_fd_t" ] || continue
      if [ -z "$_fd_floor" ] || [[ "$_fd_t" > "$_fd_floor" ]]; then _fd_floor=$_fd_t; fi
    done <<SIBLINGS
$(GIT ls-files -- "${_fd_p%/*}/RUN.*.md" 2>/dev/null)
SIBLINGS
  fi
  if [ -n "$_fd_floor" ] && { [ -z "$_fd_d" ] || [[ "$_fd_floor" > "$_fd_d" ]]; }; then _fd_d=$_fd_floor; fi
  printf '%s' "$_fd_d"
}

# IS THIS RECORD GRADED by the landed fact-set arm. Status 0 graded · 1 grandfathered · 2 the arm is
# OFF because the cutoff is blank. A record with no committed history is graded: nothing that has
# not been committed yet can predate a cutoff that has.
#
# THE LAST COMMIT FIRST, because it is one cheap walk and the first-commit read is a `--follow` walk
# per record: a path nothing wrote to at or after the cutoff cannot have begun after it, and on this
# repo that answers almost every record. Its stated limit is a history whose commit DATES run
# backwards along its parents, where the shortcut can grandfather a record the full read would grade.
check_landed_facts_due() { # record path · cutoff -> 0 graded · 1 grandfathered · 2 off
  local _ld_d _ld_l
  [ -n "${2:-}" ] || return 2
  _ld_l=$(GIT log -1 --format=%cs -- "$1" 2>/dev/null)
  [ -n "$_ld_l" ] && [[ "$_ld_l" < "$2" ]] && return 1
  _ld_d=$(read_first_commit_date "$1")
  [ -z "$_ld_d" ] && return 0
  [[ "$_ld_d" < "$2" ]] && return 1
  return 0
}

# THE LANDED FACT SET, one predicate for two callers: the leg's fact-set arm, and `--preflight`,
# which refuses to retire a record that arm would then red for ever. Three populations, each named
# for what makes a record belong to it:
#
#   landed   a recorded LANDED with no `landed-derived` - `--landed` wrote it, so it carries every fact
#            that verb writes: `landed-anchor`, `units-at-landing`, `unpushed-at-landing`
#   derived  a recorded LANDED carrying `landed-derived`, which only the rotation writes - the roster
#            the close froze, and the derivation itself
#   landing  a committed LANDING under in-place landing - the roster `--close` froze beside the phase
#
# `asks-at-landing` is not here: the freeze-presence arm grades it, and one fact graded by two arms
# is two answers to one question. PRESENCE of the key line is the test; a value is a record's own.
# Prints the missing keys, space-separated, and nothing when the set is complete.
read_missing_landed_facts() { # record file · landed|derived|landing -> the missing keys
  local _mf_f="${1:-}" _mf_k _mf_want _mf_out=""
  case "${2:-}" in
    landed)  _mf_want="landed-anchor units-at-landing unpushed-at-landing" ;;
    derived) _mf_want="units-at-landing landed-derived" ;;
    landing) _mf_want="units-at-landing" ;;
    *) return 2 ;;
  esac
  for _mf_k in $_mf_want; do
    grep -q "^$_mf_k:" "$_mf_f" 2>/dev/null || _mf_out="$_mf_out${_mf_out:+ }$_mf_k"
  done
  printf '%s' "$_mf_out"
}

# THE NEXT ANCHOR for a unit after <anchor>, or empty when this is the unit's last row. Chosen by
# ANCESTRY rather than by the order rows appear in the file: the record is append-only and a run may
# park rows in any order, so file order is not history order. The earliest strict descendant wins,
# which is the one that closes this row's window.
next_anchor() {  # anchor · newline-separated candidate anchors
  _na=$1; _nbest=""
  for _nc in $2; do
    [ -n "$_nc" ] || continue
    [ "$_nc" = "$_na" ] && continue
    GIT merge-base --is-ancestor "$_na" "$_nc" 2>/dev/null || continue
    if [ -z "$_nbest" ] || GIT merge-base --is-ancestor "$_nc" "$_nbest" 2>/dev/null; then
      _nbest=$_nc
    fi
  done
  printf '%s' "$_nbest"
}
# THE ROSTER A RUN ENTERED ITS LIVE PHASE WITH — the single answer to "what units did this run start
# with", called by BOTH the checker (check 24, which compares) and the driver (check 48, which
# decides whether an `add` row is late-but-true or a fabrication). TOOL-dUnstalledConvoy-33.
#
# It lived only in the checker, and the driver decided the same question a different way — "is the
# unit in the units region NOW" — which is a different question with a different answer. The two
# together were unsatisfiable: a run whose roster grew before anybody recorded it could never record
# it, because by then the spec existed and the region carried the id. That is the owner's first
# observation, builds refuse to rescope, living in the driver written to let them.
#
# CONTRACT. Prints the baseline units REGION, verbatim, and exits 0 ONLY when it derived a region
# carrying at least one id.
#
# THE REGION TEXT, NOT A LIST OF IDS, and the closing review's blocker is why. The first draft
# printed bare ids; check 24's second loop then asked `id_rows "$rs_was" "$rsid" | grep -q
# "| WONTDO |"`, which can never match a bare id — so its "was it ALREADY retired at the baseline"
# exemption went dead and every build carrying a WONTDO unit from before its run would have redded
# for a retirement nobody performed. The callers want membership and STATUS, and only the region
# carries both. Membership still works: `id_in` matches a whole token anywhere in the text. Exits 1 otherwise, with the reason as its ONLY output — one line, no prefix, so a caller
# can drop it straight into its own message. The reason goes to STDOUT and not stderr, so one
# capture gets either the ids or the reason and the exit code says which; a caller juggling two
# streams for one answer is a caller that will drop one. Empty is a FAILURE and not an empty success: an empty baseline
# makes every unit read as added, which is vacuously accusatory rather than vacuously true.
#
# THE BASELINE IS THE COMMIT THE RUN ENTERED ITS LIVE PHASE AT, never the pinned BASE. A run that
# classifies a unit MISSING and authors its spec is obeying the build method, and every such spec is
# absent at BASE — keying on BASE would red a run for following the method.
# The units region as it stood at a NAMED commit. A SEPARATE PREDICATE from `baseline_units`, not a
# parameterised one: the two answer different questions - "what roster did this run enter its live
# phase with" and "what roster did the owner authorize" - and one predicate serving callers whose
# edges disagree is the shape four adversarial rounds failed to make correct in this kit's dispatch
# grading. The blob read below is the shared half; the commit CHOICE is what differs.
#
# IT VALIDATES ITS COMMIT, and its sibling does not need to. `baseline_units` CHOOSES its commit by
# walking history, so it cannot be handed a bad one; this one is GIVEN one, and an EMPTY value does
# not fail the read - `GIT show ":<path>"` is INDEX syntax and SUCCEEDS, returning plausible bytes.
# A run-state file with an absent or truncated `base:` would therefore silently grade the working
# INDEX instead of the pinned BASE, and the caller's unreadable-baseline skip would never fire
# because the read worked. That is the same degeneration the driver's own `check_authorization`
# header records from an empty base turning a provenance test into a read of the git index.
pinned_units() {  # commit · build-README-path · [cutoff-date]
  _pu_c=$1; _pu_bre=$2; _pu_cut=${3:-}
  command -v region >/dev/null 2>&1 || {
    echo "pinned_units needs a region() in the calling shell and this one has none, so the units region would read as empty and be reported as an empty roster"
    return 1
  }
  case "$_pu_c" in
    [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]*) ;;
    *) echo "the pinned commit is absent or is not sha-shaped, and an empty value reads as INDEX syntax rather than failing, so the comparison would silently grade the working index: [$_pu_c]"
       return 1 ;;
  esac
  GIT cat-file -e "$_pu_c^{commit}" 2>/dev/null || {
    echo "the pinned commit does not resolve to a commit in this history: $_pu_c"
    return 1
  }
  _pu_blob=$(GIT show "$_pu_c:$_pu_bre" 2>/dev/null || true)
  _pu_date=$(GIT show -s --format=%cs "$_pu_c" 2>/dev/null || true)
  if [ -z "$_pu_blob" ]; then
    echo "no build README at the pinned commit, so there is no authorized roster to compare against"
    return 1
  fi
  if ! printf '%s\n' "$_pu_blob" | grep -qxF -- '<!-- gen:build-units -->'; then
    echo "the build README at the pinned commit carries no units region, so the comparison would be vacuous over an empty set"
    return 1
  fi
  if [ -n "$_pu_cut" ] && [ -n "$_pu_date" ] && ! printf '%s\n%s\n' "$_pu_cut" "$_pu_date" | sort -C; then
    echo "the pinned commit predates UNITS_REGION_CUTOFF, so its absent region is grandfathered rather than a defect"
    return 1
  fi
  if ! _pu_was=$(printf '%s\n' "$_pu_blob" | region - '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    echo "the build README at the pinned commit carries a units marker but not exactly one well-formed pair, so there is no single roster to compare"
    return 1
  fi
  # THE EMPTY-ROSTER REFUSAL, which the sibling also carries and for the same reason: `region` exits
  # 0 with empty stdout for a well-formed pair enclosing nothing, so a BASE README with an id-less
  # units region would otherwise return SUCCESS with an empty roster — and every caller's membership
  # test then answers "absent" for every unit in the build. Seven tracked build READMEs are in that
  # state today. Counting the two functions' refusal branches would NOT catch this: both have seven,
  # and the sets differ rather than the sizes.
  _pu_ids=$(printf '%s\n' "$_pu_was" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u)
  if [ -z "$_pu_ids" ]; then
    echo "the roster at the pinned commit names no unit, so every membership test against it answers absent and the comparison would be vacuous rather than clean"
    return 1
  fi
  printf '%s\n' "$_pu_was"
}

baseline_units() {  # run-state-path · build-README-path · [cutoff-date] · [fallback-commit]
  _bu_rel=$1; _bu_bre=$2; _bu_cut=${3:-}; _bu_fb=${4:-}
  # IT CALLS `region`, WHICH THIS LIBRARY DOES NOT DEFINE. Both current callers define their own —
  # two spellings, in the driver and in the checker, and the legs that compare them are the marker
  # contract's, which this build moved off and back onto the automatic bar. A third caller that
  # forgot would get `region: command not found` on stderr and an EMPTY region, which this function
  # would then report as an empty roster: a wrong answer wearing a legitimate refusal. Named and
  # checked rather than assumed, because a dependency a file does not state is one nobody maintains.
  command -v region >/dev/null 2>&1 || {
    echo "baseline_units needs a region() in the calling shell and this one has none, so the units region would read as empty and be reported as an empty roster"
    return 1
  }
  _bu_base=""
  for _bu_c in $(GIT log --reverse --format=%H -- "$_bu_rel" 2>/dev/null); do
    case "$(GIT show "$_bu_c:$_bu_rel" 2>/dev/null | grep -m1 '^phase:')" in
      *BUILDING*|*RUNNING*|*VERIFYING*|*LANDING*|*LANDED*) _bu_base="$_bu_c"; break ;;
    esac
  done
  # THE FALLBACK IS THE CALLER'S, passed in rather than assumed. The checker hands its pinned BASE
  # so a run-state file with no live-phase commit still gets compared; the driver hands nothing, so
  # the same case refuses an `add` rather than deciding on a baseline it did not derive.
  [ -n "$_bu_base" ] || _bu_base=$_bu_fb
  if [ -z "$_bu_base" ]; then
    echo "the run-state file has no commit carrying a live phase and no fallback was given, so there is no baseline commit"
    return 1
  fi
  _bu_blob=$(GIT show "$_bu_base:$_bu_bre" 2>/dev/null || true)
  _bu_date=$(GIT show -s --format=%cs "$_bu_base" 2>/dev/null || true)
  if [ -z "$_bu_blob" ]; then
    echo "no build README at the baseline commit, so there is no authorized roster to compare against"
    return 1
  fi
  if ! printf '%s\n' "$_bu_blob" | grep -qxF -- '<!-- gen:build-units -->'; then
    echo "the baseline build README carries no units region, so the comparison would be vacuous over an empty set"
    return 1
  fi
  if [ -n "$_bu_cut" ] && [ -n "$_bu_date" ] && ! printf '%s\n%s\n' "$_bu_cut" "$_bu_date" | sort -C; then
    echo "the baseline predates UNITS_REGION_CUTOFF, so its absent region is grandfathered rather than a defect"
    return 1
  fi
  if ! _bu_was=$(printf '%s\n' "$_bu_blob" | region - '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    echo "the baseline build README carries a units marker but not exactly one well-formed pair, so there is no single roster to compare"
    return 1
  fi
  # The ids are derived only to decide EMPTINESS. An empty baseline is not a comparison and is not
  # vacuously true either — it is vacuously accusatory, because every unit the build has would read
  # as added.
  _bu_ids=$(printf '%s\n' "$_bu_was" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u)
  if [ -z "$_bu_ids" ]; then
    echo "the baseline roster names no unit, so every unit this build has would read as added and the comparison would accuse rather than check"
    return 1
  fi
  printf '%s\n' "$_bu_was"
}

# ------------------------------------------------------------------------- the ask FILING match
# TOOL-dDerivedDocket-16 S4. Property P5 asks one question of a `BACKLOG.md` blob: does this ask
# have a row there. The DRIVER asks it at preflight, over the blob at `m-base:`; the gate leg asks
# it again over the same blob when it re-derives the pinned facts. Two spellings of one grammar is
# the class this whole file exists for, so the match lives here and neither caller writes its own.
#
# FILING IS NOT STATUS, and that is the whole reason this can live in a shell library at all. A row
# says the ask EXISTS in a tree the run did not write; what its derived status IS comes from the
# declared generator's fold, which this kit neither carries nor re-implements.
#
# ANCHORED AT COLUMN 1 BY `index(...) == 1`, not by a regex, because the id is a value a caller
# supplies: a regex would give `.` and `*` in a malformed argument meaning they do not have, and a
# substring test would let a `SCOPE` row or a prose mention answer for a filing.
#
# THE PREFIX IS `- <ID> · filed `, the ask row's own opening as the memory kit's grammar spells it.
# A row whose separator or date field differs is not a filed ask and must not answer as one.
#
# ENVIRON RATHER THAN `awk -v`: a -v assignment expands backslash sequences, and the id is a caller's
# bytes. Same rule the sibling suite's fixture writer already states for its row bodies.
ask_filed_in() { # BACKLOG.md text · ask id -> 0 when that text FILES the ask
  printf '%s\n' "$1" | AFI_ID="$2" awk '
    BEGIN { p = "- " ENVIRON["AFI_ID"] " · filed " }
    index($0, p) == 1 { f = 1 }
    END { exit !f }'
}
# THE SAME GRAMMAR READ THE OTHER WAY: every id a blob files, in file order. `--plan --asks` needs
# the SET (the asks filed in a build's own folder), and deriving it by calling the match above once
# per candidate id would need a candidate list, which is the thing this answers.
asks_filed_in() { # BACKLOG.md text -> every filed ask id, one per line, in file order
  printf '%s\n' "$1" \
    | sed -n 's/^- \([A-Z][A-Z]*-[A-Za-z0-9][A-Za-z0-9]*-[0-9][0-9]*\) · filed .*/\1/p'
}
# ...and the `unit` SUBSET. `- <ID> · filed <DATE> · unit · <TEXT>` is an ask that IS a unit of the
# build whose folder files it, so design section 19.4 makes it roster. `unit` is recognised as the
# WHOLE field after the date and never as a prefix of the text, which is the memory kit's own rule.
asks_unit_in() { # BACKLOG.md text -> every filed `unit` ask id, one per line, in file order
  printf '%s\n' "$1" \
    | sed -n 's/^- \([A-Z][A-Z]*-[A-Za-z0-9][A-Za-z0-9]*-[0-9][0-9]*\) · filed [0-9][0-9-]* · unit · .*/\1/p'
}
# ------------------------------------------------------------ the id-run expander, and the home
# MOVED HERE FROM THE DRIVER by TOOL-dDerivedDocket-18, unchanged, for the reason the ask match
# above is here: the gate leg re-derives the pinned mandate and must answer "which ids is this run
# under" with the SAME bytes the driver answered it with. Two expanders disagree silently on the
# one input that matters - a range - and the leg would then red an honest record for a row it never
# looked for. The leg can source no driver, so a shared answer has to live in the shared file.
#
# The RECORD-BINDING id grammar is WIDER than `_ids_of`'s, and reading it with the narrow one is
# wrong in both directions. `memory/HYGIENE.md` admits a trailing `@rev-N` and a contiguous run
# written `<family>-<slug>-N..M`, which EXPANDS at authoring time - and only `gen_build_index.py`
# expands it, which is the memory-tree kit's, and this kit copy-installs without it. Measured over
# this corpus: 18 of 123 tracked `spec-audit` binding lines use the range form. A join that does not
# expand blocks a unit that WAS audited under `TOOL-x-1..5`; a join that matches as a SUBSTRING lets
# `TOOL-x-19` satisfy `TOOL-x-1`. This emits whole tokens, one per line, for a `grep -qxF` join.
expand_id_runs() { # stdin: binding-line text -> stdout: ids, ranges expanded, one per line
  awk '{
    n = split($0, w, /[ \t]+/)
    for (i = 1; i <= n; i++) {
      t = w[i]
      sub(/@rev-[0-9]+$/, "", t)
      if (t ~ /^[A-Z]+-[A-Za-z0-9]+-[0-9]+\.\.[0-9]+$/) {
        p = index(t, "..")
        head = substr(t, 1, p - 1); hi = substr(t, p + 2) + 0
        match(head, /[0-9]+$/); lo = substr(head, RSTART) + 0
        stem = substr(head, 1, RSTART - 1)
        for (k = lo; k <= hi; k++) print stem k
      } else if (t ~ /^[A-Z]+-[A-Za-z0-9]+-[0-9]+$/) print t
    }
  }'
}
# The build folder an ask is FILED in: the slug segment of its own id. An id nobody filed still
# names its home this way, which is what lets the P5 refusal say WHERE to go and look. MOVED HERE
# from the driver with the expander above, and for the same reason: the leg reads the same blob per
# home and a second spelling of "which folder" would send the two readers at different files.
ask_home_of() { # ask id -> the slug segment
  local _t="${1#*-}"; printf '%s' "${_t%-*}"
}
