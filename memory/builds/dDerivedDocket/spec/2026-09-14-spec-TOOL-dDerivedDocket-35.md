# TOOL-dDerivedDocket-35 — arming and the real-tree staged reds

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 35

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g5-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g5-round1.md) | spec-audit | TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Every ask-driven path this build adds lands dark behind a blank `ASKS_CMD`, and the straggler guard
has been proven only on fixtures. Once the switch-over has put this repo in builds mode, set gov's
`ASKS_CMD`, which arms the ask-driven driver, the `asks-disposed` item, the leg's second opinions and
the inherited-red auto-file together. Then stage each guard's failing case against this repo's own
post-switch content and watch it red, because a guard proven only on a fixture has been proven
against the fixture.

## 2. Scope (IN)

- **S1** Gov's `.unattended.conf` sets `ASKS_CMD` to the memory-tree generator's `--asks` mode, in
  exactly the form the conf-example entry the ask-driver unit ships documents, so the driver's
  appended arguments reach `tools/memory-tree/gen_build_index.py`. `PROBE_ALLOW` in
  `.memory-tree.conf` stays blank, as owner ruling D12-e ships it. Observed by AC1 and AC2.
- **S2** One scratch clone of this unit's commit, whose `origin` is a local bare repository seeded
  from that commit, whose `core.hooksPath` is set to its own `.githooks`, and whose
  `merge.rows.driver` is set to the value this node carries, since a clone copies no local config.
  Every staged break below
  runs there, so the corpus a break is graded against is this repo's real post-switch content, and
  nothing a break writes can reach the repository or its remote. The clone's `.memory-tree.conf`
  declares one extra family, `EXMP`, used by the scratch fixtures alone, so every id a RED prints is
  either a real id the corpus defines or an `EXMP` id. Observed by AC7.
- **S3** The ask driver's RED: a scratch build README landed on the scratch remote's default branch,
  whose `asks:` names an id no `BACKLOG.md` files; `unattended.sh --preflight` on it refuses naming
  property P5 and the id. Observed by AC2.
- **S4** The `asks-disposed` RED: a scratch mandated run whose one mandated ask is filed and carries
  no disposition and no closing spec; `unattended.sh --close` on it refuses naming `asks-disposed`
  and the ask among its unmet items. `--close` evaluates every item and `gates-green` runs
  `GATE_CMD`, so the scratch clone's `.unattended.conf` sets `GATE_CMD` to `false`: no bar runs in
  this unit, and `gates-green` reads unmet at once. Observed by AC3.
- **S5** The leg's RED: a typed resolution table in that scratch run's folder whose first cell
  anchors an ask id filed in another folder; `bash tools/unattended/check-unattended.sh` fails
  naming the folder-wide anchor ban and the id. Observed by AC4.
- **S6** The straggler hook's RED: a branch forked from this build's pre-switch BASE, staging an edit
  to a backlog shard; `git commit` is refused by `.githooks/pre-commit`, which prints the relocation
  recipe. Observed by AC5.
- **S7** The transition audit's RED: that branch commits a shard row change with `--no-verify` and
  is merged into the scratch default branch with `git merge --no-ff`. The row driver stops the merge
  on the shard-into-view conflict; the scratch resolution takes the default branch's view and runs
  `git commit`, which `.githooks/commit-msg` refuses. Concluded with `--no-verify`, the merge makes
  `bash tools/memory-tree/check-memory-hygiene.sh` fail check 25 naming the merge, the id and the
  change commit. Observed by AC6.
- **S8** Every RED is copied verbatim into this unit's acceptance ledger, and the scratch clone is
  removed afterwards with its read-only git objects cleared first. The real tree carries only this
  unit's declared writes. Observed by AC7.
- **S9** This build's own asks after arming. Its close is the first one graded with `ASKS_CMD` set,
  so every ask homed in `memory/builds/dDerivedDocket/BACKLOG.md` must already be terminal or carry
  a disposition row there, and the unit records the list it read. Observed by AC8.
- **S10** The kickoff manifest's `last-audit` is re-stamped in the same commit, with a delta line in
  the commit message, because `.unattended.conf` is in its `watch:` list and the staged leg refuses a
  watched change without one. The §B claims that file feeds are re-read first. Observed by AC9.

## 3. Non-goals (OUT)

- No pilot run. DR §19.8 closes U15 with "the first ask-driven pilot, over a READY set the owner
  picks", and owner ruling D12-a makes every ids-driven run start from a README the owner lands.
  This run cannot land one and may not write its own authorization, so the pilot is the owner's.
- No change to what any guard decides. Each verdict here was built, and armed in its own suite, by
  the unit that owns it; this unit observes them on real content for the first time.
- No staged RED of the inherited-red auto-file. The inherited-red unit records that none is owed
  here; the auto-file goes live with S1 and is exercised by the first inherited red a later bar meets.
- No auto-resume setting. That unit ships it on in the kit and in gov by its own ruling.
- No stage of a break on the working tree. A checkout that removes a break restores the whole file,
  and the switch-over's edits sit in most of the files a break would touch.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-34` — a builds-mode tree with rendered views and filed asks.
  Without it `ASKS_CMD` has no `BACKLOG.md` to read and every break below grades an empty corpus.
- **consumes-from** `TOOL-dDerivedDocket-16` — the `ASKS_CMD` contract, its conf-example entry and
  property P5 at preflight, which S1 spells gov's value against and S3 stages. Added by this spec;
  the brief's table does not list it.
- **consumes-from** `TOOL-dDerivedDocket-17` — the `asks-disposed` item and its terms, which S4
  stages on a scratch run.
- **consumes-from** `TOOL-dDerivedDocket-18` — the folder-wide anchor ban, which S5 stages.
- **consumes-from** `TOOL-dDerivedDocket-13` — the pre-commit refusal on a pre-switch branch, which
  S6 stages.
- **consumes-from** `TOOL-dDerivedDocket-9` — check 25 and the `commit-msg` carrier, which S7
  stages. Added by this spec; the brief's roster note for this unit names it.
- **hands-off** external — the first ask-driven pilot: the owner lands a README with
  `gen_build_index.py --new-build <slug> --asks <ids>` and starts `/unattended <slug>`.

## 4. Design

### What "the real tree" means here, and why a scratch clone

DR §19.8 says "Stage RED on the real tree, confirm, and unstage". Three of the five breaks cannot be
staged in the working tree at all. A preflight reads its authorization from a README the remote's
default branch carries, so a staged README is refused for authorization before P5 is ever asked,
and the RED would be the wrong refusal. The `asks-disposed` and anchor-ban breaks need a mandated
run, which this build is not. And the two hook breaks need a pre-switch branch and a merge into the
default branch, which on the real repository would be the very straggler the guard exists to stop.

So the breaks run in one clone of this unit's commit, with a bare remote seeded from it as `origin`.
Everything a guard reads in that clone is this repository's content at that commit: the rendered
views, every filed ask, the real specs, the conf that S1 just armed. Only the scratch README, the
scratch run and the scratch branch are fixtures, and each is the smallest addition that reaches the
refusal under test. That is the same method D12-h names for driver breaks, pointed at real content
instead of an empty fixture.

### The breaks, and the refusal each must reach

| Unit | Break | Command | The RED must name |
|---|---|---|---|
| ask driver | `asks:` names an id no `BACKLOG.md` files | `unattended.sh --preflight <scratch-slug> --keepalive-id <id>` | P5 and the id |
| asks-disposed | a mandated ask filed, undisposed, unclosed | `unattended.sh --close <scratch-slug>` | `asks-disposed` and the ask |
| leg second opinions | a table row whose backticked first cell is a foreign ask id | `bash tools/unattended/check-unattended.sh` | the anchor ban and the id |
| straggler hook | a pre-switch branch staging a shard edit | `git commit` | the recipe's `--relocate` line |
| transition audit | an unaccounted shard change merged into the default | `git merge --no-ff`, `git commit`, then `check-memory-hygiene.sh` | at `commit-msg`, the unaccounted id; at the audit, the merge sha, the id, the change commit |

Two scratch builds are needed, both landed on the scratch remote's default branch before any
preflight, because P5 and authorization read the tree that remote advertises. The first names an
unfiled id and exists only to be refused (S3). The second files its one mandated ask in its own
`BACKLOG.md`, so its preflight succeeds and S4 and S5 have a mandated run to stage against.

A RED that names something else is not the RED. The scratch README must pass authorization so that
P5 is the refusal reached; the resolution table's first cell must be backticked rather than
link-wrapped, because a link-wrapped cell does not anchor (DR §5.3); and the merge must be a real
merge, because a squash leaves no transition for the audit to see (design §18r.6, hole 1).

### What S1 arms beyond the three items

`ASKS_CMD` is the single switch every ask-aware path keys on. Setting it arms the driver's preflight
properties and roster, the `asks-disposed` item, the leg's second opinions, and the inherited-red
unit's auto-file, which that unit's own spec keys on the same key. The last one means the next bar
that meets an inherited red under `INHERITED_RED=land` writes an ask into the run's own
`BACKLOG.md`, which is intended.

### This build's own close

With `ASKS_CMD` set, `asks-disposed` evaluates this build at its close. The build carries no
`asks:` fact, so its term is T0 when nothing is homed in its folder and T3 over F otherwise. After the
switch-over, this build's `BACKLOG.md` holds the signed triage dispositions and the superseding
disposal, and any ask this run filed as a discovery. S9 reads the folder's asks through
`gen_build_index.py --asks --all --json` at this unit's commit and records each with its status, so
the close cannot be the first place an undisposed ask of this run is noticed.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| gov's `ASKS_CMD` value | conf value | none; its key is the ask-driver unit's |
| the scratch slug, branch, run and ask ids | fixtures inside the scratch clone | ids in the `EXMP` family the clone alone declares; all deleted with the clone |

### The ids a copied RED carries

Each RED is copied verbatim into a tracked ledger, and hygiene check 14 counts every real-family id
a tracked record cites and nothing defines. So no fixture may carry a real-family id. The scratch
asks, the scratch run's unit and the unfiled id are `EXMP` ids, which the scratch conf declares so
the guards parse them and the real tree's check 14 ignores. The foreign ask in S5 and the shard row
in S6 and S7 are real ids the corpus already defines, so citing them is a citation of a defined id.

### Files touched (estimate)

`.unattended.conf` · `memory/guides/SESSION-KICKOFF.md` (the stamp) · this unit's acceptance-ledger
journal under `memory/builds/dDerivedDocket/build/`.

### Rollout

1. Reground, and confirm units 9, 13, 16, 17, 18 and 34 read CLOSED.
2. Set `ASKS_CMD`, re-read the manifest's claims, re-stamp, and commit.
3. Clone that commit into the scratch directory with a bare remote, and set its hooks path.
4. Stage each break in the order of the table, confirm its RED, and copy it into the ledger.
5. Read this build's own asks, record them, and remove the scratch clone.

### Alternatives rejected

- **Breaks on the working tree, removed by checkout.** Rejected in §3: three breaks cannot reach
  their refusal there, and a checkout restores whole files.
- **Breaks on an empty fixture repository.** That is what each guard's own suite already does; it
  proves the guard against the fixture and says nothing about this repo's content.
- **A separate switch per armed path.** One key is what the ask-driver unit shipped, and a second
  key for the auto-file would let a run arm half of the ask path.

## 5. Production-readiness checklist

- security — the only repository write is one conf value and the manifest stamp. Every break writes
  inside the scratch clone, and its remote is a local bare repository, so no break can push anywhere
  real. `PROBE_ALLOW` stays empty, so no filed `seen` command becomes executable.
- perf / scale — one clone of the repository and five short commands; the hygiene run is the
  longest step.
- error / empty / loading states — a RED that names the wrong refusal is recorded as a failure of the
  staging, not as a pass; a scratch step that fails to set up stops the rollout with the reason.
- observability — five verbatim REDs and the list of this build's own asks, in the ledger.
- risks — the scratch clone leaking on Windows, where read-only git objects defeat a plain removal,
  as `TOOL-aBranchedMandate-6` measured; S8 clears the bit first.
- testing — this unit IS the real-content test of five guards; each guard's arms are its own suite's.
- migration — none: the value is new, and adopters keep the blank default until their own switch.
- user docs — none here; the Skill and the protocol already document `ASKS_CMD` through the units
  that added it.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs on the real tree after this unit, it
  exits 0 with gov's `ASKS_CMD` non-blank and its protocol row present.
  Red when: the value is set in the kit's example and not in gov's `.unattended.conf`, so every run
  here still takes the not-adopted path.
- **AC2** — When `unattended.sh --preflight` runs in the scratch clone on a landed README whose
  `asks:` names an unfiled id, it refuses naming P5 and that id.
  Red when: the refusal is the authorization refusal, because the README never reached the scratch
  remote's default branch, and P5 was never asked.
- **AC3** — When `unattended.sh --close` runs on the scratch mandated run, it refuses, and among its
  unmet items it names `asks-disposed` and the undisposed ask.
  Red when: the item reads T0, not adopted, because the scratch clone's conf was not the armed one.
  cost: seconds, because the scratch `GATE_CMD` is `false` and no bar runs.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs in the scratch clone with the typed
  table in place, it fails naming the anchor ban and the foreign id.
  Red when: the table's first cell is link-wrapped, which anchors nothing and stages no break.
- **AC5** — When `git commit` runs on the scratch pre-switch branch with a shard edit staged, it is
  refused and the output carries the recipe's `migrate_backlog.py --relocate` line.
  Red when: the clone's `core.hooksPath` is unset, so no hook runs and the commit lands silently.
- **AC6** — When the scratch straggler is merged with `git merge --no-ff` and the conflict is
  resolved to the default branch's view, `git commit` is refused by `.githooks/commit-msg`;
  concluded with `--no-verify`, `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 naming the
  merge sha, the id and the change commit.
  Red when: the merge is a squash, which leaves no transition, so the audit is silent and the RED is
  never observed.
  cost: one hygiene run in the scratch clone, minutes.
- **AC7** — When `git status --porcelain` runs in the worktree after the scratch clone is removed, it
  lists nothing beyond this unit's declared writes, the scratch directory no longer exists, and
  `bash tools/memory-tree/check-memory-hygiene.sh` names no orphan id in the ledger that copied the
  REDs.
  Red when: a fixture carried a real-family id, which the copied RED then cites and check 14 reds as
  defined nowhere.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --asks --all --json` runs at this unit's
  commit, every ask homed in this build's `BACKLOG.md` is terminal or carries a disposition row
  there, and the journal lists each.
  Red when: an ask this run filed is left undisposed, which this build's own close would then red.
- **AC9** — When `bash skills/session-kickoff/manifest-check.sh` runs on the unit's commit, check 5
  passes with the re-stamped `last-audit`.
  Red when: the conf moves with no re-stamp, which the staged leg refuses at the commit.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `kickoff-manifest ratchet` · `drift-audit records`

No new gate arm. Each break is armed in the suite of the unit that built its guard; this unit
observes them on real content.

## 8. Open questions

- **F1** — Where do the breaks run? Options: (a) the working tree, removed by checkout; (b) an empty
  fixture repository; (c) a scratch clone of this unit's commit with a local bare remote. (a) cannot
  reach three of the refusals and restores whole files; (b) is what each guard's suite already does.
  RESOLVED (agent, 2026-09-14, delegated): (c).
- **F2** — Does the pilot run here? RESOLVED (agent, 2026-09-14, delegated): no. Owner ruling D12-a
  requires an owner-landed README for every ids-driven run, and this run may not write its own
  authorization; the recipe is handed to the owner.
- **F3** — Which breaks does this unit owe? DR §19.8 names three, and the brief adds the straggler
  hook and the transition audit, which DR's superseded §18.6 had given the switch-over and which the
  switch-over's spec does not stage. RESOLVED (agent, 2026-09-14, delegated): all five, since each
  guard's owner hands its real-content RED here or the brief assigns it.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds two edges the brief's table does not list,
  consumes-from units 16 and 9, whose guards S3 and S7 stage.

## 10. Reuse audit

Nothing is built, so the reuse is of methods and verdicts. The scratch-repository-with-bare-remote
method is D12-h's route (b), which the driver and lander specs of this build already use for their
own cases; this unit points it at a clone of real content. Each verdict is the owning unit's:
P5 in the ask driver, the `asks-disposed` terms, the folder-wide anchor ban, the pre-commit refusal
and check 25. `python tools/codebase-map/reuse_lookup.py "stage a break on a scratch clone of the
real tree and confirm the gate turns red"` returned name-stem neighbours only, `tree` in the recall
selftest and `load_map_tree` among them, and it reports `.sh` as an unscanned layer; no seam stages
breaks for another unit. Recall returned DR §18.6's original assignment of the straggler RED to the
switch-over, the straggler-hook unit's hand-off here, and `TOOL-aBranchedMandate-6` on scratch
repositories leaking on Windows, which S8 answers.

Where DR and this build's specs disagree: DR §19.8 lists three breaks and gives U15 a pilot; the
brief adds two breaks and D12-a moves the pilot to the owner (§8 F2, F3).

Recall terms used: `staged RED real tree arm dark default-OFF flag flip scratch clone bare remote
unstage checkout`
