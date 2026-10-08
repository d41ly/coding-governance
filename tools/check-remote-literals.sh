#!/usr/bin/env bash
# check-remote-literals.sh — kit code names no remote by literal (TOOL-dLadderedRemote-3).
#
#   bash <prefix>/check-remote-literals.sh          # assert; exit 1 naming every <path>:<line>
#   bash <prefix>/check-remote-literals.sh --list   # print the population, then every hit; exits as the assert
#
# WHY. Which remote "landed" is measured on is a per-node variance: adopter ic's node `d` names its
# remote after the project. The lander resolved it by a ladder since TOOL-aRepatriatedFork-8 S1 while
# every probe beside it spelled `origin`, so on that node drift-audit refused, the codebase-map
# baseline assert went UNGRADED and every scoped bar ran in full. The ladder is now one canonical per
# language in the gov lib dir, inlined at every site (TOOL-dLadderedRemote-1, -2); this gate is what
# stops the next probe from spelling the name again. Exit 0 clean, 1 on any hit, 2 when it cannot run.
#
# A PURE BAN, with no waiver registry and no line marker, after the install-prefix gate's precedent:
# a fixture that needs a remote names it through a variable, and a test file is outside the population.
#
# THE POPULATION is every tracked `*.sh`, `*.py` and `*.js` under this gate's own tool root and under
# `skills/`, and every tracked file under `.githooks/` — LESS `*.test.sh`, any path carrying
# `selftest`, `test_*.py`, anything under a `fixtures/` directory, and Markdown. A fixture that
# creates the remote on purpose is not a defect. Each LINE whose first non-blank text is `#`, `//`,
# `/*` or `*` is a comment and is skipped: a comment recording what a site used to read is history.
#
# THE PREDICATE, four shapes, each written once below and each built through `$N` so this file does
# not spell what it bans:
#   1. a tracking ref — `refs/remotes/` then the name, then anything but a name character;
#   2. a short ref — the name then `/HEAD`, `/main`, `/master`, or an interpolation `/$` or `/{`;
#   3. a default — the name quoted after `or`, `||` or `:-`, as in `remote = x or "<name>"`;
#   4. a remedy — `set-head`, `fetch`, `get-url`, `ls-remote` or `set-url` then the name.
#
# WHAT THIS GATE DOES NOT CHECK, said out loud because a structural ban reads as a semantic one:
#   * a remote name held in a VARIABLE and joined at run time, which spells nothing;
#   * a bare QUOTED name passed as a git argument, which cannot be told from a dictionary key of the
#     same spelling — `govkit.py` uses that word as a field name;
#   * a Python docstring or a message string QUOTING an old spelling is a hit, not a skip: only `#`,
#     `//`, `/*` and `*` lines are comments to this gate, so reword the string;
#   * any file type outside the population, and every untracked file — stage before you run it.
set -u
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir=""
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "remote-literals: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

# THIS GATE'S TOOL ROOT, DERIVED from where it sits, and an underivable one REFUSES: a literal here
# would be the install-prefix gate's class, and a root install derives the empty string.
if ! SELF_PRE=$(git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null); then
  echo "remote-literals: cannot derive this gate's own directory from '$_self_dir' — REFUSING"
  exit 2
fi
TROOT=${SELF_PRE%/}

MODE="${1:---check}"
case "$MODE" in --check|--list) ;; *) echo "usage: $(basename "$0") [--check|--list]"; exit 2 ;; esac

if [ -n "$TROOT" ]; then
  INCLUDE=("$TROOT/*.sh" "$TROOT/*.py" "$TROOT/*.js" "skills/*.sh" "skills/*.py" ".githooks/*")
else
  INCLUDE=("*.sh" "*.py" "*.js" ".githooks/*")
fi
EXCLUDE=(":(exclude)*.test.sh" ":(exclude)*selftest*" ":(exclude)*test_*.py" ":(exclude)*/fixtures/*" ":(exclude)*.md")

pop=$(git ls-files -- "${INCLUDE[@]}" "${EXCLUDE[@]}")
npop=$(printf '%s' "$pop" | grep -c . || true)
if [ "$npop" -eq 0 ]; then
  echo "remote-literals: DEAD PROBE — the population is empty, which is a broken derivation, not a clean tree"
  exit 2
fi

N=origin
Q="[\"'\`]"
PATTERNS=(
  "refs/remotes/$N([^A-Za-z0-9_.-]|\$)"
  "(^|[^A-Za-z0-9_./-])$N/(HEAD|main|master|[\${])"
  "(^|[^A-Za-z0-9_])or[[:space:]]+$Q$N$Q"
  "(\\|\\||:-)[[:space:]]*$Q?$N([^A-Za-z0-9_-]|\$)"
  "(set-head|fetch|get-url|ls-remote|set-url)[[:space:]]+$N([^A-Za-z0-9_-]|\$)"
)
args=()
for p in "${PATTERNS[@]}"; do args+=(-e "$p"); done

# `git grep` prints <path>:<line>:<text>; the awk drops a comment line and keeps the rest verbatim.
hits=$(git grep -n -I -E "${args[@]}" -- "${INCLUDE[@]}" "${EXCLUDE[@]}" 2>/dev/null \
       | awk '{ t = $0; sub(/^[^:]*:[0-9]+:/, "", t); sub(/^[ \t]+/, "", t)
               if (t ~ /^(#|\/\/|\/\*|\*)/) next; print }' || true)

if [ "$MODE" = --list ]; then
  printf '%s\n' "$pop" | sed 's/^/population  /'
fi
if [ -n "$hits" ]; then
  printf '%s\n' "$hits"
  echo "remote-literals: FAILED — $(printf '%s\n' "$hits" | grep -c .) line(s) in $npop file(s) name a remote by literal. Resolve it through the remote ladder (resolve_remote / resolve_remote_sh in the gov lib dir, inlined), never by name."
  exit 1
fi
echo "remote-literals: clean — $npop file(s), no remote named by literal"
exit 0
