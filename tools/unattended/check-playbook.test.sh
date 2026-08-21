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
  # The PIECES and their records. Without them the reader's population is empty in the scratch tree,
  # its five states are unreachable, and the arms below would each pass by finding nothing — which is
  # the defect this whole leg is about, reproduced inside its own test.
  cp -r "$HERE/fixture-pieces" "$1/tools/unattended/"
  cp -r "$HERE/fixture-records" "$1/tools/unattended/"
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

# ---- the playbook-authoring unit, AC1: the population is TREE-DERIVED, and that is what makes a playbook
# ---- gradeable from the commit that adds it — before any build README names it, and whether or not
# ---- one ever does. A creation run's whole output is a playbook with no run bound to it yet; under
# ---- the seam-derived predicate this replaced, that playbook was invisible to its own gate.
n=$((n+1))
[ -z "$(ls -A "$W/memory/builds" 2>/dev/null)" ] \
  || bad "the scratch tree carries a build README, so 'graded with no README naming it' is not what the arm above observed"
n=$((n+1))
grep -qF -- "$W/tools/unattended/playbook.fixture.md" <<<"$(cd "$W" && git ls-files | sed "s|^|$W/|")" \
  || bad "the fixture playbook is not tracked, and the leg reads git ls-files, so the population arm above passed over something else"

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

probe "grain, no records"   8 's|^records .*||' "a playbook declares a piece grain and no records root, so its pieces enumerate and none of them joins to evidence - every per-piece state would read as unrecorded and the count that means the build made what was asked would have nothing to compare; playbook:"

# ---- THE READER'S FIVE STATES. Each is staged and the COUNTS are asserted, not just a red/green:
# ---- the reader CLASSIFIES and never grades, so none of these reds the leg and an arm asserting a
# ---- red would fail on every one of them. What distinguishes a working reader from a dead one is
# ---- which column moved.
cp "$KEEP" "$F"
P1="$W/tools/unattended/fixture-pieces/one/piece.md"
R1=$(ls "$W"/tools/unattended/fixture-records/*one*.md 2>/dev/null | head -1)
counts() { run | grep -oE 'pieces [0-9]+ · verified [0-9]+ · failed [0-9]+ · stale [0-9]+ · unrecorded [0-9]+' | head -1; }
PKEEP="$TMP/p1.keep"; RKEEP="$TMP/r1.keep"
if [ -n "$R1" ] && [ -f "$P1" ]; then
  cp "$P1" "$PKEEP"; cp "$R1" "$RKEEP"
  [ "$(counts)" = "pieces 2 · verified 2 · failed 0 · stale 0 · unrecorded 0" ] && ok \
    || bad "the reader's clean state is not two verified pieces — every state arm below is measured against this one"

  printf '\nedited after its record\n' >> "$P1"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 0 · stale 1 · unrecorded 0" ] && ok \
    || bad "editing a piece after its record did not move it to STALE — the hash join is not joining"
  cp "$PKEEP" "$P1"

  mv "$R1" "$R1.hidden"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 0 · stale 0 · unrecorded 1" ] && ok \
    || bad "removing a record did not move its piece to UNRECORDED"
  mv "$R1.hidden" "$R1"

  sed -i 's/verdict PASS/verdict FAIL/' "$R1"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 1 · stale 0 · unrecorded 0" ] && ok \
    || bad "a recorded FAIL verdict did not move its piece out of VERIFIED — verified would then be a hash-join state alone, which is the defect that made fork 5 implemented by nothing"
  cp "$RKEEP" "$R1"

  mv "$P1" "$P1.hidden"
  run | grep -q 'orphan record' && ok || bad "a record whose piece is gone was not reported as an ORPHAN — the reverse direction, without which a corpus reports coverage it no longer has"
  mv "$P1.hidden" "$P1"

  # THE LIVENESS ASSERTION. Every count above can be satisfied by a tree with no pieces, so the arm
  # that matters most is the one proving the reader SAYS SO instead of reporting a clean zero.
  ( cd "$W" && sed -i 's|^grain .*|grain         = "tools/unattended/nowhere/*/piece.md"|' tools/unattended/playbook.fixture.md )
  run | grep -q 'DEAD PROBE' && ok || bad "a grain resolving no piece did not report a DEAD PROBE — a reader that enumerates zero and reports zero failures is indistinguishable from a clean run"
  [ "$(rc)" = 0 ] && ok || bad "the dead probe REDDED the leg; the reader classifies and never grades, and only --close blocks"
  cp "$KEEP" "$F"
else
  bad "the scratch tree carries no piece or no record, so all six reader arms were skipped — a skip that looks like a pass is the thing this suite exists to refuse"
fi

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
FLOOR_ASSERTIONS=41
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
