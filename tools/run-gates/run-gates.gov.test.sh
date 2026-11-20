#!/usr/bin/env bash
# run-gates.gov.test.sh — the GOV-ONLY arms of the run-gates canary. the run-gates promotion spec's S1.
#
# WHY THIS FILE EXISTS, AND WHY IT IS NOT IN THE KIT PAYLOAD. `run-gates.test.sh` SHIPS: once
# the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` makes run-gates a deployable kit, an adopter's emitted manifest runs it in
# THEIR tree. So the shipped canary may assert only what is true in ANY tree. Sibling units want
# arms that are keyed on THIS repo's corpus instead — the chunking unit's every-leg-carries-a-chunk
# assertion over gov's six declared chunk names, and the push-boundary unit's guard pin on a named
# gov leg. (A third was reserved here and is now CUT: the reuse unit's network-calling leg names.
# TOOL-aPacedTurnstile-16's re-scope ran that predicate over the real manifest for the first time,
# matched six legs and found every one of them hermetic, so there is no population to pin. The
# reservation is removed rather than left standing, because a header naming an arm nobody will write
# is the same rot in the file that exists to refuse it.) In an adopter tree the manifest
# is seeded EMPTY and emitted from descriptors with no chunk key, and gov's legs do not exist, so
# every one of those arms would red on arrival. That is
# `memory/gotchas/pin-copied-from-another-corpus.md`, the class run-gates' own spec refuses by name
# when it declines to seed an adopter with gov's leg names.
#
# The precedent is settled: <prefix>/memory-recall/kit.toml withholds check-recall.py, recall-fixture
# .json and test_recall_floor.py from the payload with a `project-owned` rule, for the same reason
# in the same words — arms keyed on this repo's own record ids are meaningless in another tree. This
# file is withheld the same way, is a leg in gov's own <prefix>/gate-legs.json, and carries an
# [[exempt_leg]] row in <prefix>/govkit/registry.toml. It is deliberately NOT a [[gate_leg]] row in
# <prefix>/run-gates/kit.toml: a descriptor row naming a leg that ships nowhere is the shape the
# deployer's selfcheck reds on, and the descriptor's FOUR rows are the legs the kit SHIPS.
#
# THE REFUSAL BELOW IS THE POINT. A gov-only harness that quietly SUCCEEDS against a foreign corpus
# is the split failing open: every arm here would pass by finding nothing, and the next unit to add
# one would inherit a green that means nothing. So this file asserts it is running in the corpus it
# was written for, and exits 2 — not 0 — when it is not.
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "gov-canary: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
KIT="${KIT_REL##*/}"
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "gov-canary: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

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
  # THE BAR'S OWN RESOLUTION, taken with no spawn (TOOL-aMeasuredDrag-11). The run-gates runner
  # exports GATE_RESOLVED_PY as four lines: the version, the launcher it resolved, and GOV_PYTHON and
  # PATH as it saw them. With no caller override the loop below is decided by GOV_PYTHON, PATH and the
  # floor, so a memo matching both byte for byte, at or above THIS floor, is what the loop would print.
  # Anything else, malformed or partial included, is ignored and the loop runs. Only an absolute
  # launcher is admitted (TOOL-aMeasuredDrag-12): a relative one names another file once a leg
  # changes directory, and a bare name does too under a PATH holding `.`.
  _rp_re=$'^([0-9]+)\\.([0-9]+)\n(/[^\n]*|[A-Za-z]:/[^\n]*|[A-Za-z]:\\\\[^\n]*)\n([^\n]*)\n(.*)$'
  if [ -z "${1:-}" ] && [[ ${GATE_RESOLVED_PY:-} =~ $_rp_re ]] \
    && [ "${BASH_REMATCH[4]}" = "${GOV_PYTHON:-}" ] && [ "${BASH_REMATCH[5]}" = "$PATH" ] \
    && [ $(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} )) -ge "$_rp_fv" ]; then
    printf '%s\n' "${BASH_REMATCH[3]}"
    return 0
  fi
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
# >>> refuse_wrong_shell — canonical copy: refuse-wrong-shell.sh in gov's lib dir (byte-identical; gated)
wrong_shell_at() {   # <abs path> <wsl 0|1>; returns 0 when the path is a Windows checkout under WSL
  [ "$2" = 1 ] || return 1
  case "$1" in /mnt/[a-z]/*) return 0 ;; esac
  return 1
}
refuse_wrong_shell() {
  _rws_wsl=0
  { [ -n "${WSL_DISTRO_NAME:-}" ] || [ -e /proc/sys/fs/binfmt_misc/WSLInterop ]; } && _rws_wsl=1
  _rws_p=${BASH_SOURCE[0]:-$0}
  case "$_rws_p" in /*) ;; *) _rws_p=$PWD/$_rws_p ;; esac
  wrong_shell_at "$_rws_p" "$_rws_wsl" || return 0
  echo "refuse_wrong_shell: WSL's bash is running $_rws_p from a Windows checkout under /mnt/;" >&2
  echo "refuse_wrong_shell: run it with Git's bash (C:/Program Files/Git/bin/bash.exe)." >&2
  return 1
}
# <<< refuse_wrong_shell
refuse_wrong_shell || exit 2
PYBIN=$(resolve_python) || { echo "gov-canary: no usable python"; exit 2; }

fail=0
a=0                          # executed assertions, printed at the end against the pinned floor
# Raised from 12 by TOOL-aShardedFloor-2, which adds the shard-contract arms (forward cover and
# reverse declaration). Stated ABSOLUTELY, never as a delta.
FLOOR_ASSERTIONS=38
# RAISED 35 -> 38 by TOOL-dWitnessedBar-60 on 2026-11-20: the bar-scrub parity arm over the shipped files
# and its two staged copies, one assertion each. Counted by reading; no suite ran.
# RAISED 25 -> 35 by TOOL-dWitnessedBar-56 on 2026-11-20: its seven local-hook plants and three peer
# plants in the verdict backends' plant loop, one assertion each. Counted by reading; no suite ran.
# RAISED 21 -> 25 by TOOL-dWitnessedBar-56 on 2026-11-20 for TOOL-dWitnessedBar-43, whose pass left the
# floor where it was: its four peer plants, peer-signed, peer-unsigned, peer-self-tag and
# peer-swapped-manifest, one assertion each in the same loop. Counted by reading; no suite ran.
# Raised 20 -> 21 by TOOL-dWitnessedBar-22, which adds G11, the `tests`-to-claims compare.
# Raised 19 -> 20 by TOOL-dWitnessedBar-12, which adds G10, the leg tags' shape and uniqueness arm.
# Raised 15 -> 16 by TOOL-dDerivedDocket-23, which adds G1b, the four-leg `signature` pin.
# Raised 16 -> 17 by PLAY-dOrderedCharter-67, which adds the python-reads scanner's plants.
# Raised 17 -> 18 by TOOL-aMeasuredDrag-4, which adds G8, the tags leg's unguarded pin.
# Raised 18 -> 19 by TOOL-dDeclaredLoop-67, which adds G9, the `loop termination` leg's unguarded pin.

# The manifest, derived the same way run-gates.sh derives it. GATE_LEGS still outranks it, which is
# what lets the fixture arms below drive this file without touching the real bar.
# Normalised through the SAME `cd ... && pwd` chain on both sides: under MSYS `git rev-parse
# --show-toplevel` answers `C:/...` and `pwd` answers `/c/...`, and a strip across the two
# flavours leaves an ABSOLUTE path that resolves to nothing.
KITDIR=$(cd "$(dirname "$0")" && pwd)
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"

# ---- G0. THE CORPUS GATE -------------------------------------------------------------------------
# Every arm in this file is keyed on gov's own manifest. Refuse — loudly, exit 2 — rather than pass,
# when the manifest is not gov's. `GATE_LEGS` pointing at a fixture is the ordinary way that happens.
#
# The witness is a leg NAME this repo has carried since long before this kit existed and that no
# adopter's emitted manifest can contain, because a target's leg list is emitted from the selected
# kits' [[gate_leg]] blocks and none of them emits a leg by this name.
WITNESS='memory hygiene'
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)
sys.exit(0 if any(l.get("name") == sys.argv[2] for l in legs) else 1)
' "$LEGS_FILE" "$WITNESS"; then
  echo "gov-canary: REFUSING — $LEGS_FILE carries no leg named '$WITNESS', so this is not the corpus"
  echo "gov-canary: these arms were written for. This harness is gov-only by design (see its header);"
  echo "gov-canary: it is withheld from the kit payload and must never report a green it did not earn."
  exit 2
fi

# ---- G1. the tail contract's other half ----------------------------------------------------------
# the run-gates promotion spec's S5 widens every report tail to TWO spaces so a reader splits the remainder
# on a double space and recovers the bare leg name. That split is only unambiguous while no leg NAME
# contains a double space. Gov's manifest is the population this repo controls, so the arm lives here.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
bad = [l["name"] for l in json.load(open(sys.argv[1])) if "  " in l.get("name", "")]
if bad:
    print("gov-canary: leg name(s) contain a DOUBLE SPACE, which makes the report tail split"
          " ambiguous: " + "; ".join(bad)); sys.exit(1)
' "$LEGS_FILE"; then fail=1; fi
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS ($a assertions)" || echo "FAIL ($a assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

# ---- G1b. `signature` sits on exactly the four legs TOOL-dDerivedDocket-23 S3 gave an `--offenders`
# mode, and nowhere else. A fifth row would name a signature nobody built a key-only mode for, whose
# output the attribution would grade as a set; a missing one leaves that leg on the byte-identical
# rule, which reads MIXED on almost every branch. Gov's corpus, so the arm lives here (AC6).
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
want = {"lexicon naming predicates", "install-prefix (shipped surface)", "drift-audit records",
        "memory hygiene"}
got = {l["name"] for l in json.load(open(sys.argv[1])) if l.get("signature")}
if got != want:
    print("gov-canary: `signature` is declared on %s; the four legs with an --offenders mode are %s"
          % (sorted(got), sorted(want))); sys.exit(1)
' "$LEGS_FILE"; then fail=1; fi

# ---- G2. the runner and both harnesses derive the manifest identically ---------------------------
# SOURCE PARITY, not a re-derivation. An earlier draft of this arm recomputed the derivation inline
# and compared the two answers, which is `memory/gotchas/two-answers-to-one-question.md` inside the
# arm written to prevent it — and it duly disagreed with itself, because the copy carried the
# pre-normalisation strip. What is asserted instead is that the three files carry the SAME two
# derivation lines, byte for byte. One answer, checked; the pattern the resolver parity gate uses.
a=$((a+1))
read_derivation() {   # FILE -> the two derivation lines, whitespace-normalised
  grep -hE '^KITDIR=|^ROOTN=|^KITREL=|^LEGS_FILE=' "$1"
}
ref=$(read_derivation "$KITREL/run-gates.sh")
if [ -z "$ref" ]; then
  echo "gov-canary: $KITREL/run-gates.sh carries no manifest derivation to compare against — the"
  echo "gov-canary: arm cannot pass by finding nothing, so this is a refusal"
  fail=1
else
  for f in "$KITREL/run-gates.test.sh" "$KITREL/run-gates.gov.test.sh"; do
    if [ "$(read_derivation "$f")" != "$ref" ]; then
      echo "gov-canary: $f derives the leg manifest differently from $KITREL/run-gates.sh, so it would"
      echo "gov-canary: grade a different file than the bar runs:"
      printf 'gov-canary:   runner: %s
' "$ref"
      printf 'gov-canary:   %s: %s
' "$f" "$(read_derivation "$f")"
      fail=1
    fi
  done
fi

# ---- G3. the push boundary FORCES the full bar ---------------------------------------------------
# MOVED here from the shipped canary by the closing review (D6). It asserts a fact about GOV's tree:
# an adopter has no `.githooks/pre-push` unless they also took the push-main kit, which is NOT in the
# default selection, so in the shipped half this arm was red on arrival in every default install.
# The property it guards is still gov's and still worth guarding — a scoped authoritative run would
# mean no run ever executes every leg against the tree that actually lands.
a=$((a+1))
# THE PUSH BOUNDARY STILL OWES A TOTAL RUN, and this arm grades the OBLIGATION rather than the
# mechanism. It used to grep for a literal `export GATE_FULL=1` at column 0, which was exactly
# right while the hook forced unconditionally and became a false red the moment the hook started
# DECIDING. Deleting it outright was the one answer this could not take: it is the only executable
# statement anywhere that the authoritative run covers the whole bar, and removing the arm that
# guards a property in the same commit that weakens the property is gating the instance rather
# than the class.
#
# Two halves. The behavioural half — one arm per forcing predicate, plus the control proving a
# scoped run is ever chosen at all — lives in `.githooks/pre-push.test.sh`, where the hook is
# really driven. What stays here is the half that is about THIS repository: that the boundary can
# still force, and that the record it decides against is not further behind than its own bound.
grep -q 'export GATE_FULL=1' "$ROOT/.githooks/pre-push" \
  || { echo "gov-canary: .githooks/pre-push has no forcing path at all — the boundary can never demand a total run"; fail=1; }
a=$((a+1))
grep -qE '^GATE_FULL_MAX_LAG=[0-9]+' "$ROOT/.githooks/pre-push" \
  || { echo "gov-canary: the staleness bound is not a source constant in the hook — a policy an environment variable can change at the moment it binds is not a policy"; fail=1; }

# THE RECORD, when there is one. A fresh clone has none, and that is a legitimate state rather
# than a defect — the hook forces a full run there, which is the safe direction. So this arm
# SKIPS, loudly and countably, instead of reddening: a skip that looks like a pass is
# indistinguishable from coverage, and a red here would fail every clone on its first push.
a=$((a+1))
gc_rec="$(git rev-parse --git-dir)/gate-full-green"
if [ -f "$gc_rec" ]; then
  gc_sha=$(awk -F'\t' '$1=="sha"{print $2}' "$gc_rec" 2>/dev/null)
  gc_bound=$(grep -m1 -oE 'GATE_FULL_MAX_LAG=[0-9]+' "$ROOT/.githooks/pre-push" | grep -oE '[0-9]+')
  if [ -n "$gc_sha" ] && [ -n "$gc_bound" ] && git merge-base --is-ancestor "$gc_sha" HEAD 2>/dev/null; then
    gc_lag=$(git rev-list --count "$gc_sha..HEAD" 2>/dev/null || echo 0)
    [ "${gc_lag:-0}" -le "$gc_bound" ] \
      || echo "gov-canary: NOTE — the recorded full green is $gc_lag commits back, past the bound of $gc_bound, so the next push will force a total run (informational, not a failure)"
  fi
else
  echo "gov-canary: SKIP the recorded-green lag arm — no gate-full-green in this git dir yet, so there is no record to measure. The boundary forces a total run in exactly this state."
fi

# ---- G4/G5. THE CHARTER STILL DESCRIBES THE RUNNER ------------------------------------------------
# Two claims `AGENTS.md` made that the profile-table unit falsified, and NOTHING ELSE observes either:
# the playbook-parity gate grades the playbook FILES rather than this repo's rendered charter, and
# drift-audit's charter signal joins leg SCRIPT PATHS. A charter that goes on stating a width formula
# the runner no longer uses is precisely the claim that unit exists to remove, so it is armed here —
# in gov's own half, because an adopter has no `AGENTS.md` of this shape and the arm would red on
# absence rather than on behaviour.
#
# BOTH HALVES OF EACH, and the positive half is why. A negative-only search passes when the sentence
# it is guarding is DELETED, which is the same green as a sentence that was never wrong. The first
# draft of this pair armed only the figure; the fix for it RELOCATED the defect to the formula half
# and every criterion stayed green.
#
# THE SUBJECT MOVED at v4.0 (TOOL-aDistilledCharter-3). The charter states one line about the bar and
# sends a reader to the merge-bar guide for how it behaves, so both claims are graded THERE, and one
# more arm holds the pointer that makes the guide the charter's answer. Before the move this canary
# read `AGENTS.md` for two strings it had stopped carrying, and would have redded on its next run.
CHARTER="$ROOT/AGENTS.md"
BAR_GUIDE="$ROOT/memory/guides/MERGE-BAR.md"
a=$((a+1))
if [ ! -f "$CHARTER" ] || [ ! -f "$BAR_GUIDE" ]; then
  echo "gov-canary: $CHARTER or $BAR_GUIDE is absent, so the charter arms would pass by finding nothing — this is a refusal"
  fail=1
else
  a=$((a+1))
  grep -qF 'memory/guides/MERGE-BAR.md' "$CHARTER" \
    || { echo "gov-canary: $CHARTER no longer sends a reader to memory/guides/MERGE-BAR.md, so the arms below grade a guide nobody is told to read"; fail=1; }
  CHARTER=$BAR_GUIDE
  # G4 — THE MEASUREMENT, AND THIS ARM STOPPED PINNING ONE. It used to require the charter to state a
  # specific wall/leg-sum pair, and that pair went stale three times in two days: 335s/95s, then
  # 393s/3085s, then 4926 s of leg-sum with a 1565 s floor, then ~265 s once seven legs left the bar.
  # Each time the charter was CORRECTED and this canary red on the correction — a gate demanding that
  # a document keep a number no document can keep.
  #
  # The rule the charter itself states is "point at the source, or gate the pair". `<git-dir>/gate-ledger.tsv`
  # carries one row per leg with its own seconds and cannot go stale, so what is worth pinning is that
  # the charter SENDS a reader there. The retired-figures arm below stays and grows: a figure quoted as
  # current is the defect, whichever figure it is.
  a=$((a+1))
  if grep -qE '335s|~?95s|3085 s|393 s wall' "$ROOT/AGENTS.md" "$BAR_GUIDE"; then
    echo "gov-canary: AGENTS.md or $BAR_GUIDE quotes a retired bar timing as if it were current (335s / 95s / 3085 s / 393 s wall); the bar's per-leg seconds live in <git-dir>/gate-ledger.tsv and prose beside a source that owns a number is the rule this arm exists to hold"; fail=1
  fi
  a=$((a+1))
  grep -q 'gate-ledger.tsv' "$CHARTER" || { echo "gov-canary: $CHARTER no longer sends a reader to <git-dir>/gate-ledger.tsv for the bar's per-leg seconds, so the negative half above would pass on a charter that says nothing about cost at all — silence and a correct pointer are not the same answer"; fail=1; }
  # G5 — the stale WIDTH FORMULA, in the backticked spelling the file actually uses. The runner reads
  # its width from a declared table now, so a charter naming a formula is telling a session something
  # it cannot verify anywhere in the tree.
  a=$((a+1))
  if grep -qF 'min(8, nproc)' "$ROOT/AGENTS.md" "$BAR_GUIDE"; then
    echo "gov-canary: AGENTS.md or $BAR_GUIDE still states the built-in width formula; the width is declared in ${PFX}${KIT}/gate-profiles.txt and read from there"; fail=1
  fi
  a=$((a+1))
  grep -qF ''"${PFX}${KIT}/gate-profiles.txt"'' "$CHARTER" \
    || { echo "gov-canary: $CHARTER does not name ${PFX}${KIT}/gate-profiles.txt as the source of the pool width, so the negative half above would pass on a DELETED sentence"; fail=1; }
fi

# ---- G6. EVERY GOV LEG DECLARES A CEILING --------------------------------------------------------
# TOOL-aBoundedCeiling-1 S9. The RUNNER deliberately does not enforce this: it cannot tell a gov leg
# somebody forgot from an adopter leg the deployer has no business bounding, so it reports an
# unbounded count and refuses nothing. The requirement over THIS corpus lives here, which is the file
# allowed to hold a claim about this repository -- see this suite's header for why that split exists.
#
# WHAT THIS DOES NOT CHECK: whether a ceiling is the RIGHT number. It grades presence and shape only.
# A leg bounded at 99999 passes here and is still unbounded in every sense that matters; the number is
# argued in the spec and in the manifest, and no gate reads an argument.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)

bad = []
for l in legs:
    if not isinstance(l, dict):
        print("gov-canary: a leg row is not an object"); sys.exit(1)
    nm = l.get("name", "?")
    if "ceiling" not in l:
        bad.append("%s declares no ceiling, so it runs unbounded and a hang in it wedges the bar" % nm)
        continue
    c = l.get("ceiling")
    if isinstance(c, bool) or not isinstance(c, int) or c <= 0:
        bad.append("%s has ceiling %r, which is not a positive integer of seconds" % (nm, c))

# LIVENESS. An empty manifest, or one this predicate never selected, would report zero problems and
# read exactly like a fully-bounded corpus. Say so instead.
if not legs:
    print("gov-canary: the manifest carries no legs at all, so this arm graded nothing"); sys.exit(1)

if bad:
    print("gov-canary: %d of %d gov leg(s) are not bounded:" % (len(bad), len(legs)))
    for b in bad[:12]:
        print("  " + b)
    if len(bad) > 12:
        print("  ... and %d more" % (len(bad) - 12))
    sys.exit(1)
' "$LEGS_FILE"; then
  fail=1
fi

# ---- G7. `memory hygiene` DECLARES NO GUARD, AND THAT IS LOAD-BEARING ----------------------------
# TOOL-aThawedCorpus-5 gave check 23 the `[ "$STAGED" = 0 ]` guard its four siblings carry, so the
# pre-commit leg no longer runs it at all. That is a deliberate COVERAGE REDUCTION, and its
# compensating control is that the push boundary still runs it: `.githooks/pre-push` always invokes
# `run-gates.sh` and only chooses between `GATE_FULL=1` and a scoped `GATE_BASE` run, while
# `run-gates.sh` skips a GUARDED leg whose pathspecs did not move against BASE.
#
# So the control holds only while this leg declares no guard. Add one and a scoped default-branch
# push skips check 23 outright, while pre-commit already skips it — the acceptance ledger would then
# be graded at neither boundary, with every gate green throughout. `TOOL-aThawedCorpus-2` proposed
# exactly that edit and was retired to preserve this property; nothing asserted it until now, which
# is the lockstep-invariant-without-a-guard shape. Round-1 diff review, F3.
#
# WHAT THIS DOES NOT CHECK: that the push boundary actually runs the leg. It grades one key on one
# row. The reachability argument lives in the checker's own header beside the exemption.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)

rows = [l for l in legs if isinstance(l, dict) and l.get("name") == "memory hygiene"]

# LIVENESS. A renamed or deleted leg would make this arm select nothing and pass in silence, which
# reads exactly like a correctly unguarded leg. Say so instead.
if len(rows) != 1:
    print("gov-canary: expected exactly one leg named \"memory hygiene\", found %d, so this arm"
          " graded nothing" % len(rows))
    sys.exit(1)

if "guard" in rows[0]:
    print("gov-canary: the `memory hygiene` leg declares a guard (%r)." % (rows[0]["guard"],))
    print("  TOOL-aThawedCorpus-5 removed check 23 from the pre-commit leg, and its compensating")
    print("  control is that this leg runs on BOTH of .githooks/pre-push branches, which is true")
    print("  only while it is unguarded. With a guard, a scoped push skips it and the acceptance")
    print("  ledger is graded at neither boundary. Remove the guard, or retire that exemption.")
    sys.exit(1)
' "$LEGS_FILE"; then
  fail=1
fi

# ---- G8. `tags (the resolver's checks)` DECLARES NO GUARD, AND SHARES THE INSTRUCTION-EDITS CHUNK --
# TOOL-aMeasuredDrag-4 took the tree's tag checks out of `instructions_edit.py check`. Its compensating
# control is that the tags leg runs on every bar that runs `instruction edits (manifest checks)`:
# unguarded, so a scoped bar never skips it, and in the same chunk, so no chunk selection splits them.
#
# WHAT THIS DOES NOT CHECK: a run that names one leg alone, a pass-leg selection, or a cached verdict.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)

TAGS, EDITS = "tags (the resolver'"'"'s checks)", "instruction edits (manifest checks)"
rows = {}
for name in (TAGS, EDITS):
    rows[name] = [l for l in legs if isinstance(l, dict) and l.get("name") == name]
    # LIVENESS, as G7 states it: a renamed or deleted leg selects nothing and would pass in silence.
    if len(rows[name]) != 1:
        print("gov-canary: expected exactly one leg named \"%s\", found %d, so this arm graded nothing"
              % (name, len(rows[name])))
        sys.exit(1)
tags, edits = rows[TAGS][0], rows[EDITS][0]

if "guard" in tags:
    print("gov-canary: the `%s` leg declares a guard (%r)." % (TAGS, tags["guard"]))
    print("  TOOL-aMeasuredDrag-4 left the tree'"'"'s tag checks to this leg alone, so a scoped bar that")
    print("  skips it grades no tag check while `%s` still runs. Remove the guard." % EDITS)
    sys.exit(1)
if tags.get("chunk") != edits.get("chunk"):
    print("gov-canary: the `%s` leg'"'"'s chunk %r differs from `%s`'"'"'s chunk %r."
          % (TAGS, tags.get("chunk"), EDITS, edits.get("chunk")))
    print("  TOOL-aMeasuredDrag-4 left the tree'"'"'s tag checks to the tags leg, so a chunk selection")
    print("  that splits the two grades no tag check. Keep them in one chunk.")
    sys.exit(1)
' "$LEGS_FILE"; then
  fail=1
fi

# ---- G9. `loop termination` DECLARES NO GUARD -----------------------------------------------------
# TOOL-dDeclaredLoop-55 S1 took the guard off this leg: its populations are gov's composition, the
# overlay, the scenarios and every live build's pin, and a `{prefix}/loop/` guard misses all but the
# first, so a scoped bar would skip the termination check over a change it reads. Modelled on G7.
#
# WHAT THIS DOES NOT CHECK: that the push boundary runs the leg, or what the leg grades. It grades one
# key on one row.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)

rows = [l for l in legs if isinstance(l, dict) and l.get("name") == "loop termination"]

# LIVENESS, as G7 states it: a renamed or deleted leg selects nothing and would pass in silence.
if len(rows) != 1:
    print("gov-canary: expected exactly one leg named \"loop termination\", found %d, so this arm"
          " graded nothing" % len(rows))
    sys.exit(1)

if "guard" in rows[0]:
    print("gov-canary: the `loop termination` leg declares a guard (%r)." % (rows[0]["guard"],))
    print("  TOOL-dDeclaredLoop-55 S1 removed it: the leg reads the overlay, the scenarios and every")
    print("  live build'"'"'s pin, which a {prefix}/loop/ guard misses, so a scoped bar would skip the")
    print("  termination check over a change it reads. Remove the guard.")
    sys.exit(1)
' "$LEGS_FILE"; then
  fail=1
fi

# ---- G10. EVERY GOV LEG CARRIES ONE `leg` TAG, AND NO TWO SHARE ONE ------------------------------
# TOOL-dWitnessedBar-12 S7: a row's `tag` is `leg.<owner>.<name>`, two segments after the namespace,
# within 64 bytes. The one check that reds a duplicated leg tag (its section 8 F10): the resolver's
# `check` keeps a tag's first definition, so two rows sharing one read green there.
#
# WHAT THIS DOES NOT CHECK: that a tag follows the rule from its row's owner and name, which only
# `leg_factory.py new` applies, to a leg it writes, nor a duplicate in any manifest but gov's own.
a=$((a+1))
if ! "$PYBIN" -c '
import json, re, sys
try:
    legs = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)
seg = "[a-z0-9][a-z0-9-]*"
bad, seen = [], {}
for l in legs:
    nm, tag = l.get("name", "?"), l.get("tag")
    if not isinstance(tag, str) or not re.fullmatch(r"leg\.%s\.%s" % (seg, seg), tag) or len(tag.encode()) > 64:
        bad.append("leg %r carries tag %r, not leg.<owner>.<name> within 64 bytes" % (nm, tag))
    elif tag in seen:
        bad.append("legs %r and %r share the tag %s" % (seen[tag], nm, tag))
    else:
        seen[tag] = nm
if not legs:
    print("gov-canary: %s holds no leg, so no tag was graded" % sys.argv[1]); sys.exit(1)
if bad:
    print("gov-canary: " + "\ngov-canary: ".join(bad)); sys.exit(1)
' "$LEGS_FILE"; then
  fail=1
fi

# ---- G11. A LEG'S `tests` AND THE DOSSIERS' CLAIMS AGREE, BOTH WAYS --------------------------------
# TOOL-dWitnessedBar-22 S5: the feature a leg tests is declared once, on its row, as `tests`; each
# dossier under the map's `features/` still claims its legs in `[claims] gate-legs` until dTotalRecall
# derives that list from the edge. Until then the two spellings are compared in both directions: a leg
# whose `tests` names `feature.<f>` is claimed by the dossier whose `feature` is <f>, and a leg a dossier
# claims names that dossier's feature in `tests`. The dossiers are read through the map's own
# `load_map_tree`, so the population is exactly the one the map gates parse, and never edited.
#
# WHAT THIS DOES NOT CHECK: a `tests` target outside `feature.*`, which no dossier claims; the claims of
# `FOUNDATION.md`, which is no feature; or that a claim names the right feature.
a=$((a+1))
if ! "$PYBIN" -c '
import json, pathlib, sys
root, legs_file = pathlib.Path(sys.argv[1]), sys.argv[2]
sys.path.insert(0, str(root / sys.argv[3]))
try:
    import map_extractors as ext, map_lib as m
    legs = json.load(open(legs_file, encoding="utf-8"))
    tree = m.load_map_tree(ext.inventory_ids(), root=root,
                           decision_id_re=getattr(ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE))
except Exception as e:
    print("gov-canary: the tests compare cannot read the manifest or the dossiers: %s" % e); sys.exit(1)
source = {d.feature: d.source for d in tree.dossiers}
claims = {}
for d in tree.dossiers:
    for nm in d.claims.get("gate-legs", ()):
        claims.setdefault(nm, set()).add(d.feature)
# LIVENESS: a map whose dossiers claim no leg compares nothing, and would pass in silence.
if not claims:
    print("gov-canary: no dossier under the map claims a leg, so the tests compare graded nothing"); sys.exit(1)
bad = []
for l in legs:
    nm = l.get("name", "?")
    said = {t[len("feature."):] for t in l.get("tests") or () if isinstance(t, str) and t.startswith("feature.")}
    for f in sorted(said - claims.get(nm, set())):
        bad.append("leg %r carries tests feature.%s, " % (nm, f)
                   + ("and %s does not claim it" % source[f] if f in source else "and no dossier declares that feature"))
    for f in sorted(claims.get(nm, set()) - said):
        bad.append("%s claims leg %r, whose tests does not name feature.%s" % (source[f], nm, f))
if bad:
    print("gov-canary: " + "\ngov-canary: ".join(bad)); sys.exit(1)
' "$ROOT" "$LEGS_FILE" "${PFX}codebase-map"; then
  fail=1
fi

# ---- verdict -------------------------------------------------------------------------------------
# The executed assertion count, in the shape <prefix>/check-testsuite-counts.sh reads, against a floor
# declared here. the run-gates promotion spec's S11: this file gets a counter and a floor at BIRTH, so it
# never needs a row in memory/project/testsuite-count-waivers.txt.
# EVERY LEG OF GOV'S REAL MANIFEST CARRIES A CHUNK, and its value is one of the six declared
# names. This is the assertion that cannot ship: an adopter's manifest is seeded empty and emitted
# from descriptors, so a shipped arm demanding a chunk key would red on arrival in every install.
# It is UNCONDITIONAL over the manifest rather than a spot check — a new leg added without a key
# would otherwise fall into `default` silently and report under a chunk nobody declared.
a=$((a+1))
"$PYBIN" -c '
import json, sys
SIX = {"records", "product", "wiring", "declarations", "selftests", "e2e"}
legs = json.load(open(sys.argv[1]))
bad = [l.get("name", "?") for l in legs if l.get("chunk") not in SIX]
if bad:
    print("gov-canary: leg(s) with no chunk key, or a value outside the six declared names %s: %s"
          % (sorted(SIX), ", ".join(bad)))
    sys.exit(1)
' "$ROOT/${PFX}gate-legs.json" || fail=1
# ---- THE SHARD CONTRACT, both directions (TOOL-aShardedFloor-2) ----------------------------------
# A sharded suite is TWO manifest rows on ONE script, and the failure that costs is silent: delete
# one row and the bar goes green having run half the suite. Nothing else notices, because every
# surviving row passes and the manifest is not compared to anything.
#
# BOTH DIRECTIONS, because either alone is satisfiable by doing nothing. Forward: every index a
# sharded script declares is present in the manifest. Reverse: a script CALLED with `--shard`
# declares a `SHARD_ARITY`, and a script that declares one is CALLED with `--shard` — which is the
# arm that catches the live pre-change shape, a script parsing no argv at all, where two `--shard`
# rows would each run the full suite: bar green, wall unchanged, leg-seconds doubled.
#
# WHAT THIS DOES NOT CHECK: that a shard actually runs the region it claims. Only the suite's own
# per-mode assertion floor sees that. This arm reads the manifest and a declaration, nothing more.
a=$((a+2))
"$PYBIN" -c '
import json, os, re, sys
root, legs_file = sys.argv[1], sys.argv[2]
legs = json.load(open(legs_file))
bad = []

# forward — every declared index present, exactly once
sharded = {}
for l in legs:
    argv = l.get("argv") or []
    if "--shard" not in argv:
        continue
    i = argv.index("--shard")
    val = argv[i + 1] if i + 1 < len(argv) else ""
    script = next((t for t in argv if t.endswith(".sh") or t.endswith(".py")), "?")
    m = re.fullmatch(r"([0-9]+)/([0-9]+)", val)
    if not m:
        bad.append("leg %r carries a malformed --shard value %r" % (l.get("name", "?"), val)); continue
    sharded.setdefault(script, []).append((int(m.group(1)), int(m.group(2)), l.get("name", "?")))
for script, rows in sorted(sharded.items()):
    arities = {r[1] for r in rows}
    if len(arities) != 1:
        bad.append("%s is called with more than one shard arity: %s" % (script, sorted(arities))); continue
    n_ = arities.pop()
    have = sorted(r[0] for r in rows)
    want = list(range(1, n_ + 1))
    if have != want:
        bad.append("%s declares arity %d but the manifest carries indices %s — expected %s"
                   % (script, n_, have, want))

# reverse — the declaration and the call agree, in both directions
for script in sorted({t for l in legs for t in (l.get("argv") or []) if t.endswith(".sh")}):
    p = os.path.join(root, script)
    if not os.path.isfile(p):
        continue
    declares = re.search(r"^SHARD_ARITY=", open(p, encoding="utf-8", errors="replace").read(), re.M)
    called = script in sharded
    if declares and not called:
        bad.append("%s declares SHARD_ARITY but no manifest row calls it with --shard — it runs whole, once" % script)
    if called and not declares:
        bad.append("%s is called with --shard but declares no SHARD_ARITY — the flag is IGNORED and every row runs the whole suite" % script)

if bad:
    print("gov-canary: shard contract violated:")
    for b in bad:
        print("  " + b)
    sys.exit(1)
' "$ROOT" "$ROOT/${PFX}gate-legs.json" || fail=1

# ---- THE PYTHON-READS SCANNER'S PLANTS (PLAY-dOrderedCharter-67) ---------------------------------
# An undefined name and a suite import outside its guard, each staged in a scratch tool root and
# each beside its passing case, so the leg's own green is not the only witness that either arm reds.
a=$((a+1))
"$PYBIN" "$KITDIR/py_reads.py" --selftest || { echo "gov-canary: py_reads.py --selftest failed"; fail=1; }

# ---- THE VERDICT BACKENDS' PLANTS (TOOL-dWitnessedBar-6 AC1 to AC6, AC7's held reader) ------------
# Each plant of the unit's design runs in its own scratch directory through `verdict_backends.py
# --fixture`, which drives `read`, the fixture lander and `remote_verdict.py --responses`, and owes
# its last scenario's exit and its all-held line. Arms: a duplicate descriptor row, an unregistered and
# an undeclared value, the full slot against the scoped one, a node's own or another tree's peer tag,
# and the witness rule's writer, liveness, failed-read and source fields. The peer plants
# (TOOL-dWitnessedBar-43 AC1, AC2, AC4) run over throwaway SSH keys: a signed GREEN standing, an unsigned
# tag, a node line another node's key signed, and a candidate emptying the leg manifest read HELD under
# dispatch-closure and workflow; each prints `not run` where no ssh-keygen runs. TOOL-dWitnessedBar-56
# (AC6, AC13): the local-hook reader reads NONE over a full GREEN its two record predicates refuse, the
# reuse pair (`reused-cache`, `reused-alone`, `no-pair`) and the selection (`no-selection`,
# `edited-selection`, `underived-selection` at the landed revision), and GREEN over `clean`; a peer ref
# the fetch cannot bring in and a verify with no ssh-keygen read DEAD PROBE, and a tag edited after it
# was signed NONE naming the bad signature. WHAT THIS DOES NOT CHECK: a
# real GitHub answer, a real peer's bar, or the lander under peer-node (push-main.test.sh's arm 43).
for vb_case in registry:2 unregistered:0 undeclared:0 local-green:1 reused-cache:1 reused-alone:1 no-pair:1 \
               no-selection:1 edited-selection:1 underived-selection:1 clean:0 peer:1 peer-signed:0 peer-unsigned:2 \
               peer-self-tag:1 peer-swapped-manifest:0 peer-tip-missing:1 peer-no-ssh-keygen:1 \
               peer-bad-signature:1 remote-green:0 \
               swapped-workflow:0 other-path:1 step-skipped:1 api-404:1 held:0; do
  a=$((a+1))
  vb_plant=${vb_case%%:*}
  vb_out=$("$PYBIN" "$KITDIR/verdict_backends.py" --fixture --plant "$vb_plant" 2>&1); vb_rc=$?
  case "$vb_rc:$vb_out" in
    "${vb_case#*:}:"*"plant $vb_plant · "*"all held"*) ;;
    *) echo "gov-canary: verdict_backends.py --fixture --plant $vb_plant exited $vb_rc, owed ${vb_case#*:} with every scenario held:"
       printf '%s\n' "$vb_out" | grep -E 'MISSED|not run|Traceback' | sed 's/^/  /'; fail=1 ;;
  esac
done

# ---- EVERY BAR CALLER THAT RECORDS A TRUSTED GREEN SCRUBS WHAT THE HOOK CLEARS (TOOL-dWitnessedBar-60) --
# The pre-push hook scrubs `BAR_SCRUBBED_KNOBS` and clears `BAR_CLEARED_KNOBS` before its bar; post-merge's
# `PM_SCRUB` and the unattended driver's `_gknobs` run bars whose green is trusted for the whole tree, so
# each must carry every one of those names. The hook's two lists and `_gknobs` are read by the one-line
# cuts the driver suite's parity arm uses; `PM_SCRUB` spans lines and is read as a range, quotes stripped
# and newlines folded to spaces, the fold post-merge itself applies. A list that reads empty is named
# too, so a moved or reworded line cannot pass this over nothing. Two staged copies prove it can fail.
# WHAT THIS DOES NOT CHECK: that either caller honours its list at run time (the evidence suite's
# post-merge arm observes one), the hook's `ENV_DROPPED_KNOBS`, or the policy keys set from R's file.
check_bar_scrub_parity() {   # hook · post-merge · driver -> one line per missing name or empty list
  local sk ck pm dr k out=""
  sk=$(sed -n 's/^BAR_SCRUBBED_KNOBS="\([^"]*\)"$/\1/p' "$1" 2>/dev/null)
  ck=$(sed -n 's/^BAR_CLEARED_KNOBS="\([^"]*\)"$/\1/p' "$1" 2>/dev/null)
  pm=$(sed -n '/^PM_SCRUB="/,/"$/p' "$2" 2>/dev/null | sed -e 's/^PM_SCRUB=//' -e 's/"//g' | tr '\n' ' ')
  dr=$(sed -n 's/^ *local _gk _gknobs="\([^"]*\)".*/\1/p' "$3" 2>/dev/null)
  [ -n "${sk// /}" ] || out+="BAR_SCRUBBED_KNOBS reads empty in $1"$'\n'
  [ -n "${ck// /}" ] || out+="BAR_CLEARED_KNOBS reads empty in $1"$'\n'
  [ -n "${pm// /}" ] || out+="PM_SCRUB reads empty in $2"$'\n'
  [ -n "${dr// /}" ] || out+="_gknobs reads empty in $3"$'\n'
  for k in $sk $ck; do
    case " $pm " in *" $k "*) ;; *) out+="PM_SCRUB in $2 lacks $k"$'\n' ;; esac
    case " $dr " in *" $k "*) ;; *) out+="_gknobs in $3 lacks $k"$'\n' ;; esac
  done
  printf '%s' "$out"
  [ -z "$out" ]
}
bsp_hook="$ROOT/.githooks/pre-push"; bsp_pm="$KITDIR/post-merge.sh"; bsp_drv="$ROOT/${PFX}unattended/unattended.sh"
a=$((a+1))
bsp_out=$(check_bar_scrub_parity "$bsp_hook" "$bsp_pm" "$bsp_drv") \
  || { echo "gov-canary: a bar caller does not scrub every knob the pre-push hook scrubs or clears:"; printf '%s\n' "$bsp_out" | sed 's/^/  /'; fail=1; }
bsp_t=$(mktemp -d)
sed '/^PM_SCRUB="/,/"$/s/ GATE_SELECTION\([ "]\)/\1/'"$bsp_pm" > "$bsp_t/post-merge.sh"
sed '/^BAR_CLEARED_KNOBS=/d' "$bsp_hook" > "$bsp_t/pre-push"
a=$((a+1))
bsp_out=$(check_bar_scrub_parity "$bsp_hook" "$bsp_t/post-merge.sh" "$bsp_drv") \
  && { echo "gov-canary: a PM_SCRUB copy with GATE_SELECTION cut passed the scrub parity arm"; fail=1; }
printf '%s\n' "$bsp_out" | grep -q '^PM_SCRUB in .* lacks GATE_SELECTION$' \
  || { echo "gov-canary: a PM_SCRUB copy with GATE_SELECTION cut was not named for it: $bsp_out"; fail=1; }
a=$((a+1))
bsp_out=$(check_bar_scrub_parity "$bsp_t/pre-push" "$bsp_pm" "$bsp_drv") \
  && { echo "gov-canary: a hook copy with no BAR_CLEARED_KNOBS line passed the scrub parity arm"; fail=1; }
printf '%s\n' "$bsp_out" | grep -q '^BAR_CLEARED_KNOBS reads empty' \
  || { echo "gov-canary: a hook copy with no BAR_CLEARED_KNOBS line was not named as an empty list: $bsp_out"; fail=1; }
rm -rf "$bsp_t"

[ "$a" -ge "$FLOOR_ASSERTIONS" ] || { echo "gov-canary: executed $a assertions, below the pinned floor $FLOOR_ASSERTIONS"; fail=1; }
if [ "$fail" = 0 ]; then
  echo "PASS ($a assertions)"
  exit 0
fi
echo "gov-canary: FAIL ($a assertions)"
exit 1
