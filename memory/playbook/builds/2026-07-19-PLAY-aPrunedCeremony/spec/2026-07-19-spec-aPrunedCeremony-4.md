# PLAY-aPrunedCeremony-4 — bookkeeping lands before the push; retire the derivable `pushed:<sha>`

**Status:** INPROGRESS · rev-4 · 2026-07-19 · node a · Tier-2 · base bf7f2c22 · reviewed wf_2f11fd07,wf_539c5419 · ratified 2026-07-19

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
  "committed before the push AND the wrap-up message". The template has 86 bytes headroom; retiring
  `pushed:<sha>` in S2 frees bytes to offset it — net must stay ≤ 32768, re-measured.
- S2 — Retire `pushed:<sha>` from the ledger status vocabulary at EVERY live site, INCLUDING the
  generators (archive snapshots under `memory/playbook/archive/**` and the two aPrunedCeremony build
  folders are excluded — frozen / self-referential):
  - `parallel-coding-governance.template.md` §3 L87 (`{in-flight | merged | pushed:<sha>}` →
    `{in-flight | merged:<sha>}`) and L88 (self-prune `pushed:/merged:<sha>` → `merged:<sha>`).
  - `memory/HYGIENE.md` L66 AND its generator source `tools/memory-tree/HYGIENE.template.md` L66.
  - `memory/project/IN-FLIGHT.md` L3 (vocab + self-prune) AND its GENERATOR
    `tools/memory-tree/adopt-memory-tree.sh` L50 — the printf that scaffolds IN-FLIGHT.md into every
    new adopter (review wf_539c5419 PLAY-4-HIGH; omitting it resurrects the retired vocab on the next
    `--scaffold`, the same generator→artifact drift the spec rejects for HYGIENE).
  - `WIRE-INTO-PROJECT.md` L134 (self-prune wording).
- S3 — Migrate node `a`'s OWN ledger rows (`memory/project/in-flight/a.md`) to the new vocab. The
  live rows use a BARE `merged` token (no sha, e.g. `**merged** (direct commit on main, NOT
  pushed)`), which the new `{in-flight | merged:<sha>}` vocab makes non-conforming — so migrate bare
  `merged` → `merged:<sha>` citing the landing/commit sha (so the self-prune's `git merge-base
  --is-ancestor <sha> main` works). Do NOT edit `memory/project/in-flight/b.md` (write-only-your-own,
  template §3 L86) — node b migrates its own bare-`merged` rows; record a backlog follow-up so it is
  tracked (inCMS RD19).
- S4 — Because S2 edits kit-shipped content (`adopt-memory-tree.sh`, `HYGIENE.template.md`), bump the
  memory-tree kit version: `KIT_MEMORY_TREE_VERSION` in `tools/memory-tree/check-memory-hygiene.sh`
  L13 (1.2 → 1.3) AND the `gov:kit memory-tree@` marker in `HYGIENE.template.md` L1, which
  `check-kit-versions.sh` L31 asserts must agree.

## 3. Non-goals (OUT)

- Not changing WHAT bookkeeping is required (DoD §1 L38-44) — only its ordering vs the push.
- Not editing archive snapshots (`memory/playbook/archive/*.md`) — frozen version records.
- Not editing node b's ledger file — its bare-`merged` rows are node b's to migrate (S3); leaving
  them transiently is the disjoint-ledger pattern the kit already relies on.

## 4. Design

### Data model

Ledger status vocabulary: `{in-flight | merged | pushed:<sha>}` → `{in-flight | merged:<sha>}`. Both
the bare `merged` and `pushed:<sha>` tokens are retired in favor of `merged:<sha>`, which carries the
sha the self-prune (`git merge-base --is-ancestor <sha> main`) needs. `pushed:<sha>` added nothing
derivable — push-state is `<sha> ancestor of the pushed default branch`.

### Inventory

| Edit site | Change | Byte effect |
|-----------|--------|-------------|
| template §1 DoD L43 | extend: "committed before the push and the wrap-up message" | +~25 |
| template §3 L87 | drop `\| pushed:<sha>`, `merged` → `merged:<sha>` | −~6 |
| template §3 L88 | self-prune `pushed:/merged:<sha>` → `merged:<sha>` | −~10 |
| `memory/HYGIENE.md` L66 + `tools/memory-tree/HYGIENE.template.md` L66 | vocab drop | uncapped |
| `memory/project/IN-FLIGHT.md` L3 + `tools/memory-tree/adopt-memory-tree.sh` L50 (generator) | vocab + self-prune drop | uncapped |
| `WIRE-INTO-PROJECT.md` L134 | self-prune wording | uncapped |
| `memory/project/in-flight/a.md` | bare `merged` → `merged:<sha>` (node-a rows) | uncapped |
| `check-memory-hygiene.sh` L13 + `HYGIENE.template.md` L1 marker | kit version 1.2 → 1.3 | uncapped |

Net template bytes: +25 (DoD) −16 (vocab) = ~+9; re-measure `check-template-size.sh` and, if over,
compress the DoD clause.

### Migration

The vocab change is backward-tolerant for the self-prune (a stale `pushed:<sha>` or bare `merged`
row still resolves an ancestor sha where one is cited), so node b's un-migrated rows are harmless
until node b's next session.

### Rollout

Doc-only; lands on `main`. Re-measure the template gate after S1+S2; run `check-kit-versions.sh`
after S4.

### Files touched (estimate)

9 files. Template net ~+9 bytes (verify ≤ 32768).

### Alternatives rejected

- **Keep `pushed:<sha>` as a sanctioned post-push write (Fork B option b).** Rejected by owner
  ratification: option a removes derivable state AND the R3 contradiction in one move.
- **Edit each artifact but not its generator.** Rejected: `HYGIENE.template.md` and
  `adopt-memory-tree.sh` are the generator sources; editing the artifact alone is the
  hand-kept-copy-drift class the kit gates elsewhere — and the next `--scaffold` overwrites the fix.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y / i18n — N/A.
- error / empty / loading states — N/A.
- observability — N/A.
- risks — node b's un-migrated bare-`merged` rows are a transient cosmetic mismatch, self-healing via
  prune; write-only-your-own forbids fixing them here (S3).
- testing + left-shift gates — no machine gate asserts the in-flight ledger vocab (the memory-tree
  hygiene check 8 governs BACKLOG/STATUS rows, not the in-flight ledger prose — verify at build); the
  gates to re-run are `check-template-size.sh` (≤32 KiB) and `check-kit-versions.sh` (after S4).
- migration / rollback — revert the edits; vocab is backward-tolerant.
- user docs — `WIRE-INTO-PROJECT.md` is the adopter doc, updated in S2.

## 6. Acceptance criteria

- AC1 — When template §1 DoD L43 is read, it states bookkeeping is committed before the push and the
  wrap-up message.
- AC2 — When `grep -rIn "pushed" .` runs (excluding `memory/playbook/archive/**` and the two
  `*/builds/2026-07-19-*-aPrunedCeremony/` folders), it returns nothing — catching the generator
  (`adopt-memory-tree.sh`) AND every self-prune span (`pushed:/merged:<sha>`, prose `pushed/merged`),
  not just the literal `pushed:<sha>` token.
- AC3 — When `bash tools/check-template-size.sh` runs after the edits, it exits 0 (≤ 32768) — proven
  by measurement.
- AC4 — When `bash tools/run-gates.sh` runs, the memory-tree hygiene gate and `check-kit-versions.sh`
  both stay green (the kit-version marker/constant agree after S4).

## 7. Gates

`tools/check-template-size.sh` (re-run, ≤32 KiB), the memory-tree hygiene gate (verify unaffected),
`tools/check-kit-versions.sh` (must stay green after the 1.2→1.3 bump). No new gate.

## 8. Open questions

- **Fork A — DoD line vs a Landing clause.** RESOLVED (owner, 2026-07-19): the DoD line is the single
  home; no separate Landing bullet.
- **Fork B — retire `pushed:<sha>` or keep it.** RESOLVED (owner, 2026-07-19): option a — RETIRE it
  (vocab → `{in-flight | merged:<sha>}`).

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft.
- rev-2 · 2026-07-19 · folded wf_2f11fd07: in-place DoD extension; raised `pushed:<sha>` as Fork B.
- rev-3 · 2026-07-19 · owner ratified Fork B option a; expanded S2 to the live-site inventory; status
  → INPROGRESS.
- rev-4 · 2026-07-19 · folded pre-code review wf_539c5419: added the IN-FLIGHT.md generator
  `adopt-memory-tree.sh` L50 to S2 (+ kit-version bump S4) — omitting it resurrected the vocab in
  every adopter; corrected S3 (live rows are bare `merged`, migrate to `merged:<sha>`, not a
  nonexistent `pushed:<sha>`); broadened AC2 to `grep -rIn "pushed"` over the whole tree.
