#!/usr/bin/env bash
# Runnable check for the .githooks/pre-commit BRANCH GUARD (playbook §3 enforcement).
# Spins a throwaway repo, wires this repo's pre-commit via core.hooksPath, and asserts:
#   1) a commit ON the default branch is allowed
#   2) a commit parked OFF the default branch in the primary tree is refused
#   3) --no-verify overrides the refusal
# The throwaway repo has none of the gate-leg scripts (tools/…, skills/…), so those legs
# self-skip and only the guard is exercised — except the codebase-map leg, whose arms follow the
# guard's and plant a stand-in gate. Run: bash .githooks/pre-commit.test.sh  (exit 0 = pass)
set -u
HOOK="$(cd "$(dirname "$0")" && pwd)/pre-commit"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
pass=0; fail=0
ck() { # name  actual_exit  expected_pass(0)/fail(1)
  local ok; if [ "$3" = 0 ]; then [ "$2" = 0 ] && ok=1 || ok=0; else [ "$2" != 0 ] && ok=1 || ok=0; fi
  if [ "$ok" = 1 ]; then echo "ok   $1 (exit $2)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $2)"; fail=$((fail+1)); fi
}

cd "$tmp" || exit 2
git init -q -b main
git config user.email t@example.com; git config user.name test
git config core.autocrlf false   # hermetic: a global autocrlf=true otherwise reaches this repo
mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit
git config core.hooksPath hk
export GOV_DEFAULT_BRANCH=main   # throwaway has no origin/HEAD — pin the default explicitly

echo a > a; git add a; git commit -q -m first; ck "commit on default branch allowed" $? 0

git checkout -q -b feature/x
echo b > b; git add b; git commit -q -m second 2>/dev/null; ck "commit off default branch refused" $? 1

git commit -q --no-verify -m second; ck "--no-verify overrides the guard" $? 0

# ---- the codebase-map leg ------------------------------------------------------------------------
# A stand-in gate at the leg's own path, red while a flag file exists. The hook consumes only the
# gate's exit status and output, so that is the whole contract the stand-in holds; the REAL gate was
# observed red on a staged break when the leg landed. These arms keep the trigger, the remedy and the
# unstaged-artifact refusal from regressing. The resolver is this repo's own, because the leg sources it.
git checkout -q main
mkdir -p tools/codebase-map tools/lib map/generated
cp "${HOOK%/*}/../tools/lib/resolve-python.sh" tools/lib/
cat > tools/codebase-map/test_codebase_map.py <<'EOF'
import os, sys
if os.path.exists("gate-red"):
    print("FAIL test_generated_artifacts_are_fresh")
    print("STALE symbols.json")
    sys.exit(1)
print("ok   test_generated_artifacts_are_fresh")
EOF
echo 'MAP_ROOT=map' > .codebase-map.conf
echo '{"v":1}' > map/generated/x.json
git add -A; git commit -q --no-verify -m map-fixture

touch gate-red
echo 'x = 1' > a.py; git add a.py
out=$(git commit -q -m a 2>&1); ck "a staged .py with a red map gate is refused" $? 1
printf '%s\n' "$out" | grep -q 'gen_map.py --write'; ck "the refusal prints the regen remedy" $? 0
git reset -q

echo 'function f() {}' > e.js; git add e.js
out=$(git commit -q -m e 2>&1); ck "a staged .js with a red map gate is refused" $? 1
printf '%s\n' "$out" | grep -q 'gen_map.py --write'; ck "the .js refusal is the map gate's" $? 0
git reset -q

echo t > b.txt; git add b.txt
git commit -q -m b >/dev/null 2>&1; ck "a commit staging no .py or .js does not run the map gate" $? 0

# Every arm below stages a file no earlier arm could have committed, so a refusal can never be
# git's "nothing to commit" — measured: reusing a.py let this arm pass with the trigger disabled.
rm gate-red
echo '{"v":2}' > map/generated/x.json; echo 'y = 2' > c.py; git add c.py
out=$(git commit -q -m c 2>&1); ck "fresh artifacts left unstaged are refused" $? 1
printf '%s\n' "$out" | grep -q 'NOT staged'; ck "the refusal names the unstaged artifacts" $? 0

git add map/generated/x.json
git commit -q -m d >/dev/null 2>&1; ck "a green map gate with its artifacts staged is allowed" $? 0

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
