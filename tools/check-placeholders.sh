#!/usr/bin/env bash
# check-placeholders.sh — the playbook's placeholder catalogue agrees with the playbook.
#
#   bash tools/check-placeholders.sh              # assert over THIS repo's template SOURCES
#   bash tools/check-placeholders.sh --check A B  # assert no placeholder SURVIVED in two FILLED files
#
# THE SUBJECT SPLIT, which is the whole design. In this repo the shipped playbook files ARE the
# un-instantiated template sources: they carry 23 and 14 placeholders permanently and by design. A
# gate asserting "no placeholder survives" over them would red on its own landing commit and could
# never go green here, so the bare mode asserts only what is true of a SOURCE:
#
#   1. every placeholder MEASURED in the two shipped files is listed in the catalogue;
#   2. the catalogue's per-file tallies equal the measurement;
#   3. a placeholder appearing in BOTH files is declared SHARED — not disjoint;
#   4. the two marker-carrying files agree on `governance-template: vN.N`.
#
# The survival predicate lives in `--check A B` and is exercised only by fixtures in the sibling
# test, never over the tracked sources. The RENDER-side owner of that predicate already exists and
# stays where it is: `tools/govkit/entries/playbook.kit.toml`'s `playbook-placeholders` hole runs it
# over the DEPLOYED pair, which is the only place "survived" is a meaningful question.
#
# (3) is what funds the standing backlog row. `customize.md` has claimed the two placeholder groups
# are disjoint through at least one correction cycle while `{{MEMORY_ROOT}}` sat in both files. A
# prose correction that nothing checks is a claim waiting to rot again; this is the gate that
# replaces it.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "check-placeholders: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

TEMPLATE="parallel-coding-governance.template.md"
COMPANION="parallel-coding-governance.domain-rules.md"
CATALOGUE="parallel-coding-governance.customize.md"

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

for f in "$TEMPLATE" "$COMPANION" "$CATALOGUE"; do
  [ -f "$f" ] || { echo "check-placeholders: missing shipped file: $f"; exit 2; }
done

placeholders_in() { grep -oE '\{\{[A-Z][A-Z0-9_]*\}\}' -- "$1" | sort -u; }

t_set=$(placeholders_in "$TEMPLATE")
c_set=$(placeholders_in "$COMPANION")
t_n=$(printf '%s\n' "$t_set" | grep -c . || true)
c_n=$(printf '%s\n' "$c_set" | grep -c . || true)
shared=$(comm -12 <(printf '%s\n' "$t_set") <(printf '%s\n' "$c_set") | grep . || true)

# NON-EMPTY POPULATION IS ITS OWN ARM. A measurement of zero would make every comparison below
# vacuously true, and a gate that passes because it found nothing is the failure this repo has a
# catalogue record about.
if [ "$t_n" -eq 0 ] || [ "$c_n" -eq 0 ]; then
  echo "check-placeholders: measured $t_n and $c_n placeholders — an empty side means the extractor"
  echo "check-placeholders: is broken, not that the files are clean. Refusing to pass."
  exit 1
fi

rc=0

# 1. catalogue coverage — every measured placeholder is listed somewhere in the catalogue.
for p in $t_set $c_set; do
  grep -qF -- "$p" "$CATALOGUE" || { echo "check-placeholders: $p is used but is NOT listed in $CATALOGUE"; rc=1; }
done

# 2. the per-file tallies. The catalogue writes them as `### In \`<file>\` — <n>`.
tally_for() { grep -oE "^### In \`$1\` — [0-9]+" "$CATALOGUE" | grep -oE '[0-9]+$' | head -1; }
t_claim=$(tally_for "$TEMPLATE"); c_claim=$(tally_for "$COMPANION")
[ -n "$t_claim" ] || { echo "check-placeholders: $CATALOGUE has no \`### In \`$TEMPLATE\` — <n>\` heading"; rc=1; }
[ -n "$c_claim" ] || { echo "check-placeholders: $CATALOGUE has no \`### In \`$COMPANION\` — <n>\` heading"; rc=1; }
[ "${t_claim:-x}" = "$t_n" ] || { echo "check-placeholders: $CATALOGUE claims $t_claim in $TEMPLATE; measured $t_n"; rc=1; }
[ "${c_claim:-x}" = "$c_n" ] || { echo "check-placeholders: $CATALOGUE claims $c_claim in $COMPANION; measured $c_n"; rc=1; }

# 3. the disjointness claim, which is the one that has actually been wrong.
if [ -n "$shared" ]; then
  if grep -qE '\*\*disjoint\*\*' "$CATALOGUE"; then
    echo "check-placeholders: $CATALOGUE calls the two placeholder groups **disjoint**, but these appear in BOTH files:"
    printf '  %s\n' $shared
    echo "check-placeholders: a shared placeholder must be filled CONSISTENTLY in two places, which is"
    echo "check-placeholders: the opposite of what 'filled in exactly one place' tells the deployer."
    rc=1
  fi
  for p in $shared; do
    grep -qE "^Shared between both files:.*$(printf '%s' "$p" | sed 's/[{}]/\\&/g')" "$CATALOGUE" || {
      echo "check-placeholders: $p appears in BOTH shipped files but is not named on the catalogue's"
      echo "check-placeholders: \`Shared between both files:\` line"
      rc=1
    }
  done
else
  grep -qE '^Shared between both files:' "$CATALOGUE" && {
    echo "check-placeholders: $CATALOGUE declares a shared placeholder line, but no placeholder is in both files"
    rc=1
  }
fi

# 4. the marker lockstep. TWO files carry the marker, not three: the catalogue is the deploy-time
# document and is exempt from the shipped surface — its only `vN.N` is prose, and a grep that
# counted it would compare a literal against a real version and red forever.
markers=$(grep -hoE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$TEMPLATE" "$COMPANION" | sort -u)
n_markers=$(printf '%s\n' "$markers" | grep -c . || true)
if [ "$n_markers" -ne 1 ]; then
  echo "check-placeholders: the two marker-carrying files disagree on governance-template:"
  for f in "$TEMPLATE" "$COMPANION"; do
    echo "  $f: $(grep -oE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$f" | head -1 || echo '(none)')"
  done
  rc=1
fi

[ "$rc" -eq 0 ] && echo "check-placeholders OK — $t_n + $c_n placeholders catalogued, $(printf '%s\n' "$shared" | grep -c . || true) shared and declared, markers agree at $markers"
exit "$rc"
