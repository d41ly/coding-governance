#!/usr/bin/env bash
# Resolve a python launcher and exec a script with it — the shim a git MERGE DRIVER needs.
#
#   bash tools/lib/pyrun.sh <script.py> [args...]
#
# WHY A SHIM EXISTS AT ALL. `tools/lib/resolve-python.sh` is source-and-call: `resolve_python()`
# prints a launcher name and returns, it executes nothing. `tools/run-gates.sh` substitutes the
# resolved launcher into every manifest leg's argv, but GIT never goes through the runner — it execs
# a `merge.<driver>.driver` command line itself — so that substitution cannot reach a merge driver
# and this file is the only place the launcher gets resolved for one. Naming a launcher literally
# instead is the Microsoft-Store-stub failure the resolver exists for, and the invocation ban in
# `tools/lib/resolve-python.test.sh` refuses it repo-wide.
#
# It SOURCES the canonical resolver rather than carrying the inline copy block. That block's parity
# population is DERIVED by `git grep -l '^# >>> resolve_python' -- '*.sh'`, so carrying the marker
# here would enlist a file in a gate it has no reason to be in; `../lib/` is always reachable
# because this file IS in `tools/lib/`. A kit copy-installed as a standalone directory cannot source
# it and carries the inline block instead — that is the case the marker is for, and this is not it.
#
# The caller HALTS on the resolver's return value: `resolve_python` echoes and returns non-zero, it
# never exits, so the substitution has to be tested here. Exit 2, matching every other consumer.
#
# NO `cd`. Git invokes a merge driver with the cwd at the top of the working tree and hands it
# `%O %A %B` relative to that, so moving the cwd can only break paths that are already correct.
# (aMendedLedger U5)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=/dev/null
. "$HERE/resolve-python.sh"
PY=$(resolve_python) || exit 2
exec "$PY" "$@"
