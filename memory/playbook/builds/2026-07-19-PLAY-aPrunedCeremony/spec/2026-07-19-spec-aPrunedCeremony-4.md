# PLAY-aPrunedCeremony-4 — bookkeeping lands before the push, not after

**Status:** OPEN · rev-1 · 2026-07-19 · node a · Tier-1 · base bf7f2c22

## 1. Goal

Add the inCMS `ARCH-aTrimmedGauntlet-2` R3 rule to the playbook's Landing protocol: ledger rows,
decision/backlog updates, and spec-status flips are committed BEFORE `git push`, so the pushed range
carries its own bookkeeping — no trailing doc-only commit after a push. The template's DoD already
says bookkeeping lands "before the wrap-up message" (§1 L43); this closes the remaining gap — the
ordering relative to the PUSH, which is where the push-then-doc-commit anti-pattern actually happens.

## 2. Scope (IN)

- S1 — Add one bullet to template §1 "Landing — merge protocol" (L46-52): bookkeeping (ledger,
  decision log/backlog, spec-status flips) is committed before the push; the pushed range carries
  it; no trailing doc-only commit after a push.
- S2 — Cross-reference the existing DoD bullet (§1 L43, "on disk before the wrap-up message") so the
  two read as one rule (bookkeeping before both the push AND the wrap-up), not two.

## 3. Non-goals (OUT)

- Not changing WHAT bookkeeping is required (that is the DoD, §1 L38-44) — only its ordering vs the
  push.
- Not addressing the gate-red-blocked-push case's ledger status here — that interacts with the
  `pushed:<sha>` vocab (template §3 L87-88), which is out of the six; if a push is blocked the row
  simply stays at its pre-push status, which the existing self-prune (§3 L88) already tolerates.

## 4. Design

### Inventory

| Edit site | Change |
|-----------|--------|
| template §1 Landing (after L48 or L51) | Add the bookkeeping-before-push bullet (S1). |
| template §1 DoD L43 | Add "before the push" alongside "before the wrap-up message" (S2). |

Proposed Landing bullet:

```
- Bookkeeping lands BEFORE the push: ledger rows, decision-log/backlog entries, and spec-status
  flips are committed in (or before) the pushed range, so it carries its own record — never a
  trailing doc-only commit after `git push` (the next node pulls a push whose docs describe it).
```

### Alternatives rejected

- **Rely on the DoD "before the wrap-up message" line alone.** Rejected: "before the wrap-up
  message" bounds the bookkeeping against the CHAT turn, not the push — a session can legitimately
  push, then write the ledger before its final message, which is exactly the push-then-doc-commit
  the rule forbids. The push is the boundary that matters.

## 6. Acceptance criteria

- AC1 — When template §1 Landing is read, it states bookkeeping is committed before the push and
  bans a trailing doc-only commit after a push.
- AC2 — When §1 DoD L43 and the new Landing bullet are read together, they name one coherent rule
  (bookkeeping before the push and before the wrap-up), not two competing deadlines.
- AC3 — When `check-template-size.sh` runs, it stays green (≤32 KiB).

## 8. Open questions

- **Fork — put the rule in DoD (L43) or Landing (L46-52)?** RECOMMEND: Landing, because the push is
  a landing action; add only a half-clause to the DoD line pointing at it, to avoid duplicating the
  rule in two sections (which would itself drift).

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
