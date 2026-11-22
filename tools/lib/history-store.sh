#!/usr/bin/env bash
# history-store.sh — the bash face of history_store.py beside it (TOOL-dQuietDisk-1 S8).
#
# The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so the block below travels
# INLINE, byte-identical, in the unattended kit's lib-unattended.sh, and
# `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts. The block finds the
# module beside the file that defines it, so each copy calls its own kit's history_store.py.
#
# USAGE — source it where resolve_python is defined, then:
#
#   init_hs <leg> <code path>... || exit 2   # the leg and its grading code; python resolved once
#   tip=$(read_hs_tip)                       # this worktree's last graded tip, or nothing
#   read_hs_items <file>                     # <item id>TAB<field>... -> <item id>TAB<hit|miss>TAB<body>
#   write_hs_items <file> [<tip>]            # <item id>TAB<field>...TAB<body>; then the tip, then the prune
#   init_bh [<repo>]                         # one `git cat-file --batch` coprocess, BH
#   read_bh_info <name>; read_bh_blob <name> # set BH_OID, BH_TYPE, BH_SIZE and BH_TEXT
#   remove_bh                                # close it
#
# Each hs call is one python process, whatever the item count. A body is escaped one way, `\\`, `\t`
# and `\n`, as the module defines. read_bh_info and read_bh_blob return 0 on an answer, 1 on `missing`
# or `ambiguous`, and 2 on a dead coprocess or a name holding a newline, which the caller grades as it
# does with no reader. read_bh_blob returns 3 where the bytes read differ from the header's size: bash
# drops a NUL, so a blob holding one reads short, and its bytes are counted under LC_ALL=C so the
# stream stays framed. WHAT THIS DOES NOT CHECK: a coprocess that hangs rather than dies.

# >>> history_store_sh — canonical copy: history-store.sh in gov's lib dir (byte-identical; gated)
init_hs() { # <leg> <code path>... -> 0 with HS_PY, HS_MODULE and HS_ARGS set; 2 with no python or no code path
  local _hs_p _hs_d
  [ "$#" -ge 2 ] || { echo "init_hs: a leg and at least one code path" >&2; return 2; }
  HS_ARGS=(--leg "$1"); shift
  for _hs_p in "$@"; do HS_ARGS+=(--code "$_hs_p"); done
  case ${BASH_SOURCE[0]} in */*) _hs_d=${BASH_SOURCE[0]%/*} ;; *) _hs_d=. ;; esac
  case $_hs_d in /*|[A-Za-z]:*) ;; *) _hs_d=$PWD/$_hs_d ;; esac
  HS_MODULE=$_hs_d/history_store.py
  HS_PY=$(resolve_python) || return 2
}
read_hs_tip() { # -> the leg's last graded tip in this worktree, or nothing
  "$HS_PY" "$HS_MODULE" "${HS_ARGS[@]}" tip
}
read_hs_items() { # <file> -> one <item id>TAB<hit|miss>TAB<body> line per line of the file
  "$HS_PY" "$HS_MODULE" "${HS_ARGS[@]}" lookup < "$1"
}
write_hs_items() { # <file> [<tip>] -> each line's item written, then the tip, then the daily prune
  if [ -n "${2:-}" ]; then
    "$HS_PY" "$HS_MODULE" "${HS_ARGS[@]}" store --tip "$2" < "$1"
  else
    "$HS_PY" "$HS_MODULE" "${HS_ARGS[@]}" store < "$1"
  fi
}
init_bh() { # [<repo>] -> 0 with the coprocess BH running; 2 where it did not start
  remove_bh
  coproc BH { exec git -C "${1:-.}" cat-file --batch 2>/dev/null; }
  [ -n "${BH_PID:-}" ] || return 2
}
read_bh_info() { # <name> -> 0 with BH_OID BH_TYPE BH_SIZE BH_TEXT set; 1 missing or ambiguous; 2 dead
  local LC_ALL=C _bh_line _bh_rest _bh_chunk _bh_left
  BH_OID="" BH_TYPE="" BH_SIZE="" BH_TEXT=""
  case $1 in *$'\n'*) return 2 ;; esac
  [ -n "${BH_PID:-}" ] && [ -n "${BH[1]:-}" ] && kill -0 "$BH_PID" 2>/dev/null || return 2
  printf '%s\n' "$1" >&"${BH[1]}" || return 2
  IFS= read -r _bh_line <&"${BH[0]}" || return 2
  case $_bh_line in *' missing'|*' ambiguous') return 1 ;; esac
  BH_OID=${_bh_line%% *}; _bh_rest=${_bh_line#* }; BH_TYPE=${_bh_rest%% *}; BH_SIZE=${_bh_rest#* }
  [[ $BH_OID =~ ^[0-9a-f]{40}([0-9a-f]{24})?$ && $BH_SIZE =~ ^[0-9]+$ ]] || return 2
  _bh_left=$BH_SIZE
  while [ "$_bh_left" -gt 0 ]; do
    IFS= read -r -d '' -n "$_bh_left" _bh_chunk <&"${BH[0]}" || return 2
    BH_TEXT+=$_bh_chunk
    if [ "${#_bh_chunk}" -lt "$_bh_left" ]; then _bh_left=$((_bh_left - ${#_bh_chunk} - 1)); else _bh_left=0; fi
  done
  IFS= read -r -d '' -n 1 _bh_chunk <&"${BH[0]}" || return 2
  [ "$_bh_chunk" = $'\n' ] || return 2
}
read_bh_blob() { # <name> -> read_bh_info's answer; 3 where BH_TEXT holds fewer bytes than BH_SIZE
  local LC_ALL=C
  read_bh_info "$1" || return
  [ "${#BH_TEXT}" -eq "$BH_SIZE" ] || return 3
}
remove_bh() { # -> the coprocess BH closed and reaped, if one runs
  local _bh_pid=${BH_PID:-}
  [ -n "$_bh_pid" ] || return 0
  [ -z "${BH[1]:-}" ] || exec {BH[1]}>&-
  wait "$_bh_pid" 2>/dev/null
  return 0
}
# <<< history_store_sh
