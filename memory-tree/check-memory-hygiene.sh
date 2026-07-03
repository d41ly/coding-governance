#!/usr/bin/env bash
# Structured-memory-tree hygiene gate — the mechanized form of <MEMORY_ROOT>/HYGIENE.md.
# Config-driven (.memory-tree.conf: MEMORY_ROOT, DISCIPLINES, FAMILIES, TOMBSTONE_ROOTS). Single source
# of truth: HYGIENE.md's "Check" section, CI, the pre-commit hook, and the local gate runner all invoke
# THIS script — never hand-copy the checks. Part of the coding-governance memory-tree kit.
#
#   memory-tree/check-memory-hygiene.sh            # full check
#   memory-tree/check-memory-hygiene.sh --staged   # pre-commit fast leg (set-checks tree-wide, file-checks on staged paths)
#
# Exit 0 + no output = clean. Anything printed is a hygiene regression.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
DISCIPLINES="architecture deployment blocks design performance"
FAMILIES="architecture:ARCH deployment:DEPLOY blocks:BLOCK design:DES performance:PERF"
TOMBSTONE_ROOTS=""     # old tree root(s) a migrated project must keep empty (e.g. "docs"); blank = skip check 11
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
M="$MEMORY_ROOT"
HERE="$(cd "$(dirname "$0")" && pwd)"
STAGED=0; [ "${1:-}" = "--staged" ] && STAGED=1

status=0
FILES=$(git ls-files "$M/")
LEGACY=$(grep -vE '^\s*(#|$)' "$M/project/legacy-files.txt" 2>/dev/null || true)
DEBT=$(grep -vE '^\s*(#|$)' "$M/project/curation-debt.txt" 2>/dev/null || true)
in_legacy() { printf '%s\n' "$LEGACY" | grep -qxF "$1"; }
in_debt()   { printf '%s\n' "$DEBT"   | grep -qxF "$1"; }
fail() { echo "HYGIENE check $1 FAILED — $2"; status=1; }
FAMILY_of() { local p; for p in $FAMILIES; do case "$p" in "$1:"*) echo "${p#*:}"; return;; esac; done; }
FAM_ALT=$(for p in $FAMILIES; do echo "${p#*:}"; done | paste -sd'|' -)   # ARCH|DEPLOY|... for regexes
_unfenced() { awk '/^[[:space:]]*(```|~~~)/ { f=!f; next } !f' "$1"; }

if [ "$STAGED" = 1 ]; then STAGED_MD=$(git diff --cached --name-only --diff-filter=ACMR -- "$M/**" | LC_ALL=C sort); fi
in_scope() { [ "$STAGED" = 0 ] && return 0; printf '%s\n' "$STAGED_MD" | grep -qxF "$1"; }

# 1 — prompt placement: prompt-kind files only under builds/*/prompts/ or archive/.
c1=$(printf '%s\n' "$FILES" \
  | grep -E '(\.prompt\.md|\.build-prompt\.md|-prompt\.md|/[0-9]{4}-[0-9]{2}-[0-9]{2}-prompt-[A-Za-z0-9-]+-[0-9]+\.md)$' \
  | grep -vE '/(builds/[^/]+/prompts/|archive/)' || true)
[ -n "$c1" ] && fail 1 "prompt-kind files outside builds/*/prompts/ or archive/:
$c1"

# 2 — link integrity (exempt DECISIONS.md / decisions/ / archive/ / TREE.md and legacy-listed recording files).
scan2=$(printf '%s\n' "$FILES" | grep -E '\.md$' | grep -vE '/(DECISIONS\.md$|decisions/|archive/|TREE\.md$)')
[ "$STAGED" = 1 ] && scan2=$(printf '%s\n' "$scan2" | { grep -xF -f <(printf '%s\n' "$STAGED_MD") || true; })
broken=$(printf '%s\n' "$scan2" | grep . | while IFS= read -r f; do
  in_legacy "$f" && continue
  d=$(dirname "$f")
  awk '/^[[:space:]]*(```|~~~)/ { fence=!fence; next } !fence' "$f" \
    | grep -oE '\]\([^)]+\.md[^)]*\)' | sed -E 's/^\]\(([^)#]+).*/\1/' \
    | while IFS= read -r t; do case "$t" in http*|/*) continue;; esac; [ -f "$d/$t" ] || echo "$f -> $t (MISSING)"; done
done)
[ -n "$broken" ] && fail 2 "broken relative .md links:
$broken"

# 3 — structure lint (depth-2; decisions/guides/archive/journal opaque).
disc_re=$(printf '%s\n' $DISCIPLINES | paste -sd'|' -)
root1=$(printf '%s\n' "$FILES" | awk -F/ '{ if (NF==2) print "F:"$2; else print "D:"$2 }' | LC_ALL=C sort -u)
bad3=$(printf '%s\n' "$root1" | grep . | while IFS= read -r e; do case "$e" in
  F:README.md|F:TREE.md|F:HYGIENE.md|D:project) ;;
  D:*) d="${e#D:}"; printf '%s\n' $DISCIPLINES | grep -qxF "$d" || echo "$M/$d";;
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
  F:README.md|F:MEMORY.md|F:IN-FLIGHT.md|F:legacy-files.txt|F:curation-debt.txt|D:journal) ;;
  F:*.md) ;;
  *) echo "$M/project/${e#*:}";; esac; done)
bad3=$(printf '%s\n%s\n' "$bad3" "$bp" | grep . || true)
[ -n "$bad3" ] && fail 3 "unexpected entries (structure):
$bad3"

# 4 — build-folder naming + FAMILY↔discipline pairing + internal shape.
bad4=""
for disc in $DISCIPLINES; do
  fam=$(FAMILY_of "$disc")
  folders=$(printf '%s\n' "$FILES" | grep -E "^$M/$disc/builds/[^/]+/" | sed -E "s#^$M/$disc/builds/([^/]+)/.*#\\1#" | LC_ALL=C sort -u)
  for fld in $folders; do
    [ -z "$fld" ] && continue
    if ! printf '%s' "$fld" | grep -qE "^[0-9]{4}-[0-9]{2}-[0-9]{2}-($FAM_ALT)-[A-Za-z0-9][A-Za-z0-9-]*$"; then
      bad4="$bad4
$M/$disc/builds/$fld (bad folder name)"; continue
    fi
    ffam=$(printf '%s' "$fld" | sed -E "s/^[0-9-]+-($FAM_ALT)-.*/\\1/")
    [ "$ffam" = "$fam" ] || bad4="$bad4
$M/$disc/builds/$fld (FAMILY $ffam != $disc→$fam)"
    ents=$(printf '%s\n' "$FILES" | grep -E "^$M/$disc/builds/$fld/" | awk -F/ '{ if (NF==5) print "F:"$5; else print "D:"$5 }' | LC_ALL=C sort -u)
    b=$(printf '%s\n' "$ents" | grep . | while IFS= read -r e; do case "$e" in
      F:README.md|F:STATUS.md|D:prompts|D:spec|D:build|D:reviews) ;;
      F:*) n="${e#F:}"; printf '%s' "$n" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}-(prompt|spec|build|review)-[A-Za-z0-9]+-[0-9]+\.md$' || echo "$M/$disc/builds/$fld/$n";;
      *) echo "$M/$disc/builds/$fld/${e#*:}";; esac; done)
    bad4="$bad4
$b"
  done
done
bad4=$(printf '%s\n' "$bad4" | grep . || true)
[ -n "$bad4" ] && fail 4 "build-folder naming/shape:
$bad4"

# 5 — recording-file naming (grandfather: legacy-files.txt).
bad5=$(printf '%s\n' "$FILES" | grep -E "^$M/[^/]+/builds/[^/]+/(prompts|spec|build|reviews)/[^/]+\.md$" | while IFS= read -r f; do
  in_legacy "$f" && continue
  base=$(basename "$f"); sub=$(printf '%s' "$f" | awk -F/ '{print $(NF-1)}')
  case "$sub" in prompts) kind=prompt;; spec) kind=spec;; build) kind=build;; reviews) kind=review;; esac
  printf '%s' "$base" | grep -qE "^[0-9]{4}-[0-9]{2}-[0-9]{2}-$kind-[A-Za-z0-9]+-[0-9]+\.md$" || echo "$f"
done)
[ -n "$bad5" ] && fail 5 "recording-file names not matching YYYY-MM-DD-<kind>-<slug>-<seq>.md (and not grandfathered):
$bad5"

# index set for checks 6/7
index_set() {
  { echo "$M/README.md"; echo "$M/TREE.md"; echo "$M/project/MEMORY.md"; echo "$M/project/IN-FLIGHT.md"
    for d in $DISCIPLINES; do for x in README DECISIONS BACKLOG TREE; do echo "$M/$d/$x.md"; done; done
    printf '%s\n' "$FILES" | grep -E "^$M/[^/]+/builds/[^/]+/STATUS\.md$"
  } | while IFS= read -r f; do [ -f "$f" ] && echo "$f"; done
}

# 6 — index size caps (grandfather: curation-debt.txt).
bad6=$(index_set | while IFS= read -r f; do
  in_debt "$f" && continue; in_scope "$f" || continue
  b=$(wc -c <"$f"); l=$(wc -l <"$f")
  { [ "$b" -gt 20480 ] || [ "$l" -gt 250 ]; } && echo "$f (${b}B ${l}L > 20480B/250L)"
done)
[ -n "$bad6" ] && fail 6 "index files over cap (rotate to archive/<INDEX>.<YYYY-MM-DD>.md):
$bad6"

# 7 — entry budget ≤300 chars (grandfather: curation-debt.txt; exempt TREE.md, IN-FLIGHT.md).
bad7=$(index_set | grep -vE '(/TREE\.md$|/IN-FLIGHT\.md$)' | while IFS= read -r f; do
  in_debt "$f" && continue; in_scope "$f" || continue
  _unfenced "$f" | awk -v F="$f" 'length($0)>300 && $0 !~ /^#/ && $0 !~ /^[[:space:]]*\|[-: |]+\|[[:space:]]*$/ { print F":"FNR" ("length($0)" chars)" }'
done)
[ -n "$bad7" ] && fail 7 "index entry lines over 300 chars:
$bad7"

# 8 — status vocabulary on BACKLOG.md / STATUS.md (grandfather: curation-debt.txt).
bad8=$( { for d in $DISCIPLINES; do echo "$M/$d/BACKLOG.md"; done; printf '%s\n' "$FILES" | grep -E "^$M/[^/]+/builds/[^/]+/STATUS\.md$"; } | while IFS= read -r f; do
  [ -f "$f" ] || continue; in_debt "$f" && continue; in_scope "$f" || continue
  _unfenced "$f" | grep -nE '^[[:space:]]*[|-].*[A-Z]+-[A-Za-z0-9]*-?[0-9]' | while IFS= read -r ln; do
    n=$(printf '%s' "${ln#*:}" | grep -oE '([·|]|^[[:space:]]*-)[[:space:]]*(OPEN|SPECCED|INPROGRESS|BLOCKED|DEFERRED|CLOSED|WONTDO)\b' | wc -l)
    [ "$n" -ne 1 ] && echo "$f:${ln%%:*}"
  done
done)
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

# grandfather stale-line guards (a listed path that no longer exists fails).
badL=$(printf '%s\n' "$LEGACY" | grep . | while IFS= read -r p; do git ls-files --error-unmatch "$p" >/dev/null 2>&1 || echo "$p"; done)
[ -n "$badL" ] && fail 5 "legacy-files.txt lists paths that no longer exist (stale-line guard):
$badL"
badD=$(printf '%s\n' "$DEBT" | grep . | while IFS= read -r p; do git ls-files --error-unmatch "$p" >/dev/null 2>&1 || echo "$p"; done)
[ -n "$badD" ] && fail 6 "curation-debt.txt lists paths that no longer exist (stale-line guard):
$badD"

exit "$status"
