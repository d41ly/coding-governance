#!/usr/bin/env bash
# Self-test for check-verifier-fanout.sh. The PREDICATE's own arms live in <prefix>/hooks/agent-cap.test.sh
# — this file tests the things the gate adds on top of it: the population, the self-exclusion, the
# empty-population failure, and that the delegation actually reaches the hook rather than reporting
# clean because nothing ran.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-verifier-fanout.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
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
_rkd_py=$(resolve_python) || { echo "check-verifier-fanout.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
HOOKS_DIR=$(resolve_kit_dir "$_rkd_py" hooks agent-cap.js "$HERE") || exit 2
HOOKS="${HOOKS_DIR##*/}"
ROOT="$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)" || exit 2
GATE="$HERE/check-verifier-fanout.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
fails=0
arm() { # label · expected-substring · command…
  local label=$1 want=$2; shift 2
  local out; out=$("$@" 2>&1)
  case "$out" in
    *"$want"*) printf 'arm ok    %s\n' "$label" ;;
    *) fails=$((fails+1)); printf 'arm FAIL  %s — expected to see: %s\n' "$label" "$want"
       printf '%s\n' "$out" | sed 's/^/      /' ;;
  esac
}

# The RED fixture is not synthetic. It is the verify stage of the bespoke closing-review workflow
# written in this repo on 2026-08-09 — reconstructed from the session transcript, because the script
# was an inline `script` string on a Workflow tool call and was never a file. That is also the point
# of the finding that moved this rule into the hook: a gate over repo files could not have seen it.
cat >"$TMP/the-incident.js" <<'EOF'
export const meta = { name: 'closing-review', description: 'the shape that motivated the rule' }
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(`Adversarially verify: ${f.title}`, { label: `verify:${f.id}` })
    .then((v) => ({ ...f, verdict: v }))))
EOF
cat >"$TMP/bounded.js" <<'EOF'
export const meta = { name: 'ok-harness', description: 'the bounded shape' }
const MAX_VERIFIERS = 5
const batches = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(batches.map((g) => () => agent(g)), 5)
EOF
# Not a workflow: no `export const meta`. It carries the banned shape, so if the marker filter is
# dropped this file starts redding the bar and the arm below says so.
cat >"$TMP/not-a-workflow.js" <<'EOF'
const helper = all.map((f) => () => agent(f.claim))
EOF

arm 'the incident script is caught' 'verifier-fanout: FAILED' bash "$GATE" "$TMP/the-incident.js"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fails:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fails:-0}" = 0 ] && exit 0; exit 1; fi
arm '...and the report names the rule' 'verify-stage agents at 5 TOTAL' bash "$GATE" "$TMP/the-incident.js"
arm 'a bounded harness is clean' 'verifier-fanout: clean' bash "$GATE" "$TMP/bounded.js"
# Both states over the SAME two files: a gate that only ever reds is not discriminating, it is broken.
arm 'a mixed set reports only the offender' 'the-incident.js' bash "$GATE" "$TMP/bounded.js" "$TMP/the-incident.js"

# Closing review round 2 L1 (TOOL-aRepatriatedFork-46 S8): an exported `GIT_DIR` turned the gate's
# second question to git into its own directory, so the hook path named nothing and node threw.
# TOOL-dGroundRules-10 retired the print verb this arm asked, so it judges a file instead.
GR="$TMP/gitdirrepo"; mkdir -p "$GR" && git -C "$GR" init -q
out=$(cd "$GR" && GIT_DIR="$GR/.git" bash "$GATE" "$TMP/bounded.js" 2>&1)
case "$out" in *'verifier-fanout: clean'*) printf 'arm ok    L1: with GIT_DIR exported the gate still reaches its predicate\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  L1: with GIT_DIR exported the gate printed:\n%s\n' "$out" | head -5 ;; esac

# The DISCOVERY path — the shipped tree. Every arm above hands the gate explicit files, and the
# explicit path never touches git, so none of them exercises the population.
arm 'the shipped tree is clean' 'verifier-fanout: clean' bash "$GATE"
# ...and it judged more than zero of them. "clean over an empty set" and "clean" print differently,
# but only because something asserts the count.
out=$(bash "$GATE" 2>&1)
n=$(printf '%s' "$out" | sed -n 's/.*clean — \([0-9]*\) workflow script.*/\1/p')
if [ -n "$n" ] && [ "$n" -ge 3 ]; then printf 'arm ok    the population is the real harness set (%s scripts)\n' "$n"
else fails=$((fails+1)); printf 'arm FAIL  the population collapsed (got %s scripts)\n' "${n:-none}"; fi

# An empty population is a FAILURE, not a pass — the class this repo keeps a catalogue record about.
E="$TMP/empty"; mkdir -p "$E"
( cd "$E" && git init -q . && git config user.email t@t.test && git config user.name t
  printf 'x\n' > README.md && git add -A && git commit -qm empty --no-verify ) >/dev/null 2>&1
mkdir -p "$E/${PFX}${HOOKS}" && cp "$ROOT/${HOOKS_DIR}/agent-cap.js" "$E/${PFX}${HOOKS}/agent-cap.js"
# TOOL-dRetiredFork-10: the gate now resolves its predicate RELATIVE TO ITSELF, so the fixture
# has to put it where an install actually puts it. It previously sat at the bare repository
# root and worked only because the gate hard-coded `$ROOT/<prefix>/hooks/` -- the literal this
# unit removes. No kit installs a workflow gate at a repo root, so the old fixture described a
# layout that never existed, and it would have kept passing while real adopters stayed broken.
mkdir -p "$E/${KIT_REL}" && cp "$GATE" "$E/${KIT_REL}/gate.sh"
arm 'an empty population is not a pass' 'the population is empty, which is not a pass' \
  bash -c 'cd "$1" && bash ./'"${KIT_REL}/gate.sh"'' _ "$E"

# The marker filter: a `.js` that is not a workflow is not judged, even carrying the banned shape.
arm 'a non-workflow .js is not judged by the discovery path' 'verifier-fanout: clean' \
  bash -c 'cp "$2" "$1/'"${PFX}x-helper.js"'" && cp "$3" "$1/'"${PFX}wf.js"'" && cd "$1" && bash ./'"${KIT_REL}/gate.sh"'' \
  _ "$E" "$TMP/not-a-workflow.js" "$TMP/bounded.js"

# The gate has no predicate of its own: break the delegation and it must FAIL, not pass quietly.
D="$TMP/nohook"; mkdir -p "$D"
( cd "$D" && git init -q . && git config user.email t@t.test && git config user.name t
  printf 'x\n' > README.md && git add -A && git commit -qm base --no-verify ) >/dev/null 2>&1
mkdir -p "$D/${KIT_REL}" && cp "$GATE" "$D/${KIT_REL}/gate.sh"
arm 'a missing predicate is a named failure' 'has no predicate to delegate to' \
  bash -c 'cd "$1" && bash ./'"${KIT_REL}/gate.sh"'' _ "$D"


# ---- TOOL-dRetiredFork-10: the gate resolves at a FOREIGN install prefix -------------------------
# These three arms are the reason the unit exists. Before it, the population filter and the hook
# path both spelled `<prefix>/`, so an adopter who installs at `scripts/` got an EMPTY population and
# a missing predicate — and every one of them carried a hand-maintained carve-out to fix it.
#
# The fixtures are built here rather than borrowed, because the two real adopters are foreign trees
# this suite must not depend on: a fixture keyed to adopter ic's current bytes grades a moving target.
# Both kit segments are the DERIVED directory names, so the foreign layout types no kit name
# (TOOL-aRepatriatedFork-30 S8): the workflows kit is this suite's own directory, the hooks kit the
# one the resolver found.
WFK=${KIT_REL##*/}; HKK=${HOOKS_DIR##*/}
mkfix() { # $1 = fixture root · $2 = where the hook goes, relative to the root ("" = no hook at all)
  local fix=$1 hookrel=$2
  mkdir -p "$fix/scripts/$WFK"
  cp "$HERE/check-verifier-fanout.sh" "$fix/scripts/$WFK/"
  # a bounded harness, so the population is non-empty and the verdict is legitimately clean
  cat >"$fix/scripts/$WFK/harness.js" <<'JS'
export const meta = { name: 'fixture', description: 'a bounded harness', phases: [] }
const LENSES = ['security', 'correctness', 'integration']
const out = await boundedParallel(LENSES.map((l) => () => agent(`check ${l}`)), 5)
JS
  if [ -n "$hookrel" ]; then
    mkdir -p "$fix/$(dirname "$hookrel")"
    cp "$ROOT/${HOOKS_DIR}/agent-cap.js" "$fix/$hookrel"
  fi
  ( cd "$fix" && git init -q . && git config user.email t@t && git config user.name t \
      && git add -A && git commit -q -m fixture --no-verify ) >/dev/null 2>&1
}

# AC2 — the adopter nc shape: kit at `scripts/`, hook a directory up from the harnesses. Rung 2.
FIX_A=$(mktemp -d); mkfix "$FIX_A" "scripts/$HKK/agent-cap.js"
out=$(cd "$FIX_A" && bash "scripts/$WFK/check-verifier-fanout.sh" 2>&1); rc=$?
if [ "$rc" = 0 ]; then printf 'arm ok    AC2: resolves at a scripts/ install and exits 0\n'
else fails=$((fails+1)); printf 'arm FAIL  AC2: a scripts/ install did not pass (rc=%s)\n%s\n' "$rc" "$out"; fi
case "$out" in *"1 workflow script"*) printf 'arm ok    AC2: and the population is non-empty there\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  AC2: population wrong at a foreign prefix: %s\n' "$out" ;; esac

# AC3 — the adopter ic shape: NO scripts/hooks/ at all, the only copy at .claude/hooks/. Rung 3, which a
# two-rung chain strands. This arm is the one that would have caught that.
FIX_B=$(mktemp -d); mkfix "$FIX_B" ".claude/hooks/agent-cap.js"
out=$(cd "$FIX_B" && bash "scripts/$WFK/check-verifier-fanout.sh" 2>&1); rc=$?
if [ "$rc" = 0 ]; then printf 'arm ok    AC3: resolves the .claude/hooks/ copy when no sibling exists\n'
else fails=$((fails+1)); printf 'arm FAIL  AC3: the third rung did not resolve (rc=%s)\n%s\n' "$rc" "$out"; fi

# AC4 — no hook anywhere. The gate must REFUSE and NAME what it probed. A gate that cannot find its
# predicate and prints a clean line is the failure this whole build keeps finding.
FIX_C=$(mktemp -d); mkfix "$FIX_C" ""
out=$(cd "$FIX_C" && bash "scripts/$WFK/check-verifier-fanout.sh" 2>&1); rc=$?
if [ "$rc" != 0 ]; then printf 'arm ok    AC4: an unresolvable predicate REFUSES (rc=%s)\n' "$rc"
else fails=$((fails+1)); printf 'arm FAIL  AC4: no hook anywhere and the gate still passed\n%s\n' "$out"; fi
case "$out" in *"hooks/"*".claude/hooks/"*) printf 'arm ok    AC4: and the refusal names the probes it tried\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  AC4: the refusal does not name its probes: %s\n' "$out" ;; esac

# ANTI-VACUITY. Every arm above would also pass if the fixtures were empty and the gate refused for
# an unrelated reason, so pin the thing that actually distinguishes them: fixture A and fixture C
# differ ONLY by the presence of the hook, and their verdicts must differ.
outA=$(cd "$FIX_A" && bash "scripts/$WFK/check-verifier-fanout.sh" 2>&1)
outC=$(cd "$FIX_C" && bash "scripts/$WFK/check-verifier-fanout.sh" 2>&1)
if [ "$outA" != "$outC" ]; then printf 'arm ok    the hook is what the fixtures are testing, not the tree shape\n'
else fails=$((fails+1)); printf 'arm FAIL  identical verdicts with and without the predicate\n'; fi

# ---- TOOL-aRepatriatedFork-4: the harnesses live under .claude/workflows/ -----------------------
# Both adopters keep their harnesses there, outside the kit prefix. The a7c78ad2 bytes read this
# fixture as EMPTY (observed: `the population is empty`); the marker is now the whole selector.
FIX_D=$(mktemp -d); mkfix "$FIX_D" "scripts/$HKK/agent-cap.js"
rm -f "$FIX_D/scripts/$WFK/harness.js"; mkdir -p "$FIX_D/.claude/workflows"
cp "$TMP/the-incident.js" "$FIX_D/.claude/workflows/incident.js"
cp "$TMP/not-a-workflow.js" "$FIX_D/.claude/workflows/helper.js"
out=$(cd "$FIX_D" && bash "scripts/$WFK/check-verifier-fanout.sh" 2>&1); rc=$?
case "$rc:$out" in 1:*"FAILED — .claude/workflows/incident.js"*) printf 'arm ok    a harness under .claude/workflows/ is judged\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  a harness under .claude/workflows/ was not judged (rc=%s)\n%s\n' "$rc" "$out" ;; esac
# ...and dropping the prefix did not drop the marker: the unmarked file carries the banned shape.
case "$out" in *helper.js*) fails=$((fails+1)); printf 'arm FAIL  an unmarked .js was judged\n%s\n' "$out" ;;
  *) printf 'arm ok    an unmarked .js under .claude/workflows/ is not judged\n' ;; esac

rm -rf "$FIX_A" "$FIX_B" "$FIX_C" "$FIX_D"

if [ "$fails" = 0 ]; then echo "PASS — check-verifier-fanout: all arms held"; exit 0; fi
echo "FAIL — $fails arm(s) failed"
exit 1
