#!/usr/bin/env bash
# pytest-parallel-guardrails.test.sh — kit self-test (TOOL-bTamedTempest-1, AC1).
# Static + import-level checks only: needs a bare stdlib Python, NOT pytest/aiosqlite.
#   Exit 0 = all checks pass · 1 = a check failed · 2 = environment missing.
set -u
KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYBIN=python3; command -v python3 >/dev/null 2>&1 || PYBIN=python
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
