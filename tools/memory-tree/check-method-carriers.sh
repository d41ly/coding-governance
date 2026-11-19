#!/usr/bin/env bash
# check-method-carriers.sh — every file that POINTS AT the build method is declared, and points
# rather than copies. Exit 0 = clean · 1 = drift · 2 = misconfigured.
#
#   bash <prefix>/memory-tree/check-method-carriers.sh
#
# WHY THIS EXISTS. The build method landed with four pointers, each a path and never a summary.
# Nothing stopped a fifth being added tomorrow as a paraphrase, and this repo grew FOUR spellings of
# its unattended rules exactly that way — one well-meaning summary at a time, none of them wrong on
# the day it was written. A new carrier should be a decision somebody makes, not a thing that happens.
#
# WHAT IT IS NOT. It does not read prose and judge whether a file restates M3. The test is structural
# — is this file declared, and does its mention look like a pointer rather than a copied section —
# and that is all it claims. A fluent paraphrase that invents its own headings passes here.
#
# THE REGISTRY IS PER-REPO, under <MEMORY_ROOT>/project/ with the gate's other waiver registries. The
# kit ships no registry: gov's rows would otherwise travel to an adopter whose tree does not contain
# those paths, and every adopter would red on install. `adopt-memory-tree.sh` scaffolds an adopter's
# from their OWN measured population.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "method-carriers: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
M="$MEMORY_ROOT"
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT_N="$(cd "$ROOT" && pwd)"
KITREL=${HERE#"$ROOT_N"/}
[ "$KITREL" = "$HERE" ] && { echo "method-carriers: cannot locate this kit inside the repo"; exit 2; }

DOC="BUILD-METHOD.md"
REG="$M/project/method-carriers.txt"
st=0
fail() { echo "METHOD-CARRIERS check $1 FAILED — $2"; st=1; }

# ---- 1: the registry must EXIST. An absent registry is the violation, not the exemption — the same
# ---- rule this tree's other registries carry. Without it every arm below reads a green empty set.
if [ ! -f "$REG" ]; then
  fail 1 "no registry at $REG, and an absent registry is not an empty one — scaffold it with 'bash $KITREL/adopt-memory-tree.sh --scaffold'"
  exit "$st"
fi

# The population. EXCLUSIONS, each for its own reason:
#   <MEMORY_ROOT>/  — the method's own render, its records, specs, reviews and backlog rows all
#                     discuss it legitimately. This also SUBSUMES the registry, which lives under
#                     project/: one exclusion, not two, and saying so keeps a future reader from
#                     adding a second that can never fire.
#   the template    — it IS the method, one render away.
#   *.test.sh       — a test builds a violating fixture on purpose, which is why
#                     `check-install-prefix.sh` excludes its own tests too.
#   this leg        — it necessarily contains the literal it greps for.
# TOOL-aScouredKit-6 — ONE grep over the whole eligible set, not one grep PER FILE. The exclusions
# are unchanged and are still applied first; only the search is batched. Measured on node `a`:
# 1156 spawns and 22.45 s became 0.69 s, at byte-identical output. This leg is `subject = repo` with
# an empty guard, so it runs on every bar in every adopting tree and its cost scaled with THEIR
# tracked file count rather than with the kit's.
#
# `grep -l` exits 1 on no match, which is the passing-zero-reads-as-failure class the charter names —
# so the pipeline is terminated with `|| true` and the EMPTY case is decided by the explicit refusal
# below, which is where it belongs. `xargs -0` with a NUL-delimited list is what keeps a path
# containing a space or a quote from being re-split, and `-r` keeps an empty list from running grep
# against stdin, which would hang the bar waiting for input nobody types.
carriers=$(git ls-files -z | while IFS= read -r -d '' f; do
  case "$f" in
    "$M"/*) continue ;;
    "$KITREL"/BUILD-METHOD.template.md) continue ;;
    "$KITREL"/check-method-carriers.sh) continue ;;
    *.test.sh) continue ;;
  esac
  printf '%s\0' "$f"
done | xargs -0 -r grep -lF -- "$DOC" 2>/dev/null || true)

# ---- 2: an EMPTY population is a refusal. If nothing outside the memory tree points at the method,
# ---- either it has been unwired — the loudest possible drift — or this selector is mis-segmented,
# ---- which is the shape that makes every arm below vacuously true. Guarded explicitly, because
# ---- `vacuous-selector-empty-population` is a class this repo has already been bitten by.
if [ -z "$carriers" ]; then
  fail 2 "no file outside $M/ mentions $DOC at all, so either the method has been unwired or this selector is mis-segmented — an empty population is not a clean one"
  exit "$st"
fi

# The python launcher, INLINED byte-identically from the canonical copy named on its marker line
# (this kit is copy-installed and has no shared lib to source): the registry is read through the
# ledger factory, which is Python (TOOL-dWitnessedBar-16 S4).
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
# The wrong-shell refusal, INLINED byte-identically beside the launcher it guards.
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
# THE REGISTRY IS A LEDGER POPULATION (TOOL-dWitnessedBar-16 S4), keyed by `path`, read through the
# ledger factory beside this leg: one `<path> TAB <count> TAB <sha> TAB <disposition>` row per declared
# carrier. Each row's why is the conversion record's, never the row's. A row the factory refuses is
# declared as its whole text, a path no tree holds, so check 4 names it as gone rather than unread.
PY=$(resolve_python) || { echo "method-carriers: no usable python, and $REG is read through the ledger factory"; exit 2; }
_rows=$("$PY" -I -c '
import sys
sys.path.insert(0, sys.argv[1])
import legacy_ledger as LL
rows, bad = LL.read_rows(sys.argv[2], 1)
for entry in bad:
    print(LL.render_malformed(entry).replace("\t", " "))
for key in rows:
    print(key[0])' "$HERE" "$REG" | tr -d '\r'; exit "${PIPESTATUS[0]}") || { echo "method-carriers: the ledger factory beside this leg did not read $REG"; exit 2; }
declared=$_rows

# ONE pass, collecting into variables the MAIN shell owns. Every `while` below would otherwise run in
# a pipeline subshell, where `st=1` is set and discarded — the defect that makes a red gate print its
# complaint and exit 0.
# `while read`, never `for x in $list`: an unquoted expansion word-splits, so any path with a space
# becomes two nonexistent paths and reds forever with no fix available to the adopter. gov's tree has
# no such path, which is exactly why this was invisible here.
undeclared=""; copied=""
while IFS= read -r c; do
  [ -n "$c" ] || continue
  printf '%s\n' "$declared" | grep -qxF "$c" || undeclared="$undeclared$c
"
  grep -qE '^## M[0-9]+' "$c" 2>/dev/null && copied="$copied$c
"
done <<EOF
$carriers
EOF
gone=""; stale=""
while IFS= read -r d; do
  [ -n "$d" ] || continue
  if [ ! -f "$d" ]; then gone="$gone$d
"
  elif ! grep -qF "$DOC" "$d"; then stale="$stale$d
"
  fi
done <<EOF
$declared
EOF

# ---- 3: every carrier is DECLARED. The drift this leg exists to catch — a new file starts
# ---- mentioning the method and nobody decided whether it points at it or restates it.
[ -z "$undeclared" ] || fail 3 "a file mentions $DOC and is not declared in $REG, so nobody decided whether it points at the method or restates it:
$(printf '%s' "$undeclared" | sed 's/^/    /')"

# ---- 4: every declared row still HITS, in both directions. A stale row is the failure
# ---- the install-prefix gate's old waiver registry produced by keying on <path>:<line> — an edit ABOVE the line
# ---- unpinned it and the gate redded on a merge that touched nothing it guarded
# ---- (TOOL-aSealedCaravan-1). This registry keys on PATH alone, so a row goes stale only when its
# ---- file really stops pointing.
[ -z "$gone" ] || fail 4 "a declared carrier no longer exists, so its row guards nothing:
$(printf '%s' "$gone" | sed 's/^/    /')"
[ -z "$stale" ] || fail 4 "a declared carrier no longer mentions $DOC, so its row is stale and would mask the next real one:
$(printf '%s' "$stale" | sed 's/^/    /')"

# ---- 5: a carrier POINTS, it does not COPY. `## M<n>` is the method's own heading grammar. It is
# ---- NOT unique tree-wide — review records use it — but every such occurrence sits inside the
# ---- <MEMORY_ROOT>/ region excluded above, so the heuristic is sound over the SCANNED population
# ---- and unsound as a general claim. Narrow on purpose: it catches the shape the four unattended
# ---- spellings actually took, a copied bulleted section, not a subtle rewording.
[ -z "$copied" ] || fail 5 "a carrier holds a '## M<n>' heading, the method's own section grammar and the shape a COPY takes rather than a pointer:
$(printf '%s' "$copied" | sed 's/^/    /')"

n=$(printf '%s\n' "$carriers" | grep -c .)
[ "$st" = 0 ] && echo "method-carriers: $n carrier(s), all declared and pointing"
exit "$st"
