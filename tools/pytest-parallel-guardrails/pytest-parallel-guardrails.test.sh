#!/usr/bin/env bash
# pytest-parallel-guardrails.test.sh — kit self-test (TOOL-bTamedTempest-1, AC1).
# Static + import-level checks only: needs a bare stdlib Python, NOT pytest/aiosqlite.
#   Exit 0 = all checks pass · 1 = a check failed · 2 = environment missing.
set -u
KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to <prefix>/lib/resolve-python.sh
# and <prefix>/lib/resolve-python.test.sh reds if any copy drifts.
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
PYBIN=$(resolve_python) || { echo "pytest-parallel-guardrails.test: no usable python"; exit 2; }
command -v "$PYBIN" >/dev/null 2>&1 || { echo "SKIP: no python available"; exit 2; }
fails=0
fail() { echo "FAIL: $1"; fails=$((fails+1)); }

# 1. Inventory — every shipped file present.
for f in README.md pyproject-snippet.toml crashprobe.py aiosqlite-seam-conftest.py \
         aiosqlite_worker_resilience.test-template.py; do
  [ -f "$KIT_DIR/$f" ] || fail "missing kit file: $f"
done

# 2. py_compile every shipped .py (syntax; the seam snippet and template import third-party
#    modules, so compile is the deepest bare-stdlib check for them).
for f in crashprobe.py aiosqlite-seam-conftest.py aiosqlite_worker_resilience.test-template.py; do
  "$PYBIN" -m py_compile "$KIT_DIR/$f" 2>/dev/null || fail "py_compile: $f"
done

# 3. Import-EXECUTE crashprobe.py under bare stdlib (its pytest import is guarded): the probe
#    must arm and create its per-worker log. Catches broken stdlib imports, the Windows/POSIX
#    platform split at import, and log-creation regressions — on the gate's platform.
tmpd="$(mktemp -d)"
# A Windows python cannot resolve MSYS-form paths (/c/..., /tmp/...) — hand it native-form paths
# (cygpath -m); on real POSIX cygpath is absent and the identity fallback applies.
py_kit="$(cygpath -m "$KIT_DIR" 2>/dev/null || echo "$KIT_DIR")"
py_tmp="$(cygpath -m "$tmpd" 2>/dev/null || echo "$tmpd")"
if CRASHPROBE_DIR="$py_tmp" "$PYBIN" -c "
import sys; sys.path.insert(0, r'$py_kit')
import crashprobe
assert crashprobe.KIT_PYTEST_GUARDRAILS_VERSION
"; then
  ls "$tmpd"/probe-*.log >/dev/null 2>&1 || fail "crashprobe import did not create its probe log"
else
  fail "crashprobe.py failed to import under bare stdlib"
fi
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fails:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fails:-0}" = 0 ] && exit 0; exit 1; fi
rm -rf "$tmpd"

# 4. Version constant well-formed + every gov:kit marker agrees with it (deployer convention:
#    the probe is removable, so the KEPT artifacts carry the version markers).
ver="$(tr -d '\r' < "$KIT_DIR/crashprobe.py" | grep -oE '^KIT_PYTEST_GUARDRAILS_VERSION = "[0-9]+\.[0-9]+"' | grep -oE '[0-9]+\.[0-9]+')"
[ -n "$ver" ] || fail "KIT_PYTEST_GUARDRAILS_VERSION missing/malformed in crashprobe.py"
if [ -n "$ver" ]; then
  for f in README.md pyproject-snippet.toml aiosqlite-seam-conftest.py \
           aiosqlite_worker_resilience.test-template.py; do
    m="$(tr -d '\r' < "$KIT_DIR/$f" | grep -oE 'gov:kit pytest-parallel-guardrails@[0-9]+\.[0-9]+' | head -1)"
    [ -n "$m" ] || { fail "gov:kit marker missing in $f"; continue; }
    [ "${m##*@}" = "$ver" ] || fail "gov:kit marker in $f is ${m##*@}, constant is $ver"
  done
fi

# 5. The four knobs present in the snippet, and faulthandler_timeout < timeout numerically.
#    CR-stripped first so a CRLF (text=auto) Windows checkout can't produce '300\r' operands.
snip="$(tr -d '\r' < "$KIT_DIR/pyproject-snippet.toml")"
for knob in 'timeout = ' 'timeout_method = "thread"' 'session_timeout = ' \
            'max-worker-restart=0' 'faulthandler_timeout = '; do
  printf '%s' "$snip" | grep -qF "$knob" || fail "snippet missing knob: $knob"
done
t="$(printf '%s' "$snip" | grep -oE '^timeout = [0-9]+' | grep -oE '[0-9]+')"
fh="$(printf '%s' "$snip" | grep -oE '^faulthandler_timeout = [0-9]+' | grep -oE '[0-9]+')"
if [ -n "$t" ] && [ -n "$fh" ]; then
  [ "$fh" -lt "$t" ] || fail "faulthandler_timeout ($fh) must be < timeout ($t)"
else
  fail "could not extract timeout/faulthandler_timeout numerically from the snippet"
fi

# 6. The test template must NOT match pytest's default python_files glob (collection hazard).
case "$(basename "$KIT_DIR/aiosqlite_worker_resilience.test-template.py")" in
  test_*.py|*_test.py) fail "test template filename matches pytest's default collection glob" ;;
esac

if [ "$fails" -gt 0 ]; then echo "pytest-parallel-guardrails self-test: $fails failure(s)"; exit 1; fi
echo "pytest-parallel-guardrails self-test: OK"
