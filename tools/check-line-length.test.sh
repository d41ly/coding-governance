#!/usr/bin/env bash
# check-line-length.test.sh — the failing case for every branch the gate carries.
#
# PORTED ONTO `<prefix>/lib/lib-selftest.sh` by TOOL-aQuenchedHarness-6, with the arm inventory
# unchanged — same labels, same staged breaks, same expected verdicts, diffed before and after by
# `bash <prefix>/lib/extract-arms.sh`. Read that harness's header for why the shape is
# declare-then-run rather than run-as-you-go; what is worth knowing HERE is what the port removed.
#
# THE COST WAS NEVER THE GATE, IT WAS THE FIXTURE. Traced at 36 s / 432 lines
# (`memory/builds/aQuenchedHarness/build/2026-09-07-build-TOOL-aQuenchedHarness-5-candidate-test.md`),
# the outer script spawned 31 `python3` — every one of them building a line of repeated characters,
# 18 of those inside a `reset` that ran before every arm. At 773 ms a python spawn on this fleet that
# is ~24 s of the 36 s, spent on strings the shell can build with no process at all. `build_line`
# below is that, in builtins; the line files are built ONCE into the fixture; and each arm now
# copies a snapshot instead of mutating one shared directory.
#
# THE PROPERTY THAT MADE THE OLD SHAPE UNPARALLELISABLE, kept as a warning against restoring it: the
# suite reused ONE scratch repo and `reset` mutated it between arms, so two arms running at once
# landed the second's setup inside the first's subject invocation. Per-arm isolation is what buys the
# pool; the pool is not an optimisation on top of it.
#
# THE HARNESS RUNS SETUP AND THE SUBJECT SEPARATELY, and that is not a style choice. An earlier draft
# ran `sh -c 'setup; gate; cleanup'` and read the rc of the CLEANUP — so every red arm reported 0 and
# the suite would have certified a gate that never fired. Setup happens first, the subject runs
# alone, and its rc is the one compared.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-line-length.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"
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
_rkd_py=$(resolve_python) || { echo "check-line-length.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
LIB_DIR=$(resolve_kit_dir "$_rkd_py" lib lib-selftest.sh "$HERE") || exit 2
LIB="${LIB_DIR##*/}"
# The policy kit, whose budgets.py answers the switch (TOOL-dGroundRules-9): copied into the fixture
# by the one arm that runs the gate WITH it, under its resolved name.
POLICY_DIR=$(resolve_kit_dir "$_rkd_py" policy budgets.py "$HERE") || exit 2
POLICY="${POLICY_DIR##*/}"
ROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "check-line-length.test: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2
. "$ROOT/$LIB_DIR/lib-selftest.sh"

GATE="$HERE/check-line-length.sh"
[ -f "$GATE" ] || { echo "check-line-length.test: no gate at $GATE"; exit 2; }

# THE SUITE STILL DECLARES ITS OWN ARM COUNT. The floor moved into the harness so eighteen ported
# suites do not carry eighteen copies of the guard, but the NUMBER is this suite's and stays here.
SELFTEST_FLOOR=20

# build_line <char> <n> — <n> copies of <char>, in builtins. `printf -v` and parameter expansion
# cost no process; this one function is where the 31 python spawns went. It is UTF-8 safe by construction:
# the replacement is the argument, so an em dash lands as one character per space.
build_line() { local pad; printf -v pad "%${2}s" ""; printf '%s\n' "${pad// /$1}"; }

# The fixture is the state the old suite's `reset` produced — a subject the gate passes on and a
# declaration naming it — plus every line file the arms need, built once instead of per arm.
build_repo() {
  mkdir -p "./${PFX}" L || return 2
  git init -q . >/dev/null 2>&1 || return 2
  git config user.email t@t && git config user.name t || return 2
  cp "$GATE" ${PFX}check-line-length.sh || return 2
  build_line x 100 > subject.md
  printf 'subject.md\t450\n' > ${PFX}line-length-limits.txt
  build_line y 451 > L/y451
  build_line y 450 > L/y450
  build_line y 300 > L/y300
  build_line y 600 > L/y600
  build_line y 10  > L/y10
  build_line — 400 > L/em400
  printf '%s\n' '```' > L/fence
  # The interpreter dies AFTER the resolver's probe accepted it — the shape a resolver cannot catch.
  printf '#!/usr/bin/env bash\n[ "$1" = "-c" ] && exit 0\nexit 4\n' > deadpy
  chmod +x deadpy
  # The policy kit's reader and a policy file at `warn`, staged aside: only the switch arm moves them in.
  mkdir -p P/kit P/gov || return 2
  for f in budgets.py policy.py caps.toml catalogue.toml; do cp "$ROOT/$POLICY_DIR/$f" P/kit/ || return 2; done
  printf '[budgets]\nenforce = "warn"\n' > P/gov/policy.toml
}
build_fixture build_repo || exit 2

arm "control · a short subject passes" 0 "0 over 450" \
    'true' 'bash '"${PFX}check-line-length.sh"''

# The `want` strings for red arms are each the branch's ENTIRE literal signature up to its first
# interpolation, which the harness meta-gate requires. An arm asserting a readable prefix keeps
# passing after the sentence it was written for is rewritten around it, and the branch quietly loses
# its only proof.
arm "an over-length line reds naming the line and its length" 1 "a subject carries line(s) over its limit of" \
    'cat L/y451 >> subject.md' 'bash '"${PFX}check-line-length.sh"''

# THE SWITCH (TOOL-dGroundRules-9). The gate copy has no policy kit beside it in the fixture, so a
# breach refuses as it did before and says why once; the arm after it moves the policy kit in beside
# the copy and commits a policy file at `warn` on main, the landed revision of a repository with no
# remote, and the same breach prints BUDGET WARN and passes.
arm "with no policy kit beside the gate a breach refuses as before, saying so" 1 \
    "no policy kit answered, so a breach refuses as before" \
    'cat L/y451 >> subject.md' 'bash '"${PFX}check-line-length.sh"''

arm "under budgets.enforce warn an over-length line prints BUDGET WARN and passes" 0 \
    "BUDGET WARN — line-length · subject.md · 451 chars over 450" \
    'cat L/y451 >> subject.md && mkdir -p .governance '"${PFX}${POLICY}"' && cp P/kit/* '"${PFX}${POLICY}"'/ && cp P/gov/policy.toml .governance/ && git symbolic-ref HEAD refs/heads/main && git add -A && git commit -qm landed --no-verify' \
    'bash '"${PFX}check-line-length.sh"''

arm "exactly at the limit passes" 0 "0 over 450" \
    'cat L/y450 >> subject.md' 'bash '"${PFX}check-line-length.sh"''

# ---------------------------------------------------------------- resolution order
arm "the DECLARATION beats the environment" 1 "limit of 200" \
    'printf "subject.md\t200\n" > '"${PFX}line-length-limits.txt"'; cat L/y300 >> subject.md' \
    'LINE_MAX=9999 bash '"${PFX}check-line-length.sh"''

arm "an UNDECLARED subject honours the environment" 1 "resolved from the environment" \
    'cat L/y300 > other.md' 'LINE_MAX=200 bash '"${PFX}check-line-length.sh"' other.md'

arm "an undeclared subject with no environment falls through to 450" 0 "limit from the default" \
    'cat L/y300 > other.md' 'bash '"${PFX}check-line-length.sh"' other.md'

arm "a POSITIONAL beats the declaration" 1 "resolved from a positional" \
    'cat L/y300 >> subject.md' 'bash '"${PFX}check-line-length.sh"' subject.md 200'

# ---------------------------------------------------------------- the exemption, and its boundary
arm "a long line INSIDE a fence does not red" 0 "0 over 450" \
    '{ cat L/fence; cat L/y600; cat L/fence; } >> subject.md' 'bash '"${PFX}check-line-length.sh"''

arm "a long line inside a TABLE does red" 1 "characters" \
    '{ printf "| "; cat L/y600; } >> subject.md' 'bash '"${PFX}check-line-length.sh"''

# ---------------------------------------------------------------- measurement and declaration hygiene
arm "a non-ASCII line is measured in CHARACTERS, not bytes" 0 "0 over 450" \
    'cat L/em400 >> subject.md' 'bash '"${PFX}check-line-length.sh"''

arm "a row naming an ABSENT path reds as stale" 1 \
    "the declaration names a subject that does not exist, so its row excuses nothing and is stale" \
    'printf "subject.md\t450\ngone.md\t450\n" > '"${PFX}line-length-limits.txt"'' \
    'bash '"${PFX}check-line-length.sh"''

arm "a NON-NUMERIC limit is a named failure, not a shell error" 1 \
    "the declared line limit for this subject is not a number, so the comparison below would be against text: '" \
    'printf "subject.md\tlots\n" > '"${PFX}line-length-limits.txt"'' \
    'bash '"${PFX}check-line-length.sh"''

arm "a declaration selecting NO subject is cannot-run" 2 "would grade nothing" \
    'printf "# only a comment\n" > '"${PFX}line-length-limits.txt"'' \
    'bash '"${PFX}check-line-length.sh"''

# ---------------------------------------------------------------- certify-without-measuring
# THE FOUR ARMS BELOW ARE ONE CLASS: the gate printed `line-length OK … 0 over 0 characters` and
# exited 0 in every one of them. `over` is empty on a clean subject and empty on a crashed scanner,
# and the shell discarded the status that told them apart. Each arm asserts a NON-ZERO verdict, so a
# regression cannot pass by printing the right words.
arm "a non-numeric POSITIONAL limit is a named failure, not a certified zero" 1 \
    "the line limit is not a number, so nothing could be compared against it: '" \
    'cat L/y300 >> subject.md' 'bash '"${PFX}check-line-length.sh"' subject.md abc'

arm "a non-numeric LINE_MAX is a named failure, not a certified zero" 1 \
    "the line limit is not a number, so nothing could be compared against it: '" \
    'cat L/y10 > other.md' 'LINE_MAX=abc bash '"${PFX}check-line-length.sh"' other.md'

# A subject whose every line sits inside a fence measures ZERO lines. Empty-population is the
# vacuity this tree bans by name: the old gate printed OK over a file it graded nothing in.
arm "a subject with NO gradeable line is a dead probe, not a clean verdict" 1 \
    "the scanner reached no gradeable line in this subject, so a clean verdict would certify a measurement that never happened" \
    '{ cat L/fence; cat L/y600; cat L/fence; } > subject.md' 'bash '"${PFX}check-line-length.sh"''

arm "a scanner that dies mid-run is a named failure, not a certified zero" 1 \
    "the offender scan did not run for this subject, so no line was measured and OK would be a lie" \
    'true' 'LINELEN_PY=$PWD/deadpy bash '"${PFX}check-line-length.sh"''

# THE INSTALL-DAY PAIR, and the two must land on DIFFERENT verdicts. The kit withholds the
# declaration on purpose — gov's rows name gov's paths, and a row naming an absent path is a stale
# red — so ABSENT is the shape every adopter starts in, and the exit 2 it used to get there was the
# very failure the withholding was made to prevent. Measured in a scratch install before this arm
# existed. Its neighbour above is what stops this one being read as "an empty population is fine".
arm "an ABSENT declaration is NOT ADOPTED at exit 0, not a red install day" 0 \
    "NOT ADOPTED — no declaration at" \
    'rm -f '"${PFX}line-length-limits.txt"'' 'bash '"${PFX}check-line-length.sh"''

run_arms check-line-length.test.sh
