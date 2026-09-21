# TOOL-dGatedProse-4 — M4 bounds the spec-audit promotion chain by review precision

**Status:** SPECCED · rev-2 · 2026-09-20 · node d · Tier-2 · base fcbfba5f · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` M4 gains one sentence bounding the spec-audit PROMOTION chain by
review precision, so a run that keeps promoting over a class no paper audit can close stops at the
round where its own signal degraded instead of discovering the limit by exhausting it. The sentence
is paid for by deleting four spans M4 does not need: three restate a rule another carrier already
states, which M1 calls a defect in M4, and the fourth states a corpus fact M9's own table already
names as its source.

## 2. Scope (IN)

- **S1** — One sentence is appended to M4's `**A BLOCKED verdict has a disposition.**` paragraph in
  `tools/memory-tree/BUILD-METHOD.template.md`, immediately after `the fold is what the next round
  measures.` Its text is fixed in §4 and is 429 bytes. Observed by AC1.
- **S2** — Four spans are deleted from M4 in the same file, 450 bytes in total, each written in §4
  VERBATIM as the file wraps it, with the carrier that keeps stating it. Observed by AC3, and the
  carriers' liveness by AC4.
- **S3** — M4's pointer at `memory/guides/REVIEW-PROTOCOL.md` is widened by the clause `and its stop
  rule`, 18 bytes, so the obligation S2's fourth deletion removes stays reachable from M4. Observed
  by AC5.
- **S4** — `memory/guides/BUILD-METHOD.md` is re-rendered from the edited template, never hand-edited,
  because the render is the direction the kit declares. Observed by AC2.
- **S5** — Both files stay inside the declared byte cap and inside M1's stated line figure. Observed
  by AC6 for the bytes and AC7 for the lines.
- **S6** — The `M4` bullet of `memory/map/features/build-method.md` names the new bound, because the
  dossier describes M4's review loop and this unit changes it. It is PROSE only: no `[claims]` key
  moves, so no generated map artifact goes stale. Observed by AC8.

## 3. Non-goals (OUT)

- **No gate, no arm, no checker.** The rule is a documented check. §4 states why, with the evidence,
  and the sentence claims no enforcement the tree does not have.
- **No precision plumbing.** `tools/workflows/unattended-build.js` will not start reading the
  `precision` its callee returns, and the driver's `--review` row grammar gains no field. That fork
  is F1 in §8.
- **No change to `REVIEW_ROUNDS`, to `RUNAWAY_CEILING`, or to the floor's value.** Rounds inside one
  generation stay governed by `REVIEW_ROUNDS` exactly as `TOOL-aProbedUnit-9` ruled on 2026-09-14.
- **The rule the backlog row states is not built.** `TOOL-dLoggedFlight-34` says a promoted
  generation is audited ONCE; the owner replaced that on 2026-09-20 after the dry run. Re-wording the
  row is a build-level write at landing, not this unit's code.
- **No re-wrapping of M4's long paragraph.** That line reaches 1047 CHARACTERS after S1 — 1053 bytes,
  and the two figures differ because the line carries em dashes and arrows; measured on the scratch
  copies, not computed, because computing it from a byte count is how the cross-read reached 1051.
  The file hard-wraps at about 100 elsewhere, so wrapping it would add roughly ten lines and breach
  M1's stated 350. The long line stays and a future editor is told why here.
- **The wrong arithmetic in `tools/template-size-limits.txt:69-70` is flagged, not fixed.** F3 in §8.
- **No retroactive audit of the corpus's existing chains.** The rule binds the next run.

### Edges

- **consumes-from** `TOOL-dGatedProse-1` — the kit version moves ONCE in this build and that unit
  owns the move. It bumps `KIT_MEMORY_TREE_VERSION` 2.79 → 2.80 and re-stamps the whole
  `gov:kit memory-tree@` marker population in the same commit, DERIVED by the marker grep rather than
  listed. That population is nine tracked files today — verified, `git grep -lF "gov:kit
  memory-tree@2.79"` returns the engine, four `tools/memory-tree/*.template.md` and the four docs
  rendered from them — and it includes line 1 of BOTH files this unit edits. So by the time this unit
  runs, its two paths are ALREADY stamped and it owes nothing: no bump, no re-stamp. Two things are
  relied on and each is checkable. First, that unit 1 left `2.80` and not a wider string: the re-stamp
  is byte-neutral only while the version stays four characters, and this unit's whole budget in §4 is
  measured at base `fcbfba5f` where the marker still reads `2.79`. A five-character version would add
  one byte to each file and this unit's figures would move with it. Second, that unit 1 left
  `kit version markers` green, since that leg is unguarded and this unit's bar at order 4 is the last
  one in the range.
- **consumes-from** `TOOL-dGatedProse-3` — that unit raises the hygiene GUIDE class caps, which do
  grade `memory/guides/BUILD-METHOD.md`: check 6's guide selector is the `memory/guides/` prefix
  (`tools/memory-tree/check-memory-hygiene.sh:719`) and the pair it reads sits at `:84`. Nothing in
  this unit depends on the raise. At 27569 bytes and 349 lines the file clears the retired 61440/750
  and the ratified 81920/1000 alike; the cap that actually binds it is the far tighter per-subject
  `27648` row in `tools/template-size-limits.txt:86`, read by a different checker. The edge exists so
  the crossing is on the record as a NON-dependency rather than as silence.
- **consumes-from** external — the precision figure this rule reads. It exists only as prose in a
  review record, written by the synthesis agent because `tools/workflows/tier2-review.js` interpolates
  it into that agent's prompt (`:506`). The run-state file carries the DISPOSITION this rule produces
  and never the PRECISION it reads: verified, `memory/builds/dMispairedQuote/RUN.md` answers zero for
  `precision` and for every one of the five figures §4 cites, while `:53` and `:63` carry
  `disposition promote` and `disposition fold` on their review rows.
- **hands-off** external — whether the bound ever becomes machine-enforced. §4 records why no
  predicate should be wired on this shape today; the measurement that would change that answer is
  named there.
- **hands-off** external — the backlog row `TOOL-dLoggedFlight-34`, whose text states the superseded
  rule and is re-worded at landing.

## 4. Design

### The sentence, verbatim

It is appended to the existing paragraph, on the same line, so no line is added:

```
 **The CHAIN of promotions is bounded by PRECISION.** Each takes a FRESH subject, so `REVIEW_ROUNDS` re-arms per subject and bounds no chain of them. A PROMOTING round whose precision, which its own record states, falls below the review protocol's floor ENDS the chain: its promotions are built from their specs as written and closed under a recorded `specs-audited` override — owed because the run CLOSES units no audit names.
```

Four words are load-bearing and each closes a defect the dry run's skeptic reproduced.

**PROMOTING.** The round whose precision decides the chain is the one that disposes, not any round.
Unit 1's spec audit in `dMispairedQuote` ran two rounds at precision 0.28 then 0.57, and only the
second promoted. The two halves come from two carriers, which is the point of the table below: the
figures are at
`memory/builds/dMispairedQuote/reviews/2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round1.md:32`
and `...-round2.md:28`, and the dispositions are at `memory/builds/dMispairedQuote/RUN.md:49`, which
carries no disposition, and `:53`, which carries `disposition promote`. A rule reading "a round" would
have ended that chain on the first, which promoted nothing.

**CHAIN, against ROUND.** Rounds inside one generation keep their `REVIEW_ROUNDS` bound, so a
generation that converges over several rounds stays correct. `TOOL-dMispairedQuote-3` is that case:
the promoted generation was audited three times at 0.48, 0.53 and 0.63
(`...-3-spec-audit-round1.md:55`, `...-round2.md:77`, `...-round3.md:72`) and exited
`disposition fold` at `memory/builds/dMispairedQuote/RUN.md:63`, the best outcome in the corpus. The backlog row's "audited once" outlaws it; this sentence does not.

**bounds no chain of them**, against the draft the skeptic refuted, which said nothing COUNTS
generations. Something does, and the code is explicit about it.
`tools/workflows/unattended-build.js:250` keeps `roundNo`; `:252` keys the subject
`<slug>-spec-set-r<N>` from `subjectRound`, which `:251` defaults to `roundNo` and `:254` refuses
above it — the `-r7` in `memory/builds/dLoggedFlight/RUN.md:165` IS that key. The chain is counted
too: on a promotion `:1255-1258` prescribes re-invoking at `round: roundNo + 1` **with no
`subjectRound`**, "so they take a fresh subject". What no code does is BOUND it, and `:685-690` is
why. The round handed to the reviewer is `roundNo - subjectRound + 1`, and that expression's own
comment reads "1 for a fresh generation, N for its Nth fold" — so a fresh subject resets it to 1. The
bound at `tools/unattended/unattended.sh:4322` then reads `RUNAWAY_CEILING` only when the subject is
the build slug and `REVIEW_ROUNDS` otherwise, so both counters re-arm per generation and neither ever
sees the chain.

**the review protocol's floor**, named rather than spelled. The value lives in
`memory/guides/REVIEW-PROTOCOL.md:198`, an M11 carrier, and writing `0.5` into M4 would be the defect
M1 names. M4 cites that carrier by path five lines above this sentence, and the preceding
`(protocol §8)` refers to `memory/guides/UNATTENDED-PROTOCOL.md:468`, so the adjective is what keeps
the two apart.

### Where precision is computed, recorded, and NOT read

| fact | site | what it means for this rule |
|---|---|---|
| computed | `tools/workflows/tier2-review.js:452` | `confirmed / (confirmed + refuted)`, unjudged findings excluded |
| logged | `tools/workflows/tier2-review.js:465` | the runner's own `precision < 0.5` note, the same floor |
| recorded | `tools/workflows/tier2-review.js:506` | interpolated into the synthesis prompt, so the RECORD states it |
| returned | `tools/workflows/tier2-review.js:684` | `precision` is a field on the success object, and `:478` on the early return |
| not read | `tools/workflows/unattended-build.js:698` | the string appears ONCE in that file, in a comment listing the callee's returns, and nowhere in code |
| not carried | `tools/unattended/unattended.sh` | the string does not appear at all; the `--review` row grammar is `verdict · blockers N · <exit> · disposition <v>`, emitted at `:4373` |
| the CONSEQUENCE is carried | a build's `RUN.md` | `disposition promote` / `disposition fold`, at `memory/builds/dMispairedQuote/RUN.md:53` and `:63` |

Counts DERIVED 2026-09-21: `precision` occurs 11 times over 9 lines in `tier2-review.js`, once in
`unattended-build.js`, zero times in `unattended.sh`. So the number the rule turns on is durable in
the review record and invisible to every downstream consumer, while the DISPOSITION it produces is on
the run record and machine-graded. That asymmetry is the whole basis of the next subsection, and it is
also why every figure above cites a review record rather than a `RUN.md` — rev-1 cited the `RUN.md`,
which cannot carry them and does not. One caveat on the two disposition rows, because they are the
oldest evidence here: `memory/builds/dMispairedQuote/RUN.md:16-17` records that
`--review --disposition` did not exist when those rounds ran and that both values were RECONSTRUCTED
by hand under `TOOL-dFoldedVerdict-3`. Today's driver writes them; those two rows were written about
it.

### Why this is a documented check and not a gate

One half of the consequence IS machine-forced, and the sentence says only that much:
`specs-audited` is a machine DoD item (`memory/guides/UNATTENDED-PROTOCOL.md:351`) that refuses a
CLOSED unit no tracked `**Serves:** spec-audit` record names, so a run that stops the chain and closes
the promotions must record `--override specs-audited`. That is why the sentence ends with the ground
for the override rather than asserting it is automatic: the item grades the CLOSE, so a run that
leaves the promotions non-terminal owes a different override and no `specs-audited` one at all.

The STOP itself is enforced by nothing, and two measurements say it should stay that way.

- **"How many records state a precision" has no answer until the predicate is named, and the three
  honest predicates disagree by a factor of nine.** Derived 2026-09-21 over
  `git ls-files 'memory/builds/*/reviews/*.md'` — 387 tracked records, 103 of whose filenames say
  `spec-audit` — each figure being the record count matching one `grep -lEi` pattern:

  | predicate | pattern | states | silent | spec-audit states / silent |
  |---|---|---|---|---|
  | A — the bare word | `precision` | 286 | 101 | 91 / 12 |
  | B — the word plus a 2dp figure on one line | `precision.*[0-9]\.[0-9]{2}` | 268 | 119 | 88 / 15 |
  | C — the shape line the synthesis prompt prescribes | `^- raw .*precision [0-9]\.[0-9]{2}` | 33 | 354 | 24 / 79 |

  A is too loose to be a figure at all — it matches the word in prose. C is the only one keyed on the
  grammar `tools/workflows/tier2-review.js:506` actually asks the synthesis agent for, and it finds
  33 records of 387. A checker would pass the other 354 in silence, which is the green-by-absence
  class the charter §7 names. Liveness: C's 33 include all five `dMispairedQuote` spec-audit records,
  the corpus instance this whole rule is built on, so a zero elsewhere is a finding and not a broken
  probe. Rev-1 stated 266/121 and 86/17 and named no predicate; neither pair reproduces under any of
  the three, and that is the defect — a figure whose predicate is unwritten cannot be re-derived, and
  the SPREAD is the actual argument.
- **A predicate keyed on the review subject grades only the harness era.** The dry run's census found
  at least four spellings of the spec-audit subject key across the tracked run records —
  `<slug>-spec-set-r<N>`, a bare `spec-set`, `<slug>-specs`, and one review-record FILENAME used as a
  subject — and its skeptic found a whole era recorded under unit-id subjects, including
  `dMispairedQuote`'s two-generation chain, which the census's own rule flags zero times. Both stages
  concluded independently that no predicate should be wired on this shape.

What would change the answer is a precision FIELD on the `--review` row, which is F1 in §8 and is
outside this unit. Until then the rule is prose, and the build README's own rules slot already binds
this build to the dry-run-before-wiring discipline.

### What it pays with

`memory/guides/BUILD-METHOD.md` measured 27572 bytes of a declared 27648 at base `fcbfba5f`, and
exactly 350 of the 350 lines M1 states. So 76 bytes and no lines were available, and the sentence
plus the pointer repair cost 447. Four spans go. Three of them — D1, D2 and D4 — are what M1's own
rule already makes a defect in M4: "nothing here is stated anywhere else in this repo", and "a rule
appearing both here and in an M11 carrier is a defect HERE. Drift resolves by deletion, not
adjudication." D3 is not that class and is not claimed as it: it is a corpus OBSERVATION rather than
a rule, its instruction survives in place, and M9's own table already names the line it describes as
its source. Its row says so.

| # | deleted from M4 | bytes | where it still lives |
|---|---|---|---|
| D1 | the runaway-ceiling sentence, from `A runaway ceiling backstops` to `BUILD-LEVEL RULES slot.`, PLUS the single space separating it from the sentence before — the span alone is 196, and since the sentence ends line 140 that space would be left as trailing whitespace | 197 | `.claude/skills/unattended/SKILL.md:702-704` and its kit template state it; `tools/unattended/unattended.sh:4373` EMITS it at the exit |
| D2 | `, never merely "changed", which 2, 1, 2 satisfies forever` | 57 | `.claude/skills/unattended/SKILL.md:707-708` and `tools/unattended/unattended.sh:4174-4175` |
| D3 | ` Most existing review records carry no` then the LINE WRAP then `verdict line; write it anyway, because M9 derives from these records.` — the span crosses `memory/guides/BUILD-METHOD.md:134-135` and the newline is one of its 108 bytes. Rev-1 wrote it unwrapped, which answers zero at base and made AC3 unfalsifiable for this row | 108 | corpus history, not a rule; the instruction to open with `## Verdict: CLEAN` stays in place and M9's own table already names that line as its source |
| D4 | `, then **STOP**: once a synthesis pass calls the design clean, stop reviewing that spec.` | 88 | `memory/guides/REVIEW-PROTOCOL.md:209-211`, an M11 carrier, which is the exact case M1 names. Rev-1 cited `:203-206`; that range is the LENSES / `MAX_LENSES` bullet |

D1 needs one more note, because it restates an owner ruling and deleting it must not lose one.
`TOOL-aBoundedVerdict-1` fork F4, RESOLVED by the owner on 2026-08-19, mandated that a ceiling firing
be said loudly in TWO carriers: the run's own output and the build README. Both survive this deletion
— the driver emits the first and the Skill states the second. M4 was a third copy. The
`BUILD-LEVEL RULES slot` wording survives inside M4 itself, in M2's classification sentence.

D4 needs the pointer repair, for the same reason. M4's existing pointer at
`memory/guides/BUILD-METHOD.md:127` reads `under its fan-out and concurrency caps, read there and not
repeated here.` and names two caps but not the stop rule, so deleting D4 without touching it would
leave the obligation unreachable from M4. The clause `and its
stop rule` is added there. The machine-enforced half of the same rule already sits in the next
paragraph, `CONVERGED is terminal for its subject`, which `--review` refuses a round against.

### Measured cost of the whole edit

Applied to scratch copies at base `fcbfba5f` on node d, 2026-09-20:

| file | before | after |
|---|---|---|
| `memory/guides/BUILD-METHOD.md` | 27572 B · 350 lines | 27569 B · 349 lines |
| `tools/memory-tree/BUILD-METHOD.template.md` | 27597 B · 350 lines | 27594 B · 349 lines |

447 in, 450 out: net −3 bytes and −1 line on both, so headroom against the declared 27648 goes
76 → 79. RE-MEASURED 2026-09-21 by applying all six edits to scratch copies of both files and
weighing the result, after the cross-read found rev-1's pair one byte adrift. The byte is D1's
separating space, priced in the row above; rev-1 carried 197 in that table and 27570 in this one, and
only one of the two could be right. Deleting D3 instead of re-pricing D1 was the other way to close
the gap and does NOT work: the payment falls to 342, the file lands at 27677, and the cap reds. The
rule
lands and the budget ends healthier than it started, which matters because `TOOL-dLoggedFlight-35`
records an unresolved owner dispute over M1's budget passage and this unit must not lean on it.

### The carrier — a render, not byte identity

`tools/memory-tree/BUILD-METHOD.template.md` is the authored source and
`memory/guides/BUILD-METHOD.md` is this repo's render of it. The comparison substitutes rather than
strips: `render_doc`, canonical at `tools/lib/render-doc.sh` and inlined byte-identically into the
parity test, drops CR and substitutes THREE tokens — `{{KIT_DIR}}`, `{{TOOL_ROOT}}` and
`{{READINESS_ROWS}}`. Read from the function body, not from that file's header comment, which still
says "two placeholders" and predates `TOOL-aJoinedCanon-9` adding the third. The template holds 4 of
the first, 7 of the second and 0 of the third, so at this install the render is
4×(+6) + 7×(−7) = −25 bytes, which is exactly the measured 27597 − 27572. Verified on the current
pair and again on the edited pair: `render_doc` over the template is byte-identical to the live file
both times.

```bash
# the direction the kit declares: edit the template, then render template -> live
bash tools/memory-tree/kit-dogfood-parity.test.sh --render
# the direct observation AC2 names, with no suite in it
KIT_REL=tools/memory-tree TOOL_ROOT=tools/ bash -c '. tools/lib/render-doc.sh; render_doc tools/memory-tree/BUILD-METHOD.template.md' | diff - memory/guides/BUILD-METHOD.md
```

Two gate legs cover the pair, both `subject: repo`: `build-method size`, which is UNGUARDED and runs
on every bar, and `kit/dogfood doc parity`, whose guard names `memory/guides/BUILD-METHOD.md`, so this
edit arms it. `build-method size` reads the `27648` row at `tools/template-size-limits.txt:86` and its
check 6 also byte-pairs that row against the file's own `**Budget:` prose line, which this edit leaves
untouched.

### Inventory, and the codebase-map obligation stated

This unit MINTS no identifier: no file, no leg, no conf key, no function, no flag. So it claims no
NEW inventory key, and the reason is a population rather than an absence of effort. Both files it
edits are already claimed, by name, in the `[paths] globs` of `memory/map/features/build-method.md`
— `tools/memory-tree/BUILD-METHOD.template.md` and `memory/guides/BUILD-METHOD.md` are the only two
entries in that list — and the dossier's `[claims]` block already holds every key this edit touches,
`build-method size` among them. Nothing new enters an enumerated set, so the coverage ratchet has
nothing to ask for.

What it DOES owe is the prose refresh in S6, and the leg that grades it is
`codebase-map coverage + freshness` — subject `repo`, NO guard, so it runs on every bar, `argv`
`python3 tools/codebase-map/test_codebase_map.py`. It is on this unit's keep-green list in §7. It
does NOT owe `python tools/codebase-map/gen_map.py --write`: that regen exists for CLAIM edits, and
`memory/map/generated/MAP.md` is claimant-annotated key rows only — verified, it answers zero for
the M4 bullet's own prose — so a prose-only bullet edit stales no generated artifact. A unit whose
edit moved a `[claims]` key would owe the regen in the same commit; this one does not, and saying so
is the point, because silence here reads as an oversight rather than as an answer.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | the authored edit: one sentence in, four out, one pointer widened |
| `memory/guides/BUILD-METHOD.md` | re-rendered from the template, never hand-edited |
| `memory/map/features/build-method.md` | one dossier bullet refreshed |

### Alternatives rejected

- **The backlog row's rule as written** — "a promoted generation is audited ONCE". Refuted by the dry
  run's skeptic against `TOOL-dMispairedQuote-3`, and it hard-codes a configurable named one sentence
  earlier in the same paragraph. The owner replaced it on 2026-09-20.
- **A round-count bound on the chain.** `TOOL-aBoundedVerdict-1` §3 records "No round CAP as the
  loop's mechanism. Withdrawn at rev-6 on the owner's instruction", and
  `memory/builds/aBoundedVerdict/reviews/2026-08-19-review-TOOL-aBoundedVerdict-1-2.md:401` raises the
  same class as finding 57 and refutes it — verbatim, "the per-subject runaway ceiling cannot bound
  the promotion chain". Rev-1 cited `:394`; the record's own line is `:401`. Bounding on precision rather than on a count is what keeps
  this from reinstating the withdrawn cap.
- **Paying with M1's budget-raise history**, the fattest trim in the file. Refused: that is the
  passage `TOOL-dLoggedFlight-35` records two opposed owner rulings over, and M3's second veto puts a
  governance-carrier change of that kind outside a run's authority.
- **Paying with M4's declared-subject rule** (`tier2-review.js` audits a spec only when the call names
  the spec kind). Refused: `memory/map/features/build-method.md:94` records that this rule was already
  lost once in a deletion no record explains and restored by `TOOL-dTieredTribunal-12`.
- **Trimming the sentence instead of the file.** A version dropping the override's ground fits in 373
  bytes, so 391 with the pointer repair, and could have spared D3's 108 — landing the file at 27621,
  inside the 27648 cap. Refused: it reads as though the override were automatic, and `specs-audited`
  grades the CLOSE rather than the stop. Refused a second time on the fold, once D3 turned out to be
  the row that made AC3 unfalsifiable: sparing it would have left the bad criterion standing and
  called that a saving.

## 5. Production-readiness checklist

- security — N/A. The unit adds no write path, no input, no surface. Editing a shipped kit template
  changes what an adopter reads, not what any code executes.
- perf / scale — N/A on the bar: no leg is added and no argv changes. Of the legs §7 names, the four
  this edit can actually arm declare 300 s each in `tools/gate-legs.json`; `kit version markers`
  declares 660 s, `memory hygiene` 12720 s and `unattended kit gate` 16040 s, and this unit lengthens
  none of them.
- error / empty / loading states — N/A for prose. The nearest analogue is the empty-population class,
  and it is answered in §4: a predicate over this shape would be silent on 121 of 387 records, which
  is why none is wired.
- observability — the rule's own input is observable only in the review record, and §4's table says
  where. Nothing reports a chain's generation count except the `-r<N>` subject key.
- risks — three, stated rather than smoothed. First, the floor may be unreachable on spec targets, though the
  measured claim is narrower than rev-1 stated:
  `memory/builds/aLexedStripper/reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round2.md:24`
  records 0.29 against round 1's 0.28, and `:28` concludes that the floor is not reachable on a
  spec-audit target **by priming alone** — a result about ONE lever, on a fan primed exactly as round
  1 prescribed, and not a general claim about the target class. Rev-1 dropped that qualifier. Taken
  with it the risk is still live, so the rule may end most chains at the first generation. That collapses to the owner's existing default of one
  round and one disposal, so it is not a defect; the value is that a HIGH-precision chain may
  continue, and `dMispairedQuote` is the corpus instance. Second, the rule is unenforced, so a run can
  ignore it; the compensating observation is that `specs-audited` forces a RECORDED override at the
  close, which is what makes the stop auditable after the fact. Third, M4's long line grows to 1047
  characters and 1053 bytes, and nothing wraps it.
- testing — no new arm. AC1 to AC8 are direct observations over two files, a render and one checker.
- migration — none. No landed record is rewritten; the corpus's existing chains are out of scope.
- user docs — none. `help/` is not part of this repo's product surface, and the governance carrier
  this unit edits IS the documentation.

## 6. Acceptance criteria

- **AC1** — When `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` are
  each searched for the literal `The CHAIN of promotions is bounded by PRECISION`, each answers
  exactly one, and both counts are inside the M4 section.
  Red when: the sentence lands in the rendered copy only, so the template answers zero and every
  adopter renders a method that carries no such rule.
  figure: DERIVED — both counts are read at observation time.
- **AC2** — When `tools/lib/render-doc.sh` is sourced with the kit directory and `tools/` bound and
  `render_doc` is run over `tools/memory-tree/BUILD-METHOD.template.md`, its output is byte-identical
  to `memory/guides/BUILD-METHOD.md`.
  Red when: the template was edited and the live copy was not re-rendered, or the live copy was
  hand-edited, either of which leaves the declared pair in drift.
  fixture: none needed — both files are tracked today and the renderer is a tracked function library.
- **AC3** — When each of §4's four deletion spans, taken VERBATIM including the newline D3 crosses,
  is searched for in `git show fcbfba5f:<path>` for both `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/BUILD-METHOD.template.md`, it answers exactly ONE in each; and when the same
  eight searches run over the working tree, each answers zero. Both halves are required, and the base
  half is what lets the criterion fail.
  Red when: a deletion is reverted — the working-tree half answers one, the file is back over its
  byte cap, and an M1 defect is restored. Red ALSO when a span answers zero at base, which means the
  span was mis-transcribed rather than deleted. That second arm is the defect this criterion carried
  at rev-1: D3 was written unwrapped, the file wraps it at `memory/guides/BUILD-METHOD.md:134-135`, so
  a literal search answered zero in both files BEFORE any edit and the criterion was satisfied whether
  the deletion happened or not.
  figure: DERIVED — sixteen searches, eight ones then eight zeros. Verified 2026-09-21 that all four
  spans as now written answer exactly one in both files at base.
- **AC4** — When each carrier in §4's deletion table is searched for the statement it is credited
  with, each answers at least one: `.claude/skills/unattended/SKILL.md` for the ceiling and for the
  strictly-smaller illustration, `tools/unattended/unattended.sh` for both again, and
  `memory/guides/REVIEW-PROTOCOL.md` for the stop rule.
  Red when: a credited carrier does not in fact state it, which turns the matching deletion from a
  displacement into a loss — the defect this criterion exists to separate from AC3's. It searches the
  FILE and not a line deliberately: the anchors in §4's table are a reader's aid, and
  `tools/check-spec-tokens.py:10` resolves a cite's existence and range without reading the cited
  line, so a drifted anchor is caught by no gate anywhere. Two of them had drifted at rev-1 and are
  corrected in the table.
- **AC5** — When M4's `Run it as a Workflow script` paragraph is read, its pointer at
  `memory/guides/REVIEW-PROTOCOL.md` carries the clause `and its stop rule`.
  Red when: the stop rule is deleted per AC3 and the pointer is left naming only the two caps, so the
  obligation is reachable from nowhere in M4.
- **AC6** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs, it exits 0
  and the size it reports is at or under the `27648` declared for that subject in
  `tools/template-size-limits.txt`.
  Red when: the sentence lands without its payment; the file then measures 28019 bytes and the checker
  fails its own check 2.
  figure: PINNED for the prediction of 27569 bytes, measured on scratch copies on node d 2026-09-21;
  DERIVED for the verdict, which the checker measures itself.
- **AC7** — When the lines of `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/BUILD-METHOD.template.md` are counted, each is at or under the 350 that M1's
  own `**Budget:` line states, and the edit leaves both at 349.
  Red when: the new sentence is wrapped onto its own lines and pushes either file past 350. No gate
  catches this: `tools/check-template-size.sh:129` parses only the bytes figure out of that line, and
  `tools/template-size-limits.txt` records the fact and prices it at `TOOL-aHoistedPass-28`. This
  criterion is the documented check that covers it.
  figure: DERIVED — both counts are read at observation time.
- **AC8** — When the `M4` bullet of `memory/map/features/build-method.md` is read, it names the
  precision bound and says the bound is enforced by no checker; and when that file's `[claims]` block
  is diffed against base `fcbfba5f`, no key has moved.
  Red when: the dossier still describes M4's review loop without the bound, which is the stale-claim
  class the map exists to prevent and the class this build's first unit is about. Red on the second
  half when a claim key did move, because this unit then owes the generated-artifact regen that §4
  declares it does not — which is what keeps that refusal falsifiable rather than convenient.

## 7. Gates

This unit adds and moves no gate arm, so it carries no `New arm:` line — and therefore it raises no
suite's assertion floor. Both floors this build touches are left exactly as the units owning them
leave them: `FLOOR_ASSERTIONS=374` at `tools/memory-tree/check-memory-hygiene.test.sh:2460`, which
`TOOL-dGatedProse-1` raises by the count of assertions it adds, and `FLOOR_ASSERTIONS=42` at
`tools/check-spec-tokens.test.sh:16`, which `TOOL-dGatedProse-2` raises the same way. This unit edits
neither suite and adds no arm to either, so it has nothing to raise and says so rather than leaving
the reader to infer it.

The legs it must keep green:

`build-method size` · `kit/dogfood doc parity` · `memory hygiene` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `unattended kit gate` · `spec tokens (a spec's own names resolve)`

`kit/dogfood doc parity` is the leg this edit arms, and its guard does name this carrier: verified in
`tools/gate-legs.json`, the guard is the six paths `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`,
`memory/guides/BUILD-METHOD.md`, `memory/guides/ANNOTATION-STYLE.md`, `tools/lib/` and
`tools/memory-tree/`. `TOOL-dGatedProse-3` §7 calls that leg unguarded; it is not, and this is the
reading two cross-reads independently resolved in this unit's favour.

`verdict epoch (kit version dates the engine)` and `codebase-map coverage + freshness` were both
missing from rev-1's list. Neither carries a guard, so both run on every bar, and the first matters to
more than this unit: it judges the whole `base..HEAD` range topologically, so a mis-ordered
kit-version bump anywhere in units 1 to 3 surfaces at THIS unit's bar, the last one in the range.
This unit's own edit cannot arm it, for the population reason in F2.

`unattended kit gate` is on that list for a reason worth stating: its check 16 body term requires M4
to spell `specs-reviewed` in backticks outside every HTML comment, because the directive registry at
`tools/unattended/unattended.sh:563` maps that handle to M4. The edit leaves that sentence untouched
and the token verified present once on the scratch copies.

## 8. Open questions

- **F1 — FACT-QUESTION · should the precision that bounds the chain become a field on the `--review`
  row, so the bound is machine-readable?** Probe: search `tools/workflows/unattended-build.js` and
  `tools/unattended/unattended.sh` for `precision`. Observation: one occurrence in the first, inside a
  comment listing the callee's return keys at `tools/workflows/unattended-build.js:698`, and zero in
  the second. Liveness: the same search over `tools/workflows/tier2-review.js` returns 11 occurrences
  over 9 lines, so the probe can produce a positive and a zero is a finding rather than a broken
  probe. Rev-1 said "ten", which is neither of those two figures. RESOLVED (agent, 2026-09-20): NOT in this unit. Adding the field
  means a new argument in the driver's `--review` grammar and a new key in the run-state record, which
  is a change to a governance carrier and to a kit's public surface — M3's second veto. The surviving
  option, stating the rule in prose and leaving the consequence to `specs-audited`, trips no veto, so
  it is taken and the field is declared a follow-up in §3.
- **F2 — FACT-QUESTION · does this unit owe a `KIT_MEMORY_TREE_VERSION` bump of its own?** Two
  checkers could say yes, neither does, and in each case the answer is a population. Probe 1:
  `tools/check-kit-versions.sh:135` derives its population from
  `git ls-files 'tools/memory-tree/*.template.md'` and asserts every marker EQUALS the constant; it
  never asserts the constant MOVED, so it cannot ask this unit for a bump. Probe 2:
  `tools/memory-tree/check-verdict-epoch.sh` DOES assert movement, topologically at `:16-19` — the
  newest commit moving a behaviour-bearing line must be an ancestor of or equal to the newest commit
  changing the constant — but its SCAN set at `:68-69` is `tools/memory-tree/check-memory-hygiene.sh`
  plus six named Python delegates, and NEITHER `BUILD-METHOD.template.md` nor its render is in it. So
  an edit to this carrier is not a verdict change that leg can see, and no bump is owed for it. That
  boundary is the one thing rev-1 left unwritten, and it is why this unit's template edit landing
  AFTER a bump is not the stale shape it would be for the engine. Liveness: `TOOL-dRetiredFork-7`'s
  AC5 required `kit version markers` to red with a marker reverted, and the verdict-epoch leg's own
  header records a measured red once `merge-rows.py` entered its scan set, so both probes can produce
  a positive. RESOLVED (agent, 2026-09-21): no bump of its own. The kit version moves ONCE in this
  build and `TOOL-dGatedProse-1` owns the move, re-stamping the derived marker population at order 1,
  which already includes both of this unit's files. This unit edits an already-stamped file and owes
  nothing. Declared as the `consumes-from TOOL-dGatedProse-1` edge in §3. Rev-1 credited the bump to
  `TOOL-dGatedProse-3`.
- **F3 — FACT-QUESTION · is the placeholder arithmetic in `tools/template-size-limits.txt:69-70`
  wrong?** It says four `{{KIT_DIR}}` grow by 6 each and five `{{TOOL_ROOT}}` shrink by 7 each, a net
  −11. Probe: count both placeholders in `tools/memory-tree/BUILD-METHOD.template.md` and compare the
  computed delta with the measured difference between the template and its render. Observation: 4 and
  7, so 4×(+6) + 7×(−7) = −25, and 27597 − 27572 = 25. Liveness: a wrong count yields a delta that
  does not equal the measured 25, which is how this was found. RESOLVED (agent, 2026-09-20): flagged
  and declared OUT in §3. It is a second mechanism, in the file that declares this unit's budget, and
  correcting its prose in the same commit as a byte-cap-relevant edit would conflate two claims about
  the same number. Follow-up owed as a backlog row at landing.
- **F4 — should the advisory high-water in `tools/template-size-highwater.txt` be re-recorded?** It
  holds 26941 for this subject and therefore already warns today at 27572; after this edit it warns at
  27569. PARKED, and it is the owner's rather than mine: the high-water is the instrument that PRICES
  growth against a recorded past, a `--bump` re-bases that price, and re-basing it in the same commit
  that spends the budget is the measurer moving its own baseline. It blocks nothing — the ratchet is
  advisory and never changes the checker's exit code — so the unit lands either way. Options seen:
  bump to the post-edit figure, leave it, or retire the row; refused to pick because none of the three
  is decided by an observation.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft. Written against the owner's ruling of 2026-09-20, which
  replaced `TOOL-dLoggedFlight-34`'s "audited once" rule with a precision bound after the dry run and
  its skeptic refuted the row as written.
- rev-2 · 2026-09-21 · cross-read fold, over all four cross-reads and the main loop's rulings R1–R4.
  FOLDED, in the order of how much they moved. **The payment arithmetic, which missed by one byte.**
  Re-measured by applying all six edits to scratch copies and weighing the result: D1 is re-priced at
  197 as the span PLUS the space separating it from the sentence before, whose removal is forced
  because the span ends line 140 and leaving the space behind leaves trailing whitespace. The span
  alone is 196, which is what the cross-read measured. §4's pair is corrected 27570/27595 →
  27569/27594 and the headroom claim 76 → 78 becomes 76 → 79. Dropping D3 was the other way to close
  the gap and is now recorded as failing: the payment falls to 342 and the file lands at 27677, over
  the cap. **AC3, which could not fail for D3.** The span is written in the table as the file wraps
  it, and AC3 becomes a two-sided observation — exactly one at base `fcbfba5f`, then zero in the tree
  — so a mis-transcribed span reds instead of passing. Verified that all four spans as now written
  answer exactly one in both files at base. **The precision-figure citation**, which named
  `memory/builds/dMispairedQuote/RUN.md` for five figures that file does not carry: re-sourced to the
  five review records line by line, and §4's site table gains the row that reconciles it with the
  documented-check argument — the run record carries the DISPOSITION at `RUN.md:53` and `:63` and
  never the precision, and that asymmetry is what the argument actually rests on. **R1.** The
  `consumes-from` edge moves from `TOOL-dGatedProse-3` to `TOOL-dGatedProse-1`, names the nine-file
  derived marker population that already covers both of this unit's paths, states that this unit does
  not bump, and names the two things it relies on unit 1 having left: a four-character `2.80`, on
  which every byte figure here depends, and a green unguarded `kit version markers`. F2 is rewritten
  on that ruling and now writes down the population boundary neither spec had — the verdict-epoch
  leg's scan set at `check-verdict-epoch.sh:68-69` excludes both BUILD-METHOD files, which is WHY a
  template edit after a bump is not the stale shape it would be for the engine. A second
  `consumes-from` to unit 3 survives as a NON-dependency: that unit raises the hygiene guide caps,
  which do grade this file, and nothing here turns on the raise. **R2.** §7 states that this unit adds
  no arm and therefore raises no assertion floor, naming both floors and the units that own them.
  **R3.** §4's inventory section now says why no new inventory key is claimed — the dossier's
  `[paths] globs` already name both files — and adds `codebase-map coverage + freshness` to §7.
  **R4** needed nothing: S1 already edits the authored template and S4 re-renders. Also folded, all
  of them citations or figures that did not reproduce: the census pair 266/121 and 86/17, replaced by
  a three-predicate table whose spread from 33 to 286 of 387 IS the argument against wiring a
  predicate; `render_doc`'s token set, three and not two, read from the function body rather than the
  header comment that still says two; the `-r<N>` mechanism re-sourced to
  `unattended-build.js:250-254`, `:685-690` and `:1255-1258` instead of paraphrased, which is what
  makes "re-arms per subject" a quotation rather than a claim; F1's liveness count ten → 11
  occurrences over 9 lines; D4's carrier anchor `REVIEW-PROTOCOL.md:203-206` → `:209-211`; the
  aBoundedVerdict finding-57 anchor `:394` → `:401`; the aLexedStripper anchor `:22` → `:24` and
  `:28` with its dropped "by priming alone" qualifier restored, which narrows that risk from a claim
  about a target class to a claim about one lever; §5's perf line, which priced two legs when §7 now
  names eight; the long line stated as 1047 characters AND 1053 bytes, because conflating the two is
  how the cross-read reached 1051; and the sentence asking `TOOL-dGatedProse-3` for a mirror
  `hands-off` line it already carries, DELETED rather than annotated.
  REFUSED, one half of one finding. This unit does not run `python tools/codebase-map/gen_map.py
  --write`. `memory/map/generated/MAP.md` carries claimant-annotated key rows and not dossier prose —
  verified, it answers zero for the M4 bullet's own wording — and this edit moves no `[claims]` key,
  so the regen the sibling finding asks for would rewrite nothing. The leg belongs in §7 and the
  regen does not; AC8 now observes the claim block against base so that refusal can itself go red.
  Nothing else was refused.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "bound a spec-audit promotion chain by review precision"`
found no existing seam for this mechanism, and that is the answer rather than a probe failure. Over
1371 symbols, 255 inventory keys, 22 affordance seams and 24 dossiers it ranked only name-stem
matches — `build_self_chain` in `tools/process-monitor/scope.py`, `boundedParallel` in the workflow
scripts, `derive_review_exit` in `tools/runlog/model.py` — none of which is a place a rule about the
promotion chain could live, and its own header says a high rank means a name recurs rather than that
the seam is the right one. The seam this unit extends is therefore a DOCUMENT and not code: M4's
existing `**A BLOCKED verdict has a disposition.**` paragraph in
`tools/memory-tree/BUILD-METHOD.template.md`, which already states the severity disposal the new
sentence hangs off, with `memory/guides/BUILD-METHOD.md` as its render. Extending that paragraph is
what keeps this unit from minting a heading, a cutoff key or a checker. One recorded disagreement
between a hit and today's tree, per M5: the dossier bullet at `memory/map/features/build-method.md:94`
closes by saying nothing yet asserts that a spec audit HAPPENED, while `specs-audited`
(`memory/guides/UNATTENDED-PROTOCOL.md:351`) does assert it at `--close` as a lower bound. The
disagreement is recorded here rather than resolved, and AC8 refreshes only the sentence this unit
makes incomplete.

Recall terms used, verbatim: `python tools/memory-recall/query.py "what bounds a spec-audit promotion
chain and where is review precision recorded" --terms "precision confirmed refuted spec-audit
promotion chain REVIEW_ROUNDS runaway ceiling specs-audited override severity disposition
BUILD-METHOD M4 floor"`. It returned 40 hits; three bind this unit. `TOOL-aProbedUnit-9` is the owner
ruling of 2026-09-14 that fixes one spec-audit round as the default, which is why the sentence leaves
rounds to `REVIEW_ROUNDS`. The aBoundedVerdict round-2 record is the prior art for the chain bound,
raised as finding 57 and refuted in 2026-08-19. The aLexedStripper round-2 record carries the measured
claim that the floor is not reachable on a spec-audit target, which §5 records as this unit's first
risk.
