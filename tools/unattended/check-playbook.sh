#!/usr/bin/env bash
# check-playbook.sh — the merge-bar leg over every tracked PLAYBOOK.
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

# --counts <playbook> — the machine-readable form, so the Definition-of-Done items read THIS
# enumerator instead of growing a second one. One implementation, two callers: the same shape unit
# 5 uses for its writer, and for the same reason — a second copy confirms the first rather than
# checking it, and the two drift on the first edit to either.
COUNTS_FOR=""
COUNTS_RUN=""
# THE PLAYBOOK MAY BE READ AT A SHA rather than off disk, and the driver passes the BASE its
# run-state file pinned. Parsing the working tree is right on the merge bar, where no run exists and
# the tree is all there is; it is wrong at the close, where the run is the actor that can edit the
# file being parsed.
#
# ONE sha, not a field list. The first cut of this passed the pinned `grain` and `records` and left
# `piece_checks` on disk, so one uncommitted line moved a piece from `unchecked` to `verified` on the
# item that takes no override — a per-field pin is a list somebody has to remember to extend, and the
# round-2 review caught it not being extended within the same commit that introduced it. Reading the
# BLOCK closes the class: no declaration added to it later can be forgotten here.
COUNTS_AT=""
[ "${1:-}" = "--counts" ] && { COUNTS_FOR="${2:-}"; COUNTS_RUN="${3:-}"; COUNTS_AT="${4:-}"; }
# MANDATORY, not advisory. Round 2 blocked a per-FIELD pin that silently reverted when a field was
# missing; the fold replaced it with a per-SHA pin that silently reverted when the sha was missing.
# `fact` returns empty with exit 0 for an absent key, so the only caller could hand this nothing and
# never know. The merge-bar path does not use `--counts`, so an absent pin is always a caller error.
if [ -n "$COUNTS_FOR" ] && [ -z "$COUNTS_AT" ]; then
  echo "check-playbook: --counts requires the sha to read the playbook at; an absent pin would silently parse the working tree, which is the file the run itself can edit"
  exit 2
fi

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

if [ -n "$COUNTS_FOR" ]; then
  PLAYBOOKS="$COUNTS_FOR
"
  POP=1
fi
[ -n "$COUNTS_FOR" ] || note "population $POP playbook(s) · canon $CANON_N section(s)${CONF_GLOB:+ · declared glob $CONF_GLOB}"

if [ "${POP:-0}" -eq 0 ]; then
  fail 1 "no tracked file carries a playbook declaration block, so every check in this leg would pass over an empty population and print a green that means the opposite of what it looks like - this leg ships a fixture playbook precisely so that cannot be the ordinary state"
  exit "$st"
fi

# ---------------------------------------------------------------- piece-record helpers
GITLS() { git ls-files -- "$1" 2>/dev/null; }
# CR-stripped like the on-disk read it stands in for, so a CRLF-committed playbook parses the same
# way through both paths — two readers of one file giving two answers is the class this replaces.
# THE PINNED READ, and both suppressions, because they are not interchangeable and neither covers
# both. A forced replace ref rewrites what a sha dereference returns without touching one tracked
# byte, and ONLY `-c core.useReplaceRefs=false` suppresses that; a graft file needs GIT_GRAFT_FILE,
# and a `-c` is per-invocation so nothing propagates it to a child. This leg is SPAWNED by the driver
# and inherits the driver's exported graft pin but not its `-c`, which is why the pin is spelled here
# and not assumed.
#
# This is the single read producing every declaration the `--counts` census grades, and that census
# is the sole evidence for `pieces-complete`, which takes no override. Round 4 measured the lever end
# to end: one replace ref flipped the census from verified=0 to verified=2 at an unchanged, honest
# sha. Round 3 filed it, and the fold recorded the fix in three documents without it reaching this
# line - check 28c is why that cannot happen again.
export GIT_GRAFT_FILE=/dev/null
GITSHOW() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false show "$1" 2>/dev/null | tr -d '\r'; }
# The record is found by its OWN `piece:` field rather than by re-deriving the writer's path rule.
# Re-deriving would be a second implementation of the writer's naming, which confirms it rather than
# checks it — and the two would drift the first time either changed.
record_for() { # records-root · piece-path -> its record, or empty
  local r
  for r in $(GITLS "$1/*.md"); do
    [ -n "$r" ] || continue
    [ "$(sed -n 's/^piece: //p' "$r" | head -1)" = "$2" ] && { printf '%s' "$r"; return 0; }
  done
  return 0
}

# ---------------------------------------------------------------- the DECLARED-LIST parse, ONCE
# A TOML list value from the declaration block -> its members, space-separated. THREE call sites had
# three spellings of this, which is why the trailing-comment strip landed in two of them and not the
# third: round 1 fixed `set_checks`, the fold added `piece_checks` seventy-five lines away without it,
# and the kit's OWN template ships `piece_checks = []    # the checks that run over ONE piece.` — a
# line that word-splits into eight phantom legs and grades every piece `unchecked`.
#
# The helper cannot live in a shared file: each kit script is copy-installed standalone. So it is
# inlined once per script and the two copies are compared against each other by a leg check, which is
# the only way two inlined copies stay one answer.
#
# The comment strip requires WHITESPACE before the `#`, so a legal `["a#b"]` survives it.
declared_list() { # body · key -> members space-separated; rc 2 on an unterminated array
  # THE LINE SELECTION LIVES HERE, and that is the whole point. Round 3's blocker: all three call
  # sites did their own `sed … | head -1`, so a LEGAL multi-line TOML array yielded the bare `[`,
  # parsed to the declared null, and every piece carrying no verdict graded `verified` — on the one
  # Definition-of-Done item that takes no `--override`. No attacker needed; an author formatting an
  # array the ordinary way was enough.
  #
  # AN UNARMED PARSE REDS RATHER THAN RETURNING THE DECLARED NULL (charter §7). Spanning the value
  # would be the other honest fix; refusing is cheaper and cannot be wrong about what it did not read.
  # THE COMMENT COMES OFF BEFORE THE TERMINATOR TEST, and the order is the whole fix. Round 4's
  # blocker: this ran the `case` on the RAW line, so a `]` anywhere in a trailing comment satisfied
  # the closed arm, the strip below then reduced the value to a bare `[`, and a legal multi-line
  # array parsed to the DECLARED NULL at rc 0 - the round-3 blocker restored by the commit that
  # fixed it. `piece_checks = [   # one per piece [see section 7]` is ordinary TOML authoring, and
  # the kit's own template puts a trailing comment on every declaration line.
  #
  # THE STRIP REQUIRES WHITESPACE BEFORE THE `#`, so a legal `["a#b"]` survives it. A `#` that IS
  # preceded by whitespace inside a quoted member (`["a", "b #c"]`) now REFUSES rather than
  # corrupting silently - the honest outcome for a line-oriented shell parser that cannot tokenise
  # TOML, and the reason this returns rather than guessing.
  # THE COMMENT COMES OFF THE WHOLE LINE, BEFORE THE KEY IS REMOVED, and the ORDER of those two is
  # the fix. Round 4 moved the strip in front of the terminator test and left it AFTER the key strip,
  # which had already eaten the whitespace the strip needs: `outputs = # globs...` lost `outputs =`
  # first, so the `#` no longer had whitespace before it, survived, and became the VALUE. Measured on
  # the shipped parser, that returned the comment text at rc 0 for every empty-valued declaration -
  # and the round-4 fold had just narrowed the outputs guard to the empty string, so a recipe-mode run
  # declaring no output globs was authorized by the repair.
  #
  # Stripping the whole line first cannot have that ordering hazard: the whitespace before a trailing
  # `#` is still there when the strip runs. A `#` with NO whitespace before it is a member character
  # (`["a#b"]`) and survives, which is the property the strip was written to keep.
  # NORMALISE FIRST, CLASSIFY SECOND, and never the other way round. Every round of this build has
  # broken here and always the same way: a decision taken on the LINE rather than on the TOKEN it is
  # about. `*'['*']'*` asked whether a `]` appeared anywhere; the comment strip asked for whitespace
  # the key strip had already eaten; and the positional closer that replaced them ran BEFORE the trims,
  # so `["a", "b"] ` - one trailing space on a perfectly closed array - was refused at rc 2 and the
  # driver told the author their bracket was unclosed. Three spellings of one mistake, each introduced
  # by the commit fixing the last.
  #
  # So the pipeline below produces a fully normalised VALUE - comment gone, key gone, CR gone, ends
  # trimmed - and nothing is asked about it until it is. A `#` at position zero is then unambiguous:
  # a TOML value cannot begin with one, so it is a comment on a key with no value at all.
  local raw
  raw=$(printf '%s\n' "$1" | grep -m1 -E "^$2[[:space:]]*=" \
        | sed 's/[[:space:]][[:space:]]*#.*$//' \
        | sed "s/^$2[[:space:]]*=[[:space:]]*//" \
        | tr -d '\r' \
        | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')
  case "$raw" in '#'*) raw='' ;; esac
  # AND THE CLOSER IS ANCHORED AT BOTH ENDS. A value is an array only if it STARTS with `[`, so
  # `k = "a[0]"` is not one and is not refused for failing to close; an array that starts is closed
  # only if it ENDS with `]`, so `["a[0]",` refuses instead of silently dropping the members below it.
  case "$raw" in
    '['*']') ;;
    '['*) return 2 ;;
  esac
  printf '%s\n' "$raw" | tr -d '"' \
    | sed 's/^\[//; s/\]$//; s/,/ /g' | tr -s ' ' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

declared_scalar() { # body · key -> the scalar it declares, comment/quotes/space stripped
  # THE SIBLING OF `declared_list`, and it selects its own line for that helper's reason: a `head -1`
  # spelled at each call site is a decision nobody reviews again. Round 3, HIGH 6: the list parse was
  # consolidated while five scalar reads stayed ad-hoc, so an adopter who filled the shipped template
  # in place and kept its comments got `grain` parsed WITH the comment — a DEAD PROBE over a tree of
  # real pieces — while `curated = ""    # who ratified…` satisfied the freeze on an unratified
  # playbook.
  #
  # Same copy-inlined discipline as its sibling: each kit script installs standalone and cannot
  # import, so both copies are byte-compared by the leg check that compares that one's.
  # THE COMMENT COMES OFF THE WHOLE LINE FIRST. Same ordering repair as the list parser, same reason:
  # the key strip consumed the whitespace this strip requires, so `curated = # who ratified...` parsed
  # to its own comment and the freeze - fork 4's only machine consequence - passed on an unratified
  # playbook. A `#` with no whitespace before it stays, because that is a value character.
  # THE `#` AT POSITION ZERO, for its sibling's reason: the trailing-comment strip needs whitespace
  # before the `#` and a key with no value at all leaves none, so `k =# note` and `k =#note` came back
  # as their own comment text at rc 0. A TOML value cannot begin with `#`.
  printf '%s\n' "$1" | grep -m1 -E "^$2[[:space:]]*=" \
    | sed 's/[[:space:]][[:space:]]*#.*$//' \
    | sed "s/^$2[[:space:]]*=[[:space:]]*//" | sed 's/^#.*$//' | tr -d '\r' \
    | sed 's/^[[:space:]]*//; s/[[:space:]]*$//' | sed 's/^"//; s/"$//' \
    | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

# ------------------------------------------------------------------------ per playbook
TOTAL_STEPS=0; TOTAL_TAGGED=0; TOTAL_WITNESS=0; TOTAL_CHECKS=0
for pb in $PLAYBOOKS; do
  [ -n "$pb" ] || continue
  if [ -n "$COUNTS_AT" ]; then
    # A PROBE THAT CANNOT MOVE SAYS SO. An unreadable blob would otherwise yield an empty body, and
    # every declaration below would parse to nothing — which reads as "declares no checks" and is
    # exactly the vacuous green this whole leg exists to refuse.
    body=$(GITSHOW "$COUNTS_AT:$pb")
    if [ -z "$body" ]; then
      fail 8 "the playbook does not resolve at the sha this count was asked for, so every declaration it carries would parse to nothing and the census would report a clean run over an unreadable file - sha and playbook follow: $COUNTS_AT and $pb"
      continue
    fi
  else
    body=$(tr -d '\r' < "$pb")
  fi

  # ---- 2: the FREEZE. `curated` is fork 4's only machine consequence.
  cur=$(declared_scalar "$body" curated)
  [ -n "$cur" ] || fail 2 "a playbook declares no curator, and the freeze is the only machine consequence a derive-then-freeze template has - a derived canon nobody ratified is a mirror of the corpus it came from, which is the one shape a template must not have; playbook: $pb"

  # ---- 3: the declared STEP SELECTOR and its shrink-only floor.
  sel=$(declared_scalar "$body" step_selector)
  # THROUGH THE SHARED PARSER, like every sibling key. This was the one fence key left on an ad-hoc
  # pipeline, and `tr -dc '0-9'` concatenated every digit in the trailing comment into the number:
  # `step_floor = 3     # at least 3, per section 5 and F2` parsed to 3352 and red a valid playbook
  # naming a floor its author never wrote, while `step_floor =    # TBD 5` parsed to 5 and bypassed
  # the no-floor refusal below with a number nobody declared.
  flo=$(declared_scalar "$body" step_floor)
  flo_bad=""
  case "$flo" in
    ''|*[!0-9]*) [ -z "$flo" ] || { fail 3 "a playbook declares a step floor that is not a number, and laundering it through a digit filter would invent one out of whatever prose follows - floor and playbook follow: [$flo] in $pb"; flo=""; flo_bad=1; } ;;
  esac
  if [ -z "$sel" ]; then
    fail 3 "a playbook declares no step selector, and a kit-fixed one either misses a playbook's steps entirely - reporting every step tagged over an empty set - or selects its prose; playbook: $pb"
    continue
  fi
  nsteps=$(printf '%s\n' "$body" | grep -cE "$sel" 2>/dev/null || true)
  TOTAL_STEPS=$((TOTAL_STEPS + nsteps))
  # THE REFUSAL IS CARRIED AS ITS OWN STATE, not by emptying the value. Round 5, LOW 10: a non-numeric
  # floor red twice - once correctly, and once more as "declares no floor", which is the wrong-cause
  # message the numeric refusal was written to replace. An author reading the second goes looking for
  # a line that is right there.
  if [ -z "$flo" ] && [ -z "$flo_bad" ]; then
    fail 3 "a playbook declares a step selector and no floor, so a selector that quietly matches nothing would report every step tagged over an empty selection; playbook: $pb"
  # AND THE COMPARISON IS GUARDED BY THE SAME STATE. Round 6, LOW 1: `flo` is emptied on a non-numeric
  # declaration and only the FIRST branch was guarded, so `[ "$nsteps" -lt "" ]` reached the shell and
  # printed `[: : integer expected` on stderr - which the driver captures with `2>&1` and folds into a
  # DoD refusal, so a raw interpreter error becomes part of an operator-facing message.
  elif [ -n "$flo_bad" ]; then :
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
  cov=$(declared_scalar "$body" coverage)
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

  # ---- 8: THE PER-PIECE RECORD READER. It CLASSIFIES and never grades: `stale` and `failed` are
  # ---- reported here with their counts and do NOT red, because only `--close` blocks on them. That
  # ---- split is what keeps this leg from redding the bar for the ordinary mid-fold state.
  # ----
  # ---- RUN-INDEPENDENT BY CONSTRUCTION. The scopes are derived from the RECORDS, never from a
  # ---- run-state file: this leg runs on the merge bar where no run exists, and a scope that needed
  # ---- one would be a scope the bar can never evaluate.
  gr=$(declared_scalar "$body" grain)
  rr=$(declared_scalar "$body" records)
  # THE DECLARED PER-PIECE LEGS. Round-1 blocker: this list had no reader anywhere in the kit while
  # three documents asserted the join, so `verified` meant "the hash matches and nobody wrote FAIL"
  # and a record carrying NO verdict at all counted as verified.
  if ! pchk=$(declared_list "$body" piece_checks); then
    fail 8 "a playbook opens a per-piece check list and does not close it on the same line, and this parser reads one line - an unarmed parse must red rather than return the declared null, because the declared null makes every piece verified on the one Definition-of-Done item that takes no override; playbook: $pb"
    # AND NO CENSUS IS PRINTED FOR IT. A machine count over a declaration nothing could read is a
    # number the caller would trust; the caller's own "no count line" refusal is the honest outcome.
    continue
  fi
  # MEDIUM 7 (round 3): the `none — <why>` escape its sibling got seventy-four lines below, in the
  # same fold. A playbook writing `none` declares no per-piece checks, and grading every piece
  # `unchecked` against the word `none` is the declared null misread as a check name.
  case "$pchk" in none|'none '*|none[!A-Za-z0-9-]*) pchk="" ;; esac
  if [ -n "$gr" ] && [ -z "$rr" ]; then
    fail 8 "a playbook declares a piece grain and no records root, so its pieces enumerate and none of them joins to evidence - every per-piece state would read as unrecorded and the count that means the build made what was asked would have nothing to compare; playbook: $pb"
  fi
  if [ -n "$gr" ] && [ -n "$rr" ]; then
    pieces=$(GITLS "$gr")
    npieces=$(printf '%s' "$pieces" | grep -c . || true)
    v=0; f=0; st_=0; un=0; uc=0; inscope=0
    for pc in $pieces; do
      [ -n "$pc" ] || continue
      rec=$(record_for "$rr" "$pc")
      if [ -z "$rec" ]; then
        # A piece with NO record belongs to no run, so it is outside `enumerate_run` entirely rather
        # than being an unrecorded member of it. Counting it there would make a run answerable for a
        # piece somebody else left in the tree.
        [ -n "$COUNTS_RUN" ] && continue
        un=$((un + 1)); inscope=$((inscope + 1)); continue
      fi
      # ENUMERATE_RUN, derived from the RECORD's own run identity and never from a run-state file:
      # this leg runs on the merge bar where no run exists.
      if [ -n "$COUNTS_RUN" ]; then
        [ "$(sed -n 's/^run: //p' "$rec" | head -1)" = "$COUNTS_RUN" ] || continue
      fi
      rh=$(sed -n 's/^hash: //p' "$rec" | head -1)
      ah=$(git hash-object "$pc" 2>/dev/null)
      if [ "$rh" != "$ah" ]; then st_=$((st_ + 1)); inscope=$((inscope + 1)); continue; fi
      # PROVENANCE and DONENESS are two questions. The hash join answers the first; the verdicts
      # answer the second, and `verified` requires BOTH — otherwise it is a semantic word for a
      # structural state, and the count that means "the build made what was asked" keys on it.
      #
      # THE JOIN IS AGAINST THE PLAYBOOK'S OWN `piece_checks`, and its absence is what the round-1
      # review called a blocker: testing for the ABSENCE of a FAIL row makes a record with no verdicts
      # at all `verified`, and `pieces-complete` then certifies pieces nothing ever checked.
      #
      # AN EXPLICIT `NA` SATISFIES A DECLARED LEG; an ABSENT row does not. That distinction is the
      # whole rule: `NA` is a judgement somebody recorded about this piece, absence is nothing at all,
      # and collapsing them would put the hole back one level down. A playbook declaring no per-piece
      # checks keeps the old meaning, which is the honest reading of declaring none.
      inscope=$((inscope + 1))
      if grep -q '^leg .* · verdict FAIL$' "$rec"; then f=$((f + 1)); continue; fi
      miss_=""
      for lg_ in $pchk; do
        grep -qxF -- "leg $lg_ · verdict PASS" "$rec" && continue
        grep -qxF -- "leg $lg_ · verdict NA" "$rec" && continue
        miss_="$miss_ $lg_"
      done
      if [ -n "$miss_" ]; then
        uc=$((uc + 1))
        [ -n "$COUNTS_FOR" ] || note "unchecked — $pc records no verdict for declared leg(s):$miss_ ($pb)"
      else
        v=$((v + 1))
      fi
    done
    # THE LIVENESS ASSERTION, first and unconditional. Every count below can be satisfied by a tree
    # with no pieces in it, and a reader that enumerates zero, joins zero and reports zero failures
    # is indistinguishable from a clean run.
    if [ -n "$COUNTS_FOR" ]; then
      # The machine line. DEAD PROBE is carried as a FIELD rather than as prose, so the caller can
      # distinguish "zero pieces" from "the grain resolved nothing" without parsing English.
      printf 'pieces=%s verified=%s failed=%s stale=%s unrecorded=%s unchecked=%s
' "$inscope" "$v" "$f" "$st_" "$un" "$uc"
    elif [ "${npieces:-0}" -eq 0 ]; then
      note "DEAD PROBE — the grain resolves no piece for $pb, so every per-piece count below is over an empty set and means nothing; reported and NOT redded here, because only --close blocks on it"
    else
      note "pieces $npieces · verified $v · failed $f · stale $st_ · unrecorded $un · unchecked $uc ($pb)"
    fi
    # THE SET RECORD, READ AND REPORTED. M4 (round-1 diff review): three documents said this leg read
    # the set record and nothing in here opened one — `record_for` and the orphan sweep both key on a
    # `piece:` line, which a set record does not carry, so both walked straight past it. The
    # set-scoped verdicts are the population a per-piece pass structurally cannot see, and on the
    # ATTENDED path, which never calls `--close`, they were graded by nothing at all.
    #
    # REPORTED, never redded, for check 8's stated reason: this block classifies and `--close` blocks.
    # The Skill says exactly that now, so the document and the code agree about which is which.
    if ! schk=$(declared_list "$body" set_checks); then
      fail 8 "a playbook opens a set-scoped check list and does not close it on the same line, and this parser reads one line - an unarmed parse must red rather than return the declared null; playbook: $pb"
      schk=""
    fi
    # M2 (round-2): the DECLARED-NULL escape its driver sibling had and this reader did not. A
    # playbook writing `none — <why>` declares no set checks, and reporting a missing set record for
    # it is a note the author cannot act on.
    #
    # HIGH 3 (round-3): matched as a WORD, not a prefix. `none*` swallowed every check whose name
    # merely starts with those letters — `nonempty-rows` read as "declares nothing", and the item
    # returned MET with no record, no verdict and no override entry.
    case "$schk" in none|'none '*|none[!A-Za-z0-9-]*) schk="" ;; esac
    if [ -n "$COUNTS_FOR" ] || [ -z "$(printf '%s' "$schk" | tr -d '[:space:]')" ]; then :; else
      # The run ids come from the PIECE records, so this reports on the runs that actually produced
      # something here rather than on a roster no merge-bar run can see.
      for rid_ in $(for r_ in $(GITLS "$rr/*.md"); do sed -n 's/^run: //p' "$r_" | head -1; done \
                    | grep . | LC_ALL=C sort -u); do
        srec_="$rr/set-$rid_.md"
        if [ -z "$(GITLS "$srec_")" ]; then
          note "no set record — run $rid_ produced pieces under $pb, which declares set-scoped checks, and nothing records whether they ran; only --close blocks on this"
          continue
        fi
        smiss_=""
        for sl_ in $schk; do
          grep -qxF -- "leg $sl_ · verdict PASS" "$srec_" && continue
          grep -qxF -- "leg $sl_ · verdict NA" "$srec_" && continue
          smiss_="$smiss_ $sl_"
        done
        [ -z "$smiss_" ] || note "set checks unrecorded — $srec_ carries no verdict for declared check(s):$smiss_"
        grep -q '^leg .* · verdict FAIL$' "$srec_" && note "set check FAILED — $srec_ records a failing set-scoped verdict, which is the check a monoculture passes every piece and fails here"
      done
    fi

    # ORPHAN RECORDS: a record whose piece is gone. The reverse direction, and without it a corpus
    # silently reports coverage it no longer has.
    [ -n "$COUNTS_FOR" ] || for rc_ in $(GITLS "$rr/*.md"); do
      [ -n "$rc_" ] || continue
      op=$(sed -n 's/^piece: //p' "$rc_" | head -1)
      [ -n "$op" ] || continue
      [ -e "$op" ] || note "orphan record — $rc_ describes $op, which is not in this tree; the record outlived its piece and is coverage nobody has"
    done
  fi
done  # ---- the population loop CLOSES HERE. It used to close ABOVE the per-piece
      # ---- reader while that reader stayed indented as its body, so the reader ran ONCE over
      # ---- the last iteration's leftover $pb and $body. Latent while the population was one.

# ---- 9: the DERIVED length budget and the drain, PRINTED. No number is written in this file.
[ -n "$COUNTS_FOR" ] || note "steps $TOTAL_STEPS · CHECK tags $TOTAL_CHECKS · of those carrying a witness $TOTAL_WITNESS"
[ -z "$COUNTS_FOR" ] && [ "$TOTAL_CHECKS" -gt 0 ] && note "witness drain $((TOTAL_WITNESS * 100 / TOTAL_CHECKS))% — reported, never redded, so a playbook adopts the witness a step at a time"

exit "$st"
