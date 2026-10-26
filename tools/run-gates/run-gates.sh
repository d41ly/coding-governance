#!/usr/bin/env bash
# run-gates.sh — the coding-governance merge bar: run every gate this repo dogfoods, report per leg.
# The full bar green at the push boundary; earlier runs scoped. Exit 0 = all passed · 1 = one or more failed · 2 = must run from the repo, or REFUSED · 3 = TREE MOVED · 4 = HOST.
# TREE MOVED: no leg failed, but the tree changed while the bar ran, so no verdict describes it; a failed leg outranks it.
# HOST: every failed leg timed out twice, the second time alone, while one spawn cost more than GATE_HOST_RATIO
# times this clone's floor. First match wins: 2 REFUSED, 1 RED, 4 HOST, 3 TREE MOVED, 0 GREEN, and exit 0 needs
# a reported leg line AND a written verdict file (TOOL-dDerivedDocket-26).
# A STALE GENERATED OUTPUT IS REFUSED before the queue, exit 2 (TOOL-aPrimedIndex-3): every output a kit
# descriptor stages is proved fresh by `regen.py --check` and none is regenerated here. GATE_REGEN_CHECK=0
# skips it; a guard-scoped leg may then let a stale output through, so the push bar scrubs that knob.
#   bash <prefix>/run-gates/run-gates.sh --regen | --regen-check | --regen-list   # the verb, no bar
#   bash <prefix>/run-gates/run-gates.sh             # legs run CONCURRENTLY, at the width
#                                                    # <prefix>/run-gates/gate-profiles.txt declares
#                                                    # for the detected cores and RAM
#   GATE_JOBS=1 bash <prefix>/run-gates/run-gates.sh # one worker — the serial bar, through this same pool
#   GATE_PROFILE=<row> bash …                        # select a table row by name, skipping detection
#   GATE_PROFILES=<path> bash …                      # read a different table; an absent path falls
#                                                    # back to the built-in formula (the rollback)
#   GATE_ATTRIBUTE=<rev> bash …                      # re-run each RED leg at <rev> and say whose red
#                                                    # it is: OWN, INHERITED, MIXED, CONTENDED or
#                                                    # DEAD PROBE. REPORT-ONLY: no exit code moves
# Legs live in the manifest DERIVED below as this kit dir's sibling (single source); this runner is
# a thin iterator over it and holds no leg command of its own.
#
# THIS RUNNER GRADES ITSELF, and that predates the red attribution (TOOL-dDerivedDocket-23): every
# verdict below is rendered by this file, so an edit here can move what any leg reads as and no leg
# can see it. The attribution does not fix that and refuses to compound it (KF3): when the diff
# between its base and the working tree touches this runner, `gate-fingerprint.sh`, the pre-push
# hook or `lib-attribute.sh`, every red reads OWN and says why. Nobody grades their own grader.
#
# Legs run through a bounded worker pool. They are safe to run together
# because each heavy leg is already hermetic — it builds its own `mktemp -d` scratch repo, sets git
# config only inside it, and never writes into the real tree. Execution order is a scheduling detail;
# REPORTING is always manifest order, so the output is byte-stable whatever the width.
set -u
KIT_RUN_GATES_VERSION=1.43   # gov:kit run-gates@1.43
# 1.40 -> 1.41: the kit ships `measure_legs.py`, a gate profiler that runs every manifest leg clean and
# unbounded, each in its own Windows Job Object, with its fixtures and its `measure-legs selftest` leg
# (TOOL-dRedressedBar-18). This runner's behaviour does not move; the profiler reads its text.
# 1.30 + 1.30 -> 1.31: merging local main's reconcile (a30f4589) into aGraftedHelix. Both lines bumped
# 1.29 -> 1.30 with different bytes, so the number alone could not tell the two kits apart.
# 1.29 -> 1.30: the shard-join comment in run-selftests.sh stops justifying its unported reverse half
# by a suite this declaration called whole; the driver suite is sharded rows now (TOOL-aGraftedHelix-41).
# 1.28 + 1.27 -> 1.29: the reconcile with origin/main 290d0d2d5. Both lines moved the kit from 1.24, so
# each spelled its own 1.25 onward: this branch's notes are first, then main's, each under its own numbers.
# 1.27 -> 1.28: every repair the runner makes on its own appends one line to the health log under the
# git common dir (TOOL-aGraftedHelix-8): the `health_log_sh` block, inlined byte-identical, and seven sites.
# 1.26 -> 1.27: the same unit's follow-up moved the kit's bytes after 1.26 was cut — its suites' bars
# run with the pause off and its prose stops restating the table's figures; no behaviour moved.
# 1.25 -> 1.26: the profile knob `mempause`, on every shipped row: dispatch HOLDS while used memory
# is above it and a leg runs (TOOL-aGraftedHelix-7). The run record gains `pauses`, the verdict
# `paused` and `paused_s`, the header and `--print-profile` `mempause`, the profile line a field, and
# stdout one `memory:` line; a table carrying the knob is refused by a runner older than this one.
# 1.24 -> 1.25: every `.leg` row gains an eighth field, `foreign`, from a census of foreign gate work
# taken while the legs run, and the header gains `census_every` (TOOL-aGraftedHelix-5). A reader that
# splits a row by position keeps working; one that reads the seventh field with a trailing catch-all
# variable folds the eighth into it, which is why the ledger block's read gained one.
# --- origin/main's line from 1.24, numbered as it landed there:
# 1.27 -> 1.28: the runner deletes the retired `gate-timings.tsv` from its git dir and the common dir
# (TOOL-aMendedFleet-72); no verdict moves.
# 1.24 -> 1.25: the manifest's NINTH field, `doc_reads`, and the docs mode `GATE_DOCS_BASE` that reads
# it (TOOL-dThriftyLanding-1); a full green is also shared through the common git dir
# (TOOL-dThriftyLanding-2). The canary's key-set pin admits the new key, which is the floor the
# deployer reads before it emits one.
# 1.21 -> 1.22: KITREL is asked of git when the prefix strip leaves it absolute, the MSYS mount
# spelling (`/tmp/x` beside git's `C:/…/Temp/x`) the `cd … && pwd` fold does not reach; with it the
# attribution's KF3 matched nothing for a tree under `/tmp`. Absorbed by aSightedSkeptic.
# 1.8 -> 1.9: both sides of the origin/main merge into dDerivedDocket shipped a 1.8 - theirs the
# run log below, ours red attribution (GATE_ATTRIBUTE, lib-attribute.sh and the manifest's eighth
# field `signature`, TOOL-dDerivedDocket-23). 1.9 carries both, and neither moves a verdict.
# 1.7 -> 1.8: every bar appends one line to the run log under the git common dir, from the EXIT trap
# (TOOL-dLoggedFlight-3). No manifest key, profile knob or stdout line moves, so neither direction of
# a skew between the runner and its table or manifest changes a verdict.
# 1.0 -> 1.1: the manifest gained `subject`, and the canary's pinned key set gained it with
# the runner. A target below 1.1 REDS on a leg row carrying the key, so govkit withholds it
# there rather than breaking a bar it was only passing through. TOOL-dUnstalledConvoy-26.
# 1.4 -> 1.5: `gate-profiles.txt` gained the `wall` knob and the runner gained `KNOWN_KNOBS`
# entry for it. THE SKEW IS ASYMMETRIC AND FATAL IN ONE DIRECTION: a 1.4 runner reading a 1.5
# table hits `prof_die` on the first row and exits 2 having run ZERO legs -- every bar, not
# some. A 1.5 runner reading a 1.4 table is fine, because an absent knob defaults. The two
# files ship in one kit and one `include = "**"` rule, so an ordinary apply moves them
# together; what is NOT covered is a partial update or a hand copy of one file, and unlike the
# 1.1 case above no govkit floor was written to withhold the table. TOOL-aQuenchedHarness-1.
# THIS SCRIPT'S OWN DIRECTORY, RESOLVED BEFORE THE `cd`. A relative `$0` is relative to the caller's
# cwd, so deriving it after `cd "$ROOT"` resolves it against the repo root instead: invoked as
# `bash ../<prefix>/run-gates/run-gates.sh` from a subdirectory the kit dir collapsed to the root, the
# manifest to `./gate-legs.json`, and the runner ran ZERO legs. Captured here, used below.
KITDIR=$(cd "$(dirname "$0")" && pwd)
# AN ABSOLUTE ARGV, BY RE-EXECUTING THROUGH THE PATH JUST RESOLVED (TOOL-dDerivedDocket-25 S4). The
# process-monitor fence attributes a process by its command line, and `bash <prefix>/run-gates/…`
# carries a RELATIVE one that no declared root can reach, so a killed runner's tree could not be
# reaped by it (TOOL-aReapedSpinner-14). Every leg subshell is a FORK of this process and inherits
# the argv, so fixing it here fixes it for all of them and for every caller at once, the operator's
# own catalogued invocation included. `exec` keeps the pid, so a caller holding it loses nothing, and
# it runs before any output, lock or scratch exists. The loop guard is the absolute `$0` itself. A
# `$0` naming no file beside the kit dir (a runner fed on stdin) is left alone rather than exec'd
# into a path that does not exist. `-x` is carried because an exec'd bash would otherwise drop it.
case "$0" in
  /*) ;;
  *) if [ -f "$KITDIR/${0##*/}" ]; then
       case "$-" in *x*) exec "${BASH:-bash}" -x "$KITDIR/${0##*/}" "$@" ;; esac
       exec "${BASH:-bash}" "$KITDIR/${0##*/}" "$@"
     fi ;;
esac
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "run-gates: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
# THE BAR'S GIT FACTS, ASKED ONCE (TOOL-aSparedSpawn-4 S7). The git dir, the common dir and HEAD were
# five separate `rev-parse` spawns, every one made from this directory after the `cd` above, and no
# later `cd` runs in this shell, so one call here answers each with the value it read. Each consumer
# keeps its own normalisation. An UNBORN branch prints both dirs and exits 1 with no HEAD line, so a
# nonzero status reads as an empty HEAD rather than as the literal word a bare `rev-parse HEAD` echoes.
# The header's `worktree` is `ROOT`, which `--show-toplevel` above already answered from here.
RG_GIT_DIR=""; RG_COMMON_RAW=""; RG_HEAD=""
_rg_facts=$(git rev-parse --git-dir --git-common-dir --verify -q HEAD 2>/dev/null); _rg_rc=$?
if [ -n "$_rg_facts" ]; then
  RG_GIT_DIR=${_rg_facts%%$'\n'*}
  case "$_rg_facts" in *$'\n'*) _rg_facts=${_rg_facts#*$'\n'}; RG_COMMON_RAW=${_rg_facts%%$'\n'*} ;; esac
  case "$_rg_facts" in *$'\n'*) [ "$_rg_rc" = 0 ] && RG_HEAD=${_rg_facts#*$'\n'} ;; esac
fi
unset _rg_facts _rg_rc
# `--hold -- <command…>` (TOOL-aFrugalTurnstile-5 S6): how a bar that is NOT this runner joins the
# host turnstile. Parsed here, before anything reads `$1`: the words are kept in `TS_HOLD` and the
# positional arguments cleared, so no verb test below can mistake a held command for its own. The
# run then takes the turnstile like a bar and runs the words right after `gate queue: acquired`.
TS_HOLD=()
if [ "${1:-}" = "--hold" ]; then
  if [ "${2:-}" != "--" ] || [ "$#" -lt 3 ]; then
    echo "run-gates: --hold needs a command: run-gates.sh --hold -- <command…>" >&2; exit 2
  fi
  shift 2; TS_HOLD=("$@"); set --
fi
# The python-launcher resolver, INLINED byte-identically from resolve-python.sh in gov's lib dir. This
# kit is deployable (the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/`), and gov's lib dir is gov-internal and never travels:
# sourcing it made this runner exit 2 with zero legs run in any tree that did not have it.
# The resolver parity gate derives its copy population by grepping for the marker below, so this
# copy enrols itself. Do not edit it here. (That gate's own script path is deliberately NOT
# spelled in this file: the canary forbids a leg's script path appearing in the runner, and it
# is right to — a comment naming one is one edit away from an inlined leg command.)
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
        # way to the direct executable where the probe named a file, so a consumer never spawns
        # the Windows App Execution Alias again; the launcher's own name otherwise.
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
    echo "resolve_python: tried:$_rp_tried"
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
  } >&2
  return 1
}
# <<< resolve_python

# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. It is read here ONCE, by a builtin, into `RKD_PROGRAM`, and never run by a python of its
# own: the legs-parse program below runs it ahead of the manifest, so the process-monitor kit dir
# costs a bar no python spawn (TOOL-aSparedSpawn-4 S10). The `|| :` is owed because `read -d ''`
# returns 1 at the end of its input.
RKD_PROGRAM=""
IFS= read -r -d '' RKD_PROGRAM <<'RKD' || :
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
PYBIN=$(resolve_python) || { echo "run-gates: no usable python — required to parse the leg manifest"; exit 2; }
# ---- THE THREE REGEN VERBS hand over before any bar machinery exists (TOOL-aPrimedIndex-2 S6) -----
# `regen.py`, beside this runner, regenerates or proves fresh every generated output the kits
# declare. These spellings exist so the one command a refusal names needs no python launcher of
# the reader's own: the interpreter is the one just resolved, and the cwd is the toplevel above.
case "${1:-}" in
  --regen)       exec "$PYBIN" "$KITDIR/regen.py" --write ;;
  --regen-check) exec "$PYBIN" "$KITDIR/regen.py" --check ;;
  --regen-list)  exec "$PYBIN" "$KITDIR/regen.py" --list ;;
esac
fails=0; n=0; skips=0; ondemands=0

# The leg manifest, overridable so a fixture can drive this runner without re-running the real bar.
# Without a seam here the only way to exercise run-gates.sh is to invoke it against the repo, which
# re-runs the whole bar recursively and clobbers the live gate-last-summary.txt mid-run -- so the
# evidence guarantee below had no way to be tested at all (TOOL-dNomadicAtlas-1).
# The manifest is the kit dir's SIBLING, derived rather than spelled: this kit installs at
# <prefix>/run-gates/ and a hardcoded path to gate-legs.json at gov's prefix resolves to nothing at any other
# prefix. GATE_LEGS still outranks the derivation (the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` S3).
# Both sides are normalised through the SAME `cd ... && pwd` chain before the strip. Under MSYS one
# directory has two spellings — `git rev-parse --show-toplevel` answers `C:/...` and `pwd` answers
# `/c/...` — and a prefix strip across the two flavours silently leaves an ABSOLUTE path, which then
# resolves to nothing. Never compare path strings across flavours.
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
# AND A MOUNT IS A THIRD SPELLING THAT `cd … && pwd` DOES NOT FOLD. Under MSYS a tree reached through
# `/tmp` stays `/tmp/x` while the same directory reached through git's `C:/…/Temp/x` answers
# `/c/…/Temp/x`, so the strip above left KITREL ABSOLUTE and every comparison against git's
# repo-relative paths (KF3 among them) matched nothing. Measured: the canary's AC5 fixture under
# `mktemp -d` read INHERITED where it must read OWN. Git answers in ONE spelling, so ask it; the strip
# stays as the fallback for a kit dir git cannot place.
case "$KITREL" in
  /*) _kr=$(unset GIT_DIR GIT_WORK_TREE; cd "$KITDIR" && git rev-parse --show-prefix 2>/dev/null) && [ -n "$_kr" ] && KITREL=${_kr%/} ;;
esac
LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"
# THE ATTRIBUTION BASE IS THIS BAR'S AND NO LEG'S. Read once and removed from the environment, so a
# leg that runs a bar of its own over a fixture — the canary does, many times — never inherits a base
# that names a commit of THIS repository and attributes its fixture's reds against nothing.
ATTR_REV=${GATE_ATTRIBUTE:-}
unset GATE_ATTRIBUTE
# THE INHERITED-RED POLICY THIS BAR WAS HANDED, and the age bound it ages an INHERITED leg under
# (TOOL-dDerivedDocket-24). Read once and removed for the base's reason above: a leg that drives a
# nested bar over a fixture must not inherit this repository's policy. The runner DECIDES nothing
# with either. The bound sizes the age probe, and the policy only permits the `gate-inherited-green`
# stamp to be WRITTEN; both readers that act on a red — the pre-push hook and the unattended driver —
# read the policy at R themselves, so a caller exporting `land` buys a stamp nobody honours without a
# read of its own. A bound that is not a positive integer, a leading zero included, asks for no age.
ATTR_POLICY=${GATE_INHERITED_RED:-}
ATTR_MAX_AGE=${GATE_INHERITED_RED_MAX_AGE:-}
unset GATE_INHERITED_RED GATE_INHERITED_RED_MAX_AGE
case "$ATTR_MAX_AGE" in ''|0*|*[!0-9]*) ATTR_MAX_AGE="" ;; esac
# WHAT THE HELD TIER WAS ASKED FOR, as every record of this run states it (TOOL-aSparedSpawn-12 S7):
# empty when held, `changed` when only the legs whose kit moved run, `1` for any other non-empty
# value. A `changed` run is never written as `1`, so a partial tier is never recorded as the whole one,
# and `.githooks/pre-push` predicate 8 forces a self-tests-on push over such a record unedited.
SELFTESTS_STAMP=${GATE_SELFTESTS:+1}
[ "${GATE_SELFTESTS:-}" = changed ] && SELFTESTS_STAMP=changed

# ---- durable per-leg evidence (TOOL-dNomadicAtlas-1) --------------------------------------------
# leg() already holds every leg's merged output in $out and PRINTS it on failure, then keeps only the
# ROW for the durable summary. The reason is in scope at the exact line the durable record is built,
# and dropped there -- so a `| tail` still loses the WHY while keeping the WHICH. adopter ic hit this for
# real: a red leg inside a push piped through `tail -45`, unidentifiable afterwards, and the
# reflexive re-run passed, so the evidence was gone for good.
#
# Resolved ONCE, and a path is never composed from an empty root: `git rev-parse --git-dir` yields
# nothing outside a repo, and composing "/gate-logs/<leg>.log" from that would write outside the tree.
# Read from the bar's one `rev-parse` above (TOOL-aSparedSpawn-4 S7).
GD=$RG_GIT_DIR
LOGDIR=""
if [ -n "$GD" ] && mkdir -p "$GD/gate-logs" 2>/dev/null; then
  LOGDIR="$GD/gate-logs"
  chmod 700 "$LOGDIR" 2>/dev/null || true
else
  echo "run-gates: evidence capture OFF (no usable git dir) — leg output is stdout-only this run" >&2
fi

# NAME -> LEG_LOG, the log path, or rc 1 when capture is off. The name maps byte by byte, so a
# multibyte character becomes one underscore PER BYTE, as the `tr -c` it replaced mapped it; the C
# locale is what makes the expansion see bytes, and it is local, so the caller's locale returns with
# the function. It leaves its answer in a global because a `$(leg_log …)` was a fork per call, and the
# `printf | tr` inside it two more (TOOL-aSparedSpawn-4 S3).
leg_log() {
  local LC_ALL=C
  [ -n "$LOGDIR" ] || return 1
  LEG_LOG="$LOGDIR/${1//[!A-Za-z0-9._-]/_}.log"
}
# A leg's output can carry an operator-exported credential; mask URL userinfo before it becomes
# durable. Terminal output was ephemeral, a file is not.
redact() { sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g'; }
# write_redacted <file> <text> — <text> into <file> as `printf '%s' <text> | redact` writes it
# (TOOL-aSparedSpawn-4 S4): through `sed` when it holds `://` and then `@`, the shape of every
# credential `redact` masks, and by a builtin otherwise. The guard is a SUPERSET test, so it can only
# send more text through `sed` than needs it, never less. Text holding a CRLF goes through `sed` too,
# because what `sed` does to one is the host's: under MSYS it reads its pipe in text mode and drops the
# CR of every CRLF, on Linux it keeps it, and only `sed` itself gives either host its own bytes.
write_redacted() {
  case "$2" in
    *://*@*|*$'\r\n'*) printf '%s' "$2" | redact > "$1" ;;
    *) printf '%s' "$2" > "$1" ;;
  esac
}

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
# Baseline for conditional legs: the mainline tip we gate against. Override with GATE_BASE.
# Unresolvable (no remote / shallow / detached) → empty, and changed() fails safe to "run".
# The remote and its branch are the ladder's above (TOOL-dLadderedRemote-2): this read a literal
# remote name, so on a node whose remote is named after the project every scoped run became a full
# one. A ladder refusal is announced once and then takes the same fail-safe.
if ! resolve_remote_sh && [ -z "${GATE_BASE:-}" ]; then
  echo "run-gates: no scope base — $RR_WHY Every guarded leg runs." >&2
fi
# The OBSERVED branch, never GOV_DEFAULT_BRANCH: an environment value must not move the scope base
# a guarded leg is skipped against (TOOL-aStandingWrit-5's class), and this read never consulted it.
DEFBR=$RR_OBSERVED
# What the evidence row `base_from` records when no GATE_BASE is given: a ladder refusal, no remote at
# all, or the remote and branch the base came from — three answers, never one spelling for two.
if [ -n "$RR_WHY" ]; then BASE_FROM_LADDER=ladder-refused
elif [ -z "$RR_REMOTE" ]; then BASE_FROM_LADDER=no-remote
else BASE_FROM_LADDER="$RR_REMOTE/${DEFBR:-main}"; fi
# THE BASE IS THE BRANCH POINT, not the remote tip, so a branch is graded on what IT changed
# rather than on everything that landed while it was open. The merge-base is used only where it
# is a PROPER ANCESTOR of HEAD; otherwise the remote tip stands.
#
# That fallback is not a nicety. An earlier draft REFUSED the base whenever the merge-base equalled
# HEAD, on the reasoning that the merge-base is degenerate on the default branch itself. The
# refusal cannot tell that case from a fresh branch cut off a fast-forwarded `main` — which is the
# commonest scoped-run state in this repository — and in both it fell back to running all 86 legs.
# Worse, it would have red the shipped canary on landing: that harness points its fixture remote at
# HEAD, so merge-base == HEAD there and the arm expecting `GATE skip  guarded` would have lost its
# skip. The origin tip handles both correctly, because `changed()` diffs BASE against the WORKING
# TREE and therefore still sees uncommitted edits.
BASE=
if [ -n "${GATE_BASE:-}" ]; then
  # An explicit base OUTRANKS the derivation, unchanged. It is the escape hatch for exactly the
  # cases no derivation gets right.
  BASE=$(git rev-parse --verify -q "$GATE_BASE" 2>/dev/null) || BASE=
else
  _tip=
  [ -z "$RR_REMOTE" ] || _tip=$(git rev-parse --verify -q "refs/remotes/$RR_REMOTE/${DEFBR:-main}" 2>/dev/null) || _tip=
  if [ -n "$_tip" ]; then
    _mb=$(git merge-base HEAD "$_tip" 2>/dev/null) || _mb=
    _head=$RG_HEAD            # the bar's one `rev-parse`, the same `--verify -q HEAD` (TOOL-aSparedSpawn-4 S7)
    if [ -n "$_mb" ] && [ "$_mb" != "$_head" ]; then BASE=$_mb; else BASE=$_tip; fi
  fi
fi
# GATE_FULL bypasses every guard, so the run checks the whole bar. `.githooks/pre-push` sets it: a
# guard may scope ANY run now, including the authoritative one — and the property that used to make
# that safe was `.githooks/pre-push` forcing GATE_FULL=1 on every push. That force is gone; what
# replaces it is a BOUNDED, RECORDED obligation in the hook, which forces a total run when no
# recorded full green covers the pushed tip, when it is more than a declared number of commits
# behind, when its tree fingerprint does not reproduce at the sha it names, or when the leg
# manifest itself moved. So a too-narrow guard costs an early signal for at most that many
# commits, rather than never being caught — and it is the hook, not this line, that is now the
# thing to read. Both fail-safes below keep their meaning: an unresolvable BASE runs everything,
# early signal rather than a wrong merge verdict. Both fail-safes below keep their meaning — an
# unresolvable BASE runs everything, and so does a guard that errors.
changed() { [ -n "${GATE_FULL:-}" ] && return 0; [ -z "$BASE" ] && return 0; ! git diff --quiet "$BASE" -- "$@" 2>/dev/null; }

# THE DOCS MODE (TOOL-dThriftyLanding-1). `GATE_DOCS_BASE=<rev>` says every path this run's push
# changed since <rev> is in the repository's declared doc class, so a leg that DECLARES which doc paths
# it reads (`doc_reads`) runs only when one of them moved. `.githooks/pre-push` sets it on a doc-only
# push and scrubs it from the environment on every other; a developer may set it by hand to ask the
# same question locally. GATE_FULL outranks it: a run that asked for the whole bar gets the whole bar.
# Unresolvable, it is OFF and says so, because a mode that silently fails to engage reads exactly
# like one that engaged and found nothing to skip.
DOCS_BASE=""
if [ -n "${GATE_DOCS_BASE:-}" ] && [ -z "${GATE_FULL:-}" ]; then
  DOCS_BASE=$(git rev-parse --verify -q "${GATE_DOCS_BASE}^{commit}" 2>/dev/null) || DOCS_BASE=""
  [ -n "$DOCS_BASE" ] || echo "run-gates: GATE_DOCS_BASE '${GATE_DOCS_BASE}' resolves to no commit, so the docs mode is OFF and every leg is decided as usual" >&2
fi
# READ ONCE, THEN WITHHELD FROM EVERY LEG. A leg that drives a nested runner over its own scratch repo
# would otherwise inherit a sha that does not exist there and print the OFF line into output it
# compares; the mode is a fact about THIS run, and no leg has a use for it.
unset GATE_DOCS_BASE
# A DOC PATH MOVED when it differs between DOCS_BASE and the working tree, OR when any commit in
# DOCS_BASE..HEAD touched it. The second half is not redundant: a path changed in one commit and
# restored in a later one has no net diff, and a leg that grades COMMITS (a pass-order or brief rule)
# still has something to grade. `--full-history` is load-bearing (TOOL-dThriftyLanding-8): without it
# git simplifies away a `--no-ff` merge's side branch that nets to nothing on these paths, and every
# landing here is such a merge. Every failure reads as MOVED, so the leg runs: the one direction this
# predicate may err in is doing more work.
check_doc_moved() {
  local hit
  [ -n "$DOCS_BASE" ] || return 0
  ! git diff --quiet "$DOCS_BASE" -- "$@" 2>/dev/null && return 0
  hit=$(git log --full-history --format=%h -1 "$DOCS_BASE..HEAD" -- "$@" 2>/dev/null) || return 0
  [ -n "$hit" ]
}

# ONE git-dir resolution for the whole runner. `GD` above and a second `gd` here used to resolve the
# same thing twice; the run record adds four more git-dir-rooted paths, and four paths hanging off
# whichever of two variables an author happened to reach for is how a record ends up half in one
# place. `gd` survives as the name the surrounding code already reads.
gd="$GD"; sfile=""; LEDGER=""
[ -n "$gd" ] && { sfile="$gd/gate-last-summary.txt"; LEDGER="$gd/gate-ledger.tsv"; }
# The dispatch hint is READ from the ledger and no longer from a separate timing cache. Field 2 is
# still the duration, which is what keeps the manifest parser below unchanged.
TIMINGS="$LEDGER"
# MERGE NOTE: `leg()` is gone — the pool replaced it with runleg() (the worker) and report_one() (the
# reporter). TOOL-dNomadicAtlas-1's durable per-leg evidence is PORTED into both rather than dropped:
# the log write lives in runleg(), which is where $out and $rc are in scope, and the `log:` pointer
# lives in report_one(), which is where FAILED_LEGS is built. Writing from the worker is strictly
# better here — the writes are per-leg files and now happen concurrently.

# ---- hardware profiles (the profile-table unit) --------------------------------------------------
# The knobs are DECLARED in a table beside this runner rather than computed from core count alone: a
# 16-core / 8 GB VM used to select width 8 and thrash, because cores were the only question asked.
# Grammar and reasoning live in the table itself; this block reads it, selects a row, and applies it.
#
# THE GOVERNING INVARIANT: no knob may ever turn a leg into a PASS or a SKIP. A knob may make the bar
# slower, and it may turn an unbounded hang into a bounded RED. It may never make the bar check less.
# KNOWN_KNOBS is the whole implemented set; the canary PINS the same set separately, which is what
# stops a coverage knob being added without an author reading this paragraph.
# `slots` (TOOL-aPairedSlots-1) is how many bars the host turnstile admits at once. It schedules bars
# and never legs, so it sits inside the invariant: a bar admitted beside another runs every leg it
# would have run alone.
KNOWN_KNOBS="width timeout wall mempause spawnpause slots"
PROFILES="${GATE_PROFILES:-$KITREL/gate-profiles.txt}"
prof_die() { echo "run-gates: $*" >&2; exit 2; }

# LENGTH-BOUNDED BEFORE ANY ARITHMETIC. Both `[ "$v" -gt 0 ]` and `$(( ))` ERROR on an int64 overflow
# instead of comparing, which is how a 20-digit width value once span the dispatch loop forever
# having executed ZERO legs. 15 digits admits every real reading below (a byte count on a 900 TB box)
# and cannot overflow int64 even after one multiply. Zero is "unknown", never a valid reading.
num_ok() { case "$1" in ''|*[!0-9]*) return 1 ;; esac; [ ${#1} -le 15 ] || return 1; [ "$1" -gt 0 ]; }

# Every source is RUN and its output validated, never probed for existence — being on PATH is not
# evidence, the lesson gov's lib-dir resolve-python.sh records. Measured on node `a`: the three core
# sources all report 16, the page arithmetic and /proc/meminfo agree within 1 MB, and `sysctl` exits
# 127, which is the case the chain must survive and does. CORE_SRC/RAM_SRC accumulate what was TRIED,
# so the visibility line names the chain whether it answered on the first source or the third.
DET_CORES=0; DET_RAM=0; CORE_SRC=""; RAM_SRC=""
det_cores() {
  local v
  DET_CORES=0
  if [ -n "${GATE_CORES+x}" ]; then CORE_SRC="seam"; num_ok "${GATE_CORES}" && DET_CORES=${GATE_CORES}; return; fi
  CORE_SRC="nproc"
  v=$(nproc 2>/dev/null); if num_ok "$v"; then DET_CORES=$v; return; fi
  CORE_SRC="$CORE_SRC,getconf"
  v=$(getconf _NPROCESSORS_ONLN 2>/dev/null); if num_ok "$v"; then DET_CORES=$v; return; fi
  CORE_SRC="$CORE_SRC,env"
  v=${NUMBER_OF_PROCESSORS:-}; if num_ok "$v"; then DET_CORES=$v; return; fi
}
# The cgroup root, seamed so a fixture can drive the container path. Without a seam this source is
# untestable on a host that is not in a container, and an untestable source rots.
CGROUP_ROOT="${GATE_CGROUP_ROOT:-/sys/fs/cgroup}"
cgroup_ram_mb() {   # -> prints the ENFORCED limit in MB, or nothing
  local f v
  for f in "$CGROUP_ROOT/memory.max" "$CGROUP_ROOT/memory/memory.limit_in_bytes"; do
    [ -r "$f" ] || continue
    v=$(head -c 32 "$f" 2>/dev/null | tr -d '[:space:]')
    # `max` (v2's no-limit spelling) and v1's 9223372036854771712 sentinel are both UNKNOWN, not
    # readings. num_ok's 15-digit bound rejects the sentinel for us, which is the bound doing a second
    # job rather than a coincidence — a 19-digit byte count is not a memory size anybody has.
    num_ok "$v" || continue
    v=$(( v / 1048576 )); num_ok "$v" || continue
    printf '%s' "$v"; return 0
  done
  return 1
}
det_ram() {   # -> DET_RAM in MB
  local pages pgsz kb v
  DET_RAM=0
  if [ -n "${GATE_RAM_MB+x}" ]; then RAM_SRC="seam"; num_ok "${GATE_RAM_MB}" && DET_RAM=${GATE_RAM_MB}; return; fi
  RAM_SRC="getconf"
  pages=$(getconf _PHYS_PAGES 2>/dev/null); pgsz=$(getconf PAGESIZE 2>/dev/null)
  if num_ok "$pages" && num_ok "$pgsz"; then
    # Divide the PAGE SIZE first so the product stays small. A page under 1 KB truncates that divisor
    # to zero, which would report NO MEMORY — a reading, and a wrong one. Guarded, so it reports
    # UNKNOWN and falls through to the next source instead.
    kb=$(( pgsz / 1024 ))
    if [ "$kb" -gt 0 ]; then v=$(( pages * kb / 1024 )); if num_ok "$v"; then DET_RAM=$v; return; fi; fi
  fi
  RAM_SRC="$RAM_SRC,meminfo"
  v=$(awk '/^MemTotal:/ { print int($2 / 1024); exit }' /proc/meminfo 2>/dev/null)
  if num_ok "$v"; then DET_RAM=$v; return; fi
  RAM_SRC="$RAM_SRC,sysctl"
  v=$(sysctl -n hw.memsize 2>/dev/null)
  if num_ok "$v"; then v=$(( v / 1048576 )); if num_ok "$v"; then DET_RAM=$v; return; fi; fi
}
# THE ENFORCED LIMIT WINS OVER THE HOST READING, and the RAM guard is the reason. Every source above
# reports HOST physical memory, which inside a memory-capped container is not the number that decides
# whether eight scratch repos fit: a 4 GB CI runner on a 512 GB host reads 512 GB, selects the widest
# row, and thrashes — the exact case the table was written for, in the environment this bar is
# scheduled to move to. MIN rather than replace, so a bogus limit can only ever make the bar SLOWER,
# which is the fail-safe direction this whole block is built on.
det_ram_capped() {
  det_ram
  local lim
  # THE SEAM WINS. `det_ram` returns early with RAM_SRC=seam precisely to signal a bypass, and capping
  # it here handed the deciding vote back to ambient container state — in the arms written so the box
  # could not decide, and against the runner's own documented promise that the seam overrides the
  # reading. It also silently replaced the deliberate UNKNOWN of `GATE_RAM_MB=0`. The container guard
  # still covers every genuinely DETECTED reading, which is the only population it was argued for.
  [ "$RAM_SRC" = seam ] && return 0
  lim=$(cgroup_ram_mb) || return 0
  [ "$DET_RAM" = 0 ] && { DET_RAM=$lim; RAM_SRC="$RAM_SRC,cgroup"; return 0; }
  [ "$lim" -lt "$DET_RAM" ] && { DET_RAM=$lim; RAM_SRC="$RAM_SRC,cgroup"; }
  return 0
}

# >>> mempause_sh — canonical copy: run-gates.sh in this kit's dir (byte-identical; gated)
# THE MEMORY PAUSE (TOOL-aGraftedHelix-7). The width is chosen ONCE, from RAM, at start; nothing
# watched memory while the work ran. A dispatcher calls `check_dispatch_pause <running>` before each
# dispatch and HOLDS that dispatch while used memory sits above `MEMPAUSE` percent and something is
# still running. Both runners carry this block byte-identical, so it reads only what its caller set:
# `MEMPAUSE` (the threshold, 0 = off), `MEMPAUSE_INERT` (1 when the host gave no reading at start)
# and `MEMPAUSE_ROWS` (the run record's `pauses` file, empty for none). Builtins only, and the
# decision reads `MEMPAUSE_READ` rather than a command substitution, so a decision forks nothing.
# A HOLD ALWAYS ENDS: nothing polls, so each decision happens at a completion, and a hold is released
# when the reading falls (`fell`), when nothing runs (`drained`), when the reading vanishes
# (`unread`), or at the first completion after `MEMPAUSE_HOLD` seconds (`bound`); the caller closes
# one the wall's break left open as `wall`. The knob narrows a pool and never turns a leg into
# anything: under pressure that never falls the pool drains toward width 1 and keeps moving.
# A SECOND READING, ONE DECISION (TOOL-aSparedSpawn-2): the spawn pause holds on the same episode
# machinery while one spawn costs over `SPAWNPAUSE` times `SPAWNPAUSE_FLOOR` microseconds, the reading
# a builtin takes from the file `SPAWNPAUSE_NOW` names. Off unless the caller sets both the ratio and a
# floor. An episode records which reading held it, and its counters split by that: the memory ones
# above count what memory held, `SPAWNPAUSE_N` and `SPAWNPAUSE_HELD_S` what spawns held.
MEMPAUSE_HOLD=300
case "${GATE_MEMPAUSE_HOLD:-}" in ''|*[!0-9]*|???????*) ;; *) MEMPAUSE_HOLD=$((10#$GATE_MEMPAUSE_HOLD)) ;; esac
MEMPAUSE_N=0; MEMPAUSE_HELD_S=0; MEMPAUSE_READ=""; MEMPAUSE_PEAK=""; MEMPAUSE_OPEN=""; MEMPAUSE_OPEN_PEAK=0
MEMPAUSE_FELL=0; MEMPAUSE_BOUND=0; MEMPAUSE_DRAINED=0; MEMPAUSE_UNREAD=0; MEMPAUSE_WALL=0
MEMPAUSE_OPEN_BY=""; SPAWNPAUSE_N=0; SPAWNPAUSE_HELD_S=0; SPAWNPAUSE_READ=""; SPAWNPAUSE_PEAK=""
# read_mem_used — used memory as a whole percent, on stdout and in MEMPAUSE_READ; rc 1 and nothing
# when no source reads. The host half is `MemTotal` against `MemAvailable`, or `MemFree` where the
# file has none (on MSYS that IS Windows' available figure); the cgroup half is its usage over its
# limit, v2 then v1, with `max` and v1's 19-digit sentinel rejected as `cgroup_ram_mb` rejects them.
# The HIGHER wins: a wrong source can only make the bar slower, the direction `det_ram_capped` takes.
read_mem_used() {
  local f="${GATE_MEMINFO:-/proc/meminfo}" cg="${GATE_CGROUP_ROOT:-/sys/fs/cgroup}" k v _
  local tot="" av="" fr="" host="" grp="" lim="" use=""
  MEMPAUSE_READ=""
  if [ -r "$f" ]; then
    while read -r k v _; do
      case "$k" in MemTotal:) tot=$v ;; MemAvailable:) av=$v ;; MemFree:) fr=$v ;; esac
    done < "$f"
  fi
  [ -n "$av" ] || av=$fr
  case "$tot" in ''|*[!0-9]*|????????????????*) tot="" ;; esac
  case "$av" in ''|*[!0-9]*|????????????????*) av="" ;; esac
  if [ -n "$tot" ] && [ -n "$av" ] && [ "$((10#$tot))" -gt 0 ]; then
    tot=$((10#$tot)); av=$((10#$av)); [ "$av" -le "$tot" ] || av=$tot
    host=$(( (tot - av) * 100 / tot ))
  fi
  for k in memory.max:memory.current memory/memory.limit_in_bytes:memory/memory.usage_in_bytes; do
    lim=""; use=""
    { read -r lim < "$cg/${k%%:*}"; read -r use < "$cg/${k#*:}"; } 2>/dev/null
    case "$lim" in ''|*[!0-9]*|????????????????*) continue ;; esac
    case "$use" in ''|*[!0-9]*|????????????????*) continue ;; esac
    [ "$((10#$lim))" -gt 0 ] || continue
    grp=$(( 10#$use * 100 / 10#$lim )); [ "$grp" -le 100 ] || grp=100
    break
  done
  [ -n "$host$grp" ] || return 1
  v=${host:-$grp}; [ -n "$grp" ] && [ "$grp" -gt "$v" ] && v=$grp
  MEMPAUSE_READ=$v
  printf '%s\n' "$v"
}
# read_spawn_now — the spawn pause's reading, microseconds a spawn, in SPAWNPAUSE_READ from the file
# SPAWNPAUSE_NOW names; rc 1 and empty when that file is absent or holds no whole number.
read_spawn_now() {
  local v=""
  SPAWNPAUSE_READ=""
  { read -r v < "${SPAWNPAUSE_NOW:-}"; } 2>/dev/null || [ -n "$v" ] || return 1
  v=${v%$'\r'}
  case "$v" in ''|*[!0-9]*|?????????????*) return 1 ;; esac
  SPAWNPAUSE_READ=$(( 10#$v ))
}
# check_dispatch_pause <running> — rc 0 HOLDS the next dispatch, rc 1 lets it go. First match: both
# readings off or INERT; no reading over its threshold (`fell`, or `unread` when a live reading gave
# none, a spawn reading counted only once an episode it held is open, since the sampler's first tick
# comes a period after dispatch begins); nothing running (`drained`), so a hold never outlives the
# last job; an episode held MEMPAUSE_HOLD seconds or more (`bound`), tested only here, so it is
# released at the first decision after the bound; else hold, opening an episode when none is open.
check_dispatch_pause() {
  local mem=0 spawn=0 by="" gone=""
  { [ "${MEMPAUSE:-0}" -gt 0 ] && [ "${MEMPAUSE_INERT:-0}" = 0 ]; } && mem=1
  { [ "${SPAWNPAUSE:-0}" -gt 0 ] && [ -n "${SPAWNPAUSE_FLOOR:-}" ]; } && spawn=1
  [ "$mem$spawn" != 00 ] || return 1
  if [ "$mem" = 1 ]; then
    if read_mem_used >/dev/null; then
      { [ -z "$MEMPAUSE_PEAK" ] || [ "$MEMPAUSE_READ" -gt "$MEMPAUSE_PEAK" ]; } && MEMPAUSE_PEAK=$MEMPAUSE_READ
      [ -n "$MEMPAUSE_OPEN" ] && [ "$MEMPAUSE_READ" -gt "$MEMPAUSE_OPEN_PEAK" ] && MEMPAUSE_OPEN_PEAK=$MEMPAUSE_READ
      [ "$MEMPAUSE_READ" -gt "$MEMPAUSE" ] && by=memory
    else
      gone=1
    fi
  fi
  if [ "$spawn" = 1 ]; then
    if read_spawn_now; then
      { [ -z "$SPAWNPAUSE_PEAK" ] || [ "$SPAWNPAUSE_READ" -gt "$SPAWNPAUSE_PEAK" ]; } && SPAWNPAUSE_PEAK=$SPAWNPAUSE_READ
      [ "$SPAWNPAUSE_READ" -gt $(( SPAWNPAUSE * SPAWNPAUSE_FLOOR )) ] && by=${by:+$by+}spawn
    else
      case "$MEMPAUSE_OPEN_BY" in *spawn*) gone=1 ;; esac
    fi
  fi
  if [ -z "$by" ]; then
    if [ -n "$gone" ]; then write_pause_row unread; else write_pause_row fell; fi
    return 1
  fi
  if [ "${1:-0}" -le 0 ]; then write_pause_row drained; return 1; fi
  if [ -n "$MEMPAUSE_OPEN" ] && [ $(( EPOCHSECONDS - MEMPAUSE_OPEN )) -ge "$MEMPAUSE_HOLD" ]; then
    write_pause_row bound; return 1
  fi
  [ -n "$MEMPAUSE_OPEN" ] || { MEMPAUSE_OPEN=$EPOCHSECONDS; MEMPAUSE_OPEN_PEAK=${MEMPAUSE_READ:-0}; MEMPAUSE_OPEN_BY=$by; }
  case "$MEMPAUSE_OPEN_BY" in "$by"|memory+spawn) ;; *) MEMPAUSE_OPEN_BY=memory+spawn ;; esac
  return 0
}
# write_pause_row <ended-by> — closes the open episode, a no-op when none is open: one `pauses` row,
# `<started-s> TAB <ended-s> TAB <held-s> TAB <peak-pct> TAB <threshold> TAB <ended-by> TAB <held-by>`,
# when the caller set MEMPAUSE_ROWS, and the counters the summaries print either way. `<held-by>` is
# `memory`, `spawn` or `memory+spawn`, appended last so no positional reader moves; the memory
# counters take an episode memory held, the spawn pair one spawns held.
write_pause_row() {
  [ -n "$MEMPAUSE_OPEN" ] || return 0
  local now=$EPOCHSECONDS held
  held=$(( now - MEMPAUSE_OPEN ))
  case "$MEMPAUSE_OPEN_BY" in
    *spawn*) SPAWNPAUSE_N=$(( SPAWNPAUSE_N + 1 )); SPAWNPAUSE_HELD_S=$(( SPAWNPAUSE_HELD_S + held )) ;;
  esac
  case "$MEMPAUSE_OPEN_BY" in
    spawn) ;;
    *)
      MEMPAUSE_N=$(( MEMPAUSE_N + 1 )); MEMPAUSE_HELD_S=$(( MEMPAUSE_HELD_S + held ))
      case "$1" in
        fell) MEMPAUSE_FELL=$(( MEMPAUSE_FELL + 1 )) ;;
        bound) MEMPAUSE_BOUND=$(( MEMPAUSE_BOUND + 1 )) ;;
        drained) MEMPAUSE_DRAINED=$(( MEMPAUSE_DRAINED + 1 )) ;;
        unread) MEMPAUSE_UNREAD=$(( MEMPAUSE_UNREAD + 1 )) ;;
        *) MEMPAUSE_WALL=$(( MEMPAUSE_WALL + 1 )) ;;
      esac ;;
  esac
  if [ -n "${MEMPAUSE_ROWS:-}" ]; then
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$MEMPAUSE_OPEN" "$now" "$held" "$MEMPAUSE_OPEN_PEAK" \
      "${MEMPAUSE:-0}" "$1" "${MEMPAUSE_OPEN_BY:-memory}" >> "$MEMPAUSE_ROWS" 2>/dev/null || true
  fi
  MEMPAUSE_OPEN=""; MEMPAUSE_OPEN_PEAK=0; MEMPAUSE_OPEN_BY=""
}
# render_pause_summary — the ONE `memory:` line a run prints after its pool drains, on every run.
render_pause_summary() {
  if [ "${MEMPAUSE:-0}" -le 0 ]; then
    printf 'memory: pause off\n'
  elif [ "${MEMPAUSE_INERT:-0}" = 1 ]; then
    printf 'memory: no reading on this host, so the %s%% pause was INERT\n' "$MEMPAUSE"
  elif [ "$MEMPAUSE_N" = 0 ]; then
    printf 'memory: no pause  (peak %s%% used, threshold %s%%)\n' "${MEMPAUSE_PEAK:-?}" "$MEMPAUSE"
  else
    printf 'memory: %s pause(s), %ss held  (peak %s%% used, threshold %s%%; fell %s, bound %s, drained %s, unread %s, wall %s)\n' \
      "$MEMPAUSE_N" "$MEMPAUSE_HELD_S" "${MEMPAUSE_PEAK:-?}" "$MEMPAUSE" \
      "$MEMPAUSE_FELL" "$MEMPAUSE_BOUND" "$MEMPAUSE_DRAINED" "$MEMPAUSE_UNREAD" "$MEMPAUSE_WALL"
  fi
}
# <<< mempause_sh
# render_spawn_summary — the `spawn:` line, after the `memory:` line and only on a run whose row turned
# the spawn pause on, so a run that leaves it off prints exactly what it printed before
# (TOOL-aSparedSpawn-2). OUTSIDE the shared block: the self-test runner never sets the knob.
render_spawn_summary() {
  [ "${SPAWNPAUSE:-0}" -gt 0 ] || return 0
  if [ -z "${SPAWNPAUSE_FLOOR:-}" ]; then
    printf 'spawn: no spawn floor recorded, so the %sx pause was INERT\n' "$SPAWNPAUSE"
  elif [ "$SPAWNPAUSE_N" = 0 ]; then
    printf 'spawn: no pause  (peak %s us a spawn, threshold %sx the %s us floor)\n' \
      "${SPAWNPAUSE_PEAK:-?}" "$SPAWNPAUSE" "$SPAWNPAUSE_FLOOR"
  else
    printf 'spawn: %s pause(s), %ss held  (peak %s us a spawn, threshold %sx the %s us floor)\n' \
      "$SPAWNPAUSE_N" "$SPAWNPAUSE_HELD_S" "${SPAWNPAUSE_PEAK:-?}" "$SPAWNPAUSE" "$SPAWNPAUSE_FLOOR"
  fi
}

# >>> health_log_sh — canonical copy: health-log.sh in gov's lib dir (byte-identical; gated)
# I3, THE HEALTH LOG (TOOL-aGraftedHelix-8): `<git-common-dir>/health.log`, one LF-terminated UTF-8
# line per automatic self-heal, four TAB-separated fields: utc (`YYYY-MM-DDTHH:MM:SS+00:00`), source
# and event (each `^[a-z][a-z0-9-]*$`), and a detail whose TAB, CR and LF are each folded to one space
# and which is cut to 240 characters. At HEALTH_LOG_CAP_LINES lines the appender first keeps the
# newest half, through a temp file and a rename, then appends. `derive_health_log <common-dir>` prints
# the path and spawns nothing; `resolve_health_log <repo-dir>` asks git once and prints it, or fails
# printing nothing; `add_health_event <log> <source> <event> <detail>` is the only writer. A refused
# token, an empty path or a failed write prints ONE `health: NOTE -` line on stderr and returns 0: it
# never fails its caller. WHAT IT DOES NOT DO: serialize concurrent writers (a trim racing an append
# can lose that line; ponytail: one rename, a lock file if a lost line is ever observed); validate
# what a detail means; or tell a repository with no writer installed from one where nothing healed.
HEALTH_LOG_CAP_LINES=500
derive_health_log() { printf '%s/health.log\n' "$1"; }
resolve_health_log() {
  local _hl_c
  _hl_c=$(git -C "$1" rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || return 1
  _hl_c=${_hl_c%$'\r'}
  [ -n "$_hl_c" ] || return 1
  derive_health_log "$_hl_c"
}
add_health_event() {
  local _hl_log=${1:-} _hl_src=${2:-} _hl_ev=${3:-} _hl_d=${4:-} _hl_why="" _hl_n=0 _hl_t
  local _hl_a=abcdefghijklmnopqrstuvwxyz
  case "$_hl_src" in ''|[!$_hl_a]*|*[!$_hl_a'0123456789-']*) _hl_why="source '$_hl_src' is not a lowercase token" ;; esac
  case "$_hl_ev" in ''|[!$_hl_a]*|*[!$_hl_a'0123456789-']*) _hl_why="event '$_hl_ev' is not a lowercase token" ;; esac
  [ -n "$_hl_log" ] || _hl_why="no log path resolved"
  if [ -z "$_hl_why" ]; then
    _hl_d=${_hl_d//$'\t'/ }; _hl_d=${_hl_d//$'\r'/ }; _hl_d=${_hl_d//$'\n'/ }; _hl_d=${_hl_d:0:240}
    _hl_t=$(date -u +%Y-%m-%dT%H:%M:%S+00:00 2>/dev/null) || _hl_t=""
    [ -n "$_hl_t" ] || _hl_why="date printed no UTC stamp"
  fi
  if [ -z "$_hl_why" ] && [ -f "$_hl_log" ]; then
    _hl_n=$(wc -l < "$_hl_log" 2>/dev/null) || _hl_n=0
    _hl_n=${_hl_n//[!0-9]/}
    if [ "${_hl_n:-0}" -ge "$HEALTH_LOG_CAP_LINES" ]; then
      { tail -n $((HEALTH_LOG_CAP_LINES / 2)) "$_hl_log" > "$_hl_log.trim.$$" && mv -f "$_hl_log.trim.$$" "$_hl_log"; } 2>/dev/null \
        || { rm -f "$_hl_log.trim.$$" 2>/dev/null; _hl_why="the trim to the newest $((HEALTH_LOG_CAP_LINES / 2)) lines failed"; }
    fi
  fi
  if [ -z "$_hl_why" ]; then
    { printf '%s\t%s\t%s\t%s\n' "$_hl_t" "$_hl_src" "$_hl_ev" "$_hl_d" >> "$_hl_log"; } 2>/dev/null && return 0
    _hl_why="the append failed"
  fi
  printf 'health: NOTE - %s: %s; nothing written\n' "${_hl_log:-(no path)}" "$_hl_why" >&2
  return 0
}
# <<< health_log_sh
# derive_temp_path <name> <dest> — sets <name> to an unpredictable sibling of <dest>; creates nothing (TOOL-dRedressedBar-24)
derive_temp_path() { if [ -n "${SRANDOM:-}" ]; then printf -v "$1" '%s.%s%s.tmp' "$2" "$SRANDOM" "$SRANDOM"; else printf -v "$1" '%s' "$(mktemp -u "$2.XXXXXXXX" 2>/dev/null)"; [ -n "${!1}" ]; fi; }

PROF_NAME=""; PROF_WIDTH=""; PROF_TIMEOUT=0; PROF_WALL=0; PROF_MEMPAUSE=0; PROF_SPAWNPAUSE=0; PROF_SLOTS=1; PROF_TAG=""; PROF_WHERE=""
if [ -f "$PROFILES" ]; then
  # GATE_PROFILE names a row and SKIPS detection; otherwise the first row both thresholds satisfy.
  if [ -n "${GATE_PROFILE:-}" ]; then PROF_WHERE="detection skipped"
  else det_cores; det_ram_capped; fi
  ln=0; declared=""; sel=""; selknobs=""
  # Every row is validated even after one is selected: a malformed row is an operator error wherever
  # it sits, and a refusal that depended on position would pass on the tables most likely to be wrong.
  while IFS=$'\t' read -r pname pcores pram pknobs || [ -n "$pname" ]; do
    ln=$((ln+1))
    # LEADING BLANKS STRIPPED BEFORE THE TEST, because the canary's own comment filter strips them
    # and this parser did not: an INDENTED comment — which this file's header explicitly invites, and
    # which the shipped table itself is full of — refused the whole bar with a message about field
    # counts. Two readers of one file disagreeing about which lines are even rows is the drift this
    # joins shut; the looser of the two wins, since no verdict can turn on a comment.
    case "${pname#"${pname%%[![:space:]]*}"}" in ''|'#'*) continue ;; esac
    case "$pknobs" in *$'\t'*) prof_die "$PROFILES:$ln: malformed profile row (more than four tab-separated fields)" ;; esac
    [ -n "$pcores" ] && [ -n "$pram" ] && [ -n "$pknobs" ] \
      || prof_die "$PROFILES:$ln: malformed profile row (expected name, min cores, min RAM MB, knobs)"
    case "$pcores$pram" in *[!0-9]*) prof_die "$PROFILES:$ln: malformed profile row (thresholds must be digits: '$pcores', '$pram')" ;; esac
    # THE DECLARED HALF OF THE COMPARISON, bounded exactly as num_ok bounds the detected half. Digits
    # alone are not enough: `[ "$DET_CORES" -ge "$pcores" ]` ERRORS on an int64 overflow rather than
    # comparing, so a twenty-digit threshold silently matched nothing and dropped the run to the
    # catch-all with no refusal at all. A bound on one side of a comparison is not a bound.
    { [ ${#pcores} -le 15 ] && [ ${#pram} -le 15 ]; } \
      || prof_die "$PROFILES:$ln: threshold too long to compare (max 15 digits): '$pcores', '$pram'"
    # A silently ignored knob is a knob the operator believes they set, so an unknown key REFUSES.
    IFS=, read -ra kv <<<"$pknobs"
    for k in "${kv[@]}"; do
      case "$k" in *=*) ;; *) prof_die "$PROFILES:$ln: malformed knob '$k' (expected key=value)" ;; esac
      case " $KNOWN_KNOBS " in *" ${k%%=*} "*) ;; *) prof_die "$PROFILES:$ln: unknown knob key '${k%%=*}' (known: $KNOWN_KNOBS)" ;; esac
      case "${k#*=}" in ''|*[!0-9]*) prof_die "$PROFILES:$ln: knob '${k%%=*}' has a non-numeric value '${k#*=}'" ;; esac
      # Same bound, same reason, and here the symptom was worse than a wrong width: an over-long
      # `timeout=` made every later `[ "$PROF_TIMEOUT" -gt 0 ]` error instead of compare, so the knob
      # was silently dropped AND the INERT warning that would have said so was disabled by the same
      # failing test. The visibility line then reported `timeout off` beside a table declaring one.
      case "${k#*=}" in ????????????????*) prof_die "$PROFILES:$ln: knob '${k%%=*}' value too long to compare (max 15 digits): '${k#*=}'" ;; esac
      # A PERCENT, so a value above 100 is a threshold no reading can cross: the knob would read as on
      # and could never hold. Refused like any malformed knob rather than clamped (TOOL-aGraftedHelix-7).
      [ "${k%%=*}" = mempause ] && [ "$((10#${k#*=}))" -gt 100 ] \
        && prof_die "$PROFILES:$ln: knob 'mempause' is a percent of used memory, 0 to 100: '${k#*=}'"
      # A WHOLE MULTIPLE OF THE SPAWN FLOOR, bounded so its product with the floor stays inside
      # int64 arithmetic at every decision (TOOL-aSparedSpawn-2).
      [ "${k%%=*}" = spawnpause ] && [ "$((10#${k#*=}))" -gt 1000 ] \
        && prof_die "$PROFILES:$ln: knob 'spawnpause' is a whole multiple of the spawn floor, 0 to 1000: '${k#*=}'"
      # A COUNT OF HOLDERS, so 0 would be a turnstile that admits nothing and every bar would queue to
      # its fail-open bound. Refused like any malformed knob (TOOL-aPairedSlots-1).
      [ "${k%%=*}" = slots ] && [ "$((10#${k#*=}))" -lt 1 ] \
        && prof_die "$PROFILES:$ln: knob 'slots' is how many bars the host turnstile admits at once, 1 or more: '${k#*=}'"
      # AND AT MOST 64 (TOOL-aPairedSlots-15): the runner builds one slot path per slot before the queue,
      # so a mistyped count of many digits hangs every bar before its first leg. `GATE_JOBS` is
      # clamped at 64 for the same reason.
      [ "${k%%=*}" = slots ] && [ "$((10#${k#*=}))" -gt 64 ] \
        && prof_die "$PROFILES:$ln: knob 'slots' is how many bars the host turnstile admits at once, at most 64: '${k#*=}'"
    done
    declared="$declared $pname"
    [ -n "$sel" ] && continue
    if [ -n "${GATE_PROFILE:-}" ]; then
      [ "$pname" = "${GATE_PROFILE}" ] && { sel=$pname; selknobs=$pknobs; }
    elif [ "$DET_CORES" -ge "$pcores" ] && [ "$DET_RAM" -ge "$pram" ]; then
      sel=$pname; selknobs=$pknobs
    fi
  done < "$PROFILES"
  if [ -z "$sel" ]; then
    [ -n "${GATE_PROFILE:-}" ] \
      && prof_die "$PROFILES: GATE_PROFILE='${GATE_PROFILE}' names no row. Declared rows:$declared"
    # Unmatchable is not the same state as ABSENT, and only one of them is an operator error: the
    # catch-all row is what makes a match unconditional, so a table with none was declared wrong.
    prof_die "$PROFILES: no row matches cores $DET_CORES / ram $DET_RAM MB — the table declares no catch-all row. Declared rows:$declared"
  fi
  PROF_NAME=$sel
  IFS=, read -ra kv <<<"$selknobs"
  for k in "${kv[@]}"; do
    case "${k%%=*}" in width) PROF_WIDTH=${k#*=} ;; timeout) PROF_TIMEOUT=${k#*=} ;;
                        wall) PROF_WALL=${k#*=} ;; mempause) PROF_MEMPAUSE=$((10#${k#*=})) ;;
                        spawnpause) PROF_SPAWNPAUSE=$((10#${k#*=})) ;;
                        slots) PROF_SLOTS=$((10#${k#*=})) ;; esac
  done
  [ -n "$PROF_WIDTH" ] || prof_die "$PROFILES: row '$sel' declares no width knob"
  PROF_TAG="detected"
  [ -n "${GATE_PROFILE:-}" ] && PROF_TAG="GATE_PROFILE"
  [ -z "$PROF_WHERE" ] && { [ "$DET_CORES" = 0 ] || [ "$DET_RAM" = 0 ]; } && PROF_TAG="detection failed"
else
  # ABSENT is a FALLBACK, not a refusal: this kit deploys, and an adopter may take it without the
  # table. Deleting the table is therefore also the documented rollback for this whole mechanism, and
  # the arm that drives this branch is what proves the rollback rather than hoping for it.
  # The 8 here is the SAME value the table's top row declares, and its measurement is argued THERE,
  # beside the number. Restating the argument in both places is how the two copies drift apart while
  # still agreeing loudly enough that nobody checks.
  det_cores; det_ram_capped
  bi=$DET_CORES; [ "$bi" -gt 0 ] || bi=4
  PROF_NAME="built-in"; PROF_WIDTH=$(( bi < 8 ? bi : 8 )); PROF_TIMEOUT=0; PROF_WALL=0; PROF_TAG="built-in default"
  # A pin the operator set and this branch cannot honour. WARNED, not refused: refusing would block
  # the documented rollback for anyone carrying GATE_PROFILE in their environment. Silence is the one
  # option ruled out — the same typo is FATAL against a present table, so staying quiet here turns a
  # refusal into an invisible no-op, which is the rule the row validator above states in as many words.
  if [ -n "${GATE_PROFILE:-}" ]; then
    echo "run-gates: GATE_PROFILE='${GATE_PROFILE}' is set but no profile table exists at $PROFILES — the built-in formula is in force and the request is IGNORED" >&2
    PROF_TAG="$PROF_TAG, GATE_PROFILE ignored"
  fi
fi

# A knob the operator set and the host cannot honour is worse than no knob: say so rather than run
# inert. `timeout` is RUN, not probed — the same rule the detection chain follows.
# PROBED WITH THE OPTION SET THE RUN ACTUALLY USES. A bare `timeout 1 true` passes on a build that
# rejects `-k`, so the probe cleared a path the leg exec then failed on — the probe and the subject
# were two different commands, which is the shape a probe exists to rule out.
# PROBED ONCE, READ TWICE. The profile knob and the per-leg ceilings need the same fact -- does
# `timeout -k` actually RUN here -- and probing it per consumer would cost a spawn each and could
# answer differently. RUN it, never `command -v` — the resolver note near the top of this file
# records why, and repeating the path here would add a kit literal that resolves to nothing in a
# target installed at another prefix.
CEILINGS_LIVE=1
# THE BOUND IS 10 s AND IT IS NOT A TIMEOUT, IT IS A CAPABILITY PROBE. `true` returns instantly, so
# the only thing a bound can add here is a FALSE NEGATIVE: at the shipped `1` it was process-creation
# latency that tripped it, not a missing binary. MEASURED node `a` 2026-08-28, `timeout -k 1s 1 true`
# 0/40 failures quiet and 7/40 under eight concurrent spawn loops, while `timeout -k 1s 10 true` was
# 0/40 under that same load. That 17% is the whole of the run-gates canary's flakiness: the suite
# probes once while the box is quiet, the runner probes again under a full bar, they disagree, and an
# arm then blames `GATE_JOBS` or the clamp for a binary that was there the entire time. Raising the
# bound costs nothing -- it is only ever reached if `timeout` genuinely hangs. TOOL-aSiftedFork-7.
timeout -k 1s 10 true >/dev/null 2>&1 || CEILINGS_LIVE=0
if [ "$PROF_TIMEOUT" -gt 0 ] && [ "$CEILINGS_LIVE" = 0 ]; then
  echo "run-gates: profile '$PROF_NAME' asks for a ${PROF_TIMEOUT}s per-leg timeout but timeout does not run here — the knob is INERT this run" >&2
  PROF_TIMEOUT=0
fi

# ---- THE SPAWN CALIBRATION (TOOL-aSparedSpawn-2). The row's width is a CAP and a measured pick may
# ---- narrow it: `--calibrate-width` times K concurrent spawn loops for each K in CALIBRATE_KS and
# ---- keeps the smallest K whose aggregate rate is within CALIBRATE_THETA percent of the best, the
# ---- knee past which more legs share one spawn throughput and only dilate each other. A bar never
# ---- calibrates; it READS the pick the verb left in `<git-common-dir>/gate-host-calibration`, one
# ---- line `<width> TAB <K=rate,…> TAB <iso-utc> TAB <boot-epoch or ->`, and uses it only when it is
# ---- well formed, under CALIBRATE_DAYS old, and written in this boot (a reboot or a scanner update
# ---- moves spawn cost by integer factors). Precedence: GATE_JOBS, then the lower of row and pick,
# ---- then the row. A cache that fails a test leaves the row standing and the profile line says
# ---- `uncalibrated` and which test, because a skip must announce itself.
# THETA IS PROVISIONAL: the width A/B that sets it (the spec's S1) is owed, so 90 is a declared
# starting point and not a measurement. It can cost speed and never a verdict.
CALIBRATE_THETA=90
CALIBRATE_KS="1 2 4 6 8"
CALIBRATE_REPS=20
CALIBRATE_DAYS=7
# THE ARM SEAM, read once and unset as GATE_SPAWN_CMD is, so no leg's nested runner inherits it: a
# comma list of one rate per K that stands in for the timed loops, so the selection grades clock-free.
CAL_RATES_SEAM=${GATE_CALIBRATION_RATES:-}
unset GATE_CALIBRATION_RATES
# THE COMMON DIR, resolved ONCE here and reused by the turnstile and the scratch-dir owner below, so
# the cache read costs a bar no git spawn of its own.
RG_COMMON=$RG_COMMON_RAW
[ -n "$RG_COMMON" ] && RG_COMMON=$(cd "$RG_COMMON" 2>/dev/null && pwd) || RG_COMMON=""
CALIB_FILE=""; [ -n "$RG_COMMON" ] && CALIB_FILE="$RG_COMMON/gate-host-calibration"

# read_boot_epoch — BOOT_EPOCH, this boot's start in epoch seconds from `/proc/uptime` with a builtin
# read, or `-` where that does not read.
read_boot_epoch() {
  local up=""
  BOOT_EPOCH=-
  { read -r up _ < /proc/uptime; } 2>/dev/null || return 0
  up=${up%%.*}
  case "$up" in ''|*[!0-9]*|??????????*) return 0 ;; esac
  BOOT_EPOCH=$(( EPOCHSECONDS - 10#$up ))
}
# parse_iso_epoch <YYYY-MM-DDTHH:MM:SSZ> — ISO_EPOCH, its epoch seconds by civil-date arithmetic
# (days from 1970-01-01, the era-of-400-years form), so the cache read spawns nothing; rc 1 on any
# other shape.
parse_iso_epoch() {
  local y m d era yoe doy
  ISO_EPOCH=""
  [[ $1 =~ ^([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})Z$ ]] || return 1
  y=$((10#${BASH_REMATCH[1]})); m=$((10#${BASH_REMATCH[2]})); d=$((10#${BASH_REMATCH[3]}))
  [ "$m" -le 2 ] && y=$(( y - 1 ))
  era=$(( y / 400 )); yoe=$(( y - era * 400 ))
  doy=$(( (153 * (m > 2 ? m - 3 : m + 9) + 2) / 5 + d - 1 ))
  ISO_EPOCH=$(( (era * 146097 + yoe * 365 + yoe / 4 - yoe / 100 + doy - 719468) * 86400
    + 10#${BASH_REMATCH[4]} * 3600 + 10#${BASH_REMATCH[5]} * 60 + 10#${BASH_REMATCH[6]} ))
}
# read_host_calibration <path> — CALIB_WIDTH, the cached pick, when the cache is valid; else empty,
# and CALIB_WHY names the first test it failed: `absent`, `malformed`, `stale` (CALIBRATE_DAYS old or
# more, or dated in the future) or `another boot` (60 s of clock jitter allowed; skipped on a host
# whose `/proc/uptime` does not read). Builtins only.
read_host_calibration() {
  local f=$1 line="" tabs w rates iso boot rest gap
  CALIB_WIDTH=""; CALIB_WHY=absent
  [ -n "$f" ] && [ -e "$f" ] || return 0
  CALIB_WHY=malformed
  [ -f "$f" ] || return 0
  { IFS= read -r line < "$f"; } 2>/dev/null || [ -n "$line" ] || return 0
  line=${line%$'\r'}
  tabs=${line//[!$'\t']/}
  [ "${#tabs}" = 3 ] || return 0
  w=${line%%$'\t'*}; rest=${line#*$'\t'}
  rates=${rest%%$'\t'*}; rest=${rest#*$'\t'}
  iso=${rest%%$'\t'*}; boot=${rest#*$'\t'}
  case "$w" in ''|0*|*[!0-9]*|???*) return 0 ;; esac
  [ -n "$rates" ] || return 0
  case "$boot" in -) ;; ''|*[!0-9]*|?????????????*) return 0 ;; esac
  parse_iso_epoch "$iso" || return 0
  CALIB_WHY=stale
  gap=$(( EPOCHSECONDS - ISO_EPOCH ))
  { [ "$gap" -ge 0 ] && [ "$gap" -lt $(( CALIBRATE_DAYS * 86400 )) ]; } || return 0
  read_boot_epoch
  if [ "$BOOT_EPOCH" != - ]; then
    CALIB_WHY="another boot"
    [ "$boot" != - ] || return 0
    gap=$(( BOOT_EPOCH - 10#$boot )); [ "$gap" -ge 0 ] || gap=$(( -gap ))
    [ "$gap" -le 60 ] || return 0
  fi
  CALIB_WIDTH=$(( 10#$w )); CALIB_WHY=""
}
read_host_calibration "$CALIB_FILE"
# F1 (a): the pick NARROWS the row and never widens it, so the row stays a cap on a host that
# measured past it, and a host never calibrated behaves exactly as before.
JOBS_ROW=$PROF_WIDTH; WIDTH_FROM=row
if [ -n "$CALIB_WIDTH" ]; then
  WIDTH_NOTE=calibrated
  if [ "${#PROF_WIDTH}" -gt 4 ] || [ "$(( 10#$PROF_WIDTH ))" -gt "$CALIB_WIDTH" ]; then
    JOBS_ROW=$CALIB_WIDTH; WIDTH_FROM=calibrated
  fi
else
  WIDTH_NOTE="uncalibrated: $CALIB_WHY"
fi
# The override names the width itself, so the line carries no note about a cache it did not consult.
[ -n "${GATE_JOBS:-}" ] && { WIDTH_FROM=GATE_JOBS; WIDTH_NOTE=""; }

# A non-numeric or <1 width is clamped to 1 rather than refused — this knob only schedules work, it
# can never skip a leg. GATE_JOBS overrides the width ONLY: the row is still selected and still
# supplies the timeout, which is what keeps the override from disabling the rest of the profile.
JOBS=${GATE_JOBS:-$JOBS_ROW}
# Bound by LENGTH before any numeric test touches the value. Both `[ "$JOBS" -lt 1 ]` and `$(( JOBS < 1 ))`
# ERROR on an int64 overflow instead of comparing, so a 20-digit value used to sail past the clamp into a
# dispatch loop whose own `[ "$(live)" -lt "$JOBS" ]` errored identically: the runner spun forever having
# executed ZERO legs and printed no verdict, which on the push boundary is a hang rather than a red.
# `:-` substitutes the default for null as well as unset, so JOBS is never empty and an '' alternative here
# would be dead — the arm that "covered" it was measuring the default width, not the clamp.
case "$JOBS" in *[!0-9]*) JOBS=1 ;; ?????*) JOBS=64 ;; esac
[ "$JOBS" -lt 1 ] && JOBS=1

# ONE visibility line, before the first leg verdict and copied into the durable records — a profile
# nobody can see is a knob nobody can debug. The parenthesised tail follows the report's two-space
# contract: `<head>  (<tail>)`, so a reader splits on the double space and gets the bare name back.
# It reports the EFFECTIVE width (post-clamp, post-GATE_JOBS) and the sources the chain TRIED, so a
# run that fell through to its second source says so instead of looking like a first-source hit.
prof_n() { if [ "$1" = 0 ]; then printf '?'; else printf '%s' "$1"; fi; }
[ -n "${GATE_JOBS:-}" ] && PROF_TAG="$PROF_TAG, GATE_JOBS"
if [ -n "$PROF_WHERE" ]; then prof_where=$PROF_WHERE
else prof_where="cores $(prof_n "$DET_CORES") via $CORE_SRC, ram $(prof_n "$DET_RAM") MB via $RAM_SRC"; fi
prof_t=off; [ "$PROF_TIMEOUT" -gt 0 ] && prof_t="${PROF_TIMEOUT}s"
# THE CEILING REGIME IS ITS OWN FIELD, and deliberately not folded into `timeout`. That field names
# the PROFILE knob, which every shipped row sets to 0, and the canary asserts it reads `off` on a
# host that cannot honour it -- overloading it made an INERT run read as a live bound. But leaving
# the line saying only `timeout off` while 85 legs carried a ceiling was the opposite lie, so the
# regime is reported beside the knob rather than instead of it. TOOL-aBoundedCeiling-1.
prof_c=live; [ "$CEILINGS_LIVE" = 1 ] || prof_c=INERT

# ---- THE WHOLE-RUN WALL. TOOL-aQuenchedHarness-1. The per-leg ceiling bounds ONE leg; nothing
# ---- bounded the RUN, so a bar's worst case was the sum of every ceiling it could reach. This is a
# ---- HANG bound and never a cost verdict: a breach is RED, naming the legs that had not returned.
#
# IT IS NOT A PROCESS-GROUP KILL, and that is the load-bearing sentence. This runner never enables
# job control -- `set -u` only, no `set -m`, no `setsid` (absent on node `a`, `command -v setsid`
# returns rc=1) -- and legs are dispatched as plain `runleg "$k" &` from the single dispatch/report
# shell. So every leg is in the RUNNER's own process group, and a group kill would take down the
# reader loop and the shell that has to render the verdict: the run would die signalled and silent
# instead of exiting non-zero with a summary. The wall kills RECORDED PER-LEG PIDS and their
# descendants, touching nothing outside that set.
#
# THE DESCENDANTS ARE COLLECTED BEFORE ANYTHING IS KILLED. Measured on this host: killing a parent
# REPARENTS its children, so they no longer match the ppid you were about to walk. One `ps` snapshot,
# the whole tree from it, then the kills.
WALL=${GATE_WALL:-$PROF_WALL}
case "$WALL" in ''|*[!0-9]*) WALL=0 ;; esac
WALL_ARMED=0; WALL_PID=""

# The descendant set of a pid, from ONE snapshot. Depth-bounded rather than "until the frontier is
# empty": a ps table that disagrees with itself mid-write must cost a truncated tree, never a spin.
scan_descendants() {
  local root=$1 snap=$2 out=$1 frontier=$1 next depth=0
  while [ -n "$frontier" ] && [ "$depth" -lt 8 ]; do
    # `$3+0 == $3` and the `$2` guard are not defensiveness: cygwin `ps -ef` prints argv RAW, so a
    # command line containing a newline splits one process across rows whose field 2 and 3 are
    # attacker-or-accident-chosen text. Snapshots on this box already carry about ten such
    # continuation rows from other sessions' multi-line `bash -c`. Without the guard this walk feeds
    # arbitrary text to `kill -9`.
    next=$(awk -v ps="$frontier" 'BEGIN{n=split(ps,a," ");for(i=1;i<=n;i++)P[a[i]]=1}
                                  NR>1 && $2 ~ /^[0-9]+$/ && $3 ~ /^[0-9]+$/ && ($3 in P) {print $2}' "$snap" 2>/dev/null | tr '\n' ' ')
    next=${next% }
    [ -n "$next" ] || break
    out="$out $next"; frontier=$next; depth=$((depth+1))
  done
  printf '%s' "$out"
}

remove_descendants() {
  local snap; snap=$(mktemp 2>/dev/null) || return 0
  ps -ef > "$snap" 2>/dev/null || : > "$snap"
  local p left=""
  for p in $(scan_descendants "$1" "$snap"); do
    case "$p" in ''|*[!0-9]*) continue ;; esac
    kill -9 "$p" 2>/dev/null || true
  done
  # WHAT IT COULD NOT KILL IS REPORTED, and this is where the wall's liveness assertion lives now.
  # A host where the walk cannot reach a leg's descendants says so with the pids, at the moment the
  # fact matters, instead of a startup probe guessing at it for every run that never breaches.
  #
  # THE SNAPSHOT IS DELETED AFTER THIS LOOP, NOT BEFORE IT. It used to be removed one line above,
  # and this loop then re-scanned the deleted path: `scan_descendants` reads it under
  # `2>/dev/null`, so a missing file yields an empty frontier and the walk returns its SEED --
  # the root pid alone. The survivor loop could therefore never examine a descendant and the
  # message below could never name one. That is byte-for-byte the failure the deleted startup
  # probe had, described a few lines further down in this same file, reintroduced by an `rm` in
  # the wrong place -- and since this is the wall's ONLY liveness assertion, the guarantee was
  # decorative. Found by the closing review of the build that wrote it. TOOL-aQuenchedHarness-1,
  # corrected in TOOL-aQuenchedHarness-7's closing pass.
  for p in $(scan_descendants "$1" "$snap" 2>/dev/null); do
    case "$p" in ''|*[!0-9]*) continue ;; esac
    kill -0 "$p" 2>/dev/null && left="$left $p"
  done
  rm -f "$snap" 2>/dev/null || true
  [ -n "$left" ] && printf 'run-gates: the wall could not reach these descendants of %s, so they are still running:%s\n' "$1" "$left" >&2
  return 0
}

# ---- A TIMED-OUT LEG'S PROCESS GROUP. TOOL-dDerivedDocket-26 F5 -----------------------------------
# The walk above follows PPIDs from a root, and after a ceiling fires that is the wrong key. `timeout`
# has returned, the leg command it ran is dead, and a descendant that outlived both was REPARENTED to
# pid 1 when its parent died, so no walk from the worker or from `timeout` reaches it again. What it
# KEEPS is its process group: `timeout` without `--foreground` makes itself the leader of a new group
# before it starts the leg, and every process the leg starts stays in that group unless it leaves.
# Measured on node `d`: a TERM-ignoring grandchild outlived `timeout -k 2s 2` returning 124, with
# PPID 1 and a PGID equal to `timeout`'s pid. The worker itself is in the RUNNER's group, which is
# why keying on `timeout`'s group can never reach the process that still has `.sec` and `.rc` to write.
#
# WHAT THIS DOES NOT REACH: a descendant that left the group on its own, by `setsid` or by job control.
# Nothing in this runner can see one of those once its parent is gone, and the retry pass that asserts
# the group is empty says nothing about it either.
#
# scan_group <pgid> — the pids in that process group, from ONE `ps` snapshot. The HEADER names the
# columns, so procps' `-o pid,pgid` and cygwin's default table (PID PPID PGID ...) both parse. A cygwin
# row may lead with a one-letter state column its header does not name, and a row whose PID field is
# not a number is the continuation of a multi-line argv, which is skipped for the reason
# `scan_descendants` gives. A PROBE THAT CANNOT MOVE SAYS SO: rc 2 when neither form yields a header
# naming both columns, so a host whose `ps` cannot show a group is never read as a group that emptied.
scan_group() {
  local snap
  snap=$(ps -e -o pid,pgid 2>/dev/null) || snap=""
  case "$snap" in *PGID*) ;; *) snap=$(ps -e 2>/dev/null) || snap="" ;; esac
  printf '%s\n' "$snap" | awk -v g="$1" '
    NR == 1 { for (k = 1; k <= NF; k++) { if ($k == "PID") p = k; if ($k == "PGID") q = k }; next }
    p && q { o = ($1 ~ /^[0-9]+$/) ? 0 : 1
             if ($(p + o) ~ /^[0-9]+$/ && $(q + o) ~ /^[0-9]+$/ && $(q + o) == g) printf "%s ", $(p + o) }
    END     { if (!p || !q) exit 2 }'
}

# remove_group_residue <pgid> — kills every process still in that group, snapshot then kill, up to
# three rounds because a loop in the group can spawn between a snapshot and its kill. Prints the pids
# it still found after the last round, and nothing when the group emptied. This shell and its parent
# are skipped by name: neither is in the group, and the guard is a belt over that fact.
remove_group_residue() {
  local g=$1 p round=0 left members
  case "$g" in ''|*[!0-9]*) return 0 ;; esac
  while :; do
    left=""
    members=$(scan_group "$g") || { printf 'unscannable'; return 0; }
    for p in $members; do
      [ "$p" = "$$" ] && continue
      [ "$p" = "${BASHPID:-}" ] && continue
      left="$left $p"
    done
    [ -n "$left" ] || return 0
    [ "$round" -lt 3 ] || { printf '%s' "${left# }"; return 0; }
    for p in $left; do kill -9 "$p" 2>/dev/null || true; done
    round=$((round + 1))
  done
}

# THERE IS NO STARTUP LIVENESS PROBE, and its removal is the single most load-bearing correction in
# this unit. One shipped, and it GRADED NOTHING on every host: it built its subject as
# `( ( sleep 90 & ) ; sleep 90 ) &`, and bash exec-replaces a subshell's last command, so `$!` WAS
# the sleep and had no children at all. The intended grandchild was reparented to PPID 1 before the
# snapshot was taken. `scan_descendants` therefore returned a one-element set on every run, the survivor
# check saw only the pid that had just been SIGKILLed, and `WALL_LIVE` was pinned at 1 with the
# INERT branch unreachable dead code. Reproduced 14/14. It cost 4.2 s quiet and 12-16 s loaded per
# bar, twice over -- two `ps -ef` walks at 0.4-3.2 s each -- to answer a question it could not ask,
# and it leaked one orphaned `sleep 90` per bar because nothing could reach the reparented child.
#
# THE ASSERTION MOVED TO THE BREACH PATH, which is the only moment the answer is needed and the only
# moment a REAL tree exists to grade. `remove_descendants` reports what it could not kill, so a host
# where the walk cannot reach a descendant says so with the pids it left behind, at the instant that
# fact matters, and costs nothing on the runs where the wall never fires.
prof_w=off; [ "$WALL" -gt 0 ] && prof_w="${WALL}s"
# ON STDERR, and independent of PROF_TIMEOUT. The pre-existing INERT notice at the profile probe is
# gated on a knob every shipped row sets to 0, so it can never fire; without this line the only
# signal that all 85 ceilings are dead would be a stdout suffix nobody reads for warnings.
if [ "$CEILINGS_LIVE" != 1 ]; then
  echo "run-gates: NOTE - this host has no runnable 'timeout -k', so EVERY leg's declared ceiling is INERT and every leg runs unbounded this run" >&2
fi
# ---- THE MEMORY PAUSE'S THRESHOLD, resolved beside the wall it shares the profile line with. The row
# ---- supplies it and `GATE_MEMPAUSE` overrides it alone, as `GATE_WALL` does the wall; an override
# ---- that is not a percent is announced and leaves the pause OFF, because a knob that silently took
# ---- some other value is a knob the operator believes they set. A threshold over a host that gives
# ---- no reading is INERT and says so here, once, instead of reading 0 % used on every decision.
MEMPAUSE=$PROF_MEMPAUSE
if [ -n "${GATE_MEMPAUSE:-}" ]; then
  case "$GATE_MEMPAUSE" in
    *[!0-9]*|????*) MEMPAUSE=101 ;;
    *) MEMPAUSE=$((10#$GATE_MEMPAUSE)) ;;
  esac
  if [ "$MEMPAUSE" -gt 100 ]; then
    echo "run-gates: NOTE - GATE_MEMPAUSE='$GATE_MEMPAUSE' is not a percent from 0 to 100, so the memory pause is OFF this run" >&2
    MEMPAUSE=0
  fi
fi
MEMPAUSE_INERT=0; MEMPAUSE_ROWS=""
if [ "$MEMPAUSE" -gt 0 ] && ! read_mem_used >/dev/null; then
  MEMPAUSE_INERT=1
  echo "run-gates: NOTE - profile '$PROF_NAME' asks to hold dispatch above ${MEMPAUSE}% used memory, but this host gives no reading (${GATE_MEMINFO:-/proc/meminfo}, nor a cgroup pair under ${GATE_CGROUP_ROOT:-/sys/fs/cgroup}), so the memory pause is INERT this run" >&2
fi
prof_m=off; prof_mrec=off
[ "$MEMPAUSE" -gt 0 ] && { prof_m="${MEMPAUSE}%"; prof_mrec=$MEMPAUSE; }
[ "$MEMPAUSE_INERT" = 1 ] && { prof_m=INERT; prof_mrec=inert; }
# THE SPAWN PAUSE'S RATIO (TOOL-aSparedSpawn-2), the row's alone. Whether a floor exists to multiply
# is known only once the floor is read, below, which is where an INERT knob says so. `prof_sp`, not
# `prof_s`, which names the slot field below (TOOL-aSparedSpawn-34).
SPAWNPAUSE=$PROF_SPAWNPAUSE
prof_sp=off; [ "$SPAWNPAUSE" -gt 0 ] && prof_sp="${SPAWNPAUSE}x"
# THE SLOT COUNT (TOOL-aPairedSlots-1): the row's `slots`, 1 where it declares none, replaced by
# `GATE_TURNSTILE_SLOTS`. A malformed override is IGNORED with a NOTE rather than refused, as
# `GATE_JOBS` is clamped rather than refused: this knob only schedules bars, so the row's value is a
# safe answer and a refusal would stop a bar over a scheduling preference. The line gains the field
# ONLY above 1, so a run at the kit default prints the line it printed before the knob existed.
if [ -n "${GATE_TURNSTILE_SLOTS:-}" ]; then
  case "$GATE_TURNSTILE_SLOTS" in
    *[!0-9]*|????????????????*) _ps_ok=0 ;;
    *) _ps_ok=1; [ "$((10#$GATE_TURNSTILE_SLOTS))" -ge 1 ] && [ "$((10#$GATE_TURNSTILE_SLOTS))" -le 64 ] || _ps_ok=0 ;;
  esac
  if [ "$_ps_ok" = 1 ]; then PROF_SLOTS=$((10#$GATE_TURNSTILE_SLOTS))
  else echo "run-gates: NOTE - GATE_TURNSTILE_SLOTS='$GATE_TURNSTILE_SLOTS' is not a count from 1 to 64, so the profile's $PROF_SLOTS slot(s) stand" >&2; fi
  unset _ps_ok
fi
prof_s=""; [ "$PROF_SLOTS" -gt 1 ] && prof_s=", slots $PROF_SLOTS"
# THE PROFILE LINE'S ONE TEMPLATE (TOOL-aPairedSlots-3): built here, and rebuilt after the turnstile
# when a shared dispatch width moves `JOBS`, so the summary file and the durable copies carry the
# width that dispatched. One function, so the two sites cannot spell the line two ways.
# The spawn ratio sits BEFORE `mempause`, whose field, with the slot count only above one slot, is
# pinned by the canary as the one that ends at the `;` (TOOL-aSparedSpawn-2).
render_prof_line() { # -> PROF_LINE, from the resolved profile and the current JOBS
  PROF_LINE="gate profile: $PROF_NAME  ($prof_where; width $JOBS${WIDTH_NOTE:+ $WIDTH_NOTE}, timeout $prof_t, ceilings $prof_c, wall $prof_w, spawnpause $prof_sp, mempause $prof_m$prof_s; $PROF_TAG)"
}
render_prof_line

# HOISTED ABOVE `--print-profile`, TOOL-dDerivedDocket-27 S3. That verb reports the queue bound,
# and a queue printed before the TTL is resolved reads 0, which is a bound on nothing. Deriving it
# takes no beacon, runs no leg and writes nothing, so the verb still exits before the turnstile.
# THE TTL IS DERIVED, never a wall clock copied out of a timing cache. What has to be outlasted is
# the gap between two heartbeat refreshes — and since TOOL-aQuenchedHarness-8 that gap is
# `TS_TICK_EVERY`, a TIMER, not "how long can one leg take". The distinction is the whole unit:
# liveness is a property of the PROCESS and is cheap to assert often; progress is a property of the
# WORK and is what the per-leg ceiling and the whole-bar wall are for. The reaper wants the first.
#
# WHAT THIS REPLACED, recorded because the cliff was real and measured. `ts_hb` used to be called at
# exactly ONE site — a leg COMPLETING — so the TTL had to outlast a whole leg. Every shipped profile
# row sets `timeout=0`, so every real run used the 1800 s fallback, while the longest recorded leg
# was 3837 s. A bar therefore went stale mid-leg on every full run, the next bar reaped its beacon as
# "stalled", and both ran. Reproduced in a scratch repo with this file unmodified: bar B printed
# `reaping the beacon of a stalled holder (heartbeat 13s old, ttl 6s)` while bar A was alive and
# working, and both exited 0. The old note here said the fix was to set `timeout=` on a profile row;
# it is not, because that value would have to exceed the longest leg, which puts TS_TTL at three
# times it and TS_MAXWAIT — a declared TS_TTL * 4 — near thirteen hours.
#
# A BACKGROUND TICKER WAS REJECTED ONCE, in `memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md`,
# on two premises. The second — "a leg-sized TTL makes it unnecessary" — is refuted by the two
# numbers above. The first — one more process on a spawn-bound machine — survives and is PRICED: at
# `TS_TTL / 6` a 4000 s bar ticks about 13 times, two spawns each, at the 319 ms per-spawn cost
# measured on node `a`; roughly 8 s against a bar that makes tens of thousands. That is the
# supersession an append-only decision log requires, written where the reversal happens.
if [ "${PROF_TIMEOUT:-0}" -gt 0 ]; then TS_TTL=$(( PROF_TIMEOUT * 3 ))
else TS_TTL=${GATE_TURNSTILE_TTL:-1800}; fi
# The bounded wait is a DECLARED MULTIPLE OF THE TTL, so it moves with the one number this unit
# derives and is never sized against a bar's wall clock. Four: long enough that a queue three deep
# behind a stalled holder still drains rather than stampeding, short enough that a wedged node
# releases within an hour.
TS_MAXWAIT=$(( TS_TTL * 4 ))

# ---- `--print-profile`: ONE RESOLVER, TWO READERS. TOOL-aQuenchedHarness-4 S11 ------------------
# Profile selection -- the hardware detection, the table walk, the clamp, the GATE_JOBS override --
# is 200 lines and lives inline here, so any second script wanting the width had to re-implement it.
# A spec audit caught exactly that: `run-selftests.sh` was specced to run "at a width read from the
# same gate-profiles.txt row the bar reads", over a seam that did not exist. Two resolvers is the
# drift class this repo gates elsewhere, so this verb is the seam instead.
#
# IT EXITS BEFORE THE TURNSTILE, and that placement is the whole of its safety: a bar that took the
# beacon to answer a question would serialise every caller behind a real run, and a caller polling it
# would wedge the repository. It also runs no leg, writes no run record and touches no ledger.
#
# TAB-SEPARATED KEY/VALUE, because the caller is a shell script and `read -r k v` is the cheapest
# correct parse there. Adding a key is safe; a reader takes the keys it knows.
#
# TWO KEYS FOR THE UNATTENDED DRIVER'S BACKSTOP, TOOL-dDerivedDocket-27 S3. `queue` is TS_MAXWAIT, the
# longest the turnstile waits before it fails open, which the driver adds to the wall because the
# wall is armed only after the queue. `ceiling_max` is the largest positive `ceiling` in the resolved
# manifest, read with the parse's own predicate, or `-` when no leg declares one; a wall below it
# fires on a healthy bar that dispatches that leg. A manifest that does not parse prints NO
# `ceiling_max` line, because "none declared" and "could not read" are two answers, and a reader
# names the key it did not get.
# ---- `--calibrate-width` (TOOL-aSparedSpawn-2): the verb that WRITES the cache the width reads above.
# It exits before the turnstile, as `--print-profile` does, runs no leg and writes no run record. It
# times what `measure_spawn_cost` times, the `GATE_SPAWN_CMD` seam's command or `true`, in K loops at
# once for each K, CALIBRATE_REPS spawns a loop, so on a loaded host it is about a minute. A rate is
# whole spawns a minute across the K loops. Output is TAB key/value, the `--print-profile` grammar.
# measure_spawn_rate <k> — CAL_RATE, spawns a minute across <k> concurrent loops; empty when a spawn
# failed, bash has no `EPOCHREALTIME`, or the clock did not move, because a zero is never a rate.
measure_spawn_rate() {
  local k=$1 j t0 t1 bad=0
  local -a pids=()
  CAL_RATE=""
  t0=${EPOCHREALTIME:-}; t0=${t0//[.,]/}
  [ -n "$t0" ] || return 0
  for ((j=0; j<k; j++)); do
    # A failed spawn's only effect is the caller's refusal (TOOL-aSparedSpawn-16 S4), which the canary arms.
    # arm-signature: could not be measured (a spawn failed, or bash has no EPOCHREALTIME), so no pick is written
    ( for ((r=0; r<CALIBRATE_REPS; r++)); do "${CAL_CMD[@]}" </dev/null >/dev/null 2>&1 || exit 1; done ) &
    pids+=("$!")
  done
  for j in "${pids[@]}"; do wait "$j" || bad=1; done
  t1=${EPOCHREALTIME//[.,]/}
  [ "$bad" = 0 ] && [ $(( 10#$t1 - 10#$t0 )) -gt 0 ] || return 0
  CAL_RATE=$(( k * CALIBRATE_REPS * 60000000 / (10#$t1 - 10#$t0) ))
  [ "$CAL_RATE" -gt 0 ] || CAL_RATE=""
}
# derive_calibrated_width <rate>… — CAL_PICK, the first K of CALIBRATE_KS whose rate is at least
# CALIBRATE_THETA percent of the best: the KNEE, never the maximum, which on a flat curve is noise.
derive_calibrated_width() {
  local -a ks=()
  local r best=0 i=0
  read -ra ks <<<"$CALIBRATE_KS"
  CAL_PICK=""
  for r in "$@"; do [ "$r" -gt "$best" ] && best=$r; done
  for r in "$@"; do
    if [ $(( r * 100 )) -ge $(( CALIBRATE_THETA * best )) ]; then CAL_PICK=${ks[$i]}; return 0; fi
    i=$(( i + 1 ))
  done
}
if [ "${1:-}" = "--calibrate-width" ]; then
  [ -n "$CALIB_FILE" ] || { echo "run-gates: --calibrate-width: no git common dir resolved, so there is nowhere to keep the pick" >&2; exit 2; }
  read -ra _cks <<<"$CALIBRATE_KS"
  _crates=()
  if [ -n "$CAL_RATES_SEAM" ]; then
    IFS=, read -ra _crates <<<"$CAL_RATES_SEAM"
    _cok=1; [ "${#_crates[@]}" = "${#_cks[@]}" ] || _cok=0
    for _r in "${_crates[@]}"; do case "$_r" in ''|0*|*[!0-9]*|??????????*) _cok=0 ;; esac; done
    [ "$_cok" = 1 ] || { echo "run-gates: --calibrate-width: GATE_CALIBRATION_RATES='$CAL_RATES_SEAM' is not ${#_cks[@]} positive whole rates, one per K in '$CALIBRATE_KS'" >&2; exit 2; }
  else
    CAL_CMD=()
    if [ -n "${GATE_SPAWN_CMD:-}" ]; then read -ra CAL_CMD <<<"$GATE_SPAWN_CMD"; else CAL_CMD=("$(type -P true 2>/dev/null)"); fi
    [ -n "${CAL_CMD[0]:-}" ] || { echo "run-gates: --calibrate-width: no spawn command resolves (no 'true' on PATH), so nothing can be timed" >&2; exit 1; }
    for _k in "${_cks[@]}"; do
      measure_spawn_rate "$_k"
      [ -n "$CAL_RATE" ] || { echo "run-gates: --calibrate-width: the spawn rate at K=$_k could not be measured (a spawn failed, or bash has no EPOCHREALTIME), so no pick is written" >&2; exit 1; }
      _crates+=("$CAL_RATE")
    done
  fi
  derive_calibrated_width "${_crates[@]}"
  _cfield=""
  for ((_i=0; _i<${#_cks[@]}; _i++)); do _cfield="$_cfield${_cfield:+,}${_cks[$_i]}=$((10#${_crates[$_i]}))"; done
  read_boot_epoch
  _ciso=$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null) || _ciso=""
  printf 'rates\t%s\n' "$_cfield"
  printf 'theta\t%s\n' "$CALIBRATE_THETA"
  printf 'pick\t%s\n'  "$CAL_PICK"
  derive_temp_path _tp "$CALIB_FILE"
  if [ -n "$_ciso" ] && { printf '%s\t%s\t%s\t%s\n' "$CAL_PICK" "$_cfield" "$_ciso" "$BOOT_EPOCH" > "$_tp"; } 2>/dev/null \
     && mv -f "$_tp" "$CALIB_FILE" 2>/dev/null; then
    printf 'cache\t%s\n' "$CALIB_FILE"
    exit 0
  fi
  rm -f "$_tp" 2>/dev/null
  echo "run-gates: --calibrate-width: the cache at $CALIB_FILE could not be written, so bars keep the width they had" >&2
  exit 1
fi

if [ "${1:-}" = "--print-profile" ]; then
  PROF_CEILING_MAX=$("$PYBIN" -c '
import json, sys
try:
    data = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception:
    sys.exit(1)
if not isinstance(data, list):
    sys.exit(1)
c = [l["ceiling"] for l in data if isinstance(l, dict) and isinstance(l.get("ceiling"), int)
     and not isinstance(l.get("ceiling"), bool) and l["ceiling"] > 0]
sys.stdout.write(str(max(c)) if c else "-")
' "$LEGS_FILE" 2>/dev/null) || PROF_CEILING_MAX=""
  printf 'name\t%s\n'      "$PROF_NAME"
  printf 'width\t%s\n'     "$JOBS"
  printf 'timeout\t%s\n'   "$PROF_TIMEOUT"
  printf 'wall\t%s\n'      "$WALL"
  printf 'queue\t%s\n'     "$TS_MAXWAIT"
  # How many bars the host turnstile admits at once, after the override (TOOL-aPairedSlots-1).
  printf 'slots\t%s\n'     "$PROF_SLOTS"
  [ -n "$PROF_CEILING_MAX" ] && printf 'ceiling_max\t%s\n' "$PROF_CEILING_MAX"
  printf 'ceilings\t%s\n'  "$CEILINGS_LIVE"
  # The EFFECTIVE threshold, 0 for off. INERT is a fact about the host and rides `line`; a second
  # reader decides it with a read of its own (TOOL-aGraftedHelix-7).
  printf 'mempause\t%s\n'  "$MEMPAUSE"
  printf 'spawnpause\t%s\n' "$SPAWNPAUSE"
  printf 'width_from\t%s\n' "$WIDTH_FROM"
  printf 'line\t%s\n'      "$PROF_LINE"
  exit 0
fi

echo "$PROF_LINE"

# ---- PROCESS-MONITOR DELEGATION. TOOL-aReapedSpinner-7.
#
# WHAT WAS ACTUALLY BROKEN, because this unit's first draft got it wrong and the spec audit caught
# it: the WALL path has walked and killed leg descendants since TOOL-aQuenchedHarness-1. The SIGNAL
# path never has. `cleanup` at the INT/TERM/HUP traps removed the scratch dir and released the
# turnstile and killed NOTHING, so a bar stopped by a signal -- a harness TaskStop, a Ctrl-C --
# deleted the directory its legs were writing into and left the whole tree running. That is the
# fourth failure in the sweep this kit was opened over.
#
# DETECTION IS THREE CONDITIONS AND IT RESOLVES HERE, before the first leg is dispatched, so a
# fallback is announced with the profile line rather than discovered mid-kill. The third condition
# is the one a file-presence test cannot see: the monitor may be installed and still refuse, if its
# declared roots do not admit this runner. The walk root is a leg process, and every leg is this
# runner's descendant, so asking whether THIS process is in scope answers it for all of them.
# The kit is found by the sibling resolver (TOOL-aRepatriatedFork-2 S3), and only once its conf says
# it is adopted, so a repo without the monitor pays no python spawn for the question.
#
# THE RESOLUTION RUNS INSIDE THE LEGS-PARSE PYTHON, below the turnstile (TOOL-aSparedSpawn-4 S10),
# which every bar starts anyway, so the question costs no python of its own. Only these DEFAULTS stay
# here, so a trap that fires during the turnstile wait reaches `run_leg_reap` with the runner's own
# walk; every other reader of these variables is on the tree-kill path, which runs after dispatch.
PROCMON_OK=0
PROCMON_WHY="not installed; tree kills use the runner's own depth-8 walk"
PROCMON_REAP=""; PROCMON_SCOPE=""
PROCMON_CONF=0
[ -f "$ROOT/.process-monitor.conf" ] && PROCMON_CONF=1

# ---- GENERATED OUTPUTS ARE PROVED FRESH BEFORE THE QUEUE (TOOL-aPrimedIndex-3) ---------------------
# The legs grade the declared generated outputs at the END of a bar, so a session learned an index
# was stale an hour in, regenerated it and ran the whole bar again. `regen.py --check` runs every
# check the kits declare, and a stale, failed or timed-out one, or a declaration it refuses, ends
# the run here with exit 2 before the turnstile: a refusal after an hour in another bar's queue is
# the cost this exists to remove. It sits after the profile line, which the canary reads first.
# NOTHING IS WRITTEN: the runner refuses and names the remedy, never regenerates the tree it grades.
# WHAT THIS DOES NOT CHECK: anything a leg does not grade on SOME bar. A skip leaves a stale output
# to its own leg only when that leg runs in this bar, and a guarded leg may not, so a skip can turn a
# refusal into a green; the pre-push hook therefore scrubs GATE_REGEN_CHECK from the bar that lands
# (TOOL-aPrimedIndex-6). A check red for a reason a regeneration cannot fix refuses too; the verb
# prints its output tail so the reader can tell. A declaration the verb refuses, its exit 2, gets its
# own remedy line, because `--regen` cannot cure it (TOOL-aPrimedIndex-7). A tree holding no kit
# descriptor at this kit's tool root is announced and costs no python spawn, which keeps a suite's
# scratch bars cheap.
case "$KITREL" in */*) _rg_tool=${KITREL%/*} ;; *) _rg_tool=. ;; esac; _rg_any=0
for _rg_f in "$_rg_tool"/*/kit.toml; do [ -f "$_rg_f" ] && { _rg_any=1; break; }; done
if [ "${GATE_REGEN_CHECK:-1}" = 0 ]; then
  echo "run-gates: generated outputs NOT checked — GATE_REGEN_CHECK=0; a stale one reds only where its own leg runs in this bar, and a guard may skip that leg"
elif [ ! -f "$KITDIR/regen.py" ]; then
  echo "run-gates: generated outputs NOT checked — no regen.py beside this runner; a stale one reds only where its own leg runs in this bar"
elif [ "$_rg_any" = 0 ]; then
  echo "run-gates: generated outputs — no kit descriptor under $_rg_tool/, so none is declared and none was checked"
else
  "$PYBIN" "$KITDIR/regen.py" --check; _rg_rc=$?
  if [ "$_rg_rc" = 2 ]; then
    echo "run-gates: REFUSED — declaration refused: a kit descriptor's generated-output rows cannot be read as written."
    echo "  fix the descriptor the line above names, then run the bar again; --regen cannot cure this"
    exit 2
  elif [ "$_rg_rc" != 0 ]; then
    echo "run-gates: REFUSED — a declared generated output above is stale or unproven, and a bar over it reds on that alone."
    echo "  regenerate every one, in stage order:  bash $KITREL/run-gates.sh --regen"
    echo "  then commit what it moved and run the bar again; GATE_REGEN_CHECK=0 skips this check"
    exit 2
  fi
fi


# The run id, derived ONCE here (TOOL-aFrugalTurnstile-5 S2): the beacon names it as `run`, and the
# run record below opens its directory under the same id. `GATE_RUN_ID` pins it, for the hook and arms.
TS_RUN="${GATE_RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)-$$}"

# ---- the turnstile: `slots` bars per HOST at a time, one by default (TOOL-aFrugalTurnstile-5, TOOL-aPairedSlots-2)
# Nothing coordinated two bars before this. `git worktree list` reports well into double figures on
# this node, and the sibling profiling build measured three full bars running at once with CPU at
# 39 %, both queues empty, and width 24 running 26 % SLOWER than width 8. The contended resource does
# not parallelise, so two concurrent bars are worse than two sequential ones and serializing them is
# the right shape for this machine rather than merely the polite one.
#
# THE KEY IS A HOST DIRECTORY, `GATE_TURNSTILE_DIR` or `~/.gov/gate-turnstile`, resolved absolutely.
# It was the git common dir, which made two REPOSITORIES two keys: on 2026-10-09 three repositories'
# bars ran at once on one host and starved each other into timeouts and load flakes. Only the beacon
# and the queue moved; the health log, the scratch owner record and its sweep stay per common dir,
# which is why `TS_COMMON` is still resolved. A host dir that cannot be created falls back to the
# common dir for both, announced, which is the per-repository behaviour this replaced.
#
# THE BEACON NAMES ITS HOLDER: `heartbeat`, `pid`, `nonce`, and `repo` (the holder's top level), `run`
# (its run id) and `ttl`. A waiter prints the holder from them and judges staleness against the
# HOLDER's `ttl`, because two repositories may run different TTLs; an absent field, as from an older
# runner's beacon, prints `-` and its TTL falls back to the waiter's own.
#
# NESTING. A holder exports `GATE_TURNSTILE_HOLDER`, its nonce, to its legs. A runner that inherits a
# value EQUAL to the live beacon's nonce runs inside the bar that holds the host, so it takes no
# ticket and records `queued_from` `nested`; without that, a suite's scratch-repo bar would queue
# behind the very bar whose leg started it. Compared, not merely present, so a value a dead bar left
# in some shell nests nothing once a successor holds. `--hold -- <command…>` takes the same turnstile
# for a command that is not this runner. `queued_from` reads `held`, `nested`, `expired`,
# `unticketed`, `docs`, `off` or `unresolved`, assigned in the block after the queue.
#
# THE DOCS KEY (TOOL-aPairedSlots-4). A DOC-ONLY bar — one whose `DOCS_BASE` resolved above, which
# `GATE_FULL` empties — takes no ticket and claims no slot: it creates `gate-docs-beacon/<run id>`
# beside the slots with the six beacon files a holder writes, exports its nonce, runs the ticker and
# arms the same nonce-guarded traps, and is admitted at once. Nothing caps how many run (owner,
# 2026-10-11). Non-doc waiters, the reap and the held count read the slots only, so a doc-only bar
# never delays, narrows or is named by a non-doc bar; nesting reads its beacon too. A doc-only run
# first sweeps the docs beacons of dead or stalled holders, nonce-guarded, since nothing else waits on
# them to notice. `--hold` is never doc-only.
#
# A COUNTING SEMAPHORE OF `TS_SLOTS` HOLDERS (TOOL-aPairedSlots-2), the profile row's `slots`. Each
# holder owns one beacon directory with its own six files: slot 1 is `gate-bar-beacon` itself, so a
# runner older than this unit, and every reader that names that path, still sees the first holder;
# slot k is `gate-bar-beacon.<k>`. The queue is unchanged and still one FIFO: only the ticket that
# sorts first may claim, it takes the first slot whose `mkdir` succeeds, and it gives up its ticket at
# once, so a second free slot is claimed one tick later by the next ticket and nobody overtakes. A
# waiter reaps dead or stalled holders slot by slot, each removal guarded by the nonce it judged; a
# release frees only the slot `TS_DIR` names, under that slot's nonce. A host whose repositories
# declare different counts admits the largest, since every runner claims among its own slots and all
# share slot 1 and the queue. At one slot every line printed and every file written is the
# single-holder runner's.
#
# WHAT THIS DOES NOT CHECK: NESTING TRUSTS AN INHERITED NONCE, which any process on this host can read
# from the beacon, so nesting decides contention and never a verdict; and a runner older than this
# change keys on its common dir and does not see the host beacon.
TS_COMMON=""; TS_DIR=""; TS_TICKET=""; TS_NONCE=""; TS_WAITED=0; TS_HELD=0; TS_Q=""; TS_UNTICKETED=0
TS_HOST=""; TS_DIR_C=""; TS_NESTED=0; TS_DOCS=0
if [ "${GATE_TURNSTILE:-1}" != 0 ]; then
  TS_COMMON=$RG_COMMON          # resolved once, above the width (TOOL-aSparedSpawn-2)
  TS_HOST=${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}
  if mkdir -p "$TS_HOST" 2>/dev/null && TS_HOST=$(cd "$TS_HOST" 2>/dev/null && pwd) && [ -n "$TS_HOST" ]; then
    TS_DIR_C="$TS_HOST/gate-bar-beacon"; TS_Q="$TS_HOST/gate-bar-queue"
  else
    if [ -n "$TS_COMMON" ]; then
      echo "run-gates: NOTE - the host turnstile directory '$TS_HOST' could not be created, so this bar queues per repository under $TS_COMMON" >&2
      TS_DIR_C="$TS_COMMON/gate-bar-beacon"; TS_Q="$TS_COMMON/gate-bar-queue"
    fi
    TS_HOST=""
  fi
fi
# THE SLOT PATHS, BUILT ONCE (TOOL-aPairedSlots-2). An array rather than a path function, so a claim,
# a reap or a count over the slots forks nothing per slot on a host where every fork is the cost.
TS_SLOTS=${PROF_SLOTS:-1}; TS_SLOT=""; TS_SLOT_DIRS=(); TS_HELD_N=0
# THE SHARED-WIDTH RULE (TOOL-aPairedSlots-3): what a bar's pool width becomes when it acquires a slot
# while another is held. `half` divides the width by the held count; `full` leaves it. The value is
# the two-bar A/B's (TOOL-aPairedSlots-9), which sets it; `full` changes no width, so it is the value
# shipped until that measurement says otherwise. The MEMORY PAUSE needs no counterpart: it reads
# `/proc/meminfo` or the cgroup pair, both host-wide, so two bars already pause on one reading.
TS_SHARE_RULE=full
if [ -n "$TS_DIR_C" ]; then
  TS_SLOT_DIRS=("$TS_DIR_C"); _ts_k=2
  while [ "$_ts_k" -le "$TS_SLOTS" ]; do TS_SLOT_DIRS+=("$TS_DIR_C.$_ts_k"); _ts_k=$((_ts_k + 1)); done
  unset _ts_k
fi
measure_held_slots() { # -> TS_HELD_N, how many of this runner's slot paths exist; builtin tests only
  local d; TS_HELD_N=0
  for d in ${TS_SLOT_DIRS[@]+"${TS_SLOT_DIRS[@]}"}; do [ -d "$d" ] && TS_HELD_N=$((TS_HELD_N + 1)); done
  return 0
}
TS_DOCS_ROOT=""; [ -n "$TS_DIR_C" ] && TS_DOCS_ROOT="${TS_DIR_C%/*}/gate-docs-beacon"
scan_dead_docs_beacons() { # -> removes each docs beacon whose pid is dead or whose heartbeat outlived its ttl, nonce-guarded
  local d hpid hb hn httl age mt cur
  [ -n "$TS_DOCS_ROOT" ] && [ -d "$TS_DOCS_ROOT" ] || return 0
  for d in "$TS_DOCS_ROOT"/*; do
    [ -d "$d" ] || continue
    # THE NONCE FIRST (TOOL-aPairedSlots-15), as `ts_try_reap` reads it: every fact judged below then
    # belongs to the holder whose nonce guards the removal. Each one-line beacon file is read by the
    # builtin, as `ts_tick_start` reads the nonce (TOOL-aSweptBar-5): a missing file reads empty.
    hn=""; { IFS= read -r hn < "$d/nonce"; } 2>/dev/null
    hpid=""; { IFS= read -r hpid < "$d/pid"; } 2>/dev/null
    hb=""; { IFS= read -r hb < "$d/heartbeat"; } 2>/dev/null
    httl=""; { IFS= read -r httl < "$d/ttl"; } 2>/dev/null; num_ok "$httl" || httl=$TS_TTL
    # AN UNFINISHED BEACON, interrupted between its `mkdir` and its first writes, has neither a pid nor
    # a heartbeat, and nothing else would ever sweep it. Its directory's age is the only clock it has;
    # one that cannot be read is left alone, since a beacon being written right now has none yet.
    if [ -z "$hpid" ] && ! num_ok "$hb"; then
      mt=$(date -r "$d" +%s 2>/dev/null) || mt=""
      num_ok "$mt" || continue
      age=$(( EPOCHSECONDS - mt ))
      if [ "$age" -gt "$httl" ] && { cur=""; { IFS= read -r cur < "$d/nonce"; } 2>/dev/null; [ "$cur" = "$hn" ]; }; then
        printf 'run-gates: sweeping the docs beacon of an unfinished holder (no pid or heartbeat, %ss old)\n' "$age" >&2
        rm -rf "$d" 2>/dev/null
      fi
      continue
    fi
    if [ -n "$hpid" ] && ! ts_alive "$hpid"; then
      cur=""; { IFS= read -r cur < "$d/nonce"; } 2>/dev/null
      [ "$cur" = "$hn" ] || continue
      printf 'run-gates: sweeping the docs beacon of a dead holder (pid %s)\n' "$hpid" >&2
      rm -rf "$d" 2>/dev/null; continue
    fi
    case "$hb" in ''|*[!0-9]*) continue ;; esac
    age=$(( EPOCHSECONDS - hb ))
    if [ "$age" -gt "$httl" ] && { cur=""; { IFS= read -r cur < "$d/nonce"; } 2>/dev/null; [ "$cur" = "$hn" ]; }; then
      printf 'run-gates: sweeping the docs beacon of a stalled holder (heartbeat %ss old, ttl %ss)\n' "$age" "$httl" >&2
      rm -rf "$d" 2>/dev/null
    fi
  done
  return 0
}
# ONE SLOT PER WORKTREE (TOOL-aPairedSlots-5). Everything a bar keeps under its worktree's git dir —
# the ledger, the run records and `current`, the summary and failure files, the gate logs, the greens
# and the queue files — assumes one writer, which the single-holder turnstile guaranteed. Two
# worktrees have two git dirs, so admitting two bars keeps that true for them; two bars in ONE
# worktree would break it. So the head does not claim while a holder's `repo` names this run's top
# level, and waits as it waits for a full host. A holder with no readable `repo`, as an older
# runner's beacon may be, does not block: it cannot be told apart from another worktree's.
# EVERY HOLDER PRESENT, AT EVERY COUNT (TOOL-aPairedSlots-15): slot 1, each `.<k>` beside it whatever
# this runner's own count, and each docs beacon. Read only up to its own count, a bar run at a lower
# count than a neighbour in its worktree claimed beside it, and the docs key was never asked; the
# nesting test reads every beacon for the same reason. At one slot with no such neighbour this finds
# slot 1 alone, which the claim tests anyway, so a bar at the kit default waits and prints as before.
TS_SAME=""
check_worktree_unheld() { # -> rc 0 when no holder names this run's top level; rc 1 with that holder's path in TS_SAME
  local d r
  TS_SAME=""
  for d in "$TS_DIR_C" "$TS_DIR_C".* ${TS_DOCS_ROOT:+"$TS_DOCS_ROOT"/*}; do
    [ -d "$d" ] || continue
    r=""; { IFS= read -r r < "$d/repo"; } 2>/dev/null
    if [ -n "$r" ] && [ "$r" = "$ROOT" ]; then TS_SAME=$d; return 1; fi
  done
  return 0
}
render_same_holder() { # -> prints TS_SAME's key, repo, run and pid, for a line that says why a bar waits
  local k
  case "$TS_SAME" in
    "$TS_DIR_C") k="slot 1" ;;
    "$TS_DIR_C".*) k="slot ${TS_SAME##*.}" ;;
    *) k="the docs key" ;;
  esac
  printf '%s — %s run %s pid %s' "$k" "$(cat "$TS_SAME/repo" 2>/dev/null)" \
    "$(cat "$TS_SAME/run" 2>/dev/null || echo -)" "$(cat "$TS_SAME/pid" 2>/dev/null || echo -)"
}
resolve_free_slot() { # -> rc 0 with TS_DIR and TS_SLOT set by the first slot whose mkdir succeeds, in slot order
  local i=0 d
  for d in ${TS_SLOT_DIRS[@]+"${TS_SLOT_DIRS[@]}"}; do
    i=$((i + 1))
    if mkdir "$d" 2>/dev/null; then TS_DIR=$d; TS_SLOT=$i; return 0; fi
  done
  return 1
}

# THE HEALTH LOG (I3, TOOL-aGraftedHelix-8), derived from the common dir this runner already holds,
# so no self-heal site below spawns git: the turnstile's here, WORK_COMMON's once it is resolved.
RG_HEALTH_LOG=""
[ -z "$TS_COMMON" ] || RG_HEALTH_LOG=$(derive_health_log "$TS_COMMON")

TS_TICK=${GATE_TURNSTILE_TICK:-2}
# The heartbeat cadence is DERIVED from the TTL and declared nowhere else, so the pair cannot drift —
# the same rule TS_MAXWAIT above already follows. Six, so a single missed tick cannot trip the reap.
TS_TICK_EVERY=$(( TS_TTL / 6 )); [ "$TS_TICK_EVERY" -ge 1 ] || TS_TICK_EVERY=1
TS_TICK_PID=""
TS_TICK_LIVE=0

ts_hb()  { local _tp; [ -n "$TS_DIR" ] && derive_temp_path _tp "$TS_DIR/heartbeat" && printf '%s' "$EPOCHSECONDS" > "$_tp" 2>/dev/null && mv -f "$_tp" "$TS_DIR/heartbeat" 2>/dev/null || true; }
ts_alive(){ kill -0 "$1" 2>/dev/null; }

# RELEASE IS NONCE-GUARDED. A run whose beacon was reaped for being stale must never delete its
# successor's: without the nonce, a slow holder that comes back to life removes a directory it no
# longer owns and two bars run anyway — the exact failure this unit exists to prevent, arriving
# through its own cleanup path.
ts_release() {
  [ -n "$TS_DIR" ] || return 0
  local _cur=""; { IFS= read -r _cur < "$TS_DIR/nonce"; } 2>/dev/null
  if [ "$_cur" = "$TS_NONCE" ]; then rm -rf "$TS_DIR" 2>/dev/null || true; fi
  TS_DIR=""
}
ts_drop_ticket() { [ -n "$TS_TICKET" ] && rm -f "$TS_TICKET" 2>/dev/null; TS_TICKET=""; }

# THE HEARTBEAT TICKER. TOOL-aQuenchedHarness-8. Three properties, and each one is a defect this
# would otherwise have introduced — none of them is decoration:
#
# 1. DETACHED FROM JOB CONTROL. The turnstile block and the dispatch pool are the SAME shell (see the
#    dispatch comment below: one shell owns every worker so it can block on `wait -n`). An undetached
#    ticker is a live job FOREVER: `live()` counts it, `GATE_JOBS=1` never satisfies
#    `[ "$(live)" -lt "$JOBS" ]`, and the terminal `wait` never returns. The unit that exists to stop
#    the bar wedging would wedge every bar, starting with the documented serial rollback. Hence
#    `disown`, and hence the arm that runs a two-leg fixture bar at GATE_JOBS=1 under an outer bound.
#
# 2. NONCE-GUARDED, exactly as `ts_release` above is, and for the same reason one level along. No
#    trap runs on SIGKILL, and `TS_DIR_C` is a CONSTANT path every later bar recreates — so a killed
#    holder's orphan would refresh its SUCCESSOR's heartbeat forever, disabling the stale-holder
#    signal repo-wide. That converts a recoverable wedge into a permanent one, which is strictly
#    worse than the defect this ticker fixes.
#
# 3. PID-CHECKED as well, because the nonce catches a beacon that was replaced and not a holder that
#    simply died before anything replaced it. Two independent exits, mirroring `ts_try_reap`'s own
#    two-signal design.
#
# The tick is `sleep` then a guarded write, never a write then a sleep: a ticker that writes once
# before checking anything is a ticker that can refresh a beacon it never owned.
#
# NO FORK BUT THE SLEEP AND THE MOVE (TOOL-aSparedSpawn-15 S3). The nonce was `$(cat ...)` and the
# time a `date +%s` subshell, two spawns a tick, and a spawn on a loaded node `a` costs 632 to 818 ms,
# so a tick ran late by over a second and a live holder read as stalled. Both are builtins now: `read`
# for the nonce, `$EPOCHSECONDS` for the time. ONE RULE, TOOL-aSparedSpawn-16 S15: the runner
# requires bash 5's `EPOCHSECONDS` and reads it bare at every site, with no fallback, because a
# `$(date +%s)` fallback is the banned `epoch-date` fork and no supported bash lacks the variable.
# The heartbeat's temp name is `derive_temp_path`'s, built from `$SRANDOM` with no fork on bash 5.1
# and later; bash 5.0 pays one `mktemp -u` a tick for it (TOOL-dRedressedBar-24).
ts_tick_start() {
  [ -n "$TS_DIR" ] || return 0
  local _hp=$$ _d=$TS_DIR _n=$TS_NONCE _every=$TS_TICK_EVERY _cur _tp
  (
    while :; do
      sleep "$_every"
      _cur=""; { IFS= read -r _cur < "$_d/nonce"; } 2>/dev/null
      [ "$_cur" = "$_n" ] || exit 0
      kill -0 "$_hp" 2>/dev/null || exit 0
      derive_temp_path _tp "$_d/heartbeat" && printf '%s' "$EPOCHSECONDS" > "$_tp" 2>/dev/null \
        && mv -f "$_tp" "$_d/heartbeat" 2>/dev/null || true
    done
  # STDIO GOES NOWHERE, and that is the whole point. Backgrounded and disowned, this
  # subshell and its `sleep` still INHERIT the runner's fd 1 and 2, and the sleep outlives
  # the bar with ppid 1 -- so anything reading the bar's output to EOF blocked for up to
  # TS_TICK_EVERY seconds AFTER it had already exited. `ts_tick_stop` does not help: it
  # kills this subshell and the sleep survives holding the fd. Measured on a 2-leg fixture:
  # captured 307s -> 19s. The body writes only to files and already swallows its own
  # errors, and the degraded-start NOTE is emitted below, outside this subshell.
  ) >/dev/null 2>&1 &
  TS_TICK_PID=$!
  disown "$TS_TICK_PID" 2>/dev/null || true
  if ts_alive "$TS_TICK_PID"; then
    TS_TICK_LIVE=1
  else
    TS_TICK_PID=""
    # DEGRADED IS ANNOUNCED. A reaper reading a heartbeat nothing writes is not a reaper, and a run
    # that proceeds silently under an unrefreshed bound is indistinguishable from one that is fine.
    echo "run-gates: NOTE - the turnstile heartbeat ticker did not start, so this run's beacon is refreshed only when a leg completes and a leg longer than ${TS_TTL}s can be reaped mid-run" >&2
  fi
}

ts_tick_stop() {
  [ -n "$TS_TICK_PID" ] || return 0
  kill "$TS_TICK_PID" 2>/dev/null || true
  TS_TICK_PID=""; TS_TICK_LIVE=0
}

# Reap a holder that cannot still be holding. TWO independent signals, because each covers a case the
# other cannot: a dead PID is immediate and certain, and a stale heartbeat catches the holder whose
# PID was recycled or which is alive but wedged.
ts_try_reap() {
  local d hpid hb age httl hn cur reaped=1
  # SLOT BY SLOT (TOOL-aPairedSlots-2): each slot is judged by its own pid and its own ttl, every dead
  # or stalled one is reaped on this tick, and a live neighbour is never touched. THE REMOVAL IS
  # NONCE-GUARDED, and the nonce is read FIRST (TOOL-aPairedSlots-15): every fact the slot is judged by
  # then belongs to the holder that nonce names, and the nonce must still be there at the removal, so a
  # slot a successor claimed after the judgement survives. Read last, a successor's nonce could vouch
  # for a dead holder's pid. That narrows TOOL-aReapedTicket-4's race to the instant between the
  # re-read and the `rm`; it does not close it.
  for d in ${TS_SLOT_DIRS[@]+"${TS_SLOT_DIRS[@]}"}; do
    [ -d "$d" ] || continue
    hn=""; { IFS= read -r hn < "$d/nonce"; } 2>/dev/null
    hpid=""; { IFS= read -r hpid < "$d/pid"; } 2>/dev/null
    hb=""; { IFS= read -r hb < "$d/heartbeat"; } 2>/dev/null
    # THE HOLDER'S TTL is the bound (TOOL-aFrugalTurnstile-5 S3): on a host-wide beacon the holder may be
    # another repository running a longer one. Anything but a positive integer, as from an older
    # runner's beacon, falls back to this waiter's own.
    httl=""; { IFS= read -r httl < "$d/ttl"; } 2>/dev/null
    num_ok "$httl" || httl=$TS_TTL
    if [ -n "$hpid" ] && ! ts_alive "$hpid"; then
      cur=""; { IFS= read -r cur < "$d/nonce"; } 2>/dev/null
      [ "$cur" = "$hn" ] || continue
      printf 'run-gates: reaping the beacon of a dead holder (pid %s)\n' "$hpid" >&2
      rm -rf "$d" 2>/dev/null
      add_health_event "$RG_HEALTH_LOG" run-gates beacon-reaped "dead holder pid $hpid"; reaped=0; continue
    fi
    case "$hb" in ''|*[!0-9]*) hb=0 ;; esac
    age=$(( EPOCHSECONDS - hb ))
    if [ "$hb" != 0 ] && [ "$age" -gt "$httl" ]; then
      cur=""; { IFS= read -r cur < "$d/nonce"; } 2>/dev/null
      [ "$cur" = "$hn" ] || continue
      printf 'run-gates: reaping the beacon of a stalled holder (heartbeat %ss old, ttl %ss)\n' "$age" "$httl" >&2
      rm -rf "$d" 2>/dev/null
      add_health_event "$RG_HEALTH_LOG" run-gates beacon-reaped "stalled holder heartbeat ${age}s ttl ${httl}s"; reaped=0
    fi
  done
  return "$reaped"
}

# Reap a QUEUE TICKET whose owner cannot still be waiting (TOOL-aReapedTicket-2) — the other half of
# `ts_try_reap`, which looks only at the beacon and RETURNS ON ITS FIRST LINE when there is no beacon
# to look at. That asymmetry was the deadlock: a bar killed while queued left a ticket that sorts
# first forever, nothing pruned it, and every later bar waited out the full TS_MAXWAIT and then ran
# UNQUEUED. The turnstile was not slowed by that — it was permanently defeated, by one death, for
# good. Measured before the fix: one leaked ticket, no beacon at all, and the next bar still reached
# `WAIT EXPIRED` and left the ticket behind for the bar after it.
#
# TWO SIGNALS, mirroring the holder's, and BOTH are chosen so they CANNOT BE TRUE OF A LIVE WAITER.
# That constraint is the whole design, not a nicety: a sweep that deletes a LIVE waiter's ticket
# leaves that waiter unable to ever match the acquire predicate, which turns a wedge affecting future
# bars into one affecting the bar in front of you. Strictly worse. So neither signal is a heuristic:
#
#   dead pid       a live waiter's own pid answers, by definition. NEGATIVE-ONLY, exactly as for the
#                  holder — a pid that answers proves nothing, because pids are recycled, so success
#                  only withholds the sweep and never confers life.
#   older than     a live waiter FAILS OPEN at TS_MAXWAIT and drops its own ticket, so a ticket past
#   TS_MAXWAIT     that bound cannot belong to one. DERIVED from the fail-open rule below rather than
#                  chosen, which is why this whole unit introduces NO new constant.
#
# THE AGE IS READ FROM THE TICKET NAME, never its mtime. The name is what the sort order is derived
# from, and a name and an mtime that disagree would give the sweep and the ordering two opinions
# about one ticket. The cutoff is computed ONCE per call and compared as a STRING: `%Y%m%dT%H%M%S` is
# lexicographically ordered by time, which is already why the queue sorts correctly — so the
# staleness test reuses that property instead of parsing a date per ticket.
#
# ON THE PID'S REACH: a ticket's pid was written by another bash process, and two different msys
# runtimes do not necessarily share a pid table. That can only make `kill -0` answer for the wrong
# process or answer when it should not — and because the signal is negative-only, both directions
# merely WITHHOLD the fast sweep and defer to the age signal. It cannot cause a false sweep, which is
# the only direction that would hurt.
ts_sweep_queue() {
  local t base pid stamp cutoff swept=0
  [ -n "$TS_Q" ] && [ -d "$TS_Q" ] || return 1
  # If `date` cannot produce the cutoff the AGE SIGNAL IS UNARMED, and it says so rather than leaving
  # a reaper silently down to one signal — which is indistinguishable from one that is working.
  cutoff=$(date -u -d "@$(( EPOCHSECONDS - TS_MAXWAIT ))" +%Y%m%dT%H%M%S 2>/dev/null) || cutoff=""
  if [ -z "$cutoff" ]; then
    printf 'run-gates: NOTE - this host cannot compute a queue staleness cutoff, so a leaked ticket whose pid has been RECYCLED will not be swept this run\n' >&2
  fi
  for t in "$TS_Q"/*; do
    [ -e "$t" ] || continue
    base=${t##*/}
    # NEVER OUR OWN, guarded explicitly. Both signals already exclude it — our pid answers and our
    # ticket is young — so this line is redundant TODAY. That is exactly the point: it is what stops
    # a later edit to either signal deleting the ticket of the process doing the sweeping.
    [ -n "$TS_TICKET" ] && [ "$base" = "${TS_TICKET##*/}" ] && continue
    stamp=${base%%-*}
    pid=${base#*-}; pid=${pid%%-*}
    # A ticket whose name we cannot read is one we must NOT delete.
    case "$stamp" in [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]T[0-9][0-9][0-9][0-9][0-9][0-9]) ;; *) continue ;; esac
    case "$pid" in ''|*[!0-9]*) pid="" ;; esac
    if [ -n "$pid" ] && ! ts_alive "$pid"; then
      printf 'run-gates: sweeping the queue ticket of a dead waiter (pid %s)\n' "$pid" >&2
      rm -f "$t" 2>/dev/null && { swept=1; add_health_event "$RG_HEALTH_LOG" run-gates ticket-swept "dead waiter pid $pid"; }
      continue
    fi
    if [ -n "$cutoff" ] && [ "$stamp" \< "$cutoff" ]; then
      printf 'run-gates: sweeping a queue ticket past the bounded wait (stamp %s, cutoff %s)\n' "$stamp" "$cutoff" >&2
      rm -f "$t" 2>/dev/null && { swept=1; add_health_event "$RG_HEALTH_LOG" run-gates ticket-swept "stamp $stamp past $cutoff"; }
    fi
  done
  [ "$swept" = 1 ]
}

# NESTED (S5): inside the bar that holds this host, as its exported nonce says, so no ticket is taken
# and nothing is claimed; the inherited value stays exported for this run's own legs.
# EVERY SLOT BEACON PRESENT is read, slot 1 and each `.<k>` beside it, not 1 to this runner's own
# count (TOOL-aPairedSlots-2 S5): a fixture bar whose table declares fewer slots than the holder that
# started it must still find its parent's nonce. A builtin glob, so an unset holder costs nothing.
TS_NEST_DIR=""
if [ -n "$TS_DIR_C" ] && [ -n "${GATE_TURNSTILE_HOLDER:-}" ]; then
  for _ts_d in "$TS_DIR_C" "$TS_DIR_C".* ${TS_DOCS_ROOT:+"$TS_DOCS_ROOT"/*}; do
    [ -d "$_ts_d" ] || continue
    _ts_n=""; { IFS= read -r _ts_n < "$_ts_d/nonce"; } 2>/dev/null
    [ "$_ts_n" = "$GATE_TURNSTILE_HOLDER" ] && { TS_NEST_DIR=$_ts_d; break; }
  done
  unset _ts_d _ts_n
fi
if [ -n "$TS_NEST_DIR" ]; then
  TS_NESTED=1
  ts_hr=""; { IFS= read -r ts_hr < "$TS_NEST_DIR/run"; } 2>/dev/null
  ts_hd=""; { IFS= read -r ts_hd < "$TS_NEST_DIR/repo"; } 2>/dev/null
  ts_hp=""; { IFS= read -r ts_hp < "$TS_NEST_DIR/pid"; } 2>/dev/null
  echo "gate queue: nested under ${ts_hr:--} — ${ts_hd:--} pid ${ts_hp:--}"
elif [ -n "$TS_DIR_C" ] && [ -n "${DOCS_BASE:-}" ] && [ "${#TS_HOLD[@]}" = 0 ]; then
  # THE DOCS KEY (TOOL-aPairedSlots-4): admitted at once, visible, nestable, released on every exit.
  TS_DOCS=1
  TS_NONCE="$$-$EPOCHSECONDS-$RANDOM"
  scan_dead_docs_beacons
  # ITS OWN WORKTREE FIRST (TOOL-aPairedSlots-15 F1): a doc-only bar waits for a holder in its own
  # worktree, whose git dir it would otherwise share, and never for another worktree's, so the host
  # queue is still never joined. Bounded and failing open at the queue's own bound.
  ts_start=$EPOCHSECONDS
  if ! check_worktree_unheld; then
    echo "gate queue: docs-only — this worktree's bar holds $(render_same_holder) — waiting for it"
    while ! check_worktree_unheld; do
      ts_try_reap; scan_dead_docs_beacons
      if [ $(( EPOCHSECONDS - ts_start )) -ge "$TS_MAXWAIT" ]; then
        echo "run-gates: turnstile WAIT EXPIRED after $(( EPOCHSECONDS - ts_start ))s (bound ${TS_MAXWAIT}s) — this doc-only bar runs beside its worktree's holder" >&2
        break
      fi
      sleep "$TS_TICK"
    done
  fi
  if mkdir -p "$TS_DOCS_ROOT" 2>/dev/null && mkdir "$TS_DOCS_ROOT/$TS_RUN" 2>/dev/null; then
    TS_DIR="$TS_DOCS_ROOT/$TS_RUN"
    printf '%s' "$EPOCHSECONDS" > "$TS_DIR/heartbeat" 2>/dev/null || true
    printf '%s' "$$"        > "$TS_DIR/pid" 2>/dev/null || true
    printf '%s' "$ROOT"     > "$TS_DIR/repo" 2>/dev/null || true
    printf '%s' "$TS_RUN"   > "$TS_DIR/run" 2>/dev/null || true
    printf '%s' "$TS_TTL"   > "$TS_DIR/ttl" 2>/dev/null || true
    printf '%s' "$TS_NONCE" > "$TS_DIR/nonce" 2>/dev/null || true
    export GATE_TURNSTILE_HOLDER="$TS_NONCE"
    ts_tick_start
    trap 'ts_tick_stop; ts_release; ts_drop_ticket' EXIT
    trap 'ts_tick_stop; ts_release; ts_drop_ticket; exit 130' INT
    trap 'ts_tick_stop; ts_release; ts_drop_ticket; exit 143' TERM
    trap 'ts_tick_stop; ts_release; ts_drop_ticket; exit 129' HUP
  else
    echo "run-gates: NOTE - the docs beacon under '$TS_DOCS_ROOT' could not be created, so this doc-only bar runs UNQUEUED and unnamed" >&2
  fi
  echo "gate queue: docs-only — admitted on the docs key, not queued"
  export GATE_TURNSTILE_HELD="${GATE_TURNSTILE_HELD:-}${GATE_TURNSTILE_HELD:+,}$TS_NONCE"
elif [ -n "$TS_DIR_C" ]; then
  TS_NONCE="$$-$EPOCHSECONDS-$RANDOM"
  mkdir -p "$TS_Q" 2>/dev/null || true
  # EVERY RUN TAKES A TICKET, including an uncontended one. A ticket whose name sorts by time is all
  # the ordering there is: every waiter reads the same listing and derives the same total order
  # independently, so there is no counter file to corrupt and no coordinator to elect.
  TS_TICKET="$TS_Q/$(date -u +%Y%m%dT%H%M%S)-$$-$RANDOM"
  : > "$TS_TICKET" 2>/dev/null || TS_TICKET=""
  # THE TICKET GETS A HANDLER THE MOMENT IT EXISTS (TOOL-aReapedTicket-1). Until this line the only
  # `ts_drop_ticket` trap was armed 24 lines below, inside the branch that WINS the beacon — so a
  # waiter polling the loop below ran with no handler at all, for the entire queue wait.
  #
  # That is the same defect the claim-time trap's own comment argues against, one participant over,
  # and the consequence is worse because the window is the whole wait rather than a few seconds: the
  # leak needs no SIGKILL, an ordinary Ctrl-C on a queued bar leaves a ticket that sorts first
  # FOREVER. Nothing prunes it, every later bar then burns the full TS_MAXWAIT and runs UNQUEUED,
  # and the turnstile is not slowed by that — it is permanently defeated. Measured before the fix:
  # one leaked ticket, no beacon at all, and the next bar still reached `WAIT EXPIRED`.
  #
  # DELIBERATELY NOT `ts_release; ts_drop_ticket`. No beacon is held here and `ts_release` returns on
  # its first line, so the release half would be inert code implying a waiter can release something
  # it never claimed. Both traps below REPLACE this one — `trap` replaces rather than appends — and
  # both are strictly wider, so there is never an instant with no handler and never two handlers
  # racing.
  #
  # THE SIGNAL ARMS RE-EXIT, and that is not cosmetic symmetry with the `cleanup` traps below — it
  # is required for correctness, and the first draft of this line got it wrong. Setting a trap on
  # INT REPLACES bash's default disposition, so a handler that does not exit drops the ticket and
  # then RESUMES the loop below. That run is now ticketless, its acquire predicate can never match
  # again, and it spins to the full bound — the exact "a waiter that can never acquire" state this
  # unit exists to remove, re-created by its own fix. Caught by running it: `timeout -s INT` had to
  # escalate to KILL because the runner would not die.
  trap 'ts_drop_ticket' EXIT
  trap 'ts_drop_ticket; exit 130' INT
  trap 'ts_drop_ticket; exit 143' TERM
  trap 'ts_drop_ticket; exit 129' HUP
  ts_start=$EPOCHSECONDS; ts_lastpos=""; ts_announced=0
  # A RUN WITH NO TICKET CANNOT EVER ACQUIRE, so it must not wait to find that out. Every iteration
  # of the loop below opens with `[ -n "$TS_TICKET" ]`, which is false forever once the write above
  # failed — so the run burned the ENTIRE TS_MAXWAIT (7200s at the shipped fallback) to reach a
  # fail-open it was entitled to on the first tick. Same class as the wedge this unit is about: a
  # loop waiting on a condition that cannot change.
  if [ -z "$TS_TICKET" ]; then
    echo "run-gates: could not create a queue ticket in $TS_Q — running UNQUEUED rather than waiting out the ${TS_MAXWAIT}s bound on a predicate that can never match" >&2
    TS_UNTICKETED=1
  fi
  while [ -n "$TS_TICKET" ]; do
    # THE CLAIM IS A DIRECTORY CREATE, which is atomic on every filesystem this runs on and needs no
    # `flock` — which does not exist on this platform. The heartbeat is written FIRST on winning, so
    # a just-claimed holder is never mistaken by a waiter for one with no clock.
    # THE DEAD-WAITER SWEEP IS NOT HERE, AND THAT IS THE FIX. It was here, silently, and being here
    # is what broke it: this loop deleted the dead ticket before `ts_sweep_queue` at the wait branch
    # below could ever see one, so the sweep that ANNOUNCES never spoke and arm 16 of
    # `run-gates.turnstile.test.sh` red on a message that was never going to be printed. Two
    # implementations of one predicate, and the quiet one won the race.
    #
    # The sweep now happens ONCE, in `ts_sweep_queue`, reached from the failure of the acquire
    # below on every tick. That call is NOT guarded on a beacon existing — which is the guard that
    # made `ts_try_reap` unable to see this wedge at all — so the wedge is still swept. The cost is
    # one extra tick before acquiring behind a dead ticket; the gain is a reason on stderr naming
    # the pid, which is the whole difference between a fixed wedge and a wedge nobody can see was
    # fixed. TOOL-aBoundedCeiling-12.
    if [ -n "$TS_TICKET" ] && [ "$(ls -1 "$TS_Q" 2>/dev/null | LC_ALL=C sort | head -1)" = "$(basename "$TS_TICKET")" ] \
       && check_worktree_unheld && resolve_free_slot; then
      printf '%s' "$EPOCHSECONDS" > "$TS_DIR/heartbeat" 2>/dev/null || true
      printf '%s' "$$"        > "$TS_DIR/pid" 2>/dev/null || true
      # The holder's name, for a waiter's queue line and a nested run's, and the TTL a waiter judges
      # it by (S2, S3). Written before the nonce, so a run that matches the nonce reads all three.
      printf '%s' "$ROOT"     > "$TS_DIR/repo" 2>/dev/null || true
      printf '%s' "$TS_RUN"   > "$TS_DIR/run" 2>/dev/null || true
      printf '%s' "$TS_TTL"   > "$TS_DIR/ttl" 2>/dev/null || true
      printf '%s' "$TS_NONCE" > "$TS_DIR/nonce" 2>/dev/null || true
      TS_HELD=1
      # The nonce goes to every leg, so a runner one of them starts NESTS rather than queueing behind
      # this bar (S5). Exported only on a hold: no other path owns the beacon it would name.
      export GATE_TURNSTILE_HOLDER="$TS_NONCE"
      # STARTED HERE, after the nonce exists and before the traps below, because the ticker's first
      # act is to compare that nonce. Started earlier it would have nothing to compare against.
      ts_tick_start
      # THE RELEASE TRAP GOES ON HERE, at the instant the beacon becomes ours, and not with the
      # scratch-dir trap further down. Everything between this line and there — the manifest
      # parse, the fingerprint, the whole run-record setup — is time during which the beacon is
      # HELD and, without this, no trap would release it. A signal in that window killed the run
      # and left the repository queueing behind nobody until the TTL expired.
      #
      # Measured, and it is the reason this is not merely tidy: the turnstile arms passed three
      # times in a row run alone and failed on TERM and HUP the moment they ran after another
      # harness. Under that load the window is seconds wide — process creation on this platform
      # has been measured 25x slower under contention — so the window is not theoretical and it is
      # widest exactly when two bars are most likely to collide.
      #
      # THE SIGNAL ARMS RE-EXIT, for the reason the ticket trap above states and which applies here
      # unchanged: this spelling was a single `EXIT INT TERM HUP` handler, so an interrupt in this
      # window released the beacon and then RESUMED — leaving the run believing it still held a
      # lock it had just given away, and running the whole bar unqueued beside whoever claimed
      # next. That is the two-bar condition this unit exists to prevent, arriving through its own
      # cleanup path, which is the same shape the nonce guard was written for.
      # `ts_tick_stop` FIRST in every handler: the ticker must stop before the beacon it refreshes
      # is removed, or a tick can land between the two and recreate a heartbeat inside a directory
      # this run has just given up. It is a belt over the nonce guard's braces, and it costs one
      # signal. These handlers do NOT cover SIGKILL — nothing does — which is why the guards inside
      # the ticker are the real mitigation and this line is only the tidy path.
      trap 'ts_tick_stop; ts_release; ts_drop_ticket' EXIT
      trap 'ts_tick_stop; ts_release; ts_drop_ticket; exit 130' INT
      trap 'ts_tick_stop; ts_release; ts_drop_ticket; exit 143' TERM
      trap 'ts_tick_stop; ts_release; ts_drop_ticket; exit 129' HUP
      # S4 (TOOL-aShardedFloor-1), and the GUARD is the whole of it. `TS_WAITED` is refreshed at
      # the BOTTOM of this loop and this path breaks above it, so a contended acquire records the
      # previous tick's value and understates the wait by up to one `TS_TICK`.
      #
      # Refreshing unconditionally — which is the obvious fix and the one first specced — breaks
      # the UNCONTENDED case instead: the clock reads whole seconds and truncates, the five processes
      # above (`ls`, `sort`, `head`, `basename`, `mkdir`) sometimes straddle a second boundary,
      # and the line below then prints `waited 1s` where `run-gates.turnstile.test.sh` asserts
      # `^gate queue: waited 0s$`. Measured on node a: 4 of 60 first-iteration acquires crossed,
      # on an idle box, in a leg that normally runs inside a concurrent bar where process
      # creation is 25x slower. `ts_announced` is 1 only once the loop has reported a position,
      # which is exactly the predicate "this run actually queued".
      #
      # RESIDUAL, named rather than left to be rediscovered: `ts_try_reap && continue` above
      # skips both this refresh AND the announce, so a run that reaps a stale holder on its first
      # iteration still records the stale value. Closing that needs a second predicate and is
      # deliberately not in this unit.
      [ "$ts_announced" = 1 ] && TS_WAITED=$(( EPOCHSECONDS - ts_start ))
      break
    fi
    # BOTH probes, on the same tick, and either one making progress re-tries the claim at once.
    # `ts_try_reap` first because it is the cheaper of the two and the commoner case; `||` because
    # when there IS a dead holder the ticket sweep can wait a tick. The two are separate functions
    # rather than one because their preconditions differ — the reaper is guarded on a beacon
    # EXISTING, which is precisely the guard that made it unable to see the wedge.
    # A DOCS BEACON in this worktree holds the claim back too (TOOL-aPairedSlots-15); its holder's
    # death is noticed here, since only a doc-only bar's own path sweeps docs beacons.
    case "$TS_SAME" in "$TS_DOCS_ROOT"/*) scan_dead_docs_beacons ;; esac
    { ts_try_reap || ts_sweep_queue; } && continue
    TS_WAITED=$(( EPOCHSECONDS - ts_start ))
    # THE WAIT BEATS (TOOL-dDerivedDocket-64). Nothing else a waiter writes moves while it waits:
    # the ticket is created once, the status file below is rewritten only when the position changes,
    # and a gate log lands only when a leg finishes, which no waiter reaches. An out-of-process
    # liveness reader dating a worktree by its newest write therefore read a healthy queued bar as
    # silent, and a resumer acting on that verdict killed it. This write, on every tick that neither
    # acquires nor makes reap or sweep progress, is the move such a reader sees: a file under THIS
    # worktree's git dir, beside `gate-logs/`, read by its mtime and never parsed. It sits above the
    # bound test so the tick that fails open still beats. It is NEVER REMOVED — not at the acquire,
    # not by a trap: a removal would drop the newest move just before the first leg lands, and a
    # leftover ages out by its mtime exactly as an old gate log does. No spawn: `printf` and the
    # redirect are builtins, and `TS_WAITED` is already computed.
    [ -n "$gd" ] && printf 'waited\t%s\n' "$TS_WAITED" > "$gd/gate-queue-heartbeat" 2>/dev/null || true
    if [ "$TS_WAITED" -ge "$TS_MAXWAIT" ]; then
      # FAILS OPEN, LOUDLY. A turnstile that can wedge a bar is worse than two bars: the run drops
      # its ticket and proceeds unqueued rather than becoming the outage. It contributes nothing to
      # the exit code, ever.
      echo "run-gates: turnstile WAIT EXPIRED after ${TS_WAITED}s (bound ${TS_MAXWAIT}s) — running UNQUEUED alongside whatever holds the beacon" >&2
      add_health_event "$RG_HEALTH_LOG" run-gates turnstile-expired "waited ${TS_WAITED}s bound ${TS_MAXWAIT}s"
      ts_drop_ticket
      break
    fi
    pos=$(ls -1 "$TS_Q" 2>/dev/null | LC_ALL=C sort | grep -n "^$(basename "${TS_TICKET:-none}")$" | cut -d: -f1)
    [ -n "$pos" ] || pos="?"
    if [ "$pos" != "$ts_lastpos" ] || [ "$ts_announced" = 0 ]; then
      # SAY WHICH OF THE TWO IS TRUE. This line used to claim a holder unconditionally, because it is
      # emitted from the FAILURE of the acquire predicate — which conflates "someone is ahead of me
      # in the queue" with "someone holds the beacon". In the reproduction that wedge was diagnosed
      # from, nothing held the beacon at all and this line still named one, sending the reader to
      # hunt a holder that did not exist. The `queued at position N (waited Ns)` tail is byte-stable
      # because `run-gates.turnstile.test.sh` greps it; only the leading clause varies.
      # The holder is NAMED from its beacon (TOOL-aFrugalTurnstile-5 S4): on a host key it may be
      # another repository, and "someone holds this" sent the reader to search every one of them.
      # ABOVE ONE SLOT the leading clause counts the held slots and names every holder
      # (TOOL-aPairedSlots-2 S6); the tail is the same bytes at every count.
      if [ "$TS_SLOTS" -gt 1 ]; then
        measure_held_slots; ts_names=""
        for _ts_d in "${TS_SLOT_DIRS[@]}"; do
          [ -d "$_ts_d" ] || continue
          ts_hr=""; { IFS= read -r ts_hr < "$_ts_d/run"; } 2>/dev/null
          ts_hd=""; { IFS= read -r ts_hd < "$_ts_d/repo"; } 2>/dev/null
          ts_hp=""; { IFS= read -r ts_hp < "$_ts_d/pid"; } 2>/dev/null
          ts_names="$ts_names${ts_names:+; }${ts_hd:--} run ${ts_hr:--} pid ${ts_hp:--}"
        done
        unset _ts_d
        if [ "$TS_HELD_N" -ge "$TS_SLOTS" ]; then
          echo "run-gates: $TS_HELD_N of $TS_SLOTS bar slots on this host are held — $ts_names — queued at position $pos (waited ${TS_WAITED}s)" >&2
        elif ! check_worktree_unheld; then
          echo "run-gates: $TS_HELD_N of $TS_SLOTS bar slots on this host are held, and this worktree's bar holds $(render_same_holder) — queued at position $pos (waited ${TS_WAITED}s)" >&2
        else
          echo "run-gates: $TS_HELD_N of $TS_SLOTS bar slots on this host are held, and a ticket sorts ahead of this one — queued at position $pos (waited ${TS_WAITED}s)" >&2
        fi
      elif [ -d "$TS_DIR_C" ]; then
        ts_hr=""; { IFS= read -r ts_hr < "$TS_DIR_C/run"; } 2>/dev/null
        ts_hd=""; { IFS= read -r ts_hd < "$TS_DIR_C/repo"; } 2>/dev/null
        ts_hp=""; { IFS= read -r ts_hp < "$TS_DIR_C/pid"; } 2>/dev/null
        echo "run-gates: another bar holds this host — ${ts_hd:--} run ${ts_hr:--} pid ${ts_hp:--} — queued at position $pos (waited ${TS_WAITED}s)" >&2
      elif ! check_worktree_unheld; then
        echo "run-gates: no bar holds this host's first slot, but this worktree's bar holds $(render_same_holder) — queued at position $pos (waited ${TS_WAITED}s)" >&2
      else
        echo "run-gates: no bar holds this host, but a ticket sorts ahead of this one — queued at position $pos (waited ${TS_WAITED}s)" >&2
      fi
      [ -n "$gd" ] && printf 'position\t%s\nwaited\t%s\n' "$pos" "$TS_WAITED" > "$gd/gate-queue-status" 2>/dev/null || true
      ts_lastpos=$pos; ts_announced=1
    fi
    sleep "$TS_TICK"
  done
  ts_drop_ticket
  [ -n "$gd" ] && rm -f "$gd/gate-queue-status" 2>/dev/null || true
  # A LINEAGE MARKER, comma-joined and exported on every path out of the queue. It is NOT the nesting
  # test: that is `GATE_TURNSTILE_HOLDER` compared with the live beacon, exported only on a hold.
  export GATE_TURNSTILE_HELD="${GATE_TURNSTILE_HELD:-}${GATE_TURNSTILE_HELD:+,}$TS_NONCE"
fi

# THE QUEUE FACTS, resolved ONCE here and emitted at three sites — the same shape as `PROF_LINE`,
# which is built once and echoed to stdout, to `gate-last-summary.txt` and to the RED-only durable
# copy. `PROF_LINE` cannot absorb the wait: it is echoed BEFORE this block, and folding the wait
# into it would delay the profile line by the entire queue wait.
#
# THE VALUE IS A DASH WHEN IT IS UNMEASURABLE, which is this file's own idiom for an input it could
# not measure (see `input_key`). A `0` recorded for a run whose turnstile was DISABLED is a
# reassuring number about a probe that never ran, and this repo's rule is that such a probe says so.
#
# `queued_from` earns its place on a TWO-way ambiguity, not a three-way one. With `-` emitted for
# `off` and `unresolved`, a `queued 0` can only mean held-and-uncontended — an `expired` run has
# burned at least `TS_MAXWAIT`, which is `TS_TTL * 4` and therefore never 0. What the second key
# carries that a bare integer cannot is the `held`/`expired` split, and the `off`/`unresolved` one.
#
# `unticketed` (TOOL-aReapedTicket-2) is a FOURTH measurable state and it is why the sentence above
# now needs this one beside it. A run whose ticket write failed cannot ever acquire, so it fails open
# on the first tick and its wait IS 0 — which would otherwise have been recorded as `expired` and
# broken the "an expired run is never 0" invariant that paragraph leans on. Splitting the state word
# keeps the invariant true as written rather than quietly falsifying it: `expired` still means the
# bound was burned, and a `queued 0` is still unambiguous once the state word is read with it.
#
# `nested` (TOOL-aFrugalTurnstile-5) is a run inside the bar that holds the host: it took no ticket
# and waited nothing, so its `queued 0` is exact rather than a held run's uncontended zero.
#
# WHAT THIS DOES NOT CHECK, stated here because a reader will assume otherwise: `unresolved` is
# UNARMED. Reaching it needs the host directory AND `git rev-parse --git-common-dir` to fail while
# the runner is already past its own repo guard, and breaking a linked worktree's `commondir` makes
# `--show-toplevel` fail too, so the runner exits 2 before this line. No fixture in the turnstile
# suite can produce it.
QUEUED="-"; QUEUED_FROM=off
if [ "${GATE_TURNSTILE:-1}" != 0 ]; then
  if   [ -z "$TS_DIR_C" ]; then QUEUED_FROM=unresolved
  elif [ "$TS_NESTED" = 1 ]; then QUEUED=0; QUEUED_FROM=nested
  elif [ "$TS_DOCS" = 1 ]; then QUEUED=0; QUEUED_FROM=docs
  elif [ "$TS_HELD" = 1 ];  then QUEUED="$TS_WAITED"; QUEUED_FROM=held
  elif [ "$TS_UNTICKETED" = 1 ]; then QUEUED="$TS_WAITED"; QUEUED_FROM=unticketed
  else                            QUEUED="$TS_WAITED"; QUEUED_FROM=expired
  fi
fi
QUEUE_SUMMARY="gate queue: queued $QUEUED from $QUEUED_FROM"

# ONE PARSEABLE LINE, always, zero when uncontended. A wrapper that brackets a wall clock around this
# runner — `profile_bar.py` is exactly one — cannot otherwise tell waiting from working, and a queue
# wait folded into a measured wall clock can push a packing ratio below 1.0, which that tool correctly
# refuses as arithmetically impossible. This unit ships the line; who consumes it is a separate
# question.
#
# ITS BYTES ARE PINNED by two consumers — `profile_bar.py`'s `$`-anchored regex and
# `run-gates.turnstile.test.sh` — so the state word above is NOT appended here. It goes to the
# header and the summary file, which is why `QUEUE_SUMMARY` is a separate string.
echo "gate queue: waited ${TS_WAITED}s"
# THE ACQUIRE LINE (TOOL-dDerivedDocket-26 S4): the instant this bar stopped waiting and started
# working, with the state word the header records beside it. The queue-status file above is deleted
# before a bar can be killed, so a caller holding a bar that died needs something durable to say
# whether it ever acquired: this line, and the `acquired` header key written from the same two
# variables. It is a line of its own so the wait line's pinned bytes do not move, and it matches no
# verdict prefix, so no wrapper counts it as a leg.
ACQUIRED=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "gate queue: acquired $ACQUIRED from $QUEUED_FROM"

# `--hold` RUNS ITS COMMAND HERE and exits, before the scratch dir, so only the turnstile's own traps
# are armed around it (TOOL-aFrugalTurnstile-5 S6). No run record, ledger row or stamp is written:
# the held command is some other bar, and its verdict is its exit status, passed through.
if [ "${#TS_HOLD[@]}" -gt 0 ]; then
  "${TS_HOLD[@]}"; ts_rc=$?
  ts_tick_stop; ts_release; ts_drop_ticket
  exit "$ts_rc"
fi

# ---- THE SHARED DISPATCH WIDTH (TOOL-aPairedSlots-3) ----------------------------------------------
# Read ONCE, right after the acquire, by a run that HOLDS a slot at a count above one: the held count
# is the slot paths that exist, this run's own included. At two or more held, `TS_SHARE_RULE` decides
# the width, `GATE_JOBS` is the operator's width and is never divided, and one `gate profile:` line
# names the width that dispatches; the first profile line was printed before the queue on purpose, so
# this is a second line rather than a rewrite of the first. A nested, expired, unticketed or
# disabled run holds no slot and reads nothing. The width is not re-read when a neighbour arrives or
# leaves: the A/B measured a fixed width per bar.
if [ "${TS_SLOTS:-1}" -gt 1 ] && [ "$TS_HELD" = 1 ]; then
  measure_held_slots
  if [ "$TS_HELD_N" -ge 2 ]; then
    if [ -z "${GATE_JOBS:-}" ] && [ "$TS_SHARE_RULE" = half ]; then
      JOBS=$(( JOBS / TS_HELD_N )); [ "$JOBS" -ge 1 ] || JOBS=1
    fi
    echo "gate profile: width $JOBS at dispatch — $TS_HELD_N of $TS_SLOTS bar slots held ($TS_SHARE_RULE)"
    render_prof_line
  fi
fi

# ---- the scratch dir: OWNED, REDIRECTED and SWEPT (TOOL-dDerivedDocket-25) -----------------------
# Every hermetic leg makes its own `mktemp -d` scratch, and before this unit every one of them landed
# in the AMBIENT `TMPDIR` and none was ever swept: node `a` measured 30733 entries there, and a bar
# killed by signal 9 left its whole scratch dir besides, since no trap runs on SIGKILL. Three moves:
#
#   OWNED     `WORK` is a NAMED `gate-work.*` dir under the ambient `TMPDIR`, captured here before
#             anything redirects it — `/tmp` when unset or empty, which is where `mktemp -d` itself
#             falls back. Its `owner` file holds this pid, the resolved git common dir and the start
#             epoch, written tmp-then-`mv` the way the run record is, so no sweeper reads half a line.
#   SWEPT     each bar removes every `gate-work.*` whose owner names THIS common dir and whose pid
#             fails `ts_alive`, with the predicate of `ts_sweep_queue`: a live pid only WITHHOLDS the
#             sweep, so a pid table that errs can only keep a dir, never remove a live bar's. A dir
#             with no readable owner is never touched, which is also why a bar that predates this
#             unit, or another repository's, is left alone (the spec's F1 kept the delete surface to
#             this repository). The owner record is removed LAST, so a sweep that fails part-way
#             leaves a dir the next bar can still prove dead and retry.
#   REDIRECTED  `TMPDIR` is exported as `$WORK/tmp` before the first leg dispatches, so every leg's
#             `mktemp -d` and every Python `tempfile` lands inside the scratch the `cleanup` trap
#             already removes. The spelling is the one `mktemp -d` returned and never a drive-letter
#             rewrite, which is what broke four arms of the template-size self-test when an external
#             root was tried (measured by the aTetheredScratch build).
#
# It runs HERE, after the turnstile, so a bar still queued never sweeps. Every refusal in this block
# sits ABOVE the `cleanup` trap, the same class as the `mktemp -d` beside it, so each removes what it
# made before it exits.
GATE_AMBIENT_TMP=${TMPDIR:-/tmp}
WORK=$(mktemp -d "$GATE_AMBIENT_TMP/gate-work.XXXXXXXX") || { echo "run-gates: cannot create a scratch dir"; exit 2; }
# THE COMMON DIR THE OWNER NAMES, the one resolution the turnstile's key also takes, made above the
# width whether or not the turnstile runs, because the sweep must still know which repository a
# scratch dir belongs to (TOOL-aSparedSpawn-2 moved it there).
WORK_COMMON=$RG_COMMON
[ -n "$RG_HEALTH_LOG" ] || [ -z "$WORK_COMMON" ] || RG_HEALTH_LOG=$(derive_health_log "$WORK_COMMON")

write_work_owner() { # -> $WORK/owner, one line: pid TAB common dir TAB start epoch; rc 1 when unwritten
  local _tp
  derive_temp_path _tp "$WORK/owner"
  printf '%s\t%s\t%s\n' "$$" "$WORK_COMMON" "$EPOCHSECONDS" > "$_tp" 2>/dev/null \
    && mv -f "$_tp" "$WORK/owner" 2>/dev/null
}

scan_dead_work() { # -> removes each gate-work dir under the ambient TMPDIR that this repo's dead bar owns
  local d own pid rest common f
  local -a doomed
  # No common dir, no proof of ownership: sweep nothing rather than match an empty field.
  [ -n "$WORK_COMMON" ] || return 0
  for d in "$GATE_AMBIENT_TMP"/gate-work.*; do
    [ -d "$d" ] || continue
    # NEVER OUR OWN, guarded explicitly although our live pid already withholds it — the same belt
    # `ts_sweep_queue` wears, for the same reason: a later edit to the pid test must not reach here.
    [ "${d##*/}" = "${WORK##*/}" ] && continue
    own=""
    { IFS= read -r own < "$d/owner"; } 2>/dev/null
    own=${own%$'\r'}
    [ -n "$own" ] || continue
    pid=${own%%$'\t'*}; rest=${own#*$'\t'}; common=${rest%%$'\t'*}
    case "$pid" in ''|*[!0-9]*) continue ;; esac
    [ "$common" = "$WORK_COMMON" ] || continue
    ts_alive "$pid" && continue
    printf 'run-gates: sweeping the scratch of a dead bar (pid %s)\n' "$pid" >&2
    doomed=()
    for f in "$d"/* "$d"/.[!.]*; do
      [ -e "$f" ] || [ -L "$f" ] || continue
      [ "${f##*/}" = owner ] && continue
      doomed+=("$f")
    done
    if { [ "${#doomed[@]}" = 0 ] || rm -rf "${doomed[@]}" 2>/dev/null; } && rm -rf "$d" 2>/dev/null; then
      add_health_event "$RG_HEALTH_LOG" run-gates scratch-swept "dead bar pid $pid"
    else
      printf 'run-gates: NOTE - the scratch of dead bar %s was not removed whole; its owner record stays, so the next bar retries: %s\n' "$pid" "$d" >&2
    fi
  done
  return 0
}

write_work_owner \
  || echo "run-gates: NOTE - no owner record could be written into $WORK, so if this bar is killed no later bar can prove it dead and sweep its scratch" >&2
mkdir "$WORK/tmp" 2>/dev/null \
  || { rm -rf "$WORK" 2>/dev/null; echo "run-gates: cannot create the legs' scratch dir under $WORK"; exit 2; }
scan_dead_work
# THE AMBIENT COUNT, ONCE PER BAR, measured after the sweep and counting this bar's own dir, so two
# bars over an unchanged ambient print the same figure and a leak reads as growth. A glob rather than
# `ls | wc -l`: no process, and no per-entry stat on a directory that may hold tens of thousands.
_te_ng=0; shopt -q nullglob && _te_ng=1
_te_dg=0; shopt -q dotglob && _te_dg=1
shopt -s nullglob dotglob
_te_all=("$GATE_AMBIENT_TMP"/*)
[ "$_te_ng" = 1 ] || shopt -u nullglob
[ "$_te_dg" = 1 ] || shopt -u dotglob
TMPDIR_ENTRIES=${#_te_all[@]}
unset _te_all _te_ng _te_dg
echo "TMPDIR entries $TMPDIR_ENTRIES"
export TMPDIR="$WORK/tmp"
# THE TRAP COVERS THE SCRATCH DIR AND THE BEACON, AND NOTHING ELSE. That exclusion is load-bearing:
# the run record below lives under the git dir and is DURABLE, so a trap that swept it would erase
# the record on every ordinary exit and on every caught signal — which is every path except the
# crash the record exists to make readable.
#
# WIDENED past EXIT because a bar is routinely interrupted, and a beacon that only releases on a
# clean exit turns every Ctrl-C into a repository that queues behind a run nobody is doing until
# the TTL expires. The signal arms re-exit with the conventional 128+n so the caller still sees
# what killed it. `cleanup` is idempotent: EXIT fires after them and must not undo a release.
# SUPERSEDES the claim-time trap above with the same release plus the scratch dir. `trap` replaces
# rather than appends, which is what makes this safe: there is never a moment with no handler, and
# never two handlers racing to remove the same directory.
# THE REAP COMES FIRST, and the order is the correctness of it: removing the scratch dir while
# the legs are still alive is what turns a live leg into a process writing to a deleted path, which
# is how the survivors in the opening sweep came to be doing nothing against directories that no
# longer existed. The release runs afterwards unconditionally.
# The teardown/wall reaper. Delegates when the monitor is usable and ALWAYS also runs the
# runner's own `remove_descendants`: two verifications by two mechanisms is not duplication here,
# it is the guard not sharing a variable with the thing it guards. Its walked/killed figures are
# the monitor's own and are printed as SEPARATE numbers -- summing them hides a walk that found
# nothing.
run_leg_reap() {
  _rlt_pid="$1"
  [ -n "$_rlt_pid" ] || return 0
  if [ "${PROCMON_OK:-0}" = 1 ]; then
    # Bounded where `timeout -k` actually runs, unbounded where the runner already established
    # it does not -- the same CEILINGS_LIVE gate every other ceiling in this file respects,
    # rather than a second opinion about the host.
    if [ "${CEILINGS_LIVE:-0}" = 1 ]; then
      _rlt_out=$(PROCMON_ROOT="$ROOT" timeout -k 5s 60 "$PYBIN" "$PROCMON_REAP" \
                   --kill-msys "$_rlt_pid" 2>&1) || true
    else
      _rlt_out=$(PROCMON_ROOT="$ROOT" "$PYBIN" "$PROCMON_REAP" --kill-msys "$_rlt_pid" 2>&1) || true
    fi
    printf '%s\n' "$_rlt_out" | sed 's/^/run-gates: /' >&2
  fi
  remove_descendants "$_rlt_pid"
}

# Every outstanding leg's tree, BOUNDED as a whole. The bound is what keeps this from becoming a
# new way to wedge the fleet: `ts_release` and `ts_drop_ticket` run after it whatever it did, so a
# hung monitor cannot strand a turnstile ticket and queue every later bar on this host behind it.
GATE_REAP_BOUND=${GATE_REAP_BOUND:-120}
run_outstanding_reap() {
  [ -n "${WORK:-}" ] && [ -d "${WORK:-}" ] || return 0
  _rol_deadline=$(( EPOCHSECONDS + GATE_REAP_BOUND ))
  for _rol_f in "$WORK"/*.pid; do
    [ -e "$_rol_f" ] || continue
    if [ "$EPOCHSECONDS" -ge "$_rol_deadline" ]; then
      echo "run-gates: teardown reap hit its ${GATE_REAP_BOUND}s bound; the remaining legs were not walked" >&2
      break
    fi
    _rol_i=${_rol_f##*/}; _rol_i=${_rol_i%.pid}
    [ -f "$WORK/$_rol_i.rc" ] && continue
    _rol_p=$(cat "$_rol_f" 2>/dev/null) || continue
    [ -n "$_rol_p" ] && run_leg_reap "$_rol_p"
  done
  return 0
}

# ---- the run log (TOOL-dLoggedFlight-3) ------------------------------------------------------------
# ONE LINE PER BAR, appended to `gates.log` under `runlog/` in the git COMMON dir, in the runlog kit's
# grammar, from the one seam every exit below this point passes through: `cleanup`, the EXIT trap. The
# common dir is shared by the primary tree and every linked worktree of a clone, so every bar a clone
# runs lands in one file. The grammar is stated in that kit's README; this block writes it and reads
# none of it.
#
# READ BACK, NEVER RECOMPUTED. The run id, the header's worktree, head, start time and full flag, the
# verdict file's counts and the failing legs' names from their `.leg` rows are all read from the run
# record below, so the line cannot disagree with the record it summarises. A run killed before its
# verdict has no verdict file, so its line says `verdict=NONE` and carries the signal's status; a
# refusal before the header says `stage=pre-header` with the header's keys empty.
#
# EVIDENCE, NEVER AN INPUT. Nothing in this runner or any gate branches on a line. A failed append
# prints ONE `run-gates: run log` line on stderr and changes neither the exit code nor stdout, and
# `GOV_RUNLOG=0` in the environment writes nothing.
#
# ONCE PER PROCESS, and the guard is load-bearing. Each signal trap below runs `cleanup` and then
# `exit`s, and that exit fires the EXIT trap, which runs `cleanup` again: the handler runs TWICE on
# every caught signal, which is the gotcha class `signal-trap-runs-the-exit-handler-twice`. The first
# entry takes the signal's status from `RUNLOG_RC`, because its own `$?` is 128+n only when the signal
# interrupted `wait -n`: a signal held behind a foreground command, a `$(fingerprint)` say, runs its
# trap when that command ends and arrives with the command's status. The second entry appends
# nothing. `cleanup`'s existing work is unchanged and still runs on both entries.
#
# ZERO SPAWNS: builtin reads, a glob, parameter expansion and one `printf >>`. The first bar a clone
# ever runs pays one `mkdir` for the journal directory, and a clone that has one pays nothing.
#
# WHAT THIS DOES NOT CATCH. An exit above the EXIT trap: not a repo, no python, a refused profile,
# `--print-profile`, the turnstile queue, the scratch-dir `mktemp` and its legs' `tmp` subdir. A
# SIGKILL, which runs no trap.
# A leg reported `(no result)`, which is counted in `failed` but has no `.leg` row and so no name on
# the line. And an unset name read inside the handler, which `set -u` would turn into a handler that
# writes nothing: every read here is defaulted for that reason, and a new read must be too.
RUNLOG_MAX_BYTES=2048   # the grammar's line cap, LF not counted
RUNLOG_FAIL_CAP=20      # fail.1 .. fail.20; the rest are counted into fail_more
RUNLOG_RC=""; RUNLOG_DONE=""

# `<key>TAB<value>` per line, the header's and the verdict's grammar, into `<prefix><key>` for each key
# the caller names and for nothing else, so a line the runner did not expect cannot set a variable.
# The caller declares the variables it names, as locals, before calling. Rc 1 when the file is absent.
read_record_keys() { # file · variable prefix · key... -> sets <prefix><key> for each named key present
  local _rk_f=$1 _rk_p=$2 _rk_k="" _rk_v="" _rk_want
  shift 2
  _rk_want=" $* "
  [ -f "$_rk_f" ] || return 1
  while IFS=$'\t' read -r _rk_k _rk_v || [ -n "$_rk_k" ]; do
    case "$_rk_want" in *" $_rk_k "*) printf -v "$_rk_p$_rk_k" '%s' "${_rk_v%$'\r'}" ;; esac
    _rk_k=""; _rk_v=""
  done 2>/dev/null < "$_rk_f"
  return 0
}

# THE ONE APPEND, in the grammar's own bytes. Each value is escaped backslash FIRST, then TAB, LF and CR,
# so the first pass cannot re-escape the others. A line over the cap is fitted by the runlog kit's
# REFERENCE rule, and its suite compares the result with that kit's `render_line`: drop whole indexed
# fields, highest index first, counting each into `fail_more`; only when none is left, cut the longest
# value outside `v n t p ev` and the `_more` counts from its end, never inside a UTF-8 character and
# never inside an escape, and measure again. `LC_ALL=C` for this function alone, so `${#v}` counts
# BYTES, which is what the cap counts.
write_runlog_verdict() { # the status the EXIT trap saw -> one ev=once line appended to the gates journal
  [ -z "${RUNLOG_DONE:-}" ] || return 0
  RUNLOG_DONE=1
  [ "${GOV_RUNLOG:-}" != 0 ] || return 0
  local LC_ALL=C bs='\' tab=$'\t' rc="${RUNLOG_RC:-${1:-}}" t="" g="" c="" dir="" line="" stage=""
  local i f nm st n=0 more=0 size=0 best blen top cut b need
  local rh_worktree="" rh_head="" rh_started="" rh_full=""
  local rv_verdict=NONE rv_ran="" rv_failed="" rv_skipped="" rv_held="" rv_reused="" rv_wall_breach=""
  local -a key=() val=() fails=()
  if [ -n "${EPOCHREALTIME:-}" ]; then t=${EPOCHREALTIME/,/.}; else printf -v t '%(%s)T' -1; fi
  # The COMMON dir from the git dir this runner already resolved, with no `git` process. A linked
  # worktree's git dir holds a `commondir` file naming the common dir relative to itself, and its `..`
  # segments are folded so a path this prints is the one git would print; the primary tree has no such
  # file and its git dir IS the common dir. Never `.git/worktrees/<name>/runlog`, which would split
  # one clone's journal in two.
  g=${GD:-}
  if [ -n "$g" ]; then
    case "$g" in /*|[A-Za-z]:[/\\]*) ;; *) g="${ROOT:-.}/$g" ;; esac
    if [ -f "$g/commondir" ]; then
      { IFS= read -r c < "$g/commondir"; } 2>/dev/null || [ -n "$c" ] || c=""
      c=${c%$'\r'}
      case "$c" in
        "") ;;
        /*|[A-Za-z]:[/\\]*) dir="$c/runlog" ;;
        *) while :; do
             case "$c" in
               ..)   g=${g%/*}; c=""; break ;;
               ../*) g=${g%/*}; c=${c#../} ;;
               *)    break ;;
             esac
           done
           dir="$g${c:+/$c}/runlog" ;;
      esac
    else
      dir="$g/runlog"
    fi
  fi
  if [ -n "${RUNDIR:-}" ]; then
    read_record_keys "$RUNDIR/header" rh_ worktree head started full || stage=pre-header
    read_record_keys "$RUNDIR/verdict" rv_ verdict ran failed skipped held reused wall_breach
    # Indexed by the leg's MANIFEST position, which names its file, so the array walks in manifest
    # order whatever order the glob returned.
    for f in "$RUNDIR"/*.leg; do
      [ -f "$f" ] || continue
      i=${f##*/}; i=${i%.leg}
      case "$i" in ""|*[!0-9]*) continue ;; esac
      nm=""; st=""
      { IFS=$'\t' read -r nm st _ < "$f"; } 2>/dev/null || [ -n "$nm" ] || continue
      # A RETRIED leg ended on its retry (TOOL-dDerivedDocket-26 S2): the first attempt's row reads
      # `timeout` and stays as written, and the `<i>.retry.leg` beside it says how the leg ended. A
      # `timeout` with no retry row is a leg the wall cut before its retry, and it did not pass.
      [ -f "$RUNDIR/$i.retry.leg" ] && { IFS=$'\t' read -r _ st _ < "$RUNDIR/$i.retry.leg"; } 2>/dev/null
      case "$st" in fail|timeout) fails[10#$i]=$nm ;; esac
    done
  else
    stage=pre-header
  fi
  key=(v t p ev run wt head started full selftests verdict stage ran failed skipped held reused
       wall_breach rc)
  val=(1 "$t" gates once "${RUNID:-}" "$rh_worktree" "$rh_head" "$rh_started" "$rh_full"
       "$SELFTESTS_STAMP" "$rv_verdict" "$stage" "$rv_ran" "$rv_failed" "$rv_skipped" "$rv_held"
       "$rv_reused" "$rv_wall_breach" "$rc")
  for i in ${fails[@]+"${!fails[@]}"}; do
    if [ "$n" -lt "$RUNLOG_FAIL_CAP" ]; then n=$((n + 1)); key+=("fail.$n"); val+=("${fails[i]}")
    else more=$((more + 1)); fi
  done
  [ "$more" -gt 0 ] && { key+=(fail_more); val+=("$more"); }
  key+=(kit); val+=("${KIT_RUN_GATES_VERSION:-}")
  for i in "${!val[@]}"; do
    f=${val[i]//"$bs"/"$bs$bs"}; f=${f//$'\t'/'\t'}; f=${f//$'\n'/'\n'}; f=${f//$'\r'/'\r'}
    val[i]=$f
    size=$(( size + ${#key[i]} + ${#f} + 2 ))
  done
  size=$(( size - 1 ))
  # STEP ONE: whole indexed fields, the highest index first, a tie going to the later field.
  while [ "$size" -gt "$RUNLOG_MAX_BYTES" ]; do
    best=-1; top=-1
    for i in "${!key[@]}"; do
      case "${key[i]}" in
        *.*) nm=${key[i]#*.}
             case "$nm" in ""|*[!0-9]*) ;; *) [ "$((10#$nm))" -ge "$top" ] && { best=$i; top=$((10#$nm)); } ;; esac ;;
      esac
    done
    [ "$best" -ge 0 ] || break
    nm="${key[best]%%.*}_more"
    size=$(( size - ${#key[best]} - ${#val[best]} - 2 ))
    key=("${key[@]:0:best}" "${key[@]:best+1}"); val=("${val[@]:0:best}" "${val[@]:best+1}")
    f=-1
    for i in "${!key[@]}"; do [ "${key[i]}" = "$nm" ] && { f=$i; break; }; done
    if [ "$f" -ge 0 ]; then
      size=$(( size - ${#val[f]} )); val[f]=$(( ${val[f]} + 1 )); size=$(( size + ${#val[f]} ))
    else
      key+=("$nm"); val+=(1); size=$(( size + ${#nm} + 3 ))
    fi
  done
  # STEP TWO: cut the longest value outside the protected keys, the first of equals, from its end.
  while [ "$size" -gt "$RUNLOG_MAX_BYTES" ]; do
    best=-1; blen=0
    for i in "${!key[@]}"; do
      case "${key[i]}" in v|n|t|p|ev|*_more) continue ;; esac
      [ "${#val[i]}" -gt "$blen" ] && { best=$i; blen=${#val[i]}; }
    done
    [ "$best" -ge 0 ] || break
    b=$(( blen - (size - RUNLOG_MAX_BYTES) )); [ "$b" -gt 0 ] || b=0
    cut=${val[best]:0:b}
    # A character cut in half is dropped whole, as the reference's decode drops it: count the
    # continuation bytes that end the value, then ask the lead byte before them how many it needed.
    b=0
    while [ "$b" -lt "${#cut}" ] && [ "$b" -lt 3 ]; do
      case "${cut:$(( ${#cut} - b - 1 )):1}" in [$'\x80'-$'\xbf']) b=$((b + 1)) ;; *) break ;; esac
    done
    if [ "$b" -lt "${#cut}" ]; then
      case "${cut:$(( ${#cut} - b - 1 )):1}" in
        [$'\xc0'-$'\xdf']) need=1 ;;
        [$'\xe0'-$'\xef']) need=2 ;;
        [$'\xf0'-$'\xf7']) need=3 ;;
        *)                 need=0 ;;
      esac
      [ "$b" -lt "$need" ] && cut=${cut:0:$(( ${#cut} - b - 1 ))}
    fi
    # ...and an escape cut in half leaves an ODD run of trailing backslashes: drop one.
    b=0
    while [ "$b" -lt "${#cut}" ] && [ "${cut:$(( ${#cut} - b - 1 )):1}" = "$bs" ]; do b=$((b + 1)); done
    [ $(( b % 2 )) -eq 1 ] && cut=${cut%?}
    size=$(( size - blen + ${#cut} )); val[best]=$cut
  done
  for i in "${!key[@]}"; do line+="${line:+$tab}${key[i]}=${val[i]}"; done
  [ -n "$dir" ] && [ ! -d "$dir" ] && mkdir "$dir" 2>/dev/null
  # THROUGH `cat`, ONE WRITE PER LINE (TOOL-aPairedSlots-7): two bars of one repository append here at
  # once. Measured on node a, three concurrent writers of 2000-byte lines through the `printf` builtin's
  # own redirection tore 146 of 3200, and of 12000-byte lines 308 of 900, while the same lines piped
  # through `cat` tore none at either size. A line grows with its failing legs' names. One spawn a bar.
  [ -n "$dir" ] && { printf '%s\n' "$line" | cat >> "$dir/gates.log"; } 2>/dev/null && return 0
  printf 'run-gates: run log — cannot append to %s, so this bar is not recorded there; its verdict, its output and its exit code are unaffected\n' \
    "${dir:-(no git dir resolved)}/gates.log" >&2
  return 0
}

# THE ATTRIBUTION WORKTREE goes on every exit path too, AFTER the reap (its R run may be what is
# being reaped) and before the scratch dir. ATTR_WT is set only once lib-attribute.sh is sourced.
# FORGOTTEN ONCE REMOVED, because `cleanup` runs twice on every caught signal (the arm below, then
# the EXIT trap its `exit` fires): the second removal of a worktree already gone fails, and printed
# an orphan line naming a path that no longer exists (the dDerivedDocket closing diff review's F5,
# the sibling runner's instance of the same class).
ATTR_WT=""
# THE TICKER AND THE CENSUS SAMPLER STOP HERE TOO (TOOL-aGraftedHelix-5). The claim-time handlers this
# trap supersedes each run `ts_tick_stop` before the release, and this one kept only the release, so
# every bar left its ticker sleeping for up to TS_TICK_EVERY, reparented to pid 1 with this runner's
# argv, and the next bar's foreign-load census on the host counted it as somebody else's gate work.
cleanup() { write_runlog_verdict "$?"; run_outstanding_reap; remove_census_watcher; if [ -n "${ATTR_WT:-}" ]; then if remove_scratch_worktree "$ATTR_WT"; then ATTR_WT=""; else echo "run-gates: the R worktree at $ATTR_WT could not be removed — remove it by hand" >&2; fi; fi; rm -rf "$WORK" 2>/dev/null || true; ts_tick_stop; ts_release; ts_drop_ticket; }
trap cleanup EXIT
trap 'RUNLOG_RC=130; cleanup; exit 130' INT
trap 'RUNLOG_RC=143; cleanup; exit 143' TERM
trap 'RUNLOG_RC=129; cleanup; exit 129' HUP

# ---- the run record (the run-record unit) --------------------------------------------------------
# The runner used to forget everything on exit: the per-leg results lived in $WORK, which the trap
# above deletes, and the three files that survived were prose for a human. The record is a directory
# of small append-once files another session can read DURING the run and after a crash.
#
# PER-RUN, never a fixed path, and that is a correctness property rather than tidiness. The `.rc`
# file is the DISPATCH SUPPRESSOR — the loop below skips any leg that already has one — so a
# leftover at a fixed path makes the runner skip a leg and print it green. Per-run uniqueness is what
# makes that impossible; nothing is cleared at the start of a run, because a start-of-run clear can
# partially fail on this platform against an open handle or an AV lock and inherit the previous run's
# verdicts, which is the same defect wearing a different hat.
GATE_RUN_KEEP=${GATE_RUN_KEEP:-5}
# DECLARED with its reasoning, not an unnamed number. Five is enough that a crashed run's record —
# the one with a header and no verdict — survives the two or three ordinary runs an operator does
# before they come back to look at it, and small enough that a header, one row per leg and a verdict
# cannot grow the git dir without practical limit.
RUNROOT=""; RUNDIR=""; RUNID=""
# THE COMPLETION FILE STAYS IN THE SCRATCH DIR, and the durable record does not hold one. This is
# the one place this unit's spec asked for something its own reasoning argues against, and the
# arm for it is what found the disagreement rather than a reading of the text.
#
# The spec asked for the completion files to MOVE into the run directory, on the reasoning that
# the file is the DISPATCH SUPPRESSOR and not a log — the loop below skips any leg that already
# has one, so a leftover makes the runner skip a leg and print it green. That reasoning is right,
# and it is an argument for keeping the suppressor OUT of the durable record: a `mktemp -d` name
# nothing outside this process can predict cannot be planted, while a run directory has a
# NAMEABLE path, and this runner accepts a pinned id through `GATE_RUN_ID`. Moving the suppressor
# somewhere addressable re-opened the hole the move was meant to close.
#
# The two jobs the file was doing come apart cleanly: suppression is per-run and must be
# unforgeable, durability is per-leg and must survive the process. The `.leg` row below is the
# durable half and it is written before the completion signal, so the record loses nothing.
# Measured: with the suppressor in the run directory, a planted `<i>.rc` suppressed its leg and
# the run reported the plant's verdict as the leg's own.
if [ -n "$gd" ]; then
  # The id is seamed for the ARM, not for the runner: an arm that plants a stale completion file has
  # to know which directory the run will open, and without the seam the plant lands somewhere the run
  # never looks and the arm passes by finding nothing.
  # Derived ONCE, above the turnstile, which writes it into the beacon as `run` (TOOL-aFrugalTurnstile-5 S2).
  RUNID="$TS_RUN"
  RUNROOT="$gd/gate-run"
  RUNDIR="$RUNROOT/$RUNID"
  if mkdir -p "$RUNDIR" 2>/dev/null; then
    chmod 700 "$RUNDIR" 2>/dev/null || true
    RC="$RUNDIR"
    derive_temp_path _tp "$RUNROOT/current"
    printf '%s' "$RUNID" > "$_tp" 2>/dev/null && mv -f "$_tp" "$RUNROOT/current" 2>/dev/null || true
    # The memory pause's episodes, one row each, beside the `.leg` rows they explain. Emptied when a
    # pinned id reuses the directory, so a row here is always this run's (TOOL-aGraftedHelix-7).
    MEMPAUSE_ROWS="$RUNDIR/pauses"
    [ -e "$MEMPAUSE_ROWS" ] && : > "$MEMPAUSE_ROWS"
  else
    # Creating the run directory fails the run the way the `mktemp -d` it sits beside already does.
    echo "run-gates: cannot create the run record at $RUNDIR" >&2; exit 2
  fi
fi
# A PINNED ID PINS THIS RUN AND NO OTHER — TOOL-dLoggedFlight-4. The pre-push hook exports one so its
# push line joins this bar's run-log line by id, and nothing here scrubs a leg's environment: left
# set, every leg inherits it, and a leg that drives a nested runner, as this kit's own suites do in
# scratch clones, would reuse ONE run directory for every nested bar it starts. That is the per-run
# uniqueness the paragraph above calls a correctness property. Read above, removed here, before any
# leg starts.
unset GATE_RUN_ID
# THE REUSE KNOBS, read once and removed for the same reason (TOOL-aFrugalTurnstile-4 S4, composed by
# TOOL-aSparedSpawn-32 S6): the pre-push hook exports `GATE_REUSE_LINEAGE` or `GATE_REUSE_PUSH` to THIS
# bar, and a leg's nested runner inheriting either, or a hand-set `GATE_REUSE`, would reuse inside a
# scratch clone that asked for nothing. The mode block below reads these three variables and never
# the environment; the header records the one mode it decides as `reuse`. `GATE_REUSE_DIGEST_ENV`,
# the file the hook writes the caller's restored environment to beside `GATE_REUSE_PUSH`
# (TOOL-aSparedSpawn-33), is read here too, and only the `push` mode's digest reads it.
REUSE_ASK_ENV=${GATE_REUSE:-}; REUSE_ASK_PUSH=${GATE_REUSE_PUSH:-}; REUSE_ASK_LINEAGE=${GATE_REUSE_LINEAGE:-}
REUSE_ASK_DIGEST_ENV=${GATE_REUSE_DIGEST_ENV:-}
unset GATE_REUSE GATE_REUSE_PUSH GATE_REUSE_LINEAGE GATE_REUSE_DIGEST_ENV

FPRINT="$KITREL/gate-fingerprint.sh"
fingerprint() { [ -f "$FPRINT" ] || { printf ''; return; }; bash "$FPRINT" "$@" 2>/dev/null; }
FPRINT_START=$(fingerprint)
# CLEAN means `git status --porcelain` EMPTY, untracked-and-unignored files included — the same
# predicate the fingerprint's own porcelain component is computed from. The obvious `git diff
# --quiet` pair ignores untracked files, and a record written from a tree with a `??` line in it
# carries a digest whose porcelain component is non-empty, which the at-a-rev form cannot reproduce
# at any sha. The push boundary would then mismatch on every later push and force the full bar
# forever while printing that the record describes a different tree — safe, permanent, and it reads
# as caution rather than as the defect it is.
# ONE PORCELAIN WALK, read by everything that needs it. Three separate `git status --porcelain`
# calls accumulated here — one for the clean test, one for the per-leg input keys, and one inside
# the fingerprint helper — and a status walk over a real tree is the expensive part of this
# runner's startup. Measured before this fold: 2136 ms from process start to the header being on
# disk, in a scratch repo with two files. The helper keeps its own walk because it is a separate
# executable a git hook calls directly and must be self-contained; the other two are the same
# question asked twice.
#
# THE WALK CARRIES CONTENT (TOOL-aSparedSpawn-1 S1). A porcelain LINE says a file is dirty, never
# what it holds, so ` M ga/f` keyed an edit-run-edit cycle as one input and reuse handed the second
# edit a green the first one earned. Each row is now `<XY> <blob-or-dash> <path>`, the blob hashed
# HERE, at the instant `FPRINT_START` was taken, so a file edited while a leg runs cannot give the
# earning row a key for bytes that leg never read. `-z` because a quoted path names no file;
# `--untracked-files=all` because the default mode reports a new directory as `?? d/` and the files
# inside it would key by nothing. A rename row is followed by its SOURCE field, which is consumed,
# not read as a path. A deleted path, or anything that is not a regular file, carries a dash: its
# absence is already in `XY`. A path holding a newline cannot ride `--stdin-paths`, so it fails the
# walk, and a failed walk is neither clean nor keyable.
# ponytail: one hash-object over the dirty set; a huge untracked tree pays `-uall` once per bar.
DIRT_ROWS=(); WALK_OK=no
if LC_ALL=C git status --porcelain -z --untracked-files=all > "$WORK/walk" 2>/dev/null; then
  WALK_OK=yes
  _wx=(); _wp=(); _wi=(); _wf=(); _wsrc=0
  while IFS= read -r -d '' _we; do
    if [ "$_wsrc" = 1 ]; then _wsrc=0; continue; fi
    case ${_we:0:2} in *R*|*C*) _wsrc=1 ;; esac
    case $_we in *$'\n'*) WALK_OK=no ;; esac
    _wx+=("${_we:0:2}"); _wp+=("${_we:3}")
    if [ -f "${_we:3}" ]; then _wi+=("${#_wf[@]}"); _wf+=("${_we:3}"); else _wi+=(-); fi
  done < "$WORK/walk"
  _wh=()
  if [ "${#_wf[@]}" -gt 0 ]; then
    mapfile -t _wh < <(printf '%s\n' "${_wf[@]}" | git hash-object --stdin-paths 2>/dev/null)
    [ "${#_wh[@]}" = "${#_wf[@]}" ] || WALK_OK=no
  fi
  if [ "$WALK_OK" = yes ] && [ "${#_wp[@]}" -gt 0 ]; then
    _wr=()
    for ((_j=0; _j<${#_wp[@]}; _j++)); do
      _wb=-; [ "${_wi[$_j]}" = - ] || _wb=${_wh[${_wi[$_j]}]}
      _wr+=("${_wx[$_j]} $_wb ${_wp[$_j]}")
    done
    mapfile -t DIRT_ROWS < <(printf '%s\n' "${_wr[@]}" | LC_ALL=C sort)
    [ "${#DIRT_ROWS[@]}" = "${#_wr[@]}" ] || WALK_OK=no
  fi
  unset _wx _wp _wi _wf _wh _wr _wb _we _wsrc _j
fi
rm -f "$WORK/walk"
# CLEAN means this listing EMPTY, untracked-and-unignored files included — not `git diff --quiet`,
# which is blind to a `??` line and would stamp a green over a tree the at-a-rev fingerprint form
# cannot reproduce at any sha. A walk that FAILED is not an empty listing, and is never clean.
TREE_CLEAN=no
[ "$WALK_OK" = yes ] && [ "${#DIRT_ROWS[@]}" = 0 ] && TREE_CLEAN=yes

# Read the leg manifest as name<RS>guard(comma-joined)<RS>argv(joined by <US>) per line, where
# RS=\x1e and US=\x1f (non-whitespace, so an empty guard field survives `read`; a tab would collapse).
# Line 1 is the advisory DISPATCH ORDER: leg indices longest-first from the timing cache the previous
# run wrote. A leg the cache does not know scores its prior instead (TOOL-aSparedSpawn-3 S5: its
# evidenced maximum, else its scaled ceiling, else 0, and 0 sorts last), so an absent or unreadable
# cache no longer yields manifest order. It is a scheduling hint only — it can never change a verdict.
# Command-substitution surfaces a parse failure (a `< <()` process-sub would swallow it).
# THE PROGRAM OPENS WITH `RKD_PROGRAM`, the sibling-kit resolver, and where the process-monitor conf
# exists it takes three more arguments and prints ONE LEADING LINE before line 1: `0`, RS and the kit
# dir, or `1`, RS and the resolver refusal. The reader strips that line before anything below reads
# line 1, so the dispatch order and every row keep their bytes (TOOL-aSparedSpawn-4 S10).
_pm_args=()
[ "$PROCMON_CONF" = 1 ] && _pm_args=(process-monitor reap.py "$KITDIR")
legs=$("$PYBIN" -c "$RKD_PROGRAM"'
import hashlib, json, os, statistics, sys
# THE PROCESS-MONITOR KIT DIR (TOOL-aSparedSpawn-4 S10), asked by argv[5] to argv[7] and answered as the
# runner wrapper of the resolver answered it: the dir relative to the nearest directory holding .git,
# or the refusal text. A refusal never ends this program, because the manifest still has to be read.
pm = None
if len(sys.argv) > 7:
    try:
        pm_d = resolve_kit_dir(*sys.argv[5:8])
        pm_r = next((p for p in (pm_d, *pm_d.parents) if (p / ".git").exists()), pm_d.anchor)
        pm = "0\x1e" + pm_d.relative_to(pm_r).as_posix()
    except Exception as e:
        pm = "1\x1e" + " ".join(str(e).splitlines())
try:
    data = json.load(open(sys.argv[1]))
except Exception as e:
    sys.stderr.write("parse error: %s\n" % e); sys.exit(3)
# AN EMPTY LIST IS NOT A PARSE ERROR (TOOL-dDerivedDocket-26 S6). It used to exit here naming no
# verdict at all; it now reaches the refusal at the foot of the runner, which refuses exit 0 over a
# run that reported no leg line and says which half was missing. Not a list is still a parse error.
if not isinstance(data, list):
    sys.stderr.write("gate-legs.json is not a list\n"); sys.exit(3)
durs = {}
cache = sys.argv[2] if len(sys.argv) > 2 else ""   # argv[1] is the MANIFEST; the cache is argv[2]
# argv[3] is the TOOL ROOT this runner derived from its own location. A manifest names its programs
# and guards through the {prefix} token (TOOL-aRepatriatedFork-29, its spec section 8 F1), resolved
# here ONCE, so every field below and every reader of these rows sees a repo-relative path. A
# manifest carrying no token, which is what the deployer emits for an adopter, passes unchanged.
troot = sys.argv[3] if len(sys.argv) > 3 else ""
# >>> resolve_prefix_token -- canonical copy: resolve_prefix_token.py in the gov lib dir (byte-identical; gated)
def resolve_prefix_token(spelled, troot):
    """<spelled> with its {prefix} token resolved against the tool root <troot>.

    An empty or "." root is a root install: the token drops with its slash, and a bare token
    becomes ".". Any other root replaces the token. Text with no token passes unchanged.
    """
    spelled = str(spelled)
    if not troot or troot == ".":
        return spelled.replace("{prefix}/", "").replace("{prefix}", ".")
    return spelled.replace("{prefix}", troot)
# <<< resolve_prefix_token
if cache and os.path.exists(cache):
    try:
        for line in open(cache, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 2: durs[p[0]] = float(p[1])
    except Exception:
        durs = {}          # a corrupt cache is a missing cache, never a failed run
# THE PRIORS (TOOL-aSparedSpawn-3 S5), for a leg the ledger holds no seconds for, so a new worktree
# does not dispatch in manifest order: the largest reading ceiling-evidence.txt beside this runner
# records for it; else its declared ceiling divided by the MEDIAN ceiling-to-reading ratio over the
# legs carrying both, re-derived here every bar (about 17 at base 22efab65, so a typed divisor would
# be wrong), or by 1 when no leg carries both; else 0. argv[4] is that file, and an unreadable one is
# a missing prior, never a failed run. Ties keep manifest order, since the sort is stable.
evid = {}
efile = sys.argv[4] if len(sys.argv) > 4 else ""
if efile and os.path.exists(efile):
    try:
        for line in open(efile, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 2 and not line.startswith("#"):
                evid[p[0]] = max(evid.get(p[0], 0.0), float(p[1]))
    except Exception:
        evid = {}
ceils = [l["ceiling"] if isinstance(l.get("ceiling"), int) and not isinstance(l.get("ceiling"), bool)
         and l["ceiling"] > 0 else 0 for l in data]
ratios = [ceils[i] / evid[data[i]["name"]] for i in range(len(data))
          if ceils[i] and evid.get(data[i]["name"], 0.0) > 0]
scale = statistics.median(ratios) if ratios else 1.0
prior = [durs[data[i]["name"]] if data[i]["name"] in durs
         else evid[data[i]["name"]] if evid.get(data[i]["name"], 0.0) > 0
         else ceils[i] / scale for i in range(len(data))]
order = sorted(range(len(data)), key=lambda i: -prior[i])
# Line 1 also carries, behind one RS, the python half of the reuse key digest (TOOL-aSparedSpawn-1
# S4): this interpreter version and its utf8 mode, read here so the digest starts no python of its own.
# The read classes per row, the fourth field below (TOOL-aSparedSpawn-13 S1).
reads = {}
for l in data:
    r = l.get("reads")
    if "reads" in l:
        known = isinstance(r, dict) and all(k in ("history", "base", "clock", "remote") for k in r)
        reads[id(l)] = ",".join(sorted(r)) if known else "impure,remote"
    else:
        reads[id(l)] = "impure,remote" if l.get("impure") else ""
rows = [" ".join(str(i) for i in order) + "\x1e" + sys.version.replace("\n", " ")
        + " utf8_mode=" + str(sys.flags.utf8_mode)]
# The fourth field is the `reads` declaration (TOOL-aSparedSpawn-13 S1): the sorted, comma-joined
# CLASSES, never the reasons, which are for a human reading the manifest. The classes are closed:
# history, base, clock, remote. A legacy `impure` with no `reads` reads as `remote,impure`, and so
# does a class outside the four or a `reads` that is no object: `impure` in this field means "key it
# as remote and never reuse it", the meaning the key had before classes existed. Reduced to known
# words here, so no prose reason can corrupt the wire format.
# The SIXTH field is `subject`, appended AFTER chunk so the chunk position is unchanged — a field
# inserted before it would be parsed as chunk by any reader that had not moved in the same commit.
# Defaulted to `repo`: a leg that has not declared is on the bar, because the other default silently
# removes an undeclared leg from every run. NOTE: this program is inside a single-quoted shell block,
# so a comment here may carry no apostrophe. TOOL-dUnstalledConvoy-26.
#
# THE CRITERION, and it is the ONE statement of it. Ask what a FAILURE of this leg MEANS:
#
#   "the kit source is broken"          -> subject = kit   (held; the owner asks for it)
#   "this repository is misconfigured"  -> subject = repo  (on the bar, every run)
#
# Asking instead what a leg TESTS is the wording that does not decide, and it decided four legs
# wrongly before this sentence replaced it. A kit whose product is a repository configuration —
# the push and commit boundaries are the case — has a self-test that reads BOTH the kit source and
# the live hook installed here, so "what does it test" has two true answers and the failure question
# has one. Those four legs are `repo`: a broken boundary in THIS repository cannot wait for somebody
# to remember a variable. TOOL-dUnstalledConvoy-30.
rows += [l["name"] + "\x1e" + ",".join(resolve_prefix_token(g, troot) for g in l.get("guard", []))
         + "\x1e" + "\x1f".join(resolve_prefix_token(a, troot) for a in l["argv"])
         + "\x1e" + reads[id(l)]
         + "\x1e" + str(l.get("chunk", "") or "")
         + "\x1e" + (l.get("subject") or "repo")
         # THE SEVENTH FIELD, appended after `subject` for exactly the reason `subject` was appended
         # after `chunk`: a field inserted before an existing one is parsed AS that one by any reader
         # that has not moved in the same commit. EMPTY when the leg declares none, which is legal and
         # is what an adopter emitted manifest carries until the deployer learns the key
         # (TOOL-aBoundedCeiling-5). A non-integer or non-positive value reads as absent rather than
         # as zero: `timeout 0` means NO timeout, so coercing junk to 0 would silently unbound the one
         # leg whose declaration was malformed.
         + "\x1e" + (str(l["ceiling"]) if isinstance(l.get("ceiling"), int)
                            and not isinstance(l.get("ceiling"), bool) and l["ceiling"] > 0 else "")
         # THE EIGHTH FIELD, `signature`, appended after `ceiling` for the reason every field since
         # `subject` was appended rather than inserted. CARRIED AND NEVER EXECUTED AT L: the red
         # attribution grades both ends with the signature in the BASE revision row, so a run cannot
         # choose its own grader by editing this one (TOOL-dDerivedDocket-23 F4). A non-list reads
         # as absent, which is the byte-identical rule and the safe direction.
         + "\x1e" + ("\x1f".join(str(a) for a in l["signature"])
                            if isinstance(l.get("signature"), list) else "")
         # THE NINTH FIELD, `doc_reads`, appended after `signature` for the same reason. ABSENT and
         # DECLARED-EMPTY must stay two values, because they mean opposite things on a doc push: no
         # declaration runs the leg, an empty one says it reads no doc path and skips it. So a
         # declared list rides behind a leading `=` and an absent one is the empty string. A non-list
         # reads as absent, which is the direction that runs the leg (TOOL-dThriftyLanding-1).
         + "\x1e" + ("=" + ",".join(resolve_prefix_token(g, troot) for g in l["doc_reads"])
                            if isinstance(l.get("doc_reads"), list) else "")
         # THE TENTH AND ELEVENTH FIELDS, appended for the same reason, read only by the held-tier
         # selection (TOOL-aSparedSpawn-12 S4): the row hash, the SHA-1 of this row as JSON with
         # sorted keys, so a record earned under another row reads as stale; and the record name,
         # the first 16 hex of the SHA-1 of the leg name, which stays put when the row changes.
         + "\x1e" + hashlib.sha1(json.dumps(l, sort_keys=True).encode()).hexdigest()
         + "\x1e" + hashlib.sha1(str(l["name"]).encode()).hexdigest()[:16]
         for l in data]
if pm is not None:
    rows = [pm] + rows
sys.stdout.buffer.write(("\n".join(rows) + "\n").encode())   # LF bytes (Windows text stdout is CRLF); \x1e field sep is non-whitespace so an empty guard field is preserved (a tab would collapse)
' "$LEGS_FILE" "$TIMINGS" "$(dirname "$KITREL")" "$KITREL/ceiling-evidence.txt" ${_pm_args[@]+"${_pm_args[@]}"}) \
  || { echo "run-gates: cannot parse $LEGS_FILE"; exit 2; }
# The leading process-monitor line, stripped before line 1 is read. A conf that exists always gets
# one, so its absence is a program that did not run the question, which reads as the resolver's
# refusal would rather than as a found kit.
PROCMON_LINE=""
if [ "$PROCMON_CONF" = 1 ]; then
  PROCMON_LINE=${legs%%$'\n'*}
  case "$legs" in *$'\n'*) legs=${legs#*$'\n'} ;; *) legs="" ;; esac
fi
unset _pm_args

# Rows stay 1:1 with the manifest so the dispatch indices address the same legs the reader reports.
# An empty name is the drop-sentinel: kept in the arrays to hold the index, never run and never counted.
names=(); guards=(); argvs=(); legreads=(); chunks=(); subjects=(); ceilings=(); signatures=(); docreads=()
rowhashes=(); heldkeys=(); ORDER=""; first=1
while IFS= read -r line; do
  if [ "$first" = 1 ]; then IFS=$'\x1e' read -r ORDER PY_ID <<<"$line"; first=0; continue; fi
  IFS=$'\x1e' read -r nm gd_ av im ch sj ce sg dr rwh_ hky_ <<<"$line"
  names+=("$nm"); guards+=("$gd_"); argvs+=("$av"); legreads+=("${im:-}"); chunks+=("${ch:-default}")
  subjects+=("${sj:-repo}"); ceilings+=("${ce:-}"); signatures+=("${sg:-}"); docreads+=("${dr:-}")
  rowhashes+=("${rwh_:-}"); heldkeys+=("${hky_:-}")
done <<<"$legs"
total=${#names[@]}

# ---- PROCESS-MONITOR DELEGATION, RESOLVED (TOOL-aSparedSpawn-4 S10) ------------------------------
# The detection the defaults above the turnstile describe, read from the leading line the legs parse
# printed: `0` and the kit dir, or the refusal, which names the places looked. Its scope probe follows
# unchanged, and the line prints here, after the turnstile lines, which is the one ORDER change.
if [ -n "$PROCMON_LINE" ] || [ "$PROCMON_CONF" = 1 ]; then
  _pm_dir=${PROCMON_LINE#*$'\x1e'}
  case "$PROCMON_LINE" in
    0$'\x1e'?*) PROCMON_REAP="$ROOT/$_pm_dir/reap.py"; PROCMON_SCOPE="$ROOT/$_pm_dir/scope.py" ;;
    *) PROCMON_WHY="adopted, but the kit is not found ($_pm_dir); tree kills use the runner's own depth-8 walk" ;;
  esac
fi
if [ -f "$PROCMON_REAP" ] && [ -f "$PROCMON_SCOPE" ]; then
  _pm_win=$(ps -W 2>/dev/null | awk -v p="$$" '$1==p {print $4}')
  if [ -z "$_pm_win" ]; then
    PROCMON_WHY="installed, but this runner has no resolvable winpid; tree kills fall back"
  elif PROCMON_ROOT="$ROOT" "$PYBIN" "$PROCMON_SCOPE" --explain "$_pm_win" 2>/dev/null \
       | grep -q "IN SCOPE"; then
    PROCMON_OK=1
    PROCMON_WHY="delegating tree kills to process-monitor"
  else
    PROCMON_WHY="installed, but its declared roots do not admit this runner; tree kills fall back"
  fi
fi
echo "run-gates: process-monitor: $PROCMON_WHY"

# ---- THE FOREIGN-LOAD CENSUS. TOOL-aGraftedHelix-5 ------------------------------------------------
# `derive-ceilings.py` argues every ceiling from the `.leg` readings this runner records, and a reading
# taken while ANOTHER session's suite or another clone's bar loaded the host reads exactly like a slow
# leg. So the run takes a census of foreign gate work while its legs run, and each `.leg` row carries
# what it found as its eighth field, `foreign`: the largest count of foreign trees a sample inside the
# leg's window saw, `unknown` when the census could not see, `0` when it saw none. The evidence tool
# argues a ceiling only from `0` rows.
#
# WHAT COUNTS. A process-table row is gate work when its WHOLE line names a script some manifest leg
# runs, this runner or its sibling self-test runner, or carries a word ending `.test.sh` or
# `selftest.py`. The tokens are derived HERE, once, from the parsed argvs: every word carrying a `/`
# and ending `.sh`, `.py` or `.js`. This runner's own ancestors and descendants are never foreign, and
# the ancestors are not decoration: an agent session's `bash -c` wrapper carries its whole command
# text, so the wrapper of the session that started THIS bar names the runner's path. A tree counts
# once, at its topmost matching process.
#
# WHAT IT CANNOT SEE, said here because a `0` reads as "quiet host": load not shaped like this
# repository's gate work — another repository's build under other script names, an on-access scanner,
# an agent's own CPU — and on Windows any process no MSYS shell spawned. Contention from this bar's
# OWN neighbours is not foreign either; `measure_neighbours` and the serial retry own that. It can
# over-count, which only sets a reading aside: a bar queued on the turnstile, a short command whose
# text names a gate script, and on Windows an orphan of this bar's own legs whose parent reads 1.
#
# THE PERIOD IS A CONSTANT, and `GATE_CENSUS_EVERY` overrides it for the fixtures: no host has asked
# for another, and a profile knob would cost the canary's pinned set.
CENSUS_EVERY=60
if [ -n "${GATE_CENSUS_EVERY:-}" ]; then
  if num_ok "$GATE_CENSUS_EVERY"; then CENSUS_EVERY=$((10#$GATE_CENSUS_EVERY))
  else echo "run-gates: NOTE - GATE_CENSUS_EVERY='$GATE_CENSUS_EVERY' is not a positive integer, so the foreign-load census samples every ${CENSUS_EVERY}s" >&2; fi
fi
CENSUS_TOKENS="$WORK/census.tokens"
{
  printf '%s\n' "$KITREL/run-gates.sh" "$KITREL/run-selftests.sh"
  for ((i=0; i<total; i++)); do
    IFS=$'\x1f' read -ra _ct_av <<<"${argvs[$i]}"
    for _ct_w in ${_ct_av[@]+"${_ct_av[@]}"}; do
      case "$_ct_w" in *[[:space:]]*) ;; */*.sh|*/*.py|*/*.js) printf '%s\n' "$_ct_w" ;; esac
    done
  done
} > "$CENSUS_TOKENS" 2>/dev/null || CENSUS_TOKENS=""
unset _ct_av _ct_w

# ---- THE HELD TIER, SELECTED BY THE KIT WHOSE SHIPPED BYTES MOVED (TOOL-aSparedSpawn-12) -----------
# `GATE_SELFTESTS=changed` runs a held leg only when one of these holds, and holds it otherwise with a
# line naming the sha it is unchanged since: it has no last-run record, an unreadable one, one whose
# sha is not an ancestor of HEAD, or one earned under another manifest row; its record sits more than
# `GATE_SELFTESTS_MAX_LAG` (default 10, owner ruling F2) first-parent commits behind HEAD; or a path in
# its SELECTION SET differs between the recorded sha and the working tree. The set is the owning
# kit's shipped sources in govkit's EPOCH_ROLES (`govkit.py shipped --epoch`, the derivation the
# version-bump rule reads) plus the suite file; the owner is every govkit entry whose `shipped` rows
# carry one of the leg's suite files, which are the argv words the census above reads. A leg no entry
# owns, and every leg when govkit cannot be reached, selects by its guard plus its suite file instead,
# and the bar says so once. A record is written only by a leg that EXECUTED green on a clean, unmoved
# tree, under any non-empty `GATE_SELFTESTS` (the writer is beside the full-green stamp).
#
# THE DECISION IS MADE ONCE, here, by one program, and read twice: the hold pass below reads the
# `<i>.unchanged` file it leaves and `report_one` prints from the same file. A leg it says nothing
# about executes, so a crashed selection costs time and never a held suite. govkit is a sibling kit and
# this runner is an engine, so it is reached through `resolve_kit_dir`, never by literal.
#
# WHAT THIS DOES NOT CHECK: that a selection set is complete. A suite reading a file its kit does not
# ship is held while that file moves, until the lag bound executes it. Untracked files are not in
# `git diff`, so a new file nobody added selects nothing. Nothing at any push boundary sets this mode,
# by owner ruling F1; it serves developer and Definition-of-Done runs.
HELD_DIR=""; [ -n "$RG_COMMON_RAW" ] && HELD_DIR="$RG_COMMON_RAW/gate-selftest-last"
if [ "${GATE_SELFTESTS:-}" = changed ]; then
  SELFTESTS_MAX_LAG=10
  if [ -n "${GATE_SELFTESTS_MAX_LAG:-}" ]; then
    if num_ok "$GATE_SELFTESTS_MAX_LAG"; then SELFTESTS_MAX_LAG=$((10#$GATE_SELFTESTS_MAX_LAG))
    else echo "run-gates: NOTE - GATE_SELFTESTS_MAX_LAG='$GATE_SELFTESTS_MAX_LAG' is not a positive integer, so the held-tier lag bound is $SELFTESTS_MAX_LAG" >&2; fi
  fi
  _sel_in=""
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    { [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; } || continue
    _sel_in+="$i"$'\x1e'"${names[$i]}"$'\x1e'"${heldkeys[$i]}"$'\x1e'"${rowhashes[$i]}"$'\x1e'"${guards[$i]}"$'\x1e'"${argvs[$i]}"$'\n'
  done
  # Output rows, RS-separated: `F` and a note printed once; `R`, a leg index and why it runs; `H`, a
  # leg index and the short sha it is unchanged since. NOTE: single-quoted, so no apostrophe below.
  # The rows go to a scratch file the loop below reads, never through a substitution: a loop fed by
  # one is the class the shell-hygiene leg counts (TOOL-aSweptBar-4).
  printf '%s' "$_sel_in" | "$PYBIN" -c "$RKD_PROGRAM"'
import subprocess, sys
here, rdir, head, bound = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
legs = [r.split("\x1e") for r in sys.stdin.buffer.read().decode("utf-8").split("\n") if r]
out = []

def run_git(*args):
    p = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, p.stdout

def check_hit(path, specs):
    for g in specs:
        if g == "" or path == g.rstrip("/") or path.startswith(g.rstrip("/") + "/"):
            return True
    return False

# The two govkit questions, asked once each. Any refusal or nonzero exit is "cannot be reached".
owners, epoch, why = None, {}, ""
try:
    gk = str(resolve_kit_dir("govkit", "govkit.py", here) / "govkit.py")
    rows = []
    for extra in ([], ["--epoch"]):
        p = subprocess.run([sys.executable, gk, "shipped", *extra], capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        if p.returncode != 0:
            raise LookupError("govkit.py shipped %s exited %d" % (" ".join(extra), p.returncode))
        rows.append([r.split("\t") for r in p.stdout.splitlines() if r.count("\t") == 2])
    owners = {}
    for e, _role, src in rows[0]:
        owners.setdefault(src, set()).add(e)
    for e, _role, src in rows[1]:
        epoch.setdefault(e, set()).add(src)
except Exception as ex:
    why = " ".join(str(ex).split())

fallback, todo = [], {}
for i, name, key, rowhash, guard, argv in legs:
    suites = [w for w in argv.split("\x1f") if "/" in w and not any(c.isspace() for c in w)
              and w.endswith((".sh", ".py", ".js"))]
    ents = set().union(*(owners.get(s, set()) for s in suites)) if owners is not None else set()
    if ents:
        specs = set(suites).union(*(epoch.get(e, set()) for e in ents))
    else:
        specs = set(suites) | set(g for g in guard.split(",") if g) if guard else {""}
        if owners is not None:
            fallback.append(name)
    sha = rowseen = ""
    try:
        with open(rdir + "/" + key, encoding="utf-8") as fh:
            for ln in fh.read().splitlines():
                k, _, v = ln.partition("\t")
                if k == "sha":
                    sha = v
                elif k == "row":
                    rowseen = v
    except OSError:
        out.append("R\x1e%s\x1eno last-run record" % i); continue
    if len(sha) < 40 or any(c not in "0123456789abcdef" for c in sha) or not rowseen:
        out.append("R\x1e%s\x1eits last-run record is unreadable" % i); continue
    if rowseen != rowhash:
        out.append("R\x1e%s\x1eits manifest row changed since its record" % i); continue
    if not head:
        out.append("R\x1e%s\x1eHEAD is unborn" % i); continue
    todo.setdefault(sha, []).append((i, specs))

for sha, members in todo.items():
    s8 = sha[:8]
    why_run = ""
    if run_git("merge-base", "--is-ancestor", sha, head)[0] != 0:
        why_run = "recorded %s is not an ancestor of HEAD" % s8
    else:
        rc, n = run_git("rev-list", "--count", "--first-parent", sha + ".." + head)
        if rc != 0 or not n.strip().isdigit():
            why_run = "the lag behind recorded %s could not be read" % s8
        elif int(n) > bound:
            why_run = "recorded %s is %d first-parent commits behind HEAD, beyond the bound %d" % (s8, int(n), bound)
    if why_run:
        out += ["R\x1e%s\x1e%s" % (i, why_run) for i, _s in members]; continue
    rc, moved = run_git("-c", "core.quotePath=false", "diff", "--name-only", "--no-renames", sha)
    if rc != 0:
        out += ["R\x1e%s\x1ethe diff since recorded %s could not be read" % (i, s8) for i, _s in members]
        continue
    moved = [m for m in moved.splitlines() if m]
    for i, specs in members:
        hit = next((m for m in moved if check_hit(m, specs)), "")
        out.append("R\x1e%s\x1e%s moved since %s" % (i, hit, s8) if hit else "H\x1e%s\x1e%s" % (i, s8))

if why:
    out.insert(0, "F\x1egovkit is not reachable (%s), so every held leg selects by its guard plus its suite file" % why)
elif fallback:
    out.insert(0, "F\x1eno kit ships the suite of %d held leg(s), so each selects by its guard plus its suite file: %s"
               % (len(fallback), ", ".join(fallback)))
sys.stdout.buffer.write("".join(r + "\n" for r in out).encode("utf-8"))
' "$KITDIR" "$HELD_DIR" "$RG_HEAD" "$SELFTESTS_MAX_LAG" > "$WORK/held-select" \
    || echo "run-gates: selftests changed: the selection program failed, so every held leg it did not decide executes" >&2
  while IFS=$'\x1e' read -r _sel_k _sel_i _sel_v; do
    case "$_sel_k" in
      F) printf 'run-gates: selftests changed: %s\n' "$_sel_i" ;;
      R) printf 'run-gates: selftests changed: %s runs (%s)\n' "${names[$_sel_i]}" "$_sel_v" ;;
      H) printf '%s' "$_sel_v" > "$WORK/$_sel_i.unchanged" ;;
    esac
  done < "$WORK/held-select"
  unset _sel_in _sel_k _sel_i _sel_v
fi

# UNBOUNDED LEGS ARE REPORTED, NEVER REFUSED. TOOL-aBoundedCeiling-1 S6. The runner cannot know
# whether a row with no ceiling is a gov leg somebody forgot or an adopter leg the deployer has no
# business bounding, and a refusal it cannot justify is a refusal that reds a tree for a field it
# has no way to supply -- the class the shipped canary header names. So this is a COUNT on the
# profile line, which is where an operator already reads this run's knobs. The DECLARATION
# requirement over gov's own corpus is S9, in run-gates.gov.test.sh, which is the suite allowed to
# hold a claim about this repository.
# Guard evaluation runs SERIALLY and up front: it is a read-only `git diff` per guarded leg, and
# deciding before dispatch keeps the skip verdict independent of scheduling.
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  # SUBJECT FIRST, and in this pass rather than in the dispatch loop. A kit-subject leg tests the
  # KIT'S OWN SOURCE and has no job in a repo that copy-installs the kit and never edits it, so it
  # runs only when asked. `GATE_FULL` deliberately does NOT ask: it means "ignore every guard", and
  # conflating it with "run the kit's own tests" would leave no way to request a complete bar
  # without them — and it is the very bypass that made `guard = ["{kit}/"]` ineffective here.
  # Deciding in the dispatch loop instead would leave an index with no result, which the reporting
  # pass reports as `(no result)`. TOOL-dUnstalledConvoy-26.
  #
  # THE CHUNK IS HELD TOO, by owner ruling 2026-08-26: EVERY self-test is on demand, not just the
  # kit-subject ones. The `subject = kit` predicate alone left SIX legs in the `selftests` chunk
  # running on every bar, because they carry `subject = repo` — the two hook self-tests, the
  # push-main self-test, the recall floor arms and the two run-gates canaries. Each is a `.test.sh`
  # or `test_*.py` that exercises a checker's own source, which is the thing this hold is for, and
  # the split by subject was grading WHOSE source rather than WHAT KIND of leg it is.
  #
  # WHAT THIS COSTS, stated rather than discovered later: the two run-gates canaries are the bar's
  # own liveness assertion — the arms that catch a guard naming an untracked path, which would
  # otherwise skip forever and silently. Holding them means a default bar no longer proves it can
  # move. That is a real reduction in what a green means, it is the owner's call, and
  # `GATE_SELFTESTS=1` remains the way to ask for it. The push boundary is where it matters, and
  # `.githooks/pre-push` decides there against a recorded green whose `selftests` key says whether
  # the recorded run had them held.
  # Under `GATE_SELFTESTS=changed` a held leg the selection above found unchanged is held the same
  # way, and its `.unchanged` file is what `report_one` names the sha from (TOOL-aSparedSpawn-12).
  if { [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; } \
     && { [ -z "${GATE_SELFTESTS:-}" ] || [ -f "$WORK/$i.unchanged" ]; }; then
    printf 'ondemand' > "$WORK/$i.rc"; continue
  fi
  # THE DOCS MODE DECIDES A DECLARING LEG BY ITS DOC READS ALONE. Its guard is a statement about
  # every path it reads, code included, and on a doc-only push no code path moved, so the narrower
  # declaration is the one that answers. A leg that declares nothing falls through to its guard, or
  # runs, exactly as before. `=` alone is a declared empty list: it reads no doc path.
  if [ -n "$DOCS_BASE" ] && [ -n "${docreads[$i]}" ]; then
    _dr=${docreads[$i]#=}
    if [ -z "$_dr" ]; then printf 'docskip' > "$WORK/$i.rc"; continue; fi
    IFS=, read -ra gp <<<"$_dr"
    check_doc_moved "${gp[@]}" || printf 'docskip' > "$WORK/$i.rc"
    continue
  fi
  [ -z "${guards[$i]}" ] && continue
  IFS=, read -ra gp <<<"${guards[$i]}"
  changed "${gp[@]}" || printf 'skip' > "$WORK/$i.rc"
done

# UNBOUNDED LEGS ARE REPORTED, NEVER REFUSED, and counted over the legs that will actually RUN.
# The runner cannot tell a leg somebody forgot from an adopter leg the deployer has no business
# bounding, so a refusal it cannot justify would red a tree for a field it has no way to supply.
# Counted HERE rather than at parse time: before the hold and guard passes the count is a fact about
# the manifest, and this line claims to be a fact about the run. TOOL-aBoundedCeiling-1 S6.
unbounded=0; willrun=0
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  [ -f "$WORK/$i.rc" ] && continue          # already held, skipped or reuse-marked: it will not run
  willrun=$((willrun + 1))
  [ -n "${ceilings[$i]:-}" ] || unbounded=$((unbounded + 1))
done
[ "$unbounded" -gt 0 ] && printf 'run-gates: %s of %s legs that will run declare no ceiling and run unbounded\n' "$unbounded" "$willrun" >&2

# The per-leg INPUT KEY: "what did this leg's verdict depend on". Written here and CONSUMED by
# the reuse unit, which is what makes the two units' authority explicit rather than assumed —
# that unit defines what the key means, this one is where the value is in scope to compute.
#
# A guarded leg is keyed on its own guard pathspecs; an unguarded leg declares by its silence
# that it reads everything, so it is keyed on the whole-tree fingerprint. Both also take the
# argv, the manifest row and what the row declares it reads beyond its inputs (`build_key_text`),
# because the same paths run by a different command, or diffed against a different baseline by a
# leg that reads one, are not the same question.
#
# INDEX-AND-WALK rather than a hash of every file: `ls-files -s` is one cheap git call per leg
# and carries the committed and staged blobs, and the dirt slice below is taken from the ONE
# whole-tree walk the run already ran, which hashed each dirty file once (TOOL-aSparedSpawn-1 S1).
#
# Empty fingerprint, a failed walk or an empty digest means we could not measure the input, and an
# unmeasurable input is NOT a reusable one: the key is a dash, which the reuse unit must treat as
# "never matches".
input_key() { # leg index -> the key, or a dash
  local i=$1 gp comp=""
  [ -n "$FPRINT_START" ] && [ "$WALK_OK" = yes ] && [ -n "$REUSE_DIGEST" ] || { printf '%s' -; return; }
  if [ -n "${guards[$i]}" ]; then
    IFS=, read -ra gp <<<"${guards[$i]}"
    comp=$(git ls-files -s -- "${gp[@]}" 2>/dev/null | LC_ALL=C sort) || comp=""
  fi
  build_key_text "$i" "$comp"
  printf '%s' "$KEY_TEXT" | git hash-object --stdin 2>/dev/null || printf '%s' -
}

# build_key_text <leg index> <its sorted `ls-files -s` listing> -> KEY_TEXT, the bytes the key
# hashes: the argv, the row's classes and hash, the declared reads, the leg's inputs and the
# toolchain digest. ONE composition for the
# per-leg `input_key` above and the precompute below, so the two cannot disagree about what a key is.
build_key_text() {
  local i=$1 comp=$2 gp dirt="" r p g
  if [ -n "${guards[$i]}" ]; then
    IFS=, read -ra gp <<<"${guards[$i]}"
    # The guard's share of the dirt, matched the way the `ls-files` pathspec above matches: the path
    # IS the guard, or sits under the directory it names, with or without its slash. A substring
    # match also took `xga/f` for guard `ga/`. Without this share a guarded leg's key would not move
    # when a guarded file is edited but not committed, which is most of the edits a developer makes.
    # ponytail: rows x guards in builtins per leg; an index by top directory if a tree dirties thousands.
    for r in "${DIRT_ROWS[@]}"; do
      p=${r:3}; p=${p#* }
      for g in "${gp[@]}"; do
        g=${g%/}
        if [ "$p" = "$g" ] || [ "${p#"$g"/}" != "$p" ]; then dirt+="$r"$'\n'; break; fi
      done
    done
    comp="$comp
$dirt"
  else
    comp="$FPRINT_START"
  fi
  # THE DECLARED READS, and only those (TOOL-aSparedSpawn-13 S2): the base where the row says `base`,
  # HEAD where it says `history` or `remote`, the UTC day where it says `clock`, the observed remote
  # where it says `remote`. An undeclared leg's key moves with none of them, so a landing that moves
  # BASE no longer misses every leg. The row hash always enters: a reworded row is another question.
  local cls=",${legreads[$i]}," ext=""
  case $cls in *,base,*) ext+="base $BASE ${GATE_PUSH_BASE:-}"$'\n' ;; esac
  case $cls in *,history,*|*,remote,*) ext+="head $RG_HEAD"$'\n' ;; esac
  case $cls in *,clock,*) ext+="day $REUSE_DAY"$'\n' ;; esac
  case $cls in *,remote,*) ext+="remote $REMOTE_OBS"$'\n' ;; esac
  printf -v KEY_TEXT '%s\n---\n%s %s\n%s---\n%s\n---\n%s\n' "${argvs[$i]}" "${legreads[$i]}" "${rowhashes[$i]}" \
    "$ext" "$comp" "$REUSE_DIGEST"
}

# THE KEYS, COMPUTED ONCE BEFORE DISPATCH (TOOL-aSparedSpawn-4 S5) into `INPUT_KEYS`, which every
# forked worker inherits, so neither the reuse block nor a ledger row asks git anything per leg. The
# per-leg question was an `ls-files -s | sort` and a `hash-object`, asked twice for a reused leg. Here
# it is one `ls-files -s` over the UNION of the guards, sorted once, so each leg's slice, taken in that
# order, is already the sorted listing its own call printed; one `awk` pass writes each slice; and
# one `hash-object --stdin-paths` hashes every key text. `--no-filters` because a path is hashed
# through the attributes a `--stdin` never sees, and `--git-dir` with `-C` because the texts live in
# the scratch dir, which a native git on an MSYS host cannot read by its POSIX name from stdin, while
# the repository's object format must still pick the hash.
#
# THE SLICE IS THE DIRT RULE: the path IS the guard, or sits under it. That is what git's pathspec
# does only for a PLAIN guard, so a guard holding a glob character, pathspec magic, a `..`, an absolute
# or empty path, `.`, or any byte `ls-files` would quote, sends its leg to `input_key`, the per-leg
# definition, unchanged. A quoted listing line is matched by its escaped text, which agrees with the raw
# path on every plain prefix. Any failure in the bulk half reads as the dash `input_key` gives a
# failed hash, never as a key: an unmeasurable input is not a reusable one. `KEYS_FAIL` names the step
# that failed, which the caller prints (TOOL-aSparedSpawn-16 S18): a silent dash is a saving lost unseen.
INPUT_KEYS=()
KEYS_FAIL=""
build_input_keys() {
  local i g gp n_bulk=0 bulk="" union=() plain shas=() k=0 comp
  local -a lines=()
  for ((i=0; i<total; i++)); do
    [ -n "${names[$i]}" ] || continue
    [ -f "$WORK/$i.rc" ] && continue          # held, skipped or docskipped: it never needs a key
    if ! { [ -n "$FPRINT_START" ] && [ "$WALK_OK" = yes ] && [ -n "$REUSE_DIGEST" ]; }; then
      INPUT_KEYS[$i]=-; continue
    fi
    plain=1
    if [ -n "${guards[$i]}" ]; then
      IFS=, read -ra gp <<<"${guards[$i]}"
      for g in "${gp[@]}"; do
        case "$g" in
          ''|.|./|/*|:*|*[!A-Za-z0-9._/@+=-]*|*..*|*//*) plain=0 ;;
        esac
      done
      if [ "$plain" = 1 ]; then union+=("${gp[@]}"); fi
    fi
    if [ "$plain" = 1 ]; then bulk+=" $i"; n_bulk=$((n_bulk + 1))
    else INPUT_KEYS[$i]=$(input_key "$i"); fi
  done
  [ "$n_bulk" -gt 0 ] || return 0
  : > "$WORK/keys.slices"
  if [ "${#union[@]}" -gt 0 ]; then
    git ls-files -s -- "${union[@]}" 2>/dev/null | LC_ALL=C sort > "$WORK/keys.listing" 2>/dev/null
    for i in $bulk; do
      [ -n "${guards[$i]}" ] && printf '%s\t%s\n' "$i" "${guards[$i]}"
    done > "$WORK/keys.guards"
    # One file per guarded leg, `keys.slice.<i>`, holding its lines of the listing in listing order. A
    # guard ending in `/` names a directory, so, as in git's pathspec, it never matches a file of that
    # exact name; without the slash it matches the file or everything under the directory.
    awk -F'\t' -v dir="$WORK" '
      FNR == NR { leg[++nl] = $1; ng[nl] = split($2, gl, ",")
                  for (j = 1; j <= ng[nl]; j++) { g = gl[j]; dn[nl, j] = sub(/\/$/, "", g); gd[nl, j] = g }
                  printf "" > (dir "/keys.slice." $1); next }
      { line = $0; p = substr(line, index(line, "\t") + 1)
        if (substr(p, 1, 1) == "\"" && substr(p, length(p), 1) == "\"") p = substr(p, 2, length(p) - 2)
        for (l = 1; l <= nl; l++) for (j = 1; j <= ng[l]; j++) {
          g = gd[l, j]
          if ((p == g && !dn[l, j]) || substr(p, 1, length(g) + 1) == g "/") { print line > (dir "/keys.slice." leg[l]); break }
        } }
      END { for (l = 1; l <= nl; l++) close(dir "/keys.slice." leg[l]) }
    ' "$WORK/keys.guards" "$WORK/keys.listing" 2>/dev/null || { KEYS_FAIL="the guard slices"; return 0; }
  fi
  for i in $bulk; do
    lines=(); comp=""
    if [ -n "${guards[$i]}" ]; then
      { mapfile -t lines < "$WORK/keys.slice.$i"; } 2>/dev/null || { KEYS_FAIL="the guard slices"; return 0; }
      [ "${#lines[@]}" -gt 0 ] && printf -v comp '%s\n' "${lines[@]}"
      comp=${comp%$'\n'}
    fi
    build_key_text "$i" "$comp"
    printf '%s' "$KEY_TEXT" > "$WORK/key.$i" || { KEYS_FAIL="a key text"; return 0; }
    printf 'key.%s\n' "$i" >> "$WORK/keys.slices"
  done
  git --git-dir="$RG_COMMON" -C "$WORK" hash-object --no-filters --stdin-paths \
    < "$WORK/keys.slices" > "$WORK/keys.shas" 2>/dev/null || { KEYS_FAIL="the key hashes"; return 0; }
  { mapfile -t shas < "$WORK/keys.shas"; } 2>/dev/null
  [ "${#shas[@]}" = "$n_bulk" ] || { KEYS_FAIL="the key hashes"; return 0; }
  for i in $bulk; do INPUT_KEYS[$i]=${shas[$k]%$'\r'}; k=$((k + 1)); done
}

# ---- REUSE: THE MODE, THE CACHE AND THE OBSERVED REMOTE (TOOL-aSparedSpawn-13, -32) -------------
# THE MODE, ONE PER RUN, by a fixed precedence (TOOL-aSparedSpawn-32 S7). Under `GATE_FULL` it is
# `lineage` when `REUSE_ASK_LINEAGE` is set and `off` otherwise, and a set `GATE_REUSE` or
# `GATE_REUSE_PUSH` is named as not used. Without it, `push` when `REUSE_ASK_PUSH` names HEAD, else
# `env` when `REUSE_ASK_ENV` is set, else `off`, and a set `GATE_REUSE_LINEAGE` is named as not used.
# `push` and `env` read the cache and `lineage` the ledger; what each mode reuses, and who sets its
# knob, is the README's reuse section. `GATE_FULL` therefore still means "no cache reuse" (S8 of -13),
# the boundary's lineage run being the one exception, because its verdicts were earned by full runs.
REUSE_MODE=off; REUSE_WHY=""; REUSE_PUSH_SHA=""; REUSE_PUSH_TIP=""; REUSE_PUSH_DIGEST=""
REUSE_CACHE=""; [ -n "$RG_COMMON_RAW" ] && REUSE_CACHE="$RG_COMMON_RAW/gate-cache"
if [ -n "${GATE_FULL:-}" ]; then
  _unused="${REUSE_ASK_ENV:+ GATE_REUSE}${REUSE_ASK_PUSH:+ GATE_REUSE_PUSH}"
  if [ -n "$REUSE_ASK_LINEAGE" ]; then
    REUSE_MODE=lineage
    [ -n "$_unused" ] && REUSE_WHY="GATE_FULL is set, so the lineage mode alone applies — not used:${_unused}"
  else
    [ -n "$_unused" ] && REUSE_WHY="GATE_FULL is set, so nothing is reused"
  fi
  unset _unused
else
  [ -n "$REUSE_ASK_LINEAGE" ] && printf 'run-gates: reuse — GATE_REUSE_LINEAGE is not used without GATE_FULL\n' >&2
  if [ -n "$REUSE_ASK_PUSH" ]; then
    read -r REUSE_PUSH_SHA REUSE_PUSH_TIP REUSE_PUSH_DIGEST _ <<<"$REUSE_ASK_PUSH"
    if [ -n "$REUSE_PUSH_DIGEST" ] && [ -n "$RG_HEAD" ] && [ "$REUSE_PUSH_SHA" = "$RG_HEAD" ]; then REUSE_MODE=push
    else REUSE_WHY="GATE_REUSE_PUSH names ${REUSE_PUSH_SHA:-nothing} and HEAD is ${RG_HEAD:-unread}, so nothing is reused"; fi
  fi
  [ "$REUSE_MODE" = off ] && [ -n "$REUSE_ASK_ENV" ] && { REUSE_MODE=env; REUSE_WHY=""; }
fi
case $REUSE_MODE in env|push)
  if [ -z "$REUSE_CACHE" ]; then REUSE_MODE=off; REUSE_WHY="no git common dir holds a cache"; fi ;;
esac
[ -n "$REUSE_WHY" ] && printf 'run-gates: reuse — %s\n' "$REUSE_WHY" >&2

# WHAT A REUSABLE `ok` MEANS. Bump this when a runner change redefines it: every recorded ledger row
# then misses at once, which is the "did more work" direction. A constant rather than the runner's
# own blob, because the runner's comments move in most builds. TOOL-aSparedSpawn-1 S5. 3 since the key
# carries declared reads and the cache replaced the ledger as the store (TOOL-aSparedSpawn-13). 4 since
# a push's key reads the caller's restored environment and PATH reads `/bin` as `/usr/bin`
# (TOOL-aSparedSpawn-33).
REUSE_SCHEMA=4
# THE TOOLCHAIN, ENVIRONMENT AND HOST DIGEST, one per run, the fourth section of EVERY key
# (TOOL-aSparedSpawn-1 S4). Two runs over identical bytes under a different git, python, bash, MSYS
# runtime or `PYTHONUTF8` are not the same question. Every `GATE_REUSE*` knob is left out so the
# earning run (unset) and the reusing run (set) can agree, and `GATE_TURNSTILE_HELD`,
# `GATE_TURNSTILE_HOLDER` and `GATE_RUN_ID` because each names this run and nothing a leg grades: the
# holder nonce, which origin's host turnstile exports above, moved every key on every run until the
# reconcile of TOOL-aSparedSpawn-32 left it out. `GATE_BASE` and `GATE_PUSH_BASE` are left out
# HERE because they enter the key of a leg declaring `base` and of no other (TOOL-aSparedSpawn-13 S2):
# hashed here they would move every key on every landing. Every other knob stays in: over-sensitive
# is a miss, never a false hit.
# THE CALLER'S ENVIRONMENT UNDER `push` (TOOL-aSparedSpawn-33, the owner's ruling on -25). A pre-push
# hook runs under git's additions, `GIT_EXEC_PATH`, a PATH head and on Git for Windows `LC_CTYPE`, so
# a key taken over this shell never met the one a direct bar earned. The hook restores the caller's
# environment as it was before git and names the file it wrote in `GATE_REUSE_DIGEST_ENV`; in the
# `push` mode that file's lines stand in for this shell's, and its PATH is the one the `tool` lines
# resolve under. The legs still run under the hook's environment: only the key reads the caller's. A
# named file that cannot be read fails the digest. Every mode reads each `/bin` in PATH as `/usr/bin`
# where `-ef` proves them one directory, since a native git round-trips PATH and the hook cannot tell
# which `/usr/bin` was a `/bin`. A value holding a newline is a `%q` line, as the hook writes it.
# WHAT IT DOES NOT SEE: a tool upgraded IN PLACE at the same path, other than git, which pays
# `git version`; and any variable outside the prefix set, which a leg may still read.
REUSE_DIGEST=$(
  printf 'schema %s\n' "$REUSE_SCHEMA"
  printf 'bash %s %s\n' "$BASH_VERSION" "$MACHTYPE"
  if [ -r /proc/version ]; then IFS= read -r r < /proc/version; printf 'runtime %s\n' "$r"; fi
  printf 'python %s %s\n' "$PYBIN" "$PY_ID"
  # An empty digest is reported after `build_input_keys` below (TOOL-aSparedSpawn-16 S18), not here.
  # arm-signature: the input keys could not be measured (the toolchain digest), so nothing is reused or cached this run
  git version 2>/dev/null || exit 1
  git config --get-regexp '^core\.(autocrlf|eol)$' 2>/dev/null
  # The environment, as `env NAME=value` lines: this shell's, from `compgen -e`, sorted, or under
  # `push` the caller's, from the hook's file. PATH is always exported, so a listing without it is a
  # failed read and fails the digest rather than dropping the env.
  evl=(); vp=""
  if [ "$REUSE_MODE" = push ] && [ -n "$REUSE_ASK_DIGEST_ENV" ]; then
    # arm-signature: the input keys could not be measured (the toolchain digest), so nothing is reused or cached this run
    { mapfile -t evl < "$REUSE_ASK_DIGEST_ENV"; } 2>/dev/null || exit 1
  else
    mapfile -t evs < <(compgen -e)
    for v in "${evs[@]}"; do
      if [[ ${!v} == *$'\n'* ]]; then printf -v l 'env %s=%q' "$v" "${!v}"; else l="env $v=${!v}"; fi
      evl+=("$l")
    done
  fi
  for l in "${evl[@]}"; do case $l in "env PATH="*) vp=${l#env PATH=} ;; esac; done
  # arm-signature: the input keys could not be measured (the toolchain digest), so nothing is reused or cached this run
  [ -n "$vp" ] || exit 1
  if [ /bin -ef /usr/bin ]; then
    vp=":$vp:"; b=:/bin: u=:/usr/bin:
    while [[ $vp == *"$b"* ]]; do vp=${vp//"$b"/"$u"}; done
    vp=${vp#:}; vp=${vp%:}
  fi
  PATH=$vp
  # Every other tool a leg names, by the location it resolves to under that PATH: argv[0], each once.
  declare -A seen=()
  for ((i=0; i<total; i++)); do
    [ -n "${names[$i]}" ] || continue
    IFS=$'\x1f' read -r t _ <<<"${argvs[$i]}"
    [ -n "$t" ] && [ -z "${seen[$t]:-}" ] || continue
    seen[$t]=1; printf 'tool %s ' "$t"; type -P "$t" || echo
  done
  # The name patterns below are copied into `.githooks/pre-push`'s view writer, which bounds what
  # reaches its file; the pre-push suite compares the two pattern texts.
  for l in "${evl[@]}"; do
    v=${l#env }; v=${v%%=*}
    case $v in GATE_REUSE*|GATE_TURNSTILE_HELD|GATE_TURNSTILE_HOLDER|GATE_RUN_ID|GATE_BASE|GATE_PUSH_BASE) continue ;;
      PATH) printf 'env PATH=%s\n' "$vp" ;;
      GATE_*|GOV_*|*_PY|GIT_*|PYTHON*|LC_*|LANG|TZ) printf '%s\n' "$l" ;; # digest-env-names
    esac
  done
) && REUSE_DIGEST=$(git hash-object --stdin 2>/dev/null <<<"$REUSE_DIGEST") || REUSE_DIGEST=""
# THE SAMPLE RATE (S6, owner ruling F2: 0.25, uniform per leg), as parts in 10000. A value that is no
# decimal from 0 to 1 is refused back to the default, loudly: a typo must not switch the sample off.
REUSE_SAMPLE=${GATE_REUSE_SAMPLE:-0.25}; SAMPLE_PM=2500
if [[ $REUSE_SAMPLE =~ ^1(\.0*)?$ ]]; then SAMPLE_PM=10000
elif [[ $REUSE_SAMPLE =~ ^0?(\.([0-9]*))?$ ]] && [ -n "$REUSE_SAMPLE" ]; then
  _f="${BASH_REMATCH[2]:-}0000"; SAMPLE_PM=$((10#${_f:0:4}))
else
  printf 'run-gates: GATE_REUSE_SAMPLE=%s is no rate from 0 to 1; sampling at 0.25\n' "$REUSE_SAMPLE" >&2
  REUSE_SAMPLE=0.25
fi
# THE DAY a `clock` leg is keyed on: whole UTC days since the epoch, from the clock bash already
# holds. `GATE_REUSE_DAY` pins it, the seam a `clock` arm needs, as `GATE_RUN_ID` pins the run id.
REUSE_DAY=${GATE_REUSE_DAY:-$((EPOCHSECONDS / 86400))}

# read_remote_heads -> REMOTE_HEADS, `<default-branch tip> <digest of the whole advertisement>`, or
# rc 1 and empty when the probe did not answer or advertised no default branch. One `ls-remote
# --heads`, bounded and redirected to a file, never captured through a pipe: a substitution waits for
# every holder of the pipe, so `timeout` would bound the verdict and not the clock. The digest is
# `git hash-object --stdin` over those bytes, which is what the pre-push hook computes over its own
# probe, so the two agree on one advertisement by construction.
read_remote_heads() {
  local f="$WORK/remote.heads" tip="" l d
  local -a lines=()
  REMOTE_HEADS=""
  [ -n "$RR_REMOTE" ] || return 1
  timeout -k 5s 20 env GIT_TERMINAL_PROMPT=0 "GIT_SSH_COMMAND=ssh -o ConnectTimeout=10 -o BatchMode=yes" \
    git -c credential.interactive=never ls-remote --heads "$RR_REMOTE" > "$f" 2>/dev/null || return 1
  { mapfile -t lines < "$f"; } 2>/dev/null
  for l in "${lines[@]}"; do
    [ "${l#*$'\t'}" = "refs/heads/${DEFBR:-main}" ] && tip=${l%%$'\t'*}
  done
  [ -n "$tip" ] || return 1
  d=$(git hash-object --stdin < "$f" 2>/dev/null) && [ -n "$d" ] || return 1
  REMOTE_HEADS="$tip $d"
}
# THE OBSERVED REMOTE a `remote` leg is keyed on (S9). Asked only when such a leg is still to run on a
# CLEAN tree, the one tree whose verdict may be written; under `push` the hook's own probe, carried in
# the knob, stands in for it. Empty means a `remote` leg neither reuses nor writes.
REMOTE_OBS=""
for ((i=0; i<total; i++)); do
  [ -n "${names[$i]}" ] && [ ! -f "$WORK/$i.rc" ] || continue
  case ",${legreads[$i]}," in *,remote,*) ;; *) continue ;; esac
  if [ "$REUSE_MODE" = push ]; then REMOTE_OBS="$REUSE_PUSH_TIP $REUSE_PUSH_DIGEST"
  elif [ "$TREE_CLEAN" = yes ] && read_remote_heads; then REMOTE_OBS=$REMOTE_HEADS; fi
  break
done

# THE HEADER, written before the first leg dispatches, in a key-per-line grammar. It is what a
# concurrent reader resolves through `gate-run/current` while the run is in flight, and what
# survives a crash to say what the run WAS when the verdict never arrived.
# The manifest blob and the graded sha, read ONCE: the header, every ledger row and the full-green
# stamp carry them, and three reads of one fact are three chances to disagree (TOOL-aFrugalTurnstile-4).
# HEAD is the one the bar's git facts already read (TOOL-aSparedSpawn-4 S7), so it costs no spawn here.
MANIFEST_BLOB=$(git hash-object -- "$LEGS_FILE" 2>/dev/null)
HEAD_SHA=$RG_HEAD
if [ -n "$RUNDIR" ]; then
  derive_temp_path _tp "$RUNDIR/header"
  {
    printf 'schema\t1\n'
    printf 'run_id\t%s\n' "$RUNID"
    printf 'started\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'head\t%s\n' "$RG_HEAD"
    printf 'base\t%s\n' "$BASE"
    printf 'base_from\t%s\n' "${GATE_BASE:+GATE_BASE}${GATE_BASE:-$BASE_FROM_LADDER}"
    printf 'fingerprint\t%s\n' "$FPRINT_START"
    printf 'tree_clean\t%s\n' "$TREE_CLEAN"
    printf 'manifest\t%s\n' "$LEGS_FILE"
    printf 'manifest_blob\t%s\n' "$MANIFEST_BLOB"
    printf 'full\t%s\n' "${GATE_FULL:+1}"
    printf 'docs_base\t%s\n' "$DOCS_BASE"
    printf 'full_from\t%s\n' "${GATE_FULL:+GATE_FULL}"
    printf 'selftests\t%s\n' "$SELFTESTS_STAMP"   # the held-tier mode, TOOL-aSparedSpawn-12
    # THE RUN ENVELOPE IS FOUR KEYS, NOT ONE. The width alone was what an earlier draft recorded,
    # written when the width was a number this script computed. It is now a DECLARED row, so a
    # later reader comparing two runs needs the row NAME, the resolved width, the per-leg timeout
    # and the detection source to tell a re-detected row from a GATE_JOBS override. These are the
    # components of PROF_LINE rather than a second derivation of the same four values.
    printf 'profile_row\t%s\n' "$PROF_NAME"
    printf 'width\t%s\n' "$JOBS"
    printf 'leg_timeout\t%s\n' "$PROF_TIMEOUT"
    # THE REGIME the legs actually ran under, beside the profile knob rather than instead of it: the
    # knob is an input a later reader may want, and the regime is what the run did.
    printf 'leg_ceilings\t%s\n' "$([ "$CEILINGS_LIVE" = 1 ] && echo live || echo inert)"
    printf 'profile_from\t%s\n' "$PROF_TAG"
    printf 'legs\t%s\n' "$total"
    printf 'worktree\t%s\n' "$ROOT"
    # THE QUEUE WAIT, paired value and source, in the header's own `value`/`_from` grammar —
    # `base`/`base_from`, `full`/`full_from`, `profile_row`/`profile_from`. Fourth instance.
    # DELIBERATELY OUTSIDE the run-envelope block above: `run-gates.evidence.test.sh` asserts that
    # block is four keys and selects them BY NAME, so a key added inside would leave that arm green
    # and only its comment lying. `schema` does not bump — every reader selects by key name, so an
    # additive key breaks none, and a bump could not be armed because nothing reads the field.
    printf 'queued\t%s\n'      "$QUEUED"
    printf 'queued_from\t%s\n' "$QUEUED_FROM"
    # THE SLOT KEYS (TOOL-aPairedSlots-2 S7), written above one slot ONLY, so a run at the kit default
    # writes the header it always wrote. `slot` is the slot this run held, `-` when it held none.
    if [ "${TS_SLOTS:-1}" -gt 1 ]; then
      printf 'slots\t%s\n' "$TS_SLOTS"
      printf 'slot\t%s\n'  "${TS_SLOT:--}"
    fi
    # THE ACQUIRE PAIR (TOOL-dDerivedDocket-26 S4), from the variables the stdout line printed, so the
    # header and the line cannot disagree about one run. Outside the envelope block for the reason above.
    printf 'acquired\t%s\n'      "$ACQUIRED"
    printf 'acquired_from\t%s\n' "$QUEUED_FROM"
    # The ambient TMPDIR count the bar printed, measured once after its sweep (TOOL-dDerivedDocket-25
    # S3). Outside the run-envelope block for the reason the queue keys above give.
    printf 'tmpdir_entries\t%s\n' "$TMPDIR_ENTRIES"
    # The census period every `.leg` row's `foreign` field was derived under (TOOL-aGraftedHelix-5): a
    # leg's window reaches three periods before its start. Outside the run-envelope block for the
    # reason the queue keys above give.
    printf 'census_every\t%s\n' "$CENSUS_EVERY"
    # The reuse key's schema (TOOL-aSparedSpawn-1 S5), so a reader can tell a schema miss from a
    # content miss. Outside the run-envelope block for the reason above.
    printf 'reuse_schema\t%s\n' "$REUSE_SCHEMA"
    # The ONE reuse mode the run took, `off`, `env`, `push` or `lineage`, and the sample rate the cache
    # modes draw at (TOOL-aSparedSpawn-13, TOOL-aFrugalTurnstile-4 S4, composed by TOOL-aSparedSpawn-32
    # S7). Outside the run-envelope block for the reason above.
    printf 'reuse\t%s\n' "$REUSE_MODE"
    printf 'reuse_sample\t%s\n' "$REUSE_SAMPLE"
    # The memory pause's threshold this run held dispatch above, `off`, or `inert` where the host gave
    # no reading (TOOL-aGraftedHelix-7). Outside the run-envelope block for the reason above.
    printf 'mempause\t%s\n' "$prof_mrec"
    # Where the width came from, `row`, `calibrated` or `GATE_JOBS`, and the spawn pause's ratio, 0
    # for off (TOOL-aSparedSpawn-2). Outside the run-envelope block for the reason above.
    printf 'width_from\t%s\n' "$WIDTH_FROM"
    printf 'spawnpause\t%s\n' "$SPAWNPAUSE"
    # The RESOLVED dispatch order, recorded here because this is the point at which it is in
    # scope. The chunking unit's ordering criteria read it from the record rather than
    # re-deriving it, which is what keeps the record's key set single-sourced.
    printf 'dispatch\t%s\n' "$ORDER"
  } > "$_tp" 2>/dev/null && mv -f "$_tp" "$RUNDIR/header" 2>/dev/null || true
  chmod 600 "$RUNDIR/header" 2>/dev/null || true
fi

# The keys are wanted by a ledger row, which needs the run directory, or by the reuse block and the
# cache write below; a bar with none of them computes none, as a bar with neither asked git for none.
if [ -n "$RUNDIR" ] || [ "$REUSE_MODE" != off ] || { [ -n "$REUSE_CACHE" ] && [ "$TREE_CLEAN" = yes ]; }; then
  build_input_keys
  # SAID ONCE, ON STDERR (TOOL-aSparedSpawn-16 S18), where the keys were wanted for a saving: an empty
  # toolchain digest or a failed bulk step leaves every key a dash, which executes everything and caches
  # nothing, and until now did so in silence. A ledger-only bar loses no saving, so it says nothing.
  [ -z "$REUSE_DIGEST" ] && KEYS_FAIL="the toolchain digest"
  if [ -n "$KEYS_FAIL" ] && { [ "$REUSE_MODE" != off ] || { [ -n "$REUSE_CACHE" ] && [ "$TREE_CLEAN" = yes ]; }; }; then
    printf 'run-gates: reuse — the input keys could not be measured (%s), so nothing is reused or cached this run\n' "$KEYS_FAIL" >&2
  fi
fi

# ---- reuse a proven green from the CACHE: the `env` and `push` modes (TOOL-aSparedSpawn-13) ---------
# OPT-IN, and that is the boundary rule rather than caution: an advisory input may cause LESS work
# only on a run that is not authoritative. An authoritative run reuses only a `remote` or `history`
# leg, at the exact pushed sha and observed tip, and is then scoped: `.githooks/pre-push` sets
# `GATE_REUSE_PUSH` on a SCOPED decision and on no other, and a run reusing anything from the cache
# stamps no green the boundary trusts (`cache_reuses`). Under `GATE_FULL` the cache is never read; the
# ledger block below is the `lineage` mode, the boundary's one exception (the mode block above).
#
# A leg is reused when ALL of: the mode allows its classes, it carries no legacy `impure`, a `remote`
# leg has an observed remote, its key was measured, its row is not quarantined, the cache holds an
# `ok` under that key in the git common dir, it has not been reused 10 runs in a row (S7), and the
# sample did not draw it (S6). Any missing term means execute: every failure mode of this block is
# "did more work", never "checked less". The cache entry is read by a builtin, so a lookup spawns
# nothing. The age count moves here, in the entry itself, and an execution under the same key resets it
# by writing a fresh entry (the cache block below).
reuses=0; cache_reuses=0; lineage_reuses=0
if [ "$REUSE_MODE" = env ] || [ "$REUSE_MODE" = push ]; then
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.rc" ] && continue                 # already decided by the guard pass
    _cls=",${legreads[$i]},"
    # A LEGACY `impure` is never reused, on any tree, however identical: it says the verdict is a
    # function of something outside the tree and says nothing about what, so no key can carry it.
    case $_cls in *,impure,*) continue ;; esac
    if [ "$REUSE_MODE" = push ]; then
      case $_cls in *,remote,*|*,history,*) ;; *) continue ;; esac
    fi
    case $_cls in *,remote,*) [ -n "$REMOTE_OBS" ] || continue ;; esac
    _key=${INPUT_KEYS[$i]:--}
    [ "$_key" != - ] && [ "${#_key}" -ge 3 ] || continue
    _q=""; { IFS= read -r _q < "$REUSE_CACHE/quarantine.${heldkeys[$i]}"; } 2>/dev/null
    if [ -n "$_q" ] && [ "$_q" = "${rowhashes[$i]}" ]; then
      printf 'run-gates: reuse — %s is quarantined until its manifest row changes\n' "${names[$i]}" >&2
      continue
    fi
    # THE AGE IS THE ENTRY'S SIXTH FIELD (TOOL-aSparedSpawn-16 S11), kept per KEY: an execution under
    # another key, a dirty tree's, no longer resets this one's count. Every field before it is written
    # non-empty, so a TAB-split read cannot shift it; a five-field entry, as an older runner wrote, reads 0.
    _st=""; _es=""; _er=""; _eh=""; _ee=""; _age=""
    { IFS=$'\t' read -r _st _es _er _eh _ee _age _ < "$REUSE_CACHE/${_key:0:2}/$_key"; } 2>/dev/null
    [ "$_st" = ok ] || continue                      # missing, unreadable or malformed: execute
    [[ $_age =~ ^[0-9]+$ ]] || _age=0
    if [ "$_age" -ge 10 ]; then
      printf '%s' "$_key" > "$WORK/$i.aged"
      printf 'run-gates: reuse — %s was reused on %s runs in a row, so it executes\n' "${names[$i]}" "$_age" >&2
      continue
    fi
    # THE DRAW, seeded from the run id so a run's draw replays: a polynomial hash of `<run id>/<leg>`
    # in shell arithmetic, which spawns nothing. ponytail: a 31-polynomial mod a prime, uniform enough
    # for a quarter-rate sample; a keyed hash if anyone ever games the draw.
    _h=7; _s="$RUNID/${names[$i]}"
    for ((_c=0; _c<${#_s}; _c++)); do
      printf -v _o '%d' "'${_s:_c:1}"; _h=$(( (_h * 31 + _o) % 1000000007 ))
    done
    if [ $((_h % 10000)) -lt "$SAMPLE_PM" ]; then
      printf '%s' "$_key" > "$WORK/$i.sampled"
      continue
    fi
    # The reuse rewrites its own entry with the count plus one, in place by `printf`. A reader that meets
    # it torn reads it malformed and executes, which costs a saving and never a verdict.
    printf 'ok\t%s\t%s\t%s\t%s\t%s\n' "$_es" "$_er" "$_eh" "$_ee" "$((10#$_age + 1))" \
      > "$REUSE_CACHE/${_key:0:2}/$_key" 2>/dev/null
    printf 'reuse' > "$WORK/$i.rc"
    cache_reuses=$((cache_reuses+1))
  done
  unset _cls _key _q _st _es _er _eh _ee _age _h _s _c _o
fi

# ---- reuse a proven green from the LEDGER: the `lineage` mode (TOOL-aFrugalTurnstile-4) ------------
# `lineage` is what `.githooks/pre-push` asks for, by `GATE_REUSE_LINEAGE`, on its own FULL decision
# for this runner (TOOL-aFrugalTurnstile-4, design D5, which supersedes TOOL-aPacedTurnstile-6's rule
# that the boundary never reuses): it takes only a verdict a FULL run on a CLEAN tree earned, on this
# same manifest blob, at an ancestor of HEAD, and a run whose every reuse is of that kind may still
# stamp `gate-full-green`. It reads the ledger and never a cache entry (TOOL-aSparedSpawn-32 S6); the
# ledger's opt-in mode is the cache's `env` mode above since TOOL-aSparedSpawn-13.
#
# A leg is reused when ALL of: the leg is not declared `impure`, a `remote` leg has an observed remote,
# its ledger row says `ok`, that row carries a key, the row's `full` is `1`, its `manifest_blob` is this
# run's, its `head` is an ancestor of HEAD, and the key equals the one computed THIS run. Any missing
# term means execute — every failure mode of this block is "did more work", never "checked less".
#
# WHAT LINEAGE REUSE DOES NOT CHECK: that a reused leg's guard names every input the leg reads, or
# that its verdict depends on the tree alone. A reused verdict is only as good as its input key, so
# a too-narrow guard or an undeclared `impure` leg is carried forward until its key moves, the
# remote base moves, or a run without `GATE_REUSE` re-executes it — the post-merge full bar is that
# run.
#
# ONE PASS over the ledger, in bash (S5), never a `grep` spawn per leg; the first row of a name wins,
# as the `grep -m1` this replaced did. Each row's tabs are folded to US (0x1f) before the split:
# `full` is empty on most rows, and a tab IFS collapses an empty field and shifts every field after it.
# The lineage terms run CHEAPEST FIRST (S6): string compares; then the earning run's header `base`,
# a file read, because the key hashes BASE and another base can never match; then ancestry, one
# git spawn per distinct head, memoized; and the key last, compared with the run's precomputed
# `INPUT_KEYS`, the one composition `input_key` also builds. A row whose run names no readable
# header falls through to the key, so a swept record costs work and never a verdict.
if [ "$REUSE_MODE" = lineage ] && [ -n "$LEDGER" ] && [ -s "$LEDGER" ]; then
  declare -A _lrow=() _rbase=()
  while IFS= read -r _line || [ -n "$_line" ]; do
    _n=${_line%%$'\t'*}
    [ -n "$_n" ] && [ "$_n" != "$_line" ] && [ -z "${_lrow[$_n]+x}" ] && _lrow[$_n]=$_line
  done < "$LEDGER"
  _anc_yes=" "; _anc_no=" "
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.rc" ] && continue                 # already decided by the guard pass
    # An IMPURE leg is never reused, on any tree, however identical. Its verdict is a function of
    # something outside the tree, so a byte-identical tree is not the same question twice. The
    # declaration is the manifest's legacy `impure`, which the cache block above refuses the same way,
    # and a `remote` leg with no observed remote is refused for the cache block's reason (S9 of -13).
    _cls=",${legreads[$i]},"
    case $_cls in *,impure,*) continue ;; *,remote,*) [ -n "$REMOTE_OBS" ] || continue ;; esac
    _row=${_lrow[${names[$i]}]-}
    [ -n "$_row" ] || continue
    _sec=; _st=; _key=; _end=; _run=; _full=; _blob=; _head=
    # The row was found BY its name field, so no name check follows: it could never fail.
    IFS=$'\x1f' read -r _n _sec _st _key _end _run _full _blob _head _ <<<"${_row//$'\t'/$'\x1f'}"
    [ "$_st" = ok ] || continue                     # a RED row is never reusable
    [ -n "$_key" ] && [ "$_key" != "-" ] || continue # no key recorded is not a match, it is a gap
    [ "$_full" = 1 ] && [ -n "$_blob" ] && [ "$_blob" = "$MANIFEST_BLOB" ] || continue
    # The run id names a path, so it is shape-checked first; one outside the shape is not refused,
    # it only loses the shortcut. `?` memoizes "no header", `=<base>` the base it recorded.
    case $_run in
      ''|*[!A-Za-z0-9TZ-]*) ;;
      *)
        if [ -z "${_rbase[$_run]+x}" ]; then
          _rbase[$_run]='?'
          if [ -f "$RUNROOT/$_run/header" ]; then
            while IFS=$'\t' read -r _hk _hv; do
              [ "$_hk" = base ] && { _rbase[$_run]="=$_hv"; break; }
            done < "$RUNROOT/$_run/header"
          fi
        fi
        case ${_rbase[$_run]} in '?'|"=$BASE") ;; *) continue ;; esac ;;
    esac
    case $_head in ''|*[!0-9a-f]*) continue ;; esac
    case $_anc_no in *" $_head "*) continue ;; esac
    case $_anc_yes in
      *" $_head "*) ;;
      *) if git merge-base --is-ancestor "$_head" HEAD 2>/dev/null; then _anc_yes="$_anc_yes$_head "
         else _anc_no="$_anc_no$_head "; continue; fi ;;
    esac
    [ "$_key" = "${INPUT_KEYS[$i]:--}" ] || continue
    printf 'reuse' > "$WORK/$i.rc"
    lineage_reuses=$((lineage_reuses+1))
  done
  unset _lrow _rbase _cls
fi

# ---- CALIBRATION: THE SPAWN FLOOR. TOOL-dDerivedDocket-26 S5 ---------------------------------------
# A leg killed by its ceiling on a loaded host reads FAIL exactly as a real hang does. The serial
# retry below answers most of that; what is left is a leg that times out AGAIN, alone, and whether that
# is about the subject or the host is a question only a measurement can answer. The measurement is the
# cost of ONE process creation, judged against the lowest this CLONE has recorded and never against a
# wall clock or another node: node `a` pays about 251 ms a process where node `d` pays 19-39, so an
# absolute figure would call one node permanently degraded (the process-creation gotcha).
#
# THE FLOOR IS READ BEFORE THIS BAR MEASURES, and the retry compares against that reading, so a bar
# never calibrates against itself and a clone's first bar cannot read HOST (the spec's F4). The start
# measurement is then folded in, the lower figure kept, tmp-then-rename so no reader sees half a
# line. A bar with no live-bounded leg to run measures nothing: none of its legs can be deferred, and
# ten spawns on every nested suite bar would buy a floor that bar can never read.
#
# THREE ARM SEAMS, none a conf key, each read once and then UNSET so no leg's nested runner inherits
# one, exactly as `GATE_RUN_ID` is: `GATE_SPAWN_CMD` names what is timed, `GATE_SPAWN_FLOOR` names the
# floor file, and `GATE_VERDICT_FAULT` makes the verdict write fail, the only way to reach the refusal
# at the foot of this file. `GATE_HOST_RATIO` is a SOURCE CONSTANT: 4 is twice the 2x spread measured
# on one node, the one value a recorded measurement supports (the spec's F1).
#
# WHAT THIS DOES NOT CHECK: that a high figure is caused by another tenant and not by something this
# bar left running. The retry pass asserts the timed-out attempts' processes are gone before it
# measures and says so when they are not, but a descendant that left its leg's process group is
# invisible to that assertion, as `remove_group_residue` states.
GATE_HOST_RATIO=4
SPAWN_CMD=${GATE_SPAWN_CMD:-}; SPAWN_FLOOR_FILE=${GATE_SPAWN_FLOOR:-}; VERDICT_FAULT=${GATE_VERDICT_FAULT:-}
# A FOURTH SEAM, TOOL-aSparedSpawn-2: `GATE_SPAWN_NOW` names a file the spawn pause reads in place of
# the census sampler's reading, as `GATE_MEMINFO` stands in for `/proc/meminfo`.
SPAWN_NOW_SEAM=${GATE_SPAWN_NOW:-}
unset GATE_SPAWN_CMD GATE_SPAWN_FLOOR GATE_VERDICT_FAULT GATE_SPAWN_NOW
[ -n "$SPAWN_FLOOR_FILE" ] || { [ -n "$WORK_COMMON" ] && SPAWN_FLOOR_FILE="$WORK_COMMON/gate-spawn-floor"; }
SPAWN_FLOOR_US=""; SPAWN_FLOOR_STATE=absent; SPAWN_US=""

# read_spawn_floor <path> — SPAWN_FLOOR_US, the recorded cost of one spawn in microseconds, and
# SPAWN_FLOOR_STATE: `read`, `absent`, or `unreadable` for anything but one well-formed
# `<ms>.<3 digits>` line in a regular file. A zero is unreadable and never a floor, since every
# measurement would exceed it and every double timeout would read HOST.
read_spawn_floor() {
  local f=$1 line="" ms whole frac
  SPAWN_FLOOR_US=""; SPAWN_FLOOR_STATE=absent
  [ -n "$f" ] && [ -e "$f" ] || return 0
  SPAWN_FLOOR_STATE=unreadable
  [ -f "$f" ] || return 0
  { IFS= read -r line < "$f"; } 2>/dev/null || [ -n "$line" ] || return 0
  line=${line%$'\r'}; ms=${line%%$'\t'*}
  case "$ms" in *.*) whole=${ms%%.*}; frac=${ms#*.} ;; *) whole=$ms; frac=000 ;; esac
  case "$whole" in ''|*[!0-9]*) return 0 ;; esac
  case "$frac" in [0-9][0-9][0-9]) ;; *) return 0 ;; esac
  [ "${#whole}" -le 9 ] || return 0
  SPAWN_FLOOR_US=$(( 10#$whole * 1000 + 10#$frac ))
  if [ "$SPAWN_FLOOR_US" -le 0 ]; then SPAWN_FLOOR_US=""; return 0; fi
  SPAWN_FLOOR_STATE=read
}

# measure_spawn_cost — SPAWN_US, the mean microseconds of one spawn over ten, or empty when a spawn
# failed, bash has no `EPOCHREALTIME`, or the clock did not move: a failed spawn measures nothing, a
# builtin clock is the only one that does not spawn a process of its own inside the measurement, and
# a zero is NEVER rounded up to a figure. A floor fabricated at one microsecond would read every later
# double timeout as HOST, which is the fallback-fabricates-the-passing-value class pointed at the host.
# An optional count replaces the ten: the census sampler times three a tick for the spawn pause.
measure_spawn_cost() {
  local -a cmd=()
  local t0 t1 k reps=${1:-10}
  SPAWN_US=""
  if [ -n "$SPAWN_CMD" ]; then read -ra cmd <<<"$SPAWN_CMD"; else cmd=("$(type -P true 2>/dev/null)"); fi
  [ -n "${cmd[0]:-}" ] || return 0
  t0=${EPOCHREALTIME:-}; t0=${t0//[.,]/}
  [ -n "$t0" ] || return 0
  for ((k=0; k<reps; k++)); do
    "${cmd[@]}" </dev/null >/dev/null 2>&1 || return 0
  done
  t1=${EPOCHREALTIME//[.,]/}
  SPAWN_US=$(( (10#$t1 - 10#$t0) / reps ))
  [ "$SPAWN_US" -gt 0 ] || SPAWN_US=""
}

# write_spawn_floor <path> <microseconds> — the floor file holds the lower of its reading and this
# figure. A path that exists and is not a regular file is left alone, and a write that fails leaves
# the old line in force; each says so on stderr.
write_spawn_floor() {
  local f=$1 us=$2 _tp
  [ -n "$f" ] && [ -n "$us" ] || return 0
  [ -n "$SPAWN_FLOOR_US" ] && [ "$SPAWN_FLOOR_US" -le "$us" ] && return 0
  if [ -e "$f" ] && [ ! -f "$f" ]; then
    echo "run-gates: the spawn floor at $f is not a regular file, so this bar's measurement is not recorded there" >&2
    return 0
  fi
  derive_temp_path _tp "$f"
  if { printf '%d.%03d\t%s\n' "$(( us / 1000 ))" "$(( us % 1000 ))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$_tp"; } 2>/dev/null \
     && mv -f "$_tp" "$f" 2>/dev/null; then
    return 0
  fi
  [ -f "$_tp" ] && rm -f "$_tp" 2>/dev/null
  echo "run-gates: the spawn floor at $f could not be written, so the floor it held stays in force" >&2
  return 0
}

read_spawn_floor "$SPAWN_FLOOR_FILE"
[ "$SPAWN_FLOOR_STATE" = unreadable ] \
  && echo "run-gates: the spawn floor at $SPAWN_FLOOR_FILE cannot be read, so it is treated as absent and no leg of this bar can read HOST" >&2
# THE SPAWN PAUSE'S INPUTS (TOOL-aSparedSpawn-2), the floor as read BEFORE this bar measures, for the
# reason the retry gives. With no floor the ratio multiplies nothing: the knob is INERT, says so
# here once, and never reads as a threshold of zero, which would hold every decision, or of infinity.
SPAWNPAUSE_FLOOR=$SPAWN_FLOOR_US
SPAWNPAUSE_NOW=${SPAWN_NOW_SEAM:-$WORK/spawn-now}
if [ "$SPAWNPAUSE" -gt 0 ] && [ -z "$SPAWNPAUSE_FLOOR" ]; then
  echo "run-gates: NOTE - profile '$PROF_NAME' asks to hold dispatch while one spawn costs over ${SPAWNPAUSE}x the spawn floor, but no floor is recorded at ${SPAWN_FLOOR_FILE:-<no common dir>}, so the spawn pause is INERT this run" >&2
fi
_sf_bounded=0
if [ "$CEILINGS_LIVE" = 1 ]; then
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.rc" ] && continue          # held, skipped or reused: it will not run, so it cannot time out
    if [ -n "${ceilings[$i]:-}" ] || [ "${PROF_TIMEOUT:-0}" -gt 0 ]; then _sf_bounded=1; break; fi
  done
fi
if [ "$_sf_bounded" = 1 ]; then
  measure_spawn_cost
  [ -n "$SPAWN_US" ] \
    || echo "run-gates: the spawn cost could not be measured, so this bar adds nothing to the floor at ${SPAWN_FLOOR_FILE:-<no common dir>}" >&2
  write_spawn_floor "$SPAWN_FLOOR_FILE" "$SPAWN_US"
fi
unset _sf_bounded

runleg() { # leg index · attempt suffix — writes .out, then .sec, then ATOMICALLY .rc (the completion signal)
  # The suffix is empty on a leg's first attempt and `.retry` on its serial retry (TOOL-dDerivedDocket-26
  # S2), so every file a retry writes sits BESIDE the first attempt's and the red attribution still
  # reads that first attempt exactly as it was written.
  local i=$1 sfx=${2:-} s e out rc tpid="" FOREIGN=unknown _tp
  local -a chunks_out=()
  # THE WALL'S HANDLE ON THIS LEG. `$BASHPID`, never `$$`: inside a backgrounded function `$$` is
  # still the RUNNER's pid, and a wall that killed that would kill the shell that has to print the
  # verdict. Written before anything else so a leg that wedges on its first line is still reachable.
  printf '%s' "$BASHPID" > "$WORK/$i$sfx.pid" 2>/dev/null || true
  local argv; IFS=$'\x1f' read -ra argv <<<"${argvs[$i]}"
  case "${argv[0]}" in python|python3) argv[0]=$PYBIN ;; esac   # the manifest stores the canonical python3; run under the resolved PYBIN
  # THE CLOCK IS A BUILTIN (TOOL-aSparedSpawn-4 S1): `EPOCHREALTIME` in nanoseconds, its separator
  # stripped, and the date builtin's whole seconds only where the shell has none, so a leg's seconds
  # field degrades to whole seconds there rather than to zero.
  if [ -n "${EPOCHREALTIME:-}" ]; then s=${EPOCHREALTIME/[.,]/}000; else printf -v s '%(%s)T000000000' -1; fi
  # legs never read stdin — deny it so a stray reader can't hang the bar. The profile's per-leg
  # timeout wraps the exec when the selected row asks for one: a leg that outlives it exits 124 and
  # is reported RED naming itself, never skipped and never green. That is a COVERAGE improvement, not
  # a carve-out — an unbounded hang wedges the whole bar and names nothing.
  #
  # CAPTURED THROUGH A FILE, NOT A PIPE, and that is the whole difference between a bound and a
  # decoration. `out=$(timeout N cmd)` reads until EOF, and EOF arrives only when the LAST inherited
  # write end closes — so a surviving grandchild holds the pipe and the worker blocks for the entire
  # hang while `timeout` cheerfully reports 124. MEASURED on the first landing of this knob: 51.4 s
  # wall against a 1 s bound, indistinguishable from the same fixture with the timeout off. The
  # verdict was bounded and the clock was not, which is the one property the knob exists for.
  # `-k` follows for the child that ignores SIGTERM; the file read cannot block on anybody.
  # THE LEG'S OWN CEILING WINS, and the two bounds NEVER wrap one leg together: nested deadlines
  # both exit 124 and the verdict cannot then say which fired. `PROF_TIMEOUT` stays the fallback for
  # a leg that declares none, which is every leg in a manifest the deployer has not yet taught the
  # key. `bound` is also what report_one reads, so the number in the verdict is the number that
  # fired rather than a second lookup that could disagree with it. TOOL-aBoundedCeiling-1.
  local bound=${ceilings[$i]:-}
  [ -n "$bound" ] || bound=$PROF_TIMEOUT
  # CEILINGS_LIVE is the liveness gate: with no runnable `timeout` a declared ceiling is INERT, and
  # the leg runs UNBOUNDED rather than being skipped. A knob may cost speed and may turn a hang into
  # a RED; it may never turn a leg into a pass or a skip (gate-profiles.txt, the governing invariant).
  [ "$CEILINGS_LIVE" = 1 ] || bound=0
  printf '%s' "$bound" > "$WORK/$i$sfx.bound"
  # `timeout` RUNS IN THE BACKGROUND AND IS WAITED ON, so this worker holds its pid (TOOL-dDerivedDocket-26
  # F5). That pid is the id of the process group `timeout` made for the leg, and it is the only handle
  # left on a descendant once the ceiling has fired: see `scan_group`. The verdict and the clock are
  # unchanged, since `wait` returns `timeout`'s own status and the capture is still through a file.
  # The `wait`'s own `2>/dev/null` is the SHELL's: a `timeout` that dies by SIGKILL makes bash print a
  # `Killed` job notice naming this file's line, and the verdict line already says it, as `run_leg_at`
  # below states for the same notice. The leg's own stderr is in the capture file either way.
  if [ "${bound:-0}" -gt 0 ]; then
    timeout -k 5s "$bound" "${argv[@]}" </dev/null >"$WORK/$i$sfx.raw" 2>&1 &
    tpid=$!
    printf '%s' "$tpid" > "$WORK/$i$sfx.tpid" 2>/dev/null || true
    wait "$tpid" 2>/dev/null; rc=$?
  else "${argv[@]}" </dev/null >"$WORK/$i$sfx.raw" 2>&1; rc=$?; fi
  # THE OUTPUT, READ BY BUILTINS (TOOL-aSparedSpawn-4 S2), byte for byte what `$(cat …)` captured:
  # `mapfile -d ''` splits at each NUL, which a bash string cannot hold and the capture dropped too,
  # the chunks are joined, and the trailing newlines the capture stripped are stripped. An absent file
  # reads empty, as `cat` did. Output that then ENDS in a CR is the one case the hosts disagree on: the
  # MSYS substitution strips a trailing CRLF as one newline, Linux keeps the CR. So that output, and
  # only that, is read by the substitution itself, which gives each host its own bytes.
  { mapfile -d '' chunks_out < "$WORK/$i$sfx.raw"; } 2>/dev/null
  printf -v out '%s' ${chunks_out[@]+"${chunks_out[@]}"}
  while [[ $out == *$'\n' ]]; do out=${out%$'\n'}; done
  [[ $out == *$'\r' ]] && out=$(< "$WORK/$i$sfx.raw")   # there to read: mapfile just read it
  # THE MASK IS SET HERE, ONCE, in this worker and only after the leg has exited, so the leg never
  # inherits it: every file below is created owner-only, which is what the two `chmod 600` gave.
  umask 077
  if [ -n "${EPOCHREALTIME:-}" ]; then e=${EPOCHREALTIME/[.,]/}000; else printf -v e '%(%s)T000000000' -1; fi
  local secs; printf -v secs '%s.%03d' "$(( (e-s)/1000000000 ))" "$(( ((e-s)/1000000)%1000 ))"
  # THE REAP, IN THE WORKER AND BEFORE ITS COMPLETION SIGNAL (TOOL-dDerivedDocket-26 F5). Whatever the
  # timed-out leg left in its group is killed here, so by the time `.rc` exists the attempt's residue
  # is gone and the serial retry and its spawn measurement run beside nothing of this attempt's. It is
  # keyed on the GROUP: the worker is not in it, so this cannot take the worker down before `.sec` and
  # `.rc`, which a walk rooted at `$BASHPID` would. Only a FIRED ceiling reaps; a leg that ends on its
  # own leaves nothing `timeout` did not already wait for, and a scan per leg would cost a `ps` each.
  local fired=0
  if [ -n "$tpid" ] && check_ceiling_fired "$rc" "$bound" "$secs"; then
    fired=1
    remove_group_residue "$tpid" >/dev/null
  fi
  # TOOL-dNomadicAtlas-1, ported into the worker: persist EVERY leg, not only the failing one — a
  # passing leg's output is what a later bisect reads, and the bytes are already in memory. Redacted,
  # because a terminal line is ephemeral and a file is not.
  local lf="" logged
  leg_log "${names[$i]}" && lf=$LEG_LOG
  printf -v logged '# run-gates | leg %s | exit %s\n%s\n' "${names[$i]}" "$rc" "$out"
  # NOT FOR THE SAMPLE'S SECOND LOOK (TOOL-aSparedSpawn-16 S16): the `log:` pointer `FAILED_LEGS` already
  # carries names this file, and it must keep naming the attempt that redded the run. The look's own
  # output stays in the run directory below.
  if [ -n "$lf" ] && [ "$sfx" != .sample ]; then
    { write_redacted "$lf" "$logged"; } 2>/dev/null || true
  fi
  printf '%s\n' "$out" > "$WORK/$i$sfx.out"
  printf '%s\n' "$secs" > "$WORK/$i$sfx.sec"
  # THE DURABLE HALF. One TSV row per leg and one copy of its output, both inside the run
  # directory, and both written BEFORE the completion signal so a concurrent reader that sees
  # `.rc` sees a complete row rather than a half-written one.
  if [ -n "$RUNDIR" ]; then
    # The output copy takes the SAME redaction and the SAME restrictive mode its `gate-logs`
    # sibling already has. It is the same bytes with a longer life, and a durable copy that skips
    # the masking its sibling applies is a credential leak the old scratch-dir lifetime was
    # merely hiding.
    { write_redacted "$RUNDIR/$i$sfx.out" "$logged"; } 2>/dev/null || true
    local st; case "$rc" in 0) st=ok ;; *) st=fail ;; esac
    # `timeout` WHEN THE CEILING FIRED (TOOL-dDerivedDocket-26 S2), so a first attempt that is about to
    # be retried is never recorded as a failure, and a retry that timed out again says which kind it was.
    [ "$fired" = 1 ] && st=timeout
    # TAB-SEPARATED and NEWLINE-FREE by construction: every field is a leg name, a token, a
    # number or a digest. The leg name is the only one an author controls, and the canary
    # already forbids a tab inside one. The EIGHTH field is `foreign`, the census's verdict on this
    # attempt's window (TOOL-aGraftedHelix-5), appended so no positional reader moves.
    derive_foreign "$s" "$e"
    derive_temp_path _tp "$RUNDIR/$i$sfx.leg"
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "${names[$i]}" "$st" "$rc" "$secs" "$s" "$e" "${INPUT_KEYS[$i]:--}" "$FOREIGN" \
      > "$_tp" 2>/dev/null \
      && mv -f "$_tp" "$RUNDIR/$i$sfx.leg" 2>/dev/null || true
  fi
  # THE ONE HEARTBEAT SITE, and it is here rather than in the reader loop because this is the
  # event the TTL is sized against: S4 refreshes at a leg COMPLETING, so "can the holder still be
  # holding" and "has a leg finished lately" are the same question. A second site in the reader
  # loop would refresh while no leg was making progress, which is the state the reaper exists to
  # detect.
  ts_hb
  # THE TAIL MARKER (TOOL-aSparedSpawn-3 S1), before `.rc`: a FIRST attempt whose own ceiling fired,
  # by the predicate `report_one` defers on, read over the same rc, bound and seconds. Written here
  # because the worker knows at completion what the manifest-order reader may not reach until the
  # floor leg ends, and the tail where its retry can run exists only while the pool still runs.
  [ "$fired" = 1 ] && [ -z "$sfx" ] && : > "$WORK/$i.defer"
  derive_temp_path _tp "$WORK/$i$sfx.rc"
  printf '%s' "$rc" > "$_tp" && mv -f "$_tp" "$WORK/$i$sfx.rc"
}

# THE TAIL CONTRACT (the run-gates promotion spec's S5). Every tailed line is `<verb>  <leg name>  <tail>`:
# TWO spaces before the parenthesised tail, on every verb, so a reader splits the remainder on a
# double space and gets the bare leg name back. A single space made that split return a TRUNCATED
# name for any leg whose name contains a space, which is most of them, and the deployer reads a
# target's verdicts exactly that way. The canary forbids a double space INSIDE a leg NAME, which is
# what keeps the split unambiguous rather than merely usually right. Every verb the sibling units
# add conforms: two spaces before any parenthesised tail.
# derive_fail_tail <rc> <bound> <seconds> — a failed attempt's tail text, without its parentheses. ONE
# derivation for a leg's first attempt and for its serial retry (TOOL-dDerivedDocket-26), so the two
# lines a retried leg can print cannot disagree about what an exit status means.
#
# `timeout` exits 124 on the TERM, and 137 once `-k` escalates to KILL — which is exactly the leg the
# kill-after exists for, so mapping only 124 left the worst case reported as a bare exit code. 124
# stays behind the bound guard, so a leg that chooses it for its own reasons is still reported as the
# code it chose; 137 has no such case to protect, because bash reports 128+9 for a SIGKILLed child and
# a leg that "chose" 137 is indistinguishable from one killed.
#
# THE BOUND IS THE ONE THAT ACTUALLY FIRED, read by the caller from what runleg recorded rather than
# re-derived. The old spelling read `PROF_TIMEOUT` for both the guard and the number, so once a leg
# carried its own ceiling and PROF_TIMEOUT stayed 0 -- which is every shipped profile row -- a killed
# leg reported a bare `(exit 124)` naming nothing. TOOL-aBoundedCeiling-1.
#
# THE SECONDS ARE THE ONES THE LEG RAN, from `.sec`, which the ledger block reads as its field 2 too,
# so this is a third reader of one value and never a second source. Verbatim, decimals and all,
# because byte-equality with the ledger row is the property; a `?` when unreadable, because any
# numeric fallback would be a second wrong answer. TOOL-aLeakedHandle-3.
#
# 124 KEEPS THE CEILING DELIBERATELY, and the asymmetry with 137 is a decision rather than an
# oversight. rc=124 means `timeout` fired its own TERM, so the ceiling is the CAUSE of the verdict and
# true by construction, while the elapsed value on that path is the ceiling plus kill-path overhead --
# measured at 12 s against a 2 s bound under load, which would send a reader hunting for a bound
# nobody declared. rc=137 is the opposite case: SIGKILL says nothing about who sent it, and
# `timeout -k`, an operator, an OOM killer and a CI cancel all arrive here identically, so the verb
# states the kill and the two numbers stay apart.
#
# NO BOUND IN PLAY, and the leg was still killed: an operator, an OOM killer, a CI cancel, or any leg
# on a host with no runnable `timeout`. The guard is the positive-bound line NEGATED so the two
# PARTITION rc=137 and nothing falls between; there is no ceiling clause because the absence IS the
# information. TOOL-aLeakedHandle-9.
derive_fail_tail() {
  local rc=$1 fired=${2:-0} secs=${3:-} t
  case "$fired" in ''|*[!0-9]*) fired=0 ;; esac
  t="exit $rc"
  { [ "$rc" = 124 ] && [ "$fired" -gt 0 ]; } && t="timed out after ${fired}s"
  { [ "$rc" = 137 ] && [ "$fired" -gt 0 ]; } && t="killed after ${secs:-?}s, ceiling ${fired}s"
  { [ "$rc" = 137 ] && ! [ "$fired" -gt 0 ]; } && t="killed after ${secs:-?}s"
  printf '%s' "$t"
}

report_one() { # leg index — emits exactly the line the serial bar has always emitted
  local i=$1 rc ftail rtail=""
  n=$((n+1))
  # THE REUSE MARKERS ON THE LEG'S OWN LINE (TOOL-aSparedSpawn-16 S17), under the two-space tail
  # contract: a leg the sample drew, or one the age bound forced, executed for a reason the line used to
  # leave to a stderr note. `-f` is a builtin test, so the read spawns nothing.
  if [ -f "$WORK/$i.sampled" ]; then rtail="  (sampled against a cached ok)"
  elif [ -f "$WORK/$i.aged" ]; then rtail="  (executed: reused on 10 runs in a row)"; fi
  if [ ! -f "$WORK/$i.rc" ]; then
    RED_LEGS="$RED_LEGS $i"
    fails=$((fails+1)); c_ran=$((c_ran+1)); c_fail=$((c_fail+1)); printf 'GATE FAIL  %s  (no result)\n' "${names[$i]}"
    FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]}  (no result)"$'\n'; return
  fi
  # Read by the builtin (TOOL-aSparedSpawn-4 S6): every one of these files holds one line, so `read`
  # answers what `$(cat …)` did without a fork, and a missing file leaves the default in place.
  rc=""; { IFS= read -r rc < "$WORK/$i.rc"; } 2>/dev/null
  if [ "$rc" = ondemand ]; then
    # THE FIFTH VERB, and it is NOT `skip`. Two reasons, both load-bearing. `skip`'s tail says
    # `unchanged vs <branch>`, which is false here — the leg is not unchanged, it is out of subject —
    # and `skips` is conjoined into the `gate-full-green` stamp, so counting an on-demand skip there
    # would silence the stamp and pin `.githooks/pre-push` into forcing a full run forever.
    ondemands=$((ondemands+1)); c_ondemand=$((c_ondemand+1))
    local since=""
    { IFS= read -r since < "$WORK/$i.unchanged"; } 2>/dev/null
    if [ -n "$since" ]; then printf 'GATE held  %s  (self-test, unchanged since %s)\n' "${names[$i]}" "$since"
    else printf 'GATE held  %s  (self-test, set GATE_SELFTESTS=1 to run)\n' "${names[$i]}"; fi
  elif [ "$rc" = skip ]; then
    skips=$((skips+1)); c_skip=$((c_skip+1)); printf 'GATE skip  %s  (unchanged vs %s)\n' "${names[$i]}" "${DEFBR:-baseline}"
  elif [ "$rc" = docskip ]; then
    # A SKIP, counted as one: `skips` is conjoined into the full-green stamp, so a docs run can never
    # stamp a green it did not earn. Its tail names the mode, because `unchanged vs <branch>` would be
    # a claim about the guard this leg was NOT decided by.
    skips=$((skips+1)); c_skip=$((c_skip+1)); printf 'GATE skip  %s  (docs-only: no path it reads moved)\n' "${names[$i]}"
  elif [ "$rc" = reuse ]; then
    # THE FOURTH VERB, padded to the same column as the other three and following the two-space tail
    # contract: a reader splits the remainder on a double space and gets the bare leg name back.
    reuses=$((reuses+1)); c_reuse=$((c_reuse+1)); printf 'GATE reuse %s  (proven green, inputs unchanged)\n' "${names[$i]}"
  elif [ "$rc" = 0 ]; then c_ran=$((c_ran+1)); printf 'GATE ok    %s%s\n' "${names[$i]}" "$rtail"
  else c_ran=$((c_ran+1))
       local fired=0 secs=""
       { IFS= read -r fired < "$WORK/$i.bound"; } 2>/dev/null
       { IFS= read -r secs < "$WORK/$i.sec"; } 2>/dev/null
       # THE SERIAL RETRY'S DEFERRAL (TOOL-dDerivedDocket-26 S1). A leg whose OWN ceiling fired is not
       # failed here: a bar under its own concurrency kills a leg at 5400 s that ran in 267 s alone
       # (TOOL-aSurfacedLexicon-22), so the first timeout is not yet a finding. It is DEFERRED, printed
       # in its manifest position with the neighbours that were running beside it, and run once more
       # alone after the pool drains. The predicate is `check_ceiling_fired`, the one the red
       # attribution reads CONTENDED by: 124 under a positive bound, or 137 under a positive bound
       # whose seconds reached it. Every other 137 -- a self-kill, an OOM kill, an operator's or a CI
       # cancel, under a bound or with none -- is a failure now, exactly as it always was.
       # The worker applied the same predicate when the attempt ended and left a `.defer` marker, so
       # the retry may already have run in the pool's tail (TOOL-aSparedSpawn-3); the tail says both.
       if check_ceiling_fired "$rc" "$fired" "$secs"; then
         c_defer=$((c_defer+1)); DEFERRED="$DEFERRED $i"
         printf "GATE retry  %s  (timed out after %ss beside %s neighbours; retried in the pool's tail, and alone after it drains unless that passes)\n" \
           "${names[$i]}" "$fired" "$(measure_neighbours "$i")"
         return
       fi
       fails=$((fails+1)); c_fail=$((c_fail+1)); RED_LEGS="$RED_LEGS $i"
       ftail="($(derive_fail_tail "$rc" "$fired" "$secs"))"
       printf 'GATE FAIL  %s  %s%s\n' "${names[$i]}" "$ftail" "${rtail# }"; sed 's/^/    /' "$WORK/$i.out"
       FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]}  $ftail"$'\n'   # TOOL-aLeasedGauntlet-1 S3: keep for the durable summary
       # TOOL-dNomadicAtlas-1: a POINTER at the leg's own output, so the durable summary answers WHY
       # and not only WHICH. A pointer, never the bytes — this file is what an operator quotes.
       leg_log "${names[$i]}" && lf=$LEG_LOG && [ -n "$lf" ] && FAILED_LEGS="${FAILED_LEGS}    log: $lf"$'\n'; fi
}

# Dispatch and report from ONE shell, so this shell owns every worker and can BLOCK on `wait -n`
# rather than poll for results. That is not a style preference: a poll tick costs a `sleep` PROCESS,
# measured at ~75ms for a 50ms sleep on this platform, and an earlier revision that polled every 50ms
# spent ~317s of a 617s serial run doing nothing but spawning them.
# Dispatch order is the advisory longest-first hint; REPORTING walks the manifest, so a leg prints
# only once every leg before it has printed.
# ---- CHUNKS BOUND REPORTING, NEVER DISPATCH (the chunking unit) --------------------------------
# The bar is FLOOR-bound: one leg is most of the wall clock, so no ordering of the other eighty-odd
# moves it. Reordering dispatch was specced and then CUT on that measurement, and what survives is
# the half the measurement supports — a reviewable verdict per chunk instead of one verdict at the
# end, on a bar where the first line used to appear minutes in.
#
# So legs run at full pool width in whatever order the longest-first hint gives, across chunk lines
# freely. Only the READER'S walk changes: from the raw index range to a flattened chunk-then-manifest
# list. Chunk ORDER is order of FIRST APPEARANCE in the manifest — no second declaration file, no
# order field, and a leg with no key falls into `default`.
#
# The manifest is deliberately NOT grouped, so this flattening is a real permutation rather than an
# identity. That is what makes the grouping observable at all, and it is why the whole-manifest
# reorder could be cut without costing this unit anything.
CHUNK_ORDER=""
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  case " $CHUNK_ORDER " in *" ${chunks[$i]} "*) ;; *) CHUNK_ORDER="$CHUNK_ORDER ${chunks[$i]}" ;; esac
done
WALK=()
for c in $CHUNK_ORDER; do
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ "${chunks[$i]}" = "$c" ] && WALK+=("$i")
  done
done
nwalk=${#WALK[@]}

disp=($ORDER); ndisp=${#disp[@]}; di=0; wi=0; next=0
[ "$nwalk" -gt 0 ] && next=${WALK[0]}
# per-chunk tallies, reset at each boundary
cur_chunk=""; c_ran=0; c_fail=0; c_skip=0; c_reuse=0; c_ondemand=0; c_defer=0; c_t0=$EPOCHSECONDS
CHUNK_ROLLUP=""
chunk_close() {   # emit the verdict for the chunk just finished
  [ -n "$cur_chunk" ] || return 0
  local secs=$(( $EPOCHSECONDS - c_t0 )) verdict
  if   [ "$c_fail" -gt 0 ]; then verdict="RED"
  # A CHUNK HOLDING A DEFERRED LEG IS `pending`, NEVER `green` (TOOL-dDerivedDocket-26 S2). Its leg has
  # not passed: it timed out once and waits for its serial retry, whose verdict the `---- retry:` line
  # after the pool drains carries. RED still outranks it, because a leg that failed outright is a
  # finding whatever the retry does.
  elif [ "${c_defer:-0}" -gt 0 ]; then verdict="pending"
  # A CHUNK IN WHICH EVERY LEG WAS SKIPPED REPORTS AS SKIPPED, never as green. On a scoped run the
  # guard pre-pass decides those legs before dispatch, so the chunk closes at once — and calling that
  # green would be the loudest possible green-by-absence, one altitude above a single leg.
  # A HELD LEG IS A LEG THAT DID NOT RUN, so it satisfies this rule exactly as a guard-skip does.
  # The rule above was already correct and already stated; what it lacked was reachability from the
  # newer skip kind, which is worse than a missing rule because the comment asserts it. A chunk of
  # nothing but kit self-tests closed GREEN on every switch-off bar. TOOL-dUnstalledConvoy-32.
  # A CHUNK THE WALL EMPTIED IS `killed`, NEVER `green`. A killed leg writes no `.rc`, so it
  # increments none of the five counters below and the chunk fell straight through to the `else`.
  # Observed: `---- chunk product: green  (0 ran, 0 failed, 0 skipped, 0 reused, 0 held)` over a
  # chunk whose every leg the wall had just SIGKILLed. This is TOOL-dUnstalledConvoy-32's rule --
  # the one the comment above already states for held legs -- reaching the newer kind of
  # did-not-run, which is exactly the reachability failure that row records.
  elif [ -f "$WORK/wall.breach" ] && [ "$c_ran" = 0 ] && [ "$c_fail" = 0 ]; then verdict="killed"
  elif [ "$c_ran" = 0 ] && [ "$c_reuse" = 0 ] && { [ "$c_skip" -gt 0 ] || [ "${c_ondemand:-0}" -gt 0 ]; }; then verdict="skipped"
  else verdict="green"; fi
  # HELD IS ITS OWN TALLY and not folded into `skipped`, for the reason the leg verb is its own verb:
  # the two have different remedies. A guard-skip runs again when its path moves; a held leg runs
  # when somebody sets the variable, and a reader who cannot tell them apart waits for the wrong one.
  printf -- '---- chunk %s: %s  (%s ran, %s failed, %s skipped, %s reused, %s held)\n' \
    "$cur_chunk" "$verdict" "$c_ran" "$c_fail" "$c_skip" "$c_reuse" "${c_ondemand:-0}"
  # PER-CHUNK WALL TIME goes to the durable records and NOT to stdout: a wall clock on a terminal
  # line invites comparison between runs that are not comparable, which is the whole reason the
  # profiling verb records an envelope.
  CHUNK_ROLLUP="${CHUNK_ROLLUP}chunk\t${cur_chunk}\t${verdict}\t${c_ran}\t${c_fail}\t${c_skip}\t${c_reuse}\t${c_ondemand:-0}\t${secs}\n"
  cur_chunk=""; c_ran=0; c_fail=0; c_skip=0; c_reuse=0; c_ondemand=0; c_defer=0; c_t0=$EPOCHSECONDS
}
# S2. ARMED AT THE FIRST DISPATCH AND NOT AT PROCESS START. Everything above this point -- the
# turnstile wait most of all -- is a bar waiting for its turn rather than a bar running, and a wall
# that counted the queue would kill a run for being polite. The queue has its own bound, TS_MAXWAIT.
#
# THE WATCHER KILLS; it does not merely mark. The reader blocks on `wait -n`, so a marker alone would
# never be read: the whole point is that every leg is wedged. Killing the outstanding legs is what
# returns the reader to a state where it can see the marker and render a verdict.
#
# DETACHED, for the reason `ts_tick_start` above is: this shell owns the pool and counts its own jobs.
arm_wall() {
  [ "$WALL" -gt 0 ] || return 0
  [ "$WALL_ARMED" = 0 ] || return 0
  WALL_ARMED=1
  # THE DEADLINE, KEPT IN THIS SHELL TOO, so the red attribution can say how much of the wall its
  # own bound would need. The watcher below computes the same instant for itself.
  WALL_END=$(( EPOCHSECONDS + WALL ))
  local _w=$WALL _work=$WORK _me=$$
  (
    # A DEADLINE, NOT A COUNTER. The first cut slept 1 second `$WALL` times, and `sleep` is external:
    # measured on this box, 20 nominal seconds took 32.9 s and 30 took 58.0 s -- a 1.65x to 1.93x
    # drift, entirely spawn cost, which made `wall=10800` fire somewhere between 4h56m and 5h48m
    # while the profile line printed 3h. A knob whose declared value is not its delivered value is
    # worse than no knob. `EPOCHSECONDS` is a bash builtin and costs nothing; the 30 s poll cuts the
    # watcher from ~0.64 spawns per elapsed second of the bar to ~0.033.
    # THE POLL SCALES WITH THE WALL, so the spawn count is bounded at about ten per run whatever the
    # wall is, and the overshoot stays proportional instead of absolute. A flat 30 s poll made an 8 s
    # fixture wall fire at 30 s -- 375% over -- while a flat 1 s poll cost 10800 spawns on the shipped
    # 3-hour row. Tenth-of-the-wall, floored at 1 s and capped at 30 s, is both: 8 spawns for the
    # fixture, 360 across three hours for the shipped value.
    _poll=$(( _w / 10 )); [ "$_poll" -ge 1 ] || _poll=1; [ "$_poll" -le 30 ] || _poll=30
    _end=$(( EPOCHSECONDS + _w ))
    while [ "$EPOCHSECONDS" -lt "$_end" ]; do
      sleep "$_poll"
      kill -0 "$_me" 2>/dev/null || exit 0
      [ -f "$_work/wall.disarm" ] && exit 0
    done
    # BREACHED. THE MARKER IS WRITTEN FIRST, BEFORE A SINGLE KILL, and the order is the whole
    # correctness of the breach path. Written last -- as it was -- the kill loop runs a
    # `remove_descendants` per stuck leg, seconds to tens of seconds wide, during which the reader loop
    # is free to report the killed legs and dispatch fresh ones. Measured with the marker last: an
    # 8 s wall, two wedged legs, and a THIRD leg started 57 s after the breach and ran to completion,
    # 149 s against an 8 s bound. Writing the marker first also collapses the race that decided
    # whether the durable run record said RED or GREEN.
    printf '%s' "$EPOCHSECONDS" > "$_work/wall.breach" 2>/dev/null || true
    for _f in "$_work"/*.pid; do
      [ -e "$_f" ] || continue
      _i=${_f##*/}; _i=${_i%.pid}
      [ -f "$_work/$_i.rc" ] && continue
      _p=$(cat "$_f" 2>/dev/null) || continue
      [ -n "$_p" ] && run_leg_reap "$_p"
    done
  ) &
  WALL_PID=$!
  disown "$WALL_PID" 2>/dev/null || true
}

remove_wall_watcher() {
  [ "$WALL_ARMED" = 1 ] || return 0
  : > "$WORK/wall.disarm" 2>/dev/null || true
  [ -n "$WALL_PID" ] && kill "$WALL_PID" 2>/dev/null
  WALL_PID=""; WALL_ARMED=0
}

# ---- THE CENSUS'S FOUR FUNCTIONS. TOOL-aGraftedHelix-5; what the census counts is stated where its
# ---- tokens are derived, above the run header.
#
# measure_foreign — ONE census line on stdout, in ONE write: the epoch second, TAB, the count of
# foreign gate-work trees or `unknown`, TAB, each tree's root as <pid>:<token>, space-separated. A root
# is written as its pid and the token that matched it, NEVER its command line, which can carry a
# credential. `unknown` when `ps` fails, when its header names no PID or PPID column, or when the
# snapshot holds no row for this runner: a snapshot that cannot see its observer is not a census of
# the observer's host. The columns are found by the header's own names, so procps and MSYS `ps -ef`
# both parse, and the WHOLE row is matched, because a start time printed with a space shifts every
# later column. `$$` is the RUNNER's pid in the detached sampler too, which is the point. Two spawns.
measure_foreign() {
  local snap ts=$EPOCHSECONDS
  if [ -z "${CENSUS_TOKENS:-}" ] || ! snap=$(ps -ef 2>/dev/null); then
    printf '%s\tunknown\t\n' "$ts"; return 0
  fi
  awk -v me="$$" -v ts="$ts" '
    FILENAME == ARGV[1] { if ($0 != "") tok[++nt] = $0; next }
    !hdr { hdr = 1; for (k = 1; k <= NF; k++) { if ($k == "PID") pc = k; if ($k == "PPID") qc = k }; next }
    # A PID or PPID that is not a number continues a multi-line argv, the guard scan_descendants wears.
    !pc || !qc || $pc !~ /^[0-9]+$/ || $qc !~ /^[0-9]+$/ { next }
    { p = $pc; par[p] = $qc
      for (i = 1; i <= nt; i++) if (index($0, tok[i])) { hit[p] = tok[i]; next }
      for (k = 1; k <= NF; k++) if ($k ~ /\.test\.sh$/ || $k ~ /selftest\.py$/) { hit[p] = $k; next } }
    END {
      if (!pc || !qc || !(me in par)) { printf "%s\tunknown\t\n", ts; exit }
      for (a = me; (a in par) && !(a in ex); a = par[a]) ex[a] = 1      # the ancestors, this runner included
      for (p in hit) {
        if (p in ex) continue
        d = 0; b = p
        while ((b in par) && b != me && d < 256) { b = par[b]; d++ }
        if (b != me) cand[p] = 1                                           # a descendant reaches this runner
      }
      for (p in cand) if (!(par[p] in cand)) { n++; r = r (r == "" ? "" : " ") p ":" hit[p] }
      printf "%s\t%d\t%s\n", ts, n, r
    }' "$CENSUS_TOKENS" - <<<"$snap"
}

# arm_census — the first sample is the RUNNER's, taken in this shell before the first leg dispatches,
# so every first-wave leg has a sample inside its window however short it is, and its `unknown` is
# announced from here: a backgrounded subshell gives no ordering against its parent and has no stderr.
# Truncating at arm means a run id reused through GATE_RUN_ID never reads a stale sample. Only the
# periodic loop is detached, and it copies `ts_tick_start` property by property: stdio to /dev/null,
# disowned so `live()` never counts it, and two exits, the runner gone or the run's disarm marker. A
# `kill -9` on the runner leaves it to exit at its next tick, holding no descriptor of the caller's.
CENSUS_ARMED=0; CENSUS_PID=""
arm_census() {
  [ "$CENSUS_ARMED" = 0 ] || return 0
  CENSUS_ARMED=1
  [ -n "$RUNDIR" ] || return 0
  local _f="$RUNDIR/census" _c="" _me=$$ _every=$CENSUS_EVERY _work=$WORK _spawn=0 _tp
  # THE SPAWN PAUSE'S READING (TOOL-aSparedSpawn-2): three timed spawns a tick, written tmp-then-rename
  # to the file the dispatcher reads with a builtin, only while the pause is live and no seam stands in.
  [ "${SPAWNPAUSE:-0}" -gt 0 ] && [ -n "${SPAWNPAUSE_FLOOR:-}" ] && [ -z "$SPAWN_NOW_SEAM" ] && _spawn=1
  measure_foreign > "$_f" 2>/dev/null
  chmod 600 "$_f" 2>/dev/null || true
  { IFS=$'\t' read -r _ _c _ < "$_f"; } 2>/dev/null
  case "$_c" in
    ''|*[!0-9]*) echo "run-gates: NOTE - the foreign-load census's first sample reads unknown (ps -ef failed, named no PID or PPID column, or did not list this runner), so a leg's foreign field reads unknown and derive-ceilings sets its reading aside" >&2 ;;
  esac
  (
    while :; do
      sleep "$_every"
      kill -0 "$_me" 2>/dev/null || exit 0
      [ -f "$_work/census.disarm" ] && exit 0
      if [ "$_spawn" = 1 ]; then
        measure_spawn_cost 3
        [ -n "$SPAWN_US" ] && derive_temp_path _tp "$_work/spawn-now" && printf '%s\n' "$SPAWN_US" > "$_tp" 2>/dev/null \
          && mv -f "$_tp" "$_work/spawn-now" 2>/dev/null
      fi
      measure_foreign >> "$_f" 2>/dev/null || exit 0
    done
  ) >/dev/null 2>&1 &
  CENSUS_PID=$!
  disown "$CENSUS_PID" 2>/dev/null || true
}

remove_census_watcher() {
  [ -n "${CENSUS_PID:-}" ] || return 0
  : > "$WORK/census.disarm" 2>/dev/null || true
  kill "$CENSUS_PID" 2>/dev/null
  CENSUS_PID=""
}

# derive_foreign <started-ns> <ended-ns> — FOREIGN, one leg attempt's `foreign` field, from the census
# samples stamped inside [start − 3 × CENSUS_EVERY, end]: their largest positive count; else `unknown`
# when one of them reads unknown or none exists; else 0. The reach is three periods because `sleep`
# on node `a` delivered 1.65 to 1.93 times its nominal seconds under load (the wall's measurement
# above), and one period would leave a short leg with no sample at all. SET, never printed, and
# builtins only: the worker would read a printed value through a subshell, which is a spawn per leg.
# An unterminated last line is a sample still being appended, and `read` skips it.
derive_foreign() {
  local lo hi ts c max=0 unk=0 any=0
  FOREIGN=unknown
  case "${1:-}${2:-}" in ''|*[!0-9]*) return 0 ;; esac
  [ -n "$RUNDIR" ] && [ -f "$RUNDIR/census" ] || return 0
  lo=$(( $1 / 1000000000 - 3 * CENSUS_EVERY )); hi=$(( $2 / 1000000000 ))
  while IFS=$'\t' read -r ts c _; do
    case "$ts" in ''|*[!0-9]*) continue ;; esac
    [ "$ts" -ge "$lo" ] && [ "$ts" -le "$hi" ] || continue
    any=1
    case "$c" in ''|*[!0-9]*) unk=1; continue ;; esac
    [ "$c" -gt "$max" ] && max=$c
  done < "$RUNDIR/census" 2>/dev/null
  if [ "$max" -gt 0 ]; then FOREIGN=$max
  elif [ "$any" = 1 ] && [ "$unk" = 0 ]; then FOREIGN=0; fi
  return 0
}

# ---- RED ATTRIBUTION, REPORT-ONLY. TOOL-dDerivedDocket-23 ----------------------------------------
# A red bar names WHICH legs failed and never WHOSE failure each one is. Five recorded stops were a
# run deciding, with nobody to ask, that a red "was not mine", and at least two of those claims were
# wrong. `GATE_ATTRIBUTE=<R>` re-runs each red leg ALONE at R — R's own manifest row, in a detached
# scratch worktree of R, under R's ceiling for that row — and prints one `GATE attr` line per red leg
# in manifest order, then `attributed N of M red legs against <R8>`. The same rows land in the run
# record as `attribution`, TAB-separated: leg · verdict · inherited · own · R sha · age · owner sha8 ·
# owner id · reason, the reason LAST, and a unit that extends the row inserts its columns before it,
# never after. The three age columns are TOOL-dDerivedDocket-24's, `-` wherever no age was asked for.
#
# IT CHANGES NO EXIT CODE. A bar red before this block is red after it; the policy that acts on a
# verdict is the inherited-red policy unit's, not this one's.
#
# R IS THE LANDING BASE, never the branch point. `TOOL-aStagedLane-6` withdrew a "not mine" claim
# measured against a base the default branch had already moved past, and left the rule this block
# implements: such a claim is indistinguishable from one nobody measured. The pre-push hook exports
# the remote sha it reads for the default branch; an R passed as a merge-base or a local ref buys an
# attribution only as fresh as that ref.
#
# THE CLASSIFIER, first match wins:
#   1  OWN, forced — the diff between R and the working tree touches this runner, the fingerprint
#      helper, the pre-push hook or lib-attribute.sh (KF3). Every red, a timed-out one included.
#   2  CONTENDED   — the leg's own attempt ended with its ceiling FIRED (`check_ceiling_fired`, spelled
#      identically on the retry side). Never re-run at R. A bound-0 rc 137 is a failure and goes on.
#   3  OWN         — no row at R · its argv differs from R's · the diff touches its COMPARATOR (every
#      tracked file under the directory of a tracked file in its argv or in R's signature argv, plus
#      each tracked root-level file those files' bytes name) · it is GREEN at R.
#   4  DEAD PROBE  — R cannot answer: no worktree, R's argv file absent, R's run past its ceiling, R's
#      output empty after normalising while it exits non-zero, the wall cut the run — or L's own
#      output normalises to nothing (KF14: an empty S(L) with a non-zero exit is evidence of nothing).
#   5  INHERITED / MIXED — with a `signature` in R's row, S(X) is that argv's stdout run in the tree
#      at X, normalised, as a SET: INHERITED when S(L) is non-empty and S(L) ⊆ S(R). Without one, S(X)
#      is the leg's normalised output, INHERITED only when byte-identical. L's own `signature` is
#      never run, so a run cannot choose its grader (F4).
#
# WHAT IT DOES NOT CHECK, said out loud. The comparator reads each grader's own directory and the root
# files its bytes name: a module imported from ANOTHER directory, or a conf named only at run time, is
# outside it, and an edit there that hides the run's own offender can read INHERITED. A grader
# directly under a top-level directory is compared against that whole directory, which reads its reds
# OWN on any edit there — the safe direction. And an untracked file is invisible to the diff.
#
# IT RUNS INSIDE THE WALL, before the watcher is removed, so one bound covers the bar and its
# attribution and the declared-wall backstop stays one number. A run the wall cuts reads DEAD PROBE
# `cut by the wall`, which reads as not inherited: the safe direction.
RED_LEGS=""; ATTR_CUT=0; WALL_END=0; ATTR_LANDABLE=0; ATTR_LAND_LEGS=""
# The serial retry's state (TOOL-dDerivedDocket-26): the legs deferred on a fired ceiling, how many
# ran again and failed again, the first attempts whose processes were not cleared, and the HOST legs
# with the lowest ratio among them, which is the figure the `gates HOST` line can claim of all of them.
DEFERRED=""; RETRIED=0; RETRY_FAILS=0; UNCLEARED=""; HOST_N=0; HOST_LEGS=""; HOST_R10=""; RESIDUE=""
TAIL_RELEASED=""   # the legs whose retry `run_tail_retry` started in the pool's tail (TOOL-aSparedSpawn-3)
ATTR_US=$'\x1f'; ATTR_RS=$'\x1e'

# check_ceiling_fired <rc> <bound> <seconds> — rc 0 when the attempt's OWN ceiling fired: 124 under a
# positive bound, or 137 under a positive bound whose seconds reached it (`timeout -k`'s KILL after an
# ignored TERM). A 137 under no bound, or short of it, is a failure like any other.
check_ceiling_fired() {
  local rc=$1 b=${2:-0} s=${3:-} si
  case "$b" in ''|*[!0-9]*) b=0 ;; esac
  [ "$b" -gt 0 ] || return 1
  [ "$rc" = 124 ] && return 0
  [ "$rc" = 137 ] || return 1
  si=${s%%.*}
  case "$si" in ''|*[!0-9]*) return 1 ;; esac
  [ "$si" -ge "$b" ]
}

# ---- THE SERIAL RETRY. TOOL-dDerivedDocket-26 S1 to S5 ---------------------------------------------
# A leg whose own ceiling fired was DEFERRED by `report_one` rather than failed. After the pool drains,
# and while the run's wall is still armed so the retry cannot outlast it, each such leg runs ONCE more,
# alone, under its own ceiling. A pass counts green and is counted in `retried`; a second timeout is a
# failure, and it is HOST when a spawn measured then costs more than GATE_HOST_RATIO times the floor
# this clone recorded before the bar began. One retry, and only for a fired ceiling: an assertion
# failure is never retried, which is why TOOL-dSpentCeiling-8's two assertion reds stay open.
#
# measure_neighbours <leg index> — how many OTHER legs were running when this one timed out: those
# whose run-record interval contains its end time, plus those still holding a pid and no result when
# the reader reaches it. A retry's pid and an attribution run's are not pool legs and are not counted.
measure_neighbours() {
  local i=$1 e="" f j k=0 js je
  [ -n "$RUNDIR" ] && [ -f "$RUNDIR/$i.leg" ] && { IFS=$'\t' read -r _ _ _ _ _ e _ < "$RUNDIR/$i.leg"; } 2>/dev/null
  case "$e" in ''|*[!0-9]*) e="" ;; esac
  for f in "$WORK"/*.pid; do
    [ -e "$f" ] || continue
    j=${f##*/}; j=${j%.pid}
    case "$j" in ''|*[!0-9]*) continue ;; esac
    [ "$j" = "$i" ] && continue
    if [ -n "$e" ] && [ -f "$RUNDIR/$j.leg" ]; then
      js=""; je=""
      { IFS=$'\t' read -r _ _ _ _ js je _ < "$RUNDIR/$j.leg"; } 2>/dev/null
      case "$js$je" in ''|*[!0-9]*) continue ;; esac
      [ "$js" -le "$e" ] && [ "$e" -le "$je" ] && k=$((k + 1))
    elif [ ! -f "$WORK/$j.rc" ]; then
      k=$((k + 1))
    fi
  done
  printf '%s' "$k"
}

# check_residue_gone <leg index> <attempt suffix> — rc 0 when that attempt's worker has exited and no
# process is left in the group its `timeout` led. RESIDUE names what is left otherwise: a live worker
# with its ppid-descendants from one snapshot, then any live member of the group, or the fact that the
# group could not be read at all. It ASSERTS and never kills, because the reap is the worker's and a
# second reaper here would hide a first one that failed.
#
# WHAT IT DOES NOT CHECK: that `scan_group` itself works. The reap and this assertion read the group
# through the same scan, so a scan that returned a wrong empty answer would blind both at once; an
# unparseable table is caught by the scan's own rc, and the canary grades the reap from the leg's side
# instead, by the grandchild's pid as the leg itself recorded it.
check_residue_gone() {
  local i=$1 sfx=${2:-} p g q snap members
  RESIDUE=""
  p=$(cat "$WORK/$i$sfx.pid" 2>/dev/null) || p=""
  if [ -n "$p" ] && kill -0 "$p" 2>/dev/null; then
    RESIDUE=$p
    if snap=$(mktemp 2>/dev/null); then
      ps -ef > "$snap" 2>/dev/null || : > "$snap"
      RESIDUE=$(scan_descendants "$p" "$snap")
      rm -f "$snap" 2>/dev/null
    fi
  fi
  g=$(cat "$WORK/$i$sfx.tpid" 2>/dev/null) || g=""
  if [ -n "$g" ]; then
    if members=$(scan_group "$g"); then
      for q in $members; do
        kill -0 "$q" 2>/dev/null && RESIDUE="$RESIDUE${RESIDUE:+ }$q"
      done
    else
      RESIDUE="$RESIDUE${RESIDUE:+ }(ps shows no process group here, so group $g could not be read)"
    fi
  fi
  [ -z "$RESIDUE" ]
}

# derive_host_note <leg index> — HOST_NOTE for a leg that timed out on its serial retry, and rc 0 when
# it reads HOST: a floor was READ before this bar measured, the processes of both attempts are
# verified gone, and one more measurement exceeds GATE_HOST_RATIO times that floor. Every other outcome
# says why HOST was not read, so a FAIL never looks as though the host was measured and cleared.
derive_host_note() {
  local i=$1 r10
  HOST_NOTE=""
  case "$SPAWN_FLOOR_STATE" in
    absent)     HOST_NOTE="no spawn floor is recorded for this clone, so HOST was not measured"; return 1 ;;
    unreadable) HOST_NOTE="the spawn floor could not be read, so HOST was not measured"; return 1 ;;
  esac
  case " $UNCLEARED " in
    *" $i "*) HOST_NOTE="an earlier attempt left processes running, so a spawn cost says nothing about the host"; return 1 ;;
  esac
  if ! check_residue_gone "$i" .retry; then
    printf 'run-gates: the serial retry of %s left processes running: %s\n' "${names[$i]}" "$RESIDUE" >&2
    HOST_NOTE="its serial retry left processes running, so a spawn cost says nothing about the host"; return 1
  fi
  measure_spawn_cost
  if [ -z "$SPAWN_US" ]; then HOST_NOTE="the spawn cost could not be measured, so HOST was not measured"; return 1; fi
  r10=$(( SPAWN_US * 10 / SPAWN_FLOOR_US ))
  if [ "$SPAWN_US" -gt $(( GATE_HOST_RATIO * SPAWN_FLOOR_US )) ]; then
    HOST_N=$((HOST_N + 1)); HOST_LEGS="$HOST_LEGS${HOST_LEGS:+, }${names[$i]}"
    { [ -z "$HOST_R10" ] || [ "$r10" -lt "$HOST_R10" ]; } && HOST_R10=$r10
    HOST_NOTE="HOST: a spawn cost $((r10 / 10)).$((r10 % 10))x this clone's floor"
    return 0
  fi
  HOST_NOTE="a spawn cost $((r10 / 10)).$((r10 % 10))x this clone's floor, under the ${GATE_HOST_RATIO}x HOST ratio"
  return 1
}

# run_leg_retry — the pass itself. Each deferred leg, in the reader's order, into fresh `.retry` files,
# its worker a background job waited on so it has a pid of its own for the wall to reach, which a
# foreground call would not: `$BASHPID` there is this shell's, and the wall would kill the runner.
# Prints one `GATE ok` or `GATE FAIL` line per retried leg and one `---- retry:` line after them.
#
# A LEG WHOSE RETRY RAN IN THE POOL'S TAIL (TOOL-aSparedSpawn-3 S3, S4) is read, not run again, when
# that attempt passed: the same line, the same count, the same health event a serial pass gives. One
# that did not pass decides nothing (F1, owner 2026-10-10): its files are set aside as `<i>.tail.*`,
# its processes are verified gone as the first attempt's are, and the leg takes the serial retry
# below, alone, so every red retry verdict and every HOST reading still comes from an attempt that
# ran alone after the drain. `<i>.retry.pid` is the witness that a tail attempt started, because the
# pool's final `wait` has reaped every tail job by now and only the serial retry writes it after.
run_leg_retry() {
  local i rc fired secs tail v f
  [ -n "$DEFERRED" ] || return 0
  [ -f "$WORK/wall.breach" ] && return 0
  for i in $DEFERRED; do
    [ -f "$WORK/wall.breach" ] && break
    rc=""
    if [ -f "$WORK/$i.retry.pid" ]; then
      [ -f "$WORK/$i.retry.rc" ] && read -r rc < "$WORK/$i.retry.rc"
      if [ "$rc" != 0 ]; then
        for f in "$WORK/$i".retry.* ${RUNDIR:+"$RUNDIR/$i".retry.*}; do
          [ -e "$f" ] && mv -f "$f" "${f%.retry.*}.tail.${f##*.retry.}" 2>/dev/null
        done
        if ! check_residue_gone "$i" .tail; then
          printf 'run-gates: the tail attempt of %s left processes running before its serial retry: %s\n' \
            "${names[$i]}" "$RESIDUE" >&2
          UNCLEARED="$UNCLEARED $i"
        fi
      fi
    fi
    RETRIED=$((RETRIED + 1))
    if [ "$rc" != 0 ]; then
      # THE FIRST ATTEMPT IS VERIFIED CLEAR, never assumed clear: its worker reaped its group before it
      # wrote `.rc`, and this is the assertion that the reap worked. A survivor is named and the leg is
      # still retried, but a second timeout then cannot read HOST, since the spawn cost is not
      # attributable to the host while this bar's own processes are running.
      if ! check_residue_gone "$i" ""; then
        printf 'run-gates: the timed-out attempt of %s left processes running before its serial retry: %s\n' \
          "${names[$i]}" "$RESIDUE" >&2
        UNCLEARED="$UNCLEARED $i"
      fi
      runleg "$i" .retry &
      wait "$!" 2>/dev/null
      if [ ! -f "$WORK/$i.retry.rc" ]; then
        [ -f "$WORK/wall.breach" ] && break      # the wall killed it: the breach block names the leg
        fails=$((fails + 1)); RETRY_FAILS=$((RETRY_FAILS + 1)); RED_LEGS="$RED_LEGS $i"
        printf 'GATE FAIL  %s  (no result on its serial retry)\n' "${names[$i]}"
        FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]}  (no result on its serial retry)"$'\n'
        continue
      fi
      rc=$(cat "$WORK/$i.retry.rc")
    fi
    if [ "$rc" = 0 ]; then
      printf 'GATE ok    %s  (retried after timeout)\n' "${names[$i]}"
      add_health_event "$RG_HEALTH_LOG" run-gates retry-passed "${names[$i]} after a $(cat "$WORK/$i.bound" 2>/dev/null || printf '?')s timeout"
      continue
    fi
    fails=$((fails + 1)); RETRY_FAILS=$((RETRY_FAILS + 1)); RED_LEGS="$RED_LEGS $i"
    fired=$(cat "$WORK/$i.retry.bound" 2>/dev/null) || fired=0
    secs=$(cat "$WORK/$i.retry.sec" 2>/dev/null) || secs=""
    if check_ceiling_fired "$rc" "$fired" "$secs"; then
      if [ "$rc" = 124 ]; then tail="timed out after ${fired}s, again on its serial retry"
      else tail="killed after ${secs:-?}s, ceiling ${fired}s, again on its serial retry"; fi
      derive_host_note "$i"
      tail="$tail; $HOST_NOTE"
    else
      tail="$(derive_fail_tail "$rc" "$fired" "$secs"), on its serial retry"
    fi
    printf 'GATE FAIL  %s  (%s)\n' "${names[$i]}" "$tail"; sed 's/^/    /' "$WORK/$i.retry.out"
    FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]}  ($tail)"$'\n'
    leg_log "${names[$i]}" && lf=$LEG_LOG && [ -n "$lf" ] && FAILED_LEGS="${FAILED_LEGS}    log: $lf"$'\n'
  done
  if [ -f "$WORK/wall.breach" ]; then v=killed
  elif [ "$RETRY_FAILS" = 0 ]; then v=green
  elif [ "$HOST_N" = "$RETRY_FAILS" ]; then v=HOST
  else v=RED; fi
  printf -- '---- retry: %s  (%s retried, %s failed)\n' "$v" "$RETRIED" "$RETRY_FAILS"
  CHUNK_ROLLUP="${CHUNK_ROLLUP}retry\t${v}\t${RETRIED}\t${RETRY_FAILS}\n"
  return 0
}

# run_tail_retry — THE TAIL RELEASE (TOOL-aSparedSpawn-3 S2). Called by the dispatch pass once every
# first attempt is dispatched: starts ONE marked leg's retry as a pool job while at most one other job
# runs. One neighbour, typically the floor leg, is the cheapest contention that still uses the idle
# slots; a retry packed beside several heavy legs recreates what killed it. The markers are a glob and
# a released leg is remembered in TAIL_RELEASED rather than read from its `.retry.pid`, which the job
# writes asynchronously, so the decision forks nothing until some marker is unreleased, and only then
# counts the running jobs. The memory pause holds it as it holds any dispatch.
run_tail_retry() {
  local f j
  for f in "$WORK"/*.defer; do
    [ -e "$f" ] || return 0
    j=${f##*/}; j=${j%.defer}
    case " $TAIL_RELEASED " in *" $j "*) continue ;; esac
    live; nlive=$LIVE_N
    [ "$nlive" -le 1 ] || return 0
    check_dispatch_pause "$nlive" && return 0
    TAIL_RELEASED="$TAIL_RELEASED $j"
    runleg "$j" .retry &
    return 0
  done
  return 0
}

# run_leg_at <dir> <bound> <out> <tag> <both|stdout> <argv…> — one argv run from <dir>, stdin denied,
# captured through a FILE (a pipe would bound the verdict and not the clock), the same launcher
# substitution `runleg` applies. The pid goes where the wall looks for unfinished legs, and the `.rc`
# beside it is what tells the wall and the teardown reap that this one returned.
run_leg_at() {
  local dir=$1 bound=$2 out=$3 tag=$4 streams=$5 rc
  shift 5
  local -a av=("$@")
  case "${av[0]:-}" in python|python3) av[0]=$PYBIN ;; esac
  case "$bound" in ''|*[!0-9]*) bound=0 ;; esac
  [ "$CEILINGS_LIVE" = 1 ] || bound=0
  # THE BRACE GROUP'S `2>/dev/null` IS THE SHELL'S, not the run's: a subshell the wall SIGKILLs makes
  # this shell print a `Killed` job notice on its own stderr, and the verdict line already says it.
  # The run's own stderr is re-pointed inside, to the capture file or to nothing.
  {
    (
      printf '%s' "$BASHPID" > "$WORK/attr-$tag.pid" 2>/dev/null
      cd "$dir" || exit 97
      if [ "$streams" = stdout ]; then exec 2>/dev/null; else exec 2>&1; fi
      if [ "$bound" -gt 0 ]; then exec timeout -k 5s "$bound" "${av[@]}"; else exec "${av[@]}"; fi
    ) </dev/null >"$out"
  } 2>/dev/null
  rc=$?
  printf '%s' "$rc" > "$WORK/attr-$tag.rc" 2>/dev/null || true
  return "$rc"
}

# read_row_at <leg name> — R's row for that leg (name · argv · ceiling · signature, RS-separated), or
# nothing. The name goes through the environment, never `-v`, which would process its escapes.
read_row_at() {
  AT_NAME=$1 awk -F"$ATTR_RS" '$1 == ENVIRON["AT_NAME"] { print; exit }' "$ATTR_ROWS" 2>/dev/null
}

# derive_comparator <L argv> <R signature argv> — the first comparator path the diff against R
# touches, or nothing. Both argvs arrive US-joined; argv[0] is the launcher and is not a grader.
derive_comparator() {
  local spec tok d r f files="" dirs=""
  local -a toks
  for spec in "$1" "$2"; do
    [ -n "$spec" ] || continue
    IFS="$ATTR_US" read -ra toks <<<"$spec"
    for tok in "${toks[@]:1}"; do
      case "$tok" in ''|-*) continue ;; esac
      if [ "$(git ls-files --full-name -- "$tok" 2>/dev/null | head -1)" = "$tok" ] \
         || [ "$(git cat-file -t "$ATTR_RSHA:$tok" 2>/dev/null)" = blob ]; then
        # The directory by EXPANSION, not `$(dirname …)`: `dirs` feeds a here-string loop below, and
        # a value assembled from a substitution is the shell-hygiene leg's class one hop away. `tok`
        # is a tracked FILE path (it passed one of the two tests above), so it has no trailing `/`
        # and the two spellings agree; a bare name is `.`, as dirname says.
        d=${tok%/*}; [ "$d" = "$tok" ] && d=.
        files="$files$tok"$'\n'; dirs="$dirs$d"$'\n'
      fi
    done
  done
  [ -n "$files" ] || return 0
  while IFS= read -r d; do
    [ -n "$d" ] || continue
    if [ "$d" = . ]; then r=$(printf '%s\n' "$ATTR_CHG" | awk 'NF { print; exit }')
    else r=$(printf '%s\n' "$ATTR_CHG" | AT_DIR="$d/" awk 'index($0, ENVIRON["AT_DIR"]) == 1 { print; exit }'); fi
    [ -n "$r" ] && { printf '%s' "$r"; return 0; }
  done <<<"$dirs"
  while IFS= read -r r; do
    case "$r" in ''|*/*) continue ;; esac
    while IFS= read -r f; do
      [ -n "$f" ] || continue
      if [ -f "$f" ]; then
        grep -qF -- "$r" "$f" 2>/dev/null && { printf '%s' "$r"; return 0; }
      else
        git show "$ATTR_RSHA:$f" 2>/dev/null | grep -qF -- "$r" && { printf '%s' "$r"; return 0; }
      fi
    done <<<"$files"
  done <<<"$ATTR_CHG"
  return 0
}

# read_offender_set <raw> <set> <set|text> — the normalised offender set, or the normalised text.
read_offender_set() {
  if [ "$3" = set ]; then
    sed -E -f "$ATTR_NORM" "$1" 2>/dev/null | grep -v '^[[:space:]]*$' | LC_ALL=C sort -u > "$2"
  else
    sed -E -f "$ATTR_NORM" "$1" > "$2" 2>/dev/null
  fi
}

# derive_attribution <leg index> — sets A_V (verdict), A_WHY (reason) and A_I / A_O (the inherited and
# own counts, or `-` where no comparison was made). Reads the globals `run_attribution` resolved.
# An INHERITED verdict also leaves what the age probe re-uses (TOOL-dDerivedDocket-24): L's normalised
# set or text in A_LSET, and R's argv, signature and ceiling in A_RARGV, A_RSIG and A_RBOUND.
derive_attribution() {
  local i=$1 rc bound secs row rargv rce rsig f rbound rc_r t0 t1 rsecs lset rset raw src src_rc
  local -a rav rsv
  A_V="DEAD PROBE"; A_WHY=""; A_I=-; A_O=-
  A_LSET=""; A_RARGV=""; A_RSIG=""; A_RBOUND=""
  if [ -n "$ATTR_WHY_ALL" ]; then A_WHY=$ATTR_WHY_ALL; return 0; fi
  if [ -f "$WORK/wall.breach" ]; then ATTR_CUT=1; A_WHY="cut by the wall"; return 0; fi
  if [ -n "$ATTR_KF3" ]; then
    A_V=OWN; A_WHY="KF3: the diff against R touches $ATTR_KF3, so this run edited its own grader"; return 0
  fi
  if [ ! -f "$WORK/$i.rc" ]; then A_WHY="no result at L, so there is nothing to compare"; return 0; fi
  rc=$(cat "$WORK/$i.rc" 2>/dev/null)
  bound=$(cat "$WORK/$i.bound" 2>/dev/null) || bound=0
  secs=$(cat "$WORK/$i.sec" 2>/dev/null) || secs=""
  if check_ceiling_fired "$rc" "$bound" "$secs"; then
    A_V=CONTENDED
    if [ "$rc" = 124 ]; then A_WHY="timed out after ${bound}s; not re-run at R"
    else A_WHY="killed after ${secs}s at its ${bound}s ceiling; not re-run at R"; fi
    return 0
  fi
  case "$ATTR_ROWS_STATE" in
    unparseable) A_WHY="the manifest at R does not parse, so R's row cannot be read"; return 0 ;;
    untracked)   A_WHY="the manifest is not tracked, so R's row cannot be read"; return 0 ;;
  esac
  row=$(read_row_at "${names[$i]}")
  if [ -z "$row" ]; then A_V=OWN; A_WHY="no row in R's manifest"; return 0; fi
  IFS="$ATTR_RS" read -r _ rargv rce rsig <<<"$row"
  if [ "$rargv" != "${argvs[$i]}" ]; then A_V=OWN; A_WHY="its argv differs from R's row"; return 0; fi
  f=$(derive_comparator "${argvs[$i]}" "${rsig:-}")
  if [ -n "$f" ]; then A_V=OWN; A_WHY="the diff against R touches its comparator: $f"; return 0; fi

  # ---- THE R RUN. One worktree serves every red leg of one bar, made on first need.
  if [ -z "$ATTR_WT" ]; then
    if [ "$ATTR_WT_FAILED" = 1 ] || ! add_scratch_worktree "$ATTR_WT_PATH" "$ATTR_RSHA"; then
      ATTR_WT_FAILED=1; A_WHY="the R worktree could not be made at $ATTR_WT_PATH"; return 0
    fi
    ATTR_WT=$ATTR_WT_PATH
    echo "run-gates: R worktree $ATTR_WT — removed on exit; an orphan is removable by hand"
  fi
  IFS="$ATTR_US" read -ra rav <<<"$rargv"
  f=${rav[1]:-}
  if [ -n "$f" ] && [ -f "$f" ] && [ ! -f "$ATTR_WT/$f" ]; then
    A_WHY="R's argv file $f is absent at R"; return 0
  fi
  rbound=${rce:-$PROF_TIMEOUT}
  t0=${EPOCHREALTIME/[.,]/}000
  run_leg_at "$ATTR_WT" "$rbound" "$ATMP/$i.r.raw" "$i" both "${rav[@]}"; rc_r=$?
  t1=${EPOCHREALTIME/[.,]/}000; rsecs=$(( (t1 - t0) / 1000000000 ))
  if [ -f "$WORK/wall.breach" ]; then ATTR_CUT=1; A_WHY="cut by the wall"; return 0; fi
  [ "$CEILINGS_LIVE" = 1 ] || rbound=0
  if check_ceiling_fired "$rc_r" "$rbound" "$rsecs"; then
    A_WHY="R's run hit its ${rbound}s ceiling, so R gave no answer"; return 0
  fi
  if [ "$rc_r" = 0 ]; then A_V=OWN; A_WHY="green at R"; return 0; fi

  # ---- THE TWO SETS.
  lset="$ATMP/$i.l.set"; rset="$ATMP/$i.r.set"
  if [ -n "${rsig:-}" ]; then
    IFS="$ATTR_US" read -ra rsv <<<"$rsig"
    for src in l r; do
      if [ "$src" = l ]; then run_leg_at "$ROOT" "$rbound" "$ATMP/$i.sl.raw" "$i-sl" stdout "${rsv[@]}"
      else run_leg_at "$ATTR_WT" "$rbound" "$ATMP/$i.sr.raw" "$i-sr" stdout "${rsv[@]}"; fi
      src_rc=$?
      if [ -f "$WORK/wall.breach" ]; then ATTR_CUT=1; A_WHY="cut by the wall"; return 0; fi
      if { [ "$src_rc" = 124 ] || [ "$src_rc" = 137 ]; } && [ "${rbound:-0}" -gt 0 ]; then
        A_WHY="R's signature ran past its ${rbound}s ceiling at $(printf '%s' "$src" | tr lr LR)"; return 0
      fi
    done
    read_offender_set "$ATMP/$i.sl.raw" "$lset" set
    read_offender_set "$ATMP/$i.sr.raw" "$rset" set
  else
    raw=$(cat "$ATMP/$i.r.raw" 2>/dev/null)
    printf '%s\n' "$raw" > "$ATMP/$i.r.out"
    read_offender_set "$WORK/$i.out" "$lset" text
    read_offender_set "$ATMP/$i.r.out" "$rset" text
  fi
  if ! grep -q '[^[:space:]]' "$rset" 2>/dev/null; then
    A_WHY="R's output normalises to nothing while it exits $rc_r"; return 0
  fi
  if ! grep -q '[^[:space:]]' "$lset" 2>/dev/null; then
    A_WHY="L's output normalises to nothing while it exits ${rc:-?} (KF14)"; return 0
  fi

  # ---- RULE 5. Sets for a signature; byte-identity without one, with set counts for the MIXED line.
  if [ -z "${rsig:-}" ] && cmp -s "$lset" "$rset"; then
    A_V=INHERITED; A_I=$(grep -c '[^[:space:]]' "$lset" || true); A_O=0
    A_LSET=$lset; A_RARGV=$rargv; A_RSIG=""; A_RBOUND=$rbound
    A_WHY="byte-identical output at L and R"; return 0
  fi
  if [ -z "${rsig:-}" ]; then
    grep -v '^[[:space:]]*$' "$lset" | LC_ALL=C sort -u > "$lset.u"
    grep -v '^[[:space:]]*$' "$rset" | LC_ALL=C sort -u > "$rset.u"
    lset="$lset.u"; rset="$rset.u"
  fi
  A_I=$(LC_ALL=C comm -12 "$lset" "$rset" | grep -c . || true)
  A_O=$(LC_ALL=C comm -23 "$lset" "$rset" | grep -c . || true)
  if [ -n "${rsig:-}" ] && [ "$A_O" = 0 ]; then
    A_V=INHERITED; A_LSET=$lset; A_RARGV=$rargv; A_RSIG=$rsig; A_RBOUND=$rbound
    A_WHY="every offender at L is an offender at R, by R's signature"; return 0
  fi
  A_V=MIXED
  if [ -n "${rsig:-}" ]; then A_WHY="offenders at L that R does not carry, by R's signature"
  else A_WHY="the output differs from R's, and R's row declares no signature"; fi
  return 0
}

# ---- AGE AND OWNER, for an INHERITED leg only. TOOL-dDerivedDocket-24 --------------------------
# An INHERITED red is one the landing base already carries, and that alone never says for how long.
# Under `GATE_INHERITED_RED_MAX_AGE=<n>` each INHERITED leg is run once more at R~n, R's n-th
# first-parent ancestor: red there with every offender L carries is `aged`. The age decides the
# ESCALATION only, never the landing (TOOL-dUnstuckLanding-22, superseding that part of
# TOOL-dDerivedDocket-24): an aged INHERITED leg lands under `land` like any other, and the driver
# files its ask at BLOCKER instead of HIGH. Otherwise the red arrived inside (R~n, R], and a bisection of that first-parent window finds
# the first landing whose run carries L's offenders — its sha8, and the first id its subject carries,
# name the OWNER. With n = 10 that is at most five more runs of one leg, on a red bar only.
#
# THE SAME COMPARISON RULE 5 MADE AT R, run from R's own row in the SAME scratch worktree checked out
# at each probe, so the normaliser that strips that worktree's path still strips it. A probe that
# cannot answer — the wall, a ceiling, a checkout that fails, an output that normalises to nothing —
# leaves the age UNPROVEN (`-`). An unproven age still lands under `land` and is never escalated,
# because nothing proves it aged.
#
# WITHOUT A SIGNATURE the probe reads red there only when every non-blank line of L's output is in
# the probe's, and red with any other output is one more probe that cannot answer: text is not an
# offender set, so a fixed offender and a moved count line look alike. Such a leg's age is therefore
# proven only while its text holds still or shrinks toward L's; a row that wants its red aged across
# a changing count declares a `signature`. Green is the only rc-1 answer, because rc 1 moves the
# bisection toward R and so makes an old red read young (closing diff review F1).
#
# WHAT IT DOES NOT CHECK. The bisection assumes the red, once present, stayed on the line: a leg that
# went red, green and red again inside the window is owned by whichever landing the search meets,
# which may be the later one. A flaky leg can bisect to the wrong owner too. The ask the driver files
# names the leg's argv so a reader can re-run it, which is the only defence this block claims.
ATTR_FPL=(); ATTR_WT_MOVED=0
# check_red_at <leg index> <sha> <probe tag> — rc 0 when the leg, run from R's row with the R worktree
# checked out at <sha>, is red there carrying every offender L carries (every line of L's, for a row
# with no signature); rc 1 when it is green there, its argv file is absent there, or a signature
# offender of L's is missing; rc 2 when that tree could not answer, or a row with no signature is red
# there with output that is not L's, with the reason in A_AGE_WHY.
check_red_at() {
  local i=$1 sha=$2 tag=$3 rc_x t0 t1 xsecs raw xset f rb=${A_RBOUND:-0}
  local -a xav xsv
  A_AGE_WHY=""
  if [ -f "$WORK/wall.breach" ]; then ATTR_CUT=1; A_AGE_WHY="cut by the wall"; return 2; fi
  ATTR_WT_MOVED=1
  if ! git -C "$ATTR_WT" checkout -q -f --detach "$sha" >/dev/null 2>&1 \
     || ! git -C "$ATTR_WT" clean -q -f -d -x >/dev/null 2>&1; then
    A_AGE_WHY="the R worktree could not be checked out at ${sha:0:8}"; return 2
  fi
  IFS="$ATTR_US" read -ra xav <<<"$A_RARGV"
  f=${xav[1]:-}
  if [ -n "$f" ] && [ -f "$f" ] && [ ! -f "$ATTR_WT/$f" ]; then return 1; fi
  t0=${EPOCHREALTIME/[.,]/}000
  run_leg_at "$ATTR_WT" "$rb" "$ATMP/$i.$tag.raw" "$i-$tag" both "${xav[@]}"; rc_x=$?
  t1=${EPOCHREALTIME/[.,]/}000; xsecs=$(( (t1 - t0) / 1000000000 ))
  if [ -f "$WORK/wall.breach" ]; then ATTR_CUT=1; A_AGE_WHY="cut by the wall"; return 2; fi
  if check_ceiling_fired "$rc_x" "$rb" "$xsecs"; then
    A_AGE_WHY="the run at ${sha:0:8} hit its ${rb}s ceiling"; return 2
  fi
  [ "$rc_x" = 0 ] && return 1
  xset="$ATMP/$i.$tag.set"
  if [ -n "$A_RSIG" ]; then
    IFS="$ATTR_US" read -ra xsv <<<"$A_RSIG"
    run_leg_at "$ATTR_WT" "$rb" "$ATMP/$i.$tag.sig" "$i-$tag-s" stdout "${xsv[@]}"
    if [ -f "$WORK/wall.breach" ]; then ATTR_CUT=1; A_AGE_WHY="cut by the wall"; return 2; fi
    read_offender_set "$ATMP/$i.$tag.sig" "$xset" set
  else
    raw=$(cat "$ATMP/$i.$tag.raw" 2>/dev/null)
    printf '%s\n' "$raw" > "$ATMP/$i.$tag.out"
    read_offender_set "$ATMP/$i.$tag.out" "$xset" text
  fi
  if ! grep -q '[^[:space:]]' "$xset" 2>/dev/null; then
    A_AGE_WHY="the output at ${sha:0:8} normalises to nothing while it exits $rc_x"; return 2
  fi
  if [ -n "$A_RSIG" ]; then
    [ -z "$(LC_ALL=C comm -23 "$A_LSET" "$xset")" ] && return 0
    return 1
  fi
  # NO SIGNATURE: THE TEXT IS NOT AN OFFENDER SET, so a line of L's missing here cannot be read as an
  # offender of L's missing here — a count line that moved reads exactly the same. Red with every
  # line L prints is red there; red with any other output is a probe that cannot answer, never the
  # rc 1 that means green, which is what it returned until the closing diff review's F1: an old red
  # whose text a later landing changed then bisected to that landing and landed as young.
  cmp -s "$A_LSET" "$xset" && return 0
  grep -v '^[[:space:]]*$' "$A_LSET" | LC_ALL=C sort -u > "$ATMP/$i.$tag.lu"
  grep -v '^[[:space:]]*$' "$xset" | LC_ALL=C sort -u > "$ATMP/$i.$tag.xu"
  [ -z "$(LC_ALL=C comm -23 "$ATMP/$i.$tag.lu" "$ATMP/$i.$tag.xu")" ] && return 0
  A_AGE_WHY="red at ${sha:0:8} with output that is not L's, and R's row declares no signature to compare offenders by"
  return 2
}

# derive_age <leg index> — after an INHERITED verdict, sets A_AGE (the owner's first-parent distance
# from R, `aged`, or `-` when not asked or unproven), A_OWN8 and A_OWNID (`-` when unknown), and
# A_AGE_NOTE, the clause the record's reason gains.
derive_age() {
  local i=$1 lo=0 hi mid rc owner
  A_AGE=-; A_OWN8=-; A_OWNID=-; A_AGE_NOTE=""
  [ -n "$ATTR_MAX_AGE" ] && [ -n "$ATTR_WT" ] && [ "${#ATTR_FPL[@]}" -gt 0 ] || return 0
  hi=${#ATTR_FPL[@]}
  # THE FAR END. A line shorter than n+1 commits has none, and the window is the whole line.
  if [ "$hi" -gt "$ATTR_MAX_AGE" ]; then
    check_red_at "$i" "${ATTR_FPL[$ATTR_MAX_AGE]}" far; rc=$?
    case "$rc" in
      0) A_AGE=aged
         A_AGE_NOTE="red with every offender at R~$ATTR_MAX_AGE ${ATTR_FPL[$ATTR_MAX_AGE]:0:8}, so older than the age bound"
         return 0 ;;
      1) ;;
      *) A_AGE_NOTE="age unproven: $A_AGE_WHY"; return 0 ;;
    esac
    hi=$ATTR_MAX_AGE
  fi
  while [ $((hi - lo)) -gt 1 ]; do
    mid=$(( (lo + hi) / 2 ))
    check_red_at "$i" "${ATTR_FPL[$mid]}" "b$mid"; rc=$?
    case "$rc" in
      0) lo=$mid ;;
      1) hi=$mid ;;
      *) A_AGE_NOTE="age unproven: $A_AGE_WHY"; return 0 ;;
    esac
  done
  owner=${ATTR_FPL[$lo]}
  A_AGE=$lo; A_OWN8=${owner:0:8}
  A_OWNID=$(git log -1 --format=%s "$owner" 2>/dev/null | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | head -1)
  [ -n "$A_OWNID" ] || A_OWNID=-
  A_AGE_NOTE="introduced by $A_OWN8, $lo first-parent landing(s) before R"
}

# run_attribution — the pass. Runs only when asked AND something is red: a green bar pays nothing.
run_attribution() {
  [ -n "${ATTR_REV:-}" ] || return 0
  [ -n "$RED_LEGS" ] || return 0
  local i m=0 nattr=0 dead=0 sum=0 unbounded=0 row rce legs_rel gcd hp k tail rec="" rem summary land_n=0
  ATMP="$WORK/attr"; mkdir -p "$ATMP" 2>/dev/null
  ATTR_WHY_ALL=""; ATTR_KF3=""; ATTR_CHG=""; ATTR_ROWS="$ATMP/rows-at-R"; ATTR_ROWS_STATE=ok
  ATTR_NORM="$ATMP/normalise.sed"; ATTR_WT_FAILED=0; ATTR_WT_PATH=""
  : > "$ATTR_ROWS"
  ATTR_RSHA=$(git rev-parse --verify -q "${ATTR_REV}^{commit}" 2>/dev/null) || ATTR_RSHA=""
  if [ -z "$ATTR_RSHA" ]; then
    ATTR_R8="${ATTR_REV}, which does not resolve to a commit here"
    ATTR_WHY_ALL="R '${ATTR_REV}' does not resolve to a commit, so nothing was run at R"
  else
    ATTR_R8=${ATTR_RSHA:0:8}
  fi
  # SOURCED HERE AND NOWHERE EARLIER, derived from this script's own directory. A runner copied into
  # a fixture without it still runs every other path; this one reads every red DEAD PROBE instead.
  if [ -z "$ATTR_WHY_ALL" ] && { [ ! -f "$KITDIR/lib-attribute.sh" ] || ! . "$KITDIR/lib-attribute.sh"; }; then
    ATTR_WHY_ALL="lib-attribute.sh is missing beside the runner, so there is no normaliser to compare with"
  fi
  if [ -z "$ATTR_WHY_ALL" ] && ! ATTR_CHG=$(git diff --name-only "$ATTR_RSHA" -- 2>/dev/null); then
    ATTR_WHY_ALL="the diff between R and this tree could not be read"
  fi
  if [ -z "$ATTR_WHY_ALL" ]; then
    # KF3. The hook's path is DERIVED from `core.hooksPath`, relative ones only: an unset path means
    # no tracked hook gates this repository's pushes, so there is no tracked hook to have edited.
    hp=$(git config --get core.hooksPath 2>/dev/null) || hp=""
    case "$hp" in ''|/*|[A-Za-z]:*) hp="" ;; *) hp="${hp%/}/pre-push" ;; esac
    for k in "$KITREL/$(basename -- "$0")" "$FPRINT" "$KITREL/lib-attribute.sh" "$hp"; do
      [ -n "$k" ] || continue
      if printf '%s\n' "$ATTR_CHG" | grep -qxF -- "$k"; then ATTR_KF3=$k; break; fi
    done
    # R'S MANIFEST, from the object store. An untracked manifest has no R copy to read.
    legs_rel=$(git ls-files --full-name -- "$LEGS_FILE" 2>/dev/null | head -1)
    if [ -z "$legs_rel" ]; then ATTR_ROWS_STATE=untracked
    elif git cat-file -e "$ATTR_RSHA:$legs_rel" 2>/dev/null; then
      git show "$ATTR_RSHA:$legs_rel" > "$ATMP/manifest-at-R" 2>/dev/null
      "$PYBIN" -c '
import json, sys
try:
    data = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception:
    sys.exit(3)
if not isinstance(data, list):
    sys.exit(3)
# THE ROWS AT R RESOLVE THE {prefix} TOKEN AGAINST THE TOOL ROOT OF THIS RUNNER, exactly as the rows
# at L do, or a manifest at R that spells its argv through the token never equals the resolved argv
# at L and every red reads OWN by "its argv differs". A manifest at R that predates the token passes
# unchanged. NOTE: this program is inside a single-quoted shell block, so it carries no apostrophe.
troot = sys.argv[2] if len(sys.argv) > 2 else ""
# >>> resolve_prefix_token -- canonical copy: resolve_prefix_token.py in the gov lib dir (byte-identical; gated)
def resolve_prefix_token(spelled, troot):
    """<spelled> with its {prefix} token resolved against the tool root <troot>.

    An empty or "." root is a root install: the token drops with its slash, and a bare token
    becomes ".". Any other root replaces the token. Text with no token passes unchanged.
    """
    spelled = str(spelled)
    if not troot or troot == ".":
        return spelled.replace("{prefix}/", "").replace("{prefix}", ".")
    return spelled.replace("{prefix}", troot)
# <<< resolve_prefix_token
out = []
for l in data:
    if not isinstance(l, dict) or not l.get("name"):
        continue
    ce = l.get("ceiling")
    ce = str(ce) if isinstance(ce, int) and not isinstance(ce, bool) and ce > 0 else ""
    sig = l.get("signature") if isinstance(l.get("signature"), list) else []
    out.append(l["name"] + "\x1e" + "\x1f".join(resolve_prefix_token(a, troot) for a in (l.get("argv") or []))
               + "\x1e" + ce + "\x1e" + "\x1f".join(resolve_prefix_token(a, troot) for a in sig))
sys.stdout.buffer.write(("\n".join(out) + "\n").encode())
' "$ATMP/manifest-at-R" "$(dirname "$KITREL")" > "$ATTR_ROWS" 2>/dev/null || ATTR_ROWS_STATE=unparseable
    fi
    # The worktree lives under the git COMMON dir, made absolute, as the baseline runner places its own.
    gcd=$RG_COMMON_RAW
    case "$gcd" in /*|[A-Za-z]:/*) : ;; '') gcd="$GD" ;; *) gcd="$ROOT/$gcd" ;; esac
    ATTR_WT_PATH="$gcd/gate-attr.$$"
    write_normaliser "$ATTR_NORM" "$ROOT" "$ATTR_WT_PATH" \
      || ATTR_WHY_ALL="the normaliser could not be written into the scratch dir"
  fi

  # THE PASS'S OWN BOUND, printed before it starts: the sum of the red legs' R ceilings.
  for i in $RED_LEGS; do
    row=$(read_row_at "${names[$i]}")
    [ -n "$row" ] || continue
    IFS="$ATTR_RS" read -r _ _ rce _ <<<"$row"
    rce=${rce:-$PROF_TIMEOUT}
    case "$rce" in ''|0|*[!0-9]*) unbounded=$((unbounded + 1)) ;; *) sum=$((sum + rce)) ;; esac
  done
  printf 'run-gates: attributing red legs against %s; bound %ss, the sum of their R ceilings' "$ATTR_R8" "$sum"
  [ "$unbounded" -gt 0 ] && printf ', plus %s leg(s) R leaves unbounded' "$unbounded"
  if [ "$WALL" -gt 0 ] && [ "$WALL_END" -gt 0 ]; then
    rem=$(( WALL_END - EPOCHSECONDS ))
    { [ "$sum" -gt "$rem" ] || [ "$unbounded" -gt 0 ]; } \
      && printf ' — it can outrun the %ss the wall has left, and an R run the wall cuts reads DEAD PROBE `cut by the wall`' "$rem"
  fi
  printf '\n'
  # THE AGE PROBE'S BOUND, printed before it starts too (TOOL-dDerivedDocket-24): one run at R~n and a
  # bisection of the window, so at most 1 + ceil(log2 n) more runs of each INHERITED leg, each under
  # R's ceiling for its row and all of them inside the same wall.
  ATTR_FPL=(); ATTR_WT_MOVED=0; ATTR_LANDABLE=0; ATTR_LAND_LEGS=""; land_n=0
  if [ -n "$ATTR_MAX_AGE" ] && [ -n "$ATTR_RSHA" ] && [ -z "$ATTR_WHY_ALL" ]; then
    mapfile -t ATTR_FPL < <(git rev-list --first-parent --max-count=$((ATTR_MAX_AGE + 1)) "$ATTR_RSHA" 2>/dev/null)
    k=1; rem=1; while [ "$rem" -lt "$ATTR_MAX_AGE" ]; do rem=$((rem * 2)); k=$((k + 1)); done
    printf 'run-gates: ageing each INHERITED leg against R~%s on the first-parent line; at most %s more run(s) of that leg, each under its R ceiling\n' "$ATTR_MAX_AGE" "$k"
  fi

  [ -n "$RUNDIR" ] && rec="$RUNDIR/attribution" && : > "$rec" 2>/dev/null
  for i in $(printf '%s\n' $RED_LEGS | LC_ALL=C sort -n -u); do
    m=$((m + 1))
    derive_attribution "$i"
    A_AGE=-; A_OWN8=-; A_OWNID=-; A_AGE_NOTE=""
    if [ "$A_V" = INHERITED ]; then
      derive_age "$i"
      # BACK TO R before the next leg's R run, which reads this same worktree. A worktree that cannot
      # be returned reads every later leg DEAD PROBE rather than grading it at the wrong commit.
      if [ "$ATTR_WT_MOVED" = 1 ]; then
        ATTR_WT_MOVED=0
        git -C "$ATTR_WT" checkout -q -f --detach "$ATTR_RSHA" >/dev/null 2>&1 \
          && git -C "$ATTR_WT" clean -q -f -d -x >/dev/null 2>&1 \
          || ATTR_WHY_ALL="the R worktree could not be returned to R after an age probe"
      fi
    fi
    case "$A_V" in
      INHERITED) tail="INHERITED · offenders $A_I · at $ATTR_R8"
                 case "$A_AGE" in
                   aged) tail="$tail · aged at R~$ATTR_MAX_AGE" ;;
                   -)    [ -n "$A_AGE_NOTE" ] && tail="$tail · age unproven" ;;
                   *)    tail="$tail · age $A_AGE · owner $A_OWN8"
                         [ "$A_OWNID" != - ] && tail="$tail $A_OWNID" ;;
                 esac
                 # EVERY INHERITED LEG COUNTS, whatever its age reads — a number, `aged`, or `-` for
                 # unproven or not asked (TOOL-dUnstuckLanding-16 S1). The age escalates the ask; it
                 # no longer decides whether the leg lands.
                 land_n=$((land_n + 1)); ATTR_LAND_LEGS="$ATTR_LAND_LEGS${ATTR_LAND_LEGS:+,}${names[$i]}" ;;
      MIXED)     tail="MIXED · inherited $A_I · own $A_O · at $ATTR_R8" ;;
      *)         tail="$A_V · $A_WHY" ;;
    esac
    if [ "$A_V" = "DEAD PROBE" ]; then dead=$((dead + 1)); else nattr=$((nattr + 1)); fi
    printf 'GATE attr  %s  %s\n' "${names[$i]}" "$tail"
    # THE ROW: leg · verdict · inherited · own · R sha · age · owner sha8 · owner id · reason, the
    # reason LAST as the red-attribution unit requires, the three age columns inserted before it.
    if [ -n "$rec" ]; then
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "${names[$i]}" "$A_V" "$A_I" "$A_O" "${ATTR_RSHA:--}" \
        "$A_AGE" "$A_OWN8" "$A_OWNID" \
        "$(printf '%s%s' "$A_WHY" "${A_AGE_NOTE:+; $A_AGE_NOTE}" | tr '\t\n\r' '   ')" >> "$rec" 2>/dev/null || true
    fi
  done
  # LANDABLE, for the inherited-green stamp alone: every red leg reads INHERITED, at any age. The
  # stamp's other preconditions are the full green's, read where it is written.
  [ "$m" -gt 0 ] && [ "$land_n" = "$m" ] && ATTR_LANDABLE=1
  summary="attributed $nattr of $m red legs against $ATTR_R8"
  [ "$dead" -gt 0 ] && summary="$summary · DEAD PROBE $dead"
  printf '%s\n' "$summary"
  [ -n "$rec" ] && chmod 600 "$rec" 2>/dev/null
  if [ -n "$ATTR_WT" ]; then
    remove_scratch_worktree "$ATTR_WT" \
      || echo "run-gates: the R worktree at $ATTR_WT could not be removed — remove it by hand" >&2
    ATTR_WT=""
  fi
  return 0
}

# live -> LIVE_N, the count of RUNNING jobs, `jobs -rp`'s meaning unchanged: the listing goes to a
# work-dir file and `mapfile` counts it, all in this shell, where `$(live)` and its `| wc -l` were a
# fork and an exec per call on every pass of the reader (TOOL-aSparedSpawn-4 S6).
live() {
  local -a pids=()
  jobs -rp > "$WORK/live.pids" 2>/dev/null
  { mapfile -t pids < "$WORK/live.pids"; } 2>/dev/null
  LIVE_N=${#pids[@]}
}
while [ "$wi" -lt "$nwalk" ]; do
  [ -f "$WORK/wall.breach" ] && break
  next=${WALK[$wi]}
  # THE CHUNK BOUNDARY. The walk is grouped, so a change of chunk here is the end of the previous
  # one — every leg of it has printed, because the reader never advances past a leg with no result.
  if [ "${chunks[$next]}" != "$cur_chunk" ]; then chunk_close; cur_chunk=${chunks[$next]}; fi
  di_before=$di
  # THE RUNNING COUNT IS CAPTURED from the test that already takes it, so the memory pause's decision
  # below asks nothing again and adds no spawn (TOOL-aGraftedHelix-7).
  while [ "$di" -lt "$ndisp" ] && { live; nlive=$LIVE_N; [ "$nlive" -lt "$JOBS" ]; }; do
    k=${disp[$di]}; di=$((di+1))
    { [ -z "${names[$k]}" ] || [ -f "$WORK/$k.rc" ]; } && continue   # sentinel, or already decided by the guard pass
    # A HOLD steps the index back and leaves the pass: the reader below then blocks on `wait -n` as it
    # does with a full pool, and a hold only happens while a leg runs, so that wait returns. The next
    # completion re-decides for this same leg.
    if check_dispatch_pause "$nlive"; then di=$((di-1)); break; fi
    arm_wall
    arm_census
    runleg "$k" &
  done
  # THE TAIL RELEASE (TOOL-aSparedSpawn-3 S2), once every first attempt is dispatched: a deferred leg's
  # retry starts here, beside at most one running job, rather than after the final `wait`.
  [ "$di" -lt "$ndisp" ] || run_tail_retry
  if [ -f "$WORK/$next.rc" ]; then report_one "$next"; wi=$((wi+1)); continue; fi
  live; if [ "$LIVE_N" -gt 0 ]; then wait -n 2>/dev/null || true; continue; fi
  # Nothing running. That is NOT yet evidence this leg has no result: `jobs -rp` counts only RUNNING
  # jobs, so a worker that finished between the file check and the count is invisible, and with
  # instant legs the pool can drain faster than the reader walks. Exhaust dispatch, reap everything,
  # and re-check before declaring a leg dead — an earlier revision skipped this and reported a
  # perfectly healthy leg as "(no result)" roughly one run in three.
  if [ "$di" -lt "$ndisp" ]; then
    # Nothing is running and legs remain. Normally the pass above dispatched one; if it dispatched
    # NOTHING, force one here so every iteration makes progress and the loop can never spin.
    # Falling through to the report instead would declare an UNDISPATCHED leg dead, and that is not
    # hypothetical: guarding on "did this pass advance?" did exactly that. The window is a worker
    # that is live when the dispatch pass looks (so nothing dispatches) and finished by the liveness
    # check (so nothing is waited on), and the timing cache makes it common by decoupling dispatch
    # order from manifest order — measured at 6 of 30 legs falsely reported, on the second run only,
    # because the first run is the one with no cache.
    if [ "$di" -eq "$di_before" ]; then
      k=${disp[$di]}; di=$((di+1))
      # THE SECOND DISPATCH SITE decides too, with nothing running: a held leg reaches this branch when
      # its runners finished between the pass's count and the liveness test, and its episode must close
      # `drained` here, or it would outlive the loop and close as `wall` with no wall fired.
      if [ -n "${names[$k]}" ] && [ ! -f "$WORK/$k.rc" ]; then check_dispatch_pause 0; runleg "$k" & fi
    fi
    continue
  fi
  wait                                     # everything dispatched and nothing running: reap, look once more
  [ -f "$WORK/$next.rc" ] && continue
  report_one "$next"; wi=$((wi+1))         # genuinely no result: report it, never hang
done
# An episode open now is one the wall's break left, or a tail release the pause held until the reader
# finished (TOOL-aSparedSpawn-3), whose leg then takes its serial retry: that one closes `drained`.
if [ -f "$WORK/wall.breach" ]; then write_pause_row wall; else write_pause_row drained; fi
wait
chunk_close                                # the last chunk has no successor to close it
# THE MEMORY PAUSE'S ONE LINE, after the pool drains and before the serial retry, so a run the wall
# stopped prints it too. Its peak varies with the host, so a whole-output reader filters it by name.
render_pause_summary
render_spawn_summary
# ONE I3 LINE PER BAR THAT PAUSED, never one per episode (TOOL-aGraftedHelix-8): the summary's counts.
[ "$MEMPAUSE_N" = 0 ] || add_health_event "$RG_HEALTH_LOG" run-gates dispatch-paused \
  "$MEMPAUSE_N pause(s) ${MEMPAUSE_HELD_S}s held peak ${MEMPAUSE_PEAK:-?}% threshold ${MEMPAUSE:-0}% fell $MEMPAUSE_FELL bound $MEMPAUSE_BOUND drained $MEMPAUSE_DRAINED unread $MEMPAUSE_UNREAD wall $MEMPAUSE_WALL"
# THE SERIAL RETRY, after the pool drains and INSIDE the wall (TOOL-dDerivedDocket-26 S1), and before
# the attribution below, which reads the red set the retry decides and each red leg's FIRST attempt.
run_leg_retry
# THE SAMPLE'S VERDICT (TOOL-aSparedSpawn-13 S6), after the serial retry and inside the wall. A drawn leg
# executed as an ordinary one; its effective verdict is its retry's where it had one. Green agrees. Red
# against the cached `ok` it was drawn from has ALREADY redded the run through its own `GATE FAIL`, and
# runs once more, alone, only to say which it was: red again is a `cache disagreement`, and the entry
# goes; green is `nondeterministic`. Either quarantines the leg against its current row hash, so it is
# never reused again until its manifest row changes. Backgrounded and waited on, as the serial retry is,
# because the wall's handle on a leg is the worker's own pid.
#
# EVERY OTHER EXECUTION TOO (TOOL-aSparedSpawn-17): a leg the age bound forced, or one a plain or push
# bar executed, whose effective verdict is red while its key holds an `ok`, is a disagreement as well.
# It runs nothing more, since its retry already gave a second look where one was due: the line, the
# entry erased, the quarantine. Otherwise the stale `ok` outlives the red and its age resets below, so a
# retried push of the same sha could reuse it. The skip set is the cache block's; every read is a builtin.
if [ -n "$REUSE_CACHE" ]; then
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    _src="$WORK/$i.rc"; [ -f "$WORK/$i.retry.rc" ] && _src="$WORK/$i.retry.rc"
    _rc=""; { IFS= read -r _rc < "$_src"; } 2>/dev/null
    if [ -f "$WORK/$i.sampled" ]; then
      _key=""; { IFS= read -r _key < "$WORK/$i.sampled"; } 2>/dev/null
      if [ "$_rc" = 0 ]; then
        printf 'run-gates: sampled %s — it executed against its cached ok and agreed\n' "${names[$i]}" >&2
        continue
      fi
      runleg "$i" .sample &
      wait "$!" 2>/dev/null
      _rc2=""; { IFS= read -r _rc2 < "$WORK/$i.sample.rc"; } 2>/dev/null
      if [ "$_rc2" = 0 ]; then
        printf 'nondeterministic · %s\n' "${names[$i]}"
      else
        printf 'cache disagreement · %s · %s\n' "${names[$i]}" "$_key"
        [ "${#_key}" -ge 3 ] && rm -f "$REUSE_CACHE/${_key:0:2}/$_key" 2>/dev/null
      fi
    else
      case "$_rc" in ''|0|ondemand|skip|docskip|reuse) continue ;; esac
      _key=${INPUT_KEYS[$i]:--}
      [ "$_key" != - ] && [ "${#_key}" -ge 3 ] || continue
      _st=""; { IFS=$'\t' read -r _st _ < "$REUSE_CACHE/${_key:0:2}/$_key"; } 2>/dev/null
      [ "$_st" = ok ] || continue
      printf 'cache disagreement · %s · %s\n' "${names[$i]}" "$_key"
      rm -f "$REUSE_CACHE/${_key:0:2}/$_key" 2>/dev/null
    fi
    printf '%s' "${rowhashes[$i]}" > "$REUSE_CACHE/quarantine.${heldkeys[$i]}" 2>/dev/null \
      || printf 'run-gates: %s could not be quarantined\n' "${names[$i]}" >&2
  done
fi
unset _key _src _rc _rc2 _st
# AFTER the pool drains and every leg has its verdict, and BEFORE the watcher goes: the wall bounds
# the bar and its attribution together (TOOL-dDerivedDocket-23 F6). A no-op unless asked and red.
run_attribution
remove_wall_watcher
remove_census_watcher

# THE LEDGER. It replaces the old `gate-timings.tsv` rather than sitting beside it: two stores of
# one fact, with the older one read by the only tool that grades the newer, is exactly the shape
# this record exists to remove. Field 2 is still the duration, which is what lets the manifest
# parser above read it as a dispatch hint with no edit at all.
#
# Rows, nine tab-separated fields: name, seconds, status, input key, ended-at, run, full,
# manifest_blob, head. The last four are the run that wrote the row: its id, `1` when it ran with
# GATE_FULL on a CLEAN tree that did NOT move while the bar ran, and empty otherwise, the leg
# manifest blob it read, and the sha it graded (TOOL-aFrugalTurnstile-4 S1). They are what the
# `lineage` mode tests, and a carried-forward row keeps the run that EXECUTED it. Advisory for
# dispatch, DURABLE for the lineage mode that reads the key; the `env` and `push` modes read the reuse
# cache in the common dir instead (TOOL-aSparedSpawn-13 S4) — a failed write costs wall clock, never a
# verdict. A moved tree blanks `full` (TOOL-aFrugalTurnstile-14 S1): its keys may describe content
# other than what the leg graded, and a lineage reuse of them could stamp a full green.
FPRINT_END=$(fingerprint)
tree_moved=no
[ -n "$FPRINT_START" ] && [ -n "$FPRINT_END" ] && [ "$FPRINT_START" != "$FPRINT_END" ] && tree_moved=yes
if [ -n "$LEDGER" ]; then
  # THE MERGE IS STAGED BESIDE THE LEDGER, under a name nobody can know before `cp` creates it
  # (TOOL-dRedressedBar-24). A fixed staging name in the scratch dir, which sits in the shared temp
  # dir, let a process that can write there plant a link the merge then wrote through.
  new="$WORK/ledger.new"; derive_temp_path merged "$LEDGER"; : > "$new"
  lfull=""; [ -n "${GATE_FULL:-}" ] && [ "$TREE_CLEAN" = yes ] && [ "$tree_moved" = no ] && lfull=1
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.sec" ] || continue
    lst=ok; lkey=-; lend=""; lsec="$WORK/$i.sec"
    if [ -n "$RUNDIR" ] && [ -f "$RUNDIR/$i.leg" ]; then
      # THE TRAILING `_` takes field 8, `foreign` (TOOL-aGraftedHelix-5): without it the key read
      # absorbed `<key>TAB<foreign>`, and a TAB inside the key breaks the ledger's nine-field grammar.
      IFS=$'\t' read -r _ lst _ _ _ lend lkey _ < "$RUNDIR/$i.leg" 2>/dev/null || { lst=ok; lkey=-; }
    fi
    # A RETRIED LEG takes its retry's seconds and the status `retried`, whatever the retry did
    # (TOOL-dDerivedDocket-26 S2). The seconds are the leg's cost ALONE, which is the better dispatch
    # hint; the status says a pass needed a second attempt, and the reuse cache writes no entry for
    # one (its first attempt was no `ok`), so it is never copied forward as a proven green.
    if [ -f "$WORK/$i.retry.sec" ]; then
      lsec="$WORK/$i.retry.sec"; lst=retried
      [ -n "$RUNDIR" ] && [ -f "$RUNDIR/$i.retry.leg" ] \
        && IFS=$'\t' read -r _ _ _ _ _ lend _ < "$RUNDIR/$i.retry.leg" 2>/dev/null
    fi
    # A RED leg's row carries no key: a key on a failed row would be a true statement about the
    # inputs and a dangerous one about the verdict, for any reader that took it for a reusable one.
    [ "$lst" = ok ] || lkey=-
    # The seconds by the builtin, a one-line file whose `$(cat …)` was a fork and an exec per leg
    # (TOOL-aSparedSpawn-4 S6).
    lsv=""; { IFS= read -r lsv < "$lsec"; } 2>/dev/null
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "${names[$i]}" "$lsv" "$lst" "$lkey" "$lend" \
      "$RUNID" "$lfull" "$MANIFEST_BLOB" "$HEAD_SHA" >> "$new"
  done
  # A guard-SKIPPED leg never enters runleg(), so it produces no .sec. Rewriting the file from this
  # run's rows alone therefore DELETED the cached duration of every skipped leg — and the runs where
  # guards fire are exactly the diff-scoped ones, so a scoped run blanked the dispatch hint the next
  # full run depends on. Carry forward any cached row this run did not measure. A leg dropped from the
  # manifest falls out on its own, because the python side keys the hint on the manifest's names.
  # KEYED ON THE FILE NAME, never `NR==FNR` (TOOL-aSparedSpawn-3 S7): with an EMPTY first file, which a
  # run that reused or guard-skipped every leg writes, `NR==FNR` holds for every line of the old ledger,
  # so each was swallowed as "seen" and the ledger the next bar dispatches by was left empty.
  cp "$new" "$merged" 2>/dev/null || true
  [ -s "$LEDGER" ] && awk -F'\t' 'FILENAME==ARGV[1]{seen[$1]=1;next} !($1 in seen)' "$new" "$LEDGER" >> "$merged" 2>/dev/null
  # ATOMIC rather than a copy in place. A reader that opens the ledger while the bar is mid-write
  # got a truncated file before; a rename is the only way this file is ever replaced now.
  mv -f "$merged" "$LEDGER" 2>/dev/null || cp "$merged" "$LEDGER" 2>/dev/null || true
  [ -e "$merged" ] && rm -f "$merged" 2>/dev/null
  # THE RETIRED CACHE IS DELETED HERE. Nothing reads `gate-timings.tsv` since the ledger replaced it,
  # yet every node that ran an older runner still holds a copy: a stale second store of one fact that
  # build records had to warn readers not to cite. The runner is the one program every node runs, so it
  # clears its own git dir and the common dir (the turnstile's `TS_COMMON`, empty when that is off).
  # That one filename and nothing else; a failed delete never moves the verdict (TOOL-aMendedFleet-72).
  rm -f "$gd/gate-timings.tsv" ${TS_COMMON:+"$TS_COMMON/gate-timings.tsv"} 2>/dev/null || true
fi

echo "----"
skipnote=""; [ "$skips" -gt 0 ] && skipnote=" ($skips skipped)"
[ "${reuses:-0}" -gt 0 ] && skipnote="$skipnote (${reuses} reused)"
# THE HELD LEGS ARE NAMED, exactly as a guard-skip and a reuse are, and for the same reason: a
# total that shrank silently reads as a bar that shrank for reasons nobody recorded. Naming the
# population is what keeps the smaller number from being a smaller lie. TOOL-dUnstalledConvoy-31.
[ "${ondemands:-0}" -gt 0 ] && skipnote="$skipnote (${ondemands} held: subject kit or chunk selftests, GATE_SELFTESTS=1 runs them)"
# A RETRIED LEG IS NAMED IN THE TOTAL TOO (TOOL-dDerivedDocket-26 S2): a green that needed a second
# attempt is green, and a reader of the one summary line should still be able to see it was one.
[ "${RETRIED:-0}" -gt 0 ] && skipnote="$skipnote (${RETRIED} retried after timeout)"

# THE COUNT THAT RAN, computed ONCE and read by the verdict record, the durable summary and stdout.
# Three call sites recomputing one figure is how two of them end up disagreeing, and this figure is
# the one a reader quotes. A leg that was held did not run, so counting it in the total is the
# green-by-absence class stated as arithmetic. TOOL-dUnstalledConvoy-31.
ran=$((n-skips-${ondemands:-0}))

# A BAR THAT RAN NOTHING BECAUSE EVERYTHING WAS HELD IS NOT A GREEN BAR. It is the loudest possible
# green-by-absence: a repository whose whole manifest is kit-subject would print `gates GREEN` on
# every run forever while executing not one leg, and the record it stamps would say so too.
# NARROW ON PURPOSE — guard-skips and reuses are ORDINARY reasons for a leg not to run, and a scoped
# run over an untouched tree legitimately executes nothing. This fires only when the on-demand hold
# is the SOLE reason: nothing ran, nothing was skipped, nothing was reused, and something was held.
# Exit 2, the runner's own configuration-refusal code, never 0 and never 1. TOOL-dUnstalledConvoy-26.
# THE BREACH VERDICT COMES FIRST, above every other exit path, and the ordering is a fix rather than
# a preference. A breach leaves `fails` at 0 and `ran` at 0 on the break path, so on a manifest whose
# walked legs were all held self-tests it satisfied every clause of the refusal below and exited 2
# announcing "this run executed NOTHING" -- a hang reported as operator error. Hoisted here it cannot.
if [ -f "$WORK/wall.breach" ]; then
  WALL_STUCK=""
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    # A SERIAL RETRY IN FLIGHT is named as one (TOOL-dDerivedDocket-26): its first attempt has an
    # `.rc`, so the test below it would skip the very leg the wall stopped.
    if [ -f "$WORK/$i.retry.pid" ] && [ ! -f "$WORK/$i.retry.rc" ]; then
      WALL_STUCK="${WALL_STUCK}  still running at the wall: ${names[$i]} (its serial retry)
"
      continue
    fi
    [ -f "$WORK/$i.rc" ] && continue
    [ -f "$WORK/$i.pid" ] || continue
    WALL_STUCK="${WALL_STUCK}  still running at the wall: ${names[$i]}
"
  done
  # A WALL THAT FIRED DURING THE RED ATTRIBUTION found every leg returned, and says which pass it cut
  # rather than reading as a wall that fired on nothing.
  [ -z "$WALL_STUCK" ] && [ "${ATTR_CUT:-0}" = 1 ] && WALL_STUCK="  cut by the wall: the red attribution pass, after every leg had returned
"
  [ -n "$WALL_STUCK" ] || WALL_STUCK="  (no leg was still marked running — the wall fired as the last leg returned)
"
  [ -n "$sfile" ] && { printf '%s
' "$PROF_LINE"; printf '%s
' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf '%b' "$WALL_STUCK"; printf 'gates RED — the %ss wall fired; the run was killed, not the legs
' "$WALL"; } >"$sfile" 2>/dev/null || true
  if [ -n "$gd" ]; then
    { printf '%s
' "$PROF_LINE"; printf '%s
' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf '%b' "$WALL_STUCK"; printf 'gates RED — the %ss wall fired; the run was killed, not the legs
' "$WALL"; } >"$gd/gate-last-failure.txt" 2>/dev/null || true
  fi
  printf '%b' "$WALL_STUCK"
  echo "gates RED — the ${WALL}s wall fired; the run was killed, not the legs"
  # THE RUN RECORD GETS ITS VERDICT BEFORE THIS EXIT. This block `exit 1`s above the verdict
  # writer at the foot of the file, so a breach left a run directory with a header and NO
  # verdict -- which is precisely the state this runner documents as its crash signal. A wall
  # firing is the most deliberate outcome the runner has and it was recording itself as a crash,
  # so the one condition the wall exists to make legible was the one it made unreadable. The
  # `[ -f "$WORK/wall.breach" ] && gate_verdict=RED` line further down could never fire for the
  # same reason, and its own neighbour comment already said so. TOOL-aQuenchedHarness-1,
  # corrected in TOOL-aQuenchedHarness-7's closing pass.
  if [ -n "$RUNDIR" ]; then
    derive_temp_path _tp "$RUNDIR/verdict"
    {
      printf 'ended\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
      printf 'verdict\t%s\n' RED
      printf 'ran\t%s\n' "$ran"
      printf 'failed\t%s\n' "$fails"
      printf 'skipped\t%s\n' "$skips"
      printf 'held\t%s\n' "${ondemands:-0}"
      printf 'reused\t%s\n' "$reuses"
      printf 'retried\t%s\n' "${RETRIED:-0}"
      printf 'paused\t%s\n' "$MEMPAUSE_N"
      printf 'paused_s\t%s\n' "$MEMPAUSE_HELD_S"
      printf 'wall_breach\t%s\n' "$WALL"
    } > "$_tp" 2>/dev/null && mv -f "$_tp" "$RUNDIR/verdict" 2>/dev/null || true
    chmod 600 "$RUNDIR/verdict" 2>/dev/null || true
  fi
  exit 1
fi

if [ "$fails" = 0 ] && [ "$ran" -le 0 ] && [ "${ondemands:-0}" -gt 0 ] \
   && [ "$skips" = 0 ] && [ "${reuses:-0}" = 0 ]; then
  echo "run-gates: every leg in this manifest is subject=kit and the self-tests were not asked for,"
  echo "run-gates: so this run executed NOTHING. Refusing to report a green over an empty population."
  echo "run-gates: run it as GATE_SELFTESTS=1, or give this manifest at least one repo-subject leg."
  # A VERDICT IS WRITTEN BEFORE THE EXIT. The run record's ABSENCE is this runner's crash signal —
  # a directory with a header and no verdict means the process died — so exiting between the two
  # manufactures that signature for a deliberate refusal, and leaves the PREVIOUS run's `gates
  # GREEN` standing in gate-last-summary.txt for anyone who reads the durable record instead of the
  # terminal. Both records say REFUSED instead. TOOL-dUnstalledConvoy-26.
  if [ -n "$RUNDIR" ]; then
    derive_temp_path _tp "$RUNDIR/verdict"
    { printf 'ended\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
      printf 'verdict\tREFUSED\n'
      printf 'ran\t0\n'
      printf 'failed\t0\n'
      printf 'skipped\t%s\n' "$skips"
      printf 'held\t%s\n' "${ondemands:-0}"
      printf 'reused\t0\n'
      printf 'retried\t0\n'
      printf 'paused\t%s\n' "$MEMPAUSE_N"
      printf 'paused_s\t%s\n' "$MEMPAUSE_HELD_S"
    } > "$_tp" 2>/dev/null && mv -f "$_tp" "$RUNDIR/verdict" 2>/dev/null || true
    chmod 600 "$RUNDIR/verdict" 2>/dev/null || true
  fi
  [ -n "$sfile" ] && printf 'gates REFUSED — every leg is a held kit self-test, so this run executed nothing\n' >"$sfile" 2>/dev/null || true
  exit 2
fi

# ---- the verdict, the full-green stamp, and the sweep --------------------------------------
# `reuses` feeds the fourth full-green precondition, counted by the reuse verb above. A run that
# reused a leg from the CACHE, `cache_reuses`, has not proven the whole bar, so it cannot stamp a full
# green. A `lineage` reuse is different in kind (TOOL-aFrugalTurnstile-4 S3): its verdict was EARNED
# by a full run on a clean tree, same manifest, an ancestor of HEAD, under an equal input key, so the
# stamp asks that every reuse was one of those AND that none came from the cache (TOOL-aSparedSpawn-32
# S8). The inherited-green stamp keeps "reused nothing".
reuses=${reuses:-0}; lineage_reuses=${lineage_reuses:-0}; cache_reuses=${cache_reuses:-0}
# `tree_moved` is computed ABOVE the ledger block, which reads it (TOOL-aFrugalTurnstile-14 S1).

# THE HELD-TIER LAST-RUN RECORDS (TOOL-aSparedSpawn-12 S4), which the `changed` selection reads. Per
# held leg that EXECUTED under any non-empty `GATE_SELFTESTS`: a first-attempt green on a tree that was
# clean when the run started and did not move writes `<common dir>/gate-selftest-last/<name key>`
# (HEAD and the manifest row hash, tmp then rename); any other ending, a red, a timeout whose retry
# passed or no result, removes it, so a red suite keeps executing until it is fixed. A green on a
# dirty or moved tree leaves the record as it was, and a held, skipped or reused leg did not execute
# and leaves it too. One file per leg, so two bars finishing together lose no row. A wall breach
# exits above this block, so its legs keep the records an earlier green earned on inputs that the
# next selection still diffs against.
if [ -n "${GATE_SELFTESTS:-}" ] && [ -n "$HELD_DIR" ] && [ -n "$RG_HEAD" ]; then
  mkdir -p "$HELD_DIR" 2>/dev/null || true
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    { [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; } || continue
    [ -n "${heldkeys[$i]}" ] || continue
    _hrc=""; { IFS= read -r _hrc < "$WORK/$i.rc"; } 2>/dev/null
    case "$_hrc" in ondemand|skip|docskip|reuse) continue ;; esac
    _hfile="$HELD_DIR/${heldkeys[$i]}"
    if [ "$_hrc" = 0 ]; then
      [ "$TREE_CLEAN" = yes ] && [ "$tree_moved" = no ] || continue
      derive_temp_path _tp "$_hfile"
      printf 'sha\t%s\nrow\t%s\n' "$RG_HEAD" "${rowhashes[$i]}" > "$_tp" 2>/dev/null \
        && mv -f "$_tp" "$_hfile" 2>/dev/null || true
    else
      rm -f "$_hfile" 2>/dev/null || true
    fi
  done
  unset _hrc _hfile
fi

# THE REUSE CACHE (TOOL-aSparedSpawn-13 S4 S5 S7), in the git common dir so every worktree of the clone
# shares it, and never in a ref, so nothing pushes it. Per leg that executed `ok` on its FIRST attempt,
# on a tree that was clean when the run started and did not move, with a measured key and no legacy
# `impure`: one entry under `<key[0:2]>/<key>`, `ok<TAB>secs<TAB>run id<TAB>HEAD<TAB>ended epoch<TAB>reuses`,
# the reuse count 0, which is the only reset the count has (TOOL-aSparedSpawn-16 S11): an execution
# under another key touches nothing of this one, and an executed red writes nothing. A held or skipped
# leg did not execute and writes nothing, and a reused one rewrites only its count, so a wrong entry
# cannot carry itself forward past the age bound. A `remote` leg
# writes only when the remote is probed again after the legs end and still advertises what it was
# keyed on (S9). Every write, tmp then rename, and the 30-day prune by mtime run in ONE python
# process, so a bar pays one spawn for them however many legs it records; any failure there costs a
# saving, never a verdict.
if [ -n "$REUSE_CACHE" ] && [ -n "$RG_HEAD" ]; then
  _cw="$WORK/cache.writes"; : > "$_cw"; _cw_remote=0
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    _crc=""; { IFS= read -r _crc < "$WORK/$i.rc"; } 2>/dev/null
    case "$_crc" in ''|ondemand|skip|docskip|reuse) continue ;; esac
    [ "$_crc" = 0 ] && [ "$TREE_CLEAN" = yes ] && [ "$tree_moved" = no ] || continue
    _ck=${INPUT_KEYS[$i]:--}
    [ "$_ck" != - ] && [ "${#_ck}" -ge 3 ] || continue
    _csec=""; { IFS= read -r _csec < "$WORK/$i.sec"; } 2>/dev/null
    case ",${legreads[$i]}," in
      *,impure,*) continue ;;
      *,remote,*) [ -n "$REMOTE_OBS" ] || continue; _cr=1; _cw_remote=1 ;;
      *) _cr=0 ;;
    esac
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$_ck" "${_csec:-0}" "${RUNID:--}" "$RG_HEAD" "$EPOCHSECONDS" "$_cr" >> "$_cw"
  done
  # THE SECOND PROBE: the remote moved while its legs ran, so their verdicts answer a question no key
  # names. Their rows are dropped; every other row stands.
  if [ "$_cw_remote" = 1 ] && { ! read_remote_heads || [ "$REMOTE_HEADS" != "$REMOTE_OBS" ]; }; then
    printf 'run-gates: reuse — the remote advertised something else after its legs ran, so no remote leg is cached\n' >&2
    _cwl=(); { mapfile -t _cwl < "$_cw"; } 2>/dev/null
    : > "$_cw"
    for _l in ${_cwl[@]+"${_cwl[@]}"}; do [ "${_l##*$'\t'}" = 1 ] || printf '%s\n' "$_l" >> "$_cw"; done
  fi
  if [ -s "$_cw" ] || [ "$REUSE_MODE" != off ]; then
    # -I: this program runs from $ROOT, where a top-level tempfile.py would shadow the stdlib module (TOOL-dRedressedBar-26)
    "$PYBIN" -I -c '
import os, sys, tempfile, time
root = sys.argv[1]
for line in sys.stdin.read().splitlines():
    f = line.split("\t")
    if len(f) < 5 or len(f[0]) < 3:
        continue
    key, tmp = f[0], ""
    try:
        d = os.path.join(root, key[:2])
        os.makedirs(d, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=d, prefix=key + ".", suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("ok\t" + "\t".join(f[1:5]) + "\t0\n")
        os.replace(tmp, os.path.join(d, key))
    except OSError:
        if tmp:
            try:
                os.remove(tmp)
            except OSError:
                pass
cut = time.time() - 30 * 86400
for sub in (os.listdir(root) if os.path.isdir(root) else []):
    p = os.path.join(root, sub)
    if len(sub) != 2 or not os.path.isdir(p):
        continue
    for n in os.listdir(p):
        try:
            if os.path.getmtime(os.path.join(p, n)) < cut:
                os.remove(os.path.join(p, n))
        except OSError:
            pass
' "$REUSE_CACHE" < "$_cw" 2>/dev/null || printf 'run-gates: reuse — the cache at %s was not written\n' "$REUSE_CACHE" >&2
  fi
  unset _cw _cw_remote _crc _ck _csec _cr _cwl _l
fi
# THE BREACH IS READ HERE, from the marker and not from `fails`. A killed leg writes no `.rc`, so
# whether `fails` moved at all is a RACE between the watcher's kill and the reader's report -- both
# outcomes were reproduced. The marker is the only fact that is true on every path, so the durable
# record reads it directly. Without this line the run record wrote `verdict GREEN / ran 0 / failed 0`
# over a bar whose legs the wall had just SIGKILLed, and that file's absence is this runner's
# documented crash signal: a breach left a plausible green one instead.
gate_verdict=GREEN; [ "$fails" = 0 ] || gate_verdict=RED
# HOST ONLY WHEN EVERY FAILED LEG IS HOST (TOOL-dDerivedDocket-26 S5). A bar with one leg that failed
# for a reason of its own is RED whatever else timed out, and its RED line names the HOST legs; HOST
# is a claim about the host, and one real failure is enough to make the claim unsafe to act on.
[ "$gate_verdict" = RED ] && [ "${HOST_N:-0}" -gt 0 ] && [ "$HOST_N" = "$fails" ] && gate_verdict=HOST
[ -f "$WORK/wall.breach" ] && gate_verdict=RED
# NO LEG LINE, NO GREEN (TOOL-dDerivedDocket-26 S6). A bar that reported not one leg -- an empty
# manifest is the reachable case -- has graded nothing, and exit 0 over it is the zero-verdict pass
# the push boundary cannot tell from a real one. It is REFUSED, and that outranks everything below.
[ "$gate_verdict" = GREEN ] && [ "$n" = 0 ] && gate_verdict=REFUSED
# A MOVED TREE OUTRANKS GREEN AND NOTHING ELSE (TOOL-dDerivedDocket-25 S5). A bar whose tree changed
# under it graded a tree that no longer exists — it may have graded a mixture — so exit 0 over it
# asserted something nobody observed, and until this line that is exactly what the runner did: the
# stamp below already refused it, and the verdict and the exit code did not. It never outranks a
# red: a failed leg is a real finding about SOME tree, and exit 3 over it would hide that, so a bar
# that failed AND moved stays RED with exit 1 and its RED line names the move.
[ "$gate_verdict" = GREEN ] && [ "$tree_moved" = yes ] && gate_verdict="TREE MOVED"

if [ -n "$RUNDIR" ]; then
  # WRITTEN LAST, and its ABSENCE is the crash signal — the only one needed. A run that dies
  # anywhere between the header and here leaves a directory with a header and no verdict, which
  # is unambiguous and costs no watchdog, no heartbeat and no second mechanism.
  # `GATE_VERDICT_FAULT` is an ARM SEAM, not a conf key (TOOL-dDerivedDocket-26 S6): it points this
  # write into a directory that does not exist, which is the only way to reach the refusal below that
  # will not certify a green whose record was never written.
  derive_temp_path _vtmp "$RUNDIR/verdict"
  [ -n "$VERDICT_FAULT" ] && derive_temp_path _vtmp "$RUNDIR/verdict-fault/verdict"
  {
    printf 'ended\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'verdict\t%s\n' "$gate_verdict"
    printf 'ran\t%s\n' "$ran"
    printf 'failed\t%s\n' "$fails"
    printf 'skipped\t%s\n' "$skips"
    printf 'held\t%s\n' "${ondemands:-0}"
    printf 'reused\t%s\n' "$reuses"
    printf 'fingerprint_end\t%s\n' "$FPRINT_END"
    printf 'tree_moved\t%s\n' "$tree_moved"
    # How many deferred legs ran again, pass or fail (TOOL-dDerivedDocket-26 S2). The drift report
    # sums it across the records it can read.
    printf 'retried\t%s\n' "${RETRIED:-0}"
    # The memory pause's episodes and the seconds they held, summed (TOOL-aGraftedHelix-7).
    printf 'paused\t%s\n' "$MEMPAUSE_N"
    printf 'paused_s\t%s\n' "$MEMPAUSE_HELD_S"
  } > "$_vtmp" 2>/dev/null && mv -f "$_vtmp" "$RUNDIR/verdict" 2>/dev/null || true
  chmod 600 "$RUNDIR/verdict" 2>/dev/null || true
fi

# THE FULL-GREEN STAMP, and its five preconditions are the whole of what makes its name true.
# An implementation that forgets ONE of them still passes every arm written for the others, which
# is why each has its own negative control in the evidence harness.
#
#   failed nothing  · skipped nothing  · reused nothing but lineage-qualified legs, and nothing from
#   the cache  · the tree did not move  · the tree was CLEAN when the run started
#
# The last one is the one a spec audit found missing. A developer's ordinary full run on a dirty
# tree would otherwise stamp a green that the push boundary later treats as proof about a tree
# nobody ever tested.
# A SIXTH PRECONDITION, and it is deliberately the MARKER rather than `fails`: a wall breach leaves
# `fails` at zero, because a killed leg writes no `.rc`. The verdict block above already exits on a
# breach, so this can never fire today — and that is exactly why it is here. A guard that reads the
# same state the bug corrupts is disabled by the bug it exists to catch.
# A SEVENTH, TOOL-dDerivedDocket-26 S6: the verdict is GREEN and its file was WRITTEN. A bar that
# refuses its own exit 0 below must not have left the stamp a later push trusts in its place.
#
# WHICH MANIFEST BOTH STAMPS RAN (TOOL-aFrugalTurnstile-1 S3, design D2). The blob alone cannot say
# which file it hashed, so a nested runner inside an adopter's wrapper bar stamped a green of this
# kit's subset that only an accidental blob mismatch kept the push boundary from trusting as the whole
# bar. Repo-relative, the spelling the pre-push hook compares with its kit sibling: a leading `./` (a
# root install's `dirname` answers `.`) is stripped; an absolute value is asked of git, in git's one
# spelling, and loses the top-level prefix only where git places it inside THIS work tree; a value git
# cannot place there stays absolute. The run header's own `manifest` key is a different record.
LEGS_REL=${LEGS_FILE#./}
case "$LEGS_REL" in
  /*|?:*) _lr=$(unset GIT_DIR GIT_WORK_TREE; cd "${LEGS_REL%/*}" 2>/dev/null \
                && [ "$(git rev-parse --show-toplevel 2>/dev/null)" = "$ROOT" ] \
                && git rev-parse --show-prefix 2>/dev/null) && LEGS_REL=$_lr${LEGS_REL##*/} ;;
esac
if [ -n "$gd" ] && [ "$fails" = 0 ] && [ "$skips" = 0 ] && [ "$reuses" = "$lineage_reuses" ] \
   && [ "$cache_reuses" = 0 ] && [ ! -f "$WORK/wall.breach" ] \
   && [ "$tree_moved" = no ] && [ "$TREE_CLEAN" = yes ] && [ -n "$FPRINT_START" ] \
   && [ "$gate_verdict" = GREEN ] && [ -f "$RUNDIR/verdict" ]; then
  derive_temp_path _tp "$gd/gate-full-green"
  {
    printf 'sha\t%s\n' "$(git rev-parse HEAD 2>/dev/null)"
    printf 'fingerprint\t%s\n' "$FPRINT_START"
    printf 'manifest_blob\t%s\n' "$MANIFEST_BLOB"
    printf 'manifest\t%s\n' "$LEGS_REL"
    # THE TWO REUSE COUNTS (TOOL-aSparedSpawn-32 S8). `reused` is how many legs this green carried
    # forward rather than ran, `0` when none (TOOL-aFrugalTurnstile-4 S3), every one of them a lineage
    # reuse under the precondition above. `reused_cache` is how many it took from the cache, always 0
    # here. The push boundary's predicate 9 reads the pair: a non-zero `reused_cache`, or a record with
    # no `reused_cache` and a non-zero `reused`, which cannot say its kind, forces the full bar.
    printf 'reused\t%s\n' "$reuses"
    printf 'reused_cache\t%s\n' "$cache_reuses"
    # WHAT THIS GREEN COVERED. Without it a record named `gate-full-green` cannot say
    # whether the kit-subject legs ran, and the push boundary would trust a partial bar as
    # a whole one. The READER of this field is TOOL-dUnstalledConvoy-27; written without
    # that reader it is an inert byte, which is what a spec audit caught rev-2 shipping.
    printf 'selftests\t%s\n' "$SELFTESTS_STAMP"
    printf 'run_id\t%s\n' "$RUNID"
    printf 'stamped\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  } > "$_tp" 2>/dev/null \
    && mv -f "$_tp" "$gd/gate-full-green" 2>/dev/null || true
  # SHARED FROM A LINKED WORKTREE (TOOL-dThriftyLanding-2). The common dir's own `gate-full-green` is
  # the PRIMARY tree's stamp and is never written from here: a branch's green that is no ancestor of
  # the default branch would replace the primary's valid one. A separate `.shared` file, which the push
  # boundary reads LAST, never displaces the primary's record. It is ONE slot per clone:
  # last writer wins, so one linked worktree's green can evict another's; that costs a saving, never a verdict,
  # because the boundary validates it with the same predicates as its own.
  _gcd=$RG_COMMON_RAW
  if [ -n "$_gcd" ] && [ -f "$gd/gate-full-green" ]; then
    _gcd_abs=$(cd "$_gcd" 2>/dev/null && pwd -P) || _gcd_abs=""
    _gd_abs=$(cd "$gd" 2>/dev/null && pwd -P) || _gd_abs=""
    if [ -n "$_gcd_abs" ] && [ -n "$_gd_abs" ] && [ "$_gcd_abs" != "$_gd_abs" ]; then
      # STAGED UNDER A NAME OF ITS OWN (TOOL-aPairedSlots-7): two bars of one repository stamp at
      # once, and a fixed staging name let one bar's `cp` truncate the file the other was moving.
      # Each `mv` now places a whole stamp, and the last writer wins. The name is `derive_temp_path`'s,
      # which no other process can know before `cp` creates it (TOOL-dRedressedBar-24). ONE statement
      # from the call to the `|| true`: the runlog suite's TWO arm extracts and runs it whole.
      derive_temp_path _tp "$_gcd_abs/gate-full-green.shared" \
        && cp "$gd/gate-full-green" "$_tp" 2>/dev/null \
        && mv -f "$_tp" "$_gcd_abs/gate-full-green.shared" 2>/dev/null \
        || rm -f "$_tp" 2>/dev/null || true
    fi
  fi
fi

# THE INHERITED-GREEN STAMP (TOOL-dDerivedDocket-24, KF2). A DIFFERENT FILE from the full green, and
# that is the whole of its safety: no reader of `gate-full-green` can ever take it for one, and this
# block never touches that file. It is written under EVERY precondition of the full green except
# "failed nothing" — skipped nothing, reused nothing, no wall, an unmoved tree that was clean when the
# run started — plus three of its own: the caller exported `land`, at least one leg failed, and every
# failed leg read INHERITED, at any age (TOOL-dUnstuckLanding-16 S1; it required a proven age inside
# the bound until ruling TOOL-dUnstuckLanding-22). No age bound is required either. It records R and
# the bound it was written under, empty when none was handed, because the pre-push hook trusts it only
# where the remote sha it receives equals `base` and the bound it reads at that sha equals `max_age`.
#
# WHAT IT DOES NOT CHECK: the policy itself. `land` here is whatever the caller exported; the hook
# reads the policy at R before it reads this file, so a stamp written under a caller's own `land`
# selects nothing at a boundary whose R says `park`.
if [ -n "$gd" ] && [ "$ATTR_POLICY" = land ] && [ "$ATTR_LANDABLE" = 1 ] \
   && [ "$fails" -gt 0 ] && [ "$skips" = 0 ] && [ "$reuses" = 0 ] && [ ! -f "$WORK/wall.breach" ] \
   && [ "$tree_moved" = no ] && [ "$TREE_CLEAN" = yes ] && [ -n "$FPRINT_START" ] && [ -n "${ATTR_RSHA:-}" ]; then
  derive_temp_path _tp "$gd/gate-inherited-green"
  {
    printf 'sha\t%s\n' "$(git rev-parse HEAD 2>/dev/null)"
    printf 'fingerprint\t%s\n' "$FPRINT_START"
    printf 'manifest_blob\t%s\n' "$(git hash-object -- "$LEGS_FILE" 2>/dev/null)"
    printf 'manifest\t%s\n' "$LEGS_REL"
    printf 'selftests\t%s\n' "$SELFTESTS_STAMP"
    printf 'base\t%s\n' "$ATTR_RSHA"
    printf 'max_age\t%s\n' "$ATTR_MAX_AGE"
    printf 'legs\t%s\n' "$ATTR_LAND_LEGS"
    printf 'reused\t%s\n' "$reuses"   # predicate 9's pair, as on the full green (TOOL-aSparedSpawn-13 S8, -32 S8)
    printf 'reused_cache\t%s\n' "$cache_reuses"
    printf 'run_id\t%s\n' "$RUNID"
    printf 'stamped\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  } > "$_tp" 2>/dev/null \
    && mv -f "$_tp" "$gd/gate-inherited-green" 2>/dev/null || true
  echo "run-gates: inherited-green stamp written — every red leg is INHERITED at ${ATTR_RSHA:0:8}${ATTR_MAX_AGE:+, aged against the ${ATTR_MAX_AGE}-landing bound}: $ATTR_LAND_LEGS"
fi

# THE SWEEP runs AFTER the verdict is written and NEVER before the first leg dispatches. Both
# halves matter: sweeping at the start would delete the crashed run's record an operator came
# back to read, and it can partially fail on this platform against an open handle, which is how a
# start-of-run clear inherits the previous run's verdicts.
if [ -n "$RUNROOT" ] && [ -d "$RUNROOT" ]; then
  ls -1t "$RUNROOT" 2>/dev/null | grep -v '^current$' | tail -n "+$((GATE_RUN_KEEP+1))" | while IFS= read -r old; do
    [ -n "$old" ] && [ "$old" != "$RUNID" ] && rm -rf "$RUNROOT/$old" 2>/dev/null || true
  done
fi
# TOOL-aLeasedGauntlet-1 S3: write the verdict + failing-leg rows to a durable file (worktree-safe
# gitdir) so a `| tail`/`Select-Object -Last N` can't discard which leg failed.
# THE MOVE NOTE rides the RED line only, where a failed leg outranked the move and the reader would
# otherwise never learn the tree also changed. A green bar that moved does not reach that line.
movenote=""; [ "$tree_moved" = yes ] && movenote=" (the tree moved while the bar ran)"
# THE HOST LEGS ride a RED line that outranked them, as the move does, so a reader of a red bar still
# learns which of its failures the host explains. The ratio the HOST line claims is the LOWEST among
# its legs, the one figure that is true of every one of them (TOOL-dDerivedDocket-26 S5).
hostnote=""; [ "${HOST_N:-0}" -gt 0 ] && hostnote=" ($HOST_N HOST: $HOST_LEGS)"
host_x="?"; [ -n "$HOST_R10" ] && host_x="$((HOST_R10 / 10)).$((HOST_R10 % 10))"
HOST_LINE="gates HOST — $HOST_N leg(s) timed out twice while a spawn cost ${host_x}x this clone's floor; the verdict is about the host, not the subject$movenote"
if [ "$gate_verdict" = REFUSED ]; then
  # EXIT 2, THE NO-LEG-LINE HALF OF S6 (TOOL-dDerivedDocket-26). Its verdict file already says REFUSED,
  # and the summary file says it too, so the previous run's `gates GREEN` does not stand there.
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf 'gates REFUSED — no leg line was reported, so this run has no verdict to give\n'; } >"$sfile" 2>/dev/null || true
  echo "gates REFUSED — no leg line was reported, so this run has no verdict to give"; exit 2
elif [ "$gate_verdict" = "TREE MOVED" ]; then
  # EXIT 3, its own status and never 0 or 1: 0 would certify a tree nobody graded, and 1 would send
  # the reader hunting a failing leg that does not exist. Every caller that reads any non-zero exit as
  # "not green" reads this one correctly without learning it. The summary file says it too, so the
  # previous run's `gates GREEN` does not stand there for anyone reading the durable record.
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf 'gates TREE MOVED — the tree changed while the bar ran, so no verdict describes it\n'; } >"$sfile" 2>/dev/null || true
  echo "gates TREE MOVED — the tree changed while the bar ran, so no verdict describes it"; exit 3
elif [ "$fails" = 0 ]; then
  # THE VERDICT-FILE HALF OF S6 (TOOL-dDerivedDocket-26). A green whose record was never written is a
  # green no boundary can confirm: the pre-push hook reads that file after an exit 0 and blocks
  # without it, and a caller that trusts the status alone is the TOOL-aSurfacedLexicon-25 path, where
  # a push proceeded with no bar run. So this runner never exits 0 without having written it.
  if [ -z "$RUNDIR" ] || [ ! -f "$RUNDIR/verdict" ]; then
    [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf 'gates REFUSED — every leg that ran passed, but the run record has no verdict file, so nothing can confirm it\n'; } >"$sfile" 2>/dev/null || true
    echo "gates REFUSED — every leg that ran passed, but the verdict file ${RUNDIR:-<no run record>}/verdict was not written, so nothing can confirm this green"; exit 2
  fi
  # THE CHUNK ROLL-UP, with per-chunk wall time, goes into the DURABLE records and never to stdout.
  # A wall clock on a terminal line invites comparison between two runs that are not comparable —
  # the profiling verb exists precisely because a duration without its envelope is not a
  # measurement.
  # `QUEUE_SUMMARY` rides beside `PROF_LINE` on every path — green, red, and the durable RED copy —
  # UNCONDITIONALLY. A line that is present on some runs and absent on others means two things.
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf 'gates GREEN — %s/%s legs passed%s\n' "$ran" "$ran" "$skipnote"; } >"$sfile" 2>/dev/null || true
  echo "gates GREEN — $ran/$ran legs passed$skipnote"; exit 0
elif [ "$gate_verdict" = HOST ]; then
  # EXIT 4, HOST (TOOL-dDerivedDocket-26 S5): every failed leg timed out on its first attempt beside
  # the pool and again ALONE, while a spawn cost more than GATE_HOST_RATIO times this clone's floor.
  # Its own status because neither neighbour is true: 1 blames the subject for a fault the host
  # explains, and 0 certifies legs that never finished. The failure record is written as a red's is,
  # so the next bar's green cannot erase the evidence of this one.
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf '%s' "${FAILED_LEGS:-}"; printf '%s\n' "$HOST_LINE"; } >"$sfile" 2>/dev/null || true
  if [ -n "$gd" ]; then
    { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf '%s' "${FAILED_LEGS:-}"; printf '%s\n' "$HOST_LINE"; } >"$gd/gate-last-failure.txt" 2>/dev/null || true
    chmod 600 "$gd/gate-last-failure.txt" 2>/dev/null || true
  fi
  echo "$HOST_LINE"; exit 4
else
  # THE SAME DENOMINATOR THE GREEN LINE USES. `$n` is the whole manifest, so a red bar that held
  # 42 legs reported `1/85 legs failed` — a ratio against a population it never ran. The two lines
  # are read by the same person in the same terminal and a figure that changes meaning between them
  # is worse than either. TOOL-dUnstalledConvoy-31.
  [ -n "$sfile" ] && { printf '%s\n' "$PROF_LINE" >"$sfile"; printf '%s\n' "$QUEUE_SUMMARY" >>"$sfile"; printf '%b' "${CHUNK_ROLLUP:-}" >>"$sfile"; printf '%s' "${FAILED_LEGS:-}" >>"$sfile"; printf 'gates RED — %s/%s legs failed%s%s%s\n' "$fails" "$ran" "$skipnote" "$movenote" "$hostnote" >>"$sfile"; } 2>/dev/null || true
  # TOOL-dNomadicAtlas-1: a SECOND copy on RED ONLY. gate-last-summary.txt is overwritten by every
  # run, so the reflexive "let me just re-run it" — which passes, when the red was a flake — erases
  # the evidence of the run that failed. This one is only ever overwritten by the next RED run.
  if [ -n "$gd" ]; then
    ffile="$gd/gate-last-failure.txt"
    { printf '%s\n' "$PROF_LINE"; printf '%s\n' "$QUEUE_SUMMARY"; printf '%b' "${CHUNK_ROLLUP:-}"; printf '%s' "${FAILED_LEGS:-}"; printf 'gates RED — %s/%s legs failed%s%s%s\n' "$fails" "$n" "$skipnote" "$movenote" "$hostnote"; } >"$ffile" 2>/dev/null || true
    chmod 600 "$ffile" 2>/dev/null || true
  fi
  echo "gates RED — $fails/$ran legs failed$skipnote$movenote$hostnote"
  [ -n "$sfile" ] && echo "gate summary saved to $sfile"
  [ -n "$gd" ] && [ -f "$gd/gate-last-failure.txt" ] && echo "gate failure record saved to $gd/gate-last-failure.txt"
  # arm-signature: gates RED — 1/2 legs failed
  exit 1
fi
