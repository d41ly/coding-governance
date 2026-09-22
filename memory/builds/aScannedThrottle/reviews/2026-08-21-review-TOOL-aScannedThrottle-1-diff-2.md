**Serves:** diff-review TOOL-aScannedThrottle-1

# Diff review — `2861ea94c55d3a603deb94e383b46dcff9093480...HEAD`, ROUND 2

Reviewed range `2861ea94c55d3a603deb94e383b46dcff9093480...HEAD` — one commit, `889c9c9` (the fold
that applied round 1's diff review), across six files, all under `memory/`. **Verdict: CLEAN WITH
FIXES — no blockers.** Nothing in this diff touches executable code, so nothing here can break a
gate or a runtime. Every finding is a durable-record defect, and the records are what this build
ships.

**Review shape.** Raw 45 · confirmed 39 · refuted 6 · unverified 0 · precision 0.87. Every confirmed
finding was re-opened against the tree at HEAD and re-derived from the bytes. The counts above are
finding counts; the 39 confirmed findings consolidate to **18 distinct defects**, because eleven of
them were filed against more than one carrier of the same number by different lenses. Each defect
names the finding ids it absorbs.

**Severity split of the 18 defects:** 0 blockers · 4 high · 8 medium · 6 low.

**D1 is not a merge blocker but it does block the unit's own CLOSE.** The fold wrote a new closing
condition whose clause (1) reads `memory/backlog/TOOL.md`, and left one row in that file
unreconciled. The unit cannot be graded CLOSED against a clause it fails.

**What this review did NOT check.** It did not re-run the bar, so no measurement in the report was
independently reproduced — only internal arithmetic and agreement with the tree. It did not
re-audit round 1's own record beyond the Fix lines this fold was applying. It did not evaluate
whether the seven minted `TOOL-aScannedThrottle-*` rows are the right rows; scope was the diff.

**One shape produced two thirds of these defects, and it is the same shape round 1 named.** A review
finding named two or three carriers of one figure; the fold corrected some of them. Eight of the
eighteen defects below are a half-applied multi-carrier fix, and in five of those the corrected half
now contradicts the uncorrected half inside a single file. Round 1 diagnosed this class and
prescribed "at all three sites" in three separate Fix lines; the fold applied two of three in each
case. That is why the left-shift suggestions converge on two gates rather than eighteen.

---

## High

### D1 · HIGH — H3's fix landed in the report only; the new closing clause (1) is unmet by the exact row it was written for

*Absorbs findings 2, 12, 23, 35 — four lenses, independently.*

`memory/backlog/TOOL.md:104` still reads `TOOL-aBoundedVerdict-10 · OPEN · unattended driver
selftest HANGS on node a inside its first --preflight (traced), zero output at 240s … Two fixes`,
with no dated disposition line. The fold added the matching `§5.1` cell at
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:541` and never
touched the row.

`git show 889c9c9 -- memory/backlog/TOOL.md` touched six rows — `aMeteredTurnstile-6`, `-3`,
`aTimedTurnstile-1`, `-2`, `-3`, `aScannedThrottle-8` — and line 104 is not among them. The
neighbouring `§5.1` rows `aTimedTurnstile-4` and `-6` did get their dated dispositions at `2861ea9`,
so this is an omission and not a policy.

Why it binds: `memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:126`
now defines closing clause (1) as *every OPEN row in `memory/backlog/TOOL.md` matching S5's
predicate carries a dated disposition line citing the report section that measured it* — the
predicate, explicitly not the report's own tables. `§5.1` rules this row IN. Derived at HEAD,
`grep -c 'TOOL-aScannedThrottle-1 §' memory/backlog/TOOL.md` returns 12 against the 14 ids
dispositioned in `§5` + `§5.1`; the two absent are `TOOL-aBoundedVerdict-10` and
`TOOL-aTetheredScratch-3` — exactly the two rows this fold added.

This is spec-audit F1's defect, "written in the report and never applied to the backlog", recurring
on the one row round 1 added specifically to retire it. Worse than a stale line: a later run grading
the close against the `§5.1` table reads CLOSE while the backlog is unreconciled.

**Fix.** Append the dated disposition to `memory/backlog/TOOL.md:104`, in the same shape as the five
rows the fold already stamped, with the verb corrected per D11: `NOT REPRODUCED 2026-08-21 by
TOOL-aScannedThrottle-1 §5.1 — that leg COMPLETED in all three reconstructed bars at 812.1 / 925.5 /
887.9 s, so the hang is intermittent or gone; the no-per-leg-deadline clause is untouched and
stands.` Apply D2's wording correction in the same edit.

**Left-shift gate — `disposition-parity`, the highest-yield gate in this review.** A check that
derives S5's predicate over `memory/backlog/TOOL.md` and asserts, in both directions, that every id
dispositioned in a build report's `§5`/`§5.1` tables carries a dated disposition line in its backlog
row, and that every predicate-matching OPEN row is dispositioned somewhere. It reds on exactly this
defect, and it would have red on F1 as well. Both directions matter: the one-directional version
certifies the report and misses the row.

---

### D2 · HIGH — the fold's new phrase "the three bars whose per-leg records survive" is false at HEAD, and contradicts the correction written in the same commit

*Absorbs findings 1, 39.*

Three sites now assert survival of per-leg records that no longer exist for **any** of the four
bars: `memory/backlog/TOOL.md:47`, `memory/backlog/TOOL.md:49`, and
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:541`.

Derived on node `a`. TZ is +0300, and the report's own run ids `130546` and `120751` fix the
mapping, so the four bars at local 14:44 / 15:07 / 15:38 / 16:05 ran at UTC 11:44 / 12:07 / 12:38 /
13:05. Enumerating every `gate-run` store under the common git dir returns three: `.git/gate-run`
holds `20260820T163240Z-457` onward, `.git/worktrees/open-builds-overview-e2db27/gate-run` holds
`20260820T143351Z-1131` onward, and `.git/worktrees/unattended-build-issues-38c32e/gate-run` holds
`20260820T185753Z-535` onward. None covers `T1144`, `T1207`, `T1238` or `T1305`. `.git/gate-logs/`
is keyed by leg NAME and overwritten per run, so it reconstructs nothing.

The report says so itself. `build:57-58` reads "`<git-dir>/gate-run/` on node `a` now holds only
`20260820T163240Z-457` onward, so the per-leg records they would be reconstructed from are gone" —
a cutoff that excludes all four bars, not just the fourth.

This is a REGRESSION introduced by the fix. Round 1's M1 prescribed the safe wording "whose floor is
recoverable (§2)", which `build:514` uses correctly; these three sites substituted a survival claim
that is not true.

**Fix.** Write, at all three sites, what is actually the case: "the three bars §2 reconstructed
before the sweep (per-leg records for all four are gone as of 2026-08-21)". The population size 3 is
right; only the reason given for it is wrong. While there, narrow `build:56-58`: the stated cutoff is
true of all four runs and therefore does not explain why the 16:05 row alone lacks figures — the
actual reason is that the other three were reconstructed before the sweep and this one never was.

**Left-shift gate — `liveness-of-cited-evidence`.** Where a record cites an on-disk evidence store —
a `gate-run` id, a log path, a timings file — as the warrant for a figure, the check resolves the
path and reds when nothing matches. Charter §7 already requires a liveness assertion on every signal;
this applies it to prose that claims a source survives.

---

### D3 · HIGH — M1 named three carriers of "812–926 s across four bars"; two were corrected and `§5.1`'s cell still says four

*Absorbs findings 17, 36.*

`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:538`, the
`TOOL-aTimedTurnstile-3` cell, still reads "the floor does not: 812–926 s across four bars, not
~76 s". `git show 2861ea9` puts round 1's third named site — `build:529` at that revision — on
exactly this cell, and M1's Fix line said verbatim "at ALL THREE sites".

`memory/backlog/TOOL.md:47` and `:49` moved. This cell did not. Two hundred lines above it,
`build:40` marks the 16:05 floor cell an em dash and `build:42-47` calls it unrecoverable, and
`build:514` says "on the three bars whose floor is recoverable" — so the report now gives two
answers to one question about its own sample size.

**Fix.** Rewrite the cell's floor clause to match `:514`: "812–926 s on the three bars whose floor is
recoverable (§2), not ~76 s" — or replace the figure with a pointer to `§2` so the range has one
source. Fold D2's wording correction in.

**Left-shift gate — `multi-site-fix-parity`,** described in the summary table below.

---

### D4 · HIGH — M3 was applied to the report's instruction cell and not to the row; one backlog file now carries two incompatible floors

*Absorbs findings 7, 13.*

`memory/backlog/TOOL.md:123`, the `TOOL-aPacedTurnstile-8` row, still reads `RAISED TO TOP and
RE-STAMPED 2026-08-21`, still asserts "the first alone is 75.6% of the 873s wall, so the bar's floor
is ~660s at any width on any hardware", and still hangs "the remaining 213s" off that floor. M3's
Site line named this row; the fold's backlog diff does not include it.

The fix landed only in `build:514`, which now says "RETRACT the row's '~660s at any width' floor —
measured at 812–926 s on the three bars whose floor is recoverable" and "The backlog has no priority
field, so 'first' is this ranking's claim, not a state the file can hold". So the report now
explicitly contradicts the row it was written to correct, and the unexhibitable `RAISED TO TOP` claim
was left standing in the carrier — at line 123 of 150, in a shard that declares no order or priority
field.

Same file, same date: `:47` and `:49` say 812–926 s, `:13` calls the 873 s figure wrong, and `:123`
argues from both retracted numbers. A session pricing the sharding work gets whichever row it greps
first.

**Fix.** Edit the row. Replace `RAISED TO TOP` with a claim the file can hold — `HIGHEST-VALUE OPEN
ROW per TOOL-aScannedThrottle-1 §4 R2` — and append: `SUPERSEDED 2026-08-21: the ~660s floor and its
873s / 213s derivations do not hold; measured floor 812–926s on the three bars §2 reconstructed,
measured mean wall 1001.3s (§2, §5).`

**Left-shift gate — `figure-carriers`.** A check over one build folder plus the backlog rows it cites
that extracts labelled quantities (`floor`, `wall`, `span`, `leg-seconds`) and reds when one label
carries two values across carriers without an explicit supersession marker. Six of these eighteen
defects are that shape.

---

## Medium

### D5 · MEDIUM — the "the predicate was RUN" census does not reconcile with itself, twice

*Absorbs findings 4, 16, 25, 38.*

`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:545` reads "Over
the 117 OPEN rows at HEAD a keyword reading of S5's six terms selects 22, of which 14 are
dispositioned above and 7 are this build's own." **14 + 7 = 21.** And `:546` reads "Four more were
read and ruled OUT" followed by **five** ids: `TOOL-aPromptedMandate-9`, `TOOL-aDeclaredBound-6`,
`TOOL-aTetheredScratch-4`, `TOOL-aBoundedVerdict-8`, `TOOL-aWalkedCorpus-5`.

Neither reading reconciles: if the ruled-out set is inside the 22 the total is 26, if outside it is
21. The generous reading is worse still. `TOOL-aTimedTurnstile-1` is `CLOSED` at `TOOL.md:47`, so it
cannot be among the 117 OPEN rows the selection is drawn from; `TOOL-aTetheredScratch-3` is declared
OUT in that same table; and the paragraph's own next sentence removes `TOOL-aBoundedVerdict-10`,
which "matched none of the six terms literally". None of 22, 14 or 7 reproduces.

Verified: `§5` holds 8 rows, `§5.1` holds 6, this build's own rows are `TOOL-aScannedThrottle-2`…`-8`
= 7 (`TOOL.md:144-150`, there is no `-1` row), and `grep -c ' · OPEN · ' memory/backlog/TOOL.md`
returns 117 — the denominator is the one figure that does reproduce.

This paragraph is the sole evidence for the completeness claim closing clause (1) now rests on, so
its arithmetic is load-bearing. A later session re-running the predicate cannot tell whether 21, 22
or 26 rows were selected, which is to say cannot tell whether the set was reproduced or a row was
dropped — the omission-versus-judgement ambiguity F4 and H2 were written to remove.

**Fix.** Re-run the selection and **print the id list rather than a total**. If a partition is kept,
state three disjoint sets whose sizes sum: selected N = dispositioned-and-OPEN + this build's own +
ruled out. Say explicitly that `TOOL-aTimedTurnstile-1` is CLOSED and `TOOL-aTetheredScratch-3` is
OUT, so neither is inside the OPEN selection.

**Left-shift gate — `census-emits-ids`.** Cheapest form: a hygiene check that reds on a prose
partition of the shape "selects N, of which A … and B …" inside a build record where A + B ≠ N. The
better form is a convention the gate can enforce — a census states ids, and the count is derived from
the list at read time, per charter §7's ban on a prose count of a derived population.

---

### D6 · MEDIUM — both `aTetheredScratch` adjudications name a subject the rows do not carry

*Absorbs findings 5, 41.*

`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:542` rules
`TOOL-aTetheredScratch-3` "OUT of the population" because "Its 'scratch' is the scratchpad directory,
not the bar's `mktemp -d` scratch repos". `memory/backlog/TOOL.md:77` says nothing of the kind: it
says `tools/memory-recall/selftest.py` leaves 2 empty `tmp.*` dirs per run that never route through
`cleanup()`, measured on a controlled TMPDIR. That script IS a bar leg — `tools/gate-legs.json`
carries `{"name": "memory-recall kit selftest", "argv": ["python3",
"tools/memory-recall/selftest.py"]}` — so the row is TMPDIR leakage from a leg the bar runs, the same
class `TOOL-aMeteredTurnstile-2` prices. The row even relates itself to that leak, "three orders of
magnitude smaller than the leak just closed".

The same paragraph, at `build:548`, labels `TOOL-aTetheredScratch-4` "(scratchpad)". `TOOL.md:76` is
about a test fixture committed into the live repo by an unguarded `cd "$D"` in
`check-wiring.test.sh`. Also not the scratchpad.

H3 asked for this row to be adjudicated in writing. An adjudication whose stated reason misreads the
row is not a defensible exclusion — it reinstates H2's defect one level up, an omission dressed as an
explicit adjudication, on the only row the fold removes from S5's population.

**Fix.** Re-adjudicate `-3` against its actual text. Either admit it to the population, or exclude it
on a stated magnitude ground — 2 dirs per run against `TOOL-aMeteredTurnstile-2`'s 1053 — as
in-scope-but-immaterial rather than out-of-population. Correct the `-4` parenthetical to name its
real subject in the same edit.

**Left-shift gate.** Not gateable; the defect is a misreading, not a mismatch a predicate can see.
This is a §10 checklist entry: *an adjudication that excludes a record quotes the record's own words
for the ground it excludes on.*

---

### D7 · MEDIUM — M6 and L6 were fixed in the backlog rows only; the report's matching carriers were left flat and present-tense

*Absorbs findings 6, 27.*

Two figures, one build, two values each.

`memory/backlog/TOOL.md:12` now reads "measured 2026-08-20 at 964.2s across the then-live
per-worktree copies, and 13.7s in the common-dir copy that survives at HEAD", while `build:516` still
asserts, undated and present-tense, "The 964.2 s of orphan rows sits in the dead `gate-timings.tsv`,
which nothing reads". Derived at HEAD, that file holds 73 rows with 4 orphans totalling 13.961 s — so
the surviving report figure is roughly 69× high.

`memory/backlog/TOOL.md:144` now reads "measured 2026-08-20 at 24 of 26 worktrees … the cleanup at
`49aea26` took it to 6", while `build:96`'s `§3.1` heading and `build:375`'s sizing sentence still say
"24 of 26" and "which today is 24 of 26". `git worktree list` returns 6.

Not a decision to freeze the report: the same commit edited `§5`'s `aPacedTurnstile-8` and
`aMeteredTurnstile-4` cells and rewrote `§2`'s correction block. The omission is selective.

**Fix.** Apply the same stamps in the report. `:516` gains "measured 2026-08-20; 13.96 s in the
common-dir copy that survives at HEAD". `:96` and `:375` gain "(measured 2026-08-20; 6 worktrees at
HEAD after the `49aea26` cleanup — re-derive with `git worktree list` before pricing)". Or point all
three report sites at the backlog rows so each figure has one source.

**Left-shift gate — `figure-carriers`,** as D4.

---

### D8 · MEDIUM — L1's third site was not fixed: `§5` still summarises the spawn tax as "within ~1.5×"

*Absorbs findings 18, 42, and finding 6's second limb.*

`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:515` still reads
"quiet-box readings sit within ~1.5× of the 2026-08-11 baseline". L1's Sites were `TOOL.md:10`,
`build:316-318` (`§3.8`) and `build:506` (the `§5` cell, now `:515`), and its Fix said "at all three
sites". The first two moved: `TOOL.md:10` and `build:326` both read "1.4–2.0×".

The ratios reproduce from `§3.8`: 32.5/22.5 = 1.444, 48.0/23.9 = 2.008, 151.2/103.7 = 1.458. So
`~1.5×` is wrong on the op that scales, and the report states the retracted bound in `§5` and the
corrected bound in `§3.8`, two hundred lines apart. `§5` is the half a session copies into a backlog
row next time.

**Fix.** Write "1.4–2.0× of the 2026-08-11 baseline" at `:515`. Note while there that both corrected
sites state a 2.0× bound and then name 2.01× in the same clause — write "~2×" or "1.4–2.1×" so the
bound covers the number printed beside it.

**Left-shift gate — `multi-site-fix-parity`.**

---

### D9 · MEDIUM — the guard census names six legs where the manifest says four, and restates the derived split in prose against §7 and against M2's own Fix line

*Absorbs findings 14, 15, 28.*

`memory/backlog/TOOL.md:48` now reads "derived from `tools/gate-legs.json` on 2026-08-21, 52 of 88
legs carry a truthy `guard` and six legs whose own name says self-test carry none (`template size
gate selftest`, `method-carriers self-test`, `agent-cap restatement self-test`, `govkit selfcheck`,
and both `testsuite counts` legs)". Two limbs, both defective.

**The enumeration is wrong.** Derived at HEAD: 88 legs, 44 in chunk `selftests`, of which exactly four
carry no guard — `template size gate selftest`, `method-carriers self-test`, `agent-cap restatement
self-test`, `testsuite counts self-test`. `govkit selfcheck` is a `declarations` leg whose name says
*selfcheck*, failing the row's own stated predicate, and it has a separate, already-guarded sibling
`govkit selftest`. `testsuite counts (every bar self-test prints one)` is also a `declarations` leg,
matching only inside a parenthetical. Round 1's M2 reached five name-matches and explicitly reduced to
four; the applied row inflated it to six, so one commit ships six, five and four as three answers to
one count.

The harm is directional. A guard makes a leg skip on records-only commits, and `AGENTS.md:480` says
guards exist so "a records-only commit runs only the legs that check this repo's actual state" —
guarding two `declarations` legs would silence them on exactly the commits they are there for.

**The prose count is the thing M2's Fix forbade.** That Fix reads verbatim: "Naming the four legs is
fine; restating the 52/88 split in prose recreates the defect one commit later." `AGENTS.md` §7 says
"NO count of a derived population is written in prose." The figure is right today — 53 legs carry a
`guard` key, 52 a truthy one, since `run-gates wiring` holds an empty array — and goes wrong on the
next manifest edit, in the row a session greps before acting on guard coverage.

**Fix.** Replace the count with a pointer and align the enumeration: "the guard mechanism it asks for
LANDED but NOT universally — derive the split from `tools/gate-legs.json`; four `selftests`-chunk legs
still carry none (`template size gate selftest`, `method-carriers self-test`, `agent-cap restatement
self-test`, `testsuite counts self-test`), and `govkit selfcheck` and `testsuite counts (every bar
self-test prints one)` are `declarations` legs and are correctly unguarded."

**Left-shift gate — `derived-count-in-prose`.** A hygiene check over `memory/` for the shape `<N> of
<M> legs` / `<N> of <M> checks` that re-derives the pair from `tools/gate-legs.json` and reds on a
mismatch. §7 already states the rule; nothing enforces it, and this is its second recurrence in two
commits.

---

### D10 · MEDIUM — `§2`'s "Every run is FLOOR-bound" universal was left standing while the README's twin was narrowed

*Absorbs findings 9, 26, 37.*

`memory/builds/aScannedThrottle/README.md:22-24` was correctly rewritten by this commit to "THREE of
them reconstruct fully, at 59.8–69.5 % pool utilization, and all three are FLOOR-bound … The fourth
carries a recovered span and a recovered verdict only."
`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:60` still reads
"**Every run is FLOOR-bound**", four lines under the paragraph that declares the 16:05 row's floor,
utilization and packing unrecoverable, and six lines under a table whose fourth floor cell is an em
dash.

L3's Fix named both carriers and prescribed the report wording verbatim. Only the README half landed.
The universal cannot be evaluated for a quarter of its population, and it is the sentence the report
itself calls the one that "decides everything below". The front page and the report now disagree about
the same population — the exact carrier divergence the fold was closing.

**Fix.** `:60` becomes "**Every run whose per-leg records were reconstructed — three of four — is
FLOOR-bound**: the single longest leg exceeds leg-seconds ÷ width."

**Left-shift gate — `multi-site-fix-parity`.**

---

### D11 · MEDIUM — `TOOL-aBoundedVerdict-10` is stamped "REFUTED as written" on evidence that does not contradict the row

*Absorbs finding 40.*

`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:541` refutes the row
because the leg "COMPLETED in all three bars … at 812.1 / 925.5 / 887.9 s". The row makes three claims
and completion times touch only one of them.

`run-gates.sh:785-787` captures each leg into a file (`>"$WORK/$i.raw" 2>&1`) and `cat`s it only after
the leg returns — so ANY 800-second leg shows zero output at 240 s by construction. The row's first
observable clause survives untouched. And the cited completion times are byte-identical to `§2`'s floor
column, so the "refuting" evidence is that this leg IS the bar's floor, which is precisely the "wedges
the WHOLE bar" symptom the row reports.

Only the literal word HANGS is addressed; two of the three clauses the cell itself quotes are left
standing while the whole row is stamped REFUTED in a durable record. That risks a future session
closing a live, traced defect, and it propagates into the backlog the moment D1 is fixed.

**Fix.** Downgrade the verb to what the evidence supports: "**NOT REPRODUCED in this sample** — the leg
completed in all three reconstructed bars (812.1 / 925.5 / 887.9 s), so the 240-second symptom did not
recur; per-leg output timing was not reconstructed, and the traced `--preflight` hang is unaddressed.
The no-per-leg-deadline clause stands." Keep the row OPEN on its own terms.

**Left-shift gate.** Not gateable. §10 checklist entry: *a disposition verb covers every clause the cell
quotes, or the cell quotes only the clause it dispositions.*

---

### D12 · MEDIUM — the 16:05 recovery presents a circular identity as an independent cross-check, and its stated division does not print the stated value

*Absorbs findings 29, 45.*

`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:54` reads "292 /
0.276 = 1058.3 s, which reconciles with 4 × 1001.3 − (970.0 + 925.5 + 1051.4) = 1058.3".

The identity is a tautology. (970.0 + 925.5 + 1051.4 + 1058.3) / 4 = 1001.3 exactly, and `git show
d16f96c` confirms 1001.3 was already in the first draft as "measured mean across four runs" beside
"Spans 925–1058 s" — so the mean was computed FROM the four spans including this one. The sentence
reads as two derivations agreeing when only one exists.

The one derivation does not produce the printed value: 292 / 0.276 = 1057.97, that is 1058.0. The
sibling at `:400`, 282 / 0.305, likewise yields 924.6 against a measured 925.5, so the method carries
about a second of error; and with 27.6 % at three significant figures the span is 1058 ± 4 s, making
the tenth spurious precision.

The whole point of the H1 rewrite was to state per cell what is measured versus reconstructed. This is
the cell whose provenance it overstates.

**Fix.** State it as one derivation with its precision and drop the circular clause: "recovered as
292 / 0.276 ≈ 1058 s (±4 s at the quoted three significant figures), carried at 1058.3 s to stay
consistent with the four-run mean of 1001.3 s **that was computed from it** — the mean is not an
independent check." Carry the same rounding into the 925–1058 s range at `:43`, `:204`, `:539` and
`README.md:22`.

**Left-shift gate.** Not gateable. §10 checklist entry: *a corroborating derivation is independent of the
value it corroborates, or it is not offered as corroboration.*

---

### D13 · MEDIUM — `§5.1`'s membership sentence undercounts its own table by two

*Absorbs findings 8, 24, 43.*

The heading at `memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:528`
was widened from "Four more OPEN rows" to "More OPEN rows", and `:531` still reads "These four qualify
on the same reading and were absent" above a table at `:534-542` holding six: `aTimedTurnstile-2`,
`-3`, `-4`, `-6`, `aBoundedVerdict-10`, `aTetheredScratch-3`.

Wrong by two in one direction, and wrong for one row in the other: `aTetheredScratch-3` is adjudicated
"OUT of the population" in that same table and therefore does not "qualify on the same reading" at all.
The undercount drops `aBoundedVerdict-10`, whose late discovery is the section's headline point. The
section exists to make the population auditable and its own membership statement does not match its
table.

**Fix.** Rewrite `:530-532`: "§2's S5 says **every** open backlog row about bar performance, and the
table above is a curated eight. Five more qualify on the same reading and were absent; a sixth,
`TOOL-aTetheredScratch-3`, is adjudicated OUT and recorded here so the exclusion is written rather than
silent."

**Left-shift gate — `census-emits-ids`,** as D5. The same convention fixes this: a section states the
ids, and the count is read off the list.

---

## Low

### D14 · LOW — the throughput cross-check does not reproduce the column it claims to reproduce, and the spec now carries a third copy

*Absorbs finding 21.*

`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:48` reads "59.8 % ×
8 = 4.78, 69.5 % × 8 = 5.56, 62.4 % × 8 = 4.99, reproducing the column above". The table at `:37`
carries **4.79** for the 14:44 run: 4644 / 970.0 = 4.7876 → 4.79, while 0.598 × 8 = 4.784 → 4.78. The
two routes agree on rows 2 and 3 and disagree on row 1 — the first row a reader checks, inside the
paragraph whose whole point is that the arithmetic already reconciles.

The fold also copied the finished column into
`memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:165`, "the column is
filled at 4.79 / 5.56 / 4.99 leg-s/s", giving one derived figure three carriers across two files — the
duplication class this build documents.

**Fix.** State the cross-check as approximate: "utilization × width reproduces it to rounding: 59.8 % ×
8 = 4.78 against 4.79 from leg-seconds ÷ span". Replace `spec:165`'s copied values with a pointer to
`§2`'s table.

**Left-shift gate — `figure-carriers`,** as D4.

---

### D15 · LOW — the corrected hapax claim is falsified by text the same commit added, and revives the vocabulary rev-2 retired

*Absorbs findings 10, 31.*

`memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:121` now reads
"'dispositioned' … was the only occurrence in the corpus at base `49aea26`, the only others since being
the audit record that raised it". The pinned half is right: `git grep -n dispositioned 49aea26` returns
exactly one line, `spec:105`. The second clause is false at HEAD — the term also appears at `build:545`
and three times in `reviews/2026-08-21-review-TOOL-aScannedThrottle-1-diff.md`, and `git show 889c9c9`
confirms the same commit that rewrote the clause created both carriers.

Beyond the miss: `build:545` uses the word operatively, "14 are dispositioned above", in exactly the
sense F3 retired it for — a property a backlog ROW acquires. The word rev-2 killed is live again in the
artifact the closing condition is about.

**Fix.** Drop the enumeration and keep the pin: "was a corpus hapax at base `49aea26`; every later
occurrence is a mention of this finding, not a defining usage." Replace "dispositioned" at `build:545`
with the closing condition's own vocabulary, "carry a dated disposition line".

**Left-shift gate.** A `git grep` one-liner in the record itself, not a gate: pin corpus-frequency claims
to a base sha and never to "since". This is charter §6's "a value stated in prose beside the source that
OWNS it rots" — a count of the corpus, stated inside the corpus.

---

### D16 · LOW — M6's replacement orphan figure does not re-derive: four orphans totalling 13.96 s, not three totalling 13.7 s

*Absorbs findings 32, 44.*

`memory/backlog/TOOL.md:12` asserts "13.7s in the common-dir copy that survives at HEAD". Derived at
HEAD from `C:/projects/coding-governance/.git/gate-timings.tsv` against `tools/gate-legs.json`: 73 rows
and **four** orphans — `memory hygiene (20 checks)` 7.846, `marker contract (4 readers)` 5.234,
`verifier fan-out (≤5 verify agents per review)` 0.650, `template size <=32KiB` 0.231 — totalling
13.961 s. The first three sum to 13.730, which is the review's 13.7; the fourth was missed.

The missed row is a renamed leg — `template size <=48KiB` at HEAD, renamed at `1640f68` — so it survives
by precisely the eviction mechanism this row exists to describe, and omitting it also omits one instance
of the defect. A correction whose entire purpose was to replace a non-reproducing figure with a
re-derivable one ships one that does not re-derive. The same 13.7-across-three reading sits in
`reviews/2026-08-21-review-TOOL-aScannedThrottle-1-diff.md:314-315`.

Bounded harm: the row instructs a later session to re-derive.

**Fix.** Write "13.96s across four orphan rows in the common-dir copy that survives at HEAD (measured
2026-08-21)", naming `template size <=32KiB` as the fourth — or drop the figure and keep only the
re-derive instruction.

**Left-shift gate — `derived-count-in-prose`,** as D9. A check that re-derives this exact pair,
`gate-timings.tsv` rows against `gate-legs.json` names, would have caught it.

---

### D17 · LOW — L4 was applied to the report and not to the backlog row it was filed against

*Absorbs finding 20.*

`memory/backlog/TOOL.md:13`, the `TOOL-aMeteredTurnstile-4` row, still reads "states 873s against a
measured mean of 1001.3s across four GATE_FULL bars, **14.7% low**" with no base named. `build:518` now
carries both readings correctly: "the charter's 873 s is 12.8 % BELOW that mean, and the mean is 14.7 %
ABOVE the charter's figure. Two readings of one gap; state the base."

L4's Sites listed `TOOL.md:13` first and `build:509` second, and its Fix said to correct both "so the two
stay one number". Under the conventional reading of "N % low" against the reference, the correct figure
is 12.8 %, so a session re-deriving the gap from the mean gets a different number and suspects the mean.
The durable carrier is the half left wrong.

**Fix.** "states 873s where the measured mean across four GATE_FULL bars is 1001.3s — the mean is 14.7%
above the charter's figure, and the charter's figure is 12.8% below the mean."

**Left-shift gate — `multi-site-fix-parity`.**

---

### D18 · LOW — the `AGENTS.md` guard universal has no backlog holder, and the row that would hold it still says "TWO live claims"

*Absorbs finding 33.*

`AGENTS.md:480` still reads "Each self-test leg carries a `guard` in the manifest naming the kit dir it
exercises", which the manifest refutes at HEAD — four `selftests`-chunk legs carry none, per D9. `git
show 889c9c9 -- AGENTS.md` is empty, so the second carrier of M2's class did not move, which is correct:
editing `AGENTS.md` is an owner turn.

But nothing holds the debt. `TOOL-aMeteredTurnstile-4` at `memory/backlog/TOOL.md:13` exists precisely to
carry `AGENTS.md`'s wrong claims and still enumerates "TWO live claims, both wrong" — the wall/leg-sum
pair and the dead `gate-timings.tsv` reference. Grepping `memory/` for the guard universal returns only
the review record, and a review is a record, not the mutable holder S5 requires. That editing `AGENTS.md`
is an owner turn is exactly why a row should hold it.

**Fix.** Extend `TOOL-aMeteredTurnstile-4` to THREE live claims: "`AGENTS.md:480` states that each
self-test leg carries a `guard`; derived from `tools/gate-legs.json` 2026-08-21, four `selftests`-chunk
legs carry none. Owner turn like the other two." Fold in D17's edit.

**Left-shift gate — `derived-count-in-prose`,** as D9, extended to universals over the manifest
(`each`, `every`) as well as counts.

---

## Left-shift summary — five gates, and one of them earns most of the value

| gate | catches | defects it would have red on |
|---|---|---|
| `multi-site-fix-parity` | For each Fix line in a `reviews/` record naming two or more `file:line` sites, assert the fold commit touched **all** of them; red on a partial application. | D3, D8, D10, D17, and the backlog halves of D1, D4, D7 — **seven of eighteen** |
| `disposition-parity` | Derive S5's predicate over `memory/backlog/TOOL.md`; assert bidirectional parity with the report's `§5`/`§5.1` tables. | D1, and spec-audit F1 before it |
| `figure-carriers` | One labelled quantity, two values, across a build folder and the backlog rows it cites, with no supersession marker. | D4, D7, D14, plus D2 and D3's contradiction limbs |
| `derived-count-in-prose` | Prose counts and universals over `tools/gate-legs.json` and `gate-timings.tsv`, re-derived at check time (charter §7). | D9, D16, D18 |
| `census-emits-ids` | A prose partition inside a build record whose parts do not sum; convention is to state ids and derive the count. | D5, D13 |

`multi-site-fix-parity` is the one to build first. It is mechanical — a review record's Fix lines already
name their sites in a fixed shape, and the fold commit is a single sha — and it reds on seven of the
eighteen defects here, including two of the four highs. It also closes the loop this build keeps
re-opening: round 1 found this class, prescribed "at all three sites" three separate times, and the fold
applied two of three each time. A prose instruction to apply a fix everywhere has now failed twice; the
third attempt should be a check.

Per charter §7, none of these five is landed until its failing case has been observed: stage the break,
confirm RED, unstage. Each has an obvious break available in this very diff.

**Three defects are not gateable** — D6, D11, D12 — and belong in the project's §10 recurring-bug-class
checklist as written manual checks: an exclusion quotes the record's own words; a disposition verb covers
every clause the cell quotes; a corroborating derivation is independent of what it corroborates.
