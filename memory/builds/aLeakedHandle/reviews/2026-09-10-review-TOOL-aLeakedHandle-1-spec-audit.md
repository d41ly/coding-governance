**Serves:** spec-audit TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3

# aLeakedHandle — Tier-2 spec audit, round 1

*Adversarial pre-code pass over the three-unit spec set for the unclosed-pipe fix, its gate, and the two ceiling-evidence repairs, at rev-1. Node `a`, 2026-09-10, base `013b1af9`. Every finding here is a defect in a document, not in shipped software — which is the point of running the pass before the first pass builds anything.*

**Range — ROUND 1**, three subjects pinned at these blobs: `memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-1.md@7461e62ecd4809807f52687e8e0984ac932ae9a2`, `memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-2.md@fe5e8bc1041342bc1bb655afec7e614bbb61137d`, `memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-3.md@090d4bea1bce8379ba3738705fe24103e9467839`.

## Verdict: BLOCKED

One blocker, and it is not a prediction. Unit 1 mints two new `gate-legs` inventory keys and names neither the codebase-map coverage ratchet in its §7 nor a single `memory/map/` path in its §4 files table; `compute_coverage` was run against the live map tree with those two names added and returns them as unclaimed. That leg carries no guard, so the unit lands red at the push boundary on a gate the spec never mentions, and the remedy is authored dossier prose rather than a mechanical regen. Four highs sit behind it, and three of them are the same shape: an acceptance criterion that cannot fail, or cannot be observed from the command it names. Unit 3 drew nothing.

### Review shape

Raw 40 · confirmed 12 · refuted 28 · unverified 0 · precision 0.30.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. No arm of this run failed to report, so the zero counts here are positive evidence rather than an absence of it, and the finding set is complete as far as four lenses reach. This run is complete.

Precision 0.30 is below the ~0.5 floor §8 sets. Read it as a signal about scope rather than about the specs: three tightly-written documents over a small, already-hardened area manufacture refuted noise, and a round 2 over the repairs should tighten the lens priming before it adds anything.

**Consolidation.** The twelve confirmed findings describe **ten distinct defects**. Two clusters merged: raw 27 and raw 39 are the same `cmd_write` contradiction seen from the criteria side and the data-model side, and raw 15 and raw 32 are two independent mechanisms breaking the same criterion (unit 2 AC5). Each row below carries its raw ids. Severities are the ones adjudicated HERE; a merged defect takes the maximum in its cluster, which promoted raw 39 (medium) into D3 and raw 32 (medium) into D4. Adjudicated totals across the ten rows: **1 blocker, 4 highs, 5 mediums, 0 lows.**

| # | Sev | Unit | Address | Defect | Raw ids |
|---|-----|------|---------|--------|---------|
| D1 | BLOCKER | 1 | §4 Files touched, §7 Gates | Two new leg names are two new inventory keys; the codebase-map coverage ratchet reds on them and the spec names neither the gate nor any `memory/map/` path | 35 |
| D2 | HIGH | 1 | §7 Gates against §6 AC8 | AC8's Red-when lives only in the two canaries, both `chunk: selftests` and held by the very bar AC8 tells the observer to run; §7 lists neither | 16 |
| D3 | HIGH | 2 | §4 Data model vs §4 Inventory, §6 AC1-AC5 | `cmd_write` never calls `read_legs`, the Data model says it always does, and no criterion drives `--write` at all | 27, 39 |
| D4 | HIGH | 2 | §6 AC5 and its `fixture:` line | AC5 cannot be observed as written: a sibling unit repopulates the UNBACKED line, and the fixture's own invocation produces no reading for the leg it names | 15, 32 |
| D5 | HIGH | 1 | §2 S6 and §6 AC9 | The sentence S6 sets out to falsify is about a construct this leg does not scan, so AC9 goes green only once a true coverage claim has been replaced by a false one | 36 |
| D6 | MEDIUM | 2 | §7 Gates, §6 AC4 | `run-gates evidence` is listed as a gate without the disclosure that no boundary runs it, so a held leg reads as a green one | 10 |
| D7 | MEDIUM | 2 | §2 S1 | S1's docstring clause claims observation by AC1, AC2 and AC5; none of the three reads the docstring, and §5 makes it the sole mitigation of a named hazard | 9 |
| D8 | MEDIUM | 1 | §3 Non-goals bullet 1, §4 Alternatives, §8 fork B | Three places size the deferred drain at "twenty edits in two files" against the same spec's table, which measures nineteen carried sites across six files in two kits | 18 |
| D9 | MEDIUM | 1 | §4 Inventory row 1 | The row names `py.function` as the cell grading a file basename; the cell for one is `py.file`, which `.lexicon.conf` does not arm, so the row's whole point is graded by nothing | 28 |
| D10 | MEDIUM | 1 | §6 AC2 | AC2's two halves belong to two different invocations — `check-unattended.sh` writes no ledger row and applies no ceiling | 29 |

---

## What this round found, in four sentences

**The set is close.** Ten defects across two units, every one repairable by a spec edit, none requiring a unit to be re-scoped or re-ordered. Unit 3 is clean as far as four lenses reached, and it is also the unit that models the honest form the other two need — its S4 is marked `NOT OBSERVED` with a reason, and its AC1 cost line discloses that `run-gates canary` sits in a chunk no boundary runs. Both of those forms exist in this build already; D2, D6 and D7 are all cases of a sibling not using them.

**The dominant class is the selftests chunk.** D2, D4 and D6 are three instances of one mechanism: a criterion or a gate list rides a leg whose `chunk` is `selftests`, `run-gates.sh` holds every such leg unless `GATE_SELFTESTS=1`, and the charter records that no boundary sets it. Verified against `tools/gate-legs.json` for all four legs involved — `run-gates canary`, `run-gates gov canary`, `run-gates evidence` and `memory-hygiene self-test` are every one of them `chunk: selftests`. A session reading §7 as its Definition of Done sees those legs held and scores the run green.

**The second class is the criterion that cannot fail.** D3 and D5 are it in its two purest forms. D3 leaves the one code path that produces the tracked artifact unobserved, so the changed call site can be omitted and every AC still passes. D5 is worse in kind rather than degree: its Red-when can only clear once somebody has written a coverage claim the leg does not back, into the gotcha record that exists to catalogue exactly that.

**Nothing here is about the fix itself.** The root-cause trace holds, the scratch-file feed in unit 1 S1 is the right shape, and the ceiling-admission rule in unit 2 S1 is the right rule. What the specs are missing is the machinery that would let anybody prove either one shipped.

---

## Blocker

### D1 — BLOCKER — unit 1 §4 Files touched (estimate), and §7 Gates

*Raw id 35.*

Unit 1 mints two new legs — `shell hygiene (a loop fed by a command substitution)` and `shell-hygiene selftest` — and adds them to `tools/gate-legs.json` in S5. Every leg name in that file is an entry in the `gate-legs` inventory, enumerated by `map_extractors.py:92`. Two new leg names are therefore two new inventory keys, and the codebase-map coverage ratchet refuses an unclaimed one.

**This is reproduced, not predicted.** `compute_coverage` over the live map tree returns clean today; with the two declared names added it returns `unclaimed: {'gate-legs': ['shell hygiene (a loop fed by a command substitution)', 'shell-hygiene selftest']}`. The leg that runs it, `codebase-map coverage + freshness`, carries **no `guard`** in `tools/gate-legs.json` — confirmed against the manifest — so it runs on every bar including the branch bar, and `baseline.toml` refuses new keys by its own header, which reserves additions for the initial backfill. The charter's Definition of Done already binds this: *new inventory keys claimed in the map tree (machine-enforced); claim edits regen the generated artifacts in the same commit*.

The spec names neither the gate in §7 nor any `memory/map/` path in §4. §5's risks bullet enumerates three other legs the unit might trip and misses this one, which is the tell — the author reasoned about gate exposure and this leg was not in the frame. The remedy is not mechanical either: `gate-lint` currently sits in `baseline.toml` with no dossier, so claiming these two keys means authoring dossier prose under `memory/map/features/` and regenerating `memory/map/generated/{MAP.md,inventories.json}`, not running a script.

**Fix.** Add `codebase-map coverage + freshness` to §7. Add the owning dossier under `memory/map/features/` plus both generated artifacts to the §4 files table. Add an acceptance criterion that runs `python3 tools/codebase-map/test_codebase_map.py` green with both leg names claimed, so the claim is observed rather than assumed.

**Left-shift gate.** The spec-side arm is small and this build is the second time it would have paid: for any spec whose §4 files table or §2 scope names `tools/gate-legs.json` as edited, assert that §7 lists `codebase-map coverage + freshness` and that §4 names at least one `memory/map/` path. No semantics, one join over two sections. The stronger version generalises it — derive which inventories a spec's declared file edits feed, and require the map gate in §7 whenever any of them is a claimed inventory.

---

## Highs

### D2 — HIGH — unit 1 §7 Gates, against §6 AC8

*Raw id 16.*

AC8's Red-when names *a guard naming an untracked path, which the run-gates canary refuses*. That refusal lives only in the two canaries, and both are `chunk: selftests` — `run-gates canary` and `run-gates gov canary`, verified in the manifest. `run-gates.sh:1228-1231` holds every `subject = kit OR chunk = selftests` leg unless `GATE_SELFTESTS=1`, and AC8 directs the observer to run `bash tools/run-gates/run-gates.sh`, which does not set it. §7 lists neither canary.

The hold's own comment at ~line 1222 says what holding them costs, in almost the words AC8 borrowed: the arms that catch a guard naming an untracked path, which would otherwise skip forever and silently. So the two new legs can land with a guard that never fires, on a unit whose entire subject is a leg that never moves. The omission is material rather than formal — `run-gates gov canary`'s guard names `tools/gate-legs.json`, which S5 edits.

**Fix.** Add both canaries to §7, and rewrite AC8's observation as `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, or as a direct run of the two suites. The default bar cannot observe the Red-when AC8 declares, and saying so is cheaper than discovering it at the lander.

**Left-shift gate.** Covered by D6's suggested arm — see there; one check closes D2, D4 and D6.

### D3 — HIGH — unit 2 §4 Data model vs §4 Inventory, against §6 AC1-AC5

*Raw ids 27, 39.*

Read at base, `derive-ceilings.py` splits three ways: `cmd_report` calls `read_legs` and `read_runs` at line 132, `cmd_check` calls `read_legs` only at 220, and `cmd_write` calls `read_runs` at 175 and **never calls `read_legs` at all**. Verified directly against the source.

§4 Data model asserts the ceiling comes from *the leg's `ceiling` in `tools/gate-legs.json`, which `read_legs` already loads for every command path that calls `read_runs`*. That is false about the one path it matters on. The same §4 Inventory contradicts it twice — *`cmd_write` gains one call to the existing `read_legs`*, and *one call site in `cmd_write`* — which is the tell rather than the cure: a spec whose two halves disagree about the source it was verified against will be read by whichever half the builder opened first, and the Data model paragraph is the one that decides whether any plumbing is needed.

The criteria then leave the path unobserved. AC1, AC2 and AC5 all drive `--report`; AC3 drives `--check`, which §4 Rollout itself says never calls `read_runs`. Nothing drives `--write` — the only path that produces the tracked artifact, and the path S1's admission rule exists to change. If `read_runs` takes the ceilings map with a default, which is the natural signature for avoiding a break at the second call site, `cmd_write` silently keeps its old ok-only behaviour and every criterion still passes green. That is §7's could-not-fail shape one level up: verified on the reporting path, unverified on the writing path. The merge bar does not catch it either, because `leg ceilings clear their evidenced maximum` runs `--check`, which reads only the two tracked files.

**Fix.** Delete the false clause from §4 Data model and say plainly that `cmd_report` already loads legs and `cmd_write` does not, so `cmd_write` acquires the `read_legs(root)` call — it already has `root` in its signature. Add an AC6 that runs the copied `--write` over the same fixture and asserts the written evidence row for the ceiling-reaching leg carries the failing row's seconds, with a Red-when naming the defaulted-parameter case explicitly.

**Left-shift gate.** The generalisable arm is a §4-vs-§6 path join: for every code path a spec's §4 Inventory lists as changed, require at least one criterion in §6 whose observation invokes it. Here that is one entry point (`--write`) against four criteria that invoke two others, and it needs no semantics beyond matching the subcommand token. Same arm reds D4's half of the same spec.

### D4 — HIGH — unit 2 §6 AC5, and its `fixture:` line

*Raw ids 15, 32. Two independent mechanisms, one criterion.*

AC5 requires `--report` to emit *no UNBACKED line at all*. Two separate things make that unobservable.

**The sibling unit repopulates the line.** `derive-ceilings.py:142-147` builds the UNBACKED list from every manifest leg with no admitted reading in the retained window, printed at 161-163. Unit 1 is `order 1` and its S5 adds two rows to the same manifest, so by the time unit 2 is verified both exist. One of them, `shell-hygiene selftest`, would be `chunk: selftests` and held on every default bar, so it acquires no reading without a deliberate `GATE_SELFTESTS=1` run and sits UNBACKED indefinitely. AC5's literal observation is broken by this build's own sibling, for a reason with nothing to do with unit 2's change — and the likely response is to waive the criterion, which is how an acceptance criterion stops being an observation. AC5's Red-when is narrower and partly rescues it, but the observation sentence is what an implementer runs.

**The fixture line's remedy does not restore it either.** `memory-hygiene self-test` is `chunk: selftests` with `guard: ['tools/lib/','tools/memory-tree/']`, confirmed in the manifest. A plain bar holds it at `run-gates.sh:1229-1230` (`printf 'ondemand' > "$WORK/$i.rc"; continue`), it never enters `runleg`, and no `.leg` row is written — so the reading AC5 needs comes only from a `GATE_SELFTESTS=1` run, which the criterion's *may have to run a bar* line does not say. Worse, `GATE_RUN_KEEP` defaults to 5 and prunes, so an ordinary bar both fails to produce the reading and evicts a retained run. And *no UNBACKED line at all* silently requires every selftests-chunk leg to still hold an admitted reading in that same five-run window, a precondition §4 never states.

**Fix.** Scope AC5's second clause to the leg it is actually about — *no longer names `memory-hygiene self-test` on the UNBACKED line* — and drop the absolute form. Change the fixture line to name the invocation that produces the reading (`GATE_SELFTESTS=1`, or `GATE_FULL=1 GATE_SELFTESTS=1`). Add a §3 Edges line recording that unit 1 adds legs to the same manifest, so the UNBACKED population is not this unit's to hold at zero.

**Left-shift gate.** A cross-unit population check: when one unit's criterion asserts a set is empty and a sibling unit at a lower `order` adds members to the same declared set, red. That is the mechanical half. The second half is D6's disclosure arm, which catches the fixture-line error.

### D5 — HIGH — unit 1 §2 S6, and §6 AC9

*Raw id 36.*

`memory/gotchas/bounded-through-a-pipe-is-unbounded.md:92-94` reads, verbatim, *Nothing sweeps other kits for `out=$(timeout`* and *Adding a repo-wide source scan is cheap and is not done here*. S6 mandates editing that record and AC9 red-whens on *the record still reads "Nothing sweeps other kits"*.

But `out=$(timeout N cmd)` is a plain assignment, and S3 scopes the new scan to a `while … done` loop whose input redirect is a heredoc or here-string holding a command substitution. This spec's own §4 population table puts every non-loop substitution — *Non-loop heredoc holding a command substitution*, *Non-loop here-string holding a command substitution* — **outside** the failing population. The new leg does not sweep for the class that sentence is about, so the sentence stays TRUE after the unit lands.

AC9 therefore reds on a correct record and can only go green once somebody has replaced a true coverage statement with a broader one nothing backs. Writing a false coverage claim into the note that exists to catalogue false coverage is the stale-claim class this repo audits for, aimed at its own catalogue. Separately, that same paragraph is a recorded decision *not* to build a repo-wide scan, and this unit reverses it without citing the reversal.

**Fix.** Rewrite S6 and AC9 to ADD a gating clause naming the new leg and the class it actually covers — loop-feeding heredocs and here-strings carrying a command substitution — while leaving the `out=$(timeout` sentence standing. Cite the *not done here* line in §4 as the prior decision this unit reverses, with the third occurrence as the reason.

**Left-shift gate.** Hard to gate mechanically and worth a §10 checklist entry instead: *when a unit's scope mandates editing a gotcha's gating section, the edited sentence must name the class the new leg's own predicate matches, not the class the incident was filed under.* The cheap mechanical proxy is a diff-time check that any edit to a `## Gating` section in `memory/gotchas/` names a leg that exists in `tools/gate-legs.json` — which would not have caught this one, and should not be sold as if it would.

---

## Mediums

### D6 — MEDIUM — unit 2 §7 Gates, and §6 AC4

*Raw id 10.*

§7 lists `run-gates evidence` as a gate without saying that no boundary runs it. It is `chunk: selftests`, `subject: kit` — verified — and `run-gates.sh:1228-1231` holds every such leg unless `GATE_SELFTESTS=1`, which the charter records no boundary sets (owner ruling, 2026-08-27). So the four arms guarding S1 bind at no merge bar. The only listed leg that DOES run at every boundary, `leg ceilings clear their evidenced maximum`, is `chunk: declarations` with argv `--check` — and §4 Rollout states `cmd_check` never calls `read_runs`. The changed predicate therefore has zero boundary-enforced coverage, and a session reading §7 as its DoD sees a held leg and scores it green.

This is the house norm, not a style preference: aHoistedPass-3, aSurfacedLexicon-6/11 and aGroundedOrientation-3 all disclose *chunk selftests, which no boundary runs* where their criteria ride such a leg, and sibling unit 3 discloses it for its own suite in AC1's cost line. Unit 2 is the outlier in its own build.

**Fix.** Add the same disclosure to §7 and to AC4 — the suite is run by hand, no boundary runs it — so a green bar is never read as covering the new predicate.

**Left-shift gate.** This is the arm worth building, and it closes D2, D4's fixture half and D6 together: for every leg name a spec's §7 lists, resolve it in `tools/gate-legs.json` and, when `chunk = selftests` or `subject = kit`, require the spec's §7 or the citing criterion to contain the invocation that actually runs it (`GATE_SELFTESTS=1` or a direct `bash <argv>`). Pure lookup, no semantics, and three of this round's ten defects are instances. `check-spec-tokens.py` already resolves §7 leg names against the manifest, so the join exists and only the chunk assertion is new.

### D7 — MEDIUM — unit 2 §2 S1

*Raw id 9.*

S1's docstring clause claims observation by AC1, AC2 and AC5. All three observe behaviour of `derive-ceilings.py` — fixture report rows, `max_s`, the live UNBACKED line — and none reads the module docstring. The clause is not decorative: §5 user-docs names the docstring as the ONLY place the admission rule is documented, and §5 risks makes it the sole mitigation of the monotone-floor hazard, *named in the docstring rather than discovered by the next reader*. So the mitigation can ship absent, or written without the slow/contended/hung ambiguity, with every named criterion green.

Sibling unit 3 has a form for exactly this case — its S4 is marked `NOT OBSERVED` with a reason — so the set is inconsistent about how an unobservable clause is declared, and this is an overclaim rather than a convention.

**Fix.** Split the docstring clause out and mark it `NOT OBSERVED` with its reason as unit 3's S4 does, or add a criterion asserting the module docstring states the ceiling-comparison rule and names what it cannot distinguish.

**Left-shift gate.** The §2-to-§6 join-lint: every criterion a scope item cites must share at least one content noun with the item's own text. *Docstring* appears in S1 and in none of AC1, AC2 or AC5, so a crude noun-overlap check reds it. This arm has been proposed by a prior audit corpus and keeps re-earning itself.

### D8 — MEDIUM — unit 1 §3 Non-goals bullet 1, §4 Alternatives, §8 fork B and its RESOLVED mark

*Raw id 18.*

Three places size the deferred drain as *twenty edits inside `check-unattended.sh` and `unattended.sh`* / *the two largest gate scripts in the tree*. The same spec's §4 measured table puts the twenty failing sites across seven files — `check-microformats.sh` 1, `check-verdict-epoch.sh` 2, `check-unattended.sh` 8, `lib-unattended.sh` 1, `unattended.sh` 6, `unattended.test.sh` 1, `check-memory-hygiene.sh` 1 — so only 14 of 20 sit in the two files named, and the carried drain is **nineteen across six files**, which is what §3's and fork B's own first sentences say. `git ls-files` confirms the spread crosses kits: `tools/check-microformats.sh` at the tool root, `tools/memory-tree/check-verdict-epoch.sh` and `check-memory-hygiene.sh` in the memory-tree kit.

Fork B's resolution rests on a blast-radius figure the spec body contradicts. The deferral itself survives — it is the right call — but the backlog row it mandates will be written from a count and a location the spec's own measurement disproves, and the next session will size the work wrong and look in the wrong two files.

**Fix.** In §3, §4 Alternatives and §8 fork B, write *nineteen sites in six files across the unattended and memory-tree kits* and point at the §4 table for the split, rather than restating a per-file count the table owns.

**Left-shift gate.** This is §6's *a value stated in prose beside the source that OWNS it rots* rule, inside a single document. The gate is a count-consistency lint: a bare integer in §3, §4 Alternatives or §8 that also appears as a column total in a §4 measured table must match it. Cheap, and it catches the twenty-vs-nineteen directly.

### D9 — MEDIUM — unit 1 §4 Inventory, row 1

*Raw id 28.*

`TEMPLATE-SPEC.md:125-126` defines the Inventory as naming each minted identifier beside the cell that grades it. Row 1 names `py.function` snake for `tools/gate-lint/sh_hygiene.py`, which is a file BASENAME — the cell for one is `py.file`. `.lexicon.conf`'s `CELLS:` block declares exactly four rows (`js.function camel`, `py.function snake`, `py.type pascal`, `sh.function snake`) and `PINS:` holds only `sh.function.conv 6`. Its own header records why: two cells were un-armed at the landing merge, `py.file` and `py.constant` grade every tracked file, and pinning them was refused.

So the correct answer for that row is `none` — the same answer its three sibling rows give — and the row's whole point (*UNDERSCORE, not the sibling's hyphen … adding a ninth grows a debt*) is graded by nothing. §7's `lexicon naming predicates` leg cannot fail on the basename, and an implementer who ships `sh-hygiene.py` to match the sibling reds no gate. §8 fork B compounds it by arguing from *the `py.file` pin* as a live precedent when no such pin exists.

**Fix.** Correct the row to `py.file` with a note that the cell is currently UN-ARMED per `.lexicon.conf`, so the underscore choice is a documented convention with no gate behind it. In fork B, attribute the *waiver wearing a ratchet's clothes* phrase to the `.lexicon.conf` comment rather than to a pin.

**Left-shift gate.** A cell-name lint on the Inventory: resolve every `<lang>.<surface>` token in a §4 Inventory row against `.lexicon.conf`'s `CELLS:` block, red on a cell the declaration does not arm unless the row also carries the word `UN-ARMED` or `none`. One lookup against a file the checker already reads, and it converts a false coverage claim into a refusal at authoring time.

### D10 — MEDIUM — unit 1 §6 AC2

*Raw id 29.*

AC2's two halves belong to two different invocations. `bash tools/unattended/check-unattended.sh` writes no ledger — `grep -c ledger` over it returns 0, and `gate-ledger.tsv` is set at `run-gates.sh:165` and written solely by the `if [ -n "$LEDGER" ]` block in that same script. Nothing else in the tree writes it. So *it emits a verdict AND the run's own gate ledger carries a seconds figure for the leg below its declared ceiling* cannot be observed from the command the criterion names. The 16040 s ceiling comparison exists only for a run driven through `run-gates.sh`, which is also the only run where the leg's `.leg` and ledger rows are produced.

Whoever runs AC2 gets a verdict and an absent ledger row, and then either records a green they did not earn or blames the change.

**Fix.** Split AC2. The direct `check-unattended.sh` run observes only *emits a verdict*; a second clause observes the ledger seconds from a `run-gates.sh` run scoped to the `unattended kit gate` leg, whose ceiling is 16040 and which carries no guard, so it runs on any bar.

**Left-shift gate.** Same family as D3's arm, from the other direction: a criterion naming exactly one command must be satisfiable by that command's own outputs. The mechanical proxy is narrow but real — if a criterion's observation names `gate-ledger.tsv`, `.leg` or a `ceiling`, require the invocation to be `run-gates.sh`, since those three artifacts have exactly one producer.

---

## Unit 3

**Zero confirmed findings.** All four lenses returned and none died, so this is evidence rather than an unreached corner — within the limit that four lenses over one short Tier-1 spec is a shallower sweep than the same four over two Tier-2 ones. Unit 3 is also the set's reference for two forms its siblings need: `NOT OBSERVED` with a reason on an unobservable scope clause (D7), and the *sits in chunk selftests, so no push boundary or default bar runs it* disclosure on a criterion that rides a held leg (D2, D6).

---

## The one gate this record would actually build

Three of the ten defects — D2, D6, and half of D4 — are the same class: **a spec's §7 or a criterion rides a leg that no boundary runs, and says nothing about it.** The arm is a lookup, not a judgement. For every leg name a spec's §7 lists, resolve it in `tools/gate-legs.json`; when its `chunk` is `selftests` or its `subject` is `kit`, require the spec to carry the invocation that actually runs it — `GATE_SELFTESTS=1`, `GATE_FULL=1`, or a direct `bash <argv>` — in §7 or in the criterion that cites it. `check-spec-tokens.py` already resolves §7 leg names against the manifest, so the join exists and only the chunk assertion is new. It would have reded three of this round's ten at authoring time, and the class is not local to this build: the house norm exists precisely because sessions keep rediscovering it by hand.

Second, and equally arithmetic: **the §4-to-§6 entry-point join** from D3 and D10. For every code path a spec's §4 Inventory lists as changed, require at least one §6 criterion whose observation invokes it. Matching a subcommand token is the whole implementation, and D3 — a spec whose one write path is graded by nothing while four criteria grade two read paths — is the shape it exists to catch.

Third, cheapest of all: **the count-consistency lint** from D8. A bare integer restated in §3, §4 Alternatives or §8 that also appears as a total in a §4 measured table must match it. One defect this round, and it is the repo's own *point at the source, or gate the pair* rule turned inward on a single document.

D1, D5, D7 and D9 are judgement calls dressed as lookups, and D1 in particular is worth a rule of its own rather than a gate: **a spec that declares an edit to a claimed inventory's source file owes the map gate in §7 and a dossier path in §4.** Everything else here is arithmetic.
