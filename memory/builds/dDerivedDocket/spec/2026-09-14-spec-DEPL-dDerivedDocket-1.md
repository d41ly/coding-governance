# DEPL-dDerivedDocket-1 — adopter runbook: backlog switch and merge attribute

**Status:** SPECCED · rev-4 · 2026-09-20 · node d · Tier-1 · base fb07ca25 · streams deployer+tooling · order 38

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round1.md) | spec-audit | TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round2.md) | spec-audit | TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 |

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
  adopter's own deployer build, gives the switch as six ordered steps by command, the fourth deleting
  the family backlog archives builds mode refuses and the sixth landing the switch when the default
  branch moved, points at the memory-tree kit README for grammar and verdicts, names the
  `memory-recall` kit as a prerequisite of the switch, and points at design section 10 for the
  measured facts about this repo's known adopters. Each step names the command it runs or the kit README row
  that states its input. Observed by AC2, AC3 and AC4.
- **S3** §3 step 2's sentence on what the scaffold writes names the shards as the default mode and
  points at §3a-asks. Observed by AC4.
- **S4** §2's bullet on the unattended kit, at `WIRE-INTO-PROJECT.md:124`, names everything the
  charter's `kit:unattended` blocks carry after the charter unit: the explicit-ask substitute, the
  pointer to the protocol's landing rule, and the protocol contract. It states no count of blocks.
  Observed by AC5.
- **S5** The scaffold's shard header at `tools/memory-tree/adopt-memory-tree.sh:281` quotes the row
  shape with the id first and exactly one status token after it, instead of saying a row leads with
  a status token. Observed by AC6.
- **S6** §2's kit list gains a bullet for the kickoff manifest, the `kickoff-manifest` kit: keeping
  it selected keeps the `kit:kickoff-manifest` block in `§1`, the manifest's merge exception, and
  dropping it removes that exception with the manifest it governs. Observed by AC5.
- **S7** The carried-prefix list. §3a-asks spells commands an operator types, each carrying a
  `tools/<kit>/` literal, so the `WIRE-INTO-PROJECT.md` row of `tools/install-prefix-carried.txt` is
  raised by hand in this pass to exactly the count the file holds once the section lands, counted as
  `check-install-prefix.sh` counts it, with the kits column that count measures, and its reason
  column gains a sentence dated at this pass
  saying the new literals are the switch's commands, which a runbook carries as content rather than
  as a path to derive, as the 2026-09-08 raise recorded (§8 F7). Observed by AC7.

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
  points at, the `--write` verb with the argument shape its S1 pins, which step 4 spells, the two
  conf keys it sets, the kept-plus-added attribute, and the landing reconcile in its §4, which step
  6 follows.
- **consumes-from** `PLAY-dDerivedDocket-1` — the charter's `kit:unattended` blocks and what they
  carry, which S4 describes, and the `kit:kickoff-manifest` fence around the kickoff-manifest merge
  exception, which S6 names. Added by this spec, not in the brief's table.
- **consumes-from** `TOOL-dDerivedDocket-9` — gov's `.githooks/commit-msg`, the reference step 5 names
  for the transition audit's commit-time carrier, and the `memory-recall` kit that audit needs under
  builds mode, which step 4 names as a prerequisite because govkit installs nothing from unit 9's
  edge. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-10` — the row driver's refusal of a shard merged into a
  view, which is the reason S1 gives for keeping the backlog attribute, and the
  `row-driver view refusal` leg S2's step 4 tells an adopter to add, which that unit's F4 keeps off
  every kit. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-11` — `--plan` and the two worksheets step 1 files. Added
  by this spec.
- **consumes-from** `TOOL-dDerivedDocket-12` — `--stragglers` and `--recipe`, which steps 2 and 5
  name, and the landing form of `--ingest` (its S6), which step 6 names. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-13` — the gov-only straggler-guard library and
  `pre-rebase` hook, which step 5 names as the reference an adopter copies. Added by this spec.
- **consumes-from** `TOOL-dDerivedDocket-36` — the kit README's backlog-mode section the new
  section points at, and its signed-records row, which step 3 points at. Added by this spec.
- **hands-off** external — a scaffold that writes no authored shard when `BACKLOG_MODE="builds"` is
  declared before adoption, which would let a fresh tree start in builds mode.

## 4. Design

### The edits, by location

| Where, at `fb07ca25`, every citation unmoved from `abac6d59` | Now | After |
|---|---|---|
| `WIRE-INTO-PROJECT.md:123`, after the lexicon bullet | no kickoff-manifest bullet in §2's kit list | the S6 bullet |
| `WIRE-INTO-PROJECT.md:124`-`:126` | "keeps the `kit:unattended` block in `§1`, which is the ONE substitute…" | names the substitute, the landing pointer and the contract |
| `WIRE-INTO-PROJECT.md:172`-`:175` | "The scaffold writes `memory/` with `builds/`, `backlog/<FAMILY>.md`, …" | the shards named as the `shards`-mode default, with a pointer to §3a-asks |
| `WIRE-INTO-PROJECT.md:198`-`:201` | "two nodes appending to `DECISIONS.md` or a backlog shard" | the same, plus a build's `BACKLOG.md` |
| `WIRE-INTO-PROJECT.md:206`-`:209` | two attribute lines | three, and one sentence on keeping the backlog line |
| after `WIRE-INTO-PROJECT.md:213` | the drift-audit anchor follows | `### 3a-asks`, then the anchor |
| `tools/memory-tree/adopt-memory-tree.sh:281` | "> Mutable. Each row leads with one status token (OPEN…WONTDO)." | the id-first shape |
| `tools/install-prefix-carried.txt:11`, the `WIRE-INTO-PROJECT.md` row | pinned at 53 | raised by hand to the count once §3a-asks lands, with a dated reason (S7) |

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

1. **Census, read-only.** `python tools/memory-tree/migrate_backlog.py --plan --record <MEMORY_ROOT>/builds/<your-slug>/build --record-as <your-unit-id>`
   files the id census, the same-id worksheet and the triage worksheet as records of your build, and
   names every row it cannot parse. Without `--record` the planner prints and writes nothing. Fix the
   unparseable rows first: the writer never drops a row.
2. **Stragglers.** `python tools/memory-tree/migrate_backlog.py --stragglers` walks every local and
   remote-tracking ref for a branch still editing a shard. Merge the ones you know before the switch.
3. **Sign both worksheets.** Your owner decides which same-id pairs are one subject and gives every
   open ask on a finished build one disposition, as the two signed records the kit README's
   signed-records row describes — the header cells `Ask`, `Verdict` and, on the triage record,
   `Field`. Preview the result with
   `python tools/memory-tree/migrate_backlog.py --plan --signed <same-id record> <triage record>`;
   the writer applies exactly what is signed. This repo's own signing, under rules its owner
   delegated, is in `memory/builds/dDerivedDocket/`.
4. **Switch in ONE commit.** Install the memory-recall kit beside memory-tree first if you have not:
   the transition audit keys every row through its anchor grammar and refuses by name without it, and
   no kit descriptor installs it for you. Mint one ask id under your build's slug for the legacy holds
   that name no id, then run
   `python tools/memory-tree/migrate_backlog.py --write --as <your-slug> --signed <same-id record> <triage record> --triage-ask <that id>`.
   It files that ask with a KEEP in your build's `BACKLOG.md`, holds each such row on it, migrates
   the rows of your rotated backlog archives with the live ones, and removes the authored shards once
   its conservation proof passes. It does not remove the archives: delete every tracked backlog
   archive whose name starts with one of your families, because builds mode keeps no backlog archive
   and `gen_build_index.py --check` refuses one, and reword any file outside `<MEMORY_ROOT>` that
   names a deleted archive, which a dead-path gate reads from git history. Then set
   `BACKLOG_MODE="builds"` and the `ASK_CUTOFF` it prints, add the `BACKLOG.md` attribute from §3
   step 4, and run `python tools/memory-tree/gen_build_index.py --write`. Add a gate leg of your own
   running `python tools/memory-tree/merge-rows.py --check`; this repo calls it
   `row-driver view refusal`, and no kit ships it. Commit when `--check` exits 0.
5. **Tell stragglers what to do.** The recipe a pre-switch branch follows is what
   `python tools/memory-tree/migrate_backlog.py --recipe` prints, the same text the generated views
   carry. The hooks that tell a branch before it lands are yours to wire: this repo's
   `.githooks/straggler-guard.sh`, `.githooks/pre-rebase` and `.githooks/commit-msg` are the
   reference, and they are not shipped by any kit.
6. **Land it when your default branch moved.** If your default branch gained backlog rows while your
   switch build ran, the row driver's refusal prints the `--relocate` recipe, which is for a
   pre-switch branch merged into a switched default branch and exits 2 in this direction. Instead,
   on your switch branch, run `git merge --no-ff --no-commit <default tip>` and take your branch's
   side of every generated view and deleted archive; run step 1's `--plan` inside a worktree of the
   tip; sign the rows it adds as step 3 did; then run
   `python tools/memory-tree/migrate_backlog.py --ingest <default tip> --as <your-slug> --signed <same-id record> <triage record> --triage-ask <that id> --dry-run`,
   pass `--confirm <id>` only for an id your branch never acted on since it forked, re-run without
   `--dry-run`, write the `ASK_CUTOFF` it prints, run
   `python tools/memory-tree/gen_build_index.py --write`, and conclude the merge. This repo's own
   landing, with its confirmation rule and its manifest re-stamp, is §4 "The landing reconcile" of
   `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md`.

A census over a FORKED engine decides more before step 4: a status your tree reads as terminal that
the kit does not, ids from an era with no slug to route by, relative links that change depth. This
repo measured those for its three known adopters in section 10 of
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`.
```

`<version>` is the `KIT_MEMORY_TREE_VERSION` the tree declares at this unit's pass, read then and
not assumed here.

### Proposed text for the smaller edits

```markdown
- **A kickoff manifest** (`kickoff-manifest` kit): the per-project manifest `/session-kickoff` reads.
  Keeping it selected keeps the `kit:kickoff-manifest` block in `§1`, the manifest's merge exception;
  dropping it removes that exception with the manifest it governs.
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

`WIRE-INTO-PROJECT.md` · `tools/memory-tree/adopt-memory-tree.sh` · `tools/install-prefix-carried.txt`
(one row raised by hand, with its reason)

### Alternatives rejected

- **Routing a fresh adoption straight to builds mode.** It needs a scaffold that writes no authored
  shard, which is a change to the adopter's behaviour (§8 F1).
- **Folding the switch into the existing §3a.** That section retires a different product's shape
  under its own version line; mixing the two makes one heading answer two upgrade questions.
- **Copying the kit README's grammar into the runbook.** A second copy of the grammar is the one
  that rots (§8 F5).

## 5. Production-readiness checklist

- security — no new write path. The section names the one sanctioned cross-folder writer and says it
  runs only in an adopter's own switch-over commit and, when the default branch moved, in the merge
  that lands that switch (step 6), each time on worksheets its owner signed.
- perf / scale — N/A: prose and one header string. The census's cost is stated by the planner unit.
- error / empty / loading states — an absent `BACKLOG_MODE` reads as `shards` and the runbook says so
  first. The writer's refusals on an unsigned or unparseable input are the switch-over unit's, and
  step 1 tells the adopter to clear what the census could not parse.
- observability — the section names what an adopter reads at each step: the census record, the
  straggler list, the writer's conservation table and printed cutoff, and the generator's `--check`.
- risks — the section names commands other units built, so a renamed flag would strand an adopter;
  AC3 grades every name at this unit's pass. The concurrent adopter-wiring session may edit §3 step 4
  too, and the landing reconciles with whichever lands first. The attribute block now exists in both
  the runbook and the kit README, as it did at `abac6d59`.
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
- **AC3** — When every command §3a-asks names is compared with its tool's `--help` usage, each flag
  it names is listed and every argument the usage marks required for that verb appears in the step,
  except `merge-rows.py --check`, whose usage prints the merge driver's four positional arguments
  (`tools/memory-tree/merge-rows.py:1098-1104`) and which is resolved by running it below; every
  repository path the section names, the three reference hooks and the switch-over spec step 6 cites
  among them, is in `git ls-files`; in AC6's scaffolded fixture, with one legacy row appended to a
  scaffolded shard and one rotated backlog archive named for a declared family committed beside it,
  step 1's command as the section spells it writes the census summary and the three worksheets under
  the named directory, and, given two signed records written by hand in the header shape the kit
  README's signed-records row states, step 4 as the section spells it migrates both rows, and with
  the archive deleted as step 4 says, `gen_build_index.py --check` exits 0 and
  `python tools/memory-tree/merge-rows.py --check` exits 0 printing its `merge-rows: check ·`
  liveness line; and each of the six numbered steps names at least one command this criterion
  resolves, or a row of `tools/memory-tree/README.md`'s backlog-modes section that exists at the
  pass; and step 4 names the memory-recall kit before its first command.
  Red when: a producing unit spelled a verb other than the design did, `--straggler` for
  `--stragglers`, and the runbook kept the design's spelling; or a step runs a verb without the
  arguments its usage requires, so a bare `--plan` writes nothing or a bare `--write` has no signed
  input, and an adopter is stranded at a command that does not do what the step says; or step 4
  omits the archive deletion, so an adopter whose tree ever rotated a backlog shard meets a `--check`
  that never exits 0; or `merge-rows.py --check` is graded against usage text that names no
  `--check` and marks three paths required, so AC3 reds on a correct driver or is waved through; or
  a step names neither a command nor a README row, so an adopter reaches it with no command and no
  format; or step 4 drops the memory-recall prerequisite, so an adopter's first builds-mode hygiene
  run refuses check 25 by name after its switch commit has landed.
  figure: the flag and path sets are DERIVED from the section at observation time.
- **AC4** — When `grep -n 'BACKLOG_MODE' WIRE-INTO-PROJECT.md` runs, every hit sits inside §3a-asks,
  one of them states that an absent key reads as `shards`, and §3 step 2 carries a pointer to
  §3a-asks.
  Red when: `BACKLOG_MODE="builds"` is written into §3's first-adoption steps, so a fresh adopter
  switches before any census exists and `--write` has no signed worksheet to apply.
- **AC5** — When `grep -n 'kit:unattended' WIRE-INTO-PROJECT.md` locates §2's bullet on the
  unattended kit, that bullet names the landing-rule pointer and the protocol contract beside the
  explicit-ask substitute, and states no count of blocks; and
  `grep -n 'kit:kickoff-manifest' WIRE-INTO-PROJECT.md` finds one bullet in §2's kit list saying that
  keeping the kit keeps §1's merge exception.
  Red when: it still describes only the ask substitute, so an operator dropping the kit is not told
  that the landing pointer and the contract leave with it; or no bullet names the kickoff-manifest
  block, so an adopter who deselects that kit loses the merge exception from its charter unnoticed.
- **AC6** — When `bash tools/memory-tree/adopt-memory-tree.sh --scaffold` runs in the scratch
  fixture, each scaffolded `memory/backlog/*.md` quotes the row shape with the id before the status
  token, `grep -c '^- '` prints 0 for every shard, and `bash tools/memory-tree/check-memory-hygiene.sh`
  over the scaffolded tree exits 0.
  Red when: the example row is written on its own `- ` line, which the zero count reports and the
  row driver would read as a row in every fresh shard.
  fixture: a scratch git repository holding a copy of the kit directory and a `.memory-tree.conf`
  copied from `tools/memory-tree/.memory-tree.conf.example`, committed before the scaffold runs.
  Measured at `abac6d59` on 2026-09-14: the scaffold wrote three shards and the hygiene gate exited 0 with
  0 graded rows.
  cost: under a minute.
- **AC7** — When `bash tools/check-install-prefix.sh` runs at this unit's commit, it prints no `ROSE`,
  `SLACK` or `SWAPPED` line for `WIRE-INTO-PROJECT.md`, and that file's row in
  `tools/install-prefix-carried.txt` carries a reason sentence dated at this pass naming §3a-asks.
  Red when: the section lands with the row unraised, so the `install-prefix (shipped surface)` leg
  DEPL's own §7 lists reds with ROSE at the post-build bar, where no pass is left to fix it; or the
  row is raised past the count the section carries, or its kits column is left behind the literals,
  which the same leg reds as SLACK or SWAPPED; or the row is raised with no reason, which the list's
  header reserves to a person writing one in the pass that needs it.
  permission: the script is the `install-prefix (shipped surface)` leg and binds at the one
  post-build bar; in the pass the raise is observed by reading the row and counting the section's
  literals.

## 7. Gates

`memory hygiene` · `playbook parity` · `install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

No new gate arm. The runbook's entry-anchor checker is on no bar at `abac6d59` or at `fb07ca25`, so
AC2 reads the position directly. `memory-hygiene self-test` is the one HELD leg in the list above:
it reads `subject = kit` in `tools/gate-legs.json` at HEAD, so a plain bar PRINTS it held and runs
it not at all. The run that covers it is the one after the last unit,
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, which this build owes because it
is kit work; `GATE_FULL=1` alone would still hold it. Every other leg in the list is
`subject = repo` and runs on any bar, so nothing else here waits on the self-test flag.

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
  the version its earlier units set is the one that dates this edit on the default branch.
  RESOLVED (agent, 2026-09-14, delegated): (b).
- **F7** — How do the switch's commands meet the carried-prefix pin on this runbook? (a) Raise the
  row by hand in this pass with a dated reason. (b) Spell the commands relative to the kit directory,
  without the `tools/` prefix. (c) Leave the pin. (b) hands an operator a variable to expand, the
  reason the 2026-09-08 raise gave, and AC3 resolves commands against tracked paths; (c) reds the
  post-build bar with no pass left to fix it. RESOLVED (agent, 2026-09-16, delegated): (a), the route
  the checker's own refusal names, as the prompt-authorized `aReapedSpinner` run took it.
- The ruling this unit carries out and does not revisit: D1, adopt per-build asks with a generated
  view while adopters keep the shards default, RESOLVED (owner, 2026-09-13).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds seven edges the brief's table does not list: one
  consumes-from the charter unit, `PLAY-dDerivedDocket-1`, and one from each unit whose commands or
  texts the new section names (9, 10, 11, 12, 13 and 36). Their producer ends are not written,
  because those specs are other writers'; this spec is Tier-1, so the hygiene gate's edge joins do
  not grade either end.
- rev-2 · 2026-09-14 · spec-audit G5 round 1 fold. M15 (29): step 3 names
  `--plan --signed` and the kit README's signed-records row with the header cells `Ask`, `Verdict`
  and `Field`; S2 says each step names a command or that row; consumes-from 36 names the row; AC3
  checks every step. M16 (41, 64): step 1 spells `--plan --record … --record-as …`, step 4 spells the
  argument shape `TOOL-dDerivedDocket-34` S1 pins, `--write --as --signed --triage-ask`, with the
  triage ask and the shard removal it performs; consumes-from 34 names that shape; AC3 resolves each
  command's full argument shape and runs step 1 on a fixture. L5 (47): corrects rev-1 — the producer
  ends of the edges from units 10, 11, 12, 13 and 36 and from PLAY-dDerivedDocket-1 are written in
  those specs, and unit 9's, the only one missing, is added in unit 9's rev-2. Orchestrator, after
  the fold: unit 10 hands off the `row-driver view refusal` leg and its F4 says an adopter adds it
  when it switches, but S2's step 4 never said so; step 4 now tells the adopter to add a leg running
  `merge-rows.py --check`, AC3 resolves that command, and consumes-from 10 names the leg.
- rev-3 · 2026-09-16 · spec-audit round 2 fold. G5 M16 (19, 42): step 4 deletes the family backlog
  archives builds mode refuses and rewords their carriers; S2. G5 M17 (58): new step 6 lands the
  switch through the landing form of `--ingest` when the default branch moved, pointing at unit 34's
  reconcile; S2, consumes-from 12 and 34. G5 M18 (18): AC3 resolves `merge-rows.py --check` by running
  it and reading its liveness line, and runs steps 1 and 4 over a fixture holding a rotated archive.
  G5 M19 (41): new S7 raises the carried-prefix row by hand, Files touched, new AC7; §8 F7. G5 L6
  (34), DEPL end: new S6 adds a kickoff-manifest bullet to §2's kit list; §4 edits row and proposed
  text; AC5; consumes-from PLAY. G2 M5 (16, 31, 48), DEPL end: consumes-from 9, S2 and step 4 name the
  `memory-recall` prerequisite unit 9 §8 F6 hands off. Fold verification: AC3 reads the
  memory-recall prerequisite in step 4, which no criterion observed; AC7 and S7 name `SLACK` and
  `SWAPPED` beside `ROSE`, the leg's other two verdicts on a raised row; §5 security names step 6's
  landing merge as the writer's second commit; §4 edits table gains the carried-prefix row.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). No scope, design or criterion moved.
  `WIRE-INTO-PROJECT.md` changed only past line 535 (dPolishedVitrine's migration blocks and
  aReplayedCard's card wiring), so every runbook line §2 S2, S4 and §4 cite sits where `abac6d59` had
  it; the carried-prefix row S7 raises still reads 53; the scaffold header at
  `tools/memory-tree/adopt-memory-tree.sh:281` and the usage lines AC3 cites are unchanged; the
  three fixture replicas §3 keeps are still three; the shipped example conf AC6 copies gained only
  a blank `SPEC_DIRECT_CUTOFF` row the hygiene engine does not read. The three reference hooks
  step 5 names are still absent, as units 9 and 13 create them. §7's prose names the one
  post-build bar, under owner ruling TOOL-aProbedUnit-8. §10.
  Extended 2026-09-20 by the regrounding consolidation, which changed no scope, design or criterion
  here and checked each of its four build-wide rules rather than assuming it. Suite permissions: no
  criterion observes a `.test.sh` or `selftest.py` FILE invocation, a merge bar or a
  `GATE_FULL=`/`GATE_SELFTESTS=` prefix; AC7 already defers its leg; and AC3's and AC6's runs of
  `gen_build_index.py --check`, `merge-rows.py --check`, the scaffolder and the hygiene engine all
  happen inside AC6's scratch fixture, which the child prompt in
  `tools/workflows/unattended-unit.js` names among the direct checks a pass may use, so none is
  deferred. §7 adds no arm, so no `New arm:` third field exists to price. AC6's `grep -c '^- '` zero
  is read over a tree the scaffolder writes in the fixture rather than over HEAD, so it is not the
  already-green class, and no other criterion asserts a phrase counts zero. And this unit touches
  no capped carrier: `WIRE-INTO-PROJECT.md`, `tools/memory-tree/adopt-memory-tree.sh` and
  `tools/install-prefix-carried.txt` each carry no row in `tools/template-size-limits.txt`.
  Extended again 2026-09-20 by the closing consolidation, which moved nothing in this spec and
  states why. The build-wide capped-carrier rule tightened from a ceiling to NET ZERO, and this unit
  writes no capped carrier, so it owes no trim and no size criterion — the three files above were
  re-checked against `tools/template-size-limits.txt` rather than carried over. The orchestrator
  ratified the deferral reading this spec already applies: a gate-leg command or a suite FILE
  invocation defers to the run at VERIFYING, while a checker run inside a fixture, a `--selftest`
  flag and a read-only verb stay in the pass, which is what keeps AC3's and AC6's fixture runs where
  they are and AC7's leg deferred. The header date moves to the last-change date, 2026-09-20, with
  the rev kept.
  Extended again 2026-09-20 by the close-out pass, which moved two words and no figure. This spec
  wrote BASE for `abac6d59` in six places while its header declares `fb07ca25`, the same
  contradiction of one word for two commits that the orchestrator ruled on for the charter unit of
  this build; every use now
  names a commit, §10 states that, and nothing measured changed. §7's prose now names the HELD leg
  it lists and the run that covers it in the orchestrator's own terms: `memory-hygiene self-test`
  reads `subject = kit` in `tools/gate-legs.json` at HEAD, so the bar after the last unit is
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` and a plain bar leaves that leg
  held. The full command is spelled in §7 prose rather than in an acceptance bullet or the leg-list
  line, the two places `tools/check-spec-tokens.py`'s bar join reads, so it adds no graded token.
  The other three closing rulings reach nothing here: this unit writes no capped carrier, so the
  net-zero rule and its 2048-byte scoping are both inapplicable; it adds no key to
  `tools/unattended/.unattended.conf.example` and sets none in `.unattended.conf`, so it owes no
  section 8 key-table row; and AC3's and AC6's fixture runs already read the narrow rule the
  orchestrator ratified. The header date already reads 2026-09-20 and the rev is kept.

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

EVERY MEASUREMENT IN THIS SPEC NAMES ITS SHA. This spec wrote BASE for `abac6d59`, the commit it was
drafted and audited at, while its header declares `fb07ca25` and four sibling specs of this build
declare BASE to BE `fb07ca25`; one word for two commits is a contradiction a reader cannot resolve,
so every use now names a commit and the word is gone. No figure moved with the spelling.

Where the design and the source disagree at `abac6d59`, re-verified here:

- Design §11 and §15's U6 say the attribute is retargeted; §18 rev-3 A2 and the switch-over's spec
  keep it and add one (§8 F3).
- Design §10's per-adopter facts were measured at `09a22d2b` for three named adopters. The runbook
  points at them rather than copying a measurement that will move.
- The scaffold header text also appears in gov's four live shard headers and in three test
  fixtures. The shard headers are the switch-over's; the fixtures are inert (§3).
- At `fb07ca25`, the base this spec is regrounded on, the runbook changed only past line 535, so §2
  and §4's line citations hold; the `WIRE-INTO-PROJECT.md` row of
  `tools/install-prefix-carried.txt` still reads 53; `tools/memory-tree/adopt-memory-tree.sh:281`,
  `tools/memory-tree/merge-rows.py:1098-1104` and the replica count are unchanged. No landed build
  adds a backlog mode, a `BACKLOG_MODE` key or a runbook switch section, and `.githooks/` holds no
  `straggler-guard.sh`, `pre-rebase` or `commit-msg` yet.

Recall terms used: `WIRE-INTO-PROJECT runbook migrate adopter shards scaffold header merge=rows attribute ledger retired status-first`
