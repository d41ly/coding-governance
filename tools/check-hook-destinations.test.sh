#!/usr/bin/env bash
# Arms for <prefix>/check-hook-destinations.sh — TOOL-dRetiredFork-21.
#
#   bash <prefix>/check-hook-destinations.test.sh
#
# Every arm here was observed RED before the gate was wired, which is the rule: a gate whose failing
# case nobody has watched fire is an assertion about nothing. The two positive breaks are staged
# into COPIES of the real tree rather than the tree itself, so a killed run cannot leave gov with a
# reverted fragment.
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-hook-destinations.test: not inside a git repository"; exit 2; }
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)" || exit 2
GATE="$ROOT/$KIT_REL/check-hook-destinations.sh"
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
_rkd_py=$(resolve_python) || { echo "check-hook-destinations.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
HOOKS_DIR=$(resolve_kit_dir "$_rkd_py" hooks agent-cap.js "$HERE") || exit 2
HOOKS="${HOOKS_DIR##*/}"
MEMORY_RECALL_DIR=$(resolve_kit_dir "$_rkd_py" memory-recall extract.py "$HERE") || exit 2
MEMORY_RECALL="${MEMORY_RECALL_DIR##*/}"
# The destination TOOL-dRetiredFork-14 withdrew: the harness's own hook directory, which is no kit.
WITHDRAWN=.claude/hooks/scratch-guard.js
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
sed -i 's|{kit}/hooks/scratch-guard.js|'"$WITHDRAWN"'|' "$d/$HOOKS_DIR/scratch-guard.fragment.json"
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
  >> "$d/$MEMORY_RECALL_DIR/adopt-memory-recall.sh"
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
sed -i 's|{kit}/hooks/scratch-guard.js|'"$WITHDRAWN"'|' "$d/$HOOKS_DIR/scratch-guard.fragment.json"
b=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" >/dev/null 2>&1; echo $?)
[ "$a" = 0 ] && [ "$b" != 0 ] && ok "the same fixture passes clean and reds broken ($a then $b)" \
                              || bad "the gate does not discriminate (clean=$a broken=$b)"
rm -rf "$d"

# ---- ARM 6: a {here} fragment in a directory NO descriptor homes REFUSES (AC6) -------------------
# TOOL-aReplayedCard-2, narrowed by TOOL-aRepatriatedFork-2 (gate repair at VERIFYING): a fragment
# under a directory NO descriptor homes ships from nowhere, and the leg must say which directory.
# Under a DIRECTORY kit's home, `{here}` is the kit dir at every prefix, so a shipped file passes
# and an unshipped one reds — the memory-recall fragment is that shape in the shipped tree.
d=$(scratch)
mkdir -p "$d/$KIT_REL/nohome"
printf '{"name": "orphan", "event": "E", "matcher": "M", "marker": "agent-cap.js", "hook_path": "{here}/agent-cap.js"}\n' \
  > "$d/$KIT_REL/nohome/orphan.fragment.json"
( cd "$d" && git add -A && git commit -q -m orphan --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "a {here} fragment under no descriptor's home REDS (rc=$rc)" \
               || bad "a {here} fragment under no descriptor's home was accepted"
case "$out" in *"orphan.fragment.json"*"'$KIT_REL/nohome' is the home of NO descriptor"*)
  ok "and the refusal names the directory" ;;
  *) bad "the refusal does not name the directory: $(printf '%s' "$out" | grep orphan | head -2)" ;; esac
rm -rf "$d"
d=$(scratch)
printf '{"name": "dirkit", "event": "E", "matcher": "M", "marker": "agent-cap.js", "hook_path": "{here}/agent-cap.js"}\n' \
  > "$d/$HOOKS_DIR/dirkit.fragment.json"
( cd "$d" && git add -A && git commit -q -m dirkit --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" = 0 ] && ok "a {here} fragment under a directory kit's home naming a shipped file passes" \
              || bad "a {here} fragment under a directory kit's home was refused: $(printf '%s' "$out" | grep -E 'FAIL|REFUS' | head -2)"
printf '{"name": "dirkit", "event": "E", "matcher": "M", "marker": "nobody.js", "hook_path": "{here}/nobody.js"}\n' \
  > "$d/$HOOKS_DIR/dirkit.fragment.json"
( cd "$d" && git add -A && git commit -q -m dirkit-unshipped --no-verify ) >/dev/null 2>&1
out=$(cd "$d" && bash "$KIT_REL/check-hook-destinations.sh" 2>&1); rc=$?
[ "$rc" != 0 ] && ok "a {here} fragment under a directory kit's home naming an unshipped file REDS (rc=$rc)" \
               || bad "a {here} fragment naming an unshipped file under a directory kit's home was accepted"
rm -rf "$d"

# ---- ARM 7: a {here} fragment under a SHARED flat home is judged at its adopter path (AC6) --------
# `<prefix>/` is the home of several flat descriptors at once. That is not undecidable: the rule is "at
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
FLOOR_ASSERTIONS=18
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
# The AGREED shape, anchored: check-testsuite-counts.sh matches this line to prove the count is
# actually printed rather than merely computed.
[ "$st" = 0 ] && echo "PASS ($n assertions)"
[ "$st" = 0 ] || echo "FAIL (check-hook-destinations: $n assertions, $st failing)"
exit $st
