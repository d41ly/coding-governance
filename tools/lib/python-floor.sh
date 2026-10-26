#!/usr/bin/env bash
# python-floor.sh — the shell half of the interpreter floor's upgrade step, `lib/python-floor-<X.Y>`
# (TOOL-dSafePassage-11). The floor is declared once, in python-floor.txt beside this file.
#
#   bash <prefix>/lib/python-floor.sh preflight              # the step's up and its witness
#   bash <prefix>/lib/python-floor.sh down <prior> <target>  # the step's down
#
# `preflight` sources the one resolver and calls it, so it refuses exactly as every gate and hook
# does: at the floor it prints the interpreter and its version and exits 0; below it, it exits 1 with
# the resolver's own refusal, byte for byte, and adds nothing. It compares no version itself.
#
# `down` runs python_floor.py's down under the resolved interpreter: every tracked .py and .toml file
# of <target> graded under the floor <prior> restores, a finding exiting 1 and writing nothing; with
# none, the declaration and every copy's literal line restored where the target carries the
# declaration, which only gov's own source tree does.
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
  down:3)
    PY=$(resolve_python) || exit 1
    exec "$PY" -I "$HERE/python_floor.py" down "$2" "$3"
    ;;
  *) echo "usage: bash <prefix>/lib/python-floor.sh preflight | down <prior> <target>" >&2; exit 2 ;;
esac
