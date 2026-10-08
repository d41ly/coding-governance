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

FLOOR_ASSERTIONS=43
PASS=0
FAIL=0
add_pass() { PASS=$((PASS+1)); }
add_fail() { FAIL=$((FAIL+1)); echo "  FAIL: $1"; }

TMPROOT=$(mktemp -d) || exit 2
trap 'rm -rf "$TMPROOT"' EXIT

# arm <label> <want-rc> <needle> -- <cmd...>
arm() {
  local label="$1" want="$2" needle="$3"; shift 4
  local out rc
  out=$("$@" 2>&1); rc=$?
  if [ "$rc" -ne "$want" ]; then
    add_fail "$label — wanted rc=$want got $rc: $(printf '%s' "$out" | head -3)"; return
  fi
  case "$out" in *"$needle"*) add_pass ;; *) add_fail "$label — rc was right but the message was not: $(printf '%s' "$out" | head -3)" ;; esac
}

# build_repo <dir> — a committed repo carrying the gate at this suite's own prefix and one clean file, so
# the population is never empty unless an arm empties it on purpose.
build_repo() {
  local d="$1"
  mkdir -p "$d/${PFX}kit"
  ( cd "$d" && git init -q && git config core.autocrlf false \
      && git config user.email t@t && git config user.name t ) || return 1
  cp "$GATE_SRC" "$d/${PFX}check-remote-literals.sh"
  printf 'echo clean\n' > "$d/${PFX}kit/clean.sh"
  ( cd "$d" && git add -A && git commit -qm base ) || return 1
}
# write_plant <dir> <relpath> <line> — write one line into a tracked file of the scratch repo
write_plant() {
  mkdir -p "$(dirname "$1/$2")"
  printf '%s\n' "$3" > "$1/$2"
  ( cd "$1" && git add -A ) || return 1
}
run_gate() { ( cd "$1" && bash "${PFX}check-remote-literals.sh" "${@:2}" ); }

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
  # TOOL-dLadderedRemote-5: the spellings the round-1 review found escaping, and two product files the
  # old path exclusions hid by matching `selftest` and `test_` anywhere in a path.
  printf '%s\n' "a shell case arm|${PFX}kit/m.sh|  *) def=\$(git symbolic-ref --short refs/remotes/$N/HEAD) ;;"
  printf '%s\n' "a prefix strip, shell|${PFX}kit/n.sh|obs=\${obs#$N/}"
  printf '%s\n' "a prefix strip, python|${PFX}kit/o.py|    branch = ref.removeprefix(\"$N/\")"
  printf '%s\n' "a defaulted get|${PFX}kit/p.py|    r = os.environ.get(\"GOV_REMOTE\", \"$N\")"
  printf '%s\n' "default after :=|${PFX}kit/q.sh|r=\${GOV_REMOTE:=$N}"
  printf '%s\n' "an unquoted assignment|${PFX}kit/r.sh|REMOTE=$N"
  printf '%s\n' "a push remedy|${PFX}kit/s.sh|git push $N HEAD:main"
  printf '%s\n' "a skills js file|skills/kit/t.js|const r = opts.remote ?? \"$N\""
  printf '%s\n' "a product file named like a test|${PFX}kit/latest_probe.py|    os.system(\"git fetch $N main\")"
  # TOOL-dLadderedRemote-6: the round-2 review's escapes, one arm per alternative.
  printf '%s\n' "a positional default|${PFX}kit/w.sh|remote=\${1:-$N}"
  printf '%s\n' "default after -|${PFX}kit/x.sh|r=\${R-$N}"
  printf '%s\n' "default after =|${PFX}kit/y.sh|r=\${R=$N}"
  printf '%s\n' "a config key|${PFX}kit/z.sh|git config --get remote.$N.url"
  printf '%s\n' "a pull with a flag|${PFX}kit/aa.sh|git pull --ff-only $N main"
  printf '%s\n' "a fetch with a flag|${PFX}kit/ab.sh|git fetch --quiet $N main"
  printf '%s\n' "an argv list|${PFX}kit/ac.py|    subprocess.run([\"git\", \"fetch\", \"--prune\", \"$N\", \"main\"])"
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
  # TOOL-dLadderedRemote-5: a VARIABLE named like the remote is not a literal remote.
  printf '%s\n' "a variable named like the remote, shell|${PFX}kit/u.sh|$N=\$RR_REMOTE; git rev-parse \"\$$N/HEAD\""
  printf '%s\n' "a variable named like the remote, js|${PFX}kit/v.js|const k = rec.a || $N.kind"
  # TOOL-dLadderedRemote-6: a bare name on an assignment's right is a VARIABLE outside shell.
  printf '%s\n' "a python variable assignment|${PFX}kit/ad.py|        self.$N = $N"
  printf '%s\n' "a js variable assignment|${PFX}kit/ae.js|const base = $N;"
  # TOOL-dLadderedRemote-7: the same bytes with NO spaces, which only the shell-only pass's file filter
  # keeps clean, and two keys spelled like the remote that the default and last-argument shapes see.
  printf '%s\n' "a js assignment with no spaces|${PFX}kit/af.js|let r=$N;"
  printf '%s\n' "a python assignment with no spaces|${PFX}kit/ag.py|x=$N"
  printf '%s\n' "a js template comparing a variable|${PFX}kit/ah.js|const label = \`\${a.kind===$N ? 1 : 2}\`;"
  printf '%s\n' "a python key list|${PFX}kit/ai.py|FIELDS = [\"kit\", \"$N\"]"
} > "$GREEN_TABLE"
# ---- RED: one shape per arm ------------------------------------------------------------------------
k=0
while IFS='|' read -r shape rel line; do
  [ -n "$shape" ] || continue
  k=$((k+1)); d="$TMPROOT/red$k"
  build_repo "$d" || { echo "remote-literals.test: could not build $d"; exit 2; }
  write_plant "$d" "$rel" "$line" || exit 2
  arm "RED $shape is named" 1 "$rel:1:" -- run_gate "$d"
  # FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
  if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${FAIL:-0}" = 0 ] && echo "PASS (${PASS:-1} assertions)" || echo "FAIL (${PASS:-1} assertions)"; [ "${FAIL:-0}" = 0 ] && exit 0; exit 1; fi
done < "$RED_TABLE"
[ "$k" = 24 ] || add_fail "the RED table read as $k rows, not 24"

# ---- GREEN: the same bytes where they must not be named --------------------------------------------
k=0
while IFS='|' read -r what rel line; do
  [ -n "$what" ] || continue
  k=$((k+1)); d="$TMPROOT/green$k"
  build_repo "$d" || exit 2
  write_plant "$d" "$rel" "$line" || exit 2
  arm "GREEN $what" 0 "remote-literals: clean" -- run_gate "$d"
done < "$GREEN_TABLE"
[ "$k" = 16 ] || add_fail "the GREEN table read as $k rows, not 16"

# ---- the population refuses to be vacuous ----------------------------------------------------------
d="$TMPROOT/empty"
mkdir -p "$d/${PFX}"
( cd "$d" && git init -q && git config user.email t@t && git config user.name t ) || exit 2
cp "$GATE_SRC" "$d/${PFX}check-remote-literals.sh"
printf 'notes\n' > "$d/notes.txt"
( cd "$d" && git add notes.txt && git commit -qm base ) || exit 2
arm "an empty population is a DEAD PROBE, never clean" 2 "DEAD PROBE" -- run_gate "$d"

d="$TMPROOT/usage"; build_repo "$d" || exit 2
arm "an unknown mode refuses" 2 "usage:" -- run_gate "$d" --nope
d="$TMPROOT/list"; build_repo "$d" || exit 2
arm "--list prints the population" 0 "population  ${PFX}kit/clean.sh" -- run_gate "$d" --list

if [ "$PASS" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-remote-literals.test FAILED — $PASS arm(s) executed, below the floor of $FLOOR_ASSERTIONS;"
  echo "  a block of arms was stranded or skipped, so a green here would certify arms that never ran."
  exit 1
fi
[ "$FAIL" = 0 ] || { echo "FAIL ($PASS assertions, $FAIL failed)"; exit 1; }
echo "PASS ($PASS assertions)"
