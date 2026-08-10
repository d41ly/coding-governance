#!/usr/bin/env bash
# check-install-prefix.test.sh — red/green arms for the install-prefix gate. Exit 0 = every arm held.
#
#   bash tools/check-install-prefix.test.sh
#
# DISCIPLINES (same as the sibling gate tests):
#  * Every arm asserts the SPECIFIC message, never the exit code alone — a probe that reads only `$?`
#    reports success while exercising nothing.
#  * Every red arm has a green control over the SAME mechanism, so an arm cannot pass because the
#    gate rejects everything.
#  * The population guards get their own arms. This gate's two `that is not a pass` branches exist
#    because an empty kit list or an empty file list would otherwise be silent success — the
#    vacuous-selector class this repo catalogues.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE="$ROOT/tools/check-install-prefix.sh"
fails=0
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

bad()  { fails=$((fails+1)); printf 'arm FAIL  %s\n' "$*"; }
good() { printf 'arm ok    %s\n' "$*"; }
# $1 label · $2 expected substring ("" = expect exit 0 and no match test) · $3 expected exit · rest: cwd
run_arm() { # label · want-substring · want-rc · dir
  local label="$1" want="$2" wrc="$3" dir="$4" out rc
  out=$(cd "$dir" && bash "$GATE" 2>&1); rc=$?
  if [ "$rc" != "$wrc" ]; then bad "$label (exit $rc, wanted $wrc): $(printf '%s' "$out" | head -2)"; return; fi
  if [ -n "$want" ] && ! printf '%s' "$out" | grep -qF "$want"; then
    bad "$label (message missing '$want'): $(printf '%s' "$out" | head -3)"; return
  fi
  good "$label"
}

# A repo shaped like an adopter: one kit under tools/, one shipped file, a waiver registry.
mkfix() { # $1 = dir · $2 = the line to put in the shipped README
  local d="$1"
  mkdir -p "$d/tools/memory-tree"
  git -C "$d" init -q
  git -C "$d" config user.email t@t.test; git -C "$d" config user.name t
  printf '#!/usr/bin/env bash\n' > "$d/tools/memory-tree/check-memory-hygiene.sh"
  printf '%s\n' "$2" > "$d/tools/memory-tree/README.md"
  cp "$GATE" "$d/tools/check-install-prefix.sh"
  printf '# waivers\n' > "$d/tools/install-prefix-waivers.txt"
  git -C "$d" add -A >/dev/null 2>&1
}

# 1. GREEN — a shipped file naming the kit at its declared prefix.
A="$TMP/green"; mkfix "$A" 'Run `bash tools/memory-tree/check-memory-hygiene.sh` to lint.'
run_arm "a tools/-prefixed path is clean" "no undeclared root-install spelling" 0 "$A"

# 2. RED — the same sentence at a root-install spelling. Same fixture, one path changed, so the arm
#    cannot be passing for an unrelated reason.
B="$TMP/red"; mkfix "$B" 'Run `bash memory-tree/check-memory-hygiene.sh` to lint.'
run_arm "a root-install path is caught" "spells a root-install kit path" 1 "$B"

# 3. ...and naming it in the waiver registry makes the SAME tree pass.
printf 'tools/memory-tree/README.md:1  deliberate, for the arm\n' >> "$B/tools/install-prefix-waivers.txt"
git -C "$B" add -A >/dev/null 2>&1
run_arm "a declared waiver clears that hit" "1 declared waiver" 0 "$B"

# 4. ...and a waiver whose spelling is gone is STALE, not a free pass. Without this a registry
#    outlives what it excused and the next violation slips in under a pin that never fell.
printf '%s\n' 'Run `bash tools/memory-tree/check-memory-hygiene.sh` to lint.' > "$B/tools/memory-tree/README.md"
git -C "$B" add -A >/dev/null 2>&1
run_arm "a waiver whose hit is gone reds as stale" "stale waiver" 1 "$B"

# 5. PROSE naming the kit is not a path. Gating it would make every sentence about a kit a violation,
#    so the predicate requires a real filename — and that exemption needs its own arm, or a future
#    tightening would silently start reporting documentation.
C="$TMP/prose"; mkfix "$C" 'The `memory-tree/` kit lives under tools/.'
run_arm "a bare kit name in prose is not a hit" "no undeclared root-install spelling" 0 "$C"

# 6. A test file is out of the population BY DESIGN — fixtures build root-prefix installs on purpose.
D="$TMP/testfile"; mkfix "$D" 'clean'
printf 'bash memory-tree/check-memory-hygiene.sh\n' > "$D/tools/memory-tree/thing.test.sh"
git -C "$D" add -A >/dev/null 2>&1
run_arm "a .test.sh fixture is excluded from the population" "no undeclared root-install spelling" 0 "$D"
# ...and the SAME content in a non-test file is caught, so arm 6 is an exclusion and not a blind spot.
mv "$D/tools/memory-tree/thing.test.sh" "$D/tools/memory-tree/thing.sh"
git -C "$D" add -A >/dev/null 2>&1
run_arm "...and the same content in a shipped file IS caught" "spells a root-install kit path" 1 "$D"

# 7. POPULATION GUARDS. Both branches say "that is not a pass" out loud; a gate whose selector went
#    empty would otherwise report success over nothing.
E="$TMP/nokits"; mkdir -p "$E"; git -C "$E" init -q
git -C "$E" config user.email t@t.test; git -C "$E" config user.name t
mkdir -p "$E/tools"; cp "$GATE" "$E/tools/check-install-prefix.sh"
git -C "$E" add -A >/dev/null 2>&1
run_arm "no kit directories -> refuses, not a silent pass" "that is not a pass" 1 "$E"

# 8. A placeholder-prefixed path is NOT a hit — it is the corrected form this gate exists to produce.
F="$TMP/placeholder"; mkfix "$F" 'Run `bash {{TOOL_ROOT}}memory-tree/check-memory-hygiene.sh` to lint.'
run_arm "a placeholder-prefixed path is not a hit" "no undeclared root-install spelling" 0 "$F"

if [ "$fails" != 0 ]; then printf 'FAIL — %d arm(s) failed\n' "$fails"; exit 1; fi
echo "PASS — check-install-prefix: all arms held"
