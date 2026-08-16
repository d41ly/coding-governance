#!/usr/bin/env bash
# The marker-region well-formedness CONTRACT, and the four live readers that must obey it.
#
#   bash tools/memory-tree/marker-contract.test.sh    # "PASS (…cases × …readers)" + exit 0 = good
#
# WHY A CONFORMANCE TEST AND NOT A SHARED FUNCTION. Three readers are awk inside the unattended kit
# and one is Python here; no single implementation serves both languages. A three-way lift INSIDE the
# unattended kit is legitimate and is deliberately deferred — the kit-independence argument does not
# forbid it, because all three awk copies live in one kit. What is forbidden is a cross-kit edge, so
# the deliverable is AGREEMENT, proven, rather than unification.
#
# THE CASE TABLE BELOW IS THE CONTRACT. No reader restates it in prose; this file is where it lives.
# It was written after the readers DISAGREED in two places, both of them the Python side being
# permissive AND mutating: an indented marker and a marker carrying trailing whitespace were each
# accepted and then re-emitted bare, silently rewriting a line the author wrote. Two trailing spaces
# are a Markdown hard line break, so that input is authored, not pathological.
#
# THE FOURTH READER IS THE ONE THAT MATTERS. `splice()` in the unattended driver is the awk side's
# WRITING path — the copy whose absence, per its own comment, once destroyed data. A conformance test
# that covers three readers and skips it covers the wrong three.
#
# THE UNATTENDED KIT IS OPTIONAL, AND THIS LEG LIVES IN memory-tree. Both kit dirs are DERIVED from
# this script's own location, never spelled: a hardcoded `tools/unattended` is wrong at every install
# prefix but the one it assumed, which is the class this repo gates repo-wide. When the sibling kit is
# absent the leg SKIPS LOUDLY and exits 0 — an adopter who installed memory-tree alone must not get a
# red bar for a kit they chose not to take, and a silent pass would claim coverage that never ran.
#
# This file deliberately does NOT define `fail() {`: check-arms.py discovers any tracked *.sh that
# does and demands a sibling test for it, and a test-for-the-test is not a thing this contract needs.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
# ASK GIT for the repo-relative prefix; never subtract one path string from another. Under
# MSYS one directory has two spellings — `git rev-parse --show-toplevel` answers `C:/…` while
# `$(cd … && pwd)` answers `/c/…` — so the strip silently does not strip and the kit path comes
# out absolute in the wrong flavour. Measured here: every python case failed with
# ModuleNotFoundError while the awk cases passed, so 3 of 4 readers still "agreed".
KIT_MT="$(git -C "$(dirname "$0")" rev-parse --show-prefix)"; KIT_MT="${KIT_MT%/}"
KITS_DIR="$(dirname "$KIT_MT")"        # the install prefix both kits sit under
U="$KITS_DIR/unattended/unattended.sh"
K="$KITS_DIR/unattended/check-unattended.sh"

st=0; ncase=0
O='<!-- gen:build-index -->'
C='<!-- /gen:build-index -->'

if [ ! -f "$U" ] || [ ! -f "$K" ]; then
  echo "marker-contract: SKIP — the unattended kit is not installed at $KITS_DIR/unattended/,"
  echo "marker-contract: so 3 of the 4 readers do not exist here. The Python reader is covered by"
  echo "marker-contract: gen_build_index.py --selftest; this leg asserts AGREEMENT and needs both sides."
  exit 0
fi

PY=""
for c in "${GOV_PYTHON:-}" python3 python py; do
  [ -n "$c" ] || continue
  if "$c" -c "import sys" >/dev/null 2>&1; then PY=$c; break; fi
done
[ -n "$PY" ] || { echo "marker-contract: no usable python launcher"; exit 2; }
T=$(mktemp -d) || exit 2
trap 'rm -rf "$T"' EXIT
cat > "$T/reader.py" <<PYR
import sys, os
sys.path.insert(0, os.path.join("$KIT_MT"))
import gen_build_index as G
mode, path = sys.argv[1], sys.argv[2]
t = open(path, encoding="utf-8", newline="").read()
try:
    out = G.apply_region(t, G.MARK_OPEN + chr(10) + "X" + chr(10) + G.MARK_CLOSE, path)
except G.Problem:
    print("refuse" if mode == "verdict" else "REFUSED")
    raise SystemExit(0)
if mode == "verdict":
    print("accept")
else:
    # The MARKER LINES as rendered, so a caller can compare them against the input bytes. Counting
    # markers could not see a rewrite: a permissive reader that re-emits the bare marker still
    # renders exactly one, so the count is identical whether the author's line survived or not.
    for line in out.split(chr(10)):
        if line.strip() in (G.MARK_OPEN, G.MARK_CLOSE):
            print(repr(line))
PYR

# ---- the four readers, each invoked as SHIPPED. The awk bodies are sliced out of the kit files at
# ---- run time rather than transcribed here, so an edit to the kit changes this test's verdict —
# ---- and a slice that fails to define its function is an ERROR, never a silent zero-reader pass.
slice() { sed -n "$2,$3p" "$1"; }
mk_awk() { # name · file · from · to  -> defines <name> in this shell from the SHIPPED bytes
  local n=$1 f=$2 a=$3 b=$4
  eval "$(slice "$f" "$a" "$b" | sed "1s/^[a-z_]*()/${n}()/")" 2>/dev/null
  declare -F "$n" >/dev/null || {
    echo "marker-contract: reader '$n' was not sliced out of $f lines $a-$b — the offsets no longer"
    echo "marker-contract: match the shipped function, so this leg would have tested nothing."
    exit 2
  }
}
mk_awk r_check  "$K" "$(grep -n '^region()' "$K" | cut -d: -f1)" "$(( $(grep -n '^region()' "$K" | cut -d: -f1) + 5 ))"
mk_awk r_unatt  "$U" "$(grep -n '^region()' "$U" | cut -d: -f1)" "$(( $(grep -n '^region()' "$U" | cut -d: -f1) + 8 ))"
mk_awk r_splice "$U" "$(grep -n '^splice()' "$U" | cut -d: -f1)" "$(( $(grep -n '^splice()' "$U" | cut -d: -f1) + 12 ))"

py_verdict() { "$PY" "$T/reader.py" verdict "$1"; }

# ONLY the readers' documented refusal code counts as a refusal. Mapping every nonzero status to
# `refuse` made a crash — an awk syntax error, a missing file, a reader that was never defined —
# indistinguishable from a correct rejection, so the suite would have gone green over a reader that
# could not run at all. Anything else reports `error`, which no `want` value matches.
verdict_awk() { # fn · file -> accept|refuse|error(N)
  "$1" "$2" "$O" "$C" >/dev/null 2>&1
  case $? in 0) echo accept ;; 3) echo refuse ;; *) echo "error($?)" ;; esac
}
verdict_splice() { # file -> accept|refuse|error(N)
  printf 'X\n' > "$T/payload"
  r_splice "$1" "$O" "$C" "$T/payload" >/dev/null 2>&1
  case $? in 0) echo accept ;; 3) echo refuse ;; *) echo "error($?)" ;; esac
}

case_run() { # name · want · file-content...
  local name=$1 want=$2; shift 2
  printf '%s\n' "$@" > "$T/case.md"
  ncase=$((ncase+1))
  local got
  for pair in "r_check:$(verdict_awk r_check "$T/case.md")" \
              "r_unatt:$(verdict_awk r_unatt "$T/case.md")" \
              "splice:$(verdict_splice "$T/case.md")" \
              "python:$(py_verdict "$T/case.md")"; do
    got=${pair#*:}
    [ "$got" = "$want" ] || { echo "FAIL [$name] ${pair%%:*} said $got, contract says $want"; st=1; }
  done
}

#            name              want     the document
case_run "column-0"           accept  "head" "$O" "body" "$C" "tail"
case_run "trailing text"      refuse  "head" "$O x" "body" "$C" "tail"
case_run "trailing space"     refuse  "head" "$O  " "body" "$C" "tail"
case_run "trailing tab"       refuse  "head" "$(printf '%s\t' "$O")" "body" "$C" "tail"
case_run "close trailing ws"  refuse  "head" "$O" "body" "$C " "tail"
case_run "indented open"      refuse  "head" "   $O" "body" "$C" "tail"
case_run "indented close"     refuse  "head" "$O" "body" "   $C" "tail"
case_run "unpaired open"      refuse  "head" "$O" "body" "tail"
case_run "reversed pair"      refuse  "head" "$C" "body" "$O" "tail"
case_run "two pairs"          refuse  "head" "$O" "b" "$C" "$O" "b" "$C"

# ---- CR TOLERANCE, ASSERTED AT SOURCE. A CRLF fixture cannot test a CR guard here: this runtime
# ---- strips the CR before awk sees a byte, so all three awk readers answer identically whether
# ---- their `sub(/\r$/…)` is present or deleted — measured, the whole suite stayed green with all
# ---- three strips removed. An exit-status fixture would assert a property no runner on this host
# ---- can observe. So the rule is read out of the SHIPPED BYTES instead, which is platform-free.
ncase=$((ncase+1))
# PER READER, not per file. Each file holds more than one reader, so a `>=1` count over the whole
# file is satisfied by a SIBLING and cannot see one reader lose its strip — measured: deleting the
# strip from region() left the file-level count at 2 and this assertion green, which is the same
# false-control shape the fixture version had.
for r in "r_check $K region" "r_unatt $U region" "r_splice $U splice"; do
  set -- $r
  ln0=$(grep -n "^$3()" "$2" | cut -d: -f1)
  if ! sed -n "${ln0},$((ln0 + 12))p" "$2" | grep -q 'sub(/\\r\$/'; then
    echo "FAIL [CR tolerance @source] reader $1 in $2 carries no record-level CR strip"; st=1
  fi
done
# exactly ONE CR, both sides: awk's `sub(/\r$/,"")` removes one, and the Python predicate must too —
# `rstrip("\r")` would remove all of them, which is a divergence no fixture on this host can show.
grep -q 'line\[:-1\] if line.endswith(CR) else line' "$KIT_MT/gen_build_index.py" || {
  echo "FAIL [CR tolerance @source] the Python marker predicate no longer strips exactly one CR"; st=1; }
# and the behavioural half, for the one reader whose CR handling this host CAN observe
printf 'head\r\n%s\r\nbody\r\n%s\r\ntail\r\n' "$O" "$C" > "$T/case.md"
[ "$(py_verdict "$T/case.md")" = accept ] || { echo "FAIL [one trailing CR] python rejected a CRLF document"; st=1; }

# ---- NO MUTATION. Counting markers cannot see a rewrite — a permissive reader re-emits exactly one
# ---- bare marker, so the count is identical whether the author's line survived or not. Compare the
# ---- rendered marker LINES against the input, on the documents a permissive reader would rewrite.
ncase=$((ncase+1))
for shape in "   $O" "$O  "; do
  printf '%s\n%s\nbody\n%s\ntail\n' "head" "$shape" "$C" > "$T/case.md"
  got=$("$PY" "$T/reader.py" lines "$T/case.md")
  [ "$got" = "REFUSED" ] || {
    echo "FAIL [no mutation] a marker line the author wrote as '$shape' was accepted and rendered as: $got"
    st=1
  }
done

[ "$st" = 0 ] && echo "PASS ($ncase cases x 4 readers, contract held)"
exit $st
