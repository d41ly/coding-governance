#!/usr/bin/env bash
# **Serves:** research TOOL-aBriskPreflight-7
# The ceilings instrument for TOOL-aBriskPreflight-7 (spec §4 "The values"), widened by TOOL-aBriskPreflight-11.
#
#   bash memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh [--selftest]
#
# Reads the committed rows beside it — the whole-preflight A/B's rows and this unit's `cw-after-<n>`,
# count and window rows — and prints the driver's three constant lines exactly as
# `tools/unattended/unattended.sh` spells them, so `diff` against
#   grep -E '^(WIRING_CEILING|PREFLIGHT_CEILING|CEILING_SPAWN_MS)=' tools/unattended/unattended.sh
# refuses a retyped constant. Per subject:
#   ceiling = the next multiple of 30 at or above W + E*max(0, S_w - S_m) + K*max(0, K_w - K_m) + U
# W the slowest untraced after-arm run, S_m and K_m its own host row's spawn5/5 and fork, E and K the
# traced counts, U the sum over the declared waits of max(0, timeout - window). S_w and K_w are priced
# at every host row on record, any arm and any exit status: S_w the larger of 2.5 s and every host
# row's spawn5/5, K_w the larger of 0.91 s and every host row's fork (both floors PINNED, node a,
# 2026-10-11). Before any subject it prints on stderr the figures it priced at and how many host rows
# set them.
# Exits 1 naming the subject when a row is missing, a timed row has no host row before it, or the
# WIRING value reaches the GATE_BOUND `.unattended.conf` declares: that ceiling races GATE_BOUND on one
# child and could never fire first. PREFLIGHT_CEILING kills nothing and compares the whole wall, which
# no bound covers, so it is printed whatever its relation to GATE_BOUND, with a stderr line when it
# sits at or above it (owner, spec 11 §8 F2).
# --selftest runs the same program text over the fixture rows below, reads no file, and asserts the
# old-arm host row sets K_w and S_w.
# WHAT IT DOES NOT CHECK: that the rows are honest readings, or that the traced count was taken from
# the tree the timed rows ran. Each row names its source; the spec's §4 "The rows this pass read"
# says why each was taken.
set -u
PROG='
  # key=value fields up to `source=`, whose free text may carry any word, `timeout` included
  { subj = ""; split("", f)
    for (i = 1; i <= NF; i++) { if ($i ~ /^source=/) break; if (index($i, "=")) { split($i, kv, "="); f[kv[1]] = kv[2] } } }
  $1 == "host" {
    hl = f["label"]; hs[hl] = f["spawn5"] / 5; hk[hl] = f["fork"] + 0; nh++
    if (hs[hl] > sw) sw = hs[hl]
    if (hk[hl] > kw) kw = hk[hl]
    prev = hl; next
  }
  $1 ~ /^label=/ {
    lab = f["label"]
    if (lab ~ /^cw-after-[0-9]+$/) subj = "wiring"
    else if (lab ~ /^ab-AN-[0-9]+$/) subj = "preflight"
    if (subj == "") { prev = ""; next }
    if (prev != lab) { printf "ceilings: %s: timed row %s has no host row before it\n", subj, lab; bad = 1; next }
    prev = ""
    if (f["rc"] != 0) next
    n[subj]++
    if (f["wall"] + 0 > W[subj]) { W[subj] = f["wall"] + 0; Sm[subj] = hs[lab]; Km[subj] = hk[lab] }
    next
  }
  $1 == "count" { E[f["subject"]] = f["execs"]; K[f["subject"]] = f["forks"]; nc[f["subject"]]++; prev = ""; next }
  $1 == "window" { u = f["timeout"] - f["window"]; if (u < 0) u = 0; U[f["subject"]] += u; nu[f["subject"]]++; prev = ""; next }
  { prev = "" }
  END {
    if (bad) exit 1
    printf "ceilings: priced at S_w=%.2f s per spawn and K_w=%.2f s per fork, the worst of %d host rows and the pinned floors\n", sw, kw, nh > "/dev/stderr"
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
      if (v[s] < gb) continue
      if (s == "wiring") { printf "ceilings: %s: %d s is at or above the declared %d s GATE_BOUND, so it could never fire first\n", s, v[s], gb; exit 1 }
      printf "ceilings: %s: %d s is at or above the declared %d s GATE_BOUND; it kills nothing and compares the whole wall, so it is printed\n", s, v[s], gb > "/dev/stderr"
    }
    printf "WIRING_CEILING=\"%d\"\nPREFLIGHT_CEILING=\"%d\"\nCEILING_SPAWN_MS=\"%d\"\n", v["wiring"], v["preflight"], int(sw * 1000 + 0.5)
  }
'
if [ "${1:-}" = "--selftest" ]; then
  # The ab-AO-9 pair has the real ab-AO-2 shape: an old-arm label no subject claims, exit 1. Its fork
  # and spawn5/5 sit above every timed row and both floors, so 9.00 and 4.00 come from the host branch.
  priced=$(awk -v gb=999999 -v sw=2.5 -v kw=0.91 -v minw=3 -v minp=2 "$PROG" 2>&1 >/dev/null <<'ROWS'
host label=ab-AO-9 spawn5=20.00 fork=9.00
label=ab-AO-9 rc=1 wall=100.0
host label=ab-AN-1 spawn5=1.00 fork=0.05
label=ab-AN-1 rc=0 wall=100.0
host label=ab-AN-2 spawn5=1.00 fork=0.05
label=ab-AN-2 rc=0 wall=100.0
host label=cw-after-1 spawn5=1.00 fork=0.05
label=cw-after-1 rc=0 wall=10.0
host label=cw-after-2 spawn5=1.00 fork=0.05
label=cw-after-2 rc=0 wall=10.0
host label=cw-after-3 spawn5=1.00 fork=0.05
label=cw-after-3 rc=0 wall=10.0
count label=t subject=wiring execs=1 forks=1 source=fixture
count label=t subject=preflight execs=1 forks=1 source=fixture
window label=t subject=wiring wait=w timeout=1 window=1 source=fixture
window label=t subject=preflight wait=w timeout=1 window=1 source=fixture
ROWS
  )
  case $priced in
    *"K_w=9.00 s per fork"*) case $priced in *"S_w=4.00 s per spawn"*) echo "ceilings selftest: ok — K_w=9.00 S_w=4.00 from the old-arm host row"; exit 0 ;; esac ;;
  esac
  printf 'ceilings selftest: FAIL — the old-arm host row did not set K_w=9.00 and S_w=4.00; read: %s\n' "$priced"
  exit 1
fi
D=$(cd "$(dirname "$0")" && pwd) || exit 2
ROOT=$(git -C "$D" rev-parse --show-toplevel) || exit 2
GB=$(sed -n 's/^GATE_BOUND="\([0-9][0-9]*\)".*/\1/p' "$ROOT/.unattended.conf")
[ -n "$GB" ] || { echo "ceilings: .unattended.conf declares no whole-number GATE_BOUND"; exit 1; }
awk -v gb="$GB" -v sw=2.5 -v kw=0.91 -v minw=3 -v minp=2 "$PROG" "$D/2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log" "$D/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log"
