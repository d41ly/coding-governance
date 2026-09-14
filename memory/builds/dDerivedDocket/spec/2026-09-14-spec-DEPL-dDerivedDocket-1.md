# DEPL-dDerivedDocket-1 — adopter runbook: backlog switch and merge attribute

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-1 · base abac6d59 · streams deployer+tooling · order 38

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Tell an adopter, in the runbook they follow, that the per-build backlog exists, that nothing
changes until they switch, and how to switch in a deployer build of their own. Add the merge
attribute a builds-mode tree needs beside the one it keeps, bring the runbook's description of the
charter's unattended blocks up to date, and fix the scaffold's shard header, whose "leads with one
status token" wording is where one adopter's status-first rows came from.

## 2. Scope (IN)

- **S1** `WIRE-INTO-PROJECT.md` §3 step 4 gains the attribute line
  `memory/builds/*/BACKLOG.md merge=rows` beside the two it has, and says the `memory/backlog/*.md`
  line stays after a switch, because the row driver is what refuses a pre-switch branch's shard
  merged into a generated view. Its sentence on who appends names a build's `BACKLOG.md` beside a
  backlog shard. Observed by AC1.
- **S2** A new `### 3a-asks` section between §3 step 4 and the `<!-- govkit:entry drift-audit -->`
  anchor at `WIRE-INTO-PROJECT.md:215`. It states the absent-key default, routes the switch to the
  adopter's own deployer build, gives the switch as five ordered steps by command, points at the
  memory-tree kit README for grammar and verdicts, and points at design section 10 for the measured
  facts about this repo's known adopters. Observed by AC2, AC3 and AC4.
- **S3** §3 step 2's sentence on what the scaffold writes names the shards as the default mode and
  points at §3a-asks. Observed by AC4.
- **S4** §2's bullet on the unattended kit, at `WIRE-INTO-PROJECT.md:124`, names everything the
  charter's `kit:unattended` blocks carry after the charter unit: the explicit-ask substitute, the
  pointer to the protocol's landing rule, and the protocol contract. It states no count of blocks.
  Observed by AC5.
- **S5** The scaffold's shard header at `tools/memory-tree/adopt-memory-tree.sh:281` quotes the row
  shape with the id first and exactly one status token after it, instead of saying a row leads with
  a status token. Observed by AC6.

## 3. Non-goals (OUT)

- No adopter is migrated. Each switches in a deployer build of its own; the owner's mandate refused
  adopter migration in this build.
- No builds-mode fresh scaffold. The scaffolder still writes authored shards (§8 F1).
- No memory-tree kit README text. Its backlog sections, its attribute block and the grammar are the
  memory-tree docs unit's, and §3a-asks points at them rather than copying them (§8 F5).
- govkit's attribute emission and the wiring check's flat-layout probe belong to the concurrent
  adopter-wiring session. This unit edits only the runbook's hand-wiring step.
- The three test fixtures that replicate the old header text, in
  `tools/memory-tree/check-memory-hygiene.test.sh` and `tools/memory-tree/merge-rows.test.sh`, stay.
  They are inert fixture strings in held suites and assert nothing about the scaffold, which is the
  replica class TOOL-dRetiredFork-31 records.
- Gov's own four shard headers are replaced at the switch-over by the generated views' header.
- No memory-tree kit version bump (§8 F6).
- The root `README.md` is untouched: shards remains the kit's default, so its line stays true.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-34` — the switched tree the section's worked example
  points at, the `--write` verb, the two conf keys it sets, and the kept-plus-added attribute.
- **consumes-from** `PLAY-dDerivedDocket-1` — the charter's `kit:unattended` blocks and what they
  carry, which S4 describes. Added by this spec, not in the brief's table.
- **consumes-from** `TOOL-dDerivedDocket-9` — gov's `.githooks/commit-msg`, the reference step 5
  names for the transition audit's commit-time carrier. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-10` — the row driver's refusal of a shard merged into a
  view, which is the reason S1 gives for keeping the backlog attribute. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-11` — `--plan` and the two worksheets step 1 files. Added
  by this spec.
- **consumes-from** `TOOL-dDerivedDocket-12` — `--stragglers` and `--recipe`, which steps 2 and 5
  name. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-13` — the gov-only straggler-guard library and
  `pre-rebase` hook, which step 5 names as the reference an adopter copies. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-36` — the kit README's backlog-mode section the new
  section points at. Added by this spec.
- **hands-off** external — a scaffold that writes no authored shard when `BACKLOG_MODE="builds"` is
  declared before adoption, which would let a fresh tree start in builds mode.

## 4. Design

### The edits, by location

| Where, at BASE | Now | After |
|---|---|---|
| `WIRE-INTO-PROJECT.md:124`-`:126` | "keeps the `kit:unattended` block in `§1`, which is the ONE substitute…" | names the substitute, the landing pointer and the contract |
| `WIRE-INTO-PROJECT.md:172`-`:175` | "The scaffold writes `memory/` with `builds/`, `backlog/<FAMILY>.md`, …" | the shards named as the `shards`-mode default, with a pointer to §3a-asks |
| `WIRE-INTO-PROJECT.md:198`-`:201` | "two nodes appending to `DECISIONS.md` or a backlog shard" | the same, plus a build's `BACKLOG.md` |
| `WIRE-INTO-PROJECT.md:206`-`:209` | two attribute lines | three, and one sentence on keeping the backlog line |
| after `WIRE-INTO-PROJECT.md:213` | the drift-audit anchor follows | `### 3a-asks`, then the anchor |
| `tools/memory-tree/adopt-memory-tree.sh:281` | "> Mutable. Each row leads with one status token (OPEN…WONTDO)." | the id-first shape |

### Proposed text for §3a-asks

The build may reword it. It may not name a flag or path the tree does not hold at the pass (AC3),
and it keeps the switch out of §3's first-adoption steps (AC4).

```markdown
### 3a-asks — Per-build asks and a generated backlog view (opt-in; memory-tree kit ≥ <version>)

**An upgrade changes nothing until you switch.** With `BACKLOG_MODE` absent from
`.memory-tree.conf` the tree runs in `shards` mode: the authored `backlog/<FAMILY>.md` files §3
scaffolds, one status slot per row. In `builds` mode each ask is filed once, as a row of
`<MEMORY_ROOT>/builds/<slug>/BACKLOG.md` in the folder of its own id's slug; its status is derived
from specs and disposition rows; and `backlog/<FAMILY>.md` becomes a GENERATED view nobody edits.
The grammar, the verdicts and the status fold are `tools/memory-tree/README.md`'s. This is the order.

**The switch is its own deployer build in your repo, never a step of a first adoption.** It
migrates your corpus, so it takes a spec, a signed record and one switch-over commit:

1. **Census, read-only.** `python tools/memory-tree/migrate_backlog.py --plan` files the id census,
   the same-id worksheet and the triage worksheet as records of your build, and names every row it
   cannot parse. Fix those first: the writer never drops a row.
2. **Stragglers.** `python tools/memory-tree/migrate_backlog.py --stragglers` walks every local and
   remote-tracking ref for a branch still editing a shard. Merge the ones you know before the switch.
3. **Sign both worksheets.** Your owner decides which same-id pairs are one subject and gives every
   open ask on a finished build one disposition. The writer applies exactly what is signed. This
   repo's own signing, under rules its owner delegated, is in `memory/builds/dDerivedDocket/`.
4. **Switch in ONE commit.** `python tools/memory-tree/migrate_backlog.py --write`, then
   `BACKLOG_MODE="builds"` and the `ASK_CUTOFF` it prints, the `BACKLOG.md` attribute from §3 step 4,
   and `python tools/memory-tree/gen_build_index.py --write`. Commit when `--check` exits 0.
5. **Tell stragglers what to do.** The recipe a pre-switch branch follows is what
   `python tools/memory-tree/migrate_backlog.py --recipe` prints, the same text the generated views
   carry. The hooks that tell a branch before it lands are yours to wire: this repo's
   `.githooks/straggler-guard.sh`, `.githooks/pre-rebase` and `.githooks/commit-msg` are the
   reference, and they are not shipped by any kit.

A census over a FORKED engine decides more before step 4: a status your tree reads as terminal that
the kit does not, ids from an era with no slug to route by, relative links that change depth. This
repo measured those for its three known adopters in section 10 of
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`.
```

`<version>` is the `KIT_MEMORY_TREE_VERSION` the tree declares at this unit's pass, read then and
not assumed here.

### Proposed text for the smaller edits

```markdown
- **Unattended runs** (`unattended/` kit): keeping it selected keeps `§1`'s `kit:unattended` blocks —
  the ONE substitute for the explicit ask before a merge and a push, the pointer to the protocol's
  landing rule, and the protocol contract. A repo that keeps them without the kit is carrying rules
  nothing can make true.

   memory/DECISIONS.md          merge=rows
   memory/backlog/*.md          merge=rows
   memory/builds/*/BACKLOG.md   merge=rows

   Keep the `backlog/*.md` line after a switch (§3a-asks): the driver is what refuses a pre-switch
   branch's shard merged into a generated view.
```

The scaffold header, inside the existing `printf` format string:

```
> Mutable. One row per ask: `- <ID> · <STATUS> · <text>`, the id first, then exactly one status token (OPEN…WONTDO).
```

### Files touched (estimate)

`WIRE-INTO-PROJECT.md` · `tools/memory-tree/adopt-memory-tree.sh`

### Alternatives rejected

- **Routing a fresh adoption straight to builds mode.** It needs a scaffold that writes no authored
  shard, which is a change to the adopter's behaviour (§8 F1).
- **Folding the switch into the existing §3a.** That section retires a different product's shape
  under its own version line; mixing the two makes one heading answer two upgrade questions.
- **Copying the kit README's grammar into the runbook.** A second copy of the grammar is the one
  that rots (§8 F5).

## 5. Production-readiness checklist

- security — no new write path. The section names the one sanctioned cross-folder writer and says it
  runs only in an adopter's own switch-over commit, on worksheets its owner signed.
- perf / scale — N/A: prose and one header string. The census's cost is stated by the planner unit.
- error / empty / loading states — an absent `BACKLOG_MODE` reads as `shards` and the runbook says so
  first. The writer's refusals on an unsigned or unparseable input are the switch-over unit's, and
  step 1 tells the adopter to clear what the census could not parse.
- observability — the section names what an adopter reads at each step: the census record, the
  straggler list, the writer's conservation table and printed cutoff, and the generator's `--check`.
- risks — the section names commands other units built, so a renamed flag would strand an adopter;
  AC3 grades every name at this unit's pass. The concurrent adopter-wiring session may edit §3 step 4
  too, and the landing reconciles with whichever lands first. The attribute block now exists in both
  the runbook and the kit README, as it did at BASE.
- testing — a scratch `git check-attr` over the attribute lines, a scratch scaffold with the hygiene
  gate run over it, a flag and path resolution pass, and a positional read of the new section.
- migration — this unit documents the switch and performs none.
- user docs — the runbook is the user document for adopters; there is no separate help page.

## 6. Acceptance criteria

- **AC1** — When the attribute lines from §3 step 4 are written into a scratch repository's
  `.gitattributes`, `git check-attr merge` prints `rows` both for `memory/backlog/TOOL.md` and for a
  path of the shape `memory/builds/*/BACKLOG.md` with a slug in place of the star.
  Red when: the builds line replaces the backlog line, the design's retired "retarget" wording,
  which prints `unspecified` for the backlog path and hands a pre-switch branch's shard to git's
  line merge.
  fixture: an empty scratch git repository; the two paths need not exist for `git check-attr`.
- **AC2** — When an `awk` pass over `WIRE-INTO-PROJECT.md` sets a flag at
  `<!-- govkit:entry memory-tree -->`, clears it at `<!-- govkit:entry drift-audit -->`, and prints
  the flag at each `### 3a-asks` heading, it prints `1` exactly once.
  Red when: the section lands after the drift-audit anchor, where the runbook's own entry anchors
  file it under that kit, or it is written twice.
- **AC3** — When every flag §3a-asks names for `migrate_backlog.py` and `gen_build_index.py` is
  looked up in that tool's usage output from `--help`, each is listed, and every repository path the
  section names, the three reference hooks among them, is in `git ls-files`.
  Red when: a producing unit spelled a verb other than the design did, such as `--straggler` for
  `--stragglers`, and the runbook kept the design's spelling, which strands an adopter at a command
  that does not exist.
  figure: the flag and path sets are DERIVED from the section at observation time.
- **AC4** — When `grep -n 'BACKLOG_MODE' WIRE-INTO-PROJECT.md` runs, every hit sits inside §3a-asks,
  one of them states that an absent key reads as `shards`, and §3 step 2 carries a pointer to
  §3a-asks.
  Red when: `BACKLOG_MODE="builds"` is written into §3's first-adoption steps, so a fresh adopter
  switches before any census exists and `--write` has no signed worksheet to apply.
- **AC5** — When `grep -n 'kit:unattended' WIRE-INTO-PROJECT.md` locates §2's bullet on the
  unattended kit, that bullet names the landing-rule pointer and the protocol contract beside the
  explicit-ask substitute, and states no count of blocks.
  Red when: it still describes only the ask substitute, so an operator dropping the kit is not told
  that the landing pointer and the contract leave with it.
- **AC6** — When `bash tools/memory-tree/adopt-memory-tree.sh --scaffold` runs in the scratch
  fixture, each scaffolded `memory/backlog/*.md` quotes the row shape with the id before the status
  token, `grep -c '^- '` prints 0 for every shard, and `bash tools/memory-tree/check-memory-hygiene.sh`
  over the scaffolded tree exits 0.
  Red when: the example row is written on its own `- ` line, which the zero count reports and the
  row driver would read as a row in every fresh shard.
  fixture: a scratch git repository holding a copy of the kit directory and a `.memory-tree.conf`
  copied from `tools/memory-tree/.memory-tree.conf.example`, committed before the scaffold runs.
  Measured at BASE on 2026-09-14: the scaffold wrote three shards and the hygiene gate exited 0 with
  0 graded rows.
  cost: under a minute.

## 7. Gates

`memory hygiene` · `playbook parity` · `install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

No new gate arm. The runbook's entry-anchor checker is on no bar at BASE, so AC2 reads the position
directly. `memory-hygiene self-test` is held and runs on the landing bar, which owes the self-tests
because this build is kit work.

## 8. Open questions

- **F1** — Does the runbook route a fresh adoption straight to builds mode? (a) Yes. (b) No: a fresh
  tree scaffolds the default shards and switches in its own deployer build like any adopter. (a)
  needs a scaffold that writes no authored shard under builds mode, a change to the adopter's
  behaviour this unit does not price, and the runbook would otherwise send a fresh tree to `--write`
  with no census behind it. RESOLVED (agent, 2026-09-14, delegated): (b), with the scaffold change
  handed off as external.
- **F2** — What does the scaffold header say? (a) Quote the id-first shape with placeholders. (b)
  Drop the grammar sentence and point at the kit README. (c) Show an example row with a real id. (b)
  loses the grammar at the one place a row gets written, which is where the misleading wording did
  its damage. (c) plants an id in every fresh tree. RESOLVED (agent, 2026-09-14, delegated): (a).
- **F3** — Does the builds attribute replace the backlog attribute? (a) Replace it, as design §9 and
  §11 first wrote. (b) Add it and keep the backlog line, as design §18 rev-3 A2 amended and the
  switch-over does for this repo. Without the backlog line a pre-switch shard merged clean under
  `-X ours` and dropped a flip in the design's lab. RESOLVED (agent, 2026-09-14, delegated): (b).
- **F4** — Where does the switch go? (a) A new `### 3a-asks` inside the memory-tree anchored region.
  (b) Inside the existing §3a. (c) A new top-level section. (b) mixes a second upgrade into a
  section about retiring the session ledger; (c) leaves it outside the kit's anchored region.
  RESOLVED (agent, 2026-09-14, delegated): (a).
- **F5** — How much does the runbook carry? (a) The whole procedure with grammar and verdicts. (b)
  The order and the commands, pointing at the kit README for grammar and verdicts. (a) is a second
  copy of the kit README. RESOLVED (agent, 2026-09-14, delegated): (b).
- **F6** — Does this unit bump the memory-tree kit version for the header edit? (a) Yes. (b) No: the
  adopter script is outside the verdict-epoch gate's scan set, and the build lands in one landing, so
  the version its earlier units set is the one that dates this edit on the default branch. RESOLVED
  (agent, 2026-09-14, delegated): (b).
- The ruling this unit carries out and does not revisit: D1, adopt per-build asks with a generated
  view while adopters keep the shards default, RESOLVED (owner, 2026-09-13).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds seven edges the brief's table does not list: one
  consumes-from the charter unit, `PLAY-dDerivedDocket-1`, and one from each unit whose commands or
  texts the new section names (9, 10, 11, 12, 13 and 36). Their producer ends are not written,
  because those specs are other writers'; this spec is Tier-1, so the hygiene gate's edge joins do
  not grade either end.

## 10. Reuse audit

The seams are the runbook's own: §3a, `WIRE-INTO-PROJECT.md:299`, is the shape for a breaking
memory-tree migration an adopter meets on upgrade, and §3a-bind is the shape for an opt-in
sub-section headed by the kit version that brings it. The attribute block and the scaffold's
`printf` header are extended in place. `python tools/codebase-map/reuse_lookup.py "adopter runbook
section that migrates an existing memory tree to a new layout"` returned name-stem neighbours only
(`tree`, `adopt`, `require_adopted_root`), none of them a runbook seam, and its coverage line reads
`unscanned layers: .sh`, so it cannot see `adopt-memory-tree.sh` at all; the seams above were found
by reading the runbook and the adopter. Recall returned the aMendedLedger doc-truth sub-spec, which
wrote §3a and set its two-products, two-version-lines rule; TOOL-dRetiredFork-31, the fixtures that
replicate the scaffold's output rather than invoking it, which is why §3 leaves them; DEPL-aSealedCaravan-3,
a runbook naming a section that does not exist, the class AC3 guards; and TOOL-aHonedRuleset-9,
the runbook's anchor checker sitting on no bar, which is why AC2 reads the position directly.

Where the design and the source disagree at BASE, re-verified here:

- Design §11 and §15's U6 say the attribute is retargeted; §18 rev-3 A2 and the switch-over's spec
  keep it and add one (§8 F3).
- Design §10's per-adopter facts were measured at `09a22d2b` for three named adopters. The runbook
  points at them rather than copying a measurement that will move.
- The scaffold header text also appears in gov's four live shard headers and in three test
  fixtures. The shard headers are the switch-over's; the fixtures are inert (§3).

Recall terms used: `WIRE-INTO-PROJECT runbook migrate adopter shards scaffold header merge=rows attribute ledger retired status-first`
