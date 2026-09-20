# TOOL-aWokenSentinel-15 — the spec-audit commission pins each subject at its committed blob and refuses a dirty subject before a lens is dispatched

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 12513c25 · streams tooling · order 20

<!-- gen:spec-records -->

*No record names this unit.*

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
  <specPath>` as `tree`, and `SUBJECTS_SCHEMA` requires both, each a 7-40 hex string. Observed by
  AC1 and AC3.
- **S2** — Directly after the existing `badSubject` refusal, the script REFUSES with a thrown error
  when any subject's `tree` differs from its `blob`, listing every such path with both hashes and
  the remedy: commit the fold, then re-invoke with the same arguments. It is a script-side compare
  of two fields the agent returned, so it holds whatever the agent's prose says. Observed by AC1
  and AC2.
- **S3** — The `tree` field is dropped before `subjects` reaches `tier2-review.js`, whose contract
  is `{path, blob}` and is not this unit's to widen; the callee's own refusal of a malformed
  subject is untouched. Observed by AC2.
- **S4** — The harness's own suite `tools/workflows/unattended-build.test.sh` gains two arms: a
  resolver return whose `tree` differs from its `blob` THROWS naming the path and both hashes, and
  a return whose two fields agree reaches the sub-workflow with `tree` absent from what it was
  handed; each observed RED first against the rendered harness at this unit's base, where the
  first arm proceeds and the second finds no `tree` to strip. Observed by AC1 and AC2.
- **S5** — The harness's header comment on the resolver stage states the pre-flight and what it
  does NOT prove: that the committed blob is the text the LENSES read is a property of a clean
  tree at dispatch time, and a fold written by a concurrent session after the check passes is
  outside it. Observed by AC3.

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
- **hands-off** external — a pre-flight inside `tier2-review.js` itself for a caller that hands it
  subjects directly, which is a different population with its own argument grammar; a backlog row
  the close mints.

## 4. Design

### The resolver's return, widened by one field

```
subjects: [{ path, blob, tree }]        // blob = git rev-parse HEAD:<path>; tree = git hash-object <path>
```

`SUBJECTS_SCHEMA` gains `tree` beside `blob` with the same `^[0-9a-f]{7,40}$` pattern and both are
`required`. The prompt sentence reads: "For each unit above that HAS a spec path, run
`git rev-parse HEAD:<specPath>` and `git hash-object <specPath>` in `<repo>` and return both; an
unspecced unit is omitted rather than given an invented hash." The agent does what only an agent
can, which is run git; the script does the compare.

### The refusal

After `badSubject`:

```
const dirty = subjects.filter(function (s) { return s.tree !== s.blob })
if (dirty.length) throw new Error(
  'unattended-build: ' + dirty.length + ' subject(s) differ between HEAD and the working tree, so a lens ' +
  'would read text the pin does not name: ' + dirty.map(function (s) { return s.path + ' HEAD ' + s.blob + ' tree ' + s.tree }).join('; ') +
  '. Commit the fold, then re-invoke with the same arguments; an audit is pinned at bytes history holds.')
subjects = subjects.map(function (s) { return { path: s.path, blob: s.blob } })
```

Shortened prefixes compare by string equality, so the prompt asks for the full 40 hex characters of
each; a resolver that abbreviates one side and not the other refuses honestly rather than passing.

### Why the refusal is a throw and not a log line

The harness's other pre-flights on this stage — an empty subject set, a subject with no hex blob —
throw, and the main loop reads a throw as "the stage did not run" with the text as its reason.
A logged skip on this path would let the audit proceed over the very text it cannot pin, which is
the round-2 outcome this unit exists to end.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tree` | a field on the resolver's return | no cell; a schema property |
| `dirty` | a `const` inside the script's audit stage | no cell; not a function |

No function is minted. The lexicon's `js.function camel` cell is unmoved.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/workflows/unattended-build.template.js` | the schema, the prompt sentence, the refusal, the strip, the header paragraph |
| `tools/workflows/unattended-build.js` | re-rendered from the template in the same commit |
| `tools/workflows/unattended-build.test.sh` | two arms over `run_wf` with a `tree` field on the stubbed resolver return |

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
- error / empty / loading states — a resolver that omits `tree` fails schema validation, which is
  the existing refusal shape; an abbreviated hash on one side refuses as a mismatch and the message
  shows both.
- observability — the throw names every dirty path with both hashes and the one remedy.
- risks — a concurrent session folding a subject after the check passes and before the lens reads
  is not caught; the header says so. A refusal stalls an unattended run until the main loop
  commits, which is the correct stall: the alternative is an audit of nothing.
- testing — §6; two arms in the harness suite, run through `run_wf` in seconds.
- migration — N/A; a caller passing `subjects` itself is outside the resolver stage and unchanged.
- user docs — none; the harness's header.

## 6. Acceptance criteria

The fixture is the suite's own: `run_wf` in `tools/workflows/unattended-build.test.sh` evaluates the
rendered script with stub hooks, and a JSON object maps the `audit:subjects` label to the resolver's
stubbed return. Each observation is one `run_wf` invocation over the file at the tip.

- **AC1** — When the stubbed resolver returns `[{path: "s3", blob: "<40 hex a>", tree: "<40 hex b>"}]`
  with the two hashes different, `run_wf` prints `THROW` and the text carries `s3`, both hashes and
  `Commit the fold`; the trace carries no `workflow` call. Observed RED first against the rendered
  harness at this unit's base, where the run proceeds to the sub-workflow.
  Red when: the audit proceeds over a dirty subject, which is the round-2 outcome; or the message
  names neither hash, which sends the reader to diff by hand.
- **AC2** — When the stubbed resolver returns the same entry with `tree` equal to `blob`, the trace
  carries the `workflow` call and the `subjects` it was handed hold `path` and `blob` only, read from
  the traced arguments with `grep -c '"tree"'` printing 0.
  Red when: `tree` reaches `tier2-review.js`, whose contract is `{path, blob}`; or an agreeing pair
  is refused, which is the pre-flight reading the wrong field.
- **AC3** — When `grep -c 'hash-object' tools/workflows/unattended-build.template.js` and the same
  over `tools/workflows/unattended-build.js` run at the tip, each prints at least 2 — the prompt
  sentence and the header paragraph — and 0 at this unit's base; and the kit's parity checker,
  run in its `--check` mode, exits 0 naming no moved render.
  Red when: the template moved and the render did not, which the parity leg reds at the close; or
  the header does not state the pre-flight and its limit.
  figure: 2 is DERIVED by the grep at observation; 0 at base is DERIVED by the same grep over the
  file at `12513c25`.
- **AC4** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js`
  runs at the tip it exits 0, and `python3 tools/memory-tree/check-arms.py --report` filtered to
  the harness suite's own file lists the two new arms' `has` sites as armed.
  Red when: the edit broke the AsyncFunction shape the runtime evaluates, or an arm exists that never
  reads the throw.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `verifier fan-out` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the `run_wf` invocations of
AC1 and AC2, the greps of AC3 and the syntax check of AC4. Under `review-protocol parity`, the
template-render pair is the join this unit moves.

New arm: `tools/workflows/unattended-build.test.sh` · a stubbed resolver return whose `tree` differs from its `blob`, and one whose fields agree; the break is the rendered harness at this unit's base · no assertion floor exists in this suite

## 8. Open questions

none

## 9. Revision log

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
