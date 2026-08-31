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
# Raised from 12 by TOOL-aShardedFloor-2, which adds the shard-contract arms (forward cover and
# reverse declaration). Stated ABSOLUTELY, never as a delta.
FLOOR_ASSERTIONS=15

# The manifest, derived the same way run-gates.sh derives it. GATE_LEGS still outranks it, which is
# what lets the fixture arms below drive this file without touching the real bar.
# Normalised through the SAME `cd ... && pwd` chain on both sides: under MSYS `git rev-parse
# --show-toplevel` answers `C:/...` and `pwd` answers `/c/...`, and a strip across the two
# flavours leaves an ABSOLUTE path that resolves to nothing.
KITDIR=$(cd "$(dirname "$0")" && pwd)
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.toml}"
# AND THE SAME FALLBACK THE RUNNER MAKES. The canonical line above is byte-identical across
# all three files because the gov-only canary asserts exactly that -- but the runner does not
# STOP there: it falls back to the legacy pair when the TOML is absent or the resolved
# interpreter cannot import tomllib. A harness that resolved only the TOML would die with a
# FileNotFoundError in every JSON-only or pre-3.11 tree where the bar itself still runs
# happily, which is a shipped leg that reds on arrival for an adopter who did nothing wrong.
if [ -z "${GATE_LEGS:-}" ]; then
  if [ ! -f "$ROOTN/$LEGS_FILE" ] || ! "$PYBIN" -c "import tomllib" 2>/dev/null; then
    LEGS_FILE="$(dirname "$KITREL")/gate-legs.json"
  fi
fi
# THE SUITES GRADE WHAT THE BAR RUNS, whatever format that is. `LEGS_FILE` is the canonical
# derivation the gov-only canary asserts byte-for-byte across all three files, so it cannot branch;
# the branch happens HERE, once, and every reader below keeps its `json.load`. Normalising to a temp
# JSON is not a second spelling of the format -- it is the same leg objects, decoded -- and it is
# what stops these harnesses from grading gate-legs.json while the bar runs gate-legs.toml, which is
# precisely the divergence the parity arm exists to catch. Removed when the legacy pair goes.
LEGS_READ="$LEGS_FILE"
case "$LEGS_FILE" in
  *.toml)
    LEGS_READ=$(mktemp) || { echo "canary: cannot create a temp file to decode $LEGS_FILE" >&2; exit 2; }
    "$PYBIN" -c 'import sys, json, tomllib
d = tomllib.load(open(sys.argv[1], "rb"))
rows = d.get("leg") or []
for r in rows:
    # The JSON dialect these readers know spells the hold as `subject`; the TOML spells it `opt_in`.
    # Decoded here so a reader that pins a key set sees the shape it was written against.
    r.setdefault("subject", "kit" if r.get("opt_in") else "repo")
json.dump(rows, open(sys.argv[2], "w"))
' "$LEGS_FILE" "$LEGS_READ" || { echo "canary: cannot decode $LEGS_FILE" >&2; exit 2; }
    [ -s "$LEGS_READ" ] || { echo "canary: decoding $LEGS_FILE produced nothing — refusing rather than grading an empty population" >&2; exit 2; }
    trap 'rm -f "$LEGS_READ"' EXIT
    ;;
esac


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
' "$LEGS_READ" "$WITNESS"; then
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
' "$LEGS_READ"; then fail=1; fi

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
# THE PUSH BOUNDARY STILL OWES A TOTAL RUN, and this arm grades the OBLIGATION rather than the
# mechanism. It used to grep for a literal `export GATE_FULL=1` at column 0, which was exactly
# right while the hook forced unconditionally and became a false red the moment the hook started
# DECIDING. Deleting it outright was the one answer this could not take: it is the only executable
# statement anywhere that the authoritative run covers the whole bar, and removing the arm that
# guards a property in the same commit that weakens the property is gating the instance rather
# than the class.
#
# Two halves. The behavioural half — one arm per forcing predicate, plus the control proving a
# scoped run is ever chosen at all — lives in `.githooks/pre-push.test.sh`, where the hook is
# really driven. What stays here is the half that is about THIS repository: that the boundary can
# still force, and that the record it decides against is not further behind than its own bound.
grep -q 'export GATE_FULL=1' "$ROOT/.githooks/pre-push" \
  || { echo "gov-canary: .githooks/pre-push has no forcing path at all — the boundary can never demand a total run"; fail=1; }
a=$((a+1))
grep -qE '^GATE_FULL_MAX_LAG=[0-9]+' "$ROOT/.githooks/pre-push" \
  || { echo "gov-canary: the staleness bound is not a source constant in the hook — a policy an environment variable can change at the moment it binds is not a policy"; fail=1; }

# THE RECORD, when there is one. A fresh clone has none, and that is a legitimate state rather
# than a defect — the hook forces a full run there, which is the safe direction. So this arm
# SKIPS, loudly and countably, instead of reddening: a skip that looks like a pass is
# indistinguishable from coverage, and a red here would fail every clone on its first push.
a=$((a+1))
gc_rec="$(git rev-parse --git-dir)/gate-full-green"
if [ -f "$gc_rec" ]; then
  gc_sha=$(awk -F'\t' '$1=="sha"{print $2}' "$gc_rec" 2>/dev/null)
  gc_bound=$(grep -m1 -oE 'GATE_FULL_MAX_LAG=[0-9]+' "$ROOT/.githooks/pre-push" | grep -oE '[0-9]+')
  if [ -n "$gc_sha" ] && [ -n "$gc_bound" ] && git merge-base --is-ancestor "$gc_sha" HEAD 2>/dev/null; then
    gc_lag=$(git rev-list --count "$gc_sha..HEAD" 2>/dev/null || echo 0)
    [ "${gc_lag:-0}" -le "$gc_bound" ] \
      || echo "gov-canary: NOTE — the recorded full green is $gc_lag commits back, past the bound of $gc_bound, so the next push will force a total run (informational, not a failure)"
  fi
else
  echo "gov-canary: SKIP the recorded-green lag arm — no gate-full-green in this git dir yet, so there is no record to measure. The boundary forces a total run in exactly this state."
fi

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
  # G4 — THE MEASUREMENT, AND THIS ARM STOPPED PINNING ONE. It used to require the charter to state a
  # specific wall/leg-sum pair, and that pair went stale three times in two days: 335s/95s, then
  # 393s/3085s, then 4926 s of leg-sum with a 1565 s floor, then ~265 s once seven legs left the bar.
  # Each time the charter was CORRECTED and this canary red on the correction — a gate demanding that
  # a document keep a number no document can keep.
  #
  # The rule the charter itself states is "point at the source, or gate the pair". `<git-dir>/gate-ledger.tsv`
  # carries one row per leg with its own seconds and cannot go stale, so what is worth pinning is that
  # the charter SENDS a reader there. The retired-figures arm below stays and grows: a figure quoted as
  # current is the defect, whichever figure it is.
  a=$((a+1))
  if grep -qE '335s|~?95s|3085 s|393 s wall' "$CHARTER"; then
    echo "gov-canary: $CHARTER quotes a retired bar timing as if it were current (335s / 95s / 3085 s / 393 s wall); the bar's per-leg seconds live in <git-dir>/gate-ledger.tsv and prose beside a source that owns a number is the rule this arm exists to hold"; fail=1
  fi
  a=$((a+1))
  grep -q 'gate-ledger.tsv' "$CHARTER" || { echo "gov-canary: $CHARTER no longer sends a reader to <git-dir>/gate-ledger.tsv for the bar's per-leg seconds, so the negative half above would pass on a charter that says nothing about cost at all — silence and a correct pointer are not the same answer"; fail=1; }
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

# ---- G6. EVERY GOV LEG DECLARES A CEILING --------------------------------------------------------
# TOOL-aBoundedCeiling-1 S9. The RUNNER deliberately does not enforce this: it cannot tell a gov leg
# somebody forgot from an adopter leg the deployer has no business bounding, so it reports an
# unbounded count and refuses nothing. The requirement over THIS corpus lives here, which is the file
# allowed to hold a claim about this repository -- see this suite's header for why that split exists.
#
# WHAT THIS DOES NOT CHECK: whether a ceiling is the RIGHT number. It grades presence and shape only.
# A leg bounded at 99999 passes here and is still unbounded in every sense that matters; the number is
# argued in the spec and in the manifest, and no gate reads an argument.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)

bad = []
for l in legs:
    if not isinstance(l, dict):
        print("gov-canary: a leg row is not an object"); sys.exit(1)
    nm = l.get("name", "?")
    if "ceiling" not in l:
        bad.append("%s declares no ceiling, so it runs unbounded and a hang in it wedges the bar" % nm)
        continue
    c = l.get("ceiling")
    if isinstance(c, bool) or not isinstance(c, int) or c <= 0:
        bad.append("%s has ceiling %r, which is not a positive integer of seconds" % (nm, c))

# LIVENESS. An empty manifest, or one this predicate never selected, would report zero problems and
# read exactly like a fully-bounded corpus. Say so instead.
if not legs:
    print("gov-canary: the manifest carries no legs at all, so this arm graded nothing"); sys.exit(1)

if bad:
    print("gov-canary: %d of %d gov leg(s) are not bounded:" % (len(bad), len(legs)))
    for b in bad[:12]:
        print("  " + b)
    if len(bad) > 12:
        print("  ... and %d more" % (len(bad) - 12))
    sys.exit(1)
' "$LEGS_READ"; then
  fail=1
fi

# ---- G7. `memory hygiene` DECLARES NO GUARD, AND THAT IS LOAD-BEARING ----------------------------
# TOOL-aThawedCorpus-5 gave check 23 the `[ "$STAGED" = 0 ]` guard its four siblings carry, so the
# pre-commit leg no longer runs it at all. That is a deliberate COVERAGE REDUCTION, and its
# compensating control is that the push boundary still runs it: `.githooks/pre-push` always invokes
# `run-gates.sh` and only chooses between `GATE_FULL=1` and a scoped `GATE_BASE` run, while
# `run-gates.sh` skips a GUARDED leg whose pathspecs did not move against BASE.
#
# So the control holds only while this leg declares no guard. Add one and a scoped default-branch
# push skips check 23 outright, while pre-commit already skips it — the acceptance ledger would then
# be graded at neither boundary, with every gate green throughout. `TOOL-aThawedCorpus-2` proposed
# exactly that edit and was retired to preserve this property; nothing asserted it until now, which
# is the lockstep-invariant-without-a-guard shape. Round-1 diff review, F3.
#
# WHAT THIS DOES NOT CHECK: that the push boundary actually runs the leg. It grades one key on one
# row. The reachability argument lives in the checker's own header beside the exemption.
a=$((a+1))
if ! "$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("gov-canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)

rows = [l for l in legs if isinstance(l, dict) and l.get("name") == "memory hygiene"]

# LIVENESS. A renamed or deleted leg would make this arm select nothing and pass in silence, which
# reads exactly like a correctly unguarded leg. Say so instead.
if len(rows) != 1:
    print("gov-canary: expected exactly one leg named \"memory hygiene\", found %d, so this arm"
          " graded nothing" % len(rows))
    sys.exit(1)

if "guard" in rows[0]:
    print("gov-canary: the `memory hygiene` leg declares a guard (%r)." % (rows[0]["guard"],))
    print("  TOOL-aThawedCorpus-5 removed check 23 from the pre-commit leg, and its compensating")
    print("  control is that this leg runs on BOTH of .githooks/pre-push branches, which is true")
    print("  only while it is unguarded. With a guard, a scoped push skips it and the acceptance")
    print("  ledger is graded at neither boundary. Remove the guard, or retire that exemption.")
    sys.exit(1)
' "$LEGS_READ"; then
  fail=1
fi

# ---- verdict -------------------------------------------------------------------------------------
# The executed assertion count, in the shape tools/check-testsuite-counts.sh reads, against a floor
# declared here. the run-gates promotion spec's S11: this file gets a counter and a floor at BIRTH, so it
# never needs a row in memory/project/testsuite-count-waivers.txt.
# EVERY LEG OF GOV'S REAL MANIFEST CARRIES A CHUNK, and its value is one of the six declared
# names. This is the assertion that cannot ship: an adopter's manifest is seeded empty and emitted
# from descriptors, so a shipped arm demanding a chunk key would red on arrival in every install.
# It is UNCONDITIONAL over the manifest rather than a spot check — a new leg added without a key
# would otherwise fall into `default` silently and report under a chunk nobody declared.
a=$((a+1))
"$PYBIN" -c '
import json, sys
SIX = {"records", "product", "wiring", "declarations", "selftests", "e2e"}
legs = json.load(open(sys.argv[1]))
bad = [l.get("name", "?") for l in legs if l.get("chunk") not in SIX]
if bad:
    print("gov-canary: leg(s) with no chunk key, or a value outside the six declared names %s: %s"
          % (sorted(SIX), ", ".join(bad)))
    sys.exit(1)
' "$ROOT/tools/gate-legs.json" || fail=1
# ---- THE SHARD CONTRACT, both directions (TOOL-aShardedFloor-2) ----------------------------------
# A sharded suite is TWO manifest rows on ONE script, and the failure that costs is silent: delete
# one row and the bar goes green having run half the suite. Nothing else notices, because every
# surviving row passes and the manifest is not compared to anything.
#
# BOTH DIRECTIONS, because either alone is satisfiable by doing nothing. Forward: every index a
# sharded script declares is present in the manifest. Reverse: a script CALLED with `--shard`
# declares a `SHARD_ARITY`, and a script that declares one is CALLED with `--shard` — which is the
# arm that catches the live pre-change shape, a script parsing no argv at all, where two `--shard`
# rows would each run the full suite: bar green, wall unchanged, leg-seconds doubled.
#
# WHAT THIS DOES NOT CHECK: that a shard actually runs the region it claims. Only the suite's own
# per-mode assertion floor sees that. This arm reads the manifest and a declaration, nothing more.
a=$((a+2))
"$PYBIN" -c '
import json, os, re, sys
root, legs_file = sys.argv[1], sys.argv[2]
legs = json.load(open(legs_file))
bad = []

# forward — every declared index present, exactly once
sharded = {}
for l in legs:
    argv = l.get("argv") or []
    if "--shard" not in argv:
        continue
    i = argv.index("--shard")
    val = argv[i + 1] if i + 1 < len(argv) else ""
    script = next((t for t in argv if t.endswith(".sh") or t.endswith(".py")), "?")
    m = re.fullmatch(r"([0-9]+)/([0-9]+)", val)
    if not m:
        bad.append("leg %r carries a malformed --shard value %r" % (l.get("name", "?"), val)); continue
    sharded.setdefault(script, []).append((int(m.group(1)), int(m.group(2)), l.get("name", "?")))
for script, rows in sorted(sharded.items()):
    arities = {r[1] for r in rows}
    if len(arities) != 1:
        bad.append("%s is called with more than one shard arity: %s" % (script, sorted(arities))); continue
    n_ = arities.pop()
    have = sorted(r[0] for r in rows)
    want = list(range(1, n_ + 1))
    if have != want:
        bad.append("%s declares arity %d but the manifest carries indices %s — expected %s"
                   % (script, n_, have, want))

# reverse — the declaration and the call agree, in both directions
for script in sorted({t for l in legs for t in (l.get("argv") or []) if t.endswith(".sh")}):
    p = os.path.join(root, script)
    if not os.path.isfile(p):
        continue
    declares = re.search(r"^SHARD_ARITY=", open(p, encoding="utf-8", errors="replace").read(), re.M)
    called = script in sharded
    if declares and not called:
        bad.append("%s declares SHARD_ARITY but no manifest row calls it with --shard — it runs whole, once" % script)
    if called and not declares:
        bad.append("%s is called with --shard but declares no SHARD_ARITY — the flag is IGNORED and every row runs the whole suite" % script)

if bad:
    print("gov-canary: shard contract violated:")
    for b in bad:
        print("  " + b)
    sys.exit(1)
' "$ROOT" "$ROOT/tools/gate-legs.json" || fail=1

[ "$a" -ge "$FLOOR_ASSERTIONS" ] || { echo "gov-canary: executed $a assertions, below the pinned floor $FLOOR_ASSERTIONS"; fail=1; }
if [ "$fail" = 0 ]; then
  echo "PASS ($a assertions)"
  exit 0
fi
echo "gov-canary: FAIL ($a assertions)"
exit 1
