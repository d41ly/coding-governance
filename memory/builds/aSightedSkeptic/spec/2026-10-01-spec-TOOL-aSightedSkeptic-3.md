# TOOL-aSightedSkeptic-3 — finders and skeptics are handed intent: a `specs` argument, and the range's commit messages by default

**Status:** SPECCED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 3 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |

<!-- /gen:spec-records -->

## 1. Goal

No lens of `tools/workflows/tier2-review.template.js` is told what the change under review was
meant to do. The closing-review invocation passes no `context`, which then defaults to "the
cumulative diff landing on main", and nothing reaches a lens that names a spec or an acceptance
criterion. This unit adds `args.specs`, a list of intent documents the caller names, renders it
into the one context block every finder and skeptic opens with, and hands every diff-kind reader
the range's commit messages, which exist in every git repository and so need no caller at all.

## 2. Scope (IN)

- **S1** — `args.specs` is read in the prelude, after the `kind` check and before the base-shape
  ladder, so a bad value refuses before any agent spawns (invariant 3 of the build's spec brief).
  Absent (`undefined`) it is the empty list. Present, it must be an array whose every member is a
  non-empty string that is repo-relative: no backslash, no leading `/`, no drive letter and no `..`
  segment. Anything else throws an Error whose message opens `tier2-review:` and names `specs`, the
  rule, the offending index and the value given. Observed by AC4.
- **S2** — `renderIntent()` is minted and called from `renderBrief(role)`, so the same INTENT block
  reaches every finder prompt and every skeptic prompt. For the diff kind it names each spec path
  with the instruction to read the ones a lens or a finding touches, says that the intent lens reads
  every one WHOLE before the diff, and that a listed document which does not exist in the repository
  is itself a finding against its path. It ALWAYS names the range's commit-log command,
  `git -C <repo> log --format=%B <base>..<head>` over the RESOLVED shas, and any spec or design
  document the diff touches or those messages name; with no `specs`, it says those are the statement
  of intent. Observed by AC1, AC2.
- **S3** — For the spec kind, `specs` is SIBLING CONTEXT: the block names the documents as not under
  audit, to be read for agreement and never reported against, and names no commit log, because a
  spec audit has no range. A spec path that is also a subject's `path` is refused before any agent
  spawns, because one document cannot be both under audit and not under it. Observed by AC5.
- **S4** — A run with neither a `context` nor a non-empty `specs` is ANNOUNCED, on both kinds: one
  `WARNING:` log line before the resume probe, and an `Intent:` sentence in the synthesis prompt's
  RUN INTEGRITY block stating where intent came from on every run. Observed by AC3.
- **S5** — `specs` joins the `inputPrint` fingerprint, so a lens file written for one set of intent
  documents is never reused for another (invariant 5). Observed by AC6.
- **S6** — The `args` header comment documents `specs:` as a `name:` key, and
  `tools/workflows/README.md` documents the argument beside the other `tier2-review.js` arguments.
  Observed by AC7.
- **S7** — The template and its render land in one commit, the render produced by the parity
  renderer and never hand-edited (invariant 1), with the per-pass direct checks green and the
  suite's assertion floor raised by the assertions this unit's arms execute. Observed by AC8.

## 3. Non-goals (OUT)

- Verifying that a listed spec exists. The harness has no filesystem (its own `HONEST LIMIT` note
  beside the review-root log line says so); S2 hands the check to the lenses, which hold one.
- Parsing a spec's acceptance criteria into structure. The intent lens reads the documents whole.
- The intent lens's own brief and the lens set. Both are `TOOL-aSightedSkeptic-5`'s.
- `REVIEW_SHAPE` and the harness version. Both move once, in the first unit built (invariants 5, 9).
- The harnessed spec audit's call in `tools/workflows/unattended-build.template.js`, which passes
  neither `specs` nor `context` and will therefore announce the absence on every audit it runs.
  Supplying one there is a change to another script's contract, outside this unit.
- `memory/guides/BUILD-METHOD.md` M8's invocation block, which does not show `specs`. It is a
  governance carrier (invariant 8); the main loop parks it for the owner.
- The codebase-map dossier's prose about this harness. Nine units touch one paragraph in sequence;
  refreshing it once, at the close, is cheaper than nine rewrites.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-1` — `renderBrief(role)`, the one block both prompts open
  with. Without it the INTENT block has no shared home and skeptics would not see it.
- **consumes-from** `TOOL-aSightedSkeptic-5` — the `intent` lens the block instructs, and the build's
  one `REVIEW_SHAPE` bump already in the review key.
- **hands-off** external — M8's invocation block in the build method, to the owner, if `specs`
  is to be shown there.
- **hands-off** external — the harnessed spec audit's call, which announces a missing intent until
  its caller supplies a context or sibling documents.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that date; units ordered before this one move the
lines but not the facts.

- The finder prompt interpolates `CONTEXT`, `REVIEW ROUND`, `BY DESIGN` and the prior findings, and
  nothing that names an intent document. The verify prompt interpolates none of them; unit 1 moves
  the shared lines into `renderBrief(role)`.
- `context` is `a.context` or a per-kind default, so an absent context is indistinguishable in the
  prompts from a supplied one.
- `inputPrint` fingerprints `context`, `byDesign` and `priorFindings`, and the comment above it
  says every input a lens prompt interpolates is in it except `repo`.
- `baseSha` and `headSha` are the probe's resolved full shas, falling back to the refs as given;
  `diffCmd` is built from them after the probe. A function called inside a finder or skeptic thunk
  reads their final values.
- The args-header arm of `tools/workflows/tier2-review.test.sh` derives every field read off the
  `a` alias and requires each to appear in the header block as a `name:` key, so `a.specs` reds it
  until the header carries `specs:`.
- Closing reviews in this repository supply intent today by writing it into `context` by hand;
  `memory/builds/dMendedRecall/reviews/2026-10-01-review-TOOL-dMendedRecall-1-closing-diff-round1.md`
  is one.

### Data model

```
args.specs : string[]            // repo-relative, forward-slash; absent => []
SPECS      : the validated list   // interpolated by renderIntent(), fingerprinted by inputPrint
```

### The INTENT block, rendered by `renderIntent()`

Diff kind:

```
INTENT — what this change was meant to do.
<when SPECS> The caller named these documents as its statement of intent:
  - <path>
  …
Read the ones your lens or your finding touches; the intent lens reads every one WHOLE before it
reads the diff. A listed document that does not exist in <repo> is itself a finding against its path.
</when>
Read the range's commit messages, `git -C <repo> log --format=%B <baseSha>..<headSha>`, and any spec
or design document the diff touches or those messages name.<when no SPECS> No spec was supplied, so
these are the statement of intent.</when>
```

Spec kind:

```
SIBLING CONTEXT — <when SPECS> documents NOT under audit, named by the caller as what the subjects
must agree with. Read them for agreement and report nothing against them:
  - <path>
  …</when><when no SPECS> none supplied; the subjects are their own statement of intent.</when>
```

The two-dot range is deliberate: `log a..b` lists the commits the diff `a...b` introduces.

### Announcement

```
WARNING: neither `specs` nor `context` was supplied — the lenses were told nothing about what this <change|spec set> is for<, beyond the range's commit messages>; pass the intent documents as `specs` or describe the change in `context`
```

The RUN INTEGRITY block gains one sentence on every run, beginning `Intent:` and stating one of: the
number of spec documents supplied; that no spec was supplied and `context` was the caller's
statement, beside the commit messages on the diff kind; or that NEITHER was supplied, which the
report must say.

### Refused values

Each is one arm of AC4, and each must throw before any agent spawns:

```
specs: 'a.md'          // not an array
specs: [7]             // a member that is not a string
specs: ['']            // an empty member
specs: ['/abs.md']     // a leading slash
specs: ['C:/x.md']     // a drive letter
specs: ['a/../b.md']   // a .. segment
specs: ['a\\b.md']     // a backslash, as a JS string literal
specs: null            // present, and not an array
```

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `renderIntent` | function, verb `render` | `js.function` |
| `SPECS` | module constant | none: constants are not graded |

`python tools/lexicon/lexicon.py --suggest renderIntent --as js.function` read `OK` on 2026-10-01.
The validation is inline beside the `kind` check, the shape the prelude already uses, so it mints no
function.

### Rollout

Edit the template, then run `bash tools/workflows/check-protocol-parity.test.sh --render` to
regenerate `tools/workflows/tier2-review.js`, and commit both together. Write the arms, observe each
RED against the render as it stood before this unit's commit by running a slice of the suite's
runner holding only that arm, and raise `FLOOR_ASSERTIONS` by the count the new arms execute,
counted off the block.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh` · `tools/workflows/README.md`

### Alternatives rejected

- **Merge the intent into `context`.** It is what callers do by hand today, and it loses the one
  thing this unit adds: a default that exists in every repository when nobody supplies one.
- **Name the commit log only when `specs` is absent.** The brief permits it, and it would hide the
  `Decided:` trailers and the per-commit scope a spec does not restate. §8 F2.
- **Silently default to the commit messages.** It is the
  `memory/gotchas/degradation-known-but-unreported.md` class: the absence must be said.

## 5. Production-readiness checklist

- security — a spec path reaches a prompt as text an agent then reads. S1 refuses absolute paths,
  `..` segments and backslashes, so a caller's typo cannot point a reviewer outside the repository.
  Intent documents and commit messages are repository content of the same trust as the diff itself.
- perf / scale — one short block per prompt and one `git log` a finder runs itself; a very long
  range's log is the finder's to page, bounded by its own context.
- error / empty / loading states — malformed `specs` refuses before any spawn; absent intent is a
  WARNING and a RUN INTEGRITY sentence; a missing document is reported by the lens that reads it.
- observability — the WARNING line, and the `Intent:` sentence in every report.
- risks — a caller who passes stale specs gets a review against stale intent; the commit messages
  are always beside them, so a disagreement between the two is visible to the intent lens.
- testing — the arms of §6, each observed RED before this unit's commit.
- migration — none. An absent `specs` behaves as before plus the commit-log default and the
  announcement; the review key already moves once for the build through `REVIEW_SHAPE`.
- user docs — `tools/workflows/README.md` and the `args` header (S6).

## 6. Acceptance criteria

Every arm named below is written into the suite beside the template by this unit's pass and
observed RED there against the render as it stood before the commit. Its passing reading is the
main loop's single suite run at `VERIFYING`, which the acceptance ledger cites.

- **AC1** — When the stub-agent runner evaluates a diff review with
  `specs: ['a.md', 'b.md']`, arm `specs reach every finder and skeptic prompt` passes:
  every `find:` and every `verify:` prompt carries `INTENT` and both paths.
  Red when: a skeptic prompt lacks the block, which means it was built outside `renderBrief(role)`.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC2** — When the runner evaluates a diff review with no `specs`, arm
  `no specs: every diff finder is handed the commit log` passes: every `find:` prompt carries
  `log --format=%B` followed by the probe's resolved base and head shas joined by `..`, and the
  sentence that the messages are the statement of intent.
  Red when: the command names the refs as given while the probe resolved them, or is absent.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC3** — When the runner evaluates a diff review with neither `context` nor `specs`, arm
  `no specs and no context: announced in the log and RUN INTEGRITY` passes: the captured log holds
  a `WARNING:` line naming `specs` and `context`, and the `synth` prompt's RUN INTEGRITY block holds
  `Intent:` and `NEITHER`; its control arm `specs supplied: no intent warning` passes over the same
  run with `specs` given.
  Red when: the absence is silent in either place, or the warning fires when intent was supplied.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC4** — When the runner evaluates a diff review with each value §4 "Refused values" lists, the
  arm `specs refused before any agent` for that value passes: the run throws a message containing `specs`, and the trace holds no agent label.
  Red when: a malformed value reaches a lens, or the refusal does not name the field.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC5** — When the runner evaluates a spec audit whose `specs` names a subject's `path`, arm
  `spec-audit: a spec that is also a subject is refused` passes; with `specs` naming another path,
  arm `spec-audit: specs render as sibling context` passes: every `find:` prompt carries
  `SIBLING CONTEXT` and that path, and none carries `log --format=%B`.
  Red when: an overlapping path is accepted, or a spec-kind prompt is handed a commit range.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC6** — When the args-variant loop of the suite carries the variant `another specs`, its two
  arms pass: a lens file written under the key without `specs` is dispatched, and one written under
  the variant's own key is reused.
  Red when: `specs` is missing from `inputPrint`, so the old file is reused.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC7** — When `grep -n 'specs:' tools/workflows/tier2-review.template.js` runs, a line inside the
  `args` header block is listed, and the header arm `the args header documents all` passes;
  `grep -c -F 'specs' tools/workflows/README.md` prints at least 1, where BASE prints 0.
  Red when: the header or the README omits the field.
- **AC8** — When the pass has committed, `node tools/workflows/check-workflow-syntax.js`,
  `bash tools/workflows/check-verifier-fanout.sh` and `bash tools/workflows/check-review-join.sh`
  each exit 0, `git diff --exit-code tools/workflows/tier2-review.js` exits 0 after a fresh run of
  the parity renderer, and `python tools/lexicon/lexicon.py --suggest renderIntent --as js.function`
  prints a line opening `OK`.
  Red when: the render was hand-edited or not regenerated, a fan-out shape changed, or the name
  leads with an undeclared verb.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/workflows/tier2-review.test.sh` · stub-agent runs with `specs` present, absent, malformed and overlapping a subject, and one args variant · `FLOOR_ASSERTIONS` raised by the count the new arms execute

## 8. Open questions

- **F1 — What does the spec kind do with `specs`?** (a) Refuse it. (b) Ignore it and announce.
  (c) Render it as sibling context, refusing a path that is also a subject. (a) and (b) throw away
  the documents M4 says spec-audit lenses should be primed with, the mandate and the overview, and
  the contradiction lens already judges a sub-spec against the main spec. (c) meets every criterion
  the others meet and gives that lens its other half; it widens no surface, since the documents are
  read, never written. Recommendation (c). RESOLVED (agent, 2026-10-01, delegated): (c), the most
  feature-rich survivor after M3's vetoes.
- **F2 — With `specs` supplied, is the diff kind still handed the commit log?** (a) Only without
  `specs`, as the brief's minimum. (b) Always. (b) costs one sentence, keeps the `Decided:`
  trailers and per-commit scope in view, and lets the intent lens see a spec and the commits
  disagree. Recommendation (b). RESOLVED (agent, 2026-10-01, delegated): (b), more stated
  behaviour for no new surface.
- **F3 — Does a spec audit with neither `context` nor `specs` announce too?** (a) Diff kind only.
  (b) Both kinds. M4 primes spec-audit lenses with the mandate and the overview, so a spec audit
  told nothing is degraded in the same way; announcing it is the build's invariant 2.
  Recommendation (b). RESOLVED (agent, 2026-10-01, delegated): (b); the harnessed audit's caller
  is the edge in §3.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the build's spec brief, the run mandate and the template
  read at `ef1dcdb6`.

## 10. Reuse audit

The codebase-map probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "hand a review finder the intent documents and commit messages of the reviewed range"
```

The `reuse_lookup.py` result: it ranked name-stem neighbours only (`read_git_range` and `derive_record_commits` in the runlog kit
among them, which read a range for a different consumer) and reported `.sh` as an unscanned layer;
no candidate carries intent into a review prompt. The seam this unit extends is the review harness
itself, claimed by `memory/map/features/review-harnesses.md`: `renderBrief(role)` from unit 1 for
the block, the prelude's `kind` refusal for the validation shape, and `inputPrint` for the key.
The recall probe surfaced `TOOL-aBoundedVerdict-14`, which added `priorFindings` and `round` as
labelled lens sections distinct from `byDesign`; this unit follows that precedent and keeps intent
out of `context` for the same reason. It also surfaced closing-review records that put intent into
`context` by hand, which is the status quo §4 Alternatives rejects.

Recall terms used: tier2-review context byDesign priorFindings finder lens prompt intent spec closing diff-review M8 invocation degradation-known-but-unreported

The question passed with them: "how is a Tier-2 review's finder told what the diff is for, and why
does the context argument default".
