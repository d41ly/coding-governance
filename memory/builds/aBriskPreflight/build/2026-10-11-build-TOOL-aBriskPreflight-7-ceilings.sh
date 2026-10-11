#!/usr/bin/env bash
# The ceilings instrument for TOOL-aBriskPreflight-7 (spec §4 "The values").
#
#   bash memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh
#
# Reads the committed after-arm rows beside it — the whole-preflight A/B's `ab-AN-<n>` rows and this
# unit's `cw-after-<n>`, count and window rows — and prints the driver's three constant lines exactly
# as `tools/unattended/unattended.sh` spells them, so `diff` against
#   grep -E '^(WIRING_CEILING|PREFLIGHT_CEILING|CEILING_SPAWN_MS)=' tools/unattended/unattended.sh
# refuses a retyped constant. Per subject:
#   ceiling = the next multiple of 30 at or above W + E*max(0, S_w - S_m) + K*max(0, K_w - K_m) + U
# W the slowest untraced run, S_m and K_m its own host row's spawn5/5 and fork, E and K the traced
# counts, U the sum over the declared waits of max(0, timeout - window), S_w the larger of 2.5 s and
# every S_m read, K_w the larger of 0.91 s and every K_m read (both floors PINNED, node a, 2026-10-11).
# Exits 1 naming the subject when a row is missing, a timed row has no host row before it, or a value
# reaches the GATE_BOUND `.unattended.conf` declares: a ceiling there can never fire first.
# WHAT IT DOES NOT CHECK: that the rows are honest readings, or that the traced count was taken from
# the tree the timed rows ran. Each row names its source; the spec's §4 "The rows this pass read"
# says why each was taken.
set -u
D=$(cd "$(dirname "$0")" && pwd) || exit 2
ROOT=$(git -C "$D" rev-parse --show-toplevel) || exit 2
GB=$(sed -n 's/^GATE_BOUND="\([0-9][0-9]*\)".*/\1/p' "$ROOT/.unattended.conf")
[ -n "$GB" ] || { echo "ceilings: .unattended.conf declares no whole-number GATE_BOUND"; exit 1; }
awk -v gb="$GB" -v sw=2.5 -v kw=0.91 -v minw=3 -v minp=2 '
  # key=value fields up to `source=`, whose free text may carry any word, `timeout` included
  { subj = ""; split("", f)
    for (i = 1; i <= NF; i++) { if ($i ~ /^source=/) break; if (index($i, "=")) { split($i, kv, "="); f[kv[1]] = kv[2] } } }
  $1 == "host" { hl = f["label"]; hs[hl] = f["spawn5"] / 5; hk[hl] = f["fork"]; prev = hl; next }
  $1 ~ /^label=/ {
    lab = f["label"]
    if (lab ~ /^cw-after-[0-9]+$/) subj = "wiring"
    else if (lab ~ /^ab-AN-[0-9]+$/) subj = "preflight"
    if (subj == "") { prev = ""; next }
    if (prev != lab) { printf "ceilings: %s: timed row %s has no host row before it\n", subj, lab; bad = 1; next }
    prev = ""
    if (f["rc"] != 0) next
    n[subj]++
    if (hs[lab] > sw) sw = hs[lab]
    if (hk[lab] + 0 > kw) kw = hk[lab] + 0
    if (f["wall"] + 0 > W[subj]) { W[subj] = f["wall"] + 0; Sm[subj] = hs[lab]; Km[subj] = hk[lab] + 0 }
    next
  }
  $1 == "count" { E[f["subject"]] = f["execs"]; K[f["subject"]] = f["forks"]; nc[f["subject"]]++; prev = ""; next }
  $1 == "window" { u = f["timeout"] - f["window"]; if (u < 0) u = 0; U[f["subject"]] += u; nu[f["subject"]]++; prev = ""; next }
  { prev = "" }
  END {
    if (bad) exit 1
    split("wiring preflight", ss, " ")
    for (j = 1; j <= 2; j++) {
      s = ss[j]; need = (s == "wiring") ? minw : minp
      if (n[s] < need) { printf "ceilings: %s: %d untraced rows, %d needed\n", s, n[s], need; exit 1 }
      if (nc[s] != 1) { printf "ceilings: %s: %d traced count rows, 1 needed\n", s, nc[s]; exit 1 }
      if (nu[s] < 1) { printf "ceilings: %s: no window row for a declared wait\n", s; exit 1 }
      ds = sw - Sm[s]; if (ds < 0) ds = 0
      dk = kw - Km[s]; if (dk < 0) dk = 0
      x = W[s] + E[s] * ds + K[s] * dk + U[s]
      c = int(x / 30); if (c * 30 < x) c++
      v[s] = c * 30
      if (v[s] >= gb) { printf "ceilings: %s: %d s is at or above the declared %d s GATE_BOUND, so it could never fire first\n", s, v[s], gb; exit 1 }
    }
    printf "WIRING_CEILING=\"%d\"\nPREFLIGHT_CEILING=\"%d\"\nCEILING_SPAWN_MS=\"%d\"\n", v["wiring"], v["preflight"], int(sw * 1000 + 0.5)
  }
' "$D/2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log" "$D/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log"
