#!/usr/bin/env bash
# profile_bar.test.sh — self-test for the bar profiler.
#
# WHAT THIS DOES NOT CHECK. It does not assert any duration against a literal, and it never will.
# Every second this bar measures is graded against load the runner does not control, and an arm
# pinned to a wall clock has already been retired twice in this repo for flapping. What is asserted
# here are properties the arithmetic must have whatever the machine is doing: which regime the
# fixture forces, and the ORDERING of the two bounds that forces it. It also does not check that the
# profiler's advice is good — only that the classification it prints follows from the numbers it read.
#
# Hermetic: every arm builds its own scratch repo under `mktemp -d`, sets git config only inside it,
# and never touches the real tree. That is what makes this leg safe to run beside the others, and it
# is also what keeps fixture leg names out of the real timing cache — a fixture run against the real
# git dir would inject rows the runner then carries forward forever.
set -u

FLOOR_ASSERTIONS=14

HERE=$(cd "$(dirname "$0")" && pwd)
n=0
bad=0

chk() { # DESCRIPTION CONDITION-ALREADY-EVALUATED-AS-RC
  n=$((n+1))
  if [ "$1" = 0 ]; then
    return 0
  fi
  bad=$((bad+1))
  echo "  ASSERT FAILED: $2"
  return 0
}

# Resolve python the way the rest of this kit does: RUN the candidate, because being on PATH is not
# evidence — the Microsoft Store python3 stub answers `command -v` and exits 9009 without running.
PY=""
for c in "${GOV_PYTHON:-}" python3 python py; do
  [ -n "$c" ] || continue
  if "$c" -c "import sys" >/dev/null 2>&1; then PY=$c; break; fi
done
[ -n "$PY" ] || { echo "profile_bar.test: no usable python launcher"; exit 2; }

build_scratch() { # LEGS-JSON -> prints the scratch dir
  local legs=$1 d
  d=$(mktemp -d) || return 1
  mkdir -p "$d/tools/run-gates"
  cp "$HERE/run-gates.sh" "$HERE/profile_bar.py" "$d/tools/run-gates/" || return 1
  ( cd "$d" \
    && git init -q . \
    && git config user.email profile-bar@test.invalid \
    && git config user.name profile-bar-test \
    && echo seed > seed.txt \
    && git add -A \
    && git commit -qm seed ) >/dev/null 2>&1 || return 1
  printf '%s' "$legs" > "$d/tools/gate-legs.json"
  printf '%s' "$d"
}

read_field() { # SCRATCH JQ-ISH-PATH -> the value from the LAST record line
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
# One leg alone exceeds the summed work of the others divided by the width, so `floor` must win by
# construction. The margin is deliberately wide (4s against 2.5s of ideal throughput) so that
# proportional dilation under a loaded machine cannot flip the classification.
FLOOR_LEGS='[
 {"name": "pb tiny one", "argv": ["bash","-c","sleep 0.5"]},
 {"name": "pb tiny two", "argv": ["bash","-c","sleep 0.5"]},
 {"name": "pb dominant", "argv": ["bash","-c","sleep 4"]}
]'
S1=$(build_scratch "$FLOOR_LEGS") || { echo "profile_bar.test: could not build scratch (floor)"; exit 2; }
( cd "$S1" && "$PY" tools/run-gates/profile_bar.py --width 2 >"$S1/out.txt" 2>&1 )
rc=$?
chk $([ "$rc" = 0 ] && echo 0 || echo 1) "floor fixture: profiler exited $rc, expected 0"
chk $([ -s "$S1/.git/gate-profile.jsonl" ] && echo 0 || echo 1) "floor fixture: no record was appended"

BOUND=$(read_field "$S1" "regime.bound" 2>/dev/null)
chk $([ "$BOUND" = floor ] && echo 0 || echo 1) "floor fixture: bound was '$BOUND', expected 'floor'"

FL=$(read_field "$S1" "regime.floor" 2>/dev/null)
TH=$(read_field "$S1" "regime.throughput" 2>/dev/null)
# ORDERING, not magnitude. This is the property the classification rests on.
ORD=$("$PY" -c "import sys; sys.exit(0 if float(sys.argv[1]) > float(sys.argv[2]) else 1)" "$FL" "$TH" 2>/dev/null; echo $?)
chk "$ORD" "floor fixture: expected floor ($FL) > throughput ($TH)"

NLEGS=$("$PY" -c "
import json,sys
rec=[json.loads(l) for l in open(sys.argv[1],encoding='utf-8') if l.strip()][-1]
print(len(rec['legs']))" "$S1/.git/gate-profile.jsonl" 2>/dev/null)
chk $([ "$NLEGS" = 3 ] && echo 0 || echo 1) "floor fixture: record holds $NLEGS leg(s), expected 3"

QUIET=$(read_field "$S1" "env.quiet" 2>/dev/null)
chk $(case "$QUIET" in true|false|unverified) echo 0 ;; *) echo 1 ;; esac) \
    "floor fixture: env.quiet was '$QUIET', expected one of true/false/unverified"

grep -q 'BOUND: floor' "$S1/out.txt"
chk $? "floor fixture: summary did not print the floor verdict"
grep -q 'binding leg is' "$S1/out.txt"
chk $? "floor fixture: summary did not name the binding leg"
rm -rf "$S1"

# ------------------------------------------------------------ arm 2: a forced throughput-bound bar
# Four equal legs at width 2: no single leg can dominate, so total work over the width must win.
THRU_LEGS='[
 {"name": "pb even one",   "argv": ["bash","-c","sleep 2"]},
 {"name": "pb even two",   "argv": ["bash","-c","sleep 2"]},
 {"name": "pb even three", "argv": ["bash","-c","sleep 2"]},
 {"name": "pb even four",  "argv": ["bash","-c","sleep 2"]}
]'
S2=$(build_scratch "$THRU_LEGS") || { echo "profile_bar.test: could not build scratch (throughput)"; exit 2; }
( cd "$S2" && "$PY" tools/run-gates/profile_bar.py --width 2 >"$S2/out.txt" 2>&1 )
rc=$?
chk $([ "$rc" = 0 ] && echo 0 || echo 1) "throughput fixture: profiler exited $rc, expected 0"

BOUND2=$(read_field "$S2" "regime.bound" 2>/dev/null)
chk $([ "$BOUND2" = throughput ] && echo 0 || echo 1) \
    "throughput fixture: bound was '$BOUND2', expected 'throughput'"

FL2=$(read_field "$S2" "regime.floor" 2>/dev/null)
TH2=$(read_field "$S2" "regime.throughput" 2>/dev/null)
ORD2=$("$PY" -c "import sys; sys.exit(0 if float(sys.argv[2]) > float(sys.argv[1]) else 1)" "$FL2" "$TH2" 2>/dev/null; echo $?)
chk "$ORD2" "throughput fixture: expected throughput ($TH2) > floor ($FL2)"

grep -q 'BOUND: throughput' "$S2/out.txt"
chk $? "throughput fixture: summary did not print the throughput verdict"
rm -rf "$S2"

# --------------------------------------------------------- arm 3: the refusals, and the report verb
# A run that produces no parseable verdict must REFUSE rather than record a measurement of nothing.
S3=$(build_scratch '[{"name": "pb nothing", "argv": ["bash","-c","exit 0"]}]') \
  || { echo "profile_bar.test: could not build scratch (refusal)"; exit 2; }
( cd "$S3" && GATE_LEGS=does-not-exist.json "$PY" tools/run-gates/profile_bar.py --width 1 >"$S3/out.txt" 2>&1 )
rc3=$?
chk $([ "$rc3" = 2 ] && echo 0 || echo 1) \
    "refusal: an unparseable manifest exited $rc3, expected 2 (a named refusal, never a record)"
chk $([ ! -s "$S3/.git/gate-profile.jsonl" ] && echo 0 || echo 1) \
    "refusal: a record was written for a run that produced no verdict"

( cd "$S3" && "$PY" tools/run-gates/profile_bar.py --report >"$S3/rep.txt" 2>&1 )
rc4=$?
chk $([ "$rc4" = 2 ] && echo 0 || echo 1) \
    "report verb: exited $rc4 with no record present, expected 2"
rm -rf "$S3"

# ---------------------------------------------------------------------------------------- verdict
if [ "$bad" -ne 0 ]; then
  echo "FAIL ($bad of $n assertions failed)"
  exit 1
fi
if [ "$n" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL (ran $n assertions, floor is $FLOOR_ASSERTIONS — arms went missing)"
  exit 1
fi
echo "PASS ($n assertions)"
