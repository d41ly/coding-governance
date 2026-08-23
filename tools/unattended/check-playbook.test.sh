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
# A CAPTURE THAT FEEDS AN ASSERTION IS SHAPE-ASSERTED BEFORE IT IS COMPARED. Round 4, MEDIUM 8: the
# tree half of the pinned-vs-tree pair below greps free-text prose, and with the capture EMPTY the
# comparison `[ "${TREE1#*verified }" != 0 ]` yielded `[ "" != 0 ]`, which is true — so the arm went
# green having compared one number against nothing. Four code paths in the leg suppress that census
# line, and a wording change empties it silently. This is `fixture-passes-by-finding-nothing` from the
# project's own checklist, inside the arm rewritten that round to remove it.
require_shape() { # value · glob · what-it-is
  n=$((n+1))
  case "$1" in
    $2) ;;
    *) st=1; echo "FAIL the capture for $3 does not have the shape every assertion below reads it as, so those assertions would compare against nothing: [$1]" ;;
  esac
}

seed() { # dir
  mkdir -p "$1/tools/unattended"
  # HERMETIC AGAINST THE MACHINE'S OWN GIT CONFIG, not only against the real tree. Round 5, MEDIUM 7:
  # the replace-ref arm below asserts a pinned read is unmoved, and a developer with
  # `core.useReplaceRefs=false` set globally would see that arm pass no matter what the leg does. A
  # fixture that reads ambient machine state is this project's own `fixture-inherits-ambient-machine-state`.
  export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
  ( cd "$1" && git init -q -b main . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false )
  cp "$HERE/check-playbook.sh" "$HERE/PLAYBOOK-TEMPLATE.template.md" "$1/tools/unattended/"
  cp "$HERE/playbook.fixture.md" "$1/tools/unattended/"
  # The PIECES and their records. Without them the reader's population is empty in the scratch tree,
  # its five states are unreachable, and the arms below would each pass by finding nothing — which is
  # the defect this whole leg is about, reproduced inside its own test.
  cp -r "$HERE/fixture-pieces" "$1/tools/unattended/"
  cp -r "$HERE/fixture-records" "$1/tools/unattended/"
  # THE CONF, because check 10 reads BYPASS_BAN from it and a fixture without one exercises the SKIP
  # path while looking exactly like a clean scan. The playbook fixture already declares its `records`
  # root, so this is the last thing standing between the scan and a real population.
  printf 'PLAYBOOK_GLOB="tools/unattended/*.md"\nBYPASS_BAN="--no-verify"\n' > "$1/.unattended.conf"
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

# ---- AC6, the ATTENDED path: the record census is read with NO run-state file anywhere in the tree.
# ---- That is the whole claim the attended path rests on — it is gated on WHAT IT PRODUCED and not
# ---- on how it ran — and the seeded tree is exactly that shape, so the arm is a check rather than a
# ---- construction. Without it the claim is true here by accident.
n=$((n+1))
[ -z "$(cd "$W" && git ls-files '*/RUN.md' 'RUN.md' 2>/dev/null)" ] \
  || bad "the scratch tree carries a run-state file, so 'the records are read with no run to name' is not what the census arm below observed"
n=$((n+1))
run | grep -qE 'pieces 2 · verified 2 · failed 0 · stale 0 · unrecorded 0 · unchecked 0' \
  || bad "the leg did not report the per-piece census over the tracked records, so the attended path's only gated surface is ungraded"

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
counts() { run | grep -oE 'pieces [0-9]+ · verified [0-9]+ · failed [0-9]+ · stale [0-9]+ · unrecorded [0-9]+ · unchecked [0-9]+' | head -1; }
PKEEP="$TMP/p1.keep"; RKEEP="$TMP/r1.keep"
if [ -n "$R1" ] && [ -f "$P1" ]; then
  cp "$P1" "$PKEEP"; cp "$R1" "$RKEEP"
  [ "$(counts)" = "pieces 2 · verified 2 · failed 0 · stale 0 · unrecorded 0 · unchecked 0" ] && ok \
    || bad "the reader's clean state is not two verified pieces — every state arm below is measured against this one"

  printf '\nedited after its record\n' >> "$P1"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 0 · stale 1 · unrecorded 0 · unchecked 0" ] && ok \
    || bad "editing a piece after its record did not move it to STALE — the hash join is not joining"
  cp "$PKEEP" "$P1"

  mv "$R1" "$R1.hidden"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 0 · stale 0 · unrecorded 1 · unchecked 0" ] && ok \
    || bad "removing a record did not move its piece to UNRECORDED"
  mv "$R1.hidden" "$R1"

  sed -i 's/verdict PASS/verdict FAIL/' "$R1"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 1 · stale 0 · unrecorded 0 · unchecked 0" ] && ok \
    || bad "a recorded FAIL verdict did not move its piece out of VERIFIED — verified would then be a hash-join state alone, which is the defect that made fork 5 implemented by nothing"
  cp "$RKEEP" "$R1"

  # ---- B1 (round-1 diff review): the SIXTH state. `verified` used to mean "the hash matches and
  # ---- nobody wrote FAIL", so a record carrying NO verdict for a leg the playbook DECLARES counted
  # ---- as verified and `pieces-complete` certified pieces nothing had checked. The fixture always
  # ---- carried a PASS, so "no FAIL" and "every declared leg passed" were the same observation in the
  # ---- only tree that tested it — which is why 43 assertions and a 92-leg bar were green over it.
  sed -i '/^leg /d' "$R1"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 0 · stale 0 · unrecorded 0 · unchecked 1" ] && ok \
    || bad "a record carrying NO verdict for a DECLARED leg still counted as verified — the piece_checks join is not joining, and pieces-complete would certify a piece nothing checked"
  cp "$RKEEP" "$R1"

  # ...and an EXPLICIT NA satisfies a declared leg, where an ABSENT row does not. That distinction is
  # the whole rule: NA is a judgement somebody recorded about this piece, absence is nothing at all.
  sed -i 's/^leg \(.*\) · verdict PASS$/leg \1 · verdict NA/' "$R1"
  [ "$(counts)" = "pieces 2 · verified 2 · failed 0 · stale 0 · unrecorded 0 · unchecked 0" ] && ok \
    || bad "an EXPLICIT NA on a declared leg did not satisfy it — NA and absence are then the same thing, and a playbook cannot record that a check does not apply to a piece"
  cp "$RKEEP" "$R1"

  # ...and a verdict for a leg the playbook does NOT declare satisfies nothing. Without this the join
  # is satisfied by any row at all, which is the shape it replaced wearing a longer predicate.
  sed -i 's/^leg .* · verdict PASS$/leg not-declared-anywhere · verdict PASS/' "$R1"
  [ "$(counts)" = "pieces 2 · verified 1 · failed 0 · stale 0 · unrecorded 0 · unchecked 1" ] && ok \
    || bad "a verdict naming an UNDECLARED leg satisfied the join, so any row at all counts and the declaration is decorative"
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

# ---- B2 (round-2 fold): --counts AT A SHA, and the liveness refusal that goes with it. Reading the
# ---- blob is what stops one uncommitted line moving a piece from `unchecked` to `verified` on the
# ---- Definition-of-Done item that takes no override — and an unreadable blob must SAY so, because an
# ---- empty body parses to "declares no checks", which is the vacuous green this leg exists to refuse.
n=$((n+1))
# The subshell's own `&&` put a ` && ` on the assertion line, which is exactly the shape
# `check-arms` reads as a NEGATIVE assertion — so this arm existed and scored as an absence test,
# which is the "something mentions it" shape that checker exists to refuse. The output is computed
# on its own line; the assertion line then carries neither the `&&` nor a here-string with one.
badsha=$( cd "$W" && bash tools/unattended/check-playbook.sh --counts tools/unattended/playbook.fixture.md '' 0000000000000000000000000000000000000000 2>&1 )
grep -qF -- "the playbook does not resolve at the sha this count was asked for, so every declaration it carries would parse to nothing and the census would report a clean run over an unreadable file - sha and playbook follow" <<<"$badsha" \
  || bad "--counts at an unresolvable sha did not refuse, so an empty body would parse as declaring no checks"
# ...and at a REAL sha it reads the BLOB, not the tree — asserted in the one direction where the
# two answers DIFFER. Round 3, HIGH 5: this arm deleted `piece_checks` on disk and asserted the
# census did not move, but the fixture records carry a PASS for every declared leg, so
# "declares nothing" and "declares legs that all passed" are the SAME census. All four cells
# printed `verified=2 unchecked=0`, including the defective working-tree read the arm was written
# to catch. `fixture-passes-by-finding-nothing`, from this project's own checklist, sitting on a
# blocker.
#
# The distinguishing input is a declared leg NO RECORD SATISFIES: committed, the pinned read must
# report it unchecked; deleted on disk, an unpinned read must not. Both halves in one arm, so the
# PAIR is what passes rather than either number alone.
cp "$KEEP" "$F"
sed -i 's|^piece_checks  = \["fixture-shape"\]|piece_checks  = ["phantom-leg"]|' "$F"
n=$((n+1))
grep -q 'phantom-leg' "$F" || bad "the phantom-leg fixture edit did not take, so both halves below would measure the shipped declaration"
( cd "$W" && git add -A >/dev/null && git commit -qm phantom )
AT=$( cd "$W" && git rev-parse HEAD )
PIN0=$( cd "$W" && bash tools/unattended/check-playbook.sh --counts tools/unattended/playbook.fixture.md '' "$AT" | grep -m1 '^pieces=' )
n=$((n+1))
[ "$PIN0" = "pieces=2 verified=0 failed=0 stale=0 unrecorded=0 unchecked=2" ] \
  || bad "a leg no record satisfies did not grade its pieces unchecked, so the arm below cannot tell the pinned read from the tree read: [$PIN0]"
sed -i '/^piece_checks/d' "$F"
PIN1=$( cd "$W" && bash tools/unattended/check-playbook.sh --counts tools/unattended/playbook.fixture.md '' "$AT" | grep -m1 '^pieces=' )
TREE1=$( cd "$W" && bash tools/unattended/check-playbook.sh | grep -oE 'pieces [0-9]+ · verified [0-9]+' | head -1 )
require_shape "$TREE1" 'pieces * · verified *' "the tree read of the census"
n=$((n+1))
[ "$PIN1" = "$PIN0" ] \
  || bad "an UNCOMMITTED piece_checks delete moved the PINNED census, so the close still reads the file the run can edit: [$PIN0] then [$PIN1]"
n=$((n+1))
case "$PIN1" in *"verified=0"*) [ "${TREE1#*verified }" -ne 0 ] || bad "the tree read and the pinned read agree over a tree where the declaration was deleted, so this arm cannot distinguish them and would pass against the defect it exists to catch" ;; *) bad "the pinned read is not the unchecked one, so the comparison below is not the one this arm makes: [$PIN1]" ;; esac
( cd "$W" && git checkout -q -- tools/unattended/playbook.fixture.md 2>/dev/null )
cp "$KEEP" "$F"
( cd "$W" && git add -A >/dev/null && git commit -qm restore-fixture )

# ---- BLOCKER (round-3): a LEGAL MULTI-LINE TOML ARRAY. Every call site did its own
# ---- `sed … | head -1`, so an array spread over lines yielded the bare `[`, parsed to the DECLARED
# ---- NULL, and graded every verdict-less piece `verified` — on the one Definition-of-Done item that
# ---- takes no override. No attacker needed: an author formatting an array the ordinary way was
# ---- enough, and check 28 CERTIFIED that output because empty was all it ever asserted.
cp "$KEEP" "$F"
sed -i 's|^piece_checks  = \["fixture-shape"\]|piece_checks  = [\n  "fixture-shape",\n]|' "$F"
n=$((n+1))
grep -q '^piece_checks  = \[$' "$F" || bad "the multi-line fixture edit did not take, so the arm below tests a single-line declaration"
out=$(run)
n=$((n+1))
grep -qF -- "a playbook opens a per-piece check list and does not close it on the same line, and this parser reads one line - an unarmed parse must red rather than return the declared null, because the declared null makes every piece verified on the one Definition-of-Done item that takes no override; playbook:" <<<"$out" \
  || bad "a multi-line declaration was accepted rather than refused, so it parses to the declared null and every unchecked piece grades verified"
n=$((n+1))
grep -qE 'pieces [0-9]+ · verified' <<<"$out" \
  && bad "the leg printed a census for a playbook whose declaration it could not read, which is a number the caller would trust"
cp "$KEEP" "$F"

# ...and the SET list refuses the same way. Both declarations are read by one parser, so both had to
# gain the refusal — a fix to one is a fix to neither, which is how the comment strip landed on one of
# them in round 2.
cp "$KEEP" "$F"
sed -i 's|^set_checks    = \["fixture-distinct"\]|set_checks    = [\n  "fixture-distinct",\n]|' "$F"
n=$((n+1))
grep -q '^set_checks    = \[$' "$F" || bad "the multi-line set_checks edit did not take"
n=$((n+1))
grep -qF -- "a playbook opens a set-scoped check list and does not close it on the same line, and this parser reads one line - an unarmed parse must red rather than return the declared null; playbook" <<<"$(run)" \
  || bad "a multi-line set_checks declaration was accepted rather than refused"
cp "$KEEP" "$F"

# ---- BLOCKER (round-4): THE SAME ARRAY, WITH A TRAILING COMMENT. The round-3 refusal ran its
# ---- terminator test on the RAW line, so a `]` anywhere in a comment satisfied the closed arm, the
# ---- strip that runs one line later reduced the value to a bare `[`, and the whole defect came back
# ---- at rc 0. The plain form above still refused — which is precisely why the round-3 arm, check
# ---- 28's round-3 specimen and 92 gate legs were all green over it. A bracketed cross-reference in a
# ---- comment is ordinary TOML authoring; no attacker is required, twice over.
cp "$KEEP" "$F"
sed -i 's|^piece_checks  = \["fixture-shape"\]|piece_checks  = [   # one per piece [see section 7]\n  "fixture-shape",\n]|' "$F"
n=$((n+1))
grep -q '^piece_checks  = \[   # one per piece \[see section 7\]$' "$F" || bad "the bracket-in-comment fixture edit did not take, so the arm below tests the comment-free form the round-3 arm already covers"
out=$(run)
n=$((n+1))
grep -qF -- "a playbook opens a per-piece check list and does not close it on the same line" <<<"$out" \
  || bad "a multi-line declaration whose opening line carries a bracket in its comment was accepted rather than refused, so it parses to the declared null and every unchecked piece grades verified"
n=$((n+1))
grep -qE 'pieces [0-9]+ · verified' <<<"$out" \
  && bad "the leg printed a census for a playbook whose declaration it could not read, which is a number the caller would trust"
cp "$KEEP" "$F"

# ---- MEDIUM 7 (round-4): the step floor came off an ad-hoc `tr -dc '0-9'`, which concatenated every
# ---- digit in the trailing comment into the number — a true refusal for a false reason, naming a
# ---- floor the author never wrote, and in the other direction a false green that bypassed the
# ---- no-floor refusal entirely.
cp "$KEEP" "$F"
sed -i 's|^step_floor.*$|step_floor    = 1     # at least 1, per section 5 and F2|' "$F"
n=$((n+1))
grep -q '^step_floor    = 1     # at least 1, per section 5 and F2$' "$F" || bad "the digit-bearing floor comment edit did not take"
out=$(run)
# THE ANCHOR, before the two negatives. Round 5, MEDIUM 9: an arm made only of `&& bad` assertions
# passes when the capture is empty, which is indistinguishable from the leg being silent for the
# right reason. Something the leg always prints has to be present first.
n=$((n+1))
grep -qE 'population [0-9]+ playbook' <<<"$out" \
  || bad "the leg produced no population line, so the two refusals asserted ABSENT below were asserted over nothing"
n=$((n+1))
grep -qE 'check 3 FAILED' <<<"$out" \
  && bad "a valid playbook whose floor line carries a digit-bearing comment red check 3, so the floor was spliced out of the prose rather than parsed: $(grep -m1 'check 3 FAILED' <<<"$out")"
n=$((n+1))
grep -qF -- 'declares a step selector and no floor' <<<"$out" \
  && bad "a floor that IS declared read as absent once its comment was stripped, which is the opposite failure and the same parser"
cp "$KEEP" "$F"

# ...and the other half of the same repair: a floor that is not a number at all. The ad-hoc read
# laundered arbitrary text through `tr -dc` and produced a number nobody wrote; refusing is the only
# honest answer, and `step_floor = soon` used to parse to the empty string and reach the no-floor
# refusal instead, which names the wrong cause.
cp "$KEEP" "$F"
sed -i 's|^step_floor.*$|step_floor    = soon|' "$F"
n=$((n+1))
grep -q '^step_floor    = soon$' "$F" || bad "the non-numeric floor edit did not take"
out=$(run)
n=$((n+1))
grep -qF -- "a playbook declares a step floor that is not a number, and laundering it through a digit filter would invent one out of whatever prose follows - floor and playbook follow: [" <<<"$out" \
  || bad "a non-numeric step floor was accepted rather than refused, so whatever prose follows the equals sign becomes the floor"
n=$((n+1))
grep -qF -- 'declares a step selector and no floor' <<<"$out" \
  && bad "a non-numeric floor ALSO reported itself absent, which is the wrong-cause message the numeric refusal exists to replace"
cp "$KEEP" "$F"

# ---- TOOL-dScriptedRepeat-13: THE BYPASS FLAG IN A TRACKED EVIDENCE RECORD. The driver refuses to
# ---- WRITE one; nothing read them back, so a flag that reached a record by any other route survived
# ---- every gate. Check 11 in the sibling leg covers run-state files and structurally cannot cover
# ---- these - it has no GITLS, no declared_scalar and enumerates no playbooks, which is why the spec
# ---- for this moved the scan here at rev-2 rather than inlining a third parser copy over there.

# AC4 FIRST, because it is the one that decides whether anything below means anything: the scan must
# say which of the two silences it is in. A skipped scan and a clean one are the same empty output.
n=$((n+1))
grep -qF -- "bypass scan - " <<<"$(run)" \
  || bad "the leg does not report the bypass scan population, so a scan that reached zero records is indistinguishable from one that read many and found nothing"

# AC1 — a PER-PIECE record carrying the flag.
cp "$KEEP" "$F"
PREC=$(cd "$W" && git ls-files 'tools/unattended/fixture-records/tools~*.md' | head -1)
n=$((n+1))
[ -n "$PREC" ] || bad "no per-piece record in the fixture, so the arm below would grade an empty population"
printf '\nlanded with --no-verify\n' >> "$W/$PREC"
n=$((n+1))
grep -qF -- "a tracked EVIDENCE RECORD names the declared bypass flag, and bypassing the lander discards the whole bar the run mandate leaned on - this is the record a reviewer reads to believe the run, so the flag being in it is the claim and the confession at once" <<<"$(run)" \
  || bad "a per-piece record naming the declared bypass flag did not red check 10"
( cd "$W" && git checkout -q -- "$PREC" )

# AC2 — a SET-scoped record carrying it, which is a different writer and a different path shape.
SREC=$(cd "$W" && git ls-files 'tools/unattended/fixture-records/set-*.md' | head -1)
n=$((n+1))
[ -n "$SREC" ] || bad "no set-scoped record in the fixture, so the arm below would grade an empty population"
printf '\nlanded with --no-verify\n' >> "$W/$SREC"
n=$((n+1))
grep -qF -- "a tracked EVIDENCE RECORD names the declared bypass flag, and bypassing the lander discards the whole bar the run mandate leaned on - this is the record a reviewer reads to believe the run, so the flag being in it is the claim and the confession at once" <<<"$(run)" \
  || bad "a set-scoped record naming the declared bypass flag did not red check 10"
( cd "$W" && git checkout -q -- "$SREC" )

# AC4's other half — no declared flag, no scan, and the leg SAYS so rather than going quiet.
( cd "$W" && printf 'PLAYBOOK_GLOB="tools/unattended/*.md"\n' > .unattended.conf )
out=$(run)
n=$((n+1))
grep -qF -- "bypass scan SKIPPED" <<<"$out" \
  || bad "with no BYPASS_BAN declared the leg does not announce the skip, so an unarmed scan reads as a clean one"
n=$((n+1))
grep -qF -- "a tracked EVIDENCE RECORD names the declared bypass flag" <<<"$out" \
  && bad "the scan ran with no declared flag, which means it is matching something other than the declaration"
( cd "$W" && printf 'PLAYBOOK_GLOB="tools/unattended/*.md"\nBYPASS_BAN="--no-verify"\n' > .unattended.conf )

# AC5 — SHARING, not liveness. The roots this scan reads must be the roots the census reads, and the
# only way to assert that is to move the declaration and watch BOTH follow. A liveness arm would pass
# over two independent derivations that happen to agree today.
cp "$KEEP" "$F"
sed -i 's|^records       = "tools/unattended/fixture-records"|records       = "tools/unattended/moved-records"|' "$F"
( cd "$W" && git mv tools/unattended/fixture-records tools/unattended/moved-records >/dev/null 2>&1 )
out=$(run)
n=$((n+1))
grep -qE 'pieces [0-9]+ · verified' <<<"$out" \
  || bad "the census lost its population when the declared root moved, so this arm cannot compare the two readers"
n=$((n+1))
grep -qF -- "bypass scan - 0 tracked" <<<"$out" \
  && bad "the census followed the moved root and the bypass scan did not, so the two readers derive their roots separately - which is the second-copy defect this unit exists to avoid"
( cd "$W" && git mv tools/unattended/moved-records tools/unattended/fixture-records >/dev/null 2>&1 )
cp "$KEEP" "$F"

# ---- ROUND 7's THREE DEFECTS IN CHECK 10, each with the arm that would have caught it. All three
# ---- are one class: a guard that reports itself armed while its population, its literal or its count
# ---- is not what the report claims.

# BLOCKER 2 — the scan used to live inside the `grain && records` block, and grain is an INDEPENDENT
# declared null. Blanking grain alone took the leg from RC=1 to RC=0 with the whole evidence corpus
# unread. The arm blanks grain, leaves records, and requires the flag in a record to still red.
cp "$KEEP" "$F"
PREC=$(cd "$W" && git ls-files 'tools/unattended/fixture-records/tools~*.md' | head -1)
printf '\nlanded with --no-verify\n' >> "$W/$PREC"
sed -i 's|^grain         = .*|grain         = ""|' "$F"
out=$(run)
n=$((n+1))
grep -qF -- "a tracked EVIDENCE RECORD names the declared bypass flag" <<<"$out" \
  || bad "with grain blanked and records still declared, the bypass scan does not run - it is reachable only through a key it does not read"
( cd "$W" && git checkout -q -- "$PREC" )
cp "$KEEP" "$F"

# BLOCKER 3 — `.unattended.conf` is a SHELL file and every other reader sources it. Two legal
# spellings that a `sed | tr -d '"' | head -1` reader resolves differently, each with a record
# carrying the flag, each required to red. Without the fix the leg exits 0 AND prints that it read
# the corpus, which is the worst of the two possible wrong answers.
for _sp in "BYPASS_BAN='--no-verify'" 'BYPASS_BAN="--no-verify"   # the flag the lander bans'; do
  cp "$KEEP" "$F"
  printf '\nlanded with --no-verify\n' >> "$W/$PREC"
  ( cd "$W" && printf 'PLAYBOOK_GLOB="tools/unattended/*.md"\n%s\n' "$_sp" > .unattended.conf )
  n=$((n+1))
  grep -qF -- "a tracked EVIDENCE RECORD names the declared bypass flag" <<<"$(run)" \
    || bad "a legal shell spelling of BYPASS_BAN resolves to something no record can contain, and the leg says nothing: $_sp"
  ( cd "$W" && git checkout -q -- "$PREC" )
done
  ( cd "$W" && printf 'PLAYBOOK_GLOB="tools/unattended/*.md"\nBYPASS_BAN="--no-verify"\n' > .unattended.conf )

# BLOCKER 3's OTHER HALF — an unarmed predicate must RED rather than print a population count over a
# literal nothing can match. A resolved value carrying whitespace is a reader that mis-parsed.
( cd "$W" && printf 'PLAYBOOK_GLOB="tools/unattended/*.md"\nBYPASS_BAN="--no-verify   # trailing prose"\n' > .unattended.conf )
n=$((n+1))
grep -qF -- "the declared bypass flag resolves to a value carrying whitespace or a comment character, which no flag does - so this leg would grep the corpus for a literal no record can contain and then report that it read the corpus. Resolved value follows: [" <<<"$(run)" \
  || bad "a bypass flag resolving to a value with whitespace in it is accepted and greped for, which no record can ever match"
  ( cd "$W" && printf 'PLAYBOOK_GLOB="tools/unattended/*.md"\nBYPASS_BAN="--no-verify"\n' > .unattended.conf )

# BLOCKER 2's TEETH — a declared flag over a declared root that enumerates NOTHING is a scan that
# cannot move, and a note never reds. This empties the records root and requires a failure.
cp "$KEEP" "$F"
sed -i 's|^records       = .*|records       = "tools/unattended/empty-records"|' "$F"
( cd "$W" && mkdir -p tools/unattended/empty-records && printf 'x\n' > tools/unattended/empty-records/.keep && git add -A >/dev/null 2>&1 )
n=$((n+1))
grep -qF -- "playbook records root(s) are declared, and the scan read ZERO tracked records - so this check is asserted over an empty population and would stay green with the flag in every record under them" <<<"$(run)" \
  || bad "a declared bypass flag over a declared records root holding no records reports a healthy zero instead of redding"
( cd "$W" && git rm -q -r --cached tools/unattended/empty-records >/dev/null 2>&1; rm -rf tools/unattended/empty-records )
cp "$KEEP" "$F"

# A TRACKED RECORD THE WORKTREE DOES NOT HAVE. The counter that proves the scan reached the corpus
# must not count a file nothing opened - the same defect as the word-split one below, one step earlier.
cp "$KEEP" "$F"
GHOST="tools/unattended/fixture-records/tools~ghost~x.md"
( cd "$W" && printf 'piece: nope\n' > "$GHOST" && git add -- "$GHOST" >/dev/null 2>&1 && rm -f "$GHOST" )
n=$((n+1))
grep -qF -- "a tracked evidence record is not readable in this worktree, so the bypass scan cannot answer for it and counting it as read would inflate the number that proves the scan reached the corpus" <<<"$(run)" \
  || bad "a record git tracks and the worktree does not have is counted as read, which inflates the only number that proves the scan reached the corpus"
( cd "$W" && git rm -q --cached -- "$GHOST" >/dev/null 2>&1 )
cp "$KEEP" "$F"

# HIGH 1 — `git ls-files` does not quote a path containing a space, so an unquoted `for` split one
# record into two names that do not exist: the flag went unread AND the liveness counter incremented
# twice for it. The arm puts the flag in a record whose name has a space and requires the red.
cp "$KEEP" "$F"
SPACED="tools/unattended/fixture-records/tools~a b~c.md"
( cd "$W" && cp "$PREC" "$SPACED" && printf '\nlanded with --no-verify\n' >> "$SPACED" && git add -- "$SPACED" >/dev/null 2>&1 )
out=$(run)
n=$((n+1))
grep -qF -- "a tracked EVIDENCE RECORD names the declared bypass flag" <<<"$out" \
  || bad "a record whose filename contains a space is never opened, so the flag in it is invisible while the scan reports a count that includes it"
n=$((n+1))
grep -qF -- "bypass scan - tools/unattended/fixture-records: 4 tracked evidence record(s) read" <<<"$out" \
  || bad "the per-root count does not equal the tracked record count, so the number that proves the scan reached the corpus is not measuring the corpus"
( cd "$W" && git rm -q --cached -- "$SPACED" >/dev/null 2>&1; rm -f "$SPACED" )
cp "$KEEP" "$F"

# ---- BLOCKER (round-4): THE REPLACE REF. `git replace -f <base> <forged>` rewrites what a sha
# ---- dereference returns without touching one tracked byte, and ONLY `-c core.useReplaceRefs=false`
# ---- suppresses it — the exported GIT_GRAFT_FILE a spawned leg inherits does NOT, and a `-c` is
# ---- per-invocation so nothing propagates it from the driver. This leg's single sha read produces
# ---- every declaration the `--counts` census grades, and that census is the sole evidence for
# ---- `pieces-complete`, which takes no override. So an unpinned read hands the run the playbook it
# ---- is graded against.
# ----
# ---- Round 3 filed this. The fold recorded the fix in the commit message, in spec 5 rev-9 and in the
# ---- acceptance ledger, and the change never reached the file. This arm and check 28c are the two
# ---- things that would have said so.
# The HONEST history declares a check nothing recorded, so its census is unchecked. The FORGED one
# declares the check the records DO satisfy. That direction is the attack: a run substitutes a
# playbook its own evidence happens to pass, which is why the honest half must be the strict one.
cp "$KEEP" "$F"
sed -i 's|^piece_checks  = .*|piece_checks  = ["phantom-leg"]|' "$F"
( cd "$W" && git add -A >/dev/null && git commit -qm honest-strict )
HONEST=$( cd "$W" && git rev-parse HEAD )
PINH=$( cd "$W" && bash tools/unattended/check-playbook.sh --counts tools/unattended/playbook.fixture.md '' "$HONEST" | grep -m1 '^pieces=' )
require_shape "$PINH" 'pieces=* verified=*' "the honest pinned census this arm compares against"
cp "$KEEP" "$F"
( cd "$W" && git add -A >/dev/null && git commit -qm forged-permissive )
FORGED=$( cd "$W" && git rev-parse HEAD )
PINF=$( cd "$W" && bash tools/unattended/check-playbook.sh --counts tools/unattended/playbook.fixture.md '' "$FORGED" | grep -m1 '^pieces=' )
require_shape "$PINF" 'pieces=* verified=*' "the forged pinned census this arm compares against"
n=$((n+1))
[ "$PINF" != "$PINH" ] \
  || bad "the forged tree grades identically to the honest one, so this arm cannot detect a substitution and would pass against the defect it exists to catch: [$PINH]"
n=$((n+1))
( cd "$W" && git replace -f "$HONEST" "$FORGED" >/dev/null 2>&1 ) \
  || bad "the replace ref could not be installed, so the lever this arm measures was never armed"
n=$((n+1))
[ -n "$( cd "$W" && git for-each-ref refs/replace/ )" ] \
  || bad "no replace ref exists after installing one, so the read below is unpinned against nothing"
# THE LEVER BITES. Round 5, MEDIUM 7: this arm proved a replace ref EXISTED and then that the pinned
# read was unmoved, which is also what a git that ignores replace refs entirely would produce - the
# arm could not tell a working pin from a machine where the lever does nothing. An UNPINNED read of
# the same sha must return the forged bytes, or there is no lever to be pinned against.
n=$((n+1))
[ "$( cd "$W" && git show "$HONEST:tools/unattended/playbook.fixture.md" | grep -c 'phantom-leg' )" = "0" ] \
  || bad "an UNPINNED read at the honest sha returned the honest bytes, so the replace ref does nothing on this machine and the pinned assertion below proves nothing"
PINR=$( cd "$W" && bash tools/unattended/check-playbook.sh --counts tools/unattended/playbook.fixture.md '' "$HONEST" | grep -m1 '^pieces=' )
n=$((n+1))
[ "$PINR" = "$PINH" ] \
  || bad "a replace ref moved the PINNED census at an unchanged, honest sha, so the run supplies the playbook it is measured against on the one item that takes no override: honest [$PINH] became [$PINR]"
( cd "$W" && git replace -d "$HONEST" >/dev/null 2>&1 )
cp "$KEEP" "$F"
( cd "$W" && git add -A >/dev/null && git commit -qm restore-after-replace )

# ---- HIGH 2 (round-3): the sha is MANDATORY. Round 2 blocked a per-FIELD pin that silently reverted
# ---- when a field was missing; the fold replaced it with a per-SHA pin that silently reverted when
# ---- the sha was missing. `fact` returns empty with exit 0, so the only caller could hand this
# ---- nothing and never know.
emptypin=$( cd "$W" && bash tools/unattended/check-playbook.sh --counts tools/unattended/playbook.fixture.md '' '' 2>&1 )
n=$((n+1))
grep -qF -- "--counts requires the sha to read the playbook at; an absent pin would silently parse the working tree, which is the file the run itself can edit" <<<"$emptypin" \
  || bad "--counts accepted an EMPTY sha, so an absent pin silently reads the file the run can edit"

# ---- HIGH 3 (round-3): the declared null is the WORD `none`. The escape prefix-matched, so a check
# ---- named `nonempty-rows` read as "declares nothing" and the item returned MET with no record.
cp "$KEEP" "$F"
sed -i 's|^set_checks    = \["fixture-distinct"\]|set_checks    = ["nonempty-rows"]|' "$F"
n=$((n+1))
grep -q 'nonempty-rows' "$F" || bad "the nonempty fixture edit did not take"
n=$((n+1))
grep -qF -- "set checks unrecorded" <<<"$(run)" \
  || bad "a set check whose name merely STARTS with none read as declaring nothing, so the item passes with no record and no verdict"
cp "$KEEP" "$F"

# ---- B1 (round-2 fold): THE TEMPLATE'S OWN COMMENT. The kit ships
# ---- `piece_checks = []    # the checks that run over ONE piece.`, and the parser that read it had
# ---- no comment strip — so the comment word-split into eight phantom legs and graded every piece
# ---- `unchecked`, on the one Definition-of-Done item that takes no override. Every hand-written
# ---- fixture drops the comment, which is exactly why no fixture caught it.
cp "$KEEP" "$F"
sed -i 's|^piece_checks  = \["fixture-shape"\]|piece_checks  = ["fixture-shape"]    # the checks that run over ONE piece.|' "$F"
sed -i 's|^set_checks    = \["fixture-distinct"\]|set_checks    = ["fixture-distinct"]  # the checks that run over ALL N.|' "$F"
n=$((n+1))
grep -q '#' <<<"$(grep '^piece_checks' "$F")" || bad "the fixture edit did not put a comment on the declaration, so the arm below tests nothing"
out=$(run)
n=$((n+1))
grep -qE 'verified 2 · failed 0 · stale 0 · unrecorded 0 · unchecked 0' <<<"$out" \
  || bad "a declaration carrying the template's OWN trailing comment did not parse to its declared checks — the comment is being read as check names"
n=$((n+1))
grep -qF -- "set checks unrecorded" <<<"$out" \
  && bad "the set-check declaration carrying a trailing comment was misparsed the same way"
cp "$KEEP" "$F"

# ---- M4 (round-1 diff review): THE SET RECORD IS READ. Three documents said this leg read it while
# ---- nothing in it opened one — `record_for` and the orphan sweep both key on a `piece:` line, which
# ---- a set record does not carry, so both walked past it. On the ATTENDED path, which never calls
# ---- `--close`, the set-scoped verdicts were graded by nothing at all.
# ----
# ---- GREEN CONTROL FIRST: the shipped fixture now carries a complete set record, so silence here is
# ---- a reader finding nothing wrong rather than a reader that never ran. The three red arms below
# ---- are what tell those apart.
SR="$W/tools/unattended/fixture-records/set-dScriptedRepeat.md"
n=$((n+1)); [ -f "$SR" ] || bad "the fixture ships no set record, so every arm below would report a missing one and prove nothing about the reader"
out=$(run)
n=$((n+1)); grep -qF -- "no set record" <<<"$out" && bad "the complete fixture still reports a missing set record"
n=$((n+1)); grep -qF -- "set checks unrecorded" <<<"$out" && bad "the complete fixture reports an unrecorded declared set check"

# ...the record REMOVED. The playbook declares a set check, pieces exist, and nothing records whether
# it ran — which is exactly the attended path's blind spot.
( cd "$W" && git rm -q tools/unattended/fixture-records/set-dScriptedRepeat.md )
n=$((n+1)); grep -qF -- "no set record" <<<"$(run)" \
  || bad "removing the set record produced no report — the leg is not reading set records at all"
( cd "$W" && git checkout -q HEAD -- tools/unattended/fixture-records/set-dScriptedRepeat.md 2>/dev/null || git reset -q HEAD -- tools/unattended/fixture-records/set-dScriptedRepeat.md )

# ...the record PRESENT but carrying no verdict for the DECLARED check. A record that merely exists is
# the shape `set-checks-recorded` used to accept, one population up from the per-piece blocker.
sed -i 's/^leg fixture-distinct · verdict PASS$/leg something-else · verdict PASS/' "$SR"
n=$((n+1)); grep -qF -- "set checks unrecorded" <<<"$(run)" \
  || bad "a set record carrying a verdict only for an UNDECLARED check was accepted, so any row at all counts"
sed -i 's/^leg something-else · verdict PASS$/leg fixture-distinct · verdict PASS/' "$SR"

# ...and a recorded FAIL is reported. This is the check a monoculture passes every piece and fails on.
sed -i 's/^leg fixture-distinct · verdict PASS$/leg fixture-distinct · verdict FAIL/' "$SR"
n=$((n+1)); grep -qF -- "set check FAILED" <<<"$(run)" \
  || bad "a FAILING set-scoped verdict went unreported"
sed -i 's/^leg fixture-distinct · verdict FAIL$/leg fixture-distinct · verdict PASS/' "$SR"
n=$((n+1)); grep -qF -- "set check FAILED" <<<"$(run)" && bad "the restore did not take, so the arm above passes on every later run"

# ---- B2 (round-1 diff review): THE READER MUST RUN FOR EVERY PLAYBOOK, not for the last one.
# ---- The whole per-piece block sat AFTER the `done` closing the population loop while indented as
# ---- its body, so it ran once over the previous iteration's leftover variables. With a population
# ---- of one — which is every tree that ships this fixture and nothing else — inside-the-loop and
# ---- after-the-loop are the same program, which is why 43 assertions and a 92-leg bar were green.
# ----
# ---- The arm is POSITIONAL by construction: the violating playbook is placed where `git ls-files`
# ---- sorts it FIRST, so under the defective code the fixture wins the leftover variables and the
# ---- violation is never read. A second playbook that sorted last would pass on the broken code too.
cp "$KEEP" "$F"
mkdir -p "$W/content"
cat > "$W/content/pb-first.md" <<'PBTWO'
# a second playbook, sorting BEFORE the kit's fixture

```toml
step_selector = "^[*][*]F[0-9]+[.]"
step_floor    = 1
outputs       = ["content/own/**"]
grain         = "content/own/*/piece.md"
piece_checks  = []
set_checks    = []
legs          = { }
coverage      = "dark"
curated       = "the round-1 fold, node d, 2026-08-21"
```

**F1.** the only step. `CHECK it exists · witness none`

## 1. Identity and provenance
none — a fixture for the multi-playbook arm.
## 2. Ground rules
none — see section 1.
## 3. Inputs and preconditions
none — see section 1.
## 4. Outputs
none — see section 1.
## 5. The step checklist
**F1.** the only step. `CHECK it exists · witness none`
## 6. The producer recipe
none — see section 1.
## 7. Per-piece checks
none — see section 1.
## 8. Set-scoped checks
none — see section 1.
## 9. Declared gate legs
none — see section 1.
## 10. Ruled out — do not re-try
none — see section 1.
## 11. Measured failure modes
none — see section 1.
## 12. Corrections to this file
none — see section 1.
PBTWO
( cd "$W" && git add -A >/dev/null && git commit -qm "second playbook" )
n=$((n+1))
[ "$(cd "$W" && git ls-files | grep -n 'content/pb-first.md' | cut -d: -f1)" -lt \
  "$(cd "$W" && git ls-files | grep -n 'playbook.fixture.md' | cut -d: -f1)" ] \
  || bad "the second playbook does not sort before the fixture, so this arm cannot distinguish inside-the-loop from after-the-loop"
out=$(run)
n=$((n+1))
grep -qF -- "population 2 playbook" <<<"$out" \
  || bad "the leg did not see two playbooks, so the arm below would pass over a population it never enumerated"
n=$((n+1))
grep -qF -- "a playbook declares a piece grain and no records root" <<<"$out" \
  || bad "the FIRST-sorting playbook's grain-without-records violation was never read — the per-piece reader is running outside the population loop and grading only the last playbook"
( cd "$W" && git rm -q content/pb-first.md && git commit -qm "drop second playbook" )
cp "$KEEP" "$F"

# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, in the shape the bar's
# `check-testsuite-counts.sh` leg requires of every self-test. Without it a block of arms stranded
# past an exit leaves the suite reporting success over the arms it never reached, which is the same
# green-by-absence this leg's own subject is about. RE-MEASURED at the round-3 fold: 72 executed,
# same absolute headroom as the pin it replaces. RE-MEASURED again at the round-4 fold: 86 executed, and at the round-5 fold: 90.
FLOOR_ASSERTIONS=82
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
