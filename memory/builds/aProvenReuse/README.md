---
slug: aProvenReuse
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-3 TOOL-aProvenReuse-4 TOOL-aProvenReuse-5 TOOL-aProvenReuse-6
authorized-by: prompt
---

# aProvenReuse — the reuse-first rule gets a machine half

## The problem this build exists to solve

`reuse-first` is a DIRECTIVE of every unattended run and it is enforced by nothing. `grep -n reuse`
over `tools/unattended/unattended.sh` returns exactly one hit — the handle's own name inside
`DIRECTIVES_CORE` — and over `tools/unattended/check-unattended.sh` it returns a comment about an
unrelated check. The kit's own Skill states the hole in as many words: *"Waiving it is SILENT: the
bar stays green over a build that skipped the reuse probes, because nothing machine-checks a spec's
reuse section for content."*

That is not a theoretical hole and this build did not have to guess at its size — but the size is a
DERIVED population, so this file does not carry its counts. AGENTS.md §7 is explicit: *"NO count of a
derived population is written in prose. The checker derives every figure it reports; a number typed
beside the thing it counts is wrong on the next commit and nobody notices."* An earlier revision
broke that rule and paid for it inside one session — round 2's F11 found this paragraph saying 346
while a rule added four paragraphs below said 348 for the same population, because the tree had
grown between the two measurements.

What was measured, and where the numbers live: **a majority of post-`SPEC10_CUTOFF` specs carrying a
§10 record no recall terms at all, and about half name neither probe.** `memory/guides/BUILD-METHOD.md`
M5 requires the terms by name, and M7's regrounding step 5 — *"Re-run the recall probe with the terms
recorded in that spec's §10"* — therefore resolves to nothing for most of the corpus. A method step
that cannot execute is a step nobody notices is missing. The exact figures, with the population each
is taken over and the date it was derived, are in
[`TOOL-aProvenReuse-1` §6 AC5](spec/2026-08-31-spec-TOOL-aProvenReuse-1.md) and in the two review
records, which is where a figure with a re-derivation instruction attached belongs.

Hygiene check 12 already parses every one of those §10 sections. It grades them on three things —
the heading is present, the body is non-empty, no skeleton placeholder survives — and on nothing
else, so `N/A — none` is a passing reuse audit. The owner's prose is the mandate and is recorded
verbatim under [prompts/](prompts/2026-08-31-prompt-TOOL-aProvenReuse-1.md).

## Expected improvements

- A spec dated at or after a declared cutoff cannot land claiming a reuse audit it did not record.
  Every spec that would fail the predicate today is grandfathered, exactly as `SPEC10_CUTOFF`,
  `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF` and `FORK_MARK_CUTOFF` already grandfather their own.
- M7 regrounding step 5 becomes executable for every spec written from here on.
- An unattended run that never ran a recall probe cannot reach `--close` silently. It can still
  override, but the override is recorded and reaches the wrap-up, which is the difference between a
  skipped check and an invisible one.
- Waiving `reuse-first` stops being silent. The waived run's `reuse-probed` line names the waiver
  and its reason instead of passing without comment.

## Detriments if this is not built

- Every future build keeps paying to rediscover seams the tree already has, which is the specific
  harm the owner's prompt names.
- The directive table keeps carrying a handle whose waiver changes nothing observable, so the
  waiver mechanism reports coverage it does not have.
- `reuse-first` remains the one directive in a 16-handle set whose satisfaction leaves no trace on
  disk, and a set with one unobservable member cannot be audited as a set.

## Build-level rules

- **Classification (M2), written before acting**: both units were MISSING at open — no conforming
  spec carried either id — and are authored by this run at **Tier 2**. An earlier revision of this
  line said Tier 1 and was corrected by the round-1 spec audit, findings 6 and 41. The tier is
  load-bearing rather than bookkeeping here: `check-memory-hygiene.sh` runs `if (hdr ~ /Tier-1/)
  next` before every section-body assertion, so under the Tier-1 reading unit 1's own predicate
  would grade a population of zero. Tier 2 is also what the kickoff manifest's tier rule assigns —
  each unit changes a kit's contract, and the pair is cross-kit.
- **Two mechanisms, two units, and the split is the tracked/local boundary.** Unit 1's evidence is
  a tracked file, so it belongs on the merge bar and works in any clone. Unit 2's evidence is a
  node-local log in the git common dir, so it belongs to the driver and could never be a bar leg.
  Putting both in one spec would make the closing diff unable to say which half a finding lands on.
- **The third gap found is deliberately NOT built, and the reason is M3 veto 2.**
  `tools/codebase-map/reuse_lookup.py` writes no log, while `tools/memory-recall/query.py` writes
  one — so of M5's two probes only one has liveness evidence available. Closing that asymmetry means
  either a cross-kit dependency (codebase-map reading a memory-recall convention) or a third
  telemetry format and a third kit version bump. It is not strictly beneficial, so protocol §11
  makes it a backlog row rather than an adoption.
- **Neither unit may red a landed spec — and "landed" includes other branches.** A predicate that
  reds 253 tracked files is not a gate, it is a migration nobody asked for, and the cutoff idiom is
  the whole reason this is landable. Round 1 found the rule broken by the build that wrote it: at a
  cutoff of this build's own date, 21 Tier-2 specs dated `2026-08-31` on three live sibling branches
  fail the predicate and would red `memory hygiene` on `main` the moment either side merges. The
  cutoff is therefore `2026-09-01`, which costs this build the ability to grade its own two specs.
  That trade is recorded in unit 1's §4 Migration rather than hidden here.
- **Two populations, and they are not interchangeable — which is the trap, not the arithmetic.**
  The ALL-TIERS figure counts every post-`SPEC10_CUTOFF` spec carrying a §10. The predicate only ever
  reaches the Tier-2 subset that survives check 12's `if (hdr ~ /Tier-1/) next`, which is smaller,
  and a criterion pinned to the larger one fails a correct implementation. Round 1 confirmed that
  confusion twice, findings 1 and 25; round 2's F11 then caught this very bullet introducing a
  SECOND denominator for the larger population, two days of tree growth apart. Both figures are
  therefore derived where they are used and stated nowhere else.

## Review rounds

**The loop exited NON-CONVERGENT, and how its standing blockers were dispositioned is recorded here
because M4 requires an abnormal exit to reach this slot rather than only a transcript.** Round 1 and
round 2 each confirmed exactly 4 blockers. The rule re-arms a round only on a STRICTLY SMALLER count,
so `--review` returned `NON-CONVERGENT — the loop STOPS here and every blocker still standing is
PROMOTED to a unit of this build`. There was no round 3.

**Every round-2 blocker was folded into the spec it belongs to rather than promoted to a unit, and
that is a judgement this run made rather than a rule it followed.** The reason: M2's decompose rule
is one MECHANISM per spec, and none of F1–F4 is a mechanism. F1 is a stale fork resolution, F3 an
acceptance criterion that cannot pass, F4 an unnamed operand; F2 is a scope addition to unit 1's own
mechanism — a shell-side default the rev-2 edit had dropped. Promoting a non-mechanism would create a
unit M2 forbids, whose spec would then need an audit, which is the regress the non-convergence rule
exists to stop. Folding is also the act M2 names for a defect in a spec: a `rev-N` bump with its §9
line. **The rule's own gap is filed as a backlog row** — when the subject of a review is a SPEC, its
blockers are defects in that spec and "promote to a unit" has no legal referent.

- **Round 2 · spec audit · BLOCKED · 4 confirmed blockers · NON-CONVERGENT.** 39 raw, 27 confirmed,
  12 refuted, precision 0.69 — up from 0.49, and every one of the 15 distinct defects was created or
  left standing by round 1's FOLD rather than by the original design, which is this repo's
  `fold-text-is-unreviewed-surface` class measured on itself.
  [The record](reviews/2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round2.md) also VERIFIED and
  confirmed three claims the fold asserts about existing code. The blocker that mattered most: unit
  1's rev-2 scope had dropped the shell-side `SPEC10_EVIDENCE_CUTOFF=""` preset, and under `set -u`
  its absence aborts the gate in every adopter tree whose conf predates the key — a checker that
  fails to run rather than one that fails.
- **Round 1 · spec audit · BLOCKED · 4 confirmed blockers.** 41 raw findings, 20 confirmed, 21
  refuted, precision 0.49, over 10 agents. The harness's SYNTHESIS agent died on a session limit and
  wrote no report, so
  [the record](reviews/2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round1.md) is derived from
  the run journal and says so in its own header. Both specs folded to rev-2. The highest-value
  finding: unit 1's log join was specified against the wrong bytes and would have shipped a
  Definition-of-Done item that reported UNMET on every conforming Windows run.

## Parked decisions

None. Nothing in this build was refused for the owner to decide: every fork its specs raised was
resolvable under the delegated authority, and every review finding was folded, adopted as a unit, or
filed as a backlog row. Parked entries would live in `RUN.md` and be surfaced in the wrap-up.

**What was filed rather than built**, because a finding with no disposition is a finding discarded:

| id | why it is a row and not a unit |
|---|---|
| `TOOL-aProvenReuse-3` | the NON-CONVERGENT disposition has no legal referent when the review subject is a SPEC; that is a defect in `BUILD-METHOD.md` M4, not in this build |
| `TOOL-aProvenReuse-4` | closing the `reuse_lookup.py` liveness gap needs a cross-kit dependency or a third telemetry format, so it fails protocol §11's strictly-beneficial test |
| `TOOL-aProvenReuse-6` | the unattended suite's bounded-observation arms are wall-clock assertions that flake under fleet load; measured three times, pre-existing, and this diff touches none of that machinery |

**Round-3 findings NOT folded, and why each**, so the next reader does not re-derive them:

- The fenced-`--terms` sub-claim of round 3's blocker is REFUTED, and this is the one place that is
  written down. It was reproduced with a standalone predicate that does not strip fences; the shipped
  checker unfences `body[]` before the arm ever runs, so that section scores `hasT=0 hasP=1` and reds
  on the TERMS arm, identically before and after the fold. That is
  `second-implementation-is-not-a-second-opinion`, and taking it at face value would have bought a
  fix for a defect that does not exist.
- The two suite totals round 3 could not verify — `check-memory-hygiene.test.sh` at 270 assertions
  and `check-unattended.sh` at exit 0 — were both OBSERVED by this run and are recorded in the commit
  that made them true. Round 3 timed out reaching them; that is a limit of that round, not a gap.
- The `marker-written-last` hole is real, unreachable in this corpus, and now DECLARED in the spec
  template's own §10 section rather than fixed. A gate that cannot state its blind spots is worse
  than one that can.

## Review rounds — the closing diff review

**The closing loop ALSO exited NON-CONVERGENT**, at 2, 1, 1 confirmed blockers. Round 3's blocker was
folded rather than promoted, for the reason recorded above the spec-audit rounds: it was a shipped
document describing a predicate it no longer had, which is a defect in a carrier and not a mechanism
M2 would let a unit hold.

**Every round's blocker lived in the FOLD, never in the code the fold was closing.** Round 1: a red
merge-bar leg this build turned red. Round 2: a conf key documented in neither protocol carrier, and
a repair that leaked on wrapped input. Round 3: a template still describing the repair that replaced
it. Three rounds, three fold defects, and the rate did not fall — which is the honest reading of why
the loop stopped rather than a reason to run a fourth.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aProvenReuse-1` | SPECCED | hygiene check 12 grades §10's CONTENT, behind a declared cutoff |
| 2 | `TOOL-aProvenReuse-2` | SPECCED | a `reuse-probed` DoD item joins the run to the recall query log |
| 3 | `TOOL-aProvenReuse-5` | SPECCED | the example-conf parity arm reaches bare presets |

*Both spec headers read `SPECCED` too. Round 2's F14 found the fold flipping these cells while
leaving both headers at `OPEN`, and the generated table below — which DERIVES from those headers —
still saying `OPEN` in the same commit.*
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-3 TOOL-aProvenReuse-4 TOOL-aProvenReuse-5 TOOL-aProvenReuse-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aProvenReuse-1 — hygiene check 12 grades §10's CONTENT, behind a declared cutoff](spec/2026-08-31-spec-TOOL-aProvenReuse-1.md) | 1 | 2 | SPECCED | rev-5 | 2026-08-31 |
| [TOOL-aProvenReuse-2 — a `reuse-probed` DoD item joins the run to the recall query log](spec/2026-08-31-spec-TOOL-aProvenReuse-2.md) | 2 | 2 | SPECCED | rev-7 | 2026-08-31 |
| [TOOL-aProvenReuse-5 — the example-conf parity arm reaches bare presets](spec/2026-08-31-spec-TOOL-aProvenReuse-5.md) | 3 | 1 | SPECCED | rev-1 | 2026-08-31 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aProvenReuse-5.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aProvenReuse-1` | no |
| 2 | `TOOL-aProvenReuse-2` | no |
| 3 | `TOOL-aProvenReuse-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
