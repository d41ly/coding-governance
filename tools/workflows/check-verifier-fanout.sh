#!/usr/bin/env bash
# check-verifier-fanout.sh — the COMMITTED workflow harnesses obey the verify-stage TOTAL and the
# loop markers, rule 2 of the agent-cap hook until TOOL-dFairHearing-16 moved it to this kit's
# check-verifier-fanout.js beside this gate (the owner's NT-27). The ref-keyed-join rule, which this
# gate also ran through the hook's `scripts` selector since TOOL-dTieredTribunal-14 S3, runs from
# check-review-join.sh alone now, as the move says.
#
#   bash <prefix>/workflows/check-verifier-fanout.sh          # every workflow script git can see
#   bash <prefix>/workflows/check-verifier-fanout.sh <file>…  # explicit files (the self-test's fixtures)
#
# Exit 0 = clean · 1 = the rule is broken · 2 = misconfigured, or its check refused a harness.
#
# THIS GATE DOES NOT IMPLEMENT THE RULE. It runs check-verifier-fanout.js over each script, and that
# file reads `<prefix>/hooks/agent-cap.js`'s views through the hook's exports, so the rule's scanner is
# the hook's one scanner. A bash re-implementation of a node predicate is two answers to one
# question: they would not disagree loudly, they would drift the day either side is tightened, and
# the gate would then bless scripts the rule denies (or the reverse) with no signal at all.
#
# ONE RULE IS NATIVE, and the hook holds no copy of it: the SLOT COUNT (TOOL-dFairHearing-13). Every
# array literal whose opening line carries the lens-slots marker holds exactly LENS_SLOTS top-level
# elements, counted at the foot of this file. The literals are rendered from the review kit's lens
# catalogue, `lenses.toml`, and the renderer does not count, so this is the one answer: a sixth
# default row renders a sixth slot and reds here. Rule 2's own array-literal allowance still
# admits the receiver; it is not consulted for the count.
#
# ONE ENTRY POINT NOW. The hook was the primary one, at the inline `script` of an ad-hoc review, until
# NT-27 retired the rule there: an inline script is bounded by the harness's own concurrency settings,
# and this gate judges every harness that lands, the ones invoked by NAME included.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "verifier-fanout: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

# ---- THE POPULATION HAS NO PREFIX -- TOOL-aRepatriatedFork-4 ----------------------------------
# Every `*.js` git lists, then the `export const meta` marker below. The marker IS the selector,
# as it is in check-workflow-syntax.js, so a harness is judged wherever it lives -- both adopters
# keep theirs under `.claude/workflows/`, which a kit-prefix filter never reached, and each carried
# a hand-kept fork to compensate. The prefix TOOL-dRetiredFork-10 derived here was doing nothing
# the marker does not, except hiding those harnesses.
HERE="$(cd "$(dirname "$0")" && pwd)"

# ---- THE PREDICATE, PROBED -------------------------------------------------------------------
# Three rungs, and the third is not optional. Adopter nc keeps its hooks a directory up from its
# harnesses, which rung 2 reaches. adopter ic has no such directory AT ALL -- its only copy sits at
# `.claude/hooks/agent-cap.js` -- so a two-rung chain strands it, and that was found by testing the
# derivation against both trees rather than by reasoning about one.
#
# F1, ratified: rung 3 stays a literal. `.claude/hooks/` is the HARNESS's own convention, not an
# install prefix an adopter chooses, and this is the one place the unit does not practise what it
# enforces. Said here rather than left for a reader to notice.
#
# TOOL-aRepatriatedFork-46: rungs 1 and 2 are the sibling-kit resolver's. It reads the install
# receipt BEFORE it probes this kit's own directory and its parent, so a hooks kit an adopter homed
# under another name is found, and it names the kit by its home rather than as a literal segment.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
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
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
HOOK=""
_hk_py=$(resolve_python 2>/dev/null) || echo "verifier-fanout: no usable python, so the install receipt and the kit probes were NOT read; only the .claude/hooks/ rung was tried" >&2
if [ -n "$_hk_py" ] && _hk_dir=$(resolve_kit_dir "$_hk_py" hooks agent-cap.js "$HERE" 2>/dev/null); then
  # The resolver answers relative to the checkout holding THIS gate, which is not the caller's
  # `$ROOT` when the gate runs from another repo (closing review round 1 H1). Asked with an inherited
  # `GIT_DIR` unset (round 2 L1): with one exported, git answers `$HERE` itself and the path names nothing.
  HOOK="$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)/$_hk_dir/agent-cap.js"
elif [ -f "$ROOT/.claude/hooks/agent-cap.js" ]; then
  HOOK="$ROOT/.claude/hooks/agent-cap.js"
fi
[ -n "$HOOK" ] || { echo "verifier-fanout: no agent-cap.js through the install receipt, at $HERE/hooks/, $HERE/../hooks/ or $ROOT/.claude/hooks/ — this gate has no predicate to delegate to"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "verifier-fanout: node not found — the predicate is a node hook"; exit 2; }

# The gate and its fixtures are outside their own population: the test's RED fixtures spell the banned
# shape on purpose, and a fixture that lands in the repo would otherwise make the merge bar
# permanently red. (They live under `mktemp -d`, so this is belt-and-braces — the same shape
# check-review-join.sh carries for the same reason.)
SELF_EXCLUDE='(^|/)check-verifier-fanout\.(sh|js|test\.sh)$'
# BASENAME-anchored, because the gate is installed under whatever prefix an adopter picks: an
# exclusion spelled with a rooted literal would name a path that exists only here.

if [ "$#" -gt 0 ]; then
  FILES=$(printf '%s\n' "$@")
  EXPLICIT=1
else
  # tracked AND untracked-but-unignored, matching the other two JavaScript gates: a new harness is
  # judged the moment it exists, not the moment someone remembers to stage it.
  # A `*.template.js` is a RENDER SOURCE, not a harness (TOOL-aRepatriatedFork-7 S7): its concurrency
  # width is the `{{FANOUT_CAP}}` token, which no hook can resolve and no runtime ever sees. What runs is
  # its render, which IS in this population, and check-protocol-parity.test.sh pins the render to it.
  FILES=$(git ls-files --cached --others --exclude-standard -- '*.js' \
    | grep -vE "$SELF_EXCLUDE" | grep -vE '\.template\.js$' | LC_ALL=C sort -u || true)
  EXPLICIT=0
fi

# A workflow script IDENTIFIES ITSELF by exporting `meta` — the same marker check-workflow-syntax.js
# uses, so a gate/helper `.js` sitting in the same directory is not judged as a harness.
SCAN=""
while IFS= read -r f; do
  [ -n "$f" ] && [ -f "$f" ] || continue
  if [ "$EXPLICIT" = 1 ] || grep -qE '^[[:space:]]*export[[:space:]]+const[[:space:]]+meta[[:space:]]*=' "$f"; then
    SCAN="$SCAN$f
"
  fi
done <<<"$FILES"

if [ -z "$SCAN" ]; then
  if [ "$EXPLICIT" = 1 ]; then
    echo "verifier-fanout: none of the named files exist — nothing was scanned, which is not a pass"
  else
    echo "verifier-fanout: no workflow script (a *.js exporting meta) anywhere git lists, .claude/workflows/ included — the population is empty, which is not a pass"
  fi
  exit 1
fi

# THE RULE IS check-verifier-fanout.js BESIDE THIS GATE (TOOL-dFairHearing-16): the hook's rule 2,
# moved to the review kit by the owner's NT-27, run per harness with the hook resolved above as its
# `--hook`, whose views and MAX_VERIFIERS it reads. The hook's `scripts` selector, which this gate used
# to call, now refuses: once rules 2 and 5 left, the mode ran nothing and could never red. Rule 5 runs
# from check-review-join.sh alone. Its exit 1 is a finding, and its 2 a refusal that ends this gate at
# exit 2, as the slot count's does below (TOOL-dFairHearing-50 S8).
FANJS="$HERE/check-verifier-fanout.js"
[ -f "$FANJS" ] || { echo "verifier-fanout: no check-verifier-fanout.js beside this gate at $HERE — the rule lives there, so a gate without it must say so, not pass"; exit 2; }
st=0
n=0
while IFS= read -r f; do
  [ -n "$f" ] || continue
  n=$((n+1))
  out=$(node "$FANJS" --hook "$HOOK" "$f" 2>&1); _fr=$?
  case "$_fr" in
    0) ;;
    1)
      echo "verifier-fanout: FAILED — $f"
      printf '%s\n' "$out" | sed 's/^/    /'
      st=1 ;;
    *) echo "verifier-fanout: the rule could not run on $f — $out"; exit 2 ;;
  esac
done <<<"$SCAN"

# THE CLEAN LINE NAMES NO NUMBER (TOOL-dGroundRules-10). The verify total is the hook's MAX_VERIFIERS,
# which the hook names in every denial, and the agent limit is the policy kit's: a number printed here
# would be a third copy of either.
[ "$st" = 0 ] && echo "verifier-fanout: clean — $n workflow script(s) obey the hook's verify-stage rule"

# ---- THE SLOT COUNT (TOOL-dFairHearing-13; one predicate and one counter since TOOL-dFairHearing-23) ----
# Over the same population: every array literal opened on a marker line holds exactly the lens count.
# The marker lines are `render_lenses.py --markers`, the renderer's own anchored regex, so a comment
# that names gov:lens-slots is no marker here either, and a gov:lens-optins literal is outside the
# count (TOOL-dFairHearing-27 S1). check-verifier-fanout.js `--slots` counts each literal with `topLevelArgs`, rule 2's own counter, over the hook's literal-blanked view, so a comma in
# a string, parentheses or braces is no slot and a trailing comma no element, and it holds the number,
# its one home, and prints the verdict. With explicit files a harness carrying no marker is legal; in
# the whole-tree mode no marked literal anywhere is a failure, because a count over nothing grades
# nothing. The slot verdict prints on a line of its own, after the hook's clean line, which stays byte
# for byte.
RENDERER="$HERE/render_lenses.py"
# A predicate that did not run is a named exit 2, never an empty marker list (TOOL-dFairHearing-27 S23):
# no renderer beside the gate, no usable python, or `--markers` exiting non-zero, its python floor's
# refusal included, since it shares the renderer's.
[ -f "$RENDERER" ] || { echo "verifier-fanout: the marker predicate did not run (no render_lenses.py beside this gate at $HERE)"; exit 2; }
[ -n "$_hk_py" ] || { echo "verifier-fanout: the marker predicate did not run (no usable python)"; exit 2; }
locs=()
while IFS= read -r f; do
  [ -n "$f" ] || continue
  _ml=$("$_hk_py" "$RENDERER" --markers "$f" 2>&1) || { echo "verifier-fanout: the marker predicate did not run (render_lenses.py --markers $f exited $?: $_ml)"; exit 2; }
  # MSYS converts an absolute path only as a whole argument, so `<path>:<line>` reached node unconverted
  # and unreadable. `cygpath -m` spells it for node; a relative path needs no spawn, and where cygpath
  # is absent the path is already native (TOOL-dFairHearing-50 S5).
  case "$f" in /*) _nf=$(cygpath -m "$f" 2>/dev/null) || _nf=$f ;; *) _nf=$f ;; esac
  for _l in ${_ml//$'\r'/}; do locs+=("$_nf:$_l"); done
done <<<"$SCAN"
if [ "${#locs[@]}" -gt 0 ]; then
  slots=$(node "$FANJS" --hook "$HOOK" --slots "${locs[@]}" 2>&1); _sr=$?
  case "$_sr" in
    0) printf '%s\n' "$slots" ;;
    1) printf '%s\n' "$slots"; st=1 ;;
    *) echo "verifier-fanout: the slot count could not run — $slots"; exit 2 ;;
  esac
elif [ "$EXPLICIT" = 0 ]; then
  echo "verifier-fanout: no lens-slot literal (a line marked gov:lens-slots) in any workflow script — the slot count graded nothing, which is not a pass"
  st=1
fi
exit "$st"
