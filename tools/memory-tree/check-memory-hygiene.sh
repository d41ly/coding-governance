#!/usr/bin/env bash
# Structured-memory-tree hygiene gate — the mechanized form of <MEMORY_ROOT>/HYGIENE.md.
# Config-driven (.memory-tree.conf: MEMORY_ROOT, DISCIPLINES, FAMILIES, TOMBSTONE_ROOTS,
# SPEC_FORMAT_CUTOFF). Single source
# of truth: HYGIENE.md's "Check" section, CI, the pre-commit hook, and the local gate runner all invoke
# THIS script — never hand-copy the checks. Part of the coding-governance memory-tree kit.
#
#   tools/memory-tree/check-memory-hygiene.sh            # full check
#   tools/memory-tree/check-memory-hygiene.sh --staged   # pre-commit fast leg (set-checks tree-wide, file-checks on staged paths)
#
# Exit 0 + no output = clean. Anything printed is a hygiene regression.
set -u
KIT_MEMORY_TREE_VERSION=2.34   # gov:kit memory-tree@2.34 — engine identity; set HERE, never from .memory-tree.conf (a project conf must not spoof it)
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
# DISCIPLINES is a CLOSED ENUM of stream values, not a directory list. Since 1.5 the tree is FLAT:
# every build lives at <MEMORY_ROOT>/builds/<slug>/ and the discipline is declared in each spec's
# status header as `streams <value>[+<value>]`. FAMILIES maps an enum value to its id prefix, its
# backlog shard, and the optional FAMILY qualifier in a recording filename.
DISCIPLINES="architecture deployment blocks design performance"
FAMILIES="architecture:ARCH deployment:DEPLOY blocks:BLOCK design:DES performance:PERF"
TOMBSTONE_ROOTS=""     # old tree root(s) a migrated project must keep empty (e.g. "docs"); blank = skip check 11
SPEC_FORMAT_CUTOFF=""  # date; specs whose filename date >= this must follow TEMPLATE-SPEC.md (check 12); blank = skip
STREAMS_CUTOFF=""      # date; specs whose filename date >= this MUST carry `· streams <value>` (check 12); blank = never required
SPEC_WITNESS_CUTOFF="" # date; specs whose filename date >= this MUST give every acceptance bullet a backticked witness (check 12); blank = never required
FORK_MARK_CUTOFF=""   # date; at/after it a terminal spec's §8 SECTION must carry the SHAPED resolution mark somewhere (check 12) - not per ITEM, see TEMPLATE-SPEC; blank = never required
REVIEW_VERDICT_CUTOFF="" # date; review records whose filename date >= this MUST carry one `## Verdict: <member>` line from the closed set (check 22); blank = never required
# The FOURTH cutoff, and the only one that ships WITH a value. Its three siblings above are rules
# that can be absent, so blank turns each of them off; this one SELECTS between two section canons
# and check 12 must pick one for every spec it grades. An empty string compares earlier than every
# date, so a blank declaration would silently demand the ten-section canon of every grandfathered
# spec in the tree — which is the one thing the cutoff mechanism exists to prevent. Blank therefore
# resolves FORWARD to this value, below the conf source (TOOL-aDeclaredBound-2).
SPEC10_CUTOFF="2026-08-04"  # date; specs dated >= this take the TEN-section canon (check 12)
_SPEC10_SHIPPED="$SPEC10_CUTOFF"   # captured BEFORE the source, so the fallback below needs no second literal
# Check 6 caps an index file BY CLASS, and the split is between PROSE and ROWS (see check 6 for the
# reasoning, which is a recorded decision). These are the DEFAULTS; a project overrides any of them
# in .memory-tree.conf, because the value that suits one corpus is not the value that suits another
# and an adopter should not have to fork a kit script they re-pull on every release. A LINE cap of 0
# means no independent line cap for that class. Validated below: awk compares a bad -v binding
# silently, so an unvalidated typo here is a gate that reds everything or nothing with no message.
INDEX_CAP_BYTES=20480         ; INDEX_CAP_LINES=250
GUIDE_CAP_BYTES=61440         ; GUIDE_CAP_LINES=750
BUILD_README_CAP_BYTES=25600  ; BUILD_README_CAP_LINES=0
# A codebase-map dossier is its own class (TOOL-aRelaxedShard-1). It is kept TIGHTER than the index
# class on purpose: check 6 is the only size gate a dossier has, and its remedy is a SPLIT rather
# than a rotation, so inheriting a relaxed index cap would loosen the one class that cannot rotate.
# Only reached where a codebase map is adopted; the selector is guarded on a non-empty MAP_SUB.
DOSSIER_CAP_BYTES=20480       ; DOSSIER_CAP_LINES=0
# Check 7's ENTRY budget, per class, on the same footing (TOOL-aDeclaredBound-1). Characters, not
# bytes: `length()` decides this verdict and whether it counts characters or bytes is a property of
# the awk build and the ambient locale, which check 7 deliberately does not pin.
ENTRY_CAP_CHARS=300           ; BUILD_README_ENTRY_CAP_CHARS=350
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"   # see the declaration above: blank resolves forward, never off
# The caps are validated HERE, once, before anything reads them — ahead of the print modes below, so
# the sibling classifier that asks this script for the index set gets a non-zero exit it turns into
# its own named refusal rather than a set derived under a conf this script would not accept. This is
# an ABORT, not a check failure: a gate that cannot read its own thresholds has not found a hygiene
# regression, it has failed to run. Same channel and status as the no-python abort below.
_capbad=""
for _k in INDEX_CAP_BYTES INDEX_CAP_LINES GUIDE_CAP_BYTES GUIDE_CAP_LINES BUILD_README_CAP_BYTES BUILD_README_CAP_LINES DOSSIER_CAP_BYTES DOSSIER_CAP_LINES ENTRY_CAP_CHARS BUILD_README_ENTRY_CAP_CHARS; do
  eval "_v=\${$_k-}"
  case "$_v" in
    *[!0-9]*|"") _capbad="$_capbad $_k='$_v' (not a whole number)"; continue ;;
  esac
  # ARITHMETIC, not a literal match. `case ... in 0)` accepted "00" and "020", which awk's `+0` belt
  # then coerced to zero — the exact silent-green this guard exists to stop, one leading zero away.
  # A zero LINE cap means "no independent line cap" and is legal. A zero BYTE or CHAR cap is not:
  # it reds every file in its class, which reads as a misconfiguration and never as an intent.
  case "$_k" in
    *_BYTES) [ "$_v" -eq 0 ] && _capbad="$_capbad $_k='$_v' (a zero byte cap reds every file in its class)" ;;
    *_CHARS) [ "$_v" -eq 0 ] && _capbad="$_capbad $_k='$_v' (a zero entry budget reds every line in its class)" ;;
  esac
done
[ -n "$_capbad" ] && { echo "HYGIENE — cannot run: size cap(s) declared in .memory-tree.conf are unusable:$_capbad"; exit 2; }
# CONVERGED. This branch (TOOL-aRelaxedShard-1) built the same feature independently and arrived at
# two byte-only keys with blank resolving FORWARD to a shipped default. main's scheme is kept because
# it is strictly more general — both axes of every class — and because its validation caught a trap the
# other did not: `case $v in 0)` accepts "00" and "020", which awk's `+0` then coerces to zero, so the
# check is arithmetic. The other design's concern was that a BLANK key must never silently disable a
# bound; the abort above satisfies that more loudly than a fall-forward would.
M="$MEMORY_ROOT"
HERE="$(cd "$(dirname "$0")" && pwd)"
# codebase-map kit interop: when its MAP_ROOT is a DIRECT child of this tree (e.g. memory/map),
# carve that subtree into the structure lint + index caps below (prose files only; the map's
# coverage/freshness gates are its own test file, not this script).
MAP_SUB=""
if [ -f "$ROOT/.codebase-map.conf" ]; then
  _cbm_root=$(. "$ROOT/.codebase-map.conf" 2>/dev/null; printf '%s' "${MAP_ROOT:-}" | tr -d '\r')
  _cbm_root="${_cbm_root%/}"   # trailing slash would mis-read a direct child as nested
  case "$_cbm_root" in "$M"/*) _s="${_cbm_root#"$M"/}"; case "$_s" in */*) ;; *) MAP_SUB="$_s";; esac;; esac
fi
STAGED=0; [ "${1:-}" = "--staged" ] && STAGED=1

status=0
FILES=$(git ls-files "$M/")

# --- PRINT MODES: this script OWNS two sets that a sibling gate needs, and a transcription of
# --- either is the drift class the kit exists to remove. `corpus_ids.py` ASKS instead of copying.
# --- The dependency runs ONE WAY: these return before check 1, so nothing recurses back here.
# --- The append-only set is check 2's exemption; the index set is check 6's byte-capped population.
APPEND_ONLY_ERE="^$M/(DECISIONS\.md$|decisions/|archive/)"
case "${1:-}" in
  --print-append-only-ere) printf '%s\n' "$APPEND_ONLY_ERE"; exit 0 ;;
esac
LEGACY=$(grep -vE '^\s*(#|$)' "$M/project/legacy-files.txt" 2>/dev/null || true)
DEBT=$(grep -vE '^\s*(#|$)' "$M/project/curation-debt.txt" 2>/dev/null || true)
# Membership via associative arrays, NOT `grep -qxF <<<"$LIST"` — the here-string forks a grep per
# call, and these run once per scanned file (minutes on a large adopter tree; a fork is ~50-100ms
# under MSYS/Windows). Exact-key lookup is semantically identical (fixed string, whole line) and
# costs zero processes. (Upstream: inCMS ARCH-aFencedNamespace-3.)
declare -A LEGACY_SET DEBT_SET
while IFS= read -r _l; do [ -n "$_l" ] && LEGACY_SET["$_l"]=1; done <<<"$LEGACY"
while IFS= read -r _l; do [ -n "$_l" ] && DEBT_SET["$_l"]=1; done <<<"$DEBT"
in_legacy() { [ -n "${LEGACY_SET[$1]+x}" ]; }
in_debt()   { [ -n "${DEBT_SET[$1]+x}" ]; }
fail() { echo "HYGIENE check $1 FAILED — $2"; status=1; }

# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh
# and tools/lib/resolve-python.test.sh reds if any copy drifts.
# Resolved ONCE for all three delegating checks (9, 13-16, 17-19) — the retired idiom sat at
# three separate sites in this file, which is three chances to fix two of them.
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
_PY=$(resolve_python) || { echo "HYGIENE — no usable python; checks 9 and 13-19 delegate to sibling modules"; exit 2; }
FAMILY_of() { local p; for p in $FAMILIES; do case "$p" in "$1:"*) echo "${p#*:}"; return;; esac; done; }
FAM_ALT=$(for p in $FAMILIES; do echo "${p#*:}"; done | paste -sd'|' -)   # ARCH|DEPLOY|... for regexes
DISC_ALT=$(printf '%s\n' $DISCIPLINES | paste -sd'|' -)                   # the streams enum, for check 12
# THE recording-name tail, in ONE place. A multi-unit build names its sub-specs
# `<date>-spec-<slug>-<seq>-u6-indexed-join.md`, and both check 5's name grammar and check 12's
# selector have to admit that suffix. They were two hand-copied EREs for one grammar and they had
# already diverged — check 12 carried the tail, check 5 did not — so widening check 5's SELECTOR
# without this would have redded 14 conforming files. Interpolated by both; never retyped.
REC_TAIL='(-[a-z0-9][a-z0-9-]*)?'

# A selector that matches NOTHING prints nothing, and nothing is what a passing check prints. The
# 1.5 flatten changed the segment count of several path selectors at once, so each one asserts its
# population is non-empty — but ONLY when the tree demonstrably holds files of that kind. A freshly
# scaffolded repo with no builds yet is a legitimate empty, not a disarmed gate, and a guard that
# cannot tell those apart makes `adopt --scaffold` produce a red tree.
#
# So the guard compares TWO granularities: the PRECONDITION asks "does a file of this kind exist
# anywhere under the memory root?" and the POPULATION asks "does one exist at the exact path this
# check expects?". Equal-and-zero is a young tree. Precondition non-zero with an empty population is
# a mis-segmented selector — the only shape that silently disarms a check — and that is what reds.
# `--staged` is exempt throughout: an empty staged set is the normal case.
POP_MISSING=""
pop_guard() { # check-number · label · population-count · precondition-count
  [ "$STAGED" = 1 ] && return 0
  [ "${3:-0}" -gt 0 ] && return 0
  [ "${4:-0}" -gt 0 ] || return 0
  POP_MISSING="${POP_MISSING}    check $1: $2 (but $4 file(s) of that kind exist elsewhere under $M/ — the selector is mis-segmented)"$'\n'
}
# Preconditions, deliberately un-segmented: they ask what KIND of file exists, never where.
PRE_ANYBUILD=$(printf '%s\n' "$FILES" | grep -cE "/builds/" || true)
PRE_RECORD=$(printf '%s\n' "$FILES" | grep -cE "/builds/.+/.+\.md$" || true)
PRE_SPEC=$(printf '%s\n' "$FILES" | grep -cE "/[0-9]{4}-[0-9]{2}-[0-9]{2}-spec-[^/]*\.md$" || true)
PRE_STATUSY=$(printf '%s\n' "$FILES" | grep -cE "(/BACKLOG\.md$|^$M/backlog/)" || true)
# Check 21's precondition. Deliberately NOT anchored to `$M/builds/<slug>/`: a precondition that
# restates its check's own population can never differ from it, so pop_guard would be unreachable
# and the vacuity guard decoration. Un-anchored, a record left at a pre-flatten path counts here and
# not there — which is exactly the mis-segmentation the guard exists to name. Extension-agnostic,
# because one record in the corpus is a shell script.
PRE_BINDABLE=$(printf '%s\n' "$FILES" | grep -cE "/(build|prompts|reviews)/" || true)
# CR-stripped + marker-matched fences: only the marker that OPENED a fence closes it (a ~~~ line
# inside a ``` fence is content, not a toggle), and \r is dropped so CRLF worktrees (autocrlf
# smudge read by WSL/Linux bash) compare equal to LF sources.
_unfenced() { awk '
  { sub(/\r$/, "") }
  /^[[:space:]]*(```|~~~)/ {
    m = ($0 ~ /^[[:space:]]*```/) ? "```" : "~~~"
    if (f == "") { f = m; next }
    if (m == f) { f = ""; next }
  }
  f == ""' "$1"; }

declare -A STAGED_SET
if [ "$STAGED" = 1 ]; then
  STAGED_MD=$(git diff --cached --name-only --diff-filter=ACMR -- "$M/**" | LC_ALL=C sort)
  while IFS= read -r _l; do [ -n "$_l" ] && STAGED_SET["$_l"]=1; done <<<"$STAGED_MD"
fi
in_scope() { [ "$STAGED" = 0 ] && return 0; [ -n "${STAGED_SET[$1]+x}" ]; }   # zero-fork (see LEGACY_SET)

# 1 — prompt placement: prompt-kind files only under builds/*/prompts/ or archive/.
c1=$(printf '%s\n' "$FILES" \
  | grep -E '(\.prompt\.md|\.build-prompt\.md|-prompt\.md|/[0-9]{4}-[0-9]{2}-[0-9]{2}-prompt-[A-Za-z0-9-]+-[0-9]+\.md)$' \
  | grep -vE '/(builds/[^/]+/prompts/|archive/)' || true)
[ -n "$c1" ] && fail 1 "prompt-kind files outside builds/*/prompts/ or archive/:
$c1"

# 2 — link integrity (exempt DECISIONS.md / decisions/ / archive/ and legacy-listed recording files).
# LIVE.md and the ledger shards are NOT exempt: their rows link to build READMEs, and a link that
# stops resolving is precisely the drift the generated index exists to prevent.
scan2=$(printf '%s\n' "$FILES" | grep -E '\.md$' | grep -vE '/(DECISIONS\.md$|decisions/|archive/)')
[ "$STAGED" = 1 ] && scan2=$(printf '%s\n' "$scan2" | { grep -xF -f <(printf '%s\n' "$STAGED_MD") || true; })
# Drop grandfathered files first (fork-free), then extract every candidate link in ONE awk pass over
# all remaining files — was `_unfenced | grep -oE | sed -E` PER FILE (3 forks × N files; the single
# biggest cost on a large adopter tree — upstream inCMS ARCH-aFencedNamespace-3). The awk inlines
# _unfenced's exact semantics (CR strip + marker-matched fences, state reset per file) and the
# grep+sed link shape INCLUDING the sed fall-through (an anchor-only `](#x.md)` stays as-is).
scan2f=""
while IFS= read -r f; do
  [ -n "$f" ] || continue
  in_legacy "$f" && continue
  scan2f+="$f"$'\n'
done <<<"$scan2"
broken=$(awk '
  { f = $0; if (f == "") next
    fence = ""
    while ((getline line < f) > 0) {
      sub(/\r$/, "", line)
      if (line ~ /^[[:space:]]*(```|~~~)/) {
        m = (line ~ /^[[:space:]]*```/) ? "```" : "~~~"
        if (fence == "") { fence = m; continue }
        if (m == fence) { fence = ""; continue }
      }
      if (fence != "") continue
      while (match(line, /\]\([^)]+\.md[^)]*\)/)) {
        mm   = substr(line, RSTART, RLENGTH)
        rest = substr(line, RSTART + RLENGTH)
        t = mm
        if (match(t, /^\]\([^)#]+/)) t = substr(t, 3, RLENGTH - 2)
        print f "\t" t
        line = rest
      }
    }
    close(f)
  }' <<<"$scan2f" | while IFS=$'\t' read -r f t; do
    case "$t" in http*|/*) continue;; esac
    d=${f%/*}                   # fork-free dirname — every path here starts "$M/", so it has a /
    [ -f "$d/$t" ] || echo "$f -> $t (MISSING)"
  done)
[ -n "$broken" ] && fail 2 "broken relative .md links:
$broken"

# 3 — structure lint (depth-2; decisions/ guides/ archive/ contents opaque).
# FLAT (1.5): the root holds the four index files, one append-only DECISIONS.md, and the fixed
# directory set. There is no discipline directory to descend into; `builds/` holds one folder per
# slug and `backlog/` holds one shard per FAMILY.
root1=$(printf '%s\n' "$FILES" | awk -F/ '{ if (NF==2) print "F:"$2; else print "D:"$2 }' | LC_ALL=C sort -u)
bad3=$(printf '%s\n' "$root1" | grep . | while IFS= read -r e; do case "$e" in
  F:README.md|F:HYGIENE.md|F:TEMPLATE-SPEC.md|F:DECISIONS.md|F:LIVE.md) ;;
  D:project|D:builds|D:backlog|D:decisions|D:guides|D:archive|D:ledger|D:gotchas) ;;
  D:*) d="${e#D:}"; [ "$d" = "$MAP_SUB" ] || echo "$M/$d";;
  *) echo "$M/${e#*:}";; esac; done)
# backlog/ holds ONLY <FAMILY>.md, one shard per declared family — a stray name there is a backlog
# nobody's status-vocabulary check will ever read.
b3b=$(printf '%s\n' "$FILES" | grep -E "^$M/backlog/" | awk -F/ -v m="$M" -v fam="$FAM_ALT" '
  { if (NF != 3) { print m "/backlog/" $3 " (nested)"; next }
    if ($3 !~ "^(" fam ")\\.md$") print m "/backlog/" $3 }' | LC_ALL=C sort -u)
# builds/ holds ONLY directories.
b3c=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/" | awk -F/ -v m="$M" '
  NF == 3 { print m "/builds/" $3 " (file at the builds root — a build is a FOLDER)" }' | LC_ALL=C sort -u)
bad3=$(printf '%s\n%s\n%s\n' "$bad3" "$b3b" "$b3c")
# project/ holds the gate's OWN waiver registries and nothing else (aMendedLedger U3). The session
# machinery it used to also hold — MEMORY.md, IN-FLIGHT.md, in-flight/, journal/, project/README.md —
# is retired, and the `F:*.md` catch-all goes with it: a directory defined as six named files cannot
# also admit any `.md` anyone drops in. Nothing scaffolds those names any more either, so an
# admitted-but-never-written entry would be a third answer to a question this list is closing.
p1=$(printf '%s\n' "$FILES" | grep "^$M/project/" | awk -F/ '{ if (NF==3) print "F:"$3; else print "D:"$3 }' | LC_ALL=C sort -u)
# The precondition is deliberately UN-SEGMENTED (see pop_guard): `project/` is drained of session
# machinery, not emptied — the registries stay — so the population is non-zero on a real tree and 0
# only when the path expression is mis-segmented, which is the one shape that silently disarms this
# sub-lint. A tree with no `.txt` anywhere is a young tree and stays silent.
PRE_REGISTRY=$(printf '%s\n' "$FILES" | grep -cE '\.txt$')
pop_guard 3 "no registry under $M/project/" \
  "$(printf '%s\n' "$FILES" | grep -cE "^$M/project/[^/]+\.txt$")" "$PRE_REGISTRY"
bp=$(printf '%s\n' "$p1" | grep . | while IFS= read -r e; do case "$e" in
  F:legacy-files.txt|F:curation-debt.txt) ;;
  F:id-orphan-waiver.txt|F:corpus-path-unresolved.txt|F:unarmed-branches.txt) ;;
  F:method-carriers.txt|F:testsuite-count-waivers.txt) ;;
  F:trace-waiver.txt) ;;
  # TOOL-dFramedEntrypoint-3 - the build-README contract registry. Same shape as
  # method-carriers.txt above: a declared population asserted in both directions by a script
  # other than this one.
  F:readme-contract.txt) ;;
  *) echo "$M/project/${e#*:}";; esac; done)
bm=""
if [ -n "$MAP_SUB" ]; then
  m1=$(printf '%s\n' "$FILES" | grep "^$M/$MAP_SUB/" | awk -F/ '{ if (NF==3) print "F:"$3; else print "D:"$3 }' | LC_ALL=C sort -u)
  bm=$(printf '%s\n' "$m1" | grep . | while IFS= read -r e; do case "$e" in
    F:README.md|F:FOUNDATION.md|F:baseline.toml|F:affordance-exempt.toml|D:features|D:generated) ;;
    *) echo "$M/$MAP_SUB/${e#*:}";; esac; done)
fi
bad3=$(printf '%s\n%s\n%s\n' "$bad3" "$bp" "$bm" | grep . || true)
[ -n "$bad3" ] && fail 3 "unexpected entries (structure):
$bad3"

# 4 — build-folder naming + internal shape.
# FLAT (1.5): ONE population, `<M>/builds/<slug>/`. The date prefix and the FAMILY prefix are gone
# with the discipline directory — a folder is named for its slug and nothing else, so there is no
# FAMILY↔discipline pairing left to assert here. A recording filename MAY carry a FAMILY qualifier
# (`<date>-<kind>-<FAMILY>-<slug>-<seq>.md`), which is how one slug shared by two families survives
# the merge into a single folder; the alternation is the CLOSED one from FAMILIES, never `[A-Z]+`.
#
# A RETIRED run-state file (2.18) joins it as a GRAMMAR rather than a literal — `RUN.<PHASE>.<8 hex>.md`,
# where the hex is the retired record's own blob hash. A build gets more than one unattended run by
# ROTATING the finished record to that name, so the family is unbounded and cannot be whitelisted by
# equality the way the three below are. It joins check 6's caps and check 7's prose exemption too: an
# archived record is the same document frozen.
#
# RUN.md (2.3) is the THIRD whitelisted root file: the run-state file an unattended run writes, which
# needs a name a resuming session can compute without knowing when the run started. A dated recording
# under build/ is legal today and has no stable resume target, which is why the name is fixed here
# rather than left to the recording grammar. It joins index_set() (check 6's caps) and check 7's
# prose exemption; it deliberately does NOT join check 8, whose seven-token status vocabulary cannot
# express the run phases — the unattended leg owns validating those.
BUILD_N=$(printf '%s\n' "$FILES" | awk -F/ -v m="$M" '$0 ~ "^" m "/builds/" && NF > 3 { print $3 }' | LC_ALL=C sort -u | grep -c .)
pop_guard 4 "no build folder under $M/builds/" "$BUILD_N" "$PRE_ANYBUILD"
bad4=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/" \
  | LC_ALL=C awk -F/ -v m="$M" -v famalt="$FAM_ALT" '
      BEGIN {
        n_m = split(m, _seg, "/"); fidx = n_m + 2    # <m>/builds/<folder>
        vre = "^[A-Za-z][A-Za-z0-9-]*$"              # the slug, alone
        rre = "^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-(prompt|spec|build|review)-((" famalt ")-)?[A-Za-z0-9]+-[0-9]+\\.md$"
        # An ARCHIVED run-state file (2.18). A GRAMMAR, because the whitelist above it is string
        # equality and a family of names cannot be spelled that way. SHAPE, not vocabulary: a phase
        # token and a content hash. `RUN\\..*\\.md` would admit `RUN.notes.md` and `RUN.md.bak` at
        # every build root forever with no waiver registry and no ratchet;
        # `RUN\\.(LANDED|ABORTED)\\.` would hard-code the unattended kit`s PHASES_TERMINAL into this
        # engine. The unattended leg owns the vocabulary — it reds on an archived record whose phase
        # is not terminal — and this gate owns the folder grammar.
        arre = "^RUN\\.[A-Z]+\\.[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]\\.md$"
      }
      function flush(   n,i,j,k,keys,tmp,type,name) {
        if (folder=="") return
        if (folder !~ vre) {
          print m "/builds/" folder " (bad folder name — expected the slug alone, no date and no FAMILY prefix)"
          folder=""; delete ent; return }
        n=0; for (k in ent) keys[++n]=k
        for (i=2;i<=n;i++){ tmp=keys[i]; j=i-1; while(j>=1 && keys[j]>tmp){keys[j+1]=keys[j];j--} keys[j+1]=tmp }
        for (i=1;i<=n;i++){ k=keys[i]; type=substr(k,1,1); name=substr(k,3)
          if (k=="F:README.md"||k=="F:RUN.md"||k=="D:prompts"||k=="D:spec"||k=="D:build"||k=="D:reviews") continue
          if (type=="F" && name ~ arre) continue
          if (type=="F"){ if (name !~ rre) print m "/builds/" folder "/" name }
          else print m "/builds/" folder "/" name }
        folder=""; delete ent
      }
      { if ($fidx!=folder){ flush(); folder=$fidx }
        if (NF==fidx+1) ent["F:" $(fidx+1)]=1; else ent["D:" $(fidx+1)]=1 }
      END { flush() }')
bad4=$(printf '%s\n' "$bad4" | grep . || true)
[ -n "$bad4" ] && fail 4 "build-folder naming/shape:
$bad4"


# 5 — recording-file naming (grandfather: legacy-files.txt).
# The optional `-<FAMILY>-` qualifier is the CLOSED alternation from FAMILIES. A generic `[A-Z]+`
# would admit a family that does not exist and make the rejection arm vacuous.
# ANY DEPTH under the four subfolders. A file one level deeper used to be governed by nothing: check
# 5 saw only direct children, and check 12's population is files that already match the dated name,
# so a free-named nested file was outside both by construction.
c5_sel=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/(prompts|spec|build|reviews)/(.+/)?[^/]+\.md$" || true)
pop_guard 5 "no recording file under $M/builds/*/{prompts,spec,build,reviews}/" \
  "$(printf '%s\n' "$c5_sel" | grep -c . || true)" "$PRE_RECORD"
bad5=$(printf '%s\n' "$c5_sel" | grep . | while IFS= read -r f; do
  in_legacy "$f" && continue
  # Fork-free basename + SUBFOLDER extraction (was basename + awk + grep = 3 forks per recording file).
  # The kind comes from the subfolder — the first segment after the build slug — NOT from the file's
  # immediate parent: `spec/units/x.md` is a spec, and `units` is not a kind.
  base=${f##*/}; rest=${f#"$M"/builds/}; rest=${rest#*/}; sub=${rest%%/*}
  case "$sub" in prompts) kind=prompt;; spec) kind=spec;; build) kind=build;; reviews) kind=review;; esac
  [[ $base =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-$kind-(($FAM_ALT)-)?[A-Za-z0-9]+-[0-9]+$REC_TAIL\.md$ ]] || echo "$f"
done)
# The DEPTH is not the problem, and the message says so on a CONTINUATION line — the first line is
# this branch's check-arms signature and its arm sits exactly at the armed floor with no slack.
[ -n "$bad5" ] && fail 5 "recording-file names not matching YYYY-MM-DD-<kind>[-<FAMILY>]-<slug>-<seq>.md (and not grandfathered):
  (nesting is fine — a sub-folder under spec/ groups a multi-unit build; the NAME is what is wrong)
$bad5"

# index set for checks 6/7
index_set() {
  { echo "$M/README.md"; echo "$M/LIVE.md"; echo "$M/DECISIONS.md"
    printf '%s
' "$FILES" | grep -E "^$M/ledger/[^/]+\.md$"
    if [ -n "$MAP_SUB" ]; then
      echo "$M/$MAP_SUB/README.md"; echo "$M/$MAP_SUB/FOUNDATION.md"
      printf '%s\n' "$FILES" | grep -E "^$M/$MAP_SUB/features/[^/]+\.md$"   # dossiers: size caps, entry-budget exempt
    fi
    printf '%s\n' "$FILES" | grep -E "^$M/backlog/[^/]+\.md$"
    printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/STATUS\.md$"
    # A BUILD README is ROWS, not prose — TOOL-aWidenedGuide-1 split the cap by CLASS on exactly that
    # distinction, and after the generated surface landed this file is four rendered regions plus one
    # bounded authored block. It carries its OWN tier below (BUILD_README_CAP_*, plus check 7's
    # chars) rather than the row-document tier, which was measured against a corpus in which these
    # files were not members at all. The numbers live at the top of this file, declared once.
    printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/README\.md$"
    # RUN.md (2.3): the run-state file is capped like every other index. It is designed to GROW —
    # a parked entry per refused decision — so the cap is the point, not an accident: the protocol
    # spills the oldest parked entries into the build's own build/ folder as a dated recording
    # (a name check 5's grammar already admits) before the cap is reached. Entry-budget exempt
    # below, because the standing mandate is verbatim prose, not index rows.
    # An ARCHIVED record (2.18) is the same document frozen, so the same cap applies to it.
    printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/RUN(\.[A-Z]+\.[0-9a-f]{8})?\.md$"
    # A GUIDE is mandatory reading — the charter points a session at it — so it carries the same
    # byte/line cap as an index. Check 16 says the same thing from the other side: a charter-cited
    # file under no cap is a read budget nobody watches. Entry-budget exempt: a guide is prose.
    printf '%s\n' "$FILES" | grep -E "^$M/guides/[^/]+\.md$"
  } | while IFS= read -r f; do [ -f "$f" ] && echo "$f"; done
}
INDEX_SET=$(index_set)   # compute ONCE; checks 6 and 7 both read it (was recomputed per check)
case "${1:-}" in --print-index-set) printf '%s\n' "$INDEX_SET"; exit 0 ;; esac   # see the PRINT MODES note above

# 6 — index size caps (grandfather: curation-debt.txt).
# Batched wc: one `wc -c` + one `wc -l` over the whole selected set (was 2 forks PER index file).
# Findings emit in index_set order (the -l stream's arg order); multi-file wc `total` lines are
# skipped by name; `+0` coerces the counts.
sel6=$(printf '%s\n' "$INDEX_SET" | while IFS= read -r f; do in_debt "$f" && continue; in_scope "$f" || continue; printf '%s\n' "$f"; done)
bad6=""
if [ -n "$sel6" ]; then
  cbytes=$(printf '%s\n' "$sel6" | xargs -r wc -c)
  clines=$(printf '%s\n' "$sel6" | xargs -r wc -l)
  # PER-CLASS CAPS. FOUR classes, and the numbers are DECLARED at the top of this file and overridable
  # per project — the value that suits one corpus is not the value that suits another.
  #
  # A guide is prose the charter points a session at and reads end to end; for it a line limit is a
  # PROXY for the read budget rather than the budget itself — check 16's `READ_PATH_CEILING` is the real
  # one, measured in bytes, and it is not relaxed here. Every other class is a row set, and for a row set
  # the line count was never the bound that bound: at check 7's declared entry budget a 250-line row
  # document may hold 75,000 B, so the byte figure decided every real case and the line figure needed
  # rows averaging under 82 B. Measured over this corpus's backlog rows: 253.7 B.
  #
  # A LINE CAP OF 0 MEANS NO INDEPENDENT LINE CAP for the class. That is how a project retires the line
  # axis for its row documents, and this repo has: `TOOL-aRelaxedShard-1` sets `INDEX_CAP_LINES=0` in
  # `.memory-tree.conf` after the owner ratified it, reversing the refusal `TOOL-aWidenedGuide-1`
  # recorded. It was a DECISION and not a tidy-up: measured over the 29-member index class, 22 sat below
  # the 81.92 B/line break-even and were line-bound FIRST, every codebase-map dossier among them. Which
  # is why a dossier is its own class here rather than inheriting a relaxed index cap — check 6 is the
  # only size gate it has, and its remedy is a SPLIT rather than a rotation.
  #
  # The shipped ratio between the classes is stated as an allowance, not an arithmetic identity: a
  # project that moves one key and not another changes it.
  bad6=$(awk -v gp="$M/guides/" -v bp="$M/builds/"           -v icb="$INDEX_CAP_BYTES" -v icl="$INDEX_CAP_LINES"           -v gcb="$GUIDE_CAP_BYTES" -v gcl="$GUIDE_CAP_LINES"           -v rcb="$BUILD_README_CAP_BYTES" -v rcl="$BUILD_README_CAP_LINES"           -v dcb="$DOSSIER_CAP_BYTES" -v dcl="$DOSSIER_CAP_LINES"           -v dp="${MAP_SUB:+$M/$MAP_SUB/features/}" '
    FNR==NR { if ($NF!="total") b[$NF]=$1; next }
    $NF=="total" { next }
    { l[$NF]=$1; ord[++n]=$NF }
    END { for(i=1;i<=n;i++){ f=ord[i]
            # +0 on every binding: awk compares an unset or non-numeric -v as a STRING, which reds
            # nothing at all. The validation at conf load is what makes these numbers; this is belt.
            cb = icb+0; cl = icl+0
            if (index(f, gp) == 1) { cb = gcb+0; cl = gcl+0 }
            # A build README: its own tier, and a 0 line cap means NO independent line cap. The line
            # count is whatever fits the byte budget at the per-line width, so there is no third
            # number to drift against the other two.
            if (index(f, bp) == 1 && f ~ /\/README\.md$/) { cb = rcb+0; cl = rcl+0 }
            # A codebase-map dossier, GUARDED on a non-empty prefix. `dp` is empty when no map is
            # adopted, and `index(f, "")` is 1 for EVERY string — an unguarded test would hand the
            # dossier bound to the whole tree and silently undo the index cap. The `ex7` selector in
            # check 7 adds its map alternatives under `[ -n "$MAP_SUB" ]` for the same reason.
            if (dp != "" && index(f, dp) == 1) { cb = dcb+0; cl = dcl+0 }
            if (b[f]+0>cb || (cl>0 && l[f]+0>cl)) {
              if (cl>0) printf "%s (%dB %dL > %dB/%dL)\n", f, b[f]+0, l[f]+0, cb, cl
              else      printf "%s (%dB > %dB; no line cap for this class)\n", f, b[f]+0, cb } } }
  ' <(printf '%s\n' "$cbytes") <(printf '%s\n' "$clines"))
fi
[ -n "$bad6" ] && fail 6 "index files over cap (rotate to archive/<INDEX>.<YYYY-MM-DD>.md; a codebase-map dossier over cap is SPLIT into two dossiers instead — never rotate FOUNDATION.md, the map gate requires it):
$bad6"

# 7 — entry budget, ENTRY_CAP_CHARS per class (grandfather: curation-debt.txt; exempt guides/*.md — a guide is prose,
#     not index rows — builds/*/RUN.md, whose standing-mandate block is quoted prose reproduced
#     verbatim and must not be reflowed to fit an index budget — and, when the codebase-map kit is
#     adopted under this tree, its dossiers/FOUNDATION (detail files).
# ONE base plus an APPEND, never a second full spelling (aMendedLedger U3). The MAP_SUB branch used to
# rebuild the whole expression, which silently dropped the guides/ alternative on any repo carrying a
# .codebase-map.conf — every guide entered this check's population and nothing said so. Two spellings
# of one expression is the two-answers-to-one-question class, and this is how it fired.
ex7='/guides/[^/]+\.md$|/builds/[^/]+/RUN(\.[A-Z]+\.[0-9a-f]{8})?\.md$'
[ -n "$MAP_SUB" ] && ex7="$ex7|/$MAP_SUB/FOUNDATION\.md\$|/$MAP_SUB/features/[^/]+\.md\$"
# ONE awk over the whole selected set (was `_unfenced | awk` = 2 forks per file; measured 7.86s here,
# TOOL-aBatchedLintel-1). `uln` counts the UNFENCED stream, which is what the old `FNR` counted — the
# piped `_unfenced` output WAS the record source, so the reported line number was never the file line
# number and must not become one.
#
# NO `LC_ALL=` prefix and no `xargs` wrapper that sets one, deliberately. `length()` decides this
# verdict and its character-versus-byte meaning is a property of the awk build and the ambient
# locale; pinning it would silently re-decide the cap on any adopter whose awk counts characters
# today. Check 8 at the batched `LC_ALL=C xargs -r awk` seventeen lines below is NOT the pattern to
# copy here — it sorts, it does not measure.
sel7=$(printf '%s\n' "$INDEX_SET" | grep -vE "$ex7" | while IFS= read -r f; do
  in_debt "$f" && continue; in_scope "$f" || continue; printf '%s\n' "$f"
done)
bad7=""
if [ -n "$sel7" ]; then
  bad7=$(awk -v bp="$M/builds/" -v ecc="$ENTRY_CAP_CHARS" -v becc="$BUILD_README_ENTRY_CAP_CHARS" '
    { f = $0; if (f == "") next
      # PER-CLASS WIDTH, both declared. A build README is four rendered regions plus one authored
      # block, and its widest authored lines were MEASURED between 300 and 331 — that measurement is
      # why the class has its own tier, and it stays true whatever an adopter declares.
      # +0 on both: awk compares an unset or non-numeric -v as a STRING, which reds nothing at all.
      cap = ecc+0
      if (index(f, bp) == 1 && f ~ /\/README\.md$/) cap = becc+0
      fence = ""; uln = 0; fm = 0; nl = 0
      while ((getline line < f) > 0) {
        sub(/\r$/, "", line)
        nl++
        # THE FRONT-MATTER BLOCK IS NOT MEASURED. It is machine-written, not read prose: `--write`
        # rewrites `ids:` from the derived roster, and that one line is 479 characters in the largest
        # build. It cannot be wrapped — parse_front_matter refuses an indented continuation and
        # check-unattended.sh check 13 parses the same block — so measuring it would cap a value no
        # author controls and no renderer may reflow. This is scoping WITHIN a file, which is what
        # the fence handling below already does. Measured: no index-set member opens with front
        # matter today, so this changes no current verdict.
        if (nl == 1 && line == "---") { fm = 1; continue }
        if (fm) { if (line == "---") fm = 0; continue }
        if (line ~ /^[[:space:]]*(```|~~~)/) {
          mk = (line ~ /^[[:space:]]*```/) ? "```" : "~~~"
          if (fence == "") { fence = mk; continue }
          if (mk == fence) { fence = ""; continue }
        }
        if (fence != "") continue
        uln++
        if (length(line) > cap && line !~ /^#/ && line !~ /^[[:space:]]*\|[-: |]+\|[[:space:]]*$/)
          print f ":" uln " (" length(line) " chars > " cap ")"
      }
      close(f)
    }' <<<"$sel7")
fi
[ -n "$bad7" ] && fail 7 "index entry lines over their declared cap:
$bad7"

# 8 — status vocabulary on the backlog shards (grandfather: curation-debt.txt).
#     STATUS.md was RETIRED by TOOL-aRuledFrontispiece-7: one existed across the whole corpus, it
#     contradicted its own build README, nothing ever wrote one, and no decision record created
#     the slot. The population is the shards alone, which is non-empty, so the guard below still
#     measures something rather than passing by finding nothing.
# One awk over the whole filtered file set (was _unfenced + grep -n PER file and a 3-fork
# printf|grep -oE|wc -l PER row). nmatch() reproduces `grep -oE '…\b' | wc -l` EXACTLY: the
# `^[[:space:]]*-` slot can only anchor once (caret pattern on the first match, no-caret thereafter),
# and the trailing `\b` is checked ZERO-WIDTH (next char is end/non-word) so it never consumes a
# following delimiter. uln counts the UNFENCED stream (== the old grep -n numbering). The two `·` in
# the patterns are the LITERAL middot byte. Validated per-row against grep over the upstream inCMS
# tree's 589 real rows — 0 mismatches (PERF-eThriftyBellows-1).
pop8=$( { printf '%s\n' "$FILES" | grep -E "^$M/backlog/[^/]+\.md$"; printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/STATUS\.md$"; } | grep -c . || true)
pop_guard 8 "no backlog shard under $M/backlog/" "$pop8" "$PRE_STATUSY"
files8=$( { printf '%s\n' "$FILES" | grep -E "^$M/backlog/[^/]+\.md$"; printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/STATUS\.md$"; } | while IFS= read -r f; do
  [ -f "$f" ] || continue; in_debt "$f" && continue; in_scope "$f" || continue; printf '%s\n' "$f"; done)
bad8=""
if [ -n "$files8" ]; then
  bad8=$(printf '%s\n' "$files8" | LC_ALL=C xargs -r awk '
    function nmatch(s,   c,first,nc,ok) { c=0; first=1
      while (length(s)>0) {
        if (first) ok=match(s,/([·|]|^[[:space:]]*-)[[:space:]]*(OPEN|SPECCED|INPROGRESS|BLOCKED|DEFERRED|CLOSED|WONTDO)/)
        else       ok=match(s,/[·|][[:space:]]*(OPEN|SPECCED|INPROGRESS|BLOCKED|DEFERRED|CLOSED|WONTDO)/)
        if (!ok) break
        nc=substr(s,RSTART+RLENGTH,1)
        if (nc=="" || nc !~ /[A-Za-z0-9_]/) { c++; s=substr(s,RSTART+RLENGTH); first=0 }
        else { s=substr(s,RSTART+1); first=0 }
      } return c }
    FNR==1 { uln=0; fence="" }
    { line=$0; sub(/\r$/,"",line)
      if (line ~ /^[[:space:]]*(```|~~~)/) { m=(line ~ /^[[:space:]]*```/)?"```":"~~~"
        if (fence=="") { fence=m; next }
        if (m==fence) { fence=""; next } }
      if (fence!="") next
      uln++
      if (line ~ /^[[:space:]]*[|-].*[A-Z]+-[A-Za-z0-9]*-?[0-9]/ && nmatch(line)!=1) print FILENAME ":" uln
    }')
fi
[ -n "$bad8" ] && fail 8 "backlog rows without exactly one status token (OPEN SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO):
$bad8"

# 9 — build-index drift (delegates to the sibling generator). The retired directory listing carried
# PATHS, which git already prints better; this carries STATUS, which git does not — and the status is
# DERIVED from each build's front matter plus its specs' status headers, so nothing is authored here
# and nothing rots.
if [ "$STAGED" = 0 ] || printf '%s\n' "$STAGED_MD" | grep -q .; then
  if ! drift=$("$_PY" "$HERE/gen_build_index.py" --check 2>&1); then fail 9 "generated build index differs from a fresh render:
$drift"; fi
fi

# 22 — THE REVIEW VERDICT VOCABULARY. A review record has to say what it concluded, in a token
# something can read, and until this check existed it did not have to say anything at all.
#
# MEASURED over the tracked corpus when this landed: 111 review records, 66 carrying a `## Verdict:`
# line and 45 carrying none, across 17 DISTINCT values — of which only `BLOCKED` and
# `CLEAN WITH FIXES` are in the closed set, and `CLEAN`, the one token the build method names as the
# review loop's only exit, occurs ZERO times. The rest are free prose: "FIX THE BLOCKER BEFORE
# LANDING", "SHIP WITH FIXES", "CHANGES REQUESTED". So the vocabulary the method states in prose was
# written consistently by nobody and read by nothing.
#
# WHY THIS IS ITS OWN CHECK NUMBER. Check 5 is a recording-FILENAME grammar and check 21 asks which
# spec a record is evidence ABOUT; hanging a verdict assertion off either would make a structural
# check read as a semantic one to everybody who did not write it. A new CHECK is the cheap option
# here — the leg's name carries no count and `tools/gate-legs.json` does not move — so the honest
# home costs an arms floor and an entry in the hygiene doc.
#
# FORWARD-ONLY, by a dated cutoff set strictly ahead of every committed record. 45 records carry no
# verdict at all and rewriting a landed review is against this tree's own rule, so the cutoff carries
# the corpus rather than a retrofit. Same instrument, and the same reason, as check 12's fork mark.
if [ -n "$REVIEW_VERDICT_CUTOFF" ]; then
  c22_sel=$(printf '%s
' "$FILES" | grep -E "^$M/builds/[^/]+/reviews/" || true)
  pop_guard 22 "no review record under $M/builds/*/reviews/" \
    "$(printf '%s
' "$c22_sel" | grep -c . || true)" "$PRE_BINDABLE"
  bad22=$(printf '%s
' "$c22_sel" | awk -v cut="$REVIEW_VERDICT_CUTOFF" '
    $0 == "" { next }
    {
      f = $0
      fbase = f; sub(/^.*\//, "", fbase)
      fdate = ""
      if (match(fbase, /[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/)) fdate = substr(fbase, RSTART, RLENGTH)
      if (fdate == "" || fdate < cut) next
      nv = 0; bad = ""
      while ((getline line < f) > 0) {
        sub(/\r$/, "", line)
        if (line ~ /^## Verdict:/) {
          nv++
          v = line; sub(/^## Verdict:[[:space:]]*/, "", v)
          gsub(/[[:space:]]+$/, "", v)
          # The CLOSED set, and nothing outside it. A trailing tally is not a member: the whole point
          # is a token a machine can compare, and "BLOCKED - 2 blockers, 2 highs" is prose wearing a
          # token as a prefix. Counts belong in the body, where 17 spellings do no harm.
          if (v != "CLEAN" && v != "CLEAN WITH FIXES" && v != "BLOCKED") bad = v
        }
      }
      close(f)
      if (nv == 0) print "  " f " (no `## Verdict:` line, so the record states no conclusion anything can read)"
      else if (nv > 1) print "  " f " (" nv " `## Verdict:` lines, so which one is the record\047s conclusion is a guess)"
      else if (bad != "") print "  " f " (verdict outside the closed set CLEAN / CLEAN WITH FIXES / BLOCKED: " bad ")"
    }')
  [ -n "$bad22" ] && fail 22 "review records at/after REVIEW_VERDICT_CUTOFF whose verdict line is missing, duplicated, or outside the closed set:
$bad22"
fi

# 21 — every record names the spec it is evidence about. Delegates the
# PARSE to the sibling generator, which already reads every record's bytes; the shell owns the four
# fail branches, because `check-arms.py` discovers its population from tracked shell and cannot see a
# Python raise. ONE invocation of the read-only mode, split here into four branch populations.
c21_sel=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/(build|prompts|reviews)/" || true)
pop_guard 21 "no record under $M/builds/*/{build,prompts,reviews}/" \
  "$(printf '%s\n' "$c21_sel" | grep -c . || true)" "$PRE_BINDABLE"
if [ "$STAGED" = 0 ] && printf '%s\n' "$c21_sel" | grep -q .; then
  b21=$("$_PY" "$HERE/gen_build_index.py" --print-bindings 2>/dev/null || true)
  miss21=$(printf '%s\n' "$b21" | sed -n 's/^A\t\([^\t]*\)\t\(.*\)$/  \1 — \2/p')
  [ -n "$miss21" ] && fail 21 "records under build/, prompts/ or reviews/ whose head carries no conformant Serves line:
$miss21"
  bad21=$(printf '%s\n' "$b21" | sed -n 's/^B\t\([^\t]*\)\t\(.*\)$/  \1 — \2/p')
  [ -n "$bad21" ] && fail 21 "Serves or Commissions lines naming an id that no spec in this tree defines:
$bad21"
  # The unbound escape. An UNDECLARED pin is a refusal, not a disabled check: `none` is a deliberate
  # declaration and the number of them is the thing a reader is entitled to see bounded.
  n21=$(printf '%s\n' "$b21" | sed -n 's/^N\t\([0-9]*\)$/\1/p' | head -1)
  pin21=${RECORD_UNBOUND_PIN-}
  if [ -z "$pin21" ]; then
    fail 21 "RECORD_UNBOUND_PIN is undeclared, so the count of records that serve no spec is unbounded — declare it in .memory-tree.conf, measured against this corpus"
  elif [ "${n21:-0}" -gt "$pin21" ]; then
    over21="  measured ${n21:-0} against the pin $pin21"
    fail 21 "records carrying the unbound Serves form outnumber their pin — bind them, or move the pin in the same commit recording the old and new values beside it:
$over21"
  fi
  # Branch 4 — the filename PROJECTS the header. Its input is the S row, because a conformant record
  # is not a finding and nothing else in the mode's output describes one. The projection is a WHOLE
  # id: family, slug and ordinal. A bound record whose name carries no family qualifier fails here,
  # since two thirds of an id is not a projection of it.
  proj21=$(printf '%s\n' "$b21" | sed -n 's/^S\t\([^\t]*\)\t[^\t]*\t\(.*\)$/\1|\2/p' | while IFS='|' read -r p ids; do
      base=${p##*/}; base=${base%.*}
      case "$base" in
        [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*) stem=${base#????-??-??-} ;;
        *) echo "  $p — the name carries no date, so no id can be read from it"; continue ;;
      esac
      rest=${stem#*-}
      claimed=$(printf '%s\n' "$rest" | grep -oE "^($FAM_ALT)-[A-Za-z0-9]+-[0-9]+" || true)
      if [ -z "$claimed" ]; then
        echo "  $p — bound, but the name carries no family-qualified id"
      else
        printf '%s\n' "$ids" | tr ' ' '\n' | grep -qxF "$claimed" || echo "  $p — the name claims $claimed"
      fi
    done)
  [ -n "$proj21" ] && fail 21 "record filenames whose family, slug and ordinal name an id their own Serves line does not list:
$proj21"
fi

# 10 — rotation note (always; cheap). FLAT (1.5): one archive at the memory root.
bad10=$(printf '%s\n' "$FILES" | grep -E "^$M/archive/[^/]+\.[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$" | while IFS= read -r a; do
    base=${a##*/}; idx="$M/${base%%.*}.md"
    [ -f "$idx" ] || continue
    head -3 "$idx" | grep -qF "$base" || echo "$a (not referenced in lines 1-3 of $idx)"
  done)
[ -n "$bad10" ] && fail 10 "rotated archives not referenced from their live index (lines 1-3):
$bad10"

# 11 — old-tree tombstone (only if TOMBSTONE_ROOTS is configured; never grandfathered).
for old in $TOMBSTONE_ROOTS; do
  if git ls-files "$old/" | grep -q .; then
    fail 11 "migrated-from tree '$old/' resurrected — $M/ is the only sanctioned memory root:
$(git ls-files "$old/" | head)"
  fi
done

# 12 — spec format ($M/TEMPLATE-SPEC.md; runs only when SPEC_FORMAT_CUTOFF is set in the conf).
# Status header (first 5 unfenced lines) for every spec incl. nested spec/<sub>/ files. Tier-2 adds:
# the canonical nine ## sections (exact, in order) · no empty section bodies (write "N/A — <why>") ·
# header rev logged in §9 · terminal Status (CLOSED/WONTDO) needs a resolved §8. Both tiers: no
# skeleton placeholders; WONTDO needs a successor/reason in the header tail. Tier-1 skips the
# section canon ("ceremony is conditional"). Pre-cutoff specs are grandfathered by FILENAME date;
# legacy-named files never match the glob. NOTE (shared idiom with checks 6/7/8): reads WORKTREE
# content in --staged mode, not the staged blob — CI's full run is the tree-wide truth.
if [ -n "$SPEC_FORMAT_CUTOFF" ]; then
SPEC_CANON='## 1. Goal
## 2. Scope (IN)
## 3. Non-goals (OUT)
## 4. Design
## 5. Production-readiness checklist
## 6. Acceptance criteria
## 7. Gates
## 8. Open questions
## 9. Revision log'
# §10 is date-gated exactly as the section canon itself is: a spec dated before SPEC10_CUTOFF keeps
# the nine-section shape, so adopting reuse-audit never retroactively reds a landed spec. The kit
# already ships tools/codebase-map/reuse_lookup.py; this is the check that makes anyone use it.
# The DECLARATION moved up beside its three sibling cutoffs (TOOL-aDeclaredBound-2). It used to sit
# here as `${SPEC10_CUTOFF:-<date>}`, which read the ENVIRONMENT after the conf had been sourced —
# two channels for one value, and the only cutoff of the four with an env form. That form is
# RETIRED: a conf declaration always won anyway, and an env override that outranks a committed
# declaration leaves no diff behind.
SPEC_CANON10="$SPEC_CANON
## 10. Reuse audit"
# ONE awk over the whole population, replacing ~13 forks PER SPEC (measured 42.88s of an 81.77s run
# here; upstream inCMS measured the same shape at 257.8s of 311s over 356 specs —
# TOOL-aBatchedLintel-1 ports PERF-aSlothfulCapstan-1). The driver is a tagged path stream built in
# the SHELL rather than an `ARGIND` switch: ARGIND is gawk-only, and upstream had a byte cap silently
# not exist under mawk because of it. `M` = tracked and in scope but absent from the worktree,
# `P` = analyse. `[ -f ]` stays a bash builtin so the absent-file finding keeps its position in the
# stream. The canon rides in on `-v canon=`: this kit has ONE nine-line canon and one equality, so it
# needs no canon records in the driver and therefore has no TAB-truncation hazard to guard against.
c12_all=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/spec/(.+/)?[0-9]{4}-[0-9]{2}-[0-9]{2}-spec-(($FAM_ALT)-)?[A-Za-z0-9]+-[0-9]+$REC_TAIL\.md$" || true)
pop_guard 12 "no spec file under $M/builds/*/spec/" "$(printf '%s\n' "$c12_all" | grep -c . || true)" "$PRE_SPEC"
c12_sel=$(printf '%s\n' "$c12_all" | grep . | while IFS= read -r f; do
  base=${f##*/}; d=${base:0:10}      # spawn-free date extract — this loop sees every spec file
  [ "$d" \< "$SPEC_FORMAT_CUTOFF" ] && continue
  in_scope "$f" || continue          # no-op in full mode; decides the WHOLE selection under --staged
  if [ -f "$f" ]; then printf 'P\t%s\n' "$f"; else printf 'M\t%s\n' "$f"; fi
done)
bad12_raw=""
if [ -n "$c12_sel" ]; then
# Every array below is read only up to its own counter (n, ng, q), so entries left from a previous
# file are unreachable and no `delete array` is needed — which also keeps this off a construct whose
# portability would have to be argued rather than read. Interval expressions are spelled out
# character by character for the same reason: on a build that does not honour `{8}` the header regex
# would demand those literal bytes and never match, redding every post-cutoff spec.
bad12_raw=$(printf '%s\n' "$c12_sel" | awk -F'\t' -v canon="$SPEC_CANON" -v canon10="$SPEC_CANON10" -v cut10="$SPEC10_CUTOFF" -v mroot="$M" -v discalt="$DISC_ALT" -v scut="$STREAMS_CUTOFF" -v wcut="$SPEC_WITNESS_CUTOFF" -v fcut="$FORK_MARK_CUTOFF" '
  $1 == "M" { print $2 " (tracked but missing from worktree)"; next }
  $1 != "P" { next }
  {
    f = $2
    # ---- the _unfenced fence machine, verbatim: CR strip, marker-matched fences ----
    n = 0; fence = ""
    while ((getline line < f) > 0) {
      sub(/\r$/, "", line)
      if (line ~ /^[[:space:]]*(```|~~~)/) {
        mk = (line ~ /^[[:space:]]*```/) ? "```" : "~~~"
        if (fence == "") { fence = mk; continue }
        if (mk == fence) { fence = ""; continue }
      }
      if (fence != "") continue
      body[++n] = line
    }
    close(f)
    # `body=$(_unfenced "$f")` held this text, and command substitution DROPS trailing newlines, so
    # the old body ended at its last non-empty line. That is load-bearing: the §8 extraction below
    # reproduces `sed "1d;$d"`, whose two deletes act on the CONCATENATED range output, and a body
    # that keeps its trailing blanks moves which line the last delete removes — inventing a finding
    # on a terminal spec whose §8 is the last section.
    while (n > 0 && body[n] == "") n--
    # ---- hdr: head -5 | grep -E "^\*\*Status:\*\* " | head -1, over the UNFENCED body ----
    hdr = ""; lim = (n < 5) ? n : 5
    for (i = 1; i <= lim; i++) if (body[i] ~ /^\*\*Status:\*\* /) { hdr = body[i]; break }
    if (hdr !~ /^\*\*Status:\*\* (OPEN|SPECCED|INPROGRESS|BLOCKED|DEFERRED|CLOSED|WONTDO) · rev-[0-9]+ · [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] · node [a-z] · Tier-[12] · base [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]/) {
      print f " (missing/invalid **Status:** header in lines 1-5)"
      next      # header unparseable — the per-field assertions below have no anchor
    }
    for (i = 1; i <= n; i++) if (body[i] ~ /<FAMILY-slug-seq>|YYYY-MM-DD/) { print f " (unfilled skeleton placeholder)"; break }
    if (hdr ~ /^\*\*Status:\*\* WONTDO/ && hdr !~ /base [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]* · ./)
      print f " (WONTDO needs a successor id or reason pointer in the header tail)"
    # ---- the FILENAME date, computed once. Not the first date in the PATH: a build folder used to
    # ---- be date-named itself, and matching the whole path grandfathered by the wrong date. Both
    # ---- the streams ratchet and the section canon read this, and BOTH tiers need the streams one,
    # ---- so it is computed above the Tier-1 exit rather than inside the Tier-2 block.
    fbase = f; sub(/^.*\//, "", fbase)
    fdate = ""
    if (match(fbase, /[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/)) fdate = substr(fbase, RSTART, RLENGTH)
    # ---- streams: the discipline is a SIGNAL, not a directory (1.5). Validated whenever present, on
    # ---- either tier; REQUIRED once the filename date reaches STREAMS_CUTOFF. `streams ` is matched
    # ---- as 8 ASCII bytes rather than by offsetting past the middot separator, whose length in
    # ---- characters-versus-bytes is a property of the awk build and the ambient locale.
    strv = ""
    if (match(hdr, /streams [A-Za-z0-9]+(\+[A-Za-z0-9]+)*/)) strv = substr(hdr, RSTART + 8, RLENGTH - 8)
    if (strv == "") {
      if (scut != "" && fdate != "" && fdate >= scut)
        print f " (filename date " fdate " is on/after STREAMS_CUTOFF " scut " but the header carries no `· streams <value>` segment; legal values: " discalt ")"
    } else {
      nsb = 0; sbad = ""
      ns = split(strv, sv, "+")
      for (si = 1; si <= ns; si++) if (sv[si] !~ "^(" discalt ")$") { nsb++; sbad = (nsb == 1) ? sv[si] : sbad ", " sv[si] }
      if (nsb > 0) print f " (streams value(s) outside the enum: " sbad "; legal values: " discalt ")"
    }
    # ---- acceptance witnesses: once the filename date reaches SPEC_WITNESS_CUTOFF, every
    # ---- acceptance bullet must name something in backticks. BOTH tiers, like the streams ratchet
    # ---- above and unlike the section canon below: a Tier-1 spec is exempt from the canon, not
    # ---- from meaning what it writes. Measured, the widened selector below makes Tier-1 a real
    # ---- population of 55 bullets; a bold-requiring one saw 18 and matched zero in every Tier-1
    # ---- spec in the tree, which would have made the both-tiers claim decorative.
    # ---- SHAPE ONLY: this asserts a bullet NAMES something, never that the named thing exists or
    # ---- that the build satisfied it. memory/TEMPLATE-SPEC.md says so where an author reads it.
    if (wcut != "" && fdate != "" && fdate >= wcut) {
      inac = 0; lab = ""; acc = ""; wbad = ""; nwb = 0
      for (i = 1; i <= n; i++) {
        L = body[i]
        if (L ~ /^## /) {
          if (inac && lab != "" && acc !~ /`[^`]+`/) { nwb++; wbad = (nwb == 1) ? lab : wbad ", " lab }
          inac = (L ~ /^## [0-9]+[.] Acceptance criteria[ 	]*$/); lab = ""; acc = ""; continue
        }
        if (!inac) continue
        # After the label, ANY non-alphanumeric byte or end of line. Spelling the separators as an
        # alternation is how a multibyte em-dash reached this file as mojibake once: those bytes
        # cross the writing tool, the shell and the awk regex parser, and only the last of the
        # three has an opinion about encoding. A negated class needs no such opinion, and it takes
        # all three real label forms in the corpus at once.
        # The list marker is now REQUIRED unless the label sits at column 0. Without that, a
        # hard-wrapped continuation opening with a cross-reference -- a line beginning
        # AC1-AC3 all red -- was read as a new head: it closed the real bullet early and
        # invented a phantom one, so a spec whose every criterion carried a witness could red
        # naming a label the file does not contain.
        if (L ~ /^([ 	]*(-|\*)[ 	]*)?(\*\*)?AC[0-9]+[a-z]?(\*\*)?([^A-Za-z0-9]|$)/) {
          if (lab != "" && acc !~ /`[^`]+`/) { nwb++; wbad = (nwb == 1) ? lab : wbad ", " lab }
          lab = L; sub(/^[ 	]*(-|\*)?[ 	]*(\*\*)?/, "", lab); sub(/[^A-Za-z0-9].*$/, "", lab)
          acc = L; continue
        }
        if (lab != "") acc = acc " " L
      }
      if (inac && lab != "" && acc !~ /`[^`]+`/) { nwb++; wbad = (nwb == 1) ? lab : wbad ", " lab }
      if (nwb > 0)
        print f " (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): " wcut " -- " wbad
    }
    # ---- TOOL-cSettledDocket-3: these two run for EVERY TIER, so they sit ABOVE the Tier-1 cut.
    # ---- TEMPLATE-SPEC calls the fork rule machine-checked; it was checked on Tier-2 alone because
    # ---- `next` is a PREFIX cut and both assertions sat behind it. Moving the cut cannot fix that:
    # ---- the two blocks that must STAY Tier-2-only (the section canon, the empty-body test) sit
    # ---- between the cut and these, so no placement runs these two while skipping those. Hoisted.
    # ---- header rev vs the §9 high-water. The range CLOSES on the next `## ` heading. Without that
    # ---- close it ran to the end of the body, so any rev-N below §9 -- in §10, or in later prose --
    # ---- raised the high-water and a header rev counted as logged whenever a larger number appeared
    # ---- anywhere further down. Reproduced at 99 against a true 1.
    # ---- A VERDICT change, measured before it landed: closing the range can only produce MORE
    # ---- findings, and over the real corpus it changes 0 of 22 in-scope specs. Nobody paid, so the
    # ---- two fixtures in the self-test are the only evidence this works -- one per sub-path, since
    # ---- the branch fires both when §9 logs a SMALLER rev and when it logs NONE.
    # ---- (No apostrophe below this line: the whole awk program is one single-quoted shell string.)
    k = "· rev-"; p = index(hdr, k); hrev = ""
    if (p > 0) { t = substr(hdr, p + length(k)); sp = index(t, " "); hrev = (sp > 0) ? substr(t, 1, sp - 1) : t }
    in9 = 0; seen = 0; mx = 0
    for (i = 1; i <= n; i++) {
      L = body[i]
      if (L ~ /^## [0-9]+\. Revision log/) in9 = 1
      else if (in9 && L ~ /^## /) in9 = 0
      if (in9) while (match(L, /rev-[0-9]+/)) {
        v = substr(L, RSTART + 4, RLENGTH - 4) + 0
        if (!seen || v > mx) mx = v
        seen = 1; L = substr(L, RSTART + RLENGTH)
      }
    }
    if (!seen || hrev + 0 > mx) print f " (header rev-" hrev " not logged in the §9 Revision log)"
    # ---- terminal status needs a resolved §8. Reproduces `sed -n "/A/,/B/p" | sed "1d;$d"`: the
    # ---- range RESTARTS on a later opener, runs to EOF when §9 never follows, and yields nothing
    # ---- when shorter than three lines because both deletes land inside it.
    if (hdr ~ /^\*\*Status:\*\* CLOSED/ || hdr ~ /^\*\*Status:\*\* WONTDO/) {
      q = 0; inr = 0
      for (i = 1; i <= n; i++) {
        L = body[i]
        if (!inr) { if (L ~ /^## [0-9]+\. Open questions/) { inr = 1; rng[++q] = L } }
        else { rng[++q] = L; if (L ~ /^## [0-9]+\. /) inr = 0 }
      }
      # TEMPLATE-SPEC promises TWO ways for a terminal spec to satisfy §8: it reads `none`, OR every
      # question is marked RESOLVED in place. Only the first was ever implemented, so the documented
      # second option was unreachable and a fully-resolved spec could not go CLOSED — a rule the doc
      # states and the gate does not enforce is the same false-claim class this catalogue exists for.
      q8 = ""; items = 0; resolved = 0
      for (i = 2; i <= q - 1; i++) {
        if (rng[i] ~ /^[[:space:]]*$/) continue
        if (q8 == "") { q8 = rng[i]; gsub(/^[[:space:]]+|[[:space:]]+$/, "", q8); q8 = tolower(q8) }  # TRIMMED AND LOWERCASED, matching the sibling reader byte for byte: it lowercases
        # its own opening line, so testing the RAW line here made `None`, `NONE` and a lowercase
        # `n/a` a none-form to one reader and not to the other - and the planning verb then routed
        # a run at READY on a spec this gate reds.
        # An ITEM is a list bullet OR a `###` sub-head; prose between items is commentary and is not
        # graded. TEMPLATE-SPEC sanctions both forms in as many words — "One fork per bullet or ###
        # sub-head" — and only the bullet was ever counted, so a spec that used sub-heads scored zero
        # items, could never satisfy `items == resolved`, and could never go terminal no matter how
        # thoroughly its forks were answered. That is the same false-claim class as the note directly
        # above, one level down: the doc offered two shapes and the gate implemented one.
        if (rng[i] ~ /^[[:space:]]*[-*][[:space:]]/ || rng[i] ~ /^###[[:space:]]/) {
          items++
          if (rng[i] ~ /RESOLVED/) resolved++
        }
      }
      # ---- THE TIGHTENED READER, gated by FORK_MARK_CUTOFF. Two defects in the loose form above,
      # ---- both live when this was written. First, `rng[i] ~ /RESOLVED/` grades only the line an
      # ---- item OPENS with, and in this corpus the mark almost never sits there — measured over the
      # ---- tracked specs, 246 of 339 items carry a conforming mark and nearly all of them carry it on
      # ---- a continuation line — so `items == resolved` was reachable mainly through the first-line
      # ---- escape beside it. Second, ANY first line starting `none` ended the question, so an
      # ---- unresolved bullet below a none form was invisible; and any prose containing the word
      # ---- resolved the section, including a sentence saying a fork was NOT resolved.
      # ---- So the walk is per ITEM, an item being its opening line PLUS its continuation lines, and
      # ---- the mark is the DOCUMENTED shape: the word, then a parenthesised attribution whose first
      # ---- field is the resolver class, whose second is a date, and whose optional third is the
      # ---- delegation qualifier. The regex is a `/.../` LITERAL rather than a -v string on purpose:
      # ---- awk processes escapes in a -v assignment, which turned `\(` into a group and made the
      # ---- sibling reader match nothing at all when it was written that way first.
      # ONE STRING for the mark, so a WRAPPED mark still matches — twelve tracked specs wrap one,
      # which is the house style of this corpus at its line width, and a line-by-line match called every
      # one of them unresolved.
      #
      # AND NOT A PER-ITEM WALK, which is the harder half and was measured wrong before it was
      # measured right. A per-item walk has to tell a FORK bullet from an OPTION bullet, and this
      # corpus does not distinguish them: of 287 section-8 bullets, 69 carry descriptive labels, and
      # among those are both resolved forks and genuinely OPEN ones. So a label-shape discriminator
      # UNDER-counts and lets a real open fork pass, which is worse than the over-counting it would
      # replace — and the over-counting was not theoretical either: a per-item walk called a RESOLVED
      # fork unresolved on a live tracked spec whose three option bullets each demanded a mark.
      #
      # What is graded is therefore what can be: a section with items and NO conforming mark
      # anywhere. An unresolved fork below a none line that looks honest is NOT detectable here and
      # is parked rather than implied away.
      bblob = ""; bitems = 0
      for (i = 2; i <= q - 1; i++) {
        L = rng[i]
        if (L ~ /^[[:space:]]*$/) continue
        bblob = bblob " " L
        if (L ~ /^[[:space:]]*[-*][[:space:]]/ || L ~ /^###[[:space:]]/) bitems++
      }
      # WHITESPACE SQUEEZED FIRST. Marks wrap INSIDE the parenthesis in this corpus - `RESOLVED
      # (owner,` then a 2-space-indented continuation - so a raw join yields three spaces where the
      # grammar wants one, and all fourteen wrapped marks still missed. The sibling reader trims
      # every line as it reads, which is why it did not need this; squeezing here makes the two
      # provably agree instead of agreeing by coincidence.
      gsub(/[[:space:]]+/, " ", bblob)
      bmark = (bblob ~ /RESOLVED \((owner|agent), [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9](, delegated)?\)/)
      if (q == 0)
        print f " (terminal Status and no Open questions section found — silence and a resolved fork are the same byte without this)"
      else if (fcut != "" && fdate != "" && fdate >= fcut) {
        # ---- A §8 with NO items and NO none form REFUSES, which the owner ratified: it is the only
        # ---- genuinely undecided population, it is reached through the empty-first-line branch, and
        # ---- an empty population passing is the shape this repo refuses by name everywhere else.
        if (bitems == 0) {
          if (q8 !~ /^none/ && q8 !~ /^n\/a/)
            print f " (terminal Status and a §8 carrying neither an item nor a none form, at/after FORK_MARK_CUTOFF " fcut "; a hollow section and a resolved one are the same byte)"
        # SAME RULE AS THE SIBLING READER: with items present, only a MARK resolves the section. The
        # opening line used to vote here too, and `/^none/` matches "none of the forks below are
        # resolved" - a denial - once the line is lowercased.
        } else if (!bmark)
          print f " (terminal Status, §8 carries items and no conforming resolution mark anywhere, at/after FORK_MARK_CUTOFF " fcut ")"
      }
      else if (q8 != "" && q8 !~ /^none/ && q8 !~ /^n\/a/ && !(items > 0 && items == resolved))
        print f " (terminal Status with unresolved §8 Open questions)"
    }

    if (hdr ~ /Tier-1/) next
    # ---- Tier-2 body assertions ----
    ng = 0; got = ""
    for (i = 1; i <= n; i++) if (body[i] ~ /^## /) { got = (++ng == 1) ? body[i] : got "\n" body[i] }
    # pick the canon by FILENAME date (computed above), mirroring how the whole check is grandfathered
    want = (fdate != "" && fdate >= cut10) ? canon10 : canon
    wantn = (want == canon10) ? "ten" : "nine"
    if (got != want) {
      print f " (## sections differ from the canonical " wantn " of " mroot "/TEMPLATE-SPEC.md):"
      print "\001\t" f      # the excerpt is a real diff — rebuilt by the post-pass below
    }
    # ---- empty section bodies. The old test was `NF > 0` on a split record; the line is read into a
    # ---- variable here, so NF does not exist and /[^ \t]/ stands in. The two agree on every
    # ---- plain-text line; they part only on an invalid multibyte byte under gawk in a UTF-8 locale.
    ne = 0; emp = ""; s = ""; cnt = 0
    for (i = 1; i <= n; i++) {
      L = body[i]
      if (L ~ /^## /) {
        if (s != "" && cnt == 0) { ne++; emp = (ne == 1) ? "    " s : emp "\n    " s }
        s = L; cnt = 0; continue
      }
      if (s != "" && L ~ /[^ \t]/) cnt++
    }
    if (s != "" && cnt == 0) { ne++; emp = (ne == 1) ? "    " s : emp "\n    " s }
    if (ne > 0) print f " (section with an empty body — write N/A — <why>):" "\n" emp
  }')
fi
# The section-canon excerpt keeps a REAL `diff`: reproducing its normal-format output inside awk
# would need a longest-common-subsequence implementation, and the mismatch path fires zero times on a
# clean tree. awk emits a sentinel record and the excerpt is rebuilt here by the ORIGINAL commands
# over the ORIGINAL inputs, so the bytes cannot drift from a second implementation. The `case` guard
# means a clean run never enters the loop.
case "$bad12_raw" in
  *$'\001'*)
    bad12=$(printf '%s\n' "$bad12_raw" | while IFS= read -r _ln; do
      case "$_ln" in
        $'\001'*)
          _f=${_ln#$'\001'$'\t'}
          _g=$(_unfenced "$_f" | grep -E '^## ' || true)
          # Diff the canon AWK CHOSE, by the same basename-date rule. Diffing the nine-canon
          # when awk wanted ten printed a BLANK excerpt for the primary new failure mode — a
          # diagnostic that cannot describe its own finding.
          _b=${_f##*/}
          _d=$(printf %s "$_b" | grep -oE "[0-9]{4}-[0-9]{2}-[0-9]{2}" | head -1)
          if [ -n "$_d" ] && ! [ "$_d" \< "$SPEC10_CUTOFF" ]; then _want=$SPEC_CANON10; else _want=$SPEC_CANON; fi
          diff <(printf '%s\n' "$_want") <(printf '%s\n' "$_g") | head -6 | sed 's/^/    /' ;;
        *) printf '%s\n' "$_ln" ;;
      esac
    done) ;;
  *) bad12=$bad12_raw ;;
esac
[ -n "$bad12" ] && fail 12 "spec files dated >= $SPEC_FORMAT_CUTOFF not conforming to $M/TEMPLATE-SPEC.md:
$bad12"
fi

# 13-16 — id + path corpus classification (delegates to the sibling classifier). ONE grammar and ONE
# walk: this script owns the append-only and index sets and PRINTS them on demand; the classifier
# owns the id grammar it imports from the recall kit. Neither transcribes the other. Every pin the
# classifier reads is measured per corpus, and blank pins turn the whole unit off.
if [ "$STAGED" = 0 ]; then
  if ! ids=$("$_PY" "$HERE/corpus_ids.py" --check 2>&1); then
    printf '%s
' "$ids"; status=1
  fi
fi

# 17-19 — the bug-class catalogue (delegates to the sibling module). The catalogue's INDEX is
# generated, every class record declares a gate or says it has none, and a record whose anchors reach
# only the append-only tree is reachable on paper and dead in practice.
if [ "$STAGED" = 0 ]; then
  if ! got=$("$_PY" "$HERE/gotchas.py" --check 2>&1); then
    printf '%s
' "$got"; status=1
  fi
fi

# 20 — the row documents' grammar, and id collisions INSIDE one file. Delegated for the same reason
# 13-19 are: the assertion is a corpus walk with a pin, which is a Python job, and check-arms.py's
# population is `*.sh` only, so the branches are armed by the module's own selftest.
if [ "$STAGED" = 0 ]; then
  if ! rowg=$("$_PY" "$HERE/row_grammar.py" --check 2>&1); then
    printf '%s
' "$rowg"; status=1
  fi
fi

# grandfather stale-line guards (a listed path that no longer exists fails).
# One `git ls-files` + set lookups, NOT `git ls-files --error-unmatch` per path — git is a heavyweight
# fork, so a long grandfather list was one spawn per line (~80s at inCMS's 522 lines). Entries are
# literal paths, never globs, so exact membership in the tracked set is equivalent.
if [ -n "$LEGACY$DEBT" ]; then
  declare -A TRACKED_SET
  while IFS= read -r _l; do [ -n "$_l" ] && TRACKED_SET["$_l"]=1; done < <(git ls-files)
  badL=$(printf '%s\n' "$LEGACY" | grep . | while IFS= read -r p; do [ -n "${TRACKED_SET[$p]+x}" ] || echo "$p"; done)
  [ -n "$badL" ] && fail 5 "legacy-files.txt lists paths that no longer exist (stale-line guard):
$badL"
  badD=$(printf '%s\n' "$DEBT" | grep . | while IFS= read -r p; do [ -n "${TRACKED_SET[$p]+x}" ] || echo "$p"; done)
  [ -n "$badD" ] && fail 6 "curation-debt.txt lists paths that no longer exist (stale-line guard):
$badD"
fi

# ---- 22: every acceptance criterion of a CLOSED Tier-2 unit is EVIDENCED or AMENDED.
# ---- TOOL-dUnstalledConvoy-12. Specs number their criteria and nothing joined a built unit back to
# ---- those numbers: `build-complete` reads terminal STATUS only, and the closing-review item says
# ---- outright that it measures a review EXISTS and never what it concluded. This is the join.
# ----
# ---- WHAT IT DOES NOT CHECK, and the header says so because a structural check reads as a semantic
# ---- one to everybody who did not write it: that an observation token names anything real, that the
# ---- observation was actually made, or that an amendment was justified. It reads SHAPE and
# ---- COVERAGE. Its inputs are both authored by whoever built the unit, so a green row here is not
# ---- evidence the unit was built correctly — only that it says which criterion each claim answers.
# ----
# ---- THE HEADING IS LOCATED BY TEXT, never by number, and by the SAME regex the acceptance-witness
# ---- rule above uses. Tier-1 has a light profile in which the section canon is not enforced, so a
# ---- Tier-1 spec's section 6 may be Gates — two closed ones in this corpus are — and a check reading
# ---- section 6 by NUMBER would red a spec that is legal under the format it enforces.
alcut="${ACCEPTANCE_LEDGER_CUTOFF:-}"
if [ -n "$alcut" ]; then
  # The ledger, flattened ONCE to `<unit> <label> <form>` triples across every tracked record. A
  # record may carry several `**Evidences:**` blocks; a block ends at the next one or at a heading.
  alledger=$(for r in $(git ls-files "$M/builds/*/build/*.md" "$M/builds/*/reviews/*.md" 2>/dev/null); do
    awk '
      /^\*\*Serves:\*\*/ { j = ($0 ~ /\*\*Serves:\*\* *journal/) }
      /^\*\*Evidences:\*\* / { u = (j ? $2 : ""); next }
      /^#/ { u = ""; next }
      u != "" && /^- *(\*\*)?AC[0-9]+/ {
        lab = $2; gsub(/\*/, "", lab); sub(/[^A-Za-z0-9].*$/, "", lab)
        form = ($0 ~ /`[^`]+`/) ? "obs" : (($0 ~ /amended rev-[0-9]+/) ? "amd" : "bad")
        print u " " lab " " form
      }' "$r"
  done)
  alpop=0; algap=""; albad=""; alnolab=""
  alspecs=$(git ls-files "$M/builds/*/spec/*.md" 2>/dev/null || true)
  # The LISTING, guarded, not the post-cutoff population: a tree whose closed Tier-2 specs all
  # predate the cutoff is a real empty and says so below, but a listing that comes back empty
  # while spec files exist is a broken selector, and it reds. That distinction is the whole
  # difference between an announced skip and a check that is dark and looks identical to green.
  pop_guard 23 "no spec file selected under $M/builds/*/spec/" "$(printf '%s
' "$alspecs" | grep -c . || true)" "$PRE_SPEC"
  for sp in $alspecs; do
    case "$(basename "$sp")" in
      [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*) sdate=$(basename "$sp" | cut -c1-10) ;;
      *) continue ;;
    esac
    printf '%s\n%s\n' "$alcut" "$sdate" | sort -C || continue
    hdr=$(sed -n '1,6p' "$sp" | grep -m1 '^\*\*Status:\*\*')
    case "$hdr" in *" CLOSED "*) ;; *) continue ;; esac
    case "$hdr" in *"Tier-2"*) ;; *) continue ;; esac
    grep -qE '^## [0-9]+[.] Acceptance criteria[ 	]*$' "$sp" || continue
    uid=$(sed -n 's/^# \([A-Z][A-Za-z0-9-]*\) .*/\1/p' "$sp" | head -1)
    [ -n "$uid" ] || continue
    # A DECLARED, NARROW EXEMPTION, listed by unit id and never by pattern. The cutoff is a DATE and
    # a date boundary falls mid-day: a unit that closed before this grammar existed can share its
    # cutoff date with one that closed after. Back-filling another build's ledger is not this build's
    # to do — a build's own folder owns its own prose — so the exemption is declared, auditable and
    # shrink-only, with its reason beside it in the conf.
    case " ${ACCEPTANCE_LEDGER_GRANDFATHER:-} " in *" $uid "*) continue ;; esac
    alpop=$((alpop + 1))
    labs=$(awk '
      /^## / { inac = ($0 ~ /^## [0-9]+[.] Acceptance criteria[ 	]*$/); next }
      !inac { next }
      /^([ 	]*(-|\*)[ 	]*)?(\*\*)?AC[0-9]+[a-z]?(\*\*)?([^A-Za-z0-9]|$)/ {
        lab = $0; sub(/^[ 	]*(-|\*)?[ 	]*(\*\*)?/, "", lab); sub(/[^A-Za-z0-9].*$/, "", lab); print lab
      }' "$sp" | sort -u)
    if [ -z "$labs" ]; then
      # A CLOSED Tier-2 spec with the heading and no labels cannot be evidenced, and "every criterion
      # is evidenced" is vacuously TRUE over none of them. That vacuity is the whole reason this arm
      # exists rather than being an oversight the check tolerates.
      alnolab="$alnolab $uid"
      continue
    fi
    for lab in $labs; do
      row=$(printf '%s\n' "$alledger" | grep -m1 -E "^$uid $lab (obs|amd|bad)$" || true)
      if [ -z "$row" ]; then algap="$algap $uid/$lab"
      else case "$row" in *" bad") albad="$albad $uid/$lab" ;; esac
      fi
    done
  done
  [ -z "$algap" ] || fail 23 "a CLOSED unit numbers an acceptance criterion that no journal record evidences, so nothing says which observation answered it and conformance is unreadable:$algap"
  [ -z "$albad" ] || fail 23 "an acceptance-ledger line is in neither legal form, and there is no third: OBSERVED carries a backticked token, AMENDED names the revision, and anything else is a checkbox:$albad"
  [ -z "$alnolab" ] || fail 23 "a CLOSED Tier-2 spec carries an acceptance-criteria section that numbers no criterion, so every claim about its coverage is vacuously true:$alnolab"
  [ "$alpop" -gt 0 ] || printf 'memory-hygiene: check 23 measured NO unit — every closed Tier-2 spec predates ACCEPTANCE_LEDGER_CUTOFF, so a green verdict here is coverage of nothing\n'
fi

# --- empty-population report (see pop_guard). Reported ONCE, after every check has run, so the
# --- message names every disarmed selector instead of the first one. A tree that genuinely has no
# --- builds yet is a real case: scaffold it, or set MEMORY_ROOT to the tree that has one.
if [ -n "$POP_MISSING" ]; then
  echo "HYGIENE FAILED — a check selected an EMPTY population. An empty selection prints nothing,"
  echo "HYGIENE which is exactly what a passing check prints, so the gate would be green over an"
  echo "HYGIENE unlinted tree. Either the tree is unscaffolded or a path selector is mis-segmented."
  printf '%s' "$POP_MISSING"
  status=1
fi

exit "$status"
