**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46

# dCalibratedLens's specs against dTendedCadence's, dFairHearing's and the cited ancestors' specs: a read-only cross-check

Node d, 2026-11-03, base `66c5b8dbf` (origin/main). dCalibratedLens's spec run began at `22a8efac3`,
the parent of its first spec commit `59d3d8e57`. Between `22a8efac3` and `66c5b8dbf`, `git log` names
no commit under `memory/builds/{dTendedCadence,dFairHearing}/spec/`, and `git diff --name-only` names
nothing under dSafePassage's, dWitnessedBar's, dRankedPlan's, dIndexedDesign's or dFurnishedOrders'
`spec/`. One commit moved an in-scope ancestor: `66f7b8d32` (merge `362790f10`, the owner's pick on
TOOL-dTotalRecall-2 §8 F6), which revised TOOL-dWellOiledMachine-6, -41 and -58 and is not in the spec
base (`git merge-base --is-ancestor 362790f10 22a8efac3` fails). No dCalibratedLens spec cites any of
the four units it moved. A delta pass would therefore be empty, so the owner asked on 2026-11-03 for a
full cross-read: every assumption a spec makes about a parent, or about an ancestor it cites directly,
compared with what that spec's DEFERRED text says now. This record is not an audit. No spec was edited
to write it, and no review harness ran. The mismatches feed the re-ground brief
[`2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md).

**Counts:** 169 assumptions · 122 AGREES · 39 MISMATCH · 8 UNKNOWN UNTIL BUILT, over 30 specs (the 28
citation specs and the 2 rule-wide candidates 22 and 41). 16 specs hold at least one MISMATCH: 1, 2, 3,
4, 8, 9, 10, 11, 13, 15, 16, 23, 24, 36, 41 and 46. By rule: 30 citation, 7 RB and 2 RK. Every
MISMATCH is pre-existing: the parent text already read so at `22a8efac3`, and none comes from
`66f7b8d32`. By the parent whose text decides the row: dFairHearing 23, dWellOiledMachine 7,
dTendedCadence 5, dRankedPlan 2, dIndexedDesign 1, dFurnishedOrders 1.

## Method

- **Population by citation.** A script stripped each spec's generated records tables, then matched
  `TOOL-<build>-<n>`, the bare `<build>-<n>`, and continuation lists (`-3 and -13`) for dTendedCadence,
  dFairHearing and the six in-scope ancestors: 28 specs. No spec uses a `tc`/`fh`/`wm` alias. Seven
  mentions name dTendedCadence or dFairHearing with no unit id (cl1:12-15, :382; cl10:12, :366;
  cl13:324; cl30:368; cl8:256-258); the readers found the owning unit for each.
- **Population by rule.** Three rules:
  - RH: the lease holder and epoch read, the one rule `66f7b8d32` applies.
  - RK: the cadence key, `GOV_CADENCE_KEY` by ask TOOL-dTendedCadence-27.
  - RB: a fact a dCalibratedLens spec states about a file at base that a parent unit's §2 changes.
    The candidate files are those that both a parent's and a dCalibratedLens spec's "Files touched"
    name, computed by script and listed per group in the brief.
  A text probe for RH and RK over the 19 specs no citation reached named 22 and 41 for RK. RH named
  only citation specs (3, 9, 12, 15). The other 17 uncited specs (19, 21, 25, 29, 31, 32, 33, 34, 35,
  38, 39, 40, 42, 43, 44, 45, 48) hit no rule probe and name no parent surface.
- **Readers.** Five `gov-spec-reviewer` agents, read-only, at effort medium, one per group of the
  brief [`2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck.md),
  with their handoffs beside it. Their returns are
  [`2026-11-03-build-TOOL-dCalibratedLens-1-crosscheck-returns`](2026-11-03-build-TOOL-dCalibratedLens-1-crosscheck-returns.md).
  Each MISMATCH there carries both sides quoted, its `Change:` and its `Cause:`.
- **The main loop** assembled the table below from the returns' tables by script, sorted by spec, and
  derived the counts from it. It changed no verdict. Where a reader's prose count differs from its
  table (E's opening says four mismatches and its table holds five; B's says 11 and its table holds
  15, because some bullets cover two rows), the table wins.
- **Aliases:** `clN:L` is line L of `spec/2026-11-0?-spec-TOOL-dCalibratedLens-N.md`. `tcN`, `fhN`,
  `spN`, `wbN`, `rpN`, `wmN`, `idN`, `foN`, `trN` and `prN` are the same for dTendedCadence,
  dFairHearing, dSafePassage, dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign,
  dFurnishedOrders, dTotalRecall and dPlacedRequest, under `../../<build>/spec/`. `BL:N` is line N of
  `memory/builds/dTendedCadence/BACKLOG.md`. All are read at `66c5b8dbf`.
- **Pending merge `0d1c1dda4`.** dShippedRelease's landing was not yet on origin/main when this record
  was written. It revises tr2 to rev-8: F6's holder verb is now TOOL-dPlacedRequest-34 S22's
  `--lease status build <slug>`. It also takes tr1 to rev-5 and wm6 to rev-6, and its dTendedCadence
  hunks are generated records rows only. Under rev-8 no RH row moves, because no dCalibratedLens spec
  reads a session, `lease`-mode class or epoch. wm6 rev-6 leaves S12, which row 136 rests on, as it
  was.
- **What it does not check:**
  - anything a parent's build run decides;
  - citations of deeper ancestors (dTotalRecall 131 mentions, dDeclaredLoop 94, dBoundRoles 10,
    dLinkedLibrary 6, dPlacedRequest 5, dGroundRules 4), which the brief put out of scope except
    tr2 through RH;
  - the 17 specs neither population reached.
  The RB probe reads only the files that both "Files touched" lists name, so a fact about a file
  either list omits is not reached. No skeptic re-ran the verdicts. Instead each re-ground writer
  re-reads both sides before it edits, and returns a row it cannot bear out as refused.

## The classes that turned up

- **A parent's later unit moved the surface.** The child cites an early unit and misses the later
  unit that moved its fact. Six rows: fh23 S15 adds a fourth parent literal (row 4); fh23 S35 owns the
  marker predicate (row 10); fh23 S42 moves `LENS_SLOTS` (row 115); fh16 S2 moves the receiver rule out
  of the hook, so the hook stops judging (rows 17 and 156); fh12 S2 moves the appendix parser into the
  factory (row 80).
- **A grammar the parent fixes, read loosely.** Nine rows: fh13's file order is slot order (row 6);
  fh13 F2's per-literal key uniqueness makes a tag name two rows (row 116); fh1 S3 adjudicates only
  tagged refs (row 94); fh1's known set has 65 rows (rows 95 and 152); fh25 runs two replays (row 96);
  fh32 S14 records two commits per replay (rows 97, 153 and 164).
- **A suite or runner the parent declares.** Six rows: fh12 F3's arms count in `run_selftest` (rows
  91, 154 and 165); fh14 S2's `case_evidence` hook (row 92); rp6's arm map (row 13); id3 AC7's literal
  key read (row 16).
- **A rule the parent states and the child copies short.** Six rows: tc1's `--key` admitted only with
  `--dry-run` (row 25); rp13 S2's four path refusals (row 107); tc48 S28's re-run journal (row 41);
  tc49/tc71's commit-carried landing (row 46); the owner's wm32 F6 (b) over a `git ls-files` reader
  (row 84); wm50's "no journal line" (row 142).
- **A file's at-base fact a parent changes (RB).** Four rows: fh17 S5 widens the `tier2-review
  self-test` guard (rows 167 and 168); tc7 S4 makes `[[exempt_leg]]` carry the whole row (row 102);
  tc9 S1 already owns `runlog.py reads` (row 131).
- **The wrong section, or a narrower reading.** Eight rows: `--stage` admits every marked literal, not
  only stages (row 9); the key forms only wm13 and tc29 give (row 26); wm53 S4, not S3 (row 59); a work
  order's nine slots (row 76); `read_act_records` reads no `Act` (row 83); wm12 S8's position-item
  fallback (row 87); the README replay procedure, not fh1 S5's clone (row 98); wm6 S12's act classes
  missing from `NOT_TRENDED` (row 136).

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | 1 | A | dFairHearing gives the harness a lens catalogue in `lenses.toml`, and four stage literals can be added to it (by name, with no id) | cite | AGREES | cl1:31-34; fh13:31-33 (S1), fh13:133-136 |
| 2 | 1 | A | A stage literal opens with `// gov:lens-slots <stage>` and holds the one line `{{LENS_SLOTS}}`, the form fh13 S3 gives | cite | AGREES | cl1:40-43; fh13:38-42, :171 |
| 3 | 1 | A | `PRESETS` (fh2 S1) gains four names; the marked receiver gains one ternary arm per literal | cite | AGREES | cl1:43-45; fh2:31-38, :137 |
| 4 | 1 | A | The receiver has seven literals in all (three from the parents plus four new) | cite | MISMATCH | cl1:143-145, :249, :319, :339; fh23:82-85 (S15), fh2:76, rp6:106-109 |
| 5 | 1 | A | fh2 S3's design-audit rows include `grounding`, `coherence` and `failure-envelope`, and those keys can recur under disjoint presets | cite | AGREES | cl1:47-49; fh2:40-43, :104-123; fh13:154, :336-342 |
| 6 | 1 | A | Slots follow file order, so each stage's new rows come first and the drawn rows follow in the table's order (deploy: `grounding` then `coherence`; maintain: `grounding`, `coherence`, `failure-envelope`) | cite | MISMATCH | cl1:163-176, AC1 :327-331; fh13:114, :172; fh2:104-123, AC2 :184-187 |
| 7 | 1 | A | Every stage row is `spec-audit` (rule 5); no key equals a literal name (rule 7); `cost` is legal beside the opt-in `cost` row because their presets are disjoint (rule 6, fh13 §8 F2) | cite | AGREES | cl1:176-179; fh13:152-155, :336-342; fh3:174 |
| 8 | 1 | A | `review_pin.py` (fh3 S8) reads the harness beside it the way `read_spec_subject_path` reads `SPEC_SUBJECT_PATH`; the subject mapping stands for `design`, `build` and an absent stage | cite | AGREES | cl1:51-56, :195-197; fh3:61-66, :191-197 |
| 9 | 1 | A | The literal set `--stage` admits is "a stage that a `gov:lens-slots` marker … declares" | cite | MISMATCH | cl1:51-54; fh13:133-136, fh2:36, fh23:82-83 |
| 10 | 1 | A | The marker set is read by a new `read_lens_literals` in `review_pin.py` | cite | MISMATCH | cl1:54-56, :220; fh23:153-156 (S35) |
| 11 | 1 | A | `PLAN_RECORD_PRESET` (rp6 S1) is `unit-spec` and is left for this build to re-point | cite | AGREES | cl1:56-57, :453-455; rp6:42, :69-71, :88 |
| 12 | 1 | A | AC5's fixture is a plan record whose first `**Serves:**` word is `plan`, as rp6 S3 plants | cite | AGREES | cl1:347; rp6:58-61, :180-181 |
| 13 | 1 | A | Re-pointing flips three rp6 arms in `tier2-review.test.sh`: its AC1, AC3 and AC4 | cite | MISMATCH | cl1:257-261; rp6:213, :195-197, :199-204 |
| 14 | 1 | A | rp6 S4's `help/loop.md` paragraph says the preset stays `unit-spec` until the Plan lenses land | cite | AGREES | cl1:261-263; rp6:62-65 |
| 15 | 1 | A | id3 S4's step 1a, with `DESIGN_REVIEW_WORKFLOWS` = `spec-review`, `spec-write`; `closing-review` is the Build review; id3 §3 and §8 F7 hand the other stages' effort to dCalibratedLens | cite | AGREES | cl1:33, :59-63, :208-211, :424-426; id3:60-69, :95-96, :170-178, :318 |
| 16 | 1 | A | Step 1a can be widened to `read_policy_setting(f"review.{stage}.effort", root)` | cite | MISMATCH | cl1:59-61; id3:70-73 (S5), :291-295 (AC7) |
| 17 | 1 | A | fh2 §4 measured a three-literal receiver as admitted by `agent-cap.js --only=scripts`, and AC3 re-measures the seven-literal receiver through the hook | cite | MISMATCH | cl1:143-145, :335-339; fh2:92-95; fh16:35-43 (S2), :229-232 (AC3) |
| 18 | 1 | A | AC2: `check-verifier-fanout.sh`'s `slots` line names each stage literal holding 5 | cite | UNKNOWN UNTIL BUILT | cl1:332-334; fh13:201, :207, :294-295; fh23:172-175 |
| 19 | 1 | A | fh2 S1 refuses `preset` beside the diff kind, and fh13 rule 5 admits one kind per literal (F2); v2:706's "dFairHearing's preset" is a spec-audit preset | cite | AGREES | cl1:397-402; fh2:31-34; fh13:152-153 |
| 20 | 1 | A | fh2 S5 logs the preset; fh13 escapes briefs | cite | AGREES | cl1:309-310, :316-317; fh2:47-49; fh13:182, :256-258 |
| 21 | 1 | A | fh3 and fh9 own the opt-in swap, lens notes after a swap and the six opt-in rows; `review.opt-in` is keyed by literal name; fh3 S11 files the six losing tests as an ask | cite | AGREES | cl1:97-102; fh3:39-43, :58-60, :67-69, :74-75; fh9:1, :38 |
| 22 | 1 | A | `review.<stage>.effort` row: `allowed` and `default` unchanged; no dTendedCadence or dFairHearing unit's §2 changes the row, `resolve_stage_efforts`, `stage-efforts`, `EFFORT_LEVELS` or `--trigger` | RB | AGREES | cl1:59-68, :75-77; catalogue.toml:1241-1245; probe: grep of every tc/fh spec for these names hits only fh11:354 (§10 prose); tc48:143-145 S37 touches only the workflow-count wording in `workflows.toml` |
| 23 | 2 | E | `run_cadence_period` sets `GOV_CADENCE_KEY` (and `GOV_CADENCE`) by ask TOOL-dTendedCadence-27 | cite | AGREES | cl2:78-79 · tc BACKLOG.md:13 ("accept `run_cadence_period` sets `GOV_CADENCE=<cadence>` and `GOV_CADENCE_KEY=<period key>`"), :48 DEFERRED; tc1:68-69, :304-307 |
| 24 | 2 | E | Inside unit 3's walk, `price` reads its key from `GOV_CADENCE_KEY` | RK | AGREES | cl2:124-125 · tc1:68-69 |
| 25 | 2 | E | `price --key <key>` writes a snapshot, and no refusal is stated for a missing key | RK | MISMATCH | cl2:77-80, AC5 cl2:406-409 · tc1:69-70, AC3 tc1:251-253 |
| 26 | 2 | E | The key grammar admits `^\d{4}-\d{2}$` and `^n\d+\.[0-9a-f]{12}$` as well as the weekly form | RK | MISMATCH | cl2:209-210 · wm13:54-55 (`derive_period` gives `weekly` `2026-W44` and `daily` only); tc BACKLOG.md:15 (tc29 adds `every-session` only) |
| 27 | 2 | E | The policy route: a bounded 30 s `policy.py get` subprocess through the inline `resolve_kit_dir`, with a refused read taking the default plus one line (TOOL-dTendedCadence-6 S1) | cite | AGREES | cl2:46-50, :494 · tc6:46-51 |
| 28 | 2, 26 | E | The flake record's name, its `Ended` field in the `- **Key:** value` grammar, its tsv rows `<leg>\t<first rc>\t<re-run rc or ->` with one row per executed leg, and that `retry-only` writes none while `quarantine` writes one (TOOL-dWitnessedBar-8 S3, S4) | cite | AGREES | cl2:67-72, :162-164, :273-275; cl26:35-37, :83-84 · wb8:48-51, :61-65, :128-149 |
| 29 | 2, 26 | E | A flake record is written for every Test-step bar, so it is "the committed per-leg verdict" and observes green legs | cite | UNKNOWN UNTIL BUILT | cl2:162-164; cl26:36-37, :166-167 · wb8:45-46 (the `flakes` route only for a red leg whose re-run reads `ok`), wb3:65-68 (`route` runs "on every red bar"), against wb30:37-40 ("A Test-step bar therefore executes the leg and `test.flakes` records its row") |
| 30 | 2, 4, 37, 46, 47 | E | The leg declaration: a `[[gate_leg]]` row in the kit descriptor or an `[[exempt_leg]]` row holding the whole row, the `[gate_leg.gov]` sub-table, `leg_factory.py new`, `--write` rendering the manifest and `--check` exiting 1 (TOOL-dWitnessedBar-11 S1 to S3) | cite | AGREES | cl2:111-115; cl4:80-84; cl37:74-75; cl46:36-45, :81-84; cl47:34-40 · wb11:36-50 |
| 31 | 2, 46 | E | A `loop-review selftest` row hand-written into `tools/gate-legs.json` before the factory lands ends up as a `[[gate_leg]]` row of `tools/loop/kit.toml` | cite | UNKNOWN UNTIL BUILT | cl2:114-115; cl46:38-40 · wb11:36-38 ("a `[[gate_leg]]` row in its kit's descriptor when an adopter receives it, else an `[[exempt_leg]]`"), :73-74 (S8) |
| 32 | 2 | E | `runlog.py journal --producer gates` / `--by-leg` as at base, which id 27 widens with `--since` and `--until` | RB | AGREES | cl2:72-74, :280-284 · tc6 S1, S2 (`read_run_record_policy`, `cmd_record`) and tc9 S1 (`reads`) change runlog.py, and none touches `journal` (`grep -- '--by-leg\|cmd_journal'` over the tc and fh specs: no hit) |
| 33 | 2 | E | The catalogue rows `review.loop.catch-source` and `review.loop.window-days`, and `verdict.flakes` defaulting to `quarantine` | RB | AGREES | cl2:156-164 · `grep 'review\.loop\|verdict\.flakes'` over the tc and fh specs: no hit |
| 34 | 2, 4, 46 | E | `tools/loop/kit.toml` gains this build's `[[gate_leg]]` rows | RB | AGREES | cl2:336; cl4:251; cl46:100 · tc18:125-128 adds two loop-kit rows of its own, which is additive and contradicts no stated fact |
| 35 | 2 | E | The `record-kinds.toml` row, the `HYGIENE.template.md` kind list and check-3 prose, the `help/README.md` line, and the `subject-pins.tsv` and `selftest-budgets.txt` regeneration | RB | AGREES | cl2:339-348 · tc6 S8, tc4, tc8, tc17 and tc43 add other kinds' rows; fh23:182, fh34:25 and fh40:95 edit other prose and the version markers; tc15:117, tc48 S34 and fh17 add other help lines; fh27 and fh23 regenerate the pins and budgets. None changes a fact these specs state. |
| 36 | 3 | C | The build-run preconditions are wm59 S1–S3 (point, row check, tick), wm13 S5 and S6 (`derive_period`, `run_cadence_period`) and wm27 S1 (`intake.py file --origin cadence`). | cite | AGREES | cl3:40-48, :153, :537-540 · wm59:35-60, wm13:54-69, wm27:33-39 |
| 37 | 3 | C | Ask tc27: `run_cadence_period` sets `GOV_CADENCE_KEY`; its severity line says a program that re-derives its period can disagree with its lease. | cite | AGREES | cl3:43, :68, :394-395 · BL:13, BL:32, tc1:301-307 |
| 38 | 3 | C | Ask tc29 gives a cadence row `period-key`; `derive_period` takes `daily` and `weekly`, and tc29 adds `every-session`. | cite | AGREES | cl3:43, :76, :172-173 · BL:15, wm13:54-56, tc2:308-313 |
| 39 | 3 | C | Ask tc30 gives the `session-start` host; `maintain.host` defaults to `session-start`, so the review runs at session start. | cite | AGREES | cl3:44, :411-412 · BL:16, tc2:50-55, :148-150, catalogue.toml:1146 |
| 40 | 3 | C | The `loop-review` row sits at `point.cadence-items` with `host-key = "maintain.host"`, the expansion's one host key. A row requires a `host-key` naming a catalogue row. | cite | AGREES | cl3:73-79, :473-478 · wm59:35-46, tc11:58-59, tc13:35, tc2:36-37 |
| 41 | 3 | C | "This is TOOL-dTendedCadence-1 S2's walk"; after an exit 1 the next wake runs the period again. | cite | MISMATCH | cl3:61-63 · tc48:123-125 |
| 42 | 3 | C | Exit 1 releases the lease as a hand-over (wm13 S6 step 5). | cite | AGREES | cl3:61-63 · wm13:67-69 |
| 43 | 3 | C | `item.loop.lease`'s actor is the executor, spelled as `item.maintain.lease` is (tc1 S1). | cite | AGREES | cl3:197 · tc1:177 |
| 44 | 3 | C | The period segment admits a dot, as tc2's `<event>.<sha12>` keys do. | cite | AGREES | cl3:190-191 · tc2:365-368 |
| 45 | 3 | C | The `file` item files through `intake.py file --origin cadence --filer`. Its text carries no period, so the content key is the filing key, a recurrence is `seen` and a new key is `filed` (wm4's rule, the route tc15 S2 takes). | cite | AGREES | cl3:96-100, :396-398 · wm27:33-39, wm4:47-49, tc15:65-69 |
| 46 | 3 | C | The record lands as a records-only intake with JSON text that the patch build re-writes, "as TOOL-dTendedCadence-1 S6 lands a maintenance record". | cite | MISMATCH | cl3:108-112 · tc71:36-40, tc49:48-51, :141-143, wm4:54 |
| 47 | 3 | C | The home follows `maintenance-record` (tc6 S6, S8) under `point.memory.record-home`, with a contained atomic write. | cite | AGREES | cl3:245-246, :541-542 · tc6:210-215, :386-392 |
| 48 | 3 | C | tc1 F1 placed Maintain's rows in its kit descriptor and rejected `loop.toml` against EX-1. Ask tc25 says `read_items` reads only `loop.toml` and `check_program` needs a `[[step]]` exit row. The ponytail names tc25. | cite | AGREES | cl3:302-309, :501-514 · tc1:286-291, :211-214, BL:11 |
| 49 | 3 | C | tc2 §4 already ran the literal-rows test: such rows certify empty periods. | cite | AGREES | cl3:388-391 · tc2:302-306 |
| 50 | 3 | C | `cadence.py` is `tools/runtime/cadence.py`, which wm59 builds. | cite | AGREES | cl3:260, :430 · wm59:43-50 |
| 51 | 3 | C | The program reads its key from `GOV_CADENCE_KEY`. `--key` works only with `--dry-run`. With no key it exits 2 with `refused: no key; run under cadence.py run loop-review`. | RK | AGREES | cl3:65-72, :419-423 · tc1:68-71, :251-253, BL:13 |
| 52 | 3 | C | The `weekly` key is the ISO week, `^\d{4}-W\d{2}$`. | RK | AGREES | cl3:184 · wm13:54-56 |
| 53 | 3 | C | The `monthly` key is `YYYY-MM` and the `every-n-landings` key is `n<k>.<sha12>`, the tick deriving both. | RK | UNKNOWN UNTIL BUILT | cl3:185-186, :479-491 · wm13:54-56 gives only `daily` and `weekly`; tc29 adds only `every-session` (tc2:310-311) |
| 54 | 3 | C | Reads no lease session, `lease`-mode class or epoch. | RH | AGREES (not bound, see 4) | cl3:65-67 |
| 55 | 3 | C | RB `tools/runtime/points.toml`: one new row; no at-base fact about the file. tc2, tc11 and tc13 add rows only. | RB | AGREES | cl3:73-79 · tc2:36-49, tc11:58-59, tc13:35 |
| 56 | 3 | C | RB `tools/policy/catalogue.toml`: the `review.loop.*` rows answer `weekly` and `60`; `maintain.host` defaults to `session-start`. No parent unit edits `review.loop.*`; tc2 S8 keeps `maintain.host`'s values and default. | RB | AGREES | cl3:169-171, :411 · tc2:107-110; `grep -rn "review\.loop\."` over the tc and fh specs printed nothing |
| 57 | 3 | C | RB `tools/memory-tree/record-kinds.toml`: a new row; tc4, tc6, tc17 and tc43 add or read other rows. | RB | AGREES | cl3:113-114, :231-243 · tc6:100-104 |
| 58 | 3 | C | RB `HYGIENE.template.md`: the closed `<kind>` list gains `loop-review`. fh23 and fh40 change only review-guidance sentences. | RB | AGREES | cl3:272-274 · fh23:182, fh40:94-95 |
| 59 | 4 | E | `derive_estimate_hours` is TOOL-dWellOiledMachine-53 S3 | cite | MISMATCH | cl4:124 · wm53:54 (S3 is `read_node_ledgers`), wm53:61-68 (S4 holds `derive_estimate_hours`) |
| 60 | 4 | E | `P90_MIN_ROWS` is 10 (wm53) | cite | AGREES | cl4:373 · wm53:68 |
| 61 | 4 | E | The spend trend is a p90 (TOOL-dWellOiledMachine-51 S3) | cite | AGREES | cl4:125 · wm51:50-53 |
| 62 | 5 | B | fh8 S8 gives the tenth column `disposition`, after `classes`; `units` goes after it (cl5:45-46, :58, :423-425, :565) | cite | AGREES | fh8:66-67 |
| 63 | 5 | B | `FINDING_SCHEMA` and `SPEC_FINDING_SCHEMA` are the finding schemas that gain `units` (cl5:56-58) | RB (`tier2-review.template.js`) | UNKNOWN UNTIL BUILT | fh18:47 (S4) and fh18:169-173: the whole-design walker schema is "`SPEC_FINDING_SCHEMA` … plus a required `walk` array" |
| 64 | 5 | B | The act record is written once per harness session (cl5:495, F1 b) | cite | AGREES | wm32:74, :86-87 "writes it once, at the act's exit" |
| 65 | 5 | B | `P90_MIN_ROWS` floor is 10 (cl5:509, F3 b) | cite | AGREES | wm53:273-276 |
| 66 | 5 | B | A new `review_replay.py --confirmed-rows` verb prints `parse_appendix_rows`' rows (cl5:305-307) | RB (`review_replay.py`) | AGREES | fh12:40-47: the parser moves to the factory, but `review_replay.py` "keeps its CLI … importing the moved names", so the fact survives |
| 67 | 5 | B | The `review.loop.retire` row at `catalogue.toml:1289-1293` has no `summary` (cl5:124-125, :180) | RB (`catalogue.toml`) | AGREES | No tc or fh spec names `review.loop.retire` (grep). Base catalogue `:1289-1292` and `unsummarised-keys.txt:192` read |
| 68 | 5 | B | A new `PARITY_ROWS` row in `resolve-python.test.sh` (cl5:310) | RB | AGREES | tc18:49 adds a row the same way. Base `:351` read |
| 69 | 5 | B | The keep kind joins `record-kinds.toml` and the HYGIENE kind list (cl5:359, :371-372) | RB | AGREES | tc4/6/17/43 and fh23/34/40 add their own rows or reword lines. None changes the row form or the list grammar cl5 writes to |
| 70 | 6 | C | rp1's scout cites `render_handoff` at `handoff.py:312`. | cite | AGREES | cl6:376-378 · `grep` found `tools/roles/handoff.py:312: def render_handoff`, also at `8bec4cef` |
| 71 | 6 | C | RB `tools/roles/README.md` and catalogue `memory.item-budget`: tc10 re-renders the catalogue region, fh23 the marker line, tc48 S37 a count. No parent edits `memory.item-budget`, `MARKER_RE` or the `check` and `roster` verbs. | RB | AGREES | cl6:33-34, :72-74 · tc10:60, :192; fh23:75; tc48:145 |
| 72 | 7 | E | The non-review act's shape-run record comes from `gov_record.py new shape-run --act`, with `Kind` `act`, `Workflow`, `Shape`, `Shape-match`, `Agents`, `Efforts`, `Out-tokens` and `Caused-by`, as wm19 §8 F2's ask of dTotalRecall (TOOL-dWellOiledMachine-19 S6) | cite | AGREES | cl7:24, :33, :64-65, :89-91, :224 · wm19:81-87, :228-237 |
| 73 | 8 | B | fh8 S8's `disposition` column comes before `units` and `cause` (cl8:37, :46, :115, :122) | cite | AGREES | fh8:66-67 |
| 74 | 8 | B | fh8 S7 allows exactly one disposition per finding, in four forms (cl8:103-104, :295-301, :353-354) | cite | AGREES | fh8:56-62 |
| 75 | 8 | B | "A workflow script has no filesystem", as fh13 §4 cites the map (cl8:108-109) | cite | AGREES | fh13:99; `review-harnesses.md:48` |
| 76 | 8 | B | A work order is the union of "the slices, the `map` slot and the `code` slot" (fo4 S1), so its paths are those three together (cl8:60-61) | cite | MISMATCH | fo4:37-38: `ORDER_SLOTS` has nine points, and fo4:51 makes the `bug-classes` slot print each class's path |
| 77 | 8 | B | The map state is read from the line `slot map · filled` (cl8:67-69, :255) | cite | AGREES | fo4:35-36, fo12:121 |
| 78 | 8 | B | The `code` slot exists, and the not-in-view cause is this build's to compute (cl8:39, :97, :115) | cite | AGREES | fo17:44-46 (S1); fo17:86 "The not-in-view cause computed from the `code` slot: dCalibratedLens (`cl-dClosedLoop-0465`)" |
| 79 | 8 | B | AC6's dTendedCadence handoff carries a `role=gov-spec-writer` marker (cl8:270-273) | cite (tc1) | AGREES | Probe: `…-TOOL-dTendedCadence-1-5-spec-writer.md:5` `<!-- gov:handoff role=gov-spec-writer build=dTendedCadence unit=- …>`. Three `-reuse-scout.md` siblings exist |
| 80 | 8 | B | `parse_appendix_rows`, `extract_line_ref`, `extract_subject_pins`, `read_record_kind` and `LINE_REF` live in `review_replay.py`, and id 33 factors `parse_appendix_rows` there (cl8:48, :53-54, :128, :137-138, :150, :186-192, :216, :338) | RB (`review_replay.py`) | MISMATCH | fh12:40-45 (S2) moves these, `review_replay.py:87-305` and the constants `:64-81`, "into the factory unedited". Base probe: `LINE_REF` `:74`, `extract_line_ref` `:87`, `extract_subject_pins` `:127`, `parse_appendix_rows` `:151` |
| 81 | 9, 12 | D | The act record carries `Item`, `Tokens-In`, `Tokens-Out` and `Wall`, and `trace.cost` writes `withheld` (cl9:34, :238; cl12:33, :77) | cite | AGREES | wm32:85-86 field list; wm32:97-99 `tokens` writes `Wall: withheld`, `none` writes all three `withheld` |
| 82 | 9, 12, 17 | D | `read_act_records(repo, build=None)` exists in `ledgers.py`, the runtime kit's one act reader (cl9:35, :334; cl12:34, :151-152, :223; cl17:37, :46-48, :222) | cite | AGREES | wm53:69-77 |
| 83 | 9, 16 | D | `ledgers.py acts` "calls `read_act_records(repo, build)` once" and prints `act` per record; cl16 id 50 maps each `Act` to its build and `Item` through it (cl9:40-43; cl16:52, :193-195) | cite | MISMATCH | wm53:76-77 reads only `Item`, `Wall`, `Tokens-In`, `Tokens-Out` per row |
| 84 | 9 (id 51) | D | `acts` reads the tracked act records with one `git ls-files` and one `git cat-file --batch`, "never one `gov_record.py show` per act" (cl9:183-188) | cite | MISMATCH | wm53:70-77 reads through `find` plus `show` per row; wm32:322-329 owner fork F6 rejected (c), the `git ls-files` listing, and picked (b) `find --all` |
| 85 | 9 | D | `Gov-Act: <act>` is written on act commits, and an owner's commit carries none (cl9:35, :55-56, :288, :335) | cite | AGREES | wm33:40-45; wm33:48-50 commit queue |
| 86 | 9, 16 | D | The journal is node-local `<git common dir>/runlog/runtime.log`; `PRODUCER_FILES` gains `runtime` in both copies; `compaction` is a class (cl9:36, :69-71, :95-96; cl16:42-45, :115-117) | cite | AGREES | wm16:56-63 |
| 87 | 9 | D | A `compaction` line carries `item=<tag\|none>`, and "an act-less session counts as `unattributed`" (cl9:37, :310-314, :341) | cite | MISMATCH (second half only) | wm12 S8: "The item is the act record's `item` for an act session, else the item TOOL-dDeclaredLoop-7's `position.py <slug> --json` names for the binding's build, else `none`" |
| 88 | 9, 12 | D | Wall time, and the reservation estimate per item kind, are wm53's (cl9:98-99; cl12:62-63) | cite | AGREES | wm53:65-69 |
| 89 | 10 | B | The factory `replay_scorer.py` holds `INSTANCES`, `read_raw_output` and `derive_paired_cases`, and a third instance is one more row (cl10:34-35, :102, :114, :120, :422) | cite | AGREES | fh12:30-39 ("It holds the `INSTANCES` table"), fh12:146-147 ("a third adds a row") |
| 90 | 10 | B | The factory re-derives every figure from committed outputs and runs no agent (cl10:380-382, F2) | cite | AGREES | fh12:21-22, fh12:90-91 |
| 91 | 10 | B | The instance's arms are `--fixture --plant` cases "run inside `review-replay selftest`" (cl10:311, :362) | cite | MISMATCH | fh12:166-168 and F3 fh12:315-317: later arms go in `replay_scorer.run_selftest` and count against `ARMS_DECLARED`. fh12:130-135 lists no `--fixture` mode |
| 92 | 10 | B | The new `INSTANCES` row needs only readers and a measure function (cl10:62-70, :201, :422) | RB (`replay_scorer.py`) | MISMATCH | fh14:41-44: each instance must declare `case_evidence`, and "An instance registered without the hook refuses at load" |
| 93 | 10 | B | A case's known rows are fh1's grammar: a `**Population:**` line and `\| tag \| address \| grade \| escaped \|` rows, read by `parse_known_set` (cl10:36, :42-44, :154-158) | cite | AGREES | fh1:47-57 |
| 94 | 10 | B | A case built from a finding (`address` is the row's `ref`, e.g. `:[§10]`) is scored through fh1 S3's adjudicated matches (cl10:48, :158, :170-171, :189-190) | cite | MISMATCH | fh1:59-61: a pair's `ref` must cite "the known row's `[tag]`". fh1:238-240 (AC2) exits 2 on a pair that cites none. fh12:50-51: a tag is "a lower-case slug in brackets" |
| 95 | 10 | B | The seed's `**Known:**` is fh1's known set, and its no-score baseline is `0/59` (cl10:72-74) | cite | MISMATCH | fh1:49 "`**Population:** 65 · reviewed 59 · escaped 6 · high 8`"; fh1:234-235 "returns 65 rows" |
| 96 | 10 | B | fh25's verdict record states one "reviewed score" for the seed's replay (cl10:73-74, :216-218) | cite | MISMATCH | fh25:34-35 "the two design-audit runs"; fh25:181-184 "Each run's … prints `reviewed <k>/59`" |
| 97 | 10 | B | The seed's `**Replayed:**` sha (and `**Base:**`) come from fh25's replay (cl10:73, :146, :161) | cite | MISMATCH | fh32:82-90 (S14) supersedes fh25 S6's single commit: the record names an orchestrating commit and each clone's `HEAD` separately. fh25:39-41 and fh32:103-107: the clone's `HEAD` is a transient placement commit |
| 98 | 10 | B | A replay runs "in an isolated clone at `**Base:**` as TOOL-dFairHearing-1 S5 runs its replay" (cl10:94-95) | cite | MISMATCH | fh25:26-27: fh1's clone step "exits 128". fh23:89-92 (S17) and fh32:99-101 (S17): the README replay section is "the procedure every later replay runs" |
| 99 | 10 | B | The seed loads lenses.toml, the three rendered audit agents and the charter template (cl10:75-79, :257-263) | cite (fh13, by surface) | AGREES | fh13:31 creates `tools/workflows/lenses.toml` at order 1, before fh25 at order 20. It is absent at HEAD (probe) |
| 100 | 10 | B | Those six paths are what fh25's replay agents loaded (cl10:78, :163) | cite | UNKNOWN UNTIL BUILT | fh1:143-148: `scriptPath` is this repo's `tier2-review.js`, `repo` is the clone at `6cfd21619` |
| 101 | 10 | B | The appendix row is fh8 S8's columns plus `units`, read by header name (cl10:189) | cite | AGREES | fh8:66-67 |
| 102 | 10 | B | A gov-only leg is a hand row in `gate-legs.json` plus an `[[exempt_leg]]` row shaped like `tier2-review self-test`'s, i.e. name and why only (cl10:62-68, :132-133, :277-278) | RB (`gate-legs.json`, `registry.toml`) | MISMATCH | tc7:82-87 (S4): the `[[exempt_leg]]` row "carries the leg's whole row under TOOL-dWitnessedBar-11 S1", and "`tools/gate-legs.json` is that row's render through `leg_factory.py --write`" |
| 103 | 10 | B | The `project-owned` rule at `kit.toml:36-37` gains `evals/**` (cl10:65-66, :134) | RB (`kit.toml`) | AGREES | fh16:69 widens the same rule "as it withholds its siblings". Base `kit.toml:35-37` read |
| 104 | 10 | B | The budget row, subject pin and `help/roles.md` / README sections are added (cl10:93-96, :226-228, :281-282) | RB | AGREES | fh23, fh27 and tc10/fh4/fh11 add rows or sections only. No parent §2 changes the row grammar these lines rely on |
| 105 | 11 | C | `decide_owner_items` (wm48 S4) walks the open owner items; one shared reader can be pulled out of it. | cite | AGREES | cl11:38, :72, :98, :343-344 · wm48:34-38 |
| 106 | 11 | C | `find_plan_record` and `read_plan_fields` are rp16 S4's. `derive_affected_systems` is rp13 S3's, with its degraded floor (rp13 S5). rp13 hands scope drift to dCalibratedLens. | cite | AGREES | cl11:38, :65-66, :334, :345 · rp16:78-86, rp13:52-66, :119-120, :134 |
| 107 | 11 | C | `drift --paths` refuses an entry "as TOOL-dRankedPlan-13 S2 refuses a scope path". | cite | MISMATCH | cl11:212-214 · rp13:52-54 |
| 108 | 11 | C | Reads policy through a bounded subprocess found by the inline `resolve_kit_dir`, as tc6 S1 does. | cite | AGREES | cl11:160-162 · tc6:46-50 |
| 109 | 11 | C | wm4's intake home `<git-common-dir>/requests/*` is node-local. | cite | AGREES | cl11:298-301, :359-360 · wm4:40-41, :79 |
| 110 | 11 | C | RB runlog files: the `rounds` verb sits beside `check-records`, and the record's `rounds` rows are read through `parse_record`. tc6 S1, S2 and S10 and tc9 add a policy read, a write rule, an anomaly list and the `reads` verb; none touches `rounds`. | RB | AGREES | cl11:55-63, :266-270 · tc6:46-60, :109-112, tc9:23 |
| 111 | 12 | D | `derive_build_spend` sums a build's act records read through `read_act_records` (cl12:22, :64-65, :224) | cite | AGREES | wm51:41-44 (S2) |
| 112 | 12 | D | An act record's date is the `<date>` its file name opens with, minted by the door at the act's exit (cl12:92-93, :203-206) | cite | AGREES | wm32:81-82 id-rule `<date>-build-<unit id>-act-<n>.md`; wm32:86-89 written once at exit, door mints `<date>` |
| 113 | 12 | D | The act record's `Epoch` field is the lease epoch (cl12:204) | cite | AGREES | wm32:50 "`epoch` (the lease epoch, or `none`)"; wm32:85 |
| 114 | 13 | A | fh13 moves gov's lenses into `lenses.toml`; the lens kind, namespace and overlay rows are dCalibratedLens's | cite | AGREES | cl13:22-24; fh13:72-73 |
| 115 | 13 | A | The slot count lives in `check-verifier-fanout.sh` (`parser=…check-verifier-fanout.sh#LENS_SLOTS`), "its one home in the fan-out leg" | cite | MISMATCH | cl13:33-34, :67-72, :168, :173-176; fh13:204 vs fh23:172-175 (S42), fh13:89 |
| 116 | 13 | A | A tag `lens.<key>` per row is derived from the key alone; AC1 prints one tag per row and `gov_tag.py show lens.coherence` resolves to "that row"; AC7's member count equals the catalogue's row count | cite | MISMATCH | cl13:45-46, :185, :278-283, :301-303; fh13:154, :336-342; fh2:40-43; fh3:172-174; step_gate.py:32-33 |
| 117 | 13 | A | A gov row is `default_in = []`, `optin = false` until its losing test (fh13 §4); the key pattern is `^[a-z][a-z0-9-]*$`; `check_catalogue` can gain a rule | cite | AGREES | cl13:53-55, :185-187, F3; fh13:126, :138-139, :143-160 |
| 118 | 13 | A | fh3 S6 renders `OPTIN_LENSES` from `optin = true` rows; an `adopter-<name>` key passes fh3 S1's key check | cite | AGREES | cl13:63-64, :265-267; fh3:35-37, :55-57; fh23:78-81 |
| 119 | 13 | A | `review.opt-in`'s grammar is fh3 S9's map; the catalogue spells it as a set (F2's ask on dFairHearing) | cite | AGREES | cl13:73-74, :326-338; fh3:67-69; catalogue.toml:417-422 |
| 120 | 13 | A | A `[[class]]` row in `surface-classes.toml` (sp10 S1); the reader contract at `step_gate.py:32-35`; `--fixture --plant`; the `RED … vanished` line | cite | AGREES | cl13:83-93; sp10:42-46 (CLOSED); step_gate.py:32-35, :65, :253; surface-classes.toml:1-12 |
| 121 | 13 | A | The leg is made by `leg_factory.py new` (wb11) as a `[[gate_leg]]` row rendered into `gate-legs.json` | cite | AGREES | cl13:94-96; wb11:36-50 |
| 122 | 13 | A | The leg kind keeps its class functions in its own kit's module (wb28) | cite | AGREES | cl13:356-357; wb28:126-130 |
| 123 | 13 | A | `tools/workflows/kit.toml`, `gate-legs.json`, `subject-pins.tsv`, `selftest-budgets.txt`, `govkit/selftest.py`: a row is added, and no at-base fact is relied on | RB | AGREES | cl13:94-96, :231-234; fh16:64-70, fh23:122-125, fh27 (row additions only) |
| 124 | 14 | A | Swap removal stays fh3's `optIn`; the run literal is fh3 S8's preset; an exclusion compiles to an fh3 S2 swap; the literal keeps five (fh13 §8 F3) | cite | AGREES | cl14:35-40, :154, :161, :373-377; fh3:39-43, :61-66; fh13:343-347 |
| 125 | 14 | A | A replay is fh12's `replay_scorer.py`, run by whoever chooses to; `replay` names its committed output | cite | AGREES | cl14:44-47, :105-106, :121; fh12:30-31, :91, :229 |
| 126 | 14 | A | fh13's `check_catalogue` rule 2 is amended "where that unit lands it" to admit `replay` on an overlay row | cite | AGREES | cl14:239-243; fh13:148-149 |
| 127 | 14 | A | `flow.promote` row: `allowed` and `default` as at base; no parent changes it or the `instructions.exclude` read in `unattended.sh` | RB | AGREES | cl14:47-54, :135-137; catalogue.toml:826-830; probe as in the cl1 RB row (no hit) |
| 128 | 15 | E | Each `warned` and `warn.<k>` value is `<leg>\t<class>\t<subject>\t<unit>`, and a held, skipped or reused leg's marker is not read (TOOL-dWitnessedBar-29 S3, S7) | cite | AGREES | cl15:34-35, :45-46, :186-187, :289 · wb29 S3, S7 (`warn.<k><TAB><leg name><TAB><class><TAB><subject><TAB><unit>`), wb29:117-120 |
| 129 | 15 | E | The verdict record's `tree` key, or `-` (TOOL-dWitnessedBar-4 S1) | cite | AGREES | cl15:35, :49-50 · wb4:42-44 |
| 130 | 15 | E | No journal class records a breach (TOOL-dWellOiledMachine-16 `JOURNAL_CLASSES`) | cite | AGREES | cl15:418 · wm16:57, :160; `grep -rn 'breach'` over wm16, wm34, wm53, wm6, wm65 and wm79 finds no breach class |
| 131 | 15 | E | `runlog.py reads` is a new verb, and "no seam counts a document's reads" | RB | MISMATCH | cl15:53-54, :197, :415 · tc9:46-56 |
| 132 | 15 | E | The extract.py readers `resolve_projects_root`, `read_records` and `derive_tool_class` survive unchanged | RB | AGREES | cl15:57, :164, :267 · tc9:48-51 reuses them unchanged; tc43 only cites `read_records` |
| 133 | 16 | D | `journal.py` has the verbs `write` and `prune`, and `classes` joins them (cl16:30-31, :357) | cite | AGREES | wm16:65-68 (S4), :69-79 (S5) |
| 134 | 16 | D | `point.journal-readers`: a reader opens a file only through `read_journal`, and runlog is the first reader (cl16:44-45, :226-227, :355-356) | cite | AGREES | wm16:85-88 |
| 135 | 16 | D | wm79 S12 drops `budget-spent`, `deadline-passed`, `cycle` and `secret-hit` "which no unit writes" (cl16:87, :112-114, :308-313, :366-367) | cite | AGREES | wm79:93-95 |
| 136 | 16 | D | `NOT_TRENDED` lists the tuple's classes that are no stall or loop event: `refusal`, `compaction`, `map-read-outside-slice`, `hook-failure`, `ledger-refused` (cl16:33-37) | cite | MISMATCH | wm6:141-142 S12 adds `act-launch`, `act-adopt`, `act-killed`, `act-exit`, `relaunch` and `limit-hold` to `JOURNAL_CLASSES` |
| 137 | 16 | D | `ledger-refused` is wm53's class (cl16:36) | cite | AGREES | wm53:56-58 |
| 138 | 16 | D | `key=` is on `no-progress` and `repeat`; the progress ledger's `new: yes/no` rows are node-local (cl16:118, :133) | cite | AGREES | wm46:41-50 (S1), :51-54 (S2), :55-63 (S3) |
| 139 | 16 | D | `rule=` is on `refusal` and `breaker-open` lines (cl16:119) | cite | AGREES | wm49:42, :147-150 |
| 140 | 16 | D | `stall` is a class wm47 journals (cl16:224) | cite | AGREES | wm47:58-59, :79 |
| 141 | 16 | D | F1's ask: a `budget-spent` line when `record_draw` returns `exhausted`, and a `deadline-passed` line when a wm47 wait reaches its deadline (cl16:319-321) | cite | UNKNOWN UNTIL BUILT | wm79:93-95 drops both; wm47:58-59 journals `stall reason=hold-ceiling` at that point |
| 142 | 16 | D | wm50 "produce[s] the lines"; F1 asks for a `cycle` line keyed `act=` or `session=` when wm50 raises a cycle owner item (cl16:85-86, :322-323) | cite | MISMATCH | wm50:86-87 non-goal: "No journal line: a node-tick sweep carries neither the `act` nor the `session` key TOOL-dWellOiledMachine-16 S3 requires; the owner item is the cycle's record." |
| 143 | 16 | D | The journal is pruned by `runtime.journal`, 60 days by default (cl16:68, :228-230) | cite | AGREES | wm16:69-79; `tools/policy/catalogue.toml:512-514` default 60 |
| 144 | 16 | D | `runtime.act-ceiling` evidence is the act record's `Wall` (cl16:132) | cite | AGREES | wm32:85-86, :92-99 |
| 145 | 17 | D | `beat.py`, `NODE_BEAT_KEYS`, `members` judging live beats, the closed key set keeping project names out, `help/runtime.md` (cl17:35-36, :56-59, :80, :139, :219, :331) | cite | AGREES | wm52:37-49 (S1), :57-61 (S3), :70-77 (S5), :78-79 (S6) |
| 146 | 17 | D | `members` reads the `node-` fields through the read-only verb wm52 §8 F3 asks of dPlacedRequest, and parses no lease record (cl17:36, :58-59, :106-107) | cite | AGREES | wm52:221-234, RESOLVED (owner, 2026-10-29) to (a); wm52:73-77 |
| 147 | 17 | D | `read_node_ledgers`; the `plan.json` pool fields; an expired reservation reads released; ledgers sit outside every repository, and the own ledger knows no fleet tag (cl17:50-54, :92-93, :145-147) | cite | AGREES | wm53:37-44 (S1), :54-60 (S3) |
| 148 | 17 | D | `derive_estimate_hours` is the one estimate: nearest-rank p90 of `Wall` per `Item`, `P90_MIN_ROWS` 10, else `runtime.act-ceiling`; `tokens`/`none` keep it at the ceiling (cl17:41-49, :85-86, :120-122, :237-244) | cite | AGREES | wm53:65-69; wm53:273-276 (F2); wm53:246-250 (AC6, 0.15 h and 1.5) |
| 149 | 17 | D | `Wall: withheld` under `tokens` and `none` (cl17:38, :118) | cite | AGREES | wm32:97-99 |
| 150 | 20 | D | wm32 joins `act` to `TYPED_RECORD_KINDS` and HYGIENE's closed list in one pass (cl20:39, :174) | cite | AGREES | wm32:74-79 |
| 151 | 22 | C | The plant runs `run` with `GOV_CADENCE_KEY=2026-W45`, an ISO week key. | RK | AGREES | cl22:43, :124 · tc1:247, :268 (the same channel), wm13:54-56 |
| 152 | 23 | B | The seed's score and baseline are "the adjudicated score TOOL-dFairHearing-25's verdict record states" (cl23:35-37, :144, :181) | cite | MISMATCH | Same as the cl10 rows: two runs (fh25:34-35, :181-184), 65 known rows (fh1:49), and two commits per record (fh32:82-90) |
| 153 | 23 | B | Replayed sha = "TOOL-dFairHearing-25's replay"; the edits to the seed's loads since then are this build's units 5 and 1 (cl23:83-90) | cite | MISMATCH | Six parent units after fh25 (order 20) edit `tier2-review.template.js`. Files touched: fh27:227 (21), fh30:117 (21), fh35:144 (22), fh32:258 (23), fh37:186 (24), fh40:316 (26). §2 Scope: fh32 S1 (template `:1021`); fh40 S1 states unit 37 edits it |
| 154 | 23 | B | The `close-bar` `--fixture` plant is an arm inside `review-replay selftest` (cl23:53-57, :145, :156) | cite | MISMATCH | Same as the cl10 arm row: fh12:166-168, :315-317 |
| 155 | 24 | A | fh2's measurement cited the same bare `agent-cap.js --only=scripts` command | cite | AGREES | cl24:20-24; fh2:92-95 |
| 156 | 24 | A | The hook at `agent-cap.js` denies a looped receiver with `spawns one agent per item` (`agent-cap.test.sh:2325`), so the payload pipe can red and green the stage receiver | RB | MISMATCH | cl24:39-43, :64-69, :111-116; fh16:35-43 (S2), :64-67 (S5), :229-232 (AC3); agent-cap.js:1940-1943 at base |
| 157 | 27 | D | `intake.py file` is wm27's verb (cl27:66) | cite | AGREES | wm27:33-38 |
| 158 | 27 | D | `run_cadence_period` releases the lease as a hand-over on a non-zero exit, and the next wake re-runs the period (cl27:21-22, :83-84; by name, no unit id) | cite | AGREES | wm13:68, :126 |
| 159 | 27 | D | The plant supplies the key as `GOV_CADENCE_KEY=2026-W45`; `--key` is admitted only with `--dry-run` (cl27:52-53, :135, :140) | RK | AGREES | tc1:68-70; tc1:301-306 ask TOOL-dTendedCadence-27, `GOV_CADENCE_KEY=<period key>`, weekly key shape `2026-W44` |
| 160 | 28, 16 | D | `read_act_records` pages past `find`'s 40-row cap (cl28:35-36, :66, :137; cl16:194-195) | cite | UNKNOWN UNTIL BUILT | wm53:73-76 splits by `--paths` glob; wm32:325-329 (owner, 2026-10-29) says wm53 "meet[s] the same cap" and is served by `find --all` |
| 161 | 30 | C | Unit 3's F5 places the rows against tc1 F1 and ask tc25. | cite | AGREES | cl30:74-77 · tc1:286-291, BL:11 |
| 162 | 30 | C | Moving the preset flips three arms of rp6 (AC1, AC3, AC4), and rp6 S4 wrote `help/loop.md`'s Plan Review paragraph. | cite | AGREES | cl30:121-123 · rp6:180-200, :63, :213 |
| 163 | 30 | C | "The dFairHearing promoted-fix brief that caps a batch spec's size." The owner is `dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md` §2, ceiling 49152 bytes from `tools/template-size-limits.txt`. cl30 is 26913 bytes (`wc -c`). | cite | AGREES | cl30:374-378 · fh20 brief:14-19 |
| 164 | 36 | B | The replayed sha is fh25's; the edits since it are units 5 and 1 only (cl36:22, :26, :45-46, :86-90) | cite | MISMATCH | Same as the cl23 edits row (fh27…fh40) |
| 165 | 36 | B | The `seed-loads` `--fixture` plant (cl36:49-62, :105) | cite | MISMATCH | Same as the cl10 arm row |
| 166 | 41 | C | `record-refuses` runs with `GOV_CADENCE_KEY=2026-W45` "as the executor supplies it". | RK | AGREES | cl41:102 · BL:13, wm13:54-56 |
| 167 | 41 | C | At base, the `tier2-review self-test` guard is `{prefix}/workflows/` and `{prefix}/memory-tree/gen_build_index.py`. | RB | MISMATCH | cl41:151-152 · fh17:45-47, :183-184 |
| 168 | 46 | E | At base the `tier2-review self-test` guard is `{prefix}/workflows/` and `{prefix}/memory-tree/gen_build_index.py`, and S5 adds three entries to it | RB | MISMATCH | cl46:85-87, :57-59 · fh17:45-47, :183-184, AC8 fh17:299-301 |
| 169 | 47 | E | The `format-guard self-test` guard and its `[[exempt_leg]]` row (name and why only) as at base | RB | AGREES | cl47:68-72 · no tc or fh §2 names that leg (`grep 'format-guard self-test'` over the tc and fh specs hits §7 gate lines only) |

## UNKNOWN UNTIL BUILT

- Row 18 (cl1 AC2's `slots` line): fh13:207 and fh13 AC4 :294-295 disagree on whether the line names
  the literals, and fh23 S42 moves the count. dFairHearing's build run decides.
- Row 29 (cl2, cl26 flake records): whether `test.flakes` writes on every Test-step bar or only on a
  routed red bar. TOOL-dWitnessedBar-8's build run decides.
- Row 31 (cl2, cl46 the loop leg's declaration): a `[[gate_leg]]` in `tools/loop/kit.toml` or an
  `[[exempt_leg]]`. TOOL-dWitnessedBar-11's adopter test decides.
- Row 53 (cl3 `monthly` and `every-n-landings` keys): decided only when cl3's own §8 F2 ask is built
  on top of tc29. The ask is filed nowhere yet.
- Row 63 (cl5 `units` on whole-design findings): whether fh18's walker schema inherits
  `SPEC_FINDING_SCHEMA`'s item. fh18's build decides.
- Row 100 (cl10 seed `**Loads:**`): whether fh25's agents load this repository's files or the clone's.
  fh25's build run decides.
- Row 141 (cl16 F1's `budget-spent` and `deadline-passed` writers): wm79 S12 drops both classes.
  dWellOiledMachine's build run decides whether it takes the ask.
- Row 160 (cl28, cl16 `read_act_records` past `find`'s cap): wm53 S4's glob split or wm32 F6's
  `find --all`. dWellOiledMachine's build run decides.

## Rule-wide hits no rule binds

Each return's section 4 gives one line per hit. In summary:

- The `epoch` hits in cl1, cl10 and cl15 name a release epoch or a Unix time bound.
- The "lease holder's node" hits in cl9 and cl15 read the walk's own node.
- cl12:204's `Epoch` is a rejected option naming the act record's field.
- cl17 reads `node-` keys and `--claims` fields 2 and 5.
- cl3 and cl5 take or reject a lease without reading another session's holder.
- `review.loop.*` keys are dCalibratedLens's own catalogue rows.
- Every overlap in the RB files that is not a row of this table adds a row and changes no fact the
  child states.

## Re-ground

Five `gov-spec-writer` agents folded the brief
[`2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md),
at effort medium, with their handoffs beside it. Their returns are
[`2026-11-03-build-TOOL-dCalibratedLens-1-reground-returns`](2026-11-03-build-TOOL-dCalibratedLens-1-reground-returns.md).

- **Outcome:** of the 39 MISMATCH rows, 38 were folded, 1 was parked (row 9) and none was refused. Row
  162 is an AGREES that follows row 13. It was folded too, because row 13's fold made cl30's "three
  arms" false.
- **Specs revised, 17:**
  - 1 rev-4, 2 rev-5, 3 rev-5, 4 rev-5, 8 rev-4, 9 rev-3, 10 rev-5, 11 rev-3, 13 rev-3;
  - 15 rev-3, 16 rev-3, 23 rev-4, 24 rev-3, 30 rev-3, 36 rev-3, 41 rev-3, 46 rev-2.

  Each spec carries one §9 line naming the brief and its rows. Each has a spec-revised deviation
  record written by the main loop: `TOOL-dCalibratedLens-<n>-deviation-<k>` with (n, k) = (1, 15),
  (2, 25), (3, 35), (4, 45), (8, 85), (9, 93), (10, 105), (11, 114), (13, 133), (15, 153), (16, 163),
  (23, 233), (24, 242), (30, 302), (36, 362), (41, 412), (46, 462). Every spec is under 49152 bytes;
  the largest is cl3 at 46753.
- **§8 marks re-picked, two, both agent-delegated:**
  - cl9 F4 is re-worded to wm12 S8's position-item fallback.
  - cl16 F1 is re-picked to (b) for `cycle` alone, since wm50 §3 writes no journal line.

  No mark the owner resolved was changed.
- **The brief's own error:** it put tc1's `--key` rule at S2. Writer W5 found it at S3 (tc1:68-70),
  and cl2 cites S3.
- **What the folds do not check:** no reviewer re-read the fold text. Each writer re-read both sides
  before it edited, and probed that the contradicted child text is gone. Each ran memory hygiene over
  a copy of the index, and the only finding was the build-index render, which the main loop owes.

## Parked for the owner

- **Parent text that looks wrong (reported, not edited).** Each line is quoted in its return's section
  5:
  - dFairHearing:
    - fh2:92-95 and fh3:114-117 measure the hook with no named payload.
    - fh13:207 contradicts fh13:294-295 on the `slots` line.
    - fh13:204 says `LENS_SLOTS` has "one home" in the `.sh`, which fh23:174-175 moves to the `.js`.
    - fh1:136-139 still gives the clone recipe that fh25:26-27 says exits 128.
    - fh17:46-47 and :183 hand-edit a `gate-legs.json` guard that wb11 makes a render.
  - dTendedCadence:
    - tc1:100-104 still describes the readings-JSON landing that tc49 and tc71 replace.
    - tc15:66-68 appends a receipt to a node-local intake.
    - tc2:51 lists `requesting-node` as a `maintain.host` value the catalogue enum lacks.
  - dWellOiledMachine:
    - wm16:56-60 still lists the four classes that wm79:93-95 drops.
    - wm53:73-76 splits `find` on an act id that wm32 F4 keeps out of the file name.
    - wm53 S4 was not moved after wm32 F6's owner pick.
    - wm52 F3 and tr2 F6 (a) ask for overlapping lease-field verbs.
    - wm32:98's `trace.cost` line cite has drifted.
  - dWitnessedBar:
    - wb8:45-46 and wb3:65-68 contradict wb30:37-40 on when a flake record is written.
  - dRankedPlan:
    - rp6:213 declares no suite arm for its AC4.
  - Found by the writers, quoted in their returns' section 4:
    - fh25:63-66 (S6) still names "the commit the runs started from", which fh32 S14 supersedes.
    - fh14:43-44 (S2) gives review-replay's `case_evidence` the shape fh32 S11 replaces.
    - fh23:153-156 (S35)'s `--markers` prints line numbers only, so a caller that needs names re-reads
      the lines it numbers.
    - id3:295 says reader coverage cannot see a variable-built key, but `check_policy.py:428-429`
      admits an `f`-prefixed literal.
    - No fh16 unit names which unit moves the `agent-cap.test.sh:2325` arm.
    - tc48:123-125's S28 journal records only completed items, and tc48's own round-1 audit found holes
      in it.
- **Row 9 is parked: a kit edge for `--stage`.** cl1 S3's `--stage` should admit only `REVIEW_STAGES`
  members, which live in `tools/roles/roles_lib.py`. But the review-harness kit requires only
  `agent-cap` and `policy` (`tools/workflows/kit.toml:10`). Making `review_pin.py` read that set is a
  new fork:
  - (a) import it, adding `roles` to review-harness's `requires`, so the two kits name each other;
  - (b) move `REVIEW_STAGES` to `review_pin.py` as its one home, reached by `roles_lib.py` along the
    existing roles → review-harness edge;
  - (c) keep a second copy with a parity arm.

  Writer W1 recommends (b). cl1 is unedited on this row, and it still admits every marked literal
  (row 9's MISMATCH stands).
- **Row 96 rests on the writer's own derivation.** cl10 S5 now seeds a case from the lower of fh25's
  two runs, `fhr1` on a tie. fh25 S5 flips the switch only when both runs meet the bar, and a baseline
  from the higher run would turn `fell` red on run-to-run noise. The other choice is one seed per run.
  The parent does not decide it.
- **Row 83 widens a parent's function from this build.** cl9 S1 now widens TOOL-dWellOiledMachine-53
  S4's `read_act_records` to read `Act`, inside dCalibratedLens's build run. An ask on dWellOiledMachine
  may be owed instead.
- **Two asks no BACKLOG holds (pre-existing).** cl16 F1's ask, now narrowed to "TWO STALL AND LOOP
  CLASSES HAVE NO WRITER", and cl3 §8 F2's "THE PERIOD KEY HAS NO MONTH AND NO LANDING COUNT" are
  each spelled "the main loop files it". No `BACKLOG.md` holds either: `grep -rn 'HAVE NO WRITER\|NO
  MONTH' memory/builds/*/BACKLOG.md` prints nothing.
- **Fold text is unreviewed.** The 17 revised specs carry about 470 inserted lines that no reviewer
  read. Recommendation: before the build run, run one spec-audit round over these 17 specs.
- **The readers disagree on rp6's arms.** Group A judged cl1's claim that re-pointing flips rp6 AC1,
  AC3 and AC4 a MISMATCH (row 13). Group C judged cl30's sentence repeating it AGREES (row 162). The
  writer of cl1 re-reads rp6 and corrects cl30 to match whatever it folds, so the two specs agree.
- **Deeper ancestors.** dCalibratedLens cites dTotalRecall 131 times and dDeclaredLoop 94 times. The
  brief scoped both out apart from tr2 through RH. Pending merge `0d1c1dda4` takes TOOL-dTotalRecall-1
  to rev-5, re-scoping when a `hand` writer is legal, and dCalibratedLens cites tr1 19 times.
  Recommendation: a second pass over dTotalRecall and dDeclaredLoop, once `0d1c1dda4` lands.
- **dFairHearing holds a live run claim** (`refs/gov/runs/dFairHearing`, beat about 1300 s at the
  start of this pass). Its folder was read and never edited. A spec it revises after `66c5b8dbf` is
  outside this record.

## Owner ruling, 2026-11-03

The owner answered this pass's report with "go with (b) for row 9, rest with recommendations".

- **Row 9:** option (b). `REVIEW_STAGES` is homed in `review_pin.py`, and `roles_lib.py` reaches it
  along the roles → review-harness edge. Folded into TOOL-dCalibratedLens-1 rev-5 as §8 F7,
  `RESOLVED (owner, 2026-11-03): (b)`. Record:
  [`deviation-16`](2026-11-03-build-TOOL-dCalibratedLens-1-deviation-16.md).
- **Row 96:** kept as the writer derived it. cl10 S5 seeds from the lower of fh25's two runs, and
  nothing is edited.
- **Row 83:** kept in this build. cl9 S1 widens `read_act_records` inside dCalibratedLens's build run,
  and no ask is filed on dWellOiledMachine. This follows the owner's standing rule that no plan counts
  on a foreign build for functionality it can fold in.
- **The two unfiled asks:** filed as TOOL-dWellOiledMachine-128 (cl3 §8 F2) and
  TOOL-dWellOiledMachine-129 (cl16 F1). The second pass found five more asks no BACKLOG held, and filed
  those too.
- **Deeper ancestors:** run as the second pass once `0d1c1dda4` landed. Record:
  [`2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck`](2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md).
- **The spec audit over the fold text:** run after both passes' folds, over every revised spec.
- **A correction to the Re-ground section above:** "the largest is cl3 at 46753" was measured before
  the index render. After the render cl3 reads 51098 bytes, because its generated records region grew.
  No gate caps a spec's size, and 49152 was only the brief's acceptance line.
