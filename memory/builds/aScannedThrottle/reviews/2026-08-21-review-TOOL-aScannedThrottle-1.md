## Verdict: CLEAN WITH FIXES
**Serves:** spec-audit TOOL-aScannedThrottle-1

Reviewed at run base `49aea26`, worktree `.claude/worktrees/unattended-ascanned-throttle-18a592`. Every claim below was opened against the tree at HEAD; every number was re-derived, not carried from the finder that raised it.

**This record is a `spec-audit` and does not discharge `closing-review-recorded`.** That DoD item (`tools/unattended/unattended.sh:1801-1825`) needs a tracked `diff-review` record naming the pinned base, and M8 forbids one standing in for the other.

## Lenses run

Five finder lenses over the spec, the build README, the report and the tree — underspecification, contradiction, unstated assumption, prior art, and scope-vs-artifact reconciliation — then a skeptic prompted to REFUTE each finding against the bytes, then this synthesis. **8 of the raised findings were refuted and are not carried here.** The refuted set clusters on one shape: lenses repeatedly claimed that a witness "exists in no tree" (AC1's readers, AC2's simulator, AC5's green bar) without crediting spec:43-45, which declares all three readers throwaway and uninstalled up front. Disclosed absence is not a gap, and four separate findings died on that.

Findings that survived are consolidated — six lenses independently filed the S5 backlog defect, and it is ONE finding, counted once.

---

## Confirmed findings

### F1 · HIGH — S5's reconciliation was written in the report and never applied to the backlog

`memory/builds/aScannedThrottle/spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md:21-22` puts "the reconciliation of every open backlog row about bar performance" IN scope. The report's §5 table at `memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:490-499` dispositions eight ids. None of them reached `memory/backlog/TOOL.md`.

`git show --numstat d16f96c -- memory/backlog/TOOL.md` returns `7  0` — seven insertions, zero deletions, a pure append of the new rows at the `@@ -137,3 +137,10 @@` hunk. The same commit's message asserts it "Ships the report, the spec, seven TOOL-aScannedThrottle rows, and eight reconciled existing rows." Its own diff contradicts the last clause. `git diff d16f96c..HEAD -- memory/backlog/TOOL.md` touches exactly one of the eight, `TOOL.md:58`, and only to insert the word "two" in an unrelated commit.

Row by row, at HEAD, with the report's contradicting verdict beside it:

| backlog line | still says | report says |
|---|---|---|
| `memory/backlog/TOOL.md:47` | `TOOL-aTimedTurnstile-1 · OPEN` | report:498 **CLOSE** — "False at HEAD" |
| `memory/backlog/TOOL.md:12` | "88 rows against 85 legs, 3 orphans holding 965s" | report:494 "0 orphans, 88 rows against 88 legs" |
| `memory/backlog/TOOL.md:11` | "786 dirs" | report:495 "**1053** … +34 %" |
| `memory/backlog/TOOL.md:10` | "not contention" | report:493 "does not survive §3.8" |
| `memory/backlog/TOOL.md:13` | cites `AGENTS.md:492`, "335s serial" | report:496 measured mean **1001.3 s** (see F13) |
| `memory/backlog/TOOL.md:14` | no R1 binding | report:497 "**KEEP OPEN, bind to R1**" |
| `memory/backlog/TOOL.md:58` | no reproduction note | report:499 "did not reproduce … spread is 25.9 %" |
| `memory/backlog/TOOL.md:123` | "floor is ~660s at any width" | report:492 "Re-stamp to the crossover target of ~766 s" |

**Why it matters.** AGENTS.md §6 makes the backlog the mutable record whose "status is updated in place". The backlog is what the next session greps; a build journal is not. A row the measurement proved false at HEAD is still advertising itself as an open lever, and `python tools/drift-audit/drift_report.py` counts it: `live_backlog_rows_per_shard 128 of 4 — out of tolerance`.

The corpus does apply row-level reconciliations in place — the same `d16f96c..HEAD` diff shows `TOOL-aTetheredScratch-4` gaining a dated in-place note and seven `aTetheredRecord` rows flipped INPROGRESS→CLOSED. And `memory/builds/aDeclaredCeiling/spec/2026-08-16-spec-PLAY-aDeclaredCeiling-1.md:20-22` states the convention outright: a row "moves to CLOSED with the measurement, because a row that says 'record the refutation' is not discharged by recording it somewhere else and leaving the row open."

**Fix.** Apply the eight dispositions to `memory/backlog/TOOL.md` in one commit, each citing the report section that measured it: flip `:47` to CLOSED with report:498's reason, re-stamp `:10`-`:14` and `:123` to the measured figures, add the note to `:58`. Re-run `bash tools/memory-tree/check-memory-hygiene.sh` — it exits 0 on the current tree, so a red after the edit is yours. Do not rewrite `d16f96c`; correct its false "eight reconciled existing rows" claim with a note in the build record.

**Scope.** spec:26-29 bars edits to `run-gates.sh`, `gate-legs.json`, `gate-profiles.txt` and `*.test.sh`, and says nothing about the backlog. `README.md:35-36`'s non-goal is about landing the recommendations. Neither reaches this edit.

---

### F2 · HIGH — §9's closing condition names a state only other builds and the owner can produce

`spec:105`: "Close it when the rows it minted are dispositioned." The minted rows are `memory/backlog/TOOL.md:144-150`, all seven `· OPEN ·`.

| row | what dispositioning it needs | barred by |
|---|---|---|
| `TOOL.md:144` (-1) | ledger read changed in `run-gates.sh` | spec:26 |
| `TOOL.md:145` (-2) | a `queued` key at `run-gates.sh:708-737` | spec:26 |
| `TOOL.md:146` (-3) | `New-MpPerformanceRecording` with admin | spec:28, and no agent has admin |
| `TOOL.md:147` (-4) | HVCI enablement date — "Owner's setting, not an agent's" | spec:28 |
| `TOOL.md:148` (-5) | edits to `run-gates.test.sh` | spec:26 |
| `TOOL.md:149` (-6) | folded into a future sharding estimate | `TOOL-aPacedTurnstile-8`'s work |
| `TOOL.md:150` (-7) | regrade `run-gates.evidence.test.sh:225` | spec:26 |

`README.md:35-36` seals it: "landing any of them is a separate unit." Two of the seven are outside ANY unattended run's reach, not merely this one's.

The cost is mechanical, not philosophical. `README.md:45` renders the sole unit `OPEN`; `tools/unattended/unattended.sh:1061` defines `nonterminal_units()` as rows not matching `| (CLOSED|WONTDO) |`; `:1794-1797` fails the DoD item with "a unit of this build is not terminal, so the build is not done". `build-complete` is in `DOD_CORE` at `unattended.sh:93` and is machine-verdicted. So the item is permanently unmeetable and every run carrying this build owes `--override build-complete` — which `unattended.sh:1762-1764` itself calls "the run authorizing itself past the one item that means the build is done."

Prior art that this is fixable, not fatal: `PLAY-aDeclaredCeiling-1` is a records-only unit that closed on having MADE its record edits, not on anyone acting on them.

**Fix.** Rev the spec to rev-2 with its §9 line and replace the closing condition with one this unit's own records can satisfy and a later reader can verify — the §5 dispositions applied to the backlog (F1), every minted row cited by report §4 (F10), and the §5 population made derivable (F4). Keep the seven rows as forward pointers in §3, never as the close gate.

**Also fold into that rev:** `spec:3` reads `**Status:** OPEN` while `spec:101` says "The measurement is complete". `memory/TEMPLATE-SPEC.md:48` fixes `OPEN` as "drafting" and offers `BLOCKED` and `DEFERRED` for a complete-but-parked unit. Note honestly that flipping to BLOCKED buys the run nothing — `unattended.sh:1794-1797` fails on any status "neither CLOSED nor WONTDO" — so do it as a truthfulness fix, not as an exit.

---

### F3 · HIGH — "dispositioned" is defined nowhere, so §9's condition has no evaluable predicate

`grep -rn "dispositioned"` across the repo, excluding `.git`, returns **exactly one line**: `spec:105`. It is a hapax — not merely undefined but used nowhere else, so there is not even a corpus usage to infer from. The related noun "disposition" appears ~30 times, all in `aBoundedVerdict` prose, and always means what a RUN does at a decision point, never a property a backlog ROW acquires. The available vocabulary is closed and does not contain it: `memory/backlog/TOOL.md:3` says each row leads with one status token, and `memory/HYGIENE.md:86` fixes that set as `OPEN · SPECCED · INPROGRESS · BLOCKED · DEFERRED · CLOSED · WONTDO`.

This is why F2 cannot be resolved by a run's judgement call. Under a loose reading ("triaged") the condition was met at mint; under a strict one ("landed") it is unsatisfiable. `memory/guides/BUILD-METHOD.md:239` forbids asking: "there is nobody to answer, so a question is a stall."

**Fix.** In the same rev-2, state the closing predicate in the corpus's own status tokens, naming the file the reader checks it against.

---

### F4 · HIGH — S5 says "every open backlog row about bar performance" and delivers a hand-picked eight; four qualifying open rows are missing

`spec:21-22` declares the population with the word "every" and defines no membership predicate. The §5 table at report:490-499 holds eight ids. Absent from it, OPEN in `memory/backlog/TOOL.md`, and squarely about the bar's wall clock:

- `TOOL.md:48` (`TOOL-aTimedTurnstile-2`) — "29 of 47 legs are SELF-TESTS holding 96.7% of wall (368.7s)", measured stale by this build's own 88-leg / 5144-leg-second figures.
- `TOOL.md:49` (`TOOL-aTimedTurnstile-3`) — "the floor is the longest leg UNDER LOAD (~76s)". The report puts the floor at ~900 s and R2 (report:379-396) makes sharding the route, not the fixture sharing this row prescribes. The report even engages it at report:336 — "confirms `TOOL-aTimedTurnstile-3`'s 1.66× figure" — and reconciles it into a NEW row (`TOOL.md:149`) while leaving the refuted floor figure standing.
- `TOOL.md:50` (`TOOL-aTimedTurnstile-4`) — "cold/warm is 1.59x … Defender exclusions are a no-code lever". Report:301-306's whole `2026-08-11 baseline` column is taken from this row's figures, R4 at report:418-419 rests its Defender refutation on that anchor, and report:505-506 names the row as unverified. Engaged three times, dispositioned zero.
- `TOOL.md:51` (`TOOL-aTimedTurnstile-6`) — "a poll tick is a PROCESS here (75ms per 50ms sleep, 317s of a 617s run)".

A scope item that says "every" and delivers a curated list cannot distinguish a complete reconciliation from a partial one — an omission is indistinguishable from a judgement call.

**Fix.** Add the four rows to report §5, and write the membership predicate into S5 so the set is derivable rather than authored: e.g. *every OPEN row in `memory/backlog/TOOL.md` whose text names the bar's wall clock, leg timings, pool width, spawn cost or scratch cost.*

---

### F5 · MEDIUM — §9 treats drift signal 6 as unanswerable while the same tool ships an exemption for exactly this shape, and the exemption carries an atomicity trap the spec does not record

§9's factual premise is TRUE and I measured it. `TRACE_GLOBS` at `tools/drift-audit/drift_signals.py:58-63` is `tools skills coding-governance-agents.template.md WIRE-INTO-PROJECT.md`; `d16f96c` touches none of them; `python tools/drift-audit/drift_report.py` reports `closed_specs_with_no_product_commit 1 of 150 — ok (pin 1, drain it)`, so a bare close takes it to 2 against pin 1 and reds the `drift-audit records` leg.

What §9 never mentions is that the signal documents its own escape for this exact shape. `tools/drift-audit/drift_report.py:554-556`: "Two shapes reach it — **a unit whose deliverable is records-only**, and a unit whose product landed BEFORE the id-in-subject convention". This unit is the first shape verbatim (spec:55, "reads records, writes one report and one backlog block"; spec:113, "Nothing was built to ship"). The registry `memory/project/trace-waiver.txt` exists and carries six live rows.

**The trap the spec does not record, and it is load-bearing.** `drift_report.py:581` restricts the population to TERMINAL specs; `:599-601` consumes a waiver row only for a spec that is present, terminal and untraceable; `:605-611` turns any leftover row into a suspect of its own. Adding the waiver row while the spec is still OPEN therefore drives the signal to 2 and reds the leg it was added to keep green. **The row and the status flip must land in one commit or neither.**

One objection I checked and cleared: `trace-waiver.txt` is SHRINK_ONLY (`drift_signals.py:81`), but signal 3 is `gateable: False` and already reads `3 of 5 — out of tolerance (report only)`, so a new row changes no gate verdict.

One correction to what the lenses claimed: there is no records-only precedent row yet. All six existing rows are the SECOND shape — `trace-waiver.txt:20` says so of the five seed rows, and `:31`'s `TOOL-dSettledRoster-5` reason is "record written AFTER the work landed … so no product subject could name a slug that did not exist yet." This unit would be the first of its kind, which argues for stating it as a decision rather than making it silently.

**Fix.** Add a §9 line in rev-2 naming `memory/project/trace-waiver.txt`, `drift_report.py:552-556`, and the one-commit atomicity constraint. Note that the waiver answers only §9's second reason; its first — "a terminal status would assert that something shipped" — is a semantic objection the waiver does not touch, though `memory/TEMPLATE-SPEC.md:50` defines CLOSED as "built and landed" and the report did land.

---

### F6 · MEDIUM — `TOOL-aScannedThrottle-1` is allocated twice, to two unrelated subjects

`spec:1` — `# TOOL-aScannedThrottle-1 — measure the lander…` — claims the id for the measurement unit. `memory/backlog/TOOL.md:144` opens `- TOOL-aScannedThrottle-1 · OPEN · the dispatch hint is stored PER-WORKTREE…`. Two different subjects, one string. The mint error is visible at report:501: "New rows to mint: `TOOL-aScannedThrottle-1` … `-5`" — the backlog range was started at -1 while the spec already held it.

**One id in two documents is not per se a defect here** — `memory/HYGIENE.md:186-188` carves out a decision-log row plus its spec H1 by design, and `TOOL-aPacedTurnstile-14` is both `memory/backlog/TOOL.md:130` and a spec H1, which is a backlog row promoted to a unit: one referent, no ambiguity. What makes this one a defect is that the two carry unrelated subjects.

**The corpus precedent is the sibling measurement build, same node and same day.** `memory/builds/aMeteredTurnstile/spec/2026-08-20-spec-TOOL-aMeteredTurnstile-1.md` holds `-1`, and every backlog row that build minted starts at `-2`. Same for `aTimedTurnstile`. AGENTS.md §2's rule ("next = numeric max of YOUR ids in that family + 1") makes this build's backlog range owe `-2..-8`.

The live consequence is at report:357, where R1's trailing citation `TOOL-aScannedThrottle-1` resolves to the spec that produced R1 as readily as to the row R1 is about.

Nothing gates it: hygiene check 13's test is "claimed by two build folders" (`HYGIENE.md:186-188`), and `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over the tree holding the collision.

**Fix.** Re-mint the backlog row as `TOOL-aScannedThrottle-8`, update the citation at report:357, and log the re-mint in §9. If the double-booking was deliberate, say so in §9 in as many words.

---

### F7 · MEDIUM — AC1 is unmet: throughput is reported for no run, and the fourth run's row is blank

`spec:72-74` requires the reconstructor to report "span, floor, **throughput** and utilization per run and names which bound binds, **for every run holding `.leg` rows**."

Report §2's columns at `:35` are span / leg-seconds / floor / utilization / packing / verdict. **No throughput column.** Grepping all 513 report lines for `throughput` returns `:24` (the tool's capability blurb), `:165-168` and `:172`, `:389`, `:454` — every one of those a bound LABEL or an adjective, never a per-run rate.

`report:40` is `| 16:05 | *in flight while this was written* | | | | | |` — six empty cells — under a heading at `:31` that claims "What four real bars measure". That run does hold `.leg` rows: report:230 enumerates its per-leg statuses at head `e6098aa43`, and report:509 counts it in "the four-run sample".

Yet the fourth span is derivable from the report's own arithmetic: report:381 gives "292 s (27.6 %) on run 130546", so 292 / 0.276 = 1058 s, and 4 × 1001.3 − (970.0 + 925.5 + 1051.4) = 1058.3. The number exists; the row does not.

This is the could-not-fail shape AGENTS.md §7 warns about: an acceptance criterion graded against a table that does not carry the column it names, and `spec:101` grades it met.

**Fix.** Add the 16:05 row (span 1058 s) and a throughput column to report §2, or rev AC1 to state what was actually measured and why the fourth run was left out. The run records for those bars are gone — `<git-dir>/gate-run/` on node `a` now holds only `20260820T163240Z-457` onward — so the row must be filled from report:381's arithmetic or marked unrecoverable in place.

---

### F8 · MEDIUM — AC4 is not met by the artifact it names, yet §9 grades every §6 criterion met

`spec:81-83` (AC4) requires every recommendation to carry "a span figure in seconds or an explicit zero". Five comply: R1 report:357 "~160 s (15.6–16.3 %)", R2 :381 "292 s", R3 :400 "0 s of span", R5 :434 "0 s directly", R6 :449 "0 s today".

`report:409` reads exactly: `**Buys UNQUANTIFIED, and the honest answer is probably less than you would hope.**` That is neither a figure nor an explicit zero. The report also breaks its own stated rule at `report:353`: "**Every entry states what it buys in seconds of span, or states zero.**"

`spec:101-102` nevertheless asserts "every §6 criterion is met". The self-grade is wrong on the one criterion any reader can re-check in thirty seconds, which is why a run inheriting this build should not treat the other §6 verdicts as load-bearing.

**Fix.** Either price R4 — report:425-430 already names the `New-MpPerformanceRecording` step that would do it — or state an explicit `0 s until measured` and move the estimate into the §6 limits. Then correct §9's blanket grade.

---

### F9 · MEDIUM — the build has no spec-audit and no closing-review record, and its own generated README says so

`find memory/builds/aScannedThrottle -type f` returns exactly four files: `README.md`, `RUN.md`, the spec, the build journal. There is no `reviews/` directory, and `git ls-files | grep -i ascannedthrottle` returns the same four paths.

`README.md:54`, inside the generated `gen:build-index` region, states it: "Ids no `spec-audit` record has ever named: TOOL-aScannedThrottle-1."

Both obligations bite. `memory/guides/BUILD-METHOD.md:86` defines unreviewed as "every spec with no review record naming it", and `:102-106` requires the record under `memory/builds/<slug>/reviews/` carrying `**Serves:** spec-audit <ids>`. Separately, `closing-review-recorded` is in `DOD_CORE` at `tools/unattended/unattended.sh:93` and `:1801-1825` requires a **tracked** `diff-review` record naming the run's pinned base at a seven-char prefix — `memory/builds/aScannedThrottle/RUN.md:20` pins `49aea26a…`, and nothing on disk can satisfy it today.

Note the report's citation at `:351` of "a five-lens adversarial pass … 55 findings; 28 survived" and at `:511-513` that the 27 refuted "are in the workflow journal, not in this report". No such journal is tracked. That pass was a findings fan over the MEASUREMENT, not an M4 spec audit and not an M8 diff review, so recovering it would discharge neither obligation.

`README.md:54` is informational — grep for `spec-audit` in `tools/memory-tree/check-memory-hygiene.sh` returns nothing, so this reds no leg today.

**Fix.** Land this record at `memory/builds/aScannedThrottle/reviews/2026-08-21-review-TOOL-aScannedThrottle-1.md`, per HYGIENE check 5's `<date>-<kind>[-<FAMILY>]-<slug>-<seq>.md` grammar, with the `## Verdict:` line and the `**Serves:** spec-audit TOOL-aScannedThrottle-1` binding line. Records-only, inside scope. The closing `diff-review` is a separate record and a separate obligation.

---

### F10 · MEDIUM — report §5's mint list undercounts by two, and one uncounted row has no measurement behind it anywhere

`report:501` reads "New rows to mint: `TOOL-aScannedThrottle-1` … `-5`, per §4." Seven landed at `memory/backlog/TOOL.md:144-150`, and `d16f96c`'s message says "seven TOOL-aScannedThrottle rows".

Row `-6` (`TOOL.md:149`, legs dilate 1.5–1.85× in the pool) is at least sourced — report:334-336 carries the figure. Row `-7` (`TOOL.md:150`) is not: grepping the report for `evidence.test`, `KILL 5`, `5-second` and `:225` returns **zero hits**. So `run-gates.evidence.test.sh:225`, its `timeout -s KILL 5` bound and the 2136 ms measurement in that row exist only in the backlog, in a corpus whose §7 rule is that a number is derived from the source that owns it.

I checked and am **refuting** the related claim that `-7` contradicts report §3.5. Report:234 ("each failed exactly once, at different commits") is scoped to the four reconstructed `GATE_FULL` bars tabled at :226-229; `-7`'s "failed both scoped bars run from this worktree today" is a different population, and the row calls itself "load-dependent, not base-deterministic", which agrees with §3.5 rather than opposing it. No contradiction to reconcile — but §3.5 never says the two populations differ, so a later reader has to work that out unaided.

**Fix.** Extend `report:501` to `-1 … -7` and give `-6` and `-7` a one-line home each. Both are 0 s of span — a correction factor and a load-dependent red — so they belong under §3 with §5 pointing at them, not in the R-ranking. Add one clause to §3.5 naming the population it sampled.

---

### F11 · MEDIUM — a backlog row this build declined to fix cites an `AGENTS.md` line and quote that no longer exist, and `AGENTS.md` still names a dead file as the live scheduling input

Two halves, both at the bytes.

`memory/backlog/TOOL.md:13` reads: ``AGENTS.md:492 claims "335s serial to ~95s at width 8"``. `grep -n "335s" AGENTS.md` returns **nothing**, and `AGENTS.md:492` is now "**How the bar behaves**, because none of this is derivable from the manifest…". The live numbers the row means are at `AGENTS.md:498` — "the full bar costs 873 s of wall clock against a 4018 s leg-sum" — which is exactly what report:496 refines to a measured mean of 1001.3 s. Following the row today leads to prose that is not the defect.

`AGENTS.md:496` reads "scheduled longest-first from a timing cache at `<git-dir>/gate-timings.tsv`". `tools/run-gates/run-gates.sh:155` sets `LEDGER="$gd/gate-ledger.tsv"` and `:158` sets `TIMINGS="$LEDGER"`; `run-gates.sh:963` states "It replaces the old `gate-timings.tsv` rather than sitting beside it". report:494 independently calls it "the dead `gate-timings.tsv`, which nothing reads." **The charter names a dead file as the live dispatch input — the subject of this build's own headline finding.**

**Fix, split by authority.** Re-citing `TOOL.md:13` at `AGENTS.md:496` and `:498` with their live quotes and the 1001.3 s measurement is records-only and inside scope; it is part of F1's edit. Editing `AGENTS.md` itself is a governance carrier and `BUILD-METHOD.md` M3 veto 2 — an owner turn. Raise it, do not do it.

---

### F12 · LOW — report:509's span range has an upper bound that appears in no table and contradicts the README shipped in the same commit

`report:509` reads "Spans 925–1058 s and utilization 59.8–69.5 %". §2's table tops out at 1051.4 s (`report:39`) and its fourth row is blank, so nothing in §2 sources 1058. `README.md:22`, landed in the same commit, says "spans of 925–1051 s"; `report:195` says "925–1051 s".

The 1058 figure is **correct** — see F7's arithmetic from report:381 — which makes `README.md:22` the outlier, not report:509. But `spec:62`'s own observability line says "every number in the report names the run it came from", and 1058 names none.

**Fix.** Fill `report:40` with the 16:05 run's figures (which is also what F7 needs) and correct `README.md:22` to 925–1058. One number, one source.

---

### F13 · LOW — §8 sends a reader to one backlog row for two carried-forward limits; that row carries one

`spec:94-97`: "Two things it could not establish (the cold/warm factor at the current leg count, and the real distribution of turnstile queue wait) … are carried forward by `TOOL-aScannedThrottle-2`."

`memory/backlog/TOOL.md:145` (`-2`) covers the turnstile queue wait only — "printed to stdout at `run-gates.sh:518` and recorded NOWHERE". The cold/warm limit is held by `TOOL-aTimedTurnstile-4` at `TOOL.md:50`, which is the row `report:505` itself names.

**Fix.** Name both rows in §8, matching report:505-506.

---

## Refuted — 8 findings

Not carried, and worth naming because they share one error. Four claimed that AC1, AC2, AC3 or AC5 "name witnesses that exist in no tree" without crediting `spec:43-45` and `report:20`, which declare all three readers throwaway, uninstalled and scratchpad-resident up front. Disclosed absence is not concealment. The others: that AC2's tolerance is stated nowhere (it is, at report:82-83); that §2 fails TEMPLATE-SPEC's verifiability rule (three of five items are plainly verifiable on disk); that the id collision breaks drift signal 6 (it joins on slug, not seq — `drift_report.py:591-597`); and that the seven-row closing set is unenumerable (`git grep 'TOOL-aScannedThrottle-' memory/backlog/TOOL.md` answers it in one command, and `README.md:7` is generated from the roster by `gen_build_index.py:827-843`).

---

## The two questions, answered directly

### (a) Is §9's closing condition actionable by a run bound to this build's declared scope?

**No.** It names a condition only other builds and the owner can satisfy. See F2 for the row-by-row mapping and F3 for the undefined predicate. The condition is unsatisfiable by ANY unattended run, not merely one bound to this scope, because `TOOL.md:146` and `:147` need admin and an owner decision that `spec:28` names in as many words.

### (b) Is anything in §2 (S1..S5) not yet on disk?

| item | state | evidence |
|---|---|---|
| S1 (spec:13-14) | **PARTIAL** | report §2 covers 3 of 4 runs; `report:40` blank; throughput reported for no run (F7) |
| S2 (spec:15-16) | ON DISK | report:82-83 fit +0.0 %, self-refusal −15.6 %; readers declared throwaway at spec:43-45 |
| S3 (spec:17-18) | ON DISK | report:265-296, 99.9 % attributed against AC3's 95 % floor |
| S4 (spec:19-20) | ON DISK | report:297-319, four spawn ops re-measured on a quiet box |
| S5 (spec:21-22) | **HALF ON DISK** | the report exists; the reconciliation was written at report:490-499 and never applied to `memory/backlog/TOOL.md` (F1), and its population is under-covered by four rows (F4) |

**S5's second half is the only unfinished scope item, and it is the only one a run bound to this build can land.**

---

## What a run bound to this build's declared scope MAY do next

All records-only. None of it lands a recommendation, so `README.md:35-36`'s non-goal does not reach any of it.

1. Apply report §5's eight dispositions to `memory/backlog/TOOL.md` in one commit (F1). Re-run `bash tools/memory-tree/check-memory-hygiene.sh`; it exits 0 today.
2. Extend report §5 to the four omitted open rows and write S5's membership predicate into the spec (F4).
3. Rev the spec to rev-2 with its §9 line: replace the closing condition (F2), state the predicate in the corpus's status vocabulary (F3), correct the §6 self-grade (F8), name both carried-forward rows in §8 (F13), and record the trace-waiver option and its one-commit atomicity constraint (F5).
4. Correct the report's bookkeeping: extend the mint line to `-7` and home rows `-6` and `-7` (F10); fill `report:40` and reconcile `README.md:22` to 925–1058 (F12, F7); re-cite `TOOL.md:13` at the live `AGENTS.md` lines (F11).
5. Re-mint the colliding backlog row as `TOOL-aScannedThrottle-8` and fix the citation at report:357 (F6).
6. Land this record under `memory/builds/aScannedThrottle/reviews/` (F9).

## What it MAY NOT do

- Touch `run-gates.sh`, `gate-legs.json`, `gate-profiles.txt` or any `*.test.sh` — `spec:26`.
- Shard the unattended selftests — `spec:27`; that is `TOOL-aPacedTurnstile-8`.
- Add a Defender exclusion or change Memory Integrity — `spec:28`; admin, and the owner's call.
- Edit `AGENTS.md` to fix the dead `gate-timings.tsv` reference — a governance carrier, `BUILD-METHOD.md` M3 veto 2, an owner turn. Raise it in the backlog instead.
- Add a `trace-waiver.txt` row on its own, or flip the status without one. The two are safe only as a single commit (F5), the waiver's first records-only instance is a decision worth surfacing, and this repo has never made one before.
- Treat `--override build-complete` as the fix for F2. The override exists; the defect is §9, and §9 is editable inside scope.
