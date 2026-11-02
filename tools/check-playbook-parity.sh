#!/usr/bin/env bash
# check-playbook-parity.sh — the playbook's claims about THIS repo, machine-checked.
#
#   bash <prefix>/check-playbook-parity.sh
#
# Exit 0 = every claim holds · 1 = a claim disagrees with its source · 2 = the gate could not run.
#
# WHY. Every other unit of this build corrected a hand-kept claim that drifted from its source, and
# four of those defects were RECURRENCES of ones a previous build had already fixed. This gate holds
# the three classes that recurred:
#
#   S1 kit coverage      — every kit govkit's registry declares is named in a playbook file or waived.
#   S2 value parity      — a value the playbook STATES equals the source that OWNS it.
#   S4 section citations — no live file cites a charter section by number, which v4.0 has none of.
#
# THERE IS NO S3. It asserted the placeholder arithmetic a deploy-time catalogue stated, and v3.0
# deleted that catalogue along with the companion carrying it — the counts have no author left to
# disagree with. Said here rather than left as a gap in the numbering, because a reader who trusts
# a header enumerating a stage the script no longer runs believes the arithmetic is still checked.
#
# WHAT IT DOES NOT DO, said here rather than implied away: it holds STRUCTURAL claims only. A fluent
# paraphrase that is subtly wrong still passes. Checking prose for accuracy in general is undecidable
# and this gate does not pretend otherwise.
#
# THE KIT POPULATION IS DECLARED, NOT LISTED (TOOL-aRepatriatedFork-54). A kit is a directory govkit's
# registry names under its `{prefix}` token — an `[[entry]]` descriptor's head, or an `[[exempt]]`
# path that is itself a directory — and that holds a tracked file. A listing of the tool root was the
# old rule, and at a repo-root install it counted `.claude/`, `skills/` and every other top-level
# directory as an undocumented kit. What it does NOT grade: a kit directory the registry never
# declares. That omission is govkit selfcheck's to red, because it asserts the registry against the
# tracked surface; this gate trusts the declaration and an unresolvable registry exits 2.
#
# ANTI-VACUITY IS THE LOAD-BEARING CONSTRAINT. `memory/gotchas/vacuous-selector-empty-population.md`
# owns the failure this gate is most likely to have: a selector that matches nothing prints nothing,
# and nothing is exactly what a passing check prints. Three arms guard it:
#   1. every S2 pair must extract a NON-EMPTY value on BOTH sides, or it reds as unresolvable;
#   2. the S1 kit set must be non-empty AND contain the frozen sentinel `memory-tree`;
#   3. the sibling self-test proves each arm reds, by feeding it a synthetic violation.
set -u
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir=""   # before the cd: $0 may be relative
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "playbook-parity: not a git tree"; exit 2; }
cd "$ROOT" || exit 2
# THE TOOL ROOT, DERIVED (TOOL-aRepatriatedFork-29 S3): the directory this gate sits in, which is
# where the kits, their sources and this gate's waiver file live. Underivable is a refusal.
if ! SELF_PRE=$(unset GIT_DIR GIT_WORK_TREE; git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null); then
  echo "playbook-parity: cannot derive this gate's own directory from '$_self_dir' — REFUSING"
  exit 2
fi

# TOOL-aRepatriatedFork-46: the hook that OWNS the fan-out values is a SIBLING kit, resolved rather than
# typed after this gate's own prefix. The resolver reads the install receipt first, then probes beside
# this gate and one level up. A miss names no file that exists, so every row reading it refuses with
# "the owning source does not exist": the refusal this gate already makes, never a guessed prefix.
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
HK_DIR="<no hooks kit>"
PB_DIR="<no playbook-render kit>"
REGISTRY=""
if _pp_py=$(resolve_python 2>/dev/null); then
  HK_DIR=$(resolve_kit_dir "$_pp_py" hooks agent-cap.js "$_self_dir" 2>/dev/null) || HK_DIR="<no hooks kit>"
  # TOOL-aDistilledCharter-8: the renderer's TEMPLATE_MAJOR is a pair whose owner is the template.
  PB_DIR=$(resolve_kit_dir "$_pp_py" playbook render_playbook.py "$_self_dir" 2>/dev/null) || PB_DIR="<no playbook-render kit>"
  # The S1 population's source, through the same resolver (TOOL-aRepatriatedFork-54).
  REGISTRY=$(resolve_kit_dir "$_pp_py" govkit registry.toml "$_self_dir" 2>/dev/null) && REGISTRY="$REGISTRY/registry.toml"
fi
TEMPLATE=coding-governance-agents.template.md
# The charter converged to ONE file at v3.0, so the kit-coverage haystack is the charter PLUS the
# runbook, which is where the kit-adoption prose moved. TWO variables and a two-file precondition:
# with no precondition on the runbook, an absent one reds every kit with a wrong reason instead of
# exiting 2 with the right one.
RUNBOOK=WIRE-INTO-PROJECT.md
WAIVERS=${PLAYBOOK_KIT_WAIVERS:-${SELF_PRE}playbook-kit-waivers.txt}
SENTINEL=memory-tree

status=0
fail() { printf 'PLAYBOOK-PARITY check %s FAILED — %s\n' "$1" "$2"; status=1; }

for f in "$TEMPLATE" "$RUNBOOK"; do
  [ -f "$f" ] || { echo "playbook-parity: missing playbook file: $f"; exit 2; }
done

# ================================================================= S1 — kit coverage ============
# The kit set is DERIVED, never hand-listed: govkit's registry declares it and the tracked surface
# confirms each member (TOOL-aRepatriatedFork-54). check-install-prefix.sh and the codebase-map
# extractor still LIST the tool root, so the three derivations now differ: a listing of a root
# install is every top-level directory, which only this gate reads as a kit population, and R2
# observed neither of the other two red there. Unresolvable or unparseable is a refusal, never an
# empty population, because an empty one is what ARM 2 below reads as broken for the wrong reason.
if [ -z "$REGISTRY" ] || ! kits=$("$_pp_py" -c '
import subprocess, sys, tomllib
with open(sys.argv[1], "rb") as fh:
    reg = tomllib.load(fh)
pre = sys.argv[2]
tracked = subprocess.run(["git", "ls-files", "-z", "--", pre or "."], capture_output=True,
                         check=True).stdout.decode("utf-8", "replace").split("\0")
# an entry names its kit by its descriptor head; an exempt row names one only by being a directory
named = [str(e.get("descriptor", "")) for e in reg.get("entry", [])]
named = [d.split("/")[1] for d in named if d.startswith("{prefix}/") and d.count("/") > 1]
named += [str(x.get("path", ""))[len("{prefix}/"):] for x in reg.get("exempt", [])
          if str(x.get("path", "")).startswith("{prefix}/")]
kits = sorted({n.split("/")[0] for n in named if n and any(t.startswith(pre + n + "/") for t in tracked)})
sys.stdout.buffer.write("".join(k + "\n" for k in kits).encode())  # bytes: Windows text mode adds CR
' "$REGISTRY" "$SELF_PRE" 2>/dev/null); then
  echo "playbook-parity: cannot read the kit population from govkit's registry.toml — the sibling-kit resolver found none beside or above ${SELF_PRE:-the repository root}, or it did not parse — REFUSING"
  exit 2
fi

# ARM 2 of the anti-vacuity set. An empty or broken derivation must red by NAME rather than report
# universal coverage: with no kits, "every kit is documented" is vacuously true.
if [ -z "$kits" ]; then
  fail 1 "the kit derivation returned an empty set, so coverage would pass by checking nothing"
elif ! printf '%s\n' "$kits" | grep -qx "$SENTINEL"; then
  fail 2 "the kit derivation lost its frozen sentinel member, so the derivation is broken rather than the tree being empty: expected to find $SENTINEL"
fi

# AC9: the registry is CONSUMED here and owned elsewhere. Absent, this gate stops rather than
# creating one — a gate that seeds its own waiver list can waive whatever it cannot check.
if [ ! -f "$WAIVERS" ]; then
  fail 3 "the kit waiver registry is absent and this gate never creates it: expected $WAIVERS"
  printf 'PLAYBOOK-PARITY: stopping — S1 cannot be evaluated without the registry.\n'
  exit 1
fi

waived=$(grep -vE '^[[:space:]]*(#|$)' "$WAIVERS" | awk '{print $1}' | sort -u)

# The match is an anchored PATH SEGMENT, case-sensitive — `tools/<kit>/` or a backticked `<kit>/` —
# never a bare substring. A substring search scores the kit `lib` many times over the trio — every
# hit inside "deliberate"/"deliberately" or "stdlib", none of them about `<prefix>/lib/` — and would
# certify it documented on that evidence. That is the vacuous-selector shape this gate exists to
# prevent, committed by the gate itself. No count is written here: the figure was measured at 7
# when this comment was drafted and was 9 by the time the build landed, which is the same
# stale-count defect one file over.
# `<prefix>/<kit>/` is the third form (TOOL-aRepatriatedFork-26 S9): the charter and the runbook spell
# a kit path with that prose token, because no install prefix is correct for every adopter.
# The first form is THIS install's own root, derived, never gov's literal one: spelled `tools/` it
# graded every other install against a root it does not have (TOOL-aRepatriatedFork-26, VERIFYING
# repair). At a root install there is no root head, and a bare `<kit>/` is the substring above.
# A `kit:<id>` fence NAMES its kit too (TOOL-aDistilledCharter-7, C7): since v4.0 the charter's
# per-kit tools and protocol lines sit inside one, and spell no install path at all.
named_in_playbook() { # <kit>
  grep -qE "${SELF_PRE:+$SELF_PRE$1/|}<prefix>/$1/|\`$1/\`|<!-- kit:$1 -->" "$TEMPLATE" "$RUNBOOK" 2>/dev/null
}

for k in $kits; do
  if named_in_playbook "$k"; then continue; fi
  if printf '%s\n' "$waived" | grep -qx "$k"; then continue; fi
  fail 4 "a kit ships and the playbook never names it, with no waiver row to excuse it: $k"
done

# AC6, both arms. The registry must be able to GROW — a missing kit reds, so an experimental kit
# needs an escape hatch — which is why it drains through these two arms instead of a shrink-only pin.
for w in $waived; do
  if ! printf '%s\n' "$kits" | grep -qx "$w"; then
    fail 5 "a waiver row names a kit that no longer exists, so the row excuses nothing and is stale: $w"
  elif named_in_playbook "$w"; then
    fail 6 "a waiver row names a kit the playbook DOES document, so the row excuses nothing: $w"
  fi
done

# ============================================================== S2 — value parity ===============
# A declared pair list: each row names a value the playbook STATES and the source that OWNS it, plus
# the extraction for each side. In-script rather than a data file (§8 F1) — it reuses the seam
# kit-dogfood-parity.PAIRS already establishes, and a data file would split one mechanism in two.
#
#   <label>~<stated-file>~<stated-extraction>~<owning-file>~<owning-extraction>
#
# The field separator is `~` and NOT `|`: a hook-matcher pair once compared `Workflow|Agent`, and
# with `|` as the delimiter that row silently reparsed into the wrong fields — a real failure for a
# fake reason, which is worse than either a pass or an honest red. `~` appears in none of these.
#
# THE STATED SIDE MOVED at v4.0. The charter keeps one digit, the verify-agent total in its `[bound]`
# line. The lens-array bound and the resolved-K ceiling are stated by the hook's own README now, so
# those two pairs read it (TOOL-aDistilledCharter-6, closing review round 1, G1: retired outright,
# their digits would drift with no gate watching); the resolved-K pair reads the README's surviving
# rule-2 sentence, the verifier bound against `MAX_VERIFIERS`. The helper's width pair is retired
# (TOOL-dGroundRules-21 S35): its README sentence described the raw-primitive ban
# TOOL-dGroundRules-10 took out, so it extracted from a rule no longer denied. The hook-matcher
# pair is retired: no prose states the matcher, and `check-wiring.sh` grades the settings file.
#
# The pair list is no longer playbook-only. TOOL-aHonedRuleset-5 added a row whose stated side is
# the kickoff MANIFEST TEMPLATE, because the value it pins -- the stamp rule's sha expression --
# has a prose home and a machine home that had already drifted into two spellings.
# What this row does NOT cover: it compares the stamp rule's sha expression and nothing else about
# the stamp. The datetime half, whether a stamp is FRESH, and whether the sha it names is reachable
# are manifest-check.sh's checks 3 and 5, not this gate's.
PAIRS="
lens-array bound~${HK_DIR}/README.md~sed -n 's/.*array LITERAL of ≤\([0-9]\+\) elements.*/\1/p'~${HK_DIR}/agent-cap.js~sed -n 's/^const MAX_LENSES = \([0-9]\+\).*/\1/p'
verify-agent total~$TEMPLATE~sed -n 's/.*at most \([0-9]\+\) verify agents TOTAL.*/\1/p'~${HK_DIR}/agent-cap.js~sed -n 's/^const MAX_VERIFIERS = \([0-9]\+\).*/\1/p'
resolved-K ceiling~${HK_DIR}/README.md~sed -n 's/.*cannot resolve to an integer ≤\([0-9]\+\).*/\1/p'~${HK_DIR}/agent-cap.js~sed -n 's/^const MAX_VERIFIERS = \([0-9]\+\).*/\1/p'
template major~${PB_DIR}/render_playbook.py~sed -n 's/^TEMPLATE_MAJOR = \([0-9]\+\).*/\1/p'~$TEMPLATE~sed -n 's/.*governance-template: v\([0-9]\+\)\..*/\1/p'
stamp rule sha expression~skills/session-kickoff/MANIFEST-TEMPLATE.md~sed -n 's/.*Stamp rule: sha = \`\([A-Z]*\)\` on any branch.*/\1/p'~skills/session-kickoff/manifest-check.sh~sed -n 's/^STAMP_SHA_RULE=\"sha = \([A-Z]*\) on any branch\".*/\1/p'
"

# The pair loop runs in a subshell (it is the right-hand side of a pipe), so its findings have to
# cross a process boundary. That crossing is now CHECKED at both ends: unchecked, an unwritable
# TMPDIR made both redirections fail silently and the gate reported "pairs in agreement" with
# rc=0 over injected drift — this stage passing by finding nothing, which is the exact class the
# gate exists to catch, in the gate.
PPTMP="${TMPDIR:-/tmp}/pp.$$"
if ! : > "$PPTMP" 2>/dev/null || [ ! -w "$PPTMP" ]; then
  fail 14 "the value-parity stage could not create its results file, so no pair was compared and this gate must not report agreement: $PPTMP"
  printf 'PLAYBOOK-PARITY: stopping — S2 cannot be evaluated without a writable results file.\n'
  exit 1
fi
{
printf '%s\n' "$PAIRS" | while IFS='~' read -r label sfile sx ofile ox; do
  [ -n "${label:-}" ] || continue
  [ -f "$ofile" ] || { printf 'PAIRFAIL~%s~the owning source does not exist: %s\n' "$label" "$ofile"; continue; }
  sval=$(eval "$sx" < "$sfile" 2>/dev/null | head -1 | tr -d '[:space:]')
  oval=$(eval "$ox" < "$ofile" 2>/dev/null | head -1 | tr -d '[:space:]')
  # ARM 1 of the anti-vacuity set, and the reason this loop cannot report ok by finding nothing.
  if [ -z "$sval" ] || [ -z "$oval" ]; then
    printf 'PAIRFAIL~%s~an extraction matched NOTHING, so the pair was never compared (stated=%s owned=%s)\n' \
      "$label" "${sval:-<empty>}" "${oval:-<empty>}"
  elif [ "$sval" != "$oval" ]; then
    printf 'PAIRFAIL~%s~the playbook states %s where %s owns %s\n' "$label" "$sval" "$ofile" "$oval"
  fi
done
printf 'PAIRSTAGE-RAN\n'
} > "$PPTMP"
# A SENTINEL proves the stage actually ran. The loop always emits it, so an empty results file
# means the subshell died or its output was lost — indistinguishable, from here, from "no pair
# disagreed", which is why it cannot be allowed to read as success.
if ! grep -q '^PAIRSTAGE-RAN$' "$PPTMP" 2>/dev/null; then
  fail 15 "the value-parity stage produced no completion sentinel, so its results were lost rather than empty and no pair was actually compared"
fi
while IFS='~' read -r tag label msg; do
  [ "$tag" = "PAIRFAIL" ] || continue
  fail 7 "a declared value pair disagrees with the source that owns it. Pair $label, detail: $msg"
done < "$PPTMP"
rm -f "$PPTMP"

# ============================================================== S4 — section citations ==========
# TOOL-aDistilledCharter-3. The charter has no numbered sections since v4.0: a rule is cited by its
# handle (`charter [gate]`) or by the guide or gate that owns it. A live file citing a charter section
# BY NUMBER points at nothing, and the next restructure would leave it pointing at the wrong thing —
# which is how the runbook's per-section kit-block counts went stale without a word.
#
# WHAT IT DOES NOT CATCH, said here so a green run is not misread. A bare `§<n>` with no charter word
# beside it cannot be told from a citation of the citing document's own sections, so it is counted
# and printed as a near-miss, never failed. A line citing the SPEC template's own sections
# (`spec template's §8`) is excluded, because TEMPLATE-SPEC.md's numbered sections are real; a line
# carrying both forms is excluded whole. Frozen records under the memory tree are outside the surface.
# This gate's own file and its self-test are excluded too: both spell the predicate on purpose.
#
# TOOL-aDistilledCharter-7 widened it after the closing review: every derived kit directory joins the
# surface, so a ROOT install (empty SELF_PRE) still grades its kits (G2); so do CLAUDE.md and the
# memory root's own live guides, DECISIONS.md excepted (G8); the pathspec-mode variables are unset,
# or a `:!` exclusion reads as a file name (G6). The predicate reads git grep's BYTES, so every
# multibyte separator is an alternative rather than a bracket member (G5).
unset GIT_LITERAL_PATHSPECS GIT_GLOB_PATHSPECS GIT_NOGLOB_PATHSPECS GIT_ICASE_PATHSPECS
s4_kitpaths=()
for k in $kits; do s4_kitpaths+=("${SELF_PRE}$k"); done
s4_paths=("${s4_kitpaths[@]}")
[ -n "${SELF_PRE%/}" ] && s4_paths+=("${SELF_PRE%/}")
s4_paths+=(skills .githooks .claude/rules .claude/skills memory/guides WIRE-INTO-PROJECT.md README.md
  AGENTS.md CLAUDE.md "$TEMPLATE" ':(glob)memory/*.md' ':!memory/DECISIONS.md'
  ":!${SELF_PRE}check-playbook-parity.sh" ":!${SELF_PRE}check-playbook-parity.test.sh")
s4_pop=$(git ls-files -- "${s4_paths[@]}" | grep -c . || true)
s4_kitpop=$(git ls-files -- "${s4_kitpaths[@]}" | grep -c . || true)
if [ "$s4_pop" -eq 0 ] || [ "$s4_kitpop" -eq 0 ] || [ -z "$(git ls-files -- "$TEMPLATE")" ]; then
  fail 17 "the section-citation surface is empty, lacks the tracked template or holds no kit file, so no citation could be found and this stage must not report clean"
else
  s4_nb=$(printf '\302\240'); s4_nd=$(printf '\342\200\223'); s4_ap=$(printf '\342\200\231')
  s4_pred='(^|[^a-z])(charter|template|playbook|governance|agents\.md)s?(\.md)?('"'"'s|'"$s4_ap"'s)?([[:space:],:(`-]|'"$s4_nd"'|'"$s4_nb"'){0,3}(§)+ ?[0-9]|§1 Landing|§16 R1|§[0-9]+ (of|in) (the )?(charter|agents\.md)'
  s4_hits=$(git grep -n -I -i -E "$s4_pred" -- "${s4_paths[@]}" 2>/dev/null | grep -v -i -E '(spec|protocol)[- ]template' || true)
  s4_near=$(git grep -n -I -E '§[0-9]' -- "${s4_paths[@]}" 2>/dev/null | grep -c . || true)
  while IFS= read -r h; do
    [ -n "$h" ] || continue
    fail 16 "a live file cites a charter section by number, and v4.0 has no numbered sections; cite the handle or the owning guide: $h"
  done < <(printf '%s\n' "$s4_hits")
  printf 'playbook-parity: S4 graded %s file(s); %s line(s) carry a section sign, any charter citation among them failed above\n' "$s4_pop" "$s4_near"
fi

# The success line reads ONLY what the surviving stages assign. The catalogue stage above
# assigned three counters this line used to print, and the script runs under `set -u` — so
# deleting that stage without rewriting this line killed the gate with an unbound-variable
# error instead of a verdict, which is the named-failure contract this tree enforces everywhere.
[ "$status" -eq 0 ] && printf 'playbook-parity OK — %s kit(s) documented or waived · pairs in agreement\n' \
  "$(printf '%s\n' "$kits" | grep -c .)"
exit "$status"
