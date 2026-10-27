#!/usr/bin/env bash
# adopt-codebase-map.test.sh — e2e self-test for the codebase-map ADOPTER. Exit 0 = every arm held.
#
#   bash <prefix>/codebase-map/adopt-codebase-map.test.sh
#
# WHY THIS FILE EXISTS. A Tier-2 review of the install-prefix work found 4 of 7 defects — including a
# blocker that wrote a conf, a whole map tree and a gate file into a repository the operator never
# named — in `adopt-codebase-map.sh`, the ONE changed file no gate leg executed. The Python engine
# beside it, carried by ~20 selftest arms, produced zero confirmed findings. That correlation is the
# whole argument for this leg: the adopter WRITES, and nothing was watching it.
#
# DISCIPLINES (same as the sibling gate tests):
#  * Every arm asserts the SPECIFIC message or the SPECIFIC on-disk effect, never the exit code
#    alone — a probe that reads only `$?` reports success while exercising nothing.
#  * A refusal arm asserts the WRITES DID NOT HAPPEN, not just that the script exited non-zero.
#    "It refused" and "it refused before writing" are different claims and only one is useful.
#  * `PASS` prints after the LAST arm.
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "adopt-codebase-map.test: not inside a git repository"; exit 2; }
# TOOL-aRepatriatedFork-46: this kit's own directory NAME, which every fixture below mirrors.
KIT_NAME="${KIT_REL##*/}"
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
# FPFX is the prefix the FIXTURES install the kit at: this install's first segment, empty at a root
# install. The kit refuses a prefix deeper than one segment by design (its adopter says so), so a
# fixture built at this install's whole depth graded that refusal at `vendor/gov/` (VERIFYING repair).
FPFX="${PFX%%/*}"; FPFX="${FPFX:+$FPFX/}"
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
KIT="$ROOT/${PFX}${KIT_NAME}"
fails=0
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

# The resolver, INLINE — this file SHIPS inside the kit, so `../lib/` does not exist in an adopting
# repo. Byte-identical to <prefix>/lib/resolve-python.sh; resolve-python.test.sh reds if a copy drifts.
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

PY=$(resolve_python "${MAP_PY:-}") || exit 2

note() { printf '%s\n' "$*"; }
bad()  { fails=$((fails+1)); printf 'arm FAIL  %s\n' "$*"; }
good() { printf 'arm ok    %s\n' "$*"; }

# A repo with the kit installed at $2 (a prefix relative to the repo root, may be empty) and a
# filled project layer, so the adopter can run to completion.
mkrepo() { # $1 = repo dir · $2 = prefix
  mkdir -p "$1" && git -C "$1" init -q
  git -C "$1" config user.email t@t; git -C "$1" config user.name t
  if [ -n "$2" ]; then mkdir -p "$1/$2"; _kd="$1/$2/codebase-map"; else _kd="$1/codebase-map"; fi
  cp -r "$KIT" "$_kd"
  rm -f "$_kd/adopt-codebase-map.test.sh"
  mkdir -p "$1/src"; printf 'def hello():\n    return 1\n' > "$1/src/mod.py"
  cat > "$_kd/map_extractors.py" <<'PY'
import map_lib as m

def inventory_ids():
    return ("mods",)

def all_inventories():
    return {"mods": m.module_inventory(m.repo_root() / "src", "mods")}
PY
  printf '%s\n' "$_kd"
}

# ---------------------------------------------------------------------------------------------
# arm 1 (review B1b) — run BY PATH from a DIFFERENT repo: refuse, and write into NEITHER tree.
# Before the fix this adopted the KIT's repo at exit 0 while printing relative paths that read as
# the cwd's repo, and it was a REGRESSION: the pre-1.1 `-ef` guard had refused the same invocation.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a1-kitrepo" "${FPFX%/}")
mkdir -p "$TMP/a1-target" && git -C "$TMP/a1-target" init -q
out=$(cd "$TMP/a1-target" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" = 0 ]; then bad "1 by-path-from-another-repo: exited 0 (must refuse)"
elif ! printf '%s' "$out" | grep -q "refusing"; then
  bad "1 by-path-from-another-repo: refused without saying why"; printf '%s\n' "$out" | sed 's/^/      /'
elif [ -f "$TMP/a1-kitrepo/.codebase-map.conf" ]; then
  bad "1 by-path-from-another-repo: WROTE a conf into the kit's own repo"
elif [ -f "$TMP/a1-target/.codebase-map.conf" ]; then
  bad "1 by-path-from-another-repo: wrote a conf into the target it never resolved"
else
  good "1 by-path-from-another-repo refuses, naming both roots, writing nothing"
fi
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fails:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fails:-0}" = 0 ] && exit 0; exit 1; fi

# ---------------------------------------------------------------------------------------------
# arm 2 (review M2) — a prefix deeper than one segment is refused BEFORE anything is written.
# The gate template resolves only <root>/codebase-map and <root>/<one>/codebase-map, so accepting a
# deeper install left a half-adopted repo whose failure was reported as a coverage violation.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a2" "a/b")
out=$(cd "$TMP/a2" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" = 0 ]; then bad "2 deep-prefix: exited 0 (must refuse)"
elif ! printf '%s' "$out" | grep -q "deeper than one segment"; then
  bad "2 deep-prefix: wrong message"; printf '%s\n' "$out" | sed 's/^/      /'
elif [ -f "$TMP/a2/.codebase-map.conf" ] || [ -d "$TMP/a2/memory" ]; then
  bad "2 deep-prefix: refused only AFTER writing (conf and/or map tree on disk)"
else
  good "2 deep-prefix refuses before writing anything"
fi

# ---------------------------------------------------------------------------------------------
# arm 3 (review H1 + L1) — a hostile install prefix must not corrupt the conf this script SOURCES.
# `&` is sed's whole-match and `\` starts an escape, so the sed stamp silently mangled the line and
# still exited 0; the next run sourced the wreckage and executed part of it. Each prefix is checked
# by SOURCING the conf in a clean subshell and comparing the resulting value exactly, and by
# asserting the run never claims success and failure for the same step in one breath (L1).
# ---------------------------------------------------------------------------------------------
# The load-bearing assertion is that the conf may only ever hold an INTENDED value: the exact stamp
# when the run claims one, and the example's untouched default when it declines. "It admitted it
# could not stamp" is not enough on its own — a mangled write plus an honest note would still leave
# a broken conf on disk. The last two prefixes are ordinary ones the conf grammar accepts, so the
# stamping's HAPPY path is armed too and this loop cannot pass by only ever declining.
DEFAULT_MDC='python <prefix>/codebase-map/map_diff.py'   # gov:literal-python — the conf VALUE compared against, never run: the example's pre-stamp shape
i=0
for prefix in 'R&D' 'a b' "x'y" 'ok-dir' 'ok.dir'; do
  i=$((i+1))
  KD=$(mkrepo "$TMP/a3-$i" "$prefix")
  out=$(cd "$TMP/a3-$i" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1)
  conf="$TMP/a3-$i/.codebase-map.conf"
  if [ ! -f "$conf" ]; then bad "3.$i prefix '$prefix': no conf created"; continue; fi
  got=$(cd "$TMP/a3-$i" && ( . ./.codebase-map.conf >/dev/null 2>&1; printf '%s' "${MAP_DIFF_CMD:-}" ))
  side=$(cd "$TMP/a3-$i" && . ./.codebase-map.conf 2>&1 >/dev/null)
  claim_fail=$(printf '%s' "$out" | grep -c "could NOT stamp" || true)
  claim_ok=$(printf '%s' "$out" | grep -c "MAP_DIFF_CMD stamped" || true)
  if [ -n "$side" ]; then
    bad "3.$i prefix '$prefix': sourcing the conf EXECUTED something: $side"
  elif [ "$claim_fail" != 0 ] && [ "$claim_ok" != 0 ]; then
    bad "3.$i prefix '$prefix': printed BOTH a failure note and a success claim"
  elif [ "$claim_ok" != 0 ] && [ "$got" != "python $prefix/${KIT_NAME}/map_diff.py" ]; then
    bad "3.$i prefix '$prefix': claimed a stamp but MAP_DIFF_CMD is '$got'"
  elif [ "$claim_fail" != 0 ] && [ "$got" != "$DEFAULT_MDC" ]; then
    bad "3.$i prefix '$prefix': declined the stamp but left MAP_DIFF_CMD as '$got' (a half-write)"
  elif [ "$claim_ok" = 0 ] && [ "$claim_fail" = 0 ]; then
    bad "3.$i prefix '$prefix': said nothing at all about the stamp"
  else
    good "3.$i prefix '$prefix': conf sources cleanly, and holds an intended value"
  fi
done

# ---------------------------------------------------------------------------------------------
# arm 4 (review H2) — the DOCUMENTED path: the operator copies the example conf FIRST, so the
# adopter's create-branch stamp never fires. The digest command must still resolve, because the
# scaffolded map README ships it. Before the fix that README named the kit's map_diff.py WITHOUT its
# prefix at a <prefix>/-prefixed install, and `ls` on it said No such file.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a4" "${FPFX%/}")
cp "$KD/.codebase-map.conf.example" "$TMP/a4/.codebase-map.conf"
out=$(cd "$TMP/a4" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" != 0 ]; then bad "4 documented-path: adoption failed"; printf '%s\n' "$out" | sed 's/^/      /'
else
  dead=""
  for tok in $(grep -ohE '[A-Za-z0-9_./-]+\.py' "$TMP/a4/memory/map/README.md" | grep '/' | sort -u); do
    [ -f "$TMP/a4/$tok" ] || dead="$dead $tok"
  done
  if [ -n "$dead" ]; then bad "4 documented-path: the scaffolded README names dead paths:$dead"
  elif ! grep -q "${FPFX}${KIT_NAME}/map_diff.py" "$TMP/a4/memory/map/README.md"; then
    bad "4 documented-path: the README carries no prefixed digest command (arm proves nothing)"
  else
    good "4 documented-path: every path the scaffolded README prints resolves"
  fi
fi

# ---------------------------------------------------------------------------------------------
# arm 5 (review B1a) — a SYMLINKED kit dir must anchor to the ADOPTING repo, never to the link
# target's repo. `git rev-parse --show-toplevel` answers with the physical path, which is why the
# adopter resolves its root logically instead. SKIPPED, loudly, where symlinks cannot be created
# (Windows without Developer Mode) — a silent skip would be the absence-reads-as-pass class.
# ---------------------------------------------------------------------------------------------
mkdir -p "$TMP/a5-src" && git -C "$TMP/a5-src" init -q
cp -r "$KIT" "$TMP/a5-src/${KIT_NAME}"; rm -f "$TMP/a5-src/${KIT_NAME}/adopt-codebase-map.test.sh"
mkdir -p "$TMP/a5-adopting/${FPFX}" && git -C "$TMP/a5-adopting" init -q
mkdir -p "$TMP/a5-adopting/src"; printf 'def hello():\n    return 1\n' > "$TMP/a5-adopting/src/mod.py"
cat > "$TMP/a5-src/${KIT_NAME}/map_extractors.py" <<'PY'
import map_lib as m

def inventory_ids():
    return ("mods",)

def all_inventories():
    return {"mods": m.module_inventory(m.repo_root() / "src", "mods")}
PY
# A POSIX symlink first; on Windows fall back to a directory JUNCTION, which needs no Developer
# Mode and is the exact shape the blocker was measured on (a junctioned kit dir resolving to the
# link target's repo). `git rev-parse --show-toplevel` follows both.
link_made=0
if ln -s "$TMP/a5-src/${KIT_NAME}" "$TMP/a5-adopting/${FPFX}${KIT_NAME}" 2>/dev/null &&
   [ -L "$TMP/a5-adopting/${FPFX}${KIT_NAME}" ]; then
  link_made=1
elif command -v cygpath >/dev/null 2>&1 && command -v cmd >/dev/null 2>&1; then
  rm -rf "$TMP/a5-adopting/${FPFX}${KIT_NAME}"
  cmd //c mklink //J "$(cygpath -w "$TMP/a5-adopting/${FPFX}${KIT_NAME}")" \
                     "$(cygpath -w "$TMP/a5-src/${KIT_NAME}")" >/dev/null 2>&1 || true
  [ -f "$TMP/a5-adopting/${FPFX}${KIT_NAME}/map_lib.py" ] && link_made=2
fi
if [ "$link_made" != 0 ]; then
  out=$(cd "$TMP/a5-adopting" && bash ${FPFX}${KIT_NAME}/adopt-codebase-map.sh --scaffold 2>&1); rc=$?
  if [ -f "$TMP/a5-src/.codebase-map.conf" ]; then
    bad "5 symlinked-kit: adopted the LINK TARGET's repo"
  elif [ "$rc" = 0 ] || [ -f "$TMP/a5-adopting/.codebase-map.conf" ]; then
    good "5 symlinked-kit anchors to the adopting repo"
  else
    bad "5 symlinked-kit: neither adopted nor refused clearly"; printf '%s\n' "$out" | sed 's/^/      /'
  fi
else
  note "arm SKIP  5 symlinked-kit — this host cannot create symlinks (no Developer Mode?)"
fi

# ---------------------------------------------------------------------------------------------
# arm 6 — the happy path still works end to end at a prefixed install, and the gate it leaves
# behind is LIVE: a new module reds it. A green adopter that installs a dead gate is the
# fixture-passes-by-finding-nothing class one level up.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a6" "${FPFX%/}")
# Run 1 creates + stamps the conf and exits 1 BY DESIGN ("EDIT IT, then re-run"); run 2 adopts.
(cd "$TMP/a6" && bash "$KD/adopt-codebase-map.sh" --scaffold >/dev/null 2>&1) || true
out=$(cd "$TMP/a6" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" != 0 ]; then bad "6 happy-path: adoption failed"; printf '%s\n' "$out" | sed 's/^/      /'
elif ! printf '%s' "$out" | grep -q "Adopted."; then bad "6 happy-path: no Adopted. line"
else
  printf 'def added():\n    return 2\n' > "$TMP/a6/src/newmod.py"
  gate=$(cd "$TMP/a6" && . ./.codebase-map.conf >/dev/null 2>&1; printf '%s' "${GATE_FILE:-tests/test_codebase_map.py}")
  if (cd "$TMP/a6" && "$PY" "$gate" >/dev/null 2>&1); then
    bad "6 happy-path: the installed gate stayed GREEN on an unclaimed new module"
  else
    good "6 happy-path adopts, and the gate it installs is live"
  fi
fi

[ "$fails" = 0 ] || { printf '%s arm(s) FAILED\n' "$fails"; exit 1; }
echo "PASS"
