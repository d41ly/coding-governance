# TOOL-dRedressedBar-16 — an apply that keeps a carried kit's claim keeps that kit's gate-leg ownership too, so a later argv change does not wedge the kit

**Status:** CLOSED · rev-5 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-16-1-acceptance-ledger.md](../build/2026-10-14-build-TOOL-dRedressedBar-16-1-acceptance-ledger.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-12-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-2-revision.md) | research | TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 |
| [2026-10-14-prompt-TOOL-dRedressedBar-16-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-16-4-revision.md) | research | TOOL-dRedressedBar-12 |
| [2026-10-14-prompt-TOOL-dRedressedBar-16-5-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-16-5-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md) | research | TOOL-dRedressedBar-19 TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 |
| [2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md) | research | TOOL-dRedressedBar-23 TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-17 |
| [2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 |
| [2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md) | diff-review | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 12 to 15
(`reviews/2026-10-14-review-TOOL-dRedressedBar-12-15-spec-audit-round1.md`) exited CONVERGED with
22 confirmed findings: no blocker, one high, 12 mediums and 9 lows. BUILD-METHOD M4 promotes the high
to its own unit, and this is that unit. It repairs `TOOL-dRedressedBar-12`, so its order is one above
unit 12's order 8. It shares that order with unit 13, and nothing downstream is renumbered.

| id | grade | item | sits in | what is wrong | closed by |
|---|---|---|---|---|---|
| 7 | HIGH | H1 | unit 12 §3 second non-goal, S2, §4 Alternatives row C5 | unit 12 keeps a carried kit in the receipt's `kits` but `apply` still passes no carry to `write_gate_legs`, so the kit's legs leave `gate_runner.emitted`; once gov changes one of those legs' argv, every `apply --kits <kit>` exits 2 and every `update --write` covering it exits 1, and neither verb can rebuild the ownership | S1 to S4 |

Unit 12's §3 says a leg row a carried kit loses from `emitted` "is re-claimed on its next run by the
same-argv rule ... so it wedges nothing". That holds only while gov's resolved argv for the leg is
unchanged. `check_leg_claimable` demands exact argv equality (`tools/govkit/govkit.py:4003-4008`), and
on a mismatch `write_gate_legs` raises the "already has a leg named ... receipt does not claim it"
Refusal (`:4143-4159`). This unit makes `apply` pass `carry_out_of_scope=True`, the rule the
function's own docstring gives a verb whose receipt keeps every claimed kit (`:4039-4043`), and arms
the narrower-apply-then-argv-change sequence that the report traced.

## 2. Scope (IN)

- **S1** — `_cmd_apply`'s LEGS call to `write_gate_legs` (`tools/govkit/govkit.py:7953-7955`) passes
  `carry_out_of_scope=True`. Nothing else in the call or in `write_gate_legs`' body moves: the carry
  at `:4303-4305` already keeps every prior `emitted` row whose `kit` is outside the selection, and
  the withheld and non-manifest branches already keep the prior rows whole. The non-manifest branch
  kept `emitted` whole while its order file, `.governance/outbox/gate-legs.md`, listed the
  selection's legs alone, so a narrower apply over a target with no runner left a carried kit's
  legs out of the order; `TOOL-dRedressedBar-23` corrects that (round-1 closing diff review report
  id 4). Observed by AC1, AC2 and AC3.
- **S2** — The `carry_out_of_scope` paragraph of `write_gate_legs`' docstring, as unit 12's S2
  leaves it, says that both verbs now keep every claimed kit in the receipt's `kits`, so both pass
  the carry, and names `TOOL-dRedressedBar-16`. It no longer argues from the same-argv rule, and it
  states why that rule is not enough: an argv gov changes is never claimable. The rewritten
  paragraph keeps `TOOL-dRedressedBar-12` beside `TOOL-dRedressedBar-16`, because spec 12's AC4
  reads that id there (`TOOL-dRedressedBar-19`, units-16-18 report id 8). Observed by AC3.
- **S3** — One `[dRB-16]` block in `tools/govkit/selftest.py`, after the `DEPL-cMendedVintage-13`
  arms, inside the scope that defines `build_gov13`, `build_target13`, `run_gov13`, `read_legs13`
  and `read_owned13` (`:15428-15512`). It runs §4's sequence on two targets built by
  `build_target13` from one gov built by `build_gov13`, and asserts AC1's and AC2's facts on the
  lines and rows they name. Every file write names `encoding="utf-8"`, and every process call goes
  through `run_gov13`, `git` or `settle`. Observed by AC1 and AC2, through the `New arm:` line in §7.
- **S4** — Spec 12 is corrected in place by this unit's spec-writer pass, `<w16>`, which runs once
  unit 12 is CLOSED and before the build pass (§4 "The spec-12 correction's pass"). It takes one rev
  bump whose revision line names report id 7 and this unit's AC1 and AC2. Its §3 second non-goal
  states that the `emitted` carry was taken by `TOOL-dRedressedBar-16`, because the same-argv rule
  does not reach an argv gov has changed. Its §4 Alternatives row C5 states that its rejection
  rested on that false premise and that this unit takes C5. Spec 12's S2 and criteria are not
  rewritten: unit 12 built against them as written, and its revision line points here. Spec 12's
  S2 states the same premise, so it carries an inline note that its rationale is superseded by
  this unit, written by `TOOL-dRedressedBar-19`'s pass `<w19>` (units-16-18 report id 31). The build
  pass writes no spec file but this one's status and date cells. Observed by AC4.
- **S5** — The unit adds no module-level function or class, no text-IO site without an encoding, and
  no kit version. Observed by AC5.
- **S6** — Every reading below goes to this unit's acceptance ledger under
  `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal TOOL-dRedressedBar-16`.
  Observed by AC4.

## 3. Non-goals (OUT)

- No change to how `write_gate_legs` keys its carry. It keeps the prior row of every kit outside the
  selection, and a prior row with no `kit`, as `update` already relies on (`:4297-4305`). Keying it
  on the claim, as unit 12 keys its row carry, would be a second rule for one list.
- No claim test on the carried rows. An orphan, a prior `emitted` row whose kit the receipt no
  longer claims, is carried too, because the carry is keyed on the selection, which the non-goal
  above keeps. It is re-carried on every narrower apply. That is an accepted gap
  (`TOOL-dRedressedBar-19`, units-16-18 report id 43).
- No change to `update`'s call (`:11888-11890`), which already passes the carry.
- No change to `check_leg_claimable` or to the Refusal it guards. A leg the target wrote under gov's
  name with another argv is still refused, which is the point of that rule.
- No repair of a target an earlier engine already wedged. Its receipt holds no row this engine
  could carry, and the Refusal's message already names the runner's argv and gov's.
- No change to `_cmd_adopt`'s receipt write (`:12692`), which unit 12 also leaves alone.
- No bug-class checklist entry. The report's left-shift names one; it is its own mechanism, and the
  S3 arm is the gate that closes this finding.
- No `help/` page. `help/` holds `README.md` and `roles.md`, and neither covers govkit.

### Edges

- **consumes-from** `TOOL-dRedressedBar-12` — the receipt carry that keeps a kit apply did not select
  in `kits`, without which `apply --kits <carried kit>` is refused as foreign before it reaches LEGS
  and this unit's arm has no wedge to show. Also the `carry_out_of_scope` docstring paragraph its S2
  writes, which S2 here rewrites, and its spec's §3 and §4 C5 row, which S4's pass `<w16>` corrects. AC1's and
  AC2's red halves read its pass commit `<p12>`.
- **hands-off** `TOOL-dRedressedBar-19` — the docstring paragraph S2 rewrites, in which that unit
  keeps unit 12's id beside this unit's, and this spec's S2, S4, §3, §4 and AC3, which it corrects in
  place: both ids required, spec 12's inline note named, the orphan carry stated as an accepted gap,
  two citations, and a row for the contract-parity reader (units-16-18 report ids 8, 9, 18, 30, 31
  and 43).
- **hands-off** `TOOL-dRedressedBar-23` — `apply`'s `carry_out_of_scope=True`, which S1 passes, so
  `write_gate_legs`' non-manifest branch sees a carry on a narrower apply. That unit lists every
  claimed kit's legs in that branch's order file, each through the `_silenced` test, and its pass
  `<w23>` corrects this spec's S1 and "What an adopter sees change" in place (round-1 closing diff
  review report id 4).

## 4. Design

### The wedge, traced

Read at `46eb75ed`, whose `tools/` equals `ebce889c`'s (`git diff --stat ebce889c7 HEAD -- tools skills`
prints nothing). Unit 12 is unbuilt there, so the sequence below is derived from the code and from
unit 12's spec, not run. The report's skeptic traced the same path and judged the fix sound.

| Step, over a manifest target claiming kits A and B, each declaring one gate leg | At `<p12>` | After S1 |
|---|---|---|
| 1. `apply` selecting A and B | `emitted` holds A's leg and B's leg | unchanged |
| 2. `apply --kits A` | `kits` keeps B (unit 12). `write_gate_legs` builds `owned` from the prior `emitted` (`:4094`) and, with no carry, returns A's row alone. B's row in the runner stays, because the write is append and replace by name | `emitted` keeps B's row, ahead of A's (`:4303-4305`) |
| 3. gov commits a change to B's leg argv | — | — |
| 4. `update --write` | `_legs_scope` holds B (`:11876-11877`). B's leg is in the runner and not in `owned`, its argv differs, so `write_gate_legs`, called at `:11888-11890`, raises; `update`'s `except Refusal` at `:11898-11903` catches it as a problem and exits 1 | B's leg is owned and rewritten with the new argv; exit 0 |
| 5. `apply --kits B` | the same raise, uncaught in `apply`; exit 2 | B's leg is owned and rewritten; exit 0 |

At the base, without unit 12, step 5 is refused earlier as foreign (`foreign_kit_present`,
`:6679-6688`), because step 2 dropped B from `kits`. So the wedge is reachable only once unit 12
lands, and both red halves read `<p12>`.

### Why the carry is consistent after unit 12

The docstring's reason for `apply` passing no carry was that `apply` rewrote `kits` and `files` to
its own selection, so a carried `emitted` row could name a kit `kits` does not (`:4039-4043`). Unit
12 removes that premise: every kit the prior receipt claims stays in `kits`. A prior `emitted` row
whose kit the prior receipt claims was written by a run that selected its kit, and that kit is
still claimed, so such a carried row names a claimed kit. That is the case this proves. A row whose
kit the receipt no longer claims is carried too, an accepted gap (§3,
`TOOL-dRedressedBar-19`, units-16-18 report id 43). A prior row with no `kit` is carried too, which the comment at `:4297-4302` calls the
safe direction. On the withheld path `emitted` is still the prior list whole (`:4327`), so S1 does
not reach it.

### What an adopter sees change

| Situation | At `<p12>` | After |
|---|---|---|
| a narrower `apply` over a manifest target | `emitted` holds only the selection's legs | `emitted` also holds every other claimed kit's legs, ahead of this run's |
| then gov changes a carried kit's leg argv, and `update --write` runs | exit 1, `the gate-leg step refused` and `does not claim it` | exit 0; the leg carries the new argv |
| or `apply --kits <that kit>` runs | exit 2, `already has a leg named` | exit 0 |
| a narrower apply where the carried kits declare `subject = "kit"` legs | the held-legs advice counts this run's legs | it counts every kit-subject leg the runner holds, which is what its own comment says it counts (`:7967-7972`) |
| any apply whose selection covers every claimed kit | as before | unchanged |
| a narrower `apply` over a target with no `[gate_runner]` | `emitted` is the prior list whole, and `.governance/outbox/gate-legs.md` lists the selection's legs alone | unchanged by this unit. `TOOL-dRedressedBar-23` lists every claimed kit's legs in the order, a carried kit's leg naming a path the target lacks under `## WITHHELD` |
| after a narrower apply, a failing contract clause whose installed consumer sits on a carried kit's leg | `check` and `update` print it as unwired, because `emitted` lost that leg | `check` and `update` red it again, as after a full apply: `derive_parity_lines` (`tools/govkit/govkit.py:6075`, its `r.fail` at `:6119-6121`, called at `:5416` and `:9658`) builds its leg words from `emitted` (`TOOL-dRedressedBar-19`, units-16-18 report id 30) |

### The arm

`build_gov13` builds a scratch gov with two kits, `demo` and `demo2`, each declaring one gate leg
(`tools/govkit/selftest.py:15428-15459`). `build_target13` builds a manifest target whose runner is
`scripts/gate-legs.json` (`:15461-15477`). The `[dRB-16]` block builds one gov and two targets. On
each target it runs `apply`, `settle`, `apply --kits demo` and `settle`. It then rewrites `demo2`'s
leg argv in the gov to `["bash", "{prefix}/demo2/engine.sh", "--drb16"]` and commits it. The block
does not use `write_vintage13`, because that helper moves `demo2`'s engine bytes and this arm needs
the leg argv to move. On the first target it runs `update --target <t> --write`; on the second,
`apply --target <t> --kits demo2`.

### Order

Order 9 ties with unit 13. Their write sets intersect on `tools/govkit/govkit.py` and
`tools/govkit/selftest.py`, so M6's first clause sequences them at dispatch. Neither reads the
other's work, so either sequence holds, and neither is an edge. Unit 14 (order 10) reads unit 12's
two carried lists and never the LEGS call, so it is a sequence after this unit and not an edge.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `[dRB-16]` | the check-label prefix of the new selftest block | none |

### The spec-12 correction's pass

No one role can write S4's correction and the product files in one commit. Under
`.claude/roles.json`, only `gov-spec-writer` writes spec files and only `gov-builder` writes
product files, and scratch-guard admits a builder's spec edit only where it moves the status and
date cells of a spec its card routes (`tools/hooks/scratch-guard.js:91-99`). So S4 is this unit's
spec-writer pass, `<w16>`, M6's "a review's fixes folded in". The main loop dispatches it at this
unit's turn, once unit 12 is CLOSED, with S4 as its brief, and before the build pass. Spec 12 then
takes its correction as a records fix with its status unchanged. It does not run earlier: spec 12
is unbuilt until then, and unit 12 builds against its §3 and §4 as written. A build pass that finds
no `<w16>` returns that to the main loop before any write.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/builds/dRedressedBar/build/`

Spec 12 is `<w16>`'s write set, not the build pass's.

### Alternatives rejected

| Candidate | The test that could make it lose | Verdict |
|---|---|---|
| C1 — `apply` passes `carry_out_of_scope=True` | step 4 or step 5 still refusing after S1; a carried row naming a kit `kits` does not | Chosen; §4 "Why the carry is consistent" answers the second |
| C2 — loosen `check_leg_claimable` to accept an argv change for a leg gov emitted before | it cannot tell gov's earlier argv from a target's own command under gov's name, which is the laundering the Refusal exists to stop (`:4143-4148`) | Rejected on `[security]` |
| C3 — let `update` and `apply` re-claim any leg whose kit the receipt claims | the same laundering, keyed on the kit instead of the argv | Rejected on `[security]` |
| C4 — narrow unit 12's non-goal to "while the argv is unchanged" and leave the wedge | the report graded the wedge HIGH, and only hand-editing the target's runner clears it | Rejected |
| C5 — the spec-12 correction in the build pass's own commit, as rev-2 wrote it | scratch-guard refuses a builder's edit to another spec, and the spec writer writes no product file, so no role can make that commit (unit 10's divergence, `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`) | Refused by the hook |

## 5. Production-readiness checklist

- security — Widens nothing. A carried row is a row this engine wrote into the prior receipt, kept
  verbatim. The Refusal for a leg the target wrote under gov's name with another argv stands.
- perf / scale — N/A — one list comprehension over the prior `emitted`, once per apply.
- error / empty / loading states — No prior receipt, or one with no `gate_runner`, carries nothing.
  An apply whose selection covers every claimed kit carries nothing, so its receipt is unchanged.
- observability — No new line. The `gate legs: emitted <n>` count still states what this run built,
  because the carry runs after it is printed (`:4295-4297`).
- risks — An existing arm that asserts `emitted` holds the selection's legs alone after a narrower
  apply would red. `grep -n 'emitted' tools/govkit/selftest.py` finds the AC-withheld and AC-ordered
  comparisons (`:4142`, `:4228-4231`), which compare one selection's runs against each other, and
  `read_owned13` membership checks, which a superset still meets. The `govkit selftest` leg grades
  the rest at the close.
- testing — AC1 and AC2 are the S3 arm's sequence run by hand in scratch targets under `%TEMP%`, with
  a `<p12>` clone for the red halves. AC3 to AC5 are source probes. The new arm is declared in §7.
- migration — N/A — no receipt field, conf key or deploy shape moves.
- user docs — N/A — `help/` holds no govkit page, and `WIRE-INTO-PROJECT.md` states nothing about
  which kits' legs a narrower apply records.

## 6. Acceptance criteria

`<p12>` and `<p16>` are the commits of units 12 and 16's build passes, as their acceptance ledgers
name them. `<w16>` is the commit of this unit's spec-writer pass, which §4 "The spec-12 correction's
pass" describes; its subject names `TOOL-dRedressedBar-16`, and this unit's ledger names it. Every command runs from the worktree root. A target and a scratch gov live under
`%TEMP%/<short-name>`, never inside the worktree, built as `build_target13` and `build_gov13` build
them (`tools/govkit/selftest.py:15428-15477`). A red half copies `tools/govkit/govkit.py` from a
local `git clone` of gov under `%TEMP%`, checked out at `<p12>`, into the scratch gov.

- **AC1** — Run §4's steps 1 to 4 with `python <g>/tools/govkit/govkit.py`, where `<g>` is the scratch
  gov carrying the tip's engine. After step 2, `.governance/install.json`'s `gate_runner.emitted`
  holds a row named `demo2 leg` with kit `demo2`. Step 4, `update --target <t> --write`, exits 0, and
  no line carries `does not claim it` or `the gate-leg step refused`. Afterwards the runner's
  `demo2 leg` row carries `--drb16` in its `argv`.
  Red when: with the `<p12>` engine, step 2's `emitted` holds no `demo2 leg` row, and step 4 exits 1
  with a line carrying `does not claim it`.
  fixture: the red half is derived from `tools/govkit/govkit.py:4094`, `:4143-4159`, the
  `write_gate_legs` call at `:11888-11890` and its `except Refusal` at `:11898-11903`, and was not
  run at spec time, because unit 12 is unbuilt. The pass observes it
  first, and a red half that exits 0 is returned to the main loop and not counted.
  cost: one gov clone, two scratch govs and eight verb runs, about two minutes.
- **AC2** — Run steps 1 to 3 on a second target, then `apply --target <t2> --kits demo2`. It exits 0,
  no line carries `already has a leg named`, and the runner's `demo2 leg` row carries `--drb16`.
  Red when: with the `<p12>` engine the same apply exits 2, and one line carries
  `already has a leg named 'demo2 leg'`.
  fixture: derived, as AC1's red half is; the pass observes it first.
- **AC3** — A python program parses `tools/govkit/govkit.py` with `ast` and finds the call to
  `write_gate_legs` inside `_cmd_apply`. Its keywords include `carry_out_of_scope` with the constant
  `True`. `ast.get_docstring` of `write_gate_legs` carries `TOOL-dRedressedBar-16`, and, joined with
  `tr '\n' ' ' | tr -s ' '`, carries no `passes no carry`. The docstring also keeps
  `TOOL-dRedressedBar-12` beside it, which `TOOL-dRedressedBar-19`'s AC8 observes (units-16-18
  report id 8).
  Red when: the call has no such keyword, as at `<p12>`, or the docstring still says `apply` passes
  no carry set, as unit 12's S2 writes it.
- **AC4** — When `git diff <w16>~1 <w16> -- memory/builds/dRedressedBar/spec/` runs, spec 12 shows
  one header rev change and one new revision line, and that line names report id 7 and this unit's
  AC1 and AC2. Spec 12 carries a CLOSED header at `<w16>~1`. At `<w16>`, spec 12's §3, cut with
  `sed -n '/^## 3. Non-goals/,/^### Edges/p'` and joined, carries `TOOL-dRedressedBar-16` and no
  `so it wedges nothing`, and its Alternatives rejected sub-section, cut with
  `sed -n '/^### Alternatives rejected/,/^## 5/p'`, carries `TOOL-dRedressedBar-16` on the C5 row.
  `git diff --name-only <p16>~1 <p16> -- memory/builds/dRedressedBar/spec/` names no file but this
  spec. The ledger S6 names exists and carries `**Serves:** journal TOOL-dRedressedBar-16`.
  Red when: spec 12 takes no bump or two, its revision line misses id 7, AC1 or AC2, it was folded
  before it closed, its §3 still says the carried kit's legs wedge nothing (as at the audited blob
  `62910df0`), or the build pass writes another spec.
- **AC5** — `git diff <p16>~1 <p16> -- tools/govkit/ | grep -E '^[+-](def|class) '` prints nothing. A
  python program imports `tools/gate-lint/encoding_posture.py` and runs `scan_text_io` over
  `tools/govkit/govkit.py` and `tools/govkit/selftest.py` at `<p16>`. Per arm, it counts exactly the
  rows `memory/project/encoding-posture-sites.txt` declares.
  Red when: the pass minted a function, or added an unencoded text-IO site.
  figure: DERIVED from the registry at observation.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the `[dRB-16]` block with `apply`'s LEGS call restored to pass no carry, as at `<p12>`, where `update --write` reports `does not claim it` and `apply --kits demo2` exits 2 on `already has a leg named` · none

The refusal join's floor does not move: S1 changes one keyword and adds no refusal branch. The
main loop observes the new arm red, then green, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, promoted at the CONVERGED exit of the units-12-15 spec audit
  for report id 7 (H1). The wedge was traced through `write_gate_legs`, `check_leg_claimable` and
  both callers at `46eb75ed`, and four candidates were graded by M12, with the pick taken by M3's
  rule.
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-19`, the batch the
  units-16-18 spec audit's minors were promoted into, for that report's ids 8, 9, 18, 30, 31 and 43.
  No scope, design or criterion moves.
- rev-3 · 2026-10-14 · S4 · §3 · §4 · AC4 · unit 10's builder divergence, applied here
  (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`): no role can make a build-pass
  commit that also edits another spec, because scratch-guard admits a builder's spec edit only to
  its own status and date cells (`tools/hooks/scratch-guard.js:91-99`). The moved item: S4, spec
  12's rev bump with its §3 second non-goal and §4 row C5 corrections, is now this unit's
  spec-writer pass `<w16>`, dispatched once unit 12 is CLOSED and before the build pass. It is not
  folded now, because unit 12 is unbuilt. §4 gains "The spec-12 correction's pass", Files touched
  lists product files and the ledger only, AC4 reads spec 12 at `<w16>` and observes that the build
  pass writes no other spec, §3's consumes-from edge names `<w16>`, and Alternatives rejected gains
  row C5. No product design or other criterion moves.
- rev-4 · 2026-10-15 · S2 · S4 · §3 · §4 · AC1 · AC3 · a records fix for TOOL-dRedressedBar-19,
  closing the units-16-18 spec audit's report ids 8, 9, 18, 30, 31 and 43 (items L6, L7, L13, L16
  and L20), written by that unit's spec-writer pass `<w19>`. The status stays CLOSED. Id 8: S2 and
  AC3 state that the rewritten paragraph keeps `TOOL-dRedressedBar-12` beside this unit's id. AC3
  read this unit's id alone, so a rewrite dropping unit 12's would have passed it and red spec 12's
  AC4; unit 16 built both ids in (`tools/govkit/govkit.py:4248-4253` at `997fc294f`), and
  TOOL-dRedressedBar-19's AC8 observes both. Id 31: S4 names the inline note spec 12's S2 now
  carries. Id 43: §3 gains the orphan carry as an accepted gap, and §4 "Why the carry is
  consistent" narrows its sentence to rows whose kit the receipt claims. Id 30: "What an adopter
  sees change" gains the row for `derive_parity_lines`. Id 9: "The arm" cites `build_gov13` from
  its `def` at `:15428`, where it cited the last line of `M13_DEPLOY`, `:15412`. Id 18: §4 step 4
  and AC1's fixture line cite the `write_gate_legs` call at `:11888-11890` and the `except Refusal`
  at `:11898-11903` apart, where both cited one range from `:11880` to `:11891` holding the call
  alone. AC1's assertions do not move. Every citation is at the base `ebce889c`, as §4's evidence
  reads it. TOOL-dRedressedBar-19's AC8, AC9, AC18, AC30, AC31 and AC43 observe these.
- rev-5 · 2026-10-15 · S1 · §3 · §4 · a records fix for TOOL-dRedressedBar-23, closing the round-1
  closing diff review's report id 4 (item M3), written by that unit's spec-writer pass `<w23>`. The
  status stays CLOSED, and no criterion text moves. S1's sentence on the non-manifest branch states
  that it kept `emitted` whole while its order file listed the selection's legs alone: at
  `c84518fff` that branch loops `selection` (`tools/govkit/govkit.py:4552`) and sets
  `emitted = list(prior)` (`:4591`). "What an adopter sees change" gains the row for a narrower
  apply over a target with no runner, and Edges gain the hands-off to TOOL-dRedressedBar-23, whose
  AC2 observes the order listing a carried kit's legs.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "carry gate leg ownership rows of kits outside a narrower
apply selection"` ranked name-stem matches (`rows`, `legs`, `kit_rel`, `resolve_kit_dir`) and no
leg-ownership function. That is a miss, recorded as one. The seam was found by reading the report's
citation: `write_gate_legs`' `carry_out_of_scope` parameter (`tools/govkit/govkit.py:4015`,
`:4303-4305`), which `update` already passes (`:11890`). S1 passes the same argument from the
other caller, so no carry logic is written. The arm extends the `DEPL-cMendedVintage-13` fixture
builders (`tools/govkit/selftest.py:15428-15512`), which already hold a two-kit gov and a manifest
target. The gotchas checklist for the two product paths selected `two-answers-to-one-question`,
which is why both verbs now take one carry rule; `staged-break-substitutes-a-synthetic-value`, which
is why the red half copies the `<p12>` engine rather than hand-editing `emitted`; and
`line-claim-matched-over-the-whole-output`, which is why AC1 and AC2 name the line they read.

The recall probe returned unit 12's §3 sentence and the report's finding, which agree with the code
re-read here. It returned `DEPL-cMendedVintage-13` AC2, the `update` half of the same rule: an
out-of-scope kit's leg stays in the runner and stays claimed by `emitted`. And it returned the
aScouredKit closing review, which measured the same class from the withheld path: `owned` derives
only from `emitted`, so a blanked list makes the next run refuse legs gov wrote.

Recall terms used: `python tools/memory-recall/query.py "why does apply pass no carry to
write_gate_legs, and what wedges when a claimed kit loses its emitted leg rows" --terms
"carry_out_of_scope emitted gate_runner owned leg claimed wedge same-argv narrower apply receipt"`
