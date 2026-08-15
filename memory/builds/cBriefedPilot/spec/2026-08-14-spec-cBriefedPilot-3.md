# TOOL-cBriefedPilot-3 — the owner's named, reasoned waiver, accepted at preflight and nowhere else

**Status:** OPEN · rev-6 · 2026-08-14 · node c · Tier-2 · base 37c05e1b · streams tooling

## 1. Goal

Give the owner a way to relax one of the eleven default directives for a single run, as a named
handle carrying a required reason, recorded where the wrap-up already reads. The waiver must be
impossible to take after the run goes unattended, because the turn that grants it is the last owner
turn there is.

## 2. Scope (IN)

- **S1** — `--waive <handle> --reason <text>`, repeatable, accepted by `--preflight` and by no other
  verb. It consumes the paired accumulator unit 1 builds; it does not build a second one.
- **S2** — five refusals, taking check numbers **37 through 41**. Number 34 is unit 4's and is the
  driver's only gap today, so this unit's numbers start above the highest spelled one; unit 6 derives
  its own from the same rule rather than restating a literal.

  Refusal 1 does NOT live in the precondition block, and that is the correction this spec needed:
  `verb_preflight` never runs when the verb is something else, so a guard placed there can never fire.
  It is a guard in the argv DISPATCH, evaluated inside the `--plan` and `--phase` arms as well as
  after the parse loop — both of those exit inside the loop, so a post-loop guard alone misses them.

  1. **(dispatch)** the verb is not `--preflight`;

  Refusals 2 through 5 validate in the precondition block ABOVE the write barrier, so a refused
  invocation leaves the run-state file byte-identical:

  2. a run-state file already exists AND the requested set differs from the recorded one. The
     comparison runs only when the invocation carries at least one `--waive` pair: an invocation
     naming no handle leaves the recorded set untouched and is NOT a refusal, which is what makes the
     `--preflight` that unit 5's §4 requires before every `--close` legal over a waived run;
  3. the handle is not in the effective directive set;
  4. no `--reason` follows the handle;
  5. the reason spells the project's declared bypass flag, or contains a newline.
- **S3** — each confirmed pair is written by the existing `park()` with a new `waiver` kind, in the
  fixed grammar `waiver · item <handle> · reason <text>`, free text last.
- **S4** — the `park()` calls are placed AFTER the `set_fact` block and BEFORE `stage_or_fail`, so the
  staged blob carries the waivers and the gate leg — whose whole per-run population is the index —
  can see them.
- **S5** — a byte-identical re-preflight after a compaction leaves the parked region diff-equal
  rather than appending a second copy of every waiver.
- **S6** — arms for all five refusals plus the idempotent-re-preflight case, in
  `unattended.test.sh`, each observed RED before the branch it arms is written.
- **S7** — `ARMS_FLOORS` for `tools/unattended/unattended.sh` is raised by the number of branches
  this unit adds, in the same commit as the branches.

## 3. Non-goals (OUT)

- **The flag accumulator itself.** Unit 1 builds it, for `--override`, and this unit reuses it. Two
  accumulators would be the same mechanism twice.
- **Any tamper evidence over a waiver line.** The owner resolved P1 on 2026-08-14 to BUY the git
  join — the worktree's waiver lines must be present in the first committed blob of the run-state
  file — but it is leg-side and lands in unit 13, not here. This unit's job ends at writing a
  well-formed line; grading it is a separate mechanism.
- **Refusing any particular handle.** The owner asked that every directive be overridable, and
  resolved P4 on 2026-08-14 without adding a refusal here. `reuse-first`'s waiver is SILENT rather
  than dangerous — it leaves the bar green over a skipped reuse audit — and it is made visible in
  unit 9's table, not blocked in this unit's branch set.
- **An eighth authored fact.** Protocol §2 pins the authored region at seven. This unit adds a fourth
  KIND to the parked region and no field.
- **Waiving a Definition-of-Done item.** A waiver relaxes a directive. `--override` remains the only
  route to a DoD item, and `authorization-reachable` stays unreachable by either.

## 4. Design

### Data model

A waiver is a pair, not a flag. The handle names the directive; the reason is free text and may
contain spaces — which is why unit 1's accumulator stores each pair in parallel arrays,
`WAIVE_ITEMS` and `WAIVE_REASONS`, with no record separator for a reason to contain. The
tab-separated, newline-delimited string the design pass sketched was rejected there on a measured
injection: a reason spelling a newline, a declared item, a tab and a word accumulates a second entry
the owner never named, and the `--waive` reason is the one free-text field an owner supplies.

The recorded form reuses `park()` because the parked region is already the place the wrap-up reads,
already survives compaction, already carries a kind discriminator, and is already exempt from the
prose rules that would otherwise reject a reason sentence. Protocol §2's fact 3 becomes four kinds:
a parked decision, an abort reason, a recorded DoD override, an owner directive waiver.

### The ordering guarantee

One branch carries it. `--waive` is accepted by `--preflight` alone, and only while no run-state file
exists or the requested set matches the recorded one. That single refusal produces three properties
at once: no other verb can take a late answer; a re-preflight after compaction cannot change a
recorded set; and the owner turn is provably before the run goes unattended, which is what keeps this
unit from contradicting M10's "never ask".

The alternative — a `--waive` verb of its own, or acceptance at `--phase` — was rejected for exactly
that reason. Any verb reachable mid-run is a place the run could answer its own question.

### Why validation sits above the write barrier

`verb_preflight` writes nothing until every precondition has passed, and its own comment says why: a
verb that writes and then discovers a refusal has already changed the state the refusal was about.
The four remaining refusals join that block. Refusal 1 cannot: it fires on a verb that never enters
this function, so it is a dispatch guard and §10 names the dispatch as a fifth seam.

The `park()` calls cannot join it, because they write. They sit after the `set_fact` block and before
`stage_or_fail`. Placing them earlier is a measured hazard rather than a stylistic one: `park()`
appends with `>>`, which CREATES the file, so calling it before the scaffold guard makes the later
splice fail with a message naming the wrong cause.

### Why a reason spelling the bypass flag is refused

`park()` writes the reason verbatim, and the leg's bypass check greps the run-state file whole. A
truthful reason that happened to name the flag would red the bar permanently, on a record no verb
rewrites. The refusal is a mirror of the one `verb_abort` already carries for the same reason.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | `--waive` parsing through unit 1's accumulator; five refusals; the `park()` loop |
| `tools/unattended/unattended.test.sh` | six arms |
| `.memory-tree.conf` | `ARMS_FLOORS` raised for the driver |

### Alternatives rejected

- **A `waivers:` run fact.** Breaks protocol §2's seven-fact contract for no gain: the parked region
  already carries kinds, and M9's wrap-up row already reads it.
- **Free-text waivers with no registry.** Makes leg check 17 ungradeable and lets a typo waive
  nothing silently.
- **Accepting waivers at `--resume`.** The compaction case is real, but a verb that can change the
  directive set mid-run is a verb the run can use on itself.

## 5. Production-readiness checklist

- security — the reason is written verbatim into a tracked file; the newline and bypass-flag
  refusals are the injection controls, and both are armed.
- perf / scale — N/A, five string comparisons at preflight.
- a11y — N/A, no user surface.
- i18n — N/A.
- error / empty / loading states — every refusal names itself and leaves the file byte-identical;
  arms assert the byte-identity, not just the exit code.
- observability — each waiver is a parked line, surfaced by `--status`, `--resume` and M9's wrap-up.
- risks — a waiver line appended by something other than the driver is accepted by shape alone. The
  owner bought the git join for it (P1); it grades leg-side in unit 13, so within THIS unit the
  exposure stands and is stated rather than implied away.
- testing + left-shift gates — six arms here, leg check 17 in unit 13.
- migration / rollback — additive; a run that passes no `--waive` behaves exactly as today.
- user docs — the Skill's table is unit 9; the protocol's §10 is unit 18.

## 6. Acceptance criteria

- **AC1** — When `--preflight` is invoked with two waive pairs, the staged run-state blob carries
  exactly two `waiver · item` lines, one per pair, with the reasons intact.
- **AC2** — When any of the five refusal conditions holds, the driver refuses and the run-state file
  is byte-identical to its pre-invocation state.
- **AC3** — When a reason containing a newline is supplied, the refusal fires and no second waiver
  line appears in the file.
- **AC4** — When `--waive` is passed to a verb other than `--preflight`, that verb refuses.
- **AC5** — When a byte-identical preflight is re-run over a live record, the parked region is
  diff-equal; when a DIFFERING set is re-run, the driver refuses and changes nothing.
- **AC6** — Each of the five refusals is observed RED with its arm in place and its branch removed.
- **AC7** — `python tools/memory-tree/check-arms.py` is green with the branch armed and the floor
  raised, and RED when the branch is present and its arm is removed — twice over: once naming
  the unarmed branch, once at the armed count against the raised floor. *An UNRAISED floor does
  NOT red on an added branch: `ARMS_FLOORS` is a one-sided minimum, so a higher count passes.
  Measured on unit 4, where the same wording was an acceptance criterion no run could fail.*

## 7. Gates

`unattended driver selftest` (`tools/unattended/unattended.test.sh`) · `harness arms`
(`tools/memory-tree/check-arms.py`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`) · the full bar at the push boundary.

## 8. Open questions

**RESOLVED (owner, 2026-08-14): no sixth refusal here; the visibility lands in unit 9's table.** The
reasoning is below and is kept because it is what changed the answer.

**P4 — how is `reuse-first`'s waiver made visible?** The design pass held that waiving it reds the
full bar, which would have argued for a sixth refusal here. That is false, measured against source:
hygiene check 12 leaves the body-assertion block at `if (hdr ~ /Tier-1/) next`, so §10 is unchecked
on a Tier-1 spec entirely; on a Tier-2 spec the body test is `/[^ \t]/`, which an `N/A` line
satisfies, and three Tier-2 specs in this corpus already ship one in a green tree. The waiver is
therefore SILENT, not loud — the worse case, because nothing reports it.

This unit adds no refusal for it. Options are to accept the silence, or to require that a waived
run's §10 name the waiver, which is unit 9's table and not this unit's branch set.
Recommendation: no sixth refusal here regardless of which the owner picks — a driver refusal
contradicts "each of them should be overridable" and its only motivation was the loud-failure story.
Resolver: owner.

**Does the idempotent re-preflight compare the SET or the ordered list? — RESOLVED at authoring: the
sorted SET.** A re-preflight naming the same two handles in the other order is the same waiver, and
comparing the ordered list would wedge a resumable run on an argument-order difference that means
nothing. This is a design decision by the spec's author rather than a fork the owner declined; it is
recorded because §4's idempotence rule depends on it.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the nine-agent design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds findings C1, C2, C8, C9, D1, D2,
  D12, FG-3 and FG-14 from that pass.
- rev-2 · 2026-08-14 · §8's P4 fork rewritten. The design pass's claim that waiving `reuse-first`
  reds the full bar was checked against source and is FALSE — check 12 exits the body block for a
  Tier-1 spec, and an `N/A` body passes the Tier-2 test, as three specs in this corpus already
  demonstrate. The sixth refusal that claim would have justified is ruled out here rather than left
  as an open option.
- rev-3 · 2026-08-14 · the owner resolved P1 and P4. §3 records that the waiver git join is BOUGHT
  and lands in unit 13 rather than being an open question; §8's P4 is marked RESOLVED with no sixth
  refusal; the idempotence comparison is fixed as the sorted SET.
- rev-4 · 2026-08-14 · two cross-read corrections. §4's data model described the accumulator as
  newline-delimited and tab-separated, which is the representation unit 1 §4 REJECTED and replaced
  with parallel arrays on the injection the delimiter permits — so this spec described the storage of
  a mechanism its own S1 says it consumes rather than builds. And §10 named the LEG's `core_of()` as
  the seam supplying refusal 3's membership test; `verb_preflight` cannot call it, and the seam is
  unit 2's `directives()` accessor in the driver.

- rev-5 · 2026-08-15 · §8's audit fold. Refusal 1 moved OUT of the precondition block — `verb_preflight` never runs
  for another verb, so a guard there can never fire; it is a dispatch guard, and §4 and §10 follow.
  S2 allocates checks 37-41, and refusal 2 now states that an invocation naming no handle is not a
  refusal, which is what makes unit 5's mandatory pre-close `--preflight` legal over a waived run.
- rev-6 · 2026-08-15 · the acceptance criterion asserting that an UNRAISED `ARMS_FLOORS`
  reds is corrected against measurement. It cannot: the floor is a one-sided minimum and a
  higher branch count passes. Found on unit 4 and swept across the set; three specs carried it.

## 10. Reuse audit

Four existing seams, all extended rather than duplicated.

- **`park()` in `tools/unattended/unattended.sh`** — the writer. It already takes a kind
  discriminator, already appends to the region the wrap-up reads, and is already used by `--abort`
  and by `--close`'s override path. A waiver is a fourth kind, not a fifth mechanism.
- **The paired flag accumulator, unit 1** — built for `--override`'s repeat bug and consumed here.
  Building a second parser for `--waive` was the pre-review design and was cut.
- **`verb_preflight`'s precondition block** — the existing write barrier. The five refusals join it
  rather than introducing a second ordering rule.
- **`directives()` in `tools/unattended/unattended.sh`, unit 2** — the membership test refusal 3
  reads. It composes `DIRECTIVES_CORE` plus `DIRECTIVES_EXTRA` in the same shape as the driver's own
  `phases()` and `dod()`, and it is the third instance of that shape. The LEG's `core_of()` reads the
  same constant from the other side, in unit 12; `verb_preflight` cannot call it, so naming it here
  would have pointed the builder at the wrong file.

- **The argv dispatch loop in `tools/unattended/unattended.sh`** — the fifth seam, and the home of
  refusal 1. It already exits inside the loop for `--plan` and `--phase`, which is why the guard is
  evaluated in those arms and not only after the loop.

Recall terms used, recorded because M7 re-runs the query: unattended run directive waiver preflight
override park run-state parked region reason record phase witness DoD close.

No seam exists for the owner-facing half — an interactive confirmation before a run goes unattended
is new, and it lives in the Skill (unit 10), not in the driver.
