#!/usr/bin/env bash
# adopt-run-gates.test.sh — the run-gates adopter, gated on EFFECTS. the run-gates promotion spec's S7.
#
# WHY EFFECTS AND NOT EXIT CODES. The adopter READS a target's declaration and can WRITE, so an
# exit-code-only arm certifies the verb by its own report. This repo already paid for that once: a
# Tier-2 review found 4 of 7 defects, one a blocker, in the single file no leg executed. Every arm
# below asserts a MESSAGE or an on-disk state, and the refusal arms additionally assert that nothing
# was written.
#
# AC6's CONTROL LIVES HERE. `adopt-run-gates.sh --check` in gov's own tree exits 0 reporting
# NOT ADOPTED — and so would a --check that did nothing whatever. The mutation arm is what
# distinguishes them: it edits the runner's printf out from under a real declaration and asserts the
# red. Without it the criterion is satisfied by a no-op.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "adopt-e2e: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
KITDIR=$(cd "$(dirname "$0")" && pwd)
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
ADOPT="$KITDIR/adopt-run-gates.sh"

FLOOR_ASSERTIONS=17
n=0
bad=0
ok()   { n=$((n+1)); echo "  ok   — $1"; }
nope() { n=$((n+1)); echo "  FAIL — $1"; bad=1; }

TMP=$(mktemp -d) || { echo "adopt-e2e: cannot create a scratch dir"; exit 2; }
trap 'rm -rf "$TMP"' EXIT

# A scratch TARGET carrying the kit at a DIFFERENT prefix from gov's, so nothing here can pass by
# accidentally resolving gov's own paths.
build_target() { # <name> <prefix> -> echoes the target root
  local t="$TMP/$1" pfx="$2"
  mkdir -p "$t/$pfx/run-gates" "$t/.governance"
  ( cd "$t" && git init -q . && git config user.email e@x && git config user.name t ) >/dev/null 2>&1
  cp "$KITDIR/run-gates.sh" "$t/$pfx/run-gates/run-gates.sh"
  cp "$ADOPT"               "$t/$pfx/run-gates/adopt-run-gates.sh"
  printf '[]\n' > "$t/$pfx/gate-legs.json"
  ( cd "$t" && git add -A && git commit -qm init ) >/dev/null 2>&1
  printf '%s' "$t"
}
write_decl() { # <target> <prefix> <ran-head> — writes the [gate_runner] declaration AND commits it, so a
         # later `git status --porcelain` reports what the ADOPTER wrote and not the fixture.
  cat > "$1/.governance/deploy.toml" <<TOML
prefix = "$2"
[gate_runner]
kind = "manifest"
observed_ran = ["$3{name}"]
observed_failed = ["GATE FAIL  {name}"]
TOML
  ( cd "$1" && git add -A && git commit -qm decl ) >/dev/null 2>&1
}

echo "== 1. NOT ADOPTED is a real answer, and it writes nothing =="
T=$(build_target notadopted vendor)
out=$( cd "$T" && bash vendor/run-gates/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'NOT ADOPTED' \
  && ok "no deploy.toml -> exit 0 reporting NOT ADOPTED" \
  || nope "no deploy.toml did not report NOT ADOPTED (rc=$rc): $out"
[ -z "$( cd "$T" && git status --porcelain )" ] \
  && ok "the NOT ADOPTED path left the target byte-identical" \
  || nope "the NOT ADOPTED path wrote into the target"

echo "== 2. a matching declaration agrees, at a NON-gov prefix =="
T=$(build_target agree vendor)
write_decl "$T" vendor 'GATE ok    '
out=$( cd "$T" && bash vendor/run-gates/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 0 ] && ok "a declaration matching the runner's printf exits 0" \
  || nope "a matching declaration did not exit 0 (rc=$rc): $out"
printf '%s' "$out" | grep -q 'observed_ran' \
  && ok "the agreeing report names the key it checked" \
  || nope "the agreeing report does not name observed_ran: $out"
[ -z "$( cd "$T" && git status --porcelain )" ] \
  && ok "--check wrote nothing on the agreeing path" \
  || nope "--check wrote into the target on the agreeing path"

echo "== 3. AC5 — the MUTATION arm, which is what makes arm 1 mean anything =="
T=$(build_target drift vendor)
write_decl "$T" vendor 'GATE ok    '
# Move the runner's output string out from under the declaration, exactly as a later unit editing
# the report verbs would. In-process `sed`, not a nested `python` heredoc: the heredoc form was
# measured SILENTLY FAILING on this host — the nested interpreter's fork dies with a cygwin
# signal-pipe error, the edit never lands, and the arm below then passes by finding the very string
# it was supposed to have removed. A mutation arm whose mutation does not happen is the
# fixture-passes-by-finding-nothing class sitting inside the arm written to prevent it, so the
# mutation is ASSERTED before the adopter is asked anything.
MUT="$T/vendor/run-gates/run-gates.sh"
sed -i 's/GATE ok    /GATE PASSED  /g' "$MUT"
if grep -q 'GATE PASSED  ' "$MUT" && ! grep -q 'GATE ok    ' "$MUT"; then
  ok "the fixture mutation actually landed (so the arm below is not vacuous)"
else
  nope "the fixture mutation did NOT land, so the drift arm would prove nothing"
fi
out=$( cd "$T" && bash vendor/run-gates/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 1 ] && ok "a declaration the runner no longer emits exits 1" \
  || nope "the drifted declaration did not exit 1 (rc=$rc): $out"
if printf '%s' "$out" | grep -q 'DRIFT' && printf '%s' "$out" | grep -q 'observed_ran'; then
  ok "the drift report says DRIFT and NAMES observed_ran (AC5)"
else
  nope "the drift report does not tie DRIFT to observed_ran: $out"
fi

echo "== 4. a declaration with the key ABSENT is reported, not read as agreement =="
T=$(build_target absentkey vendor)
cat > "$T/.governance/deploy.toml" <<'TOML'
prefix = "vendor"
[gate_runner]
kind = "manifest"
observed_ran = ["GATE ok    {name}"]
TOML
out=$( cd "$T" && bash vendor/run-gates/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'observed_failed' \
  && ok "a missing observed_failed is reported by name, not read as empty-equals-empty" \
  || nope "a missing observed_failed was not reported (rc=$rc): $out"

echo "== 5. it REFUSES across two trees rather than writing a prefix the target cannot resolve =="
T=$(build_target foreign vendor)
out=$( bash "$ADOPT" --check --target "$T" 2>&1 ); rc=$?
[ "$rc" = 2 ] && printf '%s' "$out" | grep -q 'REFUSING' \
  && ok "a kit outside the named target refuses with exit 2" \
  || nope "a cross-tree adopt did not refuse (rc=$rc): $out"
[ -z "$( cd "$T" && git status --porcelain )" ] \
  && ok "the refusal left the target byte-identical" \
  || nope "the refusal wrote into the target"

echo "== 6. a --target that does not exist refuses before reading anything =="
out=$( bash "$ADOPT" --check --target "$TMP/no-such-tree" 2>&1 ); rc=$?
[ "$rc" = 2 ] && ok "an absent --target exits 2" \
  || nope "an absent --target did not exit 2 (rc=$rc): $out"

echo "== 6b. a SCALAR observed_* is refused, because the deployer's reader ITERATES it =="
T=$(build_target scalarform vendor)
cat > "$T/.governance/deploy.toml" <<'TOML'
prefix = "vendor"
[gate_runner]
kind = "manifest"
observed_ran = "GATE ok    {name}"
observed_failed = "GATE FAIL  {name}"
TOML
out=$( cd "$T" && bash vendor/run-gates/adopt-run-gates.sh --check 2>&1 ); rc=$?
if [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'must be an ARRAY'; then
  ok "a scalar observed_* is refused by name (closing review D2/D1)"
else
  nope "a scalar observed_* was not refused (rc=$rc): $out"
fi
# ...and the control: the SAME heads in ARRAY form, with the SAME runner, must pass. Without this
# the arm above is satisfied by an adopter that refuses every declaration it is given.
T=$(build_target arrayform vendor)
write_decl "$T" vendor 'GATE ok    '
out=$( cd "$T" && bash vendor/run-gates/adopt-run-gates.sh --check 2>&1 ); rc=$?
[ "$rc" = 0 ] && ok "the same heads in ARRAY form still pass (the refusal is about the shape)"   || nope "the array form did not pass (rc=$rc): $out"

echo "== 6c. --help terminates and prints usage =="
out=$( timeout 10 bash "$ADOPT" --help 2>&1 ); rc=$?
[ "$rc" = 2 ] && printf '%s' "$out" | grep -q 'usage:'   && ok "--help prints usage and exits 2 rather than spinning on an undefined function"   || nope "--help did not terminate cleanly (rc=$rc): $out"

echo "== 7. the adopter derives its own prefix — no gov path is spelled in it =="
grep -qE '^\s*KITDIR=\$\(cd "\$\(dirname "\$0"\)" && pwd\)' "$ADOPT" \
  && ok "the kit dir is derived from the script's own location" \
  || nope "the adopter does not derive its kit dir"
grep -q 'tools/run-gates' "$ADOPT" \
  && nope "the adopter SPELLS a gov install prefix, which lands a dead path in an adopter's tree" \
  || ok "the adopter spells no install prefix"

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "adopt-e2e: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates adopter e2e, $n assertions)"
exit "$bad"
