#!/usr/bin/env bash
# Structured-memory-tree hygiene gate — the mechanized form of <MEMORY_ROOT>/HYGIENE.md.
# Config-driven (.memory-tree.conf: MEMORY_ROOT, DISCIPLINES, FAMILIES, TOMBSTONE_ROOTS,
# SPEC_FORMAT_CUTOFF). Single source
# of truth: HYGIENE.md's "Check" section, CI, the pre-commit hook, and the local gate runner all invoke
# THIS script — never hand-copy the checks. Part of the coding-governance memory-tree kit.
#
#   memory-tree/check-memory-hygiene.sh            # full check
#   memory-tree/check-memory-hygiene.sh --staged   # pre-commit fast leg (set-checks tree-wide, file-checks on staged paths)
#
# Exit 0 + no output = clean. Anything printed is a hygiene regression.
set -u
KIT_MEMORY_TREE_VERSION=1.3   # gov:kit memory-tree@1.3 — engine identity; set HERE, never from .memory-tree.conf (a project conf must not spoof it)
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
DISCIPLINES="architecture deployment blocks design performance"
FAMILIES="architecture:ARCH deployment:DEPLOY blocks:BLOCK design:DES performance:PERF"
TOMBSTONE_ROOTS=""     # old tree root(s) a migrated project must keep empty (e.g. "docs"); blank = skip check 11
SPEC_FORMAT_CUTOFF=""  # YYYY-MM-DD; specs whose filename date >= this must follow TEMPLATE-SPEC.md (check 12); blank = skip
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
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
FAMILY_of() { local p; for p in $FAMILIES; do case "$p" in "$1:"*) echo "${p#*:}"; return;; esac; done; }
FAM_ALT=$(for p in $FAMILIES; do echo "${p#*:}"; done | paste -sd'|' -)   # ARCH|DEPLOY|... for regexes
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

# 2 — link integrity (exempt DECISIONS.md / decisions/ / archive/ / TREE.md and legacy-listed recording files).
scan2=$(printf '%s\n' "$FILES" | grep -E '\.md$' | grep -vE '/(DECISIONS\.md$|decisions/|archive/|TREE\.md$)')
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

# 3 — structure lint (depth-2; decisions/guides/archive/journal opaque).
disc_re=$(printf '%s\n' $DISCIPLINES | paste -sd'|' -)
root1=$(printf '%s\n' "$FILES" | awk -F/ '{ if (NF==2) print "F:"$2; else print "D:"$2 }' | LC_ALL=C sort -u)
bad3=$(printf '%s\n' "$root1" | grep . | while IFS= read -r e; do case "$e" in
  F:README.md|F:TREE.md|F:HYGIENE.md|F:TEMPLATE-SPEC.md|D:project) ;;
  D:*) d="${e#D:}"; { printf '%s\n' $DISCIPLINES | grep -qxF "$d" || [ "$d" = "$MAP_SUB" ]; } || echo "$M/$d";;
  *) echo "$M/${e#*:}";; esac; done)
for disc in $DISCIPLINES; do
  d1=$(printf '%s\n' "$FILES" | grep "^$M/$disc/" | awk -F/ '{ if (NF==3) print "F:"$3; else print "D:"$3 }' | LC_ALL=C sort -u)
  b=$(printf '%s\n' "$d1" | grep . | while IFS= read -r e; do case "$e" in
    F:README.md|F:TREE.md|F:DECISIONS.md|F:BACKLOG.md|D:decisions|D:guides|D:archive|D:builds) ;;
    *) echo "$M/$disc/${e#*:}";; esac; done)
  bad3=$(printf '%s\n%s\n' "$bad3" "$b")
done
p1=$(printf '%s\n' "$FILES" | grep "^$M/project/" | awk -F/ '{ if (NF==3) print "F:"$3; else print "D:"$3 }' | LC_ALL=C sort -u)
bp=$(printf '%s\n' "$p1" | grep . | while IFS= read -r e; do case "$e" in
  F:README.md|F:MEMORY.md|F:IN-FLIGHT.md|F:legacy-files.txt|F:curation-debt.txt|D:journal|D:in-flight) ;;
  F:*.md) ;;
  *) echo "$M/project/${e#*:}";; esac; done)
bm=""
if [ -n "$MAP_SUB" ]; then
  m1=$(printf '%s\n' "$FILES" | grep "^$M/$MAP_SUB/" | awk -F/ '{ if (NF==3) print "F:"$3; else print "D:"$3 }' | LC_ALL=C sort -u)
  bm=$(printf '%s\n' "$m1" | grep . | while IFS= read -r e; do case "$e" in
    F:README.md|F:FOUNDATION.md|F:baseline.toml|D:features|D:generated) ;;
    *) echo "$M/$MAP_SUB/${e#*:}";; esac; done)
fi
bad3=$(printf '%s\n%s\n%s\n' "$bad3" "$bp" "$bm" | grep . || true)
[ -n "$bad3" ] && fail 3 "unexpected entries (structure):
$bad3"

# 4 — build-folder naming + FAMILY↔discipline pairing + internal shape.
# One grep+awk PER DISCIPLINE — was a per-folder full-$FILES rescan + a per-entry grep, i.e.
# O(build-folders × files): 82.5s of a 138s run on the upstream inCMS tree (137 folders / 1152 files;
# PERF-eThriftyBellows-1 there). The awk groups build files by folder (git-ls-files input is
# path-sorted, so folders and entries arrive in order), validates folder-name + FAMILY↔discipline +
# entry-shape in-process, and insertion-sorts each folder's entry set so output byte-matches the old
# `sort -u` (D: before F:, C byte order — hence LC_ALL=C). famalt/m come from the conf; the folder
# field index derives from MEMORY_ROOT's segment count (the old hardcoded NF==5 mis-parsed a
# multi-segment root). The `→` is the literal arrow byte, identical to the old message.
bad4=""
for disc in $DISCIPLINES; do
  fam=$(FAMILY_of "$disc")
  b=$(printf '%s\n' "$FILES" | grep -E "^$M/$disc/builds/[^/]+/" \
    | LC_ALL=C awk -F/ -v m="$M" -v disc="$disc" -v fam="$fam" -v famalt="$FAM_ALT" '
      BEGIN {
        n_m = split(m, _seg, "/"); fidx = n_m + 3    # <m>/<disc>/builds/<folder>
        vre = "^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-(" famalt ")-[A-Za-z0-9][A-Za-z0-9-]*$"
      }
      function flush(   n,i,j,k,keys,tmp,type,name,ffam) {
        if (folder=="") return
        if (folder !~ vre) {
          print m "/" disc "/builds/" folder " (bad folder name)"; folder=""; delete ent; return }
        ffam=folder; sub(/^[0-9-]+-/,"",ffam); sub(/-.*$/,"",ffam)   # a FAMILY token has no dash (id grammar)
        if (ffam!=fam) print m "/" disc "/builds/" folder " (FAMILY " ffam " != " disc "→" fam ")"
        n=0; for (k in ent) keys[++n]=k
        for (i=2;i<=n;i++){ tmp=keys[i]; j=i-1; while(j>=1 && keys[j]>tmp){keys[j+1]=keys[j];j--} keys[j+1]=tmp }
        for (i=1;i<=n;i++){ k=keys[i]; type=substr(k,1,1); name=substr(k,3)
          if (k=="F:README.md"||k=="F:STATUS.md"||k=="D:prompts"||k=="D:spec"||k=="D:build"||k=="D:reviews") continue
          if (type=="F"){ if (name !~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-(prompt|spec|build|review)-[A-Za-z0-9]+-[0-9]+\.md$/) print m "/" disc "/builds/" folder "/" name }
          else print m "/" disc "/builds/" folder "/" name }
        folder=""; delete ent
      }
      { if ($fidx!=folder){ flush(); folder=$fidx }
        if (NF==fidx+1) ent["F:" $(fidx+1)]=1; else ent["D:" $(fidx+1)]=1 }
      END { flush() }')
  bad4="$bad4
$b"
done
bad4=$(printf '%s\n' "$bad4" | grep . || true)
[ -n "$bad4" ] && fail 4 "build-folder naming/shape:
$bad4"

# 5 — recording-file naming (grandfather: legacy-files.txt).
bad5=$(printf '%s\n' "$FILES" | grep -E "^$M/[^/]+/builds/[^/]+/(prompts|spec|build|reviews)/[^/]+\.md$" | while IFS= read -r f; do
  in_legacy "$f" && continue
  # Fork-free basename/parent-dir + bash ERE (was basename + awk + grep = 3 forks per recording file).
  base=${f##*/}; sub=${f%/*}; sub=${sub##*/}
  case "$sub" in prompts) kind=prompt;; spec) kind=spec;; build) kind=build;; reviews) kind=review;; esac
  [[ $base =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-$kind-[A-Za-z0-9]+-[0-9]+\.md$ ]] || echo "$f"
done)
[ -n "$bad5" ] && fail 5 "recording-file names not matching YYYY-MM-DD-<kind>-<slug>-<seq>.md (and not grandfathered):
$bad5"

# index set for checks 6/7
index_set() {
  { echo "$M/README.md"; echo "$M/TREE.md"; echo "$M/project/MEMORY.md"; echo "$M/project/IN-FLIGHT.md"
    printf '%s\n' "$FILES" | grep -E "^$M/project/in-flight/[^/]+\.md$"   # per-node ledger files: 20KB cap, entry-budget exempt
    if [ -n "$MAP_SUB" ]; then
      echo "$M/$MAP_SUB/README.md"; echo "$M/$MAP_SUB/FOUNDATION.md"
      printf '%s\n' "$FILES" | grep -E "^$M/$MAP_SUB/features/[^/]+\.md$"   # dossiers: size caps, entry-budget exempt
    fi
    for d in $DISCIPLINES; do for x in README DECISIONS BACKLOG TREE; do echo "$M/$d/$x.md"; done; done
    printf '%s\n' "$FILES" | grep -E "^$M/[^/]+/builds/[^/]+/STATUS\.md$"
  } | while IFS= read -r f; do [ -f "$f" ] && echo "$f"; done
}
INDEX_SET=$(index_set)   # compute ONCE; checks 6 and 7 both read it (was recomputed per check)

# 6 — index size caps (grandfather: curation-debt.txt).
# Batched wc: one `wc -c` + one `wc -l` over the whole selected set (was 2 forks PER index file).
# Findings emit in index_set order (the -l stream's arg order); multi-file wc `total` lines are
# skipped by name; `+0` coerces the counts.
sel6=$(printf '%s\n' "$INDEX_SET" | while IFS= read -r f; do in_debt "$f" && continue; in_scope "$f" || continue; printf '%s\n' "$f"; done)
bad6=""
if [ -n "$sel6" ]; then
  cbytes=$(printf '%s\n' "$sel6" | xargs -r wc -c)
  clines=$(printf '%s\n' "$sel6" | xargs -r wc -l)
  bad6=$(awk '
    FNR==NR { if ($NF!="total") b[$NF]=$1; next }
    $NF=="total" { next }
    { l[$NF]=$1; ord[++n]=$NF }
    END { for(i=1;i<=n;i++){ f=ord[i]; if (b[f]+0>20480 || l[f]+0>250) printf "%s (%dB %dL > 20480B/250L)\n", f, b[f]+0, l[f]+0 } }
  ' <(printf '%s\n' "$cbytes") <(printf '%s\n' "$clines"))
fi
[ -n "$bad6" ] && fail 6 "index files over cap (rotate to archive/<INDEX>.<YYYY-MM-DD>.md; a codebase-map dossier over cap is SPLIT into two dossiers instead — never rotate FOUNDATION.md, the map gate requires it):
$bad6"

# 7 — entry budget ≤300 chars (grandfather: curation-debt.txt; exempt TREE.md, IN-FLIGHT.md, in-flight/*.md,
#     and — when the codebase-map kit is adopted under this tree — its dossiers/FOUNDATION (detail files).
ex7='(/TREE\.md$|/IN-FLIGHT\.md$|/in-flight/[^/]+\.md$)'
[ -n "$MAP_SUB" ] && ex7="(/TREE\.md$|/IN-FLIGHT\.md$|/in-flight/[^/]+\.md$|/$MAP_SUB/FOUNDATION\.md$|/$MAP_SUB/features/[^/]+\.md$)"
bad7=$(printf '%s\n' "$INDEX_SET" | grep -vE "$ex7" | while IFS= read -r f; do
  in_debt "$f" && continue; in_scope "$f" || continue
  _unfenced "$f" | awk -v F="$f" 'length($0)>300 && $0 !~ /^#/ && $0 !~ /^[[:space:]]*\|[-: |]+\|[[:space:]]*$/ { print F":"FNR" ("length($0)" chars)" }'
done)
[ -n "$bad7" ] && fail 7 "index entry lines over 300 chars:
$bad7"

# 8 — status vocabulary on BACKLOG.md / STATUS.md (grandfather: curation-debt.txt).
# One awk over the whole filtered file set (was _unfenced + grep -n PER file and a 3-fork
# printf|grep -oE|wc -l PER row). nmatch() reproduces `grep -oE '…\b' | wc -l` EXACTLY: the
# `^[[:space:]]*-` slot can only anchor once (caret pattern on the first match, no-caret thereafter),
# and the trailing `\b` is checked ZERO-WIDTH (next char is end/non-word) so it never consumes a
# following delimiter. uln counts the UNFENCED stream (== the old grep -n numbering). The two `·` in
# the patterns are the LITERAL middot byte. Validated per-row against grep over the upstream inCMS
# tree's 589 real rows — 0 mismatches (PERF-eThriftyBellows-1).
files8=$( { for d in $DISCIPLINES; do echo "$M/$d/BACKLOG.md"; done; printf '%s\n' "$FILES" | grep -E "^$M/[^/]+/builds/[^/]+/STATUS\.md$"; } | while IFS= read -r f; do
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
[ -n "$bad8" ] && fail 8 "backlog/STATUS rows without exactly one status token (OPEN SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO):
$bad8"

# 9 — TREE.md drift (delegates to the sibling generator).
if [ "$STAGED" = 0 ] || printf '%s\n' "$STAGED_MD" | grep -q .; then
  if ! drift=$(bash "$HERE/gen-memory-tree.sh" --check 2>&1); then fail 9 "TREE.md drift:
$drift"; fi
fi

# 10 — rotation note (always; cheap).
bad10=$(for d in $DISCIPLINES; do
  printf '%s\n' "$FILES" | grep -E "^$M/$d/archive/[^/]+\.[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$" | while IFS= read -r a; do
    base=$(basename "$a"); idx="$M/$d/${base%%.*}.md"
    [ -f "$idx" ] || continue
    head -3 "$idx" | grep -qF "$base" || echo "$a (not referenced in lines 1-3 of $idx)"
  done
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
bad12=$(printf '%s\n' "$FILES" | grep -E "^$M/[^/]+/builds/[^/]+/spec/(.+/)?[0-9]{4}-[0-9]{2}-[0-9]{2}-spec-[A-Za-z0-9]+-[0-9]+(-[a-z0-9][a-z0-9-]*)?\.md$" | while IFS= read -r f; do
  base=${f##*/}; d=${base:0:10}      # spawn-free date extract — this loop sees every spec file
  [ "$d" \< "$SPEC_FORMAT_CUTOFF" ] && continue
  in_scope "$f" || continue
  [ -f "$f" ] || { echo "$f (tracked but missing from worktree)"; continue; }
  body=$(_unfenced "$f")
  hdr=$(printf '%s\n' "$body" | head -5 | grep -E '^\*\*Status:\*\* ' | head -1)
  if ! printf '%s' "$hdr" | grep -qE '^\*\*Status:\*\* (OPEN|SPECCED|INPROGRESS|BLOCKED|DEFERRED|CLOSED|WONTDO) · rev-[0-9]+ · [0-9]{4}-[0-9]{2}-[0-9]{2} · node [a-z] · Tier-[12] · base [0-9a-f]{8}'; then
    echo "$f (missing/invalid **Status:** header in lines 1-5)"
    continue      # header unparseable — the per-field assertions below have no anchor
  fi
  printf '%s\n' "$body" | grep -qE '<FAMILY-slug-seq>|YYYY-MM-DD' && echo "$f (unfilled skeleton placeholder)"
  case "$hdr" in
    '**Status:** WONTDO'*) printf '%s' "$hdr" | grep -qE 'base [0-9a-f]{8,} · .' \
      || echo "$f (WONTDO needs a successor id or reason pointer in the header tail)";;
  esac
  case "$hdr" in *'Tier-1'*) continue;; esac
  # ---- Tier-2 body assertions ----
  got=$(printf '%s\n' "$body" | grep -E '^## ' || true)
  if [ "$got" != "$SPEC_CANON" ]; then
    echo "$f (## sections differ from the canonical nine of $M/TEMPLATE-SPEC.md):"
    diff <(printf '%s\n' "$SPEC_CANON") <(printf '%s\n' "$got") | head -6 | sed 's/^/    /'
  fi
  empty=$(printf '%s\n' "$body" | awk '/^## /{ if (s != "" && n == 0) print "    " s; s = $0; n = 0; next } s != "" && NF > 0 { n++ } END { if (s != "" && n == 0) print "    " s }')
  [ -n "$empty" ] && echo "$f (section with an empty body — write N/A — <why>):
$empty"
  hrev=${hdr#*· rev-}; hrev=${hrev%% *}
  lrev=$(printf '%s\n' "$body" | awk '/^## 9\. Revision log/{f=1} f{ while(match($0,/rev-[0-9]+/)){ v=substr($0,RSTART+4,RLENGTH-4)+0; if(!seen||v>mx){mx=v} seen=1; $0=substr($0,RSTART+RLENGTH) } } END{ if(seen) print mx }')   # was a 5-fork sed|grep|sed|sort|tail chain; numeric max, lrev only feeds a numeric test
  if [ -z "$lrev" ] || [ "$hrev" -gt "$lrev" ] 2>/dev/null; then
    echo "$f (header rev-$hrev not logged in the §9 Revision log)"
  fi
  case "$hdr" in
    '**Status:** CLOSED'*|'**Status:** WONTDO'*)
      q8=$(printf '%s\n' "$body" | sed -n '/^## 8\. Open questions/,/^## 9\. /p' | sed '1d;$d' | grep -vE '^[[:space:]]*$' | head -1)
      case "$q8" in none*|N/A*|'') ;; *) echo "$f (terminal Status with unresolved §8 Open questions)";; esac;;
  esac
done)
[ -n "$bad12" ] && fail 12 "spec files dated >= $SPEC_FORMAT_CUTOFF not conforming to $M/TEMPLATE-SPEC.md:
$bad12"
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

exit "$status"
