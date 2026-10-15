# TOOL-dRedressedBar-17 — the units-12-15 spec audit's 12 mediums and 9 lows, batched: each faulted criterion observed in a form that can pass and fail, each false sentence corrected, and the code sites they describe made to hold what the specs claim

**Status:** CLOSED · rev-6 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-build-TOOL-dRedressedBar-17-1-acceptance-ledger.md](../build/2026-10-15-build-TOOL-dRedressedBar-17-1-acceptance-ledger.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md) | research | TOOL-dRedressedBar-10 TOOL-dRedressedBar-13 TOOL-dRedressedBar-19 |
| [2026-10-14-prompt-TOOL-dRedressedBar-17-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-4-revision.md) | research | TOOL-dRedressedBar-9 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 |
| [2026-10-14-prompt-TOOL-dRedressedBar-17-5-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-5-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-17-6-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-6-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-17-7-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-7-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md) | research | TOOL-dRedressedBar-19 TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-18 |
| [2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md) | research | TOOL-dRedressedBar-23 TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 |
| [2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-16 TOOL-dRedressedBar-18 |
| [2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md) | diff-review | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 |
| [2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md) | diff-review | TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 12 to 15
(`reviews/2026-10-14-review-TOOL-dRedressedBar-12-15-spec-audit-round1.md`) exited CONVERGED with
22 confirmed findings: no blocker, one high, 12 mediums and 9 lows. BUILD-METHOD M4 promotes the
high alone, as `TOOL-dRedressedBar-16`, and batches every medium and low into ONE unit. This is that
unit. The minors land on specs 9, 12, 13, 14 and 15, so it repairs no unit in particular. It is
ordered after units 9 to 16, whose specs and tree it corrects, and the README's derived build-order
region says what follows it (`TOOL-dRedressedBar-19`, units-16-18 report id 4). It closes these
findings, by report id, each with the report item it shares:

| id | grade | item | sits in | what is wrong | closed by |
|---|---|---|---|---|---|
| 1 | MEDIUM | M1 | unit 15 S6, §5, §7 against unit 14 S4, AC1 | the `[dRB-14]` block asserts agent-cap's problem line, which the `[dRB-15]` checks assert absent on the same apply | S1 |
| 2 | MEDIUM | M2 | unit 12 S1 against AC1 to AC6; unit 14 S2 | `install.sums` and the `STEP_RECEIPT` counts are claimed observed, and no criterion reads either | S2 |
| 3 | MEDIUM | M3 | unit 13 AC15, S17 | the spelling ban spans fixture A too, so it can fail a correct build and pass a wrong one | S3 |
| 4 | LOW | L1 | unit 15 §7 | the leg line names neither `format-guard self-test` nor `kit placeholders` | S4 |
| 5 | LOW | L2 | unit 14 §3 Edges, §4 "Order, and unit 7" | denies an edge to unit 13 that its criteria use, and describes README edits as pending that are made | S5 |
| 6 | LOW | L3 | unit 13 §1 | says it is ordered after every unit, and units 14 and 15 follow it | S6 |
| 8 | LOW | L4 | unit 13 §5 risks, §3, §10 | says both sibling decode sites are strict; the regenerate site already decodes with replacement | S8 |
| 9 | LOW | L5 | unit 14 §4 "The receipt written ahead" | lists two of the six `rows.append` sites in `_cmd_apply` | S9 |
| 10 | MEDIUM | M4 | unit 15 §4 "The class gate", S5, §10 | a second argv walker with a different "is this a path" rule from `silenced_legs` | S10 |
| 11 | MEDIUM | M6 | unit 15 §3, S1, S4 Readers | two `[adopt].argv` readers answer wrong for a `via` entry beside a rendered, generated or merged rule, and a docstring quotes deleted code | S11 |
| 12 | MEDIUM | M2 | unit 12 S1, AC1, AC3 | as id 2, from the reuse lens | S12 |
| 13 | MEDIUM | M5 | unit 15 S3, §4 row 5, AC5, AC9 | the gained loop's rewrite is observed by no criterion that runs `update` | S13 |
| 15 | MEDIUM | M7 | unit 15 §7 against §4 Files touched | the leg line omits `format-guard self-test`, which the `spec tokens` leg reports | S15 |
| 16 | LOW | L6 | unit 15 AC6 | `0 naming` also matches 10, 20 and 30 | S16 |
| 18 | MEDIUM | M8 | unit 15 S6, §7 | the `govkit selftest` guard misses the two sibling-kit files the `[dRB-15]` arms grade | S18 |
| 19 | LOW | L7 | unit 14 §4 "Every reader of the receipt during CONFIGURE" | omits `tools/playbook/render_playbook.py` | S19 |
| 20 | LOW | L8 | unit 15 §3, S4 Readers, against spec 9 §4 | spec 9 still describes agent-cap's argv that unit 15 takes away | S20 |
| 21 | LOW | L9 | unit 15 S8, §4 Files touched | runs the whole `regen.py --write` and accounts only for the map | S21 |
| 22 | MEDIUM | M9 | unit 14 §4 "When CONFIGURE fails" row 2, AC4 | the early receipt holds STAGE's oids, so an interrupt after RENORMALIZE makes the re-run refuse DIRTY | S22 |
| 23 | MEDIUM | M10 | unit 14 S1, S2, §4 | both receipt writes use a plain `write_text`, so a mid-write fault truncates `install.json` | S23 |
| 24 | MEDIUM | M11 | unit 15 S1, S5, §4, AC7 | a malformed `via` value is undefined at run time: `via = ""` falls back to the entry's own argv, which silently unwires agent-cap's hook. As built at `<p15>`, selfcheck refuses `""` and a list as naming no registry entry, and crashes on neither | S24 |

Id 16 was graded medium by its finder and low by the skeptic, and the skeptic's grade binds. Id 11's
fix was judged UNSOUND, and the skeptic's corrected fix is the one S11 takes. Ids 14 and 17 were
refuted by the audit and are not findings. Units 9 to 16 build first, as written. Once they are
CLOSED, this unit's spec-writer pass corrects the false prose in specs 9, 12, 13, 14 and 15 and
writes their revision lines, because only that role writes spec files. Its build pass then
observes, over the tree they leave, the corrected form of each criterion the audit found could not
pass or could not fail, and changes the code sites §4 lists so they hold what those specs claim.

## 2. Scope (IN)

Item S<n> closes report id n. Id 7 is HIGH and belongs to `TOOL-dRedressedBar-16`, so no S7 exists,
and ids 14 and 17 were refuted, so no S14 or S17 exists. S25 is the record. Items that share a
report item share its observation, and each still names its own id.

- **S1** — id 1, M1. The checks of the `[dRB-14]` block in `tools/govkit/selftest.py` narrow to
  settings-merge's CONFIGURE line, the receipt's `scripts/hooks/agent-cap.js` row and the
  `.claude/settings.json` command. The check on agent-cap's problem line moves out of that block, so
  the `[dRB-15]` checks on the same apply own agent-cap's outcome. Spec 14's S4 states that unit 17
  narrowed the block after unit 15. Spec 15's §5 risks restates its reader inventory over the tree
  unit 14 leaves and names the `[dRB-14]` check as a reader by value. Observed by AC1.
- **S2** — id 2, M2. The `[dRB-12]` block gains three checks after its step 2. The line carrying
  `/RECEIPT]` states the lengths of the receipt's `files` and `kits`. The `(sha256, path)` pairs of
  `.governance/install.sums` equal those of every receipt row carrying `sha256`, the carried rows
  included. `govkit check --target <t>` prints no line carrying `install.sums carries` or
  `which install.sums does not`. The `[dRB-14]` block gains the same sidecar check. The revision
  lines of specs 12 and 14 state that no criterion of theirs read the sidecar and name AC2.
  Observed by AC2.
- **S3** — id 3, M3. Fixture B of the `[dRB-11]` block sits between two comment lines,
  `# [dRB-11] fixture B: begin` and `# [dRB-11] fixture B: end`. Inside them one check asserts
  that the appended agent-cap row carries none of `commit`, `sha256` and `gov_oid` before
  `write_vintage_receipt` runs, and all three after it. Fixture A's lines do not move. Spec 13's
  revision line states that AC15's span reached fixture A and names AC3. Observed by AC3.
- **S4** — id 4, L1. Spec 15's §7 leg line names `format-guard self-test` and
  `kit placeholders (a declared token its adopter substitutes)`. A sentence below it says the line
  is a floor, derived by joining §4 Files touched against the guards in `tools/gate-legs.json`, and
  names the second leg as unguarded and read by S4's Readers. Observed by AC4.
- **S5** — id 5, L2. Spec 14's Edges gain `consumes-from TOOL-dRedressedBar-13`, whose pass commit
  `<p13>` is the red-half reference of its AC1, AC2 and AC4, AC5's diff base and its `New arm:`
  line. Spec 13's Edges gain the mirror `hands-off TOOL-dRedressedBar-14`. Spec 14's "Order, and
  unit 7" points at the Build-level rules of `memory/builds/dRedressedBar/README.md` and its derived
  build-order region, and no longer describes a roster row, a step or a Build-level sentence as
  pending. Observed by AC5.
- **S6** — id 6, L3. Spec 13's §1 says it is ordered after units 10, 11 and 12, whose specs and tree
  it corrects, and points at the README's derived build-order region for the units that follow.
  Observed by AC6.
- **S8** — id 8, L4. Spec 13's §5 risks states that the regenerate site already decodes UTF-8 with
  replacement (`tools/govkit/govkit.py:10986-10988`), that its S13 makes CONFIGURE match it, and that
  only the gained loop (`:11119-11120`) decodes strictly. Its §3 fourth non-goal and its §10 cite the
  regenerate site as `:10986-10988`. Observed by AC8.
- **S9** — id 9, L5. Spec 14's §4 "The receipt written ahead" lists every append to `rows` in
  `_cmd_apply`, `:7424`, `:7502`, `:7540`, `:7593`, `:7616` and `:7621`, states that each sits before
  the STAGE step (`:7646`), and names the command that produced the list. Observed by AC9.
- **S10** — id 10, M4. One module-level generator in `tools/govkit/govkit.py`, placed after
  `silenced_legs`: `scan_entry_argv(descs, selection, target, deploy, kinds)`. It yields one tuple
  per argv element, `(eid, source, kind, name, declared, resolved, missing)`, for the kinds asked:
  `[adopt]`, `[check]`, `[[gate_leg]]` and `[[regenerate]]`. Each element goes through
  `resolve_tokens` with the `target_context` of the entry that owns it, and for `[adopt]` that is
  the source entry S24 defines. Three readers take their walk from it. `silenced_legs` asks for
  `[[gate_leg]]` and keeps its predicate and return shape. `resolve_adopter_argv` asks for `[adopt]`
  and returns the `resolved` texts, so the source-entry choice is written once. Unit 15's S5
  ownership join asks for all four. One rule grades an element in both checks: its resolved text
  carries `/` and its `missing` is empty. The `gate legs:` note counts the `[[gate_leg]]` tuples and
  the `cross-entry argv:` note counts all of them, so the two offered counts are one population and
  its part. That note reads
  `cross-entry argv: <o> argv element(s) offered by [adopt], [check], [[gate_leg]] and [[regenerate]] across <m> entries, <g> graded, <h> naming a file only another entry ships`,
  with no label narrowing the population it counts (`TOOL-dRedressedBar-19`, units-16-18 report
  id 2). Spec 15's §4 "The ownership join" and §10 say S5 extends `silenced_legs` through the
  generator. `python tools/codebase-map/gen_map.py --write` runs alone before the product commit.
  Observed by AC10.
- **S11** — id 11, M6, by the skeptic's corrected fix. The docstring of `check_entry_producer`
  quotes the CONFIGURE lines as unit 15's S2 wrote them and says `via` is followed there. Its body,
  and the merged-rule guard's body (`tools/govkit/govkit.py:7314-7316`), keep their logic. Unit 15's
  `via` rules gain a fifth, after its four: the entry's `[[files]]` holds no rule whose role is
  `rendered`, `generated` or `merged`. Its reason is
  `carries a rendered, generated or merged rule, which the producer test and the merged-rule guard read through its own [adopt] argv`.
  Spec 15's §3 non-goal on the other readers and its §4 rule table name the fifth rule. Observed by
  AC11.
- **S12** — id 12, M2. The reuse lens's reading of S2's defect, citing the sidecar's write from
  `rows` (`:8027-8028`). Closed by S2's checks. Observed by AC2.
- **S13** — id 13, M5. The `[dRB-9]` block gains one case: a target built as `stale_target` builds it
  (`tools/govkit/selftest.py:3237-3249`), with `--kits check-wiring,kickoff-manifest` in its first
  apply and `[kit.agent-cap] prefix = "scripts"` appended to its deploy, so `update --write` gains
  both agent-cap and settings-merge. Of the lines that open `govkit update — default-gained ` and
  carry `adopter exit`, exactly one names agent-cap or settings-merge, and it opens
  `govkit update — default-gained agent-cap:`. No line carries `can't open file`. The case asserts
  no exit code (§4, "Three choices"). Spec 15's §4 "What an adopter sees change" row 5 points at AC13
  in place of "Derived, not run". Observed by AC13.
- **S15** — id 15, M7. Spec 15's §7 leg line names `format-guard self-test`, as S4 states. Observed
  by AC4.
- **S16** — id 16, L6. Unit 15's AC6 is observed with the hit count parsed by `, (\d+) naming` and
  compared with 0, and its red half with 1. Spec 15's revision line names AC16. Observed by AC16.
- **S18** — id 18, M8. The `govkit selftest` leg in `tools/gate-legs.json` gains the guard paths
  `{prefix}/hooks/kit.toml` and `{prefix}/settings-merge.py`, as exact files. In a second commit
  the kickoff manifest `memory/guides/SESSION-KICKOFF.md` is re-audited against that edit and
  re-stamped, as commit `2e187ee8b` did, with a `manifest-audit:` line in its body. Spec 15's
  revision line names AC18. Observed by AC18.
- **S19** — id 19, L7. Spec 14's reader table gains a row for `tools/playbook/render_playbook.py`
  (`:79-112`, `:285`, `:482`), reached from playbook-render's adopter. The row states the
  per-kit-prefix change to the gate-runner line and the role roster. A line under the table records
  the inventory command and that it printed five files. Observed by AC19.
- **S20** — id 20, L8. Spec 9's §4 "Why the shared argv stays safe" and "What it does not check" are
  corrected in place: agent-cap runs settings-merge's argv through `[adopt] via`
  (`TOOL-dRedressedBar-15`), and the safety argument holds through `via` and the dedup on resolved
  argvs. Spec 15's S4 Readers name those two spec-9 sentences in their by-name half. Observed by
  AC20.
- **S21** — id 21, L9. Spec 15's S8 names `python tools/codebase-map/gen_map.py --write` as the run.
  Its revision line names every path unit 15's product commit moved outside its §4 Files touched, or
  states that none moved. Observed by AC21.
- **S22** — id 22, M9. When `_renormalized` is true, `_cmd_apply` writes the receipt once more,
  right after the `oid` re-stamp loop (`tools/govkit/govkit.py:7926-7936`), with `_rcpt_doc["files"]`
  re-derived as `rows + _carried_rows`, through `write_atomic`. Spec 14's "When CONFIGURE fails"
  table states that a re-run of `apply` recovers from an interrupt anywhere except between
  `git add --renormalize` and that write, a stretch in which no adopter, leg or runner runs.
  Spec 14's revision line names AC22. Observed by AC22.
- **S23** — id 23, M10. `ADOPTER_BAR_PATHS` (`:3964`) gains `receipt_path`, so the self-test's
  routing assertion grades the receipt. That arm's liveness was aggregate over the members, so a
  member matching nothing passed until `TOOL-dRedressedBar-23` graded each (round-1 closing diff
  review report id 13). Every write to it goes through `write_atomic`: unit 14's
  early write and RECEIPT write, S22's write, `update`'s three (`:12017`, `:12055`, `:12062`) and
  `adopt`'s (`:12692`). The comment above the constant and `write_atomic`'s docstring name the
  receipt. Spec 14's "When CONFIGURE fails" table gains a row for an interrupt during a receipt
  write: the previous file stays whole. Observed by AC23. The `install.sums` sidecar written beside
  each receipt stays a plain write here. `TOOL-dRedressedBar-19`'s S40 writes it first through
  `write_atomic` and the receipt last, declares it a member, and has both comments name it; an
  interrupt between the two writes then leaves a new sidecar beside the old receipt, which `check`
  reports until the next apply rewrites both (units-16-18 report ids 23 and 40).
- **S24** — id 24, M11, restated against `<p15>`. There selfcheck already takes every entry whose
  `[adopt]` table holds the `via` key, whatever its value (`tools/govkit/govkit.py:3296`), and
  refuses a value that is not a string naming a registry entry under rule 1's reason,
  `names no registry entry`, with no traceback (`:3297-3300`). So the selfcheck half is a reason
  refinement: unit 15's `via` rules gain a first rule, ahead of the four, that `<v>` is a non-empty
  string, reason `is not a non-empty string`, and `""` and a list read that reason in place of
  `names no registry entry`. The run-time half is the behaviour change. At `<p15>`,
  `resolve_adopter_argv` takes `via` as the source only when it is a non-empty string and otherwise
  falls back to the entry itself (`:1511-1512`), so `via = ""` on an entry with no argv of its own,
  as agent-cap, resolves to `[]` and CONFIGURE skips it with no line (`:7937-7939`).
  `scan_entry_argv` takes the key's presence as the delegate declaration: a value that is not a
  non-empty string naming a registry entry raises `KeyError` naming the entry, and never falls back
  to the entry's own argv. Spec 15's S1 sentence on a non-string `via` and its §4 rule table are
  corrected. Observed by AC24.
- **S25** — The record, in two passes. Specs 9, 12, 13, 14 and 15 each take ONE rev bump in this
  unit's spec-writer pass, `<w17>`, which runs once units 9 to 16 are CLOSED and before the build
  pass. Each revision line names `TOOL-dRedressedBar-17` and every report id §4's table assigns that
  spec. The build pass writes no spec file but this one's status and date cells. Every reading
  above goes to this unit's acceptance ledger under `memory/builds/dRedressedBar/build/`, carrying
  `**Serves:** journal TOOL-dRedressedBar-17`. Observed by AC25.

## 3. Non-goals (OUT)

- Rewriting a faulted criterion of specs 12 to 15. Each was built against its §6 as written. Its
  revision line states which half did not hold and names the criterion here that observes the
  corrected form. Prose stating a false fact is corrected in place, as units 10 and 13 did.
- Re-running the build of units 9 to 16, or re-observing a criterion the audit did not fault.
- The report's left-shift proposals that are their own mechanism: the spec-tokens checks, the lint
  over `.governance/` writes, the `reuse_lookup` ranking change and the new checklist entries. The
  classes the report names that already exist under `memory/gotchas/` stay as they are. S10's one
  walker and the S11 and S24 `via` rules are the gates the report names for their findings, so they
  are in scope.
- No change to `update`'s gained-loop order relative to its receipt write. A gained kit at a per-kit
  prefix is still in no receipt its sibling's adopter reads, which is unit 14's external hand-off.
- No change to `check_entry_producer`'s or the merged-rule guard's logic (S11).
- No new gate leg, and no change to any leg's argv. S18 widens one guard.
- No kit version moved. Every product file sits under `{prefix}/govkit` or is `tools/gate-legs.json`,
  and the registry exempts both (`tools/govkit/registry.toml:295-297`, `:206-208`).
- No `help/` page. `help/` holds `README.md` and `roles.md`, and neither covers govkit.

### Edges

- **consumes-from** `TOOL-dRedressedBar-9` — its `[dRB-9]` update-gaining block, which S13 extends
  with the per-kit gaining case, and its spec's §4 sentences on agent-cap's argv, which S20
  corrects. Without the block there is no update fixture to extend.
- **consumes-from** `TOOL-dRedressedBar-12` — its `[dRB-12]` block, which S2 extends, and the
  receipt carry whose sidecar S2 reads. Its spec's revision line is what S25 bumps for ids 2 and 12.
  Without the carry there are no carried rows for the sidecar to miss.
- **consumes-from** `TOOL-dRedressedBar-13` — fixture B of the `[dRB-11]` block as its S17 rebuilt
  it, which S3 brackets and checks. Its spec's §1, §3, §5 and §10 are what S6 and S8 correct, and its
  Edges take the mirror S5 writes.
- **consumes-from** `TOOL-dRedressedBar-14` — the early receipt write and `_rcpt_doc`, which S22
  writes once more and S23 routes through `write_atomic`, and its `[dRB-14]` block, which S1
  narrows and S2 extends. Its spec's S4, §3 and §4 are what S1, S5, S9, S19, S22 and S23 correct.
  AC22's and AC23's red halves read its tree.
- **consumes-from** `TOOL-dRedressedBar-15` — `resolve_adopter_argv`, the selfcheck `via` rules and
  ownership join, the gained loop's `_res_g` and the `[dRB-15]` checks, which S10, S11, S13 and S24
  extend. Its spec is what S4, S10, S11, S13, S15, S16, S18, S20, S21 and S24 correct. Most red
  halves here read its pass commit `<p15>`.
- **hands-off** `TOOL-dRedressedBar-19` — the receipt routing S23 adds, beside which that unit
  writes the sidecar first through the atomic writer and declares it a member; the comments S23
  claims observed, which it observes; the note S10 counts, whose label it corrects; the `[dRB-14]`
  checks, which it reads by label. Also this spec's §1, S10, S23, §4, §5, AC1, AC9, AC10, AC23 and
  §10, which it corrects in place (units-16-18 report ids 2, 4, 5, 16, 17, 23, 40 and 41).
- **hands-off** `TOOL-dRedressedBar-23` — `receipt_path` as a member of `ADOPTER_BAR_PATHS`, which
  S23 adds, and the `[dRB-12]` sidecar checks S2 adds, beside which that unit's `[dRB-12]` order
  checks sit. That unit grades the `[-21] AC2` routing arm's liveness per member, and its pass
  `<w23>` corrects this spec's S23 and §10 in place (round-1 closing diff review report id 13).

## 4. Design

### Evidence, read at `46eb75ed` on 2026-10-14

`46eb75ed`'s `tools/` equals `ebce889c`'s (`git diff --stat ebce889c7 HEAD -- tools skills` prints
nothing). Specs 12 to 15 were read at the blobs the report pins. Units 9 to 16 are unbuilt there, so
every reading of a code site they add is derived from their specs.

- `silenced_legs` walks `[[gate_leg]]` argv per entry through `target_context` and grades an element
  whose resolved text carries `/` and whose `missing` is empty (`tools/govkit/govkit.py:3908-3946`).
  The selfcheck note at `:3217-3221` counts every declared gate-leg argv element as offered.
  `tools/codebase-map/kit.toml:104` declares `argv = ["python", "{gate_file}"]`, whose declared text
  carries no `/`.
- `check_entry_producer`'s docstring quotes `argv = d.get("adopt", {}).get("argv") or []` and
  `if not argv: continue` (`:3687-3699`). The merged-rule guard reads the declared argv (`:7314-7316`).
  Roles `rendered` and `generated` are side-effect kinds (`:3655-3656`).
- `apply` writes the sidecar from `rows` and prints `len(rows)` and `len(selection)`
  (`:8027-8030`). `check` compares the sidecar and the receipt both ways (`:5318-5333`).
- `write_atomic` writes a sibling and `os.replace`s it (`:3967-4000`). `ADOPTER_BAR_PATHS` declares
  `'gr["file"]'` alone (`:3964`), and the `[-21] AC2` routing arm reads that constant
  (`tools/govkit/selftest.py:15838-15917`). Every receipt write in `govkit.py` is spelled
  `receipt_path.write_text` (`:8019`, `:12017`, `:12055`, `:12062`, `:12692`).
- RENORMALIZE runs `git add --renormalize` and sets `_renormalized` (`:7857-7858`). The re-stamp
  sets `oid` in memory only (`:7926-7936`). Carve-out 3 of `dirty_claimed_paths` keeps a staged path
  only when its index oid equals the recorded one (`:6918-6922`).
- The registry default at the selftest's `OLD` vintage holds `kickoff-manifest` and neither
  agent-cap nor settings-merge (`git show 24f39915:tools/govkit/registry.toml`). agent-cap requires
  `settings-merge` and `kickoff-manifest` (`tools/hooks/kit.toml:9`). The default at HEAD lists
  agent-cap before settings-merge (`tools/govkit/registry.toml:48-49`), and `derive_default_gained`
  keeps that order (`tools/govkit/govkit.py:970-997`).
- `git grep -l '>>> resolve_kit_dir' -- 'tools/*adopt-*.sh' 'tools/playbook/*.py' 'tools/settings-merge.py'`
  prints six files. One is `tools/unattended/adopt-unattended.test.sh`, a suite and no reader, so the
  inventory command S19 records adds `':!*.test.sh'` and prints five.
- `tools/gate-legs.json` sits on the kickoff manifest's `watch:` line
  (`memory/guides/SESSION-KICKOFF.md:6`), so an edit to it reds the `kickoff-manifest ratchet` until
  the manifest is re-stamped.

### Three choices, derived

**Id 13's observation is not the report's sketch.** The report asks for one
`default-gained ... adopter exit 0` line and a `scripts/hooks/agent-cap.js` command in
`.claude/settings.json`. Neither can hold. `update`'s gained loop runs before `update` writes its
receipt (`:11104-11126` against `:12017-12062`), so settings-merge.py, run as agent-cap's delegate,
finds no receipt row for a hook at `scripts/hooks/` and exits 2. That is unit 14's external
hand-off and stays out of scope here. What S3 of unit 15 changes is which argv the loop resolves,
and that is visible in the count and the kit of the adopter lines. Over `<p14>`, agent-cap's argv
resolves to `scripts/settings-merge.py` and settings-merge's to `tools/settings-merge.py`, so two
lines print and one tail carries `can't open file`. Over a gained loop that reads the declared argv,
agent-cap has none after unit 15's S4, so the one line is settings-merge's. Over S3, agent-cap
runs first and its tuple equals settings-merge's, so the one line is agent-cap's.

**Id 22 takes the report's fix (a).** Spec 14's design is that a re-run of `apply` recovers from an
interrupt, and its table claims it. Fix (b) narrows that claim to interrupts before RENORMALIZE and
leaves LEGS and AFTER, the longest stretch, exposed. Fix (a) keeps the claim true for every
stretch but one, in which nothing long runs. M3's rule takes the option that satisfies more of
the stated design, and neither option widens a surface: the extra write is to the same file,
through the atomic writer.

**Id 23 routes every receipt write, not unit 14's two.** The report's fix names unit 14's writes. The
same truncation reaches `update`'s three and `adopt`'s one, and the report's left-shift asks for a
check over `.governance/` writes. `ADOPTER_BAR_PATHS` is that check's existing seam: the routing arm
already refuses a direct write to any declared member, and its comment says adding a member is meant
to be deliberate (`:3955-3963`). The receipt is read by the adopter's `receipt sync` leg
(`tools/run-gates/check-receipt.py:60-71`), so it is an adopter-bar path. Declaring it routes every
receipt write, or the arm reds on the one left behind. That is the charter's `[class]` and `[reuse]`
rules, so the narrower option is not a fork. The `install.sums` sidecar written after each receipt
write is not routed here, and `TOOL-dRedressedBar-19`'s S40 routes it (units-16-18 report id 40).

### What this unit corrects in each spec

No one role can write these corrections and the product files in one commit. Under
`.claude/roles.json`, only `gov-spec-writer` writes spec files and only `gov-builder` writes
product files, and scratch-guard admits a builder's spec edit only where it moves the status and
date cells of a spec its card routes (`tools/hooks/scratch-guard.js:91-99`). So the rows below are
this unit's spec-writer pass, `<w17>`, M6's "a review's fixes folded in". The main loop dispatches
it once units 9 to 16 are CLOSED, with this table as its brief, and before the build pass. Each
target then takes its correction as a records fix with its status unchanged. It does not run
earlier: specs 12 to 15 are unbuilt until then, and folding into them before they build is the
first rejected alternative below. A build pass that finds no `<w17>` returns that to the main loop
before any write.

| Spec | Ids | What moves |
|---|---|---|
| 9 | 20 | §4 "Why the shared argv stays safe" and "What it does not check": the two sentences on agent-cap's argv |
| 12 | 2, 12 | revision line only: S1's sidecar and step-line claim was observed by no criterion; it names AC2 |
| 13 | 3, 5, 6, 8 | §1 ordering sentence; §3 fourth non-goal's citation; Edges gain the hands-off to unit 14; §5 risks; §10 citation; its revision line names AC3 |
| 14 | 1, 2, 5, 9, 19, 22, 23 | S4 sentence; Edges gain the consumes-from unit 13; §4 "The receipt written ahead", "When CONFIGURE fails", the reader table and "Order, and unit 7"; its revision line names AC2, AC22 and AC23 |
| 15 | 1, 4, 10, 11, 13, 15, 16, 18, 20, 21, 24 | S1 and S8 sentences; S4 Readers; §3 non-goal on the other readers; §4 rule table, ownership join and "What an adopter sees change" row 5; §5 risks; §7 leg line and its floor sentence; §10; its revision line names AC10, AC11, AC13, AC16, AC18 and AC24. The ownership join's OFFERED and GRADED sentences and its note template, which S10's population changes, were left out of this row and move in `TOOL-dRedressedBar-19`'s pass (units-16-18 report id 2) |

### The code sites

| Id | File | Change |
|---|---|---|
| 1 | `tools/govkit/selftest.py` | the `[dRB-14]` block's agent-cap problem-line check moves out; its other checks stand |
| 2, 12 | `tools/govkit/selftest.py` | the `[dRB-12]` block gains the step-line, sidecar and `check` checks; `[dRB-14]` gains the sidecar check |
| 3 | `tools/govkit/selftest.py` | fixture B's markers and its before-and-after identity check |
| 10 | `tools/govkit/govkit.py`, `memory/map/generated/` | `scan_entry_argv`; `silenced_legs`, `resolve_adopter_argv` and the S5 join read it; both notes count its tuples |
| 11 | `tools/govkit/govkit.py`, `tools/govkit/selftest.py` | `check_entry_producer`'s docstring; the fifth `via` rule; its `[dRB-15]` scratch-gov case |
| 13 | `tools/govkit/selftest.py` | the `[dRB-9]` per-kit gaining case |
| 18 | `tools/gate-legs.json`, `memory/guides/SESSION-KICKOFF.md` | two guard paths; the manifest re-stamp |
| 22 | `tools/govkit/govkit.py` | the receipt write after the re-stamp |
| 23 | `tools/govkit/govkit.py` | `receipt_path` in `ADOPTER_BAR_PATHS`; every receipt write through `write_atomic`; two comments |
| 24 | `tools/govkit/govkit.py`, `tools/govkit/selftest.py` | the first `via` rule; key presence in `scan_entry_argv`; two `[dRB-15]` scratch-gov cases |

`scan_entry_argv` yields `[adopt]` tuples only when asked for that kind, so `silenced_legs`, which
runs inside `apply`'s LEGS, never meets a `via` it cannot resolve. The S5 arm passes the generator
only the entries its `via` rules left valid, as unit 15 already states for its join.

### Order, and unit 7

Order 12 places this unit after units 9 to 16, whose specs and tree it corrects, and the README's
derived build-order region says what follows it (`TOOL-dRedressedBar-19`, units-16-18 report
id 4). Units 13, 14, 15 and 16 each write
`tools/govkit/govkit.py` or `tools/govkit/selftest.py`, so M6 sequences this unit after all of
them. Unit 16 is a sequence and not an edge: it moves `apply`'s LEGS call and spec 12's §3 and §4,
and no criterion here reads its pass. Unit 7's measurement need not cover this unit, because no kit
version moves (§3). S10 mints one function, so S10 regenerates `memory/map/generated/` itself, with
the one generator the symbol index needs.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `scan_entry_argv` | a module-level generator | `py.function`. `lexicon.py --suggest scan_entry_argv --as py.function` prints `OK — scan_entry_argv leads with scan` |
| `# [dRB-11] fixture B: begin`, `# [dRB-11] fixture B: end` | comment markers in the selftest | none |
| `is not a non-empty string`, and S11's reason text | `via` rule reasons | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/gate-legs.json`
- `memory/map/generated/`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dRedressedBar/build/`

Specs 9, 12, 13, 14 and 15 are `<w17>`'s write set, not the build pass's.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| Fold each fix into specs 12 to 15 now, before they build | M4 forbids folding at a CONVERGED exit (owner, SPEC 2026-10-05) | Refused by the method |
| Two batch units | every half that is not prose writes `tools/govkit/govkit.py` or `tools/govkit/selftest.py`: S10, S22, S23 and S24 the first, S1, S2, S3, S11 and S13 the second (M6 clause 1) | Rejected |
| Id 13 by the report's sketch | update's gained loop runs before its receipt write, so the exit-0 line and the per-kit command cannot appear (§4, "Three choices") | Rejected; S13 observes the argv choice |
| Id 22 by fix (b), a narrowed claim | it leaves LEGS and AFTER, the longest stretch, without the recovery spec 14 designed | Rejected |
| Id 23 on unit 14's two writes alone | `update`'s and `adopt`'s receipt writes keep the same truncation, and no gate grades any of them | Rejected on `[class]` |
| Id 10 with `resolve_adopter_argv` keeping its own source choice | two places then decide which entry's argv `[adopt]` runs | Rejected on `[one-fact]` |
| Id 1 by narrowing spec 14 S4's text alone | the `[dRB-14]` check is in the built tree by then, and only the code change removes the contradiction | Rejected; the spec sentence moves with it |
| The spec corrections in the build pass's own commit, as rev-2 wrote it | scratch-guard refuses a builder's edit to another spec, and the spec writer writes no product file, so no role can make that commit (unit 10's divergence, `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`) | Refused by the hook |

## 5. Production-readiness checklist

- security — S23 narrows a failure mode: no interrupted run leaves a truncated receipt for the next
  `apply` to crash on or for a resolver to read as empty. S24 turns `resolve_adopter_argv`'s
  silent fallback into a `KeyError` at run time. Selfcheck already refuses a malformed `via` at
  `<p15>`, and S24 gives that refusal its own reason. `via` is still read only from gov's
  descriptors.
- perf / scale — N/A — one more receipt write on a renormalizing apply, one generator replacing two
  loops, and four fixture cases.
- error / empty / loading states — A malformed `via` is a selfcheck finding with a reason, never a
  traceback. An interrupt during any receipt write leaves the previous file whole. The
  `install.sums` sidecar beside it is a plain write after the receipt here; once
  `TOOL-dRedressedBar-19`'s S40 writes it first through `write_atomic` and the receipt last, an
  interrupt between the two leaves a new sidecar beside the old receipt, each whole, which `check`
  reports until the next apply rewrites both (units-16-18 report id 40).
- observability — The two selfcheck notes count one population and its part, so their offered
  figures agree by construction.
- risks — `scan_entry_argv` replaces the bodies of `silenced_legs` and `resolve_adopter_argv`; spec
  15's AC5 program, re-run at `<p17>`, must return the same lists, and AC10 re-reads
  `silenced_legs` against the generator over the real registry. The `govkit selftest` leg's guard
  widens by two files, so a scoped bar runs that leg on an edit to either. Editing
  `tools/gate-legs.json` trips the run-gates canaries and the kickoff-manifest ratchet, which S18
  re-stamps. The `govkit selftest` leg grades the rest at the close.
- testing — AC1 to AC25 are source and spec greps, in-process python probes, scratch applies under
  `%TEMP%`, scratch govs shaped as `build_scratch_gov_kit` builds them, and staged copies of gov.
  The moved arms are declared in §7.
- migration — N/A — no receipt field, conf key or deploy shape moves. A receipt written by an earlier
  engine is read as before.
- user docs — N/A — `help/` holds no govkit page, and `via` is documented in its function's
  docstring (spec 15 §5).

## 6. Acceptance criteria

AC<n> observes S<n>, so the numbering skips the ids no S item carries, and S12 and S15 are observed
by AC2 and AC4. `<pN>` is the commit of unit N's build pass, as unit N's acceptance ledger names it. `<p15a>` is
unit 15's product commit. `<p17>` is this unit's product commit and `<p17m>` its manifest re-stamp
commit. `<w17>` is the commit of this unit's spec-writer pass, which §4 "What this unit corrects in
each spec" describes; its subject names `TOOL-dRedressedBar-17`, and this unit's ledger names it.
Every command runs from the worktree root. "Joined" means piped through
`tr '\n' ' ' | tr -s ' '`. `<sN>` is `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-N.md`.
A target is a fresh `git init` tree under `%TEMP%/<short-name>`, never inside the worktree, with
`core.autocrlf false` and `DEPLOY_FULL`'s answers unless a criterion says otherwise. A red half
"over `<pN>`" runs `python <clone>/tools/govkit/govkit.py` from a local `git clone` of gov under
`%TEMP%`, checked out at `<pN>`.

- **AC1** — A python program reads `tools/govkit/selftest.py` and selects `check(` calls by label:
  every call whose first argument is a string opening `[dRB-14]`, wherever it sits. None of those
  carries `kit 'agent-cap'`. A call whose label opens `[dRB-15]` holds the check that no line opens
  `govkit: kit '`. Unit 17 observed this over the span bounded by each label's outermost lines,
  which a late label can stretch over the other block's checks; the label reading is
  `TOOL-dRedressedBar-19`'s AC41 (units-16-18 report id 41). Spec 14's §2, cut with `sed -n '/^## 2. Scope/,/^## 3/p'` and joined, carries
  `TOOL-dRedressedBar-17`. Spec 15's §5, cut with `sed -n '/^## 5. Production/,/^## 6/p'` and joined,
  carries `[dRB-14]`.
  Red when: over `<p15>`, a `[dRB-14]`-labelled check carries `kit 'agent-cap'` beside the
  `[dRB-15]`-labelled check that no such line prints, so one apply cannot satisfy both.
- **AC2** — Run spec 12's §4 steps 1 and 2 with `python tools/govkit/govkit.py apply` over a target,
  committing it after each. After step 2, the line carrying `/RECEIPT]` carries
  `<n> row(s), <k> kit(s)`, where `<n>` and `<k>` are the lengths of `.governance/install.json`'s
  `files` and `kits`. `.governance/install.sums`, parsed as `check` parses it
  (`tools/govkit/govkit.py:5324-5327`), equals the set of `(sha256, path)` pairs of the receipt's rows
  carrying `sha256`, and that set holds every carried `agent-cap` and `kickoff-manifest` row.
  `python tools/govkit/govkit.py check --target <t>` prints no line carrying `install.sums carries`
  or `which install.sums does not`. After spec 14's AC1 apply, the same sidecar equality holds.
  Red when: a scratch copy of gov at the tip whose sidecar write iterates this run's `rows` alone
  makes `check` print one `which install.sums does not` line per carried hashed row. A second copy
  whose step line counts `rows` and `selection` prints `2 row(s), 1 kit(s)`.
  figure: `<n>` and `<k>` are DERIVED from the receipt at observation. Spec 12 §4 PINNED 18 and 3 at
  `29c72f51`.
  cost: two applies, a `check` and two gov copies, about three minutes.
- **AC3** — A python program reads `tools/govkit/selftest.py` between the lines
  `# [dRB-11] fixture B: begin` and `# [dRB-11] fixture B: end`. The span calls
  `write_vintage_receipt(` exactly once, and holds a check before that call asserting the agent-cap
  row carries none of `commit`, `sha256` and `gov_oid`, and one after it asserting all three. Each
  marker line occurs exactly once in the file. Spec 13's revision log holds one new line naming
  report id 3 and AC3.
  Red when: the markers are absent, as at `<p15>`, or a copy whose row is appended with the three
  keys already set reds the before-check, which is the moved arm's staged break in §7.
- **AC4** — When spec 15's §7 is cut with `sed -n '/^## 7. Gates/,/^## 8/p'`, `grep -cF` finds
  `` `format-guard self-test` `` and
  `` `kit placeholders (a declared token its adopter substitutes)` `` on its leg line, and the cut
  carries `floor`. A python program reads the backticked paths under spec 15's
  `### Files touched (estimate)`, joins each against every leg guard in `tools/gate-legs.json` with
  `{prefix}` read as `tools`, as an exact file or as a directory either side holds, and skips a
  guard more than 5 legs carry (`BROAD_LEG_FLOOR`, `tools/check-spec-tokens.py:262`). Every leg it
  finds is named on the leg line.
  Red when: the program finds `format-guard self-test` unnamed, as over the audited blob `ebbcbbf0`.
- **AC5** — When `sed -n '/^### Edges/,/^## 4/p' <s14>` runs, it carries
  `` **consumes-from** `TOOL-dRedressedBar-13` ``. The same cut of `<s13>` carries
  `` **hands-off** `TOOL-dRedressedBar-14` ``. `grep -c 'is a sequence and not an edge, because no criterion here rests on its work' <s14>`
  and `grep -c 'The README changes this implies' <s14>` each print 0. The sub-section cut with
  `sed -n '/^### Order, and unit 7/,/^### Inventory/p' <s14>` carries `README.md` and `build-order`.
  Red when: each count prints 1, as over the audited blob `565574ae`.
- **AC6** — When `sed -n '/^## 1. Goal/,/^## 2/p' <s13>`, joined, is searched with
  `grep -c 'ordered after every unit'`, it prints 0, and the cut carries `build-order`.
  Red when: it prints 1, as over the audited blob `4cc48572`.
- **AC8** — `grep -c 'which decode strictly' <s13>` prints 0. `grep -c ':10986-10987' <s13>` prints
  0, and `grep -c ':10986-10988' <s13>` prints at least 2. Spec 13's §5, cut and joined, carries
  `:11119-11120`.
  Red when: the first count prints 1 and the second 2, as over `4cc48572`.
- **AC9** — When spec 14's §4 is cut with `sed -n '/^## 4. Design/,/^## 5/p'` and joined,
  `grep -c 'The only appends are'` prints 0. The cut carries `:7424`, `:7502`, `:7540`, `:7593`,
  `:7616`, `:7621` and `rows\.append`.
  `git show 46eb75ed:tools/govkit/govkit.py | awk 'NR>=7233 && NR<=8031 && /rows\.append/ {print NR}'`
  prints exactly 7424 7502 7540 7593 7616 7621 at 46eb75ed (`TOOL-dRedressedBar-19`, units-16-18
  report id 5).
  Red when: the two-site sentence stands, as over `565574ae`.
  figure: the six line numbers are PINNED at `46eb75ed` on 2026-10-14.
- **AC10** — A python program run from `tools/govkit` imports `govkit` at `<p17>`. Over a bare target
  and `read_descriptors`, as selfcheck builds them (`tools/govkit/govkit.py:3158-3170`), the
  `[[gate_leg]]` tuples of `scan_entry_argv` whose resolved text carries `/`, whose `missing` is
  empty and whose resolved text is not in `have` group to exactly what `silenced_legs` returns. The
  tuple for the `codebase-map coverage + freshness` leg's `{gate_file}` element
  (`tools/codebase-map/kit.toml:104`) has kind `[[gate_leg]]`. `inspect.getsource` of `silenced_legs`
  and of `resolve_adopter_argv` each carries `scan_entry_argv(` and no `resolve_tokens(`.
  `python tools/govkit/govkit.py selfcheck` prints one line opening `govkit: gate legs:` and one
  opening `govkit: cross-entry argv:`. The first's offered count equals the program's count of
  `[[gate_leg]]` tuples, and the second's equals its count of all tuples. A one-liner loading
  `memory/map/generated/symbols.json` finds an entry with id `scan_entry_argv` and file
  `tools/govkit/govkit.py`. Spec 15's §10, cut with `sed -n '/^## 10. Reuse/,$p'`, carries
  `silenced_legs` and `scan_entry_argv`.
  Red when: over `<p15>` the name is absent, `silenced_legs` resolves tokens itself, and the
  `cross-entry argv:` note offers no element whose declared text lacks `/`, the `{gate_file}`
  element among them.
  figure: the counts are DERIVED at observation.
- **AC11** — `ast.get_docstring` of `check_entry_producer` carries `resolve_adopter_argv` and `via`,
  and carries no `d.get("adopt", {}).get("argv") or []`. In a scratch gov shaped as spec 15's AC7
  builds it, with `demo` declaring `requires = ["other"]`, `[adopt] via = "other"` and one
  `[[files]]` rule of role `rendered`, `<g>/tools/govkit/govkit.py selfcheck` prints exactly one line
  opening `govkit: entry 'demo' declares [adopt] via` and carrying
  `carries a rendered, generated or merged rule`. With the `rendered` rule taken out, no line opens
  `govkit: entry 'demo' declares [adopt] via`.
  Red when: the same gov around the `<p15>` `govkit.py` prints no line opening
  `govkit: entry 'demo' declares [adopt] via`.
  fixture: a `rendered` rule may draw other selfcheck findings in a scratch gov. The criterion reads
  only the line it names.
- **AC13** — Build the S13 target and run `python tools/govkit/govkit.py update --target <t> --write --to <HEAD sha>`
  at `<p17>`. Of the lines opening `govkit update — default-gained ` and carrying `adopter exit`,
  exactly one names `agent-cap` or `settings-merge`, and it opens
  `govkit update — default-gained agent-cap:`. No line carries `can't open file`.
  Red when: over `<p14>`, two such lines print, and the output carries `can't open file`. Over a
  scratch copy of gov at `<p17>` whose gained loop reads `(_d_g.get("adopt") or {}).get("argv")`,
  the one such line opens `govkit update — default-gained settings-merge:`.
  fixture: derived from `tools/govkit/govkit.py:970-997` and `:11104-11126` and from specs 9 and 15,
  and not run at spec time. The pass observes all three halves first. A half that reads otherwise is
  returned to the main loop and not counted.
  cost: two gov copies and three updates, about four minutes.
- **AC16** — `python tools/govkit/govkit.py selfcheck` at `<p17>` prints one line opening
  `govkit: cross-entry argv:`. `re.search(r", (\d+) naming", line)` matches it, and its group reads
  `0`.
  Red when: a clone of gov at `<p17>` with `tools/hooks/kit.toml` checked out from `<p14>` reads `1`
  there, as spec 15's AC6 red half does.
- **AC18** — A python program loads `tools/gate-legs.json`. The `govkit selftest` leg's `guard` holds
  `{prefix}/govkit/`, `{prefix}/hooks/kit.toml` and `{prefix}/settings-merge.py`, and each of the two
  new paths is carried by at most 5 legs. The `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names a commit at which `git show <sha>:tools/gate-legs.json`
  holds both new paths. `git log -1 --format=%B <p17m>` carries `manifest-audit:`.
  Red when: over `<p15>` the guard is `{prefix}/govkit/` alone, and the manifest's `last-audit:` names
  `ebce889c7`.
- **AC19** — Spec 14's reader table, cut with
  `sed -n '/^### Every reader of the receipt during CONFIGURE/,/^### What an adopter/p'`, carries
  `render_playbook.py` and `':!*.test.sh'`. At `<p17>`,
  `git grep -l '>>> resolve_kit_dir' -- 'tools/*adopt-*.sh' 'tools/playbook/*.py' 'tools/settings-merge.py' ':!*.test.sh'`
  prints five files, and each is named in the cut.
  Red when: the cut carries no `render_playbook.py`, as over `565574ae`.
  figure: five files, PINNED at `46eb75ed` on 2026-10-14.
- **AC20** — `grep -c 'declares the same argv' <s9>` prints 0. Spec 9's §4, cut and joined, carries
  `via` and `TOOL-dRedressedBar-15`. Spec 15's §2, cut and joined, carries
  `2026-10-14-spec-TOOL-dRedressedBar-9.md`.
  Red when: the first count prints 1, as over `git show <p15>:<s9>`.
- **AC21** — `sed -n '/^## 2. Scope/,/^## 3/p' <s15>`, joined, carries `gen_map.py --write` and no
  `regen.py --write`. Every path `git diff --name-only <p15a>~1 <p15a>` prints that is not under an
  entry of spec 15's `### Files touched (estimate)` is named in spec 15's new revision line, or that
  line states that none moved.
  Red when: S8 still names `regen.py --write`, as over `ebbcbbf0`, or a moved path goes unnamed.
- **AC22** — Make a scratch copy of gov at `<p17>` with one added line,
  `raise RuntimeError("drb17 staged fault")`, directly before the `step(STEP_LEGS, ...)` call in
  `_cmd_apply`. Over a target whose state makes `git add --renormalize` move the index blob of at
  least one claimed row, the copy's apply exits non-zero. Every row of `.governance/install.json`
  carrying an `oid` then equals the blob `git -C <t> ls-files -s -- <path>` prints. The tip's
  unpatched apply over the same uncommitted target prints no line carrying `DIRTY`.
  Red when: a second copy with the same fault and with S22's write taken out leaves at least one row
  whose `oid` differs from its index blob, and the re-run prints a line carrying `DIRTY`.
  fixture: the target state is the one `tools/govkit/govkit.py:7905-7911` names: a target whose
  checkout applies a line-ending filter to an LF-pinned, claimed path. The pass derives it on a
  target of its own, with `core.autocrlf true` where that state needs it, and records the commands.
  The red half's differing row is the liveness assertion. A state in which the red half finds every
  `oid` equal cannot discriminate, and is returned to the main loop.
  cost: two gov copies and four applies, about four minutes.
- **AC23** — `grep -c 'receipt_path.write_text' tools/govkit/govkit.py` prints 0, and
  `govkit.ADOPTER_BAR_PATHS` holds `receipt_path`. A python program run from `tools/govkit` imports
  `govkit` and wraps `pathlib.Path.write_text` so a call on a file named `install.json` or
  `install.json.govkit-new` writes half of its text and raises `OSError`. Over a target holding a
  receipt from an earlier unpatched apply, it calls `govkit.main` with the arguments of
  `apply --target <t> --kits check-wiring`. The call raises or returns non-zero. `.governance/install.json`
  then parses with `json.loads` and equals its earlier bytes, and no `install.json.govkit-new` is
  left. Spec 14's "When CONFIGURE fails" table, cut and joined, carries `write_atomic`. This
  criterion reads neither `write_atomic`'s docstring nor the comment block above
  `ADOPTER_BAR_PATHS`, which S23 claims observed, and it faults `install.json` alone, so a fault on
  the `install.sums` sidecar written beside it is not seen. `TOOL-dRedressedBar-19`'s AC23 reads
  the docstring and the comment block, and its AC40 faults the sidecar (units-16-18 report ids 23
  and 40).
  Red when: the same program over the `<p15>` engine leaves an `install.json` that `json.loads`
  refuses, because unit 14's early write truncates it in place.
- **AC24** — In scratch govs shaped as spec 15's AC7 builds them, with `demo`'s `[adopt]` holding
  `via = ""`, and again with `via = ["other"]`, each `<g>/tools/govkit/govkit.py selfcheck` prints
  exactly one line opening `govkit: entry 'demo' declares [adopt] via` and carrying
  `is not a non-empty string`. Neither output carries `Traceback`. A python program importing that
  gov's `govkit` and calling `resolve_adopter_argv` for `demo` with `via = ""` raises `KeyError`.
  Red when: around the `<p15>` `govkit.py`, `via = ""` and `via = ["other"]` each print exactly one
  line opening `govkit: entry 'demo' declares [adopt] via`, and it carries `names no registry entry`
  in place of `is not a non-empty string` (`tools/govkit/govkit.py:3296-3300`). Neither output
  carries `Traceback`. The same program over that `govkit.py` raises nothing for `via = ""`:
  `resolve_adopter_argv` falls back to `demo` and returns what demo's own `[adopt]` argv resolves
  to, `[]` where it declares none (`:1511-1518`).
  cost: three scratch govs and four selfchecks, about a minute.
- **AC25** — `git diff <w17>~1 <w17> -- memory/builds/dRedressedBar/spec/` shows specs 9, 12, 13, 14
  and 15 each with one header rev change and one new revision line. Each line names
  `TOOL-dRedressedBar-17` and every report id §4's table assigns that spec. Each of the five specs
  carries a CLOSED header at `<w17>~1`. `git diff --name-only <p17>~1 <p17> -- memory/builds/dRedressedBar/spec/`
  and the same over `<p17m>` name no file but this spec. The ledger S25 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-17`.
  Red when: a spec takes no bump, two bumps, or a revision line missing one of its ids, a target was
  folded before it closed, or a build-pass commit writes another spec.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC2 · the `[dRB-12]` and `[dRB-14]` sidecar checks over a copy whose `install.sums` write iterates this run's `rows` alone, where the carried rows are missing from the sidecar · none
New arm: tools/govkit/selftest.py · covers AC3 · fixture B's identity check over a copy that appends the agent-cap row with `commit`, `sha256` and `gov_oid` already set, where the before-half reds · none
New arm: tools/govkit/selftest.py · covers AC13 · the `[dRB-9]` per-kit gaining case over a gov whose gained loop reads the declared `[adopt].argv`, where the one adopter line opens `default-gained settings-merge:` · none
New arm: tools/govkit/selftest.py · covers AC11 AC24 · the `[dRB-15]` scratch-gov cases for the first and fifth `via` rules over the `<p15>` `govkit.py`, where `via = ""` and `via = ["other"]` each print their `via` line carrying `names no registry entry` in place of `is not a non-empty string`, `resolve_adopter_argv` falls back to `demo` for `via = ""` in place of raising `KeyError`, and `via` beside a `rendered` rule prints no `via` line · none
New arm: tools/govkit/selftest.py · covers AC23 · the `[-21] AC2` routing assertion with one receipt write respelled as `receipt_path.write_text(`, where its no-direct-write check reds · none

The refusal join's floor does not move. S11 and S24 add rules to the `via` site unit 15 adds and no
`r.fail` site of their own, and S22 and S23 add no refusal branch. The main loop observes each moved
arm red, then green, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, promoted at the CONVERGED exit of the units-12-15 spec audit.
  All 21 confirmed medium and low findings, by report id, are batched into this unit by M4. Each
  claim was re-read at `46eb75ed` and at the blobs the report pins. Id 13's observation departs from
  the report's sketch, which `update`'s receipt order makes unreachable (§4).
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-19`, the batch the
  units-16-18 spec audit's minors were promoted into, for that report's ids 2, 4, 5, 16, 17, 23, 40
  and 41. No scope, design or criterion moves.
- rev-3 · 2026-10-14 · §1 · S25 · §4 · AC25 · unit 10's builder divergence, applied here
  (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`): no role can make a build-pass
  commit that also edits another spec, because scratch-guard admits a builder's spec edit only to
  its own status and date cells (`tools/hooks/scratch-guard.js:91-99`). The moved items: S25's five
  rev bumps, and the spec halves of S1 to S6, S8 to S11, S13, S15, S16 and S18 to S24, are now this
  unit's spec-writer pass `<w17>`, dispatched once units 9 to 16 are CLOSED and before the build
  pass. They are not folded now, because specs 12 to 15 are unbuilt, and several red halves here
  read their pass commits as they were built. §4 Files touched lists product files, the manifest and
  the ledger only. AC25 reads `<w17>` in place of `<p17>` and observes that neither build-pass commit
  writes another spec. Alternatives rejected gains one row. No product design or other criterion
  moves.
- rev-4 · 2026-10-14 · §1 · S24 · §5 · AC24 · §7 · the `<w17>` writer's finding
  (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-6-revision.md`): AC24's red half could not
  reproduce over the built `<p15>`. Its selfcheck already reads the `via` key's presence and checks
  that the value is a string naming a registry entry before using it
  (`tools/govkit/govkit.py:3296-3300`), so `via = ""` and `via = ["other"]` each print one `via` line
  carrying `names no registry entry`, with no traceback, where rev-3 expected no line and an
  `unhashable` traceback. S24 is restated as a reason refinement at selfcheck and a behaviour change
  at run time, where `resolve_adopter_argv` still falls back to the entry's own argv for `via = ""`
  (`:1511-1512`, read at the tip, whose `govkit.py` equals `<p15>`'s). AC24's red half, the
  `New arm:` line for AC11 and AC24, §1's row 24 and §5's security sentence now name what `<p15>`
  does. AC24's green half, and every other scope item and criterion, do not move.
- rev-5 · 2026-10-15 · §1 · S10 · S23 · §4 · §5 · AC1 · AC9 · AC10 · AC23 · §10 · a records fix for
  TOOL-dRedressedBar-19, closing the units-16-18 spec audit's report ids 2, 4, 5, 16, 17, 23, 40
  and 41 (items L1, L2, L3, L11, L12, L15, M16 and M17), written by that unit's spec-writer pass
  `<w19>`. The status stays CLOSED. Id 4: §1 and "Order, and unit 7" say this unit is ordered after
  units 9 to 16 and point at the README's derived build-order region, since unit 18 follows it at
  order 13. Id 2: S10 restates the `cross-entry argv:` note with no label narrowing its population,
  and §4's row 15 names the ownership join's OFFERED and GRADED sentences and note template, which
  spec 15 takes in the same pass. At `997fc294f` the engine's note still carries the old label
  (`tools/govkit/govkit.py:3348`); TOOL-dRedressedBar-19's AC2 observes it gone. Id 5: AC9's cut
  requires all six append sites and its awk half names the six numbers; unit 17 observed it as
  written, and TOOL-dRedressedBar-19's AC5 reads the corrected cut. Id 16: §4 Evidence, AC10 and
  §10 cite the codebase-map argv at `:104`, which the report had right, and §10 says so. Id 17:
  "Three choices" and the code-sites row 23 say "every receipt write" with no count, since S23
  enumerates seven. Id 23: AC23 states that it read neither comment S23 claims observed, and
  TOOL-dRedressedBar-19's AC23 reads both. Id 40: S23, "Three choices", §5 and AC23 state that the
  `install.sums` sidecar stayed a plain write after each receipt write, and the order and
  interrupt behaviour TOOL-dRedressedBar-19's S40 gives it, which its AC40 observes. Id 41: AC1
  selects the `[dRB-14]` and `[dRB-15]` checks by label rather than by the span between a label's
  outermost lines; unit 17 observed the span form, which held at its pass, and
  TOOL-dRedressedBar-19's AC41 observes the label form. No other criterion's assertion moves.
- rev-6 · 2026-10-15 · S23 · §3 · §10 · a records fix for TOOL-dRedressedBar-23, closing the
  round-1 closing diff review's report id 13 (item L4), written by that unit's spec-writer pass
  `<w23>`. The status stays CLOSED, and no criterion text moves. S23's routing sentence and §10's
  "grades the new member with no new code" each gain that the arm's liveness was aggregate: at
  `c84518fff` its two liveness checks are `bool(_dest21)` and `bool(_routed21)` over the union of
  the members (`tools/govkit/selftest.py:16449-16455`), so a member matching nothing, as a renamed
  `receipt_path` would, passed. Edges gain the hands-off to TOOL-dRedressedBar-23, whose AC6
  observes one liveness check per member.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "walk every descriptor argv element per entry and resolve
it in that entry's target context"` ranked name-stem SEAMs (`resolve`, `walk`, `resolve_kit_dir`,
`read_descriptors`) and not `silenced_legs`. `python tools/codebase-map/reuse_lookup.py "write a
state file through a sibling temp file so an interrupted run leaves the previous file"` ranked `run`,
`write` and `write_text` and not `write_atomic`. Both are misses, recorded as misses. The seams
extended were found by reading the report's citations. `silenced_legs`
(`tools/govkit/govkit.py:3908-3946`) is the walker S10 generalises, and `write_atomic` with its
declared population `ADOPTER_BAR_PATHS` (`:3964-3967`) is the writer and the gate S23 extends. The
selftest's `[-21] AC2` routing arm (`tools/govkit/selftest.py:15838-15917`) grades the new member
with no new code. Its liveness was aggregate over the members, so a member matching nothing passed
until `TOOL-dRedressedBar-23` graded each. `stale_target`, `build_scratch_gov_kit` and the `-13`
builders are reused for the fixtures. The manifest re-stamp follows commit `2e187ee8b`.

The gotchas checklist for `tools/govkit/govkit.py`, `tools/govkit/selftest.py` and
`tools/gate-legs.json` selected these classes, each answered here:
- `hand-named-gate-list-green-while-the-bar-reds` and `held-suite-guard-misses-a-sibling-kit`, the
  classes of ids 4 and 18, which is why AC4 derives the leg floor and S18 widens the guard.
- `retirement-inventory-misses-readers-by-value`, the class of id 1, which is why S1 restates spec
  15's inventory over unit 14's tree.
- `two-answers-to-one-question`, which is why S10 makes one walker and one source choice.
- `a-new-leg-trips-a-growing-set-of-meta-gates`, which is why §7 names the canaries and the
  manifest ratchet for a guard edit.
- `staged-break-substitutes-a-synthetic-value` and `staged-break-runs-stale-bytecode`, which is why
  AC22's fault sits at the latest point the recovery claim covers and every staged copy is a fresh
  tree.
- `line-claim-matched-over-the-whole-output`, which is why each criterion names the line it reads.

The recall probe returned `TOOL-aEvidencedLens-20`, `TOOL-dRedressedBar-10` and
`TOOL-dRedressedBar-13`, the precedent minors batches. Each observed built units' criteria in a
corrected form and corrected prose with one rev bump per spec, and this unit takes their shape. The
report and the code agree on every citation re-read, with one exception: the receipt-reader grep
prints six files, not five, until a suite is excluded. The report's
`tools/codebase-map/kit.toml:104` for the codebase-map leg's argv was right, at the base and at
`46eb75ed` alike (`TOOL-dRedressedBar-19`, units-16-18 report id 16).

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit's batch of minor
findings closed after the faulted units are built" --terms "spec-audit minors batch promoted unit
corrected observation rev bump ledger write_atomic silenced_legs via"`
