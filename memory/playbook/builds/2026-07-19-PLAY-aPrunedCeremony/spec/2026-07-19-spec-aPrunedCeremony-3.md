# PLAY-aPrunedCeremony-3 — recurring bug class: a ratchet that never exercises its target is vacuous

**Status:** OPEN · rev-1 · 2026-07-19 · node a · Tier-1 · base bf7f2c22

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

- Not adding a machine gate — this is a review-checklist class (a "vacuous gate" cannot, in general,
  be detected by another gate without the same regress; the mitigation is the review habit of
  injecting a violation).
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
- AC2 — When the memory-tree hygiene gate runs, `.domain-rules.md` stays within its size caps and
  the file passes.

## 8. Open questions

- **Fork — one combined entry or two (matcher-never-matches vs `--check`-always-unchanged)?**
  RECOMMEND: one entry with both as sub-forms — they share the fix (inject a violation, require a
  red), and §10 favors dense combined entries over proliferation.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
