# TOOL-aGraftedHelix-15 — the build harness commits the specs its writers authored before AUDIT pins them, and its commit-first refusals name a remedy a resume cannot replay

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-1 · base 5266d22e · streams tooling · order 10 · advances TOOL-aHoistedPass-35 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-15-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-15-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 |
| [2026-10-04-prompt-TOOL-aGraftedHelix-15-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-15-1-spec-brief.md) | journal | — |
| [2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/unattended-build.template.js` tells its SPEC writers to author and never commit, and
then runs the AUDIT resolver against `HEAD` inside the same call. So every first call on a build with
a MISSING spec and a declared audit throws `no spec subjects could be pinned at round 1`. A re-invoke
under `resumeFromRunId` then replays the resolver's cached empty answer and throws again. Both were
observed on `wf_7b67cf1d-995`, the second in 20 ms. This unit adds one commit stage after the writers
return and writes the committed paths back onto their units. It also makes every refusal that asks
for a commit name a re-invoke that a resume cannot replay. One call then completes SPEC and AUDIT on
a build whose specs the harness authors.

## 2. Scope (IN)

- **S1** — A commit stage: one agent, labelled `commit:specs:<slug>`, spawned after the SPEC fan
  returns and before the AUDIT phase. It runs whenever the writers report at least one `authored` id
  that `units` carries, and the caller supplied no `subjects`. It stages exactly the authored specs
  plus what `gen_build_index.py --write` re-renders, and commits once with `Pass: none`. After the
  commit it runs the per-pass bug-class checklist over that commit. It returns `committed`, `sha`,
  `why`, `specs`, `summary` and an optional `checklist`. Observed by AC1 and AC3.
- **S2** — The stage's `specs` list writes each committed path into its unit's `specPath` for the
  rest of the call, so the resolver's roster and the hand-out roster both carry it. Where the caller
  supplied a different path, the committed one wins and a log line names both. Observed by AC2.
- **S3** — A commit stage that returns nothing, returns `committed: false`, returns a `sha` that is
  not 40 hex, omits an authored id from `specs`, or names a path outside the build's spec folder
  refuses the call before the resolver spawns, naming which. Observed by AC4.
- **S4** — The resolver also returns `notAtHead`: each audit spec that exists in the working tree
  and has no blob at `HEAD`. Any entry refuses, naming the paths and the cause. An audit unit that
  reaches the resolver branch with no `specPath`, and that `specRefused` does not carry, refuses
  before the resolver spawns, naming `--plan <slug> --paths` as the cause. An audit set whose every
  unit `specRefused` carries refuses there too, naming those refusals. Observed by AC5.
- **S5** — One remedy sentence, computed once from `specAudit` and `auditIds`, closes every refusal
  that asks for a commit. Those are S3's, S4's, the dirty-tree refusal, the empty-subject refusal and
  the clean-round no-unit refusal. It says to rebuild `units` from `--plan <slug> --paths` after
  committing, then names a fresh re-invoke without `resumeFromRunId` and, where `subjects` is legal,
  a resume with `subjects` pinned from `git ls-tree HEAD`. The empty-subject refusal also states its
  cause. Observed by AC4 and AC6.
- **S6** — Every statement of who commits agrees with S1. That is the writers' prompt, the header's
  author-never-commit paragraph, the SPEC-stage comment, the hand-out's `specPath` comment, the
  clean-round `owed` comment and `meta`. The header gains one paragraph on what the stage does not
  buy. `tools/workflows/README.md` stops counting the install paths the harness names and lists the
  build-index generator among them. Observed by AC7.
- **S7** — The render is regenerated from the template, parses, and is admitted by the fan-out hook.
  Observed by AC8.
- **S8** — The review-harness kit version and the harness's own `unattended-build@` engine identity
  each move once, after this unit's last move. Observed by AC9.
- **S9** — The harness suite gains the arms §7 names, and its moved arms are repointed. NOT OBSERVED
  by a criterion here: the suite is a kit self-test the main loop runs once at the close, and a pass
  runs no suite (shared invariant 11).
- **S10** — The commit stage's checklist output reaches whoever acts on it, because moving the spec
  commit into the program moves the checklist BUILD-METHOD M6 owes after it. On the audit route it is
  merged into the checklist the audit receives, after the resolver's, as ONE checker-shaped string
  carrying ONE by-design block. On the audit-OFF route the
  hand-out carries it with the stage's sha as `specCommit`, with the instruction to act on it before
  the first dispatch. Observed by AC1.

## 3. Non-goals (OUT)

- **Committing a fold or a promoted spec the DISPOSAL stage writes.** The caller commits those, as
  today. A re-invoke over them meets S4's named refusal rather than the bare empty one.
- **Committing beside caller-pinned `subjects`.** A caller that pinned blobs has committed. A stage
  there would also turn the resume-with-`subjects` remedy into a replay of a cached failure.
- **Teaching the resolver to find a spec for a unit that carries no `specPath`.** S4 refuses that
  unit by name instead, and the caller re-reads `--plan <slug> --paths` once its specs are committed.
- **Verifying the commit from inside the program.** A workflow script has no filesystem. On the audit
  route the resolver's separate read at `HEAD` is the cross-check, and on the audit-OFF route
  `--dispatch`'s MISSING refusal is.
- **The deferred-platform re-run.** Its "re-run ONCE with identical args" reuses the review's results
  on disk by design and asks for no commit.
- **A `closes` verb on `TOOL-aHoistedPass-35`**, the open ask on the roster's empty `specPath`. S2
  answers it on every route where the commit stage runs, which the header's `advances` verb records.
  The roster this writer was handed carried no `closes` list, so the claim of closure is left to
  whoever plans that ask.
- **The re-stage after the generator, and an arm running the stage's git sequence for real.** The
  commit S1 describes stages each spec before `gen_build_index.py --write` renders it, so the commit
  holds the pre-render blob. That repair is `TOOL-aGraftedHelix-16`'s (§3 Edges).

### Edges

- **consumes-from** `TOOL-aGraftedHelix-3` — its resolver instruction to run `gotchas.py --for-paths`,
  the optional `checklist` and `checklistPaths` fields it adds to `SUBJECTS_SCHEMA`, and its moves of
  both version lines. This unit edits the same prompt, schema and lines after it and keeps all three.
  Built before it, this unit's edits would be overwritten.
- **hands-off** `TOOL-aGraftedHelix-16` — the commit stage's git steps: the re-stage of the authored
  specs after `gen_build_index.py --write`, the post-commit `git status --porcelain` check that turns
  a dirty spec into `committed: false`, and the real-git arm that runs the traced prompt's block
  (finding 21 of the round-1 audit of units 10 to 15).

## 4. Design

### What the run observed

On `wf_7b67cf1d-995` the SPEC stage authored nine specs and committed none, as its prompt orders. The
resolver ran `git rev-parse HEAD:<specPath>` for each, all nine failed, and it returned no subjects.
The stage threw the empty-subject refusal. After a hand commit, a re-invoke with `resumeFromRunId`
replayed the resolver's cached empty answer and threw again in 20 ms. Caller-pinned `subjects` from
`git ls-tree HEAD` completed the route. The build's run-state file records this as its 17:36:04Z
rescope row.

That is the predicate's real-tree population: every first call on a build with a MISSING spec and a
declared audit. A second instance sits one step earlier. Run on 2026-10-04, this command printed
this unit's own row as `MISSING` with an EMPTY path column:

```bash
bash tools/unattended/unattended.sh --plan aGraftedHelix --paths
```

A caller that copies `--paths` therefore hands the resolver no path at all for a MISSING unit, and
the resolver's prompt skips a unit with no path.

### The commit stage (S1, S3)

**Placement.** After the SPEC merge and its refusal accounting, before `phase('Audit')`, assigned to
the `Spec` phase through `opts.phase`. The fan has fully returned there, so the stage is the only
writer. One committer after a barrier keeps the reason `TOOL-aStagedLane-3` gave for
author-never-commit, which is N writers contending on one git index.

**Trigger.** `authoredIds` is the writers' `authored` ids that `units` carries and `specRefused` does
not. The stage runs when `authoredIds` is non-empty and `args.subjects` is not an array. It is
mode-independent and audit-independent (§8 F2). Each skip logs one line naming why.

**Return schema**, copied from `UNIT_SCHEMA` in `tools/workflows/unattended-unit.js`, because
workflow scripts cannot import:

```js
const SPEC_COMMIT_SCHEMA = {
  type: 'object',
  required: ['committed', 'sha', 'why', 'specs', 'summary'],
  additionalProperties: true,
  properties: {
    committed: { type: 'boolean' },
    sha: { type: 'string' },
    why: { type: 'string' },
    specs: {
      type: 'array',
      items: { type: 'object', required: ['id', 'path'], properties: { id: { type: 'string' }, path: { type: 'string' } } },
    },
    summary: { type: 'string' },
    checklist: { type: 'string' },
  },
}
```

`checklist` is optional, so a double that omits it still validates, and an empty string is carried
as no checklist.

`sha` carries no schema pattern, matching `UNIT_SCHEMA`. The script checks it, so a bad value
refuses by name instead of failing validation into a null.

**The prompt** opens with `GROUND` and orders these steps in this sequence:

1. Find each id's spec: the file under `memory/builds/<slug>/spec/` whose H1 line opens
   `# <id> —`, which is the key `gen_build_index.py` reads the id from (`H1_RE`); its basename ends
   `-spec-<id>.md`. The status header carries no id. Return them as `specs`, repo-relative and
   forward-slashed.
2. Record `git status --porcelain --untracked-files=all` in `repo` before anything is staged. Every
   path it lists other than those specs is FOREIGN, and is never staged by this stage.
3. `git add -- <the spec paths>`, then `python {{MEMORY_TREE_DIR}}/gen_build_index.py --write`, then
   stage each path that step 2 did not list and that is changed now. Those are the generator's
   outputs. Never `git add -A` or `git add -u`. The order is load-bearing: the generator renders over
   tracked specs only, so an untracked spec leaves the index stale and hygiene check 9 reds the
   pre-commit hook.
4. Commit once on the checked-out branch. The subject is `spec(<slug>): <the ids, space-joined>`, a
   body line names this stage, and the final trailer block carries `Pass: none` and the attribution
   trailer the charter mandates. Never `--no-verify`, never amend, never push or merge.
5. A refusal from a hook, the generator or git returns `committed: false` with its first lines in
   `why`. Do not edit a spec to clear it, and do not retry around it.
6. Return `sha` as the full 40-hex `git rev-parse HEAD`.
7. Run the `CHECKLIST` command, `gotchas.py --for-diff HEAD~1..HEAD`, over the commit just made,
   and return its stdout as `checklist`. It always exits 0; an empty selection returns an empty
   string.

`Pass: none` is the trailer the precedent spec commit `b3a5e2ecf` carries. `--check-commit` returns
at a `none` trailer before it reads any declaration. Two filters keep this commit out of
`pass-order history`'s build commits, in the order they fire. `read_attribution_tokens` in
`tools/unattended/lib-unattended.sh` maps a `Pass: none` trailer to no unit token. Behind it,
`build_commit` in the same file excludes a commit confined to the build folder, the generated
indexes and the shared records, and that exclusion alone would also suffice.

**Validation**, in the script, in this order, each a throw ending in the S5 remedy:

| return | the throw names |
|---|---|
| null | the stage, and that the authored specs are on disk and uncommitted |
| `committed` is not `true` | the agent's `why`, quoted |
| `sha` fails `/^[0-9a-f]{40}$/` | the `sha` field and its value |
| an `authoredIds` member with no `specs` entry | each such id |
| a `specs` path outside `memory/builds/<slug>/spec/` | each such id and its path |

On success the stage logs `spec stage: committed <n> spec(s) at <sha>`.

**The checklist (S10).** A non-empty `checklist` is merged, under a `# ` label line naming the spec
commit, into the checklist the audit receives, after the resolver's own. It is MERGED and never
appended, because unit 3's parser in `tools/workflows/tier2-review.template.js` reads one checker
output per string: `extractByDesign` cuts out the FIRST by-design head only, and `parseChecklist`
folds every later line that does not open `- ` into the item above it. A plain append would hand
the lenses the second block's invariants as bug classes and glue its header lines onto the
resolver's last item. So `renderChecklistUnion` writes ONE checker-shaped string: both inputs'
header lines first with the label between them, then both item sets with a repeat of an item
already listed dropped by its first line, then ONE by-design head whose count is the union of both
blocks' entries, then those entries. Where no caller or resolver checklist exists, the merge over
an empty first input is the spec commit's checklist under its label. On the audit-OFF route the hand-out
gains `specCommit: {sha, checklist}`, and the hand-out's instruction says to act on that checklist
before the first `--dispatch`. M8's closing checklist over `<BASE>..HEAD` still runs; this one is the
per-pass obligation M6 attaches to the spec pass.

### The path fill (S2)

For each `specs` entry whose id is a unit of `ordered`, that unit's `specPath` becomes the committed
path. Where the caller supplied a different path, a log line names both and the committed one wins,
because it is the file history holds. `auditUnits` and `buildUnits` both filter `ordered` after this
point, so the resolver's roster and the hand-out roster read the fill.

### The resolver's `notAtHead`, and the pathless refusal (S4)

Before the resolver spawns, an audit unit with no `specPath` that `specRefused` does not carry
refuses, naming the ids. After the fill, such a unit can only be one the writers counted
`alreadyPresent` with no path from the caller. The resolver's prompt says to skip a unit with no
path, so today it is audited by nobody and nothing says so. The refusal names its cause: `units`
was copied from `--plan <slug> --paths` while the spec was MISSING, which prints an empty path, so
the caller re-reads that command now the spec is committed. This is the refusal a fresh re-invoke
after an S3 refusal meets, because the writers then count the hand-committed spec `alreadyPresent`,
no commit stage runs, and no fill happens.

Also before the resolver spawns, an audit set whose every unit `specRefused` carries refuses, naming
those refusals. Without it, live writers that refused every audit unit leave `liveWriters` above
zero, the all-dead throw does not fire, and the resolver returns nothing to pin.

The resolver prompt gains one instruction: a spec path that exists in the working tree and does not
resolve at `HEAD` goes in `notAtHead` as `{path}`, and never in `subjects`. `SUBJECTS_SCHEMA` gains
`notAtHead` as an optional array of `{path}`, so the suite's stub resolvers and unit 3's optional
fields keep working. After the existing 40-hex field check and before the dirty-tree compare, a
non-empty `notAtHead` refuses. The message says that many specs exist on disk and not at HEAD, so no
blob pins them; it names each path, says to commit them, and ends in the remedy. A partial set
refuses too. Auditing the resolved half and rostering the rest unaudited is the gap the clean-round
`owed` filter already names on its own path.

The empty-subject refusal keeps its first sentence, which operators grep. It gains the cause it can
now state, over the audit units `specRefused` does not carry: each carried a path, none resolved at
`HEAD` and none exists on disk, so the paths in `units` are wrong. It names `--plan <slug> --paths`
and ends in the remedy.

### The remedy (S5)

Computed once, after the args block, as `resumeRemedy`:

Every form opens the same way: commit the specs, then rebuild `units` from
`bash tools/unattended/unattended.sh --plan <slug> --paths`, so every unit carries its committed
`specPath`. Then:

| `specAudit` | `auditIds` | the remedy names |
|---|---|---|
| absent | any | a fresh re-invoke without `resumeFromRunId` |
| present | empty | a fresh re-invoke, or a resume with `subjects` pinned from `git ls-tree HEAD -- <spec path>` |
| present | non-empty | a fresh re-invoke only, and that `subjects` cannot stand beside `auditIds` |

Each form ends with the reason. A resume replays every agent call whose prompt is unchanged, so the
stage's cached answer returns the same refusal however the tree has moved since. That is the Workflow
runtime's documented resume contract: the longest unchanged prefix of agent calls returns cached
results. `wf_7b67cf1d-995` is its observation here. A fresh call re-runs the writers, which count each
committed spec `alreadyPresent`, so the commit stage does not run and nothing fills `specPath`. The
rebuilt `units` is what carries the paths on that call, and the resolver then reads `HEAD` live. A
resume with `subjects` skips the commit stage too, and the clean-round `owed` filter needs
`u.specPath`, so the rebuild is owed on that route as well.

The dirty-tree refusal keeps `Commit the fold` and loses `re-invoke with the same arguments`, which
under a resume is the replay. The clean-round no-unit refusal and S3's and S4's refusals end the
same way. One constant serves every such site, so the sites cannot drift into two answers.

### What the prose says (S6)

- **The writers' prompt.** "the caller commits once after all of you return, and regenerates the
  index once" becomes "one committer commits once after all of you return and regenerates the index
  once: this program's commit stage, or the caller when it pinned `subjects`".
- **The header's fan paragraph and the SPEC-stage comment's clause 3.** Both say the caller commits;
  both name the commit stage instead.
- **A new header paragraph**, opening `THE SPEC COMMIT (TOOL-aGraftedHelix-15)`, in the register of
  the header around it. It buys one call from SPEC through AUDIT on a build whose specs it authors,
  and a roster whose authored units carry their committed path. It cannot buy proof the commit
  happened: `sha` is its agent's claim, and the cross-check is the resolver's separate read at
  `HEAD` on the audit route and `--dispatch`'s MISSING refusal off it. It does not commit a disposal
  fold or a promoted spec. It does not run beside caller `subjects`. It does not make a refusal
  resume-safe; the refusal names the re-invoke that is. A caller committing in the same worktree
  while the call is outstanding meets git's index lock, which the stage reports as `committed: false`.
- **The hand-out's comment** that `specPath` is empty for every unit the SPEC stage just authored,
  and the clean-round `owed` comment that repeats it, both say the commit stage fills it, and that it
  stays empty only on a call whose stage did not run.
- **`meta`.** The Spec phase's `detail` and the `description` name the commit.
- **`tools/workflows/README.md`.** "The build harness names four install paths" loses the count,
  which charter §7 bans as a typed figure of a derived population, and its list gains the build-index
  generator. Two other carriers of the count stay: `tools/workflows/kit.toml` and
  `memory/map/features/review-harnesses.md` state it in the past tense, of what reached adopters
  before review-harness 1.8, which this unit does not change.

### Inventory

| identifier | kind | where |
|---|---|---|
| `SPEC_COMMIT_SCHEMA` | constant | the template, beside `SUBJECTS_SCHEMA` |
| `resumeRemedy` | constant | the template, after the args block |
| `authoredIds` | constant | the template, after the SPEC merge |
| `notAtHead` | resolver return field | `SUBJECTS_SCHEMA` |
| `checklist` | optional commit-stage return field | `SPEC_COMMIT_SCHEMA` |
| `specCommit` | hand-out field, `{sha, checklist}` | the audit-OFF hand-out |
| `commit:specs:<slug>` | agent label | the commit stage |
| `renderChecklistUnion` | function | the template, top level, beside `renderCloses` |
| `BY_DESIGN_HEAD` | constant | the template, a copy of `tools/workflows/tier2-review.template.js`'s |

One new named function, `renderChecklistUnion`. `python tools/lexicon/lexicon.py --suggest
renderChecklistUnion --as js.function` answered `OK`: it leads with `render`, the verb this file's
`renderRoster` and `renderCloses` already use for text it composes. No key the codebase map's
ratchet reads is added: no file, leg or conf key. The map's generated symbol index gains the
function's two rows, one per carrier, re-rendered with `gen_map.py --write` in the same commit.

The harness's emitted install paths gain `{{MEMORY_TREE_DIR}}/gen_build_index.py`, through the
render token the `CHECKLIST` constant already uses, so shared invariant 2 holds. The parity renderer
probes that directory by `gotchas.py`, and the memory-tree kit ships the generator beside it in both
install layouts.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`, by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render
- `memory/map/generated/symbols.json`, by the map's generator

### Rollout

1. Edit the template. Re-render with the workflows kit's parity script in its `--render` mode, and
   never edit a render.
2. Write the arms §7 names into the harness suite and repoint the moved ones. Do not run the suite.
3. Bump once, after the last move. The review-harness line in
   `tools/workflows/tier2-review.template.js` and line 3 of the build-harness template each go one
   minor step above their value at the pass's parent. Unit 3 moves both lines earlier in this build,
   so no literal is pinned here. Re-render.
4. No kickoff-manifest re-stamp: no file in its `watch:` moves.

### Alternatives rejected

Every candidate was weighed by READING existing artifacts. BUILD-METHOD M3 forbids a probe that
builds an arm of the fork. Three tests:

- **T1, resume.** The Workflow runtime returns cached results for the longest unchanged prefix of
  agent calls, and `wf_7b67cf1d-995` observed the replay in 20 ms. A candidate whose recovery needs
  an unchanged agent call to answer differently fails. Liveness: this probe produced its negative on
  this run.
- **T2, fresh call.** The writers' prompt counts an existing spec `alreadyPresent`, and the
  `--plan <slug> --paths` verb prints an empty path for an untracked spec, as observed above. A fresh
  call re-runs every writer, which finds each spec present, so no candidate's own stage fills
  `specPath` on that call. A candidate passes T2 only where its refusal sends the caller to re-read
  `--plan <slug> --paths` after committing, so the units the fresh call carries hold their paths.
- **T3, `pass-order history`.** `read_attribution_tokens` drops a `Pass: none` spec commit first and
  `build_commit` excludes it behind that, and every candidate puts the spec commit before any roster
  hand-out. T3 discriminates none of them. It is recorded so the next build does not re-run it.

| candidate | T1 | T2 | one call | verdict |
|---|---|---|---|---|
| (a) a commit stage after the writers | passes | passes, with the remedy's `--plan` re-read | yes | taken |
| (b) the resolver reports `notAtHead` and the harness refuses | fails | passes | no | kept as S4 and S5 |
| (c) the SPEC stage returns early with a commit instruction | fails | passes | no | rejected |
| (d) pin at `git hash-object -w` blobs, commit later | passes | passes | yes | rejected |
| (e) vary the resolver's prompt per call | n/a | passes | no | rejected |

(a) passes T1 because its first call needs no re-invoke for this cause, and a resume after a later
failure replays a commit history already holds. Its own failure path does replay, which is why it
carries (b)'s refusal and the S5 remedy. Its T2 pass rests on that remedy naming the `--plan`
re-read: rev-1 credited the resolver's live read of `HEAD`, which a pathless unit never reaches.

(b) alone fails T1 as a route: the resolver's cached answer replays. Its refusal does name the two
routes that pass. It loses on the mechanism the README roster states for this unit, because every
first call on such a build refuses.

(c) fails T1 outright. The writers' cached results still say `authored`, so a resumed call returns
early forever. Only a new caller-asserted flag breaks that loop, and it would be a fact this runtime
cannot verify: the hole the header already names for `runStateExists`.

(d) passes both tests and loses on the pin. `git hash-object -w` writes an object no commit reaches.
`gc.pruneExpire` is unset on node `a`, and git's documented default prunes an unreachable loose
object after two weeks, so a review record's `path@blob` could name nothing. The dirty-tree refusal
states the contract it would break: an audit is pinned at bytes history holds.

(e) cannot be built. A workflow script has no clock and no randomness, since `Date.now()` and
`Math.random()` throw under the runtime, so the only varying input is a caller argument. An uncached
resolver would still meet uncommitted specs on the first call.

## 5. Production-readiness checklist

- security — The stage writes inside `repo` on the checked-out branch: the authored specs and the
  generator's outputs, which the caller committed by hand until now. Step 2's record keeps a foreign
  change out of the commit, tracked or untracked. That case is live: while this spec was written,
  the worktree held another writer's untracked build brief, which a whole-tree `git add` would have
  swept into the spec commit. The stage never pushes, merges, amends or bypasses a hook.
- perf / scale — One agent and one generator run per call that authored anything, plus the
  pre-commit hook's usual staged cost. A fresh re-invoke re-runs every writer, which is why the
  remedy names the resume-with-`subjects` route wherever it is legal.
- error / empty / loading states — S3 and S4 are the error states, each a throw naming its cause and
  the remedy. Each of the stage's two skips logs one line naming why.
- observability — The commit line with its sha, one line per path the fill changed, and one line per
  skip.
- risks — The commit meets the guards a unit child's commit meets inside a workflow: the pre-commit
  hook, the `commit-msg` hook's `--check-commit`, and the scratch guard's orientation card for this
  tree. A refusal from any of them is `committed: false` and a named throw, never a silent pass. The
  tier is the README roster's (shared invariant 12): the write is the caller's existing spec commit
  moved into the program, with no new class of path. A foreign edit to a file the generator also
  rewrites stays unstaged, so the commit's index is stale there and check 9 refuses it at the hook:
  a named `committed: false`, never a commit that mixes the caller's edit in.
- testing — The arms §7 names, each observed red on its staged break at the close. The pass observes
  the program through the stub-hook probe of §6.
- migration — None. Callers keep their arguments, and an audit-OFF caller that commits after the
  call finds nothing to commit. That caller now reads the spec pass's checklist from the hand-out's
  `specCommit` instead of running it after its own commit.
- user docs — `tools/workflows/README.md`, per S6.

## 6. Acceptance criteria

Criteria AC1 to AC7 run one scratch `node` probe under the session scratchpad. It evaluates the rendered
`tools/workflows/unattended-build.js` the way the build-harness self-test's runner does: as an
AsyncFunction with stub hooks that trace each agent label and prompt and answer by label prefix.
Each staged break is made in a scratch COPY of the render and observed once.

- **AC1** — When the probe runs a call whose SPEC double authors `A-tB-1` from a unit with no
  `specPath`, with a commit double returning `committed: true`, a 40-hex `sha` and that id's path,
  the trace holds exactly one `agent:commit:specs:tB` line. It sits after the last `agent:spec:` line
  and before `agent:audit:subjects`. Its traced prompt names `gen_build_index.py --write`, the
  trailer `Pass: none`, `A-tB-1`, the H1 line as the locator, and `gotchas.py --for-diff HEAD~1..HEAD`,
  and orders every path listed before staging left unstaged as the literal `FOREIGN`. The log
  carries `spec stage: committed 1 spec(s) at` with the sha. With the commit double returning a
  checker-shaped `checklist` string, the traced audit call's `checklist` argument carries that
  string's item lines after the resolver's, a repeated item once, and exactly one by-design head,
  whose count is both blocks' entries together. With `specAudit` absent the stage still runs once,
  the roster is handed out, and the hand-out's `specCommit` carries the sha and that string.
  Red when: the stage is missing or runs after the resolver, or its checklist reaches nobody. Staged:
  the stage's `agent(` call deleted in the copy leaves no `agent:commit:` line in the trace.
  cost: an end-to-end call through the Workflow runtime cannot run inside a pass, because a sidechain
  holds no `Workflow` tool. The next harnessed build with a MISSING spec and a declared audit is that
  observation.
  permission: the permanent arms are the harness suite's, which only the main loop runs, once.
- **AC2** — When AC1's probe reaches the resolver, its traced prompt names the committed path for
  `A-tB-1`, and the hand-out's `roster` entry for `A-tB-1` carries that path as `specPath`. Run
  again with the unit carrying a caller-supplied spec path that differs from the committed one, the
  resolver prompt and the roster carry the committed path, and one log line names both paths.
  Red when: the path is not written back, or the caller's path wins. Staged: the fill loop deleted in
  the copy leaves the resolver prompt showing `(to be authored under` for `A-tB-1`.
- **AC3** — When the SPEC double authors nothing, the trace holds no `agent:commit:` line. When the
  call carries caller `subjects` beside an authored id, the trace holds none either, and the log names
  the authored id as left to the caller.
  Red when: the stage runs with nothing to commit, or beside caller `subjects`, where a resume would
  replay a cached failure.
- **AC4** — When the commit double returns null, then `committed: false` with a `why`, then a 7-hex
  `sha`, then `specs` lacking `A-tB-1`, then `specs` naming `A-tB-1` at a path under another build's
  spec folder, each run ends in `THROW`. The messages name, in turn, the stage, the `why` text, `sha`,
  `A-tB-1`, and `A-tB-1` with its path. Each carries `resumeFromRunId` and `--plan`, and no trace
  holds an `agent:audit:subjects` or a `workflow:` line. The null run repeated with `specAudit` absent
  names a re-invoke without `resumeFromRunId` and carries no `git ls-tree`.
  Red when: any of the five reaches the resolver, or the audit-OFF remedy offers a resume.
- **AC5** — When the resolver double returns no subjects and a `notAtHead` naming one path, the run
  ends in `THROW` naming that path and `not at HEAD`. Its remedy names a re-invoke without
  `resumeFromRunId` and carries `git ls-tree HEAD`. The same double under `auditIds` says `subjects`
  cannot stand beside `auditIds`, and carries no `git ls-tree`. One resolved subject beside one
  `notAtHead` path also ends in `THROW`, with no `workflow:` line. A unit carrying no `specPath`
  that no writer refused ends in `THROW` before any `agent:audit:subjects` line, naming
  `--plan <slug> --paths`; that is also the end of a fresh call over a pathless unit whose spec the
  writers count `alreadyPresent`. A call whose writers refused every audit unit ends in `THROW`
  naming those refusals, before any `agent:audit:subjects` line. The traced `agent:audit:subjects`
  prompt names `notAtHead` and the instruction that a path existing in the working tree and not
  resolving at `HEAD` goes there.
  Red when: `notAtHead` is read as an empty set, or the instruction a real resolver needs is missing.
  Staged: the `notAtHead` branch deleted in the copy lets the run reach
  `no spec subjects could be pinned` without naming the path; the instruction deleted in the copy
  reds the prompt check.
- **AC6** — When the resolver double returns no subjects and no `notAtHead`, the `THROW` keeps
  `no spec subjects could be pinned` and adds `--plan` and `resumeFromRunId`. A resolver double whose
  `tree` differs from its `blob` ends in `THROW` carrying `Commit the fold` and `resumeFromRunId`. A
  clean-round double with no owed unit ends in the clean-round `THROW`, which carries
  `resumeFromRunId` and `--plan`, and under `auditIds` carries no `git ls-tree`; a call carrying
  caller `subjects` over units with no `specPath` reaches the same `THROW`.
  `grep -c "re-invoke with the same arguments" tools/workflows/unattended-build.js` prints `0`, and
  so does `grep -c "Commit the authored specs and re-invoke" tools/workflows/unattended-build.js`.
  Red when: a refusal that asks for a commit names a re-invoke a resume replays.
- **AC7** — When the probe traces the writers' prompt, it carries
  `one committer commits once after all of you return` and not
  `the caller commits once after all of you`. This prints one header line:
  `grep -n "THE SPEC COMMIT (TOOL-aGraftedHelix-15)" tools/workflows/unattended-build.js`.
  `grep -c "names four install paths" tools/workflows/README.md` prints `0`, and
  `grep -n "gen_build_index" tools/workflows/README.md` prints the install-path sentence.
  `grep -c "the caller commits" tools/workflows/unattended-build.js` prints `0`. The hand-out's
  `specPath` comment names the commit stage, and `meta`'s `description` names the commit.
  Red when: the writers, a comment, `meta` or the README still give the old answer beside the new
  one.
- **AC8** — When the workflows kit's renderer runs ONCE in its `--render` mode at the pass's commit,
  `git status --porcelain tools/workflows/` prints nothing.
  `node tools/workflows/check-workflow-syntax.js` reports every script parsed clean. A `Workflow`
  tool-call JSON naming the rendered harness as its `scriptPath`, piped into
  `node tools/hooks/agent-cap.js`, exits 0.
  Red when: a render was edited by hand, or the hook denies the new `agent(` call.
- **AC9** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no review-harness carrier left behind, and `bash tools/check-kit-versions.sh`
  exits 0. Line 3 of `tools/workflows/unattended-build.js` carries an engine identity one minor step
  above its value at the pass's parent.
  Red when: the kit's shipped bytes moved without its version.
  figure: both versions are DERIVED from the pass's parent at observation time, because unit 3 moves
  both lines first.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `method carriers (every pointer declared)` · `pass-order history` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/workflows/unattended-build.test.sh · the commit stage's placement, prompt, log and checklist routing over a SPEC double authoring a pathless unit, with the audit declared and absent; stage the stage call deleted · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · the path fill into the resolver prompt and the roster, with and without a differing caller path; stage the fill deleted · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · the five commit-stage refusals, the outside-folder path among them, and the two skips, with the audit declared and absent · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · the notAtHead, partial, pathless, all-refused and empty refusals with and without auditIds, the resolver prompt's notAtHead instruction, the clean-round no-unit refusal with and without caller subjects, and the remedy at the dirty-tree refusal; stage the notAtHead branch deleted, then the instruction · the suite's floor rises by the arms added

Moved arms, in the same suite. The writers' "the caller commits once after them" arm is repointed at
the new sentence. Every arm that reaches the resolver or the audit-OFF hand-out without caller
`subjects` gains a commit double: the `NOSUBJ` arms, the round-1 `OFF_UNITS` arms, and the
checklist arms unit 3 adds. Their commit double returns no `checklist`, so unit 3's arms keep
reading the resolver's string unmerged. Arm (v)'s layout fixture is unchanged: its run carries
caller `subjects`, so the stage does not run there and the render emits no generator path on that
run; the generator path rides the `{{MEMORY_TREE_DIR}}` token arm (iv) already grades. The
engine-identity arm's version literal moves with S8.

The close runs the legs and the suite. A pass runs the probe and the commands of §6 as its check.

## 8. Open questions

- **F1 — Which mechanism makes one call complete SPEC and AUDIT on a build whose specs the harness
  authors, and leaves no refusal a resume can trap?**
  The candidates are (a) to (e) of §4 "Alternatives rejected", which records the test each loser
  failed. The vetoes clear (a): it adds no external dependency and no public surface, its one new
  install path sits under a directory the harness already names, it edits no governance carrier, and
  it moves an existing write rather than widening one. (b) clears them too and fails the one-call
  mechanism the README roster states for this unit.
  RESOLVED (agent, 2026-10-04, delegated): (a), carrying (b)'s refusal and the S5 remedy for every
  case the stage cannot cover.
- **F2 — Does the commit stage run only when an audit follows, or whenever the writers authored and
  the caller pinned no `subjects`?**
  Audit-only keeps audit-OFF callers committing by hand, and leaves the writers' prompt a
  mode-dependent answer about who commits. Whenever-authored gives one rule and fills the roster's
  `specPath` on both routes. It changes nothing an audit-OFF caller must do, whose own commit then
  finds nothing to commit. Its write set is the one that caller commits before any dispatch, since
  `--dispatch` refuses a unit no tracked spec defines.
  RESOLVED (agent, 2026-10-04, delegated): whenever the writers authored and the caller pinned no
  `subjects`.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, adopted mid-run from the harness's first-call audit trap on
  `wf_7b67cf1d-995`.
- rev-2 · 2026-10-04 · §3 §4 §6 §7 §10 · S1 S2 S3 S4 S5 S10 · AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 ·
  folded the round-1 spec audit of units 10 to 15 on this unit: 15 and 17 (the remedy rebuilds
  `units` from `--plan <slug> --paths`, the pathless refusal names that cause, T2's verdict for (a)
  rests on the remedy, AC3's log says left to the caller, AC5 and AC6 drive both routes); 9 and 18
  (AC4 runs the audit-OFF remedy, AC6 drives the clean-round no-unit refusal); 7 (AC5 reads the
  resolver prompt's `notAtHead` instruction); 6 (AC8 renders once and reads porcelain); 8 and 20
  (S3 and a fifth AC4 run refuse an outside-folder path); 10 (AC2's caller-path case); 27 (step 1
  locates by the H1 line); 35 (step 7 and S10 carry the per-pass checklist); 19 (the all-refused
  refusal, and the empty-subject cause over unrefused units); 11 (AC7's carriers); 30 and 37
  (`build_commit` and `read_attribution_tokens` replace a dead name); and 36 (the header's
  `advances` verb). §3 gains the hands-off to the unit promoted from finding 21.
- rev-3 · 2026-10-05 · §2 §4 §6 §7 · S10 · AC1 · the builder, against unit 3's landed parser: S10
  appended the spec commit's checklist to the audit's, and `tools/workflows/tier2-review.template.js`
  reads ONE by-design block per string (`extractByDesign` takes the first head) and folds later
  non-item lines into the item above (`parseChecklist`), so an append handed the lenses a second
  block's invariants as bug classes. The checklist is now MERGED by `renderChecklistUnion` into one
  checker-shaped string; §4's inventory gains that function and `BY_DESIGN_HEAD`, and the symbol
  index joins Files touched, so the leg line gains the two recall-floor legs that path trips. §7: arm (v)'s run carries caller `subjects`, so its fixture needs no
  stub generator, and the moved arms' commit double returns no checklist.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` over "commit authored specs before the audit resolver
pins subjects at HEAD", and over "workflow agent commits its pass and returns committed and sha",
ranked name-stem neighbours only, with `unscanned layers: .sh`. The nearest were `resolve` in
the recall conf and `measure_commitment` and `check_commitment` in `tools/runlog/record.py`, which
hash journal lines and commit nothing. So no existing seam fits through the probe, and the seams this
unit extends were found by reading the harness. They are the unit child's commit contract in
`tools/workflows/unattended-unit.js`, its `UNIT_SCHEMA` and its `Pass:` trailer rule, copied because
workflow scripts cannot import. They are the resolver and its dirty-tree refusal in
`tools/workflows/unattended-build.template.js`. And they are `read_attribution_tokens` and
`build_commit` in `tools/unattended/lib-unattended.sh`: the first drops a `Pass: none` commit's unit
tokens, and the second's path exclusion would keep a spec commit out of the build commits on its own.
Rev-1 cited the second under a name no file defines, which survives only as a historical spelling
in a comment.

The recall question was "why does the build harness spec stage not commit, and how does the audit
resolver pin spec subjects". It returned `TOOL-aStagedLane-3`, whose author-never-commit rule is about N writers on
one index, which one committer after the barrier keeps. It returned `TOOL-aWokenSentinel-15`, the
dirty-tree refusal whose remedy S5 rewrites, and `TOOL-aHoistedPass-35`, the open ask S2 answers. It
returned `TOOL-dRetiredFork-41`, the ruling that moved AUDIT's spawn to where `Workflow` exists. Where
a hit was checked against source: `TOOL-aHoistedPass-35` says no line of the program writes
`specPath` back, which is still true at base `5266d22e`.

Recall terms used: unattended-build spec stage writers author commit resolver subjects blob HEAD audit pinned resumeFromRunId caller
