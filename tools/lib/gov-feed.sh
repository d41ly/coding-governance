#!/usr/bin/env bash
# The governance change feed, canonical copy (TOOL-dPlacedRequest-13, I4).
#
# USAGE: `<prefix>/lib/` ships nothing, so a writer cannot source this file. Each writer that carries
# the `gov_ref_sh` block carries the block between the markers below INLINE beside it, byte-identical,
# and the parity table in `resolve-python.test.sh` beside this file reds a copy that drifts. Every
# carrier also holds the `health_log_sh` block inline, or reaches it through a library it sources,
# because the lock's self-heals append through it (TOOL-dPlacedRequest-36). A probe
# sources this file whole, beside gov-ref.sh. The writer census BELOW the closing marker is no
# carrier's: only the lib test and a probe read it, from here.

# >>> gov_feed_sh — canonical copy: gov-feed.sh in gov's lib dir (byte-identical; gated)
# THE NODE LOCKS (TOOL-dPlacedRequest-24): a node-local file two sessions of this node write, the
# feed's log and the offline queue's, is read and written only under a lock directory beside it in
# the common dir, taken through `write_dir_lock_wait` with the stem `node`, so a stale break appends
# `node-lock-broken` or `node-guard-cleared`. NODE_LOCK_BOUND is the seconds a node lock may hold:
# a pinned literal, because a holder does local file work alone and never pushes while it holds.
NODE_LOCK_BOUND=10
# THE DIRECTORY LOCK (TOOL-aGraftedHelix-37), a factory (TOOL-aPiecewiseGrade-6), moved into this
# block (TOOL-dPlacedRequest-24) so every carrier holds the one definition. `write_dir_lock` takes the
# lock with `mkdir` and writes its deadline into `until` and the caller's token into `owner`. A lock it cannot
# make is broken only when `check_dir_lock_stale` reads it stale - a deadline already passed,
# or none and a directory older than two minutes - and only by the writer that takes the guard
# `<lock>.break` with `mkdir`. Holding the guard it re-reads the rule, breaks a lock still stale,
# makes it again and writes both files before it releases the guard; a re-read finding the lock live,
# or a re-make losing to a plain `mkdir`, releases the guard and reports busy. So no breaker removes
# a lock another breaker made. A guard older than one minute was left by a crash: the writer finding
# it removes it and reports busy, never taking it in the same call, and the next call breaks the
# lock. Each self-heal appends a health event, named from the caller's stem, once the guard is
# released. `write_dir_lock_wait` is the one retrying take: it calls `write_dir_lock` every 50 ms
# until it takes or its ceiling in seconds passes, read on the whole-second clock. `remove_dir_lock`
# clears the lock only while its `owner` reads the caller's token, the turnstile's nonce pattern, so
# a release never removes the fresh lock of a writer that broke it. `until` stays a bare epoch.
# WHAT THIS DOES NOT CHECK: removing an abandoned guard is itself unguarded, so two writers removing
# one at once while a third takes a fresh guard between them can admit two breakers; that needs a
# writer to die or stall for a minute inside the break, then four writers in one git dir in one
# window. An owner that outlives its recorded deadline (no runnable `timeout -k`) is breakable while
# it pushes, and its own release can land between a breaker's re-read and its removal. Both the
# deadline and the age are wall-clock reads, so a clock stepped forward breaks a live lock.
# A writer in another git dir takes another lock. Each event goes through the `health_log_sh` block
# every carrier holds beside this one (TOOL-dPlacedRequest-36), to `resolve_health_log` of `ROOT`
# where the driver sets it, so its spec-tokens lock in the sidecar dir logs to the repository's log,
# else of the lock's parent, which for a node lock is the common dir: no unset name under `set -u`.
# THE OWNER'S PROCESSES, read as data in the lock (TOOL-aPiecewiseGrade-6 S9). A holder may write one
# `pid.<role>` file per process with `write_dir_lock_pid`: the pid, its procfs start token or `-`, the
# writer's runtime as `$HOSTNAME:$OSTYPE`, and an optional end file, last because a path may carry a
# space. `check_dir_lock_stale` also reads a lock stale when it holds at least one such file and every
# one names a process gone: a digit pid, this runtime, `check_proc_gone` answering gone, and an end
# file that exists or whose directory is gone, or none recorded. An empty file, the pending `-`, a
# foreign runtime or a missing stamp reads live. A lock with no pid file keeps the deadline and age
# rule alone. The procfs read is `${PROCFS_ROOT:-/proc}`: the driver sets PROCFS_ROOT from its fixture
# seam, and a carrier with no driver reads `/proc`.
# WHAT THIS DOES NOT CHECK: two process tables printing one `$HOSTNAME:$OSTYPE`, such as two MSYS
# installs on one host, read each other's pids gone and can break a live lock; and a reused pid with
# no token reads live, so its lock waits for the deadline.
PT_TOKEN=""
read_proc_token() { # pid -> sets PT_TOKEN to its procfs start token, or `-` when procfs cannot say
  local _l="" _r
  local -a _f
  PT_TOKEN=-
  case "${1:-}" in ""|*[!0-9]*) return 0 ;; esac
  { IFS= read -r _l < "${PROCFS_ROOT:-/proc}/$1/stat" || [ -n "$_l" ]; } 2>/dev/null || return 0
  # EVERY FIELD AFTER THE LAST `)` IS NUMERIC OR ONE LETTER. The command name inside the parentheses
  # may carry spaces and parentheses of its own, so the split starts after it: field 3 is `_f[0]`.
  _r=${_l##*) }
  read -r -a _f <<<"$_r"
  [ "${#_f[@]}" -ge 20 ] || return 0
  case "${_f[19]}" in ""|*[!0-9]*) return 0 ;; esac
  PT_TOKEN=${_f[19]}
  return 0
}
# Is the RECORDED process still there? Dead, or its pid now carrying another start token, is gone.
check_proc_gone() { # pid · recorded token -> 0 when that process no longer exists
  kill -0 "$1" 2>/dev/null || return 0
  [ "${2:--}" != - ] || return 1
  read_proc_token "$1"
  [ "$PT_TOKEN" != - ] && [ "$PT_TOKEN" != "$2" ] && return 0
  return 1
}
check_dir_lock_stale() { # lock dir -> 0 when its deadline passed, or it has none and is older than two minutes, or every process it records is gone
  local lu="" f p t w e n=0; { read -r lu <"$1/until"; } 2>/dev/null || :
  case "$lu" in *[!0-9]*) lu="" ;; esac
  for f in "$1"/pid.*; do
    [ -f "$f" ] || continue
    p=""; t=""; w=""; e=""; { read -r p t w e <"$f"; } 2>/dev/null || :
    case "$p" in ""|*[!0-9]*) n=-1; break ;; esac
    [ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ] && check_proc_gone "$p" "$t" \
      && { [ -z "$e" ] || [ -e "$e" ] || [ ! -d "${e%/*}" ]; } || { n=-1; break; }
    n=$((n + 1))
  done
  [ "$n" -le 0 ] || return 0
  if [ -n "$lu" ]; then [ "$lu" -lt "$EPOCHSECONDS" ]; return; fi
  [ -n "$(find "$1" -maxdepth 0 -mmin +2 2>/dev/null)" ]
}
write_dir_lock_pid() { # lock dir · role · pid, or - for pending · end file, optional -> <lock>/pid.<role> written; always 0
  read_proc_token "$3"
  printf '%s %s %s %s\n' "$3" "$PT_TOKEN" "${HOSTNAME:-}:${OSTYPE:-}" "${4:-}" >"$1/pid.$2" 2>/dev/null || :
  return 0
}
write_dir_lock() { # lock dir · owner token · seconds it may hold · health-event stem -> 0 taken, 1 busy
  local lk="$1" g="$1.break" broke=""
  if ! mkdir "$lk" 2>/dev/null; then
    check_dir_lock_stale "$lk" || return 1
    if ! mkdir "$g" 2>/dev/null; then
      if [ -n "$(find "$g" -maxdepth 0 -mmin +1 2>/dev/null)" ]; then
        rm -rf "$g"
        add_health_event "$(resolve_health_log "${ROOT:-${1%/*}}")" unattended "$4-guard-cleared" "$g"
      fi
      return 1
    fi
    if ! check_dir_lock_stale "$lk"; then rmdir "$g" 2>/dev/null; return 1; fi
    rm -rf "$lk"
    mkdir "$lk" 2>/dev/null || { rmdir "$g" 2>/dev/null; return 1; }
    broke=1
  fi
  printf '%s\n' "$(( $EPOCHSECONDS + $3 ))" >"$lk/until" 2>/dev/null || :
  printf '%s\n' "$2" >"$lk/owner" 2>/dev/null || :
  if [ -n "$broke" ]; then
    rmdir "$g" 2>/dev/null
    add_health_event "$(resolve_health_log "${ROOT:-${1%/*}}")" unattended "$4-lock-broken" "$lk"
  fi
  return 0
}
write_dir_lock_wait() { # lock dir · owner token · seconds it may hold · health-event stem · seconds to wait -> 0 taken, 1 busy
  local end=$(( EPOCHSECONDS + ${5:-0} ))
  until write_dir_lock "$1" "$2" "$3" "$4"; do
    [ "$EPOCHSECONDS" -lt "$end" ] || return 1
    sleep 0.05
  done
  return 0
}
remove_dir_lock() { # lock dir · owner token -> removes it only while its owner file reads that token
  local o=""; { read -r o <"$1/owner"; } 2>/dev/null || :
  [ -n "$2" ] && [ "$o" = "$2" ] && rm -rf "$1"
  return 0
}
# I4, THE CHANGE FEED (TOOL-dPlacedRequest-13): `<git-common-dir>/gov-feed.log`, node-local and never
# pushed, one LF-terminated line per governance ref write this node made or saw, six TAB fields:
# seq (a positive integer rising across refs), ref (the remote ref name), kind (the segment after
# `refs/gov/`), blob (the commit's tree, `-` on a deletion), commit (40 hex, 40 zeros on a deletion)
# and seen-utc (`2026-10-25T14:03:07Z`, this node's clock at the append). The key is ref, blob and
# commit. `write_gov_ref`'s success exit calls `add_feed_event`, so every writer joins by construction.
# APPENDING ONCE: under the feed's node lock (above, a 5 s wait) an event whose blob and commit
# equal the newest line of its ref appends nothing (TOOL-dPlacedRequest-27), so a retry appends nothing and a repeat with another
# event of the ref between, a second clear of `bar-red` say, appends again; `seq` is one more
# than the larger of the counter `gov-feed.seq` and the last all-digit first field of the log, so a
# lagging counter never repeats a `seq`; a last byte that is not LF is closed with one first, so a
# torn line stays for `check_feed` to name. A failure prints ONE `feed: NOTE -` line on stderr and
# returns 0, as the health log's appender does: the governance write already landed.
# THE CONTAINED APPEND (TOOL-dPlacedRequest-39): the clock test, the common dir and the git reads run
# in the caller's shell; the lock, the key check, the counter and the append run in a subshell whose
# `EXIT` trap, armed once the lock is taken, calls `remove_dir_lock` with this call's token. So an
# abort inside it, an unbound name under a carrier's `set -u`, a function no carrier defines or a
# failed write, ends the subshell alone: the append prints `feed: NOTE - <ref>: the append exited
# <rc>` and returns 0, and no lock is left for the next writer to wait out. The subshell sets no
# global a caller reads. WHAT THIS DOES NOT CHECK: an abort between the take and the trap's arming
# leaves the lock to its deadline; an abort after the line is written reads as a NOTE all the same.
# THE BASH FLOOR (TOOL-dPlacedRequest-37): a node lock's deadline reads `EPOCHSECONDS`, bash 5's,
# and this is the one take a carrier with no driver reaches, so where it is unset the append prints
# one `feed: NOTE -` line naming it and returns 0, before it touches the lock, the log or git.
# THE CACHE `refs/gov/remote/<tail>` mirrors `refs/gov/<tail>` on the remote: what this node fetched
# and, through `write_gov_ref`, what it wrote. `add_feed_sightings` appends, oldest first, the unseen
# first-parent chain of every cached ref whose tip is not the commit of the feed's newest line for
# that ref, stopping at that commit or at the first commit not authored `gov-claim`, appended as a
# lone event, so a ref another node set back to a commit an older line holds is sighted again.
# `derive_feed_events` is the same walk with no feed to stop at; `check_feed` holds a feed to it per
# ref git still holds (`missing`, `duplicate` for two consecutive events of one ref with one blob and
# commit, `extra` on a ref whose tip is a `gov-claim` commit, `order`, `torn`), and `write_feed`
# writes it as a fresh feed where none is present.
# GOVFEED_DIR names the common dir; unset, the first call resolves it once for the process.
# WHAT THIS DOES NOT CHECK: two breakers the guard's own blind spots (above) admit can both append, which
# gives two events one `seq` and loses none; `seq` and `seen-utc` are node-local and never compared; a
# ref's events from before a deletion of it are outside every chain git holds and are not compared;
# a retry made after another event of its ref landed appends again, an event that did happen.
add_feed_event() {   # ref · commit, or empty for a deletion -> 0 always, the event appended once
  local ref="$1" c="${2:-}" d k t=- r s=0 l n now tok rc=0
  [ -n "${EPOCHSECONDS:-}" ] || { printf 'feed: NOTE - no EPOCHSECONDS, bash 5 or later is required\n' >&2; return 0; }
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -n "$d" ] || { printf 'feed: NOTE - no git common dir resolves here, so this write of %s is not in the feed\n' "$ref" >&2; return 0; }
  k=${ref#refs/gov/}; k=${k%%/*}
  if [ -z "$c" ]; then
    c=0000000000000000000000000000000000000000
  else
    r=$(git rev-parse "$c^{commit}" "$c^{tree}" 2>/dev/null) || r=""
    r=${r//$'\r'/}; c=${r%%$'\n'*}; t=${r#*$'\n'}
    [ "${#c}:${#t}" = 40:40 ] || c=""
    case "$c$t" in *[!0-9a-f]*|"") printf 'feed: NOTE - %s names no commit this clone holds, so the write is not in the feed\n' "$ref" >&2; return 0 ;; esac
  fi
  tok="$BASHPID.$RANDOM"
  ( write_dir_lock_wait "$d/gov-feed.lock" "$tok" "$NODE_LOCK_BOUND" node 5 || exit 3
    trap 'remove_dir_lock "$d/gov-feed.lock" "$tok"' EXIT
    if [ -f "$d/gov-feed.log" ] && FEED_EV="$ref"$'\t'"$t"$'\t'"$c" awk -F'\t' '
        BEGIN { split(ENVIRON["FEED_EV"], ev, "\t") }
        $2 == ev[1] { p = $4 "\t" $5 }
        END { exit !(p == ev[2] "\t" ev[3]) }' "$d/gov-feed.log" 2>/dev/null; then
      exit 0
    fi
    if [ -f "$d/gov-feed.seq" ]; then { read -r s <"$d/gov-feed.seq"; } 2>/dev/null || :; fi
    s=${s%$'\r'}
    case "$s" in ""|*[!0-9]*) s=0 ;; esac
    l=0
    if [ -s "$d/gov-feed.log" ]; then
      l=$(awk -F'\t' '$1 ~ /^[0-9]+$/ { s = $1 } END { print s + 0 }' "$d/gov-feed.log" 2>/dev/null) || l=0
      case "$l" in ""|*[!0-9]*) l=0 ;; esac
      [ -z "$(tail -c1 "$d/gov-feed.log" 2>/dev/null)" ] || printf '\n' >>"$d/gov-feed.log"
    fi
    n=$(( (10#$s > 10#$l ? 10#$s : 10#$l) + 1 ))
    TZ=UTC printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1
    if ! printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$n" "$ref" "$k" "$t" "$c" "$now" >>"$d/gov-feed.log" 2>/dev/null; then
      printf 'feed: NOTE - %s/gov-feed.log could not be written, so this write of %s at %s is not in the feed\n' "$d" "$ref" "$c" >&2
    elif ! { printf '%s\n' "$n" >"$d/gov-feed.seq.$$" && mv -f "$d/gov-feed.seq.$$" "$d/gov-feed.seq"; } 2>/dev/null; then
      rm -f "$d/gov-feed.seq.$$" 2>/dev/null
      printf 'feed: NOTE - %s/gov-feed.seq could not be written; the next append reads the log past it\n' "$d" >&2
    fi
    exit 0 ) || rc=$?
  case "$rc" in
    0) ;;
    3) printf 'feed: NOTE - the feed lock in %s was held for 5s, so this write of %s at %s is not in the feed\n' "$d" "$ref" "$c" >&2 ;;
    *) printf 'feed: NOTE - %s: the append exited %s\n' "$ref" "$rc" >&2 ;;
  esac
  return 0
}
derive_feed_events() { # cache prefix · [feed file] -> `ref TAB kind TAB blob TAB commit` per event, per ref oldest first
  local pre="${1%/}/" feed="${2:-}" rows r t g s
  rows=$(git for-each-ref --format='%(refname) %(objectname)' "$pre" 2>/dev/null | FEED_FILE="$feed" FEED_PRE="$pre" awk '
    BEGIN { f = ENVIRON["FEED_FILE"]
            if (f != "") while ((getline ln < f) > 0) {
              sub(/\r$/, "", ln)
              if (split(ln, x, "\t") < 5) continue
              newest[x[2]] = x[5] } }
    { sub(/\r$/, ""); g = "refs/gov/" substr($1, length(ENVIRON["FEED_PRE"]) + 1)
      if ((g in newest) && newest[g] == $2) next
      print $2, g, (g in newest ? newest[g] : "-") }')
  [ -n "$rows" ] || return 0
  printf '%s\n' "$rows" | while read -r t g s; do
    git log --first-parent --format='%H %T %an' "$t" 2>/dev/null | awk -v ref="$g" -v stop="$s" '
      { sub(/\r$/, "") }
      $1 == stop { exit }
      { a = $0; sub(/^[^ ]+ [^ ]+ /, "", a); n++; h[n] = $1; tr[n] = $2; if (a != "gov-claim") exit }
      END { k = ref; sub(/^refs\/gov\//, "", k); sub(/\/.*$/, "", k)
            for (i = n; i >= 1; i--) printf "%s\t%s\t%s\t%s\n", ref, k, tr[i], h[i] }'
  done
  return 0
}
add_feed_sightings() { # cache prefix -> 0 always; every unseen commit of a cached ref appended oldest first
  local pre="${1:-refs/gov/remote/}" r k t c
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  [ -n "${GOVFEED_DIR%$'\r'}" ] || return 0
  while IFS=$'\t' read -r r k t c; do
    [ -z "$c" ] || add_feed_event "$r" "$c"
  done < <(derive_feed_events "$pre" "${GOVFEED_DIR%$'\r'}/gov-feed.log")
  return 0
}
check_feed() {       # cache prefix · [feed file, the node's by default] -> one line per finding and rc 1, or rc 0
  local pre="${1%/}/" f="${2:-}" dv au
  if [ -z "$f" ]; then
    [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
    f="${GOVFEED_DIR%$'\r'}/gov-feed.log"
  fi
  dv=$(derive_feed_events "$pre")
  au=$(git for-each-ref --format='%(refname) %(authorname)' "$pre" 2>/dev/null)
  FEED_FILE="$f" FEED_PRE="$pre" FEED_DV="$dv" FEED_AU="$au" awk '
    BEGIN {
      np = length(ENVIRON["FEED_PRE"])
      m = split(ENVIRON["FEED_AU"], a, "\n")
      for (i = 1; i <= m; i++) { ln = a[i]; sub(/\r$/, "", ln); if (ln == "") continue
        r = ln; sub(/ .*$/, "", r); au = ln; sub(/^[^ ]* /, "", au)
        g = "refs/gov/" substr(r, np + 1); held[g] = 1; if (au == "gov-claim") chain[g] = 1 }
      m = split(ENVIRON["FEED_DV"], a, "\n")
      for (i = 1; i <= m; i++) { if (split(a[i], x, "\t") != 4) continue
        dn[x[1]]++; ds[x[1], dn[x[1]]] = x[4]; inch[x[1] SUBSEP x[4]] = 1 }
      f = ENVIRON["FEED_FILE"]; bad = 0
      while ((getline ln < f) > 0) {
        sub(/\r$/, "", ln)
        if (split(ln, x, "\t") != 6) { print "torn " ln; bad = 1; continue }
        k = x[4] SUBSEP x[5]
        if ((x[2] in last) && last[x[2]] == k) { print "duplicate " x[2] " " x[5]; bad = 1; continue }
        last[x[2]] = k
        if (!(x[2] in held)) continue
        if ((x[2] SUBSEP x[5]) in inch) { fn[x[2]]++; fs[x[2], fn[x[2]]] = x[5]; got[x[2] SUBSEP x[5]] = 1 }
        else if (x[2] in chain) { print "extra " x[2] " " x[5]; bad = 1 }
      }
      for (g in dn) {
        j = 0; off = ""
        for (i = 1; i <= dn[g]; i++) {
          c = ds[g, i]
          if (!((g SUBSEP c) in got)) { print "missing " g " " c; bad = 1; continue }
          j++; if (off == "" && fs[g, j] != c) off = fs[g, j]
        }
        if (off != "") { print "order " g " " off; bad = 1 }
      }
      exit bad }'
}
write_feed() {       # cache prefix -> rc 0 the derived feed written, rc 2 naming a feed already present
  local pre="${1%/}/" d now n=0 l
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -n "$d" ] || { printf 'feed: no git common dir resolves here, so no feed was rebuilt\n'; return 2; }
  if [ -e "$d/gov-feed.log" ]; then printf 'feed: a feed is present, so nothing was rebuilt over it: %s\n' "$d/gov-feed.log"; return 2; fi
  TZ=UTC printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1
  { while IFS= read -r l; do n=$((n + 1)); printf '%s\t%s\t%s\n' "$n" "$l" "$now"; done < <(derive_feed_events "$pre"); } >"$d/gov-feed.log.$$" \
    && printf '%s\n' "$n" >"$d/gov-feed.seq.$$" && mv -f "$d/gov-feed.seq.$$" "$d/gov-feed.seq" && mv -f "$d/gov-feed.log.$$" "$d/gov-feed.log" \
    || { rm -f "$d/gov-feed.log.$$" "$d/gov-feed.seq.$$"; printf 'feed: %s could not be written, so no feed was rebuilt\n' "$d/gov-feed.log"; return 2; }
  printf 'feed: rebuilt %s event(s) from %s into %s\n' "$n" "$pre" "$d/gov-feed.log"
  return 0
}
print_feed() {       # [seq] -> every event whose seq is at or after it, in file order
  local from="${1:-0}" d
  case "$from" in ""|*[!0-9]*) printf 'feed: a replay starts at a sequence number, not %s\n' "$from"; return 2 ;; esac
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -f "$d/gov-feed.log" ] || return 0
  awk -F'\t' -v from="$from" 'NF == 6 && $1 ~ /^[0-9]+$/ && $1 + 0 >= from + 0' "$d/gov-feed.log"
}
# THE OBSERVER CLOCK, I8 (TOOL-dPlacedRequest-17): the one reader of a first sighting. Per
# `ref TAB commit` pair on stdin, in order, the `seen-utc` of the oldest feed line of that ref and
# commit, or `-` where the feed holds none, has none of that shape, or cannot be read. Every lease
# deadline is now minus that stamp, both read on this node's clock, never the holder's `beat-utc`.
read_first_seen() {  # `ref TAB commit` pairs on stdin -> one `seen-utc` or `-` per pair
  local f=""
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  [ -z "${GOVFEED_DIR%$'\r'}" ] || f="${GOVFEED_DIR%$'\r'}/gov-feed.log"
  FEED_FILE="$f" awk -F'\t' '
    BEGIN { f = ENVIRON["FEED_FILE"]
            if (f != "") while ((getline ln < f) > 0) {
              sub(/\r$/, "", ln)
              if (split(ln, x, "\t") != 6 || x[6] !~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z$/) continue
              if (!((x[2] SUBSEP x[5]) in seen)) seen[x[2], x[5]] = x[6] } }
    { sub(/\r$/, ""); print (($1 SUBSEP $2) in seen ? seen[$1, $2] : "-") }'
}
# <<< gov_feed_sh

# THE WRITER CENSUS (TOOL-dPlacedRequest-13 S9), outside the block, so no carrier ships it. The shape is
# check 51's in the unattended kit gate: ONE declared helper level. Limb 1: a non-comment line carrying
# the whole word `push` and a lease flag must sit in a function whose body calls a name on
# FEED_WRITER_HELPER_FNS; each other one prints `<file>:<line>` unless FEED_WRITER_EXEMPT_FNS names its
# function. Limb 2: a non-comment line carrying the word `push` and a governance ref prefix and no
# lease flag prints `<file>:<line>` in any function, since such a write is no compare-and-swap. Both
# lists are graded both ways: a helper entry that is no function of the files read, or whose body
# neither appends to the feed log nor calls another entry, and an exempt entry naming a function
# limb 1 would not hit, each print a line naming the entry; a scan that finds no lease-carrying line
# prints one line saying so, never a pass. Returns 1 when it printed anything.
# The tokens it matches are assembled from pieces, so this file's own source never matches them.
# WHAT THIS DOES NOT CHECK: a push whose ref is spelled through a variable and carries no lease; a
# push assembled across `\`-continued lines; a writer in Python; a helper of a helper.
FEED_WRITER_HELPER_FNS="add_feed_event write_gov_ref"
FEED_WRITER_EXEMPT_FNS=""
scan_feed_writers() { # file… -> one line per hit, rc 1; nothing, rc 0
  local out
  out=$(FW_HELPERS="$FEED_WRITER_HELPER_FNS" FW_EXEMPT="$FEED_WRITER_EXEMPT_FNS" awk '
    function write_held_fn() {
      if (fn != "") seen[fn] = 1
      if (np > 0 && (fn == "" || !hc)) { if (fn != "") cand[fn] = 1; if (fn == "" || !(fn in ex)) hits = hits pend }
      fn = ""; hc = 0; np = 0; pend = ""
    }
    function scan(s, at,   h) {
      for (h in helper) if (h != fn && match(s, "(^|[^A-Za-z0-9_])" h "([^A-Za-z0-9_]|$)")) { hc = 1; if (fn != "") calls[fn] = 1 }
      if (fn != "" && s ~ />>/ && index(s, LOG) > 0) apnd[fn] = 1
      if (s !~ PW) return
      if (index(s, LEASE) > 0) { nl++; np++; pend = pend "\n" at }
      else if (index(s, GOV) > 0) lim2 = lim2 "\n" at
    }
    BEGIN { LEASE = "--force-" "with-lease"; GOV = "refs/" "gov/"; LOG = "gov-" "feed.log"
            PW = "(^|[^A-Za-z0-9_])p" "ush([^A-Za-z0-9_]|$)"
            k = split(ENVIRON["FW_HELPERS"], a, /[ \t]+/); for (i = 1; i <= k; i++) if (a[i] != "") helper[a[i]] = 1
            k = split(ENVIRON["FW_EXEMPT"], a, /[ \t]+/); for (i = 1; i <= k; i++) if (a[i] != "") ex[a[i]] = 1 }
    FNR == 1 { write_held_fn() }
    { ln = $0; gsub(/\r/, "", ln); c = ln; sub(/^[ \t]+/, "", c); at = FILENAME ":" FNR }
    c ~ /^#/ { next }
    ln ~ /^function[ \t]+[A-Za-z_][A-Za-z0-9_:-]*/ || ln ~ /^[A-Za-z_][A-Za-z0-9_:-]*[ \t]*\(\)[ \t]*\{/ {
      write_held_fn(); fn = ln; sub(/^function[ \t]+/, "", fn); sub(/[ \t(].*$/, "", fn); sub(/\{.*$/, "", fn)
      body = ln; sub(/^[^{]*\{/, "", body); scan(body, at)
      if (ln ~ /\}[ \t;]*$/) write_held_fn()
      next }
    ln ~ /^\}/ { write_held_fn(); next }
    { scan(c, at) }
    END { write_held_fn()
          for (e in ex) if (!(e in cand)) hits = hits "\nFEED_WRITER_EXEMPT_FNS names " e "(), which is no function holding a lease-carrying line without a feed call"
          for (h in helper) {
            if (!(h in seen)) hits = hits "\nFEED_WRITER_HELPER_FNS names " h "(), which is no function of the files read"
            else if (!(h in apnd) && !(h in calls)) hits = hits "\nFEED_WRITER_HELPER_FNS names " h "(), whose own body neither appends to the feed log nor calls another entry"
          }
          if (nl == 0) hits = hits "\nno line of the files read carries a lease-carrying write, so the census matched nothing and passes nothing"
          printf "%s", substr(hits lim2, 2) }' "$@")
  [ -n "$out" ] || return 0
  printf '%s\n' "$out"
  return 1
}
