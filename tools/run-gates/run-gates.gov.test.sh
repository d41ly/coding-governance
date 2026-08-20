#!/usr/bin/env bash
# run-gates.gov.test.sh — the GOV-ONLY arms of the run-gates canary. the run-gates promotion spec's S1.
#
# WHY THIS FILE EXISTS, AND WHY IT IS NOT IN THE KIT PAYLOAD. `run-gates.test.sh` SHIPS: once
# the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` makes run-gates a deployable kit, an adopter's emitted manifest runs it in
# THEIR tree. So the shipped canary may assert only what is true in ANY tree. Sibling units want
# arms that are keyed on THIS repo's corpus instead — the chunking unit's every-leg-carries-a-chunk
# assertion over gov's six declared chunk names, and the push-boundary unit's guard pin on a named
# gov leg. (A third was reserved here and is now CUT: the reuse unit's network-calling leg names.
# TOOL-aPacedTurnstile-16's re-scope ran that predicate over the real manifest for the first time,
# matched six legs and found every one of them hermetic, so there is no population to pin. The
# reservation is removed rather than left standing, because a header naming an arm nobody will write
# is the same rot in the file that exists to refuse it.) In an adopter tree the manifest
# is seeded EMPTY and emitted from descriptors with no chunk key, and gov's legs do not exist, so
# every one of those arms would red on arrival. That is
# `memory/gotchas/pin-copied-from-another-corpus.md`, the class run-gates' own spec refuses by name
# when it declines to seed an adopter with gov's leg names.
#
# The precedent is settled: tools/memory-recall/kit.toml withholds check-recall.py, recall-fixture
# .json and test_recall_floor.py from the payload with a `project-owned` rule, for the same reason
# in the same words — arms keyed on this repo's own record ids are meaningless in another tree. This
# file is withheld the same way, is a leg in gov's own tools/gate-legs.json, and carries an
# [[exempt_leg]] row in tools/govkit/registry.toml. It is deliberately NOT a [[gate_leg]] row in
# tools/run-gates/kit.toml: a descriptor row naming a leg that ships nowhere is the shape the
# deployer's selfcheck reds on, and the descriptor's FOUR rows are the legs the kit SHIPS.
#
# THE REFUSAL BELOW IS THE POINT. A gov-only harness that quietly SUCCEEDS against a foreign corpus
# is the split failing open: every arm here would pass by finding nothing, and the next unit to add
# one would inherit a green that means nothing. So this file asserts it is running in the corpus it
# was written for, and exits 2 — not 0 — when it is not.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "gov-canary: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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
PYBIN=$(resolve_python) || { echo "gov-canary: no usable python"; exit 2; }

fail=0
a=0                          # executed assertions, printed at the end against the pinned floor
FLOOR_ASSERTIONS=9

# The manifest, derived the same way run-gates.sh derives it. GATE_LEGS still outranks it, which is
# what lets the fixture arms below drive this file without touching the real bar.
# Normalised through the SAME `cd ... && pwd` chain on both sides: under MSYS `git rev-parse
# --show-toplevel` answers `C:/...` and `pwd` answers `/c/...`, and a strip across the two
# flavours leaves an ABSOLUTE path that resolves to nothing.
KITDIR=$(cd "$(dirname "$0")" && pwd)
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"

# ---- G0. THE CORPUS GATE -------------------------------------------------------------------------
# Every arm in this file is keyed on gov's own manifest. Refuse — loudly, exit 2 — rather than pass,
# when the manifest is not gov's. `GATE_LEGS` pointing at a fixture is the ordinary way that happens.
#
# The witness is a leg NAME this repo has carried since long before this kit existed and that no
# adopter's emitted manifest can contain, because a target's leg list is emitted from the selected
# kits' [[gate_leg]] blocks and none of them emits a leg by this name.
WITNESS='memory hygiene'
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)
sys.exit(0 if any(l.get("name") == sys.argv[2] for l in legs) else 1)
' "$LEGS_FILE" "$WITNESS"; then
  echo "gov-canary: REFUSING — $LEGS_FILE carries no leg named '$WITNESS', so this is not the corpus"
  echo "gov-canary: these arms were written for. This harness is gov-only by design (see its header);"
  echo "gov-canary: it is withheld from the kit payload and must never report a green it did not earn."
  exit 2
fi

# ---- G1. the tail contract's other half ----------------------------------------------------------
# the run-gates promotion spec's S5 widens every report tail to TWO spaces so a reader splits the remainder
# on a double space and recovers the bare leg name. That split is only unambiguous while no leg NAME
# contains a double space. Gov's manifest is the population this repo controls, so the arm lives here.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
bad = [l["name"] for l in json.load(open(sys.argv[1])) if "  " in l.get("name", "")]
if bad:
    print("gov-canary: leg name(s) contain a DOUBLE SPACE, which makes the report tail split"
          " ambiguous: " + "; ".join(bad)); sys.exit(1)
' "$LEGS_FILE"; then fail=1; fi

# ---- G2. the runner and both harnesses derive the manifest identically ---------------------------
# SOURCE PARITY, not a re-derivation. An earlier draft of this arm recomputed the derivation inline
# and compared the two answers, which is `memory/gotchas/two-answers-to-one-question.md` inside the
# arm written to prevent it — and it duly disagreed with itself, because the copy carried the
# pre-normalisation strip. What is asserted instead is that the three files carry the SAME two
# derivation lines, byte for byte. One answer, checked; the pattern the resolver parity gate uses.
a=$((a+1))
read_derivation() {   # FILE -> the two derivation lines, whitespace-normalised
  grep -hE '^KITDIR=|^ROOTN=|^KITREL=|^LEGS_FILE=' "$1"
}
ref=$(read_derivation "$KITREL/run-gates.sh")
if [ -z "$ref" ]; then
  echo "gov-canary: $KITREL/run-gates.sh carries no manifest derivation to compare against — the"
  echo "gov-canary: arm cannot pass by finding nothing, so this is a refusal"
  fail=1
else
  for f in "$KITREL/run-gates.test.sh" "$KITREL/run-gates.gov.test.sh"; do
    if [ "$(read_derivation "$f")" != "$ref" ]; then
      echo "gov-canary: $f derives the leg manifest differently from $KITREL/run-gates.sh, so it would"
      echo "gov-canary: grade a different file than the bar runs:"
      printf 'gov-canary:   runner: %s
' "$ref"
      printf 'gov-canary:   %s: %s
' "$f" "$(read_derivation "$f")"
      fail=1
    fi
  done
fi

# ---- G3. the push boundary FORCES the full bar ---------------------------------------------------
# MOVED here from the shipped canary by the closing review (D6). It asserts a fact about GOV's tree:
# an adopter has no `.githooks/pre-push` unless they also took the push-main kit, which is NOT in the
# default selection, so in the shipped half this arm was red on arrival in every default install.
# The property it guards is still gov's and still worth guarding — a scoped authoritative run would
# mean no run ever executes every leg against the tree that actually lands.
a=$((a+1))
grep -q '^export GATE_FULL=1$' "$ROOT/.githooks/pre-push"   || { echo "gov-canary: .githooks/pre-push does not force GATE_FULL — the authoritative run would be diff-scoped"; fail=1; }

# ---- G4/G5. THE CHARTER STILL DESCRIBES THE RUNNER ------------------------------------------------
# Two claims `AGENTS.md` made that the profile-table unit falsified, and NOTHING ELSE observes either:
# the playbook-parity gate grades the playbook FILES rather than this repo's rendered charter, and
# drift-audit's charter signal joins leg SCRIPT PATHS. A charter that goes on stating a width formula
# the runner no longer uses is precisely the claim that unit exists to remove, so it is armed here —
# in gov's own half, because an adopter has no `AGENTS.md` of this shape and the arm would red on
# absence rather than on behaviour.
#
# BOTH HALVES OF EACH, and the positive half is why. A negative-only search passes when the sentence
# it is guarding is DELETED, which is the same green as a sentence that was never wrong. The first
# draft of this pair armed only the figure; the fix for it RELOCATED the defect to the formula half
# and every criterion stayed green.
CHARTER="$ROOT/AGENTS.md"
a=$((a+1))
if [ ! -f "$CHARTER" ]; then
  echo "gov-canary: $CHARTER is absent, so the charter arms would pass by finding nothing — this is a refusal"
  fail=1
else
  # G4 — the stale MEASUREMENT. The pair that replaced it is a real reading of the current bar.
  a=$((a+1))
  if grep -qE '335s|~?95s' "$CHARTER"; then
    echo "gov-canary: $CHARTER still carries the retired timing figures (335s / 95s); the measured pair for the current bar is 873 s wall against a 4018 s leg-sum"; fail=1
  fi
  a=$((a+1))
  { grep -q '873 s' "$CHARTER" && grep -q '4018 s' "$CHARTER"; } \
    || { echo "gov-canary: $CHARTER no longer states the measured pair (873 s wall against a 4018 s leg-sum), so the negative half above would pass on a DELETED sentence"; fail=1; }
  # G5 — the stale WIDTH FORMULA, in the backticked spelling the file actually uses. The runner reads
  # its width from a declared table now, so a charter naming a formula is telling a session something
  # it cannot verify anywhere in the tree.
  a=$((a+1))
  if grep -qF 'min(8, nproc)' "$CHARTER"; then
    echo "gov-canary: $CHARTER still states the built-in width formula; the width is declared in tools/run-gates/gate-profiles.txt and read from there"; fail=1
  fi
  a=$((a+1))
  grep -qF 'tools/run-gates/gate-profiles.txt' "$CHARTER" \
    || { echo "gov-canary: $CHARTER does not name tools/run-gates/gate-profiles.txt as the source of the pool width, so the negative half above would pass on a DELETED sentence"; fail=1; }
fi

# ---- verdict -------------------------------------------------------------------------------------
# The executed assertion count, in the shape tools/check-testsuite-counts.sh reads, against a floor
# declared here. the run-gates promotion spec's S11: this file gets a counter and a floor at BIRTH, so it
# never needs a row in memory/project/testsuite-count-waivers.txt.
[ "$a" -ge "$FLOOR_ASSERTIONS" ] || { echo "gov-canary: executed $a assertions, below the pinned floor $FLOOR_ASSERTIONS"; fail=1; }
if [ "$fail" = 0 ]; then
  echo "PASS ($a assertions)"
  exit 0
fi
echo "gov-canary: FAIL ($a assertions)"
exit 1
