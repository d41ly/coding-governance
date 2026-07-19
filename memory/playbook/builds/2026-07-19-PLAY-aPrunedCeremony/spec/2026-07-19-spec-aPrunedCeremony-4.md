# PLAY-aPrunedCeremony-4 — bookkeeping lands before the push, not after

**Status:** SPECCED · rev-2 · 2026-07-19 · node a · Tier-1 · base bf7f2c22 · reviewed wf_2f11fd07

## 1. Goal

Add the inCMS `ARCH-aTrimmedGauntlet-2` R3 rule to the playbook's Landing protocol: ledger rows,
decision/backlog updates, and spec-status flips are committed BEFORE `git push`, so the pushed range
carries its own bookkeeping — no trailing doc-only commit after a push. The template's DoD already
says bookkeeping lands "before the wrap-up message" (§1 L43); this closes the remaining gap — the
ordering relative to the PUSH.

## 2. Scope (IN)

- S1 — Extend the existing template §1 DoD line 43 (`… on disk before the wrap-up message (§16).`)
  IN PLACE with the push ordering — "committed before the push AND the wrap-up message" — a
  byte-neutral extension of an existing line, NOT a new bullet (the template has 86 bytes of headroom
  under a hard gate; review R-PLAY-4-HIGH).
- S2 — If a Landing-section statement is also wanted, fold a ≤~40-byte clause onto the existing
  Landing line 47, dropping any parenthetical; re-measure `check-template-size.sh` after. Any fuller
  rationale goes to `.domain-rules.md`, never as net template bytes.

## 3. Non-goals (OUT)

- Not changing WHAT bookkeeping is required (that is the DoD, §1 L38-44) — only its ordering vs the
  push.
- Not adding net template bytes — S1/S2 are in-place extensions of existing lines (§4 Rollout).
- Not unilaterally retiring `pushed:<sha>` — but the interaction with it is no longer ignored; it is
  raised as a coupled fork (§8 Fork B, review R-PLAY-4-LOW).

## 4. Design

### Inventory

| Edit site | Current text (verified live) | Change | Byte effect |
|-----------|------------------------------|--------|-------------|
| template §1 DoD L43 | "… updated — **on disk before the wrap-up message** (§16)." | Extend: "on disk and committed before the push and the wrap-up message" (S1). | small; re-measure |
| template §1 Landing L47 (optional) | existing Landing bullet | Fold a ≤40-byte "bookkeeping before the push" clause (S2). | ≈0 |

The rev-1 spec proposed a NEW 289-byte Landing bullet, which busts the ≤32 KiB gate (wf_2f11fd07).
rev-2 extends existing lines in place instead.

### Alternatives rejected

- **Add a new Landing bullet (rev-1).** Rejected: +289 bytes over an 86-byte headroom busts the hard
  size gate. Extend the existing DoD line in place.
- **Rely on the DoD "before the wrap-up message" line alone.** Rejected: it bounds bookkeeping
  against the CHAT turn, not the push — a session can push, then write the ledger before its final
  message, which is exactly the push-then-doc-commit the rule forbids. The push is the boundary that
  matters.

## 6. Acceptance criteria

- AC1 — When template §1 DoD L43 is read after this change, it states bookkeeping is committed before
  the push (and the wrap-up message), and no separate Landing rule contradicts it.
- AC2 — When `bash tools/check-template-size.sh` runs after the edit, it exits 0 (≤ 32768) — proven
  by measurement; the in-place extensions keep the file within budget.
- AC3 — When the DoD line and any Landing clause are read together, they name ONE coherent rule (no
  two competing deadlines).

## 8. Open questions

- **Fork A — DoD line vs a Landing clause.** RECOMMEND: extend the DoD line (S1) as the single home,
  since it already owns bookkeeping timing; add a Landing clause only if a lander would miss the DoD
  line. Avoid stating the rule in two places (the two-copies-drift class).
- **Fork B — the coupled `pushed:<sha>` interaction (review R-PLAY-4-LOW).** The template §3 keeps
  `pushed:<sha>` in the ledger vocab (L87) and a self-prune keyed on it (L88); a `pushed:<sha>` row
  requires a write AFTER the push, which tensions with "no trailing doc-only commit after `git
  push`". Two coherent resolutions: (a) retire `pushed:<sha>` here — vocab → `{in-flight |
  merged:<sha>}`, self-prune on `merged:<sha>` ancestry — matching the inCMS Q4 change and deriving
  push-state from git; or (b) keep `pushed:<sha>` and define the row as riding at `merged` in the
  pushed range, flipping to `pushed:<sha>` only as sanctioned next-push bookkeeping (never a
  standalone post-push commit). RECOMMEND (a) — it removes derivable state and the contradiction in
  one move — but it edits template §3, which was out of the original six, so it needs owner sign-off
  before folding into this spec's scope.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
- rev-2 · 2026-07-19 · folded review wf_2f11fd07: template ≤32 KiB budget (extend DoD L43 in place,
  not a new bullet; AC2 now measures); raised the coupled `pushed:<sha>` interaction as §8 Fork B
  rather than leaving the contradiction; status → SPECCED.
