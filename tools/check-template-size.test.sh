#!/usr/bin/env bash
# check-template-size.test.sh — self-test for <prefix>/check-template-size.sh.
#
#   bash <prefix>/check-template-size.test.sh
#
# Exit 0 = every arm held · 1 = an arm failed · 2 = the harness could not set up.
#
# WHY THIS EXISTS. Until this file landed, the gate had no test anywhere in the repo, no
# `fail()` helper and therefore no entry in check-arms.py's population: its failing case had never
# been observed by any committed harness. the charter's `[gate]` practice — "a
# gate you have only ever seen pass is an assertion about nothing." The debt was paid at the moment
# the gate's constant changed, because that is exactly when an unproven gate is most likely to be
# silently wrong.
#
# THE DECLARATION IS READ THROUGH THE POLICY READER (TOOL-dGroundRules-9). The gate no longer parses
# the limits file: the policy kit's budgets.py does, at the landed revision of the subject's
# repository, and the switch `budgets.enforce` with its pins decides whether a breach refuses. So the
# resolution arms run in a SCRATCH REPOSITORY with no remote, whose local main is its landed
# revision: a limits file at this install's own prefix, a policy file, both committed. The retired
# channels — the positional limit, MAX_BYTES and the limits-path positional — are each asserted to be
# refused or ignored, never honoured.
#
# DISCIPLINES THIS FILE OBEYS:
#  * Every arm asserts the SPECIFIC MESSAGE or the SPECIFIC BYTES, never the exit code alone. An arm
#    that reads only `$?` reports success while exercising nothing.
#  * A0 runs the gate over the tracked template and reads the limit back out of its own OK line, so
#    the SHIPPED ceiling is pinned once, against a literal.
#  * A12 compares the record KEY against a hand-written literal, never against the gate's own
#    derivation. `--bump` writes the key and the ratchet reads it back through the same code, so the
#    round-trip is green whatever the key is: unit 1 shipped machine-ABSOLUTE keys through a fully
#    green gate on exactly that path.
#  * Fixtures are batched into one scratch dir. Nothing writes into the real tree — in particular no
#    arm may touch the tracked <prefix>/template-size-highwater.txt.
#  * PASS prints after the LAST arm.
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-template-size.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE="${PFX}check-template-size.sh"
TEMPLATE="coding-governance-agents.template.md"
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
# The one arm that pins the number itself: mutating the template's declared row leaves every
# scratch-repository arm below green, since none of them reads the tracked declaration.
EXPECT_LIMIT=49152
if [ "$LIMIT" = "$EXPECT_LIMIT" ]; then
  say_ok "A0 the shipped ceiling is $EXPECT_LIMIT"
else
  say_fail "A0 the shipped ceiling is $EXPECT_LIMIT" \
    "the gate reports $LIMIT — the ceiling moved and no other arm in this file would notice"
fi
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fails:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fails:-0}" = 0 ] && exit 0; exit 1; fi

# --- the scratch repository ----------------------------------------------------------------------
# `build_scratch_repo <limits rows> <policy text>` rebuilds it: the limits file at this install's prefix, where
# the policy reader reads it, and the policy file, committed on main with no remote. The subjects are
# census names — `AGENTS.md`, the build method's path — so the reader answers them from this
# repository's rows; `notes.md` is no census row and keeps the gate's own default.
S="$TMP/repo"
build_scratch_repo() {
  rm -rf "$S"
  mkdir -p "$S/${PFX}" "$S/.governance" "$S/memory/guides" || exit 2
  printf '%b' "$1" > "$S/${PFX}template-size-limits.txt"
  printf '%b' "$2" > "$S/.governance/policy.toml"
  git -C "$S" init -q && git -C "$S" symbolic-ref HEAD refs/heads/main \
    && git -C "$S" add -A && git -C "$S" -c user.name=t -c user.email=t@t.test -c commit.gpgsign=false commit -qm fixture \
    || { printf 'harness FAILED — could not build the scratch repository\n'; exit 2; }
}
# The gate run inside the scratch repository, by its absolute path.
run_gate_in() { (cd "$S" && bash "$ROOT/$GATE" "$@"); }
WARN='[budgets]\nenforce = "warn"\n'
REFUSE='[budgets]\nenforce = "refuse"\n'

# --- A14-A19 · the declaration, read through the policy reader ----------------------------------
build_scratch_repo 'AGENTS.md\t5000\n' "$WARN"
mkfile 100 "$S/AGENTS.md"
mkfile 100 "$S/notes.md"
expect_out "A14 the DECLARED row supplies the limit" "/ 5000 bytes" 0 run_gate_in AGENTS.md
expect_out "A15 a positional limit is refused as retired, never honoured" \
  "a retired positional was given, and the limit and the limits path are read through the policy kit's budgets.py now; pass the subject, an empty second argument and the record (given" \
  2 run_gate_in AGENTS.md 9999
expect_out "A15b a limits-path positional is refused as retired" \
  "a retired positional was given" 2 run_gate_in AGENTS.md "" "" "$TMP/limits"
out=$(cd "$S" && MAX_BYTES=999999 bash "$ROOT/$GATE" AGENTS.md 2>&1)
case "$out" in
  *"/ 5000 bytes"*) say_ok "A16 the environment no longer moves a declared limit" ;;
  *) say_fail "A16 the environment no longer moves a declared limit" "expected 5000; got: $out" ;;
esac
out=$(cd "$S" && MAX_BYTES=4242 bash "$ROOT/$GATE" notes.md 2>&1)
case "$out" in
  *"/ 49152 bytes"*) say_ok "A17 an undeclared subject ignores the retired environment" ;;
  *) say_fail "A17 an undeclared subject ignores the retired environment" "expected 49152; got: $out" ;;
esac
expect_out "A18 an undeclared subject falls to the hard default" "/ 49152 bytes" 0 run_gate_in notes.md
build_scratch_repo 'AGENTS.md\tnot-a-number\n' "$WARN"
mkfile 100 "$S/AGENTS.md"
expect_out "A19 a non-numeric declared limit is a NAMED failure" \
  "the declared size limit for this subject could not be read, so nothing is compared: " 5 run_gate_in AGENTS.md
expect_out "A19b ...naming the row the policy reader refused" "row is not a number: 'not-a-number'" 5 run_gate_in AGENTS.md
build_scratch_repo 'AGENTS.md\t5000\n' '[budgets]\n"AGENTS.md" = 6000\n'
mkfile 100 "$S/AGENTS.md"
expect_out "A19c a cap held in both homes is check 5, naming both" "budgets.AGENTS.md is held in both homes" 5 run_gate_in AGENTS.md
build_scratch_repo '# no rows\n' '[budgets]\n"AGENTS.md" = 6000\n'
mkfile 100 "$S/AGENTS.md"
expect_out "A19d the policy file's value takes the row's place" "/ 6000 bytes" 0 run_gate_in AGENTS.md

# --- A20/A21 · THE PAIR TERM (TOOL-aHoistedPass-3) ----------------------------------------------
# A subject may state its own budget in its own prose, and the ceiling is ALSO in a declaration.
# Check 6 reds when the two disagree — under `warn` too, since it is correctness and not size.
BM="memory/guides/BUILD-METHOD.md"
build_scratch_repo "$BM\t30000\n" "$WARN"
printf '**Budget: <=27648 bytes, <=350 lines**\nbody\n' > "$S/$BM"
expect_out "A20 a budget line disagreeing with its declared row reds at check 6, under warn" \
  "the subject states its own budget and disagrees with its declaration" 6 \
  run_gate_in "$BM" "" "$TMP/hw-pair"
# A21 is the half that keeps the term from being disarmed by a rewrite: a prose figure this gate
# cannot parse as BYTES is not equal to any declared row, so it reds through the same branch rather
# than falling silently out of the comparison.
build_scratch_repo "$BM\t27648\n" "$WARN"
printf '**Budget: <=27 KB, <=350 lines**\nbody\n' > "$S/$BM"
expect_out "A21 a budget line the gate cannot parse as bytes reds too, naming it" \
  "'no bytes figure'" 6 run_gate_in "$BM" "" "$TMP/hw-pair"
# THE CONTROL, and it is the arm that proves the two above are not vacuous. A subject whose prose
# AGREES with its row passes, and a subject carrying no budget line at all is never compared — which
# is the second guard, and the reason the shipped subjects without one are untouched by this term.
printf '**Budget: <=27648 bytes, <=350 lines**\nbody\n' > "$S/$BM"
expect_absent "A22 an agreeing pair is not a check 6" "check 6" 0 run_gate_in "$BM" "" "$TMP/hw-pair"
build_scratch_repo 'AGENTS.md\t4096\n' "$WARN"
mkfile 100 "$S/AGENTS.md"
expect_absent "A23 a declared subject with NO budget line is never compared" "check 6" 0 \
  run_gate_in AGENTS.md "" "$TMP/hw-pair"

# --- A1/A2 · the boundary, under each value of the switch ---------------------------------------
build_scratch_repo 'AGENTS.md\t5000\n' "$REFUSE"
mkfile 5000 "$S/AGENTS.md"
expect_out "A1 at the limit exits 0" "template-size OK" 0 run_gate_in AGENTS.md
mkfile 5001 "$S/AGENTS.md"
expect_out "A2 one byte over under refuse reds, naming the overage" \
  "the file is over its size budget" 1 run_gate_in AGENTS.md
expect_out "A2b ...and the rule that set the mode" "budgets.enforce is refuse" 1 run_gate_in AGENTS.md
build_scratch_repo 'AGENTS.md\t5000\n' "$WARN"
mkfile 5001 "$S/AGENTS.md"
expect_out "A2w one byte over under warn prints BUDGET WARN and exits 0" \
  "BUDGET WARN — AGENTS.md · AGENTS.md · 5001 bytes over 5000" 0 run_gate_in AGENTS.md
expect_absent "A2x ...and is not a check 2" "check 2" 0 run_gate_in AGENTS.md
build_scratch_repo 'AGENTS.md\t5000\n' '[budgets]\nenforce = "warn"\npinned = ["AGENTS.md"]\n'
mkfile 5001 "$S/AGENTS.md"
expect_out "A2p a pinned subject refuses under warn, naming budgets.pinned" \
  "budgets.pinned names it" 1 run_gate_in AGENTS.md

# --- A24 · no python launcher: an over-cap subject refuses at check 5 (TOOL-dGroundRules-25 S35) --
# Every launcher name on PATH answers as the Microsoft Store stub does, exit 9009, and no override is
# set, so no policy kit can read the declaration: the gate's `fail 5`, never a pass unmeasured.
mkdir -p "$TMP/nopy"
for _np in python3 python py; do printf '#!/usr/bin/env bash\nexit 9009\n' > "$TMP/nopy/$_np"; chmod +x "$TMP/nopy/$_np"; done
build_scratch_repo 'AGENTS.md\t5000\n' "$REFUSE"
mkfile 5001 "$S/AGENTS.md"
expect_out "A24 with no python launcher an over-cap subject refuses at check 5" \
  "TEMPLATE-SIZE check 5 FAILED — the declared size limit for this subject could not be read, so nothing is compared: no python launcher resolved" \
  5 env -u GOV_PYTHON -u TEMPLATE_SIZE_PY PATH="$TMP/nopy:$PATH" bash -c 'cd "$1" && bash "$2" AGENTS.md' _ "$S" "$ROOT/$GATE"

# --- A3 · a missing path -------------------------------------------------------------------------
expect_out "A3 a missing subject exits 2" \
  "the file to measure does not exist" 2 bash "$GATE" "$TMP/no-such-file"

# --- A4 · CRLF at exactly the limit, normalized bytes --------------------------------------------
# The gate strips CR before measuring so a Windows autocrlf smudge cannot inflate the count. On this
# fleet that smudge is the normal state, so this arm guards what the gate was actually written for.
build_scratch_repo 'AGENTS.md\t5000\n' "$REFUSE"
{ head -c 4999 /dev/zero | tr '\0' 'x'; printf '\n'; } > "$TMP/lf"
sed 's/$/\r/' "$TMP/lf" > "$S/AGENTS.md"
expect_out "A4 CRLF at the limit still exits 0" "template-size OK" 0 run_gate_in AGENTS.md

# --- A6/A7 · the ratchet, keyed by measured file ---------------------------------------------------
# Subjects outside any census row, so the hard default applies and the ratchet alone is observed.
HW="$TMP/hw"
mkfile 1000 "$TMP/subj"
bash "$GATE" "$TMP/subj" "" "$HW" --bump >/dev/null 2>&1
expect_absent "A7 at the recorded high-water: no warn" "TEMPLATE-SIZE WARN" 0 \
  bash "$GATE" "$TMP/subj" "" "$HW"
mkfile 1001 "$TMP/subj"
# S2's A6 row requires the line to NAME H, the size and the delta — not merely to carry the
# marker. Matching the marker alone left the arm green when the numbers were removed.
expect_out "A6 one byte past the high-water warns AND exits 0" \
  "1000 -> 1001 (+1)" 0 bash "$GATE" "$TMP/subj" "" "$HW"

# --- A8 · --bump rewrites the subject's row and reports the delta -----------------------------------
expect_out "A8 --bump re-records and names the delta" \
  "high-water 1000 -> 1001 (1 bytes)" 0 bash "$GATE" "$TMP/subj" "" "$HW" --bump
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
bash "$GATE" "$TMP/other" "" "$HW" --bump >/dev/null 2>&1
before=$(awk -F'\t' -v k="$TMP/subj" '$1 == k { print $2 }' "$HW" | tr -d '[:space:]')
mkfile 900 "$TMP/other"
bash "$GATE" "$TMP/other" "" "$HW" --bump >/dev/null 2>&1
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
  "no high-water record at" 0 bash "$GATE" "$TMP/subj" "" "$TMP/definitely-absent"
printf '%s\t%d\n' "some/other/subject.md" 123 > "$TMP/hw-norow"
expect_out "A10b a record with no ROW for this subject says so and exits 0" \
  "has no row in" 0 bash "$GATE" "$TMP/subj" "" "$TMP/hw-norow"

# --- A13 · --bump cannot write, and says so instead of reporting a bump it did not make -------
expect_out "A13 an unwritable record is a named failure, not a false BUMP" \
  "the high-water record could not be written, so no bump was recorded" 4 \
  bash "$GATE" "$TMP/subj" "" "$TMP/no-such-dir/hw" --bump

# --- A11 · the record exists but this subject's row is not a number --------------------------------------
printf '%s\tnot-a-number\n' "$TMP/subj" > "$TMP/hw-bad"
expect_out "A11 a non-numeric row is a NAMED failure, not a shell error" \
  "the high-water record holds a non-numeric value for" 3 \
  bash "$GATE" "$TMP/subj" "" "$TMP/hw-bad"

# --- A12 · the record key of a repo-internal subject is the literal repo-relative path ------------------
# Compared against a hand-written string on purpose. Asking the gate what the key SHOULD be re-derives
# the bug this arm exists for: unit 1's keys landed machine-absolute because `git rev-parse
# --show-toplevel` and `pwd` answer different path forms, and the write/read round-trip agreed anyway.
HWK="$TMP/hw-key"
bash "$GATE" "$TEMPLATE" "" "$HWK" --bump >/dev/null 2>&1
key=$(cut -f1 "$HWK" | head -1)
if [ "$key" = "$TEMPLATE" ]; then
  say_ok "A12 the record key is the literal repo-relative path"
else
  say_fail "A12 the record key is the literal repo-relative path" \
    "expected exactly '$TEMPLATE', record holds '$key'"
fi

# --- the tracked record was never touched --------------------------------------------------------------
if git diff --quiet -- ${PFX}template-size-highwater.txt 2>/dev/null; then
  say_ok "harness left the tracked high-water record unmodified"
else
  say_fail "harness left the tracked high-water record unmodified" \
    "${PFX}template-size-highwater.txt differs from the index — an arm wrote into the real tree"
fi

if [ "$fails" -ne 0 ]; then
  printf 'check-template-size.test.sh FAILED — %d arm(s)\n' "$fails"
  exit 1
fi
printf 'PASS — check-template-size.test.sh: every arm held\n'
