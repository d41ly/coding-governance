#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-8
# TOOL-aSparedSpawn-8 S11 — the assertion-line inventory of one suite file, so a conversion that
# drops or doubles an assertion is caught by a diff and not by the suite's own green.
#
#   bash <this> <suite file>   ->  one `helper TAB first-quoted-argument` line per assertion call, sorted
#
# THE HELPER SET IS DERIVED FROM THE FILE, never typed. The counter is the variable the file's
# `PASS ($<counter> assertions)` line prints; when the file computes it as `<counter>=$((a+b))`, both
# `a` and `b` are counters. A helper is a function whose body increments a counter, closed over the
# functions whose bodies call a helper. An assertion line is any line outside a helper's own
# definition calling a helper at a command position, keyed by the helper and its first argument.
# EVERY EXPANSION IN THAT ARGUMENT READS AS ONE `$...` TOKEN — `$x`, `${x}`, `$(cmd …)` and `$((…))`
# alike — so a message whose text interpolates a value keys the same whichever spelling produced the
# value, which is the one edit a fork-free conversion makes to an assertion line. The literal words of
# the message, and the helper, are compared exactly.
#
# WHAT THIS DOES NOT SEE: an increment written inline on the asserting line rather than in a helper,
# a helper called through a variable or `eval`, and a call split across a line continuation, whose
# first argument then reads as empty. A miss is the same on both sides of a diff, so it cannot hide a
# dropped assertion of the kinds it does see.
set -u
f=${1:-}
[ -f "$f" ] || { echo "arm-inventory: usage: bash arm-inventory.sh <suite file> — no such file: $f" >&2; exit 2; }
awk '
  # The end of the expansion opening at s[i] ("$"), so the caller can skip it whole.
  function skipexp(s, i,   c, d, q, j) {
    c = substr(s, i + 1, 1)
    if (c == "(" || c == "{") {
      d = 0; q = ""
      for (j = i + 1; j <= length(s); j++) {
        c = substr(s, j, 1)
        if (q != "") { if (c == q) q = ""; continue }
        if (c == "\047" || c == "\"") { q = c; continue }
        if (c == "(" || c == "{") d++
        if (c == ")" || c == "}") { d--; if (d == 0) return j }
      }
      return length(s)
    }
    if (match(substr(s, i + 1), /^([A-Za-z_][A-Za-z0-9_]*|[0-9@*#?$!-])/)) return i + RLENGTH
    return i
  }
  # The first argument at the head of s, every expansion in it read as one `$...` token.
  function readarg(s,   q, i, c, a, e) {
    q = substr(s, 1, 1); a = ""
    if (q == "\047") { e = index(substr(s, 2), "\047"); return e ? substr(s, 2, e - 1) : substr(s, 2) }
    if (q == "\"") i = 2; else { q = ""; i = 1 }
    for (; i <= length(s); i++) {
      c = substr(s, i, 1)
      if (c == "\\") { a = a substr(s, i, 2); i++; continue }
      if (q == "\"" && c == "\"") break
      if (q == "" && c ~ /[ \t;|&)]/) break
      if (c == "$") { e = skipexp(s, i); if (e > i) { a = a "$..."; i = e; continue } }
      a = a c
    }
    return a
  }
  function isfn(s) { return match(s, /^[ \t]*[A-Za-z_][A-Za-z0-9_]*[ \t]*\(\)[ \t]*\{/) }
  function fname(s,   t) { t = s; sub(/^[ \t]*/, "", t); sub(/[ \t]*\(\).*/, "", t); return t }
  NR == FNR {
    sub(/\r$/, "")
    if (match($0, /PASS \(\$\{?[A-Za-z_][A-Za-z0-9_]*/)) { c = substr($0, RSTART + 7, RLENGTH - 7); sub(/^\{/, "", c); ctr[c] = 1 }
    if (match($0, /^[ \t]*[A-Za-z_][A-Za-z0-9_]*=\$\(\([A-Za-z_][A-Za-z0-9_]*\+[A-Za-z_][A-Za-z0-9_]*\)\)/)) {
      a = $0; sub(/^[ \t]*/, "", a); lhs = a; sub(/=.*/, "", lhs); sub(/^[^(]*\(\(/, "", a); sub(/\)\).*/, "", a)
      split(a, ab, "+"); sum[lhs] = ab[1] " " ab[2]
    }
    if (cur == "" && isfn($0)) {
      cur = fname($0); body[cur] = $0; start[cur] = FNR
      t = $0; sub(/#.*/, "", t)
      # A one-line body whose quoted string runs onto later lines ends where that string closes.
      oneq = (gsub(/\047/, "\047", t) % 2 == 1)
      if (!oneq && t ~ /\}[ \t;]*$/ && t !~ /\{[ \t]*$/) { stop[cur] = FNR; cur = "" }
      next
    }
    if (cur != "") {
      body[cur] = body[cur] "\n" $0
      if ($0 ~ /^\}/ || (oneq && $0 ~ /\047/ && $0 ~ /\}[ \t]*$/)) { stop[cur] = FNR; cur = ""; oneq = 0 }
    }
    next
  }
  FNR == 1 {
    for (c in ctr) if (c in sum) { split(sum[c], ab, " "); ctr[ab[1]] = 1; ctr[ab[2]] = 1 }
    for (f in body) for (c in ctr) {
      if (index(body[f], c "=$((" c "+1))") || index(body[f], c "=$((" c " + 1))") || index(body[f], "((" c "++))")) helper[f] = 1
    }
    do {
      grew = 0
      for (f in body) if (!(f in helper)) for (h in helper)
        if (match(body[f], "(^|[^A-Za-z0-9_$-])" h "([ \t;]|$)")) { helper[f] = 1; grew = 1; break }
    } while (grew)
    nh = 0; for (h in helper) nh++
    if (nh == 0) { print "arm-inventory: no function in this file increments the counter its PASS line prints, so there is no assertion population to compare" > "/dev/stderr"; bad = 1; exit 2 }
  }
  {
    sub(/\r$/, "")
    for (h in helper) if (FNR >= start[h] && FNR <= stop[h]) next
    if ($0 ~ /^[ \t]*#/) next
    line = $0
    for (h in helper) {
      rest = line
      while (match(rest, "(^|[;&|{(!][ \t]*|(then|do|else)[ \t]+|^[ \t]+)" h "([ \t]|$)")) {
        tail = substr(rest, RSTART + RLENGTH); rest = tail
        sub(/^[ \t]*/, "", tail)
        print h "\t" readarg(tail)
      }
    }
  }
  END { if (bad) exit 2 }
' "$f" "$f" | LC_ALL=C sort
exit "${PIPESTATUS[0]}"
