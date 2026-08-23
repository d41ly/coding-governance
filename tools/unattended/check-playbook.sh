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
# ---- THE CONF IS SOURCED, not re-parsed. Round 7's blocker 3: this file was the only reader in the
# ---- kit resolving a conf key with `sed | tr -d '"' | head -1` while `unattended.sh`, the sibling
# ---- leg and the adopter all `. "$CONF"`. `.unattended.conf` IS a shell file, so `BYPASS_BAN='x'`
# ---- kept its single quotes here and lost them everywhere else, a trailing comment survived here and
# ---- nowhere else, and `head -1` took the FIRST assignment where sourcing takes the last. Each of
# ---- those makes check 10 grep for a literal no record can contain WHILE STILL PRINTING that it read
# ---- the corpus - a guard that reports itself armed and is not. Two readers of one config, one of
# ---- them re-derived, is the same class check 28 exists to close for the parsers, one file over.
# ---- The subshell is the isolation: nothing the conf sets reaches this leg's own state.
# ---- AND THE READ'S OWN LIVENESS IS A VERDICT. Round 8's blocker 1: the first cut discarded the
# ---- subshell's status, so "the key is undeclared" and "the conf aborted before the assignment" were
# ---- the same empty string - and the leg then printed `bypass scan SKIPPED - no BYPASS_BAN declared`,
# ---- which is FALSE. Four of five abort shapes reach it (`exit 0`, `return 0`, a syntax error above
# ---- the assignment, an unbound reference under the inherited `set -u`), each a ONE-LINE append to a
# ---- tracked file the graded run can commit itself. rc 9 is that state and the caller reds on it.
# ---- `unset -v` first, because the subshell inherits the process environment and an EXPORTED
# ---- variable of the same name would otherwise answer for a key the conf never declares.
_conf_key() { # KEY -> the value this file's three siblings would see; rc 9 = the conf did not source
  [ -f .unattended.conf ] || return 0
  # A SENTINEL THE SOURCE HAS TO SURVIVE TO PRINT. `. file || exit 9` does NOT catch an `exit` inside
  # the sourced file - that ends the subshell at the status the FILE chose, which is exactly the
  # `exit 0` shape, and the caller then reads an empty answer as "the key is undeclared". The `OK`
  # prefix is emitted after the source and nowhere else, so its absence is the abort.
  # THE SENTINEL CARRIES SET-NESS, not just the value. Round 9's high 3: the text cross-check below
  # read "the file spells the key and the sourced view is empty" as "the source never got there" -
  # which is false for a key DELIBERATELY declared empty, and this kit's own shipped example declares
  # eleven of them that way with comments reading "BLANK turns that check off". The shell already
  # knows the difference; `${VAR+SET}` is it, and reading the file's text to guess at it was the
  # mistake. \001 separates the marker from the value because no conf value contains it.
  #
  # AND THE SOURCE'S EXIT STATUS IS NOT A VERDICT - round 9's medium 4. A conf whose last line is a
  # false `[ ... ]` or a `grep` that matched nothing returns non-zero having assigned everything
  # correctly, and `|| exit 9` refused it. The sentinel catches the shapes that matter: `exit` and an
  # unbound reference under `set -u` end the subshell before it is written, and a parse error or a
  # `return 0` above the assignment leave the marker absent while the file still spells the key.
  _CK_OUT=$( unset -v "$1" 2>/dev/null
             . ./.unattended.conf >/dev/null 2>&1
             eval "printf 'OK%s\001%s' \"\${$1+SET}\" \"\${$1:-}\"" )
  case "$_CK_OUT" in
    OK*) _CK_REST=${_CK_OUT#OK} ;;
    *) return 9 ;;
  esac
  _CK_SET=${_CK_REST%%$'\001'*}
  _CK_VAL=${_CK_REST#*$'\001'}
  # AND A CROSS-CHECK, which is never the answer and only ever a liveness verdict. `return 0` above an
  # assignment ends the SOURCE without ending the subshell, so the sentinel prints and the value is
  # still empty. If the file spells the key and the sourced view says nothing, the source did not
  # reach the assignment. This is the shape the round-7 gotcha prescribes for a second reader: keep it,
  # and red on disagreement rather than answering from it.
  if [ "$_CK_SET" != SET ] && grep -qE "^[[:space:]]*$1=" .unattended.conf; then return 9; fi
  printf '%s' "$_CK_VAL"
}
CONF_GLOB=$(_conf_key PLAYBOOK_GLOB); _ck_glob=$?; _ck=$_ck_glob
[ "$_ck" -eq 9 ] && fail 10 "the project conf could not be sourced, so every key this leg reads resolves to the empty string and the checks that depend on them announce a cause they never verified - an abort above an assignment in .unattended.conf disarms this leg while it prints that the key is undeclared"
# ---- BYPASS_BAN, the SECOND conf key this leg reads, and check 10 below is why. The driver refuses to
# ---- WRITE an evidence record naming the declared bypass flag; nothing read those records back, so a
# ---- flag that reached a tracked record by any other route was invisible after the fact. Check 11 in
# ---- the sibling leg covers run-state files and cannot cover these: it has no GITLS, no
# ---- declared_scalar and enumerates no playbooks, so the roots are unreachable from there. Measured
# ---- before this landed - all three are zero in that file and non-zero in this one, which is why the
# ---- scan is HERE, and why the alternative would have inlined a third parser copy past a gate that
# ---- compares exactly two.
CONF_BYPASS=$(_conf_key BYPASS_BAN); _ck=$?
CONF_BYPASS=${CONF_BYPASS:-}
# BOTH READS, not one. Round 9's low 6: this was assigned from the BYPASS_BAN read alone, so a
# glob read that failed while the flag read succeeded left the leg printing a refusal about a conf it
# then reported as sourced.
CONF_SOURCE_OK=1
[ "$_ck" -eq 9 ] && CONF_SOURCE_OK=0
[ "$_ck_glob" -eq 9 ] && CONF_SOURCE_OK=0
# The same refusal for the key check 10 actually reads. It is spelled twice rather than folded into
# the helper because `fail` must run in THIS shell, and the helper's answer is its stdout.
[ "$_ck" -eq 9 ] && fail 10 "the project conf could not be sourced, so the declared bypass flag resolves to the empty string and this leg would announce a skip it never verified - the corpus goes unread while the report says no flag is declared"
# ---- AND THE PARSE IS ARMED. No bypass flag carries whitespace or a `#`; a resolved value that does
# ---- is a reader that mis-parsed, and an unarmed predicate must RED rather than print a population
# ---- count over a literal nothing can match.
case "$CONF_BYPASS" in
  '') ;;
  *[[:space:]]*|*'#'*)
    fail 10 "the declared bypass flag resolves to a value carrying whitespace or a comment character, which no flag does - so this leg would grep the corpus for a literal no record can contain and then report that it read the corpus. Resolved value follows: [$CONF_BYPASS]" ;;
esac
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
$(git -c core.quotePath=false ls-files -- '*.md')
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
# ---- BYTE-FAITHFUL, AT THE SOURCE. Round 8's blocker 2: round 7 closed word-splitting and left
# ---- C-QUOTING. With the default `core.quotePath`, `git ls-files` emits a non-ASCII name as a
# ---- QUOTED, octal-escaped literal - so the reader gets a path that does not exist, the bypass grep
# ---- never opens that record, the tracked-but-absent refusal reds the merge bar on a legitimate
# ---- tree with a false cause, and the census silently grades the piece unrecorded. Record names
# ---- derive from piece paths, so any adopter with one non-Latin character in a deliverable reaches
# ---- all of it. `core.quotePath=false` alone still splits on a path containing a newline, which is
# ---- why `-z` is not optional and every consumer reads with `-d ''`.
GITLS() { git -c core.quotePath=false ls-files -z -- "$1" 2>/dev/null; }
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
  # NOT `for r in $(GITLS …)`: `git ls-files` leaves a space-containing path unquoted, so one record
  # becomes two names that do not exist. Round 7, high 1 - the class, not just the site that was filed.
  # PROCESS SUBSTITUTION, NOT A HEREDOC. `$(GITLS …)` inside a heredoc drops the NUL separators -
  # command substitution strips them, with a warning - so the whole stream arrives as one record. And
  # a PIPE would put this loop in a subshell, where every counter it increments dies at the `done`.
  # `< <(…)` is the one form that carries the bytes AND keeps the loop in this shell.
  while IFS= read -r -d '' r; do
    [ -n "$r" ] || continue
    [ -f "$r" ] || continue
    [ "$(sed -n 's/^piece: //p' "$r" | head -1)" = "$2" ] && { printf '%s' "$r"; return 0; }
  done < <(GITLS "$1/*.md")
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
TOTAL_STEPS=0
BYPASS_SEEN=0; BYPASS_ROOTS=0; BYPASS_ROOT_LIST="|"; TOTAL_TAGGED=0; TOTAL_WITNESS=0; TOTAL_CHECKS=0
# ---- THE SIXTH ENUMERATION, and round 8's high 2. The class fix converted five and the comment
# ---- claimed it covered "every place this leg walks git ls-files output" - this one was left,
# ---- and it is the worst of the six: a playbook whose path splits is never graded AT ALL, and
# ---- BYPASS_ROOTS then drops to zero, which disarms the liveness refusal added in the same fold.
while IFS= read -r pb; do
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
  # ---- 10: THE BYPASS FLAG, READ BACK OUT OF WHAT LANDED. The driver refuses to write one at record
  # ---- time and that guard is real; this is the second opinion over what is in the tree, which is the
  # ---- pair the charter asks for on a guarded surface.
  # ----
  # ---- IT NEEDS $rr AND NOTHING ELSE, which is why it is HERE. Round 7's blocker 2 found it nested
  # ---- inside the `grain && records` block below: `grain` and `records` are independent declared
  # ---- nulls, the only pairing refusal in this leg covers the REVERSE case, and a set-scoped playbook
  # ---- declaring records with no grain is exactly the shape `set_checks` is for. Blanking grain alone
  # ---- took the leg from RC=1 to RC=0 with the whole evidence corpus unread and a note saying zero.
  # ----
  # ---- THE POPULATION IS THE CENSUS OWN: same $rr from the same declared_scalar parse, same GITLS
  # ---- enumeration - not a second derivation that could disagree with the first.
  # ----
  # ---- WHAT THIS DOES NOT REACH: --record-set accepts a caller-supplied records root, so a record
  # ---- written outside every declared root is invisible here. That is the write-time guard's job and
  # ---- it holds there. Said plainly, because coverage a reader assumes is total is worse than
  # ---- coverage whose shape they know.
  if [ -n "$rr" ]; then
    # DISTINCT roots, not playbooks-that-declare-one. Round 8's low 3: two playbooks sharing a root
    # counted it twice, so the number beside the record count described a different population.
    case "$BYPASS_ROOT_LIST" in
      *"|$rr|"*) ;;
      *) BYPASS_ROOTS=$((BYPASS_ROOTS + 1)); BYPASS_ROOT_LIST="$BYPASS_ROOT_LIST$rr|" ;;
    esac
    if [ -n "$CONF_BYPASS" ]; then
      _seen_here=0
      # NOT `for bp_ in $(GITLS …)`. Round 7's high 1: `git ls-files` does not quote a path containing
      # a space, so one record split into two nonexistent names, `grep -qF` failed on both, and
      # BYPASS_SEEN incremented TWICE for the record it never opened - the liveness counter inflated by
      # exactly the file that carried the flag.
      while IFS= read -r -d '' bp_; do
        [ -n "$bp_" ] || continue
        if [ ! -f "$bp_" ]; then
          fail 10 "a tracked evidence record is not readable in this worktree, so the bypass scan cannot answer for it and counting it as read would inflate the number that proves the scan reached the corpus: $bp_"
          continue
        fi
        BYPASS_SEEN=$((BYPASS_SEEN + 1)); _seen_here=$((_seen_here + 1))
        grep -qF -- "$CONF_BYPASS" "$bp_" \
          && fail 10 "a tracked EVIDENCE RECORD names the declared bypass flag, and bypassing the lander discards the whole bar the run mandate leaned on - this is the record a reviewer reads to believe the run, so the flag being in it is the claim and the confession at once: $CONF_BYPASS in $bp_"
      done < <(GITLS "$rr/*.md")
      # PER ROOT, AND THE ZERO REDS HERE rather than on the aggregate. Round 8's high 1: the
      # repo-wide refusal could only fire in a tree where the kit's own shipped fixture root was
      # repointed at an empty directory, because `kit.toml` ships that fixture to every adopter and
      # check 1 reds on an empty playbook population - so `BYPASS_SEEN >= 3` was effectively
      # unconditional and the multi-root shape the comment described was unreachable. A declared root
      # that enumerates nothing is a scan that cannot move, and it is THIS root's fact.
      [ -n "$COUNTS_FOR" ] || note "bypass scan - $rr: $_seen_here tracked evidence record(s) read"
      # RED ONLY WHERE THE EMPTINESS IS NOT EXPLAINED BY "NOTHING HAS RUN YET". Round 9's medium 5:
      # the first cut fired on every freshly authored playbook, because a declared records root holds
      # nothing until a run writes into it and `BYPASS_BAN` is a required key in every adopter tree.
      # A grain that enumerates PIECES with a root that enumerates nothing is the real defect - work
      # exists and no evidence does - and that is the fixture-shaped case the arm actually tests.
      # LOW 8's wording too: `_seen_here` counts records this leg could READ, so a root whose records
      # are all unreadable reaches zero here having enumerated plenty. The message says which.
      if [ "$_seen_here" -eq 0 ] && [ -n "$gr" ] && [ -n "$(GITLS "$gr" | tr -d '\0')" ]; then
        fail 10 "a playbook enumerates pieces from its declared grain and NO readable record under its declared records root, with a bypass flag declared - so the readback is asserted over an empty population while the work it should cover exists: $rr in $pb"
      fi
    fi
  fi
  if [ -n "$gr" ] && [ -z "$rr" ]; then
    fail 8 "a playbook declares a piece grain and no records root, so its pieces enumerate and none of them joins to evidence - every per-piece state would read as unrecorded and the count that means the build made what was asked would have nothing to compare; playbook: $pb"
  fi
  if [ -n "$gr" ] && [ -n "$rr" ]; then
    # COUNTED BY THE LOOP, not by a second pass over a variable: `pieces=$(GITLS …)` would drop the
    # NUL separators the enumeration now carries, which is the same defect one level up.
    npieces=0
    v=0; f=0; st_=0; un=0; uc=0; inscope=0
  # PROCESS SUBSTITUTION, NOT A HEREDOC. `$(GITLS …)` inside a heredoc drops the NUL separators -
  # command substitution strips them, with a warning - so the whole stream arrives as one record. And
  # a PIPE would put this loop in a subshell, where every counter it increments dies at the `done`.
  # `< <(…)` is the one form that carries the bytes AND keeps the loop in this shell.
    while IFS= read -r -d '' pc; do
      [ -n "$pc" ] || continue
      npieces=$((npieces + 1))
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
    done < <(GITLS "$gr")
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
      # THE INNER ENUMERATION IS SPLIT-SAFE, the outer one does not need to be: run ids are the
      # payload here and no run id carries whitespace. Round 7, high 1 - the class over every place
      # this leg walks `git ls-files` output.
      _rids_=$(while IFS= read -r -d '' r_; do
        [ -n "$r_" ] || continue
        [ -f "$r_" ] || continue
        sed -n 's/^run: //p' "$r_" | head -1
      done < <(GITLS "$rr/*.md"))
      for rid_ in $(printf '%s
' "$_rids_" | grep . | LC_ALL=C sort -u); do
        srec_="$rr/set-$rid_.md"
        if [ -z "$(GITLS "$srec_" | tr -d '\0')" ]; then
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
    [ -n "$COUNTS_FOR" ] || while IFS= read -r -d '' rc_; do
      [ -n "$rc_" ] || continue
      [ -f "$rc_" ] || continue
      op=$(sed -n 's/^piece: //p' "$rc_" | head -1)
      [ -n "$op" ] || continue
      [ -e "$op" ] || note "orphan record — $rc_ describes $op, which is not in this tree; the record outlived its piece and is coverage nobody has"
    done < <(GITLS "$rr/*.md")
  fi
done <<PBLIST
$PLAYBOOKS
PBLIST
# ---- the population loop CLOSES HERE. It used to close ABOVE the per-piece
      # ---- reader while that reader stayed indented as its body, so the reader ran ONCE over
      # ---- the last iteration's leftover $pb and $body. Latent while the population was one.

# ---- 9: the DERIVED length budget and the drain, PRINTED. No number is written in this file.
[ -n "$COUNTS_FOR" ] || note "steps $TOTAL_STEPS · CHECK tags $TOTAL_CHECKS · of those carrying a witness $TOTAL_WITNESS"
# ---- THE BYPASS SCAN POPULATION, printed whether it found anything or not. A scan that reached zero
# ---- records and a scan that reached many and found nothing are the same silence, and the first is a
# ---- check that is not running.
[ -n "$COUNTS_FOR" ] || { if [ "$CONF_SOURCE_OK" != 1 ]; then
  note "bypass scan NOT RUN - the project conf did not source, so no declared value could be read; the refusal above is the verdict and this line is not a skip"
elif [ -z "$CONF_BYPASS" ]; then
  note "bypass scan SKIPPED - no BYPASS_BAN declared in .unattended.conf, so tracked evidence records are not read back for it"
else
  # THE TWO NUMBERS COUNT DIFFERENT POPULATIONS and the line now says so: records READ is the
  # per-root scan's total, roots DECLARED counts every distinct root including the ones no bypass
  # flag was declared for. Round 9's low 7 - reading them as a ratio was the invited mistake.
  note "bypass scan - $BYPASS_SEEN readable evidence record(s) read; $BYPASS_ROOTS distinct records root(s) declared across all playbooks"
fi; }
# ---- THE AGGREGATE IS A NOTE AND NOTHING ELSE. Its refusal moved per-root, where `_seen_here`
# ---- lives: a repo-wide zero can be held above zero by any one root, which is exactly how the first
# ---- cut became a check whose only reachable failing case was its own fixture.
[ -z "$COUNTS_FOR" ] && [ "$TOTAL_CHECKS" -gt 0 ] && note "witness drain $((TOTAL_WITNESS * 100 / TOTAL_CHECKS))% — reported, never redded, so a playbook adopts the witness a step at a time"

exit "$st"
