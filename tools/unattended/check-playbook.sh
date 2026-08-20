#!/usr/bin/env bash
# check-playbook.sh — the merge-bar leg over every tracked PLAYBOOK. TOOL-dScriptedRepeat-3.
#
# WHAT THIS DOES NOT CHECK, said here because a structural check reads as a semantic one to everybody
# who did not write it:
#   - whether a `CHECK`'s <why> is TRUE;
#   - whether a `GATE`'s named leg tests what the step says;
#   - whether a step followed in letter was followed in spirit;
#   - whether the playbook is right about its subject at all.
# It reads SHAPE. The drain census in check 5 is the only quantitative handle on the third.
#
# AND IT CANNOT EVALUATE ON THE ATTENDED ENTRY POINT for the scope refusal specifically: that
# refusal needs a recorded mode and a run's commit set, and both exist only through the driver.
# Unit 10's attended path is gated on what it PRODUCED, never on how it ran.
#
# THE VERDICT CHANNEL. `tools/run-gates/run-gates.sh` maps a leg's own exit: 0 prints `GATE ok`,
# anything else `GATE FAIL`; `skip` comes only from a guard file written before dispatch, so a leg
# CANNOT say "skipped". An empty PLAYBOOK population therefore exits NON-ZERO — a leg carrying this
# much enforcement must not print `GATE ok` over nothing. A zero-PIECE enumeration is a different
# fact: it is REPORTED and does not red here, because unit 5's reader classifies and never grades
# and only `--close` blocks on it.
set -u

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TEMPLATE="$HERE/PLAYBOOK-TEMPLATE.template.md"
st=0
fail() { st=1; printf 'PLAYBOOK check %s FAILED — %s\n' "$1" "$2"; }
note() { printf 'playbook: %s\n' "$1"; }

command -v git >/dev/null 2>&1 || { echo "check-playbook: no git on PATH"; exit 2; }
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "check-playbook: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2

# ---------------------------------------------------------------- the CANON, derived
# From the shipped template's own section table, never a second list. A canon spelled here and in the
# template is two answers to one question, and the copy that rots is this one.
[ -f "$TEMPLATE" ] || { echo "check-playbook: the shipped template is missing, so the canon cannot be derived and every section check below would pass over an empty list: $TEMPLATE"; exit 2; }
CANON=$(awk -F'|' '/^\| *[0-9]+ *\| /{ s=$3; gsub(/^[[:space:]]+|[[:space:]]+$/,"",s); print s }' "$TEMPLATE")
CANON_N=$(printf '%s\n' "$CANON" | grep -c . || true)
[ "${CANON_N:-0}" -gt 0 ] || { echo "check-playbook: the shipped template's section table yielded no canon rows, so the section check would pass over nothing: $TEMPLATE"; exit 2; }

# ---------------------------------------------------- the POPULATION, derived from the TREE
# A tracked file IS a playbook when it carries the declaration block, or when it matches a glob the
# project declares. NOT "what the declaration seam names": that excluded the fixture this kit ships,
# excluded a freshly created playbook no build README names yet, and contradicted the rule that a
# tracked playbook is graded from the moment it is tracked.
CONF_GLOB=""
[ -f .unattended.conf ] && CONF_GLOB=$(sed -n 's/^PLAYBOOK_GLOB=//p' .unattended.conf | tr -d '"' | head -1)
PLAYBOOKS=""
while IFS= read -r f; do
  case "$f" in *.md) ;; *) continue ;; esac
  # The TEMPLATE is the canon, definitionally not a playbook: its block is a SPECIMEN with empty
  # values, and grading it would red on every field the specimen leaves for an author to fill.
  # Found by running this predicate over the real tree before wiring it, which is the rule.
  case "$f" in */PLAYBOOK-TEMPLATE.template.md|*/PLAYBOOK-TEMPLATE.md) continue ;; esac
  if grep -q '^step_selector[[:space:]]*=' "$f" 2>/dev/null && grep -q '^```toml' "$f" 2>/dev/null; then
    PLAYBOOKS="$PLAYBOOKS$f
"
  fi
done <<EOF
$(git ls-files -- '*.md')
EOF
POP=$(printf '%s' "$PLAYBOOKS" | grep -c . || true)

note "population $POP playbook(s) · canon $CANON_N section(s)${CONF_GLOB:+ · declared glob $CONF_GLOB}"

if [ "${POP:-0}" -eq 0 ]; then
  fail 1 "no tracked file carries a playbook declaration block, so every check in this leg would pass over an empty population and print a green that means the opposite of what it looks like - this leg ships a fixture playbook precisely so that cannot be the ordinary state"
  exit "$st"
fi

# ------------------------------------------------------------------------ per playbook
TOTAL_STEPS=0; TOTAL_TAGGED=0; TOTAL_WITNESS=0; TOTAL_CHECKS=0
for pb in $PLAYBOOKS; do
  [ -n "$pb" ] || continue
  body=$(tr -d '\r' < "$pb")

  # ---- 2: the FREEZE. `curated` is fork 4's only machine consequence.
  cur=$(printf '%s\n' "$body" | sed -n 's/^curated[[:space:]]*=[[:space:]]*//p' | head -1 | tr -d '"' | sed 's/[[:space:]]*$//')
  [ -n "$cur" ] || fail 2 "a playbook declares no curator, and the freeze is the only machine consequence a derive-then-freeze template has - a derived canon nobody ratified is a mirror of the corpus it came from, which is the one shape a template must not have; playbook: $pb"

  # ---- 3: the declared STEP SELECTOR and its shrink-only floor.
  sel=$(printf '%s\n' "$body" | sed -n 's/^step_selector[[:space:]]*=[[:space:]]*//p' | head -1 | sed 's/^"//; s/"[[:space:]]*$//')
  flo=$(printf '%s\n' "$body" | sed -n 's/^step_floor[[:space:]]*=[[:space:]]*//p' | head -1 | tr -dc '0-9')
  if [ -z "$sel" ]; then
    fail 3 "a playbook declares no step selector, and a kit-fixed one either misses a playbook's steps entirely - reporting every step tagged over an empty set - or selects its prose; playbook: $pb"
    continue
  fi
  nsteps=$(printf '%s\n' "$body" | grep -cE "$sel" 2>/dev/null || true)
  TOTAL_STEPS=$((TOTAL_STEPS + nsteps))
  if [ -z "$flo" ]; then
    fail 3 "a playbook declares a step selector and no floor, so a selector that quietly matches nothing would report every step tagged over an empty selection; playbook: $pb"
  elif [ "$nsteps" -lt "$flo" ]; then
    fail 3 "a playbook's declared step selector matches fewer lines than its own declared floor, which is the signal that the selector stopped reaching the steps rather than that the steps went away - matched, floor and playbook follow: $nsteps against $flo in $pb"
  fi

  # ---- 4: the TAG GRAMMAR, read over each step's WINDOW rather than its line. A tag may be
  # ---- line-wrapped, and reading line-wise silently drops those - which is live in the corpus this
  # ---- canon came from, where two invariants have never once been validated by its own gate.
  untagged=$(printf '%s\n' "$body" | awk -v sel="$sel" '
    $0 ~ sel { if (instep && !seen) print id; instep=1; id=$0; seen=($0 ~ /GATE |CHECK/) ? 1 : 0; next }
    /^#{1,6} / { if (instep && !seen) print id; instep=0; next }
    instep && (/GATE /||/CHECK/) { seen=1 }
    END { if (instep && !seen) print id }' | head -3)
  if [ -n "$untagged" ]; then
    # BOUND TO A NAME, and every interpolation at the END. A command substitution inside the message
    # makes check-arms read `$(printf '%s'` as part of the literal signature, so the branch cannot be
    # armed at all - the same trap the driver's own positional-in-a-message rule records.
    first=$(printf '%s' "$untagged" | head -1 | cut -c1-70)
    fail 4 "a playbook carries a step with no GATE or CHECK tag in its window, so what enforces it is unstated and every reader who did not write it will assume something - offender and playbook follow: $first in $pb"
  fi

  # ---- 5: the WITNESS DRAIN CENSUS. Validated where present, REPORTED, never redded on absence -
  # ---- so an existing playbook adopts this a step at a time rather than in one migration.
  nchecks=$(printf '%s\n' "$body" | grep -cE 'CHECK' || true)
  nwit=$(printf '%s\n' "$body" | grep -cE 'CHECK[^|]*· witness ' || true)
  TOTAL_CHECKS=$((TOTAL_CHECKS + nchecks)); TOTAL_WITNESS=$((TOTAL_WITNESS + nwit))

  # ---- 6: the RUNNABILITY ORACLE and its GRADED coverage mode.
  cov=$(printf '%s\n' "$body" | sed -n 's/^coverage[[:space:]]*=[[:space:]]*//p' | head -1 | tr -d '"' | sed 's/[[:space:]]*$//')
  case "$cov" in
    resolvable|probe|dark) ;;
    '') fail 6 "a playbook declares no coverage mode for its leg registry, and a gate that quietly skips what it forgot looks exactly like coverage - declare resolvable, probe or dark; playbook: $pb" ;;
    *)  fail 6 "a playbook declares a coverage mode outside the closed set, and defaulting an unrecognised one would select a strictness nobody asked for - declared and playbook follow: $cov in $pb" ;;
  esac
  gates=$(printf '%s\n' "$body" | grep -oE 'GATE [A-Za-z0-9_.:/-]+' | awk '{print $2}' | sort -u)
  for g in $gates; do
    ent=$(printf '%s\n' "$body" | grep -oE "(^[[:space:]]*|[{,][[:space:]]*)\"?$g\"?[[:space:]]*=[[:space:]]*\"[^\"]*\"" | head -1)
    if [ -z "$ent" ]; then
      fail 6 "a playbook tags a step with a gate leg its own registry does not declare, so the tag names an enforcement nothing resolves - leg and playbook follow: $g in $pb"
      continue
    fi
    # GRADED, not merely recorded. `resolvable` is a CLAIM about the targets, and a mode nothing
    # checks is a declaration nobody can be wrong about - which is the shape a coverage mode exists
    # to avoid. `probe` and `dark` make weaker claims and are graded accordingly: nothing here, and
    # the incompleteness prints instead.
    tgt=$(printf '%s' "$ent" | sed 's/.*=[[:space:]]*"//; s/"$//')
    if [ "$cov" = resolvable ]; then
      case "$tgt" in
        */*) [ -e "${tgt%% *}" ] || fail 6 "a playbook declares coverage resolvable and names a leg target that does not resolve in this tree, so the strictness it claims is one nothing can hold it to - target, leg and playbook follow: $tgt for $g in $pb" ;;
        *)   command -v "${tgt%% *}" >/dev/null 2>&1 || fail 6 "a playbook declares coverage resolvable and names a leg command that is not on PATH, so the strictness it claims is one nothing can hold it to - target, leg and playbook follow: $tgt for $g in $pb" ;;
      esac
    fi
  done
  [ "$cov" = probe ] && note "coverage probe on $pb — existence only; whether a declared target TESTS what its step says is unchecked and this line is the whole of that admission"

  # ---- 7: the CANON. Present-but-EMPTY and `none — <why>` are different states and get different
  # ---- messages: one is a forgotten section and the other is a declared null.
  # The NAME is the canon; the number is cosmetic and ANY leading number is accepted. Coupling the
  # two was the first cut and its own self-test caught it: shrinking the canon by one row would then
  # have forced every playbook in every adopter to RENUMBER, and a canon change that rewrites its
  # subject is the shape a derived vocabulary must not have.
  while IFS= read -r sec; do
    [ -n "$sec" ] || continue
    if ! printf '%s\n' "$body" | grep -qiE "^#{2,3} *([0-9]+\. *)?$(printf '%s' "$sec" | sed 's/[][\.*^$/]/\\&/g')"; then
      fail 7 "a playbook is missing a required canon section, and an absent section is indistinguishable from a forgotten one - a section that does not apply keeps its heading and carries a declared null; section and playbook follow: $sec in $pb"
    fi
  done <<CANONEOF
$CANON
CANONEOF
done

# ---- 8: the DERIVED length budget and the drain, PRINTED. No number is written in this file.
note "steps $TOTAL_STEPS · CHECK tags $TOTAL_CHECKS · of those carrying a witness $TOTAL_WITNESS"
[ "$TOTAL_CHECKS" -gt 0 ] && note "witness drain $((TOTAL_WITNESS * 100 / TOTAL_CHECKS))% — reported, never redded, so a playbook adopts the witness a step at a time"

exit "$st"
