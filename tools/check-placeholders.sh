#!/usr/bin/env bash
# check-placeholders.sh — the playbook's version-marker lockstep, and the survival predicate.
#
#   bash tools/check-placeholders.sh              # assert the marker lockstep over the SOURCES
#   bash tools/check-placeholders.sh --check A B  # assert no placeholder SURVIVED in two FILLED files
#
# SCOPE, and what deliberately is NOT here. This gate landed carrying a third assertion — that
# a deploy-time placeholder CATALOGUE agreed with the measured sets — and `tools/check-playbook-
# parity.sh` landed on the default branch first with exactly that predicate as its S3. Two gates
# asserting one property over one file is the two-answers-to-one-question class at gate level, and
# the two disagreed immediately: each expected its own prose format, so satisfying one red the other.
# The arithmetic was ceded to parity, and v3.0 then deleted the catalogue itself — the placeholders
# are filled by `tools/playbook/` now, so there is no prose to agree with. What remains here is the
# half nothing else checks.
#
# THE SUBJECT SPLIT, which is why the survival predicate is a separate mode. In this repo the shipped
# playbook file IS the un-instantiated template source and carries placeholders permanently and by
# design. A leg asserting "no placeholder survives" over it would red on its own landing commit and
# could never go green here. So that predicate takes explicit targets and is exercised only by
# fixtures in the sibling test — never over the tracked source. The RENDER-side owner of it already
# exists and stays where it is: `tools/govkit/entries/playbook.kit.toml`'s `playbook-placeholders`
# hole runs it over the DEPLOYED charter at `{playbook_path}`, which is the only place "survived" is
# a meaningful question. The mode still takes TWO operands: an adopter whose charter renders beside a
# second filled file has two subjects, and one operand could not express that.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "check-placeholders: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

TEMPLATE="coding-governance-agents.template.md"

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

[ -f "$TEMPLATE" ] || { echo "check-placeholders: missing shipped file: $TEMPLATE"; exit 2; }

rc=0

# ONE file carries the marker now. The charter converged at v3.0 and its companion was deleted, so
# the LOCKSTEP QUESTION DIED WITH THE SECOND CARRIER. It is not weakened — it is gone, and saying so
# plainly is the point: a comparison over a population of one is not a comparison, and a gate that
# pretended otherwise would be comparing a file against itself. What survives is presence plus
# well-formedness of the single marker, which is what the kickoff engine's Step-2 fallback and the
# upstream re-pull actually read.
if ! grep -qE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$TEMPLATE"; then
  echo "check-placeholders: $TEMPLATE carries NO governance-template marker, and the kickoff"
  echo "check-placeholders: engine's Step-2 fallback plus the upstream re-pull both read it"
  rc=1
fi

n_markers=$(grep -cE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$TEMPLATE" || true)
if [ "$rc" -eq 0 ] && [ "$n_markers" -ne 1 ]; then
  echo "check-placeholders: $TEMPLATE carries $n_markers version markers rather than exactly one,"
  echo "check-placeholders: so which one a reader gets is a matter of scan order"
  rc=1
fi
marker=$(grep -oE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$TEMPLATE" | head -1)

[ "$rc" -eq 0 ] && echo "check-placeholders OK — one marker carrier at $marker"
# EXPLICIT, and it was deleted. Without it this mode's verdict is the LAST COMMAND's status, correct
# today only by short-circuit accident: `rc=1` makes the `[` fail and the AND-list returns 1. Any line
# appended below — a trailing echo, a cleanup `rm -f`, a `trap`, a bare `true` — makes the marker gate
# always-green while still printing its failure text, and the bar runs this script bare. The `--check`
# branch above already ends this way; two modes producing a verdict by two mechanisms is the asymmetry.
exit "$rc"
