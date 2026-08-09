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

# AC8 — the memory-recall recall-opened arm, all SIX states in one repo. The hook is copied only
# under `adopt-memory-recall.sh --with-hook`, so an ABSENT hook file is a TRUE signal and must print
# a skip: mirroring the agent-cap arm literally would print a permanent false UNWIRED in the repo
# that runs check-wiring.sh as its own SessionStart hook. The fragment is resolved the way the arm
# itself resolves it, so this test works in both layouts (adopter: <root>/memory-recall/).
FRAG=""; for c in "$REPO/memory-recall/recall-opened.fragment.json" "$REPO/tools/memory-recall/recall-opened.fragment.json"; do
  [ -f "$c" ] && { FRAG="$c"; break; }
done
if [ -f "$SMERGE" ] && [ -n "$FRAG" ]; then
  . "$REPO/tools/lib/resolve-python.sh"
  py=$(resolve_python) || { echo "check-wiring.test: no usable python"; exit 2; }
  newrepo
  git config core.hooksPath .githooks        # isolate: hooks wired, so only the recall arm can be unwired
  mkdir -p tools memory-recall .claude/hooks; cp "$SMERGE" tools/settings-merge.py

  # state 1 — kit not adopted (no fragment anywhere) -> skip, exit 0
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     recall' && printf '%s' "$out" | grep -q 'kit not adopted'; } \
    && ck "AC8 recall kit absent -> skip, exit 0" 1 || ck "AC8 recall kit absent -> skip, exit 0" 0

  # state 2 — kit adopted, hook opt-in NOT taken -> skip, exit 0 (never UNWIRED)
  cp "$FRAG" memory-recall/recall-opened.fragment.json
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     recall' && printf '%s' "$out" | grep -q 'opt-in not taken'; } \
    && ck "AC8 recall opt-in not taken -> skip, exit 0" 1 || ck "AC8 recall opt-in not taken -> skip, exit 0" 0

  # state 3 — hook file present but no settings block -> UNWIRED, exit 1; --session still exits 0
  printf '// stub\n' > .claude/hooks/recall-opened.js
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall'; } \
    && ck "AC8 recall hook present, unmerged -> UNWIRED, exit 1" 1 || ck "AC8 recall hook present, unmerged -> UNWIRED, exit 1" 0
  chk --session >/dev/null; [ "$?" = 0 ] && ck "AC6 --session exit 0 despite recall unwired" 1 || ck "AC6 --session exit 0 despite recall unwired" 0

  # state 3b — the SAME state with NO settings-merge.py anywhere: still UNWIRED, still exit 1.
  # This is the adopter layout the runbook produced before the delivery step existed, where the arm
  # used to print `skip … cannot verify` and exit 0 on the state the doc calls the one bad state.
  rm -f tools/settings-merge.py
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall'; } \
    && ck "AC8 recall unmerged, no settings-merge.py -> UNWIRED, exit 1" 1 || ck "AC8 recall unmerged, no settings-merge.py -> UNWIRED, exit 1" 0
  cp "$SMERGE" tools/settings-merge.py

  # state 4 — merged into settings.json -> ok, exit 0
  "$py" tools/settings-merge.py --fragment memory-recall/recall-opened.fragment.json >/dev/null 2>&1
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       recall'; } \
    && ck "AC8 recall merged -> ok, exit 0" 1 || ck "AC8 recall merged -> ok, exit 0" 0

  # state 5 — settings still dispatch the hook, the script is gone: UNWIRED, exit 1. Reachable from
  # WIRE §3c step 4 (two separate commands) in reverse order, and from any later loss of the
  # untracked hook file; Claude Code then runs `node` against nothing on every Read.
  rm -f .claude/hooks/recall-opened.js
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall' && printf '%s' "$out" | grep -q 'is missing'; } \
    && ck "AC8 recall wired but script gone -> UNWIRED, exit 1" 1 || ck "AC8 recall wired but script gone -> UNWIRED, exit 1" 0
  cleanup
else
  echo "skip recall cases — settings-merge.py or recall-opened.fragment.json not found"
fi

# AC9 — the eol arm: detect in --check, repair in --fix, and never reach past its bound.
# THE BOUND IS THE POINT, and this fixture uses the BROADEST attribute spelling an adopter might
# reasonably write. An earlier cut pinned only `.claude/**/*.md`, which pre-narrowed the population
# and made "stays inside its bound" green for the fixture's reasons rather than the gate's. Under
# `* text=auto eol=lf` the first implementation rewrote `.claude/settings.json` and stripped CR bytes
# out of the middle of a PNG — md5 changed, reported as "fixed".
newrepo
mkdir -p .claude/skills/x memory
printf '* text=auto eol=lf\n' > .gitattributes
printf 'a\nb\n' > .claude/skills/x/SKILL.md              # a rendered Skill: the whole population
printf 'a\nb\n' > memory/NOTES.md                        # outside .claude/ entirely
printf '{\n  "hooks": {}\n}\n' > .claude/settings.json    # under .claude/, pinned, NOT a Skill
printf 'PNG\r\n\032\r\nIDAT\n' > .claude/skills/x/logo.png   # binary bytes a `tr -d` would eat
git add -A; git commit -q -m eolbase
git config core.hooksPath .githooks                      # isolate: only the eol arm can be unwired
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       eol'; } \
  && ck "AC9 clean LF tree -> ok" 1 || ck "AC9 clean LF tree -> ok" 0
# the checkout defect, reproduced: CRLF in the worktree while the index stays normalised, so
# `git status` is CLEAN and only a byte-comparing gate ever notices.
printf 'a\r\nb\r\n' > .claude/skills/x/SKILL.md
printf 'a\r\nb\r\n' > memory/NOTES.md
printf '{\r\n  "hooks": {}\r\n}\r\n' > .claude/settings.json
cp .claude/skills/x/logo.png "$D/logo.before"

# THE INVISIBILITY, measured rather than asserted from the trap note. `git diff` reports NO content
# difference on the pinned file — the clean filter normalises, so there is nothing to commit — while
# the bytes on disk are CRLF. (`git status --porcelain` does list it: that is the stat cache, not a
# content verdict, and the two disagree here. The trap note's "git status stays clean" was the
# looser half of the observation; this is the half that actually explains the no-op below.)
{ [ -z "$(git diff --numstat -- .claude/skills/x/SKILL.md)" ]; } \
  && ck "AC9 git sees no content change (the defect reproduces)" 1 \
  || ck "AC9 git sees no content change (the defect reproduces)" 0
# A `git checkout --` remedy is NOT asserted here, and the reason is a measurement rather than a
# preference: on this git it DOES restore the file in this fixture, because status' stat cache flags
# it even though diff sees no content change. The two disagree, so a repair built on `git checkout`
# works or no-ops depending on which of them git consults — the previous build hit the no-op and
# needed `rm` first. Rewriting the bytes is correct in BOTH states, which is why it is what --fix
# does. Do not "simplify" it back.
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  eol' && printf '%s' "$out" | grep -q 'SKILL.md'; } \
  && ck "AC9 CRLF on a pinned .claude/ file -> UNWIRED, exit 1" 1 || ck "AC9 CRLF on a pinned .claude/ file -> UNWIRED, exit 1" 0
printf '%s' "$out" | grep -q 'memory/NOTES.md' \
  && ck "AC9 --check stays inside its bound" 0 || ck "AC9 --check stays inside its bound" 1
# --session REPORTS; only --fix rewrites. A SessionStart hook editing file bytes unattended is a far
# bigger act than setting an unset git config, which is all --session was ever allowed to do.
chk --session >/dev/null
LC_ALL=C grep -qU $'\r' .claude/skills/x/SKILL.md \
  && ck "AC9 --session reports without rewriting" 1 || ck "AC9 --session reports without rewriting" 0
chk --fix >/dev/null
LC_ALL=C grep -qU $'\r' .claude/skills/x/SKILL.md \
  && ck "AC9 --fix rewrote the pinned file to LF" 0 || ck "AC9 --fix rewrote the pinned file to LF" 1
# ...and everything OUTSIDE the bound is untouched, under the broadest attribute spelling there is.
# A repair that reaches past its population is worse than one that never ran: it rewrites bytes
# nobody asked it to.
LC_ALL=C grep -qU $'\r' memory/NOTES.md \
  && ck "AC9 --fix left the file outside .claude/ alone" 1 || ck "AC9 --fix left the file outside .claude/ alone" 0
LC_ALL=C grep -qU $'\r' .claude/settings.json \
  && ck "AC9 --fix left .claude/settings.json alone" 1 || ck "AC9 --fix left .claude/settings.json alone" 0
cmp -s .claude/skills/x/logo.png "$D/logo.before" \
  && ck "AC9 --fix did not corrupt a binary in the domain" 1 || ck "AC9 --fix did not corrupt a binary in the domain" 0
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       eol'; } \
  && ck "AC9 re-check after --fix -> ok, exit 0" 1 || ck "AC9 re-check after --fix -> ok, exit 0" 0
# A Skill directory whose name carries a SPACE. `xargs` word-split it into two nonexistent paths, the
# population came back empty, and the arm printed a green `skip` over a file with real CRLF in it.
mkdir -p ".claude/skills/my skill"
printf 'a\nb\n' > ".claude/skills/my skill/SKILL.md"
git add -A; git commit -q -m spaced
printf 'a\r\nb\r\n' > ".claude/skills/my skill/SKILL.md"
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'my skill/SKILL.md'; } \
  && ck "AC9 a Skill path with a space is still seen" 1 || ck "AC9 a Skill path with a space is still seen" 0
chk --fix >/dev/null
LC_ALL=C grep -qU $'\r' ".claude/skills/my skill/SKILL.md" \
  && ck "AC9 --fix repairs a spaced path" 0 || ck "AC9 --fix repairs a spaced path" 1
cleanup

# AC9b — no pinned .claude/ path at all: the arm SKIPS rather than reporting a clean bill over an
# empty population, which is the distinction the empty-population guard exists to make.
newrepo
git config core.hooksPath .githooks
out=$(chk --check)
printf '%s' "$out" | grep -q 'skip     eol' \
  && ck "AC9b no eol=lf pin under .claude/ -> skip, not a silent ok" 1 \
  || ck "AC9b no eol=lf pin under .claude/ -> skip, not a silent ok" 0
cleanup

# AC10 — the row-keyed merge driver arm, all SEVEN states in one repo. A merge DRIVER is per-node
# config while `.gitattributes` is committed, so "declared" and "wired" are different facts and the
# gap between them is silent: git falls back to a line merge, with a warning nobody reads, and that
# line merge is the one that duplicates a row. The remedy string is BUILT from the two resolved
# paths, so this asserts the string the arm PRINTS is the string `--fix` SETS — one truth, not two.
newrepo
git config core.hooksPath .githooks        # isolate: hooks wired, so only the merge arm can be unwired
mkdir -p tools/memory-tree tools/lib memory/backlog
WANT="bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P"

# state 1 — kit not adopted -> skip, exit 0
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     merge' && printf '%s' "$out" | grep -q 'not adopted'; } \
  && ck "AC10 merge driver absent -> skip, exit 0" 1 || ck "AC10 merge driver absent -> skip, exit 0" 0

# state 2 — the driver is present but the shim its command names is missing. git would exec a command
# that cannot start, and a merge driver that cannot start exits non-zero without writing %A.
cp "$HERE/memory-tree/merge-rows.py" tools/memory-tree/merge-rows.py
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'shim it names is missing'; } \
  && ck "AC10 shim missing -> UNWIRED, exit 1" 1 || ck "AC10 shim missing -> UNWIRED, exit 1" 0

# state 3 — both present, but no tracked path declares merge=rows: nothing to wire, so a SKIP rather
# than a permanent false UNWIRED in every repo that carries the kit without the attribute.
cp "$HERE/lib/pyrun.sh" tools/lib/pyrun.sh
git add -A; git commit -q -m kit
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     merge' && printf '%s' "$out" | grep -q 'no tracked path declares'; } \
  && ck "AC10 no merge=rows attribute -> skip, exit 0" 1 || ck "AC10 no merge=rows attribute -> skip, exit 0" 0

# state 4 — declared, config unset -> UNWIRED, exit 1, and the remedy carries the BUILT command
printf 'memory/backlog/*.md merge=rows\n' > .gitattributes
printf '# tooling backlog\n' > memory/backlog/TOOL.md
git add -A; git commit -q -m attrs
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -qF "$WANT"; } \
  && ck "AC10 declared but unset -> UNWIRED + built remedy, exit 1" 1 || ck "AC10 declared but unset -> UNWIRED + built remedy, exit 1" 0

# state 5 — --fix sets exactly that command; the re-check is ok, exit 0
chk --fix >/dev/null; got=$(git config merge.rows.driver); out=$(chk --check); rc=$?
{ [ "$got" = "$WANT" ] && [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 --fix sets the driver, re-check ok" 1 || ck "AC10 --fix sets the driver, re-check ok" 0

# state 6 — a value somebody else set is REPORTED and never clobbered (the check_hooks rule)
git config merge.rows.driver 'bash vendor/other-driver.sh %O %A %B %P'
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'NOT overwriting'; } \
  && ck "AC10 a foreign driver -> UNWIRED, exit 1" 1 || ck "AC10 a foreign driver -> UNWIRED, exit 1" 0
before=$(git config merge.rows.driver); chk --fix >/dev/null; after=$(git config merge.rows.driver)
{ [ "$after" = "$before" ] && [ "$after" != "$WANT" ]; } \
  && ck "AC10 --fix never clobbers a set driver" 1 || ck "AC10 --fix never clobbers a set driver" 0

# state 7 — --session wires the unset case too. Setting a repo-local config is exactly the class of
# act --session exists for; the eol arm's session exemption is not copied because that one rewrites
# file bytes.
git config --unset merge.rows.driver
chk --session >/dev/null; rc=$?; got=$(git config merge.rows.driver)
{ [ "$rc" = 0 ] && [ "$got" = "$WANT" ]; } \
  && ck "AC10 --session wires the driver + exit 0" 1 || ck "AC10 --session wires the driver + exit 0" 0
cleanup

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
