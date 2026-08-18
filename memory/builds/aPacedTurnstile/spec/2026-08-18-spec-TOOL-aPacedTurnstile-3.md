# TOOL-aPacedTurnstile-3 — ordered chunks, and a verdict the operator sees before the run ends

**Status:** OPEN · rev-5 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Group the legs into ordered, extensible CHUNKS so the bar emits a reviewable verdict per chunk
instead of one verdict after 873 s, with memory and docs hygiene first. This is also the fix for the
measured head-of-line defect, whose root cause is not the reporter but the ANTI-CORRELATION between
longest-first dispatch and manifest-order reporting.

## 2. Scope (IN)

- **S1** — `tools/gate-legs.json` gains one optional per-leg key naming its chunk. Chunk ORDER is
  order of first appearance; no second declaration file and no order field. A leg with no key falls
  into a default chunk.
- **S2** — EVERY leg in `tools/gate-legs.json` AS IT STANDS AT THE REORDER COMMIT gets an explicit
  chunk, and the rows are REORDERED so each chunk's rows are contiguous. Not "all 70": the manifest
  carries 70 at this spec's base and the reorder lands LAST in the build, by which point
  `TOOL-aPacedTurnstile-1` has added its adopter e2e and its wiring check and
  `TOOL-aPacedTurnstile-4` has added the turnstile suite — 73 rows. All three are added by units
  sequenced BEFORE this commit, so no later pass picks them up, and a builder assigning from a
  frozen table leaves exactly the three legs AC6's unconditional arm reds on (round 2's R17). The
  three take `e2e`, `wiring` and `selftests` respectively. The default assignment is the table below,
  whose per-chunk counts are the base-time measurement and are stated as such.
- **S3** — the runner parses the key as an added field on the existing record-separated wire
  protocol, builds an ordered chunk list and a per-chunk index list, and REPORTS chunk by chunk: the
  legs of a chunk in manifest order, then one chunk verdict line. The resolved dispatch order is
  written into the run record's header, which `TOOL-aPacedTurnstile-5` owns and this unit's ordering
  criteria read; that key is declared THERE, so the record's key set stays single-sourced.
- **S4** — dispatch becomes CHUNK-MAJOR, with an escape hatch for long poles so a single very slow
  leg still starts at time zero. Without a timing cache every duration is zero, the pole set is
  empty, and the order is pure chunk-major.
- **S5** — a chunk whose verdict is RED halts the run at the chunk BOUNDARY, never mid-chunk, unless
  the run is authoritative. Remaining chunks each print one not-reported line, still-live workers and
  THEIR DESCENDANTS are killed, and the exit is 1. Killing the shell's job is not enough: a leg runs
  through a command substitution and spawns its own children, so the halt records each leg's real pid
  and signals the process group rather than the job. Otherwise a halted run leaves scratch repos and
  live git processes behind, and the beacon release `TOOL-aPacedTurnstile-4` depends on never runs.
- **S6** — a chunk in which every leg was skipped reports as skipped, never as green, and never
  halts the run.
- **S7** — the durable summary and failure records gain a chunk roll-up including per-chunk wall
  time, which is banned from stdout but not from these files, and on a halt the list of chunks not
  reported.
- **S8** — canary arms for chunk contiguity, the report grammar, the halt and its suppression, the
  all-skipped chunk, and chunk-major dispatch. Existing arms keep their current assertions.
- **S9** — `memory/guides/SESSION-KICKOFF.md`'s gate-command block gains the chunk contract and the
  halt note. This unit owns that file for this build.

## 3. Non-goals (OUT)

- Printing a duration on stdout. The existing width-1 against width-4 equivalence arm compares
  output line for line, so any elapsed time on the stream breaks it. Per-chunk wall time goes to the
  durable records instead.
- Any new line beginning with the existing leg-verdict or summary prefixes. The chunk verb is a new
  prefix precisely so existing prefix-counting arms keep their meaning.
- Changing what any leg asserts, or any guard.
- The `AGENTS.md` timing figure. `TOOL-aPacedTurnstile-2` owns that line; this unit adds only the
  chunk contract sentence.
- Making any leg faster.

## 4. Design

### The root cause, and why report-side chunking alone would make it worse

The runner sorts dispatch longest-first from the timing cache and the reader walks the manifest.
Those two orders are near-INVERSES: the cheapest leg is dispatched last, and the reporter blocks on
whichever manifest position it occupies. That is the whole measured defect — the 0.7 s
`build README slot contract` sorts about 69th of 70 and therefore starts at roughly the total
divided by the width, around 500 s.

So a chunk whose members are cheap would still report late. Pure report-side chunking moves the
first verdict from about 240 s to about 500 s — it makes it WORSE. The fix must re-couple the two
orders, which is why dispatch becomes chunk-major and the reporter is then walking approximately the
dispatch order.

Two properties fall out. At width 1 the pole threshold is the whole total, which no leg in a
multi-leg manifest satisfies, so the pole set self-empties and the serial bar becomes genuinely
streaming — first line after the first leg rather than after all of them. And the race the runner
already documents, where the timing cache decouples dispatch from manifest order, gets RARER rather
than commoner. The arm guarding that race stays regardless.

### Data model

One optional slug per leg. Order is first appearance. Chunks are required to be CONTIGUOUS in gov's
own manifest, asserted by a canary arm, because contiguity is what makes "report order equals
manifest order" a theorem rather than a second rule. The RUNNER is nevertheless tolerant of
non-contiguity, grouping by first appearance and reporting each chunk's members in manifest order —
needed because the deployer appends emitted rows kit by kit, so an adopter's manifest can interleave
chunks. For a contiguous manifest the two behaviours coincide.

The manifest's known key set after this build is `name`, `argv`, `guard`, `chunk`, `impure`, pinned
in one place by `TOOL-aPacedTurnstile-1` and edited by whichever of this unit and
`TOOL-aPacedTurnstile-5` lands second.

The wire protocol between the runner's inline parser and its bash reader gains one field on the
existing record separator, which is non-whitespace precisely so an empty field survives the read.
The resolved width is passed to the parser so the pole threshold can be derived there.

A long pole is a leg whose cached duration is at least the total cached duration divided by the
width. Measured on node `a`: the total is 4018 s at width 8, so the threshold is 502 s and the pole
set is TWO legs — `unattended driver selftest` at 659.9 s and `unattended gate selftest` at 634.6 s.
Both start at time zero; the other six workers run chunk-major. The first draft said one leg, which
undercounted the set by half and would have let the first-batch arm pass while describing the wrong
set. Durations come from the ledger `TOOL-aPacedTurnstile-5` renames, whose
second field stays the duration for exactly this reason.

### Inventory — the default chunk assignment

Six chunks, every index claimed exactly once. The counts below are MEASURED at this spec's base,
where the manifest holds 70 legs; at the reorder commit it holds 73, and S2 names which chunk each
of the three build-added legs takes. The table is the assignment, not a census — a frozen census is
the rot class the charter already records from govkit, where a spec twice stated a figure the tree
then moved underneath.

| chunk | legs | what it grades | measured max |
|---|---:|---|---:|
| `records` | 7 | the memory tree and the build-README surface — the verdict a records-only commit waits for | 57.8 s |
| `product` | 7 | the shipped playbook, template and prefix surface | 41.5 s |
| `wiring` | 9 | is this clone wired, and does the shipped source parse | 2.6 s |
| `declarations` | 7 | registries, coverage and record-versus-reality over the live tree | 20.9 s |
| `selftests` | 35 | every red/green harness over a gate | 634.6 s |
| `e2e` | 5 | the adopters and drivers that build scratch repos | 659.9 s |

The long tail sits in `e2e` BY DESIGN, because head-of-line blocking is bounded by the slowest leg
IN A CHUNK. Predicted first verdict at width 8 on a full run: about 58 s, where `records` closes on
`memory hygiene`, against about 240 s today. On the pure-records run measured at 62 s, `selftests`
and `e2e` report as skipped wholesale, which is the readable shape the operator wants.

### Concurrency

One sentence carries it: **chunks bound REPORTING and HALTING, never DISPATCH.** Within a chunk,
legs run at full pool width. Across chunks, a later chunk's legs run concurrently with an earlier
chunk's, so the pool never idles at a boundary and the blocking reader is unchanged. Only the
reader's walk order changes, from the raw index range to a flattened chunk-then-manifest list. For a
contiguous manifest those are the same list, so the reader's diff is the indirection plus a boundary
hook.

### Halting, and the interaction with the push boundary

A red chunk stops the run at the boundary, after the red chunk is fully reported, so a red chunk
always shows every one of its legs. An all-skipped chunk never halts, because it graded nothing.

The suppression condition needs care, and this is the one place this unit and
`TOOL-aPacedTurnstile-7` genuinely collide. Today's natural spelling — halt unless the full-run flag
is set — reuses an existing asymmetry and is correct while the push boundary always sets that flag.
After `TOOL-aPacedTurnstile-7` the authoritative landing run is frequently SCOPED, so that spelling
would make the landing bar fail-fast and stop reporting later chunks, which is precisely the
behaviour a landing must not have.

Resolution: the halt is suppressed by the full-run flag OR by an explicit no-halt flag, and
`TOOL-aPacedTurnstile-7` sets the latter at the push boundary unconditionally, independently of its
own scoped-or-full decision. A landing therefore always gets a complete verdict list, and the
frequent interactive runs still get fail-fast.

For: `records` closes at about 58 s, so a red there saves roughly 800 s of waiting. Because the
per-leg logs are already durable, the halt costs no information. Against: a scoped run that halts
hides later reds and the operator re-runs. That is the accepted trade, and it is the same trade the
guard pass already makes.

Kill mechanics matter on this platform: live workers are killed and reaped BEFORE the scratch
cleanup runs, because a recursive delete over a directory with open handles fails partially on
Windows. A killed leg's own scratch repo is its own to lose.

`NOT REPORTED` is deliberate rather than `not run`: with no barrier, a later chunk's leg may already
have completed when the halt fires, and its log is already on disk.

### Rollout

Two commits, deliberately. The runner change lands first against the existing manifest order, where
every leg falls into the default chunk and behaviour is unchanged. The manifest reorder lands LAST
in the whole build, because it rewrites every row of a file four other units add rows to and the
row-keyed merge driver does not cover JSON.

**The arms split across those two commits and round 2's R14 is why.** The runner commit carries only
FIXTURE-DRIVEN arms — every assertion about the chunk verb, the halt, the ordering and the report
grammar, each driven through the manifest seam against a scratch manifest. The arms that grade the
REAL manifest — AC6's every-leg-carries-a-chunk assertion and its contiguity clause — land in the
SAME commit as the chunk keys, because against a keyless manifest they cannot pass. Splitting them
the other way would red the canary from the runner commit until the build's final commit, spanning
`-4` and `-7`, both of which run this canary in their own §7, with the pre-push hook blocking a red
push — so the middle of the sequenced build could not land, and the cheapest field repair would be
to re-weaken AC6 to the conditional form the round-1 fix removed.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | the parse field, the chunk-major key, the reader walk, the chunk verb, the halt |
| `tools/run-gates/run-gates.test.sh` | S8's arms; existing arms restated in comment only |
| `tools/gate-legs.json` | the chunk key on every leg the manifest holds at that commit (73, not the 70 at this base), and the reorder — last commit of the build |
| `memory/guides/SESSION-KICKOFF.md` | the gate-command block |
| `AGENTS.md` | the chunk contract sentence only |

### Alternatives rejected

- **A separate chunk-declaration file.** Rejected: the manifest is already the single source three
  other consumers treat it as, and a second file is a second thing to keep in step.
- **Report-side chunking only.** Rejected by the measurement above: it would move the first verdict
  later, not earlier.
- **A barrier between chunks.** Rejected: it would idle the pool at every boundary and lengthen the
  run, for a reporting property that contiguity already gives.

## 5. Production-readiness checklist

- security — no new file is written by this unit; the roll-up rides records that already exist.
- perf / scale — the reorder is a sort key change; no additional process is spawned.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell.
- error / empty / loading states — the all-skipped chunk IS the empty state and reports as skipped
  rather than green, with its own arm.
- observability — this unit is the observability fix; the measured blindness is its motivating
  failure.
- risks (concurrency, data-loss, rollback hazards) — the halt kills live workers, so the kill must
  precede the scratch cleanup. The manifest reorder is the one merge hazard and is sequenced last.
- testing + left-shift gates — the contiguity arm left-shifts the interleaved-manifest class.
- migration / rollback — a manifest with no chunk keys behaves exactly as today, which is both the
  migration path and the rollback.
- user docs — S9 plus the charter sentence.

## 6. Acceptance criteria

- **AC1** — When the runner runs against a manifest carrying NO chunk key, its stdout is identical
  line for line to the same runner over the same manifest before this unit landed, asserted in
  `tools/run-gates/run-gates.test.sh` against a fixture manifest carrying no chunk key.
- **AC2** — When a chunk completes, the runner prints one chunk verdict line naming the chunk and
  its passed, failed and skipped tallies, and `bash tools/run-gates/run-gates.test.sh` asserts the
  grammar.
- **AC3** — When a leg in an early chunk fails on a non-authoritative run, the run halts at that
  chunk's boundary, every leg of that chunk has been reported, each later chunk prints exactly one
  not-reported line, and the exit is 1 — asserted in `tools/run-gates/run-gates.test.sh`.
- **AC4** — When the same failure occurs with the no-halt flag set, every chunk is reported and no
  chunk prints a not-reported line — the property a landing depends on, asserted in
  `tools/run-gates/run-gates.test.sh`.
- **AC5** — When every leg of a chunk is skipped, that chunk reports as skipped rather than green,
  and the run does not halt there, asserted in `tools/run-gates/run-gates.test.sh`.
- **AC6** — When `bash tools/run-gates/run-gates.gov.test.sh` runs — the GOV-ONLY harness
  `TOOL-aPacedTurnstile-1` S1 splits out — it asserts UNCONDITIONALLY that every leg in
  `tools/gate-legs.json` carries a `chunk` whose value is one of the declared six, and that the
  chunks are contiguous. Stated unconditionally because a criterion beginning "when chunks are
  declared" makes the arm conditional on the very thing it exists to enforce; placed in the gov-only
  file because gov's SIX declared names are gov's corpus, an adopter's manifest is seeded empty and
  emitted from descriptors with no `chunk` key, and this arm would otherwise red on arrival in every
  target (round 2's R10). It lands in the same commit as the chunk keys, per §4 Rollout.
- **AC6b** — When `bash tools/run-gates/run-gates.test.sh` runs — the SHIPPED canary, in any tree —
  a deliberately interleaved FIXTURE manifest still reports each chunk's legs together, and a fixture
  manifest with no `chunk` key at all runs green with every leg in the default chunk. Fixture-driven
  and tree-agnostic, so it lands in the runner commit and is what an adopter receives. This is also
  what reconciles §8's catch-all: the default chunk is for adopters and for the no-chunk rollback,
  and AC6's every-leg assertion scopes to gov's manifest alone.
- **AC12** — When a run halts at a chunk boundary, no descendant process of any killed leg survives —
  asserted in `tools/run-gates/run-gates.test.sh` against a fixture leg that spawns a child. Asserting
  the printed lines and the exit code says nothing about what is still running.
- **AC7** — When the timing ledger is absent, dispatch order is pure chunk-major, asserted against
  the dispatch order the run's `header` carries under `<git-dir>/gate-run/<run-id>/`.
- **AC8** — When the ledger is present, a leg whose duration reaches the pole threshold is
  dispatched in the first batch, asserted against that same `header` field. Both poles are checked,
  not just the longest.
- **AC9** — When a run halts, `<git-dir>/gate-last-summary.txt` carries the chunk roll-up and the
  list of chunks not reported.
- **AC10** — When any chunk verdict line is printed, it carries no elapsed time, so the existing
  width-1 against width-4 equivalence arm in `tools/run-gates/run-gates.test.sh` passes unmodified.
- **AC11** — When `bash tools/check-testsuite-counts.sh` runs, the canary reports its executed
  assertion count at or above its floor, and the count registry carries no row naming it —
  `TOOL-aPacedTurnstile-1` S11 deletes that row beside the counter it adds, and the two must land
  together or one of the pair reds (round 2's R4/R5).
- **AC13** — When `memory/guides/SESSION-KICKOFF.md` is searched after S9 lands, a grep finds the
  chunk-contract sentence AND the sentence saying a red chunk halts the run, both non-zero; and the
  same positive grep finds the chunk-contract sentence in `AGENTS.md`. Round 2's R22: every sibling
  arms its doc edit and this unit armed neither of its two, while the kickoff guide is the file the
  kickoff skill loads at hand-back — so an operator would read a truncated per-chunk verdict list as
  a complete one and never learn that a red chunk stops the run.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.evidence.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/memory-tree/check-memory-hygiene.sh` · `python tools/govkit/govkit.py selfcheck` ·
`bash tools/check-playbook-parity.sh`.

## 8. Open questions

none — the forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

- **Whether the first verdict timing belongs in acceptance at all.** The research brief proposed an
  acceptance criterion asserting the first chunk verdict appears within about 90 s. RESOLVED (agent,
  2026-08-18, delegated): it does not. That is a wall-clock assertion on the real bar graded against
  load the runner does not control, which is exactly the retired-arm class this repo already paid
  for twice. The timing prediction goes to the build ledger as a measurement; the acceptance
  criteria assert ORDER and GRAMMAR, which are properties of the runner.
- **Whether `rest` is a legal chunk in gov's own manifest.** Recommendation: no. Every gov leg gets
  an explicit chunk and the contiguity arm makes an unclaimed leg visible; the default exists for
  adopters and for the no-chunk rollback path.
  RESOLVED (agent, 2026-08-18, delegated), with its REASON corrected after round 2's R29: no, `rest`
  is not legal in gov's own manifest. The protection is AC6's UNCONDITIONAL every-leg-carries-a-chunk
  assertion, not contiguity — the first ratification gave contiguity as the reason, which is the
  reasoning round 1 refuted by construction: a leg with no key falls into the default chunk, and one
  or two unclaimed legs form a default chunk that is trivially contiguous. Contiguity is kept for
  what it actually buys, report order equalling manifest order. Stating it correctly matters because
  a later editor trimming AC6 back toward its contiguity clause would believe they were keeping the
  guard §8 describes. `rest` stays in the kit for adopters and for the no-chunk rollback path, which
  is where its value is, and AC6b is the arm that grades it there.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-3 · 2026-08-18 · folded the blocker re-review: AC7 and AC8 pointed at a `header` path that
  `TOOL-aPacedTurnstile-5`'s F2 fix had moved under the per-run directory, so both read a file no
  unit writes any more. AC8 now checks both poles rather than the longest.
- rev-2 · 2026-08-18 · folded the spec audit: the dispatch-order key is declared in
  `TOOL-aPacedTurnstile-5`'s header rather than read from a field no unit wrote (F12, F13); the halt
  signals the process group, because killing the shell's job leaves the leg and its children running
  (F16); AC6 becomes unconditional and gains the every-leg-carries-a-chunk assertion (F15, F36); the
  pole set is corrected from one leg to two (F34).
- rev-4 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.
- rev-5 · 2026-08-18 · folded the round-2 spec audit. R17: S2 and the inventory stop freezing 70 —
  the reorder lands LAST, by which point `-1` has added two legs and `-4` one, so a builder
  assigning from a frozen table leaves exactly the three legs AC6 reds on; S2 now names the chunk
  each takes. R14: §4 Rollout states which arms ride which commit — fixture-driven arms with the
  runner, the real-manifest arms with the chunk keys — because AC6 asserted unconditionally against
  a keyless manifest would have kept the canary red across `-4` and `-7`, both of which run it, with
  the pre-push hook blocking every landing in between. R10: AC6 moves to the gov-only harness and
  AC6b takes the tree-agnostic half, so the shipped canary is not keyed on gov's six chunk names;
  this also reconciles §8's adopter catch-all with AC6's scope. R22: AC13 arms S9's kickoff-guide
  edit and the charter sentence, neither of which any criterion or gate observed. R29: §8's second
  resolution gave contiguity as the protection, which round 1 refuted by construction; the reason is
  restated as AC6's unconditional assertion. R4/R5: AC11 gains the registry clause.

## 10. Reuse audit

The seam this extends is the runner's existing record-separated wire protocol between its inline
manifest parser and its bash reader, which already carries an empty-field-safe separator chosen for
that property. The dispatch hint it replaces is the same longest-first sort the runner already
computes from its timing cache, now keyed by chunk with a pole escape; the cache itself is
`TOOL-aPacedTurnstile-5`'s ledger, whose second field stays the duration so this parser needs no
change. The blocking reader and its documented race are consumed unchanged. The halt reuses the
existing authoritative-run asymmetry rather than inventing a knob, extended by one explicit flag for
the collision with `TOOL-aPacedTurnstile-7`.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned `TOOL-aTimedTurnstile-3` (the
floor is the longest leg, which is why the tail sits in its own chunk) and the aTimedTurnstile
review's F3 and the `TOOL-cFinalBerth-5` row (both wall-clock arms graded against uncontrolled load,
which is why AC2's timing claim was refused).
