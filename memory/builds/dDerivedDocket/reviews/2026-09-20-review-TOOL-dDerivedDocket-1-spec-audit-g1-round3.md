**Serves:** spec-audit TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28

# dDerivedDocket — spec audit of topic group G1, kit self-protection, round 3

*Node `d`, 2026-09-20. The third Tier-2 adversarial pass over the eight G1 specs: the suite
baseline, the in-place landing, the landing path, HELD, auto-resume, the derived terminal, the gate
wall and the process ledger. This is a FOLD review, regrounded on `fb07ca25`: origin/main moved 210
commits past the original BASE `abac6d59`, HEAD merges it in, and every spec re-verified its claims
there and moved its header base under a section 9 line reading `regrounded on fb07ca25`. Code claims
below are judged at HEAD. The pass was aimed at the text no reviewer has seen — every section 9 line
dated after the round-2 record — and at whether each round-2 fix holds. Four primed finder lenses ran
and all four returned; a skeptic stage prompted to REFUTE each finding ran in five batches and all
five returned; then this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief's roster and edge tables, and the round-2 record
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md`.
Sibling specs outside G1 were read wherever an edge or an interface named them. Every high below was
re-checked against source at HEAD before it was written down, and the sites read are named in each
entry.*

**Round: 3.** Range at base `fb07ca25`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-1.md@2a98d97ba6a2dc7f60cd7ce8b8b47baef5b798d3`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-2.md@e2efa8cd08e3fc904683d59e0c9d824054cca279`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-3.md@2a51b9b1b29a6486bf71fb6631069fe7a5b143c5`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-4.md@8452c5cae20b9391d35b988e916d43981a426d0f`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-5.md@ac1df79bc9b11091efb90924c22b3abe742a32af`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-22.md@7025ac83d65076ae2b0cade83db1cc823074d5ff`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-27.md@1195055bb0363966f591aadc216367e853812878`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-28.md@7c9316b3a1282ae2b703a9f12940c97bbabbd226`

## Verdict: CLEAN WITH FIXES

No blocker stands. Both round-2 blockers were in unit 22 section 2 S4 and S17; unit 22 carries no
confirmed finding at all this round, from a full four-lens fan, which is the strongest reading any
subject in this group has had. Round-2 H1, the handed-off criterion that read an aborted suite as
clean, holds in substance: unit 2 AC9 now carries the Red-when for exactly that reading. Its fix
brought its own smaller defect, entry M5 below.

Four HIGH defects stand, one finding id each. Two of them are internal contradictions a builder
cannot resolve from the spec: unit 4 ships a third conf key its own section 4 does not price and its
own AC23 does not witness, against a byte budget that provably does not close (H2), and six units
grade their carriers against half of a two-half cap on a guide with ten percent line headroom (H1).
One is a departure from a recorded owner ruling that no fork, no DECISIONS row and no citation
acknowledges (H3). One closes a backlog row on half its ask and leaves a budget whose stated basis
that row calls impossible under eleven consuming units (H4). There are also five MEDIUM defects
(six ids) and one LOW defect (three ids).

**Decision needed:** H3 asks whether `--close` is the boundary the 2026-08-27 owner ruling names.
The build cannot pick a side for the owner, and unit 3 currently picks one silently.

Convergence under `memory/guides/BUILD-METHOD.md` M4: the blocker count fell from 2 to 0 and the high
count moved from 1 defect (2 ids) to 4 defects (4 ids). By blockers the loop would end; by highs it
does not, and three of the four highs sit in text the 2026-09-20 closing pass wrote or left stale,
which is the fold class this build keeps reproducing. H1's fold crosses six specs at once, four of
them outside the pair that carries the entry, so it should be folded in one pass rather than per unit.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero here is
evidence and not an artefact of a missing lens — which the round-2 record could not say. Three
groups of ids describe one defect each on reading, 25 with 30, and 16 with 27 and 36, and they are
merged below; the pipeline's duplicate count of 0 comes from its own exact-match dedupe, which does
not see a restatement.

## Review shape

Raw 38, confirmed 13, refuted 25, unverified 0. Precision 0.34, which is below the ~0.5 floor
section 8 of the charter sets: a next round over this group should tighten lens priming or narrow
scope before it adds agents. The 25 refuted findings are not reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 4 | 4 |
| MEDIUM | 5 | 6 |
| LOW | 1 | 3 |
| Total | 10 | 13 |

## Round-2 fixes: what this round found against them

All four lenses returned, so "no confirmed finding" here means the fix survived a complete pass.

| Round 2 | Spec | Round-3 reading | Round-3 entries |
|---|---|---|---|
| B1 | 22 | holds; the scratch-copy derivation and the staged read survived | none |
| B2 | 22 | holds; S17's exclusion moved to unit 19's terminal function | none |
| H1 | 1, 2 | holds in substance; AC9's Red-when now names the aborted-suite reading | M5 |
| M1 | 4 | no confirmed finding | none |
| M2 to M9 | 4 | no confirmed finding | none |
| M10, M11 | 1 | no confirmed finding | none |
| M12 | 5 | holds; AC15's two-fixture form is the pattern H1 asks unit 4 to copy | none |
| M13 | 3 | no confirmed finding against the kit-roots half | none |
| L1 to L8 | various | no confirmed finding | none |

The fold that closed them introduced four of this round's ten items: M5 is the permission line the
H1 fold added, L1 is the section the 2026-09-20 closing pass rewrote in unit 5 without updating its
reuse audit, and H2 and H4 sit in scope text the regrounding consolidation extended.

## High

### H1 — six size criteria grade a two-half cap by its byte half only (13)

**Where.** Unit 4 section 6 AC23, and the same clause in unit 3 AC16, unit 5 AC16, unit 22 AC19,
unit 27 AC14 and unit 28 AC13.

Each criterion grades its carrier against "the 61440-byte guide cap declared in
`tools/memory-tree/check-memory-hygiene.sh`" and reads the byte size alone, with `git cat-file -s`.
That declaration has two halves and the gate enforces both.

**Verified at HEAD.** `tools/memory-tree/check-memory-hygiene.sh:84` reads
`GUIDE_CAP_BYTES=61440         ; GUIDE_CAP_LINES=750`, and check 6 reds at `:730` on
`b[f]+0>cb || (cl>0 && l[f]+0>cl)`. `memory/guides/UNATTENDED-PROTOCOL.md` is at 675 lines and
60324 bytes: 75 lines of headroom, and six units of this build edit it. A byte-neutral edit that
replaces one long paragraph with short rows or a fenced sequence is line-positive, passes every one
of the six criteria, and reds the `memory hygiene` leg at the bar. The new `UNATTENDED-STOPS.md`
that unit 4 creates and units 3, 5, 22 and 28 write into is worse: check 6's own header records the
81.92 B/line break-even, and a companion of tables and bullets crosses 750 lines long before it
crosses 61440 bytes, so five units can each pass their size criterion and still leave a guide that
reds.

That this is an oversight and not a declared scoping is settled inside the build: units 19, 20, 31,
34 and 36 all take the line reading, unit 31 AC10 reading `wc -c` and `wc -l` side by side and unit
34 asserting `wc -l < memory/guides/SESSION-KICKOFF.md` below 750. The cluster that shares this one
sentence is the cluster that lost the line half.

**Fix.** In each of the six criteria, read BOTH caps for each carrier: byte size NOT GREATER than
the parent's and below `GUIDE_CAP_BYTES`, and `wc -l` NOT GREATER than the parent's and below
`GUIDE_CAP_LINES`, each resolved from `tools/memory-tree/check-memory-hygiene.sh` rather than typed
as a literal. Add a `Red when:` arm for a byte-neutral, line-positive edit, and one for a companion
under the byte cap and over the line cap.

**Left-shift gate.** A spec-lint arm that reds when a criterion cites a `*_CAP_BYTES` constant
without also citing the `*_CAP_LINES` constant declared on the same source line. Run the predicate
over `memory/builds/*/spec/` first and print hits and near-misses: it should hit these six and miss
units 19, 20, 31, 34 and 36. The deeper form is the one the charter already states — the criterion
should resolve both numbers from the declaring source instead of restating either.

### H2 — unit 4 ships a third conf key that nothing prices and nothing witnesses (24)

**Where.** Unit 4 section 2 S2, section 4 "Where the text goes", section 6 AC23.

S2 introduces `HOLD_CODES_EXTRA` beside the closed hold-code set. Section 4 prices exactly two
section 8 key-table rows, `HOLD_FLOOR` and `LEASE_STALE_AFTER`, at most 239 bytes together, and
AC23 witnesses exactly those two arriving. The third key is in neither.

**Verified at HEAD.** The sibling S2 models the key on, `HALT_CODES_EXTRA`, is declared at
`tools/unattended/.unattended.conf.example:210` AND carries a section 8 row at
`tools/unattended/PROTOCOL.template.md:473`. Check 22 at `tools/unattended/check-unattended.sh:1694`
extracts the first-cell key names from section 8 and joins them against that example conf in BOTH
directions, `undocumented` and `phantom`, and against the adopting project's `.unattended.conf` in
one. So a `HOLD_CODES_EXTRA` line in the example with no row reds the leg as undocumented, a row
with no example line reds it as phantom, and gov declaring it in its own conf with no row reds
`proj_extra`. AC16 already requires the driver to accept a code declared in `HOLD_CODES_EXTRA`, and
`.unattended.conf.example` is in Files touched, so the key is read from a conf either way.

The arithmetic does not close either. Section 4 commits to 646 bytes trimmed against at most 624
added, leaving 22 bytes of headroom; a third row of the siblings' size is roughly 120, which reds
AC23's own "NOT GREATER than the parent's" arm. The only path that keeps both green is to declare
the key nowhere, and that reproduces the exact adopter failure the sibling `directives-floor` hole's
`why` field records: the adopter declares it, reds their own kit gate, and has no row to tell them
why. Nothing in the spec resolves the conflict, and no listed gate catches it in the spec's favour.

**Fix.** Name `HOLD_CODES_EXTRA` in section 4's priced set — three rows, or one joined first cell
carrying `HOLD_FLOOR` and `HOLD_CODES_EXTRA` as the `KEEPALIVE_CREATE · KEEPALIVE_DELETE` row
already does — add it to AC23's arrival witness, re-price the funding against the real figure, and
state whether it is declared in `.unattended.conf.example` and in gov's own conf.

**Left-shift gate.** A spec-lint join, printed as near-misses rather than red: every ALL-CAPS conf
key a spec's section 2 introduces must appear in that spec's section 4 pricing and in one criterion's
arrival witness. The mechanical half already exists at the tree level — check 22 is the bidirectional
join — so the spec-side arm is the same predicate one level up, which is the "gate the CLASS, not the
instance" rule applied to the spec corpus.

### H3 — `--close` sets a flag a recorded owner ruling forbids a boundary to set (28)

**Where.** Unit 3 section 2 S3, and section 4's `gates-green` table.

S3 has the driver export `GATE_SELFTESTS=1` automatically at `--close` whenever the landing range
touches a `SELFTESTS_OWED_PATHS` entry. `AGENTS.md:486` carries the ruling verbatim on the
command-fence line: `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh   # also run those. ON
DEMAND ONLY: no boundary sets it (owner, 2026-08-27)`. The spec never cites that sentence and never
supersedes it.

**Verified at HEAD.** `--close`'s bar IS the landing and push-boundary bar under D12-i1 — its stamp
is what the push reuses — and AC13 requires gov's `SELFTESTS_OWED_PATHS` to cover every kit root, so
in gov every kit-work landing has an automated boundary setting the flag. The spec quotes the
ADJACENT charter sentence, "Owed by a DoD only for KIT work", inside AC13's Red-when, which shows the
author read that fence and did not handle the line above it. Fork F1 in section 8 frames the question
as how the driver DERIVES the term, never as a departure; the design's U19 entry names neither.

The two charter sentences are themselves in tension — a DoD owes the flag for kit work, and no
boundary may set it — so this is a fork for the owner rather than a defect with one right answer.
Unit 3 currently resolves it silently, in the direction the ruling forbids. The build already knows
how to close this shape: RUN.md's parked decision chose "(iii) edit no carrier and let unit 24's
DECISIONS row record the departure", realised as unit 24 S13 and AC20.

**Fix.** Add a section 8 fork citing `AGENTS.md:486` and stating why `--close` is or is not the
boundary that ruling names. Then either declare a `memory/DECISIONS.md` row recording the departure
as an S-item, with `memory/DECISIONS.md` in Files touched and a criterion reading it back, as unit 4
S11 and unit 5 S12 do, or route the sentence to the carrier unit that owns it.

**Left-shift gate.** A documented check for the fold, not a red: for each charter or protocol
sentence a spec's S-items make false, the spec must carry either a fork citing that sentence's
`file:line` or an S-item minting the superseding record. Its mechanical half is a scan listing every
`(owner, <date>)` stamp in `AGENTS.md` and asking the folder which specs touch the behaviour each one
rules on — a near-miss report, since no predicate can decide the semantic half.

### H4 — a backlog row is closed on half its ask, under eleven consuming units (29)

**Where.** Unit 1 section 2 S7, against section 3 Non-goals.

S7 writes TOOL-aTracedSpawn-1 CLOSED citing commit `8b29f0b9`. That row's ask has two halves.

**Verified at HEAD.** `memory/backlog/TOOL.md:462` still reads OPEN and ends with a two-part ask:
quote the `$1`, AND re-read the suite's recorded seconds afterwards, "a run that aborts in seconds
cannot have produced a 2569 s reading". `8b29f0b9` fixed the abort only. Section 3 declares "Any
change to a budget row in `tools/run-gates/selftest-budgets.txt`" a non-goal, and nothing in the
spec re-measures. `tools/run-gates/selftest-budgets.txt:114` still reads `unattended driver selftest
3860 ... measured 2569s on node a 2026-09-07`, so a suite that now runs to completion is budgeted
from a reading the closed record itself calls impossible.

The blast radius is what lifts this above bookkeeping. S5 and S10 make "no OVER BUDGET at L" a term
of the `verdict clean` token, and eleven consuming units read that token as their final criterion. A
budget breach then reds all eleven for a cause this unit declared out of scope, with the row that
would have explained it marked CLOSED. The unit's own handling of the sibling row shows the correct
treatment was available and not applied: TOOL-aHoistedPass-36 is kept OPEN for its stop (2).

**Fix.** Either keep TOOL-aTracedSpawn-1 OPEN for its seconds half, exactly as S7 already does for
TOOL-aHoistedPass-36, or add the re-read to S7 with the budget row in Files touched and drop it from
section 3's non-goals. Closing it on the abort alone is the one option the row's own text refuses.

**Left-shift gate.** A ratchet over the spec corpus: a spec S-item that writes a backlog id CLOSED
must cite every sentence of that row's ask, and the leg reds when the row in `memory/backlog/` is
still OPEN at the build commit with no matching status edit in the same commit. Stage the RED by
closing a two-part row on one part. This also catches the narrower live instance — a spec closing a
row the backlog has not been told about.

## Medium

### M1 — unit 27's two section 8 trims take rules, not rationale (25, 30)

**Where.** Unit 27 section 4, the paragraph naming the two trims, and section 6 AC14. Two lenses
reported this independently; it is one defect.

**Verified at HEAD.** `tools/unattended/PROTOCOL.template.md:459`'s tail from `OPTIONAL, on` is
exactly 119 bytes and is the ENTIRE optionality statement of the `UNIT_STALL_BOUND` cell:
absent-takes-the-kit-default-and-says-so, and the non-numeric-or-zero refusal, including the pointer
at `GATE_BOUND`'s terms. The spec's own rationale for the trim is that the cell "has just pointed
at" the sibling row — but the pointer is inside the trimmed span, so the rationale falsifies itself.
`:460`'s clause opening ", and so is a value at or above the runaway ceiling" is the protocol's only
statement of a refusal the driver actually makes at conf load, `tools/unattended/unattended.sh:533`
exiting 2 against `RUNAWAY_CEILING`.

After the trims the shipped table tells an adopter that `REVIEW_ROUNDS` refuses only a non-numeric
or zero value while the driver refuses a third case, and says nothing at all about
`UNIT_STALL_BOUND` being optional or what an absent or malformed value does. Nothing catches it:
check 22 extracts backticked ALL-CAPS tokens from the first cell only, and its own header says it
does not check that a row describes its key correctly. AC14 witnesses only that the two phrases
vanish and reappear in `tools/unattended/README.md`. The build has the missing arm elsewhere — unit
22's AC19 Red-when, and unit 5's AC16, which asserts the `RECALL_CLI` and `MAP_CLI` cells "still
state their meaning and their OPTIONAL terms".

**Fix.** Narrow both trims to the reason clauses: keep `OPTIONAL, on GATE_BOUND's terms` and keep
the at-or-above-ceiling refusal, trimming only the `because the ceiling would fire first` half and
the pointer's prose. Re-price the funding against the smaller figures, and give AC14 unit 22's arm —
red when a trim removes a rule rather than its argument.

**Left-shift gate.** Extend check 22 with a second, advisory pass that diffs a trimmed section 8
cell against its parent and prints a near-miss when the removed span contains `OPTIONAL`, `refusal`,
`refuses`, `is a refusal` or `exits`. Rule text and rationale are not mechanically separable, so
this is a near-miss report for the folder rather than a red.

### M2 — unit 4's `hold-floor` kit.toml hole is claimed observed by five criteria that never read it (4)

**Where.** Unit 4 section 2 S2, last sentence.

S2 lists the `tools/unattended/kit.toml` `hold-floor` hole and its discharge probe among AC1, AC2,
AC9, AC11 and AC16. Reading all five, and grepping the whole of section 6: none reads `kit.toml`,
none contains `hole`, and none runs a discharge command. The only section 6 hits for those terms are
`HOLD_FLOOR` inside AC9's driver-copy arm and AC23's protocol key-table grep. The claim is false.

The build's own convention makes the omission load-bearing rather than cosmetic: S11 in the same
section writes "NOT OBSERVED by a criterion" when nothing observes an item, so silence here reads as
coverage. The consequence is the one the sibling `directives-floor` hole's `why` field records
verbatim — a hole that is never added reds nothing in gov, because gov's conf declares the key and
the kit gate passes, and the failure surfaces only in an adopter, who reds their own unattended kit
gate with no key and no hole to tell them why.

**Fix.** Add a criterion in the shape of unit 5 AC15: run the `hold-floor` hole's discharge command
from `tools/unattended/kit.toml` over a fixture conf that omits `HOLD_FLOOR` and assert non-zero,
and over one that declares it and assert 0, staged RED against the current `kit.toml`, which carries
no such hole.

**Left-shift gate.** The join named under H2, in its second direction: every `kit.toml` hole an
S-item promises must be named by at least one criterion that runs its discharge command. Print hits
and near-misses over `memory/builds/*/spec/` before wiring, since the corpus has both forms and the
passing form is unit 5 AC15.

### M3 — unit 27's blank-profile path, the state every adopter starts in, is unobserved (6)

**Where.** Unit 27 section 2 S2 ("Observed by AC1") and section 2 S6 ("Observed by AC4 and AC5").

Both claim the blank-`GATE_PROFILE_CMD` arm is observed. AC1 gives `gates-green` a stub gate that
ANSWERS the profile with `wall 5` and `queue 20`; AC4 grades a fixture conf whose `GATE_WALL` sits
below the profile's `ceiling_max`, profile present; AC5 runs the leg over the real tree, where S8
has gov declaring the key. Grepping section 6 for the key returns only AC12's blank-`GATE_WALL` arm
and AC14's protocol grep. No criterion runs with the profile key blank.

That is the day-one state of every adopter. S2's fallback — the bar stays bounded by `GATE_BOUND`,
announced — and S6's "announce that it cannot compare" are the arms they meet first, and a build
that instead refuses at conf load, computes a backstop from an empty profile, or silently bounds the
bar at 0 passes every criterion here. Section 5's error-states row adds a third unobserved arm: a
profile that prints no `queue` or no `wall` falling back and naming the missing key. None of the
three New arm lines stages it — they stage a queueing, hanging, exit-3 and exit-4 stub, a
wall-below-ceiling conf, and a profile print. AC12 proves the spec knows how to observe a blank key,
which makes this an oversight rather than a scoping.

**Fix.** Add an arm to AC1 or a new criterion: with `GATE_PROFILE_CMD` blank, `gates-green` bounds
the stub gate at `GATE_BOUND` and announces the missing profile, `--preflight` pins no
`gate-backstop` fact, and `bash tools/unattended/check-unattended.sh` over that fixture conf
announces that it cannot compare the wall with `ceiling_max` instead of redding. Add the missing-key
arm for a profile printing neither `queue` nor `wall`.

**Left-shift gate.** The skip test, run on the fold by the folder, in its OPTIONAL-key form: for
every conf key a spec declares optional, name the criterion that runs with it absent or blank. Its
mechanical half is a scan counting optional keys in section 2 against blank-value arms in section 6
and printing the difference as near-misses.

### M4 — unit 3 retires a ratified premise from three carriers and leaves the log (33)

**Where.** Unit 3 section 2 S5, and section 10's first bullet.

S5 retires the "no verb here commits" premise from the protocol at
`tools/unattended/PROTOCOL.template.md:157`, the driver comment at `tools/unattended/unattended.sh:1680-1681`
and the test comment at `tools/unattended/unattended.test.sh:2483-2484` — all three citations check
out. Section 10 declares TOOL-dClosedLexicon-11's DECISIONS clause "superseded for in-place". The
log row is a fourth carrier and is untouched: `memory/DECISIONS.md:81` still ratifies "the archive
name derives from the record's BYTES, because no verb here commits", which gov's own mode falsifies
once `--close` commits.

No S-item claims a superseding row, `memory/DECISIONS.md` is not among the ten Files touched, AC14
greps only the protocol and the two code comments, and none of section 8's five forks raises it. No
non-goal withholds it. The charter's section 6 rule is to supersede a ratified record with a new id
and a note in the log; the note here lives in a build spec, so a session following the section 6
session-start reading order reads the stale premise and finds nothing pointing away from it. The
same build files such a row twice for this exact shape, in unit 4 S11 and unit 5 S12, so the
omission is inconsistent inside its own group, and `memory/guides/BUILD-METHOD.md` derives the
wrap-up from the rows a build mints — this unit mints none.

**Fix.** Add an S-item minting a `memory/DECISIONS.md` row under this unit's id that supersedes
TOOL-dClosedLexicon-11's clause for `in-place`, list `memory/DECISIONS.md` in Files touched, and
have AC14 or a new criterion read that row back, as unit 4's AC and unit 5's AC12 do.

**Left-shift gate.** A ratchet over the spec corpus: when a spec's section 10 or section 2 says a
`memory/DECISIONS.md` id is superseded, obsolete or overridden, that spec must list
`memory/DECISIONS.md` in Files touched and carry a criterion naming the row. Stage the RED by
removing the file from a passing spec's Files touched. The predicate is a grep for a DECISIONS id
against the Files-touched block, so it runs in milliseconds and has no semantic half.

### M5 — unit 2 AC9's permission line names a run that cannot make AC9's second observation (31)

**Where.** Unit 2 section 6 AC9, the `permission:` line.

AC9 asks for two observations: the arms for AC1 to AC8 and AC10 to AC13 passing under the flagged
bar, AND `run-selftests.sh --attribute` against BASE reading `verdict clean`. The permission line
names only `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` "and nothing earlier",
a run that never invokes `--attribute`.

**Verified at HEAD.** `tools/unattended/gate-guard.js:389` denies a token matching
`/run-selftests\.sh$/` as row D2, and `:101` exempts only
`READ_ONLY_VERBS = ['--list', '--check', '--rank', '--help', '--render']`. `--attribute` is not
among them, so the attributed half is denied during the pass and no run is named that makes it
afterwards. The criterion cannot be observed as written.

This is the round-2 H1 fold's own residue. The closing verifier fixed exactly this gap in units 3,
4, 5, 22, 27 and 28 by naming the attributed `run-unattended-gates.sh --attribute <BASE>` run beside
the VERIFYING bar; unit 2, the one spec the 2026-09-16 consolidation left behind, was re-touched on
the closing pass and did not get it. Its section 9 entry records the permission line as the whole of
that edit.

**Fix.** Extend AC9's `permission:` line to name both runs: the flagged bar for the arms, and the
VERIFYING run's attributed `bash tools/run-gates/run-selftests.sh --attribute <BASE>` over the
`push-main self-test` suite for the `verdict clean` reading.

**Left-shift gate.** A spec-lint arm, red rather than advisory because it is purely mechanical:
every command a criterion requires must be covered by that criterion's `permission:` line, and any
command whose head word `tools/unattended/gate-guard.js` denies must appear there with the verb it
carries. Stage the RED against unit 2 as it stands. The stronger form asks the guard itself —
resolve each criterion's commands through `gate-guard.js` rather than re-implementing its rows,
which is how the bar's own agent-cap leg delegates.

## Low

### L1 — unit 5's reuse audit contradicts the scope item it describes (16, 27, 36)

**Where.** Unit 5 section 10, second paragraph, against section 2 S10. Three lenses reported this
sentence; it is one defect.

Section 10 still reads that the check 22 key-table row for S1's five keys is "a row S10 does not yet
name", and that S10's sentence and that row "spend from" the 1,116 bytes of shared headroom. The
2026-09-20 closing pass made both false. S10 now names the row in terms — "ONE key-table row
carrying this unit's five conf keys joined in a single first cell" — declares it "OWED and not
optional" citing check 22, prices it inside the same 300-byte GROSS ceiling, funds it with the named
509 bytes trimmed from the `RECALL_CLI` and `MAP_CLI` cells at
`tools/unattended/PROTOCOL.template.md:482-483`, and states that the unit "lands NET ZERO OR
NEGATIVE on that carrier and spends none of the shared headroom". AC16 witnesses the row arriving,
with `grep -c 'RESUME_SCHEDULE'` moving 0 to 1, and reds if five separate rows are written instead
of the one joined cell. The spec's own revision log records the closing-pass edit that made section
10 stale.

No reconciling reading survives, and the two accounts of the shared headroom cannot both be right.
Section 10 is the section a later session reads to learn what the regrounding found, so a reader who
starts there concludes the row is unnamed, unfunded and optional and may leave it out — which reds
check 22 on the next bar, the failure S10 and AC16 were rewritten to prevent. Low, because two of
the three places say the right thing and AC16 grades the build.

**Fix.** Rewrite that clause to say S10 names and funds the joined row inside its 300-byte ceiling,
that AC16 witnesses it, and that the unit leaves the 1,116 shared bytes intact. Keep the
`tools/unattended/check-unattended.sh:1689` citation as the provenance of the requirement, and drop
the "spends from it" claim for both S10's sentence and the row.

**Left-shift gate.** No mechanical gate fits — this is prose against prose. It belongs on the fold
checklist as the sweep the closing pass owes: when a pass rewrites an S-item, re-read every other
section that names the same artefact before the pass closes. The nearest mechanical proxy is an
advisory scan for hedges like "does not yet", "not yet named" or "still unpriced" in a section 10
whose section 2 names the same artefact, printed as near-misses.

## Left-shift, by class

1. **A criterion grades one half of a two-half declaration** (H1). The class round 2 called
   "green by absence", now in its constant-citation form. The gate: a criterion citing a declared
   constant must cite every constant declared on that source line, and should resolve the value
   rather than restate it. Live hits: six specs.
2. **An S-item's promise is not carried into pricing or into a criterion** (H2, M2, M3). One join,
   run over the spec corpus in both directions: every conf key, `kit.toml` hole and optional-key
   fallback a section 2 introduces appears in the section 4 pricing and in one criterion's witness.
   Print hits and near-misses; the corpus already contains the passing forms, unit 5 AC15 and
   unit 22 AC19, so the predicate can be calibrated before it is wired.
3. **A record outside the spec is declared retired without being edited** (H3, H4, M4). Three
   different carriers — a charter ruling, a backlog row, a DECISIONS row — and one rule: a spec that
   makes an external record false must either edit it, with the file in Files touched and a criterion
   reading it back, or carry a fork citing its `file:line`. Mechanical for the backlog and DECISIONS
   halves, a fold checklist item for the charter half.
4. **A trim or a rewrite takes a rule along with its reason** (M1). Advisory diff over section 8
   cells, flagging a removed span that carries `OPTIONAL`, `refusal` or `exits`. Unit 22's AC19
   Red-when is the criterion-level form and should be copied into every spec that trims a cell.
5. **A closing pass fixes one section and leaves its neighbours** (M5, L1). The fold class this
   build has now reproduced in three consecutive rounds: round 1 fixed `--carry` and left
   `--prepared`, round 2's fold left the lease symptom one row down, and the 2026-09-20 closing pass
   left unit 2's permission line and unit 5's reuse audit behind its own edits. The check runs on
   the FOLD, by the folder: when a pass edits an S-item or adds a permission line, list the set's
   other members and give each one the same edit or a reason.

## What this round did not cover

- **The 25 refuted findings**, which are not reproduced here. They were refuted, not lost, as the
  run-integrity counters show.
- **Units outside G1**, read only where an edge or an interface named them. M4 names unit 24 (G4)
  as the precedent for its DECISIONS row and H3 names it again; those groups' own audits should
  confirm the row exists there. Nothing here clears units 6 to 21, 23 to 26 or 29 to 36,
  PLAY-dDerivedDocket-1 or DEPL-dDerivedDocket-1.
- **The design record's measured figures**, which were not independently re-derived. The 29400 s
  backstop is taken as unit 27 and round 1 computed it.
- **The 210 commits the regrounding absorbed**, beyond the specific line citations each finding
  above re-read at HEAD. Each spec's section 9 asserts its own claims were re-verified at
  `fb07ca25`; this round tested that assertion only where a finding reached it, and H4 is one place
  it did not hold — `memory/backlog/TOOL.md:462` still reads OPEN.
- **Precision was 0.34**, below the charter's floor, so the lens fan was noisier than it should have
  been. That is a property of this round rather than of the subjects, and a fourth round over the
  same specs should re-prime or narrow before it re-runs.
