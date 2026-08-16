#!/usr/bin/env bash
# check-template-size.test.sh — self-test for tools/check-template-size.sh.
#
#   bash tools/check-template-size.test.sh
#
# Exit 0 = every arm held · 1 = an arm failed · 2 = the harness could not set up.
#
# WHY THIS EXISTS. Until this file landed, the gate had no test anywhere in the repo, no
# `fail()` helper and therefore no entry in check-arms.py's population: its failing case had never
# been observed by any committed harness. `parallel-coding-governance.domain-rules.md:44-45` — "a
# gate you have only ever seen pass is an assertion about nothing." The debt was paid at the moment
# the gate's constant changed, because that is exactly when an unproven gate is most likely to be
# silently wrong.
#
# DISCIPLINES THIS FILE OBEYS:
#  * Every arm asserts the SPECIFIC MESSAGE or the SPECIFIC BYTES, never the exit code alone. An arm
#    that reads only `$?` reports success while exercising nothing.
#  * A1, A2 and A4 run the gate with NO override and read the limit back out of its own OK line. A
#    harness that exports its own MAX_BYTES tests the override path every time and never once
#    observes the SHIPPED ceiling — the arms would stay green through any edit to the default.
#    Only A5 sets the environment, because exercising the override is its whole purpose.
#  * A12 compares the record KEY against a hand-written literal, never against the gate's own
#    derivation. `--bump` writes the key and the ratchet reads it back through the same code, so the
#    round-trip is green whatever the key is: unit 1 shipped machine-ABSOLUTE keys through a fully
#    green gate on exactly that path.
#  * Fixtures are batched into one scratch dir. Nothing writes into the real tree — in particular no
#    arm may touch the tracked tools/template-size-highwater.txt.
#  * PASS prints after the LAST arm.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE="tools/check-template-size.sh"
TEMPLATE="parallel-coding-governance.template.md"
fails=0
TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT

mkfile() { head -c "$1" /dev/zero | tr '\0' 'x' > "$2"; }

say_ok()   { printf 'arm ok    %s\n' "$1"; }
say_fail() { fails=$((fails+1)); printf 'arm FAIL  %s — %s\n' "$1" "$2"; }

# expect_out <label> <expected-substring> <expected-exit> <command…>
expect_out() {
  local label=$1 want=$2 code=$3; shift 3
  local out rc
  out=$("$@" 2>&1); rc=$?
  if [ "$rc" != "$code" ]; then
    say_fail "$label" "expected exit $code, got $rc"; printf '%s\n' "$out" | sed 's/^/      /'; return
  fi
  case "$out" in
    *"$want"*) say_ok "$label" ;;
    *) say_fail "$label" "expected to see: $want"; printf '%s\n' "$out" | sed 's/^/      /' ;;
  esac
}

# expect_absent <label> <forbidden-substring> <expected-exit> <command…>
expect_absent() {
  local label=$1 nope=$2 code=$3; shift 3
  local out rc
  out=$("$@" 2>&1); rc=$?
  if [ "$rc" != "$code" ]; then
    say_fail "$label" "expected exit $code, got $rc"; printf '%s\n' "$out" | sed 's/^/      /'; return
  fi
  case "$out" in
    *"$nope"*) say_fail "$label" "did NOT expect to see: $nope"; printf '%s\n' "$out" | sed 's/^/      /' ;;
    *) say_ok "$label" ;;
  esac
}

# The SHIPPED ceiling, read back out of the gate's own OK line rather than declared here.
LIMIT=$(bash "$GATE" 2>/dev/null | sed -n 's|.*/ \([0-9][0-9]*\) bytes.*|\1|p')
case "$LIMIT" in
  ''|*[!0-9]*) printf 'harness FAILED — could not read the shipped limit from the gate OK line\n'; exit 2 ;;
esac
printf 'harness    shipped limit read from the gate: %s\n' "$LIMIT"

# --- A0 · the SHIPPED ceiling, pinned to a literal ------------------------------------------
# Deriving the limit (above) is right for the boundary arms — it keeps them honest about the
# override paths — but it means NO arm pins the number itself. Mutating the default to 131072 or
# to 40000 leaves every other arm green in both directions, on the one constant this whole build
# was convened to change. This arm is the literal, and it is deliberately the only one.
EXPECT_LIMIT=49152
if [ "$LIMIT" = "$EXPECT_LIMIT" ]; then
  say_ok "A0 the shipped ceiling is $EXPECT_LIMIT"
else
  say_fail "A0 the shipped ceiling is $EXPECT_LIMIT" \
    "the gate reports $LIMIT — the ceiling moved and no other arm in this file would notice"
fi

# --- A1 · a file of exactly MAX_BYTES ----------------------------------------------------------
mkfile "$LIMIT" "$TMP/at"
expect_out "A1 at the limit exits 0" "template-size OK" 0 bash "$GATE" "$TMP/at"

# --- A2 · a file of MAX_BYTES + 1, message names the overage -------------------------------------
mkfile "$((LIMIT + 1))" "$TMP/over"
expect_out "A2 one byte over reds, naming the overage" \
  "the file is over its size budget" 1 bash "$GATE" "$TMP/over"

# --- A3 · a missing path -------------------------------------------------------------------------
expect_out "A3 a missing subject exits 2" \
  "the file to measure does not exist" 2 bash "$GATE" "$TMP/no-such-file"

# --- A4 · CRLF at exactly MAX_BYTES normalized bytes ---------------------------------------------
# The gate strips CR before measuring so a Windows autocrlf smudge cannot inflate the count. On this
# fleet that smudge is the normal state, so this arm guards what the gate was actually written for.
{ head -c "$((LIMIT - 1))" /dev/zero | tr '\0' 'x'; printf '\n'; } > "$TMP/lf"
sed 's/$/\r/' "$TMP/lf" > "$TMP/crlf"
expect_out "A4 CRLF at the limit still exits 0" "template-size OK" 0 bash "$GATE" "$TMP/crlf"

# --- A5 · the MAX_BYTES override, BOTH directions -------------------------------------------------
mkfile 1000 "$TMP/mid"
expect_out "A5a env override below the size reds" \
  "the file is over its size budget" 1 env MAX_BYTES=999 bash "$GATE" "$TMP/mid"
expect_out "A5b env override above the size passes" \
  "template-size OK" 0 env MAX_BYTES=1001 bash "$GATE" "$TMP/mid"

# --- A6/A7 · the ratchet, keyed by measured file ---------------------------------------------------
HW="$TMP/hw"
mkfile 1000 "$TMP/subj"
bash "$GATE" "$TMP/subj" 49152 "$HW" --bump >/dev/null 2>&1
expect_absent "A7 at the recorded high-water: no warn" "TEMPLATE-SIZE WARN" 0 \
  bash "$GATE" "$TMP/subj" 49152 "$HW"
mkfile 1001 "$TMP/subj"
# S2's A6 row requires the line to NAME H, the size and the delta — not merely to carry the
# marker. Matching the marker alone left the arm green when the numbers were removed.
expect_out "A6 one byte past the high-water warns AND exits 0" \
  "1000 -> 1001 (+1)" 0 bash "$GATE" "$TMP/subj" 49152 "$HW"

# --- A8 · --bump rewrites the subject's row and reports the delta -----------------------------------
expect_out "A8 --bump re-records and names the delta" \
  "high-water 1000 -> 1001 (1 bytes)" 0 bash "$GATE" "$TMP/subj" 49152 "$HW" --bump
bumped=$(awk -F'\t' -v k="$TMP/subj" '$1 == k { print $2 }' "$HW" | tr -d '[:space:]')
if [ "$bumped" = "1001" ]; then
  say_ok "A8b the row now holds the measured size"
else
  say_fail "A8b the row now holds the measured size" "expected 1001, record holds '$bumped'"
fi

# --- A9 · a bump on one subject leaves the other subject's row byte-identical -------------------------
# THE arm that proves the KEYING. A6-A8 are all satisfiable by the single un-keyed number S8 forbids;
# only this one distinguishes them. Two consumers ride this gate ~14 KB apart, so a shared value can
# never warn for the smaller and a --bump on it makes the larger warn on every run forever.
mkfile 500 "$TMP/other"
bash "$GATE" "$TMP/other" 49152 "$HW" --bump >/dev/null 2>&1
before=$(awk -F'\t' -v k="$TMP/subj" '$1 == k { print $2 }' "$HW" | tr -d '[:space:]')
mkfile 900 "$TMP/other"
bash "$GATE" "$TMP/other" 49152 "$HW" --bump >/dev/null 2>&1
after=$(awk -F'\t' -v k="$TMP/subj" '$1 == k { print $2 }' "$HW" | tr -d '[:space:]')
if [ -n "$before" ] && [ "$before" = "$after" ]; then
  say_ok "A9 bumping one subject leaves the other row untouched"
else
  say_fail "A9 bumping one subject leaves the other row untouched" \
    "the other subject's row moved '$before' -> '$after'"
fi

# --- A10 · the record is absent ----------------------------------------------------------------------
# The two ratchet-degenerate branches share the `TEMPLATE-SIZE no-ratchet` prefix, so asserting
# that alone does not distinguish the branch each arm names — deleting either branch left the
# other arm green. Each now asserts the clause unique to its own branch.
expect_out "A10 an absent RECORD says so and exits 0" \
  "no high-water record at" 0 bash "$GATE" "$TMP/subj" 49152 "$TMP/definitely-absent"
printf '%s\t%d\n' "some/other/subject.md" 123 > "$TMP/hw-norow"
expect_out "A10b a record with no ROW for this subject says so and exits 0" \
  "has no row in" 0 bash "$GATE" "$TMP/subj" 49152 "$TMP/hw-norow"

# --- A11 · the record exists but this subject's row is not a number --------------------------------------
printf '%s\tnot-a-number\n' "$TMP/subj" > "$TMP/hw-bad"
expect_out "A11 a non-numeric row is a NAMED failure, not a shell error" \
  "the high-water record holds a non-numeric value for" 3 \
  bash "$GATE" "$TMP/subj" 49152 "$TMP/hw-bad"

# --- A12 · the record key of a repo-internal subject is the literal repo-relative path ------------------
# Compared against a hand-written string on purpose. Asking the gate what the key SHOULD be re-derives
# the bug this arm exists for: unit 1's keys landed machine-absolute because `git rev-parse
# --show-toplevel` and `pwd` answer different path forms, and the write/read round-trip agreed anyway.
HWK="$TMP/hw-key"
bash "$GATE" "$TEMPLATE" 49152 "$HWK" --bump >/dev/null 2>&1
key=$(cut -f1 "$HWK" | head -1)
if [ "$key" = "$TEMPLATE" ]; then
  say_ok "A12 the record key is the literal repo-relative path"
else
  say_fail "A12 the record key is the literal repo-relative path" \
    "expected exactly '$TEMPLATE', record holds '$key'"
fi

# --- the tracked record was never touched --------------------------------------------------------------
if git diff --quiet -- tools/template-size-highwater.txt 2>/dev/null; then
  say_ok "harness left the tracked high-water record unmodified"
else
  say_fail "harness left the tracked high-water record unmodified" \
    "tools/template-size-highwater.txt differs from the index — an arm wrote into the real tree"
fi

if [ "$fails" -ne 0 ]; then
  printf 'check-template-size.test.sh FAILED — %d arm(s)\n' "$fails"
  exit 1
fi
printf 'PASS — check-template-size.test.sh: every arm held\n'
