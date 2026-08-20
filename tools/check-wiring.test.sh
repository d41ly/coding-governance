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

# A kit file in THIS repo, resolved across both install prefixes the way every arm resolves them
# (`tools/<rel>` here, `<rel>` in a copy-installed adopter). Nothing below hard-codes `$HERE/…`:
# this test file itself ships to `<project>/tools/`, where the kits it copies from do NOT.
src_of() { for c in "$REPO/tools/$1" "$REPO/$1"; do [ -e "$c" ] && { echo "$c"; return; }; done; }

# Lay a COMPLETE, RUNNABLE merge-driver install into the cwd under prefix $1 ("tools/" here, "" for
# the copy-installed adopter layout). Complete is the point: the driver sources a resolver through
# its shim, imports its anchor grammar from the sibling memory-recall kit, and walks up for
# `.memory-tree.conf`. A fixture missing any of those holds a driver that CANNOT START — which is
# exactly the state the arm under test has to report, so it must be reachable on purpose and never
# by accident.
install_driver() {
  local p="$1" rel src
  mkdir -p "${p}memory-tree" "${p}lib" "${p}memory-recall" memory/backlog
  for rel in memory-tree/merge-rows.py memory-tree/merge-rows.sh lib/pyrun.sh lib/resolve-python.sh \
             memory-recall/extract.py memory-recall/recall_conf.py; do
    src=$(src_of "$rel")
    # A NAMED cause instead of `cp: cannot stat ''`. Every file in this list is a runtime dependency
    # of the driver — the shim's resolver, the memory-recall kit the anchor grammar is imported
    # from — so a repo carrying `merge-rows.py` without one of them carries a driver that cannot
    # start. That is a defect in the repo, not a gap in the fixture, and it reds rather than skips.
    [ -n "$src" ] || { ck "install_driver: $rel is not installed in $REPO (the driver cannot run without it)" 0; return 1; }
    cp "$src" "${p}${rel}"
  done
  printf 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\n' > .memory-tree.conf
  # A REAL ANCHORED ROW, not an empty index. The merge arm harvests the family prefix each row LEADS
  # with and requires the conf to declare it — over an index with no rows that harvest is empty and
  # state 5d below would pass by finding nothing, which is the vacuity this repo's pop_guard idiom
  # exists to refuse. State 5d IS the liveness proof: it only reds if this row is here and harvested.
  printf '# tooling backlog\n\n- TOOL-001 | a landed row, so the family harvest has a population\n' > memory/backlog/TOOL.md
  printf 'memory/backlog/*.md merge=rows\n' > .gitattributes
  git add -A; git commit -q -m driver
}

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

  # AC7b — THE STALE MATCHER. `.claude/settings.json` carries the hook under `Workflow` alone: the
  # state where a direct `Agent` spawn meets no rule at all, and the state every repo was in before
  # the widening. The retired predicate grepped the whole file for `agent-cap.js`, so it reported
  # `ok` here — it could not tell a correctly-widened wiring from a stale one and never could have.
  # This arm fails against that predicate, which is what makes it a test rather than a restatement.
  cat > .claude/settings.json <<'JSON'
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Workflow",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\""
          }
        ]
      }
    ]
  }
}
JSON
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  agent-cap' \
      && printf '%s' "$out" | grep -q "wired under matcher 'Workflow'"; } \
    && ck "AC7b a stale Workflow-only matcher -> UNWIRED naming the value found" 1 \
    || ck "AC7b a stale Workflow-only matcher -> UNWIRED naming the value found" 0
  # ...and the widened value is the one that reads ok. Without this half the arm is satisfied by a
  # checker that denies every matcher there is. Written directly rather than merged: settings-merge
  # ADDS the widened group beside a stale one instead of migrating it, so a merge here would test
  # the two-group state, which is a different fact.
  sed -i 's/"matcher": "Workflow"/"matcher": "Workflow|Agent"/' .claude/settings.json
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       agent-cap'; } \
    && ck "AC7b the widened matcher -> ok, exit 0" 1 || ck "AC7b the widened matcher -> ok, exit 0" 0
  cleanup
else
  echo "skip agent-cap cases — settings-merge.py not found next to script"
fi

# AC13 — the scratch-guard arm, FOUR states in one repo. Written like the recall arm rather than the
# agent-cap one because this arm reads marker/matcher/hook_path from the shipped fragment, so a
# fixture that hardcodes them would be testing a second spelling of the contract instead of the one
# the kit declares. Unlike recall the guard is NOT an opt-in, so a present-but-unwired hook is a real
# UNWIRED and an absent hook file is "kit not adopted here".
SGFRAG="$HERE/hooks/scratch-guard.fragment.json"
if [ -f "$SGFRAG" ] && [ -f "$SMERGE" ]; then
  newrepo; mkdir -p tools/hooks .claude/hooks
  cp "$SMERGE" tools/settings-merge.py
  cp "$SGFRAG" tools/hooks/scratch-guard.fragment.json
  git config core.hooksPath .githooks    # isolate: hooks wired, so only scratch-guard can move the exit

  # 13a — fragment shipped, hook not installed, nothing in settings: NOT adopted, must not gate.
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     scratch'; } \
    && ck "AC13a fragment present, hook absent -> skip, exit 0" 1 \
    || ck "AC13a fragment present, hook absent -> skip, exit 0" 0

  # 13b — hook installed but nothing in settings.json: the dormant-guard state, and the whole reason
  # this arm exists. A guard that is silent because it is unwired looks exactly like one that passed.
  printf '// stub\n' > .claude/hooks/scratch-guard.js
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  scratch'; } \
    && ck "AC13b hook present, unwired -> UNWIRED, exit 1" 1 \
    || ck "AC13b hook present, unwired -> UNWIRED, exit 1" 0
  chk --session >/dev/null; [ "$?" = 0 ] \
    && ck "AC13b --session exits 0 despite scratch-guard unwired" 1 \
    || ck "AC13b --session exits 0 despite scratch-guard unwired" 0

  # 13c — THE STALE MATCHER. Wired under `Bash` alone: the state where the same write through the
  # PowerShell surface meets no rule at all. A file-wide grep for the marker reports ok here, which
  # is why the arm reads the matcher and why this fixture is written directly rather than merged —
  # settings-merge ADDS a group beside a stale one instead of migrating it.
  cat > .claude/settings.json <<'JSON'
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/scratch-guard.js\""
          }
        ]
      }
    ]
  }
}
JSON
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  scratch' \
      && printf '%s' "$out" | grep -q "wired under matcher 'Bash'"; } \
    && ck "AC13c a stale Bash-only matcher -> UNWIRED naming the value found" 1 \
    || ck "AC13c a stale Bash-only matcher -> UNWIRED naming the value found" 0

  # 13d — and the declared matcher reads ok. Without this half the arm is satisfied by a checker that
  # denies every matcher there is.
  rm -f .claude/settings.json
  "${PYBIN:-python}" tools/settings-merge.py --fragment tools/hooks/scratch-guard.fragment.json >/dev/null 2>&1
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       scratch'; } \
    && ck "AC13d the fragment's own matcher -> ok, exit 0" 1 \
    || ck "AC13d the fragment's own matcher -> ok, exit 0" 0
  cleanup
else
  echo "skip scratch-guard cases — fragment or settings-merge.py not found next to script"
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
# REPORTS, does NOT gate. The committed bytes are LF, so nothing in the repository is wrong and
# nothing is dormant — and a consumer that reads the exit status as a refusal (.unattended.conf
# declares this script as its WIRING_CHECK) refused every run in a worktree carrying the artifact.
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'note     eol' && printf '%s' "$out" | grep -q 'SKILL.md'; } \
  && ck "AC9 CRLF on a pinned .claude/ file -> note, exit 0" 1 || ck "AC9 CRLF on a pinned .claude/ file -> note, exit 0" 0
printf '%s' "$out" | grep -q 'UNWIRED  eol' \
  && ck "AC9 the eol arm no longer spells the gating label" 0 || ck "AC9 the eol arm no longer spells the gating label" 1
printf '%s' "$out" | grep -q 'memory/NOTES.md' \
  && ck "AC9 --check stays inside its bound" 0 || ck "AC9 --check stays inside its bound" 1
# THE SIBLING, and without it the arm above is indistinguishable from having DELETED the eol arm:
# a genuinely dormant item in the SAME run, with the same CRLF still present, still gives rc 1 and
# still names itself. `--check` never sets config, so unsetting here does not leak into the arms
# below; it is restored immediately.
git config --unset core.hooksPath
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  hooks' && printf '%s' "$out" | grep -q 'note     eol'; } \
  && ck "AC9 a dormant item in the same run still gates, alongside the note" 1 \
  || ck "AC9 a dormant item in the same run still gates, alongside the note" 0
git config core.hooksPath .githooks
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
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'my skill/SKILL.md'; } \
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

# AC10 — the row-keyed merge driver arm, all NINE states in one repo. A merge DRIVER is per-node
# config while `.gitattributes` is committed, so "declared" and "wired" are different facts and the
# gap between them is silent: git falls back to a line merge, and that line merge is the one that
# duplicates a row. The remedy string is BUILT from the two resolved paths, so this asserts the
# string the arm PRINTS is the string `--fix` SETS — one truth, not two.
#
# The fixture lays a COMPLETE install (driver + shim + resolver + the memory-recall kit the anchor
# grammar is imported from + the conf naming the families), because the arm now RUNS the configured
# command before it says `ok`. A fixture that could not start the driver would turn every green
# below into a green for the fixture's reasons instead of the tool's.
newrepo
git config core.hooksPath .githooks        # isolate: hooks wired, so only the merge arm can be unwired
mkdir -p tools/memory-tree tools/lib memory/backlog
WANT="bash tools/memory-tree/merge-rows.sh %O %A %B %P"

# state 1 — kit not adopted -> skip, exit 0
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     merge' && printf '%s' "$out" | grep -q 'not adopted'; } \
  && ck "AC10 merge driver absent -> skip, exit 0" 1 || ck "AC10 merge driver absent -> skip, exit 0" 0

# state 2 — the driver is present but NO launcher is. git would exec a command that cannot start, and
# a merge driver that cannot start exits non-zero without writing %A: git then reports CONFLICT and
# leaves the path holding OURS-only content with no markers. The remedy has to name the launcher that
# TRAVELS WITH THE KIT, because `tools/lib/pyrun.sh` is gov-internal and an adopter never receives it.
cp "$(src_of memory-tree/merge-rows.py)" tools/memory-tree/merge-rows.py
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'merge-rows.sh beside it'; } \
  && ck "AC10 no launcher -> UNWIRED naming the kit-internal one, exit 1" 1 \
  || ck "AC10 no launcher -> UNWIRED naming the kit-internal one, exit 1" 0

# state 3 — the whole kit is present, but no tracked path declares merge=rows: nothing to wire, so a
# SKIP rather than a permanent false UNWIRED in every repo that carries the kit without the
# attribute. `install_driver` writes the attribute, so it is stripped again for this one state.
install_driver "tools/"
printf '# nothing declared here\n' > .gitattributes
git add -A; git commit -q -m nodeclare
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     merge' && printf '%s' "$out" | grep -q 'no tracked path declares'; } \
  && ck "AC10 no merge=rows attribute -> skip, exit 0" 1 || ck "AC10 no merge=rows attribute -> skip, exit 0" 0

# state 4 — declared, config unset -> UNWIRED, exit 1, and the remedy carries the BUILT command
printf 'memory/backlog/*.md merge=rows\n' > .gitattributes
git add -A; git commit -q -m attrs
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -qF "$WANT"; } \
  && ck "AC10 declared but unset -> UNWIRED + built remedy, exit 1" 1 || ck "AC10 declared but unset -> UNWIRED + built remedy, exit 1" 0

# state 5 — --fix sets exactly that command; the re-check is ok, exit 0
chk --fix >/dev/null; got=$(git config merge.rows.driver); out=$(chk --check); rc=$?
{ [ "$got" = "$WANT" ] && [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 --fix sets the driver, re-check ok" 1 || ck "AC10 --fix sets the driver, re-check ok" 0
# ...and it is the KIT-INTERNAL launcher that won, not the gov-internal shim. `install_driver` lays
# both, so without this the fallback could silently win everywhere and every arm here would still
# pass — while an adopter, who receives only the kit, got a command naming a file they do not have.
{ printf '%s' "$got" | grep -q 'memory-tree/merge-rows.sh' \
  && ! printf '%s' "$got" | grep -q 'pyrun'; } \
  && ck "AC10 the kit launcher wins over the gov-internal shim" 1 \
  || ck "AC10 the kit launcher wins over the gov-internal shim" 0

# state 5b — the config is UNCHANGED and correct, and the driver still cannot START: the resolver
# `pyrun.sh` sources is gone. MEASURED before this arm existed: `ok  merge  — merge.rows.driver
# wired`, and the very next `git merge` printed CONFLICT and left memory/DECISIONS.md holding
# OURS-only content with `grep -c '<<<<<<<'` = 0 and status UU — the incoming row simply absent.
# "Wired" has to mean the command RUNS, so this state must not be green.
# RE-AIMED: the kit-internal launcher carries the resolver INLINE, so removing `tools/lib/` no
# longer breaks it — that decoupling is the whole point of shipping a launcher with the kit. What it
# still cannot survive is a driver that will not parse. Removing the FILE would trip the
# not-adopted probe one test earlier and never reach this arm, so the content is what breaks.
cp tools/memory-tree/merge-rows.py tools/memory-tree/merge-rows.py.away
printf 'this is not python(
' > tools/memory-tree/merge-rows.py
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'cannot merge'; } \
  && ck "AC10 driver cannot start (unparseable driver) -> UNWIRED, exit 1" 1 || ck "AC10 driver cannot start (unparseable driver) -> UNWIRED, exit 1" 0
# ...and --fix must not DECLARE a broken driver wired either. Wiring a command that cannot run is
# strictly worse than leaving it unset: unset falls back to git's line merge, wired-and-broken is
# the silent take-ours above.
git config --unset merge.rows.driver
chk --fix >/dev/null; got=$(git config merge.rows.driver 2>/dev/null || true)
[ -z "$got" ] && ck "AC10 --fix refuses to wire a driver that cannot run" 1 || ck "AC10 --fix refuses to wire a driver that cannot run" 0
mv -f tools/memory-tree/merge-rows.py.away tools/memory-tree/merge-rows.py
chk --fix >/dev/null; out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the driver goes green again" 1 || ck "AC10 restoring the driver goes green again" 0

# state 5b2 — the smoke run itself cannot run. A verifier that could not verify must not print the
# same `ok` as one that did: this file already deleted a `cannot verify` skip from the recall arm for
# reporting exit 0 on the one state the runbook calls bad, and the new dependency on a temp dir is a
# second way into that state. TMPDIR points somewhere that does not exist, so mktemp -d fails.
out=$(TMPDIR=/nonexistent-check-wiring-tmp bash "$SCRIPT" --check 2>/dev/null); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'cannot verify'; } \
  && ck "AC10 unverifiable (no temp dir) -> UNWIRED, not a silent ok" 1 || ck "AC10 unverifiable (no temp dir) -> UNWIRED, not a silent ok" 0

# state 5c — the driver STARTS but cannot key a row: the sibling memory-recall kit that owns the
# anchor grammar is gone, so the deferred import raises and the fail-closed wrapper writes a conflict
# on every governed-index merge, forever. Loud rather than destructive, but the arm's own header
# claims it turns "declared" into "wired"; a driver that conflicts unconditionally is not wired.
mv tools/memory-recall tools/memory-recall.away
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'cannot merge'; } \
  && ck "AC10 driver cannot key rows (no memory-recall) -> UNWIRED, exit 1" 1 || ck "AC10 driver cannot key rows (no memory-recall) -> UNWIRED, exit 1" 0
mv tools/memory-recall.away tools/memory-recall
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the grammar kit goes green again" 1 || ck "AC10 restoring the grammar kit goes green again" 0

# state 5d — the driver STARTS, the smoke fixture merges CLEANLY, and the driver is still inert on
# the only files it is wired to: one token of drift in `.memory-tree.conf` FAMILIES
# (`tooling:TOOL` -> `tooling:TOOLS`) renames the family every landed row LEADS with. The smoke
# fixture is BUILT from the conf, so it renames with it and stays green — MEASURED: the arm printed
# `ok  merge  — merge.rows.driver wired` while the driver keyed ZERO rows and every governed
# append-collision conflicted forever. So the arm asks the declared indexes directly. This state is
# also the liveness proof for that harvest: it can only red if `install_driver`'s landed row is there
# and really is being read.
sed -i.bak 's/tooling:TOOL"/tooling:TOOLS"/' .memory-tree.conf && rm -f .memory-tree.conf.bak
grep -q 'tooling:TOOLS' .memory-tree.conf || ck "AC10 family-drift fixture: the conf edit did not apply" 0
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'does not declare TOOL'; } \
  && ck "AC10 conf renames the family the indexes use -> UNWIRED, exit 1" 1 || ck "AC10 conf renames the family the indexes use -> UNWIRED, exit 1" 0
sed -i.bak 's/tooling:TOOLS"/tooling:TOOL"/' .memory-tree.conf && rm -f .memory-tree.conf.bak
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the declared family goes green again" 1 || ck "AC10 restoring the declared family goes green again" 0

# state 5e — THE INERTNESS CHANNEL THE TWO-PLANE DRIVER OPENS, and state 5d cannot reach it.
#
# 5d drifts FAMILIES, and the smoke fixture is built FROM the conf, so its rows rename with it and
# key normally under exactly the drift being applied — 100% keyed. What reds 5d is the pre-existing
# harvest of the LANDED row's prefix, and control only reaches that harvest because the smoke
# PASSED. So 5d is a regression guard on a different arm and proves nothing about the keyed count.
#
# The state that does: a grammar that IMPORTS cleanly and keys NOTHING. Under the retired driver an
# unkeyable row was content, so the append collision conflicted and inert was loud. Under the two
# planes it is a hashed ROW, reconciliation rule 3 resolves the collision, and all twelve ids land
# exactly once at rc 0 — better than `git merge-file`, which refuses the same three blobs, while the
# id-level no-duplicate guarantee is entirely off. Every other assertion in the arm is green over it.
# `anchor_at` is REDEFINED rather than deleted, so the import still succeeds and the fail-closed
# handler is not what answers: this state is about a grammar that works and recognises nothing.
printf '\n\ndef anchor_at(line, g=None):\n    return None\n' >> tools/memory-recall/extract.py
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'HASHED'; } \
  && ck "AC10 a grammar that keys NOTHING -> UNWIRED naming the hashed count, exit 1" 1 || ck "AC10 a grammar that keys NOTHING -> UNWIRED naming the hashed count, exit 1" 0
# ...and the state really is the quiet one it claims to be: with the keyed-count assertion removed
# from the checker, this same tree passes every other assertion the arm makes. Proved by running the
# smoke's own three-way by hand and observing a clean, complete, id-preserving merge.
Q=$(mktemp -d); printf -- '- TOOL-001 | base\n' > "$Q/o"
printf -- '- TOOL-001 | base\n- TOOL-002 | ours\n' > "$Q/a"; printf -- '- TOOL-001 | base\n- TOOL-003 | theirs\n' > "$Q/b"
qerr=$(bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py "$Q/o" "$Q/a" "$Q/b" x 2>&1 >/dev/null); qrc=$?
qn=0; for i in 001 002 003; do [ "$(grep -c -- "^- TOOL-$i |" "$Q/a")" = 1 ] && qn=$((qn+1)); done
{ [ "$qrc" = 0 ] && [ "$qn" = 3 ] && printf '%s' "$qerr" | grep -q '(0 keyed, 3 hashed)'; } \
  && ck "AC10 the dead grammar still merges cleanly (0 keyed, 3 hashed) — the channel is real and quiet" 1 \
  || ck "AC10 the dead grammar still merges cleanly (0 keyed, 3 hashed) — the channel is real and quiet [rc=$qrc ids=$qn err=$qerr]" 0
rm -rf "$Q"
git checkout -q -- tools/memory-recall/extract.py 2>/dev/null || true
if grep -q 'def anchor_at(line, g=None):' tools/memory-recall/extract.py; then
  cp "$(src_of memory-recall/extract.py)" tools/memory-recall/extract.py
fi
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the real grammar goes green again" 1 || ck "AC10 restoring the real grammar goes green again" 0

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

# AC11 — the `merge=rows` ATTRIBUTE, asserted against THIS repo's REAL tree.
# The attribute is what actually ROUTES a conflict through the driver. Without it git falls back to
# its built-in line merge — the one measured introducing a duplicate id in 147 of 151 historical
# DECISIONS.md conflicts — and nothing said so: deleting both `.gitattributes` lines left every leg
# on the bar green, the driver's own replay test included, because that test writes its OWN
# `.gitattributes` inside a scratch repo and therefore proves the driver works against an attribute
# it invented rather than against this repo's.
#
# WHY THIS FILE and not the driver's replay test: that file owns the driver's BEHAVIOUR over fixtures
# it controls, and every fixture it merges is one it wrote. This file owns whether the wiring in the
# real tree is real — the question every arm above asks — and it already holds `$REPO` for exactly
# that reason. It is also already a gate leg, so the attribute becomes gated without a new leg.
#
# Read through `git check-attr`, never by grepping `.gitattributes`: attributes come from several
# files and git is the only authority on the answer. That is the same rule check_eol and
# check_merge_rows already follow, and the rule the end-to-end merge fixture applies to its own tree.
cd "$REPO"
ATTR_DRV=""; for c in "$REPO/tools/memory-tree/merge-rows.py" "$REPO/memory-tree/merge-rows.py"; do
  [ -f "$c" ] && { ATTR_DRV="$c"; break; }
done
if [ -z "$ATTR_DRV" ]; then
  echo "skip merge-attribute case — the row-keyed driver is not installed in this repo"
else
  MROOT=$(sed -n 's/^[[:space:]]*MEMORY_ROOT=//p' "$REPO/.memory-tree.conf" 2>/dev/null \
          | head -1 | tr -d '"'"'"'\r')
  [ -n "$MROOT" ] || MROOT=memory
  POP=$(git ls-files -- "$MROOT/DECISIONS.md" "$MROOT/backlog/*.md" | grep . || true)
  # POP GUARD. "Every governed index declares merge=rows" is vacuously true over zero of them, and a
  # gate that passes by finding nothing is the failure class this repo catalogues. The population is
  # asserted non-empty FIRST, and it is derived from the conf rather than listed here, so a
  # MEMORY_ROOT rename reds instead of quietly emptying the set.
  n=$(printf '%s\n' "$POP" | grep -c . || true)
  [ "${n:-0}" -ge 2 ] && ck "AC11 the governed indexes exist ($n tracked)" 1 \
                      || ck "AC11 the governed indexes exist ($n tracked)" 0
  BAD=$(printf '%s\n' "$POP" | grep . | git check-attr --stdin merge | grep -v ': merge: rows$' || true)
  if [ -z "$BAD" ]; then
    ck "AC11 every governed index declares merge=rows" 1
  else
    ck "AC11 every governed index declares merge=rows" 0
    printf '     %s\n' "$BAD"
  fi
fi

# AC12 — the PUBLISHED wiring command, DERIVED rather than proof-read.
# The kit README used to publish ONE literal that mixed the two install prefixes, naming a driver
# that exists in NEITHER layout. Configuring it verbatim reproduced the whole failure end to end:
# `can't open file '…/memory-tree/merge-rows.py'`, git printing `CONFLICT (content)`, and the path
# left holding ours-only content with `grep -c '<<<<<<<'` = 0 and status UU. Nothing gated the
# string, because the only other places the command appears either hand-type the correct one inside a
# fixture or BUILD it at runtime.
#
# So this arm does not proof-read the README. It DERIVES both spellings by running `--fix` in a
# complete fixture of each layout, then requires the README to publish exactly those two and no
# third one. A future prefix change moves the derived strings and reds the doc automatically.
newrepo; git config core.hooksPath .githooks; install_driver "tools/"
chk --fix >/dev/null; S_TOOLS=$(git config merge.rows.driver 2>/dev/null || true); cleanup
newrepo; git config core.hooksPath .githooks; install_driver ""
chk --fix >/dev/null; S_ROOT=$(git config merge.rows.driver 2>/dev/null || true); cleanup
cd "$REPO"
# LIVENESS, before anything is compared against the doc: two layouts that produced the SAME string,
# or no string at all, would turn the two greps below into one assertion wearing two hats.
{ [ -n "$S_TOOLS" ] && [ -n "$S_ROOT" ] && [ "$S_TOOLS" != "$S_ROOT" ]; } \
  && ck "AC12 the two layouts yield two distinct commands" 1 \
  || ck "AC12 the two layouts yield two distinct commands" 0
RDM=""; for c in "$REPO/tools/memory-tree/README.md" "$REPO/memory-tree/README.md"; do
  [ -f "$c" ] && { RDM="$c"; break; }
done
if [ -z "$RDM" ]; then
  echo "skip README-command case — the memory-tree kit README is not installed in this repo"
else
  grep -qF "$S_TOOLS" "$RDM" && ck "AC12 README publishes the tools/-prefix command" 1 \
                             || ck "AC12 README publishes the tools/-prefix command" 0
  grep -qF "$S_ROOT"  "$RDM" && ck "AC12 README publishes the root-prefix command" 1 \
                             || ck "AC12 README publishes the root-prefix command" 0
  # ...and NO third spelling. This is the half that fires on a mixed-prefix literal, which is a
  # command both greps above are perfectly happy to coexist with.
  STRAY=$(grep -oE 'bash [A-Za-z0-9_./-]*pyrun\.sh [A-Za-z0-9_./-]*merge-rows\.py %O %A %B %P' "$RDM" \
          | grep -vxF "$S_TOOLS" | grep -vxF "$S_ROOT" || true)
  if [ -z "$STRAY" ]; then
    ck "AC12 README publishes no third, unstartable spelling" 1
  else
    ck "AC12 README publishes no third, unstartable spelling" 0
    printf '     stray: %s\n' "$STRAY"
  fi
fi

# ---- the machine-global /session-kickoff install ------------------------------------------------
# Every arm drives HOME at a scratch dir, so nothing reads or writes the operator's real install.
# The tracked side is faked inside the throwaway repo, which is what makes the adopter arm (AC7)
# reachable at all: an adopter has the install and NO tracked kit source.
skill_fixture() {   # $1=1 to lay a tracked skills/session-kickoff/ into the repo
  FAKEHOME=$(mktemp -d); mkdir -p "$FAKEHOME/.claude/skills/session-kickoff"
  if [ "${1:-0}" = 1 ]; then
    mkdir -p skills/session-kickoff
    printf 'engine\n' > skills/session-kickoff/SKILL.md
    printf 'template\n' > skills/session-kickoff/MANIFEST-TEMPLATE.md
    printf 'checker\n' > skills/session-kickoff/manifest-check.sh
    git add -A >/dev/null 2>&1; git commit -q -m skill
  fi
}
install_engine() {  # $1=SKILL.md body
  printf '%s' "$1" > "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md"
  printf 'template\n'  > "$FAKEHOME/.claude/skills/session-kickoff/MANIFEST-TEMPLATE.md"
  printf 'checker\n'   > "$FAKEHOME/.claude/skills/session-kickoff/manifest-check.sh"
}
skill_run() { HOME="$FAKEHOME" bash "$SCRIPT" --check 2>/dev/null | grep ' skill  ' || true; }

newrepo; skill_fixture 1; rm -rf "$FAKEHOME/.claude/skills/session-kickoff"
out=$(skill_run)
case "$out" in "skip     skill"*"not installed on this machine"*) r=1 ;; *) r=0 ;; esac
ck "AC1 no install on this machine -> skip" "$r"; rm -rf "$FAKEHOME"; cleanup

newrepo; skill_fixture 1; install_engine 'engine
'
out=$(skill_run)
case "$out" in "ok       skill"*"matches tracked"*) r=1 ;; *) r=0 ;; esac
ck "AC3 installed engine matches tracked -> ok" "$r"; rm -rf "$FAKEHOME"; cleanup

newrepo; skill_fixture 1; install_engine 'DIFFERENT
'
out=$(skill_run)
case "$out" in "UNWIRED  skill"*"differs from tracked in: SKILL.md"*) r=1 ;; *) r=0 ;; esac
ck "AC2 installed SKILL.md differs -> UNWIRED naming the file" "$r"
case "$out" in *"Fix:"*) r=1 ;; *) r=0 ;; esac
ck "AC2 the UNWIRED line carries a Fix remedy" "$r"; rm -rf "$FAKEHOME"; cleanup

# AC4 — CRLF on the installed side must NOT read as drift. This is the arm that fails if either half
# of the normalisation is dropped, and the one the repo's own trap says a byte-compare always needs.
newrepo; skill_fixture 1; install_engine 'engine
'
printf 'engine\r\n' > "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md"
out=$(skill_run)
case "$out" in "ok       skill"*) r=1 ;; *) r=0 ;; esac
ck "AC4 a CRLF installed copy is not reported as drift" "$r"; rm -rf "$FAKEHOME"; cleanup

newrepo; skill_fixture 1; install_engine 'engine
'
rm -f "$FAKEHOME/.claude/skills/session-kickoff/manifest-check.sh"
out=$(skill_run)
case "$out" in "UNWIRED  skill"*"missing manifest-check.sh"*) r=1 ;; *) r=0 ;; esac
ck "a shipped file absent from the install -> UNWIRED naming it" "$r"; rm -rf "$FAKEHOME"; cleanup

# AC7 — the adopter shape: the install exists, the repo tracks no kit source. Without this state the
# check is a permanent false alarm in every adopting repo.
newrepo; skill_fixture 0; install_engine 'engine
'
out=$(skill_run)
case "$out" in "skip     skill"*"not adopted in this repo"*) r=1 ;; *) r=0 ;; esac
ck "AC7 install present, kit not adopted here -> skip (not a false alarm)" "$r"; rm -rf "$FAKEHOME"; cleanup

# AC5 — --fix must NOT touch the install. The out-of-repo write is refused by design, so the bytes
# are compared before and after rather than the refusal being argued in prose.
newrepo; skill_fixture 1; install_engine 'DIFFERENT
'
before=$(cat "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md")
HOME="$FAKEHOME" bash "$SCRIPT" --fix >/dev/null 2>&1 || true
after=$(cat "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md")
ck "AC5 --fix leaves the out-of-repo install byte-identical" "$([ "$before" = "$after" ] && echo 1 || echo 0)"
rm -rf "$FAKEHOME"; cleanup

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
