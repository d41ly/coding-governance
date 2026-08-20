#!/usr/bin/env bash
# End-to-end for adopt-unattended.sh — GATED ON EFFECTS, not on exit codes.
#
#   bash tools/unattended/adopt-unattended.test.sh    # "PASS (…assertions)" + exit 0 = good
#
# WHY EFFECTS. The adopter WRITES. An exit-code test passes on a script that refused correctly and
# on one that wrote into the wrong tree and then exited 2 for an unrelated reason. The charter
# records why this matters here: a Tier-2 review found four of seven defects, including a blocker,
# in the one file no leg executed — the codebase-map adopter. So every arm below asserts what is on
# disk in BOTH trees afterwards, and the refusal arms assert that nothing was written at all.
#
# The junction arm is a LOUD SKIP when the host cannot create a link, never a silent pass: on a
# Windows node without the privilege, `ln -s` degrades to a copy and would score a refusal as
# success.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
st=0; n=0
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }
absent() { n=$((n+1)); [ ! -e "$1" ] || { echo "FAIL $2: $1 exists and should not"; st=1; }; }
present() { n=$((n+1)); [ -e "$1" ] || { echo "FAIL $2: $1 is missing"; st=1; }; }

seed() { # dir  -> a git repo carrying the kit and a conf
  mkdir -p "$1/tools/unattended"
  ( cd "$1" && git init -q -b main . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false )
  cp "$HERE/SKILL.template.md" "$HERE/adopt-unattended.sh" "$HERE/unattended.sh" \
     "$HERE/check-unattended.sh" "$HERE/PROTOCOL.template.md" "$HERE/PLAYBOOK-TEMPLATE.template.md" "$1/tools/unattended/"
  cat > "$1/.unattended.conf" <<'EOF'
MEMORY_ROOT=memory
LANDER="bash tools/land.sh"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
WIRING_CHECK="true"
KEEPALIVE_CREATE="TheCreateCall"
KEEPALIVE_DELETE="TheDeleteCall"
KEEPALIVE_INTERVAL="every 10 minutes"
CORE_FLOOR="6:6"
KICKOFF_ENGINE=""
KICKOFF_EXITS=""
PHASES_EXTRA=""
DOD_EXTRA=""
EOF
}

# ---- ARM 1: the ordinary adopt. Asserted on the CONTENT of what was written, because "a file
# ---- appeared" is satisfied by a render that interpolated nothing.
A="$TMP/host"; seed "$A"
out=$( cd "$A" && bash tools/unattended/adopt-unattended.sh 2>&1 )
present "$A/.claude/skills/unattended/SKILL.md" "arm 1 rendered the Skill"
# check 10 of the gate compares the SHIPPED protocol against the installed copy and fails hard
# when either half is missing, so before this the kit shipped a gate no adopter could satisfy.
present "$A/memory/guides/UNATTENDED-PROTOCOL.md" "arm 1 installed the protocol's live half"
hit "$(cat "$A/memory/guides/UNATTENDED-PROTOCOL.md")" "The run is authorized by the **build folder itself**"
# TOOL-dScriptedRepeat-2 - the THIRD artifact. Asserted on CONTENT for the reason arm 1 states
# about the other two: a file appearing is satisfied by a copy that carried nothing.
present "$A/memory/guides/PLAYBOOK-TEMPLATE.md" "arm 1 installed the playbook template"
hit "$(cat "$A/memory/guides/PLAYBOOK-TEMPLATE.md")" "PROHIBITED OUTPUT unless it is a tracked"
hit "$(cat "$A/.claude/skills/unattended/SKILL.md")" "TheCreateCall"
hit "$(cat "$A/.claude/skills/unattended/SKILL.md")" "bash tools/land.sh"
hit "$(cat "$A/.claude/skills/unattended/SKILL.md")" "bash tools/unattended/unattended.sh --preflight"
same "arm 1 left no placeholder" \
  "$(grep -cE '\{\{[A-Z_]+\}\}' "$A/.claude/skills/unattended/SKILL.md" || true)" "0"
( cd "$A" && bash tools/unattended/adopt-unattended.sh --check >/dev/null 2>&1 )
same "arm 1 --check agrees with what --render just wrote" "$?" "0"

# ---- ARM 1b: HOSTILE CONF VALUES, round-tripped.
# ---- Conf values are free prose. The previous `sed` render interpolated them unescaped into
# ---- `s|…|…|`, where a `|` closed the delimiter — sed exited 1, the trailing `tr` exited 0, so a
# ---- ZERO-BYTE Skill was written and `--check` then diffed it clean against an equally empty
# ---- render. An `&` re-inserted the whole match instead. This arm is a ROUND TRIP, not a
# ---- non-empty check: the values must come back byte-for-byte, which is the only assertion that
# ---- distinguishes a correct render from a plausible one.
H="$TMP/hostile"; seed "$H"
# Written with a QUOTED HEREDOC, never `sed`: these values carry `|`, which is the delimiter every
# `s|…|…|` in this kit used, so editing them in with sed reproduces the very defect the fixture
# exists to catch. It did, on the first attempt at writing this arm.
grep -v -e '^LANDER=' -e '^KEEPALIVE_INTERVAL=' "$H/.unattended.conf" > "$H/.conf.tmp"
cat >> "$H/.conf.tmp" <<'HOSTILEEOF'
LANDER="bash tools/land.sh | tee log & echo done \\ok"
KEEPALIVE_INTERVAL="every 10 min | offset 3 & then \\wait"
HOSTILEEOF
mv "$H/.conf.tmp" "$H/.unattended.conf"
out=$(cd "$H" && bash tools/unattended/adopt-unattended.sh 2>&1); rc=$?
same "a hostile conf still adopts" "$rc" "0"
SK="$H/.claude/skills/unattended/SKILL.md"
present "$SK" "the Skill is written for a hostile conf"
hit "$(cat "$SK")" 'bash tools/land.sh | tee log & echo done \ok'
hit "$(cat "$SK")" 'every 10 min | offset 3 & then \wait'
# NEGATIVE control: a render that silently drops a substitution leaves the token standing, and would
# otherwise satisfy every assertion above by writing nothing useful.
n=$((n+1)); grep -qF '{{LANDER}}' "$SK" && { echo "FAIL a dropped substitution left {{LANDER}} standing"; st=1; }
n=$((n+1)); grep -qF '{{KEEPALIVE_INTERVAL}}' "$SK" && { echo "FAIL a dropped substitution left {{KEEPALIVE_INTERVAL}} standing"; st=1; }
# And the gate agrees, rather than comparing one empty file to another.
out=$(cd "$H" && bash tools/unattended/adopt-unattended.sh --check 2>&1); rc=$?
same "--check agrees on a hostile conf" "$rc" "0"

# ---- ARM 2: a FOREIGN repo. The kit lives in host A; the caller runs it from host B. Nothing may be
# ---- written into EITHER tree — not the caller's, and not the kit owner's.
B="$TMP/other"; mkdir -p "$B"
( cd "$B" && git init -q -b main . && git config user.email t@t.test && git config user.name t )
rm -rf "$A/.claude"
out=$( cd "$B" && bash "$A/tools/unattended/adopt-unattended.sh" 2>&1 ); rc=$?
# RE-KEYED. This asserted "is not inside", which was the PATH-STRIP refusal — and that refusal fired
# for every repo, including legitimate ones, whenever the adopter was invoked by absolute path. So
# this arm was green for the wrong reason and could not tell a foreign repo from any repo at all.
# The predicate is now repository IDENTITY, and this is its first real exercise.
hit "$out" "belongs to another repository"
same "arm 2 refuses" "$rc" "2"
absent "$B/.claude/skills/unattended/SKILL.md" "arm 2 wrote into the CALLING repo"
absent "$A/.claude/skills/unattended/SKILL.md" "arm 2 wrote into the KIT OWNER's repo"

# ---- ARM 3: an UNSUPPORTED PREFIX — whitespace in the kit path. The path is interpolated into shell
# ---- commands in the rendered Skill, so this is not cosmetic: the render would emit a command that
# ---- word-splits. Refusing beats emitting a Skill that misfires at the first verb.
C="$TMP/spaced"; seed "$C"
mkdir -p "$C/my tools" && cp -r "$C/tools/unattended" "$C/my tools/unattended"
out=$( cd "$C" && bash "$C/my tools/unattended/adopt-unattended.sh" 2>&1 ); rc=$?
hit "$out" "the kit path contains whitespace and is interpolated into shell commands"
same "arm 3 refuses" "$rc" "2"
absent "$C/.claude/skills/unattended/SKILL.md" "arm 3 wrote despite refusing"

# ---- ARM 3b: TWO SPELLINGS of one directory, invoked by ABSOLUTE path. This is the arm that would
# ---- have caught the path-strip defect, and it did not exist. The adopter used to derive KIT_REL by
# ---- stripping $ROOT off $KIT_DIR; both are the same directory but git and the caller can spell it
# ---- differently, so the strip no-opped and the not-inside guard fired for a kit that WAS inside.
# ----
# ---- IT CONSTRUCTS THE SECOND SPELLING ON PURPOSE and asserts the two really differ BEFORE asserting
# ---- the adoption. Relying on the harness's own mktemp landing under a mount point is not a
# ---- construction: on a host where /tmp is an ordinary directory the spellings agree, the arm would
# ---- pass with the fix reverted, and that is the fixture-passes-by-finding-nothing class.
# ---- ABSOLUTE invocation is load-bearing: with a relative $0 the old code re-anchored the cwd and
# ---- the strip succeeded, which is why the defect was invisible to the documented usage.
F="$TMP/spell"; seed "$F"
# The two spellings usually already EXIST and need no link: under MSYS `pwd` reports the caller's
# mount-point flavor (/tmp/...) while git reports the Windows one (C:/Users/.../Temp/...), for one
# directory. Prefer that; fall back to a symlink; skip loudly if neither yields a divergence.
F_ALT=""
if [ "$(cd "$F" && pwd)" != "$(cd "$F" && git rev-parse --show-toplevel)" ]; then
  F_ALT="$F"
elif ln -s "$F" "$TMP/spell-alt" 2>/dev/null && [ -L "$TMP/spell-alt" ]      && [ "$(cd "$TMP/spell-alt" && pwd)" != "$(cd "$TMP/spell-alt" && git rev-parse --show-toplevel)" ]; then
  F_ALT="$TMP/spell-alt"
fi
if [ -n "$F_ALT" ]; then
  # LIVENESS, asserted rather than assumed: the arm is only meaningful while the two spellings differ.
  n=$((n+1))
  [ "$(cd "$F_ALT" && pwd)" != "$(cd "$F_ALT" && git rev-parse --show-toplevel)" ]     || { echo "FAIL arm 3b fixture is inert: the two spellings agree, so it would pass with the fix reverted"; st=1; }
  out=$( cd "$F_ALT" && bash "$F_ALT/tools/unattended/adopt-unattended.sh" 2>&1 ); rc=$?
  same "arm 3b adopts despite two spellings" "$rc" "0"
  present "$F/.claude/skills/unattended/SKILL.md" "arm 3b wrote into the adopting repo"
  hit "$(cat "$F/.claude/skills/unattended/SKILL.md")" "bash tools/unattended/unattended.sh --preflight"
else
  echo "SKIP arm 3b (two spellings): this host spells one directory one way, so the arm would pass"
  echo "     with the fix reverted and proves nothing. Needs a node where pwd and git disagree."
fi

# ---- ARM 4: through a JUNCTION inside the adopting repo. This is the install shape this fleet uses,
# ---- and the codebase-map adopter's e2e scores a REFUSAL of it as a failure — so the assertion is
# ---- that it ADOPTS, anchored on the adopting repo, and writes nothing into the link target.
# ---- The walk must stay LOGICAL: resolving the link physically would adopt the target's tree.
D="$TMP/linkhost"; seed "$D"
E="$TMP/linktarget"; mkdir -p "$E"
cp -r "$D/tools/unattended" "$E/unattended"
rm -rf "$D/tools/unattended"
# ---- THE DISCRIMINATOR IS `[ -L ]` AFTER CREATION, NEVER `ln -s`'s EXIT CODE. Measured on this
# ---- fleet: `ln -s` exits 0 here and produces a real directory COPY (`-L` false, `-d` true, entries
# ---- duplicated). So an `if ln -s …; then` structure always takes the first branch and a junction
# ---- fallback behind it would be unreachable — and the copy left behind also makes the junction
# ---- creation fail, because the path is no longer empty. Hence: try, test, clean up, try the other.
link_ok=0
if ln -s "$E/unattended" "$D/tools/unattended" 2>/dev/null && [ -L "$D/tools/unattended" ]; then
  link_ok=1
else
  rm -rf "$D/tools/unattended"                       # the ln -s copy, if that is what we got
  if command -v powershell >/dev/null 2>&1 && \
     powershell -NoProfile -Command "New-Item -ItemType Junction -Path '$(cygpath -w "$D/tools/unattended" 2>/dev/null || echo "$D/tools/unattended")' -Target '$(cygpath -w "$E/unattended" 2>/dev/null || echo "$E/unattended")' -ErrorAction Stop" >/dev/null 2>&1 \
     && [ -L "$D/tools/unattended" ]; then
    link_ok=1
  fi
fi
if [ "$link_ok" = 1 ]; then
  out=$( cd "$D" && bash tools/unattended/adopt-unattended.sh 2>&1 ); rc=$?
  same "arm 4 adopts through a junction" "$rc" "0"
  present "$D/.claude/skills/unattended/SKILL.md" "arm 4 wrote into the ADOPTING repo"
  absent "$E/.claude" "arm 4 wrote into the LINK TARGET"
  hit "$(cat "$D/.claude/skills/unattended/SKILL.md")" "bash tools/unattended/unattended.sh --preflight"
else
  echo "SKIP arm 4 (junction): neither a symlink nor a junction on this host yields -L true, and a"
  echo "     directory COPY would score a refusal as success. Run this suite on a node that can link."
fi

# ---- ARM 5: a half-adoption is not an adoption. With the conf absent the adopter refuses BEFORE it
# ---- writes, so an operator never gets a Skill rendered against declarations that do not exist.
F="$TMP/noconf"; seed "$F"; rm -f "$F/.unattended.conf"
out=$( cd "$F" && bash tools/unattended/adopt-unattended.sh 2>&1 ); rc=$?
hit "$out" "no .unattended.conf at the repo root"
same "arm 5 refuses" "$rc" "1"
absent "$F/.claude/skills/unattended/SKILL.md" "arm 5 left a half-stamped adoption"

# ---- ARM 6: the kit's own template missing. Same shape from the other side, and it is the arm that
# ---- keeps a broken INSTALL from reading as a repo problem.
G="$TMP/notemplate"; seed "$G"; rm -f "$G/tools/unattended/SKILL.template.md"
out=$( cd "$G" && bash tools/unattended/adopt-unattended.sh 2>&1 ); rc=$?
hit "$out" "SKILL.template.md is missing from the kit"
same "arm 6 refuses" "$rc" "1"
absent "$G/.claude/skills/unattended/SKILL.md" "arm 6 wrote despite a missing template"

[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
