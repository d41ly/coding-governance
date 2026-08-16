# DEPL-aTetheredConvoy-1 — the truthful core: roles, the receipt, and one expansion

**Status:** OPEN · rev-4 · 2026-08-16 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Make the four facts every other unit of this build dispatches on true: which ROLE a landed file has,
what the RECEIPT records, what `plan` promises relative to what `apply` writes, and what `check`'s
per-kit state words mean. Each is measurably wrong or ambiguous today, and one of them —
role precedence — is a live path to overwriting a file the operator authored in a repository gov does
not own.

## 2. Scope (IN)

- **S1 — rule precedence, with ONE reduction key, stated once.** Two things happen and they have
  different keys, which is the distinction rev-3 collapsed and the audit caught. A `project-owned`
  rule is a SOURCE-level carve-out: it removes its matched sources from every earlier glob's
  contribution, and gov supplies no bytes for them ever. Among the rules that remain, the WRITER for
  each destination is the LAST landable rule resolving to it. Reducing by destination alone elects
  the seed template over the carve-out and makes the carve-out unobservable; reducing by source alone
  cannot express one source legitimately reaching two destinations under two roles, which two shipped
  descriptors do. Both `selfcheck` arms follow from the split: one reports every destination whose
  winning writer is not the first rule that matched it, and one reds when a source excluded by a
  carve-out is nonetheless written.
- **S2 — the role-landing closure.** Every role either lands, is written by a named other party, or
  REFUSES BY NAME. `generated`, `rendered` and `project-owned` are skipped with a PRINTED reason
  naming the party that does produce them — `project-owned` is not landable and does not become so,
  because after S3 no rule in the tree needs write-if-absent and adding the branch would be a widening
  nothing exercises. `merged` keeps its named refusal until unit 6. The silent skip that swallows
  thirteen rules across the tree today is deleted; there is no path out of the land loop that says
  nothing.
- **S3 — the playbook entry's rules are retagged `seed`.** Gov supplies those bytes once and the
  target owns them afterwards, which is exactly `seed`'s re-apply contract. This is the whole of what
  the playbook needed, and it is why S2 does not widen the landable set: the entry was mistagged, not
  under-served by the role enum.
- **S4 — receipt schema 2, and it is FROZEN here.** A `schema` integer; a per-file `version` carrying
  the kit's version constant as resolved at install; and a row for EVERY file gov is responsible for,
  derived from the resolved file set rather than serialized from the write log — which is what makes
  a `seed` row survive a second apply. Per-role row shapes are RESERVED here for the later units that
  fill them, so no unit invents a fourth spelling: `rendered` reserves template/inputs/output hash,
  `merged` reserves block id/style/block hash and carries no whole-file hash, and every gov-owned
  artifact in the target — including ones synthesized rather than copied — is a `files` row with a
  role, never a top-level block. Later units bump `schema` and extend the SAME per-role table.
- **S5 — `plan` and `apply` share ONE file-set expansion.** One function turns a descriptor's rules
  into (source, destination, role) triples; both verbs call it. `plan` marks a role `apply` cannot
  land as `SKIP` with the reason and never as `write`, and every artifact `apply` produces — including
  the ones later units add — gets a plan row through the same function.
- **S6 — the check-state vocabulary, settled ONCE and owned here.** Five states, each a measurement
  rather than a placeholder: `not-landed` (a kit with zero receipt rows whose descriptor declares at
  least one landable rule — today the no-receipt verdict is whole-target and early-returns),
  `landed-unmeasured` (legal only where the descriptor declares `[check] = { none = "<reason>" }`),
  `landed-but-inert` (reserved for a MEASURED failure), `adopted`, and `undischargeable` (reserved
  for unit 5's machine-scoped entries). The thirteen descriptors that declare no `[check]` gain the
  declared-absence form in this unit's diff, budgeted rather than discovered by a later one.
- **S7 — the step-id vocabulary, reserved ONCE and owned here.** A module-level ordered tuple naming
  every step of the hard order, including the ones this unit does not implement; every phase print
  reads it, and a `selfcheck` arm asserts the printed ids are exactly that tuple in that order.
  §4 carries the table with an owning unit per id, and no count of it appears in prose anywhere in
  this build. Reserving a name costs nothing and printing one is not required. Later units FILL steps
  and may never rename them.
- **S8 — the adopter's exit code stops being swallowed.** A non-zero adopter exit is a finding. The
  `[[outcome]]` evaluator that would interpret WHICH failure it is belongs to unit 5; until then the
  code is reported as an unclassified failure rather than printed and passed over.
- **S9 — the repairs S1–S8 surface at base**, listed in §4 rather than discovered by the builder:
  two entries carrying an empty adopter with no stated reason, one merged rule whose empty include
  list needs the delegation key unit 6 defines (restated from rev-3's "declare it a defect", because
  that rule is CORRECT and an arm reddening on it would make gov's own descriptor permanently red),
  one rule whose destination template resolves to a repo-root basename while its own `claims` spells
  the correct path, and one dead double-resolve in the check path.

## 3. Non-goals (OUT)

- **Everything the other six units own.** `update` (unit 2), the convergence ratchet (unit 3), the
  `[gate_runner]` declaration and everything that reads it (unit 4), `check`'s evidence loops and the
  `[[outcome]]` evaluator (unit 5), the `merged` writer and the `.gitattributes` phase (unit 6), the
  acceptance matrix and the refusal cross-check (unit 7). This unit lands the substrate they dispatch
  on and nothing else.
- **Claiming any clause of the hard-order criterion.** S7 reserves the step names; §4's table says
  which steps this unit implements. **ALL FOUR clauses of the contract's ordering criterion stay
  VACUOUS after this unit** — baseline-before-any-write, attributes-and-renormalize-before-the-first-
  content-write, staging-before-any-leg-runs, and gate-runner-wiring-last — because this unit
  implements neither the baseline, nor the attributes phase, nor the emitter. What it CAN assert is
  that the ids it prints appear in tuple order, which is a different and smaller claim, and §6 states
  it as one.
- **Rendering anything.** The adopters render; a second renderer racing the real one is the defect the
  contract already refuses. This unit makes a missing rendered destination a FINDING and stops there.
- **Repairing what S1 reveals beyond S9's list.** If precedence turning on surfaces a descriptor
  disagreement this spec has not named, it is a backlog row. A unit that repairs whatever its own new
  predicate finds has no bounded diff.

**Superseded by later units, recorded here so nothing is silently invalidated:** unit 6 deletes the
`merged` refusal S2 preserves, fills that role's reserved receipt row, and defines the delegation key
S9's repair needs; unit 5 fills the `rendered` and `undischargeable` rows and turns S8's unclassified
failure into a classified one; units 4, 5 and 6 fill the step ids §4's table assigns them.

## 4. Design

### The four wrong facts, measured

**A1 — precedence does not exist, and it writes a project-owned file.** The engine's land loop
iterates rules in declaration order and stamps each written file with the role of the rule that wrote
it; nothing consults a later rule. Measured on a reference install of the default set: every receipt
row carries role `engine`, and gov's own FILLED extractor module lands byte-identical in the target —
a file its own descriptor declares `project-owned` in a rule that appears three lines below the glob
that captured it. The contract's claim that no code path writes a `project-owned` file is false, and
the inherited-vacuous-numbers failure the memory-tree adopter warns about in its own closing output is
what an adopter actually receives.

This is the finding that decides this unit's position in the build. Three consumers dispatch on
`role`: `update`'s verdict table, `check`'s integrity loop, and the receipt's own row shape. A role
field that is measurably wrong on a real file in the default set, with no owner, is a data-loss path
in a repository gov does not own.

**A2 — the receipt shrinks.** A `seed` whose destination exists is skipped, and the skip returns
before the row is appended; the receipt and its sums sidecar are then serialized wholesale from the
write log. Measured: two applies of a seed-bearing kit, no gov change, leave the file list empty and
the sidecar empty. The idempotency criterion's existing arm uses a fixture kit chosen for having no
adopter — and therefore no seed rule — so it passes by finding nothing.

**A3 — `plan` promises what `apply` refuses.** The planner applies no role filter and has no branch
for a role the land loop cannot honour, so a `merged` rule prints as a `write` at exit 0 and the
writer then refuses it at exit 1. Measured on a fixture, three merged destinations and one side-effect
printed as writes, followed by "nothing was written", followed by an `apply` that refuses all three.
The set of landable roles is spelled in the engine and spelled again, by omission, in the planner. The
same divergence in the other direction is arithmetic: the planner emits one row per RULE and the
writer expands the same rule over tracked files, so the two counts are not in the same units.

**A4 — `check` prints a state it did not measure.** The default per-kit state is emitted for every
kit whose descriptor declares no check argv — thirteen of the entries — and it is the byte-identical
string the engine emits for a kit whose declared check arm FAILED. The verb's own docstring says exit
0 requires every selected kit to be adopted; measured, a kit that declares nothing prints the inert
state and exits 0. Two spellings of one fact, one of them a placeholder wearing a verdict's name.

**A5 — three silent exits from the apply path.** A role outside the landable set vanishes with no
message (thirteen rules across the tree: eight rendered, four project-owned, one generated); an
adopter exiting non-zero has its code printed and the run continues green; and the two SKIPPED notices
print unconditionally, before any selection is examined, so they are true of a selection containing
none of what they describe. Their only arm asserts the strings are present, with no position and no
negative half — it would keep passing after the steps are implemented.

### Precedence — two operations, two keys, stated once

rev-3 said "later rules win" and left the KEY ambiguous; the audit found the two halves of this spec
using different ones. The resolution is that there are genuinely two operations.

**Carve-out is keyed on SOURCE.** A `project-owned` rule declares that gov supplies no bytes for the
sources it names, ever. Resolution removes those sources from every earlier rule's contribution. This
is the only thing that rule does, and it is why `project-owned` is not landable.

**Writer election is keyed on DESTINATION.** Among the rules that survive the carve-out, the writer
for a destination is the LAST landable rule resolving to it.

Worked on the two shipped descriptors that need it. `tools/codebase-map/kit.toml` declares a `**`
engine glob, then `map_extractors.py` as `project-owned`, then `map_extractors.template.py` as `seed`
writing to `{kit}/map_extractors.py`. The carve-out removes gov's own filled module from the glob's
contribution — that is the byte an adopter must never receive. The seed rule then elects the TEMPLATE
as the writer of that destination. `tools/drift-audit/kit.toml` is identical in shape. So the file the
target ends up with is the template's, its receipt role is `seed`, and gov's filled copy is in no
receipt at all — which is what both descriptors have always meant and what no reduction key on its own
can express.

The template ALSO lands at its own kit-relative path through the glob, as `engine`. One source, two
destinations, two roles; a source-keyed reduction would have to pick one and lose the other.

**Two `selfcheck` arms follow, and neither is the other's restatement.** The first reports every
destination whose winning writer is not the first rule that matched it — the carve-out census, a NOTE
rather than a failure, because overlap is legal and is how a carve-out is spelled. The second FAILS
when a source a carve-out excluded is nonetheless written, which is A1 stated as a predicate. rev-3's
liveness half was a destination claimed by two rules "with no ordering between them", which a TOML
array of tables cannot express — the arm had no red state. §6 replaces it with one a descriptor can
actually produce.

### The step-id table

Owned here, filled by the units named. No count of these appears in prose anywhere in this build.

| # | step id | owning unit | what it does |
|---|---|---|---|
| 1 | `BASELINE` | unit 4 | read the target's own runner before any write |
| 2 | `ATTRIBUTES` | unit 6 | write the line-ending pin block |
| 3 | `LAND` | this unit | copy kit content from the gov index |
| 4 | `STAGE` | this unit | stage everything written |
| 5 | `HOOKPROBE` | unit 4 | would the operator's landing commit be refused |
| 6 | `CONFIGURE` | this unit | run each kit's adopter |
| 7 | `OBSERVE` | unit 5 | record the rendered destinations the adopters produced |
| 8 | `RENORMALIZE` | unit 6 | probe, renormalize, post-condition — deliberately AFTER configure |
| 9 | `LEGS` | unit 4 | emit legs into the target's runner, then CI |
| 10 | `AFTER` | unit 4 | the second runner read |
| 11 | `RECEIPT` | this unit | write the receipt and its sidecar |

`RENORMALIZE` sits after `CONFIGURE` rather than beside `ATTRIBUTES`, which DEPARTS from the contract's
stated hard order. Unit 6 carries the measurement that forces it: on a first install the pinned
population does not exist until the adopters have run. The departure is recorded here, in the table
every unit reads, rather than only in the unit that makes it.

### Receipt schema 2, frozen here

The receipt is written from the RESOLVED file set with a `written` boolean per row, not from the write
log. That single change is what makes a `seed` row survive, what makes `not-landed` decidable per kit
rather than per target, and what lets `update` reason about a file gov placed and did not rewrite.

Reserved per-role shapes, so no later unit invents a fourth:

| role | row carries | filled by |
|---|---|---|
| `engine` | whole-file `sha256`, `source`, `commit`, `version` | this unit |
| `seed` | the same, plus `written: false` on any re-apply | this unit |
| `project-owned` | existence and `version` only; no gov hash, because gov supplied no bytes after the first | this unit |
| `generated` | path only | this unit |
| `rendered` | template, substitution inputs with their hashes, output hash; no source commit | unit 5 |
| `merged` | `block_id`, `marker_style`, `block_sha256`, and deliberately NO whole-file `sha256` | unit 6 |
| `attributes`, `gate-leg`, `ci` | the synthesized artifact's identity and hash | units 4 and 6 |

The last row is the one the adversarial pass bought. A gov-owned artifact recorded as a top-level
receipt block is invisible to a per-row consumer, so a changed pin pattern, a renamed leg or a stale
CI setting would be classified as nothing by `update` forever — the upgrade-orphan class reintroduced
in three new places by the units built to close it. Every gov-owned path in the target is a `files`
row with a role; top-level blocks may carry extra fields, never the path.

The sidecar stays whole-file-only so it remains parseable by the checksum tool a target verifies with
bash alone, and its line count is asserted against the count of rows carrying a whole-file hash —
with the fixture receipt required to contain at least one row that does NOT, or the equality holds
vacuously.

### The state vocabulary, and why silence is not one of the states

The declared-absence form is copied from the version constant's, including its refusal text: a
descriptor may say `[check] = { none = "<reason>" }` and may not say nothing. That is the only way to
separate "nothing was measured" from "measured and broken" without reddening thirteen entries forever,
and the thirteen `none` blocks are budgeted into this unit rather than discovered by unit 5.

### Rollout

Four commits, each independently green.

1. **Precedence and the role-landing closure** — S1, S2, S3, S8, plus the precedence arm. This is the
   data-loss fix and it lands first for that reason. The receipt's role values change on the next
   apply, which is the point.
2. **Receipt schema 2** — S4, with the sidecar agreement arm. The commit that makes every later
   evidence loop non-vacuous.
3. **One expansion** — S5, with the plan-equals-apply arm over a fixture whose selection contains at
   least one unlandable role.
4. **The two vocabularies** — S6 and S7, the thirteen declared-absence blocks, and the S9 repairs.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` | the resolver, the receipt writer, the state vocabulary, the step tuple |
| Descriptors | the playbook entry, the thirteen gaining `[check] = { none }`, the four S9 repairs | the count is DERIVED by `selfcheck`, and is deliberately not written here |
| Tests | `tools/govkit/selftest.py` | every new arm plus its liveness half |
| Map | `memory/map/features/govkit.md` | the Gaps section shrinks; the seams gain the resolver |

### Alternatives rejected

**Fix precedence in `update` instead, by refusing a row claimed by two rules.** Cheaper and rejected:
the wrong role is already in every receipt on disk, and `check` and the receipt shape dispatch on it
too. Fixing the writer fixes all three; fixing one reader leaves the other two wrong.

**Keep the receipt as a write log and have `update` re-derive the expected set from the descriptors.**
Rejected. It is the same derivation done twice, in two places, disagreeing whenever the descriptors
move under an old install — and the sidecar, which a target verifies with bash alone, cannot re-derive
anything.

**Let each later unit define the receipt fields it needs.** Rejected on measurement: specced that way
in one pass, four sections produced four incompatible schemas with no version and no owner, two of
them using different names for the same boolean.

## 5. Production-readiness checklist

- security — this unit REDUCES write surface: `project-owned` stops being overwritten, which is a file
  the operator authored. Nothing new is executed and no remote is contacted.
- perf / scale — one extra pass over the resolved file set per entry; negligible against the existing
  per-file `git show`.
- a11y — N/A: a command-line tool with no interface beyond stdout.
- i18n — N/A: developer tooling, English only.
- error / empty / loading states — S2 and S6 ARE this line: every exit from the land loop and every
  per-kit state is now a named outcome rather than a silence or a placeholder.
- observability — the receipt is the surface, and this is the unit that makes it complete.
- risks — the role values in an EXISTING install's receipt are wrong and this unit does not migrate
  them; a re-apply corrects them and `update` (unit 2) must treat a schema-1 role as untrusted. Stated
  here because the alternative is a silent reinterpretation of records already on disk. Second risk:
  the carve-out changes what a first apply DELIVERS for two destinations — an adopter now receives the
  template's extractors and signals rather than gov's filled ones. That is the correction, and it is
  still a behaviour change, so an adopter re-applying after this unit sees those two files replaced.
- testing + left-shift gates — every arm carries a liveness half; the precedence arm's negative
  fixture is A1 reproduced deliberately.
- migration / rollback — receipt schema 1 is READ by unit 2 and never rewritten in place; the next
  apply writes schema 2. Rollback of this unit is the commit revert, and no target state is destroyed.
- user docs — the deploy-governance Skill gains the state vocabulary; no runbook change here.

## 6. Acceptance criteria

- **AC1** When `python tools/govkit/govkit.py apply --target <fixture> --kits codebase-map` runs, the
  landed `map_extractors.py` is byte-identical to `map_extractors.template.py` and NOT to gov's own
  filled copy, and its receipt row carries `role = "seed"` with the template as `source`. The same arm
  runs over `drift-audit`/`drift_signals.py`, so the fixture is not one-descriptor-shaped. Liveness:
  measured today the same command lands gov's FILLED copy and records `role = "engine"`, so the arm
  reds before this unit.
- **AC1b** When a fixture's `map_extractors.py` is edited before a SECOND apply, it is byte-identical
  afterwards — the `seed` contract — and gov's filled copy appears in no receipt row, asserted as an
  absence over the whole receipt rather than over one row.
- **AC2** When `python tools/govkit/selftest.py` runs the carve-out arm against gov's own descriptors
  it is silent and prints a DERIVED count of carve-outs resolved, non-zero. Liveness: a scratch
  descriptor whose LATER explicit rule must beat an earlier `include = "**"` glob is resolved
  correctly, and a mutated resolver that takes the FIRST match instead reds the arm — the mutation is
  the red state, because an ordered array of tables cannot express two rules with no ordering.
- **AC2b** When a source excluded by a `project-owned` carve-out is nonetheless written to any
  destination, `selfcheck` FAILS naming the source and the rule that wrote it. This is A1 as a
  predicate; the fixture reproduces A1 by removing the carve-out from the resolver.
- **AC3** When `apply` runs twice against a fixture with no gov change, the receipt's path set and
  every row's hash are identical between the runs, INCLUDING every `seed` row, and
  `.governance/install.sums` is byte-identical. The fixture selection must contain a `seed` rule, or
  the arm passes by finding nothing.
- **AC4** When `python tools/govkit/govkit.py plan --target <fixture> --all` and then `apply` run
  against the same fixture, the set of destinations `plan` marks `write` equals the set of paths the
  receipt records with `written: true`, exactly. The fixture selection must include at least one
  unlandable role, asserted as a `SKIP` row naming its reason.
- **AC5** When `apply` encounters a rule whose role it cannot land, it prints a line naming the role,
  the destination and the party that does produce it; the arm asserts NO rule leaves the land loop
  without a line. Liveness: a scratch descriptor carrying a role outside the enum makes `apply`
  refuse by name rather than skip.
- **AC6** When an adopter exits non-zero, `apply` reports a finding and exits non-zero; measured
  today the same condition prints the code and exits 0. Liveness: an adopter exiting 0 leaves the run
  green through the same code path.
- **AC7** When `python tools/govkit/govkit.py check --target <fixture>` runs against a kit whose
  descriptor declares `[check] = { none = "<reason>" }`, it prints `landed-unmeasured` and the
  declared reason; against a kit declaring neither argv nor a reason it REDS; and against a kit whose
  declared arm exits non-zero it prints `landed-but-inert`. Three distinct strings for three distinct
  measurements, asserted separately.
- **AC8** When a fixture's receipt CLAIMS a kit whose descriptor declares at least one landable rule
  and holds zero rows for it — a schema-1 receipt, or one deliberately row-stripped —
  `python tools/govkit/govkit.py check --target <fixture>` reports that kit `not-landed`. A target
  whose FILES were deleted while the receipt is intact is NOT this state: it is unit 5's per-row
  integrity failure, and this arm asserts `check` does not call it `not-landed`.
- **AC9** When `python tools/govkit/govkit.py selfcheck` runs, it asserts that the step ids `apply`
  prints are exactly the module-level tuple, in that order, and reds on an id printed out of order or
  absent from the tuple. Liveness: a scratch run with two ids transposed reds. The arm asserts ORDER
  among the ids this unit prints and claims NO clause of the contract's hard-order criterion — §3
  names all four as vacuous after this unit.
- **AC10** When `apply` runs against the default set, both playbook destinations exist on disk and
  are recorded with `role = "seed"`, and the `playbook-placeholders` hole probe runs against files
  that exist. Measured today the entry lands zero bytes and the probe names two absent paths.
- **AC11** When the receipt is written, every row carries a `version` resolved from the entry's
  `version_from`, and a row for an entry declaring `version_from = { none = ... }` carries the
  declared-absence marker rather than a null the next reader must interpret.
- **AC12** When `python tools/govkit/selftest.py` runs, `len(.governance/install.sums)` equals the
  count of receipt rows carrying a whole-file hash, AND the fixture receipt contains at least one row
  that carries none — the second conjunct is what stops the equality holding vacuously.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary; `GATE_FULL=1` for the DoD. No new leg in this
unit — every arm rides `govkit selftest` and `govkit selfcheck`, both already on the bar. That is
deliberate: unit 3 adds the deployability leg and unit 7 the matrix, and paying the four-gate leg tax
three times for one build is a cost this ordering avoids.

The kit version constant moves, because the engine's behaviour does; the version gate asserts it.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`. Two universal classes
are this unit's own subject — `two-answers-to-one-question` is what S4, S6 and S7 each close, and
`fixture-passes-by-finding-nothing` is why AC3, AC4 and AC12 each carry a fixture precondition rather
than only an assertion.

## 8. Open questions

none — the forks below are RESOLVED. Authority: the owner's instruction to execute this build
delegates resolver authority for THIS build only, and every fork here is one the spec already stated,
which is exactly M3's condition. Each was taken through M3's veto order; none was discarded by a veto,
and the two that touch a write or security surface are called out in the wrap-up as owner-review items
rather than treated as settled by silence.

- **F1 — does `project-owned` join the landable set, or does the playbook entry simply become
  `seed`?** RE-RESOLVED (agent, 2026-08-16, delegated, after the M4 audit): **the playbook retag
  ALONE.** The first resolution took both and was wrong on a fact neither option had checked: after
  S3 retags the playbook's two rules, the only remaining `project-owned` rules are the two carve-outs
  in the codebase-map and drift-audit descriptors, and those name sources gov must never supply. So
  a landable `project-owned` would have won zero destinations — a widened write surface with an empty
  domain, which is veto 3's shape wearing a helpful face. The role stays a SOURCE-level carve-out,
  which is observable, non-vacuous, and what both shipped descriptors have always meant. The audit
  finding that forced this is the reason a spec set gets audited before its code.
- **F2 — does this unit MIGRATE an existing install's wrong roles?** RESOLVED (agent, 2026-08-16,
  delegated): no; it only stops producing them, and unit 2 treats a schema-1 role as untrusted. A
  migration would rewrite records describing an install this unit cannot inspect.
- **F3 — the declared-absence blocks in this diff, or a grace period?** RESOLVED (agent, 2026-08-16,
  delegated): in this diff. A grace period is an undeclared absence by another name, and the arm that
  would enforce it later cannot tell a pending block from a forgotten one.

## 9. Revision log

- rev-4 · 2026-08-16 · folded the M4 spec audit, which returned BLOCKED over the whole set with four
  blockers landing here. The reduction key was spelled two ways in one document — destination in §4
  and source in S1 — and the flagship criterion asserted a role the stated key could not elect;
  precedence is now TWO operations with two keys, and the worked example is in §4. F1 is RE-RESOLVED
  as a consequence: a landable `project-owned` would have won zero destinations after S3, so the role
  stays a source-level carve-out and S2 no longer widens the landable set. AC2's liveness half was a
  state a TOML array of tables cannot express and is replaced by a resolver mutation. The hard-order
  step ids are enumerated in §4 with an owning unit each, and §3 now names ALL FOUR ordering clauses
  as vacuous after this unit rather than promising a list it did not carry. AC8 was rewritten: its
  fixture could not reach the state it graded, and it collided with unit 5's integrity arm.
- rev-3 · 2026-08-16 · M3 fork sweep: F1, F2 and F3 resolved in place under the owner's
  execute-the-build delegation. F1 was checked against M3's veto 3 and passes, because §5 already
  prices the widened write surface in this unit's own risk tier.
- rev-1 · 2026-08-16 · initial draft, as a single unit covering the update verb, a convergence
  ratchet and the prerequisite repairs. Grounded by driving `govkit` end to end into a throwaway repo
  and by comparing the descriptor leg declarations against the leg manifest.
- rev-2 · 2026-08-16 · the owner put finishing the deployer IN scope, and a twelve-agent audit and
  adversarial pass returned BLOCKED on all three lenses with ten blockers. The largest was structural:
  specced as one body of work the combined scope produced two incompatible gate-runner declarations,
  two check-state vocabularies, three step-id grammars and four receipt schemas — this repo's named
  core defect, inside the design meant to close it. This spec is narrowed to the substrate the other
  six units dispatch on, and the build gains six siblings with a written order. Three measured
  findings were folded in that rev-1 did not have: rule precedence does not exist and writes a
  `project-owned` file the operator authored; thirteen rules leave the land loop with no message and
  an adopter's non-zero exit is swallowed; and `check` emits one string for both "nothing was
  measured" and "measured and broken". The receipt is frozen here rather than in each consumer.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the resolver and the receipt. The lookup returned
`govkit.py`'s own symbols and no external seam, which is the honest answer: this unit's work is inside
one file. Four internal seams are extended rather than duplicated, and one external precedent is
copied deliberately.

`rule_sources` and `rule_destinations` are the expansion S5 unifies; the land loop's own inline
expansion is the second spelling being deleted, not a third being added.

`blob_at` stays the only reader of the gov index and gains no caller here.

`version_from = { none = "<reason>" }` and its refusal text are copied verbatim in shape for
`[check] = { none = "<reason>" }`. That is deliberate reuse of a decided question — declared absence
with a reason, refused when empty — rather than a new convention, and the refusal's own sentence about
silence not being a third option applies unchanged.

`selfcheck`'s derived-`mutates_index` arm is the template for AC9's step-tuple arm: derive the fact
from the artifact, assert it against the declaration, never trust the declared value.

`selftest.py`'s scratch-gov fixture builder is the harness for AC2's liveness half; it already
constructs a throwaway gov tree with a registry and a descriptor, so a descriptor with an impossible
overlap is a small variation rather than a new builder.

No seam exists for the receipt's schema-versioned reader, and it is small. The `written` boolean and
the per-role row table are new data, not new machinery.
