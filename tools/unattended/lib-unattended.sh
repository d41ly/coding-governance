# lib-unattended.sh — the predicates the driver and the gate leg must answer IDENTICALLY.
#
# SOURCED, never executed. It defines functions and nothing else: a file that did work on source
# would do it twice, once per caller, at whatever moment each happened to source it.
#
# WHY THIS FILE EXISTS. `unattended.sh` decides at declaration time whether two passes collide;
# `check-unattended.sh` decides after the fact whether a pass wrote what it declared. Both questions
# reduce to "has this pass committed yet", and both were written by hand, separately, in one sitting.
# The driver's copy carried a comment saying it read the question "the same way the leg reads it".
# It did not — it counted the run-state bookkeeping commit that carries a pass's own declaration, so
# every pass closed the instant it was declared and the disjointness proof found nobody to collide
# with. A closing review reproduced that with two controls: a pass whose ONLY commit was its own
# declaration read CLOSED to the driver and OPEN to the leg, and adding one product commit made both
# read closed. So the two spellings disagreed exactly on the case the disjointness proof depends on,
# and agreed everywhere else — which is why reading them side by side had not shown it.
# Pointer, not evidence: TOOL-dUnstalledConvoy-22.
#
# The lesson is not "be more careful". Two spellings of one rule is [[two-answers-to-one-question]],
# and the fix for it is one spelling, which is this file.

# --------------------------------------------------------------------------------- git, once
# Replace refs and graft advice are both OFF: a leg that reads history must see the history that is
# there, and a repo-local replace ref would silently rewrite what every predicate below answers.
# NAMED, so `GIT` and the bounded remote observation cannot drift apart. The observation cannot call
# GIT - it wraps git in `timeout` and needs the pins as argv - so the two spelled the same two
# options independently until one of them was named. The pins live HERE rather than in either
# caller, because the driver and the gate leg both source this file and a pin in one of them is a
# pin the other does not have.
GIT_PIN_REPLACE=core.useReplaceRefs=false
GIT_PIN_GRAFTADV=advice.graftFileDeprecated=false
GIT() { git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" "$@"; }

# ------------------------------------------------------------------------------- ids, anchored
# An id compared as a SUBSTRING joins `-1` to `-10`, and the joined pair is always the wrong one:
# `TOOL-x-1` is a prefix of every `TOOL-x-1N` a build with ten units will mint. The trailing class
# must exclude digits — that IS the `-1`/`-10` case — and excluding `-` keeps a hyphenated suffix
# from matching. `grep -w` is not enough: `-` is a word character to some greps and not others.
id_rows() {  # haystack-text · id  -> the lines carrying that id as a whole token
  printf '%s\n' "$1" | grep -E "(^|[^A-Za-z0-9-])$2([^A-Za-z0-9-]|\$)" || true
}
id_in() {    # haystack-text · id  -> 0 when the id appears as a whole token
  [ -n "$(id_rows "$1" "$2")" ]
}

# --------------------------------------------------------------------------- paths, normalised
# `memory`, `memory/` and `./memory` are ONE path. Compared as raw strings they are three, and a
# containment question answered on the strings reports two names of the same directory as disjoint —
# which turns every refusal built on it into a spelling test that one trailing slash passes.
normpath() {  # path -> the same path in one spelling
  _np=$1
  # REPEATED SLASHES COLLAPSE FIRST. Stripping the leading `./` before collapsing turns `.//x` into
  # the ABSOLUTE `/x` — a path in a different tree — and every containment answer after that is about
  # somewhere else. Found by the arm written for this function, which is the argument for writing it.
  while :; do case "$_np" in *//*) _np=$(printf '%s' "$_np" | sed 's|//*|/|g') ;; *) break ;; esac; done
  while :; do case "$_np" in ./?*) _np=${_np#./} ;; *) break ;; esac; done
  # THE DOT SEGMENTS, interior and trailing. `a/./b`, `a/b/.` and `a/b/./` all name what `a/b` names,
  # and every containment answer in this kit is built on this function — so a declaration spelled with
  # a dot segment was compared as a different string and the guards judged one path while the leg
  # graded another. Both spellings are broken by ONE missing step, which is why fixing only the
  # interior one would have left the class open with an instance closed.
  while :; do case "$_np" in */./*) _np="${_np%%/./*}/${_np#*/./}" ;; *) break ;; esac; done
  while :; do case "$_np" in ?*/.) _np=${_np%/.} ;; *) break ;; esac; done
  while :; do case "$_np" in ?*/) _np=${_np%/} ;; *) break ;; esac; done
  printf '%s' "$_np"
}
# `covers a b` — b is a, or sits under it. DIRECTIONAL, and what a "may this pass write here"
# question wants. `overlaps` is what every DISJOINTNESS question wants, and disjointness is what the
# dispatch refusals are actually asking: testing one direction only refuses the narrow declarations
# and admits the one that claims everything, because the widest path is under nothing.
covers() {
  _ca=$(normpath "$1"); _cb=$(normpath "$2")
  case "$_cb" in "$_ca"|"$_ca"/*) return 0 ;; esac
  return 1
}
overlaps() { covers "$1" "$2" || covers "$2" "$1"; }
# The whole-repository spellings, which normalise to something no containment test can express: `.`
# covers everything and is under nothing, and an empty path is not a path. Named here so the driver
# and any later reader refuse the same set.
is_repo_root() {
  case "$(normpath "$1")" in ""|"."|"./") return 0 ;; esac
  return 1
}

# ------------------------------------------------------------- has this pass committed yet, once
# Prints the FIRST pass commit after <anchor> and returns 0; prints nothing and returns 1 while the
# pass is still open. Three callers need this and each spelled it separately before: the driver's
# condition 1, the driver's re-declaration rule, and the leg's write-set grading.
#
# A RUN-STATE BOOKKEEPING COMMIT IS NOT A PASS COMMIT, and the skip is the load-bearing half.
# `--dispatch` STAGES the run-state file, so the run commits that declaration itself — and that
# commit's subject names the unit, because it is about that unit. Counting it closes a pass before
# the pass has written a byte, and the whole disjointness proof then runs over an empty sibling set.
#
# The window is `<anchor>..HEAD` and the answer is the FIRST qualifying commit, never a later one: a
# pass's own review fold or spec bump lands after its group has ended and is not the commit that
# closed it.
#
# THE UPPER BOUND is optional and defaults to HEAD. A unit legitimately owns several dispatch rows at
# several anchors — M6 defines five pass kinds — and with an unbounded window row one is graded
# against row two's commit, which is another pass's work. The bound does not change what counts as a
# pass commit; it changes which commits are even offered. TOOL-dUnstalledConvoy-23 S3.
pass_commit() {  # anchor · unit · run-state-path · [upper-bound, default HEAD]
  _pa=$1; _pu=$2; _prel=$3; _pto=${4:-HEAD}
  GIT rev-parse --verify --quiet "$_pa^{commit}" >/dev/null 2>&1 || return 1
  for _pc in $(GIT log --reverse --format=%H "$_pa..$_pto" 2>/dev/null); do
    id_in "$(GIT log -1 --format=%s "$_pc" 2>/dev/null)" "$_pu" || continue
    _ptouch=$(GIT diff-tree --no-commit-id --name-only -r "$_pc" 2>/dev/null | grep -vxF -- "$_prel" || true)
    [ -n "$_ptouch" ] || continue
    printf '%s\n' "$_pc"
    return 0
  done
  return 1
}

# THE NEXT ANCHOR for a unit after <anchor>, or empty when this is the unit's last row. Chosen by
# ANCESTRY rather than by the order rows appear in the file: the record is append-only and a run may
# park rows in any order, so file order is not history order. The earliest strict descendant wins,
# which is the one that closes this row's window.
next_anchor() {  # anchor · newline-separated candidate anchors
  _na=$1; _nbest=""
  for _nc in $2; do
    [ -n "$_nc" ] || continue
    [ "$_nc" = "$_na" ] && continue
    GIT merge-base --is-ancestor "$_na" "$_nc" 2>/dev/null || continue
    if [ -z "$_nbest" ] || GIT merge-base --is-ancestor "$_nc" "$_nbest" 2>/dev/null; then
      _nbest=$_nc
    fi
  done
  printf '%s' "$_nbest"
}
# THE ROSTER A RUN ENTERED ITS LIVE PHASE WITH — the single answer to "what units did this run start
# with", called by BOTH the checker (check 24, which compares) and the driver (check 48, which
# decides whether an `add` row is late-but-true or a fabrication). TOOL-dUnstalledConvoy-33.
#
# It lived only in the checker, and the driver decided the same question a different way — "is the
# unit in the units region NOW" — which is a different question with a different answer. The two
# together were unsatisfiable: a run whose roster grew before anybody recorded it could never record
# it, because by then the spec existed and the region carried the id. That is the owner's first
# observation, builds refuse to rescope, living in the driver written to let them.
#
# CONTRACT. Prints the baseline units REGION, verbatim, and exits 0 ONLY when it derived a region
# carrying at least one id.
#
# THE REGION TEXT, NOT A LIST OF IDS, and the closing review's blocker is why. The first draft
# printed bare ids; check 24's second loop then asked `id_rows "$rs_was" "$rsid" | grep -q
# "| WONTDO |"`, which can never match a bare id — so its "was it ALREADY retired at the baseline"
# exemption went dead and every build carrying a WONTDO unit from before its run would have redded
# for a retirement nobody performed. The callers want membership and STATUS, and only the region
# carries both. Membership still works: `id_in` matches a whole token anywhere in the text. Exits 1 otherwise, with the reason as its ONLY output — one line, no prefix, so a caller
# can drop it straight into its own message. The reason goes to STDOUT and not stderr, so one
# capture gets either the ids or the reason and the exit code says which; a caller juggling two
# streams for one answer is a caller that will drop one. Empty is a FAILURE and not an empty success: an empty baseline
# makes every unit read as added, which is vacuously accusatory rather than vacuously true.
#
# THE BASELINE IS THE COMMIT THE RUN ENTERED ITS LIVE PHASE AT, never the pinned BASE. A run that
# classifies a unit MISSING and authors its spec is obeying the build method, and every such spec is
# absent at BASE — keying on BASE would red a run for following the method.
# The units region as it stood at a NAMED commit. A SEPARATE PREDICATE from `baseline_units`, not a
# parameterised one: the two answer different questions - "what roster did this run enter its live
# phase with" and "what roster did the owner authorize" - and one predicate serving callers whose
# edges disagree is the shape four adversarial rounds failed to make correct in this kit's dispatch
# grading. The blob read below is the shared half; the commit CHOICE is what differs.
#
# IT VALIDATES ITS COMMIT, and its sibling does not need to. `baseline_units` CHOOSES its commit by
# walking history, so it cannot be handed a bad one; this one is GIVEN one, and an EMPTY value does
# not fail the read - `GIT show ":<path>"` is INDEX syntax and SUCCEEDS, returning plausible bytes.
# A run-state file with an absent or truncated `base:` would therefore silently grade the working
# INDEX instead of the pinned BASE, and the caller's unreadable-baseline skip would never fire
# because the read worked. That is the same degeneration the driver's own `check_authorization`
# header records from an empty base turning a provenance test into a read of the git index.
pinned_units() {  # commit · build-README-path · [cutoff-date]
  _pu_c=$1; _pu_bre=$2; _pu_cut=${3:-}
  command -v region >/dev/null 2>&1 || {
    echo "pinned_units needs a region() in the calling shell and this one has none, so the units region would read as empty and be reported as an empty roster"
    return 1
  }
  case "$_pu_c" in
    [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]*) ;;
    *) echo "the pinned commit is absent or is not sha-shaped, and an empty value reads as INDEX syntax rather than failing, so the comparison would silently grade the working index: [$_pu_c]"
       return 1 ;;
  esac
  GIT cat-file -e "$_pu_c^{commit}" 2>/dev/null || {
    echo "the pinned commit does not resolve to a commit in this history: $_pu_c"
    return 1
  }
  _pu_blob=$(GIT show "$_pu_c:$_pu_bre" 2>/dev/null || true)
  _pu_date=$(GIT show -s --format=%cs "$_pu_c" 2>/dev/null || true)
  if [ -z "$_pu_blob" ]; then
    echo "no build README at the pinned commit, so there is no authorized roster to compare against"
    return 1
  fi
  if ! printf '%s\n' "$_pu_blob" | grep -qxF -- '<!-- gen:build-units -->'; then
    echo "the build README at the pinned commit carries no units region, so the comparison would be vacuous over an empty set"
    return 1
  fi
  if [ -n "$_pu_cut" ] && [ -n "$_pu_date" ] && ! printf '%s\n%s\n' "$_pu_cut" "$_pu_date" | sort -C; then
    echo "the pinned commit predates UNITS_REGION_CUTOFF, so its absent region is grandfathered rather than a defect"
    return 1
  fi
  if ! _pu_was=$(printf '%s\n' "$_pu_blob" | region - '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    echo "the build README at the pinned commit carries a units marker but not exactly one well-formed pair, so there is no single roster to compare"
    return 1
  fi
  # THE EMPTY-ROSTER REFUSAL, which the sibling also carries and for the same reason: `region` exits
  # 0 with empty stdout for a well-formed pair enclosing nothing, so a BASE README with an id-less
  # units region would otherwise return SUCCESS with an empty roster — and every caller's membership
  # test then answers "absent" for every unit in the build. Seven tracked build READMEs are in that
  # state today. Counting the two functions' refusal branches would NOT catch this: both have seven,
  # and the sets differ rather than the sizes.
  _pu_ids=$(printf '%s\n' "$_pu_was" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u)
  if [ -z "$_pu_ids" ]; then
    echo "the roster at the pinned commit names no unit, so every membership test against it answers absent and the comparison would be vacuous rather than clean"
    return 1
  fi
  printf '%s\n' "$_pu_was"
}

baseline_units() {  # run-state-path · build-README-path · [cutoff-date] · [fallback-commit]
  _bu_rel=$1; _bu_bre=$2; _bu_cut=${3:-}; _bu_fb=${4:-}
  # IT CALLS `region`, WHICH THIS LIBRARY DOES NOT DEFINE. Both current callers define their own —
  # two spellings, in the driver and in the checker, and the legs that compare them are the marker
  # contract's, which this build moved off and back onto the automatic bar. A third caller that
  # forgot would get `region: command not found` on stderr and an EMPTY region, which this function
  # would then report as an empty roster: a wrong answer wearing a legitimate refusal. Named and
  # checked rather than assumed, because a dependency a file does not state is one nobody maintains.
  command -v region >/dev/null 2>&1 || {
    echo "baseline_units needs a region() in the calling shell and this one has none, so the units region would read as empty and be reported as an empty roster"
    return 1
  }
  _bu_base=""
  for _bu_c in $(GIT log --reverse --format=%H -- "$_bu_rel" 2>/dev/null); do
    case "$(GIT show "$_bu_c:$_bu_rel" 2>/dev/null | grep -m1 '^phase:')" in
      *BUILDING*|*RUNNING*|*VERIFYING*|*LANDING*|*LANDED*) _bu_base="$_bu_c"; break ;;
    esac
  done
  # THE FALLBACK IS THE CALLER'S, passed in rather than assumed. The checker hands its pinned BASE
  # so a run-state file with no live-phase commit still gets compared; the driver hands nothing, so
  # the same case refuses an `add` rather than deciding on a baseline it did not derive.
  [ -n "$_bu_base" ] || _bu_base=$_bu_fb
  if [ -z "$_bu_base" ]; then
    echo "the run-state file has no commit carrying a live phase and no fallback was given, so there is no baseline commit"
    return 1
  fi
  _bu_blob=$(GIT show "$_bu_base:$_bu_bre" 2>/dev/null || true)
  _bu_date=$(GIT show -s --format=%cs "$_bu_base" 2>/dev/null || true)
  if [ -z "$_bu_blob" ]; then
    echo "no build README at the baseline commit, so there is no authorized roster to compare against"
    return 1
  fi
  if ! printf '%s\n' "$_bu_blob" | grep -qxF -- '<!-- gen:build-units -->'; then
    echo "the baseline build README carries no units region, so the comparison would be vacuous over an empty set"
    return 1
  fi
  if [ -n "$_bu_cut" ] && [ -n "$_bu_date" ] && ! printf '%s\n%s\n' "$_bu_cut" "$_bu_date" | sort -C; then
    echo "the baseline predates UNITS_REGION_CUTOFF, so its absent region is grandfathered rather than a defect"
    return 1
  fi
  if ! _bu_was=$(printf '%s\n' "$_bu_blob" | region - '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    echo "the baseline build README carries a units marker but not exactly one well-formed pair, so there is no single roster to compare"
    return 1
  fi
  # The ids are derived only to decide EMPTINESS. An empty baseline is not a comparison and is not
  # vacuously true either — it is vacuously accusatory, because every unit the build has would read
  # as added.
  _bu_ids=$(printf '%s\n' "$_bu_was" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u)
  if [ -z "$_bu_ids" ]; then
    echo "the baseline roster names no unit, so every unit this build has would read as added and the comparison would accuse rather than check"
    return 1
  fi
  printf '%s\n' "$_bu_was"
}
