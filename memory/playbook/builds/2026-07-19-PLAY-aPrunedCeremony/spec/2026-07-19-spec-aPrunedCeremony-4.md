# PLAY-aPrunedCeremony-4 — bookkeeping lands before the push; retire the derivable `pushed:<sha>`

**Status:** INPROGRESS · rev-3 · 2026-07-19 · node a · Tier-2 · base bf7f2c22 · reviewed wf_2f11fd07 · ratified 2026-07-19

## 1. Goal

Two coupled ledger-hygiene changes from inCMS `ARCH-aTrimmedGauntlet-2`. (1) R3: bookkeeping (ledger
rows, decision/backlog, spec-status flips) is committed BEFORE `git push`, so the pushed range
carries its own record — no trailing doc-only commit after a push. (2) Retire the `pushed:<sha>`
ledger status (owner-ratified Fork B option a): push-state is derivable from git ancestry, so the
vocab collapses to `{in-flight | merged:<sha>}` and the self-prune keys on `merged:<sha>`. Retiring
`pushed:<sha>` also removes the only post-push write the R3 rule would otherwise contradict, so the
two changes are one coherent unit.

## 2. Scope (IN)

- S1 — Extend template §1 DoD line 43 (`… on disk before the wrap-up message (§16).`) IN PLACE:
  "committed before the push AND the wrap-up message". Byte-neutral-ish extension of an existing
  line (the template has 86 bytes headroom; retiring `pushed:<sha>` in S2 frees ~14 bytes to offset
  it — net must stay ≤ 32768, re-measured).
- S2 — Retire `pushed:<sha>` from the ledger status vocabulary at EVERY live site (archive snapshots
  under `memory/playbook/archive/**` are frozen — never edited):
  - `parallel-coding-governance.template.md` §3 L87 (`{in-flight | merged | pushed:<sha>}` →
    `{in-flight | merged:<sha>}`) and L88 (self-prune `pushed:/merged:<sha>` → `merged:<sha>`).
  - `memory/HYGIENE.md` L66 AND its generator source `tools/memory-tree/HYGIENE.template.md` L66
    (single source → generated; edit both or the kit ships drift).
  - `memory/project/IN-FLIGHT.md` L3 (the ledger pointer-stub vocab + self-prune sentence).
  - `WIRE-INTO-PROJECT.md` L134 (the adopter runbook).
- S3 — Migrate node `a`'s OWN ledger rows (`memory/project/in-flight/a.md`) from any `pushed:<sha>`
  to `merged:<sha>`. Do NOT edit `memory/project/in-flight/b.md` (write-only-your-own, template §3
  L86) — node b migrates its own header; record a backlog follow-up (`PLAY-aPrunedCeremony`-tagged)
  so it is tracked, mirroring inCMS RD19.

## 3. Non-goals (OUT)

- Not changing WHAT bookkeeping is required (DoD §1 L38-44) — only its ordering vs the push.
- Not editing archive snapshots (`memory/playbook/archive/*.md`) — they are frozen version records.
- Not editing node b's ledger file — its `pushed:` rows are node b's to migrate (S3); leaving them
  transiently is the same disjoint-ledger pattern the kit already relies on.

## 4. Design

### Data model

Ledger status vocabulary: `{in-flight | merged | pushed:<sha>}` → `{in-flight | merged:<sha>}`.
`merged:<sha>` already carries the sha, so the self-prune (`git merge-base --is-ancestor <sha>
main`) still works; `pushed:<sha>` added nothing derivable — push-state is `<sha> ancestor of the
pushed default branch`.

### Inventory

| Edit site | Change | Byte effect |
|-----------|--------|-------------|
| template §1 DoD L43 | extend: "committed before the push and the wrap-up message" | +~25 |
| template §3 L87 | drop `\| pushed:<sha>`, `merged` → `merged:<sha>` | −~6 |
| template §3 L88 | self-prune `pushed:/merged:<sha>` → `merged:<sha>` | −~10 |
| `memory/HYGIENE.md` L66 + `tools/memory-tree/HYGIENE.template.md` L66 | vocab drop `pushed:<sha>` | uncapped |
| `memory/project/IN-FLIGHT.md` L3 | vocab + self-prune drop | uncapped |
| `WIRE-INTO-PROJECT.md` L134 | self-prune wording drop | uncapped |
| `memory/project/in-flight/a.md` | migrate node-a rows to `merged:<sha>` | uncapped |

Net template bytes: +25 (DoD) −16 (vocab) = ~+9; the current file has 86 bytes headroom → still ≤
32768, but MUST be re-measured (`check-template-size.sh`) and, if over, the DoD clause compressed.

### Migration

The vocab change is backward-tolerant: a stale `pushed:<sha>` row still self-prunes (its sha is an
ancestor once pushed), so node b's un-migrated rows are harmless until node b's next session. No data
migration beyond the in-place ledger edits.

### Rollout

Doc-only; lands on `main`. Re-measure the template gate after S1+S2.

### Files touched (estimate)

7 files. Template net ~+9 bytes (must verify ≤ 32768).

### Alternatives rejected

- **Keep `pushed:<sha>`, define it as a sanctioned post-push write (Fork B option b).** Rejected by
  owner ratification: option a (retire) removes derivable state AND the R3 contradiction in one move.
- **Edit HYGIENE.md only, not its template.** Rejected: `tools/memory-tree/HYGIENE.template.md` is
  the generator source; editing one is the hand-kept-copy-drift class the kit gates elsewhere.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y / i18n — N/A.
- error / empty / loading states — N/A.
- observability — N/A.
- risks — node b's un-migrated `pushed:` rows are a transient cosmetic mismatch, self-healing via
  prune; the write-only-your-own rule forbids fixing them here (S3).
- testing + left-shift gates — no machine gate asserts the ledger vocab; the memory-tree hygiene gate
  status-vocabulary check (check 8) governs BACKLOG/STATUS rows, not the in-flight ledger prose, so
  no gate reds on the change (verify at build). Template ≤32 KiB is the one gate to re-run.
- migration / rollback — revert the edits; vocab is backward-tolerant.
- user docs — `WIRE-INTO-PROJECT.md` is the adopter doc, updated in S2.

## 6. Acceptance criteria

- AC1 — When template §1 DoD L43 is read, it states bookkeeping is committed before the push and the
  wrap-up message.
- AC2 — When `grep -rn "pushed:<sha>"` over the five live vocab files (template, HYGIENE.md,
  HYGIENE.template.md, IN-FLIGHT.md, WIRE-INTO-PROJECT.md) runs, it returns nothing (archives
  excluded).
- AC3 — When `bash tools/check-template-size.sh` runs after the edits, it exits 0 (≤ 32768) — proven
  by measurement.
- AC4 — When `bash tools/run-gates.sh` runs, the memory-tree hygiene gate stays green (the vocab
  change touches no gated check).

## 7. Gates

`tools/check-template-size.sh` (re-run, ≤32 KiB), the memory-tree hygiene gate (unaffected — verify),
`check-kit-versions.sh` (unaffected). No new gate.

## 8. Open questions

- **Fork A — DoD line vs a Landing clause.** RESOLVED (owner, 2026-07-19): the DoD line is the single
  home; no separate Landing bullet (avoids the two-copies-drift class).
- **Fork B — retire `pushed:<sha>` or keep it as a sanctioned post-push write.** RESOLVED (owner,
  2026-07-19): option a — RETIRE it (vocab → `{in-flight | merged:<sha>}`).

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
- rev-2 · 2026-07-19 · folded review wf_2f11fd07: in-place DoD extension (template budget); raised the
  `pushed:<sha>` interaction as Fork B.
- rev-3 · 2026-07-19 · owner ratified Fork B option a (retire `pushed:<sha>`) — expanded S2 to the
  full live-site inventory (template §3, HYGIENE.md + its template source, IN-FLIGHT.md,
  WIRE-INTO-PROJECT.md) + node-a row migration (b.md left per write-only-your-own → backlog); status
  → INPROGRESS.
