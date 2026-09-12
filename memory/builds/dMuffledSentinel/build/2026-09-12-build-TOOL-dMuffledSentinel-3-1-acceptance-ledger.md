# Acceptance ledger — TOOL-dMuffledSentinel-3

**Serves:** journal TOOL-dMuffledSentinel-3

Tier-1 · node d · 2026-09-12

## Why it exists

inCMS pulled `TOOL-dMuffledSentinel-2` and its `kit-versions` leg refused the pull. Bytes of both kits
had moved while `KIT_DRIFT_AUDIT_VERSION` stayed at 1.9 and `KIT_UNATTENDED_VERSION` at 1.18. This
repo's own `kit version markers` leg had passed unit 2, because it grades whether the carriers agree
with each other, never whether a version moved with its bytes. inCMS's leg asks the second question.

## The criteria

**Evidences:** TOOL-dMuffledSentinel-3

- AC1 — MET, OBSERVED — `tools/check-kit-versions.sh` exits 0 with every drift-audit carrier at 1.10.
  Its first run after the stamps alone was rc 1, naming both drift workflows' `meta.version`, which a
  stamp pattern does not reach. That run is what found them.
- AC2 — MET, OBSERVED — the same run holds all four `KIT_UNATTENDED_VERSION` lines and every template
  stamp at 1.19.
- AC3 — MET, OBSERVED — `bash tools/unattended/adopt-unattended.sh --check` exits 0 once the adopt
  script re-made the skill, protocol, verbs and playbook-template copies.

`check-unattended.sh` carries four deliberate lone CR bytes. They are the same four before and after,
and its diff is the version line alone.

## Residue

Nothing in this repo makes a kit's version move with its bytes. Only memory-tree has such a rule, its
verdict epoch. That is why unit 2 could land without a bump, and why an adopter found it rather than
this bar.
