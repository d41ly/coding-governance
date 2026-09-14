# TOOL-dDerivedDocket-31 — fork items and delegated-pass carriers

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 |

<!-- /gen:spec-records -->

## 1. Goal

Two method carriers stopped recorded runs, and the owner ruled on both (D12-i10). A section 8 has no
regular shape, so both of its readers grade the section as a whole, and an unresolved fork below a
resolved one passes; a quoted mark resolves a fork too. And M6 requires parallel passes where
disjointness is proven, while the recorded practice is to author inline, so a run that sequences
disjoint units breaks a binding rule. Give forks a regular shape and grade each one, forward-only,
and make M6 bind delegated passes only, with the rule carried into the tracked record.

## 2. Scope (IN)

- **S1** The F-item. From `FORK_ITEM_CUTOFF`, a fork in section 8 is an F-item: a column-0 bullet
  whose bold label begins with the fork id, `- **F<n>`, or a `### F<n>` sub-head, with the
  `FACT-QUESTION · ` prefix admitted before the id. An F-item's span is its opening line plus every
  line up to the next F-item or the section's end, so option bullets and prose under it belong to it.
  Observed by AC1, AC4 and AC5.
- **S2** Per-item grading in both readers, for a spec whose filename date is at or after the
  cutoff: every F-item span must carry its own conforming mark, matched over the span with whitespace
  squeezed, so a wrapped mark still counts. The hygiene reader in
  `tools/memory-tree/check-memory-hygiene.sh` applies it where it grades section 8 today, at a
  terminal status on a Tier-2 spec. `plan_state` in `tools/unattended/unattended.sh` applies it to
  any spec it grades. Observed by AC1, AC2 and AC4.
- **S3** A quoted mark does not count. Inside an F-item span, a backticked code span and a
  double-quoted span are removed before the mark is matched. Observed by AC3.
- **S4** The shape. For a spec dated at or after the cutoff whose section 8 is not a none-form, a
  column-0 bullet or sub-head before its first F-item, or a section carrying bullets and no F-item,
  is a finding. Hygiene check 12 reports it on a Tier-2 spec, live or terminal, and under `--staged`
  as its other shape arms do; `plan_state` prints FORKED for it. Observed by AC6.
- **S5** One declaration. `FORK_ITEM_CUTOFF` is declared once, in `.memory-tree.conf`, and blank
  means off. The hygiene engine reads it with its sibling cutoffs. `plan_state` takes it as a second
  argument, and every caller passes it: `--plan`, the `build-complete` term and `--dispatch` in the
  driver, and `tools/unattended/check-pass-order.sh`, which slices the function. Each reads the one
  key from `.memory-tree.conf` as text, never by sourcing it. Gov's value is derived at build time as
  the day after the newest tracked spec filename date. Observed by AC7 and AC8.
- **S6** The contract table. `tools/memory-tree/marker-contract.test.sh` gains rows for post-cutoff
  documents covering S1 to S4, with the pinned "none line, later open" gap row flipping for a
  post-cutoff document and kept as a gap for an earlier one. Observed by AC7.
- **S7** The carriers. `memory/TEMPLATE-SPEC.md` gains a `FORK_ITEM_CUTOFF` section, and its
  resolved-forks rule and skeleton section 8 describe F-items. `memory/HYGIENE.md` check 12 gains
  the cutoff. The stale "graded PER ITEM" comment on `FORK_MARK_CUTOFF` in `.memory-tree.conf` is
  corrected. BUILD-METHOD M3's sentence that both readers grade the section is updated. Each
  rendered file moves with its kit template. Observed by AC9.
- **S8** M6 binds DELEGATED passes. In `tools/memory-tree/BUILD-METHOD.template.md` and its render,
  the `parallel-when-disjoint` MUST applies to passes dispatched to other agents; an inline author
  running the passes in its own context may sequence proven-disjoint passes and says so in the
  unit's brief. The file stays inside its own declared byte and line budget. Observed by AC10.
- **S9** A DECISIONS row, keyed by this unit's own id and written by the orchestrator at build time,
  records the M6 ruling and names D12-i10, so the rule stops living in one node's local memory.
  Observed by AC11.
- **S10** The kickoff manifest. `memory/guides/SESSION-KICKOFF.md` §B says M6 makes a build
  "parallelise what it can prove disjoint", which this unit makes true only of delegated passes, so
  that claim is rewritten. `last-audit` is re-stamped in the same commit with a delta line in the
  commit message, because `.memory-tree.conf`, `tools/memory-tree/check-memory-hygiene.sh` and
  `memory/guides/BUILD-METHOD.md` are all in its `watch:` list. Observed by AC12.

## 3. Non-goals (OUT)

- **No before-state line.** D12-i10 adopts "no before-state line" as the third of its three carriers.
  The design record names it without defining it further, and this spec reads it as the rejected
  remedy for the audit cost recorded at `dPromptedSeam/RUN.md:34`, which DR 21.4 calls an accepted
  cost. The spec format gains nothing for it.
- No rewrite of any landed or live spec. Every spec dated before the cutoff keeps today's section
  reading in both readers.
- A fork written as a plain bullet inside another F-item's span stays invisible. The shape makes a
  declared fork gradeable; it cannot find an undeclared one, and the readers' own headers say so.
- The check-12 reader's other arms, and the section-by-heading work `TOOL-dTieredTribunal-17`
  records, are not touched.
- The memory-tree kit version moves once per landing range under
  `tools/memory-tree/check-verdict-epoch.sh`'s topological rule, not in this unit.
- No change to the build harness's parallel spec writers in `tools/workflows/unattended-build.js`:
  they are delegated passes, which is exactly what M6 still binds.
- M2's grouping sentence, M6's clause 3 and M9's table are the carriers unit's edits to the same
  file; this unit edits M3 and the head of M6 only.

### Edges

none

## 4. Design

### Why a regular shape now works where a per-item walk did not

`TOOL-aBoundedVerdict-4` built a per-item walk and withdrew it on two measured defects: a mark
matched line by line missed every wrapped mark, and every bullet opened an item, so option bullets
each demanded a mark. Its measurement stands: of 287 section-8 bullets, 69 carried descriptive
labels, and nothing distinguished a fork bullet from an option bullet. `memory/TEMPLATE-SPEC.md`
says closing that gap "needs §8 to have a regular shape, which is a scope change". This unit is that
scope change. The label is the discriminator: an F-item's bold label begins with `F<n>`, an option
bullet's does not, and the span absorbs the options. The mark is still matched over the squeezed
span, which keeps the wrapped-mark fix.

### The F-item grammar, measured against the corpus

```
F-item open  = "- **" [ "FACT-QUESTION · " ] "F" <digits> ( "**" | " " )  |  "### " [ "FACT-QUESTION · " ] "F" <digits>
F-item span  = its open line + every following line up to the next F-item open or the end of section 8
resolved     = the span, code spans and double-quoted spans removed, whitespace squeezed, matches the §8 mark
```

DR spells the item `- **F<n>** — <question>`. Measured on 2026-09-14 over every spec file under
`memory/builds/`, this build's drafts included, 26 bullets use that spelling and 621 use
`- **F<n> — <question>**`, the bold spanning the question, as this build's unit 4 and unit 9 specs
do. PINNED as that measurement. The grammar admits both, because the
fork id at the head of the bold label is the discriminator, and grading only the minority spelling
would push every author toward it for no gain.

### Why forward-only, with a number

Applied to every live spec, per-item grading flips 13 live specs from READY to FORKED, measured by a
throwaway probe on 2026-09-14 at BASE. Some flips are real: `dRetiredFork`'s DEPL unit 2 carries an
F1 with no mark, hidden today by F2's mark. Others are shape artifacts, such as a mark written in
prose above the F1 bullet. PINNED as that measurement. Terminal specs cannot be rewritten to clear a
finding, and 52 terminal specs would change verdict the same way. So both readers switch only for
specs dated at or after the cutoff, and the gap row in the contract table stays a documented gap for
earlier ones.

### One declaration, two readers

The two readers live in two kits and cannot share code; `marker-contract.test.sh` proves their
agreement with a case table instead. Their CUTOFF can still be one fact. `plan_state` stays a pure
function sliceable by that harness, taking the cutoff as `$2`, and `verb_plan` reads the value with
one anchored `sed` over `.memory-tree.conf`, the way `check-unattended.sh` reads its conf key names as
text before importing anything. An absent file or a blank key is the adopter default, and per-item
grading is then off in both readers, which is the same meaning blank has on the hygiene side. A
second key in `.unattended.conf` was rejected: two declarations of one date are two answers to one
question, and the reader that drifts is the one nothing re-reads.

### M6, and why the brief is the carrier

The recorded conflict is `dSealedTally/RUN.md:54`: order 1's two units were provably disjoint, M6
required concurrency, and the run sequenced them because the practice is to delegate adversarial
review and never authoring. The ruling keeps both rules by scoping one. Parallelism is a property of
DELEGATION: when passes go to other agents and their write sets are disjoint, they run together, and
`--dispatch` records both sets as today. An inline author has no second agent to run concurrently,
so sequencing is not a choice it is making against the rule. Saying so in the unit's brief keeps the
decision on the record a later reader opens, which is where the parked entry put it.

The edit replaces text rather than adding a paragraph. BUILD-METHOD's render is 26439 bytes and 337
lines against 27648 and 350 at BASE, so the headroom is 1209 bytes and 13 lines, PINNED as measured
then. The carriers unit, ordered earlier in this build, edits M2, M6's clause 3 and M9 and spends
from the same budget first, so this unit measures its headroom at its own commit, and M3's sentence
about how the readers grade is rewritten in the same pass as a replacement.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `FORK_ITEM_CUTOFF` | memory-tree conf key | screaming snake, as every key in `.memory-tree.conf` |
| the F-item grammar | spec-format rule | none; stated once, in `memory/TEMPLATE-SPEC.md` |
| any new awk or shell helper | function | lexicon `sh` function cell; each name passes `python tools/lexicon/lexicon.py --suggest <name>` first |
| the DECISIONS row | record keyed by this unit's own id | check 13; a decision row and its spec's H1 anchor one id by design |

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/check-memory-hygiene.test.sh` ·
`tools/memory-tree/marker-contract.test.sh` · `tools/unattended/unattended.sh` ·
`tools/unattended/check-pass-order.sh` ·
`tools/memory-tree/SPEC-TEMPLATE.template.md` and `memory/TEMPLATE-SPEC.md` ·
`tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` ·
`tools/memory-tree/BUILD-METHOD.template.md` and `memory/guides/BUILD-METHOD.md` ·
`.memory-tree.conf` · `tools/memory-tree/.memory-tree.conf.example` · `memory/DECISIONS.md` ·
`memory/guides/SESSION-KICKOFF.md`.

### Alternatives rejected

- **Per-item grading of every spec, unconditionally.** Rejected by the probe above: it reds 52
  frozen terminal specs and flips 13 live ones.
- **A label-shape discriminator over today's bullets.** `TOOL-aBoundedVerdict-4` measured it: it
  under-counts, letting an open fork pass, which is worse than today.
- **Declaring the cutoff in both confs.** Rejected in §4 as two answers to one question.
- **Stripping quoted spans in the section-level reading as well.** It changes a reading nothing in
  the landed corpus depends on, measured at zero specs; it is kept inside the forward-only mode so
  every behaviour change in this unit sits behind one cutoff.

## 5. Production-readiness checklist

- security — N/A: both readers read spec text and a conf value as data; nothing is executed, and the
  conf is read by `sed`, never sourced.
- perf / scale — one extra pass over section 8 per graded spec; the section is a few dozen lines.
- error / empty / loading states — a blank or absent cutoff is the declared off state; a post-cutoff
  section with no F-item and no none-form is a finding, never a pass.
- observability — each finding names the F-item's id; the contract table prints one row per case.
- risks — an author writing a real fork as a plain bullet inside another F-item's span, stated in §3
  and in both readers' headers.
- testing — new rows in `tools/memory-tree/marker-contract.test.sh`, a repo-subject leg on every bar,
  and fixture arms in `tools/memory-tree/check-memory-hygiene.test.sh`, observed at the build's one
  post-build bar and by hand in a scratch copy. This unit may not run the unattended suites, and it
  needs no arm there: their existing `plan_state` arms pass one argument, which keeps today's reading.
- migration — none for landed specs. Adopters get the key blank, which is off, and set it when they
  choose to.
- user docs — `memory/TEMPLATE-SPEC.md` is where an author reads the rule; HYGIENE and BUILD-METHOD
  point at it.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/marker-contract.test.sh` grades a terminal post-cutoff
  fixture whose F1 carries a mark and whose F2 does not, the hygiene side reds naming F2 and the
  planning side prints FORKED.
  Red when: the section-level `bmark` still decides, and F1's mark resolves F2.
- **AC2** — When the same section 8 sits in a fixture spec dated before the cutoff, the hygiene side
  is silent and `plan_state` prints READY, exactly as at BASE.
  Red when: per-item grading ignores the filename date, which reds frozen specs.
- **AC3** — When a post-cutoff F-item's only mark sits inside backticks, and separately inside double
  quotes, `marker-contract.test.sh` sees both readers call it unresolved.
  Red when: the quoted spans are not removed, the `TOOL-dHonouredPark-7` case.
- **AC4** — When a post-cutoff F-item's mark wraps inside the parenthesis, both readers call it
  resolved in `marker-contract.test.sh`.
  Red when: the span is matched line by line, the first defect `TOOL-aBoundedVerdict-4` withdrew on.
- **AC5** — When a post-cutoff F-item carries three option bullets and one mark,
  `marker-contract.test.sh` sees both readers call it resolved.
  Red when: every bullet opens an item, the second defect that walk was withdrawn on.
- **AC6** — When a post-cutoff Tier-2 fixture's section 8 opens with a plain bullet before its first
  F-item, `bash tools/memory-tree/check-memory-hygiene.sh --staged` reports the shape finding and
  `plan_state` prints FORKED.
  Red when: the shape arm is terminal-only, so a live spec escapes per-item grading by never using
  an F-item.
- **AC7** — When `bash tools/memory-tree/marker-contract.test.sh` runs, the "none line, later open"
  case reads red and FORKED for a post-cutoff document and silent and READY for an earlier one, and
  every row passes a cutoff to the sliced `plan_state`.
  Red when: the planning side is handed no cutoff, so its post-cutoff rows pass under today's
  reading.
- **AC8** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on the real tree, it is
  green with `FORK_ITEM_CUTOFF` set later than every tracked spec's filename date, and
  `unattended.sh --plan` prints the same verdict for every live build as it did at BASE.
  Red when: the cutoff sits at or before a tracked spec's date, and a landed spec goes red.
  figure: the value is DERIVED at build time from the newest tracked spec filename date, and the
  unit's journal records it.
- **AC9** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, `memory/TEMPLATE-SPEC.md`,
  `memory/HYGIENE.md` and `memory/guides/BUILD-METHOD.md` each match their kit templates with the
  F-item text in them.
  Red when: a template carries the rule and its render does not, which the parity leg reds.
- **AC10** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs, it passes,
  and M6's rule names delegated passes and the inline-author exception.
  Red when: the added text breaches 27648 bytes or 350 lines, the method's own declared budget.
- **AC11** — When `python tools/memory-recall/query.py` is asked why an inline author may sequence
  disjoint passes, with terms naming M6 and inline authoring, it returns the new
  `memory/DECISIONS.md` row.
  Red when: the row is absent or its text names neither M6 nor D12-i10, so the rule still lives only
  in node-local memory.
- **AC12** — When `bash skills/session-kickoff/manifest-check.sh` runs on the unit's commit, check 5
  passes, and the §B bullet on M6 names delegated passes.
  Red when: the stamp moves and the M6 claim is left as it was, which passes the gate while the
  stamp asserts a re-verification that did not happen.

## 7. Gates

`marker contracts` · `memory hygiene` · `memory-hygiene self-test` · `pass-order history` · `kit/dogfood doc parity` · `build-method size` · `method carriers (every pointer declared)` · `verdict epoch (kit version dates the engine)` · `kickoff-manifest ratchet` · `recall floor` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/memory-tree/marker-contract.test.sh` · post-cutoff F-item documents with an unmarked sibling, a quoted mark, a wrapped mark, option bullets, a leading plain bullet, and the none-line case · the harness's case count
New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · a post-cutoff Tier-2 fixture with a plain bullet before its first F-item · any `ARMS_FLOORS` move the new branch requires

## 8. Open questions

- **F1** — Which F-item spellings count? Options: (a) DR's `- **F<n>** —` only; (b) any column-0
  bullet or sub-head whose bold label or heading begins with the fork id. (a) grades 26 of 647
  measured fork bullets and would push authors to one spelling for no verdict gain.
  RESOLVED (agent, 2026-09-14, delegated): (b).
- **F2** — Where does `plan_state` get the cutoff? Options: (a) a second key in `.unattended.conf`;
  (b) the one key in `.memory-tree.conf`, read as text by `verb_plan`; (c) no cutoff, keyed on the
  F-item shape alone. (a) declares one date twice, and (c) flips the 13 live specs §4 names.
  RESOLVED (agent, 2026-09-14, delegated): (b).
- **F3** — Does the shape rule live on live specs or only at a terminal status? A terminal-only rule
  lets a live spec carry non-F forks that the planning verb then grades section-wise.
  RESOLVED (agent, 2026-09-14, delegated): live and terminal, on the same staged path the other
  check-12 shape arms use.
- **F4** — Where does the inline author say it sequenced disjoint work? Options: the run-state file;
  the unit's brief; nowhere. The run-state file is the run's, and an attended run has none.
  RESOLVED (agent, 2026-09-14, delegated): the unit's brief.
- The three carriers themselves, per-item F-item forks forward-only, M6 binding delegated passes
  only, and no before-state line, are RESOLVED (owner, 2026-09-13) as ruling D12-i10.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.

## 10. Reuse audit

Both readers already exist, and this unit changes their predicate rather than adding a third. The
hygiene side is the tightened section-8 block in `tools/memory-tree/check-memory-hygiene.sh` at
`:1455-1512`, gated today by `FORK_MARK_CUTOFF`; the planning side is `plan_state` in
`tools/unattended/unattended.sh`, whose section-8 branch runs from `:1700`. The agreement proof is the
case table in `tools/memory-tree/marker-contract.test.sh`, which slices `plan_state` out of the
shipped bytes and already pins the gap this unit closes. `python tools/codebase-map/reuse_lookup.py
"grade each open question fork in a spec section individually by its resolution mark"` returned
affordance-seam prose matches only, the unattended conf and the row-grammar seam among them, and it
reports `.sh` as an unscanned layer, so it cannot see either reader; no seam grades forks per item.
Recall returned `TOOL-aBoundedVerdict-4`, the per-item decision and its withdrawal, the open ask
`TOOL-dHonouredPark-7` on quoted marks, and `TOOL-aWidenedGuide-2`, which is why S1 admits a `###`
sub-head as an F-item.

Where DR and the source disagree at BASE: DR cites `plan_state` at `:1700-1741`, and the function
spans `:1660-1760` with its section-8 branch from `:1700`. DR's F-item spelling is the minority one
in the corpus (§8 F1). M12's rejected candidates and the probe that rejected each are in §4,
Alternatives rejected.

Recall terms used: `section 8 fork per-item walk RESOLVED mark plan_state option bullet
FORK_MARK_CUTOFF quoted parallel-when-disjoint inline author`
