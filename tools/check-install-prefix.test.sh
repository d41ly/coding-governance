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
CLEAN_LINE='Run `bash tools/memory-tree/check-memory-hygiene.sh` to lint.'
A="$TMP/green"; mkfix "$A" "$CLEAN_LINE"
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

# THE VERDICT IS AT THE END OF THE FILE, and it moved there because it was not. The carried-prefix
# arms below were appended after this block, so the suite printed PASS and exited 0 with a FAILING
# arm in its own output — the grader reporting green while an arm redded, which is precisely the
# class D10 is about, reproduced inside D10's own fix. A verdict that is not the last statement is
# a verdict about a prefix of the suite.


# ---------------------------------------------------------------------------------------------
# D10, from the closing review of DEPL-dCarriedReceipt: every arm above builds a fixture carrying
# none of the govkit registry the second arm's guard looks for, so that guard is true for ALL of
# them and every one takes the SKIPPED branch. The `install-prefix self-test` leg therefore reported PASS
# while the ratchet, the four awk conditions, `carried_population` and the SKIP branch itself went
# ungraded — which is why D3 and D4 could not have been seen by this suite. The instance was fixed
# during that build and the CLASS was not, which is the shape this file's own header warns about.
#
# `mkfix_source` builds a repo the second arm actually engages with: a registry, a descriptor, a
# resolver and a copy of the engine, so `carried_population` can resolve a real shippable set.
CARRIED_ARMS=0

mkfix_source() { # $1 = dir · $2 = the line to put in the shipped kit file
  local d="$1"
  mkdir -p "$d/tools/govkit/entries" "$d/tools/demo" "$d/tools/lib"
  git -C "$d" init -q
  git -C "$d" config user.email t@t.test; git -C "$d" config user.name t
  cp "$GATE" "$d/tools/check-install-prefix.sh"
  cp "$ROOT/tools/govkit/govkit.py" "$d/tools/govkit/govkit.py"
  cp "$ROOT/tools/lib/resolve-python.sh" "$d/tools/lib/resolve-python.sh"
  printf '[surface]\nglobs = ["tools/*"]\n\n[selection]\ndefault = ["demo"]\n\n[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n\n[[exempt]]\npath = "tools/lib"\nwhy = "the shared library"\n\n[[exempt]]\npath = "tools/check-install-prefix.sh"\nwhy = "the gate under test"\n' > "$d/tools/govkit/registry.toml"
  printf 'id = "demo"\nhome = "tools/demo"\nversion_from = { none = "fixture" }\n\n[check]\nnone = "a fixture kit"\n\n[[files]]\ninclude = "**"\nrole = "engine"\n\n[adopt]\nargv = []\nmutates_index = false\n' > "$d/tools/demo/kit.toml"
  printf '%s\n' "$2" > "$d/tools/demo/README.md"
  # TWO carrying files, not one, and the reason is an arm rather than symmetry: the UNRECORDED arm
  # drops ONE row and needs what is left to be non-empty, because the `-s` guard treats an emptied
  # ratchet as MISSING and never reaches the comparison. With a single carrying file that arm tested
  # the path the fix had just closed and reported it as a failure to print UNRECORDED.
  printf '#!/usr/bin/env bash\n# see tools/demo/README.md for what this does\n' > "$d/tools/demo/thing.sh"
  git -C "$d" add -A >/dev/null 2>&1
}

# The carried-prefix arm reports through its own lines, so its arms read those rather than the
# first arm's. `CARRIED_ARMS` counts how many arms actually engaged the non-SKIPPED branch — the
# liveness assertion at the bottom is what makes a future all-SKIPPED suite red by that fact.
carried_arm() { # label · want-substring · want-rc · dir · [extra argv...]
  local label="$1" want="$2" wrc="$3" d="$4"; shift 4
  local out rc
  out=$(cd "$d" && bash tools/check-install-prefix.sh "$@" 2>&1); rc=$?
  case "$out" in *"carried-prefix arm SKIPPED"*) bad "$label — fixture took the SKIPPED branch, so it graded nothing"; return ;; esac
  CARRIED_ARMS=$((CARRIED_ARMS+1))
  if [ "$rc" != "$wrc" ]; then bad "$label — rc $rc, wanted $wrc"; printf '%s\n' "$out" | sed 's/^/      /' | head -12; return; fi
  case "$out" in *"$want"*) ;; *) bad "$label — output does not carry '$want'"; printf '%s\n' "$out" | sed 's/^/      /' | head -12; return ;; esac
  good "$label"
}

# --- the SKIP branch itself gets an arm, because a skip that looks like a pass is the class ----
# REUSES the line arm 1 already spells rather than respelling it: this file is itself in the
# carried-prefix population, and the ratchet is shrink-only by design, so a second copy of a literal
# is a row that has to rise. Deriving beats spelling here for exactly the reason the gate exists.
S="$TMP/notsource"; mkfix "$S" "$CLEAN_LINE"
sout=$(cd "$S" && bash tools/check-install-prefix.sh 2>&1); src=$?
case "$sout" in
  *"carried-prefix arm SKIPPED"*) good "a non-kit-source repo SKIPS the carried arm and SAYS so" ;;
  *) bad "a non-kit-source repo does not announce the skip"; printf '%s\n' "$sout" | sed 's/^/      /' | head -8 ;;
esac
[ "$src" = 0 ] || bad "the skip should not red: rc $src"

# --- GREEN control: a kit source whose ratchet matches what is measured -----------------------
G="$TMP/src-green"; mkfix_source "$G" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$G" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
git -C "$G" add -A >/dev/null 2>&1
carried_arm "a kit source with a fresh ratchet is clean" "carried-prefix clean" 0 "$G"

# --- LIVENESS on the population: the ratchet must be NON-EMPTY, or every arm below is vacuous --
if [ -s "$G/tools/install-prefix-carried.txt" ]; then
  good "...over a NON-EMPTY ratchet, so the arms below are not grading an empty set"
else
  bad "the green fixture's ratchet is empty — every carried-prefix arm here proves nothing"
fi

# --- RED: a count that ROSE ------------------------------------------------------------------
R="$TMP/src-rose"; mkfix_source "$R" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$R" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
printf 'And also tools/demo/thing.sh again.\n' >> "$R/tools/demo/README.md"
git -C "$R" add -A >/dev/null 2>&1
carried_arm "a shipped file gaining a carried literal reds as ROSE" "ROSE" 1 "$R"

# --- RED: a count that FELL and a row that did not ---------------------------------------------
K="$TMP/src-slack"; mkfix_source "$K" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$K" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
printf 'tools/demo/thing.sh\t9\n' > "$K/tools/install-prefix-carried.txt"
git -C "$K" add -A >/dev/null 2>&1
carried_arm "a row whose count fell reds as SLACK rather than passing quietly" "SLACK" 1 "$K"

# --- RED: a carrying file with NO row, over a NON-EMPTY ratchet -------------------------------
# The ratchet must be NON-EMPTY for this arm to reach the awk at all. D4's other half changed the
# guard from `-f` to `-s`, so an empty-but-present ratchet is now treated as MISSING and never meets
# the comparison — which is the right outcome and is asserted on its own below. UNRECORDED is for
# the PARTIAL case: a ratchet recording some carrying files and not others. The first cut of this
# arm used the empty file and therefore tested a path the fix had just closed.
U="$TMP/src-unrec"; mkfix_source "$U" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$U" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
grep -v 'README\.md' "$U/tools/install-prefix-carried.txt" > "$U/keep.tmp" || true
mv "$U/keep.tmp" "$U/tools/install-prefix-carried.txt"
git -C "$U" add -A >/dev/null 2>&1
carried_arm "a carrying file with NO row reds as UNRECORDED, over a non-empty ratchet" \
            "UNRECORDED" 1 "$U"

# --- D4: an EMPTY-but-present ratchet must not invert the awk's roles -------------------------
E2="$TMP/src-empty"; mkfix_source "$E2" 'The engine lives at tools/demo/thing.sh in this repo.'
: > "$E2/tools/install-prefix-carried.txt"
git -C "$E2" add -A >/dev/null 2>&1
eout=$(cd "$E2" && bash tools/check-install-prefix.sh 2>&1); erc=$?
case "$eout" in
  *SLACK*) bad "D4: an empty ratchet inverted the awk roles and reported SLACK for every file" ;;
  *) good "D4 an empty-but-present ratchet does not invert the awk roles into SLACK" ;;
esac
[ "$erc" != 0 ] || bad "D4: an empty ratchet passed at exit 0"
case "$eout" in
  *"run --write-ratchet once"*) good "D4 ...and is treated as MISSING, which the -s guard is for" ;;
  *) bad "D4: an empty ratchet neither inverted nor read as missing"; printf '%s\n' "$eout" | sed 's/^/      /' | head -6 ;;
esac

# --- RED: a MISSING ratchet is not a clean one -------------------------------------------------
M="$TMP/src-missing"; mkfix_source "$M" 'The engine lives at tools/demo/thing.sh in this repo.'
rm -f "$M/tools/install-prefix-carried.txt"
carried_arm "a MISSING ratchet reds rather than passing" "run --write-ratchet once" 1 "$M"

# --- D3: a DEAD derivation must not write an empty ratchet at exit 0 ---------------------------
# The producer is stubbed by removing the resolver the arm requires, which is the reachable
# real-world shape: a kit source whose python cannot be resolved. Without a liveness assertion the
# gate wrote 0 rows, exited 0, and the next --check compared empty against empty forever.
D="$TMP/src-dead"; mkfix_source "$D" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$D" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
git -C "$D" add -A >/dev/null 2>&1
printf 'resolve_python() { echo /nonexistent/python-xyzzy; }\n' > "$D/tools/lib/resolve-python.sh"
dout=$(cd "$D" && bash tools/check-install-prefix.sh --write-ratchet 2>&1); drc=$?
if [ "$drc" = 0 ] && [ ! -s "$D/tools/install-prefix-carried.txt" ]; then
  bad "D3: a dead derivation truncated the ratchet to zero rows and exited 0"
else
  good "D3 a dead derivation does not write an empty ratchet at exit 0"
  CARRIED_ARMS=$((CARRIED_ARMS+1))
fi
dout2=$(cd "$D" && bash tools/check-install-prefix.sh 2>&1); drc2=$?
if [ "$drc2" = 0 ]; then
  bad "D3: --check passed while the population derivation was dead"
else
  good "D3 ...and --check reds rather than reporting a clean empty population"
fi

# --- THE LIVENESS ASSERTION ON THE SUITE ITSELF ------------------------------------------------
# A self-test whose every fixture takes one branch is `fixture-passes-by-finding-nothing` applied to
# the grader, and it needs the same treatment as any other probe that cannot move. This is the arm
# that reds if someone re-breaks `mkfix_source` and every carried arm silently goes back to SKIPPED.
if [ "$CARRIED_ARMS" -ge 5 ]; then
  good "LIVENESS $CARRIED_ARMS arm(s) actually engaged the carried-prefix branch"
else
  bad "LIVENESS only $CARRIED_ARMS arm(s) reached the carried-prefix branch — the rest SKIPPED, so this suite is grading one arm and reporting on two"
fi

if [ "$fails" != 0 ]; then printf 'FAIL — %d arm(s) failed\n' "$fails"; exit 1; fi
echo "PASS — check-install-prefix: all arms held"
