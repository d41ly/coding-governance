# Dry-run research — the six strands behind the owner's rulings this build implements

**Serves:** research TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-3 TOOL-dGatedProse-4 TOOL-dGatedProse-5

Node `d`, written 2026-09-21 on `branch/spec-prose-gates-b41f7c` at `bd44d3ff`. The source is
session-local evidence: the journal of the workflow that ran the dry run, which holds one structured
result per agent and does not outlive the session that produced it. This file is the tracked copy of
what that journal holds, and it closes finding M6 of the round-1 spec audit,
`memory/builds/dGatedProse/reviews/2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md`.
Every dry-run figure below is copied as the agent that measured it wrote it. Nothing was re-run for
this record. Where a skeptic refuted a stage-1 figure, both figures appear and the refuted one is
named. The few figures about the merged tree are marked as such and were measured for this record.

## How the dry run ran

The owner ruled on `TOOL-dLoggedFlight-31` to `TOOL-dLoggedFlight-34` on 2026-09-20, and the build
README's rules slot states the dry-run-before-wiring rule this workflow served. It ran one strand per
backlog row, and three for `TOOL-dLoggedFlight-32`, which names three checks.

Each strand is a pair of agents. A stage-1 agent implemented the ruling from its text, ran it over
the live corpus, and returned the predicate as run, the population, the hits, near misses and false
positives with their lists, a rule text, a carrier, a cost and one of two verdict tokens:
BACK_TO_OWNER or WIREABLE_WITH_NARROWING. A skeptic then implemented the same ruling independently,
tried to break stage 1, and returned whether the counts reproduced, its own hit count, whether it
refuted stage 1, what breaks, and a verdict of its own.

The journal holds twelve starts and twelve results, so no agent died. Five stage-1 agents started
before any result came back, each skeptic started when its own stage 1 returned, and the `m4-bound`
pair started after the other five skeptics had returned. Every probe an agent names sits in a session scratchpad
and is untracked, so none is reachable from this record.

The agents were told the corpus held about 40 live and about 300 closed specs. Every agent that
derived it reports both halves wrong: 641 tracked spec files, 24 live and 617 terminal, by the
liveness test `tools/check-spec-tokens.py` owns. The one exception is strand 6's stage 1, which its
skeptic corrected.

The journal carries no timestamp. The build's records date the workflow 2026-09-20, and date the
first rulings that followed it the same day. Two stage-1 agents wrote 2026-09-21 into the text they
proposed. This record does not reconcile the two.

## The six strands at a glance

| Strand | Backlog row | Population | Stage-1 hits, innocent | Stage-1 verdict | Skeptic reproduced | Skeptic hits | Refuted | Skeptic verdict | Owner, afterwards |
|---|---|---|---|---|---|---|---|---|---|
| 1 `retirement-readers` | `TOOL-dLoggedFlight-31` | 24 live specs | 3, 3 | BACK_TO_OWNER | no | 1 strict, 2 lenient | no | BACK_TO_OWNER | re-ruled to a shape check |
| 2 `ac-names-suite` | `TOOL-dLoggedFlight-32`, check A | 24 live specs | 17, 8 | BACK_TO_OWNER | no | 16, or 58 on the row's own wording | no | BACK_TO_OWNER | dropped |
| 3 `replaced-unobserved` | `TOOL-dLoggedFlight-32`, check B | 24 live specs, 224 scope items | 7, 7 | BACK_TO_OWNER | no | 11 items on 13 tokens | no | BACK_TO_OWNER | dropped |
| 4 `claims-no-key` | `TOOL-dLoggedFlight-32`, check C | 24 live specs | 7, 7 | WIREABLE_WITH_NARROWING | no | 6 | yes | BACK_TO_OWNER | mechanism not re-ruled |
| 5 `guide-cap` | `TOOL-dLoggedFlight-33` | the 7 guides | 7 measured, 6 not bound | WIREABLE_WITH_NARROWING | yes | 7 | no | WIREABLE_WITH_NARROWING | pair ratified, then raised to 98304/1200 |
| 6 `m4-bound` | `TOOL-dLoggedFlight-34` | 56 run-state files | 3 runs, 2 | WIREABLE_WITH_NARROWING | no | 3, a different set | yes | WIREABLE_WITH_NARROWING | replaced by a precision bound |

## Strand 1 — `retirement-readers`, the reader-inventory ruling

- **Predicate as run.** Over every live spec, section 2 found by heading text and split into scope
  items. An item is a retirement clause when a ceasing-to-exist verb shares it with a backticked
  NAME. The verbs: retires, is or are replaced by, removes, deletes, drops, no longer exists or
  carries or reads, stops being, ceases, goes away, leaves the layouts or set or vocabulary. A NAME
  is a code identifier, a code-file path or a CLI flag, never a `.md` doc and never an id, and a bare
  lowercase word only beside a vocabulary, kind, enum, member or layout signal. A flagged spec is a
  HIT when no other sentence in it names a retired name beside a reading verb or reader noun together
  with some other identifier.
- **Population.** 641 tracked spec files under `memory/builds/*/spec/` at any depth, 24 live and
  617 terminal.
- **Hits: 3, all innocent, precision 0.00.** aGradedDoorway-7 S2 retires nothing: the verb came from
  a sentence about a failure mode. aMendedLedger-1 S1 deletes three `.md` stubs and gives a slug a
  folder, while the spec's real retirement, S2, is invisible because its only token is a `.md` path.
  aMendedLedger-8-u9 S2 does inventory its readers, in a section-4 table and in qualified
  module-dot-symbol tokens, and the reader test wanted a sentence.
- **Near misses: 15.** The first is THE CONTROL: `TOOL-dLoggedFlight-22` at rev-3, read at
  `3b8ec944`, the revision whose by-name inventory missed three readers and blocked three spec
  audits. The predicate passes it. Its seven retirement clauses carry 15, 4, 6, 14, 14, 1 and 7
  reader-naming sentences, and rev-4, the fix, carries 18, 5, 7, 15, 15, 2 and 9. Five more are
  PARTIAL specs, where one retirement is inventoried and another is not: aMendedLedger-3-u2,
  aMendedLedger-4-u3, aMendedLedger-6-u6, bConvergentLodestar-1 and dPolishedVitrine-1. Six pass
  correctly, and three carry the verb with no name.
- **Narrowing figures.** The raw verb vocabulary flagged 19 of the 24 live specs, requiring a
  backticked NAME brought it to 14, and stage 1 judged about five of those 14 to retire nothing. A
  surrogate asking only whether a spec names any reader anywhere passed 24 of 24.
- **Cost.** 0.354 s median of five whole-process runs, of which the liveness scan is 0.125 s.
- **Stage-1 verdict: BACK_TO_OWNER**, decided by the control rather than the count. A gate green on
  its motivating defect grades nothing, and a by-value reader is a token the author never wrote,
  which no predicate over prose can see. In place of the ruled check, stage 1 proposed another: a
  `**Readers:**` clause on a retiring scope item, with a `by name:` half and a `by value:` half or
  `NO VALUE READERS` with a reason, graded for shape only, as hygiene check 25, forward-only behind a
  `READER_INVENTORY_CUTOFF` key.
- **The skeptic: counts not reproduced, not refuted, verdict BACK_TO_OWNER.** It reproduced the
  population. It reproduced the control independently, reading rev-3 at `3b8ec944` and rev-4 at
  `740f837c`: both pass, with 10 against 12 reader sentences under the strict vocabulary and 11
  against 13 under the lenient one. It attacked the structural claim hardest and could not break it.
  It did not reproduce the hits: the verb list as stated gives it 1 hit, ordinary inflections give 2,
  and only aGradedDoorway-7 is common to its list and stage 1's. Its further findings:
  - a per-item quantifier reds 4 items of rev-3 and 3 of rev-4, and none of either under the strict
    vocabulary, so the obvious narrowing reds the fix;
  - over 117 retired names the per-name inventory rate is 0.52 strict and 0.62 lenient, while the
    whole-spec verdict passes 6 of 7 flagged specs strict and 14 of 16 lenient;
  - the name test collected 42 retired names over the control, among them row-layout words such as
    commit, push, phase and gate, and it admits an elided-slug id as a CLI flag;
  - dPolishedVitrine-14 S5 is a false-positive class stage 1 did not list, flagged on "stops copying";
  - all 24 live specs carry a markdown table, and 11 of the 117 names appear only in a table row;
  - its own probe ran 268 to 301 ms whole-process, median 276 ms.
- **Refuted.** Stage 1's 3 hits, which faithful readings put at 1 or 2. Its 24 of 24 for the
  any-reader surrogate, which is 23 of 24, since dScriptedRepeat-8 carries no reader sentence. Its
  label of `3b8ec944` as a git blob, which is a commit. Its statement that the proposed check "reds
  today's fourteen the moment the cutoff passes them": cutoffs grandfather by filename date, so a
  cutoff set strictly past the commit day reaches none of the 24 live specs, now or ever. The skeptic
  also found the proposed check shape-identical to the scope-join arm, possibly a branch of it,
  which changes the obligations stage 1 quoted.
- **Owner, afterwards.** The ruled predicate is not built. The owner re-ruled a replacement on this
  evidence, and `TOOL-dGatedProse-1` builds it (unit 1, section 3). The owner's rulings of 2026-09-21
  then shaped it. O2 deleted the cutoff key, so the population is every live spec from the landing
  commit. O3 added a kind-noun vocabulary. O4 grades the `by name:` half for resolution. O5 added the
  past tense, and O6 deleted the `.md` exclusion (unit 1, section 9, rev-3 and rev-5). The owner's
  ruling to fix the corpus before the check lands is `TOOL-dGatedProse-5` (unit 1, section 1).

## Strand 2 — `ac-names-suite`, check A: a criterion names a suite or a leg

- **Predicate as run.** Over each live spec's acceptance-criteria bullets, the observation clause
  before `Red when:`. A backticked token is flagged when it is a tracked suite file (`*.test.sh`,
  `selftest.py`, `test_*.py`) at command position or before an observation verb; an identifier
  defined only inside a tracked suite module; or an exact `name` from `tools/gate-legs.json`. It is
  cleared by a permission or deferral clause, by a section-7 `New arm:` line naming the suite, by
  section 7 naming it otherwise, or by section 2 naming it. A wide first version flagged 67, and
  requiring command position or an observation verb dropped 50 of those.
- **Population.** 24 live specs.
- **Hits: 17 signals, 8 innocent, precision 9/17 = 0.53.** Six innocents are the suite-symbol arm
  meeting ordinary words and constants that happen to live in a suite module. The other two are
  bullets that write the `New arm:` attribution inline, aMendedLedger-1 AC5 and aQuarriedLantern-1
  AC13. Two of the nine guilty signals are the leg name `govkit selfcheck`, in dPolishedVitrine-1
  AC16 and AC20.
- **Near misses: 62.** The first is the motivating blocker itself: `TOOL-dLoggedFlight-26` rev-1
  AC3, read at `3b8ec944`, is cleared by the row's own exemption, because rev-1's section 7 carries a
  `New arm:` line naming the suite module. AC1 and AC2 of the same spec, both innocent, clear the same
  way. The journal counts 31 of the 62 cleared on section 2, 19 on a `New arm:` line and 30 on section
  7 naming the suite otherwise; the three figures sum past 62. The existing `bar` join grades zero
  today, since every live spec is dated 2026-09-13 or earlier and `SPEC_DIRECT_CUTOFF` is 2026-09-15.
  `permission:` appears in 7 specs corpus-wide and in no live one.
- **Cost.** 0.37, 0.36 and 0.39 s over three runs.
- **Stage-1 verdict: BACK_TO_OWNER** for the suite-symbol half. The exemption cannot separate the
  blocker from its siblings, because `New arm:` names a module and all three criteria name symbols
  inside it. What did separate them is that AC3 named a one-time probe the unit ran and discarded,
  and no token join reaches that. Stage 1 recommended wiring the leg-name half now, reporting it as
  two hits, both real, and zero false positives.
- **The skeptic: counts not reproduced, not refuted, verdict BACK_TO_OWNER on both halves.** It
  reproduced the population, the cutoff's day-one zero, the 7 and 0 for `permission:`, and the central
  refutation exactly. Under stage 1's own exemptions it gets 16 hits over a partly different set.
  Under the row's literal wording it gets 58: 39 suite-file, 16 suite-symbol and 3 leg-name. Stage 1
  had added two exemptions the owner never ruled, section 7 naming the suite and section 2 naming it,
  and those carry 38 of the 61 clearings. `New arm:` appears in 2 of the 24 live specs. Its further
  findings:
  - stage 1 missed a live leg-name hit, aTetheredScratch-2 AC8, and a live suite hit,
    bConvergentLodestar-1 AC6, spelled as a bare basename;
  - the 17 counts one bullet twice, and per bullet the figure is 7 guilty of 14, precision 0.50;
  - 41 live acceptance bullets state a suite or bar run in prose with no backticked token, invisible
    to every arm;
  - 5 of its 7 guilty bullets already match the wired `bar` regex, so the suite-file half's unique
    yield is two bullets, aMendedLedger-3-u2 AC14 and aMendedLedger-8-u9 AC20, both naming a
    `test_*.py` suite that regex omits;
  - the leg-name half has false positives in five shapes, among them a leg whose name is its
    checker's own CLI spelling, criteria that stage a checker break and name the leg while doing it,
    and aProbedUnit-6 AC11, dated one day before the cutoff, which says its legs are observed at close;
  - 89 of the 111 leg names are plain lowercase English phrases, and `tools/gate-legs.json` took 141
    commits in 60 days;
  - 166 acceptance bullets corpus-wide name a leg, exactly one carries `permission:`, and 85 of them
    share a bullet with a hit the `bar` arm already makes;
  - all 18 tracked specs at or after the cutoff are terminal and carry no leg name in a criterion;
  - 5 tracked specs carry no status header and 9 are DEFERRED, both are counted terminal, and so no
    arm ever grades them.
- **Refuted.** Stage 1's 17 hits. Its "two hits, both real, zero false positives" for the leg-name
  half, which has three live signals and false positives in five shapes. Its recommendation to wire
  that half.
- **Owner, afterwards.** Check A is DROPPED, by the owner ruling the build README records under its
  parked decisions and dates 2026-09-20: A cannot separate its motivating blocker from two innocent
  criteria of the same spec, and its exemption is absent from 22 of the 24 live specs. Nothing of it
  is built.

## Strand 3 — `replaced-unobserved`, check B: a replacement with no criterion observing the old spelling

- **Predicate as run.** Over every live spec carrying both a scope and an acceptance-criteria
  heading, each column-0 scope item with its continuation lines. A replacement clause is a backticked
  token governed by a replacement verb, passive (is or are replaced, superseded, retired, removed,
  dropped, deleted) or active third-person (replaces, supersedes, retires, removes, drops, deletes).
  That token is the OLD SPELLING, and the item is flagged when no acceptance item of the same spec
  contains it and the item carries no `NOT OBSERVED`.
- **Population.** 24 live specs.
- **Hits: 7, all innocent, precision 0.00.** Three flag a line-number citation, one of them with the
  verb attached to the wrong noun: aMendedLedger-1 S8, and aMendedLedger-6-u6 S5 twice. One is a
  defect narrative, aMendedLedger-4-u3 S4. Two have their criterion in a different spelling:
  aMendedLedger-8-u9 S2, observed module-qualified in AC20, and aTunedCompass-3 S2, observed as a grep
  argument in AC7. The last, bConvergentLodestar-1 S3, retires a file in a foreign repo, and stage 1
  called it borderline.
- **Near misses: 22**, most of them a replacement verb on a prose object with no backticked token,
  which leaves the item ungraded. aQuarriedLantern-1 S6 is the one live item where the escape
  demonstrably worked.
- **The vocabulary.** The ruling's `is replaced by` occurs zero times in the live scope sections. Of
  224 live scope items, one says REPLACED and one says replaces. The corpus says deleted (16 items),
  rather than (31), retire and its forms (14), instead of (10), drops (9) and removed (8), and 28
  scope items in 15 specs carry a replacement verb at all.
- **A narrowed predicate** drops line-number citations, joins on loose stems and drops defect
  language. Over the live corpus it returns 0 hits and 8 near misses. Run against the two instances
  the ruling cites, it fires on `TOOL-dLoggedFlight-27` S3 at rev-1 through rev-3, including rev-3,
  which closed the gap by routing the observation to `TOOL-dLoggedFlight-30`. It fires on
  `TOOL-dLoggedFlight-25` S4, whose AC2 observes the removal as a grep, and never fires on that spec's
  S2, the item the ruling names, which carries no replacement verb. Both evidence specs are CLOSED.
- **Cost.** 0.20 s for the whole probe, minimum of three runs.
- **Stage-1 verdict: BACK_TO_OWNER**, on precision. It recommended a writing rule in
  `memory/TEMPLATE-SPEC.md` beside the scope-join paragraph and a section-10 checklist entry, with no
  checker.
- **The skeptic: counts not reproduced, not refuted, verdict BACK_TO_OWNER.** It reproduced 641, 24
  and 617, the 24 specs carrying both headings, 224 scope items and 319 acceptance items, both
  evidence specs CLOSED, and the predicate reding the remedied revision and the compliant item. Its
  own predicate, written from stage 1's rule text, flags 11 items on 13 tokens: five of stage 1's
  seven survive and six are new. Its further findings:
  - on `SCOPE_JOIN_CUTOFF`'s footing, 2026-09-08, the graded population is 2 specs and 19 scope
    items, and the one hit is dPolishedVitrine-1 S10, which names eight criteria, so precision there
    is 0 of 1;
  - ten of its eleven hits name no criterion and carry no escape, so the existing shape-only
    scope-join arm already reds them; the narrowing that would clear the false positives also clears
    both cited instances, because each names a criterion, the wrong one;
  - stage 1's published join is containment, and under containment two of its seven hits are not
    hits, since the flagged token appears in aMendedLedger-4-u3 AC4 and AC5 and in aMendedLedger-8-u9
    AC20;
  - the corpus writes removals in the imperative and the gerund, which a third-person verb set
    cannot see: six live items, and aMendedLedger-4-u3 S1, whose five deleted tokens none of that
    spec's 14 criteria names, a genuine live instance of the class;
  - six of its eleven hits attach the verb to a token that is not the replaced thing: a destination,
    a container, a survivor or the new spelling;
  - a third miss-shape, a criterion observing the containing directory rather than the file,
    aMendedLedger-3-u2 S2 against its AC1;
  - 47 of the 224 live scope items carry a replacement verb and only 11 a backticked token the join
    can attach;
  - the escape is matched as a substring, exactly one live scope item uses it for real,
    dPolishedVitrine-1 S2, and the rule text's `NOT OBSERVED:` with a colon is a second spelling;
  - precision over its 11 is 0.09 to 0.18, and its probe cost 0.235 s.
- **Refuted.** Stage 1's 7 hits. Its precision of 0.00 as computed, since two of its seven are not
  produced by the join it published. Its report of zero true positives in the live corpus. Its
  framing of the narrowed predicate's failure as a zero, where on the population the arm would grade
  it is one innocent red.
- **Owner, afterwards.** Check B is DROPPED by the same ruling: B is strictly dominated by the
  existing scope-join arm, which already reds ten of the eleven items B finds, and the corpus does
  not use the vocabulary the ruling named. No unit of this build carries the writing rule both stages
  recommended.

## Strand 4 — `claims-no-key`, check C: a dossier claim naming no inventory key

- **Predicate as run.** Each live spec's paragraphs flowed into one string. Each claim verb (claim,
  claims, claimed, claiming) outside backticks, with a codebase-map dossier subject within a
  200-character look-back: a `memory/map/features/*.md` or `memory/map/FOUNDATION.md` path, or the
  bare words dossier, dossiers or codebase map. The first backticked token after the verb in the
  sentence is resolved against a live re-derivation of the map's inventories, 260 exact keys over 10
  ratchet inventories, plus the 10 inventory ids, the 17 `[paths]` globs stage 1 counted and any
  glob-shaped token. An unresolved token is a hit. A narrowed variant requires a backticked dossier
  path adjacent to the verb and a backticked object adjacent after it. It was run against a staged
  break: the pre-fix blobs of `TOOL-dLoggedFlight-25` and `TOOL-dLoggedFlight-27` at `9f43bb26^`,
  which carry the motivating sentences verbatim.
- **Population.** 24 live specs.
- **Broad hits: 7, all innocent, precision 0.00.** Claim as a noun, the verb inside a quoted
  phrase, a table row flattened into its neighbour, a that-clause, and an object-fronted relative
  clause where the claimed thing precedes the verb, at dPolishedVitrine-1:231, which is the correct
  way to write the sentence. Stage 1 called aTunedCompass-3:112 the genuine boundary case.
- **Near misses.** Stated as 12. The list carries 11 entries.
- **The narrowed variant.** 0 hits over the 24 live specs, 0 over the 617 terminal ones, 1 near miss
  in all 641, aProbedUnit-1:82, which claims a real `workflow-scripts` key and clears. It is RED on
  both staged-break blobs.
- **Cost.** 52 ms marginal on the existing `spec tokens` leg: 39 ms to import the map's extractors,
  8 ms to build the inventories, 6 ms for the regex pass. The leg runs 0.35 s, so about 15%.
- **Stage-1 verdict: WIREABLE_WITH_NARROWING.** The narrowed shape as a fifth `claims` join in
  `tools/check-spec-tokens.py` behind a `SPEC_CLAIMS_CUTOFF` key. The rule text says a dossier claims
  an exact inventory key or a `[paths]` glob and nothing else. The header was to name the two shapes
  it cannot see, an unbackticked dossier name and an object-fronted clause.
- **The skeptic: counts not reproduced, REFUTED, verdict BACK_TO_OWNER.** It reproduced 641, 24 and
  617, with the live split INPROGRESS 8, SPECCED 13, BLOCKED 2 and OPEN 1. It reproduced the 260 keys
  over 10 inventories, equal to the committed `memory/map/generated/inventories.json`, the staged
  break red on both blobs, and the judgement that the broad predicate fails. It gets 6 broad hits,
  not 7: the dossiers declare 96 `[paths]` entries, 16 wildcard-shaped and 80 exact, not 17, and the
  seventh hit's token is an exact entry of one of them. The narrowed shape is not 0 hits over the
  641 but 1, cKeyedLaunchpad-2:39, a CLOSED spec carrying the most precise dossier-claim sentence in
  the corpus. Nor is there 1 narrow-shaped near miss: there are 3 matches, two clears and that red.
  Its further findings:
  - of 13 re-spellings of the same defect in shapes the corpus uses, the narrowed predicate catches
    2, the staged break and the same sentence wrapped; the journal names nine shapes it is invisible
    to, among them a bare backticked basename, a modal, the future, the passive and an adverb
    between subject and verb;
  - a conjunction hides the second object, a claim naming a key another dossier owns passes, and a
    common-word object resolves by coincidence, since the universe holds 23 single-word
    `lexicon-verbs` keys, 3 bare git-hook names and 80 gotcha filenames;
  - 37 uppercase claim-verb tokens occur across the 641 specs, and neither the rule text nor the
    predicate says whether case matters;
  - the rule text contradicts the map's own contract, which says path globs are digest-only and
    never gated (`tools/codebase-map/gen_map.py:119`, `memory/map/README.md:28`), so the resolver
    passes a claim that books no grader, and an exact glob entry passes where a file under the same
    dossier's wildcard reds;
  - a spec is written before its code: dPolishedVitrine-1 was committed at `906604cf` 22 minutes
    before `78eb7488` created the key its dossier prose names, and the leg is unguarded and runs on
    every bar, so resolution grades a forecast against present state;
  - the join would resolve against the working tree while the checker reads the tracked tree, stated
    from source and not reproduced, and it couples the spec-tokens leg to the codebase-map kit;
  - the map's own ratchet already fails a claim naming a dead key
    (`tools/codebase-map/map_lib.py:10`), so the check shortens a loop rather than closing a hole;
  - stage 1 missed one broad near miss, dPolishedVitrine-1:617.
  It did not verify the cost figures, because doing so meant running the leg.
- **Refuted.** Stage 1's 7 broad hits. Its 17-glob universe. Its 0 narrowed hits over the terminal
  specs. Its single near miss in 641, the whole evidence that the narrowing would not red an innocent
  file. Its count of 12 near misses. The glob clause of its rule text. The cost figures stand
  unverified rather than confirmed.
- **Owner, afterwards.** The build README records checks A and B dropped and records no re-ruling of
  C's mechanism (unit 2, section 3). Unit 2 resolved its own fork F1 under BUILD-METHOD M3 as a fact
  question, on the skeptic's 22-minute window: refuse a closed set of shapes and resolve nothing
  (unit 2, section 8). The owner's ruling O2 of 2026-09-21 declined `SPEC_CLAIMS_CUTOFF`, as it
  declined every cutoff for this build's spec-prose predicates (unit 2, section 9, rev-3).
  `TOOL-dGatedProse-2` builds the join.

## Strand 5 — `guide-cap`, the guide-size cap

- **Measurement, not a predicate.** Every file under `memory/guides/`, bytes and lines against
  `GUIDE_CAP_BYTES` and `GUIDE_CAP_LINES` by check 6's own comparison. Headroom at eight candidate
  byte figures, the byte figure above which the line cap binds first, the protocol's size history
  over the 125 commits that touched it, and every live file that restates the cap.
- **Population.** The 7 guides. The strand's spec-corpus figure, 24 live, is not its own corpus.
- **Hits: 7 measured, 6 not bound by the cap.** The one breach is
  `memory/guides/UNATTENDED-PROTOCOL.md` at 62270 B and 701 lines: 830 B over 61440, 49 lines inside
  750. The others, as a share of 61440: BUILD-METHOD 27572 B and 350 lines at 44.9%, whose real bound
  is its own 27648 row in `tools/template-size-limits.txt` with 76 B free; SESSION-KICKOFF 20021 B
  and 248 lines at 32.6%; REVIEW-PROTOCOL 17479 B and 236 lines at 28.4%; UNATTENDED-VERBS 13014 B and
  143 lines at 21.2%; PLAYBOOK-TEMPLATE 11423 B and 187 lines at 18.6%; ANNOTATION-STYLE 4812 B and 89
  lines at 7.8%.
- **Near misses: 8.** Among them: `tools/unattended/PROTOCOL.template.md`, byte-identical at 62270 B,
  outside check 6 but copied into every adopter by `tools/unattended/adopt-unattended.sh`;
  `tools/unattended/SKILL.template.md` at 63477 B with no declared ceiling; `INDEX_CAP_BYTES` at the
  same 61440, which is the wrong key; `WIRE-INTO-PROJECT.md` at 59833 B, outside every registry; and a
  self-test arm whose expected string asserts the default.
- **Growth.** Since the split that moved section 7 out, 402 B and 2.65 lines a day over 20 days:
  54231 B and 648 lines then, 62270 B and 701 lines at the dry run. Over the file's whole 42 days,
  1239 B a day. The split recovered 7209 B and lasted 20 days.
- **The narrowing.** A byte-only raise is inert above 66623 B: the 49 free lines at 88.8 B a line
  cost 4353 B, and the line axis reds first, in about 18 days. Capped at 66623, a byte raise buys 11
  days.
- **Recommendation.** 81920 B and 1000 lines: 19650 B of headroom, 49 days at the measured rate, and
  1000 = 81920 / 81.92, the shipped allowance preserved. The conservative alternative, 73728 and 900,
  leaves 11458 B, 29 days. The carrier is the kit default in
  `tools/memory-tree/check-memory-hygiene.sh`, not this repo's conf, and six files change. The debt
  row in `memory/project/curation-debt.txt` must go in the same commit, because the stale-entry guard
  fails a row that hides nothing, and that guard does not run under `--staged`.
- **Cost.** None added on any bar. The growth reconstruction took about 250 git invocations, once.
- **Stage-1 verdict: WIREABLE_WITH_NARROWING**, the narrowing being that both keys move where the
  row names one.
- **The skeptic: counts reproduced, not refuted, verdict WIREABLE_WITH_NARROWING.** Every stage-1
  figure reproduces: the 7 guides and their sizes, the single breach, the split commit `dc9431f8` on
  2026-09-01 at 54231 B, the 402 B and 2.65 lines a day, and the 641, 24 and 617 spec corpus. What does
  not survive is "six files change". Its findings:
  - the kit-version bump is mandatory and missing: `tools/memory-tree/check-verdict-epoch.sh`
    requires `KIT_MEMORY_TREE_VERSION` to move for a behaviour-bearing engine line, its leg is
    unguarded, and the bump cascades through `tools/check-kit-versions.sh` to four templates and their
    four rendered copies, about 14 files and one render in all;
  - a second self-test arm breaks beside the one stage 1 named, both driven by one fixture, and that
    self-test is held on an ordinary bar, so the break would land green;
  - the 66623 B break-even uses the file's average density; the marginal density of the measured
    growth, 151.7 B a line, puts it near 69700 B, roughly 18 days rather than 11;
  - a seventh live restatement of the line cap sits in a mutable row of `memory/backlog/TOOL.md`;
  - existing adopters copied the example conf into their live conf at adoption, so neither edit
    reaches them;
  - no gate compares `tools/memory-tree/.memory-tree.conf.example` with the engine defaults;
  - the bar is not red today, because the debt row already waives the protocol, so the raise
    exchanges a recorded waiver for a raised cap.
  It could not break the recommendation: 81920 and 1000 keep the 81.92 B a line allowance, bytes stay
  the binding axis, and the cap still binds exactly one file.
- **Refuted.** No count. The carrier list, "six files change", and the 66623 B break-even as a
  provable figure.
- **Owner, afterwards.** The owner ratified 81920 bytes and 1000 lines on 2026-09-21 (ruling O1),
  then raised the pair to 98304 bytes and 1200 lines the same day, once the merged tree showed the
  protocol growing faster than this strand measured. `TOOL-dGatedProse-3` builds the raised pair. Its S8 carries the kit-version move
  the skeptic found missing, and its section 3 hands off the adopter migration and a prose-parity
  gate rather than building them.
- **On the merged tree**, at `bd44d3ff`: the protocol is 64939 B and 704 lines against the unchanged
  61440 and 750 at `tools/memory-tree/check-memory-hygiene.sh:84`, its debt row still stands, and
  `KIT_MEMORY_TREE_VERSION` is 2.82. The dry run's headroom and day figures are against 62270 B.

## Strand 6 — `m4-bound`, the spec-audit promotion chain

- **A census, since the row is a prose edit.** Arm A: over every tracked `memory/builds/*/RUN.md`,
  the review rows, dropping the subject equal to the bare slug, which is the closing diff review, and
  every unit-id subject. Each surviving subject is one audited spec-set generation, and a run with two
  or more is a promotion chain. Arm B: ten carriers grepped for text the new rule would contradict.
  Arm C: the candidate edit applied to scratch copies of both BUILD-METHOD files and weighed against
  `tools/template-size-limits.txt`.
- **Population.** 56 tracked run-state files, 42 with any review row, 15 with any spec-audit
  generation. Its spec figure, 620 tracked and 17 live, is the exception noted above.
- **Hits: 3 runs, 2 innocent, precision 0.33.** dLoggedFlight is the true hit: promoting generations
  r4 to r7, then an override at round 7, whose recorded precision was 0.27 against the 0.5 floor.
  aGradedMandate's two generations stopped on their own, which the rule permits, and dTieredTribunal's
  second subject is a fold re-key rather than a promotion.
- **Near misses: 12.** The list names one-generation runs under the harness-era subject naming and
  under three older ones, and two runs whose `--override specs-audited` is the arrived-CLOSED
  exemption, three of the corpus's four overrides.
- **Arm C.** A 384 B rule text, paid for by three deletions inside M4 of 197, 57 and 108 B.
  `memory/guides/BUILD-METHOD.md` goes from 27572 to 27594 B against its 27648 row, and from 350 to
  349 lines. The template goes from 27597 to 27619 B. The advisory high-water, 26941, already fires.
- **Arm B.** Nothing becomes false. The unattended Skill's bounded-exit bullet becomes incomplete,
  and the harness's re-invoke message offers no stopping route.
- **An aside it flagged.** The comment in `tools/template-size-limits.txt` explaining this cap says
  five `{{TOOL_ROOT}}` for a net of minus 11. The template holds seven, a net of minus 25, which is
  the delta the two files show.
- **Stage-1 verdict: WIREABLE_WITH_NARROWING.** The rule as a documented check paid for by the three
  deletions, and no predicate, since the review-subject key has at least four spellings.
- **The skeptic: counts not reproduced, REFUTED, verdict WIREABLE_WITH_NARROWING**, the same token
  with almost none of the same reasoning. It reproduced the edit arithmetic exactly (384 B in,
  197 + 57 + 108 = 362 B out, net plus 22, 27594 B and 349 lines, 54 B left), the override census, the
  placeholder correction, and the mechanism claim that nothing BOUNDS a promotion chain. It did not
  reproduce the census. Its own hits are also 3, a different set: dLoggedFlight, aGradedMandate and
  dMispairedQuote, found from `**Serves:** spec-audit` lines crossed with the run-state files'
  rescope rows. Its further findings:
  - Arm A drops unit-id subjects by construction, and 140 of the 250 review rows are unit-id shaped;
    dMispairedQuote is a genuine two-generation chain recorded that way, so "bites once in 56 tracked
    runs" is false;
  - that run's promoted unit took three rounds and disposed by fold, and "fresh subject, one round,
    never re-rounded" would forbid it;
  - "NOTHING counts generations" is wrong, since the harness keeps a round number and keys each
    subject `-r<N>` from it; what holds is that nothing BOUNDS them;
  - "one round" hard-codes `REVIEW_ROUNDS`, which the same paragraph names and a project may raise;
  - half the new sentence restates the unattended Skill;
  - the draft cites no prior art: finding 57 of aBoundedVerdict's review of 2026-08-19 raised this
    chain and was refuted on a reading that covers only the closing round, and that spec withdrew a
    round cap on the owner's instruction;
  - over all 387 review records, keyed on the binding line, 25 builds carry two or more spec-audit
    generations and 49 build and id-set pairs were audited 2 to 4 times;
  - a run-state file exists for 56 of 119 build folders, and 30 of the 63 without one hold spec-audit
    records, so an attended build cannot appear in the census;
  - under stage 1's own rule dLoggedFlight carries five generations, not four, and aGradedMandate's
    first row is 2026-08-30T23:41:31Z, not the one stage 1 quoted;
  - stage 1's glob skipped `spec/units/`, 21 tracked files of which 7 are live, and the checker's own
    join gives 641 and 24, with 575 CLOSED rather than 561;
  - `specs-audited` forces the override only when the run closes the promoted units;
  - the render substitutes no `{{READINESS_ROWS}}` in this template.
  Its narrowing: drop "one round, never re-rounded", say nothing BOUNDS generations, ground the
  override on the run closing units no audit names, and cite the prior art. That version is shorter
  than 384 B, so the byte budget stops being the binding constraint.
- **Refuted.** Stage 1's census: 3 flagged runs, which its own rule makes 2, against 25 builds on the
  binding line. "Bites once in 56 tracked runs". The chain length of 4, which is 5. The 620 tracked
  and 17 live specs, which are 641 and 24, and the 561 CLOSED, which is 575. "Nothing becomes false"
  and "NOTHING counts generations".
- **Owner, afterwards.** The owner replaced the row's "audited once" rule with a precision bound on
  2026-09-20, after this dry run and its skeptic (unit 4, sections 3 and 9, rev-1), and
  `TOOL-dGatedProse-4` writes it. The byte budget the edit spends is the question
  `TOOL-dLoggedFlight-35` records, and a ruling on it belongs to that row and to unit 4, not here.
- **On the merged tree**, at `bd44d3ff`: `memory/guides/BUILD-METHOD.md` is 27641 B and 352 lines
  against the same 27648 row. Of the three spans Arm C deleted, only the runaway-ceiling sentence is
  still present as Arm C spelled it. The dry run's arithmetic describes the file before the merge,
  and the spec audit's B1 is its re-derivation.

## What this record does not do

- **It re-runs nothing.** The figures are the journal's. The probes are untracked, so re-deriving a
  figure means re-implementing the predicate from the text above. Expect a different count: three
  faithful readings of strand 1 gave 1, 2 and 3 hits, strand 2 gave 16, 17 and 58, and strand 3 gave
  7 and 11.
- **It summarises the long lists.** Rule texts, carrier lists and the skeptics' what-breaks lists are
  condensed here, and every figure a summary keeps is the one the journal carries.
- **It spells as few code names as it can.** It sits under `memory/builds/`, and the round-1 audit's
  H4 found that unit 1's resolution corpus, as then specified, keeps build records in its content
  match, so any name spelled here would resolve by quotation alone. Hits are therefore cited by spec
  and item rather than by the tokens they flagged. H4's fix takes build records out of that corpus.
