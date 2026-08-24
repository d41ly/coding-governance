#!/usr/bin/env bash
# profile_bar.test.sh — self-test for the bar profiler.
#
# WHAT THIS DOES NOT CHECK. It does not assert any duration against a literal, and it never will.
# Every second this bar measures is graded against load the runner does not control, and an arm
# pinned to a wall clock has already been retired twice in this repo for flapping. What is asserted
# here are properties the arithmetic must have whatever the machine is doing: which regime a fixture
# forces, the ORDERING of the two bounds that forces it, and whether each refusal fires. It also does
# not check that the profiler's advice is good, only that what it prints follows from what it read.
#
# EVERY ARM BELOW THAT TESTS A REFUSAL ASSERTS ITS OWN PRECONDITION FIRST. A fixture that fails to
# make the cache read-only, or fails to export the variable it is testing, would otherwise pass by
# finding nothing — which is this repo's `fixture-passes-by-finding-nothing` class, and which the
# first version of this file committed three times over.
#
# Hermetic: every arm builds its own scratch repo under `mktemp -d`, sets git config only inside it,
# and never touches the real tree. That is what makes this leg safe beside the others, and it keeps
# fixture leg names out of the real timing cache, which the runner would carry forward forever.
set -u

FLOOR_ASSERTIONS=36

HERE=$(cd "$(dirname "$0")" && pwd)
export HERE_DIR="$HERE"   # the inline python arms import profile_bar from it
n=0
bad=0

chk() { # RC DESCRIPTION
  n=$((n+1))
  [ "$1" = 0 ] && return 0
  bad=$((bad+1))
  echo "  ASSERT FAILED: $2"
  return 0
}

PY=""
for c in "${GOV_PYTHON:-}" python3 python py; do
  [ -n "$c" ] || continue
  if "$c" -c "import sys" >/dev/null 2>&1; then PY=$c; break; fi
done
[ -n "$PY" ] || { echo "profile_bar.test: no usable python launcher"; exit 2; }

build_scratch() { # LEGS-JSON -> prints the scratch dir
  local legs=$1 d
  d=$(mktemp -d) || return 1
  mkdir -p "$d/tools/run-gates" "$d/guarded"
  cp "$HERE/run-gates.sh" "$HERE/profile_bar.py" "$d/tools/run-gates/" || return 1
  ( cd "$d" \
    && git init -q . \
    && git config user.email profile-bar@test.invalid \
    && git config user.name profile-bar-test \
    && echo seed > seed.txt && echo g > guarded/g.txt \
    && git add -A && git commit -qm seed ) >/dev/null 2>&1 || return 1
  printf '%s' "$legs" > "$d/tools/gate-legs.json"
  printf '%s' "$d"
}

field() { # SCRATCH DOTTED-PATH -> value from the LAST record line
  "$PY" - "$1/.git/gate-profile.jsonl" "$2" <<'PYEOF'
import json, sys
last = None
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if line:
        last = json.loads(line)
if last is None:
    sys.exit(1)
cur = last
for part in sys.argv[2].split("."):
    cur = cur[int(part)] if isinstance(cur, list) else cur[part]
print(cur)
PYEOF
}

# ---------------------------------------------------------------- arm 1: a forced floor-bound bar
# Width is set to the LEG COUNT deliberately: throughput is then the MEAN and floor the MAX, so a
# per-leg overhead `c` is added to both and cancels exactly. The first version of this fixture used
# width 2 and a 4s dominant leg, and flipped to throughput-bound the day per-leg spawn cost reached
# ~1.5s on this node — an arm graded against load, which is the class this file's header disavows.
FLOOR_LEGS='[
 {"name": "pb tiny one", "argv": ["bash","-c","sleep 0.2"]},
 {"name": "pb tiny two", "argv": ["bash","-c","sleep 0.2"]},
 {"name": "pb dominant", "argv": ["bash","-c","sleep 6"]}
]'
S1=$(build_scratch "$FLOOR_LEGS") || { echo "profile_bar.test: could not build scratch (floor)"; exit 2; }
( cd "$S1" && "$PY" tools/run-gates/profile_bar.py --width 3 >"$S1/out.txt" 2>&1 )
chk $? "floor fixture: profiler exited non-zero"
chk $([ -s "$S1/.git/gate-profile.jsonl" ] && echo 0 || echo 1) "floor fixture: no record appended"
B=$(field "$S1" "regime.bound" 2>/dev/null)
chk $([ "$B" = floor ] && echo 0 || echo 1) "floor fixture: bound was '$B', expected floor"
FL=$(field "$S1" "regime.floor" 2>/dev/null); TH=$(field "$S1" "regime.throughput" 2>/dev/null)
"$PY" -c "import sys;sys.exit(0 if float(sys.argv[1])>float(sys.argv[2]) else 1)" "$FL" "$TH" 2>/dev/null
chk $? "floor fixture: expected floor ($FL) > throughput ($TH)"
NL=$("$PY" -c "
import json,sys
r=[json.loads(l) for l in open(sys.argv[1],encoding='utf-8') if l.strip()][-1]
print(len(r['legs']))" "$S1/.git/gate-profile.jsonl" 2>/dev/null)
chk $([ "$NL" = 3 ] && echo 0 || echo 1) "floor fixture: record holds $NL leg(s), expected 3"
Q=$(field "$S1" "env.quiet" 2>/dev/null)
chk $(case "$Q" in true|false|unverified) echo 0 ;; *) echo 1 ;; esac) "floor fixture: env.quiet '$Q' outside the closed set"
# PACKING is a structural invariant: wall cannot be under the ideal these durations imply.
P=$(field "$S1" "regime.packing" 2>/dev/null)
"$PY" -c "import sys;sys.exit(0 if float(sys.argv[1])>=0.99 else 1)" "$P" 2>/dev/null
chk $? "floor fixture: packing $P is below 1.0, which is arithmetically impossible"
grep -q 'BOUND: floor' "$S1/out.txt"; chk $? "floor fixture: summary omitted the floor verdict"
grep -q 'binding leg is' "$S1/out.txt"; chk $? "floor fixture: summary did not name the binding leg"
grep -q 'runner exit 0' "$S1/out.txt"; chk $? "floor fixture: summary did not report the runner exit"
rm -rf "$S1"

# ------------------------------------------------------------ arm 2: a forced throughput-bound bar
THRU_LEGS='[
 {"name": "pb even one",   "argv": ["bash","-c","sleep 2"]},
 {"name": "pb even two",   "argv": ["bash","-c","sleep 2"]},
 {"name": "pb even three", "argv": ["bash","-c","sleep 2"]},
 {"name": "pb even four",  "argv": ["bash","-c","sleep 2"]}
]'
S2=$(build_scratch "$THRU_LEGS") || { echo "profile_bar.test: could not build scratch (throughput)"; exit 2; }
( cd "$S2" && "$PY" tools/run-gates/profile_bar.py --width 2 >"$S2/out.txt" 2>&1 )
chk $? "throughput fixture: profiler exited non-zero"
B2=$(field "$S2" "regime.bound" 2>/dev/null)
chk $([ "$B2" = throughput ] && echo 0 || echo 1) "throughput fixture: bound was '$B2', expected throughput"
FL2=$(field "$S2" "regime.floor" 2>/dev/null); TH2=$(field "$S2" "regime.throughput" 2>/dev/null)
"$PY" -c "import sys;sys.exit(0 if float(sys.argv[2])>float(sys.argv[1]) else 1)" "$FL2" "$TH2" 2>/dev/null
chk $? "throughput fixture: expected throughput ($TH2) > floor ($FL2)"
grep -q 'BOUND: throughput' "$S2/out.txt"; chk $? "throughput fixture: summary omitted the throughput verdict"
rm -rf "$S2"

# ------------------------- arm 3: the recorded width is the width the CHILD used, not a re-guess
# The runner honours an inherited GATE_JOBS. Deriving the recorded width from cpu_count instead makes
# `throughput`, `bound`, `ideal` and `packing` all wrong together, in a record advertised as
# comparable across months. Every other arm passes --width, so this branch is reachable only here.
S3=$(build_scratch "$FLOOR_LEGS") || { echo "profile_bar.test: could not build scratch (width)"; exit 2; }
( cd "$S3" && GATE_JOBS=1 "$PY" tools/run-gates/profile_bar.py >"$S3/out.txt" 2>&1 )
chk $? "width fixture: profiler exited non-zero"
W=$(field "$S3" "width" 2>/dev/null)
chk $([ "$W" = 1 ] && echo 0 || echo 1) "width fixture: recorded width '$W' but GATE_JOBS=1 was exported"
WS=$(field "$S3" "width_source" 2>/dev/null)
chk $(case "$WS" in GATE_JOBS*) echo 0 ;; *) echo 1 ;; esac) "width fixture: width_source '$WS' does not name GATE_JOBS"
rm -rf "$S3"

# ---------------------------------- arm 4: --scoped CLEARS an inherited GATE_FULL, in both directions
# PRECONDITION-ASSERTED: the guarded leg must actually skip under --scoped, which proves GATE_FULL was
# cleared. Without the precondition this arm would pass on a fixture whose guard never fired.
GUARD_LEGS='[
 {"name": "pb guarded", "argv": ["bash","-c","sleep 0.2"], "guard": ["guarded/"]},
 {"name": "pb always",  "argv": ["bash","-c","sleep 0.2"]}
]'
S4=$(build_scratch "$GUARD_LEGS") || { echo "profile_bar.test: could not build scratch (scoped)"; exit 2; }
( cd "$S4" && GATE_FULL=1 GATE_BASE=HEAD "$PY" tools/run-gates/profile_bar.py --width 2 --scoped >"$S4/out.txt" 2>&1 )
chk $? "scoped fixture: profiler exited non-zero"
grep -q 'GATE skip' "$S4/out.txt" 2>/dev/null || grep -q '1 skipped' "$S4/out.txt" 2>/dev/null
SKIPPED=$("$PY" -c "
import json,sys
r=[json.loads(l) for l in open(sys.argv[1],encoding='utf-8') if l.strip()][-1]
print(sum(1 for l in r['legs'] if l['verdict']=='skip'))" "$S4/.git/gate-profile.jsonl" 2>/dev/null)
chk $([ "${SKIPPED:-0}" -ge 1 ] && echo 0 || echo 1) \
    "scoped fixture: no leg skipped, so an inherited GATE_FULL was NOT cleared (precondition unmet)"
FULLF=$(field "$S4" "full" 2>/dev/null)
chk $([ "$FULLF" = False ] && echo 0 || echo 1) "scoped fixture: record says full=$FULLF, expected False"
rm -rf "$S4"

# --------------------------- arm 5: leg output cannot fabricate a verdict row through a stray \x1e
# The runner indents a failing leg's own output after LF and after LF alone, so any other byte
# `splitlines()` treats as a break lets that output present a row at column 0. \x1e is the runner's
# own field separator, so this is reachable by accident.
INJ=$("$PY" - <<'PYEOF'
import sys, os
sys.path.insert(0, os.path.join(os.environ["HERE_DIR"]))
import profile_bar as p
evil = "GATE FAIL  real leg  (exit 1)\n    tail \x1eGATE ok    injected leg\n"
names = [n for n, _ in p.parse_verdicts(evil)]
print("INJECTED" if "injected leg" in names else ("OK" if names == ["real leg"] else "UNEXPECTED:%s" % names))
PYEOF
)
chk $([ "$INJ" = OK ] && echo 0 || echo 1) "injection arm: parse_verdicts returned $INJ"

# ------------------------------- arm 6: a LEDGER that did not move is REFUSED, not published
# The store this arm freezes is `<git-dir>/gate-ledger.tsv`, which the run-record unit made the
# one place per-leg durations live. It used to name `gate-ledger.tsv`; when that file stopped
# being written the arm reported "first run wrote no timing cache", which is the freshness probe
# correctly refusing to grade a store nothing updates.
# PRECONDITION-ASSERTED: the arm first proves the cache is genuinely unwritable. If chmod does not
# take on this platform the arm reports that instead of passing.
S6=$(build_scratch "$FLOOR_LEGS") || { echo "profile_bar.test: could not build scratch (stale)"; exit 2; }
( cd "$S6" && "$PY" tools/run-gates/profile_bar.py --width 3 >/dev/null 2>&1 )
chk $([ -s "$S6/.git/gate-ledger.tsv" ] && echo 0 || echo 1) "stale arm: first run wrote no ledger"
ledger_before=$(cat "$S6/.git/gate-ledger.tsv" 2>/dev/null)
# THE FREEZE IS A RUNNER THAT DOES NOT WRITE, not a permission bit. Three ways of making the
# ledger unwritable were measured on this platform and none of them holds: `chmod -w` on the file
# and on its directory both leave `mv -f` free to replace it, because a rename is a directory
# operation and MSYS does not enforce the mode. The earlier spelling therefore asserted a
# PRECONDITION that silently stopped being true the moment the runner started replacing the
# ledger atomically, and the arm went from proving something to proving nothing.
#
# A stub runner creates the state the refusal actually exists for — a run that produced no new
# durations, so every duration available belongs to an earlier run — without depending on
# filesystem semantics this platform does not offer. It emits the runner's own verdict grammar so
# the profiler gets that far, and never touches the ledger.
cat > "$S6/tools/run-gates/run-gates.sh" <<'STUB'
#!/usr/bin/env bash
echo "gate profile: stub  (fixture; width 3, timeout off; stub)"
# The leg NAMES come from the manifest, so they match the ledger rows the real first run wrote.
# A stub that invented its own names produced a different refusal — 'no executed leg carried a
# duration' — which is also honest and is not the one this arm grades.
nm=$(grep -o '"name"[[:space:]]*:[[:space:]]*"[^"]*"' tools/gate-legs.json | sed 's/.*"name"[[:space:]]*:[[:space:]]*"//; s/"$//')
cnt=0
while IFS= read -r n; do [ -n "$n" ] || continue; printf 'GATE ok    %s
' "$n"; cnt=$((cnt+1)); done <<<"$nm"
echo "----"
echo "gates GREEN — $cnt/$cnt legs passed"
exit 0
STUB
( cd "$S6" && "$PY" tools/run-gates/profile_bar.py --width 3 >"$S6/stale.txt" 2>&1 )
rc=$?
chk $([ "$(cat "$S6/.git/gate-ledger.tsv" 2>/dev/null)" = "$ledger_before" ] && echo 0 || echo 1) \
    "stale arm: PRECONDITION UNMET — the ledger moved under the stub runner, so this arm proves nothing"
chk $([ "$rc" != 0 ] && echo 0 || echo 1) \
    "stale arm: profiler exited 0 on a ledger that did not move, publishing an earlier run's durations"
grep -qiE 'did not move|EARLIER run|impossible' "$S6/stale.txt"
chk $? "stale arm: the refusal did not name the stale ledger"
rm -rf "$S6"

# --------------------------------------- arm 7: a RED bar is reported as red, with a named caveat
FAIL_LEGS='[
 {"name": "pb passes", "argv": ["bash","-c","sleep 0.3"]},
 {"name": "pb breaks", "argv": ["bash","-c","sleep 0.3; exit 3"]}
]'
S7=$(build_scratch "$FAIL_LEGS") || { echo "profile_bar.test: could not build scratch (red)"; exit 2; }
( cd "$S7" && "$PY" tools/run-gates/profile_bar.py --width 2 >"$S7/out.txt" 2>&1 )
chk $([ -s "$S7/.git/gate-profile.jsonl" ] && echo 0 || echo 1) "red arm: no record appended for a red bar"
EX=$(field "$S7" "exit" 2>/dev/null)
chk $([ "${EX:-0}" != 0 ] && echo 0 || echo 1) "red arm: recorded runner exit was '$EX', expected non-zero"
FLC=$("$PY" -c "
import json,sys
r=[json.loads(l) for l in open(sys.argv[1],encoding='utf-8') if l.strip()][-1]
print(len(r.get('failed_legs',[])))" "$S7/.git/gate-profile.jsonl" 2>/dev/null)
chk $([ "${FLC:-0}" -ge 1 ] && echo 0 || echo 1) "red arm: failed_legs was empty for a red bar"
grep -q 'CAVEAT: the bar was RED' "$S7/out.txt"; chk $? "red arm: summary printed no RED caveat"
rm -rf "$S7"

# --------------------------------------------------- arm 8: the refusals, and the report verb
S8=$(build_scratch '[{"name": "pb nothing", "argv": ["bash","-c","exit 0"]}]') \
  || { echo "profile_bar.test: could not build scratch (refusal)"; exit 2; }
( cd "$S8" && GATE_LEGS=does-not-exist.json "$PY" tools/run-gates/profile_bar.py --width 1 >"$S8/out.txt" 2>&1 )
rc=$?
chk $([ "$rc" = 2 ] && echo 0 || echo 1) "refusal: unparseable manifest exited $rc, expected 2"
chk $([ ! -s "$S8/.git/gate-profile.jsonl" ] && echo 0 || echo 1) "refusal: a record was written for a run with no verdict"
( cd "$S8" && "$PY" tools/run-gates/profile_bar.py --report >"$S8/rep.txt" 2>&1 )
rc=$?
chk $([ "$rc" = 2 ] && echo 0 || echo 1) "report verb: exited $rc with no record present, expected 2"
rm -rf "$S8"

# ------------- arm 9: check_quiet reports `unverified` when it cannot read a command line
# The predicate that shipped grepped MSYS `ps` for a substring its output structurally cannot hold,
# so it returned the affirmative on every Windows node, forever. The property that matters is not
# what it answers on this machine — that varies — but that it REFUSES to answer when blind. Driven
# through the injected runner so the blind case is reachable without breaking the host.
QB=$("$PY" - <<'PYEOF'
import sys, os
sys.path.insert(0, os.environ["HERE_DIR"])
import profile_bar as p


class Fake:
    returncode = 0
    # Rows for other processes, none of them ours, and none carrying a readable command line —
    # exactly what a query that cannot read command lines returns.
    stdout = "4242|\n4243|\n"


state, detail = p.check_quiet(_runner=lambda *a, **k: Fake())
print(state)
PYEOF
)
chk $([ "$QB" = unverified ] && echo 0 || echo 1)     "quiet blind arm: returned '$QB' when the query could not read a command line, expected unverified"

QS=$("$PY" - <<'PYEOF'
import sys, os
sys.path.insert(0, os.environ["HERE_DIR"])
import profile_bar as p
print(p.check_quiet()[0])
PYEOF
)
chk $(case "$QS" in true|false|unverified) echo 0 ;; *) echo 1 ;; esac)     "quiet arm: live state '$QS' outside the closed set"

# ---------------------------- arm 10: the packing invariant refuses an impossible wall clock
# Wall cannot be below the ideal its own durations imply. Reached directly rather than through a run,
# because a refusal only reachable via genuinely stale data is a refusal nobody ever arms.
PK=$("$PY" - <<'PYEOF'
import sys, os
sys.path.insert(0, os.environ["HERE_DIR"])
import profile_bar as p
good = p.check_packing(10.0, 5.0)[0]
bad = p.check_packing(2.0, 5.0)[0]
print("%s,%s" % (good, bad))
PYEOF
)
chk $([ "$PK" = "True,False" ] && echo 0 || echo 1)     "packing arm: check_packing(possible,impossible) returned '$PK', expected True,False"

# ---------------------------------------------------------------------------------------- verdict
if [ "$bad" -ne 0 ]; then
  echo "FAIL ($bad of $n assertions failed)"
  exit 1
fi
# ------------------- arm 9: THE VERB SET AGREES WITH THE RUNNER, and `held` is in it
# TOOL-dUnstalledConvoy-26 added a fifth verb to run-gates.sh and not to this reader, so 42 of gov's
# 85 legs were dropped from every profile with nothing reporting a gap. That is the same silent
# under-count the file's own comment records for `reuse`, one verb later. The set is now DERIVED from
# the runner and compared, so the sixth verb reds instead of vanishing.
VB=$("$PY" - <<'PYEOF'
import sys, os
sys.path.insert(0, os.environ["HERE_DIR"])
import profile_bar as p

runner = os.path.join(os.environ["HERE_DIR"], "run-gates.sh")
emitted = p.derive_runner_verbs(runner)
if emitted is None:
    print("UNREADABLE")
else:
    unknown = sorted(emitted - set(p.PINNED_VERBS))
    # LIVENESS: a derivation that found nothing agrees with everything. `held` specifically, because
    # it is the verb that motivated the arm and its absence is the regression to catch.
    if len(emitted) < 4 or "held" not in emitted:
        print("UNARMED:%s" % sorted(emitted))
    else:
        print("OK" if not unknown else "UNKNOWN:%s" % unknown)
PYEOF
)
chk $([ "$VB" = OK ] && echo 0 || echo 1) "verb-set arm: derived-vs-pinned returned $VB"

# ...and a `held` line actually PARSES, with its name recovered through the two-space tail contract.
# The set agreeing is not the same fact as the regex matching.
HV=$("$PY" - <<'PYEOF'
import sys, os
sys.path.insert(0, os.environ["HERE_DIR"])
import profile_bar as p

line = "GATE held  a kit self-test  (kit self-test, set GATE_SELFTESTS=1 to run)\n"
got = p.parse_verdicts(line)
print("OK" if got == [("a kit self-test", "held")] else "GOT:%s" % got)
PYEOF
)
chk $([ "$HV" = OK ] && echo 0 || echo 1) "held-parse arm: parse_verdicts returned $HV"

# ...and a held leg is NOT counted as executed work. It did not run, so a profile that averaged it
# in would report a bar that is faster than the bar.
NR=$("$PY" - <<'PYEOF'
import sys, os
sys.path.insert(0, os.environ["HERE_DIR"])
import profile_bar as p

print("OK" if "held" in p.NOT_RUN and "skip" in p.NOT_RUN else "GOT:%s" % (p.NOT_RUN,))
PYEOF
)
chk $([ "$NR" = OK ] && echo 0 || echo 1) "not-run arm: NOT_RUN returned $NR"

if [ "$n" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL (ran $n assertions, floor is $FLOOR_ASSERTIONS — arms went missing)"
  exit 1
fi
echo "PASS ($n assertions)"
