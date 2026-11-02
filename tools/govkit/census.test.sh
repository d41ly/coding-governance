#!/usr/bin/env bash
# Arms for <prefix>/govkit/census.py — DEPL-dRetiredFork-7.
#
# DELIBERATELY NOT A BAR LEG, and this header states the compensating check rather than leaving
# the exemption bare (§7: an exemption is not coverage). The census reads repositories gov does
# not own; nothing on gov's bar reaches outside this repository, so a leg that ran it would
# either red on a machine where the adopters are absent or pass by finding nothing — the
# green-by-absence shape this build has spent units removing. Compensating check: these arms run
# ON DEMAND against SYNTHETIC repositories built here, so they need no adopter present and are
# the thing to run whenever census.py changes.
#
#   bash <prefix>/govkit/census.test.sh
#
# Every arm below builds its own gov and its own adopter. None of them reads a real adopter tree:
# a fixture that depends on inCMS's current bytes grades a moving target and reports the wrong
# thing on the day inCMS changes.

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
KIT_REL=$(derive_self_rel "$HERE") || { echo "census.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
HERE=$(cd "$(dirname "$0")/../.." && pwd)
CENSUS="$HERE/$KIT_REL/census.py"   # this kit's own file, by the directory it sits in (TOOL-aRepatriatedFork-46)

# THROUGH THE ONE RESOLVER, never a bare launcher name. The MS-Store `python3` stub answers
# `command -v` and then exits 9009, so a bare name is not an answer — and the invocation ban in
# `<prefix>/lib/resolve-python.test.sh` refuses one repo-wide, which is how this file was caught:
# it shipped with six bare `python` calls and redded that leg on the closing bar.
# TOOL-aRepatriatedFork-46: carried INLINE; it was sourced from the library directory, which ships nowhere.
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
PY="$(resolve_python)"
n=0; st=0

ok()   { n=$((n+1)); echo "ok   $1"; }
bad()  { n=$((n+1)); echo "FAIL $1"; st=1; }
has()  { case "$1" in *"$2"*) return 0 ;; *) return 1 ;; esac; }

# ---------------------------------------------------------------- a gov with a real HISTORY -----
# Two commits, so exactly one blob per file is HEAD's and exactly one is a prior vintage. Without
# the second commit there is no DRIFT class to test and every arm below would be vacuous.
GOV=$(mktemp -d)
(
  cd "$GOV" && git init -q . && git config user.email t@t && git config user.name t
  mkdir -p ${PFX}kit
  printf 'v1 engine\n' > ${PFX}kit/engine.sh
  printf 'stable\n'    > ${PFX}kit/stable.sh
  git add -A && git commit -q -m v1 --no-verify
  printf 'v2 engine\n' > ${PFX}kit/engine.sh
  git add -A && git commit -q -m v2 --no-verify
) >/dev/null 2>&1

mkadopter() { # $1 = dir; builds a tree with one file of each class
  mkdir -p "$1/.governance" "$1/scripts"
  printf 'stable\n'     > "$1/scripts/stable.sh"   # == gov HEAD          -> IN-SYNC
  printf 'v1 engine\n'  > "$1/scripts/engine.sh"   # == gov's FIRST commit -> DRIFT
  printf 'local only\n' > "$1/scripts/mine.sh"     # in no gov commit ever -> FORK
  cat > "$1/.governance/install.json" <<JSON
{"schema":3,"gov_commit":"none","prefix":"scripts","kits":["kit"],"files":[
 {"path":"scripts/stable.sh","role":"engine","kit":"kit","source":"${PFX}kit/stable.sh"},
 {"path":"scripts/engine.sh","role":"engine","kit":"kit","source":"${PFX}kit/engine.sh"},
 {"path":"scripts/mine.sh","role":"engine","kit":"kit","source":"${PFX}kit/mine.sh"}]}
JSON
  ( cd "$1" && git init -q . && git config user.email t@t && git config user.name t \
      && git add -A && git commit -q -m a --no-verify ) >/dev/null 2>&1
}

# ---- ARM 1: the three classes are actually DISTINGUISHED ----------------------------------------
# The whole thesis of this census is that DRIFT and FORK are different questions. If a stale copy
# and a novel file landed in one bucket the tool would be a HEAD-diff wearing a costume, and every
# number this build rests on would be inflated by every stale copy in every adopter.
A1=$(mktemp -d); mkadopter "$A1"
out=$("$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" 2>&1)
has "$out" "IN-SYNC: 1" && ok "the HEAD-identical file is IN-SYNC" \
                        || bad "IN-SYNC not 1: $(printf '%s' "$out" | head -12)"
has "$out" "DRIFT: 1"   && ok "the file matching gov's FIRST commit is DRIFT, not a fork" \
                        || bad "DRIFT not 1: $(printf '%s' "$out" | head -12)"
has "$out" "FORK: 1"    && ok "the file in no gov commit ever is a FORK" \
                        || bad "FORK not 1: $(printf '%s' "$out" | head -12)"
has "$out" 'scripts/mine.sh' && ok "the fork is NAMED, not just counted" \
                             || bad "the fork was counted but not named"

# ---- ARM 2: AC4, the vacuity refusal, with its FAILING CASE OBSERVED ----------------------------
# Staged deliberately: an adopter whose receipt maps nothing. A census that printed "0 forks" here
# would be indistinguishable from a clean tree, which is the exact defect class this build keeps
# finding. The refusal must be LOUD and the exit code must not be 0.
A2=$(mktemp -d)
mkdir -p "$A2/.governance"
printf '{"schema":3,"prefix":"scripts","kits":[],"files":[]}\n' > "$A2/.governance/install.json"
( cd "$A2" && git init -q . && git config user.email t@t && git config user.name t \
    && git add -A && git commit -q -m e --no-verify ) >/dev/null 2>&1
out=$("$PY" "$CENSUS" --adopter "$A2" --name t --gov "$GOV" 2>&1); rc=$?
[ "$rc" -ne 0 ] && ok "a census mapping ZERO files exits non-zero (got $rc)" \
                || bad "a zero-map census exited 0 — it reported a clean tree it never measured"
has "$out" "REFUSED" && ok "and says REFUSED in as many words" \
                     || bad "no REFUSED in: $out"
has "$out" "cannot report a clean tree" && ok "and says why a zero map is not a clean result" \
                                        || bad "the refusal does not explain itself"

# ---- ARM 3: the refusal is NOT vacuous ---------------------------------------------------------
# ARM 2 alone would pass if the tool refused ALWAYS. This is the negative half, and without it
# ARM 2 proves only that the program can print a word.
out=$("$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" 2>&1); rc=$?
[ "$rc" -eq 0 ] && ok "a census that DOES map files runs to completion" \
                || bad "the tool refuses even a good tree (rc=$rc)"
has "$out" "REFUSED" && bad "a populated census still printed REFUSED" \
                     || ok "and does not print REFUSED"

# ---- ARM 4: an ABSENT file is its own class, never a fork --------------------------------------
# A receipt row whose file was deleted has NO blob to test. Calling that "in no gov commit ever"
# is true and useless: it would put every deleted file in the retirement programme.
A4=$(mktemp -d); mkadopter "$A4"; rm -f "$A4/scripts/mine.sh"
out=$("$PY" "$CENSUS" --adopter "$A4" --name t --gov "$GOV" 2>&1)
has "$out" "ABSENT: 1" && ok "a declared-but-deleted file is ABSENT, not a fork" \
                       || bad "deleted file misclassified: $(printf '%s' "$out" | head -12)"

# ---- ARM 5: the census is READ-ONLY in both trees -----------------------------------------------
# It reads repositories gov does not own. A tool that writes to a foreign tree while measuring it
# would be uninvitable, and nothing else here would catch a stray write.
before_gov=$(cd "$GOV" && git status --porcelain | wc -l)
before_ad=$(cd "$A1" && git status --porcelain | wc -l)
"$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" >/dev/null 2>&1
after_gov=$(cd "$GOV" && git status --porcelain | wc -l)
after_ad=$(cd "$A1" && git status --porcelain | wc -l)
[ "$before_gov" = "$after_gov" ] && [ "$before_ad" = "$after_ad" ] \
  && ok "neither tree changed: the census only reads" \
  || bad "the census dirtied a tree (gov $before_gov->$after_gov, adopter $before_ad->$after_ad)"

# ---- ARM 6: a DRIFT row is not silently promoted when gov's HEAD moves --------------------------
# The regression this guards: re-testing against HEAD only. Move gov forward again; the adopter's
# v1 file must STILL be DRIFT, because v1 is still in the history even though HEAD has left it.
( cd "$GOV" && printf 'v3 engine\n' > ${PFX}kit/engine.sh && git add -A \
    && git commit -q -m v3 --no-verify ) >/dev/null 2>&1
out=$("$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" 2>&1)
has "$out" "DRIFT: 1" && ok "a vintage stays DRIFT after gov's HEAD moves past it again" \
                      || bad "moving HEAD reclassified a vintage: $(printf '%s' "$out" | head -12)"

rm -rf "$GOV" "$A1" "$A2" "$A4"
echo "census.test.sh: $n arms, $([ $st -eq 0 ] && echo PASS || echo FAIL)"
exit $st
