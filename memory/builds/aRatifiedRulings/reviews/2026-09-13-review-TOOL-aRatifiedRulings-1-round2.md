**Serves:** spec-audit TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4

# Tier-2 spec audit — the `aRatifiedRulings` spec set, round 2

Written 2026-09-13 on node `a` by the tier2-review harness (`tools/workflows/tier2-review.js`): four primed finder lenses, an adversarial skeptic per finding, one synthesis pass. Subject: the four SPECCED units of `memory/builds/aRatifiedRulings/` at rev-2, after the round-1 fold landed in `97f6b915`, read at the blobs named on the range line and against the tree at `97f6b915` for every source claim (the build's pinned base is still `16da4c6a`; the two trees differ only under `memory/builds/aRatifiedRulings/`).

Reviewed subjects, pinned: `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-1.md@558511dcbd83fc4d74cb56f12be1e0a5d25d0154` · `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-2.md@5397081955bd030b841e6dc264d14f08922816bd` · `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-3.md@d10f146cb518c543c90c42a398ddf425fd56c11a` · `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-4.md@2726fc5490ce06256252733b7e92401bca212d61` · ROUND 2.

## Verdict: CLEAN WITH FIXES

The round-1 blocker is gone: units 1 and 2 now give one owner for the `KIT_UNATTENDED_VERSION` bump, the closing pass, and no two specs contradict each other on a shared constant. What remains is three defects at HIGH, each of which makes a criterion or a licence fail against a correct build of its own spec and each of which is repairable inside that spec: unit 1's AC7 join both reads red as spelled and cannot fail once spelled correctly; unit 4's AC5 stub reds the canary suite's own unguarded `timeout` calls; and the concurrency licence in unit 1 §4 and unit 2 §3 is one the dispatch driver refuses for the ordinary pass shape. Seven MEDIUM and five LOW ids follow, all edits in place. Nothing here needs the owner; every fix is derivable from the sources the specs already cite.

**Review shape:** raw 28 · confirmed 18 · refuted 10 · unverified 0 · precision 0.64.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every lens and every skeptic batch came back, so the finding set is complete for the lenses that ran and a zero count below is positive evidence rather than an artefact of a dead lens. The pipeline's duplicate pass found none; the clustering below is this report's own, because several confirmed ids state one defect from different lenses and the fix is written once per defect. The per-id table keeps all 18 rows so the counts returned to the caller agree with what was adjudicated here.

**Adjudicated severities:** BLOCKER 0 · HIGH 6 · MEDIUM 7 · LOW 5. The six HIGH ids are three defects (clusters A, B, C); the seven MEDIUM ids are six defects; the five LOW ids are five.

Severity meaning in this record, unchanged from round 1: BLOCKER — the set cannot be dispatched as written, a cross-unit contradiction the roster must settle before any pass starts. HIGH — a unit lands red, a criterion cannot be observed, or a licence the spec grants is refused by the driver, under a correct build of its own spec; fixable inside that spec. MEDIUM — a premise or an observation is false against source, so a reader acting on it does the wrong thing, but a build can still land green by luck or by discovering it at the bar. LOW — a figure, a quoted form or a sentence does not reproduce; no verdict changes.

Where a lens and this report disagree on a severity, this report's adjudication stands and is stated in the cluster. Ids 8 and 24 were filed MEDIUM and are HIGH here because they are the same defect as id 1 and a defect has one severity; id 18 was filed MEDIUM and is HIGH here for the same reason against id 17.

---

## Per-id severity table

| id | severity | unit | address | cluster |
|----|----------|------|---------|---------|
| 1 | HIGH | 1 | §6 AC7 join · §2 S5 | A |
| 8 | HIGH | 1 | §6 AC7 join · §2 S5 | A |
| 24 | HIGH | 1 | §6 AC7 join, the `diff-tree` spelling | A |
| 17 | HIGH | 1 | §4 Rollout, write-set paragraph | B |
| 18 | HIGH | 2 | §3 "No sequencing with unit 1 is owed" · §3 "Nothing else leaves the population" | B |
| 16 | HIGH | 4 | §6 AC5 · §4 "Measured 2026-09-13 on this host" | C |
| 9 | MEDIUM | 1, 4 | U1 §4 Rollout · U4 §4 Rollout | B |
| 3 | MEDIUM | 2 | §2 S4 · §4 "The arm" Red-first · §6 AC3, AC4 | D |
| 4 | MEDIUM | 4 | §2 S3, the `FLOOR_ASSERTIONS` clause · §6 (no AC) | E |
| 11 | MEDIUM | 1 | §6 AC4, positive-artifact clause | F |
| 21 | MEDIUM | 1 | §6 AC4, positive-artifact clause | F |
| 23 | MEDIUM | 2, 1 | U2 §8 F1 RESOLVED · U1 §3 Edges, first hands-off bullet | G |
| 25 | MEDIUM | 4 | §3 `KIT_RUN_GATES_VERSION` bullet, against U1 §8 F2 | H |
| 10 | LOW | 1 | §6 AC7, `figure` paragraph | A |
| 13 | LOW | 1 | §7 chunks-and-guards paragraph | I |
| 14 | LOW | 3 | §2 S5, against §7 and AC3 | J |
| 15 | LOW | 3 | §6 AC2, against AC1 and the §4 cost table | K |
| 28 | LOW | 4 | §4 "The gate arm", first bold paragraph | L |

---

## HIGH

### A — `TOOL-aRatifiedRulings-1` §6 AC7, the same-commit join, with §2 S5 (ids 1, 8, 24 HIGH; id 10 LOW)

AC7 is the only criterion that observes S5's rule that the 2.69 to 2.70 bump lands in the same commit as the M4 edit that incurs it, and its join fails in both directions. As spelled, it cannot go green: `git diff-tree --name-only <sha>` without `-r` prints the sha and the top-level directories only — on the last real bump `a3b4ca1e` it prints `memory` and `tools` and nothing else, and `tools/memory-tree/BUILD-METHOD.template.md` appears only under `git diff-tree -r --no-commit-id --name-only`, which is the spelling the kit's own checker uses at `check-unattended.sh:2347`. So the "Red when" clause, "the value-changing commit's tree does not carry the template", fires against a correct build (id 24). Spelled with `-r`, it cannot go red: `check-kit-versions.sh:135-147` reds any tracked `tools/memory-tree/*.template.md` whose line-1 marker disagrees with `KIT_MEMORY_TREE_VERSION`, so the commit that moves the constant necessarily moves the marker on line 1 of `BUILD-METHOD.template.md` in the same commit, and the template is listed whether or not the M4 paragraph rode along. `a3b4ca1e`, a check-21 commit with no method edit, lists the template at 2 lines for its marker alone. The natural split S5 forbids — M4 bytes in commit X, constant and markers in commit Y — reads green; the only split the join can catch is markers-first-constant-later, which `kit version markers` already reds (ids 1, 8). The `figure` clause says the join "does that job" of grading the template-only bump's placement; it does not, and unit 1's own §3 edge says no other gate does either.

Id 10, LOW, sits in the same paragraph: AC7 says `check-verdict-epoch.sh` prints its `no behaviour-bearing engine line moved` form. The constant line `KIT_MEMORY_TREE_VERSION=2.69   # ...` at `check-memory-hygiene.sh:20` is itself a non-comment engine line, so `behav_in` counts a constant-only bump as 2 moved lines and the gate prints its second clean form, `clean — 2 line(s) moved in <W> and the version moved 2.69 -> 2.70 in <S>`, with W and S the same commit. The pass condition (`clean`, exit 0) holds; the quoted form does not, and the sentence "it cannot grade the placement of a template-only bump" is argued from the wrong branch.

**Fix.** Join on the bytes S5 dates, not on the file. Replace the `diff-tree` clause with: the sha from `git log -G'^KIT_MEMORY_TREE_VERSION=' --format=%H <base>..<tip> -- tools/memory-tree/check-memory-hygiene.sh` equals the sha from `git log -S'CONVERGED is terminal for its subject' --format=%H <base>..<tip> -- tools/memory-tree/BUILD-METHOD.template.md`, or equivalently `git show <bump-sha> -- tools/memory-tree/BUILD-METHOD.template.md | grep -c '^+.*CONVERGED is terminal'` prints `1`. Red when the two shas differ or the added-line count is `0`. State that the marker line alone does not satisfy the join. If a `diff-tree` read is kept anywhere in the criterion, spell it `-r --no-commit-id --name-only`. For id 10, quote the second clean form and say the bump is the only engine line that moves, so W and S coincide by construction.

**Left-shift.** Two classes, one documented and one gateable. The gateable one: an AC that names a git command is run as written against the tree during the audit and its output quoted; the acceptance ledger already demands a command reproduce its figure, and the spec-audit brief gets a standing "run every quoted command" lens, which is what caught id 24. The documented one is §7's could-not-fail class: an AC that observes a placement rule names the commit shape that reds it, and if that shape is already refused by a leg on the bar the AC is redundant with that leg and says so rather than claiming an observation. Propose one sentence for `memory/TEMPLATE-SPEC.md` §6 to that effect; check 12 grades §6 structure and could carry "an AC with a `Red when` naming no commit shape or staged break" once the sentence exists.

### B — `TOOL-aRatifiedRulings-1` §4 Rollout, write-set paragraph, and `TOOL-aRatifiedRulings-2` §3 "No sequencing with unit 1 is owed" (ids 17, 18 HIGH; id 9 MEDIUM, shared with unit 4 §4 Rollout)

Both specs derive "the pair may run concurrently, and this spec derives no ordering rule" (unit 1) and "the roster may run the two in either order or concurrently" (unit 2) from product-file write sets. A pass's write set in this kit is never only its product files. Every pass commit moves its spec's status header, which hygiene check 9 (`gen_build_index --check`, run by the pre-commit staged leg whenever `memory/` is touched) forces to regenerate `memory/LIVE.md` and `memory/ledger/<month>.md` in the same commit, and every pass edits the build README; the parent's pass commit `922fd926` wrote all four, and every parent dispatch row declared them. `--dispatch` check 49 condition 1 at `unattended.sh:4853` refuses a declared path that `overlaps` any still-open sibling's, where `lib-unattended.sh:100-105` defines `overlaps` as `covers` both ways and `covers` returns 0 on equality. Two open passes honestly declaring `memory/LIVE.md` collide; a pass declaring less than it writes prints check-23 lines instead. So no two passes of this build can be open concurrently, and a roster that groups two of them on the specs' licence is refused at the second declaration and the run parks. Units 1 and 4 additionally both declare `memory/guides/SESSION-KICKOFF.md` (unit 1's Rollout and Files table; unit 4's Rollout says "This unit declares it at dispatch"), which is not a `SHARED_RECORDS` member and collides on equality the same way (id 9). Unit 2 §3 also says `--dispatch` "refuses to declare" `memory/LIVE.md` and the ledger "because they are `SHARED_RECORDS` or `GENERATED_INDEXES`"; `SHARED_RECORDS` in `.unattended.conf` is `DECISIONS.md`, `memory/backlog` and `readme-contract.txt` only, and `unattended.sh:4780` accepts a generated index declared alone, refusing only index-plus-generator, which the parent's own rows declaring `memory/LIVE.md memory/ledger/2026-09.md` demonstrate. The 24 check-23 lines naming those files fire because those passes did not declare them, not because they could not. Product-file disjointness itself stands; the paragraph exists to spare the roster re-derivation and derives the wrong licence.

**Fix.** In unit 1 §4 Rollout, replace the concurrency sentence with: product files are disjoint, but every pass declares its spec, the build README, `memory/LIVE.md` and the ledger shard, and units 1 and 4 both declare `memory/guides/SESSION-KICKOFF.md`, so passes of this build are SEQUENTIAL under check 49 condition 1 and the roster orders them; the second of units 1 and 4 to land re-stamps `last-audit` over the first per the charter's kickoff-manifest merge exception. Drop the "each declares its ledger by FILE" derivation or restate it as applying only if two passes are ever open together. Mirror the sequencing sentence in unit 2 §3 and unit 4 §4 Rollout, and correct unit 2's `GENERATED_INDEXES` sentence to "accepted alone, refused only beside its generator", citing `unattended.sh:4780`.

**Left-shift.** The record half of a write set is the same for every pass in this kit, so it belongs in the method, not in each spec's prose: one sentence in the memory-tree kit's `BUILD-METHOD.template.md` M6 stating that a pass's declared set always includes its spec, the build README and the two generated indexes, so `parallel-when-disjoint` never holds for two passes of one build and the roster sequences by default. Mechanically, `--dispatch` could print the implied record set beside the declared one so the roster reads it from the driver rather than from a sibling spec's derivation. Until either lands, the audit brief's lens "does this Rollout count the record files" is the documented check, and it caught this.

### C — `TOOL-aRatifiedRulings-4` §6 AC5, with §4 "Measured 2026-09-13 on this host" (id 16)

AC5 runs the canary suite under a `timeout` stub that exits 1 and expects `PASS (<n> assertions)`. The suite's `HAVE_TIMEOUT` guards are at `run-gates.test.sh:158-249`, `1082-1090` and `1131-1211` only. The five `GATE_JOBS` clamp arms at `:531-546` (`timeout "$CLAMP_BUDGET" bash -c ...` at `:534`, and `:517` inside `clamp_expired_verdict`), the clamp-verdict self-tests at `:560-574`, the distinguishability arm at `:581-589` and the wall arms at `:1562` and `:1574` are top-level and unguarded. Under a stub that exits 1 without running its arguments, `out` at `:534` is empty and `trc=1`, so all five widths print `did not clamp to a working width` and set `fail=1`; `:560` expects `BOTH expired` from a real rc-124 expiry and gets `the clamp let it spin`; `:581-588` then compares two equal strings and reds. `PASS ($n assertions)` prints only at `fail=0`, so the PASS line and its `<n>` are unobservable under the stub AC5 names, and the criterion reads red on a correct landing. Section 4's measured paragraph enumerated the RUNNER's `timeout` sites (`run-gates.sh:371`, `:1009`) and never the suite's own.

**Fix.** Specify the stub's shape in AC5 and in §4's measured paragraph: it refuses only the `-k` form the two probes use and delegates everything else to the real binary by absolute path — `case "$1" in -k) exit 1;; esac; exec /usr/bin/timeout "$@"` — since the clamp arms never pass `-k`, `runleg`'s `-k` call is gated on `bound>0` and the reaper's on `CEILINGS_LIVE`. Name `:517`, `:534`, `:560`, `:1562` and `:1574` as the calls the stub must pass through, and re-measure the paragraph's "stubbed run closes one below" figure under that stub.

**Left-shift.** A stub named in an AC gets its reach derived, not read: `grep -n '\btimeout ' <suite>` against the guard ranges, quoted in the ledger. The gateable version is in the suite itself, which this unit already edits: guard the clamp and wall arms' `timeout` calls on `HAVE_TIMEOUT` with an announced SKIP, or have them call `timeout` by the absolute path the probe resolved, so a `PATH` stub can never red an arm that is not testing the stubbed behaviour. That is a one-unit change to a file in this unit's Files touched and belongs in it.

---

## MEDIUM

### D — `TOOL-aRatifiedRulings-2` §2 S4 · §4 "The arm" Red-first paragraph · §6 AC3, AC4 (id 3)

S4 claims the arm's "failing case observed RED against the unfixed checker", and §4 Red-first names fixtures A and E as the two that print `FAIL unexpected` at base. B also reds at base, because `check-unattended.sh:2357` prints every undeclared path in one `wrote` line and B's `miss` on `build-brief.md` fails while the brief is still in it; §4's naming only A and E is itself incomplete. C and D, however, assert that check 23 STILL reports the post-hoc brief path and `other.md`, which the checker at base already does, so they pass before and after the fix. AC3's "Red when: the rows are read from the working-tree file" and AC4's "Red when: the membership test is a containment test" name defects nobody stages, in §4, §6 or §7. §4 calls C and D the pins for the two rejected alternatives that define the ruling's boundaries, so the spec ships its two boundary gates having only ever seen them pass, against the build README's own rule and the same class the round-1 audit folded into unit 3 as one staged break per assertion. A `covers`-based or working-tree-based implementation passes every red-first observation as specced.

**Fix.** Add to §4 Red-first and to AC3 and AC4 the staged break per control, each confirmed red before being unstaged and quoted in the ledger: C — swap the `git show "$dshit:$f"` read for a `cat "$f"` of the working tree and observe C's `hit` print `FAIL missing`; D — swap the exact `case` membership for `covers` and observe D's `hit` fail; B — name it beside A and E as red at base, with the reason.

**Left-shift.** The acceptance ledger carries one row per fixture naming the break that reds it and the invocation read, which is the round-1 cluster I shape and is already the documented check; a fixture row whose break is "the checker at base" while the fixture asserts a behaviour the base checker has is the smell, and a ledger check that refuses a control row with no named break is the mechanical form.

### E — `TOOL-aRatifiedRulings-4` §2 S3, the `FLOOR_ASSERTIONS` clause, with no §6 criterion (id 4)

S3 says `FLOOR_ASSERTIONS` "rises by the number of increments the arm adds" and §7 repeats it, and no criterion observes the raise. `run-gates.test.sh:48` pins `FLOOR_ASSERTIONS=146` and the suite's only comparison is `[ "$n" -ge "$FLOOR_ASSERTIONS" ]` at `:1675`; §4 records the last canary closing at 148 against 146. AC5's "`<n>` at or above the raised `FLOOR_ASSERTIONS`" is satisfied at the unraised value (150 or 151 is ≥ 146), its "executes three fewer than the raised floor" Red-when bites only if the raise happened, and `check-testsuite-counts.sh` grades the constant's shape only (its header: "IT RUNS NOTHING"). A pass that adds the arm and forgets the raise meets every criterion and leaves five assertions of slack, which is the stranded-arm class the pin exists to catch. Unit 2 AC6 and unit 3 AC4 in the same build observe their raises explicitly; this spec claims an observation it does not have.

**Fix.** Add to AC5, or as a new AC7: `grep -E '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.test.sh` at the landed tip reads the base value at `run-gates.test.sh:48` plus three (149 from the 146 at `16da4c6a`, DERIVED from the file at base); Red when it reads the base value, or when the stubbed run's `<n>` is below it.

**Left-shift.** Every S-item names the AC that observes it, and S3 names AC5 for a clause AC5 does not read; the audit's "every S-item clause is read by a named AC" lens caught it and stays the documented check. Mechanically, `check-testsuite-counts.sh` could compare the pinned floor against the `n` of the last `run-gates canary` row in `<git-dir>/gate-ledger.tsv` and warn on slack above a declared width, but the ledger is per-host and the check runs nothing by design, so that is its owner's call.

### F — `TOOL-aRatifiedRulings-1` §6 AC4, the positive-artifact clause (ids 11, 21)

AC4 requires the landed run's redirected file to hold `MARK review-loop`, but that marker is written to stderr (`unattended.test.sh:4532`, `echo "MARK review-loop" >&2`) while `hit`/`miss`/`same` at `:69-71` print their `FAIL` lines to stdout, and the criterion says only "output redirected to a file". Under a stdout-only redirect, the natural reading and the form AC4's own cost line prescribes ("redirect and grep the file"), the file holds the FAIL-line delta and no MARK, and AC4's own red-when then classifies a correct landing as "the region never ran". A false red, not a false green, but it is the liveness half of the only criterion that observes the new arm, and one of its two literal readings yields the wrong verdict.

**Fix.** Spell the redirect as `> <file> 2>&1` for both runs and say the MARK lives on stderr.

**Left-shift.** The "redirect and grep the file" prescription that specs in this repo copy into their `cost:` lines gets `2>&1` wherever it is spelled, starting with `memory/TEMPLATE-SPEC.md`'s AC example, so the convention carries both streams by default. No gate; a one-token convention.

### G — `TOOL-aRatifiedRulings-2` §8 F1 RESOLVED paragraph, and `TOOL-aRatifiedRulings-1` §3 Edges, first hands-off bullet (id 23)

Both define the closing pass's carrier list as "every carrier `tools/check-kit-versions.sh` pairs plus the two renders `adopt-unattended.sh` re-makes", and F1 says the list is spelled precisely so it is not remembered. The population is larger than the spelling. `b8e8d6dc`, the commit `TOOL-dMuffledSentinel-3` names, moved fifteen unattended files: four `.sh` constants, five `*.template.md`, `tools/unattended/README.md`, `tools/unattended/playbook.fixture.md`, and four installed copies (`.claude/skills/unattended/SKILL.md` plus `memory/guides/UNATTENDED-PROTOCOL.md`, `PLAYBOOK-TEMPLATE.md` and `UNATTENDED-VERBS.md`). `adopt-unattended.sh --check`, the every-bar `unattended skill wiring` leg, re-makes and diffs five installed artifacts, not two; and `DEPL-aHoistedPass-10`, OPEN, records `tools/unattended/README.md:1` as outside both populations `check-kit-versions.sh` reads. A closing pass following the spelled list writes at least three undeclared renders (check 23 of the unattended kit gate, the class unit 2 exists to narrow) or leaves `README.md:1` at 1.19 with no gate to say so, which is that backlog row's defect recurring under a spec that claimed to list every carrier.

**Fix.** Replace the enumeration in both places with the derived probe the record already uses (`TOOL-dFoldedVerdict-6`, `TOOL-aHonedRuleset-3`): the closing pass declares every file `git grep -l 'gov:kit unattended@'` returns plus the four `.sh` constants, cites `b8e8d6dc` as the commit shape, and deletes the word "two".

**Left-shift.** The gate is `DEPL-aHoistedPass-10`'s own remedy and belongs to its owner: `check-kit-versions.sh` reads the marker population by that grep rather than by a fixed pairing, so `README.md:1` joins the set it grades. Until then, a spec that enumerates a kit's carriers cites the grep it enumerated from, and the audit's command-reproduction lens (cluster A) re-runs it.

### H — `TOOL-aRatifiedRulings-4` §3, the `KIT_RUN_GATES_VERSION` bullet, against `TOOL-aRatifiedRulings-1` §8 F2 (id 25)

Unit 1 §8 F2 resolves "bump both" for a TEMPLATE-only edit, ranking `TOOL-dMuffledSentinel-3` (2026-09-12) as the later ruling over a leave-it precedent (`8c759e50`, 2026-09-05) and saying the adopter-side refusal applies to a template exactly as to a checker. Unit 4 §3 then leaves `KIT_RUN_GATES_VERSION` at 1.6 for a RUNNER-bytes edit on the strength of `922fd926` (2026-09-10), a leave-it precedent that also predates `dMuffledSentinel-3`, and names the very refusal class as an accepted residual. One build reads one record two ways, with the stronger case (checker bytes) getting the weaker treatment, and the closing pass F1 already charges with the unattended bump could carry a run-gates bump in the same commit shape `b8e8d6dc` used for two kits at once. The supporting figure also does not reproduce: `git log 6462556a..922fd926 -- tools/run-gates/run-gates.sh` lists `922fd926` itself and nothing between, and five commits, not four, touched the kit directory. Not a blocker: the two constants are different and the roster can follow both bullets, which is why this is a consistency defect and not a contradiction.

**Fix.** Route a 1.6 to 1.7 run-gates bump to the closing pass beside the unattended one, with its two carriers (`run-gates.sh:19` and `tools/run-gates/README.md`) named in that pass's declaration; or, if 1.6 is to stand, say in §8 why the later record does not bind run-gates rather than citing the earlier precedent. Correct the commit count either way.

**Left-shift.** A build's specs that cite one decision id resolve it one way: the spec-audit brief's cross-unit lens over §3 and §8 marks naming the same `FAMILY-slug-seq` is the documented check, and it caught this. A join over citations is a prose judgement, so no gate is proposed.

---

## LOW

### I — `TOOL-aRatifiedRulings-1` §7, chunks-and-guards paragraph (id 13)

The paragraph, which says it read `tools/gate-legs.json` on 2026-09-13, states `kit/dogfood doc parity` as guarded on two paths, `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/`. The manifest guards it on six: `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/ANNOTATION-STYLE.md`, `tools/lib/`, `tools/memory-tree/`. `kit-dogfood-parity.test.sh`'s PAIRS line renders all four docs, so this unit's own `--render` plus the marker bump rewrites `HYGIENE.md`, `TEMPLATE-SPEC.md` and `ANNOTATION-STYLE.md` too, and the derived sentence "a scoped bar whose diff misses both skips it" is false for a diff touching any re-rendered sibling. Fix: quote the guard list as the manifest has it, or point at the row instead of restating it.

**Left-shift.** A `spec tokens` arm: for every leg name in a spec's §7 followed by "guarded on", the backticked paths must equal that leg's `guard` list in the manifest, set-wise. One join over a file the leg already parses; stage the break on this paragraph, observe RED, then fix it.

### J — `TOOL-aRatifiedRulings-3` §2 S5, against §7 and AC3 (id 14)

S5 calls the second cost reading "the one full-bar row the landing bar produces (AC3)". The landing bar is `.unattended.conf`'s `GATE_CMD`, `bash tools/run-gates/run-gates.sh`, with no `GATE_SELFTESTS`; the spec's own §7 says the leg is `chunk: selftests`, held on every boundary, and AC3 names the hand-run `GATE_FULL=1 GATE_SELFTESTS=1` bar as its only observation. A reader of S5 either expects a row the landing push never produces or reads the landing bar's green as the AC3 observation, which §7 says it is not. Fix: reword S5 to "the one full bar the run buys by hand with `GATE_FULL=1 GATE_SELFTESTS=1` (AC3)".

**Left-shift.** None beyond the edit; §7 and AC3 already state the rule and the audit's S-to-AC lens is the documented check.

### K — `TOOL-aRatifiedRulings-3` §6 AC2, against AC1 and the §4 cost table (id 15)

AC2 names the untraced invocation `time bash tools/memory-tree/check-memory-hygiene.test.sh` and in the same criterion requires each of the four readings to carry "its checker-invocation count from a `PS4` trace beside it" as the artifact that THAT run executed the suite. An untraced run yields no trace, and §4's table treats traced and plain readings as different classes (598.7 s against 790.7 s). Either the four readings are really `bash -x` runs, in which case the literal command is wrong and the 0.8 ratio was derived on the traced class, which is fine but must be said; or the count is AC1's single trace copied beside four untraced readings, in which case it is not a per-reading artifact, and the before runs at base, red by §4's own statement, then have no PASS line and nothing else to prove the arm ran. The two clauses cannot both be met literally. Fix: pick one and write it — run the paired readings as `time bash -x` with stderr to a file and count from each run's own trace, or drop "its" and state that the count is AC1's and the PASS line is the after-runs' artifact.

**Left-shift.** None beyond the edit; the round-1 arithmetic lens covers the class.

### L — `TOOL-aRatifiedRulings-4` §4 "The gate arm, and the class it cannot escape", first bold paragraph (id 28)

"The population this branch serves is EMPTY and no run of the real bar can reach it" contradicts the spec two paragraphs down and its own Alternatives bullet: `run-gates.sh:1393-1394` runs `[ "$CEILINGS_LIVE" = 1 ] || bound=0` before the `.bound` write, so on a timeout-less host every leg of a real bar runs with `bound=0` and any operator or OOM kill reaches the new branch with a real leg. The spec says so itself ("on a host without one, `CEILINGS_LIVE=0` ... sets bound to 0 anyway"; "the host where the branch is MOST reachable"), and AC5's `PATH`-stub method reproduces that host on this box, so the observation waits on nothing. The arm's placement outside `HAVE_TIMEOUT` is justified by exactly the reachability the sentence denies. Fix: qualify the claim to hosts with a runnable `timeout`, and name the timeout-less bar as the one real population the branch serves.

**Left-shift.** None; a one-sentence self-contradiction the audit's consistency lens caught.

---

## What this round did not cover

The lenses were spec-audit lenses reading the four rev-2 specs against the tree at `97f6b915`; no product code was reviewed, because none exists yet for this build. The 10 refuted findings are recorded in the harness's own artefacts and are not restated here. Nothing was sampled: every lens read every spec, and every finding met a skeptic. The round-1 clusters were re-read at their folded text and none of them recurs as written; three of this round's clusters (A, B, G) are defects in the folded text itself, which is the ordinary shape of a second round. A third round is owed only for clusters A, B and C, scoped to unit 1 §4 Rollout and §6 AC7, unit 2 §3, and unit 4 §4 and §6 AC5 at their new blobs; the MEDIUM and LOW edits can be verified by the fold's own diff.
