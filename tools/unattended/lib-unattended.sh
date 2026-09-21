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
#
# WHAT IT HOLDS: `GIT` and its two pins; `resolve_sidecar_dir`, the one derivation of the sidecar
# root the driver and the resume tick both read; `read_bound_key`, the one reader of a bound conf
# key both of them call; `read_host_name`, `read_pid_image` and `check_pid_alive`, the one reading
# of "which node, which process" the lease writer and both pid probes share; the anchored id tests;
# path containment; and "has this pass committed yet". The same rule admits the resume tick as a
# third sourcer.

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
# NO MEMO LIVES HERE, and the attempt is recorded because it looked obviously right.
# TOOL-aQuenchedHarness-10 cached this wrapper on argv, having measured that 436 of the leg's
# 1008 git calls are byte-identical repeats. It bought almost nothing: about twenty call sites
# invoke `GIT` inside `$( )`, and whole functions — `pass_commit`, `next_anchor`,
# `baseline_units`, `pinned_units` — are themselves called through command substitution, so
# every cache entry they filled died with the subshell that filled it. `rev-parse HEAD` still
# cost 39 spawns with the cache active.
#
# It also RED-ED check 28, which is the better reason it is gone: that check reads this
# definition LINE and requires the replace-ref pin on it, so a wrapper whose body carries the
# pin while its signature does not is exactly the unpinned-wrapper shape it exists to catch.
# The lesson the measurement actually supports: fill tables ONCE in the main shell before the
# loops, which is what `is_published` now does, rather than caching a wrapper that is mostly
# called from subshells.
GIT() { git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" "$@"; }

# THE SIDECAR ROOT, derived ONCE, HERE and nowhere else: `<git-dir>/unattended`, the WORKTREE's git
# dir — where `gate-logs/` already lives — never the common dir, because a run lives in one
# worktree and one sidecar per worktree is the whole point. Every reader of a sidecar file (the
# stall log at `--liveness`, the stop log at `--landed`, the resume log in the tick) calls this
# rather than respelling it; the driver and the tick both source this file, so a second spelling in
# either would be two answers to one question, and the kit gate counts the literal on exactly one
# code line across the three. An empty answer is a DEAD PROBE for the caller, never a path composed
# from an empty root — the caller refuses, it does not default. Moved from the driver, where unit 2
# defined it, by TOOL-aWokenSentinel-20; the body is unit 2's, unchanged.
resolve_sidecar_dir() { # -> <git-dir>/unattended, or nothing when the git dir cannot be derived
  local g; g=$(GIT rev-parse --git-dir 2>/dev/null) || g=""
  [ -n "$g" ] || return 1
  printf '%s/unattended\n' "$g"
}

# ------------------------------------------------------------------------------ bounds, once
# MOVED from the driver by TOOL-aWokenSentinel-5, body unchanged: the resume tick reads its two
# knobs through this function, and the driver its four, so it lives where both source it. THE
# CALLING-SHELL CONTRACT, on the function line and ASSERTED by its first line (TOOL-aWokenSentinel-18):
# `${!name}` reads the calling shell, and the NOTE interpolates `$CONF`, so a caller that named no
# conf would be handed a default announced with nowhere to change it — `Declare one in  to change
# it`, the empty path — or, under `set -u`, a shell error naming neither contract nor remedy. That
# is a refusal here, in the one function every caller shares, so the next script that sources this
# library from an unsourced shell refuses on its first run instead of taking the defaults silently.
# A BOUND KEY: DEFAULTED, VALIDATED, AND ANNOUNCED. TOOL-aBoundedCeiling-6, hoisted at its second
# instance by TOOL-aProbedUnit-3 — the charter's section 12 extracts the shared contract when the
# second caller arrives, and the third (`REVIEW_ROUNDS`) is a call, never a third `case`.
#
# A conf that declares nothing still gets a bound, because the population that produced the observed
# 3h19m hang is exactly the one that never edits this key. What it does NOT get is silence: the line
# below says which number is in force and where it came from, so a defaulted pin is never invisible.
#
# A malformed value is a REFUSAL rather than a silent fallback. "0" would mean no bound at all to
# `timeout`, so accepting junk and coercing it would unbound the one project whose declaration was
# wrong -- the failure landing on whoever tried hardest to configure it.
#
# <UNIT> is an argument because a caller may count rounds rather than seconds, and a refusal that
# says `seconds` about a round count is a false sentence. No `fail` branch here: this runs before
# `fail()` exists and refuses with exit 2, the misconfiguration code, exactly as the block it replaces.
read_bound_key() { # NAME · DEFAULT · UNIT · NOTE — the caller sourced the conf into THIS shell and named it in CONF
  [ -n "${CONF:-}" ] && [ -f "$CONF" ] || {
    echo "unattended: REFUSING - read_bound_key was called with CONF unset or naming no file, so its NOTE could name nowhere to declare the key and a default would be taken from nowhere; set CONF to the sourced conf before the call" >&2
    exit 2; }
  local _bk_name="$1" _bk_default="$2" _bk_unit="$3" _bk_note="$4" _bk_val
  _bk_val="${!_bk_name:-}"
  case "$_bk_val" in
    "") printf -v "$_bk_name" '%s' "$_bk_default"
        echo "unattended: NOTE - this project declares no $_bk_name, so $_bk_note. Declare one in $CONF to change it." >&2 ;;
    *[!0-9]*|0)
        echo "unattended: REFUSING - $_bk_name is declared as '$_bk_val', which is not a positive integer of $_bk_unit. A bound that cannot be parsed is a bound nobody set, and 0 means no bound at all." >&2
        exit 2 ;;
  esac
}

# --------------------------------------------------------------------------- processes, once
# THE LEASE NAMES A PROCESS, NOT A NUMBER (TOOL-aWokenSentinel-5, folding the closing review's id 2).
# A pid alone proves that SOME process holds the number: a reboot mid-run — a recorded event on
# this fleet — recycles it to whatever the owner starts next, and a run branch checked out on a
# second node carries the first node's pid into the second's process table. So the lease records
# the node and the image beside the pid, and the aliveness probe matches all it was given. Three
# functions, in the library because the driver WRITES the facts and the resume tick READS the
# launched pid back through the same probe; a spelling in each would be two answers to one question.

# THE NODE, one spelling: `COMPUTERNAME` where Windows sets it, `hostname` elsewhere, LOWERCASED
# because the two disagree on case for one machine (measured on node `a`, 2026-09-21: `COMPUTERNAME`
# upper, `hostname` lower). Empty when neither answers; the caller records `absent` for that.
read_host_name() { # -> the node's name, lowercased, or nothing
  local h="${COMPUTERNAME:-}"
  [ -n "$h" ] || h=$(hostname 2>/dev/null) || h=""
  [ -n "$h" ] || return 1
  printf '%s\n' "$h" | tr '[:upper:]' '[:lower:]'
}

# THE IMAGE HOLDING A PID. Prints the image name and returns 0 when a process holds the pid; 1 when
# none does; 2 when the probe could not look — an absent or non-numeric pid, a missing tool, a tool
# that exited non-zero — because a tool that answered nothing is not a `no`. Under MSYS the probe is
# `tasklist` and its OUTPUT decides: MEASURED on node `a`, 2026-09-16, it exits 0 for a live pid AND
# for a dead one (printing `INFO: No tasks are running`), so the exit code decides nothing; and
# `kill -0` on a live Windows pid reports `No such process` there, so the POSIX arm alone would read
# every live run on this fleet as dead. The row is `<image> <pid> <session> <session#> <mem>`, and
# the image is every field BEFORE the one equal to the pid, so an image with a space survives.
# Elsewhere `kill -0` decides existence and `ps -o comm=` names the image, UNVERIFIED (no registered
# node is POSIX).
read_pid_image() { # pid -> image on stdout; 0 held · 1 no such process · 2 the probe answered nothing
  local pid="$1" out img
  case "$pid" in ""|absent|*[!0-9]*) return 2 ;; esac
  case "$(uname -s 2>/dev/null)" in
    MINGW*|MSYS*|CYGWIN*)
      command -v tasklist >/dev/null 2>&1 || return 2
      out=$(tasklist //FI "PID eq $pid" //NH 2>/dev/null) || return 2
      img=$(printf '%s\n' "$out" | tr -s '\r\t ' '   ' | awk -v p="$pid" '{ for (i = 2; i <= NF; i++) if ($i == p) { s = $1; for (j = 2; j < i; j++) s = s " " $j; print s; exit } }')
      [ -n "$img" ] || return 1
      printf '%s\n' "$img" ;;
    *)
      kill -0 "$pid" 2>/dev/null || return 1
      img=$(ps -o comm= -p "$pid" 2>/dev/null | sed 's/^ *//; s/ *$//'); printf '%s\n' "${img:-unknown}" ;;
  esac
}

# DOES THE RECORDED PID EXIST, AND IS IT THE RECORDED PROCESS. `yes`, `no` or `unknown`: `unknown`
# when the probe could not look; `no` when nothing holds the pid, OR when something does and the
# recorded image does not match it — the recycled-pid case, and a tree kill aimed there lands on the
# owner's new interactive session, an IDE, or `explorer.exe` and every child. An image of `absent`
# or none at all matches anything: a lease written before the image was recorded, or by a harness
# whose pid the probe could not see, keeps the pid-only reading it always had, and the header says
# so rather than pretending that lease is guarded. Existence is not progress: a hung process is `yes`.
# MOVED from the driver by TOOL-aWokenSentinel-5's fold of the closing review; the pid half is unit
# 2's, unchanged in its verdicts.
check_pid_alive() { # pid · [image] -> yes | no | unknown
  local img rc
  img=$(read_pid_image "$1"); rc=$?
  case "$rc" in 2) echo unknown; return 0 ;; 1) echo no; return 0 ;; esac
  case "${2:-}" in ""|absent|"$img") echo yes ;; *) echo no ;; esac
}

# ------------------------------------------------------------------------------- ids, anchored
# An id compared as a SUBSTRING joins `-1` to `-10`, and the joined pair is always the wrong one:
# `TOOL-x-1` is a prefix of every `TOOL-x-1N` a build with ten units will mint. The trailing class
# must exclude digits — that IS the `-1`/`-10` case — and excluding `-` keeps a hyphenated suffix
# from matching. `grep -w` is not enough: `-` is a word character to some greps and not others.
id_rows() {  # haystack-text · id  -> the lines carrying that id as a whole token
  printf '%s\n' "$1" | grep -E "(^|[^A-Za-z0-9-])$2([^A-Za-z0-9-]|\$)" || true
}
# PURE BASH, AND THIS ONE IS THE HOT PATH. `id_rows` forks a subshell and spawns a `grep` per
# call, and `pass_commit` calls this once per commit in its window -- 1528 calls in one run of
# `check-unattended.sh`, measured on node `a` 2026-09-07, which was the largest single spawn
# population left in the leg after the `git log -1` removal above it.
#
# THE PATTERN IS `id_rows`'S, and the two are EQUIVALENT on a multi-line haystack even though
# grep anchors per LINE and bash anchors per STRING: a newline is itself a member of the
# negated class each anchor alternates with, so every position where grep's `^` or `$` would
# match is a position where the character-class branch matches instead. That is the kind of
# claim that is obviously true and occasionally false, so it was checked differentially over
# seventeen cases -- both anchors, both multi-line edges, the `-1`/`-10` trap and the
# hyphenated suffix -- before this landed, and the leg's whole stdout is byte-identical
# across the change. TOOL-aQuenchedHarness-7.
#
# `id_rows` KEEPS its grep: it returns the matching LINES, which is a different job, and it is
# not called per commit.
id_in() {    # haystack-text · id  -> 0 when the id appears as a whole token
  [[ $1 =~ (^|[^A-Za-z0-9-])"$2"([^A-Za-z0-9-]|$) ]]
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

# --------------------------------------------------- the paths a unit's brief rows name, once
# Prints, one per line and normalised, every path a ` brief · item <unit> · reason ` row names in
# the run-state file AS IT STANDS AT <commit>. Two consumers, one parser: `pass_commit` subtracts
# this set before it calls a commit a pass commit, and check 23 subtracts the same set before it
# grades what that commit carried. When the exclusion lived in check 23 alone, a `{run-state,
# brief}` bookkeeping commit naming the unit — the ordinary shape, since `--brief` requires the
# brief TRACKED and stages the run-state file beside it — was SELECTED as the pass commit, graded
# clean once the brief was forgiven, and the pass's real commit was never read. The closing diff
# review of aRatifiedRulings, finding 7. Only the leg was fooled: the driver's condition 1 also
# requires an `overlaps` hit against the declared set before it closes a pass, and a brief overlaps
# nothing an ordinary pass declares.
#
# THE TREE AT THE COMMIT, never the working copy: a row appended after the commit is outside it by
# construction, which is what keeps a post-hoc `--brief` from excusing a stray write. Selected on
# the whole field with both separators, so `-1` is not a prefix of `-10`; parsed with
# `check-brief-recorded.sh`'s own expansions, so a grammar change breaks every reader the same way.
# The blob lands in a VARIABLE and the loop reads the variable through a heredoc: a substitution in
# the heredoc body is the class `pass_commit` deadlocked on.
read_brief_paths() {  # commit · unit · run-state-path
  _rb_run=$(GIT show "$1:$3" 2>/dev/null || true)
  while IFS= read -r _rb_r; do
    case "$_rb_r" in *" brief · item $2 · reason "*) ;; *) continue ;; esac
    _rb_r=${_rb_r#* · reason }; _rb_r=${_rb_r#* }
    normpath "$_rb_r"; printf '\n'
  done <<RBP
$_rb_run
RBP
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
# THE BRIEF `--brief` STAGED IS THE SAME KIND OF BOOKKEEPING: a commit whose touch set minus the
# run-state file minus the paths its brief rows name is EMPTY moved nothing the pass wrote, and the
# walk continues to the commit that did (`read_brief_paths` above).
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
  # THE SUBJECT COMES OUT OF THE SAME WALK AS THE SHA. It used to cost a `git log -1` per
  # commit in the window, on every call, and this function is called once per (anchor, unit)
  # pair -- so the same commits were re-read once per pair. Profiled on node `a` 2026-09-07
  # over a full run of `bash tools/unattended/check-unattended.sh`: 1528 of that run's 2513
  # git spawns were this one line, against 31 for the `--follow` walk everyone assumes is the
  # expensive one. `%H%x09%s` gets both out of one walk. TOOL-aQuenchedHarness-7.
  #
  # A FILE, NEVER A PIPE AND NO LONGER A HEREDOC. The heredoc was here for a real reason and the
  # reason still stands: a piped `while` runs in a subshell and this loop RETURNS from the function,
  # so the `return 0` below would exit the subshell and the function would fall through. What the
  # heredoc solved in one direction it broke in the other, because its body was a COMMAND
  # SUBSTITUTION: `$( )` reads until EOF, EOF arrives when the LAST inherited write end closes, and
  # `GIT` is a shell FUNCTION — so the substitution forks a subshell which forks `git`, and the
  # reader waits on a grandchild's write end. On 2026-09-10 that never closed: the `unattended kit
  # gate` leg sat at zero CPU for 63 minutes, with the forked subshell holding both ends of its own
  # pipe on fd 3 and fd 4 and no descendant alive, until an operator killed it.
  #
  # The walk therefore runs in the CURRENT shell with its stdout redirected to a scratch file, and
  # the loop reads that file by redirect. No pipe exists, so no EOF has to arrive; a redirect from a
  # file creates no subshell, so `return 0` still returns from `pass_commit`. Both properties at
  # once, which is what the heredoc could not do.
  # `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` is the class; the `shell hygiene (a loop
  # fed by a command substitution)` merge-bar leg now refuses it repo-wide. TOOL-aLeakedHandle-1.
  #
  # A SCRATCH FILE THAT CANNOT BE CREATED IS A NAMED REFUSAL, not a fall-through to `return 1`.
  # `return 1` already MEANS "this pass has not committed yet", so answering a broken TMPDIR with it
  # would report every open pass as open forever and read as a correct answer. Both callers spell
  # `$(pass_commit … || true)`, so rc 2 reaches them as the same empty answer rc 1 does — the
  # difference is the stderr line, which is the only thing that makes a broken TMPDIR visible.
  _pf=$(mktemp) || { printf 'lib-unattended: pass_commit cannot create a scratch file, so it cannot say whether this pass committed\n' >&2; return 2; }
  GIT log --reverse --format="%H%x09%s" "$_pa..$_pto" >"$_pf" 2>/dev/null || :
  # It reads LINES rather than word-splitting because a subject holds spaces, and the possibly-empty
  # field is LAST for the reason memory/gotchas/empty-field-collapses-unless-it-is-last.md states.
  while IFS=$'\t' read -r _pc _psub; do
    [ -n "$_pc" ] || continue
    id_in "$_psub" "$_pu" || continue
    _ptouch=$(GIT diff-tree --no-commit-id --name-only -r "$_pc" 2>/dev/null | grep -vxF -- "$_prel" || true)
    [ -n "$_ptouch" ] || continue
    # EXACT membership against the newline-wrapped set, deliberately not `covers`: a row naming a
    # directory must forgive nothing under it. Same test check 23 makes, on the same set.
    _pnl=$'\n'; _pbrief="$_pnl$(read_brief_paths "$_pc" "$_pu" "$_prel")$_pnl"
    _pleft=""
    for _pp in $_ptouch; do
      case "$_pbrief" in *"$_pnl$_pp$_pnl"*) ;; *) _pleft=1; break ;; esac
    done
    [ -n "$_pleft" ] || continue
    printf '%s\n' "$_pc"
    rm -f "$_pf"
    return 0
  done <"$_pf"
  rm -f "$_pf"
  return 1
}

# ------------------------------------------------------------- which commit BUILT this unit, once
# ONE PREDICATE, TWO WINDOWS. This is the whole build-commit definition and every caller passes its
# own window rather than its own copy. A second copy would be two answers to one question, and the
# copy would be the one that drifts.
#
# LIFTED OUT OF `check-pass-order.sh` BY TOOL-aHoistedPass-7, and the lift is the work rather than
# the bookkeeping. It lived there as `_find_build_commit`, INDENTED inside that leg's per-unit loop
# together with the only other function that file has, so neither existed until the block ran and no
# sibling could source the file and call either. The symbol was reusable and the SEAM was not, which
# a grep for the name cannot tell apart. Sourcing the file and invoking the name can, and that is the
# test this move owes.
#
# THE WINDOW ARGUMENTS ARE OPTIONAL AND DEFAULT TO THE IN-RANGE WALK — unbounded, `--reverse` —
# because that is the question every caller but one asks. Dropping them to fit a five-argument
# signature would have deleted the pre-anchor violation class rather than moved it.
#
# THE EXCLUSION IS THE BUILD'S WHOLE FOLDER PLUS THE GENERATED INDEXES AND THE SHARED RECORDS, and
# getting this wrong made a CONFORMING run unlandable, twice. It was `spec/` and `reviews/` alone,
# and a spec pass legitimately writes more than those two: the regenerated index, the build README,
# the run-state file and the month ledger all sit outside them. So a SPEC commit naming the unit id
# won the selection and its caller then graded ITS parent — where, correctly, no spec exists yet.
# `SHARED_RECORDS` was omitted after that and it is not a corner: template section 1 MANDATES a
# backlog row, so a conforming spec-first run writes `memory/backlog/<FAMILY>.md` in the same commit,
# which put the commit back outside the exclusion and redded the run that followed the method
# exactly. `GENERATED_INDEXES` arrives as `index:generator` pairs; only the index half is an excluded
# path, because a commit touching the GENERATOR is touching product code.
build_commit() {  # rev-range · unit-id · build-dir · generated-indexes · shared-records · [cap] · [order]
  _bc_range=$1; _bc_id=$2; _bc_dir=$3; _bc_gen=$4; _bc_shared=$5
  _bc_cap=${6:-}
  # `$#` AND NOT `${7:-...}`: the pre-anchor caller passes an EMPTY order deliberately, meaning
  # newest-first, and a `:-` default cannot tell that from an absent argument.
  if [ "$#" -ge 7 ]; then _bc_ord=$7; else _bc_ord=--reverse; fi
  _bc_ex=""
  for _bc_i in $_bc_gen; do
    _bc_p=${_bc_i%%:*}
    [ -n "$_bc_p" ] && _bc_ex="$_bc_ex -e ^$_bc_p"
  done
  for _bc_s in $_bc_shared; do
    [ -n "$_bc_s" ] && _bc_ex="$_bc_ex -e ^$_bc_s"
  done
  # THE CAP BOUNDS THE ENUMERATION, not only the loop body. `for _c in $(rev-list ...)` runs the
  # whole traversal in a command substitution BEFORE the first iteration, so a loop-only cap bounds
  # the VERDICT and not the WORK — the `bounded-through-a-pipe-is-unbounded` class. The pre-anchor
  # window is the entire history behind an anchor, so `--max-count` is what bounds it.
  #
  # THE TWO WINDOWS WALK IN OPPOSITE DIRECTIONS, and getting that wrong is what made the pre-anchor
  # probe unable to see its own target. The IN-RANGE walk wants the EARLIEST build commit, so it is
  # `--reverse`. The PRE-ANCHOR probe wants ANY violating commit behind the anchor, and the nearest
  # is both the likeliest and the one that must survive truncation — so it walks NEWEST-FIRST and
  # truncates the FAR end.
  #
  # WHAT WENT WRONG, because it is worth one reader's minute. `rev-list --reverse --max-count=N`
  # applies the count during traversal and reverses AFTER, so the anchor is the LAST element of the
  # window, not the first. The probe was written `--reverse` for both windows on the belief that it
  # yielded the commits nearest the anchor; it yields the farthest. So the one commit the probe
  # exists to reach was dropped by the cap whenever the history behind it was deeper — and the
  # truncation arm could not see that, because it used the record-only fixture, where the correct and
  # the broken behaviour give the same verdict.
  #
  # Truncation is therefore reported AFTER the walk, on the count actually emitted.
  #
  # `cap+1` FETCHED, `cap` GRADED, so truncation is EXACT. With `--max-count=$cap` a complete walk of
  # an exactly-cap-deep window is indistinguishable from a truncated one, and the caller reported
  # TRUNCATED for a probe that had in fact seen everything. Fetching one extra is the only way to
  # know there was more.
  # Does the caller carry a subject cache? Asked ONCE, outside the walk.
  if declare -p _SUBJ >/dev/null 2>&1; then _bc_cache=1; else _bc_cache=0; fi
  _bc_n=0; _bc_mc=""
  [ -n "$_bc_cap" ] && _bc_mc="--max-count=$((_bc_cap+1))"
  for _bc_c in $(GIT rev-list $_bc_ord $_bc_mc $_bc_range 2>/dev/null); do
    _bc_n=$((_bc_n+1))
    # the (cap+1)-th commit is the SENTINEL: proof that more exists, never graded.
    if [ -n "$_bc_cap" ] && [ "$_bc_n" -gt "$_bc_cap" ]; then printf 'TRUNCATED'; return 0; fi
    # FROM THE CALLER'S SUBJECT CACHE WHEN THERE IS ONE, and this is not an optimisation you may drop.
    # `check-pass-order.sh` builds `_SUBJ` in one `git log` over all of HEAD and asserts its size
    # against `rev-list --count`, then walks 10,811 commits through here. Reading a subject per commit
    # instead costs a `git log` AND a `printf|tr` on every one of them, and the leg's own ledger prices
    # the difference at 591 s cached against 3977-5401 s uncached — the second of which straddles its
    # own 5400 s ceiling, so the leg stops being able to answer at all.
    #
    # IT WAS ORPHANED BY THE LIFT THAT CREATED THIS FUNCTION. The cache and its reader were one
    # inline block; the reader moved here and the read did not come with it, so `_SUBJ` was still
    # BUILT and size-asserted by the caller and consulted by nothing. Caught at the push boundary by
    # a 6.7x leg-level regression, not by anything that reads the code.
    #
    # THE PROBE IS DECLARED-ONCE, not per commit: `declare -p` is a builtin but this loop runs tens of
    # thousands of times, and a caller that declares no `_SUBJ` must not error under `set -u`.
    if [ "$_bc_cache" = 1 ]; then _bc_subj=${_SUBJ[$_bc_c]-}; else _bc_subj=""; fi
    # A cached value is ALREADY tokenised and space-padded on both ends, so an empty read is a MISS
    # and nothing else — an empty subject caches as two spaces. A miss falls back to the pair of
    # processes the cache replaced rather than reading as "this commit does not name the id", which
    # would grade the unit unbuilt and report a clean bill.
    #
    # THE WHOLE-TOKEN MATCH is `memory/gotchas/id-matched-as-a-substring`: every id ending in a 1-up
    # sequence is a prefix of nine others, so an unanchored `TOOL-x-1` matches `TOOL-x-19`'s commit.
    [ -n "$_bc_subj" ] || _bc_subj=" $(GIT log -1 --format=%s "$_bc_c" 2>/dev/null | tr -c 'A-Za-z0-9-' ' ') "
    case "$_bc_subj" in *" $_bc_id "*) ;; *) continue ;; esac
    # Did it touch anything outside this build's own record surface?
    if GIT show --pretty=format: --name-only "$_bc_c" 2>/dev/null \
       | grep -v '^$' | grep -qv -e "^$_bc_dir/" $_bc_ex; then
      printf '%s' "$_bc_c"; return 0
    fi
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
