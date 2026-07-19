STATUS: IN-PROGRESS

# aPrunedCeremony build — status

Line 1 is the machine-readable state the watchdog cron reads: `STATUS: IN-PROGRESS` flips to
`STATUS: COMPLETE` only when the closing review is clean AND the branch is merged+pushed.

Build of the 6 aPrunedCeremony specs (PLAY-1..4 + TOOL-1/-2), owner-approved 2026-07-19 with two
ratified decisions: **retire `pushed:<sha>`** (PLAY-4 Fork B option a) and **build the
manifest+canary** (TOOL-1 Fork A → build). Worktree `C:\projects\coding-governance-pc` on
`feature/pruned-ceremony-build-a` off `729a1ee3`. Node `a`. Merge+push only when fully done.

## Build units

- BU-0 · CLOSED · ratified specs (PLAY-4/TOOL-1 rev-4, TOOL-2 rev-3); pre-code review wf_539c5419 (7 confirmed, 2 build-breaking HIGHs) folded before code
- BU-P1 · CLOSED · PLAY-1 full-run-at-push-boundary: reworded template L48/L126/L185 + AGENTS.md gate-suite + run-gates.sh L3 header; template 32737/32768 (31 under)
- BU-P2 · CLOSED · PLAY-2 fail-closed coarse scoping rule added to .domain-rules.md §10 (+ the enforcement-conditional detail cut from the capped template L48)
- BU-P3 · CLOSED · PLAY-3 vacuous-ratchet bug class added to .domain-rules.md §10
- BU-P4 · CLOSED · PLAY-4 DoD extended (bookkeeping before push) + pushed:<sha> retired at all 8 live sites incl. the adopt-memory-tree.sh + HYGIENE generators; kit 1.2→1.3; node-a rows migrated to merged:<sha>; template 32735/32768; kit-versions + AC2 grep clean
- BU-T1 · CLOSED · TOOL-1 manifest+canary BUILT: gate-legs.json (15 legs) + run-gates.sh iterator (PYBIN substitution, startup probe, \x1e field sep) + run-gates.test.sh + .gitattributes + AGENTS.md. Full run 15 legs GREEN; canary catches an injected path; AC5 verified
- BU-T2 · OPEN · TOOL-2 pre-push enforcement: .githooks/pre-push + pre-push.test.sh + .gitattributes hook pins + AGENTS.md + drift-note

## Closing

- PENDING · closing adversarial review of the whole diff
- PENDING · merge --no-ff to local main + push (owner pre-authorized on completion)
- PENDING · final overview; delete watchdog cron

## Constraints

- The template `≤32 KiB` gate has ~86 bytes headroom — re-run `check-template-size.sh` after EVERY
  template edit; retiring pushed:<sha> SAVES bytes, the DoD extension ADDS — net must stay ≤32768.
- `HYGIENE.md` mirrors `tools/memory-tree/HYGIENE.template.md` — edit both (single source).
- Commit per BU; gate suite (`bash tools/run-gates.sh`) green before merge.
