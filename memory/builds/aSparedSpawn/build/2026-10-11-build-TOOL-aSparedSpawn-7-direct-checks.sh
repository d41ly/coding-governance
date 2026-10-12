#!/usr/bin/env bash
# TOOL-aSparedSpawn-7 - the pass's direct checks of the two `--only` selectors, over HAND-BUILT fixture
# repositories in a scratch root, never over this tree. No suite and no slice of one.
#
#   bash <this> probe <unattended-fixture> <sel>...        # rc, liveness line and any unbound read per selector
#   bash <this> partition <unattended-fixture> <parent-leg> # unscoped bytes vs the parent, and the partition
#   bash <this> hpartition <hygiene-fixture>                # the hygiene gate's partition
#
# A fixture is a `git init` holding the kit under tools/ (tools/unattended/ with this tree's
# .unattended.conf, or tools/memory-tree/ with a three-key .memory-tree.conf and a memory/ tree). The
# PARTITION is AC8's shape: the SET of lines the unscoped run prints equals the union of the lines the
# scoped runs print over every selection, liveness lines set aside. It reads stdout and stderr for the
# unattended leg, stdout alone for the hygiene gate, whose notices go to stderr by design.
set -u
mode=${1:?usage: direct-checks.sh probe|partition|hpartition <fixture> ...}; FX=${2:?fixture}; shift 2
cd "$FX" || exit 2
L=tools/unattended/check-unattended.sh
H=tools/memory-tree/check-memory-hygiene.sh
case "$mode" in
  probe)
    for sel in "$@"; do
      out=$(GOV_UNATTENDED_REPORT=1 bash "$L" --only "$sel" 2>&1); rc=$?
      printf '== --only %s rc=%s\n' "$sel" "$rc"
      printf '%s\n' "$out" | grep -E '^check-unattended: |unbound variable|command not found|^UNATTENDED check' | cut -c1-220
    done ;;
  partition)
    # the parent copy sits beside the leg so it resolves the same kit; its own check 36 then sees it,
    # which is the one line the comparison below is expected to differ by
    cp "${1:?parent leg}" tools/unattended/check-unattended-base.sh
    bash tools/unattended/check-unattended-base.sh > ../p.base 2>&1; echo "base rc=$?"
    rm -f tools/unattended/check-unattended-base.sh
    bash "$L" > ../p.cut 2>&1; echo "cut rc=$?"
    diff ../p.base ../p.cut | cut -c1-200
    : > ../p.union
    for sel in core 28 30 31 32 33 39 40 15 41 42 43 47 48 49 50 51; do
      bash "$L" --only "$sel" > ../p.one 2>&1; rc=$?
      printf -- '--only %s rc=%s liveness lines: %s\n' "$sel" "$rc" "$(grep -c '^check-unattended: --only ' ../p.one)"
      grep -v '^check-unattended: --only ' ../p.one >> ../p.union
    done
    sort -u ../p.cut > ../p.cut.s; sort -u ../p.union > ../p.union.s
    if cmp -s ../p.cut.s ../p.union.s; then echo "partition: EQUAL ($(grep -c . ../p.cut.s) distinct lines)"; else echo "partition: DIFFER"; diff ../p.cut.s ../p.union.s | cut -c1-200; fi ;;
  hpartition)
    bash "$H" > ../h.whole 2>/dev/null; echo "unscoped rc=$?"
    : > ../h.union
    for s in 1 2 3 4 5 6 9 10 11 12 13 17 20 21 22 23 24 26 27 28; do
      bash "$H" --only "$s" > ../h.one 2>/dev/null; rc=$?
      printf -- '--only %s rc=%s %s\n' "$s" "$rc" "$(grep '^HYGIENE --only ' ../h.one)"
      grep -v '^HYGIENE --only ' ../h.one >> ../h.union
    done
    sort -u ../h.whole > ../h.whole.s; sort -u ../h.union > ../h.union.s
    if cmp -s ../h.whole.s ../h.union.s; then echo "partition: EQUAL ($(grep -c . ../h.whole.s) distinct lines)"; else echo "partition: DIFFER"; diff ../h.whole.s ../h.union.s | cut -c1-200; fi ;;
  *) echo "direct-checks: unknown mode '$mode'"; exit 2 ;;
esac
