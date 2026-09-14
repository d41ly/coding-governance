#!/usr/bin/env bash
# Arms for tools/check-hook-destinations.sh — TOOL-dRetiredFork-21.
#
#   bash tools/check-hook-destinations.test.sh
#
# Every arm here was observed RED before the gate was wired, which is the rule: a gate whose failing
# case nobody has watched fire is an assertion about nothing. The two positive breaks are staged
# into COPIES of the real tree rather than the tree itself, so a killed run cannot leave gov with a
# reverted fragment.
set -u
KIT_REL="${KIT_REL:-tools}"
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)" || exit 2
GATE="$ROOT/$KIT_REL/check-hook-destinations.sh"
n=0; st=0
ok()  { n=$((n+1)); echo "ok   $1"; }
bad() { n=$((n+1)); echo "FAIL $1"; st=1; }

# A scratch clone of the tracked tree. `git archive` gives the INDEX, so a staged edit is included
# and an unstaged scratch file is not — which is what makes these arms reproducible.
scratch() {
  local d; d=$(mktemp -d)
  ( cd "$ROOT" && git archive HEAD ) | tar -x -C "$d" 2>/dev/null
  # overlay anything staged-but-uncommitted, so the arms grade what is about to land
  ( cd "$ROOT" && git diff --cached --name-only 2>/dev/null ) | while IFS= read -r f; do
    [ -n "$f" ] && [ -f "$ROOT/$f" ] && { mkdir -p "$d/$(dirname "$f")"; cp "$ROOT/$f" "$d/$f"; }
  done
  ( cd "$d" && git init -q . && git config user.email t@t && git config user.name t \
      && git add -A && git commit -q -m fixture --no-verify ) >/dev/null 2>&1
  echo "$d"
}

# ---- ARM 1: the shipped tree is clean ------------------------------------------------------------
if bash "$GATE" >/dev/null 2>&1; then ok "the shipped tree passes"; else bad "the shipped tree does not pass"; fi

# ---- ARM 2: a fragment naming an undeclared destination REDS (AC4) -------------------------------
d=$(scratch)
sed -i 's|{kit}/hooks/scratch-guard.js|.claude/hooks/scratch-guard.js|' "$d/$KIT_REL/hooks/scratch-guard.fragment.json"
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "a fragment naming a withdrawn path REDS (rc=$rc)" \
               || bad "a fragment naming a withdrawn path was accepted"
case "$out" in *"scratch-guard.fragment.json"*".claude/hooks/scratch-guard.js"*)
  ok "and the refusal names BOTH the fragment and the destination" ;;
  *) bad "the refusal does not name both: $(printf '%s' "$out" | head -2)" ;; esac
rm -rf "$d"

# ---- ARM 3: an adopter installing into an undeclared destination REDS ----------------------------
# This is the state that actually existed: `adopt-memory-recall.sh --with-hook` re-created the copy
# TOOL-dRetiredFork-14 withdrew. Arm 2 alone would NOT have caught it, because that installer reads
# no fragment — a gate over declarations cannot see an installer.
d=$(scratch)
printf '\ncp "$HERE/recall-opened.js" "$ROOT/.claude/hooks/recall-opened.js"\n' \
  >> "$d/$KIT_REL/memory-recall/adopt-memory-recall.sh"
( cd "$d" && git add -A && git commit -q -m break --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "an adopter writing into .claude/hooks/ REDS (rc=$rc)" \
               || bad "an adopter re-creating the withdrawn copy was accepted"
case "$out" in *"adopt-memory-recall.sh installs a hook"*) ok "and names the installer" ;;
  *) bad "the refusal does not name the installer" ;; esac
rm -rf "$d"

# ---- ARM 4: an EMPTY fragment population REFUSES (AC5) -------------------------------------------
# Zero fragments and a clean tree print the same thing unless the gate says otherwise, and the
# fragments are tracked, so zero means the selector broke.
d=$(scratch)
( cd "$d" && git rm -q $(git ls-files '*.fragment.json') && git commit -q -m nofrags --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "an empty fragment population REFUSES (rc=$rc)" \
               || bad "a gate with no subject reported success"
case "$out" in *"REFUSING"*"no subject"*) ok "and says it has no subject rather than printing a zero" ;;
  *) bad "the refusal does not explain itself: $(printf '%s' "$out" | head -2)" ;; esac
rm -rf "$d"

# ---- ARM 5: ANTI-VACUITY — the clean and broken trees must differ --------------------------------
# Every arm above would also pass if the gate refused unconditionally. This pins that the verdicts
# actually diverge on the same fixture shape.
d=$(scratch)
a=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" >/dev/null 2>&1; echo $?)
sed -i 's|{kit}/hooks/scratch-guard.js|.claude/hooks/scratch-guard.js|' "$d/$KIT_REL/hooks/scratch-guard.fragment.json"
b=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" >/dev/null 2>&1; echo $?)
[ "$a" = 0 ] && [ "$b" != 0 ] && ok "the same fixture passes clean and reds broken ($a then $b)" \
                              || bad "the gate does not discriminate (clean=$a broken=$b)"
rm -rf "$d"

# ---- ARM 6: a {here} fragment in a directory NO flat descriptor homes REFUSES (AC6) --------------
# TOOL-aReplayedCard-2. `{here}` means "beside a flat kit's engine"; a fragment carrying it under a
# directory-shaped kit's home ships from nowhere, and the leg must say which directory rather than
# pass because the flat-kit rule found nothing to compare.
d=$(scratch)
printf '{"name": "orphan", "event": "E", "matcher": "M", "marker": "agent-cap.js", "hook_path": "{here}/agent-cap.js"}\n' \
  > "$d/$KIT_REL/hooks/orphan.fragment.json"
( cd "$d" && git add -A && git commit -q -m orphan --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "a {here} fragment under a non-flat home REDS (rc=$rc)" \
               || bad "a {here} fragment under a non-flat home was accepted"
case "$out" in *"orphan.fragment.json"*"'$KIT_REL/hooks' is the home of NO kind=flat"*)
  ok "and the refusal names the directory and the flat-kit rule" ;;
  *) bad "the refusal does not name the directory: $(printf '%s' "$out" | grep orphan | head -2)" ;; esac
rm -rf "$d"

# ---- ARM 7: a {here} fragment under a SHARED flat home is judged at its adopter path (AC6) --------
# `tools/` is the home of several flat descriptors at once. That is not undecidable: the rule is "at
# least one flat descriptor homes the directory", and `{prefix}/<file>` is then compared against the
# WHOLE declared set. The fixture names a file a flat kit ships beside the fragment.
d=$(scratch)
printf '{"name": "shared", "event": "E", "matcher": "M", "marker": "settings-merge.py", "hook_path": "{here}/settings-merge.py"}\n' \
  > "$d/$KIT_REL/shared-home.fragment.json"
( cd "$d" && git add -A && git commit -q -m shared --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" = 0 ] && ok "a {here} fragment under a shared flat home passes (rc=$rc)" \
              || bad "a {here} fragment under a shared flat home was refused: $(printf '%s' "$out" | grep -E 'FAIL|REFUS' | head -2)"
case "$out" in *"shared-home.fragment.json -> $KIT_REL/settings-merge.py in the tree, ships as"*)
  ok "and the ok line prints both spellings" ;;
  *) bad "the ok line does not print both spellings: $(printf '%s' "$out" | grep shared-home | head -1)" ;; esac
# ...and the SAME shape naming a file the flat kits do NOT ship reds, both spellings printed: the
# flat-home test alone must not be enough.
printf '{"name": "unshipped", "event": "E", "matcher": "M", "marker": "nobody.sh", "hook_path": "{here}/nobody.sh"}\n' \
  > "$d/$KIT_REL/unshipped.fragment.json"
( cd "$d" && git add -A && git commit -q -m unshipped --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "a {here} fragment naming an unshipped file under a flat home REDS (rc=$rc)" \
               || bad "a {here} fragment naming an unshipped file was accepted"
case "$out" in *"unshipped.fragment.json"*"'$KIT_REL/nobody.sh' in the tree, which would ship as"*"'$KIT_REL/nobody.sh'"*)
  ok "and the refusal prints the in-tree and the adopter spelling" ;;
  *) bad "the refusal does not print both spellings: $(printf '%s' "$out" | grep unshipped | head -2)" ;; esac
rm -rf "$d"

# ---- ARM 8: the PARITY arm fires when the two readers disagree ----------------------------------
# The gate reads `{kit}`/`{here}` from `check-wiring.sh --resolve-fragment` and from
# `settings-merge.py --resolve-fragment` and refuses on a mismatch. Staged by breaking the shell
# reader's `{here}` expansion in a COPY of the tree, so the two answers differ on every {here}
# fragment and agree on every {kit} one.
d=$(scratch)
sed -i 's#{here}/|${here:+$here/}|g#{here}/|elsewhere/|g#' "$d/$KIT_REL/check-wiring.sh"
grep -q 'elsewhere/' "$d/$KIT_REL/check-wiring.sh" || bad "the parity fixture did not stage its break (the resolver's {here} line moved)"
( cd "$d" && git add -A && git commit -q -m parity --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "two readers disagreeing on a token REDS (rc=$rc)" \
               || bad "the gate accepted two readers that disagree"
case "$out" in *"the two readers DISAGREE"*"elsewhere/"*) ok "and the refusal prints both readers' answers" ;;
  *) bad "the refusal does not name the disagreement: $(printf '%s' "$out" | grep -E 'FAIL' | head -2)" ;; esac
rm -rf "$d"

# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not the written one. An arm stranded
# past an early exit disappears silently; the floor is what turns that into a failure instead of a
# smaller green number nobody reads.
FLOOR_ASSERTIONS=16
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
# The AGREED shape, anchored: check-testsuite-counts.sh matches this line to prove the count is
# actually printed rather than merely computed.
[ "$st" = 0 ] && echo "PASS ($n assertions)"
[ "$st" = 0 ] || echo "FAIL (check-hook-destinations: $n assertions, $st failing)"
exit $st
