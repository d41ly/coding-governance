# aPrunedCeremony build log

Build of the 6 aPrunedCeremony specs into `coding-governance`, worktree
`C:\projects\coding-governance-pc` on `feature/pruned-ceremony-build-a` off `729a1ee3`, node `a`.
Unattended, owner-authorized 2026-07-19. Merge+push only when fully done.

## Ratified functional decisions (rule D)

- **RD1 · retire `pushed:<sha>`** (owner, 2026-07-19; PLAY-4 Fork B option a). Ledger vocab →
  `{in-flight | merged:<sha>}`; self-prune keys on `merged:<sha>`. Sites: template §3 L87-88,
  HYGIENE.md L66 + its template source, IN-FLIGHT.md L3, WIRE-INTO-PROJECT.md L134, node-a ledger
  rows. Node b's rows left per write-only-your-own (backlog follow-up).
- **RD2 · build the manifest+canary** (owner, 2026-07-19; TOOL-1 Fork A → build, overriding the
  defer recommendation). `gate-legs.json` + `run-gates.sh` iterator + `run-gates.test.sh` canary.
- **RD3 · PLAY-1 enforcement wording is conditional** (recommended, accepted via "build"): the
  post-merge scoped run is conditional on the runner supporting whole-run diff-scoping; the kit's
  `run-gates.sh` scopes only self-test legs, so the wording must not presume a mechanism the kit
  lacks.
- **RD4 · PLAY-2 lands in `.domain-rules.md` §10**, not the template (byte budget); discriminates on
  indirection so the kit's own `leg_if_changed` is not banned.
- **RD5 · PLAY-4 DoD line is the single home** for the before-push rule (Fork A); no separate Landing
  bullet.
- **RD6 · TOOL-2 pre-push built; drift-signal scoped to the copy-install path** (not universally
  N/A); `.gitattributes` gains explicit hook LF pins.
- **RD7 · template edits are byte-neutral in-place rewords or externalize** — the ≤32 KiB gate has
  ~86 bytes headroom; re-measure after every template edit (the load-bearing constraint).

## Build order (files overlap — sequential, single node)

BU-P1 → BU-P4 (template + AGENTS + run-gates header + ledger vocab) → BU-P2/P3 (domain-rules) →
BU-T1 (run-gates rewrite — supersedes the P1 header edit's file, so P1's run-gates.sh header rides
into the T1 rewrite) → BU-T2 (hooks). Re-measure template size after every template touch; run the
full gate suite before merge.

## Log

- 2026-07-19 · BU-0 · specs ratified to rev-3 (PLAY-4, TOOL-1) / INPROGRESS (others); STATUS + this
  log created; watchdog cron d1961337 scheduled. Pre-code adversarial review next.
- 2026-07-19 · BU-0 · pre-code review wf_539c5419 (7 confirmed, 2 build-breaking HIGHs) folded before
  code: PLAY-4 rev-4 (IN-FLIGHT.md generator + kit bump + bare-merged migration), TOOL-1 rev-4
  ($PYBIN substitution + canary grep + AC5), TOOL-2 rev-3 (GOV_GATE_CMD seam + 3rd-field classify).
- 2026-07-19 · BU-P1..P4 built: template rewords (full-run-at-push-boundary, byte-neutral, 32735/32768),
  domain-rules §10 (fail-closed scoping + vacuous-ratchet), pushed:<sha> retired at all live sites +
  kit 1.2→1.3. Node-b rows left for node b (PLAY-aPrunedCeremony-5).
- 2026-07-19 · BU-T1 built: gate-legs.json (15 legs) + run-gates.sh manifest iterator (PYBIN
  substitution, \x1e field sep, exit-propagating parse, startup probe) + run-gates.test.sh canary.
  Full run 15 GREEN; canary catches injected path; AC5 verified.
- 2026-07-19 · BU-T2 built: .githooks/pre-push (remote-ref classify, pushed-tip precondition,
  GOV_GATE_CMD seam) + pre-push.test.sh (5 cases pass) + hook LF pins + AGENTS boundary note. 16 GREEN.
- 2026-07-19 · Closing review wf_3c0f6fa3 (5 confirmed, 0 HIGH) folded: canary rejects malformed legs;
  gate-legs.json added to watch list; node-b backlog row; comment fix; default-branch LOW accepted.
  6 specs → CLOSED. Full suite GREEN. Merging + pushing next.
