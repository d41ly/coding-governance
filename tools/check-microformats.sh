#!/usr/bin/env bash
# check-microformats.sh — grade the charter's micro-format DEFINITIONS against their own grammar.
#
#   bash tools/check-microformats.sh [<file>]
#
# SUBJECT. The RULESET — `coding-governance-agents.template.md` — because that is the source. A
# target's rendered charter carries the same block, and it is proved equal to this one by
# `tools/playbook/adopt-playbook.sh --check` rather than graded twice.
#
# WHAT IT KEYS ON. The HTML-comment fence pair around the definition list, and nothing else. It
# cannot key on a heading: the section has none. It cannot key on a column-zero list marker either,
# because the emission rule de-indents the definitions into siblings of the section's own prose
# rules, so a marker-anchored selector would select the whole section.
#
# WHAT IT DOES NOT CHECK, said here rather than implied away: it holds SYNTAX. Whether a shape's
# FIELDS are the right fields is a design question this gate has no opinion about, and a shape that
# is perfectly well-formed and semantically wrong passes.
#
# Exit 0 = every definition satisfies the grammar · 1 = an offender · 2 = could not run.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "check-microformats: not a git tree"; exit 2; }
cd "$ROOT" || exit 2

FILE=${1:-coding-governance-agents.template.md}
OPEN='<!-- microformats -->'
CLOSE='<!-- /microformats -->'
# The frozen SENTINEL. The keyword set is DERIVED from the block — a hand-typed copy inside this gate
# would be a mirror of the subject it grades, which the charter forbids by name. That derivation can
# break silently and certify an empty set, so one membership is pinned.
SENTINEL=committed

status=0
fail() { printf 'MICROFORMAT check %s FAILED — %s\n' "$1" "$2"; status=1; }

[ -f "$FILE" ] || { echo "check-microformats: no such file: $FILE"; exit 2; }

n_open=$(grep -cF "$OPEN" "$FILE" || true)
n_close=$(grep -cF "$CLOSE" "$FILE" || true)
if [ "$n_open" -ne 1 ] || [ "$n_close" -ne 1 ]; then
  echo "check-microformats: the definition block is not delimited by exactly one fence pair in"
  echo "check-microformats: $FILE — found $n_open opener(s) and $n_close closer(s). A gate that"
  echo "check-microformats: cannot find its block must say so, never report a clean set."
  exit 2
fi

block=$(awk -v o="$OPEN" -v c="$CLOSE" 'index($0,o){f=1;next} index($0,c){f=0} f' "$FILE")
defs=$(printf '%s\n' "$block" | grep -E '^- `.*`$' || true)
n_defs=$(printf '%s\n' "$defs" | grep -c . || true)

if [ "$n_defs" -eq 0 ]; then
  echo "check-microformats: the fence pair is present and encloses no definition line, so every"
  echo "check-microformats: predicate below would pass over an empty set."
  exit 2
fi

keywords=$(printf '%s\n' "$defs" | sed -E 's/^- `([^ ]+).*/\1/')
if ! printf '%s\n' "$keywords" | grep -qx "$SENTINEL"; then
  fail 1 "the keyword derivation lost its frozen sentinel member, so the derivation is broken rather than the block being empty: expected to find $SENTINEL"
fi

while IFS= read -r line; do
  [ -n "$line" ] || continue
  body=${line#- \`}; body=${body%\`}
  head=${body%% — *}
  # ---- the joiner appears exactly once
  n_join=$(printf '%s' "$body" | grep -o ' — ' | grep -c . || true)
  if [ "$n_join" -ne 1 ]; then
    fail 2 "a definition carries $n_join joiners rather than exactly one, so its head and tail cannot be told apart: $body"
    continue
  fi
  # ---- the joiner's POSITION: nothing but the head precedes it. A separate predicate from the
  # ---- count, because three shapes once satisfied the count while failing the position.
  # THERE IS NO ⏳ EXEMPTION HERE, and there used to be one that could not be taken. The arm read
  # `[ "$head" = "⏳" ] || fail 3`, guarded by a case matching heads that CONTAIN A SPACE — and the
  # hourglass head is three bytes with no space in it, so the case never selected it and the equality
  # was never evaluated. Re-derived over the live block: all heads print space-free. The glyph passes
  # this predicate the same way every keyword does, by being one token; the exemption only told a
  # reader it was special. `memory/gotchas/armed-but-unreachable-rule.md` is the class.
  case "$head" in
    *" "*) fail 3 "a definition puts a field ahead of its joiner, so the head is not one keyword: $body" ;;
  esac
  # ---- parentheses, outside markdown-link syntax
  stripped=$(printf '%s' "$body" | sed -E 's/\[[^]]*\]\([^)]*\)//g')
  case "$stripped" in
    *"("*|*")"*) fail 4 "a definition carries a bare parenthesis, which the grammar admits only as markdown-link syntax: $body" ;;
  esac
  # ---- a colon acting as a joiner or a label. Glued to a value (a port) is legal.
  case "$body" in
    *": "*) fail 5 "a definition uses a colon as a label, which the grammar admits only glued to a value: $body" ;;
  esac
  # ---- placeholders are lowercase angle-bracket names
  while IFS= read -r ph; do
    [ -n "$ph" ] || continue
    case "$ph" in
      *[A-Z]*) fail 6 "a placeholder is not a lowercase angle-bracket name: $ph in $body" ;;
    esac
  done <<EOF
$(printf '%s' "$body" | grep -oE '<[^>]+>' || true)
EOF
done <<EOF
$defs
EOF

[ "$status" -eq 0 ] && printf 'microformats OK — %d definition(s) graded, %d keyword(s) derived\n' \
  "$n_defs" "$(printf '%s\n' "$keywords" | sort -u | grep -c .)"
exit "$status"
