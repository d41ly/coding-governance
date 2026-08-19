#!/usr/bin/env bash
# cross-component.test.sh — the DRIVER and then the LEG, over ONE tree.
#
# TOOL-aPromptedMandate-6, closing TOOL-aStandingWrit-8: this kit had driver arms, leg arms and
# Skill-parity arms, and ZERO arms that ran the driver and THEN the leg against the same repository.
# Both halves could agree with themselves and disagree with each other, and nothing looked. Every
# arm below was first performed BY HAND during this build; the reproduction record under
# memory/builds/aPromptedMandate/build/ carries the observed output each one asserts.
#
# WHY A SEPARATE LEG rather than arms in the driver suite: that suite pins a single unit-branch
# commit and never pushes. The arms here deliberately MOVE the advertised branch tip, and
# retrofitting that into a shared fixture would perturb every existing arm in a 1600-line file.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
st=0; n=0
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }

# LOUD SKIP, never a silent one: a host that cannot host the fixture must not score a missing
# capability as a pass. The adopter suite's junction arm is spelled the same way for the same reason.
WORK=$(mktemp -d 2>/dev/null) || { echo "SKIP cross-component: no mktemp -d on this host"; exit 0; }
trap 'rm -rf "$WORK"' EXIT
cd "$WORK" || { echo "SKIP cross-component: cannot enter the scratch tree"; exit 0; }

git init -q --bare origin.git 2>/dev/null || { echo "SKIP cross-component: git init --bare unavailable"; exit 0; }
# The bare repo must ADVERTISE a HEAD symref. `git init --bare` leaves HEAD pointing at whatever
# init.defaultBranch says, which then dangles — and `ls-remote --symref --exit-code HEAD` exits 2
# against that, which is the anchor observation's own refusal. Without this line every arm below
# would die on a defect in the FIXTURE while reading as a defect in the kit.
git --git-dir=origin.git symbolic-ref HEAD refs/heads/main
git init -q repo && cd repo
git config user.email t@t; git config user.name t; git config commit.gpgsign false
git checkout -q -b main

mkdir -p memory/guides tools/unattended .claude/skills/unattended
# The REAL files, not stubs. Measured during this build: an incomplete fixture makes the leg fail on
# checks that have nothing to do with the subject, and a naive arm reading "the leg failed" scores
# that as a correct refusal. This is `fixture-passes-by-finding-nothing` inverted — the fixture fails
# by finding the WRONG thing — which is why the completeness precondition below runs before any arm.
cp "$HERE/unattended.sh" "$HERE/check-unattended.sh" "$HERE/PROTOCOL.template.md" \
   "$HERE/SKILL.template.md" tools/unattended/
cp "$HERE/../../memory/guides/BUILD-METHOD.md" memory/guides/
cp "$HERE/../../memory/guides/UNATTENDED-PROTOCOL.md" memory/guides/
sed -e 's|{{MEMORY_ROOT}}|memory|g' -e 's|{{KIT_DIR}}|tools/unattended|g' \
    -e 's|{{KEEPALIVE_CREATE}}|CronCreate|g' -e 's|{{KEEPALIVE_DELETE}}|CronDelete|g' \
    -e 's|{{KEEPALIVE_INTERVAL}}|every 10 minutes|g' -e 's|{{LANDER}}|bash tools/push-main.sh|g' \
    -e 's|{{ANCHOR_SCOPE}}|published|g' "$HERE/SKILL.template.md" > .claude/skills/unattended/SKILL.md
sed -e 's/^ANCHOR_SCOPE=.*/ANCHOR_SCOPE="published"/' -e 's|^GATE_CMD=.*|GATE_CMD="true"|' \
    -e 's|^WIRING_CHECK=.*|WIRING_CHECK="true"|' -e 's|^KICKOFF_ENGINE=.*|KICKOFF_ENGINE=""|' \
    "$HERE/../../.unattended.conf" > .unattended.conf
git add -A >/dev/null && git commit -q -m base --no-verify
git remote add origin ../origin.git && git push -q origin main

drive() { bash tools/unattended/unattended.sh "$@" 2>&1; }
leg()   { bash tools/unattended/check-unattended.sh 2>&1; }
mk() { # slug · optional extra front-matter line
  mkdir -p "memory/builds/$1"
  { echo '---'; echo "slug: $1"; [ -n "${2:-}" ] && echo "$2"; echo 'streams: tooling'; echo '---'
    echo; echo "# $1"; echo; echo '<!-- roster:units -->'; echo '| # | Unit |'; echo '|---|---|'
    echo '| 1 | the unit |'; echo '<!-- /roster:units -->'
    echo; echo '<!-- gen:build-index -->'
    # TOOL-aBoundedVerdict-11 S5 - the NESTED units pair. Check 21 requires it on every tracked build
    # README, so a fixture that omits it reds the leg on the fixture rather than on the kit.
    echo '<!-- gen:build-units -->'; echo '<!-- /gen:build-units -->'
    echo '<!-- /gen:build-index -->'; } > "memory/builds/$1/README.md"
}

# ---- PRECONDITION: the fixture is COMPLETE before anything perturbs it. An arm that runs against a
# ---- half-built tree tests the fixture, not the kit, and reports it as a kit verdict.
git checkout -q -b unit
out=$(leg)
same "fixture precondition: the leg is silent over the untouched fixture" "$out" ""

# ---- ARM 1: a build folder the RUN authored, branch NOT pushed. Nothing published authorizes it.
mk tRun
git add -A >/dev/null && git commit -q -m "run-authored build folder" --no-verify
before=$([ -f memory/builds/tRun/RUN.md ] && git hash-object memory/builds/tRun/RUN.md || echo none)
out=$(drive --preflight tRun --keepalive-id k1)
hit "$out" "the remote advertises no tip for the branch this run is on, so nothing published authorizes it"
same "arm 1 wrote no run-state file" "$([ -f memory/builds/tRun/RUN.md ] && git hash-object memory/builds/tRun/RUN.md || echo none)" "$before"

# ---- ARM 2: the SAME tree with the branch pushed. Two commands is the whole difference, and that
# ---- is protocol section 1 cost 1 stated as an executable fact rather than as prose.
git push -q origin unit
out=$(drive --preflight tRun --keepalive-id k1)
hit "$out" "preflight OK"
hit "$(cat memory/builds/tRun/RUN.md)" "anchor-kind: run-branch"

# ---- ARM 3: the LEG over arm 2's tree. Exit 0 AND no output — a leg that fails silently and a leg
# ---- that passes share an exit code, so the code alone cannot tell them apart. This build's first
# ---- leg run returned 0 for one arm while other checks were failing.
git add -A >/dev/null && git commit -q -m runstate --no-verify && git push -qf origin unit
out=$(leg); rc=$?
same "arm 3: the leg accepts a run-branch anchor, exit code" "$rc" "0"
same "arm 3: the leg accepts a run-branch anchor, output" "$out" ""

# ---- ARM 4a/4b: the SCOPE-INTEGRITY seam, RE-AIMED by the aBoundedVerdict merge. These arms were
# ---- written against the AUTHORED `roster:units` pair and byte-equality; TOOL-aBoundedVerdict-11 S6
# ---- moved the authorization subject to the GENERATED `gen:build-units` region and compares unit-ID
# ---- SETS, requiring the BASE set to be a SUBSET of HEAD. Perturbing the authored roster now moves
# ---- nothing this check reads, so these arms would have passed vacuously against a DELETED check -
# ---- which is the trap the original comment below warns about, one level up.
# ----
# ---- THE DIRECTIONS ARE NOT SYMMETRIC, and that is the design rather than a gap. An ADDITION comes
# ---- from a new spec, and `build-complete` then requires that unit terminal before close, so a run
# ---- cannot buy itself anything by widening. A REMOVAL is the attack: drop an unfinished unit and
# ---- build-complete passes over work nobody did. 4a proves an addition is admitted; 4b proves a
# ---- removal is refused.
# ----
# ---- Keyed on the DoD VERDICT, never on close output: --close evaluates the item as
# ---- `check_authorization ... >/dev/null 2>&1`, so every message it emits is discarded and an arm
# ---- reading that output is green whether the scope is legal, illegal, or the check is deleted.
UROW='| [TOOL-tRun-1 - the unit](spec/2026-08-19-spec-TOOL-tRun-1.md) | OPEN | rev-1 | 2026-08-19 |'
awk -v r="$UROW" '$0 == "<!-- /gen:build-units -->" { print r } { print }' memory/builds/tRun/README.md > "$WORK/r" && mv "$WORK/r" memory/builds/tRun/README.md
git add -A >/dev/null && git commit -q -m "scope grew" --no-verify && git push -qf origin unit
out=$(drive --close tRun)
miss "$out" "authorization-reachable"

# ---- 4b: the id present at the pinned BASE is REMOVED and the run does NOT re-push. BASE carries
# ---- TOOL-tRun-1 because arm 4a pushed it, HEAD does not, so BASE is no longer a subset and this
# ---- run narrowed the scope it was authorized for.
grep -v "TOOL-tRun-1 " memory/builds/tRun/README.md > "$WORK/r" && mv "$WORK/r" memory/builds/tRun/README.md
git add -A >/dev/null && git commit -q -m "scope narrowed, unpushed" --no-verify
out=$(drive --close tRun)
hit "$out" "authorization-reachable"
# ---- ARM 5: the PROMPT-MODE seam. The driver records the mode from the blob at BASE and the leg
# ---- re-derives it from that same blob independently. This is the driver/leg seam for the new mode
# ---- bit, and without it two other specs name a left-shift gate that does not cover them.
git checkout -qf -B unit2 main
mk tPrompt "authorized-by: prompt"
git add -A >/dev/null && git commit -q -m "prompt-authorized build folder" --no-verify
git push -qf origin unit2
out=$(drive --preflight tPrompt --keepalive-id k2)
hit "$out" "preflight OK"
hit "$(cat memory/builds/tPrompt/RUN.md)" "mode: prompt"
git add -A >/dev/null && git commit -q -m runstate2 --no-verify && git push -qf origin unit2
out=$(leg)
same "arm 5: the leg's own re-derivation agrees with the recorded mode" "$out" ""

# ---- ARM 5b: the record CLAIMS a mode its own BASE does not grant. It breaks the RECORD, not the
# ---- anchor - and it has to, because `mode:` and `base:` are both PINNED ONCE: a re-preflight after
# ---- editing the README cannot produce the disagreement, since neither fact moves. Measured while
# ---- writing this arm, which is exactly the fixture-that-cannot-trigger-its-own-rule class.
sed -i 's/^mode: prompt$/mode: slug/' memory/builds/tPrompt/RUN.md
git add -A >/dev/null && git commit -q -m "forged mode" --no-verify && git push -qf origin unit2
hit "$(leg)" "a run-state file records an authorization mode the build README at its own recorded BASE does not declare"

FLOOR_ASSERTIONS=13
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
