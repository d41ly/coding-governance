# TOOL-dFairHearing-4 — skeptic batches sorted by cited address

**Status:** DEFERRED · rev-4 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0071@8d3a19dc whole

**Carries:** node:item.review.refute

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-4-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-4-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md) | research | TOOL-dFairHearing-18 TOOL-dFairHearing-27 TOOL-dFairHearing-25 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md) | spec-audit | TOOL-dFairHearing-14 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 |

<!-- /gen:spec-records -->

## 1. Goal

The review harness sorts its findings by one shared address key before it slices them into the
fixed count of skeptic batches, so two lenses citing one defect meet one skeptic. Today ids are
assigned lens by lens and `chunk` slices them contiguously, so 70 of 924 cross-lens same-address
pairs (8%) share a skeptic, and each of the 9 verified refutations by design beside a confirmed twin
sat in a different batch (`gap-review-06`; PINNED 2026-10-15 by the research instrument I15,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication-instruments.md:300-313`,
where the same sort raised the share to 541 of 924, 59%). The sort ships behind a default-off
argument, so `TOOL-dFairHearing-1`'s replay can run it against today's batches.

## 2. Scope (IN)

- **S1** — `deriveAddressKey(f)`, the one address key, and `checkSameAddress(a, b)`, its equality
  with the diff kind's ±3-line slack, both pure and defined once in the prelude of
  `tools/workflows/tier2-review.template.js`. Observed by AC1, AC2.
- **S2** — `deriveAddressOrder(findings)`, a sorted copy of the findings by that key, ids breaking
  ties. Observed by AC3.
- **S3** — the `batchBy` argument, a closed set `id` or `address`, default `id`, refused outside the
  set before any agent, and documented in the `args` header. Observed by AC4.
- **S4** — the verify stage slices `verifyOrder`, the findings in the order `batchBy` picks, through
  the same `chunk(x, Math.ceil(x.length / MAX_VERIFIERS))` line marked `gov:fixed-verifiers`, so the
  skeptic count and the batch sizes are unchanged. Observed by AC5, AC7.
- **S5** — each batch is labelled `verify:batch-<n>`, its resume file is `verify-batch-<n>.json`, and
  that file carries its member ids as `ids`, on both orders. Observed by AC5, AC6.
- **S6** — the carriers that spell the label, the file name or the argument:
  `tools/workflows/README.md` and the review protocol, template and render. Observed by AC8.
- **S7** — the suite arms the `New arm:` line in §7 declares. Observed by AC1, AC2, AC3, AC4, AC5,
  AC6 through that line, RED-first at the close.

## 3. Non-goals (OUT)

- No default flip. `batchBy` stays `id` until `TOOL-dFairHearing-1`'s replay records a hit, which is
  that unit's verdict (the brief's S9).
- No same-address pair handed to the synthesis: that is `TOOL-dFairHearing-7`, which calls S1.
- No change to a skeptic prompt's judging text, its schema's verdict fields or the join on the
  orchestrator-assigned integer id. A batch's membership and order move, nothing it is asked.
- No `REVIEW_SHAPE` move. The review key does not need one: every verify file this unit can reuse is
  named `verify-batch-<n>.json`, which no run before this unit wrote, and each is matched by its batch
  print over the ids, claims and fixes it judged (template :1362).
- No address sort in `tools/workflows/drift-audit-code.template.js` or
  `tools/workflows/drift-audit-state.template.js`: the clause names the review's skeptic batches.
- No diff-kind instruction that a verdict name its probe. `item.review.refute`'s full witness in
  the flow-steps record also asks that, and §8 F6 settles why this unit does not add it.
- No scorer change. The replay scorer's address reading is `TOOL-dFairHearing-12`'s, written to agree
  with S1 field for field.
- No help page: no page under `help/` describes the review harness (`help/README.md`,
  `help/measure-legs.md`, `help/roles.md` are the whole folder).
- No kit version moved: the lander mints them (`tools/push-main.sh:26-32`).

### Edges

- **hands-off** `TOOL-dFairHearing-7` — the same-address pairs it hands the synthesis are judged by
- **hands-off** `TOOL-dFairHearing-32` — the round-3 spec audit's minors on this spec, ids 2, 10, 14, 15, 19, 23, 32 and 33: the resume probe's spelling observed (its S1 to S4), the section class widened (its S5), the third difference named (its S6) and the scorer non-goal restated (its S7, S8); AC8's absence patterns, §4's section class and "two named places", and §3's "field for field" are superseded there
  `checkSameAddress` over `deriveAddressKey`, the one key, and it defines no address reading of its own
- **hands-off** `TOOL-dFairHearing-1` — the replay runs the address-ordered verify stage through this
  unit's default-off argument and owns the verdict that would flip its default
- **hands-off** `TOOL-dFairHearing-12` — `deriveAddressKey`'s spec-kind reading (the first `[tag]`,
  else the leftmost section token), which its `extract_tag_ref` agrees with on the tag and the `§<n>`
  forms rather than spelling a second address reading
- **hands-off** `TOOL-dFairHearing-18` — the whole-design preset's address reading calls this unit's
  key rather than spelling a second one
- **hands-off** `TOOL-dFairHearing-23` — finding id 52 of the round-1 spec audit: the address key folding a repo-absolute path and a drive letter's case (its S48, AC39)

## 4. Design

### The address key

`deriveAddressKey(f)` returns `{ file, at, lens, id }`. It is defined beside `renderAuditBinding`
(template :318-328), inside the prelude the suite slices, and reads the run's kind from `isSpec`
(template :199). It never reads `f.ref`, so no Map or object is keyed on a `.ref` string, which
agent-cap's RULE 5 refuses (`tools/hooks/agent-cap.js:1780-1784`).

- `file` is `String(f.file)` trimmed, every `\` folded to `/`, and one leading `./` dropped.
- On the diff kind `at` is `f.line` when it is an integer, else `null`.
- On the spec kind `at` is read from `f.where`: the first `[tag]` anywhere in it, a lower-case slug in
  brackets, wins. Failing one, the LEFTMOST section token does: `section <n>` or `§ <n>`, normalised to
  `§<n>`; or a whole-word `S<n>` or `AC<n>`, normalised to upper case. Failing both, `at` is `null`.
  An empty or multi-address `where` therefore takes its first address.
- `lens` and `id` are the finding's own: `lens` the key the harness dispatched (template :1246), `id`
  the integer it assigned (template :1247).

The reading reproduces the key the research measured, not a literal sort, which the debt round found
does not reproduce the gain (`batch-sort-key`,
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md:234`).
The instrument's `loc` (`…-research-review-adjudication-instruments.md:1661-1667`) took the same
tag, then the same four section forms. It differs in two named places: a token here must stand as a
whole word, and an unaddressed spec finding falls to its lens rather than to its whole `where` text,
as the review system record's design says (`2026-10-15-build-PLAY-dClosedLoop-1-review-system.md:206-208`).

`checkSameAddress(a, b)` takes two keys. It is true when the files are equal, neither `at` is `null`,
and the diff kind's lines differ by at most `ADDRESS_LINE_SLACK`, the constant 3, or the spec kind's
tokens are equal. A finding with no address is never the same address as anything, so a lens's
unaddressed findings are never read as twins of each other. The slack lives here and not in the sort,
because a tolerance cannot be a sort key: equality within ±3 is not transitive (§8 F2).

`deriveAddressOrder(findings)` returns a new array sorted by `file`, then `at` (integers by value,
tokens by code unit, `null` after every address of its file), then `lens`, then `id`. It never sorts
its argument in place: `allFindings` keeps id order for the ledger, the appendix and the lens yield.

### The verify stage

At template :1352-1353:

```js
const MAX_VERIFIERS = {{FANOUT_CAP}}
const verifyOrder = batchBy === 'address' ? deriveAddressOrder(allFindings) : allFindings
const batches = chunk(verifyOrder, Math.ceil(verifyOrder.length / MAX_VERIFIERS)) // gov:fixed-verifiers
```

The marked line keeps the one shape agent-cap admits for a verifier receiver, `chunk(x,
Math.ceil(x.length / K))` with `K` a bound identifier (`tools/hooks/agent-cap.js:481-485`, its regex
at :632), so the hook and `tools/workflows/check-verifier-fanout.sh`, which pipes each harness to it
(:206-212), read the same bound. The comment above it (template :1347-1351) loses its claim that a
label names a contiguous id range and states that the order is `batchBy`'s. The log line after it
(template :1354) appends `by id` or `by address`, so a run's record says which batches it built.

`batchBy` is read beside `intensity` (template :210-217): absent reads `id`, and anything but the
strings `id` and `address` throws, naming the field and the two legal values, before the resume probe
spawns. The `args` header (template :91-139) gains a `batchBy:` key line, which the suite's D9 arm
requires of every field read off `a` (`tools/workflows/tier2-review.test.sh:303-313`). It does not
join the review key's input print: a verify file is reused only for the exact members and order its
batch print covers, so an `id` run's file can never answer an `address` run's batch of other members.

### Labels and resume files

- `batchLabels` (template :1363) becomes `verify:batch-${gi + 1}`, on both orders.
- The reuse lookup (template :1364-1373) looks for `verify-batch-${gi + 1}.json`, still requiring the
  run's key and the batch print.
- The skeptic's durability instruction (template :1427-1431) writes `verify-batch-<n>.json` and adds
  `"ids":[<the batch's ids, in batch order>]` beside `key` and `batch`.
- The keyed schema for verify files (template :1037) requires `ids`, an integer array, added to the
  properties `buildKeyedSchema` declares (template :66-72), so a file in the old shape is skipped by
  name and its batch dispatched.
- The resume probe's instruction (template :1021) names `find-<lens>.json or verify-batch-<n>.json`.

A batch label no longer tells its ids, so the file carries them; `pending` and the log keep naming the
label, which is what a re-run dispatches.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `deriveAddressKey` | function, `tools/workflows/tier2-review.template.js` | `js.function`, OK |
| `deriveAddressOrder` | function, same file | `js.function`, OK |
| `checkSameAddress` | function, same file | `js.function`, OK |
| `ADDRESS_LINE_SLACK` | constant, same file | none |
| `verifyOrder` | constant, same file | none |
| `batchBy` | harness argument | none |
| `verify:batch-<n>` | agent label stage | none |
| `verify-batch-<n>.json`, `ids` | resume file name and field | none |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as js.function`
and answered OK.

### Migration

None. A verify file named `verify-<a>-<b>.json` under an older key is never looked up again, so a
resumed run dispatches that batch afresh, which a resume already does for any file it cannot match.

### Rollout

Dark: the default `id` slices exactly the batches today's code slices, renamed. The replay runs
`batchBy: 'address'`.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`, its render
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`: the `args` paragraphs beside `intensity` (:270-276) and the agent-label
  table's verify row (:456)
- `tools/workflows/REVIEW-PROTOCOL.template.md`: the resume file name at :210
- `memory/guides/REVIEW-PROTOCOL.md`, its render

The two renders come from `bash tools/workflows/check-protocol-parity.test.sh --render`, the pairs'
documented writer (that script's header, line 6). The suite's 25 `verify:ids` references are
rewritten to the new labels as part of its edit.

### Alternatives rejected

- **One batch per file or section.** It brings 7 of 8 verified twins together, but the largest batch
  grows in 41 of 50 reports, up to 3.83 times (the research record's candidate 3a,
  `…-research-review-adjudication.md:97`), and a fixed count was the point of `MAX_VERIFIERS`.
- **A string key with the line bucketed to fours.** It is a sort key and an equality at once, but
  lines 11 and 12 fall in two buckets and lines 8 and 11 in one, so it misses twins the ±3 rule names.
- **The `ref` string as the key.** It is display-only after the id join (template :1239-1240), and a
  Map keyed on it is the join RULE 5 bans.

## 5. Production-readiness checklist

- security — no new write path. The skeptic's durability write gains one field in a file it already
  writes under the key directory; the key derivation reads no `ref`.
- perf / scale — one sort of the raw findings, O(n log n) over tens of findings, once per run.
- error / empty / loading states — an illegal `batchBy` refuses before any agent; a finding with no
  address sorts last in its file and is never a twin; a verify file without `ids` is skipped by name.
- observability — the existing log line `<n> finding(s) -> <k> verifier(s)` gains the order, `by id`
  or `by address`, so a run says which batches it built.
- risks — a batch boundary can still split one address's findings, the 41% the research left apart;
  the replay reports the same-batch rate under the key built.
- testing — the pass probes S1 to S5 by a prelude slice and a stub-agent run, and the hook by a direct
  payload; the suite arm in §7 is observed RED then GREEN by the main loop at the close.
- migration — none, as §4 Migration says.
- user docs — none owed: §3 names the help folder and why it does not change.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut
  as `tools/workflows/tier2-review.test.sh:67-81` cuts it and returning `deriveAddressKey` as
  `tools/workflows/tier2-review.test.sh:237` returns `renderAuditBinding`, a diff-kind run keys
  `{file: '.\\src\\a.js', line: 12, lens: 'security', id: 3}` to
  `{file: 'src/a.js', at: 12, lens: 'security', id: 3}`. A spec-kind run keys the `where` values
  `section 4 [walk-table] Design`, `section 2 S5`, `AC3 against section 6`, `§ 7` and
  `status header` to the `at` values `[walk-table]`, `§2`, `AC3`, `§7` and `null`.
  Red when: the tag is read only after the section token, so `section 4 [walk-table] Design` keys
  to `§4`.
- **AC2** — When the same probe returns `checkSameAddress`, two diff keys on one file at lines 10 and
  13 are the same address, at 10 and 14 are not, at line 10 of two files are not, and a key whose `at`
  is `null` matches nothing, itself included. Two spec keys at `§2` are the same address and at `§2`
  and `§3` are not.
  Red when: the slack is tested as `< 3`, so lines 10 and 13 read as two addresses.
- **AC3** — When the probe calls `deriveAddressOrder` on six diff findings in id order, ids 1 and 4
  citing `a.js` at lines 100 and 42 from two lenses, it returns a new array holding the `a.js`
  findings adjacent with line 42 first, ordered by file, line, lens and id, while the array passed in
  still reads ids 1 to 6 in order; a spec finding whose `at` is `null` sorts after every addressed
  finding of its file.
  Red when: lines compare as strings, so line 100 sorts before line 42.
- **AC4** — When the prelude is evaluated as the suite's `arm` does (`tools/workflows/tier2-review.test.sh:89-99`),
  `batchBy` absent, `'id'` and `'address'` each proceed and resolve to that value, absent to `'id'`;
  `'section'`, `1` and `null` each throw naming `batchBy`.
  Red when: the refusal is removed and `'section'` proceeds on id-ordered batches.
- **AC5** — When a scratch stub-agent run of `tools/workflows/tier2-review.js`, shaped as
  `tools/workflows/tier2-review.test.sh:333-357`, hands a diff review five lenses of two findings
  each, every lens's first finding citing `a.js` line 10 and its second its own file, the run with
  `batchBy: 'address'` puts the five `a.js` findings in three consecutive batches, and the run without
  it puts no two `a.js` findings in one batch. Both spawn exactly five skeptics labelled
  `verify:batch-1` to `verify:batch-5`, and each verify prompt names `verify-batch-<n>.json` and an
  `"ids":[` list equal to its own findings' ids.
  Red when: `chunk` still slices `allFindings`, so the address run's batches equal the default's.
  cost: a scratch runner of about 60 lines, modelled on that suite's stubs.
- **AC6** — When the same runner's resume probe returns every lens file and a verify file named
  `verify-batch-1.json` carrying the run's key, the batch print the first verify prompt names, and
  `ids`, that batch is not dispatched and `batchesReused` is 1, as
  `tools/workflows/tier2-review.test.sh:600-613` observes for today's name. The same file named
  `verify-1-2.json` is dispatched, and so is one lacking `ids`.
  Red when: the reuse lookup still builds `verify-<first>-<last>.json`, so the new file is never
  reused.
- **AC7** — When the payload `tools/workflows/check-verifier-fanout.sh:206-212` builds is made from
  `tools/workflows/tier2-review.js` and piped to `node tools/hooks/agent-cap.js --only=scripts`, it
  exits 0; made from a scratch copy whose marked line reads
  `chunk(verifyOrder, 1) // gov:fixed-verifiers`, it exits non-zero.
  Red when: the `batches` line drops its `gov:fixed-verifiers` marker or splits across lines, and the
  hook denies the render.
- **AC8** — When `git grep -n -e 'verify:ids' -e 'verify-<first id>'` runs over `tools/` and
  `memory/guides/`, it prints nothing; `grep -n 'verify:batch-<n>'` finds the verify row of `tools/workflows/README.md`;
  `grep -n 'verify-batch-<n>.json'` finds the resume sentence of
  `tools/workflows/REVIEW-PROTOCOL.template.md` and `memory/guides/REVIEW-PROTOCOL.md`; and
  `grep -n 'batchBy'` finds the README's argument paragraph and the template's `args` header.
  Red when: the template is edited and the README's verify row still reads `verify:ids-<a>-<b>`.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `verifier fan-out` · `unattended-build self-test` · `review-join self-test` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the base harness, which defines no address key, refuses no batchBy value, slices id-ordered batches on every run and names verify files by id range · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`, which the header
  regex at `tools/memory-tree/tree_lib.py:377` joins. Observation, 2026-10-23: the set is
  `OPEN SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO`, so a `DRAFT` header parses as no header and
  the unit reads MISSING. Liveness: the probe reads the tuple that would carry `DRAFT` if the
  vocabulary admitted it. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, the token
  `memory/TEMPLATE-SPEC.md` gives a spec in drafting.
- **F2 — Where does the ±3-line slack of the brief's S4 live, given one key must both sort and
  compare?** Options: (a) a key object for the sort plus `checkSameAddress` for equality, the slack in
  the latter; (b) a string key with the line bucketed, one value for both; (c) a clustering pass that
  assigns each finding a cluster anchor before the sort. (b) misses twins at a bucket edge, which fails
  the slack the brief states; (c) is order-dependent under a non-transitive relation and adds a pass
  nothing else needs. (a) keeps `deriveAddressKey(f)` spelled as the brief spells it and adds one pure
  predicate beside it. RESOLVED (agent, 2026-10-23, delegated): (a), by M3's most criteria satisfied,
  rung 3.
- **F3 — Which section tokens does the spec kind read: the brief's `[tag]` then `§<n>`, or the
  research's set?** The review system record says "the first `[tag]` or section token"
  (`2026-10-15-build-PLAY-dClosedLoop-1-review-system.md:206-207`), and the instrument that measured
  the 59% read `section <n>`, `§<n>`, `S<n>` and `AC<n>` (`…-research-review-adjudication-instruments.md:1661-1667`);
  the debt round found a key that does not reproduce the measurement does not reproduce the gain.
  RESOLVED (agent, 2026-10-23, delegated): the research's set, normalised as §4 states, by rung 1:
  the design record states the token class and its instrument defines it. The brief's spelling is
  the subset this extends, so no other writer's reading changes.
- **F4 — Does the label rename ride the default `id` order too?** Options: (a) `verify:batch-<n>` on
  both orders; (b) the old id-range label under `id` and the new one under `address`. (b) keeps two
  label grammars, two file names and two reuse lookups in one harness, and its old label is true only
  of one order. RESOLVED (agent, 2026-10-23, delegated): (a), by fewer open questions, rung 3.
- **F5 — What is the dark switch: an argument or a conf key, and its spelling?** Options: (a) a harness
  argument `batchBy`, a closed set refused outside it, the shape `intensity` takes; (b) a default-off
  key in a kit conf. The harness has no filesystem at run time, so a conf key would still reach it as
  an argument a caller reads and passes. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3.
- **F6 — Does carrying `item.review.refute` oblige the diff skeptic to name its probe in each
  verdict?** The flow-steps record's witness for the item asks that every finding has one verdict
  and each verdict names its probe (`2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:572`); the
  ownership record assigns the item to this build through this clause alone, "skeptic batches sorted
  by cited address" (`2026-10-17-build-PLAY-dClosedLoop-1-ownership.md:78`). One verdict per finding
  already holds: the join counts every finding with no usable verdict as unverified (template
  :1445-1469). RESOLVED (agent, 2026-10-23, delegated): no prompt change here, by rung 1, the
  ownership record.
- **F7 — Editing the review protocol's resume-file sentence changes a governance carrier; does the
  build's grant cover it?** `PLAY-dClosedLoop-3` grants the carrier changes a build's own clauses name.
  This clause moves the file name, and clause `cl-dClosedLoop-0077` names
  `tools/workflows/REVIEW-PROTOCOL.template.md` as a record this build brings back in line with the
  code. RESOLVED (agent, 2026-10-23, delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the resume-file name in tools/workflows/REVIEW-PROTOCOL.template.md and its render memory/guides/REVIEW-PROTOCOL.md

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 4, the brief's S4, S5 and S9, the
  review system record's batches by address, and the verify stage read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.
- rev-3 · 2026-10-23 · §3 · the hygiene check's edge parity (check 12): `TOOL-dFairHearing-12`'s §3
  consumes `deriveAddressKey`'s spec-kind reading from this unit, and this spec declared no hands-off
  back. Fixed here, by a hands-off edge to `TOOL-dFairHearing-12`: S1 already produces the key, and
  §3's non-goals already name that unit's reader as written to agree with it.
- rev-4 · 2026-10-23 · §3 · the round-3 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-32,
  naming the eight minors it closes on this spec and what it supersedes.

## 10. Reuse audit

The seams extended are the verify stage's own: `chunk` and the marked `batches` line
(`tools/workflows/tier2-review.template.js:24-28`, :1352-1353), the batch print, label and reuse
lookup (:1362-1373), the keyed schema (:66-72), and the argument ladder `intensity` uses (:210-217).
The new functions sit beside `renderAuditBinding` (:318-328) in the prelude the suite already slices.
No second batching helper, no second id join. `python tools/codebase-map/reuse_lookup.py "sort review
findings by cited file and line before slicing skeptic batches"` ranked generic name stems (`before`,
`slice`, `check_line`, `build_ask_sort_key` in `tools/memory-tree/backlog.py`) and named no seam in the
review harness, so the seams were found by reading the source. `python tools/memory-recall/query.py`
returned the brief's row, the gap register row for `gap-review-06`, the review system record's
batches-by-address design and the debt round's `batch-sort-key` and `batch-contiguity` rows. Each
agrees with source except one count: the research record says 24 `verify:ids-a-b` references sit in
the suite (`…-research-review-adjudication.md:100`), and `grep -c verify:ids` over
`tools/workflows/tier2-review.test.sh` prints 25 at base, as the debt round's correction says.

Recall terms used: skeptic batch contiguous chunk address twins verify label fixed-verifiers resume file sort
