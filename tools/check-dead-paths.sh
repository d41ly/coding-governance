#!/usr/bin/env bash
# check-dead-paths.sh — nothing outside `memory/`, and no map dossier or gotcha page, may name a file this repo DELETED
# or renamed away.
#
#   bash <prefix>/check-dead-paths.sh            # assert; exit 1 on an unwaived hit
#   bash <prefix>/check-dead-paths.sh --list     # print every hit, waived or not (authoring aid)
#   bash <prefix>/check-dead-paths.sh --needles  # print the derived needle set (authoring aid)
#
# WHY. `<prefix>/check-install-prefix.sh` already owns half of the dead-path class: a path spelled at
# the wrong PREFIX. The other half is a path that is dead because the file was DELETED, and until
# this gate landed nothing held it. Measured on the v3.0 charter convergence, which deleted two
# companion files: carriers still naming them survived in the repo's front door, the charter every
# session reads, the install runbook, kit READMEs an adopter receives, the kickoff engine's hand-back
# offer, two self-test rule citations, a registry reason string, and a gate's own over-budget REMEDY
# — a message that fires ~1.4 KiB from the ceiling, at the one moment someone needs a followable
# instruction. Several sat on a line the same diff edited: the filename was updated and the clause
# beside it was not. That is not a run of independent oversights, it is one missing gate.
#
# NO COUNT OF THAT POPULATION IS WRITTEN HERE. `--list` derives it, and a figure in this header would
# be a number nothing recomputes — which is the same rot the gate exists to catch.
#
# THE NEEDLES ARE DERIVED FROM GIT, never listed. A basename this repo once tracked and no longer
# tracks is a name that resolves to nothing, and git knows the set exactly. That derivation is what
# keeps the false-positive rate at zero: `package.json`, `GEMINI.md` and `docs/PARALLEL.md` are named
# all over the shipped surface and were never files here, so they are never needles. MEASURED against
# the alternative — flagging any path-shaped token that does not resolve — 217 hits, essentially all
# of them legitimate fixture literals inside Python selftests. That gate would have been waived into
# uselessness on its first day.
#
# EACH NEEDLE ALSO CONTRIBUTES ITS DISTINCTIVE TAIL, because carriers abbreviate. The dead
# `parallel-coding-governance.domain-rules.md` was spelled `.domain-rules.md` in the README and
# `…domain-rules.md` in a kit README, and a full-basename scan saw NEITHER — it is not a refinement,
# it is most of what this gate finds on the real tree. `check-dead-paths.test.sh` arms both spellings
# separately for that reason.
# The tail is the last dotted component plus the extension, and it stops there: the bare extension
# would match everything. A tail that still names a tracked file is DROPPED, so a deleted `a.test.sh`
# cannot make every `test.sh` in the tree a violation.
#
# WHAT IT DOES NOT CATCH, said plainly because a reader who over-trusts this gate is worse off than
# one who does not use it. It matches FILENAMES. A carrier that names the deleted thing in prose
# without spelling a filename — "per its customize companion", "its own 'Customize before use'
# block", "the product template + its two companions" — is invisible here, and carriers of exactly
# that shape were in the v3.0 set. They were found by READING, not by this gate, and nothing here
# would have caught them. It is a floor, not the answer.
# A RENAME whose source sat under `memory/` is not a needle (TOOL-aRepatriatedFork-45): those are
# records re-filed, and the one such name spelled outside `memory/`, `BACKLOG.md`, is an adopter's
# live backlog file. And a rename is only seen as one above git's rename-similarity threshold (50% by
# default); below it git records a delete plus an add, which the deletion half already reads, so the
# threshold moves a name between the halves and drops none — unless rename detection is switched off
# outright, which the rename sentinel refuses.
#
# `memory/` IS OUT OF SCOPE, and that is a rule rather than a convenience. Specs, reviews, build
# ledgers and archived snapshots are append-only records: they describe what WAS true, and a record
# that names a file deleted after it was written is correct, not stale. Rewriting one to please a
# gate would be falsifying the record.
#
# EXCEPT THE MAP DOSSIERS under `memory/map/features/` (closing review round 1 L1,
# TOOL-aRepatriatedFork-30 S9). A dossier is not a record of what was true: it is the live inventory a
# session reads to learn what the tree holds, rewritten on every touch, and one describing a deleted
# registry as current was the worst place for a dead path to live. They are graded like any carrier.
# SO ARE THE GOTCHA PAGES under `memory/gotchas/` (closing review round 2 L2, TOOL-aRepatriatedFork-30
# S10): `gotchas.py` serves each as a live checklist item, and one still told its reader to hand-write
# rows in a deleted registry. The class is a surface SERVED AS LIVE, not the one folder it bit first.
#
# WAIVERS are the tracked ledger population `dead-path-waivers` at `memory/project/`, beside every other
# population (TOOL-dWitnessedBar-16 S14), one row per waived text; a waiver whose resolved line is no
# longer a hit reds as stale.
#
# IT NEVER MATCHED THE INSTALL-PREFIX GATE'S OLD WAIVER REGISTRY, and the divergence was DELIBERATE
# rather than an oversight: that sibling stayed `<path>:<line>` until TOOL-aRepatriatedFork-30
# deleted it with the rest of that gate's exemptions. The owner ruled ONE file, and a registry moves
# when its own keying has actually failed, not by association.
set -u
# Captured BEFORE the `cd`, because `$0` may be relative (TOOL-aRepatriatedFork-29 S3).
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir=""
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "dead-paths: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

# THIS GATE'S OWN DIRECTORY, DERIVED, and an underivable one REFUSES. Its own two files sit here, and
# every waiver row names its file through the `{prefix}` token the loop below resolves against this
# answer, so gov runs at whatever kit root it was checked out under. The registry itself sits in
# `memory/project/`, spelled as `check-spec-tokens.py` spells its own, so no install prefix names it.
if ! SELF_PRE=$(unset GIT_DIR GIT_WORK_TREE; git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null); then
  echo "dead-paths: cannot derive this gate's own directory from '$_self_dir' — REFUSING"
  exit 2
fi
WAIVERS="memory/project/dead-path-waivers.txt"
# The `{prefix}` resolution (TOOL-aRepatriatedFork-47), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test.
# >>> resolve_prefix_sh -- canonical copy: kit-rel.sh in the gov lib dir (byte-identical; gated)
resolve_prefix_sh() {
  local _rps_s="$1"
  case "${2:-}" in
    ""|.) _rps_s=${_rps_s//"{prefix}/"/}; _rps_s=${_rps_s//"{prefix}"/.} ;;
    *) _rps_s=${_rps_s//"{prefix}"/"$2"} ;;
  esac
  printf '%s\n' "$_rps_s"
}
# <<< resolve_prefix_sh
TABC=$(printf '\t')
# FROZEN SENTINEL. The needle derivation walks history and could go silently empty — a bad
# `--diff-filter`, a shallow clone, a `git log` that stops answering — and an empty needle set makes
# this gate pass by matching nothing, which is the vacuous-selector shape
# (`memory/gotchas/vacuous-selector-empty-population.md`). This basename was deleted at 5b00666 and
# will never return, so its ABSENCE from the derived set means the derivation broke, not that the
# tree got clean.
SENTINEL="parallel-coding-governance.domain-rules.md"
# The rename half's own frozen sentinel: the v3.0 product template's old name, reachable ONLY through
# a rename row, so its absence means the rename read broke. It is checked against the rename half
# alone, never the union, or a deletion of the same name could hold it up.
RENAME_SENTINEL="parallel-coding-governance.template.md"

MODE="${1:---check}"
case "$MODE" in --check|--list|--needles) ;; *) echo "usage: $(basename "$0") [--check|--list|--needles]"; exit 2 ;; esac

# --- the needle set, derived ----------------------------------------------------------------------
# Every path ever deleted or renamed away, reduced to basenames, minus every basename the tree still
# carries. A file deleted from one directory and re-added in another is NOT dead: the name still
# resolves.
tracked=$(git ls-files)
[ -n "$tracked" ] || { echo "dead-paths: git ls-files is empty — that is not a pass"; exit 2; }
tracked_base=$(printf '%s\n' "$tracked" | sed 's|.*/||' | sort -u)

deleted_base=$(git log --diff-filter=D --name-only --pretty=format: -- . \
               | sed '/^$/d; s|.*/||' | sort -u)
[ -n "$deleted_base" ] || { echo "dead-paths: git history reports no deletion at all — the derivation is broken, not the tree clean"; exit 2; }

# THE RENAME HALF (TOOL-aRepatriatedFork-45). git records a `git mv` as R, never D, so the OLD name of
# a renamed file is gone exactly as a deleted one is and the read above never sees it. Column 2 of an
# `R<score>` row is the source. Sources under `memory/` are records re-filed, and the one such name
# spelled outside it, `BACKLOG.md`, is an adopter's live file, so they stay out, mirroring the
# haystack's own exclusion.
renamed_base=$(git log --diff-filter=R --name-status --pretty=format: -- . \
               | awk -F'\t' 'NF >= 3 && $2 !~ /^memory\// { print $2 }' \
               | sed 's|.*/||' | sort -u)

gone=$(printf '%s\n%s\n' "$deleted_base" "$renamed_base" | sort -u \
       | grep -vxF -f <(printf '%s\n' "$tracked_base") || true)

# Each gone basename plus its distinctive tail. `a.b.md` -> `a.b.md` and `b.md`; `a.md` -> `a.md`.
# Then drop any needle that still SUFFIXES a tracked path, which is what stops a generic tail.
#
# ONE awk PASS, deliberately. The first draft filtered in a shell loop that spawned sed and grep per
# needle; measured at 12.3s on this tree and ~2s in a two-commit fixture, which made the self-test the
# slowest leg on the bar by an order of magnitude. The comparison is O(tracked x needles) either way —
# what cost the twelve seconds was process creation, not the string work.
needles=$(printf '%s\n' "$gone" \
  | awk 'NF { print; n = split($0, p, "."); if (n > 2) print p[n-1] "." p[n] }' \
  | sort -u \
  | awk -v tracked="$tracked" '
      BEGIN { nt = split(tracked, tp, "\n") }
      # A compiled artifact or an editor scratch name is not a documentation carrier; excluding it
      # keeps the waiver list about prose. Extension-driven so it needs no per-name list.
      /\.(pyc|pyo|orig|rej)$/ || $0 == ".gitkeep" { next }
      {
        n = $0; ln = length(n)
        for (i = 1; i <= nt; i++) {
          p = tp[i]
          if (p == n) next
          d = length(p) - ln
          if (d > 0 && substr(p, d + 1) == n) {
            c = substr(p, d, 1)
            if (c == "/" || c == ".") next
          }
        }
        print n
      }')
[ -n "$needles" ] || { echo "dead-paths: the derived needle set is EMPTY, so this gate would match nothing and pass"; exit 1; }

if ! printf '%s\n' "$needles" | grep -qxF "$SENTINEL"; then
  echo "dead-paths: the frozen sentinel '$SENTINEL' is not in the derived needle set."
  echo "dead-paths: it was deleted at 5b00666 and cannot come back, so the DERIVATION is broken —"
  echo "dead-paths: a clean verdict from here would be this gate matching nothing and calling it green."
  exit 1
fi
# Read against the rename half ALONE, never the union, so a deletion of the same basename can never
# mask an empty rename read. After the deletion sentinel, so each refusal keeps its own message.
if ! printf '%s\n' "$renamed_base" | grep -qxF "$RENAME_SENTINEL"; then
  echo "dead-paths: the frozen rename sentinel '$RENAME_SENTINEL' is not in the derived rename set."
  echo "dead-paths: it was renamed away at 5b00666 and cannot come back, so the rename"
  echo "dead-paths: DERIVATION is broken — renamed-away names would go unseen and the gate call it green."
  exit 1
fi

if [ "$MODE" = --needles ]; then
  printf '%s\n' "$needles"
  exit 0
fi

# --- the haystack ---------------------------------------------------------------------------------
# Everything tracked except `memory/` (append-only records) and this gate's own two files, which name
# every needle by construction, PLUS the map dossiers and the gotcha pages, which are served as live
# guidance and not kept as records.
RE=$(printf '%s\n' "$needles" | sed 's/[.[\*^$]/\\&/g' | tr '\n' '|'); RE=${RE%|}
hits=$( { git grep -nE "$RE" -- ':(exclude)memory/*' \
                              ":(exclude)$WAIVERS" \
                              ":(exclude)${SELF_PRE}check-dead-paths.sh" \
                              ":(exclude)${SELF_PRE}check-dead-paths.test.sh"
          git grep -nE "$RE" -- 'memory/map/features/*' 'memory/gotchas/*'; } 2>/dev/null \
       | awk -F: '{print $1":"$2}' | sort -u)

# --- resolve the registry -------------------------------------------------------------------------
# TOOL-dHonouredPark-3. A row is keyed by TEXT and an occurrence ORDINAL, and resolving each one to
# the `<path>:<line>` token it names is the WHOLE change: every set difference below is untouched, so
# "stale" keeps the exact meaning line keying gave it -- MEMBERSHIP in the derived hit set, which
# still reds a row whose line survives but whose needle left the derivation. A predicate asking only
# "does this text still appear somewhere" would be strictly weaker and would waive nothing while
# reporting green.
#
# THE REGISTRY IS A LEDGER POPULATION (TOOL-dWitnessedBar-16 S4), `dead-path-waivers`, a declared set
# keyed by <path> and <line-text>, read through gov's ledger factory: `<path> TAB <line-text> TAB
# <count> TAB <sha> TAB <disposition>`. The ordinal left the key: the count holds how many identical
# lines of that text the row waives, its occurrences 1 to <count>, so N identical carriers are one row
# of count N. A row's reason is the conversion record's, never the row's, and a row the factory
# refuses is MALFORMED, never a silently absent waiver. An absent registry waives nothing and spawns
# no python.
#
# ENVIRON, NEVER `awk -v`. A `-v` assignment expands backslash sequences, so a waived line holding a
# literal `\n` -- there is one on this tree, the STATUS.md size fixture -- compares unequal to itself
# and the row reads stale for a reason nobody could see. Measured on that row before this was
# written; it fails RED rather than green, which is why it would have cost a debugging session
# rather than a wrong verdict.
# The launcher resolver and the wrong-shell refusal, INLINED byte-identically from the canonical
# copies named on their marker lines and gated by the resolve-python self-test's parity table, as
# check-playbook-parity.sh carries them: sourcing them from a lib path spelled here named a kit
# directory, which the install-prefix leg counts (TOOL-dWitnessedBar-16 S15).
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
waived_rows=""; malformed=""; unresolved=""
if [ -f "$WAIVERS" ]; then
  _py=$(resolve_python) || { echo "dead-paths: no usable python, and $WAIVERS is read through the ledger factory -- REFUSING"; exit 2; }
  # The rows go to a scratch FILE and the loop reads the file: a loop fed by a here-string over a
  # command substitution's value is the stall `sh_hygiene.py` gates (TOOL-dWitnessedBar-16 S15).
  _wfile=$(mktemp) || { echo "dead-paths: no scratch file could be made for $WAIVERS -- REFUSING"; exit 2; }
  trap 'rm -f "$_wfile"' EXIT
  ("$_py" -I -c '
import sys
sys.path.insert(0, sys.argv[1])
import legacy_ledger as LL
rows, bad = LL.read_rows(sys.argv[2], 2, verbatim=(1,))
for entry in bad:
    print("BAD\t" + LL.render_malformed(entry).replace("\t", " "))
for (path, text), (count, _tail, _number, _row) in sorted(rows.items(), key=lambda kv: kv[1][2]):
    print("ROW\t%s\t%d\t%s" % (path, count, text))' "$_self_dir/lib" "$WAIVERS" | tr -d '\r'; exit "${PIPESTATUS[0]}") \
    > "$_wfile" || { echo "dead-paths: the ledger factory in $_self_dir/lib did not read $WAIVERS -- REFUSING"; exit 2; }
  while IFS= read -r _row; do
    case "$_row" in
      BAD"$TABC"*) malformed="$malformed${_row#BAD"$TABC"}
"; continue ;;
      ROW"$TABC"*) _row=${_row#ROW"$TABC"} ;;
      *) continue ;;
    esac
    _wpath=${_row%%"$TABC"*}; _rest=${_row#*"$TABC"}
    case "$_wpath" in *"{prefix}"*) _wpath=$(resolve_prefix_sh "$_wpath" "${SELF_PRE%/}") ;; esac
    _count=${_rest%%"$TABC"*}; _wtext=${_rest#*"$TABC"}
    if [ ! -f "$_wpath" ]; then
      unresolved="$unresolved$_wpath:<file is gone>
"; continue
    fi
    _word=0
    while [ "$_word" -lt "$_count" ]; do
      _word=$((_word + 1))
      _hitline=$(NEEDLE="$_wtext" ORD="$_word" awk '
          BEGIN { t = ENVIRON["NEEDLE"]; want = ENVIRON["ORD"] + 0; n = 0 }
          { s = $0; sub(/\r$/, "", s); sub(/^[ \t]+/, "", s); sub(/[ \t]+$/, "", s)
            if (s == t) { n++; if (n == want) { print NR; exit } } }
          END { }' "$_wpath")
      if [ -z "$_hitline" ]; then
        unresolved="$unresolved$_wpath:<no occurrence $_word of that text>
"; continue
      fi
      waived_rows="$waived_rows$_wpath:$_hitline
"
    done
  done < "$_wfile"
fi
waived_rows=$(printf '%s' "$waived_rows" | grep -c . >/dev/null 2>&1 && printf '%s' "$waived_rows" | sed '/^$/d' || true)
waived_n=$(printf '%s\n' "$waived_rows" | grep -c . || true)

# A row that cannot be RESOLVED is reported by its own reason and never by omission. Dropping it from
# the waived set would make it look like a row nobody wrote, and the carrier it excused would come
# back as an ordinary unwaived hit with no trace of the waiver that stopped covering it.
if [ -n "$malformed" ]; then
  echo "dead-paths: MALFORMED waiver row(s) -- the ordinal is absent, zero or not a number:"
  printf '%s' "$malformed" | sed '/^$/d' | sed 's/^/  /'
  exit 1
fi

if [ "$MODE" = --list ]; then
  echo "dead-paths: $(printf '%s\n' "$hits" | grep -c .) hit(s) over $(printf '%s\n' "$needles" | grep -c .) derived needle(s)"
  printf '%s\n' "$hits" | while IFS= read -r h; do
    [ -n "$h" ] || continue
    if printf '%s\n' "$waived_rows" | grep -qxF "$h"; then printf '  waived  %s\n' "$h"
    else printf '  HIT     %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"; fi
  done
  exit 0
fi

# SET DIFFERENCE, not a grep per row. Same reason as the needle pass above: the loops below now only
# ever walk the rows that will actually be printed.
#
# NO `-e ''` GUARD ON THE PATTERN SIDE, which the first draft carried to "handle" an empty registry.
# MEASURED: `grep -vxF -e '' -f <file>` ignores the `-f` patterns entirely — all nine waived hits on
# this tree came back as unwaived. It is not needed either: `-f` with a pattern file that is empty,
# or that holds a single empty line, contributes no matches under `-xF`, so both spellings of an
# absent registry already behave. Checked both by hand rather than reasoned about.
unwaived=$(printf '%s\n' "$hits" | grep -vxF -f <(printf '%s' "$waived_rows") || true)
stale_rows=$(printf '%s\n' "$waived_rows" | grep -vxF -f <(printf '%s' "$hits") || true)

bad=0
for h in $unwaived; do
  if [ "$bad" = 0 ]; then
    echo "dead-paths: a file outside memory/, or a map dossier, names a path this repo DELETED or renamed away. A reader"
    echo "dead-paths: who follows it finds nothing, and nothing else in the bar reds. Repoint it at what"
    echo "dead-paths: replaced the file, or add a row to $WAIVERS with the reason the name must stay."
  fi
  bad=$((bad+1))
  printf '  %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"
done
[ "$bad" = 0 ] || exit 1

# A waiver that no longer names a hit is a stale row: the carrier it excused is gone, and leaving it
# lets the NEXT one in silently under a pin that never fell.
stale=0
for w in $stale_rows; do
  [ "$stale" = 0 ] && echo "dead-paths: stale waiver(s) — the carrier they excuse is gone; delete the row:"
  stale=$((stale+1)); printf '  %s\n' "$w"
done
# UNRESOLVED rows are stale too, and are reported with the reason they could not resolve: the file is
# gone, or the text was REWORDED and the carrier it excused no longer exists. Re-pointing such a row
# at whatever now sits nearby is the proximity error that earned this whole re-key.
if [ -n "$unresolved" ]; then
  [ "$stale" = 0 ] && echo "dead-paths: stale waiver(s) — the carrier they excuse is gone; delete the row:"
  printf '%s' "$unresolved" | sed '/^$/d' | sed 's/^/  /'
  stale=$((stale+1))
fi
[ "$stale" = 0 ] || exit 1

echo "dead-paths: clean — $(printf '%s\n' "$needles" | grep -c .) derived needle(s), $waived_n declared waiver(s), no undeclared carrier"
