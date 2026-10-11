# TOOL-aOrientedCast-9 — the unattended Skill and verbs pass the renderer's `roles` to every harness call

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-2 · base 646d4a73581393acbf42f33864a9808c96d00a0c · streams tooling · order 6 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |

<!-- /gen:spec-records -->

## 1. Goal

An unattended run composes its harness calls from the verbs carrier, which names no `roles`. From
the spawn guard's landing every such call is refused at the tool call, and from the write gate's
every untyped builder is refused its writes, gov's own concurrent runs included. This unit gives the
verbs carrier one rule: every call to the build, unit and review harnesses carries the `roles`
object the handoff renderer's `harness-args` prints, and a typed unit's divergence is answered by a
spec revision instead of a stop. An adopter without the roles kit passes none, and its harnesses log
their per-stage fallback.

## 2. Scope (IN)

- **S1** — The verbs carrier's "Drive the build as ONE program" bullet gains the rule, spelled once:
  every `Workflow` call to `unattended-build.js` and `unattended-unit.js`, and the closing review's
  `tier2-review.js` call that M8 composes, carries `roles`, the JSON the roles kit's
  `handoff.py harness-args <harness>` prints for that harness. Observed by AC1 and AC5.
- **S2** — The same rule names the two cases that pass no `roles`. With no `.claude/roles.json` the
  roles kit is not installed: the call carries no `roles`, and each harness logs its per-stage
  fallback. A session started before the rendered agent types existed cannot spawn them: it passes
  none either, and once the spawn guard has landed it holds and a fresh session takes over. Observed
  by AC1.
- **S3** — The bullet's stop rule distinguishes a divergence. A child returning `diverged: true`
  stopped before its code on the spec section its `why` names, so the main loop has that spec revised
  by the spec-writer role through a rendered handoff, as the `/build` Skill's stage 5 does, and then
  dispatches the unit again. Any other `committed:false` still stops the loop. Observed by AC2.
- **S4** — The bullet's deferred-review sub-bullet promises an on-disk result only where one exists:
  the returned judges' results are on disk where the audit ran them untyped, under
  `workerType: 'none'`; under `roles` none is, and the hand-back's `next` says the re-run dispatches
  every judge again. Observed by AC3.
- **S5** — `memory/guides/UNATTENDED-VERBS.md` is re-installed from the template by
  `adopt-unattended.sh` in the same commit and stays byte-identical to it. Observed by AC4.

## 3. Non-goals (OUT)

- The unattended Skill, as §8 F1 resolved. Its drive line names the two build harnesses by
  `scriptPath` and no argument of either; `scratch`, `base` and `specAudit` are composed in the verbs
  carrier, which the Skill names as winning any difference, and `roles` joins them there. The Skill
  measures 10239 of its 10240-byte ceiling. AC6 observes it unmoved.
- M8's call block in the memory-tree kit's BUILD-METHOD template, which shows the closing review's
  arguments without `roles`. The rule here and the `/build` Skill both add `roles` to M8's
  composition; the block itself is the external hands-off below.
- The driver's relaunch line in `unattended.sh`, which says a deferred review's files exist "where it
  ran under workerType 'none' as the build harness's audit does". Under `roles` the audit no longer
  does, and the line's own next clause already covers a review under a named type. It is product code
  outside this unit's write set, named in the same hands-off.
- The harnesses, the renderer, the catalogue and the two guards. This unit edits text a caller reads.
- A kit-version bump. The unattended kit moves once, in the run's mint commit.

**Why this unit may edit a governance carrier.** `UNATTENDED-VERBS.md` is the unattended protocol's
companion, a governance carrier, and M3's veto 2 reserves a change to one for the owner. This edit
is inside the build's brief item 5, "The build harnesses take their role text and agent type from
the catalogue", and inside the owner-confirmed goal that spec writing, spec review, building and
closing review run only in their role agents, "attended or unattended". Without it the two guards
refuse every untyped unattended harness call and builder from their landing. The run added this unit
with `--rescope add` after the M2 cross-read.

### Edges

- **consumes-from** `TOOL-aOrientedCast-2` — the harness-arguments verb whose output the rule passes.
  Without it the rule names a command that does not exist.
- **consumes-from** `TOOL-aOrientedCast-4` — the build and unit harnesses' stage keys, `builder` and
  the audit's three review keys included, the unit harness's `diverged` field S3 branches on, and the
  audit hand-back's durability branch S4 describes. Without it `roles` is an argument the two build
  harnesses do not read.
- **consumes-from** `TOOL-aOrientedCast-5` — the review harness's stage keys, which the closing
  review's `roles` carries.
- **hands-off** `TOOL-aOrientedCast-6` — the write gate that refuses an untyped builder; from its
  landing an unattended unit pass is admitted only when this rule typed it.
- **hands-off** `TOOL-aOrientedCast-7` — the spawn guard that refuses a harness call with no `roles`;
  from its landing an unattended harness call is admitted only when it follows this rule.
- **hands-off** external — a run already in flight whose session read the verbs carrier before this
  text. Reconciling with a main that carries the two guards does not by itself bind it: on the landing
  node the guards bind from the moment the landing merge is in the primary tree, because hooks run
  from there. From then its next harness call without `roles` is refused at the tool call, the refusal
  naming the harness-arguments verb, and its untyped builder is refused every product write. It cannot
  comply from the session it is in, whose agent registry predates the rendered types, so a typed
  spawn would not start. It holds, and a fresh session takes it over through the verbs carrier's
  Resume path and reads this rule from the reconciled tree.
- **hands-off** external — M8's call block in the memory-tree kit's BUILD-METHOD template gaining
  `roles`, and the driver's relaunch line in the unattended kit's driver dropping its claim that the
  build harness's audit runs untyped; both are carriers outside this build's write sets.

## 4. Design

### Evidence

Read at `646d4a73` on 2026-10-11, node a; `git diff --stat 646d4a73 HEAD` over `tools`, `skills`,
`memory/guides` and `.claude` prints nothing at HEAD `ee951807`.

- `adopt-unattended.sh` RENDERS the Skill from `SKILL.template.md`, substituting its tokens, and
  COPIES the verbs carrier from `VERBS.template.md`, because it "carries no placeholder"
  (`tools/unattended/adopt-unattended.sh:391-396`). Its `--check` compares the installed copy with the
  template with no normalisation (`:534-539`), and check 10 of the unattended kit gate compares the
  same pair (`tools/unattended/check-unattended.sh:3090-3094`). So the verbs carrier can carry no
  token, and names a sibling kit's script by kit and bare file name, as it already names "the
  memory-tree kit's" `gotchas.py --for-diff` (`tools/unattended/VERBS.template.md:747-748`).
- The Skill's drive line names the two build harnesses by `scriptPath` and no argument
  (`tools/unattended/SKILL.template.md:123-124`), and the Skill calls itself a ROUTER whose verbs
  section "wins any difference" (`:9-11`). Check 31 reads the backticked `workflows/*.js` tokens from
  the rendered Skill (`tools/unattended/check-unattended.sh:5627-5641`).
- `bash tools/check-template-size.sh .claude/skills/unattended/SKILL.md` prints 10239 of 10240 bytes,
  1 under, PINNED 2026-10-11. The row's comment says growth past it "means prose is coming back that
  belongs in" the verbs carrier's paths section (`tools/template-size-limits.txt:119-125`).
- The verbs carrier is 84167 bytes and 979 lines, CR-stripped, against the hygiene gate's guide caps
  of 98304 bytes and 1200 lines (`tools/memory-tree/check-memory-hygiene.sh:114`), PINNED 2026-10-11.
- The "Drive the build as ONE program" bullet composes every argument the caller passes the two
  build harnesses (`tools/unattended/VERBS.template.md:718-746`). Its deferred sub-bullet says every
  returned agent's result is on disk "because the build harness runs its audit under
  `workerType: 'none'`" (`:733-738`), and its plan sub-bullet says "A child returning
  `committed:false` stops the loop" (`:744`).
- The closing review's call is M8's block (`memory/guides/BUILD-METHOD.md:260-263`), which the verbs
  carrier reaches through "the rule is M4 and M8" (`tools/unattended/VERBS.template.md:765`); neither
  the Skill nor the verbs carrier names `tier2-review.js`.
- The sibling specs this rule reads: `harness-args` takes `unattended-build`, `unattended-unit` or
  `tier2-review` and prints `{}` for a harness whose workflows declare no stage
  (`TOOL-aOrientedCast-2` §4). The unit harness returns `diverged`, and a roled audit's deferral
  re-dispatches every judge (`TOOL-aOrientedCast-4` S8, S13). An absent `.claude/roles.json` adds no
  arm to either guard (`TOOL-aOrientedCast-6` S5, `TOOL-aOrientedCast-7` S2).

### The text

S1 and S2, one sentence group placed after the bullet's "Every call is made by `scriptPath`, never
by `name`: the fan-out guard's read-window narrowing is conditional on `scriptPath`.":

```text
**Every harness call also carries `roles`**: the JSON the roles kit's
`handoff.py harness-args <harness>` prints, `<harness>` being `unattended-build`, `unattended-unit`
or, for the closing review M8 composes, `tier2-review`. With no `.claude/roles.json` the roles kit
is not installed: pass no `roles`, and each harness logs its per-stage fallback. A session started
before the rendered agent types existed cannot spawn them: it passes none too, and once the spawn
guard has landed it holds and a fresh session takes over.
```

S3, in place of the plan sub-bullet's "A child returning `committed:false` stops the loop.":

```text
A child returning `diverged: true` stopped before its code on the spec section its `why` names:
have that spec revised by the spec-writer role through a rendered handoff, as the `/build` Skill's
stage 5 does, then dispatch the unit again. Any other `committed:false` stops the loop.
```

S4, in place of the deferred sub-bullet's "nothing was recorded or built and every returned agent's
result is on disk, because the build harness runs its audit under `workerType: 'none'`.":

```text
nothing was recorded or built. Every returned agent's result is on disk where the audit ran its
judges untyped, under `workerType: 'none'`; under `roles` none is, and the hand-back's `next` says
the re-run dispatches every judge again.
```

The three edits add about 800 bytes and 7 lines to the carrier, an estimate PINNED at writing; the
hygiene gate re-derives both against its caps.

### Rollout

- Lands at order 6, beside `KICK-aOrientedCast-2`, whose write set it does not touch: after the
  renderer at order 2 and the harnesses' `roles` at orders 4 and 5, and before the write gate at 9 and
  the spawn guard at 10. One commit carries the template and the copy that
  `bash tools/unattended/adopt-unattended.sh` re-installs; the adopter re-renders the Skill to the
  same bytes.
- This run is one of the sessions S2 names: its agent registry predates the rendered types, so its
  remaining passes keep calling the harnesses untyped, as the catalogue-render and build-harness
  specs state, and the guards bind it only after the landing merge.
- The unattended kit's version and its carriers move once, in the run's mint commit;
  `govkit.py epoch` reports the move owed until then.
- Adopters receive the rule at their next `govkit update`, which re-copies the carrier. Where the
  roles kit is absent the rule reads as its no-roles case, and neither guard is armed.

### Inventory

None minted: the rule names existing verbs, fields and files.

### Files touched (estimate)

`tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **The rule in the Skill as well.** §8 F1.
- **One sentence per call site.** Two build-harness calls share the bullet, and the closing review
  reaches it through M8; three spellings of one rule are three places to rot. The rule is spelled
  once, and S3 and S4 read the fields it makes appear.
- **The renderer named by path.** The carrier is copied, never rendered, so it can carry no token,
  and a literal path to a sibling kit is what the kit authoring rule bans.
- **M8's block edited here.** It is the memory-tree kit's BUILD-METHOD template, outside the
  unattended kit; the external hands-off names it.

## 5. Production-readiness checklist

- security — Text only. The rule widens nothing: the guards decide, and a caller following it passes
  role names the renderer derived from the catalogue.
- perf / scale — One `harness-args` call per harness call, one Python spawn of a second or two; a
  build of N units pays it N + 2 times.
- error / empty / loading states — An adopter without the roles kit is told to pass nothing; a
  session that cannot spawn the types is told to pass nothing and to hand over once the guard lands.
- observability — The harnesses log each stage's type or fallback, and a refused call names the verb.
- risks — A session that passes `roles` it cannot spawn sees dead agents, which the harnesses already
  count. The revision procedure S3 points at is the `/build` Skill's stage 5, so a change there moves
  the unattended branch too, which is the point of pointing. The bug class this guards against is
  `two-answers-to-one-question`, the reason the rule is spelled once.
- testing — The direct checks below; no suite arm. The adopter's `--check` and check 10 of the
  unattended kit gate already grade the carrier pair.
- migration — None for data. A run in flight follows §3's first external hands-off.
- user docs — The verbs carrier is the user doc.

## 6. Acceptance criteria

- **AC1** — When `grep -o "handoff.py harness-args" memory/guides/UNATTENDED-VERBS.md | wc -l` runs
  after the pass it prints 1 where base prints 0, and the bullet holding it names `unattended-build`,
  `unattended-unit` and `tier2-review`, and the role index's path under the Claude directory.
  Red when: the rule is absent, spelled at a second site, or silent on a repository without the roles
  kit.
- **AC2** — When `grep -c "A child returning" memory/guides/UNATTENDED-VERBS.md` runs it prints 1 as
  at base, that line carries `diverged: true`, and
  `grep -c "Any other .committed:false. stops the loop" memory/guides/UNATTENDED-VERBS.md` prints 1
  where base prints 0.
  Red when: a typed unit's divergence still stops the run, or an ordinary failure no longer does.
- **AC3** — When `grep -c "because the build harness runs its audit under" memory/guides/UNATTENDED-VERBS.md`
  runs it prints 0 where base prints 1, and the deferred sub-bullet names `roles` and carries
  `dispatches every judge again`.
  Red when: the carrier still promises an on-disk result a roled audit never wrote.
- **AC4** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the pass it exits 0,
  and `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` exits 0; with one
  byte appended to the installed copy, `--check` exits 1 naming `UNATTENDED-VERBS.md`, and restored it
  exits 0.
  Red when: the shipped carrier and the installed copy differ, or the edit landed in only one of them.
- **AC5** — When `handoff.py harness-args <name>`, the roles kit's renderer, runs for each harness
  name the rule spells, each exits 0 and prints a non-empty JSON object.
  Red when: the rule names a harness the verb refuses or maps to nothing, so a caller following it
  passes no role.
  fixture: the renderer of `TOOL-aOrientedCast-2` and the catalogue of `TOOL-aOrientedCast-1`, both
  landed at earlier orders.
- **AC6** — When `git diff --exit-code 646d4a73 -- tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md`
  runs after the pass it exits 0, and `bash tools/check-template-size.sh .claude/skills/unattended/SKILL.md`
  exits 0.
  Red when: the router grew to restate a rule the verbs carrier owns, or past its ceiling.

## 7. Gates

`unattended skill wiring` · `unattended kit gate` · `unattended skill size` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds no arm: the adopter's `--check` and check 10 of the unattended kit gate already grade
the carrier pair, and every criterion above is a direct read.

## 8. Open questions

- **F1 — Does the unattended Skill's drive line state the rule, or only the verbs carrier?** The fold
  brief asks that wherever the Skill or the verbs tell the main loop to call a harness, the call
  carries `roles`, and the Skill's drive line names the two build harnesses.
  - (a) The verbs carrier alone. The Skill's line names no argument of either call today and routes
    their composition to the carrier that "wins any difference"; `roles` joins `scratch`, `base` and
    `specAudit` there. The Skill's bytes do not move.
  - (b) A pointer in the drive line, about 30 bytes, paid by trimming another Skill sentence. It
    rewrites guidance no finding flagged, in the file every unattended run loads first.
  - (c) The same pointer, paid by raising the Skill's 10240-byte ceiling row. That row exists to keep
    composition prose out of the router, and every raise recorded in that file is the owner's, so it
    is M3's veto 2.
  Recommendation: (a). (c) is vetoed. Of the survivors, (a) meets every criterion (b) would, since the
  Skill already sends a reader to the carrier for every required argument, and it leaves no unflagged
  sentence rewritten.
  RESOLVED (agent, 2026-10-11, delegated): (a), as §3 states; AC6 observes the Skill unmoved.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the M2 cross-read's findings 1, 2 and 4 and the main loop's
  decision to add this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the unattended verbs carrier tells the main loop to
compose each harness Workflow call's args, adding a roles object printed by the handoff renderer"`
ranked name-stem symbols first, `main`, `parse_args` and `leading_verb` among them, none a seam
for caller text, and the inventory key `UNATTENDED-VERBS.md` among the guides. That carrier is the
seam this unit extends: its "Drive the build as ONE program" bullet already composes every other
argument of the two build-harness calls. The copy and its byte compare are `adopt-unattended.sh`'s,
reused unchanged, and the revision procedure S3 points at is the `/build` Skill's stage 5
(`KICK-aOrientedCast-2`), not specified a second time here.

`python tools/memory-recall/query.py` was asked "how does an unattended run compose its harness
Workflow calls, and what must change when the harnesses take a roles argument and the spawn guard
refuses an untyped call". It surfaced this build's spec brief on units 4, 5 and 7, the run record's
`--rescope add` row for this unit, `TOOL-dRetiredFork-41` and `TOOL-dRetiredFork-22` on the build
harness's audit stage, which cannot run in a sidechain, and `TOOL-aHoistedPass-21` on whether a
`Workflow` call is authorized where a direct spawn is not.

Recall terms used: `unattended verbs scriptPath Workflow harness roles workerType agentType passes-harnessed deferred-platform diverged spawn guard`
