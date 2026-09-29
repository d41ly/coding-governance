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
#   3. ONE CUTOFF IS ONE-SIDED, THE OTHER IS SHARED. FORK_MARK_CUTOFF gates the hygiene side alone;
#      the planning verb is tightened unconditionally, because it grades only the specs of the build
#      currently running. A case may therefore legitimately get two different verdicts, and the
#      table says so per row. FORK_ITEM_CUTOFF (TOOL-dDerivedDocket-31) gates BOTH: the engine sources
#      it and the planning side reads the same line as TEXT through the unattended library, so every
#      planning row below receives the value that reader returns for the fixture conf, and the rows
#      dated past it are the per-F-item contract.
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
# The planning side's cutoff reader and the second planning caller, both DERIVED from the install
# prefix like the driver above. The reader is sliced the same way, so the harness grades shipped bytes.
L="$KITS_DIR/unattended/lib-unattended.sh"
PO="$KITS_DIR/unattended/check-pass-order.sh"
_rc_start=$(grep -n '^read_fork_cutoff()' "$L" | cut -d: -f1)
_rc_end=$(awk -v s="${_rc_start:-0}" 'NR>s && /^}/ {print NR; exit}' "$L")
[ -n "$_rc_start" ] && [ -n "$_rc_end" ] && [ "$_rc_end" -gt "$_rc_start" ] || { echo "FAIL cannot slice read_fork_cutoff out of $L, so every planning row below would be handed a cutoff nothing read"; exit 1; }
mk_awk r_cutoff "$L" "$_rc_start" "$_rc_end"

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
  # ahead of every landed spec so nothing ratified goes retroactively red. FORK_ITEM_CUTOFF sits
  # BETWEEN the two fixture eras: the 2026-08-09 rows keep the section-wide reading, the 2026-09-20
  # rows are graded per F-item.
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\nFORK_MARK_CUTOFF="2026-08-01"\nFORK_ITEM_CUTOFF="2026-09-15"\n' > .memory-tree.conf
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
MARK_NAMES=(); MARK_DATES=(); MARK_WANT_HYG=""; MARK_WANT_PLAN=""
# The FILENAME DATE is the fifth argument, 2026-08-09 by default, and BOTH copies carry it: the
# planning copy is named `<date>-plan-<n>.md` because `plan_state` reads the date from the basename,
# exactly as the engine does, and a dateless name would grade every row under the old reading.
mark_case() { # name · want_hygiene(red|silent) · want_plan(READY|FORKED) · section-8 body · [date]
  mark_case_n=$((mark_case_n+1))
  local slug="tMark$mark_case_n" d="${5:-2026-08-09}"
  mkdir -p "$FT/memory/builds/$slug/spec"
  spec_doc "CLOSED" "$4" > "$FT/memory/builds/$slug/spec/$d-spec-ARCH-$slug-1.md"
  spec_doc "SPECCED" "$4" > "$T/$d-plan-$mark_case_n.md"
  MARK_NAMES+=("$1"); MARK_DATES+=("$d")
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
# a regular shape, which is a scope change and not a predicate change. TOOL-dDerivedDocket-31 IS that
# scope change, FORWARD-ONLY: this row stays a gap for a document dated before FORK_ITEM_CUTOFF, and
# its post-cutoff twin below reads red and FORKED.
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
# CASE AND WRAPPING GET THEIR OWN ROWS, because reverting either fix left this table green. The case
# alignment and the whitespace squeeze were both landed with no row that could see them, which is the
# could-not-fail shape this whole build is about - in the artifact whose job is proving the two
# readers agree.
#
# THE DENIAL ROW is the one that matters most: `/^none/` is an UNANCHORED prefix on a lowercased
# line, so a sentence saying the forks are NOT resolved read as a none-form and resolved the section.
# Aligning the readers on case aligned them on that. With items present the opening line no longer
# votes at all; only a conforming mark does.
mark_case "denial that starts with none" red   FORKED   'None of the forks below are resolved.

- **F1 — open?** nobody has signed this off.'
mark_case "none form in mixed case"     silent READY    'None - every fork below is RESOLVED in place.

- **F1 — answered?** yes.
  RESOLVED (owner, 2026-08-09): picked.'
mark_case "N/A in upper case, no items" silent READY    'N/A'

# ---- TOOL-dDerivedDocket-31 - THE F-ITEM ROWS, every one dated PAST the fixture FORK_ITEM_CUTOFF.
# ---- An F-item opens on a column-0 `- **F<n>` bullet or a `### F<n>` sub-head and spans every line
# ---- to the next one; each span needs its OWN mark. The hygiene side grades them at a terminal
# ---- status, and a Tier-2 section of any other shape through its shape arm; the planning side
# ---- grades the same bytes. The two defects the withdrawn per-item walk was measured on each get a
# ---- row: a wrapped mark (line-by-line matching) and option bullets (every bullet opening an item).
PD=2026-09-20
mark_case "item: F2 unmarked below a marked F1" red FORKED '- **F1 — answered?** options.
  RESOLVED (owner, 2026-08-09): picked.

- **F2 — not answered?** still open, no mark.' "$PD"
mark_case "item: both marked"              silent READY  '- **F1 — one?** RESOLVED (owner, 2026-08-09): a.
- **F2 — two?** RESOLVED (agent, 2026-08-09, delegated): b.' "$PD"
mark_case "item: mark only in backticks"   red    FORKED '- **F1 — one?** write `RESOLVED (owner, 2026-08-09): a` once decided.' "$PD"
mark_case "item: mark only in dquotes"     red    FORKED '- **F1 — one?** write "RESOLVED (owner, 2026-08-09): a" once decided.' "$PD"
mark_case "item: mark wrapped at the paren" silent READY '- **F1 — one?** options and a recommendation.
  RESOLVED (owner,
  2026-08-09): picked A.' "$PD"
mark_case "item: three options, one mark"  silent READY  '- **F1 — which way?** three ways.
- (a) the first way
- (b) the second way
- (c) the third way
  RESOLVED (owner, 2026-08-09): (a).' "$PD"
mark_case "item: none line, later open"    red    FORKED 'none - every fork below is RESOLVED in place.

- **F1 — answered?** yes.
  RESOLVED (owner, 2026-08-09): picked.

- **F2 — not answered?** still open, no mark.' "$PD"
mark_case "item: plain bullet before F1"   red    FORKED '- a note written as a bullet before any fork
- **F1 — one?** RESOLVED (owner, 2026-08-09): a.' "$PD"
mark_case "item: bullets and no F-item"    red    FORKED '- **Q — a question without a fork id?** RESOLVED (owner, 2026-08-09): a.' "$PD"
# ONE ROW PER ADMITTED SPELLING, each unmarked, so an engine admitting fewer either never opens the
# F-item (and the shape arm reds it instead of the mark arm) or opens it and still grades it.
mark_case "spelling: F1 bold, then the question" red FORKED '- **F1** — a question, unmarked.' "$PD"
mark_case "spelling: bold spans the question"    red FORKED '- **F1 — a question?** unmarked.' "$PD"
mark_case "spelling: a sub-head"                 red FORKED '### F1 — a question

options, unmarked.' "$PD"
mark_case "spelling: fact-question prefix"       red FORKED '- **FACT-QUESTION · F1 — does X hold?** a probe decides it, unmarked.' "$PD"
mark_case "item: none, zero items"          silent READY  'none - no forks here.' "$PD"

( cd "$FT" && git add -A >/dev/null 2>&1 && git -c commit.gpgsign=false commit -q -m fx --no-verify ) >/dev/null 2>&1
hyg_out=$( cd "$FT" && bash "$HYG" 2>&1 )
# THE PLANNING SIDE'S CUTOFF, read from the SAME fixture conf through the reader the planning callers
# use. A row handed no cutoff would pass its post-cutoff case under the old reading, which is the
# defect the call-site count below guards in the shipped callers.
ITEM_CUT=$(r_cutoff "$FT/.memory-tree.conf")
ncase=$((ncase+1))
[ "$ITEM_CUT" = "2026-09-15" ] || { echo "FAIL [item/cutoff] the planning reader read [$ITEM_CUT] from the fixture conf, which declares 2026-09-15"; st=1; }

i=0
for want_h in $MARK_WANT_HYG; do
  i=$((i+1))
  nm=${MARK_NAMES[i-1]}
  ncase=$((ncase+1))
  # Only the section-8 verdict is read. The scratch tree reds other checks on purpose and that noise
  # is ignored, exactly as this kit's sibling test documents — but the grep is anchored on the FILE
  # plus the section-8 reason, so an unrelated fault on the same file cannot forge a hit.
  if printf '%s\n' "$hyg_out" | grep -q "tMark$i-1.md (terminal Status.*§8\|tMark$i-1.md (terminal Status and a §8\|tMark$i-1.md (§8 is not F-item shaped"; then got_h=red; else got_h=silent; fi
  [ "$got_h" = "$want_h" ] || { echo "FAIL [mark/$nm] hygiene said $got_h, contract says $want_h"; st=1; }
done

i=0
for want_p in $MARK_WANT_PLAN; do
  i=$((i+1))
  nm=${MARK_NAMES[i-1]}
  ncase=$((ncase+1))
  got_p=$(r_plan "$T/${MARK_DATES[i-1]}-plan-$i.md" "$ITEM_CUT")
  [ "$got_p" = "$want_p" ] || { echo "FAIL [mark/$nm] plan_state said $got_p, contract says $want_p"; st=1; }
done

# THE FINDING NAMES THE FORK. A red row proves only that something about the section reddened; the
# per-item reading exists to say WHICH F-item is open, and the row above has a marked F1 beside it.
ncase=$((ncase+1))
printf '%s\n' "$hyg_out" | grep -F 'F-items carrying no conforming resolution mark in their own span' | grep -qE ': F2$' || {
  echo "FAIL [item/names-F2] the hygiene side did not name F2 as the open F-item below a marked F1"; st=1; }

# ---- BLANK AND ABSENT ARE THE DECLARED OFF STATE, in BOTH readers. Blank is the shipped adopter
# ---- default and the one value a date comparison gets wrong by default: every filename date sorts at
# ---- or after the empty string. So the post-cutoff F2 row is re-graded with the key blank and then
# ---- with it absent, and both readers must answer as they did before this cutoff existed.
_f2=$(printf '%s\n' "${MARK_NAMES[@]}" | grep -nxF 'item: F2 unmarked below a marked F1' | cut -d: -f1)
for _off in blank absent; do
  if [ "$_off" = blank ]; then _kv='FORK_ITEM_CUTOFF=""\n'; else _kv=''; fi
  printf "MEMORY_ROOT=memory\nDISCIPLINES=\"architecture\"\nFAMILIES=\"architecture:ARCH\"\nSPEC_FORMAT_CUTOFF=\"2026-07-15\"\nFORK_MARK_CUTOFF=\"2026-08-01\"\n$_kv" > "$FT/.memory-tree.conf"
  _cut=$(r_cutoff "$FT/.memory-tree.conf"); _crc=$?
  _ho=$( cd "$FT" && bash "$HYG" 2>&1 )
  ncase=$((ncase+1))
  [ "$_crc" = 0 ] && [ -z "$_cut" ] || { echo "FAIL [item/$_off] the planning reader returned rc=$_crc [$_cut] for a conf whose key is $_off"; st=1; }
  ncase=$((ncase+1))
  if printf '%s\n' "$_ho" | grep -q "tMark$_f2-1.md (terminal Status.*§8\|tMark$_f2-1.md (§8 is not F-item shaped"; then
    echo "FAIL [item/$_off] with FORK_ITEM_CUTOFF $_off the hygiene side still graded the post-cutoff F2 row per item"; st=1
  fi
  ncase=$((ncase+1))
  _p=$(r_plan "$T/$PD-plan-$_f2.md" "$_cut")
  [ "$_p" = READY ] || { echo "FAIL [item/$_off] with FORK_ITEM_CUTOFF $_off plan_state said $_p for the post-cutoff F2 row, and the section-wide reading says READY"; st=1; }
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

# ---- EVERY PLANNING CALLER PASSES THE CUTOFF. A `plan_state` call handed one argument grades the
# ---- section as a whole, so it would plan READY on an unmarked F2 below a marked F1 while every row
# ---- above stayed green: the table grades the classifier, and this grades who calls it. Enumerated
# ---- by grep over the driver and the pass-order leg, comment lines dropped; the COUNT is printed and
# ---- a zero is a dead probe, never a clean one.
_pcs=$(grep -nE 'plan_state "' "$U" "$PO" 2>/dev/null | grep -vE '^[^:]+:[0-9]+:[[:space:]]*#')
_pcs_n=$(printf '%s\n' "$_pcs" | grep -c . || true)
_pcs_bad=$(printf '%s\n' "$_pcs" | grep . | grep -vE 'plan_state "[^"]+" "\$FORK_CUTOFF"' || true)
ncase=$((ncase+1))
if [ "${_pcs_n:-0}" -eq 0 ]; then
  echo "FAIL [item/callers] DEAD PROBE: no plan_state call site was found in $U or $PO, so no caller was graded"; st=1
elif [ -n "$_pcs_bad" ]; then
  echo "FAIL [item/callers] a plan_state call site does not pass the cutoff as its second argument:"; printf '%s\n' "$_pcs_bad"; st=1
else
  echo "marker-contract: $_pcs_n plan_state call site(s) in the driver and the pass-order leg, each passing the cutoff"
fi

# ---- THE TWO READINGS OF ONE LINE, compared at TEST time. The engine SOURCES the conf; the planning
# ---- side re-parses it as text, because it must not execute a second kit's conf. The sanctioned form
# ---- of that re-parse is a compare against the authoritative read, so each spelling below goes to
# ---- both the sliced reader and a subshell `.` of the same file. Column-0 spellings must AGREE. A
# ---- spelling a shell accepts and the reader does not model must agree or REFUSE naming its line —
# ---- never come back blank, which is the declared OFF state and would silence the planning side alone.
CF="$T/cut.conf"
check_reader_pair() { # name · conf body · want (agree|refuse|refuse-value)
  printf '%s\n' "$2" > "$CF"
  local _t _trc _s
  _t=$(r_cutoff "$CF"); _trc=$?
  _s=$( . "$CF" >/dev/null 2>&1; printf '%s' "${FORK_ITEM_CUTOFF-}" )
  ncase=$((ncase+1))
  case "$3:$_trc" in
    agree:0) [ "$_t" = "$_s" ] || { echo "FAIL [reader/$1] text read [$_t], a sourced read [$_s]"; st=1; } ;;
    refuse:2) printf '%s' "$_t" | grep -qF 'in a spelling this text reader does not resolve' || { echo "FAIL [reader/$1] refused without naming the unresolved line: $_t"; st=1; } ;;
    refuse-value:2) printf '%s' "$_t" | grep -qF 'which is neither blank nor a zero-padded ISO date' || { echo "FAIL [reader/$1] refused a bad value without saying why: $_t"; st=1; } ;;
    *) echo "FAIL [reader/$1] wanted $3, the text reader returned rc=$_trc [$_t] and a sourced read gave [$_s]"; st=1 ;;
  esac
}
check_reader_pair "quoted, trailing comment" 'FORK_ITEM_CUTOFF="2026-09-15"  # note' agree
check_reader_pair "single-quoted"            "FORK_ITEM_CUTOFF='2026-09-15'" agree
check_reader_pair "repeated, last wins"      'FORK_ITEM_CUTOFF="2026-09-01"
FORK_ITEM_CUTOFF="2026-09-15"' agree
check_reader_pair "bare value"               'FORK_ITEM_CUTOFF=2026-09-15' agree
check_reader_pair "matched and empty"        'FORK_ITEM_CUTOFF=' agree
check_reader_pair "not a date"               'FORK_ITEM_CUTOFF=2026-09-15x' refuse-value
check_reader_pair "export prefix"            'export FORK_ITEM_CUTOFF="2026-09-15"' refuse
check_reader_pair "indented"                 '  FORK_ITEM_CUTOFF="2026-09-15"' refuse
check_reader_pair "inside a conditional"     'if true; then FORK_ITEM_CUTOFF="2026-09-15"; fi' refuse


# =============================================================================================
# CONTRACT 3 - THE REVIEW-VERDICT VOCABULARY. Spelled independently in two kits with nothing pairing
# them: the unattended driver holds REVIEW_VERDICTS, the hygiene engine hardcodes the same three
# tokens in its own awk. A drift lets a run RECORD a verdict the hygiene gate then refuses, on an
# append-only record no verb can rewrite - the same cross-kit edge contract 2 exists to forbid, and
# the one the sibling grammar got and this pair did not.
#
# BOTH SIDES ARE READ AS DATA, never sourced, so this compares the shipped bytes rather than a copy.
ncase=$((ncase+1))
_cv_drv=$(sed -n 's/^REVIEW_VERDICTS="\(.*\)"$/\1/p' "$U" | head -1 | tr '|' '
' | sort)
_cv_hyg=$(grep -oE 'v != "[A-Z][A-Z ]*"' "$HYG" | sed 's/.*"\(.*\)"/\1/' | sort -u)
if [ -z "$_cv_drv" ] || [ -z "$_cv_hyg" ]; then
  echo "FAIL [verdict/read] one side of the verdict vocabulary read as EMPTY, so the comparison below would pass by comparing nothing: driver=[$_cv_drv] hygiene=[$_cv_hyg]"
  st=1
elif [ "$_cv_drv" != "$_cv_hyg" ]; then
  echo "FAIL [verdict/agree] the driver and the hygiene engine disagree on the closed verdict set, so a run can record a token the gate then refuses forever: driver=[$(echo $_cv_drv | tr '
' ' ')] hygiene=[$(echo $_cv_hyg | tr '
' ' ')]"
  st=1
fi


[ "$st" = 0 ] && echo "PASS ($ncase cases across 3 contracts, marker-region, section-8 mark with its F-item cutoff, and review verdicts, held)"
exit $st
