#!/usr/bin/env bash
# Fixtures for the row-keyed merge driver (aMendedLedger U5; upstream ARCH-dQuarriedLedger-1 U9 S4).
#
# The risk this leg exists to close is a driver that exits 0 having DROPPED a row — invisible by
# construction, because a clean merge prints nothing alarming and the row is simply gone. So every
# rc-0 case asserts ID-SET EQUALITY between the union of the three inputs (minus the ids an honoured
# delete removed) and the file the driver wrote, computed by a grammar-independent ORACLE regex
# rather than by the driver's own grammar. An id-set equality over two empty sets is not evidence, so
# the oracle is proved live in this same run — `memory/backlog/DEPL.md` and `memory/backlog/KICK.md`
# carry zero anchors today, which is exactly how an arm passes by finding nothing.
#
# Case 2 is the one that matters most: it is the exact shape that broke `merge=union` (a row whose
# text differs on BOTH sides), and it asserts a CONFLICT rather than two rows. Union introduced a
# duplicate in 147 of 151 historical DECISIONS.md conflicts upstream; this is where that claim is
# falsified or confirmed.
#
# AN ID-SET ORACLE CANNOT SEE A DUPLICATE, and three separate corruptions arrived through that hole:
# a section heading copied onto two new ids (case 10), an incoming row filed under the wrong
# `## FAMILY` (case 11), and an unkeyable row written twice (case 12) — all three at exit 0, no
# markers, audit line `clean`. So every rc-0 arm now also asserts NO id occurs twice in the written
# file, the oracle is widened to the suffixed id form the driver's own grammar cannot key, and both
# halves of that oracle are proved live in case 0d before anything leans on them.
#
#   bash tools/memory-tree/merge-rows.test.sh
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SELF="$HERE/$(basename "$0")"
ROOT="$(cd "$HERE/../.." && pwd)"
cd "$ROOT" || exit 2
st=0
TMP=$(mktemp -d); SCRATCH=""
cleanup() { cd "$ROOT" 2>/dev/null || true; rm -rf "$TMP" $SCRATCH; }
trap cleanup EXIT

# The interpreter comes from the ONE resolver, never from a launcher name typed here: a name that is
# on PATH and cannot run is the Microsoft-Store-stub defect the resolver exists for.
# shellcheck source=/dev/null
. "$ROOT/tools/lib/resolve-python.sh"
PY=$(resolve_python) || { echo "FAIL no usable python on this host — every arm below is unrunnable"; exit 2; }

DRV="bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py"
bad() { echo "FAIL $1"; st=1; }

# THE ORACLE — a family-agnostic id shape, deliberately NOT the driver's grammar. Keying the
# assertion on the same regex the driver keys the merge on would make every arm self-consistent and
# blind: a grammar that stopped recognising a row would remove it from BOTH sides of the comparison.
# THE `[a-z]*` TAIL IS THE POINT, not a tidy-up. Without it the oracle shared the driver grammar's
# trailing `\b`, so this corpus's ratified correction-id form (`…-1b`) fell out of BOTH sides of
# every comparison here — measured on the real memory/DECISIONS.md at 38 of 73 rows unkeyed, the two
# newest of them minted by the build that shipped this driver. The remedy for a blind spot the
# oracle shares with the subject is to WIDEN the oracle, never to point it at the driver's regex.
ORACLE='\b[A-Z]+-[A-Za-z0-9]+-[0-9]+[a-z]*\b'
ids() { grep -ohE "$ORACLE" "$@" 2>/dev/null | LC_ALL=C sort -u | tr '\n' ' '; }
# ...and the same oracle asked the other question. `sort -u` above makes `ids` structurally unable to
# report a duplicate, which is exactly how a doubled row passed an id-SET comparison.
dups() { grep -ohE "$ORACLE" "$@" 2>/dev/null | LC_ALL=C sort | uniq -d | tr '\n' ' '; }
minus() {  # $1 = a space-separated set · rest = members the honoured deletes removed
  local all=$1 t d keep out=""; shift
  for t in $all; do
    keep=1; for d in "$@"; do [ "$t" = "$d" ] && keep=0; done
    [ "$keep" = 1 ] && out="$out$t "
  done
  printf '%s' "$out"
}
row() { printf -- '- %s · OPEN · %s\n' "$1" "$2"; }
pre() { printf '# Index\n\nRouting prose, unkeyable by design.\n\n'; }
# The line number of the FIRST match, or 0. Both halves matter: the placement arms below compare two
# line numbers, and the defect they were written for DUPLICATES a heading — so an un-headed
# `grep -n | cut` hands `[` two numbers on two lines and bash aborts the comparison with
# `integer expected` instead of the arm reporting anything. A missing match answers 0, and every
# caller tests for that EXPLICITLY — 0 wins a `-lt` against any real line number, so a vanished row
# would otherwise satisfy the placement it was supposed to prove.
at_line() { local n; n=$(grep -n -- "$1" "$2" 2>/dev/null | head -1 | cut -d: -f1); printf '%s' "${n:-0}"; }

# $1 label · $2 expected rc · $3 expected id set · rest: ids an honoured delete removed
run() {
  local label=$1 want_rc=$2 want_ids=$3 rc u expect got d; shift 3
  u=$(ids "$TMP/o" "$TMP/a" "$TMP/b")            # BEFORE the driver overwrites %A
  expect=$(minus "$u" "$@")
  [ "$expect" = "$want_ids" ] \
    || bad "$label: the declared id set [$want_ids] is not the input union minus the declared deletes [$expect]"
  $DRV "$TMP/o" "$TMP/a" "$TMP/b" x >/dev/null 2>&1 && rc=0 || rc=$?
  [ "$rc" = "$want_rc" ] || bad "$label: rc=$rc, expected $want_rc"
  got=$(ids "$TMP/a")
  [ "$got" = "$want_ids" ] || bad "$label: ids [$got], expected [$want_ids]"
  # THE SECOND ORACLE, and it runs on the OBSERVED rc, never the expected one. A conflict legitimately
  # writes one id twice (case 2 is built on exactly that), so a blanket no-duplicate rule would red
  # the arm that proves the driver conflicts instead of duplicating. But keying on `want_rc` would
  # exempt precisely the regression this exists to catch — a driver that was SUPPOSED to conflict and
  # exited 0 instead would have its duplicate skipped along with its rc. rc 0 is the regime where a
  # duplicate is invisible: no markers, nothing unmerged, `clean` printed, the file quietly wrong.
  if [ "$rc" = 0 ]; then
    d=$(dups "$TMP/a")
    [ -z "$d" ] || bad "$label: rc 0 and the written file carries a DUPLICATE id [$d]"
  fi
}

# --- 0. the ORACLE is live, on a named population -------------------------------------------------
# `pop_guard` idiom: a set comparison whose two sides are both empty holds for the wrong reason, and
# two of this corpus's four backlog shards legitimately carry zero anchors.
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; row TOOL-zFixture-3 base; } > "$TMP/oracle"
[ "$(ids "$TMP/oracle")" = "TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-3 " ] \
  || bad "oracle: a 3-row fixture did not yield its three ids — every id-set arm below is vacuous"
[ -n "$(ids memory/DECISIONS.md)" ] \
  || bad "oracle: the real memory/DECISIONS.md yielded NO ids — the oracle does not see this corpus"

# --- 0a. the driver PARSES under the interpreter the shim actually resolves -----------------------
"$PY" -c 'import py_compile,sys; py_compile.compile(sys.argv[1], cfile=sys.argv[2], doraise=True)' \
      tools/memory-tree/merge-rows.py "$TMP/mr.pyc" >/dev/null 2>&1 \
  || bad "merge-rows.py does not compile under the resolved interpreter ($PY)"

# ...and the version-INDEPENDENT half of the same concern, which py_compile on a modern node cannot
# see: `f"{"CONFLICT" if … else "clean"}"` is a nested SAME-quote f-string, PEP 701, valid only on
# 3.12+. `resolve_python` imposes NO version floor, so the interpreter a node hands this driver is
# whatever it has, and a driver that fails to START exits non-zero without writing %A — git then
# leaves OURS-only content with no markers. Upstream's arm needed `uv python find 3.11` and SKIPPED
# where uv was absent; this repo depends on uv nowhere, so a skippable arm would be a silent hole.
FSTR='f"[^"]*\{[^}"]*"'
nested=$(awk '!/^[[:space:]]*#/' tools/memory-tree/merge-rows.py | grep -nE "$FSTR" || true)
[ -z "$nested" ] || { echo "FAIL merge-rows.py carries a nested same-quote f-string (PEP 701, 3.12+):"; printf '%s\n' "$nested" | sed 's/^/    /'; st=1; }
# ...the ban FIRES on the shape it bans, or "clean" means "the predicate is broken".
printf 'v = f"{"X" if c else "y"}"\n' > "$TMP/pep701.py"
grep -qE "$FSTR" "$TMP/pep701.py" || bad "the PEP-701 predicate does not match the shape it bans"
# ...and does NOT fire on an ordinary f-string, or every interpolation in the driver reds.
printf 'v = f"{a} row(s) from {b}"\n' > "$TMP/plain.py"
grep -qE "$FSTR" "$TMP/plain.py" && bad "the PEP-701 predicate fires on an ordinary f-string"
# ...the comment exemption, with its own red half: the driver DOCUMENTS the banned shape in a comment,
# and a predicate that fires on the prose explaining a fix is this repo's catalogued self-inflicted red.
printf '# v = f"{"X" if c else "y"}"\n' > "$TMP/comment.py"
[ -z "$(awk '!/^[[:space:]]*#/' "$TMP/comment.py" | grep -E "$FSTR" || true)" ] \
  || bad "the PEP-701 ban fires on a COMMENT explaining the shape"
printf 'v = f"{"X" if c else "y"}"\n' > "$TMP/comment.py"
[ -n "$(awk '!/^[[:space:]]*#/' "$TMP/comment.py" | grep -E "$FSTR" || true)" ] \
  || bad "the SAME line uncommented is exempt too — the comment strip is doing nothing"

# --- 0b. the launcher shim's contract -------------------------------------------------------------
# (i) no arguments -> exit 2, and the usage text carries the four placeholders. Upstream prints
# `__doc__.split("\n\n")[0]` — the summary sentence alone — so its refusal never says how to wire the
# driver it is refusing to run.
out=$($DRV 2>&1 >/dev/null); rc=$?
[ "$rc" = 2 ] || bad "no-argument invocation exited $rc, expected 2"
for ph in '%O' '%A' '%B' '%P'; do
  printf '%s\n' "$out" | grep -qF -- "$ph" || bad "the usage text does not carry the $ph placeholder"
done
# (ii) the shim HALTS on the resolver's return value rather than falling through. The arm has to
# shadow ALL THREE launcher names first: `resolve_python` returns on the first candidate that RUNS,
# so an unusable GOV_PYTHON on a host with a working python3 resolves to python3 and exits 0 BY
# DESIGN — the named-failure block is unreachable until every candidate is dead.
mkfake() { mkdir -p "$1"; printf '#!/usr/bin/env bash\nexit %s\n' "$3" > "$1/$2"; chmod +x "$1/$2"; }
C="$TMP/allbad"; mkfake "$C" python3 9009; mkfake "$C" python 9009; mkfake "$C" py 9009
out=$(PATH="$C:$PATH" GOV_PYTHON="$C/python3" $DRV 2>&1); rc=$?
[ "$rc" = 2 ] || bad "the shim exited $rc with no usable launcher, expected 2"
printf '%s\n' "$out" | grep -qF "GOV_PYTHON is set to '$C/python3' and did not run" \
  || bad "the shim did not surface the resolver's named GOV_PYTHON failure"
# (iii) the shim SOURCES the resolver, so it must NOT carry the inline-copy marker block — that
# population is derived by grep, and enlisting the shim would put it in a parity gate it has no
# reason to be in.
copies=$(git grep -l '^# >>> resolve_python' -- '*.sh' || true)
[ -n "$copies" ] || bad "no inline resolver copy found — the marker-population assertion below is vacuous"
printf '%s\n' "$copies" | grep -qx 'tools/lib/pyrun.sh' \
  && bad "tools/lib/pyrun.sh carries the resolver marker block; it SOURCES the resolver instead"

# --- 0c. FAIL CLOSED: every deferred-resolution failure becomes a conflict, never a take-ours ------
# The driver reads its anchor grammar from the worktree at merge time. At module scope that import
# failing killed the process before %A was written — git then leaves OURS-only content with no
# markers, and the incoming rows are gone with nothing saying so. The import is deferred so all three
# failures land in main()'s fail-closed handler. Simulated on scratch trees rather than by breaking
# the real kit under a concurrently-running gate.
failclosed() {  # $1 label · $2 scratch tree holding tools/memory-tree/merge-rows.py
  { pre; row TOOL-zFixture-1 base; } > "$TMP/o"
  { pre; row TOOL-zFixture-1 base; } > "$TMP/a"
  { pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 INCOMING; } > "$TMP/b"
  if "$PY" "$2/tools/memory-tree/merge-rows.py" "$TMP/o" "$TMP/a" "$TMP/b" x >/dev/null 2>&1; then
    bad "$1: the driver reported SUCCESS with no resolvable anchor grammar"
  fi
  grep -q 'INCOMING' "$TMP/a" || bad "$1: the incoming row vanished — this is the silent-take-ours shape"
  grep -q '^<<<<<<< ours$' "$TMP/a" || bad "$1: no conflict markers written"
}
mkscratch() { local d; d=$(mktemp -d); SCRATCH="$SCRATCH $d"
  mkdir -p "$d/tools/memory-tree" "$d/tools/memory-recall"
  cp tools/memory-tree/merge-rows.py "$d/tools/memory-tree/"
  printf '%s' "$d"; }
S=$(mkscratch); cp .memory-tree.conf "$S/"
printf 'this is not valid syntax(\n' > "$S/tools/memory-recall/extract.py"
failclosed "broken grammar" "$S"
S=$(mkscratch); cp .memory-tree.conf "$S/"          # kit dir present, extract.py absent
failclosed "missing grammar module" "$S"
S=$(mkscratch)                                       # no .memory-tree.conf above the driver
cp tools/memory-recall/extract.py tools/memory-recall/recall_conf.py "$S/tools/memory-recall/"
failclosed "missing .memory-tree.conf" "$S"

# --- 0d. the oracle is strictly WIDER than the driver's grammar, and `dups` fires -----------------
# The oracle earns its keep only if it can see something the subject cannot; otherwise "independent"
# is a comment, not a property. Both halves are proved here, in both directions, before any arm below
# leans on them: the widened oracle KEYS a suffixed id, the driver's own `key()` returns None for the
# identical line, `dups` REPORTS a repeat, and `dups` stays silent on a singleton.
SUFFIXED='- TOOL-zFixture-9b · a suffixed id the driver grammar cannot key'
printf '%s\n' "$SUFFIXED" > "$TMP/suffixed"
[ "$(ids "$TMP/suffixed")" = "TOOL-zFixture-9b " ] \
  || bad "oracle: the widened oracle does not see a suffixed id — case 12 would assert nothing"
"$PY" - "$SUFFIXED" <<'PYEOF' || bad "oracle: the DRIVER keys the suffixed id, so the oracle is no wider than the subject — pick a shape the grammar really misses"
import importlib.util, sys
sys.dont_write_bytecode = True   # a test that leaves __pycache__ in tools/ dirties the tree it gates
spec = importlib.util.spec_from_file_location("mr", "tools/memory-tree/merge-rows.py")
mr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mr)
sys.exit(0 if mr.key(sys.argv[1] + "\n") is None else 1)
PYEOF
{ printf '%s\n' "$SUFFIXED"; printf '%s\n' "$SUFFIXED"; } > "$TMP/twice"
[ "$(dups "$TMP/twice")" = "TOOL-zFixture-9b " ] \
  || bad "dups: a doubled id was not reported — every rc-0 arm's duplicate half is vacuous"
[ -z "$(dups "$TMP/suffixed")" ] || bad "dups: a singleton id was reported as a duplicate"

# --- 1. disjoint appends — the case the unit is FOR -----------------------------------------------
{ pre; row TOOL-zFixture-1 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 ours; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-3 theirs; } > "$TMP/b"
run "disjoint appends" 0 "TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-3 "

# --- 2. the shape that broke union: same id, different text, both sides ---------------------------
{ pre; row TOOL-zFixture-1 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 ours; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 theirs; } > "$TMP/b"
run "same id both sides" 1 "TOOL-zFixture-1 "
n=$(grep -c '^- TOOL-zFixture-1 ' "$TMP/a")
[ "$n" = 2 ] || bad "union-shape: expected both texts inside markers, got $n TOOL-zFixture-1 lines"
grep -q '^<<<<<<< ours$' "$TMP/a" || bad "union-shape: no conflict marker written"

# --- 3. one side edits, the other does not — take the change, silently ----------------------------
{ pre; row TOOL-zFixture-1 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 theirs; } > "$TMP/b"
run "one-sided edit" 0 "TOOL-zFixture-1 "
grep -q 'theirs' "$TMP/a" || bad "one-sided edit: took ours, not the side that changed"

# --- 4. a row deleted on one side — honour the delete, do not resurrect ---------------------------
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; } > "$TMP/b"
run "delete honoured" 0 "TOOL-zFixture-1 " TOOL-zFixture-2

# --- 4b. DELETE/MODIFY, both directions — the interaction that lost data upstream -----------------
# Case 4 only ever deletes a row NEITHER side touched, so both mixed cases walk straight through: the
# driver honours the delete, discards the other side's EDIT, and exits 0 "clean". Git conflicts on
# delete/modify precisely because neither resolution is the tool's to choose.
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 EDITED; } > "$TMP/b"
run "ours deleted, theirs edited" 1 "TOOL-zFixture-1 TOOL-zFixture-2 "
grep -q 'EDITED' "$TMP/a" || bad "delete/modify: theirs' edit was DISCARDED"

{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 EDITED; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; } > "$TMP/b"
run "ours edited, theirs deleted" 1 "TOOL-zFixture-1 TOOL-zFixture-2 "
grep -q 'EDITED' "$TMP/a" || bad "modify/delete: ours' edit was DISCARDED"

# --- 4c. conflict markers name ours/theirs, never a scratch path ----------------------------------
grep -q '^<<<<<<< ours$' "$TMP/a" || bad "markers: no ours marker"
if grep -qE '^(<<<<<<<|>>>>>>>|\|\|\|\|\|\|\|).*[A-Za-z]:[\\/]' "$TMP/a"; then
  bad "markers: a conflict marker carries an absolute path instead of ours/theirs"
fi

# --- 5. an unkeyable line INSIDE the row block keeps its position ---------------------------------
# Measured on this corpus: `## KICK — kickoff`, `## TOOL — tooling` and the `*(none yet)*` placeholder
# sit INSIDE memory/DECISIONS.md's row block, interleaved between anchored rows. A driver that
# hoisted them to the end would corrupt the file while exiting 0.
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n'; row TOOL-zFixture-2 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n'; row TOOL-zFixture-2 base; row TOOL-zFixture-4 ours; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n'; row TOOL-zFixture-2 base; } > "$TMP/b"
run "interleaved heading" 0 "TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-4 "
[ "$(grep -n '## Section two' "$TMP/a" | cut -d: -f1)" -lt "$(grep -n '^- TOOL-zFixture-2 ' "$TMP/a" | cut -d: -f1)" ] \
  || bad "interleaved heading: the section heading moved below its row"

# --- 6. empty %O — the file was ADDED on both sides; merge as a pure union of keys ----------------
: > "$TMP/o"
{ pre; row TOOL-zFixture-1 ours; } > "$TMP/a"
{ pre; row TOOL-zFixture-2 theirs; } > "$TMP/b"
run "empty base" 0 "TOOL-zFixture-1 TOOL-zFixture-2 "

# --- 7. identity: merging a real governed index against itself must change NOTHING ----------------
# The cheapest proof that the region split and the lead-in model do not mangle real files, and the
# one that caught upstream's first draft: it hoisted every unkeyed line to the end of the block.
# ENUMERATED BY GLOB, not listed, so a new backlog shard is covered the day it lands.
GOVERNED=$(printf '%s\n' memory/DECISIONS.md memory/backlog/*.md)
ngov=$(printf '%s\n' "$GOVERNED" | grep -c .)
[ "$ngov" -ge 2 ] || bad "identity: the governed-index glob matched $ngov files — the arm collapsed"
while IFS= read -r f; do
  [ -n "$f" ] && [ -f "$f" ] || continue
  cp "$f" "$TMP/o"; cp "$f" "$TMP/a"; cp "$f" "$TMP/b"
  $DRV "$TMP/o" "$TMP/a" "$TMP/b" x >/dev/null 2>&1 \
    || bad "identity $f: the driver reported a conflict merging a file with itself"
  cmp -s "$f" "$TMP/a" || bad "identity $f: output differs from input"
done <<EOF
$GOVERNED
EOF
# ...and both line-ending flavours EXPLICITLY, so all four newline sites are under a `cmp` regardless
# of how this node happens to have checked the tree out. This repo's nodes run core.autocrlf=true and
# the governed indexes are CRLF in the worktree, which is the format git hands a merge driver; a node
# that checked out LF must still not be told the CRLF sites are green.
LC_ALL=C tr -d '\r' < memory/DECISIONS.md > "$TMP/lf.md"
awk '{ printf "%s\r\n", $0 }' "$TMP/lf.md" > "$TMP/crlf.md"
LC_ALL=C grep -qU $'\r' "$TMP/crlf.md" || bad "the CRLF fixture carries no CR — the newline arm is vacuous"
for f in "$TMP/lf.md" "$TMP/crlf.md"; do
  cp "$f" "$TMP/o"; cp "$f" "$TMP/a"; cp "$f" "$TMP/b"
  $DRV "$TMP/o" "$TMP/a" "$TMP/b" x >/dev/null 2>&1 \
    || bad "identity $(basename "$f"): the driver reported a conflict merging a file with itself"
  cmp -s "$f" "$TMP/a" || bad "identity $(basename "$f"): line endings were rewritten"
done
# ...and a file with NO anchors at all is entirely preamble and round-trips unchanged.
{ pre; printf 'No id anywhere in this document.\n'; } > "$TMP/none.md"
cp "$TMP/none.md" "$TMP/o"; cp "$TMP/none.md" "$TMP/a"; cp "$TMP/none.md" "$TMP/b"
$DRV "$TMP/o" "$TMP/a" "$TMP/b" x >/dev/null 2>&1 || bad "identity no-anchor: reported a conflict"
cmp -s "$TMP/none.md" "$TMP/a" || bad "identity no-anchor: output differs from input"

# --- 7b. a PREAMBLE that genuinely three-way merges, in both line-ending flavours ------------------
# THE IDENTITY ARMS ABOVE CANNOT REACH `git merge-file` AT ALL: `text_merge` short-circuits on
# `a == b`, `o == a` and `o == b`, and an identity merge satisfies all three. So sites 2 and 3 of the
# newline contract — the temp writes and the captured stdout — are under test HERE and nowhere else.
# Measured: with upstream's `capture_output=True, text=True` on that capture (universal-newline mode)
# every identity arm still passes and this one reds, which is the whole reason the divergence is
# written down rather than inherited. Counting bytes rather than parsing lines is deliberate — awk on
# a Cygwin/MSYS node strips CR before it sees a byte, so a CR guard must be built out of `tr`/`wc`.
# The two edited lines are held APART by four unchanged ones on purpose: diff3 folds adjacent hunks
# into one conflicting region, so a fixture with them side by side asserts a conflict rather than the
# clean prose merge this arm is about.
prose()  { printf '# Index\n\n%s\n\nrouting prose\nmore routing prose\n\n%s\n\n' "$1" "$2"; }
cprose() { printf '# Index\r\n\r\n%s\r\n\r\nrouting prose\r\nmore routing prose\r\n\r\n%s\r\n\r\n' "$1" "$2"; }
crow() { printf -- '- %s · OPEN · %s\r\n' "$1" "$2"; }
endings() {  # "<CR count>:<LF count>" of a file
  printf '%s:%s' "$(LC_ALL=C tr -dc '\r' < "$1" | wc -c | tr -d ' ')" \
                 "$(LC_ALL=C tr -dc '\n' < "$1" | wc -c | tr -d ' ')"
}
{ cprose alpha beta;  crow TOOL-zFixture-1 base; } > "$TMP/o"
{ cprose ALPHA beta;  crow TOOL-zFixture-1 base; } > "$TMP/a"
{ cprose alpha BETA;  crow TOOL-zFixture-1 base; } > "$TMP/b"
run "crlf preamble three-way" 0 "TOOL-zFixture-1 "
grep -q 'ALPHA' "$TMP/a" || bad "crlf preamble: ours' prose edit was lost"
grep -q 'BETA' "$TMP/a" || bad "crlf preamble: theirs' prose edit was lost"
cr=$(endings "$TMP/a")
[ "${cr%%:*}" = "${cr##*:}" ] \
  || bad "crlf preamble: CR:LF byte counts are $cr — a newline site translated the merged region"
{ prose alpha beta; row TOOL-zFixture-1 base; } > "$TMP/o"
{ prose ALPHA beta; row TOOL-zFixture-1 base; } > "$TMP/a"
{ prose alpha BETA; row TOOL-zFixture-1 base; } > "$TMP/b"
run "lf preamble three-way" 0 "TOOL-zFixture-1 "
cr=$(endings "$TMP/a")
[ "${cr%%:*}" = 0 ] || bad "lf preamble: CR:LF byte counts are $cr — a CR was introduced into an LF file"

# --- 8. the printed audit line must RECONCILE with the file the driver just wrote -----------------
# That line is the only output this module produces, and it is the number an operator audits an
# auto-resolved merge with. Upstream shipped it unable to see a loss: `kept` was
# `sum(1 for k in a_order if k in A)` — a tautology, because `rows()` appends to `order` on exactly
# the branch that assigns `out[k]`. Reproduced there: base and ours 3 rows, theirs 1, both deletes
# honoured, a ONE-row file written, exit 0, and `3 row(s) from ours, 0 new from theirs, clean`
# printed. So this arm compares the counts against the RESULT, and case (b) is the discriminating one
# — `kept` there is 1 while the %A row count is 3, so the old expression cannot pass it.
audit() {   # $1 label · $2 want_rc · $3 want_kept · $4 want_took · $5 want_dropped
  local label=$1 want_rc=$2 rc err line kept took drop nrows
  err=$($DRV "$TMP/o" "$TMP/a" "$TMP/b" x 2>&1 >/dev/null) && rc=0 || rc=$?
  [ "$rc" = "$want_rc" ] || bad "audit $label: rc=$rc, expected $want_rc"
  line=$(printf '%s\n' "$err" | grep '^merge-rows: ' | tail -1)
  if [ -z "$line" ]; then
    bad "audit $label: the driver printed no audit line — nothing to reconcile"; return
  fi
  read -r kept took drop <<EOF
$(printf '%s\n' "$line" | awk '{print $2, $6, $10}')
EOF
  [ "$kept:$took:$drop" = "$3:$4:$5" ] \
    || bad "audit $label: printed kept:took:dropped $kept:$took:$drop, expected $3:$4:$5"
  nrows=$(grep -c '^- TOOL-' "$TMP/a")
  [ $((kept + took)) = "$nrows" ] \
    || bad "audit $label: printed $((kept + took)) row(s) but the written file holds $nrows"
}

# (a) disjoint appends — the ordinary shape; every counted row is really in the output
{ pre; row TOOL-zFixture-1 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 ours; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-3 theirs; } > "$TMP/b"
audit "disjoint appends" 0 2 1 0

# (b) THE DISCRIMINATING CASE. Two theirs-side deletes honoured: `kept` must be 1, not 3.
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; row TOOL-zFixture-3 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; row TOOL-zFixture-3 base; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; } > "$TMP/b"
audit "two deletes honoured" 0 1 0 2

# (c) the mirror — ours deleted a row theirs left alone, and theirs added one
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; row TOOL-zFixture-3 theirs; } > "$TMP/b"
audit "ours deleted, theirs appended" 0 1 1 1

# --- 9. END TO END: a real two-branch `git merge` through the real wiring --------------------------
# Everything above drives the driver by hand. This drives GIT, through the `.gitattributes` line and
# the `merge.rows.driver` config a node actually carries, which is the only arm that can catch a
# wiring string that does not start the driver at all. THREE directories are copied, not two: the
# configured command is `bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py …` and its paths are
# RELATIVE, so a fixture carrying only the two kits cannot launch anything.
E=$(mktemp -d); SCRATCH="$SCRATCH $E"
mkdir -p "$E/tools/memory-tree" "$E/tools/memory-recall" "$E/tools/lib" "$E/memory/backlog"
cp .memory-tree.conf "$E/"
cp tools/memory-tree/merge-rows.py "$E/tools/memory-tree/"
cp tools/memory-recall/extract.py tools/memory-recall/recall_conf.py "$E/tools/memory-recall/"
cp tools/lib/pyrun.sh tools/lib/resolve-python.sh "$E/tools/lib/"
(
  cd "$E" || exit 2
  git init -q -b main
  git config user.email t@e; git config user.name t; git config core.autocrlf false
  printf 'memory/DECISIONS.md merge=rows\nmemory/backlog/*.md merge=rows\n' > .gitattributes
  git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'
  { printf '# tooling backlog\n\n> Mutable. Each row leads with one status token.\n'
    row TOOL-zFixture-1 base; } > memory/backlog/TOOL.md
  git add -A; git commit -q -m base
  git checkout -q -b side
  row TOOL-zFixture-3 theirs >> memory/backlog/TOOL.md
  git commit -q -am theirs
  git checkout -q main
  row TOOL-zFixture-2 ours >> memory/backlog/TOOL.md
  git commit -q -am ours
  # the attribute must be what GIT judges, not what a grep of .gitattributes says
  git check-attr merge -- memory/backlog/TOOL.md | grep -q 'merge: rows' \
    || { echo "FAIL end-to-end: git does not resolve memory/backlog/TOOL.md to merge=rows"; exit 1; }
  git merge -q --no-edit side >/dev/null 2>&1 || { echo "FAIL end-to-end: git merge did not auto-resolve"; exit 1; }
  for want in TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-3; do
    c=$(grep -c "^- $want " memory/backlog/TOOL.md)
    [ "$c" = 1 ] || { echo "FAIL end-to-end: $want appears $c time(s), expected exactly 1"; exit 1; }
  done
  grep -q '<<<<<<<' memory/backlog/TOOL.md && { echo "FAIL end-to-end: conflict markers in an auto-resolved file"; exit 1; }
  exit 0
) || st=1

# --- 10. BOTH NODES OPEN THE SAME EMPTY SECTION — the shared lead-in is emitted ONCE ---------------
# A row is its lead-in plus its anchor, so when both sides add the FIRST row of the same section the
# two rows are id-disjoint and each carries its own copy of the SAME base furniture: the `## FAMILY`
# heading and the `*(none yet)*` placeholder. Both copies were emitted. Reproduced on the real
# memory/DECISIONS.md with two nodes opening `## DEPL`: rc 0, zero markers, audit line
# `1 new from theirs … clean`, and the heading present TWICE in an append-only file. The CONTROL is
# what makes it decisive — `git merge-file` on the identical three inputs returns rc 1 with one
# conflict hunk and one heading, so the driver was strictly WORSE than no driver on this input.
# `## KICK` and `## DEPL` are both empty in this corpus today, so the trigger is the next session in
# which two nodes each land a first decision in the same family.
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n*(none yet)*\n'; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n'; row TOOL-zFixture-2 ours; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n'; row TOOL-zFixture-3 theirs; } > "$TMP/b"
want_h=$(grep -h '^## ' "$TMP/o" "$TMP/a" "$TMP/b" | LC_ALL=C sort -u | grep -c .)   # BEFORE %A moves
[ "$want_h" = 1 ] || bad "shared lead-in: the fixture declares $want_h distinct headings, expected 1"
run "both nodes open the same empty section" 0 "TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-3 "
got_h=$(grep -c '^## ' "$TMP/a")
[ "$got_h" = "$want_h" ] \
  || bad "shared lead-in: the result carries $got_h '## ' heading line(s) against $want_h distinct across the three inputs"
[ "$(grep -c 'none yet' "$TMP/a")" = 0 ] \
  || bad "shared lead-in: the placeholder BOTH sides replaced is back in the merged file"
h=$(at_line '^## Section two$' "$TMP/a"); r=$(at_line '^- TOOL-zFixture-2 ' "$TMP/a")
{ [ "$h" -gt 0 ] && [ "$r" -gt 0 ] && [ "$h" -lt "$r" ]; } \
  || bad "shared lead-in: heading at line $h, ours' row at line $r (0 = absent) — the heading must open its section"

# --- 11. a %B-only row in a NON-FINAL section stays inside its section -----------------------------
# The mirror of case 5, which only ever covers a heading whose position must be PRESERVED — it adds
# the extra row on ONE side and never asks where an incoming row lands. Emitting every theirs-only
# row after ALL of ours' rows files an incoming decision under whatever `## FAMILY` heading happens
# to be last; position survived only when the incoming row was the FIRST of its section and so
# carried its own heading. Reproduced on the real file: an incoming `## PLAY` row landed under
# `## TOOL`, rc 0 clean. The CONTROL again decides it — the identical two inserts through git's
# built-in three-way merge resolve rc 0 with that row correctly under `## PLAY`, so this was a
# REGRESSION against the merge being replaced, not a design trade.
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n'; row TOOL-zFixture-2 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; printf '\n## Section two\n\n'; row TOOL-zFixture-2 base; row TOOL-zFixture-4 ours; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-5 theirs; printf '\n## Section two\n\n'; row TOOL-zFixture-2 base; } > "$TMP/b"
run "b-only row in a non-final section" 0 "TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-4 TOOL-zFixture-5 "
h=$(at_line '^## Section two$' "$TMP/a")
r=$(at_line '^- TOOL-zFixture-5 ' "$TMP/a"); m=$(at_line '^- TOOL-zFixture-4 ' "$TMP/a")
{ [ "$h" -gt 0 ] && [ "$r" -gt 0 ] && [ "$r" -lt "$h" ]; } \
  || bad "b-only placement: the incoming row is at line $r against the next heading at line $h (0 = absent) — it was filed into the wrong section"
{ [ "$m" -gt 0 ] && [ "$m" -gt "$h" ]; } \
  || bad "b-only placement: ours' own row is at line $m against the heading at line $h (0 = absent) — it left the section it was added to"

# --- 12. an UNKEYABLE row minted on both nodes, in different regions -------------------------------
# The keyed path guarantees uniqueness only for the rows the grammar KEYS, and it keys 35 of this
# corpus's 73 — the session era is bounded by `\b`, so the ratified `…-1b` correction form does not
# key at all. The other 38 are content: they reach the output down two independent paths (a row's
# lead-in, and the preamble/trailer text merges), so the same unkeyable row filed in different
# regions was written TWICE at rc 0 with the audit line reading `clean`, under a docstring claiming a
# row appears at most once BY CONSTRUCTION. It does not; the postcondition is what makes it true, and
# the driver must refuse rather than auto-resolve. Note git's own merge duplicates this input too —
# the bar here is not "no worse than git", it is "never a silent duplicate in an append-only record".
mk12() {
  { pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/o"
  { pre; row TOOL-zFixture-1 base; printf '%s\n' "$SUFFIXED"; row TOOL-zFixture-2 base; } > "$TMP/a"
  { pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; printf '%s\n' "$SUFFIXED"; } > "$TMP/b"
}
mk12
err=$($DRV "$TMP/o" "$TMP/a" "$TMP/b" x 2>&1 >/dev/null)
printf '%s\n' "$err" | grep -q 'DuplicatedContent' \
  || bad "unkeyable duplicate: the refusal does not name the postcondition — stderr was [$err]"
printf '%s\n' "$err" | grep -qF 'TOOL-zFixture-9b' \
  || bad "unkeyable duplicate: the refusal does not name the line it refused over"
mk12
run "unkeyable row minted on both nodes" 1 "TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-9b "
grep -q '^<<<<<<< ours$' "$TMP/a" \
  || bad "unkeyable duplicate: rc 1 with NO markers is the marker-free-UU trap — write the conflict"
# ...and the postcondition does NOT fire on the same row arriving from one side only, or every clean
# append below it is one refusal away from unusable.
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/o"
{ pre; row TOOL-zFixture-1 base; printf '%s\n' "$SUFFIXED"; row TOOL-zFixture-2 base; } > "$TMP/a"
{ pre; row TOOL-zFixture-1 base; row TOOL-zFixture-2 base; } > "$TMP/b"
run "unkeyable row from one side only" 0 "TOOL-zFixture-1 TOOL-zFixture-2 TOOL-zFixture-9b "

# The count is DERIVED from the file, not typed: a hand-maintained tally reads as a claim about
# coverage and goes stale the first time a group is added without touching it.
ngroups=$(grep -c '^# --- ' "$SELF")
[ "$ngroups" -ge 20 ] || bad "the fixture-group scan found $ngroups groups — the count is mis-selecting"
[ "$st" = 0 ] && echo "PASS — merge-rows: $ngroups fixture groups held"
exit "$st"
