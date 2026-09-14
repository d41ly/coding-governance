#!/usr/bin/env bash
# check-arms-groups.sh — the structural group linter over the batched gate self-test. TOOL-aBatchedArm-2.
#
#   bash <kit>/check-arms-groups.sh [<test file>]   # default: check-unattended.test.sh beside this script
#
#   exit 0 = every group clean · 1 = a rule red · 2 = REFUSED (unreadable file, an empty delimiter
#   set, zero groups or zero arms parsed — a linter that parsed nothing never prints a clean verdict)
#
# WHAT IT GRADES. One pass over ONE text file, no subprocess per group, no suite executed. The file
# is cut into GROUPS at every tree reset, and three rules are read off each group's LINKAGE:
#   rule A — a batched group (one carrying an `emitted` call, the token TOOL-aBatchedArm-1 gives a
#            tree shared by more than one arm) contains a `miss` or a `same` at all. A control asserts
#            SILENCE, and on a shared tree a branch a group-mate's break pushed dark is byte-identical
#            to one that stayed silent, so no control is ever batched (TOOL-dScriptedRepeat-15 S3).
#   rule B — two arms in one group carry an identical assertion text: one break cannot satisfy two
#            assertions, so the second is either dead or a copy-paste that asserts nothing new.
#   rule C — a `run` capture in a group is assigned to a name other than `out`: a baseline captured
#            under one name and read by another group is a poisoned baseline, invisible to `emitted`.
# THE DELIMITER IS RESOLVED FROM THE FILE, never typed: every function whose body performs a hard
# reset (`git reset --hard`) or calls one that does, transitively, is a tree reset; plus every
# `if in_shard k` region seam. An empty resolution REFUSES. A bare `reset_tree` grep is not the
# delimiter — spec-audit round 2 measured 24 boundaries it cannot see — and a merged pair of groups
# manufactures rule-B and rule-C reds on correct code while hiding real ones.
#
# WHAT IT DOES NOT GRADE, said here because a structural check reads as a semantic one to everybody
# who did not write it (AGENTS.md §7):
#   - ADEQUACY. Whether an arm proves anything, whether a `hit` proves what its author meant, or
#     whether a branch the suite never names is reachable. It reads linkage, not meaning.
#   - THE `emitted` SET. Whether a group's expected signature set is correct, complete or observed is
#     the helper's own business at run time; the sentinel `"?"` is COUNTED on the liveness line and
#     never graded, and a typed-rather-than-observed set is invisible here.
#   - THE CHECKER. Which branches `check-unattended.sh` has, and which fire, is `check-arms.py`'s
#     question; this file is never opened.
#   - INLINE ARMS. Assertions spelled as `n=$((n+1)); … || { echo "FAIL …"; st=1; }` carry no helper
#     name and are not arms to this linter; only `hit`, `miss` and `same` calls are.
#   - FUNCTION BODIES and comments. A call inside a helper's definition is a definition, not a group.
#   - EXISTING VIOLATIONS are reported, never waived: the count over the tracked suite is the unit's
#     starting figure and lives in its acceptance ledger, not in a registry here.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
[ -n "$HERE" ] || { echo "check-arms-groups: cannot derive my own directory, so the default subject cannot be found"; exit 2; }
FILE="${1:-$HERE/check-unattended.test.sh}"
[ -f "$FILE" ] || { echo "check-arms-groups: REFUSED — no such file to lint: $FILE"; exit 2; }

echo "check-arms-groups: linting $FILE"
echo "check-arms-groups: does NOT grade adequacy, the emitted set, the checker, inline arms, function bodies or comments — linkage only (rules A, B, C; header above)"

awk '
# ---- helpers ------------------------------------------------------------------------------------
function strip(s) {                       # quoted strings and `${…}` out, then the comment tail
  gsub(/"[^"]*"/, "", s); gsub(/\047[^\047]*\047/, "", s); gsub(/\$\{[^}]*\}/, "", s)
  sub(/(^|[ \t])#.*$/, "", s); return s
}
function first_word(s,   w) {             # the command word of one `;`-separated segment
  sub(/^[ \t({!]+/, "", s)
  if (match(s, /^[A-Za-z_][A-Za-z0-9_]*/)) return substr(s, RSTART, RLENGTH)
  return ""
}
function is_boundary(s,   t, k, m, parts, w) {   # s is already stripped
  t = s; gsub(/(&&|\|\||\||;)/, "\n", t)
  m = split(t, parts, "\n")
  for (k = 1; k <= m; k++) { w = first_word(parts[k]); if (w != "" && (w in DEL)) return 1 }
  return 0
}
function calls_member(s,   k, m, parts, w) {     # any word of a stripped body line in DEL
  m = split(s, parts, /[^A-Za-z0-9_]+/)
  for (k = 1; k <= m; k++) { w = parts[k]; if (w != "" && (w in DEL)) return 1 }
  return 0
}
{ n++; L[n] = $0 }
END {
  if (n == 0) { print "check-arms-groups: REFUSED — the file is empty, so it graded nothing"; exit 2 }
  # ---- pass 1: function spans, brace-balanced over stripped lines; every line of a body is skipped
  nf = 0
  for (i = 1; i <= n; i++) {
    if (L[i] ~ /^[A-Za-z_][A-Za-z0-9_]*\(\)[ \t]*\{/) {
      name = L[i]; sub(/\(\).*$/, "", name)
      depth = 0; j = i
      while (j <= n) {
        s = strip(L[j]); depth += gsub(/\{/, "{", s) - gsub(/\}/, "}", s)
        if (depth <= 0) break
        j++
      }
      if (j > n) j = n
      nf++; FN[nf] = name; FA[nf] = i; FZ[nf] = j
      for (k = i; k <= j; k++) INFN[k] = 1
      i = j
    }
  }
  # ---- the delimiter set: roots perform a hard reset; the closure is over callers, to a fixpoint
  ndel = 0
  for (f = 1; f <= nf; f++) {
    for (k = FA[f]; k <= FZ[f]; k++) {
      s = strip(L[k])
      if (s ~ /(^|[^A-Za-z0-9_])git[ \t]+reset([ \t]|$)/ && s ~ /--hard/) { DEL[FN[f]] = 1; break }
    }
  }
  do {
    changed = 0
    for (f = 1; f <= nf; f++) {
      if (FN[f] in DEL) continue
      for (k = FA[f]; k <= FZ[f]; k++) if (calls_member(strip(L[k]))) { DEL[FN[f]] = 1; changed = 1; break }
    }
  } while (changed)
  set = ""
  for (f = 1; f <= nf; f++) if (FN[f] in DEL) { set = set " " FN[f]; ndel++ }
  if (ndel == 0) {
    print "check-arms-groups: REFUSED — no function in the file performs a hard reset, so the delimiter set is EMPTY and nothing can be cut into groups"
    exit 2
  }
  print "check-arms-groups: delimiter set resolved from the file:" set " (" ndel " helper(s), root = git reset --hard, closed over callers) plus every `if in_shard` seam"
  # ---- pass 2: boundaries and groups over top-level logical lines
  g = 0; nb = 0; seams = 0; arms = 0; sent = 0; nfind = 0; fa = 0; fb = 0; fc = 0
  GS[0] = 0                                   # group 0 is the prologue before the first boundary
  for (i = 1; i <= n; i++) {
    if (INFN[i]) continue
    s = L[i]; j = i
    while (s ~ /\\[ \t]*$/ && j < n) { sub(/\\[ \t]*$/, "", s); j++; t = L[j]; sub(/^[ \t]+/, "", t); s = s " " t }
    st = strip(s)
    if (st ~ /^[ \t]*$/) { i = j; continue }
    if (s ~ /^if[ \t]+in_shard[ \t]/) { g++; nb++; seams++; GS[g] = i; i = j; continue }
    if (is_boundary(st)) { g++; nb++; GS[g] = i }
    # arms
    if (s ~ /^[ \t]*(hit|miss|same)[ \t]/) {
      h = s; sub(/^[ \t]*/, "", h); sub(/[ \t].*$/, "", h)
      text = ""
      if (h == "same") { if (match(s, /^[ \t]*same[ \t]+"[^"]*"/)) { text = substr(s, RSTART, RLENGTH); sub(/^[ \t]*same[ \t]+/, "", text) } }
      else if (match(s, /"[^"]*"[ \t]*$/)) { text = substr(s, RSTART, RLENGTH); sub(/[ \t]*$/, "", text) }
      if (text == "") { text = s; sub(/^[ \t]*/, "", text) }
      arms++; NA[g]++
      AL[g, NA[g]] = i; AH[g, NA[g]] = h; AT[g, NA[g]] = text
    }
    # the batched marker and its sentinel
    if (s ~ /^[ \t]*emitted[ \t]/) { NE[g]++; if (s ~ /^[ \t]*emitted[ \t]+"\?"([ \t]|$)/) sent++ }
    # captures
    if (match(s, /^[ \t]*[A-Za-z_][A-Za-z0-9_]*=\$\(/)) {
      nm = substr(s, RSTART, RLENGTH); sub(/^[ \t]*/, "", nm); sub(/=.*$/, "", nm)
      rest = substr(s, RSTART + RLENGTH)
      while (match(rest, /^[ \t]*[A-Za-z_][A-Za-z0-9_]*=[^ \t]*[ \t]+/)) rest = substr(rest, RSTART + RLENGTH)
      if (rest ~ /^[ \t]*run([ \t;)|>]|$)/) {
        NC[g]++
        if (nm != "out") { nfind++; fc++; F[nfind] = "RED rule C · group at line " GS[g] " · line " i ": capture `" nm "` is not this group'"'"'s own `out` — a baseline read from another name is poisoned" }
      }
    }
    i = j
  }
  # ---- rule A and rule B, per group
  for (q = 1; q <= g; q++) {
    if (NE[q] > 0) for (a = 1; a <= NA[q]; a++) if (AH[q, a] == "miss" || AH[q, a] == "same") {
      nfind++; fa++; F[nfind] = "RED rule A · group at line " GS[q] " · line " AL[q, a] ": " AH[q, a] " " AT[q, a] " — a control inside a batched group"
    }
    split("", seen); split("", lines)
    for (a = 1; a <= NA[q]; a++) { key = AT[q, a]; seen[key]++; lines[key] = lines[key] " " AL[q, a] }
    for (key in seen) if (seen[key] > 1) { nfind++; fb++; F[nfind] = "RED rule B · group at line " GS[q] " · lines" lines[key] ": " seen[key] " arms carry one text " key }
  }
  # ---- liveness FIRST, then the findings, then the verdict
  withArms = 0; batched = 0
  for (q = 1; q <= g; q++) { if (NA[q] > 0) withArms++; if (NE[q] > 0) batched++ }
  print "check-arms-groups: boundaries " nb " (" seams " seams) · groups " g " · with arms " withArms " · arms " arms " · batched " batched " · sentinels " sent
  if (g == 0 || arms == 0) {
    print "check-arms-groups: REFUSED — parsed " g " group(s) and " arms " arm(s), so it graded nothing; this is not a clean verdict"
    exit 2
  }
  for (k = 1; k <= nfind; k++) print F[k]
  if (nfind > 0) { print "check-arms-groups: RED — " nfind " finding(s) · rule A " fa " · rule B " fb " · rule C " fc; exit 1 }
  print "check-arms-groups: GREEN — 0 findings over " g " groups and " arms " arms"
  exit 0
}' "$FILE"
