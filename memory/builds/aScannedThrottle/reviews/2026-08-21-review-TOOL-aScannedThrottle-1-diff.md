**Serves:** diff-review TOOL-aScannedThrottle-1

# Diff review — `49aea26a704537a8299da825b72796bef5953262...HEAD`, ROUND 1

Reviewed range `49aea26a704537a8299da825b72796bef5953262...HEAD` — two commits, `51486db` (the M4
spec audit) and `2861ea9` (the S5 reconciliation fold), 405 insertions across eight files, all under
`memory/`. **Verdict: CLEAN WITH FIXES — no blockers.** Nothing in this diff touches executable
code, so nothing here can break a gate or a runtime; every finding is a durable-record defect, and
the records are the deliverable this build ships.

**Review shape.** Raw 30 · confirmed 23 · refuted 7 · unverified 0 · precision 0.77. Every confirmed
finding was re-opened against the tree at HEAD and re-derived from the bytes; the counts above are
finding counts, and the 23 confirmed findings consolidate to **15 distinct defects** because seven
of them were filed against more than one carrier of the same number. Each defect below names the
finding ids it absorbs.

**Severity split of the 15 defects:** 0 blockers · 3 high · 6 medium · 6 low.

**What this review did NOT check.** It did not re-run the bar, so no measurement in the report was
independently reproduced — only the report's internal arithmetic and its agreement with the tree.
It did not audit the 262-line spec-audit record that `51486db` added, except where this diff's own
claims cite it. It did not evaluate whether the seven minted `TOOL-aScannedThrottle-*` rows are the
right rows; scope was the diff.

**One shape produced two thirds of the confirmed findings.** A figure was measured once, written
into three or four carriers, then corrected in some of them. The correction commit is itself the
largest instance: it establishes that the 16:05 run has no recoverable floor, and then counts that
run in a four-bar floor range three times. Nine of the fifteen defects below are that shape, which
is why the left-shift suggestions converge on two gates rather than fifteen.

---

## Blockers

**None.** No finding in this round blocks the landing. The three highs below are recorded-fact
defects in a build whose deliverable IS its records, so they are worth fixing before the unit
closes, but none of them makes the merge unsafe.

---

## High

### H1 — the §2 correction closes AC1 on a premise its own table refutes
*(finding ids 1, 19)*

**Site:** `memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:48-49`

The correction added by this diff reads: *"Throughput is likewise unrecoverable for every row,
because leg-seconds ÷ span needs the span this table lacked."* Three of the four rows in the table
twelve lines above carry BOTH operands:

| run | leg-seconds | span | leg-s ÷ span | util × width |
|---|---|---|---|---|
| 14:44 | 4644 | 970.0 s | 4.79 | 59.8 % × 8 = 4.78 |
| 15:07 | 5144 | 925.5 s | 5.56 | 69.5 % × 8 = 5.56 |
| 15:38 | 5245 | 1051.4 s | 4.99 | 62.4 % × 8 = 4.99 |
| 16:05 | — | 1058.3 s | — | — |

It is not even a division away: throughput is utilization × width, and utilization is already a
column — so the arithmetic was demonstrably already done. The stated reason is also backwards for
the one genuinely incomplete row, because 16:05 is the row that HAS a span (recovered two sentences
earlier at `:45-46`) and lacks leg-seconds.

This matters beyond tidiness. The spec's rev-2 entry at
`memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:145-148` cites this
sentence as the reason AC1's throughput criterion is withdrawn rather than met. An acceptance
criterion is therefore recorded as honestly-unmeetable when 75 % of it is one column of arithmetic
the table already contains. The same paragraph also calls the 16:05 row's remaining cells
UNRECOVERABLE while its verdict is recoverable from the report's own §3.5 table at `:230-233`,
which lists that run at head `e6098aa43` with failed legs "none".

**Fix.** Add the throughput column and fill it for the three complete rows — 4.79 / 5.56 / 4.99
leg-s/s, or 580.5 / 643.0 / 655.6 s under §3.2's `leg-seconds ÷ 8` reading; pick one and say which.
Fill the 16:05 verdict cell as GREEN citing §3.5. Narrow `:48-49` to what is actually gone:
*"throughput, floor, utilization and packing are unrecoverable for the 16:05 row alone, because its
per-leg records are gone."* Then correct the spec's rev-2 §6 self-grade to say AC1 is met for three
of four runs, not that it is uncorrectable.

**Left-shift gate.** A `record-table-claims` leg over `memory/builds/*/build/*.md`: for every
markdown table, count the filled cells per column, then scan the same file for a sentence asserting
a population over that column (`every row`, `for every run`, `across four bars`). Red when the
asserted population exceeds the filled-cell count, and red when a column the record's own acceptance
criteria name is absent entirely. Its header must state what it does not check: it compares stated
population against filled cells, never whether any value is correct.

### H2 — the new closing condition's clause (1) evaluates the authored table, not S5's derived predicate
*(finding id 2)*

**Site:** `memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:125-126`

S5 at `spec:23-26` declares the population **DERIVED, not authored**: every row in
`memory/backlog/TOOL.md` whose status token is `OPEN` and whose text names the bar's wall clock,
leg timings, pool width, dispatch order, spawn cost or scratch cost. The closing condition written
a hundred lines below evaluates something else — *"Every id in the report's §5 and §5.1"* — which is
an authored list of twelve rows at `build:505-512` and `build:528-531`.

No clause can therefore detect a row that satisfies the predicate and the report omitted. The unit
can satisfy all three clauses and CLOSE with S5 unmet. That is precisely the defect F4 was written
to kill — an omission indistinguishable from a judgement call — reinstated one level up, inside the
mechanism that was supposed to retire it.

**Fix.** Restate clause (1) as the predicate rather than the table: *"every OPEN row in
`memory/backlog/TOOL.md` matching S5's predicate carries a dated disposition line citing the report
section that measured it."* The concrete row that already escapes it is H3.

**Left-shift gate.** Make the predicate executable. A `spec-population` leg that reads a spec's
DERIVED-population declaration from a machine-readable block in the spec, evaluates it against the
named file, and asserts every selected id carries a disposition naming the spec's unit id. That
turns S5 from a sentence into a check and closes H2 and H3 with one mechanism. Where a spec declares
no such block, the leg must print a named refusal rather than passing green.

### H3 — S5's predicate selects an OPEN row the build never engaged: `TOOL-aBoundedVerdict-10`
*(finding id 17)*

**Site:** `memory/backlog/TOOL.md:104`, uncovered by
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:521` (§5.1's
completeness claim)

`memory/backlog/TOOL.md:104` is `· OPEN ·` and reads: *"`unattended driver selftest` HANGS on node
`a` inside its first `--preflight` (traced), zero output at 240s. It wedges the WHOLE bar at 46/65:
`run-gates.sh` has no per-leg deadline."* That names leg timings and the bar's wall clock directly,
on the exact leg §2 records as the floor. A recursive grep for `aBoundedVerdict-10` across
`memory/builds/aScannedThrottle/` returns nothing — not the spec, not the report, not the audit
record, not `RUN.md`.

The omission is material, not cosmetic. The floor leg completed in every bar this build
reconstructed, at 812.1 / 925.5 / 887.9 s, so the row's HANGS claim is either intermittent or gone —
a real answer the reconciliation had in hand and did not write down. `TOOL-aTetheredScratch-3` at
`memory/backlog/TOOL.md:77` is a second candidate on the "scratch cost" arm and needs adjudicating
in or out, in writing.

**Fix.** Add a `TOOL-aBoundedVerdict-10` row to report §5.1 carrying the four-bar evidence for that
leg, apply the dated disposition to `memory/backlog/TOOL.md:104`, adjudicate
`TOOL-aTetheredScratch-3` explicitly, and re-run the predicate over the whole file before claiming
the set is complete.

**Left-shift gate.** The `spec-population` leg from H2 catches this by construction. Until it
exists, the manual check is one command: grep `memory/backlog/TOOL.md` for OPEN rows matching the
six predicate terms, and diff that id set against the report's §5 and §5.1 tables.

---

## Medium

### M1 — "four GATE_FULL bars measure 812-926s" counts a bar whose floor the same commit calls unrecoverable
*(finding ids 3, 13, 23)*

**Sites:** `memory/backlog/TOOL.md:47` · `memory/backlog/TOOL.md:49` ·
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:529`

Report §2's floor column holds exactly three values — 812.1, 925.5, 887.9 — and the 16:05 row's
floor cell is an em dash, marked UNRECOVERABLE by the correction this same commit added at
`build:42-47`. Yet three sentences written by this commit attribute the range to four bars:

- `TOOL.md:47` (`TOOL-aTimedTurnstile-1`, now **CLOSED**) — *"the current floor, which four
  GATE_FULL bars measure at 812-926s"*
- `TOOL.md:49` (`TOOL-aTimedTurnstile-3`) — *"the floor is 812-926s across four bars"*
- `build:529` — the same phrase in §5.1's table cell

The quoted range is precisely min/max of the three. A row was closed as "FALSE at HEAD" on a sample
size the citing commit simultaneously records as three, and the population size is what makes the
range look stable to whoever prices sharding next. The 16:05 span is 1058.3 s and every measured run
has floor/span between 0.84 and 1.00, so that run's floor could plausibly sit above 926 s — the
overclaim is not merely unsupported, it may be wrong.

**Fix.** Write *"812-926 s across the three bars whose floor is recoverable (§2)"* at all three
sites. The span range 925-1058 s is fine at four, because §2 recovers that one number
arithmetically; the floor is not.

**Left-shift gate.** The `record-table-claims` leg from H1, extended to `memory/backlog/*.md`: a
backlog row citing a build report's figure together with a population size (`across N bars`) is
checked against that report's filled-cell count for the column it names.

### M2 — "each self-test leg now carries a `guard` in the manifest" is false at HEAD
*(finding ids 10, 25)*

**Site:** `memory/backlog/TOOL.md:48` (`TOOL-aTimedTurnstile-2`, marked STALE by this diff)

Derived from `tools/gate-legs.json` at HEAD: 88 legs, 53 carrying a `guard` key and 52 a truthy one
(`run-gates wiring` carries an empty array). Of the 39 legs whose own name says self-test or
selftest, five carry no guard key at all:

- `template size gate selftest`
- `method-carriers self-test`
- `agent-cap restatement self-test`
- `testsuite counts self-test`
- `testsuite counts (every bar self-test prints one)`

The last is a declarations-chunk leg whose name merely contains the phrase, so four are true
unguarded self-tests. The row is the one a session greps before acting on guard coverage, and it now
says the coverage is complete — which also pre-empts `TOOL-aPacedTurnstile-9`, whose whole subject
is proving a guard population complete. `AGENTS.md` carries the same universal, so this is a class
with two carriers rather than one line.

This is exactly the shape AGENTS.md §7 bans: a count of a derived population written in prose beside
the manifest that owns it.

**Fix.** Replace the universal with a pointer, not a fresher number: *"the guard mechanism it asks
for LANDED; derive the split from `tools/gate-legs.json` — a handful of self-tests still carry
none."* Naming the four legs is fine; restating the 52/88 split in prose recreates the defect one
commit later.

**Left-shift gate.** A `manifest-claims` leg holding a closed set of phrases about `gate-legs.json`
(`each self-test leg`, `every leg`, `N of M legs`, `only leg N has a guard`) and re-deriving each
from the manifest, over tracked prose in `AGENTS.md`, `memory/backlog/*.md` and
`memory/builds/**/*.md`. Its header must state that it checks only the enumerated phrases, so an
unenumerated wording passes silently.

### M3 — `TOOL-aPacedTurnstile-8`'s disposition claims a state the file cannot represent, and leaves the refuted number standing
*(finding ids 5, 24)*

**Site:** `memory/backlog/TOOL.md:123`

Two problems in one row, both introduced by this diff's one-line in-place edit (hunk
`@@ -120,7 +120,7 @@`).

**"RAISED TO TOP" is unexhibited.** The row did not move — it sits at line 123 of 150 — and the
shard declares no rank, priority or order field. `memory/backlog/TOOL.md:3` declares only a status
token per row, the hygiene backlog checks cover entry budget and status vocabulary with no order
field, and file order is append-at-bottom by slug, so this build's own rows are last. A repo-wide
grep finds `RAISED TO TOP` only in this row and the report line that prescribed it: a corpus hapax
with no evaluable predicate, which is the exact class rev-2 invoked three paragraphs earlier to kill
"dispositioned" at `spec:117-120`.

**The superseded figures were never retracted.** The row still asserts *"the bar's floor is ~660s at
any width on any hardware"*, *"75.6% of the 873s wall"* and *"the remaining 213s"* (= 873 − 660),
while `:47` and `:49` in the same file and the same diff assert 812-926 s, and `:13` calls the same
873 s figure 14.7 % low against a measured 1001.3 s mean. One backlog file now carries two
incompatible floors. Report `:505`'s instruction was *"Re-stamp to the crossover target of ~766 s
rather than to a floor number"*; the appended clause added the crossover and left the number it was
meant to replace. Every other disposition in this diff names the figure that no longer holds —
`aTimedTurnstile-3`'s even ends *"Correct the floor figure, or the row argues from a number 11x
low"*. The same defect, handled two ways in one commit.

**Fix.** Replace `RAISED TO TOP` with a claim the file can carry — *"HIGHEST-VALUE OPEN ROW per
`TOOL-aScannedThrottle-1` §4 R2"* — since the ranking lives in the report, not here. And append the
retraction: *"the row's ~660s floor and its 873s / 213s derivations are SUPERSEDED — measured floor
is 812-926s and measured mean wall 1001.3s (§2, §5)."*

**Left-shift gate.** Extend the hygiene backlog check that already gates the seven-token status
vocabulary with a second closed set: the ALL-CAPS disposition verbs a row may carry (`CLOSED`,
`REFINED`, `STALE`, `RE-CITED`, `RE-MEASURED`, `CONFIRMED`, `KEPT OPEN`, `SUPERSEDED`). An
unrecognised one like `RAISED TO TOP` reds and has to be argued into the set. Cheap, and it is the
same mechanism check 8 already runs one column over.

### M4 — the parked owner decision rests on a misstatement of the waiver registry's contents
*(finding id 6)*

**Sites:** `memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:140` and
the verbatim duplicate at `memory/builds/aScannedThrottle/RUN.md:24`

Both read *"All six existing rows are the OTHER shape (product landed before the id-in-subject
convention)."* `memory/project/trace-waiver.txt` refutes it twice over:

- Its own header at `:20` still says *"All five seed rows are the SAME shape"* — the header count
  and the data-row count already disagree at HEAD.
- Row `:31` (`TOOL-dSettledRoster-5`) landed `474043e` / `d2a40aa` on 2026-08-20, **after**
  `TRACE_CUTOFF = '2026-08-11'` (`tools/drift-audit/drift_signals.py:52`), and its stated reason is
  that the record was written after the work at owner request — not a pre-convention subject.
- Row `:30` (`TOOL-aWireWarden-1`) reads *"it DOES name TOOL-aWireWarden-1, in the BODY"* — a
  subject-scope waiver, a third shape.

`RUN.md:24` is the parked-decision record the owner reads to make a gate-exemption call on this
exact shrink-only registry, so the wrong contents are the input to that decision.

**Fix.** Correct both copies to: *"five of the six rows are pre-cutoff subjects
(`trace-waiver.txt:20-29`); the sixth, `TOOL-dSettledRoster-5`, is a record-after-the-fact waiver,
and `TOOL-aWireWarden-1` is a subject-scope one — none of the six is records-only, so this would be
the first."* The load-bearing conclusion survives intact; only the premise moves.

**Left-shift gate.** Two, both cheap. (1) A `waiver-header-count` check: the header of every
`memory/project/*.txt` registry that states a row count must match its actual data-row count — that
single assertion catches the five/six drift at its source. (2) Forbid the duplication: `RUN.md`'s
parked-decision line should cite the spec section rather than copy its sentence, and a
`duplicate-prose` check over a build folder can red on any sentence of 15 or more words appearing in
two tracked records.

### M5 — rev-2 cites review counts the linked record does not carry
*(finding id 12)*

**Site:** `memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:115`

The line reads *"verdict CLEAN WITH FIXES, 38 confirmed of 46"*, one line below a link to
`reviews/2026-08-21-review-TOOL-aScannedThrottle-1.md`. That record carries exactly 13 `### F`
headings, F1 through F13, and states at `:10` that *"8 of the raised findings were refuted"*, i.e.
21 raised. Grepping the record for the numerals 38 and 46 returns nothing, and no 46-item population
exists anywhere in it — its scope table at `:231-236` holds five rows, S1 through S5. The pair is
not a rounding of the earlier lens pass either, which reads 55 findings and 28 survived at
`review:166`. The string "38 confirmed" does appear in a different build's review record,
`memory/builds/aRelaxedShard/reviews/2026-08-17-review-TOOL-aRelaxedShard-1.md:10`, which is the
likeliest carry-over.

A reader who follows the link one line above cannot reconcile either number, so the only check a
later session can run against the citation fails.

**Fix.** State the counts the record supports — *"13 confirmed, 8 refuted"* — or add the
pre-consolidation raised and confirmed totals to the record's own Lenses-run section, so the spec's
figures have a source to be re-derived from.

**Left-shift gate.** A `citation-figures` leg: where a markdown link to a tracked in-repo file is
followed within three lines by a numeral pair of the shape `<n> confirmed of <n>`, grep the linked
file for both numerals and red on a miss. Narrow, mechanical, and it is the second instance of this
class in two rounds.

### M6 — `TOOL-aMeteredTurnstile-3`'s orphan sizing does not reproduce, and the row carries two inflation figures
*(finding id 27)*

**Site:** `memory/backlog/TOOL.md:12`

The new text asserts in the present tense: *"The 964.2s of orphan rows sits in the dead
`gate-timings.tsv`."* A machine-wide search finds exactly one `gate-timings.tsv`, at
`C:/projects/coding-governance/.git/gate-timings.tsv`: 73 rows, 1299.44 s total, last written
2026-08-18 03:25, whose three orphan rows are `memory hygiene (20 checks)` at 7.846 s,
`marker contract (4 readers)` at 5.234 s and `verifier fan-out` at 0.650 s — **13.7 s**, not the
813.0 + 131.3 + 19.9 = 964.2 s the row asserts. No worktree holds a legacy file; 6 worktrees remain
on node `a` and none carries one, so the nine-worktree, 88-row population the report measured is
unreachable at HEAD. The worktree cleanup landed at `b927a92` / `49aea26` on 2026-08-20 at 23:30,
which is this run's pinned BASE, and the row was rewritten at `2861ea9` on 2026-08-21 — stale on
write, not merely aged.

Separately the row now carries two inflation figures for the same three orphans: its surviving text
says *"= 12% inflation on any sum"* against `build:151`'s *"inflates any sum taken from it by 23 %"*,
and the disposition restates the 964.2 s without reconciling either.

The row's conclusion survives — it also says *"nothing is currently inflated by it"* — so the harm
is a sizing figure wrong by roughly 70×, not a wrong decision.

**Fix.** Date-stamp the reading instead of restating it: *"…the orphan rows sit in the dead
`gate-timings.tsv`; measured 2026-08-20 at 964.2s across the then-live per-worktree copies, and
13.7s in the common-dir copy that survives at HEAD."* Drop or correct the surviving "12% inflation"
so one figure stands.

**Left-shift gate.** A `present-tense-census` check over `memory/backlog/*.md`: a row asserting a
count of a filesystem population (`N dirs`, `N of M worktrees`, `N rows`) must carry a
`measured <YYYY-MM-DD>` stamp within the same row. It cannot verify the number — say so in the
header — but it converts every such claim into one a later session knows to re-derive. This gate
alone covers M6, L6 and part of L4.

---

## Low

### L1 — "within ~1.5x of the 2026-08-11 baseline" is contradicted by the numbers in the same row
*(finding ids 8, 28)*

**Sites:** `memory/backlog/TOOL.md:10` ·
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:316-318` (§3.8) ·
`build:506` (§5's disposition table)

The row lists baseline 22.5 / 23.9 / 103.7 ms against quiet-box 32.5 / 48.0 / 151.2 ms — ratios
1.44× for `bash -c true`, **2.01×** for `git rev-parse` and 1.46× for `python -c pass` — then
summarises all three as within ~1.5×. The tilde stretches to ~1.6, not to 2.0, and the op that
misses the bound is the one that scales: the report's own dead-ends table at `build:481` counts
roughly 750 process creations per run, about 140 of them git.

The row's direction survives — the tax is load-dependent, not standing — which is why this is low
rather than medium. The bound as written is still wrong on the op a skeptic probes first.

**Fix.** Write *"within 1.4-2.0× of the 2026-08-11 baseline"* at all three sites, so the stated
bound covers the numbers printed beside it.

**Left-shift gate.** The `record-table-claims` leg from H1 covers the report sites. For the backlog
row, the same leg extended to check that a summary bound stated in a row is not exceeded by any
ratio derivable from the numbers in that row, regex-scoped to the `<n>ms -> <n>ms` and `within ~<n>x`
shapes — and its header must say that is all it sees.

### L2 — the span-range correction was applied to three carriers and not to the two that derive from it
*(finding ids 14, 21)*

**Sites:** `memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:204`
and `:226`

This diff moved the span range to 925-1058 s at §2, at `build:539` and at `README.md:22`. Two §3.4
and §3.5 statements that consume it did not move: `:204` still reads *"With a service time of
925-1051 s"* and `:226` still reads *"against a 15.4-17.5 min service time"*, which is 924-1050 s.
Both feed the queueing conclusion of ~31-35 min and the "near 60 % utilization" turnstile figure.

The audit's F12 at `review:198-206` explicitly enumerated THREE carriers, naming the pre-correction
line number of `:204` among them, and closed with *"One number, one source"* — while its Fix line
named only two of the three sites its own body had identified. The half-application is against the
finding's own instruction, not a reading imposed on it.

**Fix.** Update `:204` to 925-1058 s and `:226` to 15.4-17.6 min, or replace both with a pointer to
the §2 table so the range has exactly one source.

**Left-shift gate.** A `figure-carriers` leg over a build folder: extract labelled figure shapes
(`<n>-<n> s`, `<n>.<n> s`, `<n>.<n> %`) with their nearest preceding noun, and red when the same
label carries two different values inside one build. This is the highest-yield gate on this list —
it reaches L2, M1, L1, L3 and L4 with one predicate. Its header must state that it cannot see a
figure stated only once, and that a deliberate before/after pair needs a marker to be exempt.

### L3 — the README's four-bar summary asserts a utilization range and a universal over a run with neither
*(finding ids 9, 29)*

**Sites:** `memory/builds/aScannedThrottle/README.md:22-24` ·
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:51` and `:539`

The README — the build's front page, and the first thing a reader meets — says *"Four real
`GATE_FULL=1` width-8 bars on node `a` reconstruct to spans of 925-1058 s at 60-70 % pool
utilization. Every one is FLOOR-bound."* §2's utilization column carries three values, 59.8 / 69.5 /
62.4 %, and a bare em dash for the fourth, whose cells the same commit declares unrecoverable. The
universal *"Every run is FLOOR-bound"* at `build:51` sits directly under that table and cannot be
evaluated for the 16:05 row at all.

In the report the caveat is at least adjacent. In the README it is absent, with no marker that a
quarter of the population is unmeasured. `build:539` carries the identical four-run framing, so this
lives in two carriers.

**Fix.** README: *"three bars reconstruct fully to spans of 925-1051 s at 59.8-69.5 % utilization,
and a fourth to a 1058 s span only; every one measured is FLOOR-bound."* Report `:51`: *"Every run
whose per-leg records survive — three of four — is FLOOR-bound."*

**Left-shift gate.** The `record-table-claims` leg from H1, run over `README.md` as well as
`build/*.md`: a build README asserting a population size or a range must not exceed the filled-cell
count of the table it summarises.

### L4 — "14.7% low" names no base, and the two readings differ by two points
*(finding id 15)*

**Sites:** `memory/backlog/TOOL.md:13` ·
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:509`

The mean of the four spans is (970.0 + 925.5 + 1051.4 + 1058.3) / 4 = 1001.3 s. 873 / 1001.3 =
0.8719, so 873 s is **12.8 % below** the mean; 1001.3 / 873 = 1.147, so the mean is **14.7 % above**
873 s. The row writes *"states 873s against a measured mean of 1001.3s across four GATE_FULL bars,
14.7% low"* with no base named, and under the conventional reading of "N % low" — error relative to
the reference value — the correct figure is 12.8 %. A later session re-deriving the gap from the
mean will not reproduce 14.7 % and will suspect the mean instead.

It is transcribed faithfully from `build:509`, so the ambiguity has propagated from the report into
the durable backlog row.

**Fix.** Pick a base and say it: *"the measured mean is 14.7 % higher than the charter's 873 s"*, or
*"873 s is 12.8 % below the measured mean of 1001.3 s."* Correct `build:509` in the same edit so the
two stay one number. The row's other half is fine — the span IS recoverable for all four runs,
unlike the floor in M1, so "across four GATE_FULL bars" is correct here.

**Left-shift gate.** No cheap mechanical gate reaches "which base does this percentage use". This is
a §10 checklist entry: *a percentage stated as a deviation names its base, or restates the
comparison as "X is N % of Y".* A documented manual check, run in every Tier-2 over a record
carrying derived figures.

### L5 — rev-2's one checkable claim is refuted by the record it cites five lines above
*(finding id 16)*

**Site:** `memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:119-120`

rev-2 states in the present tense that "dispositioned" is a corpus hapax that *"appears in this file
and nowhere else"*. `git grep -n dispositioned` at HEAD returns seven lines across two files:
`reviews/2026-08-21-review-TOOL-aScannedThrottle-1.md` at `:49`, `:73`, `:75` and `:89`, and `spec`
at `:112`, `:118` and `:119`. The falsifying file is the audit record the spec links five lines
above at `:114`, added by the same two-commit range.

The underlying reasoning still holds — the review's uses are mentions, not a defining usage — but
the sentence as written is a checkable assertion that is false at HEAD, and it is the one claim in
rev-2 a reader can test in a single command.

**Fix.** Past-tense it and pin the tree: *"was a corpus hapax at base `49aea26` — the only other
occurrences are the audit record that raised it."*

**Left-shift gate.** A `hapax-claims` phrase check: a tracked record asserting *"appears in this
file and nowhere else"*, *"the only occurrence"* or *"nowhere else in the corpus"* must carry a base
sha or a date stamp in the same sentence. Cheap grep, and it converts an assertion that rots into
one that stays true.

### L6 — the re-minted `TOOL-aScannedThrottle-8` restates a worktree census that was already 4× stale when written
*(finding id 30)*

**Site:** `memory/backlog/TOOL.md:144`

The row restates in the present tense *"24 of 26 worktrees on node a have no ledger"*.
`git worktree list` returns **6** worktrees on node `a`, and `gate-ledger.tsv` exists in the common
dir plus two linked worktrees. The worktree cleanup landed at `b927a92` / `49aea26` on 2026-08-20 at
23:30 — that sha is this run's pinned BASE — and `git show 2861ea9 -- memory/backlog/TOOL.md` shows
the row being ADDED with the old census on 2026-08-21 at 01:02. Stale on write, not merely aged.

The count is the row's sizing argument — *"Costs 15.6-16.3% of span on every cold worktree, which is
where every new unit starts"* — so a reader pricing the fix prices a 4×-inflated population. The
mechanism and the fix are untouched; only the magnitude is wrong, which is why this is low.

**Fix.** Date-stamp the census rather than restating it: *"measured 2026-08-20 at 24 of 26 worktrees
with no ledger; re-derive with `git worktree list` before pricing — the population moves."*

**Left-shift gate.** The `present-tense-census` check from M6 covers this row exactly.

---

## Left-shift summary — five gates cover thirteen of the fifteen defects

| gate | catches | shape |
|---|---|---|
| `figure-carriers` (per build folder) | L2, M1, L1, L3, part of H1 | one labelled figure, two values inside one build, RED |
| `record-table-claims` | H1, M1, L3, L1 | a prose population (`every row`, `across four bars`) exceeding the table's filled-cell count, RED |
| `spec-population` | H2, H3 | a spec's DERIVED-population declaration evaluated against the named file; an unclaimed selected id, RED; an undeclared block, named refusal |
| `present-tense-census` | M6, L6, part of L4 | a filesystem count in a backlog row with no `measured <date>` stamp, RED |
| `manifest-claims` | M2 | an enumerated phrase about `tools/gate-legs.json` re-derived from the manifest, RED on mismatch |

Two defects have no cheap gate and belong in the §10 checklist instead: **L4**, a percentage stated
as a deviation must name its base; and **M3**'s retraction half, a disposition that supersedes a
figure names the figure it supersedes. M3's other half, M4 and M5 each get a one-line check of their
own — a backlog disposition-verb vocabulary, a registry header self-count, and a citation-figure
grep.

**Every gate above is unbuilt.** Per §7 none of them is landed until its failing case has been
observed: stage the break, confirm RED, unstage. Each candidate predicate should also be run over
the real tree before wiring, printing hits AND near-misses — on this corpus the `figure-carriers`
predicate will almost certainly surface live instances outside this build, which is the point.
