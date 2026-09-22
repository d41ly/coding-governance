# TOOL-aUnmannedHelm-1 — the run-state file, and the hygiene contract that admits it

**Status:** CLOSED · rev-5 · 2026-08-10 · node a · Tier-2 · base e7ec3365 · streams tooling · ratified 2026-08-10 · review wf_077104e6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-10-review-TOOL-aUnmannedHelm-1-1.md](../reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-1.md) | spec-audit | — |
| [2026-08-10-review-TOOL-aUnmannedHelm-1-2.md](../reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-2.md) | diff-review | TOOL-aUnmannedHelm-4 TOOL-aUnmannedHelm-5 TOOL-aUnmannedHelm-6 TOOL-aUnmannedHelm-7 TOOL-aUnmannedHelm-8 TOOL-aUnmannedHelm-9 |

<!-- /gen:spec-records -->

## 1. Goal

Make `RUN.md` a legal, gated citizen of a build folder, so an unattended run has one durable place
to record what only it knows. This is unit 1 of seven; the master scope and the ratified decision
menu live in this build's `README.md`, per `memory/TEMPLATE-SPEC.md`. Every other unit consumes the
contract defined here, which is why it is specced first and alone.

The file is illegal today. Hygiene check 4 whitelists exactly `README.md`, `STATUS.md` and four
directories at a build-folder root; a fixture run through the real engine reds with
`HYGIENE check 4 FAILED — build-folder naming/shape`.

## 2. Scope (IN)

- **S1 · the whitelist entry.** Admit `RUN.md` at a build-folder root in
  `tools/memory-tree/check-memory-hygiene.sh`, and move the four places that state the build-folder
  shape in the same commit: `memory/HYGIENE.md`, `tools/memory-tree/HYGIENE.template.md`,
  `memory/README.md`, and `tools/memory-tree/adopt-memory-tree.sh`. The first two are the
  kit/dogfood parity pair; the second two are the review's finding that the shape is written in four
  places, not two.
- **S2 · the membership decision, per check.** `RUN.md` joins `index_set()`, which imports check 6's
  20480 B and 250-line caps. It is added to check 7's `ex7` exemption alongside `guides/`, because
  the mandate block is prose. It does NOT join check 8: the phase vocabulary is deliberately not the
  seven-token status vocabulary, and unit 4's leg owns validating it.
- **S3 · the version and the arms.** `KIT_MEMORY_TREE_VERSION` moves, because the verdict-epoch leg
  reds when a non-comment line of the engine moves without it. Each new refusal branch gets a
  positive assertion naming its own failure text in `check-memory-hygiene.test.sh`, and the
  `ARMS_FLOORS` entry for that gate is re-measured upward.
- **S4 · the file contract.** The marker-pair region split, the five authored facts, the anchor ban,
  and the rule that the authored half never restates a derivable fact.
- **S5 · the size budget and the spill rule.** A file designed to grow inside a 20480 B cap needs a
  stated budget and somewhere for the overflow to go.
- **S6 · the fixtures.** A red and a green case per new branch, run through the real engine before
  any of it is trusted.

## 3. Non-goals (OUT)

- **Rendering the generated region.** Unit 3's driver renders it; this unit defines its contract.
- **Validating the phase vocabulary.** Unit 4's leg owns it, following B1.
- **Asserting the mandate.** Unit 3's `--preflight` does that, and unit 4's leg checks reachability.
- **Teaching `gen_build_index.py` to expose the spec BASE.** B2 made the run BASE authored, so the
  generator needs no change and is not in this unit's file list.
- **Wiring `RUN.md` to the row-keyed merge driver.** The qualifying grammar is stated in §4 so the
  option stays open; the wiring waits for a second node demonstrably writing one `RUN.md`.
- **Retiring `STATUS.md`.** It stays the human overview.
- **Editing `agent-cap.js`, its test, its wired copy, or the review protocol's text.** All of it is
  `TOOL-aNumeralWarden-1`'s after the F2 fold. Two specs claiming one edit is how a half-applied
  change passes every gate.

## 4. Design

### Data model — the two regions

`memory/builds/<slug>/RUN.md`, split mechanically rather than by discipline:

- **Generated**, delimited by a marker pair and rendered by unit 3's driver, reusing
  `apply_region()`'s contract verbatim: exactly one open marker, exactly one close, close after
  open, replace the slice, never a whole-file regex. It carries the unit list and per-unit status,
  both of which `gen_build_index.py` already derives from build front matter and spec status
  headers. Unit 4's leg byte-compares it against a fresh render.
- **Authored**, carrying exactly five facts and nothing else.

### The five authored facts

Nothing in the tree derives any of them, which is the test for belonging here.

1. **The standing mandate, verbatim.** The input the whole run is a function of. Prose, so it is why
   `RUN.md` needs the check-7 exemption.
2. **The phase**, from a closed vocabulary that unit 4's leg validates, each claim carrying a
   git-checkable witness.
3. **The keepalive id**, recorded by `--preflight` from the value the agent hands it. Per B3 the
   scheduling and the reaping are the agent's, because the cron store is in-memory and session-
   scoped, reachable only through the agent's own tool calls and never from a script.
4. **Parked decisions**, each with the question, the options seen, and the reason the run refused. A
   bare "parked" is indistinguishable from "forgotten".
5. **The run's BASE sha.** B2: `gen_build_index.py` captures `base` in `HDR_RE` and drops it in
   `parse_spec`, so it is not derived; and with seven sub-specs there are seven per-unit bases, none
   of which is the run's branch base that `--preflight` pins once at run start. It is a runtime
   observation with no re-derivable source, so it is authored.

The prohibition on the authored half narrows accordingly: it must never restate a unit status, or a
**per-unit spec BASE**. Restating the run's own BASE is not possible, because nothing else holds it.

### The anchor ban

Check 13 files any anchor found inside `memory/builds/<slug>/` under that slug, so a dash row
reading `- <FAMILY>-<slug>-<seq> ·` inside `RUN.md` makes this build a claimant of that id.

Corrected at rev-4, against the engine rather than against this paragraph. Check 13 counts BUILD
FOLDERS, not definitions — `corpus_ids.py` says so in its own comment, because a decision-log row and
its spec's H1 anchor one id by design. A backlog row therefore defines an id and adds no folder, so a
`RUN.md` dash row naming its OWN build's id collides with nothing. What DOES collide is the row a
run-state file is most likely to write: a parked or dependency entry leading with another build's id,
which makes this folder a second claimant. The ban is unchanged and its reach is wider than stated —
it binds hardest on exactly the cross-build rows the authored region exists to hold.

Second correction: checks 13-16 are OFF outright when every pin in `.memory-tree.conf` is blank
(`armed()`). Measured while arming this — on a tree with no pin, `def_builds` held both slugs and
`--check` still returned 0 — so the fixture lives in its own scratch tree with `ORPHAN_ID_PIN` set,
and an arm written against the main fixture tree would have passed against a disabled check.

Authored rows therefore cite ids inline in prose and never lead with a dash or a pipe followed by an
id. Check 14 binds from the other side: a bare id may not appear before something anchors it, so a
unit is minted as a backlog row before `RUN.md` names it. A sha and a workflow id are safe on both
counts, being neither links nor grammar-recognised ids.

Check 2 binds too: no relative `.md` link may name a file that does not exist yet, so a planned unit
is named, never linked, until its sub-spec lands.

### The size budget and the spill rule

`index_set()` membership imports check 6's 20480 B and 250-line cap onto a file designed to grow.
The authored region is budgeted at 8 KB, and the protocol caps live parked entries; when the budget
is reached, the oldest parked entries spill into the build's own `build/` folder as a dated
recording, a name check 5's grammar already admits. The budget is stated here so unit 2's protocol
can enforce it and unit 4's leg can observe it.

### Why not check 8

Check 8 demands exactly one of `OPEN SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO` on any
bullet or pipe row naming an id. The phase vocabulary is deliberately a different closed set,
because `CLOSED` in the spec vocabulary already means "built AND landed" and there is no token for
"built and reviewed, not yet merged" — the exact gap `aPrunedCeremony` invented `## Closing` and a
bare `STATUS:` line for, both of which rotted. Joining check 8 would either red the mandate and
parked rows or force the phase enum back onto the vocabulary that cannot express the state. B1
resolves it by leaving phase validation to the kit's own leg, which is also where the declaration
that F3 makes project-owned is validated.

### The precedent, restated

`memory/builds/aPrunedCeremony/STATUS.md` still reads `STATUS: IN-PROGRESS` with an open row for
deleting the watchdog cron, while the generated region of the same build's `README.md` correctly
reads `CLOSED · 6 unit(s)`. The authored half rotted and the derived half did not, in the one file
this build proposes to institutionalise. That is the whole argument for the mechanical split, and
`memory/gotchas/two-answers-to-one-question.md` is `universal: true`, so every reviewer of this diff
is asked about it by machine.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` and `check-memory-hygiene.test.sh`; `memory/HYGIENE.md`
and `tools/memory-tree/HYGIENE.template.md` in one commit; `memory/README.md`;
`tools/memory-tree/adopt-memory-tree.sh`; `.memory-tree.conf` for the re-measured `ARMS_FLOORS`
entry. Not touched: `gen_build_index.py`, `tools/hooks/agent-cap.js` and its test and wired copy
(`TOOL-aNumeralWarden-1` owns those), `tools/check-wiring.sh` (its eol population is derived from
`git ls-files` plus `git check-attr`, so unit 5's `.gitattributes` pin suffices).

### Alternatives rejected

- **A dated recording under `build/`.** Legal today with no kit change, but a resuming session
  cannot compute the filename of a file written three days ago, so there is no stable resume target.
- **Reusing `STATUS.md`.** Zero kit change, but it makes one file answer two questions, and the kit
  calls `STATUS.md` a human overview required only when the build is large.
- **Outside `memory/` entirely.** Escapes every hygiene check, including the ones that would have
  caught its rot, and lands in a `PRODUCT_GLOBS` path, which changes what the drift oracle reads.
- **Keeping the BASE in the generated region.** It is not derived, and seven sub-specs give seven
  per-unit values, none of which is the run's.

## 5. Production-readiness checklist

- **security** — N/A for this unit; it changes a gate's whitelist and a file contract, and adds no
  write path. Unit 3 owns the write guards.
- **perf / scale** — the engine change is a whitelist entry and one exemption; no measurable cost.
  The bar measures **239 s at `b476a55` on node a**, 39 of 39 with one skipped. That is the
  re-runnable baseline; the 213 s figure carried at rev-2 had no in-tree source and was stale.
- **a11y · i18n** — N/A.
- **error / empty / loading states** — every new refusal names its own message, never the exit code,
  because exit 1 is shared by every branch of this engine.
- **observability** — `RUN.md` is the observable; unit 3's `--status` reads it.
- **risks** — the dominant one is two answers to one question if the authored half drifts into
  restating a derivable fact. Second: a growing file inside a fixed cap, addressed by the spill rule.
- **testing + left-shift gates** — red and green fixtures per branch through the real engine, plus
  the arms obligation on each new `fail`.
- **migration / rollback** — additive. No existing build folder is required to grow a `RUN.md`, and
  the whitelist entry reverts independently.
- **user docs** — the four shape-stating sites move together, which is the whole of this unit's doc
  surface.

## 6. Acceptance criteria

- **AC1** — When a build folder holds a `RUN.md`, `bash tools/run-gates.sh` is green. When the same
  file is renamed to a name matching neither the whitelist nor the dated-recording grammar, for
  example `RUNSTATE.md`, hygiene check 4 reds with `HYGIENE check 4 FAILED — build-folder
  naming/shape` naming the file. Both states observed.
- **AC2** — When a `RUN.md` exceeds 20480 B or 250 lines, check 6 reds naming it; at the budget it
  is green. When the authored region carries a mandate line longer than 300 characters, check 7 is
  silent, because the `ex7` exemption covers it. All three observed.
- **AC3** — When a `RUN.md` authored row leads with a dash and an id, check 13 reds on the duplicate
  claimant; when the same id is cited inline in prose, it is green. Both observed.
- **AC4** — When the authored region restates a unit status or a per-unit spec BASE, unit 4's leg
  reds naming the field. Restating the run's own BASE is not reachable, and the fixture proves the
  ban does not fire on it.
- **AC5** — When `KIT_MEMORY_TREE_VERSION` is left unmoved while a non-comment line of
  `check-memory-hygiene.sh` moves, the verdict-epoch leg reds; moving the constant clears it.
- **AC6** — When any new `fail` branch's positive assertion is deleted from
  `check-memory-hygiene.test.sh`, `check-arms.py` reds naming that branch, and the re-measured
  `ARMS_FLOORS` entry for the gate is at or above the branch and armed counts.
- **AC7** — When a build folder carries no `RUN.md`, every leg is green and silent. A young tree is
  not a violation, and this case is armed explicitly so the guard's own false-red is pinned.

## 7. Gates

The standing bar, `bash tools/run-gates.sh`. Newly relevant existing legs for this unit: memory
hygiene, the verdict-epoch leg, kit/dogfood parity for the `HYGIENE` twins, `check-arms.py`, the
hygiene engine's own self-test, and `tools/memory-tree/hygiene-parity.test.sh`, whose baseline floor
derives from the kit version this unit moves. The manifest ratchet applies because
`.memory-tree.conf` is on its watch list, so `last-audit` re-stamps with a delta line.

Before the review of this unit's diff, run
`python tools/memory-tree/gotchas.py --for-diff <base>..<head>`; it emits
`two-answers-to-one-question` unconditionally, which is the class this unit is most exposed to.

**Build-wide constraint this unit inherits:** the drift signal
`non_terminal_specs_cited_by_product_source` measures 2 against a pin of 2, with zero headroom. No
file under `tools/`, `skills/`, `.claude/`, the playbook template, its two companions, or
`WIRE-INTO-PROJECT.md` may cite this build's own ids while the owning sub-spec is non-terminal.
`memory/` is deliberately outside that glob set, so records may cite freely.

## 8. Open questions

none

Two forks were raised by the Tier-2 review and both are resolved; they are kept below as the record
of what was decided. The leading token is what check 12 reads on a terminal spec — it accepts only
`none`/`N/A` there, and the "fully RESOLVED" alternative `TEMPLATE-SPEC.md` documents is not
implemented (`TOOL-aCandidStub-3`). The build-level decision menu is in this build's `README.md`.

### B1 — what does `RUN.md` join in the hygiene engine?

RESOLVED (owner, 2026-08-10): the check-4 whitelist and `index_set`, with a check-7 exemption
alongside `guides/`; NOT check 8. The unattended leg owns phase-vocabulary validation. Rejected: a
check-4-only entry, which would make the kit's own leg re-implement a working size cap; and full
membership with the phase enum collapsed onto the seven-token vocabulary, which loses the
built-but-not-landed state.

### B2 — where does the run's BASE sha live?

RESOLVED (owner, 2026-08-10): the authored region, as the fifth underivable fact. Rejected: teaching
`gen_build_index.py` to render the base it currently discards, which does not answer which of seven
per-unit bases is the run's; and a driver-owned state file, which adds a second state location no
hygiene check watches.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, as the master spec for all seven units. Grounded on a
  five-lens reconnaissance plus two direct measurements on node a: the `PreToolUse` payload keys,
  and a four-call burst proving hook processes overlap and a read-then-decide counter miscounts.
- rev-2 · 2026-08-10 · all five owner forks ratified. F2 went against the recommendation, so the
  agent-cap half moved to `TOOL-aNumeralWarden-1` and this build gained a dependency on it.
- rev-3 · 2026-08-10 · folded the Tier-2 review, 50 confirmed findings at precision 0.88. Four
  decision-shaped findings ratified by the owner. Restructured per B4: the master scope and the
  decision menu moved to this build's `README.md` as `memory/TEMPLATE-SPEC.md` directs, and this
  file narrowed to unit 1. B1 resolves the check-8 collision, B2 gives the run BASE a legal home,
  B3 splits the keepalive by actor in unit 2, and the stale agent-cap file list is gone with the
  units it belonged to. Corrected here: the four shape-stating doc sites, AC1's fixture, the 239 s
  bar baseline, and §10's characterisation of the nine `unattended` files.
- rev-4 · 2026-08-10 · BUILT, on the unit branch, unmerged — hence INPROGRESS rather than CLOSED,
  which this spec's own §4 defines as built AND landed. Engine at kit memory-tree@2.3: `RUN.md` in
  check 4's whitelist, in `index_set()` and in `ex7`; NOT in check 8. Four doc sites moved in one
  commit. Self-test 120 -> 130 assertions. Two §4 claims were corrected by running the predicate
  before trusting it, per the standing trap: check 13 keys on BUILD FOLDERS rather than on
  definitions, and checks 13-16 are disabled outright when every pin is blank, which would have left
  the anchor arm passing against a switched-off check. No new `fail` branch was added, so
  `ARMS_FLOORS` stays 14:14 — S3's re-measurement is vacuous here rather than skipped, and
  `check-arms.py --check` is green.

- rev-5 · 2026-08-10 · LANDED on `main` in the merge commit that closes this build. CLOSED in this tree's vocabulary means built AND landed, which is true from the moment that commit exists; the push publishes it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "unattended autonomous session driver with status file
and watchdog"` returns no seam. The closest hits are `derive_status` in `gen_build_index.py` and
`signal_spec_status` in `drift_report.py`, both fan-in 0, and no affordance seam matches.

A tree-wide grep for `unattended` over tracked files hits nine. The rev-2 characterisation of them
was wrong and is corrected: five are records of past runs, two carry the drift-audit skill's own
unattended trigger, and two state the rule that a session-scoped mode must report rather than
rewrite. Whether unit 3's `--close` reuses the drift-audit skill's trigger is unit 3's decision to
record, not this unit's.

The seams this unit wires through rather than reinvents:

- `gen_build_index.py` `apply_region()` — the generated-region splice contract, reused verbatim.
- `gen_build_index.py`'s derivation — the unit list and per-unit status come from the two sources it
  already reads; the driver renders, it does not re-derive.
- `check-memory-hygiene.sh` `index_set()` and `ex7` — the caps and the prose exemption are joined,
  not re-implemented, and `guides/` is the precedent for both halves.
- `check-memory-hygiene.sh` `pop_guard` — the empty-population precondition, in the two-granularity
  form the engine actually uses rather than the inverted one carried at rev-2.
- `memory/builds/aPrunedCeremony/STATUS.md` — the hand-rolled precedent this unit replaces, and the
  evidence for the mechanical split.
