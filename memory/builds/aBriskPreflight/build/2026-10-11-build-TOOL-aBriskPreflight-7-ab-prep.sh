#!/usr/bin/env bash
# ab-prep.sh <arm-dir> <code-sha> <tree-sha>
# A throwaway clone for one A/B arm of a whole preflight. The memory tree is <tree-sha> (the run's tip),
# the product code is <code-sha>'s (BASE for the old arm, the tip for the new one), and a fixture build
# folder `aTimedFixture` is committed on top as the only commit the branch carries past local main.
# origin is the local bare mirror, fetch AND push, so a claim push never reaches GitHub.
set -u
arm=$1; code=$2; tree=$3
SRC=C:/projects/coding-governance
R="$TEMP/bp/R.git"
rm -rf "$arm"
git clone -q --local --no-checkout "$SRC" "$arm" || exit 2
cd "$arm" || exit 2
git remote set-url origin "$R"
git fetch -q origin '+refs/heads/*:refs/remotes/origin/*' || exit 2
git remote set-head origin main >/dev/null
git config core.hooksPath .githooks
git config merge.rows.driver 'bash tools/memory-tree/merge-rows.sh %O %A %B %P'
git config merge.ours.driver true
git config user.name ab; git config user.email ab@invalid
git checkout -q -b fixture "$tree" || exit 2
# the installed /session-kickoff engine is a junction to the PRIMARY checkout, so the skill arm compares
# against that tree; both arms carry its copy so neither reds on an engine the build does not touch
inst="$HOME/.claude/skills/session-kickoff"
for f in SKILL.md MANIFEST-TEMPLATE.md manifest-check.sh; do cp "$inst/$f" "skills/session-kickoff/$f"; done
git add skills/session-kickoff && git commit -q -m "arm engine as installed" --no-verify || true
# the product code the arm runs: every path the build touches, at <code-sha>
paths=".githooks tools/check-wiring.sh tools/unattended .unattended.conf"
if [ "$code" != "$tree" ]; then
  git checkout -q "$code" -- $paths && git commit -q -m "arm code at $code" --no-verify || true
fi
# local main = everything but the fixture, so the carried-branch check sees only the fixture folder
git branch -f main HEAD
mkdir -p memory/builds/aTimedFixture/prompts
F=memory/builds/aTimedFixture
sed 's/aBriskPreflight/aTimedFixture/g' memory/builds/aBriskPreflight/README.md \
  | sed '/^authorized-by: prompt$/a status: INPROGRESS' \
  | sed '/TOOL-aTimedFixture-10`/d' \
  | awk '/^<!-- gen:build-index -->/{print; print "<!-- /gen:build-index -->"; skip=1; next} skip&&/^<!-- \/gen:build-edges -->/{skip=0; next} !skip' > "$F/README.md"
sed 's/aBriskPreflight/aTimedFixture/g' memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md \
  > "$F/prompts/2026-10-11-prompt-TOOL-aTimedFixture-1-brief.md"
git add "$F" && python tools/memory-tree/gen_build_index.py --write >/dev/null 2>&1
git add "$F"
git commit -q -m "records(aTimedFixture): the A/B fixture build" --no-verify -- "$F" || exit 2
# the generator also re-rendered views outside the folder; the arm starts from a clean tree
git checkout -q -- . && git clean -fdq
[ -z "$(git status --porcelain)" ] || { echo "ab-prep: the arm tree is not clean"; git status --short | head; exit 2; }
git -C "$R" update-ref -d refs/gov/runs/aTimedFixture 2>/dev/null
echo "prepared $arm · fixture $(git rev-parse --short HEAD) · main $(git rev-parse --short main) · code $code"
