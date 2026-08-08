#!/usr/bin/env bash
# Self-test for the one python-launcher resolver. Three things, because the resolver is only as good
# as the weakest of them:
#   1. BEHAVIOUR — against a fake stub that answers `command -v` and exits 9009, which is the exact
#      Microsoft Store defect this unit exists for. A fixture that used a merely-absent launcher
#      would pass against the OLD code too.
#   2. PARITY — every INLINE copy is byte-identical to the canonical block. Copy-installed kits
#      cannot source `../lib/`, so copies exist by design; drift between them is what a gate is for.
#   3. THE BAN — the retired `command -v python3 || python` idiom cannot come back in any tracked
#      `*.sh`, and the population is derived by scanning, not by listing.
#   bash tools/lib/resolve-python.test.sh    # "PASS (…)" + exit 0 = good
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT=$(cd "$HERE/../.." && pwd)
CANON="$HERE/resolve-python.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
st=0; n=0
ok()  { n=$((n+1)); }
bad() { echo "FAIL $1"; st=1; n=$((n+1)); }

# ---- 1. BEHAVIOUR -------------------------------------------------------------------------------
# A real python, found by the resolver itself before any fixture PATH is in play. If this repo has
# no python at all the whole bar is already dead, so an unresolvable launcher here is a hard error
# rather than a skip that reports success.
# shellcheck source=/dev/null
. "$CANON"
REALPY=$(resolve_python) || { echo "FAIL no python on this host at all — the arms below cannot run"; exit 2; }
REALPY_ABS=$(command -v "$REALPY")

mkfake() { # $1=dir $2=name $3=exit-code — a launcher that EXISTS, answers `command -v`, and cannot run
  mkdir -p "$1"
  printf '#!/usr/bin/env bash\nexit %s\n' "$3" > "$1/$2"
  chmod +x "$1/$2"
  # Windows resolves .exe/.cmd before an extensionless file on PATH; git-bash runs the extensionless
  # one, which is what this fixture needs, so no .exe twin is written.
}

# (a) the stub SHADOWS the real python3 — PREPENDED to the live PATH, never replacing it. A PATH cut
# down to the fixture dirs takes bash and every coreutil with it, and the arm then fails for a reason
# that has nothing to do with the resolver.
B="$TMP/stub"; mkfake "$B" python3 9009
got=$(PATH="$B:$PATH" bash -c '. "$1"; resolve_python' _ "$CANON" 2>/dev/null)
{ [ -n "$got" ] && [ "$got" != python3 ]; } || bad "a 9009 stub first on PATH was accepted (got '$got')"; ok
PATH="$B:$PATH" "${got:-false}" -c 'import sys' >/dev/null 2>&1 || bad "the resolver returned '$got', which does not run"; ok
# ...and the same PATH under the OLD idiom picks the stub — the arm is only meaningful because the
# defect reproduces. Without this the green half above could be passing for an unrelated reason.
oldpick=$(PATH="$B:$PATH" bash -c 'p=python3; command -v python3 >/dev/null 2>&1 || p=python; echo "$p"')
[ "$oldpick" = python3 ] || bad "the retired idiom did NOT pick the stub — the fixture does not reproduce the defect"; ok
PATH="$B:$PATH" python3 -c 'import sys' >/dev/null 2>&1 \
  && { bad "the fake stub actually ran — it is not standing in for a stub"; }; ok

# (b) nothing on PATH runs: all three launcher names shadowed by stubs.
C="$TMP/allbad"; mkfake "$C" python3 9009; mkfake "$C" python 9009; mkfake "$C" py 9009
out=$(PATH="$C:$PATH" bash -c '. "$1"; resolve_python' _ "$CANON" 2>&1); rc=$?
[ "$rc" != 0 ] || bad "an all-broken PATH still returned 0"; ok
grep -qF 'no usable python launcher' <<<"$out" || bad "the all-broken failure does not name itself"; ok
grep -qF 'tried: python3 python py' <<<"$out" || bad "the failure does not list the candidates it tried"; ok

# (c) GOV_PYTHON, both states. An override that is set and unusable must be a NAMED failure — the
# operator believes they chose, and a silent fall-through hides that they did not.
got=$(PATH="$B:$PATH" GOV_PYTHON="$REALPY_ABS" bash -c '. "$1"; resolve_python' _ "$CANON" 2>/dev/null)
[ "$got" = "$REALPY_ABS" ] || bad "a working GOV_PYTHON was not used (got '$got')"; ok
out=$(PATH="$C:$PATH" GOV_PYTHON="$C/python3" bash -c '. "$1"; resolve_python' _ "$CANON" 2>&1); rc=$?
[ "$rc" != 0 ] || bad "an unusable GOV_PYTHON fell through to a 0 exit"; ok
grep -qF "GOV_PYTHON is set to '$C/python3' and did not run" <<<"$out" \
  || bad "an unusable GOV_PYTHON was not NAMED in the failure"; ok

# (d) the caller's own published override goes first and is named on failure.
got=$(PATH="$B:$PATH" bash -c '. "$1"; resolve_python "$2"' _ "$CANON" "$REALPY_ABS" 2>/dev/null)
[ "$got" = "$REALPY_ABS" ] || bad "a working caller override was not used first (got '$got')"; ok
out=$(PATH="$C:$PATH" bash -c '. "$1"; resolve_python "$2"' _ "$CANON" "$C/py" 2>&1)
grep -qF "the caller's override '$C/py' was tried FIRST and did not run" <<<"$out" \
  || bad "an unusable caller override was not named"; ok

# (e) echo-and-return, not exit. Six of the seven consumers run `set -u` WITHOUT `set -e`, so a
# resolver that only `return 1`s cannot halt them — the caller has to be able to test a substitution.
out=$(PATH="$C:$PATH" bash -c 'set -u; . "$1"; PY=$(resolve_python) || { echo HALTED; exit 3; }; echo "NOTHALTED $PY"' _ "$CANON" 2>/dev/null); rc=$?
[ "$out" = HALTED ] && [ "$rc" = 3 ] || bad "the caller could not halt on failure (out='$out' rc=$rc)"; ok

# ---- 2. PARITY ----------------------------------------------------------------------------------
# The canonical block, and every tracked file that carries a copy of it.
blk() { awk '/^# >>> resolve_python/{f=1} f{print} /^# <<< resolve_python/{if(f)exit}' "$1"; }
want=$(blk "$CANON")
[ -n "$want" ] || bad "the canonical resolver has no marked block"; ok
copies=$(cd "$ROOT" && git grep -l '^# >>> resolve_python' -- '*.sh' | grep -v '^tools/lib/resolve-python' || true)
[ -n "$copies" ] || bad "no inline copy found — the parity arm would be judging an empty population"; ok
while IFS= read -r rel; do
  [ -n "$rel" ] || continue
  if [ "$(blk "$ROOT/$rel")" != "$want" ]; then
    bad "inline copy drifted from tools/lib/resolve-python.sh: $rel"
  fi
  ok
done <<<"$copies"

# ---- 3. THE BAN ---------------------------------------------------------------------------------
# The retired idiom, in any tracked `*.sh`. Comments are stripped first: this file and the resolver
# both EXPLAIN the idiom they replace, and a predicate that fires on the prose documenting the fix is
# the self-inflicted red this repo has a catalogue record about.
banned=$(cd "$ROOT" && git grep -nE 'command -v (python3|python|py)\b' -- '*.sh' \
  | grep -v '^tools/lib/resolve-python' \
  | awk -F: '{ line=$0; sub(/^[^:]*:[0-9]+:/, "", line); if (line !~ /^[[:space:]]*#/) print }' || true)
[ -z "$banned" ] || { echo "FAIL the retired python-launcher idiom is back:"; printf '%s\n' "$banned" | sed 's/^/    /'; st=1; }
ok
# ...and the ban's own population is non-empty, or it is a gate over nothing.
nsh=$(cd "$ROOT" && git ls-files -- '*.sh' | grep -c . || true)
[ "$nsh" -gt 10 ] || bad "the ban scanned $nsh shell files — the population collapsed"; ok
# ...and it FIRES on a planted line, so "clean" means "looked and found nothing".
plant="$TMP/plant.sh"; printf '#!/usr/bin/env bash\ncommand -v python3 >/dev/null 2>&1 || PY=python\n' > "$plant"
grep -qE 'command -v (python3|python|py)\b' "$plant" || bad "the ban predicate does not match the idiom it bans"; ok
printf '#!/usr/bin/env bash\n# command -v python3 is the retired idiom\n' > "$plant"
awk '$0 !~ /^[[:space:]]*#/' "$plant" | grep -qE 'command -v (python3|python|py)\b' \
  && bad "the ban fires on a COMMENT explaining the idiom"; ok

[ "$st" = 0 ] && echo "PASS — resolve-python: $n assertions held"
exit "$st"
