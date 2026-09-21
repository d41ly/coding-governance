**Serves:** spec-audit TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7
**Commissions:** TOOL-aWokenSentinel-8..14

# aWokenSentinel — spec audit of the seven-unit set, round 1

*Node `a`, 2026-09-20. A Tier-2 adversarial pass over the seven specs before any code: a fan of four
primed finder lenses, a skeptic stage in five batches prompted to REFUTE each finding, one synthesis.
The mandate was underspecification, contradiction between sibling specs on the four axes (scope,
interface, ordering, acceptance), unstated assumptions about the harness and the driver, and criteria
that cannot fail, with every code claim checked against the cited file and line at the build's base
`5f9648d6`. The synthesis re-read at source every claim the blocker and the highs rest on; what it
re-read, and what it did not run, is listed at the end.*

**Round: 1.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-1.md@0ff841f7e14a1d0f979e0072f95c2b8f4ea40f0d`
- `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-2.md@05587878894fe8ba87f0d44bfd2d1ec6237f4190`
- `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-3.md@f38ae77cf2ad9e02445e294b5eec795ff1250e8e`
- `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-4.md@1e2e0b95c1344a15aa3263b4641754da40956ca8`
- `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-5.md@8ef99d269ba605882c8c761a498bc29289a7ea48`
- `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-6.md@68920c9cc1ebb474498b2d9f9e0e3c97ad61f727`
- `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-7.md@da5f86b312637b9a9b677fcb1992a2f5c6121af9`

## Verdict: BLOCKED

One blocker defect stands, and it is the build's own purpose inverted. `TOOL-aWokenSentinel-7` makes
`--landed` refuse until a stop-guard line recorded in phase `LANDING` exists, and its remedy tells the
session to END THE TURN so the stop-guard "records the listing and continues you". But `--landed` runs
after the lander by the Skill's own order, so at every point that refusal can fire the witness is
already on `origin/<default>`; `TOOL-aWokenSentinel-2` grades that `finished-unstamped`, and
`TOOL-aWokenSentinel-3`'s ratified decision table ALLOWS that stop. The turn ends, the idle-wake was
reaped before `--close`, the tick skips a non-STALE run, and the record sits at `LANDING` with its work
on `main` — the six-records defect the build cites as its motivation, now manufactured by the unit
built to close it. Six high defects follow. Two are contradictions between ratified siblings that red
a sibling's criterion or a merge-bar leg with no unit owning the fix (a second `--status` line against
the suite arm spec 5 F1 already measured; a `STOP_GUARD_BLOCKS` knob with no protocol row for check
22). Two are mechanisms that cannot work as written (the tick's `read_bound_key` calls never see a
declared key; the real-driver arms run in a fixture with an unborn HEAD). One orders a tree kill before
the check that decides whether anything can resume it. Every unit drew at least one confirmed finding.

## Review shape

Raw 54, confirmed 43, refuted 11, unverified 0, precision 0.80. Precision sits well above the ~0.5
floor §8 sets; the fan was sized right for this surface and no lens needs re-priming on that account.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by the pipeline's
dedup stage. The run is complete on its own terms. Because no lens died, no zero below is a zero from
absence; every unit was read by all four lenses. The pipeline's dedup found 0, but the 43 confirmed
findings contain many that name one defect from different lenses (four lenses found the second
`--status` line, three found the inline sidecar root, five found the dossier row). The fold below is
editorial: it groups them into 28 distinct defects and keeps every raw id. Each raw id takes the
severity of the defect it evidences, so the per-id tally and the integers returned with this report
agree by construction.

| Defect | Severity | Raw ids folded in |
|---|---|---|
| B1 the `--landed` refusal's remedy ends a turn the stop-guard allows; the run wedges at LANDING | blocker | 18, 29, 43 |
| H1 `--status` grows a second stdout line; the `:1874` arm and the driver header red | high | 1, 21, 30, 44 |
| H2 `STOP_GUARD_BLOCKS` has no section 8 row; check 22 reds from unit 3 to the close | high | 19, 31 |
| H3 spec 5 spells the sidecar root inline; spec 7 AC12 reds with no owner | high | 4, 20, 34 |
| H4 the tick kills a live tree before asking whether it can resume it | high | 22 |
| H5 the tick's `read_bound_key` calls never see a declared key | high | 26, 33 |
| H6 the real-driver arms run in a fixture with an unborn HEAD | high | 32 |
| M1 AC8 cannot fail; units 6 and 7 rewrite one dossier bullet | medium | 2, 25, 28, 37, 49 |
| M2 AC6 counts `read_bound_key` mentions: 5 at base, not 3 | medium | 5, 23, 41 |
| M3 spec 2 S5's four carriers have no criterion | medium | 6 |
| M4 spec 1 S6's suite prologue exports have no criterion | medium | 7 |
| M5 spec 3's knob and suite carriers have no criterion | medium | 8 |
| M6 spec 6's one-copy absent-owner rule is not observed | medium | 9 |
| M7 no unit writes `STOP_GUARD_BLOCKS=` into the root conf; spec 6 AC6 reds | medium | 24 |
| M8 `RESUME_STALE_BOUND_DEFAULT` derives from kit defaults, not the declared bounds | medium | 35 |
| M9 `STOP_GUARD_BLOCKS=12` sits above the harness's 8-consecutive cap | medium | 45 |
| L1 two announced skips in the walk have no criterion | low | 10 |
| L2 spec 2 S2 "exits 0 on any run-state file" contradicts §4 and AC8 | low | 11 |
| L3 `last-move-source: write` is never observed | low | 12 |
| L4 the NOTE's single-absent arms are unobserved | low | 13 |
| L5 `sidecar-unwritable` and the `LIVENESS_BOUND_MS` row are unobserved | low | 14 |
| L6 the `<kid\|none>` grammar's `none` arm is unobserved | low | 15 |
| L7 `stall-recorder.test.sh` in `project-owned` has no criterion | low | 16 |
| L8 three of spec 6 S2's Skill edits have no criterion | low | 17 |
| L9 spec 2 S2's key order differs from §4's | low | 27 |
| L10 the LANDING-is-close-only rule is cited to the wrong id | low | 50 |
| L11 `RUN.md:24` should be `:30` | low | 52 |
| L12 the roster row says `--close` | low | 53 |

Tally by raw id: **3 blocker · 13 high · 15 medium · 12 low** = 43. Severities RAISED from the
skeptic's verdict, argued where the defect is: 29 and 43 (skeptic: high) sit in B1, because one
defect has one severity and this one wedges every wired landing; 4 and 34 (skeptic: medium) sit in
H3, because a sibling's ratified criterion that reds on a line no unit is scoped to fix is the same
red-with-no-owner class as H2; 26 (skeptic: medium) sits in H5, because a mechanism that cannot work
as written and whose only observation passes for the wrong reason is not a medium on the unit's
central verb; 28 and 41 (skeptic: low) sit in M1 and M2 as further evidence of those defects. One
severity was folded DOWN: 2 (skeptic: high) sits in M1, because a vacuous criterion whose worst case
is a dossier sentence written twice reds no gate and wedges no run.

## Findings

| # | Sev | Unit(s) | Address | One line |
|---|---|---|---|---|
| B1 | blocker | TOOL-7, TOOL-3, TOOL-2 | TOOL-7 §2 S2, §4 'The read' (both refusal texts), §8; TOOL-3 §4 'The decision' row `FINISHED-UNSTAMPED`; TOOL-2 §2 S3 | The remedy ends the turn; at that point the witness is on `origin/<default>`, the verdict is `FINISHED-UNSTAMPED`, and spec 3's table ALLOWS — nothing continues the session. |
| H1 | high | TOOL-7, TOOL-5 | TOOL-7 §2 S4, §4 '`--status` and `--close`', §5, §6 AC5; TOOL-5 §8 F1, Edges | A second stdout line survives `sed 's/.*· next //'` at `unattended.test.sh:1874`; the arm reds on every fixture and the driver header's "one line" is false. |
| H2 | high | TOOL-3, TOOL-6 | TOOL-3 §3 'No prose carriers', §4 'The knob', Files touched; TOOL-6 §4 line 150 | The example gains `STOP_GUARD_BLOCKS="12"`; no unit adds its section 8 row; check 22 joins both directions and reds `undocumented in the protocol`. |
| H3 | high | TOOL-5, TOOL-7, TOOL-2 | TOOL-5 §4 '`--status` (S8)' line 251, §2 S8, §6 AC9; TOOL-2 §4 item 9, §6 AC7; TOOL-7 §2 S9, §6 AC12 | Unit 5 spells `$(GIT rev-parse --git-dir)` inline; unit 7's AC12 pins that grep at exactly 1 and cannot see whose line made it 2. |
| H4 | high | TOOL-5 | §4 'The decision, per run' rows 153–155; §2 S6; §3; §5 | STALE + `pid-alive: yes` kills the tree, THEN the login row runs; a logged-out node kills and announces it cannot resume. |
| H5 | high | TOOL-5 | §4 'The walk', 'Data model'; §2 S3; §6 AC5 | The conf is sourced only in a subshell for `MEMORY_ROOT`; `read_bound_key` reads `${!name}` from the calling shell and prints `$CONF`; every tick takes the defaults. |
| H6 | high | TOOL-3, TOOL-4 | TOOL-3 §4 'The fixture and the direct observation', §6 AC11; TOOL-4 §4 fixture paragraph, §6 AC10 | `seed()` never commits; `git log -1 --format=%ct` is a dead probe on an unborn HEAD; `--liveness` fails 52 and AC11 can never block. |
| M1 | medium | TOOL-7, TOOL-6 | TOOL-7 §4 'The carriers' dossier row, §6 AC8; TOOL-6 §2 S6, §4 'Dossier', §10 | Unit 6 rewrites the bullet at order 6, so unit 7's `grep -c` is 0 at its own base; `map_diff.py` reports no freshness. |
| M2 | medium | TOOL-2 | §6 AC6; §2 S5; §10 | `grep -c 'read_bound_key'` is 5 at base (definition, three calls, a comment), so "at least 4" holds before any work. |
| M3 | medium | TOOL-2 | §2 S5; §6 AC6, AC10 | Four carriers named, none read by a criterion; a pass declaring the key nowhere passes. |
| M4 | medium | TOOL-1 | §2 S6; §6 AC1–AC5 | Nothing reads `unattended.test.sh` for the prologue exports; unit 2's AC5 depends on `fixture-session`. |
| M5 | medium | TOOL-3 | §2 S5, S6; §6 AC5–AC7, AC12, AC13 | `kit.toml optional_keys`, the example line and `project-owned` are unread by every AC. |
| M6 | medium | TOOL-6 | §2 S1; §8 F2; §4 items 4–5; §6 AC1 | The one-copy rule every pointer targets has no needle in AC1. |
| M7 | medium | TOOL-6, TOOL-3 | TOOL-6 §2 S5, §4 'Conf', §6 AC6; TOOL-3 §4 'The knob', §8 F3, Edges | Spec 3 hands the root-conf line to unit 6; spec 6 adds only a rationale "above a key that carries none"; AC6 wants the key located. |
| M8 | medium | TOOL-2 | §4 'The bound (S5)' | `GATE_BOUND_DEFAULT + 1800` ignores a raised `GATE_BOUND`; a long bar's silence reads STALE and unit 5 kills it. |
| M9 | medium | TOOL-3 | §4 'The knob'; §6 AC5, AC6 | The harness ends the turn after 8 consecutive blocks; blocks 9–12 and the `blocks-exhausted` row are unreachable in one turn. |
| L1 | low | TOOL-5 | §2 S2; §4 'The walk' | The non-zero `--liveness` skip and the no-conf skip have no arm. |
| L2 | low | TOOL-2 | §2 S2 vs §4, §6 AC8 | S2 says exit 0 on any run-state file; a dead probe exits 1 with one present. |
| L3 | low | TOOL-2 | §2 S4; §6 AC5, AC8 | AC5 runs on a clean tree; the dirty-write signal is never seen. |
| L4 | low | TOOL-1 | §2 S1; §4 step 4; §6 AC2 | Only the both-unset arm of the three-way NOTE is observed. |
| L5 | low | TOOL-3 | §2 S3; §4 'The sidecar line', 'The decision' | The unwritable-sidecar allow and the 60 s bound have no arm. |
| L6 | low | TOOL-7 | §6 AC5 | All three AC5 fixtures print `keepalive: k1`; the `none` arm is unobserved. |
| L7 | low | TOOL-4 | §2 S4; §6 AC7–AC9 | No AC reads `kit.toml`; the suite ships to adopters with every AC green. |
| L8 | low | TOOL-6 | §2 S2; §6 AC2 | The absent-owner sentence, the new section's content and the Reap prose are unread. |
| L9 | low | TOOL-2 | §2 S2 vs §4 steps 5–6, §6 AC2 | S2 orders `pid-alive` before `keepalive`; §4 prints it after. |
| L10 | low | TOOL-7 | §4 'Why the line's own phase field decides' | The close-only rule is `TOOL-cFinalBerth-1` S9; `aBoundedVerdict-15` has no S9. |
| L11 | low | TOOL-7 | §10 | `RUN.md:24` is the `## Parked` heading; the CORRECTION row is `:30`. |
| L12 | low | TOOL-7 | §2 S6; README roster row 7 | The roster says CHECKED at `--close`; the spec puts the check at `--landed`. |

---

### B1 — blocker — TOOL-7 §2 S2, §4 'The read' (both refusal texts), §8, against TOOL-3 §4 'The decision' and TOOL-2 §2 S3 — raw 18, 29, 43

**The defect.** S2 refuses `--landed` when the sidecar's newest stop-guard line was recorded in any
phase other than `LANDING`, and both refusal texts (spec 7 lines 135–142) end with the same remedy:
END THE TURN, because "the stop-guard records the listing and continues you", then re-run `--landed`.
Section 4 states the premise outright — the stop-guard refuses a `LANDING` record's stop — and cites
nothing for it. The siblings say otherwise, and the driver fixes the order:

- `--close` prints `COMMIT the run-state file, then land with: $LANDER` (`unattended.sh:3244`) and
  `verb_landed`'s own comment calls it "the only verb that runs after the push" (`:3502`); the Skill
  says "Run this AFTER the lander returns, not before" (`SKILL.template.md:829-832`). The lander
  pushes `main`, which moves `refs/remotes/origin/main`.
- So at every point the S2 refusal can fire, the record is `LANDING` with a sha witness that is
  already an ancestor of `origin/<default>`. Spec 2 S3 (line 35–36) grades exactly that
  `finished-unstamped`.
- Spec 3's ratified decision table, line 149: `FINISHED-UNSTAMPED | any | any | allow |
  finished-unstamped`. The sidecar line is written; the session is not continued.

After the instructed turn end nothing resumes the session: `keepalive-reaped` was attested before
`--close`, so the idle-wake is gone, and spec 5's table acts on `STALE` only. Every wired, bound
landing that follows the documented order — which is every one, since the S2 check fires whenever the
newest stop line predates the close, and on a one-turn landing it always does — wedges at `LANDING`
with its work on `main` and no `LANDED` stamp. That is the class spec 2 §1 cites as the motivating
defect, produced by the unit built to close `TOOL-aPromptedMandate-11`. Spec 7 §8 rejects B1 (pass as
`unchecked`) for firing only by accident of a turn boundary; the chosen shape fires on every landing.
Spec 7's own AC3 fixture (preflight witness, then push `HEAD:main`) is the finished-unstamped shape,
and no criterion observes the continuation the remedy promises.

**The fix.** Pick one and say which spec 3 row it rests on. (a) Spec 3's table gains a phase-aware row:
`FINISHED-UNSTAMPED` with the newest stop line recorded in a phase other than `LANDING`, for a bound
session → BLOCK once, reason `landing-unstamped`, text `re-run --landed`; spec 3 AC3 gains that half,
and spec 7's remedy then truthfully says "continues you". The six old records that motivated the
allow row are unbound and never reach the table. (b) Spec 7 mandates the turn boundary BETWEEN
`--close` and the lander (close, commit, end turn — verdict `LIVE`, stop blocked and continued —
lander, `--landed`) in the Skill's landing section and in the refusal texts. (c) Spec 7 returns to
the brief's B1 and S2/AC2 become the announced `unchecked` pass. Whichever, spec 7 §4 stops asserting
that the stop-guard refuses a `LANDING` record's stop, §10 gains a line citing spec 2 S3 and spec 3's
table, and an AC observes the continuation on a fixture whose witness is already on `origin/main`.

**Left-shift.** One harness arm in `unattended.test.sh` that drives the documented landing order
(close → commit → lander → `--landed`) against a wired stop-guard stub over a fixture remote and
asserts the record reaches `LANDED` without a second turn; RED today. For the spec-audit lens: a
remedy that says "end the turn" must cite the decision-table row that continues it — a documented
check, since no gate can read intent.

### H1 — high — TOOL-7 §2 S4, §4 '`--status` and `--close`', §5, §6 AC5, against TOOL-5 §8 F1 and Edges — raw 1, 21, 30, 44

**The defect.** S4 has `verb_status` print an unconditional second stdout line (`keepalive: <kid|none>
· last harness listing …`) on every record, and §5 asserts "no existing arm changes its assertion".
At base, `unattended.test.sh:1874` is `same … "$(run --status tRun | sed 's/.*· next //')"
"$want_unit"`, and `same` is byte equality (`:71`). The sed leaves line 2 intact, so the captured value
is two lines against one unit id and the arm reds on every fixture — `--keepalive-id` is mandatory at
`--preflight`, so every fixture carries a keepalive fact. Spec 5 §8 F1 measured exactly this arm and
chose a field on the existing line for that reason; spec 5's hands-off edge to unit 7 records the
collision without resolving it. The driver header `:8` promises `--status <slug>  # one line`, and
spec 7's carrier table omits it. AC5 asserts only that the first line is byte-identical, which cannot
see a whole-output reader. The `:1859` `grep -c 'next '` arm and the `:1028` `head -1` read survive.

**The fix.** Take spec 5 S8's shape: the listing becomes a field on the existing status line, omitted
when unrecorded. Or, if a second line is kept, Files touched and AC5 name the `:1874` arm (to
`head -1`) and the header line `:8` as edits, spec 5's hands-off sentence is corrected, and AC5
asserts the whole `--status` output through the arm's own pipeline. Either way `:1874` joins §10's seams.

**Left-shift.** The header's "one line" becomes an arm: `run --status <slug> | wc -l` = 1 — the
promise is then a check rather than a comment. For the audit: a unit changing a verb's stdout lists
every suite reader of that verb (`grep -n 'run --status' unattended.test.sh`) in Files touched or
states why each survives; documented, run by the lens.

### H2 — high — TOOL-3 §3 'No prose carriers', §4 'The knob', Files touched, against TOOL-6 §4 line 150 and TOOL-5 §2 S3 — raw 19, 31

**The defect.** Spec 3 adds `STOP_GUARD_BLOCKS="12"` to `tools/unattended/.unattended.conf.example`
(Files touched, line 313) and lists no protocol edit; its §3 assigns every protocol edit to unit 6
(`section 8` appears zero times in spec 3). Spec 6 §4 line 150: "The section 8 key table is not this
unit's: each knob's row lands with the unit that reads the key." Specs 2 and 5 add their own rows;
spec 3 does not, and no other spec names a `STOP_GUARD_BLOCKS` row. Check 22 of
`tools/unattended/check-unattended.sh` (`:1685-1726`) joins the example's `^[A-Z_]+=` keys against the
rendered protocol's section 8 key column in both directions and fails on `undocumented in the
protocol`. The `unattended kit gate` leg is therefore red from unit 3's commit through the close, with
every later unit's §7 listing it as green.

**The fix.** Spec 3 S5 and Files touched take the section 8 row for `STOP_GUARD_BLOCKS` in
`tools/unattended/PROTOCOL.template.md` plus the re-render of `memory/guides/UNATTENDED-PROTOCOL.md`
in the same commit — the shape spec 2 S5 and spec 5 S3 already use; §3's 'No prose carriers' bullet
exempts that one row; §7 names check 22; an AC mirrors spec 5 AC6's awk-cut section 8 grep.

**Left-shift.** A spec-set check: join every spec's Files-touched paths against the guards in
`tools/gate-legs.json`, and require the guarded leg to appear in that spec's §7 — a unit that touches
a leg's subject and does not name the leg is the shape this defect took. Runnable over the spec
folder with stdlib; RED on spec 3 today.

### H3 — high — TOOL-5 §4 '`--status` (S8)' line 251, §2 S8, §6 AC9, against TOOL-2 §4 item 9, §6 AC7 and TOOL-7 §2 S9, §6 AC12 — raw 4, 20, 34

**The defect.** Spec 5 line 251 reads the sidecar as `$(GIT rev-parse --git-dir)/unattended/
resume.<slug>.log` inside `verb_status` and never names `resolve_sidecar_dir` (zero hits over spec
5). Spec 2 introduces that function at order 2 as the ONE derivation, "never respelled", and its AC7
reds when "the root is spelled inline … leaves unit 7 a second spelling to drift from". Spec 7 AC12
requires `grep -c 'rev-parse --git-dir' tools/unattended/unattended.sh` to print exactly 1 at its tip
(0 at base, verified) and S9 scopes extracting unit 2's inline copy only. Unit 2 makes the count 1,
unit 5 makes it 2 before unit 7 starts, so unit 7 either rewrites unit 5's line unscoped or reds its
own AC12 — a red with no owner, and the two-spellings class spec 5 §3 itself invokes.

**The fix.** Spec 5 S8 reads through `$(resolve_sidecar_dir)/resume.<slug>.log`; §10 names
`resolve_sidecar_dir` as the seam and the consumes-from edge to unit 2 names it; AC9 gains "and
`grep -c 'rev-parse --git-dir' tools/unattended/unattended.sh` is unchanged from this unit's base".
The tick keeps its own spelling in its own file.

**Left-shift.** Spec 7 AC12 is the right gate in the wrong place: land the count-is-1 assertion as a
`check-unattended.sh` check over the driver so it binds every unit, not only unit 7's pass.

### H4 — high — TOOL-5 §4 'The decision, per run' rows 153–155, §2 S6, §3, §5 — raw 22

**The defect.** Row 153: `STALE | under the cap | yes | — | kill the tree, then the two rows below`.
Rows 154–155 then consult `claude auth status`; a logged-out CLI is a SKIP with nothing launched. So on
a logged-out node the tick's first act is to kill the recorded pid's tree and its second is to print
that it cannot resume the run. §3 and S6 promise only "never a launch", and §5 states the false-STALE
harm as "duplicated work" — false on this path, where the harm is a killed session with no resumer. A
stale-looking healthy session (a 26-minute bar with the transcript silent) is the case spec 2 M8 makes
likely. AC2's logged-out arm uses `pid: 999999999`, so the kill under a logged-out CLI is unobserved.
Two nuances the finding overstated: the kill fires once per run, since `pid-alive` turns `no` after
it, and the research's class-D lockout is a usage limit rather than a logged-out CLI. The ordering and
the missing risk row stand.

**The fix.** Move the login row above the kill row — kill only when a launch will follow; §5 states
that a logged-out node kills nothing; AC2 gains a second half: `pid-alive: yes` (AC4's sleep) with
`STUB_LOGGED_IN=false` → the sleep survives and the SKIP line prints.

**Left-shift.** That AC2 half as a tick arm. For §10's checklist: "a destructive step ordered before
the precondition that makes it useful" — the tick is the first out-of-process killer in the kit and
the class will recur.

### H5 — high — TOOL-5 §4 'The walk', 'Data model', §2 S3, §6 AC5 — raw 26, 33

**The defect.** The tick reads `RESUME_ATTEMPTS` and `RESUME_TURNS` through the hoisted
`read_bound_key`, which reads `${!_bk_name:-}` from the CALLING shell and interpolates `$CONF` into
its NOTE (`unattended.sh:358-368`); the driver makes it work by `. "$CONF"` at `:341`. Spec 5 §4
sources each worktree's `.unattended.conf` only "in a subshell" for `MEMORY_ROOT` and never says which
conf is sourced into the tick's own shell, nor that `CONF` is set. As written every tick takes 6 and
40, prints `declares no RESUME_ATTEMPTS … Declare one in  to change it` with an empty path even for a
project that declares the key, and AC5's only arm (declares none → NOTE) is green for the wrong
reason; AC1 and AC3 exercise the defaults only. The spec also does not say whether the `--repo` root's
conf or each worktree's governs.

**The fix.** §4 states the read: per worktree, a subshell sources that conf, sets `CONF` to it, runs
the two `read_bound_key` calls and prints the resolved values the walk consumes (or the knobs are
declared root-scoped and read once from `$ROOT/.unattended.conf`). AC5 gains an arm with
`RESUME_ATTEMPTS="2"` declared and two seeded post-move lines → `ATTEMPTS EXHAUSTED`, no NOTE.

**Left-shift.** That arm, plus one asserting the NOTE's interpolated conf path is non-empty — a NOTE
naming no file is the signature of this defect and is greppable.

### H6 — high — TOOL-3 §4 'The fixture and the direct observation', §6 AC11; TOOL-4 §4 fixture paragraph, §6 AC10 — raw 32

**The defect.** Both real-driver integration arms run `--liveness fx` in a `git init` fixture "seeded
the way `adopt-unattended.test.sh`'s `seed()` builds one". That seed (`:38-80`) `git add`s one stub and
never commits — zero `git commit` lines in the suite. `print_audit`'s clock block (`:3013-3025`), which
spec 2 moves verbatim into `read_tree_clocks`, marks `git log -1 --format=%ct` dead on the empty answer
an unborn HEAD gives, and spec 2 §4 makes any dead probe a `fail 52` refusal: exit 1, no verdict line.
The hook reads `liveness-unreadable` and ALLOWS, so spec 3 AC11 ("the invocation blocks") can never go
green; spec 4 AC10's `last-stall:` line is step 9 of the verb, after the clocks at step 7, so neither
`last-stall: none` nor the post-payload line ever prints. Both arms red for a reason unrelated to the
hooks they test.

**The fix.** Both fixture paragraphs and both `fixture:` lines state one commit after seeding
(`git add -A && git commit -q -m seed --no-verify`), or the arms assert the check-52 refusal
explicitly; §10 of each cites `unattended.sh:3013-3018`'s `git log` probe.

**Left-shift.** `seed()` in `adopt-unattended.test.sh` gains that commit, so every future borrower
inherits a born HEAD; the audit checklist gains "a fixture built from another suite's seed inherits
that seed's HEAD state".

### M1 — medium — TOOL-7 §4 'The carriers' (dossier row), §6 AC8, against TOOL-6 §2 S6, §4 'Dossier', §10 — raw 2, 25, 28, 37, 49

**The defect.** `memory/map/features/unattended.md:270` reads "The keepalive half is unenforceable by
construction" (count 1 at base). Spec 6 §4 'Dossier' (order 6) replaces that bullet with text already
saying "checked at `--landed` against the harness's own stop listing". Spec 7 §4 (order 7) derives its
carrier list "by git grep at base", rewrites the same bullet with different text, and AC8 asserts
`grep -c 'unenforceable by construction'` prints 0 — already true before unit 7 starts. AC8's second
half has `map_diff.py` "report the dossier fresh"; that tool attributes a `<base>..<head>` range and
prints no freshness, as spec 6 §10 already measured, and the freshness check is `gen_map.py --check`.
Neither half can go red: unit 7's edit is unobservable, and two ratified records prescribe two texts
for one paragraph in a dossier spec 6 measures at 93 bytes of headroom.

**The fix.** Spec 7 drops the dossier row from 'The carriers', Files touched and AC8 (spec 6's text
already says what unit 7 wants), or spec 6 S6 leaves that bullet to unit 7 and says so through the
Edges list. AC8 becomes `python tools/codebase-map/gen_map.py --check` exits 0 plus a positive grep
(`checked at --landed` once) that is 0 at unit 7's own base.

**Left-shift.** For the audit's priming: a `prints 0` criterion states its count at the unit's ORDER
base, not the build base; a lens executes every "at base" claim. `--dispatch`'s refusal of a path two
units declare as a write could extend from generated indexes to any dossier — a documented candidate,
not asked for here.

### M2 — medium — TOOL-2 §6 AC6, §2 S5, §10 — raw 5, 23, 41

**The defect.** AC6: `grep -c 'read_bound_key' tools/unattended/unattended.sh` "prints at least 4 …
and prints 3 at base". At `5f9648d6` it prints 5 — the definition `:358`, calls `:369 :370 :529`, a
comment `:525` — and §10 itself names three existing callers. The tip clause holds before any work and
the red condition ("the count stays 3") is unreachable; a fourth `case` for the key passes. S5's
"beside its two siblings" and §10's "third caller" are the same miscount.

**The fix.** AC6: `grep -c '^read_bound_key RESUME_STALE_BOUND ' tools/unattended/unattended.sh`
prints 1 and 0 at base (or the `-cE '^read_bound_key [A-Z_]+ '` form: 4, and 3 at base); S5 and §10
say three siblings, fourth caller.

**Left-shift.** Same as M1's: base-count claims are executed at the audit, not read.

### M3 — medium — TOOL-2 §2 S5, §6 AC6, AC10 — raw 6

**The defect.** S5 names four carriers for the key — `.unattended.conf`, the example, `kit.toml
optional_keys`, the protocol section 8 row — and says "Observed by AC6". AC6 observes the NOTE, the
`abc` refusal and the count (M2); AC10 observes that the conf appears in the commit, not what it
declares. No gate joins `kit.toml optional_keys` to anything (`govkit.py` reads key lists for
`requires_if` only), and check 22 fires only at the close, so a pass declaring the key nowhere passes.

**The fix.** The spec 5 AC6 shape: `grep -c RESUME_STALE_BOUND` over each of the four files prints 1
(the section 8 region cut by awk), every count 0 at base.

**Left-shift.** A `check-unattended.sh` check joining `kit.toml optional_keys` to the example's keys —
the one carrier no gate reads today — which also serves M5.

### M4 — medium — TOOL-1 §2 S6, §6 AC1–AC5 — raw 7

**The defect.** S6 adds the suite prologue exports (`CLAUDE_CODE_SESSION_ID=fixture-session`,
`CLAUDE_PID=999999999`) and a new arm block and says "Observed by AC1 to AC5", but AC1–AC4 set the env
explicitly or run over the record AC1 left, and AC5 greps the driver; nothing reads
`unattended.test.sh`, and the unit adds no `fail` branch for the harness-arms leg to count. Spec 2's
AC preamble and its AC5 transcript arm depend on `fixture-session`; a forgotten export stamps every
fixture record with the real session id and unit 2 fails on a defect unit 1 never observed. Spec 1 §4
cites the fixture-inherits-ambient-state gotcha as the class and observes no guard against it.

**The fix.** `grep -c '^export CLAUDE_CODE_SESSION_ID=fixture-session' tools/unattended/
unattended.test.sh` and the pid twin, each 1 and 0 at base, plus one grep for the arm block's needle
(`--keepalive-id zzz`).

**Left-shift.** Those greps as the ledger's tokens; the class rule for the lens: an "Observed by"
claim over a FILE carrier names an AC whose command reads that file by path.

### M5 — medium — TOOL-3 §2 S5, S6, §6 AC5–AC7, AC12, AC13 — raw 8

**The defect.** S5 ("declared in the kit descriptor's `optional_keys` and in the shipped conf
example") says Observed by AC6/AC7; S6's "`kit.toml` carrying the suite in its `project-owned` list"
says AC12/AC13. AC5–AC7 feed payloads to the copied hook and read `BLOCKS_DEFAULT`; AC12/AC13 observe
the merger and `check-hook-destinations`. No criterion greps `kit.toml` or the example (contrast spec
5 AC11's `grep -c 'resume-tick.test.sh' tools/unattended/kit.toml`). The suite can ship to adopters
and the key can be missing from the descriptor with every AC green; the section 8 half is H2.

**The fix.** `grep -c STOP_GUARD_BLOCKS tools/unattended/kit.toml` and over the example print 1;
`grep -c 'stop-guard.test.sh' tools/unattended/kit.toml` prints 1; all 0 at base.

**Left-shift.** A `govkit selfcheck` arm: every `*.test.sh` under a kit dir is in that kit's
`project-owned` list — a real gate for the withheld-suite class (also L7), which nothing asserts today
(grepped `govkit`, `check-install-prefix`, `run-selftests`).

### M6 — medium — TOOL-6 §2 S1, §8 F2, §4 items 4–5, §6 AC1 — raw 9

**The defect.** F2 resolves that the absent-owner RULE lives once in section 5, with the Skill, the
stop-guard reason and the tick payload pointing at it; §4 item 5 is that rule and item 4 the three
actors; S1 says Observed by AC1, AC5, AC7. AC1 greps the failure-domain sentence, the heading, five
mechanism names and the absence of `for four kit versions` — nothing from item 5 (no `park`,
`asking`, `absent`) and nothing distinguishing item 4. AC5 is a `cmp` of template and render, AC7 a
byte cap. A section 5 omitting the one-copy rule passes all three and leaves every pointer dangling.

**The fix.** AC1 gains a needle from item 5 (`makes no measured observable worse` or `never ends its
turn by asking`) and one from item 4 (`AGENT`, `DRIVER`), each 1 in both files and 0 at base.

**Left-shift.** Same class rule as M4; the render `cmp` already guards template↔render parity, so
one needle in the template is enough.

### M7 — medium — TOOL-6 §2 S5, §4 'Conf', §6 AC6, against TOOL-3 §4 'The knob', §8 F3, Edges — raw 24

**The defect.** Spec 3 §4 'The knob' does not edit the root `.unattended.conf` and says "unit 6 adds
all four knobs"; its Edges hand unit 6 "the root conf's `STOP_GUARD_BLOCKS` line with its rationale".
Spec 6 S5/§4 'Conf' adds only a rationale "above a key that carries none" — its Files-touched row
reads "comments; rationale where absent" — while its AC6 requires each key "located in
`.unattended.conf`". Specs 2 and 5 each add their own root-conf keys, contradicting spec 3's "all
four". No unit's scope writes `STOP_GUARD_BLOCKS=` into the root conf, so spec 6 AC6 reds at its own
pass; an ad-hoc addition then trips check 22's `proj_extra` direction unless H2's row exists.

**The fix.** Spec 6 S5 and §4 'Conf': "adds the KEY line where a unit left the root conf untouched
(`STOP_GUARD_BLOCKS`, per spec 3 F3) and the rationale where absent"; spec 3 F3 and §4 restate that
units 2 and 5 declare their own root-conf keys and unit 6 declares only this one.

**Left-shift.** Spec 6 AC6's "located" grep is the gate once the writer is named; the cross-spec
class is the audit's "consumes-from row names the artifact, not the unit" — documented.

### M8 — medium — TOOL-2 §4 'The bound (S5)' — raw 35

**The defect.** `RESUME_STALE_BOUND_DEFAULT=$((GATE_BOUND_DEFAULT + 1800))`, rationalised as "one
`UNIT_STALL_BOUND` above" `GATE_BOUND`, derives from the KIT defaults although the DECLARED
`GATE_BOUND` and `UNIT_STALL_BOUND` are both resolved at `unattended.sh:369-370` before the insertion
point, and it retypes 1800 beside `UNIT_STALL_BOUND_DEFAULT` — the two-numbers class the driver's
`REVIEW_ROUNDS_DEFAULT` comment records a closing review already found. An adopter who raises
`GATE_BOUND` (the conf's own documented remedy for a longer bar) gets a stale bound BELOW its bar
bound; a full bar's silence reads STALE and unit 5's tick kills the healthy bar — the risk spec 5 §5
names, made likely by the default.

**The fix.** Derive `$((GATE_BOUND + UNIT_STALL_BOUND))` after both reads and interpolate the derived
figure into the NOTE; or declare the default kit-scoped and have the conf comment tell a project
raising `GATE_BOUND` to raise this key too. AC6's needle then reads the derived value.

**Left-shift.** A driver NOTE (or refusal) at conf read when `RESUME_STALE_BOUND < GATE_BOUND +
UNIT_STALL_BOUND`: the driver refuses a bound under which its own bar reads dead.

### M9 — medium — TOOL-3 §4 'The knob', §6 AC5, AC6 — raw 45

**The defect.** `STOP_GUARD_BLOCKS` defaults to 12, "three keepalive cadences plus headroom"; the
NOTE promises "blocked at most 12 times per run and session" and the reason prints `<n>/12`.
`memory/builds/aReplayedCard/build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md:299`
(verdicts 8, 22, confirmed against the hooks doc) records that the harness ends the turn after 8
consecutive stop-hook blocks. In the class-E case the hook exists for, every block is consecutive, so
blocks 9–12 and the `blocks-exhausted` row are unreachable inside a turn, and AC5/AC6 observe the
budget only against a stub. Nuance: the sidecar count persists across a `--resume`, so 12 can
accumulate over several turns; the spec's rationale and reason text do not say so and are wrong for
the single-turn case.

**The fix.** Cite the aReplayedCard record; pin the default at or below 8, or derive it from that cap
and say so in the hook header beside the knob; state in §3 what the harness bounds versus what the hook
bounds; one arm or a documented manual check observing the harness ending a session under a knob
above the cap.

**Left-shift.** The harness cap as a named constant in the hook with the record cited beside it; a
suite arm asserting `BLOCKS_DEFAULT <= HARNESS_CONSECUTIVE_CAP`.

### L1 — low — TOOL-5 §2 S2, §4 'The walk' — raw 10

The walk designs two announced skips — a non-zero `--liveness` exit prints `liveness probe failed:
<line>` and skips; a worktree without `.unattended.conf` is skipped with one line — and §5 rests
"nothing resumes on a probe that answered nothing" on the first. §7's arm covers "every decision of
section 4's table", whose rows are the five verdict/attempts/login rows only. **Fix:** one arm with a
stub driver exiting 1 → the line prints, no launch, no attempt line; one worktree without a conf → the
skip line and the other tree still walked. **Left-shift:** those two arms.

### L2 — low — TOOL-2 §2 S2 vs §4, §6 AC8 — raw 11

S2 says the verb "exits 0 on any run-state file"; §4 makes a dead probe "the second `fail 52` branch
… exit 1, and no verdict line prints", S8 lists it, and AC8 pins exit 1 with the file present. Two
answers to one question inside the scope list; spec 5 happens to read S8 correctly. **Fix:** S2:
"exits 0 on any run-state file whose probes answer; a dead probe is the check-52 refusal of S8".
**Left-shift:** none gateable; the lens's contradiction axis.

### L3 — low — TOOL-2 §2 S4, §6 AC5, AC8 — raw 12

S4 claims the four-signal clock is observed by AC5 and AC8; AC5's three halves observe `commit`,
`gate-log` and `transcript` on a CLEAN tree, and AC8's dirty half observes the check-52 refusal plus
the audit's `last-write none`. A `print_liveness` maximum that drops `TC_LASTW` reads a run mid-edit as
STALE and passes every AC; unit 5 then kills it. **Fix:** AC5 gains a touched untracked file over the
hour-old commit → `last-move-source: write`, `stale: no`. **Left-shift:** that arm.

### L4 — low — TOOL-1 §2 S1, §4 step 4, §6 AC2 — raw 13

The NOTE's three-way alternation `<session id|pid|session id or pid>` has one arm observed: AC1 sets
both variables (no NOTE) and AC2 unsets both. A NOTE with the wrong noun, or `session: absent`
written when only `CLAUDE_PID` is unset, is green. **Fix:** AC2 gains `env -u CLAUDE_PID` alone →
`exposes no pid` exactly once with `session: abc` still recorded. **Left-shift:** that arm.

### L5 — low — TOOL-3 §2 S3, §4 'The sidecar line', 'The decision' — raw 14

The `sidecar-unwritable` allow (stderr, nothing written) and the 60 s `LIVENESS_BOUND_MS` row carry
§5's "a broken hook never blocks a stop"; AC7 observes stub exit 1 and a missing `verdict:` line only.
A hook that blocks with no derivable count loops the session; a hung `--liveness` with no wired bound
hangs every stop. **Fix:** one arm with the sidecar directory made a file → allow with the stderr
line and no write; the bound overridable by an env var so a sleeping stub observes
`liveness-unreadable` in seconds. **Left-shift:** those two arms.

### L6 — low — TOOL-7 §6 AC5 — raw 15

The grammar is `keepalive: <kid|none> · …` and S4 claims AC5 observes it, but AC5's three fixtures all
print `keepalive: k1`; AC4's keepalive-line-deleted form is never run through `--status`. **Fix:** AC5
gains the fourth fixture with `keepalive: none · last harness listing none: unrecorded` — or its
field form if H1 takes spec 5's shape. **Left-shift:** that arm.

### L7 — low — TOOL-4 §2 S4, §6 AC7–AC9 — raw 16

S4 lists `stall-recorder.test.sh` in the descriptor's `project-owned` list as observed by AC7–AC9,
which observe the merger, the fragment loop and `check-hook-destinations.sh`; none reads `kit.toml`,
and no gate asserts a kit's `*.test.sh` is withheld. The suite ships to every `govkit apply` adopter
green. **Fix:** `grep -c 'stall-recorder.test.sh' tools/unattended/kit.toml` prints 1 and 0 at base.
**Left-shift:** the `govkit selfcheck` arm proposed under M5.

### L8 — low — TOOL-6 §2 S2, §6 AC2 — raw 17

AC2 greps `cannot be corrected in place`=0, `--keepalive-id` in `## Resume`, the `## What wakes a
stalled run` heading, `schedule the idle-wake NOW`, and two absent names. Nothing observes the
absent-owner sentence appended to the idle-wake section, the new section's content, or `## Reap` /
`## If it cannot finish` saying idle-wake; AC8's sweep passes any file in the commit's `--stat`.
**Fix:** AC2 gains `stop-guard`, `stall-recorder`, `resume-tick` and `--liveness` inside the new
section's awk cut, and `idle-wake` at least once in the `## Reap` cut, each 0 at base.
**Left-shift:** those greps.

### L9 — low — TOOL-2 §2 S2 vs §4 steps 5–6, §6 AC2 — raw 27

S2 orders the keys `session, pid, pid-alive, keepalive` "in this order"; §4 prints `session, pid,
keepalive` at step 5 and `pid-alive` at step 6, and AC2 binds to "section 4's order". Readers in
specs 3 and 5 go by key (`sed -n 's/^verdict: //p'`), so the harm is two contracts for one wire order.
**Fix:** S2 matches §4's step order (or the reverse) and AC2 cites S2. **Left-shift:** none needed
beyond AC2 once the two agree.

### L10 — low — TOOL-7 §4 'Why the line's own phase field decides' — raw 50

The LANDING-is-close-only rule is attributed to "S9 of `TOOL-aBoundedVerdict-15`"; that spec has no
S9 (`grep -c 'S9'` = 0) and its S1 is the staging fix `unattended.sh:2324` cites as the second
omission. The rule is S9 of `memory/builds/cFinalBerth/spec/2026-08-13-spec-cFinalBerth-1.md:56`
(commit `e59e5b66`), and the driver's branch comment at `:2312` is that S9. **Fix:** cite
`TOOL-cFinalBerth-1` S9 for the rule and keep `aBoundedVerdict-15` for the staging only.
**Left-shift:** a documented check that every `S<n> of <id>` citation resolves to a `**S<n>**` line
in that spec — greppable, and `corpus_ids.py` already resolves the id half.

### L11 — low — TOOL-7 §10 — raw 52

`memory/builds/aPromptedMandate/RUN.md:24` is the `## Parked` heading; the CORRECTION row recording
two keepalives listed as live is `:30`, which the build's own research record cites. **Fix:** cite
`RUN.md:30`. **Left-shift:** same check as L10 for `<path>:<line>` citations, which
`check-spec-tokens.py` joins by path only.

### L12 — low — TOOL-7 §2 S6; `memory/builds/aWokenSentinel/README.md` roster row 7 — raw 53

The roster row reads "`keepalive-reaped` becomes CHECKED at `--close` against the cron listing";
spec 7 §3 lists 'Check at `--close`' as a rejected alternative and S2/S3 put the check at `--landed`.
The row was authored at `--rescope` after base, so S6's git-grep-at-base sweep cannot reach it and
its scope (carriers calling the item unobservable) does not cover it. `memory/LIVE.md` renders the
status row and a link, not the Mechanism column, so the wrong verb lives in the README rather than in
`LIVE.md`. **Fix:** add the roster row to S6's carrier list and correct it to `--landed` in the pass
commit. **Left-shift:** none gateable; a `--rescope` that edits the roster after specs exist is the
class, and the audit's carrier axis reads the README beside the specs.

---

## The cross-read on the four axes

Where two specs disagree, both are named, because a fix to one that leaves the other is a fold.

- **Interface.** TOOL-7 S4's second `--status` line versus TOOL-5 F1's field and the suite's `:1874`
  reader (H1). TOOL-5 S8's inline sidecar root versus TOOL-2's `resolve_sidecar_dir` and TOOL-7 AC12
  (H3). TOOL-7's remedy versus TOOL-3's `FINISHED-UNSTAMPED → allow` row and TOOL-2 S3 (B1). TOOL-2 S2's
  key order versus its own §4 (L9). TOOL-2 S2's exit contract versus its own AC8 (L2).
- **Ordering.** TOOL-6 at order 6 rewrites the dossier bullet TOOL-7 at order 7 greps for (M1).
  TOOL-3 at order 3 adds an example key whose section 8 row nobody adds, so the kit gate is red from
  order 3 to the close (H2). TOOL-5 at order 5 makes the `rev-parse` count 2 before TOOL-7's AC12 pins
  it at 1 (H3). TOOL-5's kill row precedes its login row (H4). The lander precedes `--landed`, which is
  what makes B1 fire on every landing rather than by accident.
- **Scope.** TOOL-3 says unit 6 adds all four root-conf knobs; TOOL-6 adds rationales only; TOOL-2
  and TOOL-5 add their own (M7). TOOL-3 assigns every protocol edit to unit 6; TOOL-6 assigns each
  knob's row to the unit that reads the key (H2). TOOL-7 S9 scopes extracting unit 2's inline copy and
  not unit 5's (H3). TOOL-5 sources the conf in a subshell and reads the keys from its own shell (H5).
- **Acceptance.** Criteria that hold at base: TOOL-2 AC6 (M2), TOOL-7 AC8 both halves (M1). Criteria
  that cannot go green: TOOL-3 AC11 and TOOL-4 AC10 (H6). Criteria that pass for the wrong reason:
  TOOL-5 AC5 (H5). Carriers with no criterion: TOOL-2 S5 (M3), TOOL-1 S6 (M4), TOOL-3 S5/S6 (M5),
  TOOL-6 S1 and S2 (M6, L8), TOOL-4 S4 (L7). Arms of a grammar unobserved: L1, L3, L4, L5, L6.

**Prior art the specs re-invent or misread.** `read_bound_key`'s calling-shell contract, which the
driver satisfies by sourcing `$CONF` first (H5). `resolve_sidecar_dir`, introduced by a sibling in the
same set (H3). `seed()`'s unborn HEAD, borrowed without its consequence (H6). `gen_map.py --check` as
the freshness observation, already measured by spec 6 §10 and re-missed by spec 7 (M1). The harness's
8-consecutive cap, recorded in aReplayedCard (M9). `TOOL-cFinalBerth-1` S9 (L10).

**Harness and driver assumptions, and which were verified.** That the stop-guard blocks a
`LANDING` record's stop was ASSUMED by spec 7 and is contradicted by spec 3's table; read, not run
(B1). That the lander pushes before `--landed` is the Skill's text and the driver's comment; read (B1).
The 8-consecutive cap rests on the aReplayedCard record's verdict against the hooks doc; not
re-fetched here (M9). `claude auth status`'s logged-out exit code is recorded by spec 5 as unmeasured,
and that stays so (H4). PreToolUse/Stop payload fields are those the existing hooks read; no spec
assumes a field they do not.

## What this pass did NOT do, said rather than implied

- **It read documents and the source they cite; it drove no fixture.** The synthesis re-read at
  base `5f9648d6`: `tools/unattended/unattended.test.sh:71,1028,1859,1874`;
  `tools/unattended/unattended.sh:8,358-370,525-529,3244,3502` and the `rev-parse --git-dir` count;
  `tools/unattended/check-unattended.sh:1726` (check 22's failure text); `memory/map/features/
  unattended.md:270`; `tools/unattended/adopt-unattended.test.sh` for `git commit` (0);
  `tools/unattended/SKILL.template.md:815-832`; the aReplayedCard design record `:299`; and every
  spec line the table above cites. Reproductions that are the skeptic's and are reported as such:
  `map_diff.py`'s output surface (M1), the `stat`-shadowed dead-probe path of AC8 (L3), and the
  `check-unattended.sh:1685-1726` join body (H2), of which only the failure line was re-read here.
- **A spec audit grades what a document says.** B1 was found by reading three ratified records
  against the driver's order; the defect a correct-sounding sentence hides in an unbuilt mechanism
  is out of reach here, and every unit's confirmed set is subject to that limit.
- **The units' section 8 alternatives were read for what they resolve, not re-adjudicated** — except
  spec 7's rejection of B1, which the blocker turns on and which is argued above.
- **Precision was 0.80.** Reported; no re-priming is owed on that account. Round 2 should re-audit
  the revised set at its new blobs with one lens on B1's chosen resolution across specs 2, 3 and 7
  together, and one on the no-criterion class, since seven of the twenty-eight defects here span two
  specs, two are criteria that already hold at base, and eleven are carriers or grammar arms no
  criterion reads.
