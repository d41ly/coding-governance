#!/usr/bin/env bash
# check-placeholders.sh — the playbook's version-marker lockstep, and the survival predicate.
#
#   bash tools/check-placeholders.sh              # assert the marker lockstep over the SOURCES
#   bash tools/check-placeholders.sh --check A B  # assert no placeholder SURVIVED in two FILLED files
#
# SCOPE, and what deliberately is NOT here. This gate landed carrying a third assertion — that
# `customize.md`'s placeholder catalogue agrees with the measured sets — and `tools/check-playbook-
# parity.sh` landed on the default branch first with exactly that predicate as its S3. Two gates
# asserting one property over one file is the two-answers-to-one-question class at gate level, and
# the two disagreed immediately: each expected its own prose format, so satisfying one red the other.
# The arithmetic is parity's. What remains here is the half nothing else checks.
#
# THE SUBJECT SPLIT, which is why the survival predicate is a separate mode. In this repo the shipped
# playbook files ARE the un-instantiated template sources and carry placeholders permanently and by
# design. A leg asserting "no placeholder survives" over them would red on its own landing commit and
# could never go green here. So that predicate takes an explicit target pair and is exercised only by
# fixtures in the sibling test — never over the tracked sources. The RENDER-side owner of it already
# exists and stays where it is: `tools/govkit/entries/playbook.kit.toml`'s `playbook-placeholders`
# hole runs it over the DEPLOYED pair, which is the only place "survived" is a meaningful question.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "check-placeholders: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

TEMPLATE="parallel-coding-governance.template.md"
COMPANION="parallel-coding-governance.domain-rules.md"

# --- the fixture-only survival mode ---------------------------------------------------------------
if [ "${1:-}" = "--check" ]; then
  [ $# -eq 3 ] || { echo "usage: $(basename "$0") --check <filled-a> <filled-b>"; exit 2; }
  rc=0
  for f in "$2" "$3"; do
    [ -f "$f" ] || { echo "check-placeholders: no such file: $f"; exit 2; }
    while IFS= read -r hit; do
      echo "check-placeholders: SURVIVING PLACEHOLDER in $f — ${hit}"
      rc=1
    done < <(grep -noE '\{\{[A-Z][A-Z0-9_]*\}\}' -- "$f" || true)
  done
  [ "$rc" -eq 0 ] && echo "check-placeholders OK — no placeholder survived in the two filled files"
  exit "$rc"
fi

[ "${1:---assert}" = "--assert" ] || { echo "usage: $(basename "$0") [--check <a> <b>]"; exit 2; }

for f in "$TEMPLATE" "$COMPANION"; do
  [ -f "$f" ] || { echo "check-placeholders: missing shipped file: $f"; exit 2; }
done

rc=0

# TWO files carry the marker, not three. `customize.md` is the deploy-time catalogue, is exempt from
# the shipped surface, and its only `vN.N` is prose — a gate built to "three" would compare a literal
# against a real version and red forever. That miscount reached a spec through a review fold and was
# caught only by measuring.
#
# PRESENCE FIRST, then agreement. Counting DISTINCT markers alone reads "one file has v2.9 and the
# other has none" as agreement: a comparison over a population of one is not a comparison.
for f in "$TEMPLATE" "$COMPANION"; do
  grep -qE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$f" || {
    echo "check-placeholders: $f carries NO governance-template marker — the lockstep comparison"
    echo "check-placeholders: needs both carriers present, or it compares one file against itself"
    rc=1
  }
done

markers=$(grep -hoE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$TEMPLATE" "$COMPANION" | sort -u)
n_markers=$(printf '%s\n' "$markers" | grep -c . || true)
if [ "$rc" -eq 0 ] && [ "$n_markers" -ne 1 ]; then
  echo "check-placeholders: the two marker-carrying files disagree on governance-template:"
  for f in "$TEMPLATE" "$COMPANION"; do
    echo "  $f: $(grep -oE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$f" | head -1 || echo '(none)')"
  done
  rc=1
fi

[ "$rc" -eq 0 ] && echo "check-placeholders OK — both marker carriers agree at $markers"
exit "$rc"
