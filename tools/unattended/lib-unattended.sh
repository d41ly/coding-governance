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
# with. A closing review reproduced that with two controls (TOOL-dUnstalledConvoy-22).
#
# The lesson is not "be more careful". Two spellings of one rule is [[two-answers-to-one-question]],
# and the fix for it is one spelling, which is this file.

# --------------------------------------------------------------------------------- git, once
# Replace refs and graft advice are both OFF: a leg that reads history must see the history that is
# there, and a repo-local replace ref would silently rewrite what every predicate below answers.
GIT() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false "$@"; }

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
