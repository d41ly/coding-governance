# TOOL-dUnstalledConvoy-4 — M2 and M3 gain the amendment vocabulary, and a mandate delegates scope inside the build's stated goal

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

## 1. Goal

M3 states that a standing mandate "does not delegate SCOPE" and that a scope fork must be parked.
Two of the five aborted runs in this tree parked on exactly that and stopped with the work complete.
This unit delegates scope inside the build's stated goal, names the three amendment acts, and pins
the one act the code already refuses so the method cannot authorise an impossible move.

## 2. Scope (IN)

- **S1** — M3's `What is delegated` paragraph is rewritten. A standing mandate delegates the owner's
  resolver authority for the named build INCLUDING scope, bounded by S2. The "park it" instruction
  for a scope fork is deleted, because it is the instruction that produced the stalls.
- **S2** — the bound is stated as one invariant: **the build README's goal statement is what a run may
  not amend.** Everything downstream of it — a spec's scope, its non-goals, the roster — is
  amendable in service of that goal. This replaces veto 2's owner turn for changes made in service of
  the stated goal, and leaves vetoes 1 and 3 in force.
- **S3** — M2's `Act` block gains a fifth act, **AMEND**, with three forms: RETIRE a unit by moving
  its spec to `WONTDO` with a successor or reason pointer in the header tail; SUPERSEDE it by
  authoring a replacement unit and retiring the original; and ADD a unit the build turns out to need.
- **S4** — M2 states the act the code REFUSES: an id, once in the build README's generated units
  region at the run's pinned BASE, may never leave it. `check_authorization` compares the BASE and
  HEAD id sets as a subset and refuses removals, and `authorization-reachable` is the one Definition
  of Done item with no override. Retiring is a status flip, never a deletion.
- **S5** — M3's `Mark it in place` rule extends to an amendment: the resolver and authority are named
  the same way, and an amendment made under a mandate is marked `RESOLVED (agent, <date>,
  delegated)`, never signed as the owner.
- **S6** — every amendment owes a run-state record. M2 points at the verb
  `TOOL-dUnstalledConvoy-5` builds rather than describing it, per M1's rule that nothing stated here
  is stated elsewhere.
- **S7** — `tools/memory-tree/BUILD-METHOD.template.md` and `memory/guides/BUILD-METHOD.md` move
  together, and the result is re-measured against M1's own budget before commit.

## 3. Non-goals (OUT)

- The verb, its record and its check. Those are units 5 and 6.
- Loosening veto 1 or veto 3. A run still may not ship an option that fails an acceptance criterion
  or a gate the spec already wrote, and still may not widen a security, data or write surface beyond
  what the unit's risk tier priced. Both remain owner turns.
- Letting a run amend the build README's goal statement. That is S2's invariant and it is what makes
  "inside the stated goal" a bound rather than a phrase.
- Any change to the status vocabulary. `WONTDO` already exists, is already terminal for
  `build-complete`, and already requires a successor id or reason pointer in the header tail.
- Any change to M12. Its closing line already defers to M3's limit on authority, and it inherits
  whatever M3 says without an edit.

## 4. Design

### The three acts, and the one refusal

| Act | Mechanism | Roster effect | Legal today |
|---|---|---|---|
| RETIRE | spec status to `WONTDO`, successor or reason in the header tail | id stays, row status changes | yes, and undocumented |
| SUPERSEDE | author the replacement, retire the original, cross-point both | id added, original stays | yes, and undocumented |
| ADD | author a new unit and its spec | id added | yes, and undocumented |
| DELETE | remove the id from the roster | id removed | **no — structurally refused** |

The first three columns were verified against source before this spec was written. `WONTDO` is one of
the two statuses `nonterminal_units` accepts as finished, so a retired unit does not block
`build-complete`. `check_authorization` admits additions and refuses removals, so ADD and SUPERSEDE
pass the authorization comparison and DELETE cannot. The method has been forbidding what the code
permits, and silent about the one act the code actually refuses.

### Why the goal statement is the invariant

Delegating scope needs a bound, or "inside the build's goal" is a phrase rather than a rule. The
build README's goal is the right one for three reasons. It is written before the run's branch exists
and is therefore part of the authorization the run cannot have authored. It is already read at the
pinned BASE by `check_authorization`, so it is already in the trusted set. And it is the one sentence
the owner actually wrote when they started the build.

A run that discovers the goal itself is wrong has found the one fork it must still park. That is a
narrow, well-defined exit rather than the broad one M3 has today, and it is the difference between a
run that stalls on a detail and a run that stops because the premise failed.

### Where the amendment record lives

An amendment leaves three traces and the method names all three: the spec's own `§9` revision line
and `§8` resolution mark, the build README's roster and generated region, and the run-state file via
unit 5's verb. The third is what makes the amendment visible to a gate. The first two are what make
it visible to a reader.

### Line budget — the live risk

`memory/guides/BUILD-METHOD.md` is 20 567 bytes and 283 lines against M1's stated 22 528 and 290, so
the headroom is **seven lines** and units 4 and 8 both write this file. S1 replaces a paragraph of
comparable length and is close to neutral. S3 and S4 are additions.

This unit's budget is **four lines net**, leaving three for unit 8. It is measured with `wc` against
M1's figures before commit, not estimated. If the pair does not fit, the disposition is a fork to the
owner, because M1's budget is a stated constraint of a governance carrier and M3's veto 2 makes
changing one an owner turn — a veto this unit deliberately does NOT relax for M1 itself, since a run
raising the budget of the file that states its own limits is the circularity the whole rule exists to
prevent.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | M2 `Act` block, M3 `What is delegated` and `Mark it in place` |
| `memory/guides/BUILD-METHOD.md` | the render of the same |
| `memory/HYGIENE.md` and its template | nothing, unless the `WONTDO` tail rule needs a pointer |

### Alternatives rejected

- **Retire-and-supersede without ADD.** The recommendation the owner declined at kickoff. Recorded as
  rejected by owner decision rather than by test.
- **A new terminal status for a retired unit.** `WONTDO` already means "abandoned or superseded" and
  already demands a successor pointer. A second token would be two answers to one question.
- **Delegating by relaxing veto 2 generally.** Rejected: veto 2 also covers a new external dependency
  and a new install location, neither of which the stalls were about, and both of which are genuinely
  the owner's. S2 relaxes it only for changes in service of the stated goal.

## 5. Production-readiness checklist

- security — veto 3 is untouched, so a run still cannot widen a security or write surface past its
  tier's price without an owner turn. That is the bound that matters here.
- perf / scale — N/A — documentation.
- a11y — N/A — documentation.
- i18n — N/A — documentation.
- error / empty / loading states — N/A — documentation.
- observability — S6's pointer to unit 5's verb is what makes an amendment observable rather than
  inferred from a diff.
- risks (concurrency, data-loss, rollback hazards) — the real risk is a run amending its way out of a
  hard problem. S2's invariant and the retained vetoes are the bound; unit 6's check is the detector.
- testing + left-shift gates — the method carriers check and the kit-version marker check both read
  this file. Adding an M-section changes neither, but the marker population is derived rather than
  enumerated and an open row records a remedy message that names too few carriers.
- migration / rollback — none. Existing specs already use `WONTDO` legally.
- user docs — the Skill's directive table row for `forks-resolved` points at M3 and needs no edit,
  because it names the rule rather than restating it.

## 6. Acceptance criteria

- **AC1** — M3 no longer contains the instruction to park a scope fork, verified by `grep` for the
  deleted sentence returning nothing in `memory/guides/BUILD-METHOD.md`.
- **AC2** — M2's `Act` block names AMEND with its three forms, and M2 states that an id may not leave
  the roster.
- **AC3** — `bash tools/memory-tree/check-method-carriers.sh` stays green, and the template and the
  render are byte-identical modulo the install prefix.
- **AC4** — `wc -c` and `wc -l` on `memory/guides/BUILD-METHOD.md` are within M1's stated budget after
  the edit, and the figures appear in the commit message.
- **AC5** — `python tools/memory-tree/corpus_ids.py --report` shows the read path below
  `READ_PATH_CEILING`, since this file is one of its six members.
- **AC6** — A reader can answer, from M2 and M3 alone, which of the four acts in §4's table the code
  refuses and why, observed in `memory/guides/BUILD-METHOD.md`.

## 7. Gates

`method carriers` · `kit version markers` · `memory-tree hygiene` · the full bar at the push
boundary.

## 8. Open questions

- **F1 — does the AMEND act belong in M2 or in M3?** M2 owns classification and action; M3 owns
  authority. S3 puts the acts in M2 and the authority in M3, which matches how the two sections
  already divide. The alternative folds both into M3 and costs fewer lines, which matters given the
  seven-line headroom. **Recommendation: as specified**, and fall back to the M3-only placement only
  if the measurement in §4 shows the split does not fit. Either way this is a placement fork, not a
  content fork, and it does not change what the method permits.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an unattended run changes its own build scope and retires
a planned unit"` returns the `build-method` and `build-readme-surface` dossiers plus the
`unattended` affordance seam, and no function seam above the fan-in threshold. There is no code seam
to extend here: the acts this unit documents are already permitted by `nonterminal_units` and
`check_authorization`, both read at source, and the unit adds no machinery.

`python tools/memory-recall/query.py "may an unattended run rescope its build, supersede or retire a
spec when building uncovers new detail" --terms "spec supersede retire rescope amend build-method
fork rule pass loop regrounding unattended directive scope change"` returns the method-ownership
record, the standing-mandate authorization record and the two aborted runs whose reasons this spec
quotes. The prior art says the method belongs to the memory-tree kit and is pointed at by the
unattended kit, which is why S7 moves the template and the render together.

Recall terms used: spec supersede retire rescope amend build-method fork rule pass loop regrounding
unattended directive scope change.
