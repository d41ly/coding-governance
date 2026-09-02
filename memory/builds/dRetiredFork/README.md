---
slug: dRetiredFork
node: d
opened: 2026-09-02
streams: tooling+deployer
roster: TOOL+DEPL
ids: DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18
---

# dRetiredFork — gov stops generating the forks, and takes back the fixes its adopters hold

## The problem this build exists to solve

Two adopters declare 44 forks of gov's own kit files. Classified against gov's bytes, five are
genuine and three of those five are misfiled. The rest belong to gov: fourteen are gov spelling
`tools/` into bytes it ships, eight are gov defects an adopter fixed privately and never sent back,
and the remainder are checkers with no way to be told what to scan and numbers with no owner.

`derive_carry_rung` at `tools/govkit/govkit.py:5135` already reconciles a pure repath with no
operator turn. It absorbs zero of NicoCares' nineteen forks, because whole-file equality decides a
rung and every `nc carve-out N/20` comment an adopter wrote to document a repath is the residual
byte that defeats it. So a kit pull is a build, not a command: the last one at inCMS was a
twelve-unit spec at rev-4 to move two kits by one minor version each.

## Expected improvements

- `govkit update --write` becomes the whole update at both adopters, because nothing is left for a
  person to merge.
- Fourteen path forks reconcile automatically, and the literals that generate them stop shipping.
- gov gains eight fixes it does not have today, each found by a tree that could not send it back.
- Two of NicoCares' 41 gate legs exist only to police the freeze and can retire.

## Detriments if this is not built

- The fork surface grows at gov's own commit rate, a median 29 commits a day on the deployable
  surface, so each release manufactures carve-outs faster than any adopter drains them.
- Seven known gov defects stay live in gov and in every future adopter, and an eighth claim stays
  unreconciled against a shipped fixture that contradicts it.
- inCMS stays un-updatable by any command, its receipt refusing before it classifies a row.

## Build-level rules

- **Every absorption lands as its own unit.** M2's one-mechanism rule, applied literally: nine
  separable upstream fixes are nine units, because a closing diff cannot attribute a finding
  otherwise.
- **A path fix is a DERIVATION or a RENDER, never a new config key.** A key cannot be read by an
  adopter whose installed kit predates it, and both adopters are 164 commits behind.
- **Deleting a population filter is refused.** Measured: `tools/workflows/check-review-join.sh:56`
  and `check-verifier-fanout.sh:45` apply no marker filter, so dropping `grep -E '^tools/.*\.js$'`
  widens review-join's population from 7 files to 10 and pulls in `agent-cap.js`, whose own ban
  table trips the predicate. Basename anchoring is the form; filter deletion reds the bar.
- **Every absorbed fix must be behaviour-preserving in gov's own tree**, proven by running the
  affected leg before and after, not asserted.
- **No new bar leg without its wall-clock ceiling and its `memory/project/testsuite-count-waivers.txt`
  row.** `tools/check-testsuite-counts.sh` derives its population from `tools/gate-legs.json`.
- **A kit self-test may not be added to the bar.** Owner ruling of 2026-08-23, restated in `AGENTS.md`.
- **The authoring rule does not land in the charter template.** Measured 2026-09-02: 48867 of 49152
  bytes, 285 free, already WARN past its recorded high-water. It lands in `tools/hooks/README.md`
  and `AGENTS.md`.
- **Never absorb an adopter's fix without reproducing it at HEAD first.** Spec-audit round 1 was
  BLOCKED on six findings; one measured a unit's whole premise inverted. All six are folded at rev-2.

## Parked decisions

- **The fan-out cap stays a file constant, and the ground is thinner than it looks.** The only
  carrier is `tools/hooks/README.md:96` — "`AGENT_CAP` in the environment is REFUSED, not honoured —
  the bound is a file constant" — which is a kit README, not a ratified record in
  `memory/DECISIONS.md`. A declared bound also serves one adopter only, since inCMS's cap is 5.
  `TOOL-dRetiredFork-14` halves the carrier count without touching the number. Whether the number
  itself may become a key is an OWNER TURN, not a settled refusal, and is parked as one.
- **swydee is deferred, and the measurement inverts its priority.** Of its 35 differing kit files, 32
  are byte-identical to some gov vintage — drift, not divergence — and only three diverge at all. It
  has no receipt, which makes it the cleanest available proof that a foreign prefix works. Onboarding
  it is a follow-up build, not a unit here.
- **inCMS's `gen_build_index.py` is misfiled, not forked.** gov's file is 2519 lines with 59 defs,
  inCMS's 518 with 14, and they share three symbol names. There is no upstream file to converge on.
  Reclassifying that registry row is `DEPL-dRetiredFork-7`; rewriting either program is not in scope.
- **The three `role = "forked"` memory-recall sources are untouched.** The direction is
  gov-from-target and the role is report-only in both directions by ratified design. The two
  registers disagree about them, which `DEPL-dRetiredFork-7` records rather than resolves.
- **Doing nothing was priced and is not recommended, but it is not absurd.** Four weeks since the pin
  produced one incident, a 1.11/1.12 version skew, caught by a gate NicoCares already runs.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 0 | `TOOL-dRetiredFork-18` | 1 | the build-index gap lines call the wrap helper written for them |
| 1 | `TOOL-dRetiredFork-1` | 1 | memory-tree arms `pop_guard` on check 6, as it already does on eight siblings |
| 1 | `TOOL-dRetiredFork-2` | 1 | the git-environment leak, one defect at two legs, stops reaching a subprocess |
| 1 | `TOOL-dRetiredFork-3` | 2 | a build README header that is present and unparseable stops reading as absent |
| 1 | `TOOL-dRetiredFork-4` | 1 | an adopter's fail-open claim is reconciled against a fixture that contradicts it |
| 1 | `TOOL-dRetiredFork-5` | 1 | four codebase-map selftest arms stop printing "NOT a pass" and being stamped ok |
| 1 | `TOOL-dRetiredFork-6` | 2 | the drift-audit note is DERIVED from its counters instead of hand-written |
| 1 | `TOOL-dRetiredFork-7` | 2 | the review join gains the dead-agent-wave arity arm |
| 1 | `TOOL-dRetiredFork-8` | 2 | check-wiring resolves the settings file instead of spelling one path |
| 1 | `TOOL-dRetiredFork-9` | 1 | a `_`-prefixed subfolder of `spec/` is not a spec, and C21 batches its greps |
| 2 | `TOOL-dRetiredFork-10` | 2 | three workflows gates anchor their locator and population on a basename |
| 2 | `TOOL-dRetiredFork-11` | 1 | `.githooks/pre-push` derives its install prefix instead of spelling it |
| 2 | `TOOL-dRetiredFork-12` | 2 | `playbook.fixture.md` becomes `rendered`, so the suite above it can follow a variable |
| 3 | `TOOL-dRetiredFork-13` | 1 | the `KIT_REL` default reaches the remaining test and selftest surface |
| 4 | `TOOL-dRetiredFork-14` | 2 | one hook copy is shipped and wired, not two |
| 5 | `TOOL-dRetiredFork-15` | 2 | five memory-tree values a project owns become declared keys |
| 5 | `TOOL-dRetiredFork-16` | 2 | a project adds a check without editing a kit engine |
| 9 | `TOOL-dRetiredFork-17` | 2 | the authoring rule, and the gate that turns the carried-literal ratchet into a ban |
| 2 | `DEPL-dRetiredFork-7` | 2 | the undeclared-fork census, and the ledger contract both adopters need |
| 6 | `DEPL-dRetiredFork-1` | 2 | the carry map stops dropping a gov directory that fans into two destinations |
| 6 | `DEPL-dRetiredFork-2` | 2 | `update` lands a gov source that has no receipt row |
| 6 | `DEPL-dRetiredFork-4` | 1 | the lf-pin pathspec goes over stdin, so a large adopter stops crashing |
| 6 | `DEPL-dRetiredFork-5` | 1 | `check` runs the `[[outcome]]` probe instead of grading on an exit code |
| 7 | `DEPL-dRetiredFork-3` | 2 | `update` re-runs the adopters, renderers and generators it invalidates |
| 8 | `DEPL-dRetiredFork-6` | 2 | `govkit contribute` — the route by which an adopter's fix becomes gov's |

The `#` column is the `order` verb each spec declares. Units sharing a value are the parallel group.
Order 1 is nine independent absorptions that need no design decision and no key; order 2 begins only
after `DEPL-dRetiredFork-7` has measured what the two registers do not declare, because a sweep that
retires a fork nobody counted cannot be verified.

**The build is done when `govkit update --write` is the whole update at both adopters.** That is one
observation, not a tally: a run that lands every stale row, re-renders every rendered row, re-runs
every invalidated generator, re-stamps `gov_commit`, and leaves nothing for a person to merge.

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 25 unit(s) · node d · opened 2026-09-02 · streams tooling+deployer
ids DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7
ids TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRetiredFork-18 — the gap lines use the wrap helper written for them](spec/2026-09-02-spec-TOOL-dRetiredFork-18.md) | 0 | 1 | INPROGRESS | rev-1 | 2026-09-02 |
| [TOOL-dRetiredFork-1 — memory-tree arms `pop_guard` on check 6](spec/2026-09-02-spec-TOOL-dRetiredFork-1.md) | 1 | 1 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-2 — the git-environment leak, one defect at two legs](spec/2026-09-02-spec-TOOL-dRetiredFork-2.md) | 1 | 1 | OPEN | rev-1 | 2026-09-02 |
| [TOOL-dRetiredFork-3 — a present-but-unparseable build README header stops reading as absent](spec/2026-09-02-spec-TOOL-dRetiredFork-3.md) | 1 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-4 — reconcile inCMS's agent-cap fail-open claim against HEAD](spec/2026-09-02-spec-TOOL-dRetiredFork-4.md) | 1 | 1 | OPEN | rev-3 | 2026-09-02 |
| [TOOL-dRetiredFork-5 — four codebase-map selftest arms stop being stamped ok](spec/2026-09-02-spec-TOOL-dRetiredFork-5.md) | 1 | 1 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-6 — the drift-audit note is DERIVED from its counters](spec/2026-09-02-spec-TOOL-dRetiredFork-6.md) | 1 | 2 | OPEN | rev-1 | 2026-09-02 |
| [TOOL-dRetiredFork-7 — the review join gains the dead-agent-wave arity arm](spec/2026-09-02-spec-TOOL-dRetiredFork-7.md) | 1 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-8 — check-wiring resolves the settings file instead of spelling one path](spec/2026-09-02-spec-TOOL-dRetiredFork-8.md) | 1 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-9 — `_`-prefixed spec subfolders, and C21's batched greps](spec/2026-09-02-spec-TOOL-dRetiredFork-9.md) | 1 | 1 | OPEN | rev-1 | 2026-09-02 |
| [DEPL-dRetiredFork-7 — the undeclared-fork census, and the ledger contract](spec/2026-09-02-spec-DEPL-dRetiredFork-7.md) | 2 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-10 — three workflows gates anchor their locator and population on a basename](spec/2026-09-02-spec-TOOL-dRetiredFork-10.md) | 2 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-11 — `.githooks/pre-push` derives its install prefix](spec/2026-09-02-spec-TOOL-dRetiredFork-11.md) | 2 | 1 | OPEN | rev-1 | 2026-09-02 |
| [TOOL-dRetiredFork-12 — `playbook.fixture.md` becomes `rendered`](spec/2026-09-02-spec-TOOL-dRetiredFork-12.md) | 2 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-13 — the `KIT_REL` default reaches the remaining test and selftest surface](spec/2026-09-02-spec-TOOL-dRetiredFork-13.md) | 3 | 1 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-14 — one hook copy is shipped and wired, not two](spec/2026-09-02-spec-TOOL-dRetiredFork-14.md) | 4 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-15 — five memory-tree values a project owns become declared keys](spec/2026-09-02-spec-TOOL-dRetiredFork-15.md) | 5 | 2 | OPEN | rev-1 | 2026-09-02 |
| [TOOL-dRetiredFork-16 — a project adds a check without editing a kit engine](spec/2026-09-02-spec-TOOL-dRetiredFork-16.md) | 5 | 2 | OPEN | rev-2 | 2026-09-02 |
| [DEPL-dRetiredFork-1 — the carry map stops dropping a gov directory that fans into two destinations](spec/2026-09-02-spec-DEPL-dRetiredFork-1.md) | 6 | 2 | OPEN | rev-2 | 2026-09-02 |
| [DEPL-dRetiredFork-2 — `update` lands a gov source that has no receipt row](spec/2026-09-02-spec-DEPL-dRetiredFork-2.md) | 6 | 2 | OPEN | rev-3 | 2026-09-02 |
| [DEPL-dRetiredFork-4 — the lf-pin pathspec goes over stdin](spec/2026-09-02-spec-DEPL-dRetiredFork-4.md) | 6 | 1 | OPEN | rev-2 | 2026-09-02 |
| [DEPL-dRetiredFork-5 — `check` runs the `[[outcome]]` probe instead of grading an exit code](spec/2026-09-02-spec-DEPL-dRetiredFork-5.md) | 6 | 1 | OPEN | rev-1 | 2026-09-02 |
| [DEPL-dRetiredFork-3 — `update` re-runs the adopters, renderers and generators it invalidates](spec/2026-09-02-spec-DEPL-dRetiredFork-3.md) | 7 | 2 | OPEN | rev-3 | 2026-09-02 |
| [DEPL-dRetiredFork-6 — `govkit contribute`, the route by which an adopter's fix becomes gov's](spec/2026-09-02-spec-DEPL-dRetiredFork-6.md) | 8 | 2 | OPEN | rev-2 | 2026-09-02 |
| [TOOL-dRetiredFork-17 — the authoring rule, and the gate that turns the ratchet into a ban](spec/2026-09-02-spec-TOOL-dRetiredFork-17.md) | 9 | 2 | OPEN | rev-2 | 2026-09-02 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 0 | `TOOL-dRetiredFork-18` | no |
| 1 | `TOOL-dRetiredFork-1`, `TOOL-dRetiredFork-2`, `TOOL-dRetiredFork-3`, `TOOL-dRetiredFork-4`, `TOOL-dRetiredFork-5`, `TOOL-dRetiredFork-6`, `TOOL-dRetiredFork-7`, `TOOL-dRetiredFork-8`, `TOOL-dRetiredFork-9` | yes |
| 2 | `DEPL-dRetiredFork-7`, `TOOL-dRetiredFork-10`, `TOOL-dRetiredFork-11`, `TOOL-dRetiredFork-12` | yes |
| 3 | `TOOL-dRetiredFork-13` | no |
| 4 | `TOOL-dRetiredFork-14` | no |
| 5 | `TOOL-dRetiredFork-15`, `TOOL-dRetiredFork-16` | yes |
| 6 | `DEPL-dRetiredFork-1`, `DEPL-dRetiredFork-2`, `DEPL-dRetiredFork-4`, `DEPL-dRetiredFork-5` | yes |
| 7 | `DEPL-dRetiredFork-3` | no |
| 8 | `DEPL-dRetiredFork-6` | no |
| 9 | `TOOL-dRetiredFork-17` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
