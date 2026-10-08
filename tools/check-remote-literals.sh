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
# `skills/`, and every tracked file under `.githooks/` — LESS `*.test.sh`, a `*selftest*.py`, a
# `test_*.py` by basename, anything under a `fixtures/` directory, and Markdown. A fixture that
# creates the remote on purpose is not a defect, and the exclusions match test files by their NAME so
# product code such as a self-test RUNNER stays graded (TOOL-dLadderedRemote-5). A LINE whose first
# non-blank text is `#` is a comment and is skipped, and so is one led by `//`, `/*` or `*` in a
# `*.js` file only: in shell a `*)` line is a `case` arm, which is code.
#
# THE PREDICATE, five shapes, each written once below and each built through `$N` so this file does
# not spell what it bans:
#   1. a tracking ref — `refs/remotes/` then the name, then anything but a name character;
#   2. a short ref or prefix — the name then `/`, led by anything but a name character, `.`, `/` or
#      `$`, so `${x#<name>/}` and `removeprefix("<name>/")` count and a variable `$<name>/x` does not;
#   3. a default — the name QUOTED after `or`, `||` or `??`; the name after a parameter expansion's
#      `-`, `:-`, `=` or `:=`, the parameter being a name, a digit or a special parameter with an
#      optional `[...]` subscript and an optional `!` (`${1:-<name>}`, `${opts[r]:-<name>}` and
#      `${!ref:-<name>}` included); the name quoted as a call's last argument after a comma, as in
#      `.get(k, "<name>")`; or as the last element of a list opened right after `(` or `,`, as in
#      `run(["git", "remote", "show", "<name>"], check=True)` — a list assigned to a name is not;
#   4. an assignment — a variable set to the QUOTED name in any file, or to the bare name in a shell
#      file only, as in `REMOTE=<name>`: in Python or JS the bare form reads a variable;
#   5. a remedy — `set-head`, `fetch`, `get-url`, `ls-remote`, `set-url`, `push` or `pull`, any
#      dash-led flags, then the name; the same verb QUOTED in an argv list followed by quoted flags and the
#      quoted name, as in `["git", "fetch", "<name>"]`; or `remote.<name>.` as a config key.
#
# WHAT THIS GATE DOES NOT CHECK, said out loud because a structural ban reads as a semantic one:
#   * a remote name held in a VARIABLE and joined at run time, which spells nothing;
#   * a bare QUOTED name passed as a git argument anywhere but last and outside the argv shape above,
#     or last in a list assigned to a name, which cannot be told from a dictionary key or a key list
#     of the same spelling — `govkit.py` uses that word as a field name;
#   * a PATH HOLDING A COLON: the filter splits a hit on its first colon, so a comment line there is
#     not skipped and reads as a hit, a false RED; only a path holding `:<digits>:` followed by a
#     comment leader can hide a real hit.
#
# WHAT IT REDS THAT IS NOT A REMOTE: a key list or tuple whose last element is the name, passed
# straight into a call (`w.writerow(["kit", "<name>"])`, `itemgetter("kit", "<name>")`). Hoist the
# list into a named constant, which no shape reads as a call argument.
#   * a call or an argv list WRAPPED across lines: every shape reads one line;
#   * a flag's SEPARATE value between a remedy verb and the name, as in `fetch --depth 1 <name>`:
#     the flag group admits dash-led words only;
#   * a revision range such as `<name>..HEAD`, and a comparison such as `== "<name>"`;
#   * a Python docstring or a message string QUOTING an old spelling is a hit, not a skip: only the
#     comment leaders above are skipped, so reword the string;
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
  INCLUDE=("$TROOT/*.sh" "$TROOT/*.py" "$TROOT/*.js" "skills/*.sh" "skills/*.py" "skills/*.js" ".githooks/*")
else
  INCLUDE=("*.sh" "*.py" "*.js" ".githooks/*")
fi
EXCLUDE=(":(exclude)*.test.sh" ":(exclude,glob)**/*selftest*.py" ":(exclude,glob)**/test_*.py"
         ":(exclude,glob)**/fixtures/**" ":(exclude)*.md")

pop=$(git ls-files -- "${INCLUDE[@]}" "${EXCLUDE[@]}")
npop=$(printf '%s' "$pop" | grep -c . || true)
if [ "$npop" -eq 0 ]; then
  echo "remote-literals: DEAD PROBE — the population is empty, which is a broken derivation, not a clean tree"
  exit 2
fi

N="ori""gin"   # assembled, so this file does not spell what it bans
Q="[\"'\`]"
END="([^A-Za-z0-9_-]|\$)"
VERB="(set-head|fetch|get-url|ls-remote|set-url|push|pull)"
PATTERNS=(
  "refs/remotes/$N([^A-Za-z0-9_.-]|\$)"
  "(^|[^A-Za-z0-9_./\$-])$N/"
  "(^|[^A-Za-z0-9_])or[[:space:]]+$Q$N$Q"
  "(\\|\\||\\?\\?)[[:space:]]*$Q$N$Q"
  "\\$\\{!?([A-Za-z_][A-Za-z0-9_]*|[0-9]+|[@*#?!\$-])(\\[[^]]*\\])?:?[-=]$Q?$N$END"
  "(\\(|,)[[:space:]]*\\[[^]]*,[[:space:]]*$Q$N$Q[[:space:]]*\\]"
  ",[[:space:]]*$Q$N$Q[[:space:]]*\\)"
  "(^|[^A-Za-z0-9_])[A-Za-z_][A-Za-z0-9_]*[[:space:]]*=[[:space:]]*$Q$N$Q"
  "$VERB([[:space:]]+-[^[:space:]]+)*[[:space:]]+$N$END"
  "$Q$VERB$Q([[:space:]]*,[[:space:]]*$Q-[^\"'\`]*$Q)*[[:space:]]*,[[:space:]]*$Q$N$Q"
  "remote\\.$N\\."
)
# THE UNQUOTED ASSIGNMENT is a literal only in shell, where `REMOTE=<name>` is a string; in Python or
# JS the same bytes read a VARIABLE, so this shape runs over the shell population alone.
SH_PATTERNS=(
  "(^|[^A-Za-z0-9_])[A-Za-z_][A-Za-z0-9_]*=$N([[:space:];]|\$)"
)
if [ -n "$TROOT" ]; then SH_INCLUDE=("$TROOT/*.sh" "skills/*.sh" ".githooks/*")
else SH_INCLUDE=("*.sh" ".githooks/*"); fi
args=()
for p in "${PATTERNS[@]}"; do args+=(-e "$p"); done
sh_args=()
for p in "${SH_PATTERNS[@]}"; do sh_args+=(-e "$p"); done

# `git grep` prints <path>:<line>:<text>; the awk drops a comment line and keeps the rest verbatim.
# The shell-only pass appends to the general one, and both go through the one comment filter. The
# merge dedupes on the WHOLE line, so two distinct hits are never collapsed into one.
hits=$({ git grep -n -I -E "${args[@]}" -- "${INCLUDE[@]}" "${EXCLUDE[@]}" 2>/dev/null
         git grep -n -I -E "${sh_args[@]}" -- "${SH_INCLUDE[@]}" "${EXCLUDE[@]}" ":(exclude)*.py" ":(exclude)*.js" 2>/dev/null; } \
       | awk '!seen[$0]++' \
       | awk '{ t = $0; sub(/^[^:]*:[0-9]+:/, "", t); sub(/^[ \t]+/, "", t)
               p = $0; sub(/:.*/, "", p)
               if (t ~ /^#/) next
               if (p ~ /\.js$/ && t ~ /^(\/\/|\/\*|\*)/) next
               print }' || true)

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
