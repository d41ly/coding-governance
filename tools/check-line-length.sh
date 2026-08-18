#!/usr/bin/env bash
# check-line-length.sh — a declared maximum line length for agent-instruction prose.
#
#   bash tools/check-line-length.sh                    # every declared subject
#   bash tools/check-line-length.sh <file>             # one subject
#   LINE_MAX=200 bash tools/check-line-length.sh <file>
#
# WHY. A rule that runs past a screen is a rule nobody re-reads and a diff nobody can review. The
# default is 450 characters, which is generous: it catches the paragraph-as-a-line class without
# forcing prose into a shape.
#
# RESOLUTION, in order: a positional $2, then the DECLARATION, then the environment, then the hard
# default. The declaration outranks the environment deliberately — a declared per-subject pin is
# policy, and an environment variable is a local override for a subject nobody declared. Without
# that ordering one exported variable silently lifts every declared subject at once. This is the
# same ordering `tools/check-template-size.sh` records at length, and for the same reason.
#
# CHARACTERS, NOT BYTES. These files carry non-ASCII glyphs, so a byte count would grade a line with
# six em dashes as eighteen characters longer than it reads. Measured over this corpus the two differ
# by roughly one per cent, which is enough to move an offender count. `awk` in the C locale counts
# BYTES, so the measurement tool is chosen rather than assumed.
#
# WHAT IS EXEMPT, said here so a green run is not misread. A FENCED code block holds a command whose
# length its author does not choose, and wrapping one changes what it means. Markdown TABLES are NOT
# exempt: a table row is prose in a grid and can be split. Nothing protects a long line inside a
# fence, and if a definition list ever grows one this gate will not see it.
#
# THE FENCE PARSER IS THIS FILE'S SIXTH COPY IN THIS TREE, and that is deliberate rather than
# careless. The hygiene gate's is a private shell function nothing exports; that script already
# carries four more inline copies; and this gate sits outside the memory-tree kit, so sourcing it
# would be the cross-kit edge this repo forbids. The precedent that keeps such copies honest is one
# shared case table with agreement proven across implementations.
#
# NOT ADOPTED IS EXIT 0, and only when the declaration is ABSENT and no subject was named. This gate
# is opt-in — the declaration is deliberately withheld from the kit payload, because gov's rows name
# gov's paths and a row naming an absent path is a stale red — so an adopter installs it with no
# declaration at all, and an install-day exit 2 is the very failure that withholding was meant to
# prevent. It is the `tools/lexicon/lexicon.py` posture and it is announced rather than silent. The
# vacuity it would otherwise open is closed elsewhere: gov's own declaration is a govkit `[[exempt]]`
# row, and selfcheck reds on an exemption whose path is gone, so deleting it here cannot go quiet.
# A declaration that EXISTS and selects nothing is still exit 2 — that is an authoring error, not an
# unadopted gate, and it is the anti-vacuity arm.
#
# Exit 0 = every subject within its limit, or not adopted · 1 = an offender or a stale row · 2 = could not run.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "check-line-length: not a git tree"; exit 2; }
cd "$ROOT" || exit 2

DECL=${DECL:-tools/line-length-limits.txt}
HARD_DEFAULT=450
status=0
fail() { printf 'LINE-LENGTH check %s FAILED — %s\n' "$1" "$2"; status=1; }

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
PY_BIN=$(resolve_python "${LINELEN_PY:-}") || exit 2

# The offender scanner. One python invocation, because the fence machine has to be a real parser and
# `awk` in the C locale counts BYTES rather than characters.
SCAN=$(mktemp); trap 'rm -f "$SCAN"' EXIT
cat > "$SCAN" <<'PYSCAN'
import sys
path, limit = sys.argv[1], int(sys.argv[2])
fence = None
for n, raw in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
    line = raw.rstrip()
    stripped = line.lstrip()
    if fence is None:
        if stripped.startswith('```') or stripped.startswith('~~~'):
            fence = stripped[:3]
            continue
    else:
        if stripped.startswith(fence):
            fence = None
        continue
    if len(line) > limit:
        print(f'{n}:{len(line)}')
PYSCAN

count_over() { "$PY_BIN" "$SCAN" "$1" "$2"; }

subjects=""
if [ "$#" -gt 0 ]; then
  subjects=$1
  POSITIONAL_LIMIT=${2:-}
else
  if [ ! -f "$DECL" ]; then
    echo "check-line-length: NOT ADOPTED — no declaration at $DECL and no subject given, so this"
    echo "check-line-length: tree has named nothing to grade. Write one TAB-separated <path> <chars>"
    echo "check-line-length: row in that file to adopt the gate, and this leg starts measuring."
    echo "check-line-length: A subject with no row of its own is graded at the $HARD_DEFAULT default."
    exit 0
  fi
  subjects=$(grep -vE '^[[:space:]]*(#|$)' "$DECL" | awk -F'\t' '{print $1}')
  POSITIONAL_LIMIT=
fi

[ -n "$subjects" ] || { echo "check-line-length: the declaration selects no subject, so this gate would grade nothing"; exit 2; }

for f in $subjects; do
  declared=""
  if [ -f "$DECL" ]; then
    declared=$(awk -F'\t' -v k="$f" '$1 == k { print $2 }' "$DECL" | tr -d '[:space:]')
  fi
  if [ -n "$declared" ] && ! printf '%s' "$declared" | grep -qE '^[0-9]+$'; then
    fail 1 "the declared line limit for this subject is not a number, so the comparison below would be against text: '$declared' for $f in $DECL"
    continue
  fi
  if [ ! -f "$f" ]; then
    # A row naming an absent path is STALE, and a stale row silently narrows the population it was
    # written to cover — the same class as a waiver whose subject is gone.
    fail 2 "the declaration names a subject that does not exist, so its row excuses nothing and is stale: $f in $DECL"
    continue
  fi
  limit=${POSITIONAL_LIMIT:-${declared:-${LINE_MAX:-$HARD_DEFAULT}}}
  src="the declaration"
  [ -n "$POSITIONAL_LIMIT" ] && src="a positional"
  if [ -z "$POSITIONAL_LIMIT" ] && [ -z "$declared" ]; then
    src="the environment"; [ -z "${LINE_MAX:-}" ] && src="the default"
  fi
  over=$(count_over "$f" "$limit")
  n=$(printf '%s\n' "$over" | grep -c . || true)
  if [ "$n" -gt 0 ]; then
    fail 3 "a subject carries line(s) over its limit of $limit characters, resolved from $src: $f"
    printf '%s\n' "$over" | while IFS=: read -r ln len; do
      [ -n "$ln" ] && printf '  %s:%s is %s characters\n' "$f" "$ln" "$len"
    done
  else
    printf 'line-length OK — %s: 0 over %d characters (limit from %s)\n' "$f" "$limit" "$src"
  fi
done

exit "$status"
