# TOOL-cBriefedPilot-1 — the paired flag accumulator, and an `--override` that can be used twice

**Status:** CLOSED · rev-3 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling · ratified 2026-08-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |

<!-- /gen:spec-records -->

## 1. Goal

Make `--override <item> --reason <text>` repeatable, so a `--close` blocked on two Definition-of-Done
items can be unblocked in one invocation. Today the dispatch stores a scalar at
`tools/unattended/unattended.sh:1005`, a second occurrence overwrites the first, and `verb_close`
blocks on the second unmet item at `:950` before it ever reaches the `park` at `:952` — a dead end
with nobody present to read it. This build adds two DoD items and eleven waivable directives on top
of that parser, so it is the first thing that has to move.

## 2. Scope (IN)

- **S1** — the dispatch accumulates `--override` into two parallel arrays, `OV_ITEMS` and
  `OV_REASONS`, one element per occurrence, replacing the scalar `OV`.
- **S2** — `--reason` closes the pair the preceding flag opened. With no pair open it keeps its
  present scalar meaning, which is what `--abort <slug> --reason <text>` uses. A flag still pending
  when argv ends is flushed with an EMPTY reason, so it meets the refusal that already exists for it
  instead of vanishing.
- **S3** — `verb_close` validates, skips and parks EVERY accumulated item. The undeclared-item
  refusal, the missing-reason refusal and the `authorization-reachable` refusal each run per item,
  and one `park` entry and one echo are written per item.
- **S4** — the three refusal messages are byte-unchanged, so their arms stay valid, no ordinal moves
  and `ARMS_FLOORS` does not move. This unit adds no `fail` branch.
- **S5** — three arms in `tools/unattended/unattended.test.sh`: two pairs both skip and both park;
  `--override authorization-reachable` refuses when it is SECOND in the list; an `--override` with
  no following `--reason` refuses.

## 3. Non-goals (OUT)

- **`--waive`.** Unit 3 adds one line to the same `case` arm and a second pair of arrays,
  `WAIVE_ITEMS` and `WAIVE_REASONS`. This unit builds the arm and its first consumer.
- **Refusing a reason that spells the declared bypass flag.** That is unit 3's, in
  `verb_preflight`'s precondition block, and it is a rule about the RECORD rather than about the
  parser.
- **Telling the agent that the pair repeats.** `tools/unattended/SKILL.template.md:92` spells one
  pair and says nothing about repeating it. That file is written by units 9 through 11, and the
  sentence is unit 9's S6; two units editing one template is the write-set collision M6 names.
- **Deduplicating a repeated item.** `--override a --reason x --override a --reason y` parks two
  entries for one item. Loud, harmless and not worth a branch.

## 4. Design

### Data model

Two parallel arrays, index-joined, appended in the dispatch and read by `verb_close` as globals —
an array cannot be passed as an argument, so `verb_close` loses its second and third parameters.
`tools/run-gates.sh:118-128` already carries exactly this shape (`names=(); guards=(); argvs=()`
then `for ((i=0; i<total; i++))`), for the same reason: a list of records whose fields are free
text.

Empty-array expansion is the one trap. `${#OV_ITEMS[@]}` is safe under `set -u` everywhere; a bare
`"${OV_ITEMS[@]}"` on an empty array is not, across the bash versions an adopter may run. The C-style
index loop never expands the array at all, which is why `run-gates.sh` uses it.

### Why arrays and not the delimited string the design pass sketched

The design pass proposed `item<TAB>reason` lines accumulated newline-delimited. A reason is free
text, and any single-character record separator is a separator the reason can contain: a reason
spelling a newline followed by `records-current`, a tab and a word accumulates a SECOND override the
owner never named, on an item that IS declared, so no refusal fires. An array has no delimiter to
attack, and nothing has to split, so it is also the shorter diff.

The newline is still a hazard for the RECORD — `park()` at `:995` interpolates the reason verbatim
and the parked region has a line grammar — but that hazard predates this unit and is §8's fork.

### The refusal loop

`verb_close`'s `if [ -n "$ov" ]` block becomes a loop over the indices, and the skip at `:940`
becomes a membership test over the space-joined item list. That is safe because a declared DoD item
cannot contain a space: the existing `case " $(dod) " in *" $ov:"*` test already depends on it.

The `authorization-reachable` refusal therefore fires wherever the item appears in the list, which is
what S5's second arm pins. The three messages keep their exact text; check-arms takes the longest
literal run between interpolations as the signature, so renaming the bound variable from `ov` to
`item` in the trailing value changes nothing it reads.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the dispatch at `:1000-1006`, `verb_close` at `:915-961`) ·
`tools/unattended/unattended.test.sh` (three arms).

### Alternatives rejected

- **`--override a,b --reason x`.** One reason for two items is one reason too few; the wrap-up reads
  parked entries individually and each has to carry its own.
- **Accepting `--reason` before its flag.** The scalar parser accepted either order and mispaired
  silently. Order now matters, and the mispairing surfaces as the missing-reason refusal. Every
  invocation in the self-test and in the Skill already writes the documented order.

## 5. Production-readiness checklist

- security — an owner-supplied reason reaches `park()` verbatim. The array carries no delimiter for
  it to attack; the residual record-side newline hole is §8's fork and is not created here.
- perf / scale — N/A.
- a11y · i18n — N/A.
- error / empty / loading states — an unpaired `--override` refuses through the branch that exists
  for it today.
- observability — one parked entry and one echo per overridden item, where there was one of each.
- risks — `verb_close` reads globals instead of parameters. The driver already reads `TB`, `ASHA`
  and `M` that way, so this is the existing convention rather than a new one.
- testing + left-shift gates — S5's three arms, plus the pre-existing single-override arms as the
  no-regression control.
- migration / rollback — a single `--override` invocation behaves exactly as today.
- user docs — the Skill's Close section, in units 9 through 11. Named in §3, not built here.

## 6. Acceptance criteria

- **AC1** — When `--close` is invoked with two `--override <item> --reason <text>` pairs, both items
  are skipped, the run closes, and the parked region carries one entry per item with its own reason
  intact.
- **AC2** — When `--override authorization-reachable --reason <text>` is the SECOND pair, the
  non-overridable refusal fires and the close blocks.
- **AC3** — When an `--override` is passed with no following `--reason`, the existing missing-reason
  refusal fires.
- **AC4** — The pre-existing single-override arms are green unchanged, including the end-to-end path
  that closes on `gates-green` and writes its reason into the run-state file.
- **AC5** — `python tools/memory-tree/check-arms.py` is green with `ARMS_FLOORS` unedited, which is
  the observation that no message was reworded and no branch was added.

## 7. Gates

`unattended driver selftest` (`tools/unattended/unattended.test.sh`) · `harness arms`
(`tools/memory-tree/check-arms.py`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`) · the full bar at the push boundary.

## 8. Open questions

none — the fork below is RESOLVED (agent, 2026-08-15, delegated): option (b), the newline
  refusal stays in unit 3's precondition block and covers `--waive` alone.

  **This overrides the fork's own recommendation, on M3 veto 1.** Option (a) — one shared refusal at
  the dispatch `--reason` arm — is the better principle and the spec argues it well: `park()` is the
  shared writer, and this driver's own `refuse_if_terminal` comment records what a rule spelled at one
  call site costs. But a shared refusal is a NEW `fail` branch in THIS unit, and this unit's S4 states
  that it adds none while AC5 observes `check-arms.py` green with `ARMS_FLOORS` UNEDITED. M3 rule 1
  discards an option that fails an acceptance criterion already written in the spec, so (a) is
  discarded and (b) survives. Taking (a) would have meant rewriting S4, AC5 and unit 3's S2 to rescue
  an option the veto ladder had already removed.

  **The residual is real and is not closed by this resolution:** the newline hole stays open for the
  `override` and `abort` park kinds, which is pre-existing and which this unit did not create. It is
  filed rather than absorbed, because absorbing it is exactly the scope creep the veto prevented.

**Where does the newline refusal on a `--reason` live?** `park()` writes a reason verbatim into a
region with a line grammar, so a reason containing a newline can write a second parked line — after
unit 3 that includes a well-formed `waiver · item <handle> · reason <text>` line that leg check 17
would then grade. The hole is open today for the `override` and `abort` kinds and is not created by
this unit; the arrays close it for the parser only.

Options: one refusal at the shared `--reason` arm in the dispatch, covering `--override`, `--waive`
and `--abort` in one branch; or unit 3's precondition-block refusal, which covers `--waive` alone
and leaves the other two kinds as they are. Recommendation: the shared one, because `park()` is the
shared writer and a rule spelled at one call site is a rule that will be missing from the next —
this driver's own `refuse_if_terminal` comment at `:563` says so about the identical mistake. It
would move a clause out of unit 3's fifth refusal rather than add a branch anywhere. Resolver: owner.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the nine-agent design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds C1 and D2. §4 replaces that pass's
  tab-separated, newline-delimited accumulator with parallel arrays, on the injection the delimiter
  permits.
- rev-2 · 2026-08-14 · §3's deferral repointed. It named "units 9 through 11" without naming one, and
  none of the three had claimed the sentence; it is unit 9's S6, added there on the same cross-read.

- rev-3 · 2026-08-15 · §8 resolved under the standing mandate. Option (a) was discarded on M3
  veto 1 — it would have added a `fail` branch this unit's own S4 and AC5 forbid. Scope, acceptance
  and `ARMS_FLOORS` are unchanged; the residual newline hole for the other two park kinds is filed.

## 10. Reuse audit

- **`tools/run-gates.sh:118-128`** — the seam this unit copies: parallel arrays filled in a parse
  loop and read back through a C-style index loop, including the empty-array discipline. It exists
  because the same problem was already solved once here.
- **`verb_close`'s three refusal branches in `tools/unattended/unattended.sh`** — extended in place.
  Their messages are the contract with `check-arms.py`, so they are moved and not rewritten.
- **`park()` in the same file** — already takes a kind and an item; it is called once per overridden
  item instead of once, with no change to the helper.
- **The `case " $(dod) " in *" $ov:"*` membership idiom** — reused verbatim for the per-item skip
  test.

`python tools/codebase-map/reuse_lookup.py "repeatable flag accumulator argv pairs override reason"`
returned no candidate above a bash file, and printed its own reason: the map has no symbol extractor
for the bash layer, so a seam there is invisible to it and must be found by hand. The four above were
found by hand and the query is recorded so the next author does not re-run it expecting more.

Recall terms used: unattended override reason accumulator dispatch argv pair close DoD park parked
region refusal arms floor.
