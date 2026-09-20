# Acceptance ledger — TOOL-dMuffledSentinel-2

**Serves:** journal TOOL-dMuffledSentinel-2

Tier-1 · node d · 2026-09-12

## Why it exists

Closing inCMS's `ARCH-dMuffledSentinel-1` ran into both legs this unit touches, and both findings were
true: the spec was written after the code, and the whole change is tooling outside `PRODUCT_GLOBS`.
Each leg waives only from `<MEMORY_ROOT>/project/`, which inCMS retired, and whose hygiene gate
refuses one. inCMS's owner chose to fix that here rather than re-open the directory there.

## Order

The spec went in first, at `0f259923`, and the build at `dc02dfcd` sits directly on it. So this
unit's own `pass-order history` grade has a spec at its build commit's parent, which unit 1's did not.

## The criteria

**Evidences:** TOOL-dMuffledSentinel-2

- AC1 — MET, OBSERVED — `2026-09-12-build-TOOL-dMuffledSentinel-2-1-pass-order-probe.sh` moves this
  tree's registry out of `memory/project/`, declares `PASS_ORDER_WAIVER`, and the real leg reports
  all 3 rows waived from the new path. At the spec commit, with the old leg, the same step is rc 1.
- AC2 — MET, OBSERVED — the same probe's first run, key blank, reports the 3 rows waived from the
  default path, at both refs.
- AC3 — MET, OBSERVED — a declared `probe/absent.txt` exits 2 with `PASS_ORDER_WAIVER names
  probe/absent.txt`. The old leg exits 1 there instead, having read the absent file as no waivers.
- AC4 — MET, OBSERVED BY STAGED BREAK — `tools/drift-audit/selftest.py` relocates its registry and
  declares `TRACE_WAIVER`, and the waived spec is silent. With `drift_report.py` swapped back to
  its committed bytes, that arm and both below it fail and nothing else does.
- AC5 — MET, OBSERVED — a declared path that is absent, and one that climbs out with `..`, each come
  back as a `(declared TRACE_WAIVER)` row beside the spec it failed to waive.

A precondition runs before the key arms in both places. Relocated with no key, the spec fires in the
suite and the units red in the probe. Without it, a key arm over something already silent would
pass whatever the engine did.

## What the bar found

`unattended kit gate` check 22 redded the first cut: the protocol's binding key table must document
every conf key, and `PASS_ORDER_WAIVER` was not in it. The row is added and the copy re-made with
the kit's adopt script. The check-23 lines that the same leg prints were a red herring: they print at
exit 0 on `main` too.

## Residue

The unattended dossier sits at its byte cap, so the seam note that belongs under its reuse
affordance was not added: one more line reds check 6, and the remedy is a dossier split. The note
is here instead. `PASS_ORDER_WAIVER` is the pattern for any registry an adopter must house outside
`<MEMORY_ROOT>/project/`: blank keeps the kit path, and a declared path must resolve.

Otherwise none here. inCMS declares both keys and closes `ARCH-dMuffledSentinel-1` after its next pull.
