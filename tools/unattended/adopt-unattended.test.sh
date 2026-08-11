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
     "$HERE/check-unattended.sh" "$HERE/PROTOCOL.template.md" "$1/tools/unattended/"
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
hit "$(cat "$A/memory/guides/UNATTENDED-PROTOCOL.md")" "standing mandate"
hit "$(cat "$A/.claude/skills/unattended/SKILL.md")" "TheCreateCall"
hit "$(cat "$A/.claude/skills/unattended/SKILL.md")" "bash tools/land.sh"
hit "$(cat "$A/.claude/skills/unattended/SKILL.md")" "bash tools/unattended/unattended.sh --preflight"
same "arm 1 left no placeholder" \
  "$(grep -cE '\{\{[A-Z_]+\}\}' "$A/.claude/skills/unattended/SKILL.md" || true)" "0"
( cd "$A" && bash tools/unattended/adopt-unattended.sh --check >/dev/null 2>&1 )
same "arm 1 --check agrees with what --render just wrote" "$?" "0"

# ---- ARM 2: a FOREIGN repo. The kit lives in host A; the caller runs it from host B. Nothing may be
# ---- written into EITHER tree — not the caller's, and not the kit owner's.
B="$TMP/other"; mkdir -p "$B"
( cd "$B" && git init -q -b main . && git config user.email t@t.test && git config user.name t )
rm -rf "$A/.claude"
out=$( cd "$B" && bash "$A/tools/unattended/adopt-unattended.sh" 2>&1 ); rc=$?
hit "$out" "is not inside"
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

# ---- ARM 4: through a JUNCTION inside the adopting repo. This is the install shape this fleet uses,
# ---- and the codebase-map adopter's e2e scores a REFUSAL of it as a failure — so the assertion is
# ---- that it ADOPTS, anchored on the adopting repo, and writes nothing into the link target.
# ---- The walk must stay LOGICAL: resolving the link physically would adopt the target's tree.
D="$TMP/linkhost"; seed "$D"
E="$TMP/linktarget"; mkdir -p "$E"
cp -r "$D/tools/unattended" "$E/unattended"
rm -rf "$D/tools/unattended"
if ln -s "$E/unattended" "$D/tools/unattended" 2>/dev/null && [ -L "$D/tools/unattended" ]; then
  out=$( cd "$D" && bash tools/unattended/adopt-unattended.sh 2>&1 ); rc=$?
  same "arm 4 adopts through a junction" "$rc" "0"
  present "$D/.claude/skills/unattended/SKILL.md" "arm 4 wrote into the ADOPTING repo"
  absent "$E/.claude" "arm 4 wrote into the LINK TARGET"
  hit "$(cat "$D/.claude/skills/unattended/SKILL.md")" "bash tools/unattended/unattended.sh --preflight"
else
  echo "SKIP arm 4 (junction): this host cannot create a symlink, so a copy would score a refusal"
  echo "     as success. Run this suite on a node with the privilege to cover the junction shape."
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
