# TOOL-aPacedTurnstile-3 — ordered chunks, and a verdict the operator sees before the run ends

**Status:** OPEN · rev-9 · 2026-08-20 · node a · Tier-2 · base 43a6c13e · streams tooling

## 1. Goal

Group the legs into ordered, extensible CHUNKS so the bar reports chunk by chunk, each chunk closed
by its own verdict line, instead of one undifferentiated list of every leg followed by a single
verdict at the end. The defect this closes is operator VISIBILITY, not wall clock: the sibling build
`aMeteredTurnstile` measured 9.3 minutes of silence before the first leg verdict on a full bar, and
what finally arrives is a flat list whose length is itself derived rather than fixed.

## 2. Scope (IN)

- **S1** — `tools/gate-legs.json` gains one optional per-leg key naming its chunk. Chunk ORDER is
  order of first appearance; no second declaration file and no order field. A leg with no key falls
  into a default chunk.
- **S2** — EVERY leg in `tools/gate-legs.json` AS IT STANDS AT THIS UNIT'S COMMIT gets an explicit
  chunk key. No count is written here, and none is written beside the manifest either. Earlier revs
  of this item computed one — 70 at the old base, then 73, then 74 — and every one of those figures
  was wrong before the ink dried, because the manifest grows from OUTSIDE this build's roster: of the
  legs added between the old base `6517579f` and the re-scope base, only a minority came from units
  this spec names. A closed set named here is wrong by CONSTRUCTION, not merely stale. A builder
  derives the population at the commit with
  `python -c "import json;print(len(json.load(open('tools/gate-legs.json'))))"` and assigns each row
  by the routing rule in §4 Inventory. The whole-manifest row REORDER this item used to carry is
  CUT — §3 records it with its reason.
- **S3** — the runner parses the key as an added field on the existing record-separated wire
  protocol, builds an ordered chunk list and a per-chunk index list, and REPORTS chunk by chunk: the
  legs of a chunk in manifest order, then one chunk verdict line. Dispatch is untouched.
- **S6** — a chunk in which every leg was skipped reports as skipped, never as green. On a scoped
  run the guard pre-pass decides those legs before dispatch, so such a chunk reports at once.
- **S7** — the durable summary and failure records gain a chunk roll-up including per-chunk wall
  time, which is banned from stdout but not from these files.
- **S8** — arms for the report grammar, the all-skipped chunk and the interleaved-fixture grouping go
  in the SHIPPED canary `tools/run-gates/run-gates.test.sh`, because all of them are fixture-driven
  and true in any tree. The every-leg-carries-a-chunk assertion over gov's REAL manifest goes in
  `tools/run-gates/run-gates.gov.test.sh`, the gov-only harness `TOOL-aPacedTurnstile-1` split out
  and `tools/run-gates/kit.toml` withholds from the payload, matching AC6 and AC6b. An earlier draft
  put a real-manifest arm in the shipped canary, which is the file AC6 had just moved it out of, and
  would have re-created the red-on-arrival failure round 2's R10 named (round 3's T9). Existing arms
  keep their current assertions.
- **S9** — `memory/guides/SESSION-KICKOFF.md`'s gate-command BLOCK gains the chunk contract. This
  unit owns that BLOCK for this build — not the file, which is edited by three other units:
  `TOOL-aPacedTurnstile-1` S10 repointed four path spellings there including the manifest-audit
  `watch:` line, `TOOL-aPacedTurnstile-2` repaired the width claim inside this very block, and
  `TOOL-aPacedTurnstile-7` S9 rewrites the safety-property sentence. The first two have LANDED: line
  6 of that file already carries the repointed `watch:` spellings and line 77 already carries the
  profile-table width claim. The exclusive-ownership claim an earlier draft made was the set's only
  statement about who may touch that file and it was false, so a builder on `-1` would have read it
  as licence to skip the `watch:` repoint whose omission fails the kickoff ratchet (round 3's T17).

## 3. Non-goals (OUT)

- **The whole-manifest row REORDER, and the contiguity property it produced.** Cut by the 2026-08-20
  re-scope. It bought no wall clock — with dispatch unchanged it never could — while rewriting every
  row of a file three OPEN sibling builds are queued to add rows to, and the row-keyed merge driver
  does not cover JSON. The consequence is deliberate and permanent: gov's chunks are NON-CONTIGUOUS
  in the manifest, so the runner's group-by-first-appearance walk is the only mode rather than a
  fallback, and AC6 loses its contiguity clause. The recommendation is recorded as refused, not
  deleted, because a later editor reading "report order equals manifest order" as a theorem would
  re-derive the reorder to get it back.
- **Chunk-major dispatch (the cut S4), its long-pole escape hatch, and AC7 and AC8 with it.** The bar
  is FLOOR-bound: measured 2026-08-20 at sha `43a6c13e` on a quiet node `a` by
  `python tools/run-gates/profile_bar.py` under `GATE_FULL=1`, one leg is 836.5 s of a 1033.2 s wall,
  81 % of it, and that instrument states the consequence in its own output — no width and no ordering
  of the other legs goes below the floor. Scheduling on a floor-bound bar buys ZERO, so this unit
  stops touching dispatch at all. AC8's pole arithmetic went with it; the threshold it pinned is not
  restated anywhere in this spec, because a formula whose only consumer is cut is a trap.
- **The chunk-boundary HALT, its no-halt flag, its process-group kill, and AC3, AC4 and AC12.** Cut
  with S5 by the same re-scope. A halt is a scheduling decision about work not yet done, and its only
  payoff was wall clock the floor makes unavailable. Two live consequences fall out and are the
  reason this is recorded rather than dropped: `TOOL-aPacedTurnstile-7`'s S7 dependency on the
  no-halt flag DISSOLVES, so `-7` no longer waits on this unit; and the "chunks not reported" half of
  S7 and of AC9 dissolves with it, since no run stops early.
- **The run-record dispatch-order header key.** S3 used to ask `TOOL-aPacedTurnstile-5` to declare a
  header field carrying the resolved dispatch order, read by AC7 and AC8. With dispatch unchanged
  there is no new order to record, so this unit WITHDRAWS the request. If `-5`'s own spec still
  declares that key when it lands, it declares a key nothing reads — a smaller defect than a key
  nothing writes, which is why the withdrawal is stated here rather than negotiated.
- Printing a duration on stdout. The existing width-1 against width-4 equivalence arm at
  `tools/run-gates/run-gates.test.sh` compares output line for line, so any elapsed time on the
  stream breaks it. Per-chunk wall time goes to the durable records instead.
- Any new line beginning with the existing leg-verdict or summary prefixes. The chunk verb is a new
  prefix precisely so existing prefix-counting arms keep their meaning.
- Changing what any leg asserts, or any guard.
- The `AGENTS.md` timing figure. `TOOL-aPacedTurnstile-2` owns that line; this unit adds only the
  chunk contract sentence.
- Making any leg faster. That is the only thing that moves this bar's wall clock, and it is a
  separate build.

## 4. Design

### The root cause, and what the re-scope leaves of the fix

The runner sorts dispatch longest-first from the timing cache and the reader walks the manifest, so
the reader blocks on whatever manifest position the cheapest leg occupies. Those two orders are near
INVERSES. The original design broke the inversion by making dispatch chunk-major; the re-scope cut
that, because the arithmetic says it cannot pay on a floor-bound bar. What survives is a change to
the reader's WALK ORDER alone, and this section states plainly what that does and does not buy,
because the previous rev's argument for the opposite conclusion is still in the revision log.

What it buys unconditionally: STRUCTURE. Every leg's verdict lands inside a named chunk, each chunk
is closed by one verdict line carrying its own tallies, and the durable roll-up says where the run's
time went. An operator reading a bar whose leg count is itself derived gets a grouped list instead of
a flat one, and that property holds at every width and on every tree.

What it buys conditionally: the FIRST signal. The reader stops blocking on manifest index 0 and
blocks instead on the first leg of the first chunk. On a scoped run that is a guaranteed win, because
the guard pre-pass decides skipped legs before any dispatch happens, so a chunk whose legs are all
guarded out reports the instant the walk reaches it. On a FULL run the gain depends on where the
first chunk's legs land in the unchanged longest-first order, which is a measurement rather than a
prediction — take it with `python tools/run-gates/profile_bar.py`, which records the run envelope
alongside the numbers, and never from `<git-dir>/gate-timings.tsv`, which is a last-write-wins
dispatch hint that mixes runs and inflates under contention. §8 carries the one open question this
leaves.

What it costs: nothing in wall clock. Chunks bound REPORTING only, so the pool never idles, no leg
starts later than it does today, and the LAST line still appears when the last leg finishes.

### Data model

One optional slug per leg. Order is first appearance. Chunks are NOT required to be contiguous —
that requirement was the reorder's product and the reorder is cut, so the runner's tolerant mode is
the only mode: group by first appearance, report each chunk's members in manifest order. The same
tolerance is what an adopter needs anyway, because the deployer appends emitted rows kit by kit and
an adopter's manifest can interleave chunks for reasons no gov decision controls.

The manifest's known key set after this build is `name`, `argv`, `guard`, `chunk`, pinned in one
place by `TOOL-aPacedTurnstile-1`. The `impure` key an earlier draft listed here is cut by
`TOOL-aPacedTurnstile-6`'s own re-scope and is not this unit's to add.

The wire protocol between the runner's inline parser and its bash reader gains one field on the
existing record separator, which is non-whitespace precisely so an empty field survives the read.

AC6's every-leg assertion is a RATCHET, and the cost is stated rather than discovered: once it lands,
every future commit that adds a manifest row must name a chunk for it or gov's bar reds. That is the
intended behaviour and it is the same shape as the codebase-map key ratchet, but it is a standing
obligation on builds outside this roster, which is the strongest single reason this unit lands LAST.

### Inventory — the default chunk assignment

Six chunks, every leg claimed exactly once. What follows is the ROUTING RULE, not a census. Earlier
revs carried a per-chunk leg count and a measured-max column; both were censuses of a population that
moved while the spec sat open, and a builder assigning from a frozen table leaves exactly the legs
AC6's unconditional arm reds on — which is the failure round 2's R17 was raised to prevent and which
the frozen table then re-created anyway.

| chunk | what it grades, and therefore what routes to it |
|---|---|
| `records` | the memory tree and the build-README surface — the verdict a records-only commit waits for |
| `product` | the graders of the shipped playbook, template, prefix and micro-format surface |
| `wiring` | every leg asking whether this clone is wired and whether the shipped source parses |
| `declarations` | registries, coverage, and record-versus-reality over the live tree |
| `selftests` | every red/green harness over a gate, and every canary |
| `e2e` | every leg that builds a scratch repo and drives an adopter or a driver end to end |

The rule was run over the manifest as it stands at this spec's base and every row routes under it, so
SIX declared names still suffice and `tools/run-gates/run-gates.gov.test.sh:8`, which already says
"six declared chunk names", does not move. Note for the builder: the longest leg on this bar is a
`selftests` leg, not an `e2e` one. An earlier rev asserted the tail sits in `e2e` BY DESIGN and used
that to argue chunk-major dispatch was safe; the claim was false and the argument it supported is
cut, so nothing now depends on which chunk holds the tail.

### Concurrency

One sentence carries it: **chunks bound REPORTING, never DISPATCH.** Legs run at full pool width in
whatever order the existing longest-first hint gives, across chunk lines freely. Only the reader's
walk order changes, from the raw index range to a flattened chunk-then-manifest list. Because gov's
manifest is deliberately non-contiguous, that flattening is a real permutation rather than an
identity, so the reader's diff is the indirection plus a per-chunk boundary hook — and the race the
runner already documents, where the timing cache decouples dispatch from manifest order, is neither
worsened nor improved. The arm guarding that race stays untouched.

### Rollout

ONE commit. The two-commit split earlier revs specified existed to sequence the manifest reorder
last, and round 2's R14 required the real-manifest arms to ride the same commit as the chunk keys
because against a keyless manifest they cannot pass. With the reorder cut and this unit last in the
build order, a single commit satisfies R14 trivially and leaves no window in which the canary is red.
That window was the whole hazard: it would have spanned sibling units that run this canary, with the
pre-push hook blocking a red push, and the cheapest field repair would have been to re-weaken AC6 to
the conditional form the round-1 fix removed.

Build order after the 2026-08-20 re-scope is `-5 → -4 → -6 → -7 → -3`. This unit is last because it
is reporting-only and has NO dependents, not because anything waits on it — the edge that used to run
`-3 → -4` was the halt's kill path, and the edge `-6 → -3` was the base the chunk-skip reporting was
graded against. Both dissolve with the cuts in §3.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | the parse field, the chunk list, the reader walk, the chunk verb, the roll-up |
| `tools/run-gates/run-gates.test.sh` | S8's fixture-driven arms, and the assertion floor raised to cover them |
| `tools/run-gates/run-gates.gov.test.sh` | AC6's every-leg assertion over gov's real manifest |
| `tools/gate-legs.json` | the chunk key on every leg the manifest holds at that commit, DERIVED there and written as no figure here |
| `memory/map/features/run-gates.md` | the dossier whose subject this unit changes: refresh the prose the runner change invalidates and append this unit's id to its `decisions` list |
| `memory/guides/SESSION-KICKOFF.md` | the gate-command block |
| `AGENTS.md` | the chunk contract sentence only |

One landing-report trap, recorded so nobody investigates it twice: `AGENTS.md` sits at exactly its
recorded high-water in `tools/template-size-highwater.txt`, so S9's added sentence emits a
`TEMPLATE-SIZE WARN` from `tools/check-template-size.sh` and wants a deliberate `--bump` in the same
commit. It is advisory rather than red, and the declared ceiling has room for the sentence.

### Alternatives rejected

- **A separate chunk-declaration file.** Rejected: the manifest is already the single source three
  other consumers treat it as, and a second file is a second thing to keep in step.
- **Reporting each leg as it completes, in dispatch order.** Rejected: it would give the earliest
  possible first signal and destroy byte-stability across widths, which the width-1 against width-4
  equivalence arm exists to hold.
- **A barrier between chunks.** Rejected: it would idle the pool at every boundary and lengthen the
  run, for a reporting property the walk order already gives.
- **Chunk-major dispatch.** Rejected by the floor measurement — see §3, where it is recorded as a
  cut rather than as a design option, because it was previously IN scope.

## 5. Production-readiness checklist

- security — no new file is written by this unit; the roll-up rides records that already exist.
- perf / scale — reporting-only; no additional process is spawned and no leg starts later.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell.
- error / empty / loading states — the all-skipped chunk IS the empty state and reports as skipped
  rather than green, with its own arm.
- observability — this unit is the observability fix; the measured silence is its motivating failure.
- risks (concurrency, data-loss, rollback hazards) — the halt and its worker kill are cut, so the
  data-loss surface is gone. The residual risk is AC6's ratchet: after it lands, a leg added by any
  build with no chunk key reds gov's bar.
- testing + left-shift gates — the interleaved-fixture arm left-shifts the non-contiguous-manifest
  class, which is now gov's own permanent state rather than an adopter-only one.
- migration / rollback — a manifest with no chunk keys behaves exactly as today, which is both the
  migration path and the rollback.
- user docs — S9 plus the charter sentence.

## 6. Acceptance criteria

Five criteria were CUT by the 2026-08-20 re-scope — the halt pair, the two dispatch-order ones, and
the descendant-kill one — and §3 records each with its reason. The surviving ids keep their numbers,
gaps and all, so sibling specs and review rounds that cite them still resolve.

- **AC1** — When the runner runs against a manifest carrying NO chunk key, its stdout is identical
  line for line to the same runner over the same manifest before this unit landed, asserted in
  `tools/run-gates/run-gates.test.sh` against a fixture manifest carrying no chunk key.
- **AC2** — When a chunk completes, the runner prints one chunk verdict line naming the chunk and
  its passed, failed and skipped tallies, and `bash tools/run-gates/run-gates.test.sh` asserts the
  grammar.
- **AC5** — When every leg of a chunk is skipped, that chunk reports as skipped rather than green,
  asserted in `tools/run-gates/run-gates.test.sh` against a fixture whose guards exclude a whole
  chunk.
- **AC6** — When `bash tools/run-gates/run-gates.gov.test.sh` runs — the GOV-ONLY harness
  `TOOL-aPacedTurnstile-1` split out — it asserts UNCONDITIONALLY that every leg in
  `tools/gate-legs.json` carries a `chunk` whose value is one of the declared six. Stated
  unconditionally because a criterion beginning "when chunks are declared" makes the arm conditional
  on the very thing it exists to enforce; placed in the gov-only file because gov's SIX declared
  names are gov's corpus, an adopter's manifest is seeded empty and emitted from descriptors with no
  `chunk` key, and this arm would otherwise red on arrival in every target (round 2's R10). The
  contiguity clause this criterion used to carry is cut with the reorder.
- **AC6b** — When `bash tools/run-gates/run-gates.test.sh` runs — the SHIPPED canary, in any tree —
  a deliberately interleaved FIXTURE manifest still reports each chunk's legs together and in
  manifest order within the chunk, and a fixture manifest with no `chunk` key at all runs green with
  every leg in the default chunk. This is the arm that grades gov's own permanent shape as well as an
  adopter's, since gov's manifest is not reordered, and it is what reconciles §8's catch-all: the
  default chunk is for adopters and for the no-chunk rollback.
- **AC9** — When a run completes, `<git-dir>/gate-last-summary.txt` carries the chunk roll-up with
  per-chunk wall time, asserted in `tools/run-gates/run-gates.test.sh` by reading that file after a
  fixture run.
- **AC10** — When any chunk verdict line is printed, it carries no elapsed time, so the existing
  width-1 against width-4 equivalence arm in `tools/run-gates/run-gates.test.sh` passes unmodified.
- **AC11** — When `bash tools/check-testsuite-counts.sh` runs after this unit's arms land, the
  canary's printed assertion count meets a `FLOOR_ASSERTIONS` RAISED in the same commit to cover
  them, and the count registry `memory/project/testsuite-count-waivers.txt` still names no run-gates
  path. The landing-coordination clause this criterion used to carry described work
  `TOOL-aPacedTurnstile-1` S11 finished; what remains is a guard that a new arm which never executes
  cannot pass unnoticed.
- **AC13** — When `memory/guides/SESSION-KICKOFF.md` and `AGENTS.md` are searched after S9 lands, a
  grep finds the chunk-contract sentence in both, non-zero in each. Round 2's R22: every sibling arms
  its doc edit and this unit armed neither of its two, while the kickoff guide is the file the
  kickoff skill loads at hand-back. The halt sentence this criterion also grepped for is cut with the
  halt.
- **AC14** — When `bash tools/run-gates/profile_bar.test.sh` runs on this unit's diff, it is green:
  the profiler parses the runner's verdict stream and this unit adds a new line shape to it. Its
  parser skips any line its `VERDICT` regex does not match, so the chunk verb passes through — that
  is a property to ASSERT on this diff, not to assume, and the leg is guarded on `tools/run-gates/`
  so it fires whether or not anyone remembers.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.gov.test.sh` ·
`bash tools/run-gates/run-gates.evidence.test.sh` · `bash tools/run-gates/profile_bar.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `bash tools/check-template-size.sh AGENTS.md` ·
`bash tools/check-line-length.sh` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/memory-tree/check-memory-hygiene.sh` · `python tools/govkit/govkit.py selfcheck` ·
`bash tools/check-playbook-parity.sh`.

The last four legs on the first line, plus the two `check-` legs on the second, are additions since
the old base `6517579f`: `profile-bar selftest` landed from `aMeteredTurnstile` into this unit's own
kit directory and is guarded on it, and `charter size` and `line length` both grade files §4 Files
touched names. A spec that lists only the gates that existed when it was written sends its builder
into a red bar it did not predict.

## 8. Open questions

- **Does the surviving reporting-only change actually move the first signal on a FULL bar?** The
  re-scope kept "the early first signal" in this unit's value while cutting chunk-major dispatch,
  which is the mechanism the previous rev argued was necessary for it. The two are in tension and
  this spec does not resolve it by assertion. On a SCOPED run the win is structural and certain, per
  §4. On a full run the reader stops blocking on manifest index 0 and blocks on the first chunk's
  first leg instead, and whether that leg completes earlier is a fact about the unchanged
  longest-first dispatch order, not about this change. Options seen, none picked: (a) accept the
  grouped output and the scoped-run win as this unit's whole value, and record the full-run figure as
  a measurement in the build ledger rather than as a claim; (b) reopen a NARROW dispatch preference
  confined to the first chunk only, as its own unit, if a measurement shows no movement; (c) drop the
  first-signal language from this unit's goal entirely and let it be a structure change. Whichever is
  taken, the number comes from `python tools/run-gates/profile_bar.py` on a quiet node and never from
  `<git-dir>/gate-timings.tsv`.

The two forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

- **Whether the first verdict timing belongs in acceptance at all.** The research brief proposed an
  acceptance criterion asserting the first chunk verdict appears within about 90 s. RESOLVED (agent,
  2026-08-18, delegated): it does not. That is a wall-clock assertion on the real bar graded against
  load the runner does not control, which is exactly the retired-arm class this repo already paid
  for twice. The timing goes to the build ledger as a measurement; the acceptance criteria assert
  ORDER and GRAMMAR, which are properties of the runner. The re-scope leaves this resolution
  standing, and the open fork above is why it matters more now than it did: with dispatch untouched,
  a timing criterion would be graded almost entirely on load.
- **Whether `rest` is a legal chunk in gov's own manifest.** Recommendation: no. Every gov leg gets
  an explicit chunk and AC6's arm makes an unclaimed leg visible; the default exists for adopters and
  for the no-chunk rollback path.
  RESOLVED (agent, 2026-08-18, delegated), with its REASON corrected after round 2's R29: no, `rest`
  is not legal in gov's own manifest. The protection is AC6's UNCONDITIONAL every-leg-carries-a-chunk
  assertion, which round 1 established is the only thing that can catch an unclaimed leg — one or two
  unclaimed legs form a default chunk that would satisfy any weaker structural test. The 2026-08-20
  re-scope makes this the ONLY protection, since the contiguity clause that once shared the sentence
  is cut with the reorder. `rest` stays in the kit for adopters and for the no-chunk rollback path,
  which is where its value is, and AC6b is the arm that grades it there.

## 9. Revision log

- rev-9 · 2026-08-20 · folded the owner's re-scope. This unit was designed around SCHEDULING, and the
  measurement taken at sha `43a6c13e` says scheduling cannot pay here: one leg is 836.5 s of a
  1033.2 s wall, so the bar is floor-bound and `tools/run-gates/profile_bar.py` states in its own
  output that no width and no ordering moves that number. So the dispatch half of this unit is cut —
  S4, the pole escape, AC7, AC8 — along with the chunk-boundary halt (S5, AC3, AC4, AC12) whose only
  payoff was wall clock the floor makes unavailable, and the whole-manifest row reorder (S2's second
  half) which rewrote every row of a file three open siblings are queued to add rows to and bought
  nothing measurable in exchange. Every cut is recorded in §3 with its reason rather than deleted,
  because the argument FOR chunk-major dispatch is still in this log and a later reader will find it.
  Three consequences ride along: `-7` no longer waits on this unit, since the no-halt flag it
  consumed is gone; gov's chunks are permanently non-contiguous, so AC6 loses its contiguity clause
  and AC6b's interleaved fixture becomes the primary arm rather than the adopter-only one; and the
  rollout collapses to one commit, which removes the red-canary window the two-commit split existed
  to manage. Separately, every pinned figure in the file was replaced with a derivation or a
  sha-and-date citation, per the re-scope's D1: the leg counts in S2 and the inventory table, the
  measured-max column, the pole arithmetic, and the 58 s / 62 s / 240 s / 500 s / 873 s first-verdict
  predictions were all computed against a 70-leg manifest that no longer exists, and the inventory's
  "the tail sits in `e2e`" was simply false — the longest leg is a `selftests` leg. §7 gained three
  legs that did not exist at the old base and that fire on this unit's diff, §4 Files touched gained
  the `memory/map/features/run-gates.md` dossier the runner change invalidates, AC11 was rewritten
  from a landing-coordination note about work `-1` already finished into a floor guard on this unit's
  own new arms, and AC14 was added because `profile_bar.py` parses the very verdict stream this unit
  changes. The header base moved from `6517579f` to `43a6c13e`, the sha the re-scope reground against,
  because §4 now cites files that did not exist at the old one. One genuinely undecided item went to
  §8 rather than being resolved by guess: the re-scope keeps "the early first signal" in this unit's
  value while cutting the mechanism the previous rev argued delivers it, and on a full bar that gain
  is now a measurement rather than a prediction.

- rev-8 · 2026-08-20 · S9's editor map named three units and `TOOL-aPacedTurnstile-2` made it four:
  that unit's own S8 falsified the width claim inside this block, and the kickoff ratchet forces the
  repair rather than permitting it. Recorded here because this unit rebases onto a rewritten line and
  onto both moved audit stamps, and a map that says three when four edited is the kind of false
  record a builder trusts. Raised by that unit's closing diff review.

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
- rev-6 · 2026-08-18 · folded the round-3 blocker re-review. T7/T11: the leg arithmetic R17 fixed
  moved again in the same fold, because the fix for R10 gave `TOOL-aPacedTurnstile-1` a fourth
  manifest leg — 73 becomes 74, the gov-only canary takes `selftests`, and both carriers now say the
  figure is DERIVED and has already moved once, with S2's count-free leading clause named as the
  binding one. T9/T22: this unit alone of the four carrying the gov harness was never swept — §7
  gains it, §4 Files touched gains its row, and S8 stops assigning the contiguity arm to the shipped
  canary AC6 had just moved it out of, which would have re-created the red-on-arrival R10 named.
  T17: S9's exclusive-ownership claim over the kickoff guide is narrowed to the gate-command BLOCK,
  since `-1` and `-7` both edit that file and one of those edits is the `watch:` line whose omission
  fails the kickoff ratchet.
- rev-7 · 2026-08-18 · folded round 4's V6: §4 Data model was T9's fourth carrier and the one the
  round-3 fold missed — it still assigned contiguity to "a canary arm" while AC6, AC6b, S8, §7 and
  the files-touched row all name the harness by path. It now names it too, and stops using the bare
  word for both harnesses.

## 10. Reuse audit

The seam this extends is the runner's existing record-separated wire protocol between its inline
manifest parser and its bash reader, which already carries an empty-field-safe separator chosen for
that property. The blocking reader and its documented race are consumed unchanged, and the
longest-first dispatch sort is now left alone entirely rather than re-keyed.

`tools/run-gates/profile_bar.py` landed into this unit's own kit directory from the sibling build
`aMeteredTurnstile` after the first audit and is the reuse this revision takes: it already owns the
floor-versus-throughput arithmetic an earlier rev of §4 froze into prose, deriving both bounds live
from the executed leg costs, and it already carries the run envelope that makes two measurements
comparable. This spec therefore points at it for every timing figure instead of restating one. It is
also a CONSUMER of the stream this unit changes, which is why AC14 exists.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned `TOOL-aTimedTurnstile-3` (the
floor is the longest leg, which the 2026-08-20 measurement confirms and which is why the scheduling
half of this unit is cut) and the aTimedTurnstile review's F3 and the `TOOL-cFinalBerth-5` row (both
wall-clock arms graded against uncontrolled load, which is why AC2's timing claim was refused).
