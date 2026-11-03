#!/usr/bin/env bash
# Self-test for check-verifier-fanout.sh and its rule, check-verifier-fanout.js. The first half tests
# what the gate adds: the population, the self-exclusion, the empty-population failure, and that the
# delegation actually reaches the rule rather than reporting clean because nothing ran. The second
# half is the rule's OWN arms, moved here from <prefix>/hooks/agent-cap.test.sh with the rule
# (TOOL-dFairHearing-16), the base-versus-now property arm among them.
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

# ---- TOOL-dFairHearing-13: the slot count, the one rule this gate holds natively -----------------
# AC3: the shipped harness with a sixth element planted in its `unit-spec` literal. The hook denies a
# sixth element too, so the arm keys on the SLOTS line, which a gate that counts nothing never prints.
SIX="$TMP/six-slots.js"
awk '{ print } /gov:lens-slots unit-spec$/ { print "  { key: \x27sixth\x27, brief: \x27a planted sixth slot\x27 }," }' \
  "$ROOT/$KIT_REL/tier2-review.js" > "$SIX"
out=$(bash "$GATE" "$SIX" 2>&1); rc=$?
case "$rc:$out" in 1:*"SLOTS — "*"literal unit-spec holds 6 slot(s)"*) printf 'arm ok    AC3: a sixth slot in a marked literal reds the slot count\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  AC3: a sixth slot was not named (rc=%s)\n%s\n' "$rc" "$out" ;; esac
# AC5: punctuation inside a string and a trailing comma are no slots.
cat >"$TMP/punct.js" <<'EOF'
export const meta = { name: 'slot-fixture', description: 'five slots whose strings carry punctuation' }
const a = 1, b = 2
const L = [ // gov:lens-slots unit-spec
  { key: 'one', brief: 'commas, inside, a string' },
  { key: 'two', brief: "a ] bracket and a [ one" },
  { key: 'three', brief: 'a quote \' and a "double"' },
  { key: 'four', brief: `a template span ${a, b} and ${[1, 2].join(', ')}` }, // a, comment ]
  /* a block, comment ] */ { key: 'five', brief: 'the last, with a trailing comma' },
]
EOF
out=$(bash "$GATE" "$TMP/punct.js" 2>&1); rc=$?
case "$rc:$out" in 0:*"slots — 1 lens-slot literal(s), each holding 5"*) printf 'arm ok    AC5: strings, comments and a trailing comma do not move the slot count\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  AC5: the punctuated literal did not count 5 (rc=%s)\n%s\n' "$rc" "$out" ;; esac
# AC6: a whole tree whose only workflow script carries no marker. The count graded nothing, which is
# not a pass. `$E` already holds a hook, the gate and one bounded workflow script, from the arm above.
out=$(cd "$E" && bash "./${KIT_REL}/gate.sh" 2>&1); rc=$?
case "$rc:$out" in 1:*"no lens-slot literal (a line marked gov:lens-slots) in any workflow script"*) printf 'arm ok    AC6: an empty marker population is not a pass\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  AC6: a tree with no marked literal did not red (rc=%s)\n%s\n' "$rc" "$out" ;; esac

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

# ==== RULE 2'S OWN ARMS, moved from the hook's suite (TOOL-dFairHearing-16) ========================
# Rule 2 left agent-cap.js for check-verifier-fanout.js beside this gate, and its arms came with it,
# each keeping its label, its payload and the hook's verdict: 2 for a deny, 0 for an admit. Only the
# helpers below are new. `run_fan` is the hook's interface over the rule's new home: the payload on
# stdin, and the script it carries, or the file its `scriptPath` names, judged by
# check-verifier-fanout.js from the payload's `cwd` where it names one, over a COPY of the hook beside
# scratch-guard.js and no policy kit, as the hook's suite judged it, so a writer split reads
# MAX_VERIFIERS. The home's 1 (a finding) and 2 (a refusal: a file it cannot read) are the hook's 2,
# which denied both; a payload carrying no source is the hook's 0. The counters are this section's.
unset CLAUDE_PROJECT_DIR
TESTPY=$_rkd_py
FANJS="$HERE/check-verifier-fanout.js"
ARMS_HOOKS="$TMP/arms-hooks/hooks"; mkdir -p "$ARMS_HOOKS"; cp "$ROOT/$HOOKS_DIR/agent-cap.js" "$ROOT/$HOOKS_DIR/scratch-guard.js" "$ARMS_HOOKS/"
HOOK="$ARMS_HOOKS/agent-cap.js"
pass=0; fail=0
# ponytail: run_home is check-review-join.test.sh's twin; one suite library is the step if a third suite needs it.
run_home() { # <home.js> [arg...]; payload on stdin -> the hook's exit code for it; the home's stderr on stderr
  local src rc home=$1; shift
  src=$(node -e '
    const fs = require("fs")
    let d
    try { d = JSON.parse(fs.readFileSync(0, "utf8")) } catch { process.exit(3) }
    const ti = (d && d.tool_name === "Workflow" && d.tool_input) || {}
    let f = ""
    if (ti.script) { fs.writeFileSync(process.argv[1], ti.script); f = process.argv[1] } else if (ti.scriptPath) f = ti.scriptPath
    if (!f) process.exit(4)
    process.stdout.write((typeof d.cwd === "string" ? d.cwd : "") + "\n" + f)' "$TMP/fan-arm.js") || return 0
  ( c=${src%%$'\n'*}; if [ -n "$c" ]; then cd "$c" || exit 3; fi; node "$home" --hook "${ARM_HOOK:-$HOOK}" "$@" "${src#*$'\n'}" 2>"$TMP/home.err" ); rc=$?
  cat "$TMP/home.err" >&2
  # A 1 or 2 is the hook's deny only when the home SAID so: node's own exit 1 on a crash, a home that
  # never loaded, is the hook's crash, which admits, so a deny arm cannot pass on it.
  case "$rc" in 1|2) grep -qE '^(BLOCKED by agent-cap:|check-verifier-fanout:|check-review-join:)' "$TMP/home.err" && return 2 ;; esac
  return "$rc"
}
run_fan() { run_home "$FANJS"; }
check() { # name expected_exit json
  printf '%s' "$3" | (cd "$TMP" && run_fan) >/dev/null 2>"$TMP/err"; local got=$?
  if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
js() { # name expected_exit  (script on stdin)
  local name=$1 want=$2
  local payload
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  check "$name" "$want" "$payload"
}
run_limit_call() { # name expected_exit payload-json hook [text stderr must carry]
  local got
  printf '%s' "$3" | (cd "$TMP" && ARM_HOOK=$4 run_fan) >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" = "$2" ] && { [ -z "${5:-}" ] || grep -qF -- "$5" "$TMP/err"; }; then
    echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else
    echo "FAIL $1 (exit $got, want $2${5:+, stderr carrying '$5'})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
}
# The property arm's BASE, the hook blob the S9 arm below compares against; an adopter tree where it
# does not resolve gets that arm's announced skip.
GOV_BASE_SHA=${GOV_BASE_SHA:-d65da7ab}
git -C "$HERE" show "$GOV_BASE_SHA:$HOOKS_DIR/agent-cap.js" > "$TMP/base-hook.js" 2>/dev/null || : > "$TMP/base-hook.js"

# ---- the first arms ------------------------------------------------------------------------------
# Rule 1, the ban on raw `parallel`/`pipeline`, retired in TOOL-dGroundRules-10 with its corpus:
# the harness's own concurrency settings bound how many run at once. This first arm still DENIES, by
# rule 2, because the raw primitive fans an agent over an unbounded receiver.
check "a raw parallel fanning an agent over an unbounded map → deny (rule 2)" 2 '{"tool_name":"Workflow","tool_input":{"script":"const r = await parallel(D.map(d => () => agent(d.p)))"}}'
# The helper line itself is sanctioned, and its fan-out receiver is now BOUNDED — the old fixture
# fanned `D.map(d=>()=>agent(d.p))`, which rule 2 correctly denies. A fixture that the gate must
# reject cannot double as the fixture proving it accepts.
check "boundedParallel + marker → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"async function boundedParallel(t,cap=5){const o=[];for(let i=0;i<t.length;i+=cap)o.push(...await parallel(t.slice(i,i+cap))); // gov:bounded-fanout\nreturn o}\nconst LENSES = [1,2,3]\nconst r = await boundedParallel(LENSES.map(d=>()=>agent(d)),5)"}}'

# ---- the LOOP KEYWORD SET (TOOL-aWeldedTribunal-1) ----------------------------------------------
# Every loop-recognition path must see the SAME keyword set. Six sites in agent-cap.js used to hold
# their own `for|while` regex, and two ordinary spellings matched none of them: `for await (` puts an
# identifier between the keyword and the paren, and a `do { … } while (…)` block's opening line
# carries no keyword at all. Both were MEASURED at exit 0 against the shipped hook before this unit.
#
# ARMS PER WALK, NOT PER KEYWORD. The same fan expressed as `for await (` must deny whether it is
# reached through the BRACE walk or the OPENER walk — those are different predicates and the opener
# walk needs the end-of-text form, so a single arm would certify coverage it does not have.
check "for-await thunk array (brace walk) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const th = []\nfor await (const f of allFindings) { th.push(() => agent(f.claim)) }\nawait Promise.all(th.map(t=>t()))"}}'
check "do-while thunk array (brace walk) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const th = []\nlet i = 0\ndo { th.push(() => agent(allFindings[i].claim)); i++ } while (i < allFindings.length)\nawait Promise.all(th.map(t=>t()))"}}'
check "for-await inline agent (opener walk) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"for await (const f of allFindings) await agent(f.claim)"}}'
check "do-block inline agent → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"let i = 0\ndo { await agent(allFindings[i].claim); i++ } while (i < allFindings.length)"}}'
# THE NEGATIVE DIRECTION. A widened predicate that denies innocent files is the failure this pair
# exists to catch; measured over all eight tracked *.js, ZERO lines match the widened form and not
# the old one, so nothing legal may change verdict.
check "bounded fan, no loop → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const LENSES = [1,2,3]\nawait boundedParallel(LENSES.map(L=>()=>agent(L)), 5)"}}'
check "the words for-await inside a string → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const note = \"we never write for await (x of y) here\"\nawait boundedParallel(T, 5)"}}'

# ---- a GROWN receiver loses its bound (TOOL-aWeldedTribunal-2) ----------------------------------
# `const batches = []` counts zero elements and is blessed by the array-literal case; a later
# `batches.push(...)` grows it to one entry per finding with the bound still standing. The arms
# assert on the refusal TEXT, not just the exit code: an arm checking non-zero alone cannot tell
# this rule's denial from the loop ban's, and a criterion that could not was this unit's own blocker.
#
# THE ADJACENCY IS THE POINT. The hook judges only lines containing `agent(`, and `push` is not an
# ITER_CALL — so the agent call must sit lexically INSIDE the map receiver's parens for the iter arm
# to be reached at all. `push` on one line and a detached `.map` on another is LEGAL and stays 0.
check "grown-by-push receiver → deny, naming the mutation" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.push(f)\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
check "grown-by-unshift receiver → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.unshift(f)\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
check "grown-by-splice receiver → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.splice(0, 0, f)\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
# THE NEGATIVES. An empty literal nobody grows is legal, and so is a growth whose fan is not
# adjacent — a non-mutating `.concat`/`.flat`/`.flatMap` must NOT take a bound back, which is what
# the pre-wiring run over this tree refuted the first vocabulary for.
check "empty literal never grown → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nawait boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)"}}'
check "grown but the fan is not adjacent → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const batches = []\nbatches.push(f)\nconst out = batches.map((b) => b())\nawait agent(\"one call\")"}}'
check "concat does not grow the receiver → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nconst more = LENSES.concat(extra)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# ---- the closing diff review's fold. Every arm below FAILED before its fix, and each was
# ---- reproduced by running the shipped hook rather than argued.
# THE ACCEPTED RESIDUAL, and the arm states it as such rather than hiding it. A BLOCK comment
# mentioning a growth REVOKES the bound and denies the script. Four review rounds went into trying
# to strip comments out of the take-back view and each attempt bought a FAIL-OPEN instead, because
# this file models no regex literal and every strip inherits that blindness in a new shape. The
# strip is gone; the false deny is accepted, which is the fail-closed direction and the behaviour
# that shipped before this build. Cost: one reworded comment. The alternative cost an agent burst.
check "a block comment naming a push DENIES (accepted residual, fail-closed)" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n/* never do LENSES.push(x) here */\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# A LINE comment is different and still allows: the lexed view breaks on `//` itself, so no strip
# of ours is involved. Kept as an arm because the two comment forms now diverge, and a reader who
# assumes they behave alike would be wrong.
check "a line comment naming a push does not take the bound back → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n// never do LENSES.push(x)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# A MEMBER CHAIN IS NOT THE TOP-LEVEL NAME. Without a left guard the regex captured the LAST segment,
# so `state.lenses.push(x)` denied a script naming a variable nothing had touched.
check "a member-chain push does not revoke an unrelated name → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst lenses = [1,2,3]\nstate.lenses.push(x)\nawait boundedParallel(lenses.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# A REMOVAL-ONLY SPLICE SHRINKS. Denying it states "was GROWN" about an array that got smaller.
check "removal-only splice does not take the bound back → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3,4,5]\nLENSES.splice(0, 2)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
check "a 3-argument splice INSERTS, so it still takes the bound back → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nLENSES.splice(0, 0, extra)\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
# THE TAKE-BACK CASCADES. A derivation is bounded only because its SOURCE was; when the source loses
# its bound the derived name must lose it too, or an unbounded fan is admitted one `.filter()` away.
# Two arms, one per sweep — the reassignment sweep had this hole before this build and now does not.
check "push-then-derive: the derived name loses its bound too → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst batches = []\nbatches.push(f)\nconst groups = batches.filter(Boolean) // gov:fixed-verifiers\nawait boundedParallel(groups.map((g) => () => agent(g)), MAX_VERIFIERS)"}}'
check "reassign-then-derive: the derived name loses its bound too → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nlet items = [1, 2]\nitems = allFindings\nconst groups = items.filter(Boolean) // gov:fixed-verifiers\nawait boundedParallel(groups.map((g) => () => agent(g)), MAX_VERIFIERS)"}}'
check "derive from a source that KEEPS its bound → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nconst groups = LENSES.filter(Boolean) // gov:fixed-verifiers\nawait boundedParallel(groups.map((g) => () => agent(g)), MAX_VERIFIERS)"}}'

# ---- THE FROZEN DENY CORPUS (TOOL-aWeldedTribunal-2, round 2 of the closing review) -------------
# WHY THIS EXISTS, and it is the most useful thing in this file. The fold that fixed round 1's
# false-DENY findings traded them for four fail-OPEN bound escapes, and this suite was 196 passed,
# 0 failed while it happened — because every arm above pins the exact script a review reported and
# none pins the CLASS. A green leg over a broken control is the shape the charter names, and it
# happened here, in the file that enforces the fan-out cap.
#
# So: ONE GROWTH, spelled every way legal JavaScript allows, all of which must DENY. Adding a
# spelling is one line; a view change or a regex tightening that blinds any of them reds. That is
# the difference between gating an instance and gating a class.
#
# `LENSES` is bounded by its literal; each line grows it; the fan is bounded-looking and must
# therefore be refused because the receiver is not.
arm_growth_denies() { # $1 = label, $2 = the mutation line
  check "deny-corpus: $1" 2 "$(node -e '
    const m = process.argv[1]
    const s = "export const meta={name:\"x\",description:\"y\"}\nconst MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n"
            + m + "\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)\n"
    process.stdout.write(JSON.stringify({tool_name:"Workflow",tool_input:{script:s}}))' "$2")"
}
arm_growth_denies "a plain push"                    'LENSES.push(x)'
arm_growth_denies "an unshift"                      'LENSES.unshift(x)'
arm_growth_denies "an inserting splice"             'LENSES.splice(0, 0, x)'
arm_growth_denies "a splice with a spread"          'LENSES.splice(...more)'
arm_growth_denies "inside a template interpolation" 'const s = `${LENSES.push(x)}`'
arm_growth_denies "after a closing paren"           'if (x) LENSES.push(y)'
arm_growth_denies "nested in another call"          'sink.push(LENSES.push(9))'
arm_growth_denies "after a semicolon"               'let i = 0; LENSES.push(x)'
arm_growth_denies "inside an arrow body"            'const f = () => LENSES.push(x)'
arm_growth_denies "as an expression statement"      '(LENSES.push(x))'
# THE VIEW AXIS, which is the one every fold of this build broke and the first corpus did not reach.
# Round 3's blocker: the take-back view stripped block comments over the JOINED text, so a `/*` in a
# regex literal — this file models none, by standing decision — opened a phantom comment that ate
# every take-back down to the next real `*/`. Ten spellings of the MUTATION could not see it,
# because the mutation was never what changed.
arm_growth_denies "below a regex literal containing a comment opener" 'const re = /[/*]/
LENSES.push(x)
const t = 1 /* a later real closer */'
arm_growth_denies "between two regex literals"      'const a = /[/*]/
LENSES.push(x)
const b = /[*/]/'
arm_growth_denies "on the same line as a closed block comment" '/* note */ LENSES.push(x)'
# ROUND 4's blocker: a regex literal and a REAL closer on the SAME line. Every strip this build
# tried paired the two; there is no strip now, so the growth is simply visible.
arm_growth_denies "regex literal and a real closer on one line" 'if (/[/*]/.test(s)) LENSES.push(x) /* ok */'
arm_growth_denies "regex literal, growth and closer, all one line" 'const re = /[/*]/; LENSES.push(x); const t = 1 /* pad */'
# ROUND 4's high: a comment in the argument list hid a top-level spread from the arity test. An
# argument list carrying a comment is no longer graded at all.
arm_growth_denies "a comment hiding a spread in splice args" 'LENSES.splice(0, /*
*/ ...rest)'
# The reassignment half of the same view, which round 3 found this fold had newly broken.
check "deny-corpus: a reassignment below a regex-literal comment opener" 2 "$(node -e '
  const s = "export const meta={name:\"x\",description:\"y\"}\nconst MAX_VERIFIERS = 5\nlet LENSES = [1,2,3]\n"
          + "const re = /[/*]/\nLENSES = allFindings\nconst t = 1 /* closer */\n"
          + "await boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)\n"
  process.stdout.write(JSON.stringify({tool_name:"Workflow",tool_input:{script:s}}))')"
# AND THE NEGATIVE HALF OF THE VIEW AXIS. A comment that MENTIONS a growth grows nothing, and a
# spread NESTED in a removal-only splice's argument is not a spread argument.
check "view axis: a single-line block comment mentioning a push DENIES (residual)" 2 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\n/* never do LENSES.push(x) here */\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'
check "view axis: a spread nested in a removal-only splice → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const MAX_VERIFIERS = 5\nconst LENSES = [1,2,3]\nLENSES.splice(0, Math.min(...ns))\nawait boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)"}}'

check "a legal multi-line prompt with a bounded fan → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const LENSES = [1,2,3]\nconst prompt = `line one\nline two\nline three`\nawait boundedParallel(LENSES.map((L) => () => agent(prompt)), 5)"}}'

# ---- rule 2: verifier arity ---------------------------------------------------------------------
# THE PROVENANCE OF THESE FIXTURES: the first is the verify stage of the bespoke closing-review
# workflow written in this repo's own session on 2026-08-09, reconstructed from the transcript. It is
# not a synthetic approximation of the mistake; it is the mistake. The nine after it are the evasions
# a reviewer proposed when asked to defeat the rule — each was ALLOWED by an earlier cut of this hook
# and each is here because it was, not because it was imagined.
js "rule2: one agent per finding → deny" 2 <<'EOF'
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(`Adversarially verify: ${f.title}`, { label: `verify:${f.id}` })))
EOF
js "rule2: fan-out wrapped over many lines → deny" 2 <<'EOF'
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(
    `line one
line two
line three
line four
line five
line six`,
    { label: `verify:${f.id}` })), 5)
EOF
js "rule2: flatMap → deny" 2 <<'EOF'
const r = await boundedParallel(all.flatMap((f) => [() => agent(f.claim)]), 5)
EOF
js "rule2: Array.from → deny" 2 <<'EOF'
const r = await boundedParallel(Array.from(all, (f) => () => agent(f.claim)), 5)
EOF
js "rule2: loop-built thunks → deny" 2 <<'EOF'
const th = []
for (const f of all) {
  th.push(() => agent(f.claim))
}
const r = await boundedParallel(th, 5)
EOF
js "rule2: forEach-built thunks → deny" 2 <<'EOF'
const th = []
all.forEach((f) => th.push(() => agent(f.claim)))
const r = await boundedParallel(th, 5)
EOF
js "rule2: renamed receiver → deny" 2 <<'EOF'
const groups = all
const r = await boundedParallel(groups.map((f) => () => agent(f.claim)), 5)
EOF
# The marker is a CLAIM; these three make it falsely and must still red, or the whitelist degenerates
# into "write the magic comment".
js "rule2: marker over chunk(all,1) → deny" 2 <<'EOF'
const b = chunk(all, 1) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marker over splitInto(all, all.length) → deny" 2 <<'EOF'
const b = splitInto(all, all.length) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marker with a literal above the cap → deny" 2 <<'EOF'
const b = splitInto(all, 9) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF

# ---- gov:sequential-agents (TOOL-dFoldedVerdict-4) ----------------------------------------------
# THE ONE LOOP SHAPE THE HOOK ADMITS. Owner-ratified spelling, 2026-09-01. It exists because a
# ratified `parallelism route: none` verdict forbids the bounded PARALLEL fan this hook permits while
# this hook forbade the strictly sequential dispatch that verdict requires — a harness iterating a
# build's units sat in the gap and could not be written at all.
#
# The ADMIT arm first, then one arm per clause. Each refusal names the FIRST clause that failed, so
# a fixture breaking two clauses proves only the earlier one — which is why C8's fixture keeps its
# `await` and breaks the function boundary instead.
js "seq: marked, bounded receiver, awaited, one call → ALLOW" 0 <<'EOF'
const MAX = 5
const units = [1, 2, 3, 4, 5]
const out = []
for (const u of units) { // gov:sequential-agents(MAX)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
js "seq: an array LITERAL receiver is bounded too → ALLOW" 0 <<'EOF'
const units = ['a', 'b', 'c']
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C3 — a bare marker claims concurrency one and says nothing about the TOTAL, which is the half the
# owner ruling insists on. Two rules, not one.
js "seq: a bare marker with no bound → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C4 — the number is CHECKED, through the same resolver every other consumer uses.
js "seq: a bound above the cap → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(9)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# AC6 — a bound the file cannot RESOLVE, in the two shapes that look resolved and are not. An
# `<expr> || <int>` right-hand side is a caller-settable knob wearing a constant's clothes, which is
# how two shipped harnesses raised their own verifier count past the cap while every gate stayed
# green; a `.length` is a number nobody wrote down.
js "seq: an or-bound K → deny" 2 <<'EOF'
const K = (args && args.cap) || 5
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(K)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
js "seq: a .length K → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(units.length)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C6 — THE CLAUSE THAT CARRIES THE WEIGHT. Without it the marker's number is an author's assertion
# over an array of any size, which is the shape the owner ruling names as the thing to refuse.
js "seq: marked, but the receiver is not proven bounded → deny" 2 <<'EOF'
const units = findings.map((f) => f.id)
const out = []
for (const u of units) { // gov:sequential-agents(5)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C7 — AWAIT-ADJACENCY on THIS occurrence. A loop that collects unawaited calls is building a thunk
# array with extra steps.
js "seq: marked and bounded but the call is not awaited → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(agent('do ' + u, { label: 'u' }))
}
EOF
# C8 — awaited, but through a function boundary, which is the evasion the ban exists for. This
# fixture keeps the `await` deliberately: break C7 as well and the refusal names C7 and proves
# nothing about C8.
js "seq: awaited THROUGH a function boundary → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  const run = async () => out.push(await agent('do ' + u, { label: 'u' }))
  await run()
}
EOF
# THE NINTH CONDITION, judged after the scan. Two awaited calls in one marked body spend twice the
# bound, so the marker would name a number the loop does not obey.
js "seq: TWO awaited calls in one marked body → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(await agent('a ' + u, { label: 'u' }))
  out.push(await agent('b ' + u, { label: 'u' }))
}
EOF
# NESTED LOOPS FAIL CLOSED with no extra clause: the walk stops at the first enclosing loop, so an
# unmarked inner loop inside a marked outer one is refused at the inner header.
js "seq: an unmarked inner loop inside a marked outer one → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  for (const p of u.parts) {
    out.push(await agent('do ' + p, { label: 'p' }))
  }
}
EOF
# AND THE UNMARKED LOOP STILL DENIES WITH ITS ORIGINAL SENTENCE. This is the arm that proves the
# marker is an affordance and not a weakening: no claim, no change.
js "seq: an unmarked loop is denied exactly as before → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) {
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF

# ---- THE CLOSING REVIEW'S FOLD. Four refusals, every one of them a bypass that was EXECUTED against
# ---- the shipped hook before it existed. All four are the same shape one level up: the predicate
# ---- read a LINE where the rule is about a CONSTRUCT, or bounded a BODY where the charter bounds a
# ---- TOTAL.
# The receiver clause used to take the FIRST `of <ident>)` anywhere on the header line, so a block
# comment supplied a bounded token for a loop iterating caller-sized data. One agent per element.
js "seq fold: a bounded token from a BLOCK COMMENT does not bless the loop -> deny" 2 <<'EOF'
const OK = ['a', 'b', 'c']
async function run(args) {
  for (/* of OK) */ const f of args.findings) await agent(f) // gov:sequential-agents(5)
}
EOF
# ...and from a guard clause on the same line.
js "seq fold: a bounded token from a GUARD clause does not bless the loop -> deny" 2 <<'EOF'
const OK = ['a', 'b', 'c']
async function run(args) {
  if ('probe' in OK) for (const f of args.findings) await agent(f) // gov:sequential-agents(5)
}
EOF
# A `while` has no iteration source this scan can size, so a bound over one is a claim about nothing.
js "seq fold: a marked while loop -> deny" 2 <<'EOF'
const OK = ['a', 'b', 'c']
async function run(args) {
  const queue = args.findings.slice()
  while (queue.length && ('probe' in OK)) { // gov:sequential-agents(5)
    await agent(queue.pop())
  }
}
EOF
# Two openers on one line: the brace walk stops at the shared header and the inner loop never gets
# its own. This is the fixture that refuted the old "nested loops fail closed" comment.
js "seq fold: two loop openers on one header line -> deny" 2 <<'EOF'
const OK = ['a', 'b']
async function run(args) {
  const ALL = args.findings
  for (const g of OK) for (const f of ALL) await agent(f) // gov:sequential-agents(5)
}
EOF
# THE SWEEP COUNTED LINES, NOT CALLS. Five awaited calls on one line contributed one entry, so the
# group stayed at 1 and 25 spawns landed under a marker naming 5.
js "seq fold: five awaited calls on ONE line -> deny" 2 <<'EOF'
const UNITS = ['a', 'b', 'c', 'd', 'e']
async function run() {
  for (const u of UNITS) { // gov:sequential-agents(5)
    await agent(u); await agent(u); await agent(u); await agent(u); await agent(u)
  }
}
EOF
# TWO HONEST MARKERS MULTIPLY. Every clause satisfied, 5 x 5 = 25 spawns. The bound is a TOTAL and
# the sweep relates no two headers.
js "seq fold: two nested marked loops -> deny" 2 <<'EOF'
const UNITS = ['a', 'b', 'c', 'd', 'e']
async function run() {
  for (const u of UNITS) { // gov:sequential-agents(5)
    for (const v of UNITS) { // gov:sequential-agents(5)
      await agent(u + v)
    }
  }
}
EOF
# ...and an UNMARKED outer loop does it unboundedly, while never being evaluated itself because no
# agent( line is attributed to it.
js "seq fold: a marked loop inside an UNMARKED loop -> deny" 2 <<'EOF'
const UNITS = ['a', 'b', 'c', 'd', 'e']
async function run(args) {
  for (const x of args.findings) {
    for (const u of UNITS) { // gov:sequential-agents(5)
      await agent(u)
    }
  }
}
EOF

# THE BYPASSES. Every one of these was ALLOWED by the first cut of rule 2 and reported "clean" by the
# merge-bar leg that delegates to it — found by an adversarial review of the commit that introduced
# the rule, each reproduced against this tree before it was fixed. They are here because a whitelist
# is only as good as the spellings it refuses, and the ones it has never seen are the ones that get
# written. The root cause was a single line: an unrecognised receiver fell through to ALLOW.
js "bypass: the marker on the agent() line itself → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.map((f) => () => agent(f.claim)), 5) // gov:fixed-verifiers
EOF
js "bypass: a .filter().map() chain → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.filter(Boolean).map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a call-result receiver → deny" 2 <<'EOF'
const r = await boundedParallel(Object.values(byId).map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a spread literal → deny" 2 <<'EOF'
const items = [...allFindings]
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: [].concat(x) → deny" 2 <<'EOF'
const items = [].concat(allFindings)
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a reassigned receiver → deny" 2 <<'EOF'
let items = [1, 2]
items = allFindings
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a braceless for-of body → deny" 2 <<'EOF'
const out = []
for (const f of allFindings) out.push(await agent(f.claim))
EOF
js "bypass: a braceless while body → deny" 2 <<'EOF'
let i = 0
while (i < all.length) out.push(await agent(all[i++].claim))
EOF
js "bypass: a marked .concat() derivation → deny" 2 <<'EOF'
const LENSES = [{ k: 1 }, { k: 2 }]
const more = LENSES.concat(allFindings) // gov:fixed-verifiers
const r = await boundedParallel(more.map((f) => () => agent(f.k)), 5)
EOF
js "bypass: .reduce() instead of .map() → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.reduce((a, f) => a.concat([() => agent(f.claim)]), []), 5)
EOF

# ---- rule 2: the shapes that MUST pass ----------------------------------------------------------
# Without these the rule could be satisfied by denying everything, which is a gate that stops work
# rather than stopping a defect.
js "rule2: bounded group count + marker → allow" 0 <<'EOF'
const MAX_VERIFIERS = 5
const batches = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(batches.map((g) => () => agent(g)), 5)
EOF
js "rule2: a fixed lens literal → allow" 0 <<'EOF'
const LENSES = [{ k: 'security' }, { k: 'correctness' }, { k: 'seams' }, { k: 'dead-code' }]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
# THE LENS ALLOWANCE IS THE SAME 5 AS EVERYTHING ELSE, and these three arms are why it can be. It
# read as 6 for one release and that was never a decision: the counter scored `1 + every top-level
# comma`, so a prettier-formatted 5-element array measured 6 and the constant had been raised to fit
# the error. Both drift-audit waves ship exactly this shape, so without the trailing-comma arm below
# lowering the number would deny two shipped harnesses — and the arm that proves the count is fixed
# has to be the multi-line, trailing-comma form, because the single-line one never mis-measured.
js "rule2: five lenses, prettier-formatted with a trailing comma → allow" 0 <<'EOF'
const LENSES = [
  { k: 'dead-code' },
  { k: 'unwired' },
  { k: 'duplication' },
  { k: 'inefficient' },
  { k: 'instruments' },
]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: six lenses → deny (the allowance is 5)" 2 <<'EOF'
const LENSES = [{ k: 'a' }, { k: 'b' }, { k: 'c' }, { k: 'd' }, { k: 'e' }, { k: 'f' }]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: six lenses with a trailing comma → deny (the comma is not a sixth escape)" 2 <<'EOF'
const LENSES = [
  { k: 'a' },
  { k: 'b' },
  { k: 'c' },
  { k: 'd' },
  { k: 'e' },
  { k: 'f' },
]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a marked derivation from a bounded literal → allow" 0 <<'EOF'
const ALL_LENSES = [{ s: 'a' }, { s: 'b' }, { s: 'c' }]
const LENSES = a.lenses ? ALL_LENSES.filter((L) => a.lenses.includes(L.s)) : ALL_LENSES // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.s)), 5)
EOF
# TOOL-dTieredTribunal-13 S5 — the marked branch now judges EVERY top-level value branch. THREE of
# these five DENY arms are the reproduced holes: before this unit each PASSED, because either accept
# could return on a single arm while the other stayed caller-supplied. The other two are the guards
# inside the new predicate, which had no arm at all — and a guard nobody has watched fail is an
# assertion about nothing. Every one was run against the shipped file and its verdict recorded.
js "rule2: marked ternary whose OTHER arm is caller-supplied → deny" 2 <<'EOF'
const SPEC = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.kind === 'spec' ? SPEC : args.customLenses // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: marked .filter ROOTED on a caller value → deny" 2 <<'EOF'
const ALL = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.lenses.filter((L) => ALL.includes(L)) // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: bounded split in one arm, caller value in the other → deny" 2 <<'EOF'
const MAX_VERIFIERS = 5
const items = [1, 2, 3]
const b = cond ? chunk(items, Math.ceil(items.length / MAX_VERIFIERS)) : args.custom // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marked line whose right-hand side yields NO branch → deny" 2 <<'EOF'
const LENSES = // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
EOF
js "rule2: marked ternary whose : is not on the line → deny" 2 <<'EOF'
const SPEC = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.kind === 'spec' ? SPEC // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a marked ternary between two sibling literals → allow" 0 <<'EOF'
const SPEC_LENSES = [{ k: 'a' }, { k: 'b' }]
const DIFF_LENSES = [{ k: 'c' }, { k: 'd' }]
const LENSES = kind === 'spec-audit' ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a single synthesis agent → allow" 0 <<'EOF'
const synth = await agent('synthesize the confirmed findings', { label: 'synth' })
EOF
# The synthesis stage builds its PROMPT with a .map over every finding. A proximity-based scan read
# that as a fan-out and denied a one-agent call — measured on <prefix>/workflows/tier2-review.js:290.
js "rule2: a synth prompt that quotes a .map → allow" 0 <<'EOF'
const synth = await agent(
  'findings:\n' + allFindings.map((f) => f.claim).join('\n'),
  { label: 'synth' })
EOF

# ---- scriptPath: a saved script is a FILE, and a node hook has fs -------------------------------
# Exiting 0 here made both rules unenforceable the moment anyone wrote the offending script to disk.
# NODE'S VIEW OF THE PATH, not the shell's. Under MSYS/git-bash one directory has two spellings and
# `mktemp -d` hands back the POSIX one (`/tmp/tmp.X`), which node cannot open. The first cut of these
# three arms passed for the wrong reason: the "offending file denied" arm was green because the read
# FAILED, not because the rule fired — a fixture that proves nothing while looking like proof.
NODEDIR=$(cd "$TMP" && pwd -W 2>/dev/null || printf '%s' "$TMP")
GOOD="$TMP/good.js"; printf 'const s = await agent("one")\n' > "$GOOD"
BAD="$TMP/bad.js";   printf 'const r = await boundedParallel(all.map((f) => () => agent(f.c)), 5)\n' > "$BAD"
GOOD="$NODEDIR/good.js"; BAD="$NODEDIR/bad.js"
check "scriptPath → clean file allowed" 0 "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\"}}"
check "scriptPath → offending file denied" 2 "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$BAD\"}}"
check "scriptPath → unreadable path refused, not waved through" 2 '{"tool_name":"Workflow","tool_input":{"scriptPath":"/no/such/workflow.js"}}'
# ---- rule 2: the marked K and a reassigned receiver, each refusal asserting its own text ----------
# Rule 3, which resolved every concurrency width, retired in TOOL-dGroundRules-10 with its arms.
# These three were filed beside it and are rule 2's: the marker's K resolves through the one binder,
# and an `<expr> || <int>` fallback or a reassignment takes the bound back. Each asserts its message,
# because every rule exits 2.
msg() { # name expected_exit needle   (script on stdin)
  local name=$1 want=$2 needle=$3 payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" | (cd "$TMP" && run_fan) >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" != "$want" ]; then
    echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); return
  fi
  if grep -qF "$needle" "$TMP/err"; then echo "ok   $name"; pass=$((pass+1))
  else echo "FAIL $name (exit $got as wanted, but no branch named: $needle)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}

msg "rule2: a marked K bound by an || fallback → deny" 2 \
  'which this file does not show to be bounded' <<'EOF'
const MAX_VERIFIERS = (args && args.maxVerifiers) || 5
const b = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
# A BARE REASSIGNMENT invalidates the NUMBER, not just the receiver: `let K = 5; K = 500` published a 5.
msg "rule2: a reassigned K → deny" 2 \
  'which this file does not show to be bounded' <<'EOF'
let K = 5
K = 500
const b = chunk(all, Math.ceil(all.length / K)) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF

# D10 - a REASSIGNED receiver must SAY so. The reason map is written by both scan passes and was
# never cleared on accept, so a name refused on pass 1 for declaration order and then accepted on
# pass 2 kept the pass-1 text; the sweep below took the name back and the refusal printed an
# explanation of a branch pass 2 had just blessed. This arm asserts the TEXT, because an exit-code
# arm cannot tell a right reason from a wrong one.
msg "rule2: a reassigned marked receiver -> deny NAMING the reassignment" 2   'was REASSIGNED after its bounded assignment' <<'EOF'
let LENSES = ALL.filter((L) => L.on) // gov:fixed-verifiers
const ALL = [1, 2, 3]
LENSES = args.custom
const r = await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
EOF

# The rule-2 remediation text names the number it enforces, and the constant it lives in.
if grep -qF "verify-stage agents at 5 TOTAL, this hook's MAX_VERIFIERS" <(printf '%s' '{"tool_name":"Workflow","tool_input":{"script":"const r = await boundedParallel(all.map((f) => () => agent(f.c)), 5)"}}' | (cd "$TMP" && run_fan) 2>&1); then
  echo "ok   rule-2 deny text names the 5-verifier cap"; pass=$((pass+1))
else echo "FAIL rule-2 deny text does not name the cap"; fail=$((fail+1)); fi

# TOOL-dGroundRules-18 — rule 2 judges a `gov:fixed-writers` split against the agent limit and a
# `gov:fixed-verifiers` split against MAX_VERIFIERS whatever the limit. The copy sits beside a STUB
# policy-mirror.js answering the limit, which the hook's `readWriterBound` reads, and each arm runs the
# rule from that scratch checkout, the payload's `cwd`. Its settings, at 4, are what rule 7 read when
# the hook ran these arms (TOOL-dGroundRules-68); the review kit's check runs no rule 7. With no stub,
# the bound is MAX_VERIFIERS.
WS="$TMP/writer-split"; WS_HOOKS="$WS/hooks" WS_POLICY="$WS/policy"; mkdir -p "$WS_HOOKS" "$WS_POLICY" "$WS/.claude"; cp "$ROOT/$HOOKS_DIR/agent-cap.js" "$ROOT/$HOOKS_DIR/scratch-guard.js" "$WS_HOOKS/"
printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"4","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"4"}}\n' > "$WS/.claude/settings.json"
( unset GIT_DIR GIT_WORK_TREE; cd "$WS" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
    && git config user.name t && git add -A && git commit -qm writer-split --no-verify )
write_limit_stub() { # limit
  printf 'class PolicyRefusal extends Error {}\nmodule.exports = { PolicyRefusal, readPolicy: () => ({ value: %s, source: "stub", reason: "stub" }) }\n' "$1" > "$WS_POLICY/policy-mirror.js"
}
WS_WRITER='{"tool_name":"Workflow","cwd":"'"$NODEDIR/writer-split"'","tool_input":{"script":"const SPEC_WRITERS = 6\nconst g = chunk(s, Math.ceil(s.length / SPEC_WRITERS)) // gov:fixed-writers\nconst r = await boundedParallel(g.map((x) => () => agent(x)), SPEC_WRITERS)"}}'
WS_VERIFIER='{"tool_name":"Workflow","cwd":"'"$NODEDIR/writer-split"'","tool_input":{"script":"const K = 6\nconst g = chunk(all, Math.ceil(all.length / K)) // gov:fixed-verifiers\nconst r = await boundedParallel(g.map((x) => () => agent(x)), 5)"}}'
write_limit_stub 4
run_limit_call "writer split: K 6 above a stub limit of 4 -> deny, naming the marker" 2 "$WS_WRITER" "$WS_HOOKS/agent-cap.js" 'gov:fixed-writers but its bounded split'
run_limit_call "writer split: ...and the K it read against that limit" 2 "$WS_WRITER" "$WS_HOOKS/agent-cap.js" 'resolves to 6, above the bound 4: runtime.agents-in-flight'
write_limit_stub 6
run_limit_call "writer split: K 6 at a stub limit of 6 -> allow (control)" 0 "$WS_WRITER" "$WS_HOOKS/agent-cap.js"
run_limit_call "verifier split: K 6 under a stub limit of 6 -> deny, against MAX_VERIFIERS" 2 "$WS_VERIFIER" "$WS_HOOKS/agent-cap.js" 'above the bound 5: MAX_VERIFIERS'
rm -f "$WS_POLICY/policy-mirror.js"
run_limit_call "writer split: no policy kit beside the hooks kit -> deny, against MAX_VERIFIERS" 2 "$WS_WRITER" "$WS_HOOKS/agent-cap.js" 'above the bound 5: MAX_VERIFIERS, as no policy kit'

# ---- rule 2: LENS PROSE IS NOT CODE (TOOL-aLexedStripper-2) --------------------------------------
# Every arm below is the SAME correct five-element lens array, fanned through the sanctioned helper.
# Only the English inside one prompt differs, and every one of them must ADMIT.
#
# THE PROVENANCE: five of these spellings DENIED against `agent-cap` 1.8, measured across both array
# shapes before the fix was wired — a literal `...` read as a spread by the array-literal guard, and
# an unmatched `[`, `]`, `)` or `}` read as bracket structure by the join-forward walk or by
# `topLevelArgs`. An adopter hit this and filed it as a gov ask; their diagnosis blamed apostrophes
# and prescribed U+2019, and both of those admit at 1.8 — which is why the apostrophe and U+2019 rows
# are here too, as the negative result.
#
# The ADMIT direction is the whole point of this group. A fixture set that only ever asserts denials
# cannot catch a guard that has become a blanket.

js "rule2 prose: a literal ... in a prompt is not a spread" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows ... then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched [ in a prompt is not an array" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows [see the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched ] in a prompt does not close the array" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows], then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched ) in a prompt does not shift the depth" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows), then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched } in a prompt does not close the element" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows}, then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: apostrophes and an em dash, the adopter's stale diagnosis" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `check S2's rows and the table's keys — then stop` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: SIX lenses still deny, whatever the prose" 2 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `list the rows ... then the table` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
  { key: "f", prompt: `six` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# ---- rule 2: an interpolation holds CODE, and both directions are checked ------------------------
# `blankLiterals` blanks `${…}` bodies. Rule 2 may not, or an `agent(` written inside one becomes
# invisible to the only rule that bounds it. The multi-line shape is the one a per-line span view
# cannot reach: its `}` is not on its opening line.

js "rule2 interp: an unbounded fan inside a single-line interpolation denies" 2 <<'EOF'
const all = args.everything
const r = `x: ${await Promise.all(all.map((f) => agent(f.p)))}`
return r
EOF

js "rule2 interp: an unbounded fan inside a MULTI-line interpolation denies" 2 <<'EOF'
const all = args.everything
const report = `results: ${await Promise.all(
  all.map((f) => agent(f.prompt))
)}`
return report
EOF

js "rule2 interp: a BOUNDED fan inside an interpolation still admits" 0 <<'EOF'
const L = [{a:1},{a:2},{a:3},{a:4},{a:5}]
const r = `res: ${await boundedParallel(L.map((x) => () => agent(x)), 5)}`
return r
EOF

# ---- rule 2: template-literal edges (TOOL-aLexedStripper-2 S2, TOOL-aLexedStripper-5) ------------
# A nested template must BALANCE, or the fallback path fires on a legal script. A backtick that this
# file cannot model — inside a regex literal, a string, or a comment — must not change a verdict:
# the fallback returns the pre-change view, so these are the shipped hook's own answers.

js "rule2 edges: a nested template balances and admits" 0 <<'EOF'
const n = `a${`b`}c`
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a regex literal admits a legal harness" 0 <<'EOF'
const re = /`/
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick in a regex character class admits" 0 <<'EOF'
const re = /[`~]/g
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a quoted string admits" 0 <<'EOF'
const s = "a ` b"
const t = 'c ` d'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a comment admits" 0 <<'EOF'
// a stray ` in a line comment
/* and one ` in a block comment */
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# THE FAIL-OPEN THIS GROUP EXISTS FOR. An unterminated template literal blanks everything below it
# under a naive template-aware view, hiding the fan entirely. The fallback denies it because the
# shipped hook denies it — which is the property, not a coincidence.
js "rule2 edges: an unbounded fan below an unterminated backtick still denies" 2 <<'EOF'
const stray = `an unterminated template literal
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF


# The same class in the OTHER field-count regime. A stray `)` drives topLevelArgs' depth negative and
# every comma AFTER it then counts at top level, so denial depends on how many commas follow -- i.e.
# on how many fields each element has. A one-field array is denied only when the prose sits in the
# LAST element; a two-field one is denied wherever it sits. Both regimes are here because a fixture
# in one of them measures the other wrongly, which is how two independent grids disagreed on `)`.
js "rule2 prose: one-field element, stray ) in the LAST element" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { prompt: `one` },
  { prompt: `two` },
  { prompt: `three` },
  { prompt: `four` },
  { prompt: `list the rows), then the table` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# The other end of the same rule: a `)` with no comma after it inside its element was ALWAYS harmless,
# so this arm admits at BASE too. It is here to pin the boundary, not the fix -- without it the group
# only ever asserts the denying side and cannot notice the guard becoming a blanket.
js "rule2 prose: a stray ) at the very end of the prose was never a denial" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `the rows, then the table)` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF


# ---- renderCodeView: the FAIL-OPEN arms (TOOL-aLexedStripper-5) ----------------------------------
# Every arm here is a script the SHIPPED hook denies, and each one was ADMITTED by some revision of
# renderCodeView before it reached this file. They exist because two closing-review rounds found a
# fail-open in this view and the first repair was measured insufficient for the second shape. A view
# that blanks anything can hide a fan-out; these are the shapes that proved it.

js "renderCodeView: an unbounded fan below an unterminated block-comment opener denies" 2 <<'EOF'
const x = 1 /* never closed
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF

js "renderCodeView: a regex-borne /* closed by a later ordinary */ denies" 2 <<'EOF'
const re = /\/*/
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
const d = a */ b
EOF

# The apostrophe inside a regex literal. The view used to run to end of line and synthesize a closer
# the source never had, taking the fan on that line with it.
js "renderCodeView: an apostrophe in a regex does not swallow the fan on its line" 2 <<'EOF'
const all = args.everything
if (/won't/.test(args.s)) await Promise.all(all.map((f) => agent(f.prompt)))
EOF

js "renderCodeView: the same line without the apostrophe denies too (control)" 2 <<'EOF'
const all = args.everything
if (/wont/.test(args.s)) await Promise.all(all.map((f) => agent(f.prompt)))
EOF

js "renderCodeView: an unpaired double quote does not swallow the fan on its line" 2 <<'EOF'
const all = args.everything
if (x === 5") await Promise.all(all.map((f) => agent(f.prompt)))
EOF



# ---- TOOL-dMispairedQuote-1: a quote pairs with the WRONG partner ---------------------------------
# Every arm below was staged RED against the tip before it landed. The defect: each of this file's
# string views pairs a quote with the next quote of the same kind on the line, so an apostrophe in
# prose earlier on that line pairs with the quote opening `agent('a'` and the span blanked between
# them carries the fan-out. `addc6169` already demanded a matching PAIR; a pair exists, and it is the
# wrong one. The construct holding the apostrophe is not the mechanism -- these arms carry a regex, a
# double-quoted string, a block comment and a template literal, and the shipped hook admitted all
# four. The CONTROL beside each is the same line with the apostrophe removed.

# Rule 1's seven arms here, a raw `parallel` beside a prose apostrophe, retired with that rule in TOOL-dGroundRules-10
# (TOOL-dGroundRules-10); the defect they pinned is a view's, and rule 2's and rule 5's arms keep it.
js "mispaired quote: rule 2 counter loses the agent( -> deny" 2 <<'EOF'
const re = /won't/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)
EOF

js "mispaired quote: rule 2 control, no apostrophe -> deny" 2 <<'EOF'
const re = /wont/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)
EOF

# ---- and the ADMIT direction, which is half the class -------------------------------------------
# A fixture group that only ever asserts denials cannot catch a fail-closed that has become a
# fail-open. Each of these passes at the tip and must keep passing.

js "mispaired quote: aLexedStripper-5's own fixture stays legal -> allow" 0 <<'EOF'
const SEP = /[`]/
const all = ['a','b']
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF

# ---- TOOL-dMispairedQuote-3: no denial may be LOST ------------------------------------------------
# Correcting what counts as a string literal does not only un-hide fan-outs; it un-hides every other
# character the old mispairing was blanking, and rules 2, 3 and 5 walk brackets and balance parens
# ACROSS lines. Three DENY-to-ADMIT moves were reproduced against unit 1 alone. Each has a fixture
# here, and each was ALSO closed by the property arm below -- which is what makes the property worth
# its bytes: the next repair to these views inherits it without knowing these three shapes.

# Its four fixtures here hit rule 3 (a width of 50) and rule 1 (a raw primitive), which retired in TOOL-dGroundRules-10
# (TOOL-dGroundRules-10); three of them stay in the property's population below as expected losses.

# ---- TOOL-aRepatriatedFork-7 S3: the NESTED-INTERPOLATION matrix ---------------------------------
# A nested `${` zeroed the ONE depth counter the lexed view kept, so a brace open around an inner
# template -- an object literal, a block, an arrow body -- closed the OUTER interpolation at its own
# `}` and every fan-out after it left the view. a7c78ad2 admitted four of these five nested forms at
# exit 0 through the sanctioned helper, where the raw-text rule has no reason to fire. `depth-two`
# opens no brace and is the class's control. Every nested form and its flat control must be denied
# BY THE VERIFY-STAGE RULE, asserted on its text: an exit code alone cannot tell rules apart. The
# files also join the S9 property population below (F3), so no BASE denial among them can be lost.
mkdir -p "$TMP/nest"
NEST_HELPER='async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}'
NEST_FAN='await boundedParallel(findings.map((g) => () => agent(g)), 5)'
write_nest_pair() { # name nested-script flat-script, FAN standing for the unbounded verify stage
  printf '%s\n%s\n' "$NEST_HELPER" "${2//FAN/$NEST_FAN}" > "$TMP/nest/$1.js"
  printf '%s\n%s\n' "$NEST_HELPER" "${3//FAN/$NEST_FAN}" > "$TMP/nest/$1-flat.js"
}
write_nest_pair depth-two 'const s = `a ${ `b ${ x } c` + FAN } d`' 'const s = `a ${ 1 + FAN } d`'
write_nest_pair depth-three 'const s = `a ${ f({ k: `b ${ g({ m: `c ${ y } d` }) } e` }) + FAN } z`' 'const s = `a ${ f({ k: 1 }) + FAN } z`'
write_nest_pair object-before-inner 'const s = `a ${ f({ k: `b ${ x } c` }) + FAN } d`' 'const s = `a ${ f({ k: 1 }) + FAN } d`'
write_nest_pair arrow-body 'const s = `a ${ [1].map((v) => { return `b ${ v } c` }).join("") + FAN } d`' 'const s = `a ${ [1].map((v) => { return v }).join("") + FAN } d`'
write_nest_pair multi-line 'const s = `a ${ f({ k: `b ${ x } c` })
  + FAN
} d`' 'const s = `a ${ f({ k: 1 })
  + FAN
} d`'
nest_n=0
for f in "$TMP"/nest/*.js; do
  [ -f "$f" ] || continue
  nest_n=$((nest_n+1))
  n=$(basename "$f" .js)
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":open(sys.argv[1],encoding="utf-8").read()}}))' "$f")
  printf '%s' "$payload" | (cd "$TMP" && run_fan) >/dev/null 2>"$TMP/err"; rc=$?
  if [ "$rc" = 2 ] && grep -qF 'spawns one agent per item' "$TMP/err"; then
    echo "ok   nesting matrix: $n -> denied by the verify-stage rule"; pass=$((pass+1))
  else
    echo "FAIL nesting matrix: $n exited $rc without the verify-stage denial"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1))
  fi
done
if [ "$nest_n" = 10 ]; then
  echo "ok   nesting matrix: all 10 fixtures were written and judged"; pass=$((pass+1))
else
  echo "FAIL nesting matrix: $nest_n fixture(s) judged, want 10 -- a matrix that judged fewer certifies shapes it never saw"; fail=$((fail+1))
fi

# ---- S9: THE PROPERTY. No script this hook denied at BASE may be admitted now. --------------------
# The population is every tracked file PLUS the fixtures below. The second half is not padding:
# unit 1 alone flips ZERO tracked files, because every reproduced shape is synthetic. A property arm
# whose population holds no instance of the class it guards can only ever pass.
if [ -s "$TMP/base-hook.js" ]; then
  mkdir -p "$TMP/nrfix"
  # TOOL-dGroundRules-10: `backtick-in-regex.js` and `exposed-backtick.js` (rule 3, a width of 50) and
  # `template-borne-comment.js` (rule 1) are denied at BASE by rules TOOL-dGroundRules-10 retired, so each prints a
  # `RETIRED rule <n>` line and is never counted as lost.
  # TOOL-dFoldedVerdict-4 S7. The FIRST is the ratified path: BASE denies it, this hook admits it, and
  # deleting the marker restores the denial — which is what makes the loss marker-attributed rather
  # than merely tolerated. The SECOND is the control: an unmarked braceless loop that BOTH hooks deny,
  # so the affordance is proven scoped to the marker and not to loops in general.
  cat > "$TMP/nrfix/seq-marked-bounded.js" <<'EOF'
const MAX = 5
const units = [1, 2, 3, 4, 5]
const out = []
for (const u of units) { // gov:sequential-agents(MAX)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
  cat > "$TMP/nrfix/seq-unmarked-braceless.js" <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) out.push(await agent('do ' + u, { label: 'u' }))
EOF
  cat > "$TMP/nrfix/backtick-in-regex.js" <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /it's`don't/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF
  cat > "$TMP/nrfix/exposed-backtick.js" <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /a'b`c/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF
  cat > "$TMP/nrfix/template-borne-comment.js" <<'EOF'
const p = `see 'http://x' now`; await parallel(all.map(f))
EOF
  # TOOL-aRepatriatedFork-7 F3: the nesting matrix joins the population, so no fixture of it that BASE
  # denied -- every flat control, and `depth-two` -- may be admitted now.
  cp "$TMP"/nest/*.js "$TMP/nrfix/" 2>/dev/null || true
  # ONE NODE FOR THE WHOLE PROPERTY (TOOL-aSparedSpawn-11 S1, owner ruling F1 (a)). The loop below
  # used to be Python starting `node` per population file and per hook, about 3700 processes and
  # most of this suite's wall clock. The runner compiles each hook ONCE as a `vm.Script` and runs every
  # payload in a FRESH context with the hook's own CommonJS arguments: the real `require`, except that
  # `fs.readFileSync(0)` returns the payload; a `process` whose `exit` records the FIRST code and
  # throws a sentinel; and an `argv` naming the hook as `node <hook>` would. An uncaught throw is 1,
  # as real node exits, and a return with no exit is 0. The cwd and environment are this shell's, as
  # the Python loop's were. What it reads is unchanged: every `git ls-files` path split on
  # whitespace, plus the fixtures; each body decoded as UTF-8 with universal newlines, as Python's
  # `read_text` did; admission is `exit != 2`; the ratification re-run strips every marker token;
  # zero denials or zero ratifications red. The parity arm after it is the guard against the one
  # risk this buys: an in-process verdict that real node would not give.
  # THE CURRENT SIDE IS THE TWO HOMES (TOOL-dFairHearing-16): rules 2 and 5 left the hook, so "now"
  # denies a script when check-verifier-fanout.js or check-review-join.js finds in it, each loaded ONCE
  # as a module over the hook copy and run in this process; the parity mode holds that verdict to
  # both CLIs run as node runs them. BASE is still the hook blob, run as a vm script.
  cat > "$TMP/nr.js" <<'JSEOF'
'use strict'
const fs = require('fs')
const path = require('path')
const vm = require('vm')
const Module = require('module')
const cp = require('child_process')
const [mode, baseHook, curHook, fanJs, joinJs, root, fixdir, strideArg] = process.argv.slice(2)
const BOUND_MS = 120000
const STOP = { stop: 'process.exit' }
// The rules TOOL-dGroundRules-10 retired, by the opening text of their BASE denial.
const RETIRED = [[1, 'raw parallel()/pipeline()'], [3, 'a bound is written here that this file cannot resolve']]

function loadHook(file) {
  const abs = path.resolve(file)
  // A hashbang is legal only at the very start of a script, and the wrapper below is not the start.
  // Blanking the line keeps every line number the hook's own.
  const src = fs.readFileSync(abs, 'utf8').replace(/^#!.*/, '')
  const wrapped = '(function (exports, require, module, __filename, __dirname, process, console) {' + src +
    '\n}).apply(__nrArgs[0], __nrArgs)'
  return { abs, script: new vm.Script(wrapped, { filename: abs }), req: Module.createRequire(abs) }
}

function runInProcess(hook, payload, flags = []) {
  let code = null
  let err = ''
  // Both views proxy an EMPTY target and read the real object inside the trap, so no proxy invariant
  // ties a returned value to a non-configurable property of the real `fs` or `process`.
  const fsView = new Proxy({}, {
    get: (_t, k) => (k === 'readFileSync'
      ? (fd, ...rest) => (fd === 0 ? payload : fs.readFileSync(fd, ...rest))
      : fs[k]),
    has: (_t, k) => k in fs,
  })
  const req = (id) => (id === 'fs' || id === 'node:fs' ? fsView : hook.req(id))
  const sink = { write: () => true }
  // STDERR IS RECORDED (TOOL-dGroundRules-10): a BASE denial is named by its opening text.
  const errSink = { write: (t) => { err += String(t); return true } }
  const proc = new Proxy({}, {
    get: (_t, k) => {
      if (k === 'exit') return (c) => { if (code === null) code = c === undefined ? 0 : c; throw STOP }
      if (k === 'argv') return [process.execPath, hook.abs, ...flags]
      if (k === 'stdout') return sink
      if (k === 'stderr') return errSink
      const v = process[k]
      return typeof v === 'function' ? v.bind(process) : v
    },
    has: (_t, k) => k in process,
  })
  const quiet = { log() {}, error() {}, warn() {}, info() {}, debug() {} }
  const mod = { exports: {} }
  const ctx = vm.createContext({ __nrArgs: [mod.exports, req, mod, hook.abs, path.dirname(hook.abs), proc, quiet] })
  try {
    hook.script.runInContext(ctx, { timeout: BOUND_MS })
  } catch (e) {
    if (e !== STOP && code === null) {
      if (e && e.code === 'ERR_SCRIPT_EXECUTION_TIMEOUT') throw new Error('TIMEOUT after ' + BOUND_MS + ' ms')
      code = 1
    }
  }
  return { code: code === null ? 0 : code, err }
}

function runSpawned(hook, payload) {
  const r = cp.spawnSync(process.execPath, [hook.abs], { input: payload, timeout: BOUND_MS, stdio: ['pipe', 'ignore', 'ignore'] })
  return r.status === null ? 'killed' : r.status
}

function readBody(p) {
  try {
    return fs.readFileSync(p, 'utf8').replace(/\r\n?/g, '\n')
  } catch {
    return null
  }
}

// THE PAYLOAD CWD IS THE FIXTURE DIR, which no checkout holds (TOOL-aSweptBar-1 S3). With no `cwd` the
// hook falls back to this checkout, whose `.claude/roles.json` arms rule 6 against every inline script,
// so every BASE denial read as a rule 6 denial and nothing was ratified. Under no checkout rule 6 stays
// unarmed, and so does rule 7 (TOOL-dGroundRules-10), and the property compares the script rules with
// BASE, which predates both.
function buildPayload(body) {
  return JSON.stringify({ tool_name: 'Workflow', cwd: path.resolve(fixdir), tool_input: { script: body } })
}

const tracked = cp.execFileSync('git', ['-C', root, 'ls-files'], { encoding: 'utf8', maxBuffer: 1 << 28 })
  .split(/\s+/).filter(Boolean).map((f) => path.join(path.resolve(root), f))
const fixtures = fs.readdirSync(fixdir).filter((f) => f.endsWith('.js')).sort().map((f) => path.join(fixdir, f))
const base = loadHook(baseHook)
const fan = require(path.resolve(fanJs))
const join = require(path.resolve(joinJs))
fan.loadHook(curHook)
join.loadHook(curHook)
// "Now": 2 when either home finds in the body, as the hook exited 2 on either rule; else 0.
function runHomes(body) {
  return fan.scanFanout(body).length || join.scanJoin(body).length ? 2 : 0
}
// The same verdict from each CLI as node runs it, over the body written to a scratch file.
function runHomeClis(body) {
  const f = path.join(fixdir, '.parity-body.txt')
  fs.writeFileSync(f, body)
  const codes = [fanJs, joinJs].map((js) => {
    const r = cp.spawnSync(process.execPath, [js, '--hook', curHook, f], { timeout: BOUND_MS, stdio: ['ignore', 'ignore', 'ignore'] })
    return r.status === null ? 'killed' : r.status
  })
  if (codes.includes(1)) return 2
  return codes.every((c) => c === 0) ? 0 : 'refused ' + codes.join('/')
}

try {
  if (mode === 'property') {
    const lost = []
    const ratified = []
    const retired = []
    let denied = 0
    let n = 0
    for (const p of tracked.concat(fixtures)) {
      const body = readBody(p)
      if (body === null) continue
      const payload = buildPayload(body)
      const a = runInProcess(base, payload)
      n += 1
      if (a.code !== 2) continue
      denied += 1
      const b = runHomes(body)
      // ADMISSION IS `exit != 2`, not `exit == 0`: the hook BLOCKS only on 2, so a crash is an admission too.
      if (b !== 2) {
        // AN EXPECTED LOSS (TOOL-dGroundRules-10): BASE denied it by a rule this unit retired, named by the
        // denial's opening text. BASE runs rule 2 before both, so that text means rule 2 admitted it
        // there, and BASE under `--only=join` must admit it too, so a rule-5 denial is never hidden
        // behind a retired one. Never counted as lost.
        const rule = RETIRED.find(([, text]) => a.err.startsWith('BLOCKED by agent-cap: ' + text))
        if (rule && runInProcess(base, payload, ['--only=join']).code !== 2) {
          retired.push('RETIRED rule ' + rule[0] + ': ' + p)
          continue
        }
        // CLASS-SCOPED RATIFICATION (TOOL-dFoldedVerdict-4): denial restored by stripping every marker
        // token means the marker bought the loss; anything else is a regression.
        const r = runHomes(body.split('gov:sequential-agents').join(''))
        if (r === 2) ratified.push(p + ' (exit ' + b + ', denial restored by removing the marker)')
        else lost.push(p + ' (exit ' + b + ')')
      }
    }
    for (const f of retired) console.log(f)
    for (const f of lost) console.log('LOST a denial: ' + f)
    for (const f of ratified) console.log('RATIFIED a marker-attributed loss: ' + f)
    console.log('population ' + n + ' scanned, ' + denied + ' denied at BASE, ' + lost.length +
      ' denial(s) lost, ' + ratified.length + ' ratified, ' + retired.length + ' retired-rule loss(es) excluded')
    process.exitCode = lost.length || denied === 0 || ratified.length === 0 ? 1 : 0
  } else if (mode === 'parity') {
    // ponytail: a fixed stride over the sorted tracked list keeps the sample a handful of spawns; a
    // narrower stride buys coverage at about a second per spawn on a Windows node.
    const stride = Number(strideArg)
    const sample = fixtures.slice()
    const sorted = tracked.slice().sort()
    for (let i = 0; i < sorted.length; i += stride) sample.push(sorted[i])
    const bad = []
    let compared = 0
    let denies = 0
    for (const p of sample) {
      const body = readBody(p)
      if (body === null) continue
      const payload = buildPayload(body)
      for (const [name, inProc, real] of [
        ['BASE hook', runInProcess(base, payload).code, runSpawned(base, payload)],
        ['current homes', runHomes(body), runHomeClis(body)]]) {
        compared += 1
        if (real === 2) denies += 1
        if (inProc !== real) bad.push(name + ' on ' + p + ': in-process exit ' + inProc + ', node exit ' + real)
      }
    }
    for (const b of bad) console.log('DISAGREE ' + b)
    console.log('parity ' + compared + ' verdict(s) compared over ' + sample.length + ' payload(s), ' +
      denies + ' deny verdict(s) from real node, ' + bad.length + ' disagreement(s)')
    process.exitCode = bad.length || denies === 0 ? 1 : 0
  } else {
    console.log('nr.js: unknown mode ' + mode)
    process.exitCode = 2
  }
} catch (e) {
  console.log('nr.js: ' + (e && e.message ? e.message : String(e)))
  process.exitCode = 1
}
JSEOF
  node "$TMP/nr.js" property "$TMP/base-hook.js" "$HOOK" "$FANJS" "$HERE/check-review-join.js" "$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)" "$TMP/nrfix" > "$TMP/nr.out" 2>&1
  if [ $? = 0 ]; then
    echo "ok   no-regress: no denial lost against BASE ($(tail -1 "$TMP/nr.out"))"; pass=$((pass+1))
  else
    echo "FAIL no-regress: a denial the BASE hook made is gone"; sed 's/^/     /' "$TMP/nr.out"; fail=$((fail+1))
  fi
  # S2 — PARITY: every fixture above plus every 400th tracked path, through the in-process runner AND
  # through a real `node` per hook. Any disagreement reds naming the payload, and so does a sample in
  # which real node denied nothing, since a parity over admissions alone cannot see an exit stub that
  # drops its code.
  node "$TMP/nr.js" parity "$TMP/base-hook.js" "$HOOK" "$FANJS" "$HERE/check-review-join.js" "$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)" "$TMP/nrfix" 400 > "$TMP/nrp.out" 2>&1
  if [ $? = 0 ]; then
    echo "ok   no-regress parity: the in-process runner agrees with real node ($(tail -1 "$TMP/nrp.out"))"; pass=$((pass+1))
  else
    echo "FAIL no-regress parity: the in-process runner and real node disagree"; sed 's/^/     /' "$TMP/nrp.out"; fail=$((fail+1))
  fi
else
  echo "skip no-regress property arm — the BASE blob does not resolve in this tree, so there is no shipped hook to compare verdicts against"
fi


# ---- closing-review folds: a guard that times out, or crashes, does not guard --------------------
# A PreToolUse hook is NON-BLOCKING when it times out AND when it exits 1. Both were reachable.

# F1. `checkLiteralOpen` copied the whole line prefix per quote, so cost was quadratic in LINE
# length and every ordinary `return 'x'` paid it. Measured before the fix: 253 KB on one line took
# 33.8 s against 62 ms at BASE. This arm is a RATIO against a CONTROL, never a typed ceiling
# (TOOL-aSparedSpawn-15 S1): the same 8000 literals ONE PER LINE are timed first, in this process,
# and the one-line run may take at most four times that plus 2 s, both read from EPOCHREALTIME. A
# loaded host slows both runs alike, so the verdict stops being a function of the box, while a walk
# that is quadratic in LINE length grows the one-line run only. The typed 10 s it replaced redded on
# a loaded node `a`, where one spawn costs 632 to 818 ms. The absolute hook timeout is NOT this arm's
# question: a slowdown linear in both runs is not the defect it guards. Both runs must ADMIT (exit
# 0), so a hook that crashed fast on either cannot pass the ratio by doing no work. EVERY LITERAL
# FOLLOWS `void`: the walk runs only for a quote glued to an identifier, and the `f(a1, 'lit1')`
# this arm used to time put a comma there, so the restored per-quote copy never ran and the arm
# could not fail on the regression it names. Measured on node `a`: with the copy restored the
# one-line run took 19 to 23 s against 0.9 to 1.3 s one per line; shipped, 0.3 to 0.9 s both ways.
long_one=$("$TESTPY" -c "
import json
n = 8000
line = 'const x = [' + ','.join(\"f(a%d, void 'lit%d')\" % (i, i) for i in range(n)) + ']'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': line}}))
")
long_ctl=$("$TESTPY" -c "
import json
n = 8000
body = 'const x = [' + chr(10) + (',' + chr(10)).join(\"f(a%d, void 'lit%d')\" % (i, i) for i in range(n)) + chr(10) + ']'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': body}}))
")
c0=${EPOCHREALTIME//[.,]/}
printf '%s' "$long_ctl" | (cd "$TMP" && run_fan) >/dev/null 2>&1; ctl_rc=$?
c1=${EPOCHREALTIME//[.,]/}
printf '%s' "$long_one" | (cd "$TMP" && run_fan) >/dev/null 2>&1; one_rc=$?
c2=${EPOCHREALTIME//[.,]/}
ctl_ms=$(( (10#$c1 - 10#$c0) / 1000 )); one_ms=$(( (10#$c2 - 10#$c1) / 1000 )); lim_ms=$(( 4 * ctl_ms + 2000 ))
if [ "$ctl_rc" != 0 ] || [ "$one_rc" != 0 ]; then
  echo "FAIL quadratic ratio: the hook exited $one_rc on ONE line and $ctl_rc one per line, not 0 for both, so the timing compares runs that did not do the work"; fail=$((fail+1))
elif [ "$one_ms" -le "$lim_ms" ]; then
  echo "ok   quadratic ratio: 8000 literals on ONE line in ${one_ms} ms against ${ctl_ms} ms one per line (<= 4x + 2000 = ${lim_ms} ms)"; pass=$((pass+1))
else
  echo "FAIL quadratic ratio: 8000 literals on ONE line took ${one_ms} ms against ${ctl_ms} ms one per line (> 4x + 2000 = ${lim_ms} ms) — a walk quadratic in line length is back, and a hook that times out is NON-BLOCKING"; fail=$((fail+1))
fi

# F2. A throw in the corrected views must not become an admission. This script drives
# `parseBranches` past its recursion limit, which is PRE-EXISTING: the BASE hook exits 1 on it and
# therefore does not block. Denying is stricter than BASE and is this file's stated posture.
deep=$("$TESTPY" -c "
import json
k = ' ? args.big : '.join('c%d' % i for i in range(9000))
sc = 'const K = ' + k + ' : args.big // gov:fixed-verifiers\nawait boundedParallel(K.map((g) => () => agent(g)), 5)'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': sc}}))
")
printf '%s' "$deep" | (cd "$TMP" && run_fan) >/dev/null 2>&1; deeprc=$?
if [ "$deeprc" = 2 ]; then
  echo "ok   crash posture: a script neither view can scan is DENIED, not admitted at exit 1"; pass=$((pass+1))
else
  echo "FAIL crash posture: a script neither view can scan exited $deeprc — only 2 blocks"; fail=$((fail+1))
fi



rm -rf "$FIX_A" "$FIX_B" "$FIX_C" "$FIX_D"

# Rule 2's moved arms count on their own pair, and fail the verdict like any other arm.
echo "---- rule 2's arms: $pass passed, $fail failed ----"
fails=$((fails+fail))
if [ "$fails" = 0 ]; then echo "PASS — check-verifier-fanout: all arms held"; exit 0; fi
echo "FAIL — $fails arm(s) failed"
exit 1
