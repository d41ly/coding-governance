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
# THE FOURTH READER IS THE ONE THAT MATTERS. `splice()` in unattended.sh is the awk side's WRITING
# path — the copy whose absence, per its own comment, once destroyed data. A conformance test that
# covers the three readers and skips it covers the wrong three.
#
# This file deliberately does NOT define `fail() {`: check-arms.py discovers any tracked *.sh that
# does and demands a sibling test for it, and a test-for-the-test is not a thing this contract needs.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
st=0; ncase=0
O='<!-- gen:build-index -->'
C='<!-- /gen:build-index -->'
PY=""
for c in "${GOV_PYTHON:-}" python3 python py; do
  [ -n "$c" ] || continue
  if "$c" -c "import sys" >/dev/null 2>&1; then PY=$c; break; fi
done
[ -n "$PY" ] || { echo "marker-contract: no usable python launcher"; exit 2; }
T=$(mktemp -d) || exit 2
trap 'rm -rf "$T"' EXIT
cat > "$T/reader.py" <<'PYR'
import sys, os
sys.path.insert(0, os.path.join("tools", "memory-tree"))
import gen_build_index as G
mode, path = sys.argv[1], sys.argv[2]
t = open(path, encoding="utf-8", newline="").read()
try:
    out = G.apply_region(t, G.MARK_OPEN + chr(10) + "X" + chr(10) + G.MARK_CLOSE, path)
except G.Problem:
    print("refuse" if mode == "verdict" else "-1")
    raise SystemExit(0)
print("accept" if mode == "verdict" else str(out.count(G.MARK_OPEN)))
PYR


# ---- the four readers, each invoked as SHIPPED. The awk bodies are sliced out of the kit files at
# ---- run time rather than transcribed here, so an edit to the kit changes this test's verdict —
# ---- that is the property AC6 asserts, and a transcription would silently stop tracking the kit.
slice() { sed -n "$2,$3p" "$1"; }
mk_awk() { # name · file · from · to  -> defines <name> in this shell from the SHIPPED bytes
  local n=$1 f=$2 a=$3 b=$4
  eval "$(slice "$f" "$a" "$b" | sed "1s/^[a-z_]*()/${n}()/")"
}
U=tools/unattended/unattended.sh
K=tools/unattended/check-unattended.sh
mk_awk r_check "$K" "$(grep -n '^region()' "$K" | cut -d: -f1)" "$(( $(grep -n '^region()' "$K" | cut -d: -f1) + 5 ))"
mk_awk r_unatt "$U" "$(grep -n '^region()' "$U" | cut -d: -f1)" "$(( $(grep -n '^region()' "$U" | cut -d: -f1) + 8 ))"
mk_awk r_splice "$U" "$(grep -n '^splice()' "$U" | cut -d: -f1)" "$(( $(grep -n '^splice()' "$U" | cut -d: -f1) + 12 ))"

py_verdict() { "$PY" "$T/reader.py" verdict "$1"; }

verdict_awk() { # fn · file -> accept|refuse
  if "$1" "$2" "$O" "$C" >/dev/null 2>&1; then echo accept; else echo refuse; fi
}
verdict_splice() { # file -> accept|refuse   (splice takes a payload file)
  printf 'X\n' > "$T/payload"
  if r_splice "$1" "$O" "$C" "$T/payload" >/dev/null 2>&1; then echo accept; else echo refuse; fi
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

# One trailing CR is TOLERATED by every reader — the CRLF worktree case, asserted rather than assumed.
printf 'head\r\n%s\r\nbody\r\n%s\r\ntail\r\n' "$O" "$C" > "$T/case.md"
ncase=$((ncase+1))
for pair in "r_check:$(verdict_awk r_check "$T/case.md")" "r_unatt:$(verdict_awk r_unatt "$T/case.md")" \
            "splice:$(verdict_splice "$T/case.md")" "python:$(py_verdict "$T/case.md")"; do
  [ "${pair#*:}" = accept ] || { echo "FAIL [one trailing CR] ${pair%%:*} said ${pair#*:}, contract says accept"; st=1; }
done

# The Python reader must not MUTATE an accepted document's marker lines. The awk readers cannot: two
# only read, and splice re-emits the line it matched. This is the half that made the divergence
# dangerous rather than merely inconsistent.
printf 'head\n%s\nbody\n%s\ntail\n' "$O" "$C" > "$T/case.md"
out=$("$PY" "$T/reader.py" count "$T/case.md")
[ "$out" = 1 ] || { echo "FAIL [no mutation] the accepted document rendered $out open markers, expected 1"; st=1; }

[ "$st" = 0 ] && echo "PASS ($ncase cases x 4 readers, contract held)"
exit $st
