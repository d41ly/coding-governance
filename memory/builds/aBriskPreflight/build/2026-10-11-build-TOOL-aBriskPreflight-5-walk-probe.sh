#!/usr/bin/env bash
# **Serves:** research TOOL-aBriskPreflight-5
# TOOL-aBriskPreflight-5's instrument: the live-run walk over THIS tree's run records, read through
# the driver's own functions, before and after the derivation cache.
#
#   bash <this> --fields [--fail-batch] <driver> <scratch-dir> <label>    # AC1, AC3
#   bash <this> --walk <driver> <scratch-dir> <label>                     # AC2, AC4
#
# Run from the repository root. <driver> is an unattended.sh; the lib-unattended.sh beside it is
# used, else the tree's own. The driver's text up to its argument parser is copied with that library
# into <scratch-dir>/h-<label>/, the harness body at the end of this file is appended, and the copy
# runs from the root: every function is the driver's own and no verb runs. AREF and ASHA are taken
# from origin/main, so no network is read.
#
# --fields derives every tracked run record twice in one process, unprimed and then primed, and
# compares DP_PHASE DP_LANDING DP_AREF DP_TIP DP_REASON DP_BY field by field. Each primed arm prints
# one `primed` line: what the prime cached, how many git processes the primed walk started (GIT_TRACE),
# and how many batched calls were made to fail. The last line is
#   records=<N> landing=<L> held=<H> differences=<D>
# with L the records whose phase is LANDING and H those HELD under a hand-off code, both read by
# `fact`. It exits 1 when D is not 0, when N differs from `git ls-files` over the two run-record
# globs, when L is 0, or when an arm's liveness fails: the plain arm must cache phases, landing
# commits and ancestry and start NO git process in its walk, or it never read the cache.
# --fail-batch adds two arms under a `git` on PATH that exits 128 for one batched call, `diff
# --name-only` and then `rev-list`. Each must observe that failure, cache nothing for the step that
# failed, and start git in its walk, which is the old reading taking over.
# --walk runs check_single_live as preflight does for slug aBriskPreflight and prints its stdout;
# `cache=<n>`, the four DPC_ arrays' sizes summed, or `cache=absent` for a driver with none, goes to
# stderr.
#
# WHAT IT DOES NOT CHECK: a record shape this tree does not hold, since the population is today's;
# and a driver whose argument parser no longer opens with the marker line the cut keys on, which
# refuses rather than guessing.
set -u
mode=${1:-}; fail=""
[ "${2:-}" = --fail-batch ] && { fail=1; shift; }
drv=${2:-}; scr=${3:-}; label=${4:-}
case "$mode" in --fields|--walk) ;; *) mode="" ;; esac
if [ -z "$mode" ] || [ ! -f "$drv" ] || [ -z "$scr" ] || [ -z "$label" ]; then
  echo "usage: $0 --fields [--fail-batch] <driver> <scratch-dir> <label> | --walk <driver> <scratch-dir> <label>"; exit 2
fi
marker='^VERB=""; SLUG=""; KID=""'
grep -q "$marker" "$drv" || { echo "probe: $drv holds no argument-parser marker line, so no prologue can be cut from it"; exit 2; }
lib="$(dirname "$drv")/lib-unattended.sh"; [ -f "$lib" ] || lib=tools/unattended/lib-unattended.sh
# The shell's own spelling of the directory, since it goes onto PATH, where a drive colon splits it.
d="$scr/h-$label"
mkdir -p "$d" && d=$(cd "$d" && pwd) || exit 2
sed "/$marker/,\$d" "$drv" > "$d/unattended.sh"
cp "$lib" "$d/lib-unattended.sh"
sed -n '/^# ==== harness body/,$p' "$0" >> "$d/unattended.sh"
PROBE_ASHA=$(git rev-parse origin/main) || { echo "probe: origin/main does not resolve"; exit 2; }
PROBE_NLS=$(git ls-files ':(glob)memory/builds/*/RUN.md' ':(glob)memory/builds/*/RUN.*.md' | wc -l)
PROBE_GIT=$(command -v git)
export PROBE_MODE="$mode" PROBE_DIR="$d" PROBE_ASHA PROBE_NLS PROBE_GIT PROBE_ARMS="plain${fail:+ diff rev-list}" PROBE_FAIL=""
if [ -n "$fail" ]; then
  mkdir -p "$d/fakebin"
  printf '%s\n' '#!/bin/sh' \
    'case " $* " in *" $PROBE_FAIL "*) [ -n "$PROBE_FAIL" ] && { printf x >> "$PROBE_DIR/failed"; exit 128; } ;; esac' \
    'exec "$PROBE_GIT" "$@"' > "$d/fakebin/git"
  chmod +x "$d/fakebin/git"
fi
bash "$d/unattended.sh"
exit $?

# ==== harness body: appended after the driver's prologue by the lines above, never run from here
AREF=refs/heads/main; ASHA=$PROBE_ASHA
if [ "$PROBE_MODE" = --walk ]; then
  SLUG=aBriskPreflight
  check_single_live
  if declare -p DPC_PHASE >/dev/null 2>&1; then
    echo "cache=$(( ${#DPC_PHASE[@]} + ${#DPC_HOLD[@]} + ${#DPC_LANDING[@]} + ${#DPC_ANC[@]} ))" >&2
  else
    echo "cache=absent" >&2
  fi
  exit 0
fi
declare -p DPC_PHASE >/dev/null 2>&1 || { echo "probe: this driver has no DPC_ cache, so --fields has nothing to compare"; exit 2; }
pb_recs=(); pb_l=0; pb_h=0; pb_d=0; pb_bad=""
declare -A pb_u=()
for pb_f in $(GIT ls-files ":(glob)$M/builds/*/RUN.md" ":(glob)$M/builds/*/RUN.*.md" 2>/dev/null); do pb_recs+=("$pb_f"); done
for pb_f in "${pb_recs[@]}"; do
  read_derived_phase "$pb_f"
  pb_u[$pb_f]="$DP_PHASE|$DP_LANDING|$DP_AREF|$DP_TIP|$DP_REASON|$DP_BY"
  case "$(fact "$pb_f" phase)" in
    LANDING) pb_l=$((pb_l + 1)) ;;
    HELD) check_handoff_code "$(fact "$pb_f" hold-code)" && pb_h=$((pb_h + 1)) ;;
  esac
done
for pb_arm in $PROBE_ARMS; do
  case "$pb_arm" in
    diff) PATH="$PROBE_DIR/fakebin:$PATH"; hash -r; export PROBE_FAIL="diff --name-only" ;;
    rev-list) export PROBE_FAIL="rev-list" ;;
  esac
  rm -f "$PROBE_DIR/failed" "$PROBE_DIR/git-trace"
  read_derived_phase --prime "${pb_recs[@]}"
  pb_ln=0; for pb_k in "${!DPC_LANDING[@]}"; do [ -n "${DPC_LANDING[$pb_k]}" ] && pb_ln=$((pb_ln + 1)); done
  pb_cp=${#DPC_PHASE[@]}; pb_cl=${#DPC_LANDING[@]}; pb_ca=${#DPC_ANC[@]}
  export GIT_TRACE="$PROBE_DIR/git-trace"
  pb_ad=0
  for pb_f in "${pb_recs[@]}"; do
    read_derived_phase "$pb_f"
    pb_v="$DP_PHASE|$DP_LANDING|$DP_AREF|$DP_TIP|$DP_REASON|$DP_BY"
    [ "$pb_v" = "${pb_u[$pb_f]}" ] \
      || { pb_ad=$((pb_ad + 1)); printf 'DIFF %s %s: unprimed [%s] primed [%s]\n' "$pb_arm" "$pb_f" "${pb_u[$pb_f]}" "$pb_v"; }
  done
  unset GIT_TRACE
  pb_g=$(grep -c 'trace: built-in: git ' "$PROBE_DIR/git-trace" 2>/dev/null); pb_g=${pb_g:-0}
  pb_x=0; [ -f "$PROBE_DIR/failed" ] && pb_x=$(wc -c < "$PROBE_DIR/failed")
  pb_d=$((pb_d + pb_ad))
  printf 'primed %s: cached-phase=%d cached-landing=%d (non-empty %d) cached-anc=%d git-in-primed-walk=%d batch-failures=%d differences=%d\n' \
    "$pb_arm" "$pb_cp" "$pb_cl" "$pb_ln" "$pb_ca" "$pb_g" "$pb_x" "$pb_ad"
  case "$pb_arm" in
    plain) [ "$pb_cp" -gt 0 ] && [ "$pb_ln" -gt 0 ] && [ "$pb_ca" -gt 0 ] && [ "$pb_g" = 0 ] \
             || pb_bad="$pb_bad; the plain arm cached nothing for a step or started git in its walk" ;;
    diff) [ "$pb_x" -gt 0 ] && [ "$pb_cl" = 0 ] && [ "$pb_ca" = 0 ] && [ "$pb_g" -gt 0 ] \
            || pb_bad="$pb_bad; the diff arm did not fail its batch, cached a landing answer, or never fell back" ;;
    rev-list) [ "$pb_x" -gt 0 ] && [ "$pb_ca" = 0 ] && [ "$pb_ln" -gt 0 ] && [ "$pb_g" -gt 0 ] \
                || pb_bad="$pb_bad; the rev-list arm did not fail its batch, cached ancestry, or never fell back" ;;
  esac
done
read_derived_phase --prime
printf 'records=%d landing=%d held=%d differences=%d\n' "${#pb_recs[@]}" "$pb_l" "$pb_h" "$pb_d"
[ "${#pb_recs[@]}" = "$PROBE_NLS" ] || pb_bad="$pb_bad; records ${#pb_recs[@]} is not the ls-files count $PROBE_NLS"
[ "$pb_l" -gt 0 ] || pb_bad="$pb_bad; no LANDING record, so no derivation was exercised"
[ "$pb_d" = 0 ] || pb_bad="$pb_bad; $pb_d field difference(s)"
[ -z "$pb_bad" ] || { echo "RED${pb_bad}"; exit 1; }
echo "GREEN"
exit 0
