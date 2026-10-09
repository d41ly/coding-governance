#!/usr/bin/env bash
# check-verdict-epoch.sh — the kit version DATES the engine's verdicts, so it must move when they do.
#
#   bash <prefix>/memory-tree/check-verdict-epoch.sh [<base>]     # default base: GATE_PUSH_BASE, else the mainline merge-base
#
# Exit 0 = the constant is honest for this range, or the bump is owed at the lander · 1 = the engine
# moved and the constant did not, at the push boundary · 2 = misconfigured.
#
# THE BUMP IS MINTED BY THE LANDER, NOT MADE ON A BRANCH (TOOL-aMendedFleet-65 S7). gov's
# `push-main.sh` writes the next value into the prepared merge, so the obligation binds at the PUSH
# BOUNDARY: with `GATE_PUSH_BASE` set, which `.githooks/pre-push` exports for a default-branch push,
# or with an explicit <base>, every finding below fails as it always did. With neither, an engine
# move the constant does not date prints one `owed at the lander` line and exits 0 — so an
# off-boundary run does NOT check that a branch bumped, only that the gate is configured and has a
# base. The bump search reads a merge against its FIRST parent, which is how a minted merge dates
# the moves it carries.
#
# WHY. `hygiene-parity.test.sh` derives its baseline floor from the first commit introducing the
# CURRENT `KIT_MEMORY_TREE_VERSION`, on the stated ground that the constant marks when the verdicts
# last changed. Measured, that ground gave way: this repo changed check 5's selector, the §9 rev
# range and the index set across three commits while the constant sat at 1.5, so the floor pointed at
# a commit from before those changes and the parity harness accepted a baseline it could not legally
# compare against. The floor was not wrong about WHERE to look; the constant was wrong about WHEN.
#
# THE RULE IS TOPOLOGICAL, not an endpoint comparison. Let W be the NEWEST commit in `<base>..HEAD`
# that moves a behaviour-bearing line of the engine, and S the NEWEST commit in that range that
# actually CHANGES the value of `KIT_MEMORY_TREE_VERSION`. Then W must be an ancestor of, or equal
# to, S: the bump has to come at or after the last change it claims to date.
#
# WHY NOT THE ENDPOINTS. The first cut compared the constant at the two ends of the range, and that
# is satisfied by a bump ANYWHERE in it — so a bump in commit 2 excused every verdict change in
# commits 3..n. Reproduced: base(1.5) -> "bump + change"(1.6) -> "later change, no bump" read clean.
#
# WHY NOT PER-COMMIT. Measured on this repo's own history: 129 commits, 22 of which move a
# behaviour-bearing line of the engine or its delegates, against 7 bumps that actually happened. A
# per-commit rule would demand 22 — three times the churn — and a constant that increments on a fifth
# of all commits stops meaning "the verdict epoch" and starts meaning "someone edited the file".
# The topological rule asks for ONE bump per range, correctly placed. That is the same shape
# `skills/session-kickoff/manifest-check.sh` check 5 already uses for its `last-audit` re-stamp, and
# it is here because that rule is proven rather than because it is new.
#
# S IS VALIDATED, NOT MATCHED. A commit that touches the constant's LINE without changing its VALUE —
# a comment reflow, a marker edit — is not a bump. Each candidate is confirmed by parsing the value
# at the commit and at its parent, which is the same structural check manifest-check applies to its
# own stamp, and for the same reason: a decoy edit must not be able to launder a change.
#
# IT OVER-COUNTS, DELIBERATELY. A rename or a whitespace-only refactor changes no verdict and still
# demands a bump. That is the safe direction: the cost is three lines and a `--render`, and the
# alternative — deciding from a diff whether a verdict moved — is the judgement call that produced
# the stale constant in the first place. A line whose first non-space character is `#` cannot change
# what `sh` or `awk` does, so the exemption cannot hide a behaviour change.
set -u
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir=""
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "verdict-epoch: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

# THE ENGINE IS NOT ONE FILE. Checks 9 and 13-19 delegate to sibling Python modules, so 8 of the 19
# verdicts live outside the shell script — a change to `gotchas.py`'s classifier moves what the gate
# SAYS exactly as surely as a change to check 5's selector. The first cut diffed only the shell file
# and would have let all of them drift under a still constant.
#
# AND THE CHAIN IS TWO HOPS, not one. `corpus_ids.py` is listed, but it deliberately declares no
# grammar of its own (`corpus_ids.py:12`): `grammar()` returns `extract.grammar_for(root)`, so the
# regex that decides checks 13-16's verdicts lives one file further out, in the memory-recall kit.
# Measured on the commit that widened it: the session era went `\d+` to `\d+[a-z]*`, check 14's
# answer went 5 orphans to 9, and this gate printed `clean` with the constant untouched — the same
# defect TOOL-aBatchedTribunal-6o closed for the three modules below, one hop short. A kit an adopter
# has not installed is skipped by the `[ -f ]` guard, so listing it costs a non-adopter nothing.
#
# AND `merge-rows.py` IS IN THE SET, which is the same one-hop-short shape found a third time. The
# merge driver ships in this kit and the constant DATES the kit's verdicts; a redesign of what the
# driver does with three blobs moves a kit verdict exactly as surely as a change to check 5's
# selector, and nothing forced a bump. Measured before it was added: the driver's whole merge
# algorithm was replaced and this gate printed `clean` with the constant untouched. The driver is
# not a check — its "verdict" is the file it writes — and that is the reason it belongs here rather
# than an argument against it: an adopter reading `memory-tree@2.0` is being told which merge
# semantics their indexes were merged under.
#
# AND `tree_lib.py` (TOOL-aRepatriatedFork-9): the conf parser, the fence reader and the status
# vocabulary every delegate above reads moved there, so a change to any of them moves a verdict. It
# is spelled off ENGINE's own directory, because the carried-prefix ban takes no new literal.
#
# THE ENGINE IS THIS SCRIPT'S NEIGHBOUR, derived (TOOL-aRepatriatedFork-2 S2): both lines spelled
# gov's prefix, so at both adopters this gate exited 2 naming an engine that sat beside it. The
# memory-recall delegate is a SIBLING kit, found through the sibling-kit resolver, which reads the
# install receipt before it probes beside this kit and one level up (TOOL-aRepatriatedFork-46: the
# two probes used to type the kit's name after this kit's own base). A miss is SAID, never skipped.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
_kit=$(unset GIT_DIR GIT_WORK_TREE; git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null) || { echo "verdict-epoch: cannot derive this gate's own directory from '$_self_dir'"; exit 2; }
ENGINE="${_kit}check-memory-hygiene.sh"
_recall=""
if _ve_py=$(resolve_python 2>/dev/null); then
  _ve_mr=$(resolve_kit_dir "$_ve_py" memory-recall extract.py "$_self_dir" 2>/dev/null) && _recall="$_ve_mr/extract.py"
  [ -n "$_recall" ] || echo "verdict-epoch: note — no memory-recall kit's extract.py through the install receipt or beside this kit, so its lines are not in the scan set"
else
  echo "verdict-epoch: note — no usable python, so the memory-recall kit was not resolved and its lines are not in the scan set"
fi
DELEGATES="${_kit}tree_lib.py ${_kit}row_grammar.py ${_kit}gen_build_index.py ${_kit}corpus_ids.py ${_kit}gotchas.py $_recall ${_kit}merge-rows.py"
[ -f "$ENGINE" ] || { echo "verdict-epoch: $ENGINE is missing — this gate reads the engine's own source"; exit 2; }
SCAN="$ENGINE"
for _d in $DELEGATES; do [ -f "$_d" ] && SCAN="$SCAN $_d"; done

# The remote ladder (TOOL-dLadderedRemote-2), INLINED byte-identically from the canonical copy
# named on its marker line and gated by the resolve-python self-test.
# >>> remote_ladder_sh -- canonical copy: resolve-remote.sh in the gov lib dir (byte-identical; gated)
# resolve_remote_sh -> RR_REMOTE RR_BRANCH RR_OBSERVED RR_WHY, rc 0; rc 1 with RR_WHY on a refusal.
# The ladder, row for row, is resolve_remote.py in the gov lib dir: GOV_REMOTE, else the current
# branch remote unless it is ".", else the ONLY remote; several and none chosen, or a name that is
# no remote here, refuses naming GOV_REMOTE; no remote at all is RR_REMOTE="" and rc 0. RR_OBSERVED
# is what <remote>/HEAD names; RR_BRANCH is GOV_DEFAULT_BRANCH, else RR_OBSERVED. Fetches nothing.
# RR_GIT names the git command, so a caller holding a pinned wrapper function passes it.
resolve_remote_sh() {
  local _rr_git=${RR_GIT:-git} _rr_names _rr_n _rr_list _rr_cur _rr_where _rr_how=GOV_REMOTE _rr_head _rr_bad
  RR_REMOTE=${GOV_REMOTE:-}; RR_BRANCH=""; RR_OBSERVED=""; RR_WHY=""
  _rr_names=$("$_rr_git" remote 2>/dev/null) || _rr_names=""
  _rr_n=$(printf "%s" "$_rr_names" | grep -c . || true)
  _rr_list=$(printf "%s" "$_rr_names" | tr "\n" " ")
  [ -n "$_rr_list" ] || _rr_list=none
  # FULL refs, never `--short`: a tag or branch sharing the name makes the short form ambiguous.
  _rr_cur=$("$_rr_git" symbolic-ref --quiet HEAD 2>/dev/null) || _rr_cur=""
  case "$_rr_cur" in refs/heads/?*) _rr_cur=${_rr_cur#refs/heads/} ;; *) _rr_cur="" ;; esac
  if [ -z "$RR_REMOTE" ] && [ -n "$_rr_cur" ]; then
    RR_REMOTE=$("$_rr_git" config "branch.$_rr_cur.remote" 2>/dev/null) || RR_REMOTE=""
    _rr_how="branch.$_rr_cur.remote"
    [ "$RR_REMOTE" != . ] || RR_REMOTE=""
  fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -eq 1 ]; then RR_REMOTE=$_rr_names; fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -gt 1 ]; then
    _rr_where="a detached HEAD"; [ -z "$_rr_cur" ] || _rr_where="branch $_rr_cur"
    RR_WHY="cannot choose a remote: GOV_REMOTE is unset, $_rr_where has no configured remote, and this repository has $_rr_n remotes ($_rr_list). Name it: export GOV_REMOTE=<remote>."
    return 1
  fi
  # A name holding whitespace is no remote: `grep -F` would split it into several patterns.
  case "$RR_REMOTE" in *[[:space:]]*) _rr_bad=1 ;; *) _rr_bad=0 ;; esac
  if [ -n "$RR_REMOTE" ] && { [ "$_rr_bad" = 1 ] || ! printf "%s\n" "$_rr_names" | grep -qxF -- "$RR_REMOTE"; }; then
    RR_WHY="$_rr_how names $RR_REMOTE, which is no remote of this repository ($_rr_list). Name one that is: export GOV_REMOTE=<remote>."
    RR_REMOTE=""
    return 1
  fi
  if [ -n "$RR_REMOTE" ]; then
    _rr_head=$("$_rr_git" symbolic-ref --quiet "refs/remotes/$RR_REMOTE/HEAD" 2>/dev/null) || _rr_head=""
    case "$_rr_head" in "refs/remotes/$RR_REMOTE"/?*) RR_OBSERVED=${_rr_head#"refs/remotes/$RR_REMOTE"/} ;; esac
  fi
  RR_BRANCH=${GOV_DEFAULT_BRANCH:-$RR_OBSERVED}
  return 0
}
# <<< remote_ladder_sh
BASE="${1:-}"
BOUNDARY=1
# An ALL-ZERO GATE_PUSH_BASE reads as UNSET (TOOL-aMendedFleet-111 S3): the hook exports the remote's
# old sha, all zeros on a push that CREATES the default branch, and no commit carries that name.
case "${GATE_PUSH_BASE:-}" in ""|*[!0]*) ;; *) GATE_PUSH_BASE="" ;; esac
[ -z "$BASE" ] && [ -n "${GATE_PUSH_BASE:-}" ] && BASE=$GATE_PUSH_BASE
if [ -z "$BASE" ]; then
  BOUNDARY=0
  # The remote and its branch are the ladder's above (TOOL-dLadderedRemote-2), `main` when none is
  # named. A ladder refusal is this gate's failed exit, naming it: falling back to a local branch is
  # what the remote-first order exists to prevent.
  if ! resolve_remote_sh; then
    echo "verdict-epoch: FAILED — no mainline base to compare against: $RR_WHY"
    exit 1
  fi
  DEF="${RR_BRANCH:-main}"
  BASE=""
  [ -z "$RR_REMOTE" ] || BASE=$(git merge-base "$RR_REMOTE/$DEF" HEAD 2>/dev/null || true)
  [ -n "$BASE" ] || BASE=$(git merge-base "$DEF" HEAD 2>/dev/null || true)
fi
# No resolvable base — a shallow clone, a fresh init, a detached probe. SKIP LOUDLY: silence here
# would be indistinguishable from "the constant is fine", which is the failure this gate exists for.
if [ -z "$BASE" ]; then
  echo "verdict-epoch: FAILED — no mainline base to compare against, so this gate cannot judge"
  echo "verdict-epoch: anything. A shallow clone or a differently-named default branch does that."
  echo "verdict-epoch: Fetch full history (CI: fetch-depth: 0), or set GOV_DEFAULT_BRANCH."
  echo "verdict-epoch: This exits 1 on purpose: run-gates judges a leg by its exit code, so a"
  echo "verdict-epoch: zero-status skip would be indistinguishable from a pass, forever."
  exit 1
fi
git cat-file -e "$BASE^{commit}" 2>/dev/null || { echo "verdict-epoch: base '$BASE' is not a commit in this repo"; exit 2; }

# Behaviour-bearing added/removed lines in ONE commit. `-U0` so context lines cannot be mistaken for
# changes; the `+++`/`---` headers are dropped. A merge commit prints nothing here, which is right:
# a merge introduces no line its parents did not already carry.
behav_in() {  # $1=commit · $2=pathspec (default: the whole scan set) -> count
  git diff-tree -U0 --no-commit-id -r -p "$1" -- ${2:-$SCAN} 2>/dev/null \
    | grep -E '^[+-]' | grep -vE '^(\+\+\+|---)' | sed 's/^.//' \
    | grep -vE '^[[:space:]]*(#|$)' | grep -c . || true
}
# WHICH of the scanned files moved. The failure used to name only a sha, and the scan set is now four
# files across TWO kits: "$W moved 3 lines" leaves the reader to diff the commit themselves to learn
# whether the engine, a delegate or the shared grammar was what moved. One `behav_in` per scanned
# file, and only on the failure path, so the clean path costs nothing.
moved_files() {  # $1=commit -> space-separated paths
  local f out=""
  for f in $SCAN; do [ "$(behav_in "$1" "$f")" -gt 0 ] && out="$out $f"; done
  printf '%s' "${out# }"
}
verat() {  # $1=rev -> the constant's value at that rev ("" if absent/unparseable)
  git show "$1:$ENGINE" 2>/dev/null | sed -n 's/^KIT_MEMORY_TREE_VERSION=\([0-9.]*\).*/\1/p' | head -1
}

now=$(verat HEAD)
was=$(verat "$BASE")
[ -n "$now" ] || { echo "verdict-epoch: cannot read KIT_MEMORY_TREE_VERSION from $ENGINE at HEAD"; exit 2; }
# An UNREADABLE old constant is not "it changed". The comparison below only fires when `was` is
# non-empty, so a reader that stopped matching would silently excuse every future change — the
# fail-open direction, in the gate whose whole job is to notice a constant that stopped being true.
# `was` is legitimately empty only when the base PREDATES the constant, and git can be asked which.
if [ -z "$was" ] && git show "$BASE:$ENGINE" 2>/dev/null | grep -q 'KIT_MEMORY_TREE_VERSION'; then
  echo "verdict-epoch: FAILED — $ENGINE at $BASE carries KIT_MEMORY_TREE_VERSION but this gate could"
  echo "verdict-epoch: not parse it, so the comparison below would pass without comparing anything."
  echo "verdict-epoch: Fix the constant's format (want 'KIT_MEMORY_TREE_VERSION=<X.Y>') or the reader."
  exit 2
fi

# W — the NEWEST commit in the range that moves a behaviour-bearing line. Walked newest-first rather
# than taken from `rev-list -1`, because the newest commit TOUCHING the engine may have moved only
# comments, and a comment is not a verdict.
W=""; moved=0
while IFS= read -r c; do
  [ -n "$c" ] || continue
  n=$(behav_in "$c")
  if [ "$n" -gt 0 ]; then W="$c"; moved=$n; break; fi
done <<EOF
$(git rev-list "$BASE"..HEAD -- $SCAN 2>/dev/null)
EOF

if [ -z "$W" ]; then
  echo "verdict-epoch: clean — no behaviour-bearing engine line moved since ${BASE} (version $now; scanned $SCAN)"
  exit 0
fi

# A VENDORED ENGINE IS DATED BY GOV, NOT BY THE PULL'S COMMIT ORDER (TOOL-aClassedKnob-3). An adopter's
# pull may write gov's bytes in several commits, the constant first, and the rule below then reads
# gov's own bump as older than gov's own change. When the committed install receipt at HEAD records
# every scanned file with `oid` = its blob at HEAD = `gov_oid`, and the engine row's version is the
# constant at HEAD, these are gov's unmodified bytes at a vintage gov's lander dated, so the range has
# nothing of its own to date. A local edit moves a blob off the receipt and falls through to the rule.
# gov has no receipt, so gov's own verdict never takes this path.
# WHAT THIS DOES NOT CHECK: that the receipt is honest. A hand-edited row claiming gov's blob for a
# local edit passes here; the receipt is govkit's record and is graded there.
check_receipt_vintage() {  # -> 0 when the receipt at HEAD vouches for every scanned blob at version $now
  local py tree
  py=$(resolve_python 2>/dev/null) || return 1
  git cat-file -e "HEAD:.governance/install.json" 2>/dev/null || return 1
  tree=$(git ls-tree HEAD -- $SCAN 2>/dev/null) || return 1
  git show "HEAD:.governance/install.json" 2>/dev/null | "$py" -c '
import json, re, sys
scan, now, engine, tree = sys.argv[1].split(), sys.argv[2], sys.argv[3], sys.argv[4]
blobs = {}
for line in tree.splitlines():
    meta, _, path = line.partition("\t")
    blobs[path] = meta.split()[2]
rows = {r.get("path"): r for r in (json.load(sys.stdin).get("files") or []) if isinstance(r, dict)}
for f in scan:
    r = rows.get(f) or {}
    if not blobs.get(f) or r.get("oid") != blobs[f] or r.get("gov_oid") != blobs[f]:
        sys.exit(1)
m = re.match(r"KIT_MEMORY_TREE_VERSION=([0-9.]+)", str(rows[engine].get("version") or ""))
sys.exit(0 if m and m.group(1) == now else 1)
' "$SCAN" "$now" "$ENGINE" "$tree"
}
if check_receipt_vintage; then
  echo "verdict-epoch: clean — vendored at gov's memory-tree $now: every scanned file at HEAD is gov's own blob as .governance/install.json records it, so gov's landing dated them ($moved line(s) moved in $W)"
  exit 0
fi

# S — the NEWEST commit in the range that actually CHANGES the constant's value. Candidates come from
# a `-G` search: `-S` counts OCCURRENCES of a string, and `KIT_MEMORY_TREE_VERSION=` occurs exactly
# once before and once after a bump, so the count never moves and the bump is never reported —
# measured, the first cut found no bump at all. `-G` matches changed LINES, which is what a bump is;
# manifest-check.sh uses -G on its own stamp for exactly this reason. Each candidate is then
# VALIDATED against its parent: a commit that reflows the
# comment on that line, or re-types the same number, touches it without dating anything.
S=""
while IFS= read -r cand; do
  [ -n "$cand" ] || continue
  cur=$(verat "$cand")
  prev=$(verat "$cand^")
  if [ -n "$cur" ] && [ "$cur" != "$prev" ]; then S="$cand"; break; fi
done <<EOF
$(git log --format=%H --no-patch --diff-merges=first-parent -G'^KIT_MEMORY_TREE_VERSION=' "$BASE"..HEAD -- "$ENGINE" 2>/dev/null)
EOF

# OFF THE PUSH BOUNDARY a move the constant does not date is the lander's to mint, not a failure.
check_owed_at_lander() {
  [ "$BOUNDARY" = 1 ] && return 0
  echo "verdict-epoch: owed at the lander — $moved behaviour-bearing line(s) moved in $W and the version is still $now; push-main.sh mints it"
  exit 0
}

remedy() {
  echo "verdict-epoch: Bump it in ALL THREE places, which must move together, in a commit at or after"
  echo "verdict-epoch: ${W}:"
  echo "verdict-epoch:   $ENGINE (the constant AND the gov:kit marker on that same line)"
  echo "verdict-epoch:   ${_kit}HYGIENE.template.md (line 1)"
  echo "verdict-epoch:   memory/HYGIENE.md (line 1) — then: bash ${_kit}kit-dogfood-parity.test.sh --render"
  echo "verdict-epoch: Or re-land through push-main.sh, whose --prepare mints it into the prepared merge."
}

if [ -z "$S" ]; then
  check_owed_at_lander
  echo "verdict-epoch: FAILED — $moved behaviour-bearing line(s) of the engine moved in $W, and NO"
  echo "verdict-epoch: commit in ${BASE}..HEAD changes KIT_MEMORY_TREE_VERSION (still $now)."
  echo "verdict-epoch:   moved: $(moved_files "$W")"
  echo "verdict-epoch: The constant is what dates the engine's verdicts — hygiene-parity.test.sh"
  echo "verdict-epoch: derives its baseline floor from it — so leaving it makes that floor point at a"
  echo "verdict-epoch: commit from before this change."
  remedy
  exit 1
fi

if ! git merge-base --is-ancestor "$W" "$S" 2>/dev/null; then
  check_owed_at_lander
  echo "verdict-epoch: FAILED — the bump is OLDER than the change it claims to date."
  echo "verdict-epoch:   last behaviour-bearing engine change: $W ($moved line(s))"
  echo "verdict-epoch:   moved: $(moved_files "$W")"
  echo "verdict-epoch:   last KIT_MEMORY_TREE_VERSION change:  $S"
  echo "verdict-epoch: A bump anywhere in the range used to satisfy this gate, so one early bump"
  echo "verdict-epoch: excused every verdict change after it. The bump has to come at or after the"
  echo "verdict-epoch: last change, or the floor it feeds still points before that change."
  remedy
  exit 1
fi
echo "verdict-epoch: clean — $moved line(s) moved in $W and the version moved ${was:-<absent>} -> $now in $S"
