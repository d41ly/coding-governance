#!/usr/bin/env bash
# adopt-unattended.sh — install the unattended-run kit's project-facing surface.
#
#   tools/unattended/adopt-unattended.sh            # render .claude/skills/unattended/SKILL.md
#   tools/unattended/adopt-unattended.sh --check    # verify the rendered Skill still matches the kit + conf
#
# Exit 0 = rendered / in sync · 1 = drift or a missing prerequisite · 2 = misconfigured.
#
# `--check` is the merge-bar arm. It renders to a temp file and DIFFS, so a hand-edited Skill reds
# instead of being quietly accepted. Both sides are CR-normalised, because a byte-comparing gate
# needs both halves: the `eol=lf` pin so the committed bytes are right, AND normalisation in the
# comparison so a Windows checkout does not report every line of an untouched file as drift.
#
# NO `fail()` HELPER, deliberately. `check-arms.py` discovers any tracked `*.sh` that defines one and
# calls `fail <n> "` as a GATE needing an armed sibling test, and an adopter is not a gate. The two
# existing adopters use plain `echo` + `exit` for the same reason; this is the third instance of a
# shape, not a new one.
set -u
MODE="${1-}"
case "$MODE" in
  ""|--check) ;;
  *) echo "usage: $0 [--check]"; exit 2 ;;
esac

# THE KIT DIR IS RESOLVED FIRST, BEFORE ANY `cd`. The walk below starts here, and the `cd "$ROOT"`
# further down re-anchors the cwd — which is precisely what used to make this derivation depend on
# how the adopter was INVOKED. See the strip note below.
KIT_DIR="$(cd "$(dirname "$0")" && pwd)"

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "unattended: not a git repo"; exit 2; }
ROOT="$(cd "$ROOT" && pwd)"

# WHICH TREE AM I ALLOWED TO TOUCH — asked FIRST, before anything else is read. The ordering is
# load-bearing: running this from a repo that does not own the kit used to reach the conf check
# first, whose message ("no .unattended.conf at the repo root") sends the operator to create a conf
# in the very repo the adopter must not adopt. Measured by the e2e's foreign-repo arm.
#
# THIS USED TO BE `KIT_REL=${KIT_DIR#"$ROOT"/}` AND THAT WAS A DEFECT, not a shortcut. The two
# operands are two spellings of one directory whenever the adopter is invoked by ABSOLUTE path:
# `ROOT` carries git's flavor (`/c/Users/…/Temp/x`) and `KIT_DIR` the caller's (`/tmp/x`), `/tmp`
# being an MSYS MOUNT POINT rather than a symlink, so the strip no-ops, `KIT_REL` comes out absolute,
# and the refusal below fires for a kit that is perfectly well inside the repo. Invoked RELATIVELY it
# worked, because the old `cd "$ROOT"` ran first and re-anchored `dirname "$0"` — so the bug was
# invisible to the documented invocation and visible to the e2e's two absolute-path arms. The old
# comment here claimed the shared `cd … && pwd` chain made both sides comparable; it does not, and
# claiming sufficiency is what kept this alive.
#
# So: NOTHING IS COMPARED AS A PATH STRING ANY MORE. Two different questions, two mechanisms.
#
# (1) WHAT PATH DO WE RENDER — a purely LOGICAL upward walk from the kit dir, building the relative
# path from basenames and stopping at the first `.git`. It compares nothing, so no pair of spellings
# can disagree. `-e` and not `-d`, because a linked worktree's `.git` is a FILE and this fleet nests
# worktrees inside the repository.
#
# THE WALK IS LOGICAL, NOT PHYSICAL, and that is the junction contract. `pwd` without `-P` keeps the
# path the caller traversed, so a kit dir that is a JUNCTION inside the adopting repo anchors to the
# ADOPTING repo — which is the install shape this fleet uses, and the codebase-map adopter's e2e
# scores a refusal of it as a FAILURE. Resolving physically would follow the link to the target and
# adopt the wrong tree, silently. Asking git instead is NOT an option and was measured: both
# `git rev-parse --show-prefix` after a `cd` and `git -C <junction> rev-parse --show-prefix` answer
# with the junction's TARGET.
KIT_ROOT=""; KIT_REL=""; _p="$KIT_DIR"
while : ; do
  _parent="$(dirname "$_p")"
  [ "$_parent" = "$_p" ] && break                     # filesystem root; no boundary found
  KIT_REL="$(basename "$_p")${KIT_REL:+/$KIT_REL}"
  if [ -e "$_parent/.git" ]; then KIT_ROOT="$_parent"; break; fi
  _p="$_parent"
done
if [ -z "$KIT_ROOT" ]; then
  echo "unattended: the kit at $KIT_DIR is not inside any git repository — refusing to touch anything."
  echo "  The walk up from the kit dir reached the filesystem root without finding a .git, so there"
  echo "  is no repo whose declarations this kit could install."
  exit 2
fi

# (2) IS THE KIT IN THE REPO WE ARE ADOPTING — repository IDENTITY, asked of git on BOTH sides so one
# speller answers both. `--path-format=absolute` is the load-bearing half, not decoration: bare
# `--git-common-dir` prints the RELATIVE `.git` from any toplevel, so two unrelated repositories both
# answer `.git` and compare EQUAL — the refusal would never fire — while a linked worktree answers an
# absolute path and would compare UNEQUAL to its own primary tree. Measured both ways on this fleet.
# `--absolute-git-dir` is NOT a substitute: in a linked worktree it names that worktree's private git
# dir, not the common one, so it would refuse the very install shape this fleet uses.
_kit_id="$(git -C "$KIT_ROOT" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)" || _kit_id=""
_root_id="$(git -C "$ROOT" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)" || _root_id=""
if [ -z "$_kit_id" ] || [ "$_kit_id" != "$_root_id" ]; then
  echo "unattended: the kit at $KIT_DIR belongs to another repository — refusing to touch either tree."
  echo "  You are standing in $ROOT. A kit outside the adopting repo would render a Skill whose"
  echo "  commands point at another checkout, and would install this repo's declarations into"
  echo "  somebody else's."
  exit 2
fi

# EVERY WRITE GOES TO $ROOT, THE OPERATOR'S TREE — never to $KIT_ROOT. The two are the same directory
# for an ordinary install and DIFFERENT working trees of one repository when the operator runs from a
# linked worktree, which the identity test above deliberately admits. `$KIT_ROOT` fed the walk and the
# comparison and has no further business here: writing there would put the rendered Skill and the
# committed protocol copy into a tree the operator is not standing in, at exit 0.
cd "$ROOT" || exit 2
# An UNSUPPORTED PREFIX. The kit path is interpolated into shell commands in the rendered Skill, so
# whitespace in it does not merely look wrong — it renders `bash my kit/unattended.sh --status`,
# which runs `bash my` with three arguments. Refuse rather than emit a Skill that misfires.
case "$KIT_REL" in
  *[[:space:]]*)
    echo "unattended: the kit path contains whitespace and is interpolated into shell commands: $KIT_REL"
    echo "  The rendered Skill would emit a command that word-splits. Install the kit at a path"
    echo "  with no spaces, or quote-harden the template first."
    exit 2 ;;
esac

TEMPLATE="$KIT_DIR/SKILL.template.md"
[ -f "$TEMPLATE" ] || { echo "unattended: SKILL.template.md is missing from the kit at $KIT_DIR"; exit 1; }

CONF="$ROOT/.unattended.conf"
[ -f "$CONF" ] || { echo "unattended: no .unattended.conf at the repo root — render it after adopting the project layer"; exit 1; }
# An interpolated key left UNSET keeps its own placeholder, so an undeclared value reds on the
# placeholder arm instead of rendering a clean sentence with a hole in it. Absence-of-placeholder is
# not presence-of-value, and "" made every such key invisible to the only check looking for it.
MEMORY_ROOT=memory; LANDER="{{LANDER}}"; KEEPALIVE_CREATE="{{KEEPALIVE_CREATE}}"
KEEPALIVE_DELETE="{{KEEPALIVE_DELETE}}"; KEEPALIVE_INTERVAL="{{KEEPALIVE_INTERVAL}}"
# TOOL-aPromptedMandate-5 - ANCHOR_SCOPE is the ONE interpolated key that must NOT keep its
# placeholder when undeclared. Every adopter shipped today declares it blank, which is legal and
# means the strict anchor; a placeholder there would red the placeholder arm for the majority case.
ANCHOR_SCOPE=""
# shellcheck disable=SC1090
. "$CONF"
# The EFFECTIVE scope, not the raw declaration. Absent, blank and misspelled all keep the strict
# anchor - the driver's own value guard falls through exactly this way - and the Skill has to state
# what the run will DO rather than what the file happens to say. Deriving it here also means the
# rendered sentence can never be a hole: there is no value of the key that produces an empty cell.
case "$ANCHOR_SCOPE" in
  published) ANCHOR_EFFECTIVE=published ;;
  *)         ANCHOR_EFFECTIVE=default-branch ;;
esac

SKILL_DIR="$ROOT/.claude/skills/unattended"
SKILL_OUT="$SKILL_DIR/SKILL.md"
PROTO_SHIP="$KIT_DIR/PROTOCOL.template.md"
PROTO_REL="$MEMORY_ROOT/guides/UNATTENDED-PROTOCOL.md"
PROTO_OUT="$ROOT/$PROTO_REL"
# TOOL-dScriptedRepeat-2 - the THIRD artifact. COPIED rather than rendered, for the reason the
# protocol is: it carries no placeholder, so a render step would be a second spelling of `cat`.
PBT_SHIP="$KIT_DIR/PLAYBOOK-TEMPLATE.template.md"
PBT_REL="$MEMORY_ROOT/guides/PLAYBOOK-TEMPLATE.md"
PBT_OUT="$ROOT/$PBT_REL"

# NON-ZERO on a failed substitution. A conf value carrying the s||| delimiter makes sed exit 1 while
# the trailing `tr` still exits 0, so the adopter wrote a ZERO-BYTE Skill and --check then diffed
# empty against empty and certified it. pipefail plus the emptiness refusal below turn that silent
# truncation into a loud one. Escaping the values themselves is tracked separately.
render() { # -> stdout; LF only (the render is pinned eol=lf in .gitattributes)
  # NO `sed`. Conf values are FREE PROSE, and unescaped they landed in `s|…|…|` where a `|` closes
  # the delimiter (sed exits 1, the trailing `tr` exits 0, so a ZERO-BYTE Skill was written and
  # `--check` certified it) and an `&` re-inserts the whole match. Two attempts to escape around that
  # were wrong — one replaced `| & \` with a bare `&` and corrupted values worse than no escaping —
  # because the count of backslash-consuming layers between the source and the regex engine was not
  # knowable. So the engine that needs them is gone.
  #
  # THE REPLACEMENT MUST BE QUOTED. Bash 5.1 gave pattern substitution a sed-like `&` meaning "the
  # matched text"; quoting any part of the replacement inhibits it. Measured on 5.3.9 with V='a&b':
  # unquoted `${t//\{\{K\}\}/$V}` yields `a{{K}}b`, quoted yields `a&b`. A backslash is likewise
  # eaten unquoted and preserved quoted. The quotes are the fix, not decoration.
  local out
  # The `X` sentinel exists because `$( )` strips ALL trailing newlines: without it a template
  # ending in two blank lines renders with one, and the parity diff blames the author for it. `cat`
  # gets its own subshell and an explicit `exit 1`, because a substitution reports the LAST command's
  # status — printf's, always 0 — so the guard below was unreachable without it.
  out=$( cat "$TEMPLATE" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  out=${out//\{\{MEMORY_ROOT\}\}/"$MEMORY_ROOT"}
  out=${out//\{\{LANDER\}\}/"$LANDER"}
  out=${out//\{\{KEEPALIVE_CREATE\}\}/"$KEEPALIVE_CREATE"}
  out=${out//\{\{KEEPALIVE_DELETE\}\}/"$KEEPALIVE_DELETE"}
  out=${out//\{\{KEEPALIVE_INTERVAL\}\}/"$KEEPALIVE_INTERVAL"}
  out=${out//\{\{ANCHOR_SCOPE\}\}/"$ANCHOR_EFFECTIVE"}
  printf '%s' "$out"
}

if [ "$MODE" = "--check" ]; then
  # An UNRENDERED Skill is a named refusal, never a skip. "The file is not there" and "the file
  # matches" are different answers, and only one of them means the kit is installed.
  [ -f "$SKILL_OUT" ] || { echo "unattended: $SKILL_OUT is not rendered — run $0"; exit 1; }
  TMP=$(mktemp) || exit 2
  trap 'rm -f "$TMP"' EXIT
  render > "$TMP" || { echo "unattended: the render FAILED — the template could not be read; refusing to compare"; exit 1; }
  [ -s "$TMP" ] || { echo "unattended: the render produced an EMPTY file — comparing it to an equally empty Skill is the green-by-absence shape this kit refuses"; exit 1; }
  if ! diff -q <(tr -d '\r' < "$SKILL_OUT") "$TMP" >/dev/null 2>&1; then
    echo "unattended: $SKILL_OUT is out of sync with SKILL.template.md + .unattended.conf"
    echo "  re-render with: $0"
    diff <(tr -d '\r' < "$SKILL_OUT") "$TMP" | head -20 | sed 's/^/    /'
    exit 1
  fi
  # A surviving placeholder means the conf declared nothing for it, which renders a Skill telling the
  # agent to call `{{KEEPALIVE_CREATE}}`. In sync with the template and useless.
  if grep -qE '\{\{[A-Z_]+\}\}' "$SKILL_OUT"; then
    echo "unattended: $SKILL_OUT still carries an unfilled placeholder — .unattended.conf declares no value for it"
    grep -nE '\{\{[A-Z_]+\}\}' "$SKILL_OUT" | head -5 | sed 's/^/    /'
    exit 1
  fi
  # The adopter installs THREE artifacts, so --check verifies three. Checking only the one it renders
  # reported "in sync" over a protocol half that had been deleted or hand-edited — and check 10 of
  # the gate fails HARD when that half is missing, so the drift would surface as an unexplained gate
  # failure somewhere else entirely. The count is stated here and in the arm below it; both move
  # together or neither does.
  if [ ! -f "$PROTO_OUT" ]; then
    echo "unattended: $PROTO_REL is missing — run $0 to install the protocol's live half"; exit 1
  fi
  if ! diff -q <(tr -d '' < "$PROTO_OUT") "$PROTO_SHIP" >/dev/null 2>&1; then
    echo "unattended: $PROTO_REL has drifted from the shipped protocol; re-run $0"; exit 1
  fi
  # TOOL-dScriptedRepeat-2 - the third artifact, with its own TWO refusals. NOT-INSTALLED and
  # DRIFTED are separate messages: one sends the reader to run the adopter and the other to read a
  # diff, and one message would send half of them to the wrong place.
  if [ ! -f "$PBT_OUT" ]; then
    echo "unattended: $PBT_REL is missing — run $0 to install the playbook template"; exit 1
  fi
  if ! diff -q <(tr -d '' < "$PBT_OUT") "$PBT_SHIP" >/dev/null 2>&1; then
    echo "unattended: $PBT_REL has drifted from the shipped playbook template; re-run $0"; exit 1
  fi
  echo "unattended: in sync (skill rendered from template + .unattended.conf)"
  exit 0
fi

# THE PROTOCOL PAIR. check 10 compares the SHIPPED protocol against the installed copy, and fails
# hard when either half is missing — "a parity check with one file is a check that cannot fail".
# Nothing installed the live half, so that check was UNPASSABLE in every adopter: the kit shipped
# a gate its own adopter could not satisfy. Copied, not rendered — the protocol carries no
# placeholder, so a render step would be a second spelling of `cat`.
mkdir -p "$ROOT/$MEMORY_ROOT/guides"
if [ ! -f "$PROTO_OUT" ] || ! diff -q <(tr -d '' < "$PROTO_OUT") "$PROTO_SHIP" >/dev/null 2>&1; then
  tr -d '' < "$PROTO_SHIP" > "$PROTO_OUT"
  echo "unattended: installed $PROTO_REL"
fi
# TOOL-dScriptedRepeat-2 - the playbook template, the same shape as the protocol above it.
if [ ! -f "$PBT_OUT" ] || ! diff -q <(tr -d '' < "$PBT_OUT") "$PBT_SHIP" >/dev/null 2>&1; then
  tr -d '' < "$PBT_SHIP" > "$PBT_OUT"
  echo "unattended: installed $PBT_REL"
fi
mkdir -p "$SKILL_DIR"
TMPW=$(mktemp) || exit 2
render > "$TMPW" || { rm -f "$TMPW"; echo "unattended: the render FAILED — the template could not be read; the Skill is unchanged"; exit 1; }
# Write through a temp file and refuse an EMPTY one. Redirecting straight into the target truncated it
# to zero bytes the instant sed failed, and then reported success.
[ -s "$TMPW" ] || { rm -f "$TMPW"; echo "unattended: the render produced an EMPTY file — refusing to install it over the Skill"; exit 1; }
mv "$TMPW" "$SKILL_OUT"
echo "unattended: rendered $SKILL_OUT"
cat <<EOF
unattended: next
  1. Pin the render LF in .gitattributes:  .claude/skills/unattended/SKILL.md text eol=lf
     (without it a checkout can land CRLF while git status stays clean, and the --check leg
      reports every line of an untouched file as drift)
  2. git add the render and the pin, then run: $0 --check
  3. Wire '$0 --check' and 'bash $KIT_REL/check-unattended.sh' into your gate manifest.
EOF
