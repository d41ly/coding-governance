# PLAY-aPrunedCeremony-3 — recurring bug class: a ratchet that never exercises its target is vacuous

**Status:** CLOSED · rev-2 · 2026-07-19 · node a · Tier-1 · base bf7f2c22 · reviewed wf_2f11fd07 · ratified 2026-07-19

## 1. Goal

Add one recurring-bug-class entry to `.domain-rules.md` §10, generalized from two inCMS
`ARCH-aTrimmedGauntlet-2` review catches: a coverage/parity ratchet whose matcher never matches the
real code idiom (it greps a literal path the code builds segment-by-segment) matches nothing and
passes while checking nothing; and a `--check` freshness gate whose correct output is always
"unchanged" on every machine asserts nothing. The rule: prove a gate CATCHES an injected regression,
never trust that it is green.

## 2. Scope (IN)

- S1 — Add one bullet to `.domain-rules.md` §10 (Recurring bug classes), in the existing dense
  one-sentence-plus-fix house style, placed near the other test/gate-integrity entries (§10 L47,
  L53-54).

## 3. Non-goals (OUT)

- Not adding a machine gate at the kit level — coding-governance ships docs, not the downstream
  project's CI, so no single kit gate covers the general class; it lands as a review-checklist class
  here. Note the class is only PARTLY ungateable: the "gate a non-empty selection" sub-form IS
  cheaply machine-checkable in a concrete project (assert the selection the ratchet iterates is
  non-empty), which is the fix the entry itself prescribes (review R-PLAY-3-LOW).
- Not restating §10's existing "verify the COMPUTED value" (L47) or "documented checks" (L53-54)
  entries — this class is distinct: the GATE ITSELF is inert, not the value under test.

## 4. Design

### Inventory

| Edit site | Change |
|-----------|--------|
| `.domain-rules.md` §10 (after L47 or near L53) | Add the vacuous-ratchet bullet (S1). |

Proposed entry (house style — one dense sentence + the fix):

```
- A ratchet/parity gate that never exercises its target is vacuous and reads as coverage: a
  coverage check that greps for a literal (a path, a symbol) the real code never spells because it
  builds it segment-by-segment matches the empty set and passes checking nothing; a `--check`
  freshness gate whose correct output is "unchanged" on every machine that runs it asserts nothing.
  Prove the gate CATCHES an injected regression (feed it a synthetic violation → it must red), and
  gate a non-empty selection, never trust a green.
```

### Alternatives rejected

- **Fold into the existing L47 "verify the COMPUTED value" entry.** Rejected: that entry is about
  the VALUE resolving to nothing; this is about the CHECK resolving to nothing. Different failure,
  different fix (inject-and-confirm-red vs measure-the-rendered-value).

## 6. Acceptance criteria

- AC1 — When `.domain-rules.md` §10 is read, it contains a class covering both the never-matching
  matcher and the always-"unchanged" `--check` gate, with the "prove it catches an injected
  regression" fix.
- AC2 — `.domain-rules.md` has NO machine size cap and is not scanned by the memory-tree hygiene
  gate (which scans only `memory/**`) nor by `check-template-size.sh` (which caps only the template);
  it is the template's designated overflow companion. Acceptance is therefore a read confirming the
  new class is present, distinct from the L47 "verify the COMPUTED value" entry, and fits the §10
  house style — not a gate pass (review R-PLAY-3-MED).

## 8. Open questions

none — the fork below is RESOLVED (owner-ratified 2026-07-19); kept for the record.

- **Fork — one combined entry or two (matcher-never-matches vs `--check`-always-unchanged)?**
  RESOLVED (2026-07-19): built as recommended — one entry with both as sub-forms — they share the fix (inject a violation, require a
  red), and §10 favors dense combined entries over proliferation.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
- rev-2 · 2026-07-19 · folded review wf_2f11fd07: corrected AC2 (domain-rules has no machine size cap
  and the memory-tree gate does not scan it; acceptance is a manual read); softened the §3
  "cannot be detected by another gate" over-claim (the non-empty-selection sub-form is gateable);
  status → SPECCED.
