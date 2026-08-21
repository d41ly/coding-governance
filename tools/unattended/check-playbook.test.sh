#!/usr/bin/env bash
# check-playbook.test.sh — the self-test for the playbook validity leg.
#
# HERMETIC: every arm runs in its own scratch git repo under `mktemp -d`, never in the real tree.
# The leg reads `git ls-files`, so a test that mutated the real tree would be testing this
# repository's contents rather than the predicate.
#
# EVERY ARM IS A STAGED BREAK WITH AN EXPECTED CHECK NUMBER. Asserting only that the leg RED would
# pass whenever anything at all was wrong, which is the shape that lets a predicate drift onto a
# different population and still look armed. The arms assert WHICH check spoke.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT
n=0; st=0
ok()   { n=$((n+1)); }
bad()  { n=$((n+1)); st=1; echo "FAIL $1"; }

seed() { # dir
  mkdir -p "$1/tools/unattended"
  ( cd "$1" && git init -q -b main . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false )
  cp "$HERE/check-playbook.sh" "$HERE/PLAYBOOK-TEMPLATE.template.md" "$1/tools/unattended/"
  cp "$HERE/playbook.fixture.md" "$1/tools/unattended/"
  ( cd "$1" && git add -A >/dev/null && git commit -qm seed )
}

run() { ( cd "$W" && bash tools/unattended/check-playbook.sh 2>&1 ); }
rc()  { ( cd "$W" && bash tools/unattended/check-playbook.sh >/dev/null 2>&1; echo $? ); }

W="$TMP/w"; seed "$W"
F="$W/tools/unattended/playbook.fixture.md"
KEEP="$TMP/keep.md"; cp "$F" "$KEEP"

# ---- the GREEN control, first and deliberately. Ten red arms with no green one are satisfied by a
# ---- leg that reds on everything, and that leg looks exactly this armed.
[ "$(rc)" = 0 ] && ok || bad "the shipped fixture does not pass its own leg"
hitline=$(run | grep -c 'population 1 playbook' || true)
[ "$hitline" = 1 ] && ok || bad "the leg did not report a population of exactly one over the seeded tree"

probe() { # label · expected check · sed program · expected message signature
  cp "$KEEP" "$F"; ( cd "$W" && sed -i "$3" tools/unattended/playbook.fixture.md )
  out=$(run); r=$?
  got=$(printf '%s\n' "$out" | grep -oE 'check [0-9]+ FAILED' | head -1)
  if [ "$r" -eq 0 ]; then bad "$1: the leg exited 0 — the check is UNARMED, not lenient"
  elif ! printf '%s' "$got" | grep -q "check $2 "; then
    bad "$1: expected check $2, got [$got] — the wrong arm fired, which is worse than none"
  else ok
  fi
  # The MESSAGE as well as the number. The number alone passes when a branch's text drifts away from
  # the arm naming it, which is how a signature and its assertion stop describing the same branch.
  n=$((n+1))
  grep -qF -- "$4" <<<"$out" || { st=1; echo "FAIL missing: $4"; }
  cp "$KEEP" "$F"
}

probe "no curator"          2 's/^curated .*/curated       = ""/' "a playbook declares no curator, and the freeze is the only machine consequence a derive-then-freeze template has - a derived canon nobody ratified is a mirror of the corpus it came from, which is the one shape a template must not have; playbook:"
probe "no step selector"    3 's/^step_selector.*/step_selector = ""/' "a playbook declares no step selector, and a kit-fixed one either misses a playbook's steps entirely - reporting every step tagged over an empty set - or selects its prose; playbook:"
probe "floor above steps"   3 's/^step_floor.*/step_floor    = 99/' "a playbook's declared step selector matches fewer lines than its own declared floor, which is the signal that the selector stopped reaching the steps rather than that the steps went away - matched, floor and playbook follow:"
probe "untagged step"       4 's/`CHECK the canon is prose[^`]*`//' "a playbook carries a step with no GATE or CHECK tag in its window, so what enforces it is unstated and every reader who did not write it will assume something - offender and playbook follow:"
probe "unknown coverage"    6 's/^coverage .*/coverage      = "banana"/' "a playbook declares a coverage mode outside the closed set, and defaulting an unrecognised one would select a strictness nobody asked for - declared and playbook follow:"
probe "coverage absent"     6 's/^coverage .*//' "a playbook declares no coverage mode for its leg registry, and a gate that quietly skips what it forgot looks exactly like coverage - declare resolvable, probe or dark; playbook:"
probe "gate not declared"   6 's/GATE fixture-shape/GATE fixture-nowhere/' "a playbook tags a step with a gate leg its own registry does not declare, so the tag names an enforcement nothing resolves - leg and playbook follow:"
probe "resolvable dead tgt" 6 's|fixture-shape = "tools/unattended/check-playbook.sh"|fixture-shape = "tools/unattended/gone.sh"|' "a playbook declares coverage resolvable and names a leg target that does not resolve in this tree, so the strictness it claims is one nothing can hold it to - target, leg and playbook follow:"
probe "no step floor"       3 's/^step_floor.*//' "a playbook declares a step selector and no floor, so a selector that quietly matches nothing would report every step tagged over an empty selection; playbook"
probe "resolvable dead cmd" 6 's|fixture-shape = "tools/unattended/check-playbook.sh"|fixture-shape = "definitely-not-on-path-xyz"|' "a playbook declares coverage resolvable and names a leg command that is not on PATH, so the strictness it claims is one nothing can hold it to - target, leg and playbook follow"
probe "canon section gone"  7 's/^## 8\. Set-scoped checks/## 8. Something Else Entirely/' "a playbook is missing a required canon section, and an absent section is indistinguishable from a forgotten one - a section that does not apply keeps its heading and carries a declared null; section and playbook follow:"

# ---- check 1: the EMPTY POPULATION. The fixture leaves the tree entirely, which is the only way to
# ---- reach it — and it is the arm that matters most, because the state it catches is the one that
# ---- otherwise prints `GATE ok` over an empty set for the leg carrying this mode's enforcement.
cp "$KEEP" "$F"
( cd "$W" && git rm -q tools/unattended/playbook.fixture.md )
out=$(run); r=$?
if [ "$r" -ne 0 ] && printf '%s\n' "$out" | grep -q 'check 1 FAILED'; then ok
  n=$((n+1)); grep -qF -- "no tracked file carries a playbook declaration block, so every check in this leg would pass over an empty population and print a green that means the opposite of what it looks like - this leg ships a fixture playbook precisely so that cannot be the ordinary state" <<<"$out" || { st=1; echo "FAIL missing: no tracked file carries a playbook declaration block, so every check in this leg would pass over an empty population and print a green that means the opposite of what it looks like - this leg ships a fixture playbook precisely so that cannot be the ordinary state"; }
else bad "empty population: expected check 1 and a non-zero exit, got rc=$r"; fi
# and the leg must NOT print a green-looking line in that state
printf '%s\n' "$out" | grep -q 'population 0 playbook' && ok || bad "the empty-population report does not name the count it found"
( cd "$W" && git checkout -q -- tools/unattended/playbook.fixture.md 2>/dev/null || git reset -q HEAD tools/unattended/playbook.fixture.md )
cp "$KEEP" "$F"

# ---- the DECLARED-NULL versus EMPTY distinction, which check 7 exists to make. A section carrying
# ---- `none — <why>` PASSES; the same heading with nothing under it is a forgotten section. Without
# ---- this pair the canon check is satisfied by a heading and teaches authors to leave stubs.
cp "$KEEP" "$F"
[ "$(rc)" = 0 ] && ok || bad "the fixture's `none — <why>` section 6 does not satisfy the canon check"

# ---- THE CANON IS DERIVED, and this is the arm that proves it. Removing a row from the shipped
# ---- template must shrink what the leg demands; if it does not, the canon is hardcoded somewhere
# ---- and the template is decoration.
( cd "$W" && sed -i '/^| 8 | Set-scoped checks/d' tools/unattended/PLAYBOOK-TEMPLATE.template.md \
    && sed -i 's/^## 8\. Set-scoped checks/## 8. Renamed/' tools/unattended/playbook.fixture.md )
[ "$(rc)" = 0 ] && ok || bad "removing a canon row from the template did not relax the section check — the canon is not derived from the template"
seed_out=$(run | grep -c 'canon 11 section' || true)
[ "$seed_out" = 1 ] && ok || bad "the leg did not report the shrunken canon count it derived"

# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, in the shape the bar's
# `check-testsuite-counts.sh` leg requires of every self-test. Without it a block of arms stranded
# past an exit leaves the suite reporting success over the arms it never reached, which is the same
# green-by-absence this leg's own subject is about.
FLOOR_ASSERTIONS=28
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
