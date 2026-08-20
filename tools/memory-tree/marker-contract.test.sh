#!/usr/bin/env bash
# The reader CONTRACTS this repo cannot express as shared code, and the live readers that must obey
# each one. Two contracts live here now, which is why the leg is named in the plural:
#
#   1. MARKER-REGION well-formedness — four readers, three awk in the unattended kit and one Python
#      here. The original contract, and the reason this harness exists.
#   2. The section-8 RESOLUTION MARK — two readers, one per kit, grading whether a fork is resolved.
#      Added when both were tightened from a first-line substring to a per-item shaped mark; they
#      cannot share code across a kit boundary, so AGREEMENT is proven instead.
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


# =============================================================================================
# CONTRACT 2 — THE SECTION-8 RESOLUTION MARK. Two readers, one per kit, and they cannot share code:
# `plan_state` is awk inside the unattended driver, the hygiene side is awk inside this kit's engine,
# and a cross-kit edge is the thing this harness exists to forbid. So AGREEMENT is proven.
#
# WHY THE TWO SIDES ARE DRIVEN DIFFERENTLY, which is the part a reader will not guess. Three
# obstacles, each measured rather than assumed:
#
#   1. NOT SLICEABLE. The hygiene predicate is inline inside one long single-quoted awk program with
#      no function boundary, so the mk_awk slicing used above has nothing to cut. The alternative was
#      lifting it into its own shell function first; that restructures a thousand-line program to make
#      a test convenient, so the hygiene side is driven through a FIXTURE REPO instead — the way this
#      kit's own sibling test already drives it.
#   2. DISJOINT POPULATIONS. The hygiene section-8 block runs ONLY under a terminal status; the
#      planning verb discards its own classification for exactly those statuses. So no single fixture
#      document can be graded by both, and each case is written TWICE — same section 8, different
#      status — which is why the table carries a per-reader verdict and not one shared answer.
#   3. THE CUTOFF IS ONE-SIDED. FORK_MARK_CUTOFF gates the hygiene side alone; the planning verb is
#      tightened unconditionally, because it grades only the specs of the build currently running.
#      A case may therefore legitimately get two different verdicts, and the table says so per row.
#
# THE TABLE IS THE CONTRACT. Neither reader restates it in prose.

# The planning reader, sliced out of the SHIPPED driver bytes like the three above it.
#
# THE END LINE IS DERIVED, NOT COUNTED. It was `start + 45`, and the function has since grown past
# that: the slice silently truncated the last seven lines, which are the ones that decide READY vs
# FORKED. A magic span over a live function is a fixture that stops covering what it names, and it
# reports nothing when it does - the same could-not-fail shape this contract exists to catch.
_ps_start=$(grep -n '^plan_state()' "$U" | cut -d: -f1)
_ps_end=$(awk -v s="$_ps_start" 'NR>s && /^}/ {print NR; exit}' "$U")
[ -n "$_ps_end" ] && [ "$_ps_end" -gt "$_ps_start" ] || { echo "FAIL cannot find the closing brace of plan_state in $U, so the sliced reader below would be graded against a fragment"; exit 1; }
mk_awk r_plan "$U" "$_ps_start" "$_ps_end"

FT=$(mktemp -d) || exit 2
trap 'rm -rf "$T" "$FT"' EXIT
HYG="$ROOT/$KIT_MT/check-memory-hygiene.sh"
if [ ! -f "$HYG" ]; then
  echo "marker-contract: SKIP contract 2 — no hygiene engine at $HYG, so only one of its two readers exists"
else
( cd "$FT" || exit 2
  git init -q . >/dev/null 2>&1
  git config user.email t@t.test; git config user.name t; git config core.autocrlf false
  # The cutoff sits BELOW the fixture dates on purpose: these documents are the only place the
  # tightened hygiene reader can be exercised at all, because the real cutoff is deliberately set
  # ahead of every landed spec so nothing ratified goes retroactively red.
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\nFORK_MARK_CUTOFF="2026-08-01"\n' > .memory-tree.conf
  printf 'sentinel\n' > memory/HYGIENE.md 2>/dev/null || { mkdir -p memory && printf 'sentinel\n' > memory/HYGIENE.md; }
) >/dev/null 2>&1

# spec_doc <status> <the section 8 body>
spec_doc() {
  printf '# ARCH-tMark-1 — fixture\n\n**Status:** %s · rev-1 · 2026-08-09 · node a · Tier-2 · base 0123abcd\n\n## 1. Goal\n\nA goal.\n\n## 2. Scope (IN)\n\n- S1 something.\n\n## 3. Non-goals (OUT)\n\n- Nothing else.\n\n## 4. Design\n\nThe design.\n\n## 5. Production-readiness checklist\n\n- security: N/A.\n\n## 6. Acceptance criteria\n\n- AC1 When run, `check-memory-hygiene.sh` passes.\n\n## 7. Gates\n\n- memory hygiene.\n\n## 8. Open questions\n\n%s\n\n## 9. Revision log\n\n- rev-1 · 2026-08-09 · initial draft.\n\n## 10. Reuse audit\n\nNo existing seam fits.\n' "$1" "$2"
}

# Write every case into the fixture repo as a TERMINAL spec, one build folder each, then run the
# hygiene gate ONCE over the whole tree. N gate runs would cost N process startups to learn the same
# thing; the gate reports every file it faults, so one run answers every row.
mark_case_n=0
# AN ARRAY, because these names are MULTI-WORD. As a space-separated string with `set -- $MARK_NAMES`
# they word-split: ten cases became ~33 positional parameters, so case 1 reported as `none,`, case 2
# as `zero`, case 3 as `items`. Grading was unaffected - the fixture index drives it - so the
# misattribution surfaced only on the run where a row goes red, which is the one run the label has
# to be right on. It surfaced on exactly such a run: a real failure reported itself as `[mark/on]`.
MARK_NAMES=(); MARK_WANT_HYG=""; MARK_WANT_PLAN=""
mark_case() { # name · want_hygiene(red|silent) · want_plan(READY|FORKED) · section-8 body
  mark_case_n=$((mark_case_n+1))
  local slug="tMark$mark_case_n"
  mkdir -p "$FT/memory/builds/$slug/spec"
  spec_doc "CLOSED" "$4" > "$FT/memory/builds/$slug/spec/2026-08-09-spec-ARCH-$slug-1.md"
  spec_doc "SPECCED" "$4" > "$T/plan-$mark_case_n.md"
  MARK_NAMES+=("$1")
  MARK_WANT_HYG="$MARK_WANT_HYG $2"
  MARK_WANT_PLAN="$MARK_WANT_PLAN $3"
}

#          name                     hygiene   plan     the section 8 body
mark_case "none, zero items"        silent    READY    'none - no forks here.'
mark_case "marked on the open line" silent    READY    '- **F1 — a question?** RESOLVED (owner, 2026-08-09): picked.'
mark_case "marked on continuation"  silent    READY    '- **F1 — a question?** options.
  RESOLVED (agent, 2026-08-09, delegated): picked.'
mark_case "word, no attribution"    red       FORKED   '- **F1 — a question?** RESOLVED: informally, sometime.'
# THE PARKED GAP, PINNED AS A GAP RATHER THAN LEFT UNMENTIONED. A `none` opening line followed by an
# unresolved fork is NOT caught by either reader, and both say READY/silent. The per-item walk that
# would catch it was withdrawn on measurement: this corpus does not distinguish a FORK bullet from an
# OPTION bullet - of 287 section-8 bullets, 69 carry descriptive labels, and among those are both
# resolved forks and genuinely open ones - so a walk over-counts on real specs (it called a RESOLVED
# fork unresolved on a live tracked spec whose three option bullets each demanded a mark) and any
# label-shape discriminator under-counts instead, which is worse. Closing it needs section 8 to have
# a regular shape, which is a scope change and not a predicate change.
mark_case "none line, later open"   silent    READY    'none - every fork below is RESOLVED in place.

- **F1 — answered?** yes.
  RESOLVED (owner, 2026-08-09): picked.

- **F2 — not answered?** still open, no mark.'
mark_case "first line denies it"    red       FORKED   'F1 below is NOT RESOLVED and needs the owner.

- **F1 — a question?** options, unmarked.'
mark_case "resolver off the set"    red       FORKED   '- **F1 — a question?** options.
  RESOLVED (builder, 2026-08-09): picked by a name the grammar does not admit.'
mark_case "fact-question, no mark"  red       FORKED   '- **FACT-QUESTION · F1 — does X hold?** a probe decides it.'
mark_case "fact-question + mark"    silent    READY    '- **FACT-QUESTION · F1 — does X hold?** a probe decides it.
  RESOLVED (agent, 2026-08-09, delegated): it holds.'
mark_case "hollow: no item, no none" red      FORKED   'This section says nothing at all in prose.'
# THE MARK WRAPS, which is this corpus's house style at its line width: fourteen tracked specs carry
# one, and every reader matched line-by-line missed all fourteen. It wraps INSIDE the parenthesis, so
# joining the section without squeezing whitespace leaves three spaces where the grammar wants one -
# the half of the fix that a naive join silently omits.
mark_case "mark wrapped at the paren" silent  READY    '- **F1 — a question?** options and a recommendation.
  RESOLVED (owner,
  2026-08-09): picked A.'
# AN EMPTY SECTION IS A REFUSAL in both readers - the build's own ratified fork. plan_state printed
# READY for it while the hygiene reader red it, and this is the one case that separates a resolved
# section from a hollow one, so it is the case the contract most needed and did not have. The
# neighbouring `hollow` row uses a PROSE line, which both readers already refuse.
mark_case "empty: no body at all"   red       FORKED   ''

( cd "$FT" && git add -A >/dev/null 2>&1 && git -c commit.gpgsign=false commit -q -m fx --no-verify ) >/dev/null 2>&1
hyg_out=$( cd "$FT" && bash "$HYG" 2>&1 )

i=0
for want_h in $MARK_WANT_HYG; do
  i=$((i+1))
  nm=${MARK_NAMES[i-1]}
  ncase=$((ncase+1))
  # Only the section-8 verdict is read. The scratch tree reds other checks on purpose and that noise
  # is ignored, exactly as this kit's sibling test documents — but the grep is anchored on the FILE
  # plus the section-8 reason, so an unrelated fault on the same file cannot forge a hit.
  if printf '%s\n' "$hyg_out" | grep -q "tMark$i-1.md (terminal Status.*§8\|tMark$i-1.md (terminal Status and a §8"; then got_h=red; else got_h=silent; fi
  [ "$got_h" = "$want_h" ] || { echo "FAIL [mark/$nm] hygiene said $got_h, contract says $want_h"; st=1; }
done

i=0
for want_p in $MARK_WANT_PLAN; do
  i=$((i+1))
  nm=${MARK_NAMES[i-1]}
  ncase=$((ncase+1))
  got_p=$(r_plan "$T/plan-$i.md")
  [ "$got_p" = "$want_p" ] || { echo "FAIL [mark/$nm] plan_state said $got_p, contract says $want_p"; st=1; }
done

# THE CONTROL, and without it every row above could be passing for the wrong reason. The gate must
# have actually RUN over these fixtures: if the fixture repo were misbuilt, or the engine exited
# early, every case would read `silent` and the four rows wanting `silent` would pass while the six
# wanting `red` failed loudly — but a future edit that flipped all ten to `silent` would go green.
ncase=$((ncase+1))
printf '%s\n' "$hyg_out" | grep -q 'tMark' || {
  echo "FAIL [mark/control] the hygiene engine named no fixture at all, so contract 2 graded nothing"
  st=1
}
fi


# =============================================================================================
# CONTRACT 3 - THE REVIEW-VERDICT VOCABULARY. Spelled independently in two kits with nothing pairing
# them: the unattended driver holds REVIEW_VERDICTS, the hygiene engine hardcodes the same three
# tokens in its own awk. A drift lets a run RECORD a verdict the hygiene gate then refuses, on an
# append-only record no verb can rewrite - the same cross-kit edge contract 2 exists to forbid, and
# the one the sibling grammar got and this pair did not.
#
# BOTH SIDES ARE READ AS DATA, never sourced, so this compares the shipped bytes rather than a copy.
ncase=$((ncase+1))
_cv_drv=$(sed -n 's/^REVIEW_VERDICTS="\(.*\)"$//p' "$U" | head -1 | tr '|' '
' | sort)
_cv_hyg=$(grep -oE 'v != "[A-Z][A-Z ]*"' "$HYG" | sed 's/.*"\(.*\)"//' | sort -u)
if [ -z "$_cv_drv" ] || [ -z "$_cv_hyg" ]; then
  echo "FAIL [verdict/read] one side of the verdict vocabulary read as EMPTY, so the comparison below would pass by comparing nothing: driver=[$_cv_drv] hygiene=[$_cv_hyg]"
  st=1
elif [ "$_cv_drv" != "$_cv_hyg" ]; then
  echo "FAIL [verdict/agree] the driver and the hygiene engine disagree on the closed verdict set, so a run can record a token the gate then refuses forever: driver=[$(echo $_cv_drv | tr '
' ' ')] hygiene=[$(echo $_cv_hyg | tr '
' ' ')]"
  st=1
fi


[ "$st" = 0 ] && echo "PASS ($ncase cases across 3 contracts, marker-region, section-8 mark and review verdicts, held)"
exit $st
