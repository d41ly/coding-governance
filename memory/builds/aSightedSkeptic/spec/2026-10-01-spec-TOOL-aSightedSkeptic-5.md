# TOOL-aSightedSkeptic-5 — five diff lenses, with verification and intent added, project lens notes, and one review-shape bump

**Status:** CLOSED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 1 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 TOOL-aSightedSkeptic-10 |
| [2026-10-01-build-TOOL-aSightedSkeptic-5-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-5-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-5-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-5-2-build-brief.md) | journal | — |
| [2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md](../reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md) | diff-review | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |

<!-- /gen:spec-records -->

## 1. Goal

The diff lens set of `tools/workflows/tier2-review.template.js` misses the defect this repository
finds most often, a check that cannot fail, and its security brief is shaped for a web application.
This unit replaces the four diff lenses with the owner's five, `security correctness seams
verification intent`, lets a caller append a project addendum to any lens through `args.lensNotes`,
and bumps the review key once for the whole build so no lens file written by the old prompts is
reused by the new ones. It also moves the harness version to 1.17, once, for the build.

## 2. Scope (IN)

- **S1** — `DIFF_LENSES` becomes an array literal of exactly five elements, keyed `security`,
  `correctness`, `seams`, `verification`, `intent`, in that order, carrying the briefs §4 pins. The
  `regressions` lens is retired: its checklist sweep moves to the split `TOOL-aSightedSkeptic-4`
  builds. `SPEC_LENSES` and the receiver line `const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES`
  with its `gov:fixed-verifiers` marker are untouched. Observed by AC1, AC2, AC8.
  - **Readers:** by name: `tools/workflows/tier2-review.template.js` and its render
    `tools/workflows/tier2-review.js` declare the key, and `tools/workflows/tier2-review.test.sh`
    names its find label in three arms and in its list of lens files. by value:
    `tools/workflows/tier2-review.test.sh` counts four `find:` spawns on a diff run, four pending
    labels when every lens dies, and the comment above `buildLensReturn` derives four ids from four
    lenses; `README.md` and `WIRE-INTO-PROJECT.md` each state "four finder lenses"; the meta phase
    detail on line 10 of the template states "4 finder lenses". Lens files already on disk under
    `<git-common-dir>/review-lenses/` carry the old key and are never reused, by S3.
- **S2** — The brief texts carry no web-application item. `correctness` loses "client/server
  validation divergence" and "error/empty/loading states"; `security` is rewritten around the trust
  boundaries of code in general. Observed by AC2.
- **S3** — A literal `const REVIEW_SHAPE = 'lenses5-r1'` joins the object `inputPrint` fingerprints,
  so every review key this harness derives changes once, and the resume probe's directory, which
  interpolates `inputPrint`, follows without a second edit. Later units of this build do not touch
  it. Observed by AC6.
- **S4** — `args.lensNotes`, an object mapping a lens key of the CURRENT kind to a non-empty string.
  Absent, it defaults to `{}`. Present but not a plain object, a key naming no lens of the current
  kind, or a value that is not a non-empty string throws `tier2-review: …` naming the field, the
  legal key set and what was given, before any agent spawns. Applies to both kinds, each against
  its own lens set. Observed by AC3, AC4.
- **S5** — A note is appended to its own lens's finder prompt directly after the `LENS:` line, and
  to no other prompt. `lensNotes` joins the `inputPrint` fingerprint. Observed by AC3, AC6.
- **S6** — Absent `lensNotes` is ANNOUNCED: one `log('WARNING: …')` line, and a clause in the
  synthesis prompt's RUN INTEGRITY block naming the lenses that received a note or saying none did.
  Observed by AC5.
- **S7** — The args header comment documents `lensNotes:` as a `name:` key, so the self-test's
  header arm keeps passing. Observed by AC7.
- **S8** — The tier2-review self-test's existing arms are re-keyed from the four-lens set to the
  five-lens set, and its `FLOOR_ASSERTIONS` is raised by exactly the assertions this unit adds.
  Observed by AC7.
- **S9** — The harness version moves `1.16` → `1.17` on the template's meta line, all three tokens
  on it: `version`, `gov:kit tier2-review@` and `gov:kit review-harness@`. Observed by AC9.
- **S10** — The render `tools/workflows/tier2-review.js` is regenerated from the template by the
  parity gate's render mode, never hand-edited, and lands in the same commit. Observed by AC10.
- **S11** — The lens count is corrected where a reader is told it: the meta phase detail, the root
  `README.md`, `WIRE-INTO-PROJECT.md`, and a new section of `tools/workflows/README.md` that lists
  the five diff lenses and documents `lensNotes`. Observed by AC11.

## 3. Non-goals (OUT)

- The checklist argument and its split across lenses. Between this unit and that one, no lens
  sweeps a bug-class checklist; the build lands as one, so no released harness carries the gap.
- `args.specs`, the commit-message default for every finder, and `renderBrief`. The intent lens
  brief here names its own sources so the lens works on the day it lands.
- `MAX_VERIFIERS`, the verify batching, and `tools/hooks/agent-cap.js`, none of which is edited.
- A light lens subset or any other way of running fewer than five diff lenses.
- Governance carriers (invariant 8 of the shared spec brief). Two now read incompletely and are
  left for the owner: the dimension-finder list in `memory/guides/REVIEW-PROTOCOL.md` names
  neither verification nor intent, and BUILD-METHOD M8's invocation block shows no `lensNotes`.
  The main loop parks both.
- The codebase-map dossier `memory/map/features/review-harnesses.md`: grepped at BASE, it names no
  lens key and no lens count, so nothing in it goes stale.

### Edges

- **hands-off** `TOOL-aSightedSkeptic-1` — that unit's prompt changes ride the one `REVIEW_SHAPE` bump made here.
- **hands-off** `TOOL-aSightedSkeptic-2` — the verify prompt and schema changes ride the same `REVIEW_SHAPE` bump.
- **hands-off** `TOOL-aSightedSkeptic-3` — the intent lens's documents arrive through `args.specs`; that unit may reword the intent brief's source sentence to read them first.
- **hands-off** `TOOL-aSightedSkeptic-4` — the checklist sweep the retired lens claimed, now owed by the split over the five lenses through `args.checklist`.
- **hands-off** `TOOL-aSightedSkeptic-7` — `LIGHT_LENSES` is chosen from the five keys pinned here.
- **hands-off** `TOOL-aSightedSkeptic-8` — every finding carries the `lens` key of one of these five.
- **hands-off** external — the owner turn on the two carriers named above, parked by the main loop.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that date.

- `DIFF_LENSES` is lines 326-347 of the template: four elements, the fourth `regressions`, whose
  brief tells the lens to run "the PROJECT's recurring-bug-classes checklist" and hands it none.
- `inputPrint` is line 396: `deriveFnv1a(renderCanonical({ context, byDesign, priorFindings }))`.
  The probe prompt at line 416 composes the key directory from `inputPrint` by interpolation, and
  `deriveReviewKey` at line 400 appends it. One edit to the object reaches both.
- The finder prompt's lens line is line 509, `LENS: ${L.brief}`.
- The RUN INTEGRITY block is lines 758-764 of the synthesis prompt.
- The meta phase detail on line 10 reads `4 finder lenses`.
- The args header comment is lines 74-81. The self-test's D9 arm reads every `a.<field>` after
  `const a = cfg` and requires each as a `name:` key there.
- The sample figures in the shared spec brief are the owner's analysis, PINNED at `ef1dcdb6`:
  could-not-fail checks are 13-19% of sampled findings, and no current brief names them.

### Data model

The five briefs, verbatim. Each is one or two sentences, and none names a web surface.

| key | brief |
|---|---|
| `security` | Security: trust boundaries for THIS kind of code. Commands built from interpolated input (shell, SQL, regex, paths), path traversal and symlinks, secrets reaching logs or output, authorization or enforcement that can be bypassed, and output from another program or agent trusted without validation. |
| `correctness` | Correctness: logic bugs, wrong conditionals and edge cases, off-by-one, type and encoding coercion drift, error and empty-input paths, and two copies of one rule that disagree. |
| `seams` | today's brief, unchanged |
| `verification` | Verification: does every behaviour this diff changes have a check that can FAIL? Report a test or gate whose fixture never triggers the rule, a predicate that matches nothing, a skip that reads as a pass, and a changed behaviour with no check at all. |
| `intent` | Intent: does the diff do what its stated intent says? Read the range's commit messages and any spec or design document the diff touches or those messages name, then report an acceptance criterion with no code behind it, a stated mechanism that is not the one built, and scope beyond what was asked. |

`lensNotes` shape: `{ "<lens key>": "<non-empty string>" }`. The legal keys are the keys of
`LENSES` for the current kind: the five above for `diff-review`, the four `SPEC_LENSES` keys for
`spec-audit`.

### Flow

1. The validation block sits directly after the `LENSES` line and before `inputPrint`, because it
   needs the current kind's keys and must run before the resume probe, the first agent. It is
   top-level code, not a function. Its refusals read:
   `tier2-review: \`lensNotes\` must be an object mapping a <kind> lens key to a non-empty string; legal keys: <k1 | k2 | …>. Got <JSON of the offending value or key>.`
2. Absent `lensNotes` logs
   `WARNING: no \`lensNotes\` supplied — every lens runs on the kit's generic brief, with no project addendum`.
3. `inputPrint` becomes
   `deriveFnv1a(renderCanonical({ shape: REVIEW_SHAPE, context, byDesign, priorFindings, lensNotes }))`.
   `REVIEW_SHAPE` is declared beside it with a comment stating invariant 5: one bump for the build.
4. The finder prompt, after `LENS: ${L.brief}`, carries
   `PROJECT NOTE FOR THIS LENS (from the caller's lensNotes): <note>` only where a note exists for
   `L.key`. Nothing is filtered off the `LENSES` receiver.
5. The RUN INTEGRITY block gains one clause: `lens notes supplied for: <keys>`, or
   `lens notes: none supplied, so every lens ran on the kit's generic brief`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `REVIEW_SHAPE` | top-level string constant | none; `.lexicon.conf` declares only `js.function` for this language |
| `lensNotes` | top-level constant and `args` field | none, as above |

No function is minted, so no name is asked of the lexicon.

### Rollout

The pass edits the template, writes the arms into the self-test, rewrites the three prose
carriers of the lens count, then runs the parity gate's render mode,
`bash tools/workflows/check-protocol-parity.test.sh --render`, so the render is regenerated rather
than typed. Template and render land in one commit with the version move.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` ·
`tools/workflows/tier2-review.test.sh` · `tools/workflows/README.md` · `README.md` ·
`WIRE-INTO-PROJECT.md`

### Alternatives rejected

Tested against the BASE source before the pick; the test that rejected each is named.

- **A sixth lens instead of retiring `regressions`.** `tools/hooks/agent-cap.js` sizes an array
  literal receiver and admits at most five elements, and the review protocol's lens allowance is
  the same number. A sixth element is denied at the tool call.
- **Filtering the receiver to skip a lens.** The shared spec brief's invariant 4 and the owner
  memory on map/filter chains: the hook refuses a reshaped receiver.
- **`REVIEW_SHAPE` as a new key segment.** Rejected in §8 F1: two sites spell the key format, the
  derivation at line 400 and the probe prompt at line 416, and a segment must be added to both.

## 5. Production-readiness checklist

- security — `lensNotes` is caller text interpolated into a finder prompt, the same principal and
  the same channel as `context`; no new trust boundary. A refusal message echoes the offending key
  through `JSON.stringify`, as the `kind` refusal already does.
- perf / scale — one more finder per diff review, inside the one wave the fan-out cap already
  bounds: five lenses at a cap of five is still one wave. Verify agents are unchanged.
- error / empty / loading states — every malformed `lensNotes` refuses before the first agent; an
  absent one defaults and is announced.
- observability — the WARNING line and the RUN INTEGRITY clause; the five `find:<key>` labels in the
  journal.
- risks — every lens file on disk under the old key stops being reused, which costs one full fan on
  the first re-run of an interrupted review after the upgrade. That is the intended effect of S3.
  Adopters whose own tests count four lenses will see that count move; the kit's README states it.
- testing — the new and re-keyed arms of the tier2-review self-test, run once at VERIFYING; the
  direct checks of §6 in the pass.
- migration — none; `lensNotes` is optional and absent means today's behaviour plus the warning.
- user docs — the new section of `tools/workflows/README.md`, and the two root documents' counts.

## 6. Acceptance criteria

- **AC1** — When the tier2-review self-test runs at VERIFYING, its arm
  `the diff lens set is security correctness seams verification intent` passes: a complete
  diff-review run over stub agents spawns exactly the `find:` labels `find:security find:correctness
  find:seams find:verification find:intent`, in that order. In the pass,
  `sed -n '/^const DIFF_LENSES = \[/,/^\]/p' tools/workflows/tier2-review.template.js | grep -oE "key: '[a-z]+'"`
  prints those five keys in that order and nothing else.
  Red when: the arm runs against the BASE render, which spawns four lenses ending in
  `find:regressions`.
  permission: the suite runs once, at VERIFYING, by the main loop; the RED-first observation is the
  main loop's, running the final suite in a frozen clone at this unit's parent commit.
- **AC2** — When `sed -n '/^const DIFF_LENSES = \[/,/^\]/p' tools/workflows/tier2-review.template.js | grep -ciE "client/server|loading|auth/RBAC|SSRF|regressions"`
  runs, it prints 0, where BASE prints at least 3.
  Red when: a brief keeps a web-application item or the retired key survives in the literal.
- **AC3** — When the self-test runs at VERIFYING, its arm
  `a lensNotes entry reaches its own lens prompt and no other` passes: with
  `lensNotes: { verification: 'NOTE-MARK' }`, the `find:verification` prompt carries `NOTE-MARK`
  and the other four `find:` prompts and every `verify:` prompt do not.
  Red when: the note is ignored, which is BASE, or appended to every lens.
  permission: as AC1.
- **AC4** — When the self-test runs at VERIFYING, its arm
  `a malformed lensNotes refuses before any agent spawns` passes over six cases: a string, an
  array, `null`, a key `regressions` on a diff review, a key `verification` on a spec audit, and a
  value `''`. Each throws a message carrying `lensNotes` and the legal key list, and each run's
  trace holds no agent. The same arm's control, `{ 'prior-art': 'n' }` on a spec audit, proceeds.
  Red when: any case is accepted, which is BASE for all six, or an agent spawns before the throw.
  permission: as AC1.
- **AC5** — When the self-test runs at VERIFYING, its arm
  `absent lensNotes is announced in the log and in RUN INTEGRITY` passes: a run with no `lensNotes`
  logs a line beginning `WARNING:` that names `lensNotes`, and its `synth` prompt carries
  `lens notes: none supplied`; a run with `{ security: 'n' }` logs no such warning and its `synth`
  prompt carries `lens notes supplied for: security`.
  Red when: the absence is silent, which is BASE.
  permission: as AC1.
- **AC6** — When the self-test runs at VERIFYING, its arm
  `a lens file written under another review shape is dispatched` passes: the arm evaluates the
  script once with the `REVIEW_SHAPE` literal rewritten, asserts the rewrite took and the two keys
  differ, then feeds a `find-security.json` under the rewritten key to the real script and observes
  `find:security` dispatched, and one under the real key reused. The key-component loop of the
  same suite gains the variant `another lensNotes`, observed both ways like its siblings.
  Red when: `REVIEW_SHAPE` or `lensNotes` does not reach `inputPrint`, so the old file is reused.
  permission: as AC1.
- **AC7** — When `grep -c "regressions" tools/workflows/tier2-review.test.sh` runs it prints 0,
  where BASE prints 6, and at VERIFYING the self-test's summary line reports at least its raised
  `FLOOR_ASSERTIONS`, with the args-header arm `the args header documents all` passing.
  Red when: an arm still names the retired lens, an added arm is stranded past an early exit, or
  `lensNotes:` is missing from the header.
  figure: the new floor is DERIVED by the pass, counted off the arms it adds, and stated in the
  commit's `Decided:` trailer; BASE's 6 is PINNED at `ef1dcdb6`.
- **AC8** — When `bash tools/workflows/check-verifier-fanout.sh`,
  `bash tools/workflows/check-review-join.sh` and `node tools/workflows/check-workflow-syntax.js`
  run, each exits 0.
  Red when: `DIFF_LENSES` gains a sixth element or the `LENSES` receiver is reshaped, either of
  which the agent-cap hook denies.
- **AC9** — When `bash tools/check-kit-versions.sh` runs it exits 0, and
  `grep -c "version: '1.17', // gov:kit tier2-review@1.17 // gov:kit review-harness@1.17" tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js`
  prints 1 for each file.
  Red when: one of the three tokens is left at 1.16, which the version gate pairs and reds.
- **AC10** — When `sed "s/{{FANOUT_CAP}}/5/g" tools/workflows/tier2-review.template.js | diff - tools/workflows/tier2-review.js`
  runs it prints nothing.
  figure: 5 is DERIVED, the value `bash tools/workflows/check-verifier-fanout.sh --print-cap` prints
  in this repository; re-read it before the observation.
  Red when: the render was hand-edited or not regenerated.
- **AC11** — When `grep -c "four finder lenses" README.md WIRE-INTO-PROJECT.md` runs it prints 0
  for each, `grep -c "4 finder lenses" tools/workflows/tier2-review.template.js` prints 0, and
  `grep -c "lensNotes" tools/workflows/README.md` prints at least 1.
  Red when: a reader is still told the old count, or the new argument is undocumented.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended-build self-test` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `review-join ban (no ref-keyed join)` · `workflow script syntax` · `kit version markers` · `lexicon naming predicates`

New arm: tools/workflows/tier2-review.test.sh · `the diff lens set is security correctness seams verification intent`, staged by the BASE render · FLOOR_ASSERTIONS raised by the count added
New arm: tools/workflows/tier2-review.test.sh · `a lensNotes entry reaches its own lens prompt and no other` · as above
New arm: tools/workflows/tier2-review.test.sh · `a malformed lensNotes refuses before any agent spawns`, six bad values · as above
New arm: tools/workflows/tier2-review.test.sh · `absent lensNotes is announced in the log and in RUN INTEGRITY` · as above
New arm: tools/workflows/tier2-review.test.sh · `a lens file written under another review shape is dispatched`, staged by rewriting the literal · as above

## 8. Open questions

- **F1 — Where does `REVIEW_SHAPE` join the review key?** (a) Into the object `inputPrint`
  fingerprints. (b) As a new segment of `deriveReviewKey`'s string. (b) must be spelled twice, in
  the derivation at line 400 and by hand in the probe prompt at line 416, and it changes the key's
  format, which the self-test's key-shape arm pins. (a) is one edit both sites already read, and the
  format is unchanged. Recommendation (a). RESOLVED (agent, 2026-10-01, delegated): (a), the
  option with fewer sites to keep in agreement and no open follow-up, M3's tie-break.
- **F2 — How is an absent `lensNotes` announced?** (a) A `WARNING:` log line and a RUN INTEGRITY
  clause, as invariant 2 of the shared spec brief states for every project-specific input. (b) A
  plain log line, since a missing addendum does not degrade a lens the way a missing checklist does.
  (b) disagrees with the shared invariant every sibling spec states, which M2's interface axis
  forbids, and a WARNING on a default run is what "never a silent default" means.
  Recommendation (a). RESOLVED (agent, 2026-10-01, delegated): (a), the option every sibling spec
  agrees with.
- **F3 — Who rewrites "four finder lenses" in `README.md` and `WIRE-INTO-PROJECT.md`?** (a) This
  unit, since it changes the count. (b) Park it for the owner. Neither file is a carrier that
  invariant 8 or BUILD-METHOD M11 names, so veto 2 does not reach them, and leaving them makes the
  shipped runbook state a false count. Recommendation (a). RESOLVED (agent, 2026-10-01,
  delegated): (a), the more feature-rich survivor; no veto applies.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the owner's mandate, the shared spec brief, and the
  template, its self-test and its render read at `ef1dcdb6`.

## 10. Reuse audit

The probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "the finder lens catalogue a review harness fans out over"
```

It ranked `deriveReviewKey` in `tools/workflows/tier2-review.template.js` and the agent-cap
`fanoutFindings` and `capFindings` among name-stem matches, and reported `.sh` as an unscanned layer.
The seams extended are all in the file this unit edits: the `DIFF_LENSES` literal, the
`inputPrint` fingerprint that `deriveReviewKey` and the probe prompt already read, the finder
prompt's `LENS:` line, and the synthesis prompt's RUN INTEGRITY block. For a per-lens caller
addendum no existing seam fits: no harness in `tools/workflows/` accepts one, and the drift-audit
siblings' `COMMON` block is shared by every lens rather than addressed to one. The recall hits
confirm the four-lens shape is recorded in closing reviews (aStagedLane) and the key's components in
TOOL-dDerivedDocket-29, and none records a decision to keep `regressions`.

Recall terms used: tier2-review DIFF_LENSES regressions lens brief finder security correctness seams review key inputPrint resume reuse

The question passed with them: "why does the tier2 review harness have four diff lenses including a
regressions lens, and how does the review key decide reuse".
