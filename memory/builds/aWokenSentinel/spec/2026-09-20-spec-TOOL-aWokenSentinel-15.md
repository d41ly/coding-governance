# TOOL-aWokenSentinel-15 — the spec-audit commission pins each subject at its committed blob and refuses a dirty subject before a lens is dispatched

**Status:** CLOSED · rev-2 · 2026-09-21 · node a · Tier-2 · base 12513c25 · streams tooling · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-15-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-15-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-15-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-15-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit findings B1 (round 2, raw ids 1, 20, 32 and 47) and B2 (raw ids 2, 21, 33 and 46):
the round-2 commission pinned specs 8 and 14 at the blobs `git rev-parse HEAD:<path>` answered,
while the working tree held uncommitted rev-2 folds of both files, and every lens read the working
tree. A disposition recorded against the pin is a disposition of a text nobody can open, and the next
commit could move it again before anything re-pins it. The immediate fix is a record act — the two
rev-2 folds are committed with the disposal that authored this spec, and the audit record names the
committed blobs — and this unit closes the CLASS: the harness's resolver stage returns each subject's
committed blob AND its working-tree hash, and `tools/workflows/unattended-build.js` refuses to
dispatch a lens while any subject differs between the two, naming the paths and the remedy, so an
audit is always of bytes a pin names.

## 2. Scope (IN)

- **S1** — The resolver prompt in `tools/workflows/unattended-build.template.js` (rendered to
  `tools/workflows/unattended-build.js` by `check-protocol-parity.test.sh --render` in the same
  commit) asks, per spec, for `git rev-parse HEAD:<specPath>` as `blob` and `git hash-object
  <specPath>` as `tree`, both as the full 40-hex object name, and `SUBJECTS_SCHEMA` requires both
  at `^[0-9a-f]{40}$`. The suite's `run_wf` stub never evaluates a schema, so the script itself
  refuses, INSIDE the resolver branch, a resolved entry whose `tree` or `blob` is not exactly 40
  hex, naming the field — a refusal shaped like `badSubject` and distinct from the dirty verdict.
  Observed by AC1, AC3 and AC5.
- **S2** — INSIDE the resolver branch — the `if (!subjects)` block at `unattended-build.js:642`,
  directly after `subjects = res.subjects` at `:657` and the field refusal of S1 — the script
  REFUSES with a thrown error when any resolved subject's `tree` differs from its `blob`, listing
  every such path with both hashes and the remedy: commit the fold, then re-invoke with the same
  arguments. It is a script-side compare of two fields the agent returned, so it holds whatever
  the agent's prose says. A caller-supplied `subjects` set never enters the branch: it is `{path,
  blob}` by S3's contract, carries no `tree`, and is authoritative by the comment at `:632`, so the
  compare and the strip cannot read it. Observed by AC1, AC2 and AC4.
- **S3** — The `tree` field is dropped, inside the same branch, before `subjects` reaches
  `tier2-review.js`, whose contract is `{path, blob}` and is not this unit's to widen; the
  callee's own refusal of a malformed subject and the existing `badSubject` refusal at `:669`,
  which runs over supplied and resolved sets alike, are untouched. Observed by AC2.
- **S4** — The harness's own suite `tools/workflows/unattended-build.test.sh` gains three arms
  over the `NOSUBJ` args at `:742`, the one fixture whose args carry no `subjects` and so reach
  the stubbed resolver: a return whose `tree` differs from its `blob` THROWS naming the path and
  both hashes; a return whose two fields agree reaches the sub-workflow with `tree` absent from
  what it was handed; and a return with `path` and `blob` only THROWS naming `tree` and not the
  fold. Each is observed RED first against the rendered harness at this unit's base, where the
  first arm proceeds, the second finds no `tree` to strip and the third proceeds. The two existing
  `NOSUBJ` arms at `:743` and `:924` gain a 40-hex `blob` and an equal `tree` on their stubbed
  return, because the field refusal of S1 reads them too. Observed by AC1, AC2 and AC5.
- **S5** — The harness's header comment on the resolver stage states the pre-flight and what it
  does NOT prove, in a sentence carrying the phrase `after the check passes`: that the committed
  blob is the text the LENSES read is a property of a clean tree at dispatch time, and a fold
  written by a concurrent session after the check passes is outside it. Observed by AC3, which
  pins that phrase.

## 3. Non-goals (OUT)

- **No change to `tier2-review.js`.** It refuses an unpinned subject already and reads the working
  tree by design; the pre-flight lives one stage earlier, where the pin is made.
- **No auto-commit.** A dirty subject is a fold the main loop wrote and did not commit, which is
  BUILD-METHOD M6's "commit at the end of every pass" left undone; the harness names the debt
  rather than paying it, because a commit made by the harness would carry no pass subject.
- **No pin at the working-tree hash.** `git hash-object` without `-w` writes nothing, and with it
  writes an unreachable object that the next `gc` drops; an audit pinned there is an audit of bytes
  no history holds.
- **No re-audit of specs 8 and 14 by this unit.** The round-3 audit the disposal commissions reads
  them at their committed rev-2 blobs like every other subject; this unit is about the round after
  that.

### Edges

- **consumes-from** external — the workflows kit's resolver stage, `SUBJECTS_SCHEMA` at
  `tools/workflows/unattended-build.js:377`, the resolver prompt at `:651` and the `badSubject`
  refusal at `:669`, all rendered from the template beside them; and the suite's `run_wf` runner,
  which evaluates the script with stub hooks and records what each stage returned.
- **hands-off** `TOOL-aWokenSentinel-21` — the suite these arms join sits on no leg, no budget
  row and no floor, so a throw over its supplied-subject fixtures reds nothing; that unit puts it
  in the declared self-test population with a shrink-only `FLOOR_ASSERTIONS`, and the fixtures
  become an executed arm for this compare.
- **hands-off** external — a pre-flight inside `tier2-review.js` itself for a caller that hands it
  subjects directly, which is a different population with its own argument grammar; a backlog row
  the close mints.

## 4. Design

### The resolver's return, widened by one field

```
subjects: [{ path, blob, tree }]        // blob = git rev-parse HEAD:<path>; tree = git hash-object <path>
```

`SUBJECTS_SCHEMA` gains `tree` beside `blob`, both `required` and both at `^[0-9a-f]{40}$` — the
full object name, which is what both git commands print by default. The prompt sentence reads:
"For each unit above that HAS a spec path, run `git rev-parse HEAD:<specPath>` and
`git hash-object <specPath>` in `<repo>` and return both as the full 40-character object names; an
unspecced unit is omitted rather than given an invented hash." The agent does what only an agent
can, which is run git; the script does the compare.

### The refusal

Inside `if (!subjects)`, directly after the `subjects = (res && Array.isArray(res.subjects)) ?
res.subjects : []` line at `:657`, so a supplied set never reaches it:

```
const badResolved = subjects.findIndex(function (s) {
  return !s || !/^[0-9a-f]{40}$/.test(String(s.blob || '')) || !/^[0-9a-f]{40}$/.test(String(s.tree || ''))
})
if (badResolved !== -1) throw new Error(
  'unattended-build: resolved subject ' + badResolved + ' does not carry a 40-hex blob and a 40-hex tree: ' +
  JSON.stringify(subjects[badResolved]) + '. The resolver returns both full object names or the pre-flight cannot compare them.')
const dirty = subjects.filter(function (s) { return s.tree !== s.blob })
if (dirty.length) throw new Error(
  'unattended-build: ' + dirty.length + ' subject(s) differ between HEAD and the working tree, so a lens ' +
  'would read text the pin does not name: ' + dirty.map(function (s) { return s.path + ' HEAD ' + s.blob + ' tree ' + s.tree }).join('; ') +
  '. Commit the fold, then re-invoke with the same arguments; an audit is pinned at bytes history holds.')
subjects = subjects.map(function (s) { return { path: s.path, blob: s.blob } })
```

The two hashes compare by string equality, so the prompt asks for the full 40 characters of each
and the schema and the `badResolved` refusal both pin that length; a resolver that abbreviates one
side is refused naming the field, never read as a dirty tree with a remedy that is false for a
clean one. The existing `badSubject` at `:669` stays where it is and keeps its `{7,40}` pattern,
because it grades the supplied set too and a caller's contract is not this unit's to narrow.

### Why the refusal is a throw and not a log line

The harness's other pre-flights on this stage — an empty subject set, a subject with no hex blob —
throw, and the main loop reads a throw as "the stage did not run" with the text as its reason.
A logged skip on this path would let the audit proceed over the very text it cannot pin, which is
the round-2 outcome this unit exists to end.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tree` | a field on the resolver's return | no cell; a schema property |
| `badResolved` | a `const` inside the resolver branch | no cell; not a function |
| `dirty` | a `const` inside the resolver branch | no cell; not a function |

No function is minted. The lexicon's `js.function camel` cell is unmoved.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/workflows/unattended-build.template.js` | the schema, the prompt sentence, the field refusal, the compare and the strip inside the resolver branch, the header paragraph |
| `tools/workflows/unattended-build.js` | re-rendered from the template in the same commit |
| `tools/workflows/unattended-build.test.sh` | three arms over `run_wf` with the `NOSUBJ` args and a `tree` field on the stubbed resolver return; the two existing `NOSUBJ` stubs at `:743` and `:924` widened to a 40-hex `blob` with an equal `tree` |

### Alternatives rejected

- **Have the resolver agent refuse.** An agent told to refuse on a dirty tree may instead return
  the HEAD blob and say nothing, which is the round-2 shape; a compare the script performs over two
  fields the schema requires cannot be talked out of.
- **Have the lenses read `git show <blob>` instead of the tree.** Four lens prompts and the
  skeptic batches would each need the redirection, the report would cite lines of a text nobody
  can open in the tree, and a fold made against it would land on the working tree anyway.
- **A `git status --porcelain` check over the whole tree.** It refuses on any dirty file, including
  the review record the previous stage wrote and has not committed; the population that matters is
  the subjects.

## 5. Production-readiness checklist

- security — N/A; the script compares two strings an agent returned and throws.
- perf / scale — one extra `git hash-object` per subject, milliseconds.
- error / empty / loading states — a resolver that omits `tree`, or abbreviates either hash, is
  refused by the script's `badResolved` naming the field, because the suite's stub evaluates no
  schema and a schema-only refusal would be observable by nothing; a differing pair refuses as
  dirty and the message shows both hashes.
- observability — the throw names every dirty path with both hashes and the one remedy.
- risks — a concurrent session folding a subject after the check passes and before the lens reads
  is not caught; the header says so. A refusal stalls an unattended run until the main loop
  commits, which is the correct stall: the alternative is an audit of nothing.
- testing — §6; three arms in the harness suite, run through `run_wf` in seconds, and one
  supplied-subject fixture read through the same runner as the control.
- migration — N/A; a caller passing `subjects` itself never enters the resolver branch, where the
  field refusal, the compare and the strip all live, so the fifteen supplied-subject fixtures of
  the harness suite read exactly as before.
- user docs — none; the harness's header.

## 6. Acceptance criteria

The fixture is the suite's own: `run_wf` in `tools/workflows/unattended-build.test.sh` evaluates the
rendered script with stub hooks, and a JSON object maps the `audit:subjects` label to the resolver's
stubbed return. AC1, AC2 and AC5 pass the `NOSUBJ` args at `:742`, the fixture whose args carry no
`subjects`, because the stubbed resolver is consulted only there; AC4's control passes the `UNITS`
args at `:89`, whose `subjects` are supplied. Each observation is one `run_wf` invocation over the
file at the tip.

- **AC1** — When the stubbed resolver returns `[{path: "s3", blob: "<40 hex a>", tree: "<40 hex b>"}]`
  with the two hashes different, `run_wf` over the `NOSUBJ` args prints `THROW` and the text
  carries `s3`, both hashes and `Commit the fold`; the trace carries no `workflow` call. Observed
  RED first against the rendered harness at this unit's base, where the run proceeds to the
  sub-workflow.
  Red when: the audit proceeds over a dirty subject, which is the round-2 outcome; or the message
  names neither hash, which sends the reader to diff by hand.
- **AC2** — When the stubbed resolver returns the same entry with `tree` equal to `blob`, `run_wf`
  over the `NOSUBJ` args traces the `workflow` call and the `subjects` it was handed hold `path`
  and `blob` only, read from the traced arguments with `grep -c '"tree"'` printing 0.
  Red when: `tree` reaches `tier2-review.js`, whose contract is `{path, blob}`; or an agreeing pair
  is refused, which is the pre-flight reading the wrong field.
- **AC3** — When `grep -c 'hash-object' tools/workflows/unattended-build.template.js` and the same
  over `tools/workflows/unattended-build.js` run at the tip, each prints at least 2 — the prompt
  sentence and the header paragraph — and 0 at this unit's base; `grep -c 'after the check passes'`
  over each file prints at least 1 at the tip and 0 at base, which is the limit sentence and
  nothing else carries it; and the kit's parity checker, run in its `--check` mode, exits 0 naming
  no moved render.
  Red when: the template moved and the render did not, which the parity leg reds at the close; or
  the header states the pre-flight without its limit, which the second grep alone can see — the
  first is met by the prompt sentence and the schema comment together.
  figure: 2 and 1 are DERIVED by the greps at observation; the zeros at base are DERIVED by the
  same greps over the files at `12513c25`.
- **AC4** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js`
  runs at the tip it exits 0; `grep -c 'Commit the fold' tools/workflows/unattended-build.test.sh`
  and `grep -c '"tree"' tools/workflows/unattended-build.test.sh` each print at least 1 and 0 at
  this unit's base; and `run_wf` over the `UNITS` args at `:89`, whose `subjects` are supplied,
  traces the `workflow` call and prints no `THROW` and no `Commit the fold`.
  Red when: the edit broke the AsyncFunction shape the runtime evaluates; or an arm exists that
  never reads the throw; or a supplied subject reads as dirty, which is the round-3 H1 placement —
  the compare outside the resolver branch, throwing on fifteen fixtures the suite already feeds
  through this stage.
  figure: both counts are DERIVED by the greps at observation over the tip and over the file at
  `12513c25`.
- **AC5** — When the stubbed resolver returns `[{path: "s3", blob: "<40 hex a>"}]` with no `tree`,
  `run_wf` over the `NOSUBJ` args prints `THROW` and the text carries `40-hex tree` and not
  `Commit the fold`; against the rendered harness at this unit's base the run proceeds to the
  sub-workflow.
  Red when: an omitted `tree` reads as dirty, which sends the reader to commit a fold that does not
  exist; or it proceeds, which is a pre-flight with one of its two inputs missing.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `verifier fan-out` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the `run_wf` invocations of
AC1, AC2, AC4 and AC5, the greps of AC3 and AC4 and the syntax check of AC4. Under
`review-protocol parity`, the template-render pair is the join this unit moves. The suite itself
is a held leg from unit 21 on, one order after this unit, and its first flagged green is where the
three arms run beside the fifteen supplied-subject fixtures.

New arm: `tools/workflows/unattended-build.test.sh` · a stubbed resolver return whose `tree` differs from its `blob`, one whose fields agree, and one with no `tree`, all over the `NOSUBJ` args; the break is the rendered harness at this unit's base · `FLOOR_ASSERTIONS` is `TOOL-aWokenSentinel-21`'s, pinned at that unit's order from a static count that includes these arms; none exists at this unit's order

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-09-20 · S1 · S2 · S3 · S4 · S5 · §3 · §4 · §5 · AC1 · AC2 · AC3 · AC4 · AC5 · §7 ·
  folded spec-audit round 3: sibling agreement for the promoted `TOOL-aWokenSentinel-21` (H1, raw
  26) — the compare and the strip live INSIDE the resolver branch after `:657`, so a supplied
  `{path, blob}` set never reads as dirty, AC1, AC2 and AC5 pass the `NOSUBJ` args, AC4 reads a
  supplied-subject fixture as the control, §5's migration row says what the branch placement
  buys, and the suite's floor is unit 21's; M1 (raw 1, 22, 36) — AC4's `check-arms.py` clause
  named a population that excludes both harness files, so the arms are observed by their own
  needles; M2 (raw 2) — the stub evaluates no schema, so the script refuses a resolved entry
  missing `tree` by name, observed by the new AC5; M3 (raw 3) — AC3 pins a phrase only the limit
  sentence carries; L1 (raw 25) — the prompt sentence asks for the full 40 characters and the
  schema and the refusal pin that length, so §4's prose and its quoted sentence agree.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 2 as the
  promotion of B1 (raw ids 1, 20, 32, 47) and B2 (raw ids 2, 21, 33, 46), one unit because one check
  covers the class.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "pin an audit subject at its committed blob and refuse a
dirty working tree before dispatching a review lens"` ranked `blob_oid` and `blob_at` in
`tools/govkit/govkit.py` — Python helpers that hash a file and read a blob at a revision for the
kit installer's own drift check, not reachable from a workflow script, which has no filesystem —
and the three `*Refused` classes of the process-monitor kit; no existing seam fits in the harness's
runtime. The seam, read at source, is the resolver stage itself: `SUBJECTS_SCHEMA` at
`tools/workflows/unattended-build.js:377`, the prompt at `:651` that already asks for
`git rev-parse HEAD:<specPath>`, and the `badSubject` refusal at `:669` whose shape the new refusal
copies. The recall probe's top hits were `TOOL-aRootedPrefix-3` (a checker measuring raw
working-tree bytes rather than committed ones, the same distinction) and this build's own round-2
audit record at the B1 paragraph; no prior record names a blob-pin pre-flight.

Recall terms used: `blob pin subject spec-audit immutable bytes working tree uncommitted resolver stage hash-object lens dispatch refuse`
