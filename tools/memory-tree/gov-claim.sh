#!/usr/bin/env bash
# gov-claim.sh — a slug's claim ref and an ask family's counter ref on the remote, each written by a
# leased compare-and-swap through the one governance ref writer (TOOL-dTotalRecall-3).
#
#   bash <this kit>/gov-claim.sh slug <slug> --claimant <key> [--offline warn|refuse|follow-leases]
#   bash <this kit>/gov-claim.sh ask <FAMILY> <slug> --claimant <key> [--offline warn|refuse|follow-leases]
#
# Exit and the one line it prints on stdout:
#   0 `claimed refs/gov/claims/<slug> <sha>`  the slug is this claimant's, new or replayed
#   0 `minted <FAMILY>-<slug>-<n>`             the id, new or replayed
#   0 `local <ref> · no remote`                the clone declares no remote, so no clone shares a namespace
#   1 `taken <ref> by <claimant-key>`          another claimant holds the slug
#   2 `refused <why>`                          offline under `refuse`, a malformed argument, a refused
#                                              remote, or a push not completed
#   4 `waiting offline <ref>`                  offline under `warn` or `follow-leases`; nothing written or queued
#
# THE ARGUMENTS ARE VALIDATED BEFORE ANY REMOTE CALL (`check_claim_args`): `<key>` is twelve lowercase hex
# digits; `<FAMILY>` is a prefix of the `FAMILIES` pairs in `.memory-tree.conf`, which this sources as
# the hygiene gate does; `<slug>` matches the admit grammar `id_grammar.py --print slug-re <root>`
# prints, the mint grammar being the caller's; `--offline` absent is `refuse`; and
# CLAUDE_CODE_SESSION_ID, written on the `session:` line, is letters, digits and dashes or unset. The
# slug `asks` is refused to the `slug` verb, since `refs/gov/claims/asks/` is the counters' subtree.
# Every ref name is built from validated parts only.
#
# THE SLUG CLAIM is `refs/gov/claims/<slug>`, in the claim grammar `--entry-claim` writes: a header
# `gov-claim claims/<slug>`, a blank line, `claimant-key: <key>` and `session: <id or absent>`. One
# bounded fetch reads it into this node's cache ref `refs/gov/remote/claims/<slug>`. Present, its
# first-parent history carrying this key is a replay, exit 0, and any other is exit 1, `taken`; absent,
# it is created by a push leased on empty, and a lost create is read again as present. A later commit on
# it is parented on its tip, so its root commit, the claim, never changes, and no writer deletes it:
# `remove_gov_ref` refuses every ref under `refs/gov/claims/`.
# THE COUNTER is `refs/gov/claims/asks/<FAMILY>-<slug>`, its tip holding the last minted `seq:`, its
# commits adding `family:` and `seq:` to the claim's keys. One bounded fetch reads it and the remote's
# default branch; a replay prints that commit's id; else the next id is the greater of the tip's `seq`
# and the highest `<FAMILY>-<slug>-<n>` a tracked file of the default branch tip or of HEAD names, plus
# one, pushed leased on the tip read. A lost push repeats from the fetch, up to three times.
# A WRITE NOT COMPLETED IS READ AGAIN ONCE: two creates racing on one ref leave the loser refused by the
# remote itself, `(reference already exists)`, which the writer reads as not completed, so a ref that
# then reads moved off the tip leased on is a lost race, and an unmoved one the refusal, exit 2.
# OFFLINE, a fetch that does not answer, writes nothing and queues nothing, the route `--entry-claim`
# takes over the same namespace: `refuse` exits 2, `warn` and `follow-leases` exit 4.
#
# WHAT THIS DOES NOT CHECK: an id a build's run minted on a branch no remote holds yet, which the floor
# cannot see; a replay older than the 64 first-parent commits it reads; and whether the remote's
# default branch is the one the caller lands on, which the remote ladder answers.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
# The blocks below are INLINE, byte-identical to their canonical copies in gov's lib dir, because this
# kit is copy-installed and that dir ships nothing; its resolve-python.test.sh reds a copy that drifts.
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
# >>> gov_feed_sh — canonical copy: gov-feed.sh in gov's lib dir (byte-identical; gated)
# THE NODE LOCKS (TOOL-dPlacedRequest-24): a node-local file two sessions of this node write, the
# feed's log and the offline queue's, is read and written only under a lock directory beside it in
# the common dir, taken through `write_dir_lock_wait` with the stem `node`, so a stale break appends
# `node-lock-broken` or `node-guard-cleared`. NODE_LOCK_BOUND is the seconds a node lock may hold,
# a pinned literal over every section it covers (TOOL-dPlacedRequest-49 S33): the feed append,
# `add_feed_event`; the queue's append, `add_gov_queue`, and its flush's two file passes,
# `write_gov_queue`, which pushes with no lock held; the offline write's hold through
# `write_gov_queue_hold`, from its read of the queue through its append, which builds the commit but
# never pushes; and `write_request_record`'s compare, copy and `.typed` append. The longest is the
# offline write's hold, measured once on node d on 2026-11-20 over the lease fixture:
# 1.412 s, PINNED, under this bound.
NODE_LOCK_BOUND=10
# THE DIRECTORY LOCK (TOOL-aGraftedHelix-37), a factory (TOOL-aPiecewiseGrade-6), moved into this
# block (TOOL-dPlacedRequest-24) so every carrier holds the one definition. `write_dir_lock` takes the
# lock with `mkdir`, sets `_fl_mine=1` in the caller's shell, then writes the caller's token into
# `owner` and only then its deadline into `until` (TOOL-dPlacedRequest-49 S5), so a taken lock always
# carries the token `remove_dir_lock` matches, even where an abort stops the take. A lock it cannot
# make is broken only when `check_dir_lock_stale` reads it stale - a deadline already passed,
# or none and a directory older than two minutes - and only by the writer that takes the guard
# `<lock>.break` with `mkdir`. Holding the guard it re-reads the rule, breaks a lock still stale,
# makes it again and writes both files before it releases the guard; a re-read finding the lock live,
# or a re-make losing to a plain `mkdir`, releases the guard and reports busy. So no breaker removes
# a lock another breaker made. A guard older than one minute was left by a crash: the writer finding
# it removes it and reports busy, never taking it in the same call, and the next call breaks the
# lock. Each self-heal appends a health event, named from the caller's stem, once the guard is
# released. `write_dir_lock_wait` is the one retrying take: it calls `write_dir_lock` every 50 ms
# until it takes or its ceiling in seconds passes, read on the whole-second clock. `remove_dir_lock`
# clears the lock only while its `owner` reads the caller's token, the turnstile's nonce pattern, so
# a release never removes the fresh lock of a writer that broke it. `until` stays a bare epoch.
# WHAT THIS DOES NOT CHECK: removing an abandoned guard is itself unguarded, so two writers removing
# one at once while a third takes a fresh guard between them can admit two breakers; that needs a
# writer to die or stall for a minute inside the break, then four writers in one git dir in one
# window. An owner that outlives its recorded deadline (no runnable `timeout -k`) is breakable while
# it pushes, and its own release can land between a breaker's re-read and its removal. Both the
# deadline and the age are wall-clock reads, so a clock stepped forward breaks a live lock.
# A writer in another git dir takes another lock. Each event goes through the `health_log_sh` block
# every carrier holds beside this one (TOOL-dPlacedRequest-36), to `resolve_health_log` of `ROOT`
# where the driver sets it, so its spec-tokens lock in the sidecar dir logs to the repository's log,
# else of the lock's parent, which for a node lock is the common dir: no unset name under `set -u`.
# THE OWNER'S PROCESSES, read as data in the lock (TOOL-aPiecewiseGrade-6 S9). A holder may write one
# `pid.<role>` file per process with `write_dir_lock_pid`: the pid, its procfs start token or `-`, the
# writer's runtime as `$HOSTNAME:$OSTYPE`, and an optional end file, last because a path may carry a
# space. `check_dir_lock_stale` also reads a lock stale when it holds at least one such file and every
# one names a process gone: a digit pid, this runtime, `check_proc_gone` answering gone, and an end
# file that exists or whose directory is gone, or none recorded. An empty file, the pending `-`, a
# foreign runtime or a missing stamp reads live. A lock with no pid file keeps the deadline and age
# rule alone. The procfs read is `${PROCFS_ROOT:-/proc}`: the driver sets PROCFS_ROOT from its fixture
# seam, and a carrier with no driver reads `/proc`.
# WHAT THIS DOES NOT CHECK: two process tables printing one `$HOSTNAME:$OSTYPE`, such as two MSYS
# installs on one host, read each other's pids gone and can break a live lock; and a reused pid with
# no token reads live, so its lock waits for the deadline.
PT_TOKEN=""
read_proc_token() { # pid -> sets PT_TOKEN to its procfs start token, or `-` when procfs cannot say
  local _l="" _r
  local -a _f
  PT_TOKEN=-
  case "${1:-}" in ""|*[!0-9]*) return 0 ;; esac
  { IFS= read -r _l < "${PROCFS_ROOT:-/proc}/$1/stat" || [ -n "$_l" ]; } 2>/dev/null || return 0
  # EVERY FIELD AFTER THE LAST `)` IS NUMERIC OR ONE LETTER. The command name inside the parentheses
  # may carry spaces and parentheses of its own, so the split starts after it: field 3 is `_f[0]`.
  _r=${_l##*) }
  read -r -a _f <<<"$_r"
  [ "${#_f[@]}" -ge 20 ] || return 0
  case "${_f[19]}" in ""|*[!0-9]*) return 0 ;; esac
  PT_TOKEN=${_f[19]}
  return 0
}
# Is the RECORDED process still there? Dead, or its pid now carrying another start token, is gone.
check_proc_gone() { # pid · recorded token -> 0 when that process no longer exists
  kill -0 "$1" 2>/dev/null || return 0
  [ "${2:--}" != - ] || return 1
  read_proc_token "$1"
  [ "$PT_TOKEN" != - ] && [ "$PT_TOKEN" != "$2" ] && return 0
  return 1
}
check_dir_lock_stale() { # lock dir -> 0 when its deadline passed, or it has none and is older than two minutes, or every process it records is gone
  local lu="" f p t w e n=0; { read -r lu <"$1/until"; } 2>/dev/null || :
  case "$lu" in *[!0-9]*) lu="" ;; esac
  for f in "$1"/pid.*; do
    [ -f "$f" ] || continue
    p=""; t=""; w=""; e=""; { read -r p t w e <"$f"; } 2>/dev/null || :
    case "$p" in ""|*[!0-9]*) n=-1; break ;; esac
    [ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ] && check_proc_gone "$p" "$t" \
      && { [ -z "$e" ] || [ -e "$e" ] || [ ! -d "${e%/*}" ]; } || { n=-1; break; }
    n=$((n + 1))
  done
  [ "$n" -le 0 ] || return 0
  if [ -n "$lu" ]; then [ "$lu" -lt "$EPOCHSECONDS" ]; return; fi
  [ -n "$(find "$1" -maxdepth 0 -mmin +2 2>/dev/null)" ]
}
write_dir_lock_pid() { # lock dir · role · pid, or - for pending · end file, optional -> <lock>/pid.<role> written; always 0
  read_proc_token "$3"
  printf '%s %s %s %s\n' "$3" "$PT_TOKEN" "${HOSTNAME:-}:${OSTYPE:-}" "${4:-}" >"$1/pid.$2" 2>/dev/null || :
  return 0
}
write_dir_lock() { # lock dir · owner token · seconds it may hold · health-event stem -> 0 taken, 1 busy
  local lk="$1" g="$1.break" broke=""
  if ! mkdir "$lk" 2>/dev/null; then
    check_dir_lock_stale "$lk" || return 1
    if ! mkdir "$g" 2>/dev/null; then
      if [ -n "$(find "$g" -maxdepth 0 -mmin +1 2>/dev/null)" ]; then
        rm -rf "$g"
        add_health_event "$(resolve_health_log "${ROOT:-${1%/*}}")" unattended "$4-guard-cleared" "$g"
      fi
      return 1
    fi
    if ! check_dir_lock_stale "$lk"; then rmdir "$g" 2>/dev/null; return 1; fi
    rm -rf "$lk"
    mkdir "$lk" 2>/dev/null || { rmdir "$g" 2>/dev/null; return 1; }
    broke=1
  fi
  _fl_mine=1
  printf '%s\n' "$2" >"$lk/owner" 2>/dev/null || :
  printf '%s\n' "$(( $EPOCHSECONDS + $3 ))" >"$lk/until" 2>/dev/null || :
  if [ -n "$broke" ]; then
    rmdir "$g" 2>/dev/null
    add_health_event "$(resolve_health_log "${ROOT:-${1%/*}}")" unattended "$4-lock-broken" "$lk"
  fi
  return 0
}
write_dir_lock_wait() { # lock dir · owner token · seconds it may hold · health-event stem · seconds to wait -> 0 taken, 1 busy
  local end=$(( EPOCHSECONDS + ${5:-0} ))
  until write_dir_lock "$1" "$2" "$3" "$4"; do
    [ "$EPOCHSECONDS" -lt "$end" ] || return 1
    sleep 0.05
  done
  return 0
}
remove_dir_lock() { # lock dir · owner token -> removes it only while its owner file reads that token
  local o=""; { read -r o <"$1/owner"; } 2>/dev/null || :
  [ -n "$2" ] && [ "$o" = "$2" ] && rm -rf "$1"
  return 0
}
# I4, THE CHANGE FEED (TOOL-dPlacedRequest-13): `<git-common-dir>/gov-feed.log`, node-local and never
# pushed, one LF-terminated line per governance ref write this node made or saw, six TAB fields:
# seq (a positive integer rising across refs), ref (the remote ref name), kind (the segment after
# `refs/gov/`), blob (the commit's tree, `-` on a deletion), commit (40 hex, 40 zeros on a deletion)
# and seen-utc (`2026-10-25T14:03:07Z`, this node's clock at the append). The key is ref, blob and
# commit. `write_gov_ref`'s success exit calls `write_feed_success`, which calls `add_feed_event`, so every
# writer joins by construction.
# APPENDING ONCE: under the feed's node lock (above, a 5 s wait) an event whose blob and commit
# equal the newest line of its ref appends nothing (TOOL-dPlacedRequest-27), so a retry appends nothing and a repeat with another
# event of the ref between, a second clear of `bar-red` say, appends again; `seq` is one more
# than the larger of the counter `gov-feed.seq` and the last all-digit first field of the log, so a
# lagging counter never repeats a `seq`; a last byte that is not LF is closed with one first, so a
# torn line stays for `check_feed` to name. A failure prints ONE `feed: NOTE -` line on stderr and
# returns 0, as the health log's appender does: the governance write already landed.
# THE CONTAINED APPEND (TOOL-dPlacedRequest-39): the clock test, the common dir and the git reads run
# in the caller's shell; the lock, the key check, the counter and the append run in a subshell whose
# `EXIT` trap is armed BEFORE the take (TOOL-dPlacedRequest-49 S6) and acts only once `write_dir_lock`
# has set `_fl_mine`, which the subshell empties first: it then releases the lock directory where its
# `owner` reads this call's token, and clears one with no `owner` only while no `gov-feed.lock.break`
# guard exists (TOOL-dPlacedRequest-52 S20); every other lock it leaves. A breaker in `write_dir_lock`
# holds that guard from before its `rm -rf` until after it writes `owner`, so a breaker's window is
# never cleared. So an abort anywhere after the `mkdir`, an unbound
# name under a carrier's `set -u`, a function no carrier defines or a failed write, ends the subshell
# alone: the append prints `feed: NOTE - <ref>: the append exited <rc>` and returns 0, and no lock is
# left for the next writer to wait out; a busy take, exit 3, finds the flag empty and leaves the
# holder's lock. The subshell sets no global a caller reads. WHAT THIS DOES NOT CHECK: the one window
# left is a third writer's own `mkdir`-to-`owner` window, after a peer broke this writer's lock and
# released it, which a holder that outlives NODE_LOCK_BOUND and a full peer cycle can find at its exit
# and clear; an abort after the line is written reads as a NOTE all the same.
# THE BASH FLOOR (TOOL-dPlacedRequest-37): a node lock's deadline reads `EPOCHSECONDS`, bash 5's,
# and this is the one take a carrier with no driver reaches, so where it is unset the append prints
# one `feed: NOTE -` line naming it and returns 0, before it touches the lock, the log or git.
# THE CACHE `refs/gov/remote/<tail>` mirrors `refs/gov/<tail>` on the remote: what this node fetched
# and, through `write_gov_ref`, what it wrote. `add_feed_sightings` appends, oldest first, the unseen
# first-parent chain of every cached ref whose tip is not the commit of the feed's newest line for
# that ref, stopping at that commit or at the first commit not authored `gov-claim`, appended as a
# lone event, so a ref another node set back to a commit an older line holds is sighted again.
# `derive_feed_events` is the same walk with no feed to stop at; `check_feed` holds a feed to it per
# ref git still holds (`missing`, `duplicate` for two consecutive events of one ref with one blob and
# commit, `extra` on a ref whose tip is a `gov-claim` commit, `order`, `torn`), and `write_feed`
# writes it as a fresh feed where none is present.
# GOVFEED_DIR names the common dir; unset, the first call resolves it once for the process.
# WHAT THIS DOES NOT CHECK: two breakers the guard's own blind spots (above) admit can both append, which
# gives two events one `seq` and loses none; `seq` and `seen-utc` are node-local and never compared; a
# ref's events from before a deletion of it are outside every chain git holds and are not compared;
# a retry made after another event of its ref landed appends again, an event that did happen.
# A staging name beside <dest> that nobody can know before it is written: <dest>.<SRANDOM twice>.tmp, or
# mktemp -u's where bash has no SRANDOM; 1 when neither names one. The run-gates runner carries the same line.
derive_temp_path() { if [ -n "${SRANDOM:-}" ]; then printf -v "$1" '%s.%s%s.tmp' "$2" "$SRANDOM" "$SRANDOM"; else printf -v "$1" '%s' "$(mktemp -u "$2.XXXXXXXX" 2>/dev/null)"; [ -n "${!1}" ]; fi; }
add_feed_event() {   # ref · commit, or empty for a deletion -> 0 always, the event appended once
  local ref="$1" c="${2:-}" d k t=- r s=0 l n now tok rc=0
  [ -n "${EPOCHSECONDS:-}" ] || { printf 'feed: NOTE - no EPOCHSECONDS, bash 5 or later is required\n' >&2; return 0; }
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -n "$d" ] || { printf 'feed: NOTE - no git common dir resolves here, so this write of %s is not in the feed\n' "$ref" >&2; return 0; }
  k=${ref#refs/gov/}; k=${k%%/*}
  if [ -z "$c" ]; then
    c=0000000000000000000000000000000000000000
  else
    r=$(git rev-parse "$c^{commit}" "$c^{tree}" 2>/dev/null) || r=""
    r=${r//$'\r'/}; c=${r%%$'\n'*}; t=${r#*$'\n'}
    [ "${#c}:${#t}" = 40:40 ] || c=""
    case "$c$t" in *[!0-9a-f]*|"") printf 'feed: NOTE - %s names no commit this clone holds, so the write is not in the feed\n' "$ref" >&2; return 0 ;; esac
  fi
  tok="$BASHPID.$RANDOM"
  ( _fl_mine=
    trap '[ -z "$_fl_mine" ] || { [ -s "$d/gov-feed.lock/owner" ] || [ -e "$d/gov-feed.lock.break" ] || rm -rf "$d/gov-feed.lock"; remove_dir_lock "$d/gov-feed.lock" "$tok"; }' EXIT
    write_dir_lock_wait "$d/gov-feed.lock" "$tok" "$NODE_LOCK_BOUND" node 5 || exit 3
    if [ -f "$d/gov-feed.log" ] && FEED_EV="$ref"$'\t'"$t"$'\t'"$c" awk -F'\t' '
        BEGIN { split(ENVIRON["FEED_EV"], ev, "\t") }
        $2 == ev[1] { p = $4 "\t" $5 }
        END { exit !(p == ev[2] "\t" ev[3]) }' "$d/gov-feed.log" 2>/dev/null; then
      exit 0
    fi
    if [ -f "$d/gov-feed.seq" ]; then { read -r s <"$d/gov-feed.seq"; } 2>/dev/null || :; fi
    s=${s%$'\r'}
    case "$s" in ""|*[!0-9]*) s=0 ;; esac
    l=0
    if [ -s "$d/gov-feed.log" ]; then
      l=$(awk -F'\t' '$1 ~ /^[0-9]+$/ { s = $1 } END { print s + 0 }' "$d/gov-feed.log" 2>/dev/null) || l=0
      case "$l" in ""|*[!0-9]*) l=0 ;; esac
      [ -z "$(tail -c1 "$d/gov-feed.log" 2>/dev/null)" ] || printf '\n' >>"$d/gov-feed.log"
    fi
    n=$(( (10#$s > 10#$l ? 10#$s : 10#$l) + 1 ))
    TZ=UTC printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1
    if ! printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$n" "$ref" "$k" "$t" "$c" "$now" >>"$d/gov-feed.log" 2>/dev/null; then
      printf 'feed: NOTE - %s/gov-feed.log could not be written, so this write of %s at %s is not in the feed\n' "$d" "$ref" "$c" >&2
    elif st=""; ! { derive_temp_path st "$d/gov-feed.seq" && printf '%s\n' "$n" >"$st" && mv -f "$st" "$d/gov-feed.seq"; } 2>/dev/null; then
      [ -z "$st" ] || rm -f "$st" 2>/dev/null
      printf 'feed: NOTE - %s/gov-feed.seq could not be written; the next append reads the log past it\n' "$d" >&2
    fi
    exit 0 ) || rc=$?
  case "$rc" in
    0) ;;
    3) printf 'feed: NOTE - the feed lock in %s was held for 5s, so this write of %s at %s is not in the feed\n' "$d" "$ref" "$c" >&2 ;;
    *) printf 'feed: NOTE - %s: the append exited %s\n' "$ref" "$rc" >&2 ;;
  esac
  return 0
}
# THE ONE SUCCESS EXIT (TOOL-dPlacedRequest-34 S5): a governance write that landed sets this node's cache
# ref `refs/gov/remote/<tail>` to the commit it wrote, or clears it on a deletion, then appends the event,
# so the cache always names what this node last wrote or fetched. `write_gov_ref` calls it, and so does a
# carrier whose push is no `write_gov_ref` call, the lander's fenced beat (S6). A cache ref git cannot
# move prints ONE `feed: NOTE -` line and the event is appended all the same: the write already landed.
write_feed_success() { # ref · commit, or empty for a deletion -> 0 always; the cache ref set or cleared, the event appended
  if [ -n "${2:-}" ]; then git update-ref "refs/gov/remote/${1#refs/gov/}" "$2" 2>/dev/null
  else git update-ref -d "refs/gov/remote/${1#refs/gov/}" 2>/dev/null; fi \
    || printf 'feed: NOTE - the cache ref refs/gov/remote/%s was not set to this write\n' "${1#refs/gov/}" >&2
  add_feed_event "$1" "${2:-}"
  return 0
}
derive_feed_events() { # cache prefix · [feed file] -> `ref TAB kind TAB blob TAB commit` per event, per ref oldest first
  local pre="${1%/}/" feed="${2:-}" rows r t g s
  rows=$(git for-each-ref --format='%(refname) %(objectname)' "$pre" 2>/dev/null | FEED_FILE="$feed" FEED_PRE="$pre" awk '
    BEGIN { f = ENVIRON["FEED_FILE"]
            if (f != "") while ((getline ln < f) > 0) {
              sub(/\r$/, "", ln)
              if (split(ln, x, "\t") < 5) continue
              newest[x[2]] = x[5] } }
    { sub(/\r$/, ""); g = "refs/gov/" substr($1, length(ENVIRON["FEED_PRE"]) + 1)
      if ((g in newest) && newest[g] == $2) next
      print $2, g, (g in newest ? newest[g] : "-") }')
  [ -n "$rows" ] || return 0
  printf '%s\n' "$rows" | while read -r t g s; do
    git log --first-parent --format='%H %T %an' "$t" 2>/dev/null | awk -v ref="$g" -v stop="$s" '
      { sub(/\r$/, "") }
      $1 == stop { exit }
      { a = $0; sub(/^[^ ]+ [^ ]+ /, "", a); n++; h[n] = $1; tr[n] = $2; if (a != "gov-claim") exit }
      END { k = ref; sub(/^refs\/gov\//, "", k); sub(/\/.*$/, "", k)
            for (i = n; i >= 1; i--) printf "%s\t%s\t%s\t%s\n", ref, k, tr[i], h[i] }'
  done
  return 0
}
add_feed_sightings() { # cache prefix -> 0 always; every unseen commit of a cached ref appended oldest first
  local pre="${1:-refs/gov/remote/}" r k t c
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  [ -n "${GOVFEED_DIR%$'\r'}" ] || return 0
  while IFS=$'\t' read -r r k t c; do
    [ -z "$c" ] || add_feed_event "$r" "$c"
  done < <(derive_feed_events "$pre" "${GOVFEED_DIR%$'\r'}/gov-feed.log")
  return 0
}
check_feed() {       # cache prefix · [feed file, the node's by default] -> one line per finding and rc 1, or rc 0
  local pre="${1%/}/" f="${2:-}" dv au
  if [ -z "$f" ]; then
    [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
    f="${GOVFEED_DIR%$'\r'}/gov-feed.log"
  fi
  dv=$(derive_feed_events "$pre")
  au=$(git for-each-ref --format='%(refname) %(authorname)' "$pre" 2>/dev/null)
  FEED_FILE="$f" FEED_PRE="$pre" FEED_DV="$dv" FEED_AU="$au" awk '
    BEGIN {
      np = length(ENVIRON["FEED_PRE"])
      m = split(ENVIRON["FEED_AU"], a, "\n")
      for (i = 1; i <= m; i++) { ln = a[i]; sub(/\r$/, "", ln); if (ln == "") continue
        r = ln; sub(/ .*$/, "", r); au = ln; sub(/^[^ ]* /, "", au)
        g = "refs/gov/" substr(r, np + 1); held[g] = 1; if (au == "gov-claim") chain[g] = 1 }
      m = split(ENVIRON["FEED_DV"], a, "\n")
      for (i = 1; i <= m; i++) { if (split(a[i], x, "\t") != 4) continue
        dn[x[1]]++; ds[x[1], dn[x[1]]] = x[4]; inch[x[1] SUBSEP x[4]] = 1 }
      f = ENVIRON["FEED_FILE"]; bad = 0
      while ((getline ln < f) > 0) {
        sub(/\r$/, "", ln)
        if (split(ln, x, "\t") != 6) { print "torn " ln; bad = 1; continue }
        k = x[4] SUBSEP x[5]
        if ((x[2] in last) && last[x[2]] == k) { print "duplicate " x[2] " " x[5]; bad = 1; continue }
        last[x[2]] = k
        if (!(x[2] in held)) continue
        if ((x[2] SUBSEP x[5]) in inch) { fn[x[2]]++; fs[x[2], fn[x[2]]] = x[5]; got[x[2] SUBSEP x[5]] = 1 }
        else if (x[2] in chain) { print "extra " x[2] " " x[5]; bad = 1 }
      }
      for (g in dn) {
        j = 0; off = ""
        for (i = 1; i <= dn[g]; i++) {
          c = ds[g, i]
          if (!((g SUBSEP c) in got)) { print "missing " g " " c; bad = 1; continue }
          j++; if (off == "" && fs[g, j] != c) off = fs[g, j]
        }
        if (off != "") { print "order " g " " off; bad = 1 }
      }
      exit bad }'
}
write_feed() {       # cache prefix -> rc 0 the derived feed written, rc 2 naming a feed already present
  local pre="${1%/}/" d now n=0 l lt="" st=""
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -n "$d" ] || { printf 'feed: no git common dir resolves here, so no feed was rebuilt\n'; return 2; }
  if [ -e "$d/gov-feed.log" ]; then printf 'feed: a feed is present, so nothing was rebuilt over it: %s\n' "$d/gov-feed.log"; return 2; fi
  TZ=UTC printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1
  derive_temp_path lt "$d/gov-feed.log" && derive_temp_path st "$d/gov-feed.seq" \
    || { printf 'feed: no staging name resolves beside %s, so no feed was rebuilt\n' "$d/gov-feed.log"; return 2; }
  { while IFS= read -r l; do n=$((n + 1)); printf '%s\t%s\t%s\n' "$n" "$l" "$now"; done < <(derive_feed_events "$pre"); } >"$lt" \
    && printf '%s\n' "$n" >"$st" && mv -f "$st" "$d/gov-feed.seq" && mv -f "$lt" "$d/gov-feed.log" \
    || { rm -f "$lt" "$st"; printf 'feed: %s could not be written, so no feed was rebuilt\n' "$d/gov-feed.log"; return 2; }
  printf 'feed: rebuilt %s event(s) from %s into %s\n' "$n" "$pre" "$d/gov-feed.log"
  return 0
}
print_feed() {       # [seq] -> every event whose seq is at or after it, in file order
  local from="${1:-0}" d
  case "$from" in ""|*[!0-9]*) printf 'feed: a replay starts at a sequence number, not %s\n' "$from"; return 2 ;; esac
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -f "$d/gov-feed.log" ] || return 0
  awk -F'\t' -v from="$from" 'NF == 6 && $1 ~ /^[0-9]+$/ && $1 + 0 >= from + 0' "$d/gov-feed.log"
}
# THE OBSERVER CLOCK, I8 (TOOL-dPlacedRequest-17): the one reader of a first sighting. Per
# `ref TAB commit` pair on stdin, in order, the `seen-utc` of the oldest feed line of that ref and
# commit, or `-` where the feed holds none, has none of that shape, or cannot be read. Every lease
# deadline is now minus that stamp, both read on this node's clock, never the holder's `beat-utc`.
read_first_seen() {  # `ref TAB commit` pairs on stdin -> one `seen-utc` or `-` per pair
  local f=""
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  [ -z "${GOVFEED_DIR%$'\r'}" ] || f="${GOVFEED_DIR%$'\r'}/gov-feed.log"
  FEED_FILE="$f" awk -F'\t' '
    BEGIN { f = ENVIRON["FEED_FILE"]
            if (f != "") while ((getline ln < f) > 0) {
              sub(/\r$/, "", ln)
              if (split(ln, x, "\t") != 6 || x[6] !~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z$/) continue
              if (!((x[2] SUBSEP x[5]) in seen)) seen[x[2], x[5]] = x[6] } }
    { sub(/\r$/, ""); print (($1 SUBSEP $2) in seen ? seen[$1, $2] : "-") }'
}
# <<< gov_feed_sh
# >>> gov_ref_sh — canonical copy: gov-ref.sh in gov's lib dir (byte-identical; gated)
# I1 AND I2, ONE WRITER FOR EVERY GOVERNANCE REF (TOOL-dPlacedRequest-11): a run claim, the bar-red
# ref and every later register, request and card ref are written here, never by a hand copy.
# `build_gov_commit` builds the commit over the empty tree under the fixed `gov-claim` identity,
# parented on the tip its caller read, so `git log <ref>` on the remote lists every write in order; a
# create, whose tip read is empty, is the one parentless commit. It prints nothing and returns 1 when
# git cannot build it. `write_gov_ref` pushes `--porcelain --force-with-lease=<ref>:<expected>`, the
# expected sha EMPTY for a create, and the porcelain line whose second field ends in `:<ref>` decides,
# never the exit alone: `!` with `(stale info)` or `(fetch first)` is 1, LOST; any other `!`, no status
# line, or the bound firing (124) is 2, NOT COMPLETED; any other flag is 0. The cause is in
# GOVREF_WHY. An EMPTY source returns 2 `no source` and pushes nothing, so a failed build captured as
# `c=$(build_gov_commit …)` is never a deletion; `remove_gov_ref` is the one deletion form, its
# expected sha non-empty, and it reaches the same push and porcelain read through `write_gov_ref`,
# which admits an empty source only when `remove_gov_ref` is its caller. NO CLAIM REF IS PRUNED
# (TOOL-dTotalRecall-3 S5): `remove_gov_ref` returns 2 for any ref under `refs/gov/claims/`, a slug's
# claim and an ask family's counter, naming the rule in GOVREF_WHY, before it reaches the push.
# THE CALLER SETS THREE NAMES: GOVREF_RUNNER, a function taking `<outfile> <git args…>` that runs git
# bounded and writes its stdout to the file; GOVREF_REMOTE, the remote NAME the push names, so the
# pre-push hook observes `<name>/HEAD`; GOVREF_GITDIR, the git dir whose `pre-push-refusal` a hook
# writes, empty to read no token.
# NO REFUSAL TOKEN IS THIS PUSH'S CAUSE. The refusal file is one per git dir and nothing here removes
# it, so another push from the same git dir can write it while this call runs: a token newer than the
# stamp this call created just before its push is appended on rc 2 as an ADVISORY only. The
# `default-branch` hint comes from this call's own read: rc 2 and no `refs/remotes/<name>/HEAD`.
# The stamp is a scratch file of its own, never the push's output file, which git writes after the
# hook ran and so would read every token as stale.
# THE ONE SUCCESS EXIT JOINS THE FEED (TOOL-dPlacedRequest-13 S3): it calls `write_feed_success` from
# the `gov_feed_sh` block every carrier of this one carries beside it (TOOL-dPlacedRequest-34 S5), which
# sets this node's cache ref `refs/gov/remote/<tail>` to what it wrote, or clears it on a deletion, and
# appends the event. A lost or uncompleted write appends nothing.
# WHAT THIS DOES NOT CHECK: a token written in the stamp's own filesystem tick reads as stale and is
# omitted; a token another push wrote during this call reads as fresh and is printed beside this
# push's own cause, never as it.
build_gov_commit() { # tip read or empty · message -> prints the commit; rc 1 when git cannot build it
  local t c
  local -a p=()
  [ -z "$1" ] || p=(-p "$1")
  t=$(git mktree </dev/null 2>/dev/null) && [ -n "$t" ] || return 1
  c=$(GIT_AUTHOR_NAME=gov-claim GIT_AUTHOR_EMAIL=gov-claim@invalid GIT_COMMITTER_NAME=gov-claim GIT_COMMITTER_EMAIL=gov-claim@invalid \
    git commit-tree "$t" "${p[@]}" -m "$2" 2>/dev/null) && [ -n "$c" ] || return 1
  printf '%s\n' "$c"
}
write_gov_ref() {    # ref · expected sha or empty · src -> 0 written, 1 lost, 2 not completed; GOVREF_WHY
  local ref="$1" exp="$2" src="$3" s f rc l line rf="" tok="" hd=""
  GOVREF_WHY=""
  if [ -z "$src" ] && [ "${FUNCNAME[1]:-}" != remove_gov_ref ]; then GOVREF_WHY="no source"; return 2; fi
  s=$(mktemp) || { GOVREF_WHY="cannot create a scratch file to bound the push"; return 2; }
  f=$(mktemp) || { rm -f "$s"; GOVREF_WHY="cannot create a scratch file to bound the push"; return 2; }
  "$GOVREF_RUNNER" "$f" push --porcelain "--force-with-lease=$ref:$exp" "$GOVREF_REMOTE" "$src:$ref" && rc=0 || rc=$?
  line=""
  while IFS= read -r l; do
    case "$l" in ?$'\t'*":$ref"$'\t'*) line=${l%$'\r'} ;; esac
  done <"$f"
  if [ "$rc" = 124 ]; then GOVREF_WHY="the push was killed by this kit's own bound"; rc=2
  elif [ -z "$line" ]; then GOVREF_WHY="git push exited $rc and printed no status line for $ref"; rc=2
  elif [ "${line:0:1}" != '!' ]; then rc=0
  else
    case "$line" in
      *"(stale info)"*|*"(fetch first)"*) GOVREF_WHY="lost the race on the lease: ${line##*$'\t'}"; rc=1 ;;
      *) GOVREF_WHY="the push was refused: ${line##*$'\t'}"; rc=2 ;;
    esac
  fi
  if [ "$rc" = 2 ]; then
    [ -z "${GOVREF_GITDIR:-}" ] || rf="$GOVREF_GITDIR/pre-push-refusal"
    if [ -n "$rf" ] && [ "$rf" -nt "$s" ]; then
      { IFS=$'\t' read -r tok _ <"$rf"; } 2>/dev/null || :
      GOVREF_WHY="$GOVREF_WHY · a pre-push refusal was recorded during this push: ${tok:-an empty refusal file}"
    fi
    hd=$(git symbolic-ref -q "refs/remotes/$GOVREF_REMOTE/HEAD" 2>/dev/null) || hd=""
    [ -n "$hd" ] || GOVREF_WHY="$GOVREF_WHY · default-branch · fix once: git remote set-head $GOVREF_REMOTE -a"
  fi
  rm -f "$s" "$f"
  [ "$rc" = 0 ] || return "$rc"
  write_feed_success "$ref" "$src"
  return 0
}
remove_gov_ref() {   # ref · expected sha -> as write_gov_ref, pushing the ref's deletion
  GOVREF_WHY=""
  case "$1" in refs/gov/claims/*) GOVREF_WHY="a ref under refs/gov/claims/ is never deleted: a claim and a counter are append-only"; return 2 ;; esac
  [ -n "$2" ] || { GOVREF_WHY="no expected sha"; return 2; }
  write_gov_ref "$1" "$2" ""
}
# <<< gov_ref_sh

GC_USAGE="usage: gov-claim.sh slug <slug> --claimant <key> [--offline warn|refuse|follow-leases] | ask <FAMILY> <slug> --claimant <key> [--offline <value>]"
GC_VERB=""; GC_FAMILY=""; GC_SLUG=""; GC_KEY=""; GC_OFFLINE=refuse; GC_SESSION=absent; GC_ROOT=""
GC_REF=""; GC_CACHE=""; GC_WHY=""

# ---- the bounded network call, in the shape of post-merge's `run_remote` --------------------------
GC_BOUND=60; GC_CONNECT_BOUND=20; GC_LOWSPEED_BYTES=1000
GC_BOUND_LIVE=1
timeout -k 1s 10 true >/dev/null 2>&1 || GC_BOUND_LIVE=0
run_claim_remote() { # <outfile> · <git args…> -> rc (124 = the wall fired); output to a FILE, never a pipe
  local out=$1; shift
  local -a pre=()
  [ "$GC_BOUND_LIVE" = 1 ] && pre=(timeout -k 5s "$GC_BOUND")
  "${pre[@]}" env GIT_TERMINAL_PROMPT=0 \
      "GIT_SSH_COMMAND=ssh -o ConnectTimeout=$GC_CONNECT_BOUND -o BatchMode=yes" \
    git -c credential.interactive=never \
        -c "http.lowSpeedLimit=$GC_LOWSPEED_BYTES" -c "http.lowSpeedTime=$GC_BOUND" \
        "$@" >"$out" 2>/dev/null
}

check_claim_args() { # argv -> 0 with GC_VERB GC_FAMILY GC_SLUG GC_KEY GC_OFFLINE GC_SESSION GC_ROOT GC_REF GC_CACHE; 1 with GC_WHY
  local -a pos=()
  local key_set="" off_set="" py re pair fams="" hit=""
  GC_WHY=""
  GC_VERB=${1:-}; [ "$#" = 0 ] || shift
  while [ "$#" -gt 0 ]; do
    case "$1" in
      --claimant|--offline)
        [ "$#" -ge 2 ] || { GC_WHY="$1 takes a value"; return 1; }
        if [ "$1" = --claimant ]; then
          [ -z "$key_set" ] || { GC_WHY="--claimant is given twice"; return 1; }
          key_set=1; GC_KEY=$2
        else
          [ -z "$off_set" ] || { GC_WHY="--offline is given twice"; return 1; }
          off_set=1; GC_OFFLINE=$2
        fi
        shift 2 ;;
      -*) GC_WHY="$1 is no option"; return 1 ;;
      *) pos+=("$1"); shift ;;
    esac
  done
  case "$GC_VERB:${#pos[@]}" in
    slug:1) GC_SLUG=${pos[0]} ;;
    ask:2) GC_FAMILY=${pos[0]}; GC_SLUG=${pos[1]} ;;
    *) GC_WHY="the verb is slug with one slug or ask with a family and a slug"; return 1 ;;
  esac
  [ -n "$key_set" ] || { GC_WHY="--claimant <key> is required"; return 1; }
  [[ $GC_KEY =~ ^[0-9a-f]{12}$ ]] || { GC_WHY="the claimant key is not twelve lowercase hex digits"; return 1; }
  case "$GC_OFFLINE" in warn|refuse|follow-leases) ;; *) GC_WHY="--offline is one of warn, refuse, follow-leases"; return 1 ;; esac
  [[ $GC_SLUG =~ ^[A-Za-z0-9]+$ ]] || { GC_WHY="the slug is not letters and digits"; return 1; }
  [ "$GC_VERB:$GC_SLUG" != slug:asks ] || { GC_WHY="the slug asks names the counters' subtree refs/gov/claims/asks/"; return 1; }
  [ -z "$GC_FAMILY" ] || [[ $GC_FAMILY =~ ^[A-Z][A-Z0-9]*$ ]] || { GC_WHY="the family is not an upper-case prefix"; return 1; }
  GC_SESSION=${CLAUDE_CODE_SESSION_ID:-absent}
  [[ $GC_SESSION =~ ^[A-Za-z0-9-]+$ ]] || { GC_WHY="CLAUDE_CODE_SESSION_ID is not letters, digits and dashes"; return 1; }
  GC_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || GC_ROOT=""
  GC_ROOT=${GC_ROOT%$'\r'}
  [ -n "$GC_ROOT" ] || { GC_WHY="not inside a git work tree"; return 1; }
  if [ -n "$GC_FAMILY" ]; then
    FAMILIES=""
    [ ! -f "$GC_ROOT/.memory-tree.conf" ] || . "$GC_ROOT/.memory-tree.conf"
    for pair in $FAMILIES; do
      fams="$fams ${pair#*:}"
      [ "${pair#*:}" != "$GC_FAMILY" ] || hit=1
    done
    [ -n "$hit" ] || { GC_WHY="the family $GC_FAMILY is none of FAMILIES in .memory-tree.conf:${fams:- none}"; return 1; }
  fi
  py=$(resolve_python) || { GC_WHY="no python resolves, so the slug grammar cannot be read"; return 1; }
  re=$("$py" "$HERE/id_grammar.py" --print slug-re "$GC_ROOT" 2>/dev/null) || re=""
  re=${re%%$'\n'*}; re=${re%$'\r'}
  [ -n "$re" ] || { GC_WHY="id_grammar.py printed no slug grammar for $GC_ROOT"; return 1; }
  [[ $GC_SLUG =~ $re ]] || { GC_WHY="the slug $GC_SLUG is not admitted by the slug grammar $re"; return 1; }
  if [ "$GC_VERB" = slug ]; then GC_REF="refs/gov/claims/$GC_SLUG"
  else GC_REF="refs/gov/claims/asks/$GC_FAMILY-$GC_SLUG"; fi
  GC_CACHE="refs/gov/remote/${GC_REF#refs/gov/}"
  return 0
}

# A replay is read from the cache ref's first-parent history, newest first and at most 64 commits:
# GC_HIT is the newest commit carrying `claimant-key: <key>` and GC_SEQ its `seq`, GC_HOLDER the oldest
# claimant key read, the claim's own on a slug ref, and GC_TIP_SEQ the tip's `seq`. The log goes to a
# FILE and the loop reads the file, never a here-string of a command substitution.
GC_HIT=""; GC_SEQ=""; GC_HOLDER=""; GC_TIP_SEQ=""
read_claim_replay() { # cache ref · key -> 0 with GC_HIT and GC_SEQ where the key is in its history, else 1
  local f line sha="" k="" s="" n=0
  GC_HIT=""; GC_SEQ=""; GC_HOLDER=""; GC_TIP_SEQ=""
  f=$(mktemp) || return 1
  git log --first-parent -n 64 --format='%x01%H%n%B' "$1" -- >"$f" 2>/dev/null || { rm -f "$f"; return 1; }
  while IFS= read -r line || [ -n "$line" ]; do
    line=${line%$'\r'}
    case "$line" in
      $'\001'*)
        if [ -n "$sha" ] && [ -z "$GC_HIT" ] && [ "$k" = "$2" ]; then GC_HIT=$sha; GC_SEQ=$s; fi
        [ -z "$k" ] || GC_HOLDER=$k
        sha=${line#$'\001'}; k=""; s=""; n=$((n + 1)) ;;
      "claimant-key: "*) k=${line#claimant-key: } ;;
      "seq: "*) s=${line#seq: }; [ "$n" != 1 ] || GC_TIP_SEQ=$s ;;
    esac
  done <"$f"
  rm -f "$f"
  if [ -n "$sha" ] && [ -z "$GC_HIT" ] && [ "$k" = "$2" ]; then GC_HIT=$sha; GC_SEQ=$s; fi
  [ -z "$k" ] || GC_HOLDER=$k
  [ -n "$GC_HIT" ]
}

derive_ask_floor() { # family · slug · revs… -> prints the highest <n> of <family>-<slug>-<n> a tracked file at any rev names, 0 for none
  local fam=$1 slug=$2 f m n=0 r
  shift 2
  f=$(mktemp) || return 1
  for r in "$@"; do
    git grep -ohE "(^|[^A-Za-z0-9])$fam-$slug-[0-9]+" "$r" -- >>"$f" 2>/dev/null
  done
  while IFS= read -r m || [ -n "$m" ]; do
    m=${m%$'\r'}; m=${m##*-}
    [ "${#m}" -le 9 ] || continue
    m=$((10#$m))
    [ "$m" -le "$n" ] || n=$m
  done <"$f"
  rm -f "$f"
  printf '%s\n' "$n"
}

# Each verb's one bounded fetch reads the claim ref into its cache ref by a one-`*` refspec, so an
# absent ref is an empty answer rather than a failed fetch, and `--prune` drops a cache ref the remote
# no longer holds; the counter's fetch also takes the default branch. A fetch that does not answer is
# offline.
run_slug_claim() { # -> the exit of the table above, for GC_REF
  local f rc tip c m tries=0 why=""
  printf -v m '%s\n\n%s\n%s' "gov-claim claims/${GC_REF#refs/gov/claims/}" "claimant-key: $GC_KEY" "session: $GC_SESSION"
  while :; do
    f=$(mktemp) || { echo "refused cannot create a scratch file to bound the fetch of $GC_REF"; return 2; }
    run_claim_remote "$f" fetch --no-tags --no-write-fetch-head --no-auto-maintenance --prune "$GOVREF_REMOTE" "+$GC_REF*:$GC_CACHE*" && rc=0 || rc=$?
    rm -f "$f"
    if [ "$rc" != 0 ]; then
      [ "$GC_OFFLINE" != refuse ] || { echo "refused offline · $GC_REF · the fetch from $GOVREF_REMOTE exited $rc, and leases.offline is refuse"; return 2; }
      echo "waiting offline $GC_REF · the fetch from $GOVREF_REMOTE exited $rc, and leases.offline is $GC_OFFLINE: nothing is written or queued, so a re-run claims it once the remote answers"; return 4
    fi
    add_feed_sightings refs/gov/remote/
    tip=$(git rev-parse -q --verify "$GC_CACHE^{commit}" 2>/dev/null) && tip=${tip%$'\r'} || tip=""
    if [ -n "$tip" ]; then
      if read_claim_replay "$GC_CACHE" "$GC_KEY"; then echo "claimed $GC_REF $GC_HIT"; return 0; fi
      echo "taken $GC_REF by ${GC_HOLDER:-a claim carrying no claimant-key}"; return 1
    fi
    [ -z "$why" ] || { echo "refused $GC_REF · $why"; return 2; }
    [ "$tries" -lt 3 ] || { echo "refused $GC_REF · the create was lost and the ref then read absent, four times"; return 2; }
    c=$(build_gov_commit "" "$m") || { echo "refused $GC_REF · the claim commit could not be built in this clone"; return 2; }
    write_gov_ref "$GC_REF" "" "$c" && rc=0 || rc=$?
    case "$rc" in
      0) echo "claimed $GC_REF $c"; return 0 ;;
      1) tries=$((tries + 1)) ;;
      # A CREATE ANOTHER CLONE WON IN THE SAME INSTANT is refused by the remote itself, `[remote rejected]
      # (reference already exists)`, which the writer reads as not completed: so a write not completed
      # is read again once, a ref now present being the lost create, one still absent the refusal.
      *) why=$GOVREF_WHY ;;
    esac
  done
}

run_ask_mint() { # -> the exit of the table above, for GC_REF
  local f rc tip c m top floor next lost=0 why="" was=""
  local -a spec=("+$GC_REF*:$GC_CACHE*") revs=()
  [ -z "$RR_BRANCH" ] || spec+=("+refs/heads/$RR_BRANCH:refs/remotes/$GOVREF_REMOTE/$RR_BRANCH")
  while :; do
    f=$(mktemp) || { echo "refused cannot create a scratch file to bound the fetch of $GC_REF"; return 2; }
    run_claim_remote "$f" fetch --no-tags --no-write-fetch-head --no-auto-maintenance --prune "$GOVREF_REMOTE" "${spec[@]}" && rc=0 || rc=$?
    rm -f "$f"
    if [ "$rc" != 0 ]; then
      [ "$GC_OFFLINE" != refuse ] || { echo "refused offline · $GC_REF · the fetch from $GOVREF_REMOTE exited $rc, and leases.offline is refuse"; return 2; }
      echo "waiting offline $GC_REF · the fetch from $GOVREF_REMOTE exited $rc, and leases.offline is $GC_OFFLINE: nothing is written or queued, so a re-run mints once the remote answers"; return 4
    fi
    add_feed_sightings refs/gov/remote/
    tip=$(git rev-parse -q --verify "$GC_CACHE^{commit}" 2>/dev/null) && tip=${tip%$'\r'} || tip=""
    if [ -n "$why" ]; then
      [ "$tip" != "$was" ] || { echo "refused $GC_REF · $why"; return 2; }
      lost=$((lost + 1)); why=""
      [ "$lost" -le 3 ] || { echo "refused $GC_REF · lost the race four times, the last read again after: $GOVREF_WHY"; return 2; }
    fi
    top=0
    if [ -n "$tip" ]; then
      if read_claim_replay "$GC_CACHE" "$GC_KEY"; then
        [[ $GC_SEQ =~ ^[0-9]+$ ]] || { echo "refused $GC_REF · the replayed commit ${GC_HIT:0:12} carries no seq"; return 2; }
        echo "minted $GC_FAMILY-$GC_SLUG-$GC_SEQ"; return 0
      fi
      [[ $GC_TIP_SEQ =~ ^[0-9]{1,9}$ ]] || { echo "refused $GC_REF · its tip ${tip:0:12} carries no seq"; return 2; }
      top=$((10#$GC_TIP_SEQ))
    fi
    revs=()
    [ -z "$RR_BRANCH" ] || ! git rev-parse -q --verify "refs/remotes/$GOVREF_REMOTE/$RR_BRANCH^{commit}" >/dev/null 2>&1 \
      || revs+=("refs/remotes/$GOVREF_REMOTE/$RR_BRANCH")
    git rev-parse -q --verify "HEAD^{commit}" >/dev/null 2>&1 && revs+=(HEAD)
    floor=0
    [ "${#revs[@]}" = 0 ] || floor=$(derive_ask_floor "$GC_FAMILY" "$GC_SLUG" "${revs[@]}") \
      || { echo "refused $GC_REF · cannot create a scratch file to read the floor"; return 2; }
    [ "$floor" -le "$top" ] || top=$floor
    next=$((top + 1))
    printf -v m '%s\n\n%s\n%s\n%s\n%s' "gov-claim claims/${GC_REF#refs/gov/claims/}" "claimant-key: $GC_KEY" \
      "session: $GC_SESSION" "family: $GC_FAMILY" "seq: $next"
    c=$(build_gov_commit "$tip" "$m") || { echo "refused $GC_REF · the counter commit could not be built in this clone"; return 2; }
    write_gov_ref "$GC_REF" "$tip" "$c" && rc=0 || rc=$?
    case "$rc" in
      0) echo "minted $GC_FAMILY-$GC_SLUG-$next"; return 0 ;;
      1) lost=$((lost + 1))
         [ "$lost" -le 3 ] || { echo "refused $GC_REF · lost the race four times: $GOVREF_WHY"; return 2; } ;;
      # As the slug claim's: a write not completed is read again once, a tip moved off the one this push
      # was leased on being a lost race, an unmoved tip the refusal.
      *) why=$GOVREF_WHY; was=$tip ;;
    esac
  done
}

check_claim_args "$@" || { echo "refused $GC_WHY"; echo "$GC_USAGE" >&2; exit 2; }
cd "$GC_ROOT" || { echo "refused cannot enter $GC_ROOT"; exit 2; }
resolve_remote_sh || { echo "refused $RR_WHY"; exit 2; }
[ -n "$RR_REMOTE" ] || { echo "local $GC_REF · no remote"; exit 0; }
GOVREF_RUNNER=run_claim_remote; GOVREF_REMOTE=$RR_REMOTE
GOVREF_GITDIR=$(git rev-parse --absolute-git-dir 2>/dev/null) || GOVREF_GITDIR=""
GOVREF_GITDIR=${GOVREF_GITDIR%$'\r'}
if [ "$GC_VERB" = slug ]; then run_slug_claim; else run_ask_mint; fi
exit $?
