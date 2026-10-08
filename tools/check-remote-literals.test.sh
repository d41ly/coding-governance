#!/usr/bin/env bash
# check-remote-literals.test.sh — self-test for <prefix>/check-remote-literals.sh (TOOL-dLadderedRemote-3).
#
#   bash <prefix>/check-remote-literals.test.sh
#
# Exit 0 = every arm held · 1 = an arm failed · 2 = the harness could not set up.
#
# EVERY ARM ASSERTS A MESSAGE, never an exit code alone: a planted hit, an empty population and a
# refusal to derive the tool root all exit non-zero, and an arm reading only `$?` cannot tell them
# apart. Each RED arm plants ONE shape in a clean scratch repo and asserts the gate names THAT file and
# line, so deleting one pattern from the gate reds exactly the arm for its shape. Each GREEN arm plants
# the same bytes where the population or the comment rule must leave them alone.
#
# The planted remote name is assembled from two halves, so this file, like the gate, does not spell
# what it bans — though as a `*.test.sh` it sits outside the population either way.
#
# NOTHING HERE TOUCHES THE REAL TREE. The gate `cd`s to its own git toplevel, so every arm runs a
# copy of it from inside the scratch repo it was built for.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "remote-literals.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture path below is spelled through it (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"
GATE_SRC="$HERE/check-remote-literals.sh"
[ -f "$GATE_SRC" ] || { echo "remote-literals.test: no gate at $GATE_SRC"; exit 2; }

FLOOR_ASSERTIONS=19
PASS=0
FAIL=0
ok()  { PASS=$((PASS+1)); }
bad() { FAIL=$((FAIL+1)); echo "  FAIL: $1"; }

TMPROOT=$(mktemp -d) || exit 2
trap 'rm -rf "$TMPROOT"' EXIT

# arm <label> <want-rc> <needle> -- <cmd...>
arm() {
  local label="$1" want="$2" needle="$3"; shift 4
  local out rc
  out=$("$@" 2>&1); rc=$?
  if [ "$rc" -ne "$want" ]; then
    bad "$label — wanted rc=$want got $rc: $(printf '%s' "$out" | head -3)"; return
  fi
  case "$out" in *"$needle"*) ok ;; *) bad "$label — rc was right but the message was not: $(printf '%s' "$out" | head -3)" ;; esac
}

# mkrepo <dir> — a committed repo carrying the gate at this suite's own prefix and one clean file, so
# the population is never empty unless an arm empties it on purpose.
mkrepo() {
  local d="$1"
  mkdir -p "$d/${PFX}kit"
  ( cd "$d" && git init -q && git config core.autocrlf false \
      && git config user.email t@t && git config user.name t ) || return 1
  cp "$GATE_SRC" "$d/${PFX}check-remote-literals.sh"
  printf 'echo clean\n' > "$d/${PFX}kit/clean.sh"
  ( cd "$d" && git add -A && git commit -qm base ) || return 1
}
# plant <dir> <relpath> <line> — write one line into a tracked file of the scratch repo
plant() {
  mkdir -p "$(dirname "$1/$2")"
  printf '%s\n' "$3" > "$1/$2"
  ( cd "$1" && git add -A ) || return 1
}
gate() { ( cd "$1" && bash "${PFX}check-remote-literals.sh" "${@:2}" ); }

N="ori""gin"
# The tables are written to scratch FILES and the loops read those, never a heredoc: a loop fed by a
# heredoc whose body holds a command substitution is the shell-hygiene leg's class.
RED_TABLE="$TMPROOT/red.tsv"; GREEN_TABLE="$TMPROOT/green.tsv"
{
  printf '%s\n' "tracking ref|${PFX}kit/a.sh|d=\$(git symbolic-ref --short refs/remotes/$N/HEAD)"
  printf '%s\n' "short ref|${PFX}kit/b.py|    tip = read(f\"$N/{branch}\")"
  printf '%s\n' "short ref, shell interpolation|${PFX}kit/c.sh|git merge-base \"$N/\$DEF\" HEAD"
  printf '%s\n' "short ref, a named branch|${PFX}kit/d.js|const base = a.base || \"$N/main\""
  printf '%s\n' "default after or|${PFX}kit/e.py|    remote = (_rn.stdout.strip() or \"$N\")"
  printf '%s\n' "default after :-|${PFX}kit/f.sh|r=\${GOV_REMOTE:-$N}"
  printf '%s\n' "remedy|${PFX}kit/g.py|    raise Refusal(\"run git remote set-head $N -a\")"
  printf '%s\n' "a shipped git hook|.githooks/pre-commit|def=\$(git symbolic-ref --short refs/remotes/$N/HEAD)"
} > "$RED_TABLE"
{
  printf '%s\n' "a *.test.sh file|${PFX}kit/x.test.sh|git update-ref refs/remotes/$N/main HEAD"
  printf '%s\n' "a selftest path|${PFX}kit/selftest.py|run(\"git\", \"update-ref\", \"refs/remotes/$N/main\", tip)"
  printf '%s\n' "a test_*.py file|${PFX}kit/test_x.py|run(\"git\", \"update-ref\", \"refs/remotes/$N/main\", tip)"
  printf '%s\n' "a fixtures/ directory|${PFX}kit/fixtures/repo.sh|git symbolic-ref refs/remotes/$N/HEAD refs/remotes/$N/main"
  printf '%s\n' "a # comment|${PFX}kit/h.sh|  # this read refs/remotes/$N/HEAD before TOOL-dLadderedRemote-2"
  printf '%s\n' "a // comment|${PFX}kit/i.js|// the default used to be $N/main"
  printf '%s\n' "a Markdown file|${PFX}kit/README.md|run git remote set-head $N -a"
  printf '%s\n' "a name merely containing the word|${PFX}kit/j.py|    origins = rec.get(\"${N}al_${N}s\")"
} > "$GREEN_TABLE"
# ---- RED: one shape per arm ------------------------------------------------------------------------
k=0
while IFS='|' read -r shape rel line; do
  [ -n "$shape" ] || continue
  k=$((k+1)); d="$TMPROOT/red$k"
  mkrepo "$d" || { echo "remote-literals.test: could not build $d"; exit 2; }
  plant "$d" "$rel" "$line" || exit 2
  arm "RED $shape is named" 1 "$rel:1:" -- gate "$d"
  # FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
  if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${FAIL:-0}" = 0 ] && echo "PASS (${PASS:-1} assertions)" || echo "FAIL (${PASS:-1} assertions)"; [ "${FAIL:-0}" = 0 ] && exit 0; exit 1; fi
done < "$RED_TABLE"
[ "$k" = 8 ] || bad "the RED table read as $k rows, not 8"

# ---- GREEN: the same bytes where they must not be named --------------------------------------------
k=0
while IFS='|' read -r what rel line; do
  [ -n "$what" ] || continue
  k=$((k+1)); d="$TMPROOT/green$k"
  mkrepo "$d" || exit 2
  plant "$d" "$rel" "$line" || exit 2
  arm "GREEN $what" 0 "remote-literals: clean" -- gate "$d"
done < "$GREEN_TABLE"
[ "$k" = 8 ] || bad "the GREEN table read as $k rows, not 8"

# ---- the population refuses to be vacuous ----------------------------------------------------------
d="$TMPROOT/empty"
mkdir -p "$d/${PFX}"
( cd "$d" && git init -q && git config user.email t@t && git config user.name t ) || exit 2
cp "$GATE_SRC" "$d/${PFX}check-remote-literals.sh"
printf 'notes\n' > "$d/notes.txt"
( cd "$d" && git add notes.txt && git commit -qm base ) || exit 2
arm "an empty population is a DEAD PROBE, never clean" 2 "DEAD PROBE" -- gate "$d"

d="$TMPROOT/usage"; mkrepo "$d" || exit 2
arm "an unknown mode refuses" 2 "usage:" -- gate "$d" --nope
d="$TMPROOT/list"; mkrepo "$d" || exit 2
arm "--list prints the population" 0 "population  ${PFX}kit/clean.sh" -- gate "$d" --list

if [ "$PASS" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-remote-literals.test FAILED — $PASS arm(s) executed, below the floor of $FLOOR_ASSERTIONS;"
  echo "  a block of arms was stranded or skipped, so a green here would certify arms that never ran."
  exit 1
fi
[ "$FAIL" = 0 ] || { echo "FAIL ($PASS assertions, $FAIL failed)"; exit 1; }
echo "PASS ($PASS assertions)"
