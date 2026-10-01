# TOOL-aSightedSkeptic-4 — a `checklist` argument whose classes are split across the lenses that run

**Status:** CLOSED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 4 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-4-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-4-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-4-2-build-brief.md) | journal | — |
| [2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md](../reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md) | diff-review | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |

<!-- /gen:spec-records -->

## 1. Goal

At BASE one lens of `tools/workflows/tier2-review.template.js` is told to run "the PROJECT's"
recurring-bug-class checklist, and the harness has no argument that could carry one. Callers in this
repository paste the checklist into `context` instead, so every lens receives every class: a 45-file
range selects 52 classes, too many for one agent to sweep. This unit adds `args.checklist`, splits
its items so each is swept by exactly one running lens, tells each lens to sweep its share against
the subject, and lets the run say which lens held which item. A run without one says so.

## 2. Scope (IN)

- **S1** — `parseChecklist(value)` is minted and called in the prelude, after the `kind` check and
  before the base-shape ladder, so a bad value refuses before any agent spawns. Absent
  (`undefined`), it returns no item. A STRING is read with `\r\n` folded to `\n`: lines before the
  first line starting `- ` are the PREAMBLE, each line starting `- ` opens an ITEM, and every
  following line up to the next item attaches to it, blank lines skipped and trailing whitespace
  trimmed. A whitespace-only string has no item. A string carrying non-whitespace and no item line
  REFUSES, naming the item shape and telling the caller to pass an array. An ARRAY is its items,
  each a string with non-whitespace content, and has no preamble. Any other value, or a bad array
  member, REFUSES with an Error whose message opens `tier2-review:` and names `checklist`, the rule
  and the value or index given. The result is `CHECKLIST_ITEMS` and the preamble beside it.
  Observed by AC1, AC2, AC5.
- **S2** — `deriveChecklistShares(items, keys)` is minted. It assigns item `n` (1-based, in the
  order given) to `keys[(n - 1) % keys.length]`, so every item is in exactly one share and every
  key has a share, possibly empty. It is called with the keys of the lenses that run, which at this
  unit is every lens of `LENSES` in order. Observed by AC1, AC3.
- **S3** — Each finder prompt carries a CHECKLIST block after its lens brief: the preamble, the
  count of its share against the whole, its items each labelled `C<n>`, and the instruction to sweep
  exactly those classes against the subject, to report only a FRESH hit (a defect of that class the
  subject introduces or touches), and to begin such a finding's claim with its `C<n>` label. A lens
  whose share is empty is told the items are held by the other lenses. With no item at all the block
  is absent. Skeptic prompts carry no share. Observed by AC1, AC3.
- **S4** — When a checklist has items, one log line before the Find phase names every lens's share
  by label, and the synthesis prompt's RUN INTEGRITY block gains a `Checklist:` sentence giving the
  item count and the per-lens split. Observed by AC3.
- **S5** — No checklist, or one with no item, is ANNOUNCED on both kinds: a `WARNING:` log line,
  worded apart for absent and for empty, and a `Checklist:` sentence in RUN INTEGRITY saying the
  project's recurring bug classes were not swept and a zero count is not evidence they are absent.
  Observed by AC4.
- **S6** — The spec kind splits over `SPEC_LENSES` the same way, sweeping "the spec set" in place of
  "the diff" (the build's invariant 7). Observed by AC6.
- **S7** — The parsed checklist joins the `inputPrint` fingerprint, so a lens file swept under one
  checklist is never reused under another; because the split is a pure function of the items and the
  keys, a reused lens held the share the current run would have handed it. Observed by AC7.
- **S8** — The `args` header documents `checklist:` as a `name:` key, and
  `tools/workflows/README.md` documents the argument, its two shapes and the split. Observed by AC8.
- **S9** — The template and its render land in one commit, the render produced by the parity
  renderer, with the per-pass direct checks green and the suite's assertion floor raised by the
  assertions this unit's arms execute. Observed by AC9.

## 3. Non-goals (OUT)

- Producing the checklist. The harness names no checker and no path into another kit (invariant 2);
  this repository's caller runs `python tools/memory-tree/gotchas.py --for-diff <range>` and passes
  its stdout.
- A keyword or vocabulary table routing items to lenses. §8 F1 records why it lost.
- A schema field for the class a finding hit. The `C<n>` claim prefix carries it without widening
  `FINDING_SCHEMA`.
- The lens set, the lens briefs, `REVIEW_SHAPE` and the version: `TOOL-aSightedSkeptic-5`'s.
- Which lenses run under a light intensity. That is the edge below.
- The harnessed spec audit's call in `tools/workflows/unattended-build.template.js`, which passes no
  checklist and will announce the absence on every audit; and M8's invocation block in
  `memory/guides/BUILD-METHOD.md`, a governance carrier (invariant 8), parked by the main loop.
- The codebase-map dossier's prose, refreshed once at the close rather than by each unit.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-5` — the five `DIFF_LENSES` keys the split runs over, and
  the lens set in which no brief tells a lens to run an unnamed project checklist any more.
- **hands-off** `TOOL-aSightedSkeptic-7` — under `LIGHT_LENSES`, the split is computed over the
  lenses that actually run, not the declared five, so no item lands on a skipped lens.
- **hands-off** external — M8's invocation block in the build method, to the owner, if
  `checklist` is to be shown there.
- **hands-off** external — the harnessed spec audit's call, which announces a missing checklist
  until its caller supplies one.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that date.

- The only checklist text in the template is the `regressions` brief, "run the PROJECT's
  recurring-bug-classes checklist against the diff and report only fresh hits", and no `args`
  field carries one.
- Closing reviews here pass the checklist through `context`, so every lens receives all of it:
  `memory/builds/dMendedRecall/reviews/2026-10-01-review-TOOL-dMendedRecall-1-closing-diff-round1.md`
  records "31 anchored classes plus 6 universal" handed that way.
- `python tools/memory-tree/gotchas.py --for-diff` prints two `#` header lines, then one item per
  class: a `- [ ] <name>` line followed by indented lines carrying a one-line description and the
  path of the class's note, items separated by blank lines. Every item therefore names its class and
  describes it without a lens brief. Two real ranges, PINNED 2026-10-01: `0cfdd64b~6..0cfdd64b`
  (49 files) selected 52 items, and `ef1dcdb6~2..ef1dcdb6` (31 files) selected 43.
- The brief records 11 to 88 classes over 21 past closing ranges, median about 30, PINNED at the
  brief's writing.

### Data model

```
args.checklist   : string | string[]          // absent => no item
parseChecklist(v)  -> { preamble: string, items: string[] }
CHECKLIST_ITEMS  : string[]                   // the items, in the order given
deriveChecklistShares(items, keys) -> { <key>: [{ n, text }] }   // n is 1-based; item n -> keys[(n-1) % K]
```

### The CHECKLIST block in a finder prompt

```
CHECKLIST — the project's recurring bug classes, split across the lenses so each is swept once.
<preamble, when one was given>
This lens holds <m> of the <N> items; the others hold the rest.
C<n> <item text>
…
Sweep EACH class above against <the diff|the spec set> and report only a FRESH hit: a defect of
that class the <diff|spec set> introduces or touches. Begin such a finding's claim with its C<n>
label. A class with no hit needs no finding.
```

An empty share reads `This lens holds none of the <N> items; the other lenses hold them all.`

### Announcement and integrity

```
checklist: <N> item(s) over <K> lens(es), each swept by exactly one — <key> C1 C6 …; <key> C2 C7 …
WARNING: no `checklist` was supplied — no lens sweeps the project's recurring bug classes; pass the caller's checklist output as `checklist`
WARNING: `checklist` was supplied with no item — no lens sweeps the project's recurring bug classes
```

RUN INTEGRITY gains `Checklist: <N> item(s), each assigned to exactly one of <K> lens(es): <key> <m>, …`
or, with no item, `Checklist: NONE swept — <absent|supplied with no item>; a zero count is not
evidence the project's recurring bug classes are absent.`

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `parseChecklist` | function, verb `parse` | `js.function` |
| `deriveChecklistShares` | function, verb `derive` | `js.function` |
| `CHECKLIST_ITEMS` | module constant | none: constants are not graded |

Both names read `OK` from `python tools/lexicon/lexicon.py --suggest <name> --as js.function` on
2026-10-01. `parse` fits because a non-blank string with no item raises; `derive` because the split
is computed from the items and the keys and never authored.

### Rollout

Edit the template, run `bash tools/workflows/check-protocol-parity.test.sh --render`, commit the
template and `tools/workflows/tier2-review.js` together. Write the arms, observe each RED against the
render as it stood before this unit's commit by running a slice of the suite's runner holding only
that arm, and raise `FLOOR_ASSERTIONS` by the count the new arms execute, counted off the block.
`deriveChecklistShares` runs over the lens keys, not as a reshaping of the `LENSES` receiver, so the
fan-out stays the marked literal (the build's invariant 4).

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh` · `tools/workflows/README.md`

### Alternatives rejected

Three candidates differing in MECHANISM were tested against the two real checklists in Evidence
before choosing; each candidate's losing condition was written down first.

- **(a) Every lens receives every item and self-selects.** Loses if the run cannot say which lens
  swept which item. It cannot: self-selection leaves no record, and each lens carries all 52 or 43
  items, which is the status quo the mandate's finding 4 names as too many for one agent. It also
  contradicts the brief's pinned "every item is assigned to EXACTLY ONE running lens".
- **(c) Keyword routing of item text to lens briefs.** Loses if any lens carries more than twice its
  fair share on a real checklist. A routing table of eleven to fourteen words per lens, run over the
  two checklists in the scratchpad, put 31 of 52 and 25 of 43 items on the verification lens, 60%
  and 58% against a fair share of 20%, and matched no keyword for 10 and 9 items. A tuned table
  could do better on this corpus, and it would then encode this repository's vocabulary into a
  harness the build requires to assume nothing about an adopter.
- **(b) Round-robin by item order** survived. Loses if an item cannot be swept without the brief of
  the lens it lands on; every item measured carries its class name, a description and a note path,
  so it is self-describing. The largest share is the ceiling of N over K, 11 of 52 and 9 of 43 at
  five lenses, and the split is deterministic, which is what lets S7's reuse stay correct.

## 5. Production-readiness checklist

- security — N/A: the checklist is caller text interpolated into prompts, the trust the caller's
  `context` already has; nothing is executed or written from it, and a malformed value refuses
  before any agent spawns.
- perf / scale — each lens's prompt grows by its share only, about a fifth of the checklist; an
  88-class checklist puts at most 18 items on one lens at five lenses.
- error / empty / loading states — absent and empty are each announced in their own words; a
  non-blank string with no item refuses rather than collapsing into one item; an empty share is
  said in the prompt rather than left blank.
- observability — the share log line, the WARNING lines, and the `Checklist:` sentence in every
  report; the `C<n>` prefix lets a report or a later ledger attribute a hit to its class.
- risks — round-robin may hand a class to a lens whose brief is far from it, which the item's own
  description mitigates; a checklist in another shape must be passed as an array, which the refusal
  tells the caller.
- testing — the arms of §6, each observed RED before this unit's commit.
- migration — none: an absent `checklist` behaves as before plus the announcement, and the key moves
  once for the build through `REVIEW_SHAPE`.
- user docs — `tools/workflows/README.md` and the `args` header (S8).

## 6. Acceptance criteria

Every arm named below is written into the suite beside the template by this unit's pass and
observed RED there against the render as it stood before the commit. Its passing reading is the
main loop's single suite run at `VERIFYING`, which the acceptance ledger cites.

- **AC1** — When the stub-agent runner evaluates a diff review whose `checklist` is a string of a
  two-line `#` preamble and seven `- [ ] ` items, arm
  `checklist string: every item in exactly one finder prompt` passes: across the five `find:`
  prompts each item's text occurs exactly once, item `n` sits in the prompt of the lens at position
  `(n - 1) % 5` in lens order labelled `C<n>`, every prompt carries the preamble and the instruction
  to begin a hit's claim with its label, and no `verify:` prompt carries an item.
  Red when: an item is in two prompts or in none, the order is not round-robin, or a skeptic is
  handed a share.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC2** — When the same checklist is passed with `\r\n` line ends and with indented continuation
  lines, arm `checklist string: continuation lines stay with their item` passes, each item's
  continuation text in the same prompt as its `- ` line; and when it is passed as a seven-element
  array, arm `checklist array: each element is one item` passes with the same split and no preamble.
  Red when: a CRLF string parses differently from its LF twin, or a continuation line lands in
  another lens's share.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC3** — When the AC1 run is read, arm `checklist: the log names every lens's share` passes: the
  captured log holds one `checklist:` line naming each lens key with its labels, and the `synth`
  prompt's RUN INTEGRITY block holds `Checklist:` and the item count. When a three-item checklist is
  passed, arm `checklist: fewer items than lenses leaves an explicit empty share` passes: two
  `find:` prompts carry `holds none`.
  Red when: the assignment is not recoverable from the log, or an empty share reads as no checklist.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC4** — When the runner evaluates a diff review with no `checklist`, arm
  `checklist absent: announced in the log and RUN INTEGRITY` passes: a `WARNING:` line names
  `checklist`, the `synth` prompt carries `Checklist: NONE swept`, and no `find:` prompt carries
  `CHECKLIST`. With `checklist: '   '`, arm `checklist empty: announced as supplied with no item`
  passes; with AC1's checklist, its control arm `checklist supplied: no checklist warning` passes.
  Red when: either absence is silent, or the warning fires over a checklist with items.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC5** — When the runner evaluates a diff review with each of `checklist: 7`, `checklist: {}`,
  `checklist: null`, `checklist: [1]`, `checklist: ['  ']` and `checklist: 'no item line here'`,
  the arm `checklist refused before any agent` for that value passes: the run throws a message
  containing `checklist`, and the trace holds no agent label.
  Red when: a malformed value reaches a lens, or a non-blank string with no item becomes one item.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC6** — When the runner evaluates a spec audit with AC1's checklist, arm
  `spec-audit: the checklist splits over the spec lenses` passes: each item occurs in exactly one of
  the four `find:` prompts, which say `the spec set`.
  Red when: the spec kind is handed no share, or a share over keys it does not run.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC7** — When the args-variant loop of the suite carries the variant `another checklist`, its two
  arms pass: a lens file written under the key without a checklist is dispatched, and one written
  under the variant's own key is reused.
  Red when: the checklist is missing from `inputPrint`, so a lens swept under no checklist is reused.
  permission: the suite run is the main loop's, at `VERIFYING`.
- **AC8** — When `grep -n 'checklist:' tools/workflows/tier2-review.template.js` runs, a line inside
  the `args` header block is listed, and the header arm `the args header documents all` passes;
  `grep -c -F 'checklist' tools/workflows/README.md` prints at least 1, where BASE prints 0.
  Red when: the header or the README omits the field.
- **AC9** — When the pass has committed, `node tools/workflows/check-workflow-syntax.js`,
  `bash tools/workflows/check-verifier-fanout.sh` and `bash tools/workflows/check-review-join.sh`
  each exit 0, `git diff --exit-code tools/workflows/tier2-review.js` exits 0 after a fresh run of
  the parity renderer, and `python tools/lexicon/lexicon.py --suggest parseChecklist --as js.function`
  and the same for `deriveChecklistShares` each print a line opening `OK`.
  Red when: the render was hand-edited or not regenerated, the fan-out receiver was reshaped, or a
  name leads with an undeclared verb.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/workflows/tier2-review.test.sh` · stub-agent runs with a checklist as a string, a CRLF string, an array, three items, none, an empty one, six malformed values, a spec audit, and one args variant · `FLOOR_ASSERTIONS` raised by the count the new arms execute

## 8. Open questions

- **F1 — How are the items split across the lenses?** (a) Every lens gets everything and
  self-selects. (b) Round-robin by item order over the lenses that run. (c) Keyword routing of item
  text to lens briefs. §4 Alternatives rejected records each candidate's losing condition and the
  measurement that decided it: (a) cannot say which lens swept what and contradicts the pinned
  exactly-one rule; (c) put 58% to 60% of two real checklists on one lens and would encode one
  repository's vocabulary. (b) meets every criterion. Recommendation (b). RESOLVED (agent,
  2026-10-01, delegated): (b), the most feature-rich survivor after M3's vetoes.
- **F2 — What does a non-blank string with no `- ` item do?** (a) Become one item. (b) Refuse,
  telling the caller to pass an array. (a) puts a whole checklist on one lens, the defect this unit
  exists to remove, and does it silently; (b) is the build's invariant 3 and costs a caller one
  conversion. Recommendation (b). RESOLVED (agent, 2026-10-01, delegated): (b).
- **F3 — Does the absence announce on the spec kind too?** (a) Diff kind only. (b) Both. Invariant 7
  applies this unit to both kinds, and invariant 2 announces every absent project input.
  Recommendation (b). RESOLVED (agent, 2026-10-01, delegated): (b); the harnessed audit's caller is
  the edge in §3.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the build's spec brief, the run mandate, the template read
  at `ef1dcdb6`, and two checklists `gotchas.py` produced for real ranges.

## 10. Reuse audit

The codebase-map probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "split a recurring bug class checklist across review lenses so each class is swept once"
```

It ranked name-stem neighbours only (`derive_tool_class` and `contrib_propose_class` among them,
none of which partitions a list across agents) and reported `.sh` as an unscanned layer. No existing
seam fits the split: the harness's only partition, `chunk`, slices findings into contiguous skeptic
batches, and a contiguous split would hand one lens a run of neighbouring classes and the last lens
the short remainder, so round-robin is written instead. The seams extended are the review harness,
claimed by `memory/map/features/review-harnesses.md`: the prelude's `kind` refusal for the
validation shape, the finder prompt beside the lens brief, the RUN INTEGRITY block, and
`inputPrint`. The recall probe surfaced `TOOL-aFoldedQuarry-6`, which made the `--for-diff` stdout
the reviewer checklist, and closing-review records handing that stdout through `context`, which is
candidate (a) as practised.

Recall terms used: gotchas.py --for-diff checklist recurring-bug-class regressions lens tier2-review lens brief closing review M8 bug classes sweep

The question passed with them: "how does a closing review receive the recurring bug-class
checklist, and which lens sweeps it".
