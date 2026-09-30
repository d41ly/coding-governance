#!/usr/bin/env bash
# foreign-prefix.gov.test.sh — every declared self-test, run with gov's tool root moved to a FOREIGN
# prefix, must reach parity with its own run at gov's prefix. TOOL-aRepatriatedFork-30 S1: the held
# leg TOOL-aRepatriatedFork-18 §7 specified and parked.
#
#   bash <prefix>/run-gates/foreign-prefix.gov.test.sh [--kit <substring>]
#
# WHY. Units 23 to 29 drained every kit path gov spelled as a literal, and the install-prefix ban
# grades the SPELLING. Whether a suite still RUNS once its tool root sits somewhere else is a
# different question, and only running it there answers it: a fixture that builds its layout from a
# literal prefix passes every text check and fails at the first prefix it was not written for.
#
# HOW, and every step is an existing seam rather than a comparison of this file's own.
#   1. A scratch clone of this repository at HEAD, under `mktemp -d`, deleted on exit.
#   2. The POPULATION is the declared one, `selftest-budgets.txt` beside this file, withheld suites
#      included (TOOL-aRepatriatedFork-30 §8 F3 (b)), less this leg's own row: a leg that ran itself
#      would recurse. Its row leaves the clone's budget file and manifest together, so the clone's
#      declaration still agrees with itself in both directions.
#   3. `run-selftests.sh --pooled --calibrate` at gov's prefix writes each row's reading — exit
#      status, `FAIL` count, executed count — into the clone's pooled evidence.
#   4. The WHOLE tool root moves with `git mv` to each prefix of §8 F1 (b) — `scripts/`,
#      `vendor/gov/` and the repo root — and `run-selftests.sh --pooled` grades each move. That mode's
#      verdict IS parity against the calibration, and a `MISMATCH`, a timeout or a refusal reds this
#      leg, named with the prefix it happened at.
#
# ROWS WITH NO TRAILER. `--pooled` witnesses a completion only through a trailer line, and a
# calibrate that meets a row without one writes no reading, after which every `--pooled` refuses the
# whole run. So before calibrating, the clone's evidence declares every kit directory a pooled kit
# and `run-selftests.sh --check` runs its static trailer arm over them; each row that arm names is
# declared `no-trailer` in the clone, so its reading is exit status plus `FAIL` count and the gap is
# printed on its row instead of refusing the rest.
#
# WHAT THIS DOES NOT CHECK:
#   * an executed count for a suite whose trailer does not carry one in `--pooled`'s own shape: that
#     suite is compared on exit status and `FAIL` count, with its completion witnessed by its trailer,
#     so an arm it skips without printing a FAIL line is invisible here;
#   * a literal prefix used only INSIDE a suite's own scratch fixture. A fixture laid out at a literal
#     prefix and read only at that prefix is self-consistent, so it passes at every host prefix —
#     measured on this leg's red control. What reds here is a suite reading the HOST tree through a
#     literal; the spelling inside a fixture is the install-prefix ban's to grade;
#   * gov's wiring OUTSIDE the tool root — `.claude/`, the hooks path, the charter — which does not
#     move, so a suite reading it sees gov's own spelling at every prefix;
#   * an ADOPTER's tree. This moves GOV, it installs into nobody's repository: `govkit apply` has its
#     own suites, and an apply target lacks the records and withheld suites this leg compares.
# COST: hours. One calibrate and three pooled runs of the whole population, held, run once per build.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "foreign-prefix: not inside a git work tree"; exit 2; }
# The tool root and this kit's directory name, DERIVED. Moving the tool root is the whole leg, so
# a literal here would be the one path it could never move.
if ! TROOT=$(git -C "$HERE/.." rev-parse --show-prefix 2>/dev/null); then
  echo "foreign-prefix: cannot derive the tool root above $HERE — REFUSING"; exit 2
fi
TROOT=${TROOT%/}
KIT=$(basename "$HERE")
if [ -z "$TROOT" ]; then
  echo "foreign-prefix: gov sits at the repo root here, so there is no tool root to move — REFUSING"
  echo "foreign-prefix: rather than grading a relocation that cannot be performed."
  exit 2
fi
# The python-launcher resolver, INLINED byte-identically from the canonical copy named on its
# marker line: a bare launcher name is not an answer on a host with the Store stub.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
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
SELF_ROW="foreign-prefix parity (every self-test at three prefixes)"
FLOOR_ASSERTIONS=4
FILTER=""
while [ $# -gt 0 ]; do
  case "$1" in
    --kit) FILTER=${2:-}; [ -n "$FILTER" ] || { echo "foreign-prefix: --kit takes a substring"; exit 2; }; shift 2 ;;
    *) echo "usage: bash $0 [--kit <substring>]"; exit 2 ;;
  esac
done

fails=0; passed=0
print_fail() { fails=$((fails+1)); printf 'FAIL  %s\n' "$*"; }
print_pass() { passed=$((passed+1)); printf 'ok    %s\n' "$*"; }

TMPD=$(mktemp -d) || { echo "foreign-prefix: mktemp failed"; exit 2; }
[ "${GOV_FOREIGN_KEEP:-0}" = 1 ] || trap 'rm -rf "$TMPD"' EXIT
G="$TMPD/g"
git clone -q --no-hardlinks "$ROOT" "$G" || { echo "foreign-prefix: could not clone $ROOT"; exit 2; }
cd "$G" || exit 2
git config user.email foreign-prefix@gov.test; git config user.name foreign-prefix
echo "foreign-prefix: clone of $(git rev-parse --short HEAD) at $G, tool root '$TROOT'${FILTER:+, rows matching '$FILTER'}"

remove_own_row() {
  # Both declarations at once: the budget row and the manifest leg. Bytes in, bytes out, so an LF
  # file stays LF.
  local py
  py=$(resolve_python) || return 1
  "$py" - "$TROOT/$KIT/selftest-budgets.txt" "$TROOT/gate-legs.json" "$SELF_ROW" <<'PY'
import json, sys
budgets, legs, row = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(budgets, "rb").read().split(b"\n")
open(budgets, "wb").write(b"\n".join(l for l in b if not l.startswith(row.encode() + b"\t")))
raw = open(legs, "rb").read().decode("utf-8")
doc = json.loads(raw)
kept = [l for l in doc if l.get("name") != row]
if len(kept) != len(doc):
    open(legs, "wb").write((json.dumps(kept, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
PY
}

add_trailerless_rows() {
  # --check's static trailer arm, scoped to every directory a row's argv can lie under, names each row
  # that prints no trailer outside a guard. Each is declared trailer-less in the CLONE only.
  local ev="$TROOT/$KIT/selftest-pooled-evidence.txt" names
  printf '# pooled-kit: {prefix}\n# pooled-kit: .githooks\n# pooled-kit: skills\n' >> "$ev"
  names=$(bash "$TROOT/$KIT/run-selftests.sh" --check 2>&1 | sed -n "s/^  row '\(.*\)'[: ].*/\1/p" | sort -u)
  [ -z "$names" ] || printf '%s\n' "$names" | sed 's/^/# no-trailer: /' >> "$ev"
  printf '%s\n' "$names" | grep -c . || true
}

set_tool_root() { # $1 = the new prefix, empty for the repo root
  local to="$1" c
  case "$to" in
    "") for c in $(git ls-tree --name-only HEAD "$TROOT/" | sed "s|^$TROOT/||"); do
          [ -e "$c" ] && { echo "foreign-prefix: '$c' already exists at the repo root, so the root move would collide"; return 1; }
          git mv "$TROOT/$c" "$c" || return 1
        done ;;
    *) mkdir -p "$(dirname "$to")"; git mv "$TROOT" "$to" || return 1 ;;
  esac
  git commit -q -m "foreign-prefix: tool root at ${to:-the repo root}"
}

run_at_prefix() { # $1 = prefix, empty for the repo root
  local p="$1" out rc
  git reset -q --hard "$BASE" && git clean -qfdx
  if ! set_tool_root "$p"; then print_fail "could not move the tool root to ${p:-the repo root}"; return; fi
  out=$(bash "${p:+$p/}$KIT/run-selftests.sh" --pooled ${FILTER:+--kit "$FILTER"} 2>&1); rc=$?
  printf '%s\n' "$out" | sed "s|^|[${p:-root}] |"
  if [ "$rc" = 0 ]; then
    print_pass "every selected row reached parity with gov's prefix at ${p:-the repo root}"
  else
    print_fail "at ${p:-the repo root} (exit $rc): $(printf '%s\n' "$out" | grep -E '^(MISMATCH|TIMEOUT|WALL|UNTRAILED)' | sed -E 's/ {2,}[0-9]+s .*$//' | tr '\n' ';')"
  fi
}

remove_own_row || { echo "foreign-prefix: could not remove this leg's own row from the clone"; exit 2; }
echo "foreign-prefix: $(add_trailerless_rows) row(s) declared trailer-less in the clone"
git add -A && git commit -q -m "foreign-prefix: population and trailer declarations" || true
cal=$(bash "$TROOT/$KIT/run-selftests.sh" --pooled --calibrate ${FILTER:+--kit "$FILTER"} 2>&1); crc=$?
printf '%s\n' "$cal" | sed "s|^|[$TROOT, calibrate] |"
if [ "$crc" = 0 ]; then
  print_pass "the calibrate at gov's prefix read every selected row"
else
  print_fail "the calibrate at gov's prefix red (exit $crc), so no prefix can be graded against it"
  echo "FAIL — $fails check(s) failed"; exit 1
fi
git add -A && git commit -q -m "foreign-prefix: calibrated at $TROOT" || true
BASE=$(git rev-parse HEAD)
for P in scripts vendor/gov ""; do
  if [ "$P" = "$TROOT" ]; then echo "foreign-prefix: skip ${P} — it is gov's own prefix, which the calibrate already read"; continue; fi
  run_at_prefix "$P"
done
[ "$fails" = 0 ] && [ "$passed" -lt "$FLOOR_ASSERTIONS" ] && print_fail "only $passed of the $FLOOR_ASSERTIONS verdicts ran (floor FLOOR_ASSERTIONS)"
[ "$fails" = 0 ] && echo "PASS ($passed assertions)"
[ "$fails" = 0 ] || { echo "FAIL — $fails check(s) failed"; exit 1; }
