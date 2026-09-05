**Serves:** journal TOOL-aHoistedPass-2

# Acceptance ledger — TOOL-aHoistedPass-2

Tier-2 · node a · 2026-09-05 · landed at `8c759e50`

`passes-harnessed:M6` bound every unattended run to a route that did not exist: 0 of 17 core
directive handles appeared in `BUILD-METHOD.md`, and check 16 arm B asserted only that the cited
section EXISTS. The route is written, all seventeen handles are anchored, and arm B now reads the
cited section's body.

## Acceptance criteria

**Evidences:** TOOL-aHoistedPass-2

- AC1 — MET — the staged break, through the REAL gate: the M6 `passes-harnessed` anchor deleted,
  `bash tools/unattended/check-unattended.sh` prints `UNATTENDED check 16 FAILED` naming the body
  term's refusal. Restored after, and the same gate is green.
- AC2 — MET — the staged break the `<!-- … -->` block strip exists for, through the real gate. With
  the anchor present ONLY inside a MULTI-line comment whose SECOND line carries it, check 16 still
  reds. The four-fixture predicate table measured beside it: the file at BASE RED under both forms,
  an honest sentence PASS under both, a single-line comment RED under both, and the multi-line
  evasion **PASS under the naive line-prefix filter and RED under the block strip**. That row is the
  whole argument for the strip being block-wise.
- AC3 — MET — with the anchors in place, `bash tools/unattended/check-unattended.sh` exits 0 with
  zero `FAILED` lines.
- AC4 — MET — each of the seventeen `DIRECTIVES_CORE` handles is found backticked inside its own
  `^## M<n>` slice of the render: **17 of 17**. The same derivation returned 0 of 17 at the spec's
  base and at the run's BASE.
- AC5 — MET — `grep -c unattended-build memory/guides/BUILD-METHOD.md` returns 1.
- AC6 — MET — `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0.
- AC7 — MET — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` exits 0 at
  **26941 of 27648 bytes, 97.4%**, and `wc -l` is **341** against the `≤350` line half. The high-water
  row was re-bumped 25338 to 26941 because this growth is the growth `TOOL-aHoistedPass-3` funded.
- AC8 — MET — `grep -c "pass-order leg over the commit graph"` returns **1** in each half. The clause
  is NARROWED and not struck: the phrase is kept contiguous on one line precisely so this criterion
  can observe it, and `memory/DECISIONS.md:125` ratifies the claim a strike would have deleted.
- AC9 — MET — `diff` of the two protocol halves CR-normalised prints nothing, both at 55964 bytes and
  662 lines, under `INDEX_CAP_BYTES="61440"`.
- AC10 — MET — §12's state-refusal sentence names `MISSING` and `THIN`, says they are the whole of what
  the verb inspects, and `grep -c FORKED` over that paragraph returns 0.
- AC11 — MET — `bash tools/unattended/adopt-unattended.sh --check` exits 0.
- AC12 — MET — the rendered Skill carries all four branch spellings: `(READY - build it)`,
  `every tracked spec is terminal`, `no tracked spec grades as a unit`, and a branch naming THIN,
  FORKED and MISSING together.
- AC13 — MET — the rendered Skill states that every call is made by `scriptPath` and never by `name`,
  and names `--override build-complete` as the only escape from an early stop.
- AC14 — MET — `bash tools/check-install-prefix.sh` exits 0 with
  `tools/unattended/SKILL.template.md` recorded at **3** and a hand-written reason column on that row.
- AC15 — MET — `bash tools/check-kit-versions.sh` exits 0 and
  `bash tools/memory-tree/check-verdict-epoch.sh` exits 0, at whatever values the order-2 units set,
  named nowhere in this criterion. This unit moved neither version.
- AC16 — MET at the leg — `bash skills/session-kickoff/manifest-check.sh` exits 0 with `last-audit`
  re-stamped. Its C9 clause grades only at the full bar, which is a push-boundary observation.
- AC17 — NOT OBSERVED, the one unverified premise: that a `scriptPath` call from the rendered Skill
  makes one `scriptPath` `Workflow` call and has it TAKEN. This run did not make one: it built
  the units directly, so the observation was never available to it. The premise the whole hoist rests
  on therefore stays exactly as unverified as the spec says it is, and this row is where that is
  recorded rather than a green tick nobody earned.
- AC18 — MET — the three residual clauses appear once per half and `check-unattended.sh` is green:
  `bash tools/unattended/check-unattended.sh` exits 0.
- AC19 — MET — `grep -c "unreachable except through both"` returns `0` in both halves, and the
  sentences that replaced §12's first two name DISPOSAL as the third stage and state that what the
  program holds is the ROSTER HAND-OUT rather than the build's reachability. Labelled AC19 at rev-5;
  it was a second AC18 until then, and two criteria under one id means one verdict row can be
  reported as satisfying both.

## What the spec could not have known

**Section 7 said the term "adds no new numbered branch, so it owes no new arm". Measured false.** The
unarmed-branch pin registry is INDEX-keyed, so inserting a branch into check 16 renumbered five
pinned siblings out from under their signatures and `check-arms --check` redded on all five. Three
arms in `check-unattended.test.sh` now carry the term's whole signature and the five shifted pins were
re-emitted; the new branch is ARMED, not pinned.

**An arm must carry the WHOLE signature, not a prefix.** `check-arms` takes the longest literal run of
a message as its signature, so the gate's sentence was shortened afterwards purely so one arm line
could hold it. The predicate never changed.

## What is held by the run and by nothing else

Two dangling references ship: `tools/workflows/unattended-unit.js` until order 4, and
`--plan <slug> --paths` until order 5. The second is worse than the first, because `verb_plan`
DISCARDS an unrecognised trailing argument rather than refusing it — the run gets the padded table,
exit 0 and no refusal. Disclosed in F2 at rev-5, with the cheaper permanent fix named and left out of
scope.
