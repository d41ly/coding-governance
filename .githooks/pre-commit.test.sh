#!/usr/bin/env bash
# Runnable check for the .githooks/pre-commit BRANCH GUARD (playbook §3 enforcement).
# Spins a throwaway repo, wires this repo's pre-commit via core.hooksPath, and asserts:
#   1) a commit ON the default branch is allowed
#   2) a commit parked OFF the default branch in the primary tree is refused
#   3) --no-verify overrides the refusal
# The throwaway repo has none of the gate-leg scripts (tools/…, skills/…), so those legs
# self-skip and only the guard is exercised. Run: bash .githooks/pre-commit.test.sh  (exit 0 = pass)
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
mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit
git config core.hooksPath hk
export GOV_DEFAULT_BRANCH=main   # throwaway has no origin/HEAD — pin the default explicitly

echo a > a; git add a; git commit -q -m first; ck "commit on default branch allowed" $? 0

git checkout -q -b feature/x
echo b > b; git add b; git commit -q -m second 2>/dev/null; ck "commit off default branch refused" $? 1

git commit -q --no-verify -m second; ck "--no-verify overrides the guard" $? 0

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
