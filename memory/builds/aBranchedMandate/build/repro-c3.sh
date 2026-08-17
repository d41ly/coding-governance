#!/usr/bin/env bash
# repro-c3.sh — reproduce the unattended authorization refusal for a build committed on the run's
# own branch. Companion to 2026-08-16-build-aBranchedMandate-1-worktree-refusal-reproduction.md.
#
#   bash memory/builds/aBranchedMandate/build/repro-c3.sh
#
# Exit 0 = the refusal reproduced (check 6). Exit 1 = it did NOT, which is the interesting outcome:
# either the anchor observation failed for an unrelated reason, or the rule has changed.
#
# It builds its own bare origin ADVERTISING a HEAD symref. Without that advertisement the driver
# refuses at check 27/28 instead, and a fixture that fails earlier than the rule it is testing is a
# fixture that proves nothing.
set -u

KIT=${1:-$(git rev-parse --show-toplevel)/tools/unattended}
[ -f "$KIT/unattended.sh" ] || { echo "repro: no unattended.sh under $KIT"; exit 2; }

O=$(mktemp -d); ORIGIN="$O/origin.git"
git init -q --bare "$ORIGIN"
git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main

R=$(mktemp -d); cd "$R" || exit 2
git init -q -b main .
git config user.email repro@example.invalid
git config user.name repro
cp -r "$KIT" ./unattended

cat > .unattended.conf <<'CONF'
MEMORY_ROOT=memory
LANDER="true"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
WIRING_CHECK="true"
KEEPALIVE_CREATE="X"
KEEPALIVE_DELETE="Y"
KICKOFF_ENGINE=""
KICKOFF_EXITS="6"
CORE_FLOOR="10:6"
PHASES_EXTRA=""
DOD_EXTRA=""
CONF

echo seed > seed.txt
git add -A >/dev/null && git commit -q -m seed
git remote add origin "$ORIGIN"
git push -q origin main

# The owner's flow under test: branch first, then spec and commit the build ON the branch.
git checkout -q -b unit
mkdir -p memory/builds/aTestBuild/spec
cat > memory/builds/aTestBuild/README.md <<'MD'
---
slug: aTestBuild
---
# aTestBuild

<!-- gen:build-index -->
| [X-1](spec/1.md) | OPEN |
<!-- /gen:build-index -->
MD
echo spec > memory/builds/aTestBuild/spec/1.md
git add -A >/dev/null && git commit -q -m "spec the build on the unit branch"

echo "HEAD          $(git rev-parse HEAD)"
echo "merge-base    $(git merge-base origin/main HEAD)"
out=$(bash unattended/unattended.sh --preflight aTestBuild --keepalive-id k1 2>&1)
echo "$out"

# Keyed on the SIGNATURE, not on the exit code and not on the ordinal. A non-zero exit is produced by
# every one of this verb's refusals, so asserting on it would let any unrelated refusal score as a
# successful reproduction — which is the fixture-passes-by-finding-nothing class.
case "$out" in
  *"no build README at the pinned BASE"*)
    echo "REPRODUCED — check 6 refused a build committed on the run's own branch"; exit 0 ;;
  *)
    echo "NOT REPRODUCED — the refusal above is not the authorization one; read it before assuming the rule changed"; exit 1 ;;
esac
