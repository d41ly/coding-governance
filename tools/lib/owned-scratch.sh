#!/usr/bin/env bash
# owned-scratch.sh — the bash face of an owned, swept scratch root (TOOL-dQuietDisk-9 S4).
#
# The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so the block below travels
# INLINE, byte-identical, in the run-gates kit's two runners, and `<prefix>/lib/resolve-python.test.sh`'s
# parity table reds a copy that drifts. The owner line and the Python face are stated once, in
# `owned_scratch.py`'s module docstring beside this file.
#
# USAGE — define `derive_temp_path`, `ts_alive` and `add_health_event` as the runner does (the
# `health_log_sh` block and the runner's two one-line helpers), source this, then:
#
#   write_work_owner "$dir" "$common" || echo "no owner record" >&2
#   scan_dead_work "$ambient" "$dir" "$common" "$health_log"
#
# The block defines none of the three helpers, so the owner write keeps the caller's unpredictable
# staging name. WHAT IT DOES NOT CHECK: a `py:` owner, whose native pid `kill -0` cannot judge from an
# MSYS shell and which the Python face sweeps; a relative common dir; and a pid reused since its owner died.

# >>> owned_work_sh — canonical copy: owned-scratch.sh in gov's lib dir (byte-identical; gated)
write_work_owner() { # <dir> <common> -> <dir>/owner, one line: pid TAB common dir TAB start epoch; rc 1 when unwritten
  local _tp
  derive_temp_path _tp "$1/owner"
  printf '%s\t%s\t%s\n' "$$" "$2" "$EPOCHSECONDS" > "$_tp" 2>/dev/null \
    && mv -f "$_tp" "$1/owner" 2>/dev/null
}

scan_dead_work() { # <ambient> <own dir> <common> <health log> -> removes each gate-work dir under <ambient> a dead bar owns
  local d own pid rest common f
  local -a doomed
  # No common dir, no proof of ownership: sweep nothing rather than match an empty field.
  [ -n "$3" ] || return 0
  for d in "$1"/gate-work.*; do
    [ -d "$d" ] || continue
    # NEVER OUR OWN, guarded explicitly although our live pid already withholds it — the same belt
    # `ts_sweep_queue` wears, for the same reason: a later edit to the pid test must not reach here.
    [ "${d##*/}" = "${2##*/}" ] && continue
    own=""
    { IFS= read -r own < "$d/owner"; } 2>/dev/null
    own=${own%$'\r'}
    [ -n "$own" ] || continue
    pid=${own%%$'\t'*}; rest=${own#*$'\t'}; common=${rest%%$'\t'*}
    case "$pid" in ''|*[!0-9]*) continue ;; esac
    # THIS REPOSITORY'S, or an ORPHAN's: an absolute common dir that names no directory any more, a
    # fixture repository its suite removed (TOOL-dQuietDisk-9 S9). Another live repository's root and
    # a relative common dir are never touched.
    if [ "$common" != "$3" ]; then
      case "$common" in /*|[A-Za-z]:[/\\]*) ;; *) continue ;; esac
      [ -d "$common" ] && continue
    fi
    ts_alive "$pid" && continue
    printf 'run-gates: sweeping the scratch of a dead bar (pid %s)\n' "$pid" >&2
    doomed=()
    for f in "$d"/* "$d"/.[!.]*; do
      [ -e "$f" ] || [ -L "$f" ] || continue
      [ "${f##*/}" = owner ] && continue
      doomed+=("$f")
    done
    if { [ "${#doomed[@]}" = 0 ] || rm -rf "${doomed[@]}" 2>/dev/null; } && rm -rf "$d" 2>/dev/null; then
      add_health_event "$4" run-gates scratch-swept "dead bar pid $pid"
    else
      printf 'run-gates: NOTE - the scratch of dead bar %s was not removed whole; its owner record stays, so the next bar retries: %s\n' "$pid" "$d" >&2
    fi
  done
  return 0
}
# <<< owned_work_sh
