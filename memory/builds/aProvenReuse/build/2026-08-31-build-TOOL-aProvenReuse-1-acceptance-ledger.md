# Acceptance ledger — TOOL-aProvenReuse-1 and -2

**Serves:** journal TOOL-aProvenReuse-1 TOOL-aProvenReuse-2

Every criterion below is answered by something that was RUN on node `a` on 2026-08-31. Where a
criterion is answered by a SUITE rather than by a single observation, the entry says so rather than
implying a direct sighting, and where the evidence is weaker than the criterion asked for the entry
says that too.

**Evidences:** TOOL-aProvenReuse-1

- AC1 — `§10 Reuse audit does not record the recall terms used` — observed with
  `SPEC10_EVIDENCE_CUTOFF` temporarily armed at `2026-08-04`, over the live corpus. The failure text
  names the section and the missing arm. Staged as a cutoff move, not a fixture edit, so the arm was
  exercised against real specs.
- AC2 — `does not record the probe result` — the same run. The full line goes on to name the three
  accepted spellings, and it is textually distinct from AC1's, which is what makes the arms
  separable.
- AC3 — `exit=0` with the cutoff at its declared value while pre-cutoff specs carrying neither fact
  are tracked. The grandfathering is observed rather than argued.
- AC3a — `miss 'tFixture-84.md (§10 Reuse audit'` in `check-memory-hygiene.test.sh`. WEAKER than a
  direct sighting: it is a fixture assertion, covered by the suite, and I did not watch it fail with
  the Tier-1 cut removed. Labelled weaker deliberately.
- AC4 — `0` findings and `exit=0`, the bar green at `SPEC10_EVIDENCE_CUTOFF="2026-09-01"`.
- AC5 — `188` files named, `exit=1`, armed at `2026-08-04`. Re-derived at build time rather than
  copied: the `253` in the build README is the ALL-TIERS figure over 348 §10-bearing specs, and the
  arm reaches only the 264 Tier-2 ones. After round 3 added the ORDER note the same run names `193`,
  the extra five being the specs whose probe token sits only after their terms marker.
- AC5a — the cutoff hazard enumerated across `git for-each-ref refs/heads` before the value was
  pinned: `21` Tier-2 specs dated `2026-08-31` on three sibling branches, `8` on
  `branch/unattended-kit-adversarial-review-6810dc`, `7` on `branch/paired-lexer-followup-9c31a2`,
  `6` on `branch/gate-bar-tooling-review-020565`. That measurement is why the cutoff is `2026-09-01`.
- AC6 — `PASS (270 assertions)`, `exit=0`. The count moved 254 → 262 → 269 → 270 as the arms landed.
- AC7 — `bash tools/check-kit-versions.sh` `exit=0` after `2.50 → 2.51`.
- AC8 — `kit-parity: shipped and installed docs agree (3 pairs, rendered for 'tools/memory-tree')`,
  `exit=0`, and the rendered `memory/TEMPLATE-SPEC.md` §10 names both required facts and the
  `SPEC10_EVIDENCE_CUTOFF` key.
- AC9 — `bash skills/session-kickoff/manifest-check.sh` `exit=0` after each `last-audit` re-stamp;
  the pre-commit hook refused the first attempt naming the three watched files, which is the arm
  firing rather than the criterion being assumed.
- AC10 — `hasT=0 hasP=0` over the copyable skeleton's own §10 body, fed to a harness carrying the
  shipped predicate verbatim. Direct observation, not inferred from a fixture passing.
- AC11 — `hasT=1 hasP=0` over a §10 whose terms list wraps with `reuse_lookup` on the continuation
  line. Same harness. This is the case the per-line repair got wrong, and it was measured at
  `hasT=1 hasP=1` before the section-truncation fix.

**Evidences:** TOOL-aProvenReuse-2

- AC1 — `the reuse-first directive was waived at preflight` — `unattended.test.sh` arm 5, against a
  fixture run-state file carrying a `waiver · item reuse-first` row, asserting the reason reaches the
  message. Covered by the suite, `PASS (669 assertions)` on shard 2/2.
- AC2 — `the recall query log is ABSENT` — arm 2, with a `miss` on AC3's text so the two UNMET
  messages are proven distinct rather than assumed.
- AC3 — `holds no query for this tree` — arm 3, with the reciprocal `miss` on AC2's text.
- AC3a — `declares no readable RECALL_CLI` — arms 1 and 1b, blank and unresolvable, both reaching the
  same outcome, and 1b asserts the offending value appears in the message.
- AC4 — `1 recall query recorded for this tree` — arm 4, fixture row reproducing a real row's
  escaping. Separately observed LIVE in this repo: the declared `RECALL_CLI` resolves and the join
  returns `3 recall queries` for this tree, which is this build's own probes.
- AC4a — `1 recall query recorded for this tree` with a `miss` on `2 recall queries` — the prefix
  arm. Restaged mid-build: the first version used a PARENT row and pinned nothing, measured `1` with
  and without `-x`; a CHILD row measures `1` and `2`.
- AC5 — covered by the suite's existing override arms, which assert `--override` records a parked
  entry and that `--override authorization-reachable` is still refused. WEAKER: I did not run an
  override for `reuse-probed` specifically, so the negative control is observed and the positive is
  inherited from the shared code path.
- AC6 — `10 against 11` — `UNATTENDED check 3 FAILED`, the declared Definition-of-Done floor sitting
  below the kit's own core count, with `CORE_FLOOR` staged back to `12:10`. `exit=0` once restored.
- AC6a — `says 'Ten', driver carries 11` — the count-sentence join, observed by reverting it. The
  row join was staged separately and refused with a distinct message naming `reuse-probed` as a core
  item absent from the protocol's table. Two staged breaks, two refusals, neither inferred.
- AC7 — `PASS (226 assertions)` shard 1/2 and `PASS (669 assertions)` shard 2/2. Three earlier runs
  of shard 2/2 failed a wall-clock assertion under cross-session load; the clean run is the evidence
  and the flake is filed as `TOOL-aProvenReuse-6`.
- AC8 — `bash tools/check-kit-versions.sh` `exit=0` after `1.12 → 1.13`, and the retired
  silent-waiver phrases are gone from `tools/unattended/SKILL.template.md` and its render.
- AC9 — `bash skills/session-kickoff/manifest-check.sh` `exit=0` after the `.unattended.conf`
  re-stamp.
