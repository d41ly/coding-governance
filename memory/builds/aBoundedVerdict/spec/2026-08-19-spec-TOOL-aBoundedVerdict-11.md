# TOOL-aBoundedVerdict-11 — the units region becomes generated, mandatory, and read by name

**Status:** SPECCED · rev-2 · 2026-08-19 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

The unattended driver decides "is this build finished" by selecting rows out of a shared markdown
region by their SHAPE, and a sibling kit began rendering a second table into that same region on
2026-08-17 — so every review and journal record now counts as an unfinished unit. Give the units
table a marker pair of its own, render it, require it, and make all three consumers read it by name
instead of by row shape.

## 2. Scope (IN)

- **S1** — `gen_build_index.py` renders the Units table inside its own `<!-- gen:build-units -->`
  pair, nested within the existing `gen:build-index` region so no slot order changes. The Records
  table stays where it is; what changes is that the units table is now addressable.
- **S2** — one helper in `unattended.sh` returns unit rows from that named region, and the three
  call sites that today spell the shape selector independently — `unit_rows` (`:913`), the
  `units-at-landing` freeze (`:1078`) and the "next non-terminal unit" line (`:1339`) — all route
  through it. Three spellings of one question become one.
- **S3** — the helper refuses a malformed or absent pair with a NAMED refusal rather than falling
  through to an empty selection. `region` exits 3 for absent and for malformed alike, and this kit
  has already paid once for reading that single status as "absent".
- **S4** — the region is REQUIRED for a build an unattended run may close, and the requirement is
  enforced where an agent meets it rather than only in a comment: `--preflight` refuses a build
  whose README carries no well-formed pair, naming the render command that creates one.
- **S5** — a corpus migration pass: every tracked build README gains the pair by re-render, and the
  gate leg gains a check that every build README carries exactly one well-formed pair.
- **S6** — the owner's ratified resolution for the authored `roster:units` pair: the frozen
  AUTHORIZATION scope stops being an authored region of a mutable file. `check_authorization`
  compares the **set of unit IDS** extracted from the generated units region in the BASE blob against
  the same set at HEAD, and requires the BASE set to be a SUBSET of the HEAD set — additions
  admitted, removals refused. It compares the id set and **not the row bytes**; rev-2 corrects rev-1,
  which said "refusing any row CHANGED", and §4 states why that would have refused every run that did
  any work.
- **S7** — the disarmed control is re-armed: one driver test arm has `build-complete` and
  `closing-review-recorded` BOTH met with no `--override` at all, over a fixture whose README is
  re-rendered and whose `reviews/` holds a tracked record.

## 3. Non-goals (OUT)

- **The authored `roster:units` pair is not deleted in this unit.** It keeps its meaning for the
  builds that carry one until the migration in S5 completes; retiring it is the follow-up the
  revision log names, and doing both in one unit makes the migration unreviewable.
- No change to the Records table's content, position, or the two coverage joins
  `TOOL-aTetheredRecord-5` added. This unit does not relitigate that unit's design; it gives the
  driver an address so the two kits stop sharing one selector.
- No change to `build-complete`'s five terms beyond the region they read. Their MESSAGES are
  `TOOL-aBoundedVerdict-12`'s scope, not this unit's.
- No new phase, no new DoD item, no change to the DoD floor.
- Not the `--status` output FORMAT. This unit makes the value correct; nothing about the line's
  shape changes.

## 4. Design

### Data model

One new nested marker pair. The units table moves inside it; nothing else moves.

```
<!-- gen:build-index -->
**Build status:** …
ids …
<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [<id> — <title>](spec/<file>) | CLOSED | rev-N | <date> |
<!-- /gen:build-units -->
| Record | Kind | Serves |
…
<!-- /gen:build-index -->
```

Nesting rather than a sibling region is deliberate: `GEN_REGIONS` is the canonical region order and
appending an entry registers a new region for both creation and rendering, which would put the units
table outside the region every existing reader already brackets. Nesting keeps `gen:build-index`
byte-identical in extent and gives the driver an inner address.

**Why not the `spec/` link discriminator.** The audit's proposed one-line fix —
`grep -E '^\| \[[^]]*\]\(spec/'` — is correct today and drops all 124 record rows while keeping all
173 unit rows. It is rejected as the PRIMARY mechanism for the reason this defect exists: it is a
third shape rule inferred from what the other kit's renderer currently emits, and the next table
that links into `spec/` re-opens the same hole silently. It is kept as the migration's transitional
reader (Rollout, below), where its blast radius is one release and its correctness is measurable
against the corpus it ships against.

### Why the comparison is over IDS and not over row bytes

Rev-1 specified a byte-level comparison admitting added rows and refusing changed ones. **That was
wrong, and measurably so.** The two regions do not have the same stability:

| region | a row looks like | moves when |
|---|---|---|
| authored `roster:units` | `\| 1 \| \`TOOL-X-4\` \| 2 \| mechanism \|` | someone hand-edits it |
| generated units region | `\| [TOOL-X-1 — title]` then a spec link, then `\| CLOSED \| rev-4 \| 2026-08-17 \|` | **any unit's status, rev or date changes** |

The authored region works as a frozen scope precisely because it carries no status, no rev and no
date. The generated one carries all three, rendered from each spec's status header — so building a
unit moves its row from `SPECCED · rev-1` to `CLOSED · rev-3` and re-renders the date. A byte-level
"no row changed" test would therefore refuse **every run that built anything**, on the
non-overridable item, which is strictly worse than the defect it replaces: it would convert
"unsatisfiable for a build carrying a roster" into "unsatisfiable for any build that does work".

The id SET is the right invariant because it is what the scope actually IS. Which units the run may
work on is frozen; everything else in a row — status, rev, date, title, the spec's filename — is
DERIVED from a document the run is authorized to edit, and freezing a derived value would freeze the
work itself. So: extract ids from both sides with the same extraction, require BASE ⊆ HEAD.

What this deliberately does not catch, stated rather than discovered later: a row whose id is
unchanged but whose spec LINK now points at a different file. That is a re-pointing rather than a
scope change, the title moves with the spec's own H1 for legitimate reasons, and including either in
the comparison reintroduces exactly the churn this correction removes.

### Inventory

| Concern | Today | After |
|---|---|---|
| how a unit row is identified | row shape, spelled 3× in one file | one named region, one helper |
| a second table in the region | counts as unfinished units | invisible to the driver |
| `build-complete` on a build with a review | cannot pass, 49/49 builds | passes when its units are terminal |
| `--status` next unit | may name a journal or a review record | names a unit or says there is none |
| `units-at-landing` | would freeze record filenames into a terminal record | freezes unit ids |
| the frozen authorization scope | an AUTHORED region of a mutable file, opt-in by presence | the generated region's unit-ID SET, BASE ⊆ HEAD |
| a build README with no units region | legal, and silently unclosable | refused at `--preflight`, with the render command named |

### Migration

Two populations, and they are not symmetric.

**The corpus (49 build READMEs).** `--write` CREATES a missing generated region pair and `--check`
never demands one, which is what lets the pair ship without re-rendering the corpus in the same
commit. So the migration is a single `--write` pass, and S5's leg check is what makes it permanent.

**The seven tracked run-state files.** Four are LANDED and two of those carry a `units-at-landing`
fact frozen BEFORE the regression reached their READMEs — both measured clean, six ids each, no
record filenames. So no terminal record needs repair, and this unit MUST NOT rewrite one: a frozen
fact is a record, and re-deriving it from today's README would replace an accurate answer with a
reconstruction. The three ABORTED records freeze nothing.

That asymmetry is the migration's whole risk surface, and it is why S6's comparison is specified as
BASE-blob against HEAD rather than against any recorded copy.

### Rollout

1. Render the pair and migrate the corpus (S1, S5's `--write` half).
2. Land the helper reading the named region, with the transitional `spec/` link fallback for a
   README not yet re-rendered — so a mid-migration tree is never selecting record rows.
3. Land the `--preflight` refusal (S4) and the leg check (S5), which together make the fallback
   unreachable.
4. Delete the fallback in the same unit, once the leg proves no tracked README needs it. A fallback
   that outlives its migration is the dual-spelling debt this repo already carries elsewhere.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` (the region and its `GEN_REGIONS` entry) ·
`tools/memory-tree/marker-contract.test.sh` (a fourth reader joins the case table) ·
`tools/unattended/unattended.sh` (the helper, three call sites, `--preflight`, `check_authorization`) ·
`tools/unattended/unattended.test.sh` (S7's re-armed control, plus arms per new refusal) ·
`tools/unattended/check-unattended.sh` + `.test.sh` (S5's check) ·
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (the roster
bullet stops reading opt-in) · `memory/map/features/build-readme-surface.md` and
`memory/map/features/unattended.md` (both dossiers claim this region) · 49 build READMEs by render ·
the two kit version constants · `.memory-tree.conf` (`ARMS_FLOORS`).

### Alternatives rejected

- **The `spec/` link discriminator alone.** Rejected as primary above; kept as the transitional
  reader with a stated deletion point.
- **Anchor on the `| Unit | Status |` header and stop at the blank line.** No marker to add, but it
  makes the driver depend on another kit's column NAMES, which is a weaker contract than its shape
  rule, not a stronger one.
- **Have the unattended kit call `gen_build_index.py` and read its structured output.** Correct in
  the abstract and rejected on the dependency: the unattended kit ships without the memory-tree kit
  today, and `tools/lib/` is gov-internal and ships nothing.
- **Keep the authored `roster:units` pair as the frozen scope and only fix the selector.** This is
  the minimal fix and it leaves the owner's ratified decision unimplemented, `build-complete`
  dependent on an undocumented hand-edit, and the promotion disposition still refused on any
  roster-carrying build.
- **Freeze the scope in the run-state file at `--preflight`.** Refused on
  `memory/gotchas/inputs-inside-the-subjects-reach.md`: that file is written by the run, so a scope
  frozen there is compared against bytes its subject supplied.

## 5. Production-readiness checklist

- **security** — S6 is the security-relevant half. The append-admitting comparison must refuse a
  CHANGED row, not merely detect a shorter list; a run that edits an existing unit's id or status
  and appends a row must be refused. Arm both directions.
- **perf / scale** — N/A. One extra `region` call per read, on files measured in kilobytes.
- **a11y** — N/A, no user surface.
- **i18n** — N/A.
- **error / empty / loading states** — the empty selection is the failure mode this unit exists to
  remove: a build with zero units must be a NAMED refusal and never an empty pass. `build-complete`'s
  term 4 already exists for that reason and its rationale is now load-bearing.
- **observability** — the refusals in S3 and S4 name the render command. A refusal that does not tell
  an unattended agent the repair verb is a stall.
- **risks** — the migration is a 49-file render; a partial migration is covered by the transitional
  reader. Rollback is the fallback reader plus reverting the helper. The concurrency risk is real and
  bounded by the build method's clause 3: this unit renders an artifact AND edits its generator, so it
  may not run concurrently with any pass that renders a build README.
- **testing + left-shift gates** — S5's leg check is the left-shift for the corpus half; S7's re-armed
  control is the left-shift for the item half. The class this defect belongs to
  (`two-answers-to-one-question`, one question spelled three times) is left-shifted by S2 collapsing
  the three spellings, which is a structural fix rather than a gate.
- **migration / rollback** — Migration and Rollout above.
- **user docs** — the protocol pair's roster bullet, and both map dossiers.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs over this corpus, every
  tracked build README carries exactly one well-formed `gen:build-units` pair, and
  `python tools/memory-tree/gen_build_index.py --check` is clean.
- **AC2** — When the driver's unit helper runs over `memory/builds/aBranchedMandate/README.md`, it
  returns 4 unit rows and 0 non-terminal, against the 13 and 7 the shipped `unit_rows` returns today.
- **AC3** — When `bash tools/unattended/unattended.sh --status aBranchedMandate` runs, the `next`
  field names a unit id or the literal no-non-terminal-unit text, and never a path under `build/`,
  `reviews/` or `prompts/`.
- **AC4** — When a fixture build has a tracked `reviews/` record naming its pinned base and all its
  units CLOSED, `--close` reports `close OK` with **no** `--override` argument — the arm S7 adds to
  `tools/unattended/unattended.test.sh`, which fails against the shipped driver.
- **AC5** — When a fixture README's `gen:build-units` markers are duplicated or transposed, the
  helper's caller prints the S3 refusal naming the file, and `--close` does not report the build
  complete.
- **AC6** — When `--preflight` runs against a build whose README carries no units pair, it refuses
  and its message contains `gen_build_index.py --write`.
- **AC7** — When a run appends a unit row to the generated region, `check_authorization` returns 0;
  when it DELETES one, it refuses. Two arms, both directions, in
  `tools/unattended/unattended.test.sh`.
- **AC7a** — When an existing unit's status moves `SPECCED` → `CLOSED` and its rev bumps, and the
  region is re-rendered by `python tools/memory-tree/gen_build_index.py --write`,
  `check_authorization` returns 0 — the arm that proves the comparison is over ids and not bytes, and
  the one that fails against rev-1's design.
- **AC8** — When `bash tools/unattended/check-unattended.sh` runs over a fixture tree holding one
  build README with no units pair, it reds naming that file; over the real tree it is clean.
- **AC9** — When `bash tools/memory-tree/marker-contract.test.sh` runs, its case table drives the new
  region through every live reader of the generated-region markers.
- **AC10** — When the two existing `units-at-landing` facts are compared before and after this unit,
  they are byte-identical — the migration rewrites no terminal record.

## 7. Gates

`bash tools/run-gates.sh` whole, and specifically: `memory/` hygiene (check 9's fresh-render
comparison over 49 READMEs) · `build README slot contract` · `tools/memory-tree/marker-contract.test.sh` ·
`unattended driver selftest` · `unattended kit gate` + its sibling test ·
`tools/memory-tree/kit-dogfood-parity.test.sh` and `tools/workflows/check-protocol-parity.test.sh`
(the protocol pair moves) · `harness arms` (`check-arms.py`, one arm per new `fail`) ·
`codebase-map coverage + freshness` (both dossiers claim the region) · `kit version markers` ·
`verdict epoch` (the hygiene engine is untouched, but the memory-tree kit version moves).

## 8. Open questions

- **F1 — does the units region nest inside `gen:build-index`, or become a sibling entry in
  `GEN_REGIONS`?** Nesting keeps every existing reader's bracket byte-identical and costs the
  generator a nested-render path it does not have today. A sibling entry is the generator's natural
  extension point and moves the units table OUT of the region three legs and two dossiers already
  describe, which is a corpus-wide re-read. **Recommendation: nest.** The cost is one generator
  path; the alternative's cost is every reader of the outer region.
  RESOLVED (agent, 2026-08-19, delegated): nest. Under §4's stated reason — the alternative moves a
  region that three legs and two dossiers bracket, and this fork's options differ in mechanism
  rather than in what gets built, so it is inside the delegated set.

- **F2 — does the transitional `spec/` fallback reader ship at all?** Shipping it makes a
  mid-migration tree safe and adds a dual spelling with a stated deletion point in the same unit.
  Not shipping it means step 2 of the rollout is only correct after step 1 has landed everywhere,
  which for a single-repo corpus is one commit. **Recommendation: ship it, delete it in step 4.**
  The corpus is one repo today, but the kit is deployable, and an adopter's tree migrates on their
  schedule rather than in our commit.

- **F3 — OWNER, not delegated. Does the authored `roster:units` pair get retired, and when?**
  This unit deliberately leaves it standing (§3). Retiring it removes the last authored-region
  dependency from the authorization path and invalidates nothing, because S6 replaces what it was
  for; keeping it means two regions can disagree about a build's scope, which is the class this
  build keeps finding. The options differ in what gets built, so §3's fork rule sends it to the
  owner rather than resolving it here.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's blocker 1·8·27 and from
  the owner's ratified resolution recorded in the design pass. F1 and F2 resolved under the
  delegated fork rule with their grounds stated; F3 raised to the owner as a scope fork.
- rev-2 · 2026-08-19 · **S6's comparison corrected from row bytes to the unit-ID SET, before any
  code was written.** Found by verifying rev-1's own claim against the two regions rather than
  assuming it: the authored region carries id, tier and a mechanism label and is stable across a
  build, while the generated region carries STATUS, REV and a last-change date rendered from each
  spec's header. A byte-level "no row changed" test over the generated region would have refused
  every run that built anything — on the one item `verb_close` will not override — which is a worse
  failure than the one this unit exists to fix. AC7 is split and AC7a is new: it re-renders a
  status-and-rev change and asserts the check still passes, which is the arm rev-1's design fails.
  The limit of an id-set comparison is stated in §4 rather than left to be discovered.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve a blocked review verdict and close an unattended
run"` returned `.unattended.conf` and `UNATTENDED-PROTOCOL.md` as affordance seams and no symbol-level
seam for region reading — the query was aimed at the review loop, not at region plumbing, and it is
recorded here as the SET-level pass the method asks for once.

The seam this unit extends is named from source rather than from that probe: **`GEN_REGIONS` in
`tools/memory-tree/gen_build_index.py`**, which `memory/map/features/build-readme-surface.md:87`
identifies as the canonical region order and the registration point for a new region. The dossier's
own Gaps section records the unwrapped-roster population this unit migrates, and states that making
the pair mandatory was deferred to `TOOL-cBriefedPilot-18` — **a stale deferral, verified here**:
that unit is CLOSED, its S12 made the roster required only in the PROTOCOL TEXT, and its AC9 claims a
grep for `Opt-in by presence` returns zero where it returns two. So the mechanism was unowned, which
is why this unit takes it rather than waiting on another node.

Recall terms used: `closing review round cap blocked verdict adversarial diff fold unattended close
build-complete DoD stall halt`.
