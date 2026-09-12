#!/usr/bin/env bash
# **Serves:** journal TOOL-dMuffledSentinel-2
# TOOL-dMuffledSentinel-2 — a probe for PASS_ORDER_WAIVER, over a throwaway clone of THIS tree.
#
# WHY A PROBE AND NOT SUITE ARMS. `tools/unattended/`'s self-test suites carry a standing owner
# instruction not to be run, and an arm nobody may run is an assertion nobody has observed. This
# drives the REAL leg, `tools/unattended/check-pass-order.sh`, over a --shared clone of the ref it is
# given, where the leg grades real history against the real registry. It asserts four outcomes, one
# of them a precondition, and it is the acceptance evidence for AC1, AC2 and AC3.
#
#   bash <this file> [<ref>]    # default HEAD; pass the ref before the change to watch AC1 and AC3 red
#
# Each run of the leg walks the whole history, so the probe costs about four leg runs of wall clock.
set -u
REF=${1:-HEAD}
SRC=$(git rev-parse --show-toplevel) || exit 2
SHA=$(git -C "$SRC" rev-parse --verify "$REF^{commit}") || { echo "probe: $REF is not a commit"; exit 2; }
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT
git clone -q --shared --no-checkout "$SRC" "$T/r" || exit 2
cd "$T/r" || exit 2
git config user.email probe@local
git config user.name probe
git config core.autocrlf false
git checkout -q "$SHA" || exit 2

REG=memory/project/pass-order-waiver.txt
[ -f "$REG" ] || { echo "probe: $REG is absent at $REF, so there is nothing to relocate"; exit 2; }
# The rows the shipped registry carries: every one must stay waived through the relocation.
n0=$(grep -cvE '^[[:space:]]*(#|$)' "$REG")
[ "$n0" -gt 0 ] || { echo "probe: $REG carries no rows, so every arm below would pass vacuously"; exit 2; }

fail=0
check_leg() {   # $1 = name, $2 = the exit status wanted, $3 = a fixed string the output must carry
  bash tools/unattended/check-pass-order.sh > "$T/out" 2>&1
  rc=$?
  if [ "$rc" = "$2" ] && grep -qF -- "$3" "$T/out"; then
    echo "ok   $1"
  else
    echo "FAIL $1 (rc=$rc, wanted $2 and: $3)"
    tail -n 4 "$T/out" | sed 's/^/       /'
    fail=1
  fi
}

check_leg "AC2 — the default registry waives its $n0 row(s) with the key blank" 0 \
  "$n0 waived by $REG"

mkdir -p probe
git mv "$REG" probe/pass-order-waiver.txt
git commit -q -m "probe: the registry leaves memory/project/" --no-verify
check_leg "precondition — relocated with no key, the default path is empty and the units red" 1 \
  "0 waived by $REG"

printf '\nPASS_ORDER_WAIVER="probe/pass-order-waiver.txt"\n' >> .unattended.conf
check_leg "AC1 — PASS_ORDER_WAIVER reads the registry where it is declared" 0 \
  "$n0 waived by probe/pass-order-waiver.txt"

sed -i 's|^PASS_ORDER_WAIVER=.*|PASS_ORDER_WAIVER="probe/absent.txt"|' .unattended.conf
check_leg "AC3 — a declared registry not tracked at HEAD refuses and names the key" 2 \
  "PASS_ORDER_WAIVER names probe/absent.txt"

[ "$fail" = 0 ] && echo "probe: PASS at $SHA" || echo "probe: FAILED at $SHA"
exit "$fail"
