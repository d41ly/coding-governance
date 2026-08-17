# TOOL-aRuledFrontispiece-10 — the corpus retrofit and the kit version bump

**Status:** CLOSED · rev-2 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Turn the machinery this build lands into corpus bytes, once, in a commit whose entire diff a renderer
derives. `--write` runs over every tracked build README, filling the generated regions units 2, 3 and
4 declare, and `KIT_MEMORY_TREE_VERSION` moves once here so the engine's verdicts are dated at or
after the last commit that moved a scanned line. No authored byte is touched: unit 11, at position 9
of the build README's `#` column, restructures the authored prose and inserts the `roster:units`
pairs before this unit runs.

## 2. Scope (IN)

- **S1** — sequencing, as a deliverable rather than as an intention. The generator changes, their arms
  and unit 11's authored conformance all land in their own units' commits BEFORE any README is
  re-rendered. The re-render is then a commit whose entire diff is machine-derivable, and a reviewer
  reads `python tools/memory-tree/gen_build_index.py --check` output against it rather than reading a
  corpus-wide diff.
- **S2** — the re-render. `python tools/memory-tree/gen_build_index.py --write` over the whole tree, in
  one commit, changing no byte a human wrote. This is where the three new generated regions first
  exist in the corpus, because `--write` CREATES a missing pair at the slot position the contract
  defines. That behaviour is unit 1's; this unit is its first corpus-scale caller and adds no marker
  machinery of its own.
- **S3** — `KIT_MEMORY_TREE_VERSION` moves 2.16 to 2.17 at the constant plus its seven mirrors, in one
  commit. Three mirrors are re-rendered by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` rather than hand-edited.
- **S4** — the generator's `--selftest` gains an arm that drives a fixture carrying the RETROFITTED
  shape — the plan pair present, all three new generated regions present — through `--write` and then
  `--check`, asserting the second run is clean. The existing fixed-point arm covers the pre-retrofit
  shape only, and no earlier unit's fixture carries every region at once, so this arm is the
  integration boundary of the whole build and belongs to the unit that first crosses it.
- **S5** — the byte-tier measurement, which is taken here because it cannot be taken anywhere earlier.
  Every tracked build README is measured against check 6's build-README byte tier after `--write` and
  before the commit lands. A breach STOPS the landing and goes to the owner with the measurement;
  this unit changes neither the tier nor the render to make a number fit. §4 Migration carries the
  ladder and §3 states what is not this unit's to choose.
- **S6** — no cutoff, and the absence is recorded rather than assumed. `SPEC_FORMAT_CUTOFF`,
  `SPEC10_CUTOFF` and `STREAMS_CUTOFF` all grandfather by filename date; this retrofit adds no fourth
  knob of that kind, so a build README's age never exempts it.
- **S7** — the landing rule. Build READMEs carry no merge driver, so the re-render is landed as a
  reconcile-then-push in one sitting, and a conflict inside a generated region is resolved by
  re-running `--write`, never by choosing a side.
- **S8** — no artifact count, README count or arm count is written into any record this unit lands.
  Each is read from the gate that derives it, and every comparison is this unit's own tip against its
  own parent commit. A figure quoted from `base 96141aed` is not usable here at all: that tree does
  not contain this build's own folder, so its artifact count is a different corpus's.

## 3. Non-goals (OUT)

- Editing an authored byte of any build README. Unit 11 owns every prose relocation and every
  `roster:units` insertion, and lands at position 9, immediately before this unit. If unit 11's
  commit has not landed, this unit does not run.
- Inserting a generated marker pair by hand. Unit 1's `--write` creates a missing pair at the slot
  position; this unit calls `--write` and adds no marker machinery.
- Refusing a mis-bounded prose block, or any other slot violation. Unit 1 owns the slot refusals under
  `--check-format`, and its S1a keeps them off the render path on purpose.
- Choosing the byte tier, or the remedy if S5's measurement breaches it. The remedies are a curation
  pass, a grandfather row in `memory/project/curation-debt.txt` or a different number, and all three
  are owner calls. This unit owns the measurement and the stop, never the number.
- Changing what renders inside `<!-- gen:build-index -->`. Unit 5's wrap is what moves that slice;
  this unit renders it and observes the movement, and AC9 is that observation.
- Retrofitting anything outside `memory/builds/*/README.md`. Guides, specs, `memory/README.md` and the
  map are untouched.
- Bumping any other kit version. `KIT_UNATTENDED_VERSION` moves only if unit 8 changes that kit's
  engine, and that is unit 8's to declare.

## 4. Design

### Inventory

The version value has eight spellings across seven tracked files. Seven of the eight are mirrors of
the constant, and they are not equally defended — the gate column is the load-bearing one, because a
mirror nothing compares is a mirror that goes stale silently.

| Spelling | Gated by |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh:13`, the constant | `tools/check-kit-versions.sh` presence check; `check-verdict-epoch.sh` parses it |
| the same line's `gov:kit memory-tree@` marker | NOTHING — verified against source, see below |
| `tools/memory-tree/HYGIENE.template.md:1` | `check-kit-versions.sh`, derived template loop |
| `tools/memory-tree/BUILD-METHOD.template.md:1` | the same loop |
| `tools/memory-tree/SPEC-TEMPLATE.template.md:1` | the same loop |
| `memory/HYGIENE.md:1` | `kit-dogfood-parity.test.sh`, transitively |
| `memory/TEMPLATE-SPEC.md:1` | the same |
| `memory/guides/BUILD-METHOD.md:1` | the same |

`check-kit-versions.sh` compares the constant against every tracked
`tools/memory-tree/*.template.md` marker and against nothing else in this kit. The marker sharing the
constant's own line is therefore unchecked, even though the same file asserts exactly that pairing for
`agent-cap.js` and `settings-merge.py`. Closing it is a one-line addition to that gate and is NOT in
this unit's scope; what this unit owes is that the miss cannot happen silently here, which AC4 buys
with a grep over the carriers this table names.

The three live copies are gated only through the render: `kit-dogfood-parity.test.sh` substitutes
`{{KIT_DIR}}` and `{{TOOL_ROOT}}` into each template and byte-compares the result against the
installed copy. So a template bumped without a `--render` reds, and a live copy hand-edited to the new
number without its template also reds. Neither can be bumped alone.

### Migration

The corpus is the tracked `memory/builds/*/README.md` set. The live count is read from
`gen_build_index.py --check`, never from this file, and it moves whenever a build folder opens.

Two things change in the corpus at commit C, and both are renderer output:

1. The `gen:build-index` slice moves wherever unit 5's wrap re-flows a `**Build status:**` line that
   exceeds the wrap width. Which files those are is a measurement, not a list — it changes as rosters
   and statuses move, including inside this build.
2. The three new pairs `gen:build-order`, `gen:build-edges` and `gen:build-docs` appear, with their
   regions rendered. **No unit hand-inserts them.** Unit 1's `--write` creates a missing generated
   pair at the slot position its contract defines, so the insertion is renderer output like the
   region it delimits. Unit 1 owns that behaviour; this unit calls it once over the whole tree.

That second point rests on an ASYMMETRY unit 1 owns and this unit depends on: creating a missing pair
is a `--write` behaviour that `--check` does not demand. If `--check` demanded a pair that is not
there, hygiene check 9 would red at the tip of every region unit from position 3 onward, each of those
units would have to re-render the corpus in its own commit, and there would be nothing left for this
commit to render. AC1 is where the asymmetry is observed rather than assumed.

Unit 11's authored moves cost the render nothing and cannot pre-empt this commit: for a build README
the rendered artifact IS the file with its regions replaced, so relocating authored bytes is a fixed
point of `--check` on the same run. That is what makes position 9 and position 10 separable commits
rather than one.

**The byte tier, taken here because no earlier unit can take it.** Fork 3 set check 6's build-README
tier at 25600 bytes, and units 2, 3 and 4 each add a rendered region to every README that carries the
source for it. The corpus's largest entry point had under one kilobyte of headroom when this revision
was measured with `wc -c` over the tracked set, so a breach is the expected outcome rather than a tail
risk. The figure is re-measured at commit C rather than carried forward, because unit 5's wrap and
unit 11's moves both change it and because a quoted headroom is exactly the drifting number S8 exists
to refuse. If the measurement breaches, this unit stops: the render is not trimmed to fit and the tier
is not raised. The three remedies — a curation pass over the offending README, a row in the empty
shrink-only `memory/project/curation-debt.txt`, or a different tier — are owner calls, and whichever
is taken is recorded as a new id in `memory/DECISIONS.md` by the turn that takes it. This unit mints
no such row otherwise. Spec-5 §5 and §8 hand this measurement here explicitly; it stops here.

The recurring class is `gate-green-by-accident-on-generated-bytes`. Its fix has two halves and both
are already present: `.gitattributes:34` pins `memory/**/*.md text eol=lf` so the committed bytes are
LF, and `read_text` at `gen_build_index.py:93-97` decodes and replaces CRLF before any comparison, so
a Windows checkout cannot red a correct tree. Neither half is added here — both are asserted, because
a corpus-wide re-render is exactly the moment a half-present fix looks green.

### Rollout

Three commits, in this order, all after positions 1 through 9 of the build README's `#` column have
landed. This unit is position 10 and unit 6's leg is position 11, so unit 6 lands AFTER this unit and
is not a precondition of it.

1. **A — the integration arm.** S4's fixed-point arm over the retrofitted fixture, in
   `tools/memory-tree/gen_build_index.py`. It changes no rendered byte, so it does not disturb S1's
   promise about commit C.
2. **B — the version bump.** The constant and its same-line marker at
   `tools/memory-tree/check-memory-hygiene.sh:13`, the three templates, then
   `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` for the three live copies. Reviewed as
   an eight-line diff.
3. **C — the re-render.** `--write`, then `--check`, then S5's measurement. Reviewed as `--check`
   output.

Commit B must be the NEWEST commit in the range that touches
`tools/memory-tree/check-memory-hygiene.sh` or any of the six delegates `check-verdict-epoch.sh`
scans, which include `tools/memory-tree/gen_build_index.py`. The gate's rule is topological: the
newest behaviour-bearing engine change must be an ancestor of, or equal to, the newest commit that
changes the constant's value. Commit A precedes B and commit C touches no scanned file, so neither
displaces it.

**What can displace it is position 11.** Any commit after B that moves a behaviour-bearing line of
`gen_build_index.py` reds the verdict-epoch leg at the build's tip, and unit 6 lands after this unit.
The constraint this unit's bump imposes on the rest of the build is therefore explicit: after commit
B, no unit may move a scanned line. Unit 6's own deliverables — a `tools/gate-legs.json` row, a
charter bullet and a map dossier — touch no scanned file and satisfy that constraint; a verb, a mode
tuple or a usage line does not, and belongs in unit 1's commit at position 1 where the verb is
defined. The alternative is a second bump, which is what the build's rule against a mid-build bump
exists to avoid.

Landing is positional. `git check-attr merge -- memory/builds/aStandingWrit/README.md` reports
`unspecified`, so the row-keyed driver that protects `memory/DECISIONS.md` and the backlog shards does
not cover build READMEs — git's built-in three-way text merge does, across the whole corpus at once.
Every spec status header on any node is an input to its own build's rendered region, so a concurrent
node landing one spec makes commit C's rendered bytes stale for that build and produces a textual
conflict inside a generated region. The rule in S7 follows: fetch, rebase, re-run `--write`, push, in
one sitting; and resolve any conflict inside a generated region by re-rendering rather than by picking
a side, because both sides are outputs and neither is evidence.

### Files touched (estimate)

Commit A: `tools/memory-tree/gen_build_index.py` and its `--selftest` arms. Commit B:
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/HYGIENE.template.md` ·
`tools/memory-tree/BUILD-METHOD.template.md` · `tools/memory-tree/SPEC-TEMPLATE.template.md` ·
`memory/HYGIENE.md` · `memory/TEMPLATE-SPEC.md` · `memory/guides/BUILD-METHOD.md`. Commit C: every
`memory/builds/*/README.md`, plus `memory/LIVE.md` and the ledger shards if any build's derived status
moved. No authored line in any of them.

### Alternatives rejected

A filename-date cutoff, the mechanism `SPEC_FORMAT_CUTOFF` and `SPEC10_CUTOFF` already provide for
specs. It is the cheapest option and the owner declined it. Recorded because it will be proposed
again: a cutoff would leave the corpus permanently two-shaped, and the format leg in unit 6 would then
have to carry the cutoff too, which is a second knob for one corpus.

Landing the bump and the re-render in one commit. Rejected because it destroys the reviewability
property S1 exists for: the eight version lines would be indistinguishable, in a diff, from the
mechanical output of the renderer.

Taking the authored retrofit here, which is what rev-1 of this spec did. Rejected by the owner in
favour of a unit of its own at position 9. Two operations on authored bytes inside a unit whose whole
claim is that its diff is machine-derived is a contradiction the reviewability property cannot
survive, and the audit found four separate defects inside those two operations.

Handing the byte-tier measurement back to unit 5. Rejected because unit 5 lands at position 6, before
any of the three new regions exists in a single file, so the number it would measure is not the number
the tier has to hold. The measurement has been handed forward three times already; S5 is where it
stops.

## 5. Production-readiness checklist

- security — N/A. No new input crosses a trust boundary; every file read is tracked and read today.
- perf / scale — one `--write` over the corpus, the same pass the gate already runs on every push.
- a11y — N/A. No user-facing surface.
- i18n — N/A. Markers and version strings are ASCII literals.
- error / empty / loading states — a build with no roster table, one with no record but its README,
  and one whose sources declare no order and no edges must each render without a region rather than
  with an empty one; each is an arm.
- observability — every refusal names the file and the line, the version bump is observable as one
  grep over the carriers §4 names, and the byte measurement is `wc -c` over a tracked set.
- risks — the byte tier is expected to BIND at commit C, and S5's stop is the whole mitigation.
  Second, the two LANDED run-state files hold a copy of a `gen:build-index` slice, and unit 8's
  terminal-phase carve-out means no leg reports it going stale; the copies go stale at whichever
  commit first re-renders that slice, which is unit 5's at position 6, and AC9 is how this unit proves
  it is not that commit. Third, the bump dates the engine, so any later commit in this build that
  moves a scanned line reds the verdict-epoch leg.
- testing + left-shift gates — S4's fixed-point arm over the retrofitted fixture, plus a second
  consecutive `--check` at commit C's own tip. Unit 6's format leg runs over the real corpus at
  position 11, after this unit, so it is not an observation available here.
- migration / rollback — commit C reverts as one revert and restores the previous rendered bytes;
  commit B reverts as an eight-line revert plus a `--render`; commit A reverts as one file. Reverting
  C alone leaves the version claiming an epoch the corpus no longer matches, so C and B revert
  together or not at all.
- user docs — the slot contract lands in `memory/HYGIENE.md` and its kit template in unit 1; this unit
  only carries their version markers.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs at this unit's parent
  commit it reports clean, and when it runs again at commit C's tip it reports clean at the SAME
  artifact count. Both figures are read from the gate's own output rather than written here, and their
  equality is the observation that a re-render creates and destroys no artifact.
- **AC2** — When `git diff` is read between commit B's tree and commit C's tree, every changed line
  lies inside a generated region, on one of the marker lines `--write` created to open or close one,
  or on the `ids:` front-matter line.
- **AC3** — When commit C has landed, each of the three new pairs is present in exactly the build
  READMEs its owning unit's source selects, checked with `git grep -l '<!-- gen:build-order -->'` and
  its two siblings against that unit's own selector re-run, never against a file list written here.
- **AC4** — When the bump lands,
  `git grep -l 'memory-tree@2\.16' -- tools/memory-tree/ memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/BUILD-METHOD.md`
  prints nothing, and `bash tools/check-kit-versions.sh` exits 0. The pathspec is load-bearing: an
  unscoped grep matches this spec's own §4 table and can never print nothing.
- **AC5** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the bump, it exits 0
  without needing `--render`, proving the three live copies were re-rendered rather than hand-typed.
- **AC6** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs at commit C's tip, it prints
  `clean` and names commit B as the commit in which the version moved.
- **AC7** — When `python tools/memory-tree/gen_build_index.py --selftest` runs at commit A's tip, the
  new arm over the retrofitted fixture passes and the total arm count is strictly greater than at this
  unit's parent commit.
- **AC8** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at commit C's tip, check 6
  reports no build README over its byte tier. If it names one, commit C does not land and §4
  Migration's escalation is taken instead of any edit to the render or the tier.
- **AC9** — When the `<!-- gen:build-index -->` slice of every build README is extracted from commit
  B's tree and again from commit C's tree with `git show` and the two sets are compared byte for byte,
  no slice differs. Unit 5 re-renders the files its wrap changes inside its own commit at position 6,
  so the corpus already carries the wrapped slice by commit B, and this unit's `--write` adds only the
  three new regions beside it. A difference here means a re-render was deferred into this commit and
  the two `RUN.md` copies went stale under it. The comparison is direct rather than a check-8 verdict
  because unit 8's terminal-phase carve-out skips that check's equality refusal for both LANDED
  `RUN.md` files, so check 8 reports green whether the slice moved or not.
- **AC10** — When `git check-attr eol -- memory/builds/cBriefedPilot/README.md` runs after commit C it
  reports `lf`, and a second consecutive `python tools/memory-tree/gen_build_index.py --check` on the
  unmodified tree is clean, which is the pair that closes
  `gate-green-by-accident-on-generated-bytes` for the largest re-rendered file.

## 7. Gates

`bash tools/run-gates.sh` in full, because this unit re-renders the corpus and dates the engine. The
legs that can only be judged here: `verdict epoch (kit version dates the engine)` · `kit version
markers` · `kit/dogfood doc parity` · `memory hygiene (20 checks)` for check 9 over the re-rendered
corpus and checks 6 and 7 over the grown files · `build-index selftest` · `unattended kit gate` for
check 8 · `codebase-map coverage + freshness`. Before the review,
`python tools/memory-tree/gotchas.py --for-diff <parent>..HEAD` names the classes this diff can hit;
`gate-green-by-accident-on-generated-bytes` is the one already known.

Commit B edits `tools/memory-tree/check-memory-hygiene.sh`, which `memory/guides/SESSION-KICKOFF.md`
watches, so `skills/session-kickoff/manifest-check.sh` needs a `last-audit` re-stamp no earlier than
the build's LAST watch-touching commit. That re-stamp is not this unit's to make — at position 10 it
would be stale before the build tip — and it is named here so the obligation is visible from the unit
that creates half of it.

## 8. Open questions

none — forks 3, 5 and 7 at the build README resolved the three this unit would otherwise have asked,
and the owner's refusal of a grandfather cutoff resolved the fourth. The byte-tier breach S5 expects
is not a fork: this unit's answer is to stop and hand the owner a measurement, and the number is
explicitly outside its authority under §3.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit
  (`reviews/2026-08-16-review-aRuledFrontispiece-1.md`), which carried five blockers against this
  unit. Deleted the whole authored retrofit — the roster wrapping and the six-file prose relocation
  table — which the owner moved to a new unit 11 at position 9; the audit found that operation built
  fork 1's rejected Option B and manufactured eight slot violations it could not see. Deleted the
  bounded-prose refusal, which reversed unit 1's S1a, named an anchor mechanism a position-bounded
  block has no referent for, and designed a 39-file rewriter the same document called hand work; the
  refusal lives in unit 1's `--check-format`. Restated §4 Rollout's precondition against the build
  README's `#` column, positions 1 through 9, after the audit found this unit and unit 6 each claiming
  to land before the other, and moved the "format leg over the real corpus" claim out of §5 since unit
  6 is position 11. Recorded in §4 Migration that `--write` creates the three new marker pairs and
  that unit 1 owns that behaviour, which dissolves the set-level blocker that no unit inserted them,
  and named the `--check` asymmetry it depends on. Replaced the old AC10 — which could not fail,
  because unit 8's carve-out skips check 8's equality refusal for both LANDED run-state files — with
  AC9's direct byte comparison of the region across commits B and C. TOOK the byte-tier measurement
  the audit found handed forward three times, as S5 plus AC8, with the number reserved to the owner in
  §3. Derived AC1's counts instead of spelling them and dropped every figure quoted from
  `base 96141aed`, whose tree does not contain this build's folder. Scope items renumbered S1 to S8
  with no survivor's meaning changed.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `retrofit corpus generated
region marker kit version bump verdict epoch byte compare eol pin fixed point render parity`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| splice into a named marker pair, creating it when absent | `apply_region` at `gen_build_index.py:493`, parameterised and taught to create by unit 1 | REUSE as unit 1 leaves it; this unit adds no marker machinery |
| re-render a shipped template into its live copy | `kit-dogfood-parity.test.sh --render` and its `PAIRS` list | REUSE unchanged — it already covers all three doc pairs |
| prove a render is its own fixed point | the `write then check is a fixed point` arm in `--selftest` | EXTEND — a second fixture carrying the retrofitted shape |
| force the version to move with the engine | `check-verdict-epoch.sh` | REUSE unchanged; this unit satisfies it rather than changing it |
| measure a document against a byte tier | check 6's awk in `check-memory-hygiene.sh`, given its third class by unit 5 | REUSE unchanged — S5 reads the verdict, it does not re-implement the cap |

`python tools/codebase-map/reuse_lookup.py "retrofit a generated marker region across every file
in a corpus"` returned `apply_region` and `render_region` in `gen_build_index.py` as the only
marker-region seams, `kit-dogfood-parity.PAIRS` as the only template-to-live render seam, and
`gate-green-by-accident-on-generated-bytes.md` as the governing gotcha class.

Every claim about existing code in this spec was verified against source at rev-2: the eight version
spellings over seven files, `gen_build_index.py` as one of the six delegates
`check-verdict-epoch.sh` scans, the absent merge attribute on a build README, the absence of any gate
pairing the constant with the marker on its own line, both tracked `RUN.md` files at `phase: LANDED`,
and the fact that `memory/builds/aRuledFrontispiece/` does not exist at `base 96141aed`.
