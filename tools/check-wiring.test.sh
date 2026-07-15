#!/usr/bin/env bash
# Runnable check for tools/check-wiring.sh. Spins throwaway repos and asserts the wired/unwired
# detection, the never-clobber auto-fix, and the always-exit-0 --session mode. Run: bash tools/check-wiring.test.sh
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"      # safe dir to return to before any rm -rf
SCRIPT="$HERE/check-wiring.sh"
SMERGE="$HERE/settings-merge.py"
pass=0; fail=0
ck() { if [ "$2" = 1 ]; then echo "ok   $1"; pass=$((pass+1)); else echo "FAIL $1"; fail=$((fail+1)); fi; }

D=""; OOT=""
newrepo() {   # cd (in THIS shell) into a fresh repo with a tracked .githooks/pre-commit
  D=$(mktemp -d); cd "$D" || exit 2
  git init -q -b main; git config core.autocrlf false; git config user.email t@e; git config user.name t
  mkdir .githooks; printf '#!/bin/sh\nexit 0\n' > .githooks/pre-commit; chmod +x .githooks/pre-commit
  git add -A; git commit -q -m init
}
cleanup() { cd "$REPO"; [ -n "$D" ] && rm -rf "$D"; [ -n "$OOT" ] && rm -rf "$OOT"; D=""; OOT=""; }
chk() { bash "$SCRIPT" "$@" 2>/dev/null; }   # run the checker, drop stderr noise

# AC1 — unset core.hooksPath -> UNWIRED + exit 1
newrepo
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  hooks'; } && ck "AC1 unset -> UNWIRED, exit 1" 1 || ck "AC1 unset -> UNWIRED, exit 1" 0
# AC2 — --fix sets it, re-check exits 0
chk --fix >/dev/null; got=$(git config core.hooksPath); chk --check >/dev/null; rc=$?
{ [ "$got" = ".githooks" ] && [ "$rc" = 0 ]; } && ck "AC2 --fix wires, re-check exit 0" 1 || ck "AC2 --fix wires, re-check exit 0" 0
cleanup

# AC3 — valid out-of-tree hooksPath -> WIRED, --fix never clobbers
newrepo
OOT=$(mktemp -d); printf '#!/bin/sh\nexit 0\n' > "$OOT/pre-commit"; chmod +x "$OOT/pre-commit"
git config core.hooksPath "$OOT"
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       hooks'; } && ck "AC3 out-of-tree -> WIRED" 1 || ck "AC3 out-of-tree -> WIRED" 0
# never-clobber: git may re-spell the path (MSYS /tmp -> C:/Temp), so compare git's OWN value
# before vs after --fix, and assert it was NOT reset to the .githooks fix target.
before=$(git config core.hooksPath); chk --fix >/dev/null; after=$(git config core.hooksPath)
{ [ "$after" = "$before" ] && [ "$after" != ".githooks" ]; } && ck "AC3 --fix never clobbers a set value" 1 || ck "AC3 --fix never clobbers a set value" 0
cleanup

# AC4 — non-literal ./.githooks -> WIRED
newrepo; git config core.hooksPath ./.githooks
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       hooks'; } && ck "AC4 ./.githooks -> WIRED" 1 || ck "AC4 ./.githooks -> WIRED" 0
cleanup

# AC5a — all wired -> exit 0
newrepo; git config core.hooksPath .githooks; chk --check >/dev/null; [ "$?" = 0 ] && ck "AC5 all wired -> exit 0" 1 || ck "AC5 all wired -> exit 0" 0
cleanup
# AC5b — non-git dir -> exit 0
D=$(mktemp -d); cd "$D"; chk --check >/dev/null; [ "$?" = 0 ] && ck "AC5 non-git -> exit 0" 1 || ck "AC5 non-git -> exit 0" 0
cleanup
# AC5c — repo without .githooks -> skip, exit 0
D=$(mktemp -d); cd "$D"; git init -q -b main; git config user.email t@e; git config user.name t; git commit -q --allow-empty -m init
chk --check >/dev/null; [ "$?" = 0 ] && ck "AC5 no .githooks -> skip, exit 0" 1 || ck "AC5 no .githooks -> skip, exit 0" 0
cleanup

# AC6 — --session auto-wires unset AND exits 0
newrepo
chk --session >/dev/null; rc=$?; got=$(git config core.hooksPath)
{ [ "$rc" = 0 ] && [ "$got" = ".githooks" ]; } && ck "AC6 --session wires + exit 0" 1 || ck "AC6 --session wires + exit 0" 0
cleanup

# AC7 — agent-cap adopted but unwired -> --check UNWIRED (exit 1); --session still exits 0
if [ -f "$SMERGE" ]; then
  newrepo; mkdir -p tools .claude/hooks; cp "$SMERGE" tools/settings-merge.py; printf '// stub\n' > .claude/hooks/agent-cap.js
  git config core.hooksPath .githooks     # isolate: hooks wired, so only agent-cap can be unwired
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  agent-cap'; } && ck "AC7 agent-cap unwired -> UNWIRED, exit 1" 1 || ck "AC7 agent-cap unwired -> UNWIRED, exit 1" 0
  chk --session >/dev/null; [ "$?" = 0 ] && ck "AC6 --session exit 0 despite agent-cap unwired" 1 || ck "AC6 --session exit 0 despite agent-cap unwired" 0
  cleanup
else
  echo "skip agent-cap cases — settings-merge.py not found next to script"
fi

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
