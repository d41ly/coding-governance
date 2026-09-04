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

# --- L1: THE GOAL STATE, GATED. DEPL-dCarriedReceipt-15's stated direction is to shrink these
# counts to zero, and the liveness assertion used to sit on the HIT set — so a live derivation over
# a repo that genuinely carries no literals was indistinguishable from a dead one, and on the day
# the repo reached its own goal this leg would red with a false statement and no override short of
# editing the gate. Asserted here as the endpoint rather than as today's tree.
Z="$TMP/src-goal"; mkfix_source "$Z" 'The engine lives at {{TOOL_ROOT}}demo/thing.sh in this repo.'
printf '#!/usr/bin/env bash
# see {{TOOL_ROOT}}demo/README.md for what this does
' > "$Z/tools/demo/thing.sh"
git -C "$Z" add -A >/dev/null 2>&1
(cd "$Z" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
git -C "$Z" add -A >/dev/null 2>&1
zout=$(cd "$Z" && bash tools/check-install-prefix.sh 2>&1); zrc=$?
if [ "$zrc" = 0 ]; then
  good "L1 a kit source carrying ZERO literals is CLEAN — the goal state passes"
  CARRIED_ARMS=$((CARRIED_ARMS+1))
else
  bad "L1: the goal state reds — a repo that reached zero cannot pass its own gate"
  printf '%s
' "$zout" | sed 's/^/      /' | head -8
fi
case "$zout" in
  *"POPULATION is empty"*) bad "L1: a live derivation over a zero-hit repo was called DEAD" ;;
  *) good "L1 ...and the liveness assertion does not misreport it as a dead probe" ;;
esac

# --- L5: THE `FILENAME == pinf` ROLE RULE, ARMED DIRECTLY ---------------------------------------
# Round 2's L5 measured this: swapping `FILENAME == pinf` back to `NR==FNR` in the gate left all 22
# arms green. The unreachability is structural rather than lucky — the roles only diverge when file
# 1 has ZERO records, and the sibling `-s` guard exits before awk ever runs on an empty ratchet — so
# no arm routed through the gate can reach the divergent input. Per §7, a rule whose failing case has
# never been observed is an assertion about nothing, and the next person tidying that awk undoes it
# silently.
#
# So this arm skips the gate and feeds the awk PROGRAM ITSELF the one input the roles disagree on.
# The program text is EXTRACTED from the gate rather than copied here: a copy would be two answers to
# one question, and an edit to the real awk has to reach this arm or the arm grades a fossil.
_awkprog="$TMP/role.awk"
awk '/^  awk -F/ {grab=1; next} grab && /^    \}.*CARRIED/ {print "}"; exit} grab {print}' \
  tools/check-install-prefix.sh > "$_awkprog"
if [ ! -s "$_awkprog" ] || ! grep -q 'UNRECORDED' "$_awkprog"; then
  bad "L5: could not EXTRACT the awk program from the gate — this arm is grading nothing, which is the exact class it exists to close"
else
  # File 1 is the ratchet and is EMPTY (zero records). File 2 carries one measured row.
  : > "$TMP/role-pin.tsv"
  printf 'tools/demo/thing.sh\t2\n' > "$TMP/role-now.tsv"
  _rout=$(awk -F'\t' -v pinf="$TMP/role-pin.tsv" -f "$_awkprog" \
            "$TMP/role-pin.tsv" "$TMP/role-now.tsv" 2>&1)
  # `FILENAME == pinf` — pin[] stays empty, now[] takes the row, so UNRECORDED, which is the truth.
  # `NR==FNR`          — pin[] takes FILE 2's row, now[] stays empty, so `SLACK … -> 0 (delete the
  #                      row)`: telling the operator to delete a ratchet that records nothing, while
  #                      the correct verdict never prints. That is D4/D13's original defect verbatim.
  case "$_rout" in
    *UNRECORDED*)
      good "L5 a ZERO-RECORD ratchet keeps the awk roles straight — UNRECORDED, the true verdict"
      CARRIED_ARMS=$((CARRIED_ARMS+1)) ;;
    *SLACK*)
      bad "L5: the awk roles INVERTED on a zero-record file 1 — it read the MEASURED file as the pin and printed SLACK. This is the D4/D13 defect back, and it is what NR==FNR does on this input" ;;
    *)
      bad "L5: the awk printed neither verdict on a zero-record file 1, so this arm observed nothing: $_rout" ;;
  esac
fi

# --- TOOL-dRetiredFork-17: THE RATCHET IS A BAN ------------------------------------------------
# THESE ARMS INVOKE THE GATE, and the first version did not. It hand-copied the gate's awk into
# the suite and asserted on the copy, so it graded a transcription rather than the shipped code.
# The closing review proved the consequence by staging a break: replacing the whole refusal
# condition with `if false; then` left every arm green and the suite closing PASS. A gate whose
# failing case has never been observed is an assertion about nothing, and a SUITE that cannot see
# its gate switched off is that same defect one level up.
#
# The copies had already drifted, which is the other half of why the shape was wrong: the suite's
# `seen[$1]=1` clause had grown a comment filter the shipped gate does not have.
BAN_ARMS=0
ban_arm() { # label · want-substring · want-rc · dir · [argv...]
  local before=$CARRIED_ARMS
  carried_arm "$@"
  [ "$CARRIED_ARMS" -gt "$before" ] && BAN_ARMS=$((BAN_ARMS+1))
  return 0
}

# B1 — a NEW carrier is REFUSED by the writer, where the ratchet it replaced would have absorbed it.
B1="$TMP/ban-new"; mkfix_source "$B1" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$B1" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
printf '#!/usr/bin/env bash\n# and see tools/demo/thing.sh too\n' > "$B1/tools/demo/second.sh"
git -C "$B1" add -A >/dev/null 2>&1
ban_arm "B1 --write-ratchet REFUSES a new carrier instead of absorbing it" "NEW carrier" 1 "$B1" --write-ratchet

# B2 — a RISEN count is refused too, and reported as its own verdict because the remedy differs.
B2="$TMP/ban-rise"; mkfix_source "$B2" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$B2" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
printf 'And again tools/demo/thing.sh.\n' >> "$B2/tools/demo/README.md"
git -C "$B2" add -A >/dev/null 2>&1
ban_arm "B2 --write-ratchet REFUSES a risen count" "RISEN count" 1 "$B2" --write-ratchet

# B3 — THE NEGATIVE, and the arm that stops B1 and B2 proving too much. A DROP must still be
# writable, or the ban has broken the ratchet it replaced and the only legal state is whatever the
# file already says, forever.
B3="$TMP/ban-drop"; mkfix_source "$B3" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$B3" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
printf 'nothing carried here now\n' > "$B3/tools/demo/README.md"
git -C "$B3" add -A >/dev/null 2>&1
b3out=$(cd "$B3" && bash tools/check-install-prefix.sh --write-ratchet 2>&1); b3rc=$?
if [ "$b3rc" = 0 ]; then
  good "B3 ...and a DROP is still written — the ban did not break progress"
  BAN_ARMS=$((BAN_ARMS+1))
else
  bad "B3 a DROP was REFUSED (rc $b3rc) — the ban forbids recording progress, so the only legal state is the current one forever"
  printf '%s\n' "$b3out" | sed 's/^/      /' | head -8
fi

# B4 — a hand-written reason column SURVIVES a legitimate write. Without the join that preserves
# it, the next drop erases every justification in the file and leaves a ban nobody can account for.
B4="$TMP/ban-reason"; mkfix_source "$B4" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$B4" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
awk -F'\t' -v OFS='\t' '/README/ { print $1, $2, $3, "a person decided this"; next } { print }' \
  "$B4/tools/install-prefix-carried.txt" > "$B4/.tmpban" \
  && mv "$B4/.tmpban" "$B4/tools/install-prefix-carried.txt"
printf 'nothing carried here now\n' > "$B4/tools/demo/thing.sh"
git -C "$B4" add -A >/dev/null 2>&1
(cd "$B4" && bash tools/check-install-prefix.sh --write-ratchet >/dev/null 2>&1)
if grep -q 'a person decided this' "$B4/tools/install-prefix-carried.txt"; then
  good "B4 a hand-written reason column survives a later write"
  BAN_ARMS=$((BAN_ARMS+1))
else
  bad "B4 the reason column was ERASED by a later write — every justification in a ban list would be lost on the next drop"
fi

# B5 — the epoch guard. `--rebaseline` is the ONE mode that may add rows, so a guard that does not
# hold turns the ban back into an exemption form with a longer name.
B5="$TMP/ban-epoch"; mkfix_source "$B5" 'The engine lives at tools/demo/thing.sh in this repo.'
(cd "$B5" && bash tools/check-install-prefix.sh --rebaseline >/dev/null 2>&1)
ban_arm "B5 --rebaseline REFUSES when the recorded epoch already matches" "REFUSING to rebaseline" 1 "$B5" --rebaseline

if [ "$BAN_ARMS" -ge 5 ]; then
  good "LIVENESS $BAN_ARMS ban arm(s) engaged the real gate"
else
  bad "LIVENESS only $BAN_ARMS ban arm(s) reached the gate — the rest fell through or SKIPPED, so this section reports on arms that did not run"
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
