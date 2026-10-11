**Serves:** diff-review TOOL-dRemeasuredRender-1 DEPL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2

# Tier-2 closing diff review — dRemeasuredRender, ROUND 1

*This is the closing adversarial review of build dRemeasuredRender's three units, run through
`tools/workflows/tier2-review.js` at intensity full. Five lenses read the diff and a skeptic batch
then tried to refute every finding. The record is synthesized from the lens and skeptic outputs.
Its grades are the skeptics' binding grades under the severity rubric.*

Reviewed range: 17472e212ffd0d5e3be825502c6169bbeb2e952f...bac1a4fb5f9fcf5f7d924dcf8e7e17cc924f0149

## Verdict: CLEAN WITH FIXES

No finding is a blocker.
One finding is high (id 4). It must be folded before landing, because it writes a receipt that
certifies bytes as rendered at a vintage they were never rendered from.
Three findings are medium and seven are low.
Every confirmed fix except one was judged sound by a skeptic.
The fix the skeptic rejected (id 10) is replaced below by the skeptic's corrected fix.

## Review shape

Review shape: intensity full, raw 13, confirmed 11, refuted 2, unverified 0 (0 uncertain), precision 0.85.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| verification | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings | ids |
|---|---|---|---|
| blocker | 0 | 0 | none |
| high | 1 | 1 | 4 |
| medium | 2 | 3 | 1, 11 · 6 |
| low | 4 | 7 | 5 · 12, 13 · 7, 9, 10 · 3 |
| total | 7 | 11 | |

Two findings were refuted.
Id 2 duplicates id 1 and overstates its reach.
Id 8 misreads the arm's header, and blob_oid is independently checked against git elsewhere in the suite.
Both are listed in the appendix only.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Verdict hygiene: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 10 judged sound, 1 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 3 RE-GRADED by the skeptic (ids 3, 5 and 12, each medium to low).
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 3 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 42 items, each assigned to exactly one of 5 lenses (security 9, correctness 9, seams 8, verification 8, intent 8).
- By design: the caller's byDesign.

Every counter that could mark the run incomplete is zero, so this run is complete.
No lens died, so the finding set is complete for the brief the lenses ran on.
The empty lens notes mean each lens worked from the generic brief, and that is a limit on depth, not a gap in the count.

## Findings

### HIGH-1 — an accepted no-render outcome gets a receipt stamped at `to_commit` (id 4)

- **Where:** [tools/govkit/govkit.py](../../../../tools/govkit/govkit.py) line 11769, which is the re-measure step in `_cmd_update` and its call into `measure_rendered_rows`.
- **Unit:** DEPL-dRemeasuredRender-1.
- **Defect:** The step treats any kit that is in `_rg_snap` and not in `_rr_refused` as rendered.
  `_rg_snap[_eid]` is set before any argv runs, and `_rr_refused` is filled only when `_bad` is true.
  `outcome_accepted` returns True for a non-zero exit whose matched outcome declares `ok`.
  Four shipped outcomes are accepted that way, and each one is a stop that renders nothing:
  memory-tree 3 `not-rendered-here`, memory-tree 1 `seed-and-stop`, lexicon 1 `no-project-layer`
  and codebase-map 1 `seeded-conf`.
- **Consequence:** For such a kit, `measure_rendered_rows` stamps `sha256` and `oid` from the
  untouched hand-authored or older-vintage bytes, and `commit`, `version` and `gov_oid` at
  `to_commit`. `govkit check` then reads the row as clean. The next update grades the template from
  a vintage the file was never rendered at. memory-tree's kit.toml records the exit-3 state as
  measured at a real adopter this week. At base, rendered rows went through the `how != "table"`
  arm as 'reported only', so this diff introduced the false receipt. It is the silent-stale receipt
  the unit set out to remove. The skeptic graded it high rather than blocker because the
  consequence is limited to receipt and grading accuracy.
- **Fix (judged SOUND by the skeptic):** Record, per kit, whether every regenerate argv actually
  rendered. Add the kit to an `_rr_norender` set beside `_rr_refused` whenever an argv exits
  non-zero and is accepted only through an `ok = true` outcome, or a block is skipped for an empty
  argv. Route such a kit's rendered rows to KEPT with a reason like "its render stopped at accepted
  outcome '<means>' without rendering". Add a self-test arm whose fixture regenerate exits through
  an accepted non-zero outcome, assert the row keeps its record, and observe the arm red with the
  guard removed.
- **Left-shift gate:** Add a govkit selfcheck over every shipped kit.toml. It lists each
  `[[regenerate]]` outcome declared `ok = true` with a non-zero exit, and requires that outcome to
  carry an explicit `renders = true|false` key. The re-measure step then reads that key instead of
  inferring a render from acceptance. This is class `fallback-fabricates-the-passing-value`.

### MEDIUM-1 — the post-render hole verdict is printed before the verify pass can roll the render back (ids 1, 11)

- **Where:** [tools/govkit/govkit.py](../../../../tools/govkit/govkit.py) lines 10993 and 10994,
  in the re-probe inside the regenerate loop (10982-10998).
- **Unit:** DEPL-dRemeasuredRender-2.
- **Defect:** The re-probe prints "'<id>' is discharged after the render; the early verdict does
  not stand" inside the per-kit regenerate loop. The verify pass runs afterwards (around 11160). On
  a green-to-red check it adds the kit to `_rolled_kits` (11262), and the rollback restores every
  `_rg_snap` path to its pre-argv bytes (11468-11491). The bytes that discharged the hole are then
  gone, and no later line corrects the verdict. DEPL-dRemeasuredRender-1 placed its re-measure
  after the verify pass for exactly this reason and gates it on `_rolled_kits` (11763). The two
  units answer the same question, whether the render still stands, in two different ways. This is
  class `two-guards-one-question-two-answers`.
- **Consequence:** The run withdraws an enforcement signal on the strength of bytes it then
  reverts. The path is narrow. lexicon's hole probe and its `[check]` are the same argv, so they
  cannot diverge on the same bytes. drift-audit's hole probe (`drift_report.py --check`) differs
  from its `[check]` (`adopt-drift-audit.sh --check`), and a later kit's regenerate can still break
  a check in between. The run that reaches this path already fails and prints ROLLED BACK, so the
  effect is contained. Spec S3 covers accepted and refused renders but not rolled-back ones. The
  dRR-2 arms use `[check] none`, so no arm reaches this path.
- **Fix (judged SOUND by the skeptic, for both ids):** Defer the after-render hole verdict until
  the verify pass has filled `_rolled_kits`. Keep each kit's early-undischarged holes (`_hu_rr`,
  keyed by kit), and run the re-probe and its print beside the DEPL-1 re-measure step. For a
  rolled-back kit, either re-probe the restored bytes or print that the render was rolled back and
  the early undischarged verdict stands again. Add a selftest arm with a kit whose `[check]` goes
  green-to-red after a render that discharges its hole, and observe it red against the current
  placement.
- **Left-shift gate:** Add a selftest structural arm that lists every operator-facing verdict line
  `_cmd_update` prints about a rendered file's bytes, and asserts each one is emitted after the
  verify pass's `_rolled_kits` is final. Record the class in the bug-class checklist as
  "a verdict about bytes printed before the step that can revert them".

### MEDIUM-2 — the rolled-back and not-run KEPT guards have no arm (id 6)

- **Where:** [tools/govkit/govkit.py](../../../../tools/govkit/govkit.py) lines 11764 and 11768,
  which are the 'its kit was rolled back' and 'its render did not run this time' branches.
- **Unit:** DEPL-dRemeasuredRender-1.
- **Defect:** Spec S2 requires both KEPT exclusions and says AC3 observes them. selftest.py
  asserts only 'its render was refused' ([dRR-1 AC3], around 1897). A grep finds neither of the
  other two strings in selftest.py, and no arm checks that such a row is unchanged.
- **Consequence:** If the `_rolled_kits` or `_rg_snap` guard were reordered or dropped, the step
  would stamp a rolled-back or declined row at `to_commit` over bytes never rendered at that
  vintage, and `govkit selftest` would stay green. The aRF-17 S1 fixture (`kit_rb`, selftest.py
  around 1736) already reaches the rolled-back branch, and nothing asserts what it prints. There is
  no runtime effect today.
- **Fix (judged SOUND by the skeptic):** In the aRF-17 S1 arm (selftest.py around 1751-1765),
  record the `docs/out.md` row before the update. After the update, assert that stdout carries
  'receipt: KEPT [rendered] docs/out.md — its kit was rolled back' and that
  `read_row17(t, 'docs/out.md')` equals the row from before the update. Add one arm, or extend a
  `GOVKIT_RERENDER=0` or held-kit (aHI-4) arm, that asserts the 'its render did not run this time'
  KEPT line and an unchanged row. Observe both red with their guard removed.
- **Left-shift gate:** Add a selftest meta-arm that greps every `KEPT [...] — <reason>` literal in
  govkit.py and requires each reason string to appear in at least one selftest assertion. This is
  class `observed-by-claim-no-arm-discharges`, and the gate reaches it at the code side.

### LOW-1 — the same rollback defect as MEDIUM-1, at the seams lens's binding grade (id 5)

- **Where:** [tools/govkit/govkit.py](../../../../tools/govkit/govkit.py) line 10993.
- **Unit:** DEPL-dRemeasuredRender-2.
- **Defect:** This is the seams lens's report of the defect in MEDIUM-1. The re-probe's
  'discharged' line runs inside the regenerate loop, before the verify pass that can restore the
  pre-render bytes from `_rg_snap`.
- **Grade note:** The skeptic re-graded it from medium to low, because the effect is one wrong
  status line on a run that already fails. That grade binds this id. The reviewer judges medium
  right for the defect, as ids 1 and 11 are graded, since the same consequence cannot carry two
  severities. The binding rule keeps id 5 at low, and the shared fix discharges all three ids.
- **Fix (judged SOUND by the skeptic):** Keep each kit's `_hu_rr` list and run the re-probe and its
  print after the verify pass, next to the re-measure step. For a kit in `_rolled_kits`, re-probe
  after the restore, or print that the render was rolled back and the early verdict stands. The
  alternative is to keep the re-probe where it is and suppress the 'discharged' line for a kit
  that is later rolled back. MEDIUM-1's fix is the same fix and covers this id.
- **Left-shift gate:** The same gate as MEDIUM-1.

### LOW-2 — spec "Observed by" claims that no arm discharges (ids 12, 13)

- **Where:** [tools/govkit/selftest.py](../../../../tools/govkit/selftest.py) line 1905 (the dRR-2
  loop) and line 1887 (the dRR-1 AC3 arms).
- **Units:** DEPL-dRemeasuredRender-2 (id 12) and DEPL-dRemeasuredRender-1 (id 13).
- **Defect, id 12:** DEPL-2 S3 says the re-probe "runs whether the argv was accepted or refused"
  and is observed by AC2. Both the hp and hf fixtures use `gen_cg`, which exits 0. The only
  refusing fixture, `gen_rr`, declares no hole. No arm runs the re-probe after a refused argv. The
  re-probe sits outside `if _bad` (govkit.py 10985), so the code is correct today. The skeptic
  re-graded this from medium to low.
- **Defect, id 13:** DEPL-1 S2 lists four KEPT reasons and says AC3 observes them. AC3 drives
  only the refused reason. Both dRR-1 fixture kits declare `[check] none`, so neither can roll back.
  This overlaps MEDIUM-2 at the spec-claim side. Id 6 carries the missing arms, and id 13 carries
  the ledger claim that over-states them.
- **Consequence:** A regression would pass every arm. Moving the re-probe into the accepted
  branch, or moving the re-measure back into the regenerate loop, are both examples. The spec and
  the acceptance ledger certify observations no arm makes.
- **Fix (judged SOUND by the skeptic, for both ids):** For id 12, add a third fixture to the dRR-2
  loop whose generator writes the file and then exits non-zero (the `gen_rr` pattern). Assert both
  that the after-render hole line prints and that the regenerate was REFUSED. Otherwise correct
  S3's "Observed by" to NOT OBSERVED. For id 13, add an arm with a kit whose `[check]` passes
  before the update and fails after the render. Assert that the row is unchanged and that
  "KEPT [rendered] ... its kit was rolled back" prints. Otherwise narrow S2's "Observed by" to the
  refused reason. MEDIUM-2's fix supplies this arm.
- **Left-shift gate:** Extend the spec-ledger check so that each "Observed by AC<n>" clause names
  the selftest arm label that observes it, and require that label to exist in the named suite. A
  clause covering several reasons then needs one label per reason. This is class
  `observed-by-claim-no-arm-discharges`.

### LOW-3 — measure and re-probe branches no arm drives (ids 7, 9, 10)

- **Where:** [tools/govkit/govkit.py](../../../../tools/govkit/govkit.py) line 8722 (the `version`
  re-stamp), line 8707 (the absent-file KEPT branch, with the `git hash-object` failure at 8714)
  and line 10998 (the re-probe's third verdict arm).
- **Units:** DEPL-dRemeasuredRender-1 (ids 7 and 9) and DEPL-dRemeasuredRender-2 (id 10).
- **Defect, id 7:** The dRR-1 fixture `kit_rm` (selftest.py 1857) declares
  `version_from = { none = "fixture" }`. `resolve_entry_version_at` returns '(none declared)' at
  both vintages, and no arm reads `_rm_row['version']`. Deleting
  `row["version"] = resolve_version(row)` leaves every arm green.
- **Defect, id 9:** No arm drives 'its file is absent after the render' or the 'would not hash'
  branch, although spec S2 lists the absent file as a required reason. A regression could crash on
  a deleted output or write `oid: ""`.
- **Defect, id 10:** The re-probe's third arm ('re-probed after the render reads <verdict> ..., so
  neither verdict is confirmed', for no-launch or needs-answer) has no arm. Spec rev-2 added the
  line so that the early line is never left unanswered.
- **Consequence:** These are coverage gaps only. Shipped behaviour is correct today.
- **Fix, id 7 (judged SOUND by the skeptic):** Give the dRR-1 kit a
  `version_from = { file = ..., pattern = ... }` whose file changes between vintage A and vintage
  B. Assert that `_rm_row['version']` equals B's line and differs from `_rm_before['version']`.
- **Fix, id 9 (judged SOUND by the skeptic):** Add a dRR-1 sub-arm whose `gen.sh` removes
  `docs/out.md` after an accepted exit 0. Assert the 'KEPT [rendered] docs/out.md — its file is
  absent after the render' line, an unchanged row, and the count line '0 re-measured · 1 kept'.
- **Fix, id 10 (the finder's fix was judged UNSOUND, and this is the skeptic's corrected fix):**
  Lift the re-probe's verdict-to-line mapping (undischarged, discharged, other) into a small pure
  helper in govkit.py. Unit-test it in-process in selftest.py with a
  `('demo-hole', 'no-launch', '<detail>')` tuple, and assert the helper returns the 'so neither
  verdict is confirmed' line.
- **Left-shift gate:** Add the same reason-literal meta-arm as MEDIUM-2, widened to every operator
  line `measure_rendered_rows` and the re-probe can print. For fields a function re-stamps, add a
  fixture rule: every re-stamped receipt field differs between the arm's two vintages, so an arm
  cannot pass on a value that stays constant.

### LOW-4 — the [aHI-1 S3] arm is now satisfied by the post-render line (id 3)

- **Where:** [tools/govkit/selftest.py](../../../../tools/govkit/selftest.py) lines 1810-1812.
- **Unit:** DEPL-dRemeasuredRender-2.
- **Defect:** The arm claims the update names the hole "there too", meaning before the regenerate.
  It matches "'demo-hole' is undischarged (probe exit 3)" anywhere in the output. After DEPL-2, only
  the post-render re-probe prints that string (govkit.py 10991). The early line now reads 'probes
  undischarged before the render'.
- **Consequence:** The arm's label claims a property it no longer observes. The skeptic re-graded
  it from medium to low. The dRR-2 arms assert that the early line exists and, for hf, that the
  final line follows it, so removing the early probe would still red the suite.
- **Fix (judged SOUND by the skeptic):** Point the arm at the early line, "'demo-hole' probes
  undischarged before the render (probe exit 3)" with its reason. Optionally add a second assertion
  that the post-render "is undischarged" line comes after it, as the dRR-2 hf arm does with
  `_hp_final > _hp_early`.
- **Left-shift gate:** Record class `line-claim-matched-over-the-whole-output` in the bug-class
  checklist. An arm that claims a line's position (before or after a step) asserts an index
  ordering against a sibling line, never a bare `in stdout`.

## Fold order

1. HIGH-1 (id 4): add the no-render set, the KEPT reason and its arm.
2. MEDIUM-1 with LOW-1 (ids 1, 11, 5): move the hole verdict after the verify pass and add the rollback arm.
3. MEDIUM-2 with LOW-2 (ids 6, 12, 13): add the rolled-back, not-run and refused-with-hole arms, and correct the specs' "Observed by" lines.
4. LOW-3 and LOW-4 (ids 7, 9, 10, 3): add the coverage arms and repoint the aHI-1 arm.

Each new arm must be observed red against the current govkit.py before it counts.

review-shape kind=diff-review round=1 intensity=full at=synth raw=13 confirmed=11 refuted=2 unverified=0 blocker=0 high=1 medium=3 low=7 agents=11 out-tokens=100042

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/govkit/govkit.py:10993 | medium | medium | confirmed | Confirmed at govkit.py:10982-10998. The re-probe and its 'is discharged after the render; the early verdict does not stand' line print inside the regenerate loop. The verify pass at 11160 and later runs afterwards and can add the kit to _rolled_kits (11262). The rollback then restores every _rg_snap path to its pre-argv bytes (11468-11491), so the bytes that discharged the hole are gone. Nothing after that point re-prints or corrects the hole verdict. DEPL-1 deliberately gates its re-measure on _rolled_kits (11763), so the two units treat the same rollback differently. The path is narrow. No shipped kit reaches it today: lexicon's [check] and its lexicon-ratified discharge are the same `adopt-lexicon.sh --check`, so a hole that discharges after the render cannot sit beside a check that goes green-to-red. A held kit never regenerates. The path also needs a check that goes green-to-red, and such a run already fails and writes a rollback order. Still, the engine prints a hole verdict about bytes it then reverts, and no selftest arm covers it (the dRR-2 fixtures use `[check] none`). It is an advisory line in a run that already fails, so the effect is contained: medium. | sound | - |
| 2 | correctness | tools/govkit/govkit.py:10985 | medium | - | refuted | This duplicates finding 1: the same defect at the same site (the re-probe verdict printed in the regenerate loop before the verify pass can roll the kit back). It also overstates one part. A refused argv does not by itself roll anything back: refusal adds the kit to _rr_refused and calls r.fail, and the bytes stand unless the kit's own check goes green-to-red in the verify pass, which is exactly finding 1's path. A held kit, which is rolled back whatever its check says, never runs its regenerate or its re-probe (the `continue` at 10847-10852). The only real reach is the case finding 1 already confirms. | sound | - |
| 3 | correctness | tools/govkit/selftest.py:1810 | medium | low | confirmed | Confirmed at selftest.py:1810-1812. The [aHI-1 S3] arm, labelled as naming the hole 'there too' (before the regenerate, beside the AC4 ordering arm), still matches "'demo-hole' is undischarged (probe exit 3) — the fixture hole". After DEPL-2 only the post-render re-probe prints that string (govkit.py:10991). The early line now reads 'probes undischarged before the render'. So the arm no longer observes the property its label claims, despite the spec's 'holds unchanged'. The effect is contained. The dRR-2 arms assert that the early line exists (`_hp_early >= 0`) and, for hf, that the final line follows it, so removing the early probe would still go red in the suite. That makes this a misleading arm label with no coverage hole: low. | sound | line-claim-matched-over-the-whole-output |
| 4 | seams | tools/govkit/govkit.py:11769 | high | high | confirmed | I confirmed this against the code. In the regenerate loop, `_rg_snap[_eid]` is set before any argv runs. `_rr_refused` is filled only when `_bad` is true. `outcome_accepted` returns True for a non-zero exit whenever the matched outcome has `ok`. Four declared outcomes are accepted that way: memory-tree 3 `not-rendered-here`, memory-tree 1 `seed-and-stop`, lexicon 1 `no-project-layer` and codebase-map 1 `seeded-conf`. Every one of them is a stop that renders nothing. The memory-tree kit.toml comment says a target holding hand-authored docs is a real, measured state that ends at exit 3. For such a kit the new step at govkit.py ~11760 sees it absent from `_rolled_kits` and `_rr_refused` and present in `_rg_snap`. `measure_rendered_rows` then stamps `sha256`/`oid` from the untouched bytes, and `commit`/`version`/`gov_oid` at `to_commit`. At base the row was never re-stamped: rendered rows go through the `how != "table"` arm as 'reported only'. So this diff introduced a receipt that claims a render at a vintage the file was never rendered from, and `check` now reads it clean. Spec S1 reads 'ran and were accepted' literally and never considered a no-render accepted outcome. The path is reachable at a real adopter, but its consequence is limited to receipt and grading accuracy, so I grade it high rather than blocker. | sound | fallback-fabricates-the-passing-value |
| 5 | seams | tools/govkit/govkit.py:10993 | medium | low | confirmed | The re-probe and its 'is discharged after the render; the early verdict does not stand' line run inside the regenerate loop. That is before the verify pass at ~11160, which can put a kit in `_rolled_kits` and restore its rendered/declared paths from `_rg_snap`. Spec S3 also has the re-probe run after a refused argv, the case most likely to precede a green-to-red rollback. When the kit is rolled back, the restored pre-render bytes are the ones the probe failed on, and no later line corrects the 'discharged' claim. Base printed only the early 'is undischarged' line, which a rollback would have left true, so the diff introduced this. Reaching it needs a hole probe that passes on the render while the kit's own check reds. The effect is one wrong status line on a run that already prints ROLLED BACK and fails. Behaviour does not change, so I grade it low. | sound | - |
| 6 | verification | tools/govkit/govkit.py:11764 | medium | medium | confirmed | selftest.py asserts only one KEPT reason, 'its render was refused' ([dRR-1 AC3] at ~1897). No arm asserts 'its kit was rolled back' or 'its render did not run this time', and none checks that such a row is left unchanged. Grep finds neither string in selftest. Spec S2 lists all four reasons and claims 'Observed by AC3', but AC3 covers only the refused path. The aRF-17 S1 fixture (kit_rb, ~1736) does reach the rolled-back branch. Its gen.sh exits 0, its check reds on v2, and the kit is rolled back, yet nothing asserts the KEPT line or the row. If the `_rolled_kits` guard were dropped, the step would stamp a rolled-back row at to_commit and selftest would stay green. That is a real gap in the spec's claimed coverage of a safety guard. It has no runtime effect today. | sound | - |
| 7 | verification | tools/govkit/govkit.py:8722 | low | low | confirmed | measure_rendered_rows (govkit.py:8722) sets row['version'] = resolve_version(row), and _resolve_ver_at (8791) calls resolve_entry_version_at. That function returns '(none declared)' whenever version_from has 'none' (line 701). The dRR-1 fixture kit_rm (selftest.py:1857) declares version_from = { none = "fixture" }, so the row's version is '(none declared)' before and after the run. No dRR-1 arm reads _rm_row['version'] at all. If the version line were deleted or given the wrong resolver, every arm would stay green. The gap is real, but it is only missing coverage. Shipped behaviour is correct today, so the grade is low. | sound | - |
| 8 | verification | tools/govkit/selftest.py:1879 | low | - | refuted | The finding misreads the arm's header. Its claim to be 'not the code under test asking itself' covers the `oid` only, which is graded against the target's index entry from `git ls-files -s`. It never claims that for gov_oid. blob_oid (govkit.py:6419) predates this diff and is the suite's standing oracle for gov_oid; dozens of arms use it the same way (7734, 8440, 9280). The suite also checks blob_oid against git independently: at 9274 an index entry from ls-files must equal GK11.blob_oid(...), and 7797 does the same. So a wrong header or encoding in blob_oid would turn other arms red, and the 'arm stays green' impact does not hold for the suite. This arm's job is to show that gov_oid moved to the vintage-B template blob (tpl2, which is not tpl), and it does that. No defect here was introduced by this diff. | sound | assertion-between-two-derived-values |
| 9 | verification | tools/govkit/govkit.py:8707 | low | low | confirmed | measure_rendered_rows has two KEPT branches: 'its file is absent after the render' (govkit.py:8707) and the `git hash-object` failure (8714). No selftest arm drives either one. A grep for 'absent after the render' and 'would not hash' in selftest.py finds nothing. Spec S2 lists 'its file is absent' as a required reason and says 'Observed by AC3', but the AC3 arm (selftest.py:1886-1899) only drives the refused-render reason. The coverage gap is real. Current code handles both cases correctly, so the effect is only the risk of a regression shipping unnoticed. Grade low. | sound | - |
| 10 | verification | tools/govkit/govkit.py:10998 | low | low | confirmed | govkit.py:10996-10998 has a third else-arm, for a re-probe that reads neither discharged nor undischarged (run_hole_probes can return no-launch on OSError). Spec §5 commits to that behaviour: 'a re-probe reading neither verdict prints one line saying so'. The dRR-2 loop in selftest.py:1905-1931 runs only the hp fixture (discharged) and the hf fixture (undischarged), so no arm reaches the else-arm. Today the branch is correct. Only a future regression would go unseen, and the spec claims no arm for it ('two self-test arms'), so this is a coverage gap with no effect on behaviour. | unsound | - |
| 11 | intent | tools/govkit/govkit.py:10994 | medium | medium | confirmed | The re-probe and its final print sit inside the per-kit regenerate loop (govkit.py:10985-10998). The verify pass starts at about line 11159. On a green-to-red check transition it adds the kit to _rolled_kits and restores the _rg_snap bytes, which include the kit's rendered/generated rows. The diff introduced the 'is discharged after the render; the early verdict does not stand' line. Before it, the base printed 'is undischarged', which a rollback would have made true again. For lexicon the hole probe and the [check] are the same argv, so the two cannot diverge on the same bytes. A later kit's regenerate could still break the check in between. drift-audit's hole probe (drift_report.py --check) also differs from its [check] (adopt-drift-audit.sh --check), so the divergence can be reached on a narrow path. The effect is contained: that run fails (r.fail), says the kit was rolled back, and DEPL-1 prints KEPT 'rolled back, and the render with it'. The operator still reads a hole verdict that the restored bytes contradict. | sound | two-guards-one-question-two-answers |
| 12 | intent | tools/govkit/selftest.py:1905 | medium | low | confirmed | Spec S3 says the re-probe 'runs whether the argv was accepted or refused ... Observed by AC2'. Both dRR-2 fixtures (hp and hf, selftest.py:1905-1916) use gen_cg, which exits 0. The aHI-1 arm also uses gen_cg. The only refusing fixture, gen_rr (dRR-1 AC3), declares no hole. So no arm runs the re-probe after a REFUSED argv. In code, the re-probe sits outside `if _bad` (govkit.py:10985), so behaviour is correct today. The defect is the spec and ledger claiming an observation that no arm makes, plus the coverage gap that leaves. Neither affects behaviour, so the grade is low. | sound | observed-by-claim-no-arm-discharges |
| 13 | intent | tools/govkit/selftest.py:1887 | low | low | confirmed | This holds as a gap between what the spec claims is tested and what the tests actually check. The behaviour itself is correct. S2 in spec DEPL-dRemeasuredRender-1 lists four reasons for KEPT (render did not run, refused, kit rolled back, file absent) and says 'Observed by AC3'. AC3 and its arms in tools/govkit/selftest.py (the [dRR-1 AC3] checks) only use a regenerate that refuses. Both fixture kits declare `[check] none = "fixture"`, so the verify pass can never roll them back, and no arm reaches the `_eid in _rolled_kits` branch. The branch that never runs this run's regenerate (`_eid not in _rg_snap`) and the absent-file reason in measure_rendered_rows are not reached either. The diff introduced both the spec claim and the arms, so this is in scope. The code itself is right: the re-measure block runs after the verify pass, and `_rolled_kits` is checked before `_rr_refused` and `_rg_snap`. So nothing wrong ships. The cost is that a regression, such as moving the re-measure back into the regenerate loop or dropping the `_rolled_kits` test, would pass every arm. That makes it a coverage and claim mismatch with no behavioural effect, so the severity is low. | sound | observed-by-claim-no-arm-discharges |
