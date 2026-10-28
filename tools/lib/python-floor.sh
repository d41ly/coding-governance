#!/usr/bin/env bash
# python-floor.sh — the shell half of the interpreter floor's upgrade step, `lib/python-floor-<X.Y>`
# (TOOL-dSafePassage-11). The floor is declared once, in python-floor.txt beside this file.
#
#   bash <prefix>/lib/python-floor.sh preflight              # the step's up and its witness
#   bash <prefix>/lib/python-floor.sh down <prior> <target> [<to>, required outside gov]  # the step's down, <to> gov's HEAD by default on gov's own tree
#   bash <prefix>/lib/python-floor.sh floor                  # the declared floor, checked
#
# `preflight` sources the one resolver and calls it, so it refuses exactly as every gate and hook
# does: at the floor it prints the interpreter and its version and exits 0; below it, it exits 1 with
# the resolver's own refusal, byte for byte, and adds nothing. It compares no version itself.
#
# `down` runs python_floor.py's down under the resolved interpreter: the files the rollback to the
# commit <to> restores, read at <to>, graded under the floor <prior> restores (TOOL-dSafePassage-26
# S10, S11), a finding exiting 1 and writing nothing; with none, the declaration and every copy's
# literal line restored where the target carries the declaration, which only gov's own tree does.
#
# `floor` is the one shell reader of python-floor.txt (TOOL-dSafePassage-26 S53): read_floor's rule,
# exactly <major>.<minor> and one optional LF, applied with no Python; it prints the value, or exits 1
# naming the file.
#
#   Exit 0 at the floor or restored · 1 below the floor, or a down finding · 2 wrong invocation.
set -u
case "$0" in */*) HERE=${0%/*} ;; *) HERE=. ;; esac
# shellcheck source=/dev/null
. "$HERE/resolve-python.sh"
case "${1:-}:$#" in
  preflight:1)
    PY=$(resolve_python) || exit 1
    VER=$("$PY" -I -c 'import sys; print("%d.%d.%d" % sys.version_info[:3])') || exit 1
    printf 'python-floor: %s runs Python %s, at the floor %s declares\n' "$PY" "${VER%$'\r'}" "$HERE/python-floor.txt"
    ;;
  down:3|down:4)
    PY=$(resolve_python) || exit 1
    exec "$PY" -I "$HERE/python_floor.py" down "${@:2}"
    ;;
  floor:1)
    # Read whole, so a second line is seen; one trailing LF is the file's own and is dropped.
    v=$(cat "$HERE/python-floor.txt" 2>/dev/null; printf x) || v=x
    v=${v%x}; v=${v%$'\n'}; v=${v%$'\r'}  # a CRLF checkout's line end, as read_floor reads it
    if [[ $v =~ ^[0-9]+\.[0-9]+$ ]]; then printf '%s\n' "$v"; else
      printf 'python-floor: %s must be one <major>.<minor> line, and it reads %q\n' "$HERE/python-floor.txt" "$v" >&2; exit 1
    fi
    ;;
  *) echo "usage: bash <prefix>/lib/python-floor.sh preflight | down <prior> <target> [<to>, required outside gov] | floor" >&2; exit 2 ;;
esac
