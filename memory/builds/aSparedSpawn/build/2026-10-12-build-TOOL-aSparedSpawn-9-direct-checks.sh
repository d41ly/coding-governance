#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-9
# TOOL-aSparedSpawn-9 - the pass's direct checks of the environment identity, the template-less init
# and newrepo's copy, over HAND-BUILT repositories in a scratch root, plus two reads of the converted
# suites. No suite runs and no slice of one: AC4's suite observation, AC5 and AC7 are owed at VERIFYING.
#
#   bash <this> <scratch-root>     # run from the repository root; prints one PASS/FAIL line per check
#
# What this does NOT check: that any converted suite still passes, or that its arm inventory and its
# git exec count moved as AC5 and AC7 require. Those need the suites themselves.
set -u
S=${1:?a scratch root}; mkdir -p "$S" || exit 2
bad=0
ok() { echo "PASS $1"; }
nope() { echo "FAIL $1"; bad=1; }
SUITES="tools/run-gates/run-gates.test.sh tools/run-gates/run-gates.evidence.test.sh
tools/run-gates/run-gates.turnstile.test.sh .githooks/pre-push.test.sh tools/push-main.test.sh
.githooks/pre-push.runlog.test.sh .githooks/pre-commit.test.sh tools/memory-tree/check-memory-hygiene.test.sh
tools/memory-tree/gen_build_index.py tools/memory-tree/corpus_ids.py tools/memory-tree/gotchas.py
tools/memory-tree/row_grammar.py tools/memory-tree/migrate_backlog.py tools/memory-tree/check-arms.py
tools/drift-audit/selftest.py tools/check-wiring.test.sh tools/lexicon/selftest.py
tools/memory-tree/check-verdict-epoch.test.sh"

# AC1 - the exported triple outranks a global autocrlf=true and lands nothing in .git/config.
mkdir -p "$S/home"; printf '[core]\n\tautocrlf = true\n' > "$S/home/.gitconfig"
rm -rf "$S/ac1"
got=$( export HOME="$S/home" GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
       git init -q --template= "$S/ac1" && git -C "$S/ac1" config --get core.autocrlf )
loc=$( HOME="$S/home" git -C "$S/ac1" config --local --get core.autocrlf; echo "rc=$?" )
ctl=$( HOME="$S/home" git -C "$S/ac1" config --get core.autocrlf )
[ "$got" = false ] && [ "$loc" = "rc=1" ] && [ "$ctl" = true ] \
  && ok "AC1 env false over a global true ($got), nothing local ($loc), control without env reads $ctl" \
  || nope "AC1 got '$got', local '$loc', control '$ctl'"

# AC3 - a template-less init writes no sample hook; the control init writes them.
rm -rf "$S/ac3" "$S/ac3c"; git init -q --template= "$S/ac3"; git init -q "$S/ac3c"
n=$(find "$S/ac3/.git" -name '*.sample' | wc -l); c=$(find "$S/ac3c/.git" -name '*.sample' | wc -l)
[ "$n" -eq 0 ] && [ "$c" -gt 0 ] && ok "AC3 --template= writes $n sample hooks, the default init $c" \
  || nope "AC3 --template= wrote $n sample hooks, the default init $c"
# ...and every fixture init in the converted suites spells it, but the two GIT_DIR reproductions.
miss=$(grep -nE 'git( -C [^ ]+)? init|"init", "-q"|_git\("init"' $SUITES | grep -v -- '--template=' \
       | grep -vE '^[^:]+:[0-9]+:\s*#|GIT_DIR=|`git init`' || true)
[ -z "$miss" ] && ok "AC3 every fixture init in the converted suites passes --template=" \
  || nope "AC3 inits without --template=: $miss"

# AC2 - no per-fixture identity or autocrlf write is left in the converted suites.
hits=$(grep -nE 'config (user\.(email|name)|core\.autocrlf)|"config", "(user\.(email|name)|core\.autocrlf)"' $SUITES || true)
[ -z "$hits" ] && ok "AC2 no identity or autocrlf config write remains" || nope "AC2 remaining: $hits"

# AC6 - no converted suite runs status, diff or add against its host tree.
host=$(grep -nE '(git -C "?\$\{?(ROOT|REPO|SRC|ROOT_ABS)\}?"?|cd "?\$\{?(ROOT|REPO|SRC|ROOT_ABS)\}?"? *(&&|;)[^)]*git) (status|diff|add)' $SUITES || true)
[ -z "$host" ] && ok "AC6 no host-tree status, diff or add in a suite carrying the triple" \
  || nope "AC6 host-tree hashing call: $host"

# AC4, the mechanism only - a seed built once and copied twice: one HEAD, unshared .git, a commit in
# the first copy absent from the second. The suite's own observation is owed at VERIFYING.
rm -rf "$S/seed" "$S/c1" "$S/c2"; mkdir -p "$S/seed" "$S/c1" "$S/c2"
( export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@e GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@e
  cd "$S/seed" && git init -q --template= -b main && mkdir .githooks \
  && printf '#!/bin/sh\nexit 0\n' > .githooks/pre-commit && git add --chmod=+x .githooks/pre-commit \
  && git commit -q -m init ) || nope "AC4 seed build failed"
cp -a "$S/seed/." "$S/c1/" && cp -a "$S/seed/." "$S/c2/"
h1=$(git -C "$S/c1" rev-parse HEAD); h2=$(git -C "$S/c2" rev-parse HEAD)
( export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@e GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@e
  git -C "$S/c1" commit -q --allow-empty -m arm-one )
a1=$(git -C "$S/c1" rev-parse HEAD); a2=$(git -C "$S/c2" rev-parse HEAD)
mode=$(git -C "$S/c2" ls-files -s .githooks/pre-commit | cut -c1-6)
[ "$h1" = "$h2" ] && [ "$a1" != "$h1" ] && [ "$a2" = "$h2" ] && [ "$mode" = 100755 ] \
  && ! [ "$S/c1/.git" -ef "$S/c2/.git" ] \
  && ok "AC4 mechanism: one HEAD ${h1:0:8}, the first copy's commit absent from the second, mode $mode" \
  || nope "AC4 mechanism: h1=$h1 h2=$h2 a1=$a1 a2=$a2 mode=$mode"
exit "$bad"
