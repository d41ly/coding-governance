**Serves:** spec-audit TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4

# Tier-2 spec audit — the `aRatifiedRulings` spec set, round 1

Written 2026-09-13 on node `a` by the tier2-review harness (`tools/workflows/tier2-review.js`): four primed finder lenses, an adversarial skeptic per finding, one synthesis pass. Subject: the four SPECCED units of `memory/builds/aRatifiedRulings/`, read at the blobs named on the range line and against the tree at `16da4c6a` for every source claim.

Reviewed subjects, pinned: `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-1.md@879f668878ff69f3205a569deb3876f410f63495` · `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-2.md@d480f30b71031f49797dfadb7fb77a1ef41d06c2` · `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-3.md@f05e1e1230e4d5343961c6ada09a61ce3ea2eb94` · `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-4.md@33085525fae58c37c1de59ee7c4249a758d4b505` · ROUND 1.

## Verdict: BLOCKED

One defect blocks the set: units 1 and 2 give opposite orders for the single `KIT_UNATTENDED_VERSION` bump, and the M2 roster cannot follow both. Everything else is repairable in place with the edits below, but two more criteria (unit 2 AC7, unit 2 AC6) red against a correct implementation of their own spec, and unit 4 as specced lands red on a boundary leg its gate list cannot see.

**Review shape:** raw 53 · confirmed 29 · refuted 24 · unverified 0 · precision 0.55.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every lens and every skeptic batch came back, so the finding set is complete for the lenses that ran and a zero count below is positive evidence rather than an artefact of a dead lens. The pipeline's duplicate pass found none; the clustering below is this report's own, because several confirmed ids state one defect from different lenses and the fix is written once per defect. The per-id severity table keeps all 29 rows so the counts returned to the caller agree with what was adjudicated here.

**Adjudicated severities:** BLOCKER 4 · HIGH 7 · MEDIUM 13 · LOW 5. The four BLOCKER ids are one defect (cluster A) reported by four lenses; the seven HIGH ids are five defects; the thirteen MEDIUM ids are seven defects.

Severity meaning in this record: BLOCKER — the set cannot be dispatched as written, a cross-unit contradiction the roster must settle before any pass starts. HIGH — a unit lands red, or a criterion cannot be observed, under a correct build of its own spec; fixable inside that spec. MEDIUM — a premise or an observation is false against source, so a reader acting on it does the wrong thing, but a build can still land green by luck or by discovering it at the bar. LOW — a figure or a header field does not reproduce; no verdict changes.

---

## Per-id severity table

| id | severity | unit | address | cluster |
|----|----------|------|---------|---------|
| 1 | BLOCKER | 1 | §2 S5 · §4 Rollout · §6 AC7 | A |
| 12 | BLOCKER | 1 | §2 S5 · §6 AC7 · §4 Rollout | A |
| 30 | BLOCKER | 1 | §2 S5 · §6 AC7 · §4 Rollout | A |
| 43 | BLOCKER | 1 | §2 S5 · §6 AC7 · §4 Rollout | A |
| 3 | HIGH | 2 | §6 AC7 · §2 S1 · §4 "Why the tree at the pass commit" | D |
| 42 | HIGH | 2 | §6 AC6 · §4 "The arm" · §6 AC1 | E |
| 45 | HIGH | 3 | §6 AC3 · §4 "The mechanism" | H |
| 5 | HIGH | 3 | §6 AC2 · §2 S5 | G |
| 10 | HIGH | 4 | §2 · §6 · §7 | M |
| 15 | HIGH | 4 | §2 · §4 Files touched · §7 | M |
| 29 | HIGH | 4 | §2 S1 · §4 Files touched · §7 | M |
| 2 | MEDIUM | 1 | §4 Rollout, write-set paragraph | B |
| 13 | MEDIUM | 1 | §4 Rollout, write-set paragraph | B |
| 34 | MEDIUM | 1 | §4 Rollout | B |
| 44 | MEDIUM | 1, 2 | U1 §4 Rollout · U2 §3 · U2 §8 F1 | B, C |
| 4 | MEDIUM | 2 | §3 non-goals · §8 F1 | C |
| 14 | MEDIUM | 2 | §3 non-goals · §8 F1 | C |
| 46 | MEDIUM | 3 | §6 AC2 | G |
| 7 | MEDIUM | 3 | §6 AC5 · §6 AC6 | I |
| 22 | MEDIUM | 3 | §6 AC5 · §6 AC6 · §7 "New arm" | I |
| 20 | MEDIUM | 3 | §8 F2 · §7 "New arm" · §6 AC4 | J |
| 31 | MEDIUM | 3 | §8 F2 RESOLVED · §6 AC4 | J |
| 16 | MEDIUM | 4 | §4 "The gate arm" · §10 | N |
| 33 | MEDIUM | 4 | §2 S3 · §4 "The gate arm" | N |
| 23 | LOW | 3 | §3 main-tree bullet · §5 perf · §4 region table | K |
| 24 | LOW | 3 | §4 "The mechanism" vs Inventory | K |
| 26 | LOW | 1 | §4 "The M4 bytes" · §8 F1 | L |
| 28 | LOW | 2 | status header tail · §8 F1 | F |
| 49 | LOW | 2 | status header tail · §8 F1 | F |

---

## BLOCKER

### A — `TOOL-aRatifiedRulings-1` §2 S5 · §4 Rollout · §6 AC7, against `TOOL-aRatifiedRulings-2` §3 and §8 F1 (ids 1, 12, 30, 43)

Unit 1 S5 puts the unattended kit bump, 1.19 to 1.20, "in the same commit as the edit that incurs them"; its Rollout says "the first of the two to land performs the 1.19 to 1.20 move and the second asserts the carriers agree"; AC7 asserts `KIT_UNATTENDED_VERSION=1.20` at unit 1's landed tip, with a figure clause that tolerates only "a sibling unit has already moved the unattended constant", never "nobody has yet". Unit 2 §3 says "No kit version bump inside this unit" and its §8 F1, RESOLVED and marked by design for this audit, bumps ONCE "by the closing pass after both units that edit `check-unattended.sh` have landed". That is three rules for one constant and no two of them agree.

Whichever the build follows, another spec's text is violated. Follow F1: unit 1's tip reads 1.19 across all four carriers (`unattended.sh:42`, `check-unattended.sh:40`, `check-brief-recorded.sh:49`, `check-pass-order.sh:38`) and AC7 reds at unit 1's own landing. Follow unit 1: if it lands first it stamps 1.20 and unit 2 then moves `check-unattended.sh` bytes under an already-stamped version, the adopter-refusal class `TOOL-dMuffledSentinel-3` records and F1 was written to prevent; if unit 2 lands first it does not bump (its own §3), and unit 1 as second is told by its own Rollout only to "assert the carriers agree" while AC7 demands 1.20. No build record (`README.md`, `RUN.md`, the run-mandate prompt) arbitrates, and no epoch gate covers the unattended kit, so nothing mechanical picks an order.

**Fix.** Align unit 1 with unit 2 F1, since F1 is the resolved fork. S5 keeps the manifest re-stamp and the memory-tree 2.69 to 2.70 move, which no sibling contests; the unattended half leaves S5 and the Rollout's carrier list. AC7 is re-cut to assert `KIT_MEMORY_TREE_VERSION=2.70` with every memory-tree carrier agreeing, `KIT_UNATTENDED_VERSION` UNCHANGED at 1.19 with `bash tools/check-kit-versions.sh` exiting 0, and `check-verdict-epoch.sh` printing `clean` for the memory-tree bump only. The Rollout paragraph points at unit 2 F1 instead of restating a different rule. The closing pass, which F1 already charges with the bump and the carrier list, also owes the epoch-gate observation for the unattended bytes both units moved; F1's declaration should say so, because a bump commit that lands AFTER the byte-moving commits is the shape AC7's "Red when" currently calls a refusal, and the closing pass must show the gate accepts it or state that the gate does not cover this kit.

**Left-shift.** A version-carrier constant (`KIT_<X>_VERSION`) pinned to a value in one spec's AC while a sibling spec of the same build, or a RESOLVED fork in it, assigns that bump to another pass is a shared claim with two owners. The `spec tokens` leg already joins a spec's paths against the tree; extend it to join `KIT_[A-Z_]+_VERSION=<v>` literals across the specs of one build and red when two specs pin different owners for one constant unless one cites the other's fork id. Until that lands, the audit brief's amendment-leaves-its-other-half-standing lens is the documented check, and it caught this.

---

## HIGH

### D — `TOOL-aRatifiedRulings-2` §6 AC7, with §2 S1 and §4 "Why the tree at the pass commit" (id 3)

AC7 requires that after the fix no `unattended: check 23 —` line names a path ending in `-build-brief.md`, and its figure pins "the lines that fall silent are 5". At least one live row cannot go silent under S1's own rule. `TOOL-dRetiredFork-6`'s pass commit `ffdaa82b` carries the brief path and NOT the run-state file: `git diff-tree ffdaa82b` lists the brief but not `RUN.md`, and `git show ffdaa82b:memory/builds/dRetiredFork/RUN.md` holds zero `brief · item TOOL-dRetiredFork-6 · reason` rows, because the brief and dispatch rows both first land in `295e58d8` five seconds later. Under S1's read of the run-state file at the pass commit the exclusion set for that unit is empty, the brief path stays in the `wrote` list, and AC7 reds against a correct S1/AC3 implementation. The pinned 5 counted rows without checking each row's membership in its pass commit's tree, the same class as the parent's predicate-grades-a-subset-while-its-note-reports-the-whole-population.

**Fix.** Derive AC7's expected set from the population: for each (anchor, unit) with a brief row, the path is excluded iff `git show <pass>:<run-state file>` carries the row. AC7 asserts exactly that set falls silent and names the residual, at least the `TOOL-dRetiredFork-6` line, as still firing by design. If the ruling instead wants every brief silenced, the in-force window must be the pass window `[anchor, dstop)` rather than the pass commit's tree, and fixture C must be re-cut to a row appended after `dstop`; that is a different S1 and the spec must say which.

**Left-shift.** A PINNED figure that names a command reproduces from that command or it is not pinned. Record the one-line derivation beside the figure (here: the loop over live rows with the `git show` membership test) in the build folder, so the audit re-runs it rather than re-counting by hand. Whether `check-spec-tokens` can grade a `figure:` clause is a question for that tool's owner; the documented check is the one this audit ran.

### E — `TOOL-aRatifiedRulings-2` §6 AC6, §4 "The arm" (Red-first paragraph), §6 AC1 (id 42)

The spec's observation is a `PASS (<n> assertions)` line that `tools/unattended/check-unattended.test.sh` cannot print at base. Backlog row `TOOL-aHoistedPass-38` (OPEN, 2026-09-05) records the suite RED in both shards for pre-existing causes, and two of them are still in the tree: `mkconf` (`check-unattended.test.sh:81-106`) declares no `DISPOSITION_CUTOFF`, so `check-unattended.sh:418` echoes its notice on every default run and `same ... ""` at `:283` (shard 1) and `:1880` (shard 2) fail; and `pedit 's/^Ten kit-owned core items\./...'` at `:1924`/`:1929` is a fixture no-op against `PROTOCOL.template.md:324`, which reads "Twelve", so `mutate` (`:245`) sets `st=1`. `PASS ($n assertions)` prints only at `st=0` (`:3191`); `n` prints otherwise only on a floor breach (`:3131`). So §4's "the same invocation prints `PASS (<n> assertions)`" is false regardless of the fix, AC6 is unobservable, and the raised floors "PINNED from the `n` the suite itself printed" cannot be read from the suite's own output. Unit 1's AC4 makes exactly this disclosure for its sibling suite by citing `TOOL-aTracedSpawn-3`; unit 2 makes none, so a reader takes a FAIL exit as the arm's failure.

**Fix.** Cite `TOOL-aHoistedPass-38` in AC1's permission clause the way unit 1 AC4 cites its row. Make the observation for AC1 through AC5 the FAIL-line delta between the base checker and the fixed one; exit status is not the observation. Re-key AC6 to "no `FAIL executed ... against a floor` line appears" and read `n` from a `PS4` trace or a counted print rather than the PASS line. Or name repairing causes 1 and 3 of that row as a precondition and route it to the owner, since it is outside this ruling's mandate; the spec must pick one.

**Left-shift.** A spec whose AC reads a suite's PASS line owes that suite's base status. The cheap check is in the spec-audit brief: for every `*.test.sh` an AC names, grep `memory/backlog/*.md` for an OPEN row naming it and require the citation. A gate could do the same join, but the suite's own repair (`-38`) is the real left-shift and belongs to its owner.

### H — `TOOL-aRatifiedRulings-3` §6 AC3, with §4 "The mechanism" cost prediction (id 45)

S5 asserts both the standalone reading and the full-bar row land inside the untouched 900 s ceiling, but the spec gives only standalone projections (790.7 × 0.63 = 498 s plain, 431 s traced) and never states a contention multiplier. The park the ruling cites as its measurement (`memory/builds/aJoinedCanon/RUN.md`, 2026-09-07T00:02:53Z) records a ~660 s standalone killed past 900 s under the full bar, at least 1.36×, and a 2.9× contention multiplier measured on a hygiene leg (48 s quiet, 139 s at width 8); `TOOL-aPooledSweep-4` records this suite at 1126 s serial and 972 s pooled. The spec's own post-cut projection is 498 to 657 s standalone; times the recorded multipliers that is 677 to 1905 s. AC3's "below 900" is not implied by any number the spec holds, §5 risk (2) only names AC3 as "the full-bar observation", and no disposition exists for an AC3 red: the ceiling is untouched by mandate and candidate C is a hands-off edge. A build that lands AC1, AC2 and AC4 through AC6 green can strand on the one criterion that tests the ruling's word.

**Fix.** Add the multiplier from the park to §4, derive the standalone target AC2 must hit for AC3 to hold (900 s divided by the multiplier), and write AC3's red disposition: candidate C (about 200 s a run by the spec's own figures) is PROMOTED into this build as its own unit rather than handed off, or the red row is recorded as the ruling's next input with the ceiling still untouched.

**Left-shift.** A criterion that decides whether a ruling's answer holds carries a disposition for its red, in §5 risk or §8, or it is a fork left unmarked. Propose one sentence in `memory/TEMPLATE-SPEC.md` §6: an AC whose red has no written next move is an open question and takes an F-id. That is a template rule, gated by check 12's fork-mark predicate once the sentence exists.

### G — `TOOL-aRatifiedRulings-3` §6 AC2 and §2 S5 (id 5 HIGH; id 46 MEDIUM)

The 600 s bound sits inside the spec's own measured noise on both sides. The base tree already read 598.7 s in the traced run the spec lists as one of its three quiet readings, so the timing half of AC2 is met with no change. On the other side, the derivation the AC states is "790.7 × 0.63 = 498 s, plus headroom for the 1.32× spread", which is 657 s, yet the bound written is 600 (600/498 = 1.20); the 63% also assumes the whole 222.9 s region vanishes while §4 predicts ~57 s survives, so 498 is optimistic before the spread is applied. A correct change reading 620 to 700 s on a quiet box, inside the band §4 itself calls "not measurable to better than a factor of two", reds AC2. S5's before/after pair of the same invocation, with invocation counts, is asserted by no criterion, so the ruling's word CHEAPER is observed only by AC1's invocation-count proxy. Id 46 adds that the "three quiet readings" omit `TOOL-aPooledSweep-4`'s 1126 s serial reading of this suite on the same node and day, a record the spec cites two paragraphs earlier for a different fact; admitting it puts the worst × 0.63 at 709 s.

**Fix.** Make AC2 a paired reading of the same invocation on the same box back-to-back: before at `16da4c6a` via a frozen clone, after at the landed tip, asserting after ≤ 0.8 × before, both recorded in the ledger with their checker-invocation counts. Keep AC1's deterministic invocation count as the primary observation and demote 600 s to a note against the 900 s ceiling. If a bound stays, derive it from the spread-adjusted worst (657 s, or 709 s with the aPooledSweep reading admitted) and say why any reading is excluded.

**Left-shift.** An AC that states its own arithmetic must reproduce it: the audit brief gets a standing arithmetic lens (every `×`, `=`, `%` in §4 through §6 recomputed). The paired-reading shape removes the pinned bound entirely, which is the better fix; `memory/gotchas/measure-the-metric-the-owner-names.md` already records the class.

### M — `TOOL-aRatifiedRulings-4` §2 (no S-item) · §4 Files touched · §6 (no AC) · §7 (ids 10, 15, 29)

`tools/run-gates/run-gates.sh` is on the kickoff manifest's `watch:` line (`memory/guides/SESSION-KICKOFF.md:6`). `skills/session-kickoff/manifest-check.sh` check 5 (`:285-311`) is topological: the newest watch-touching commit must be an ancestor of a commit that changed the `last-audit` value, else fail 5; its staged leg C5s (`:405-420`) refuses the commit outright unless the stamp is bundled. The `kickoff-manifest ratchet` leg is chunk `records`, subject `repo`, no guard in `tools/gate-legs.json`, so every bar runs it. Reproduced in a scratch clone: one appended comment line to `run-gates.sh` committed without a re-stamp printed `MANIFEST check 5 FAILED — watched files changed since last-audit with no re-stamp`. Unit 4 scopes no re-stamp in S1 through S4, lists no `SESSION-KICKOFF.md` edit in Files touched, has no AC for it, and §7 names only `run-gates canary`, `memory hygiene` and `spec tokens`. Landed as specced, unit 4 reds the ratchet on the next boundary bar unless unit 1's unrelated stamp happens to land later, an ordering nothing states. Unit 1 handles the identical obligation for `BUILD-METHOD.md` (S5, AC6, Files touched), so this is a gap, not a convention. Whether `KIT_RUN_GATES_VERSION` (1.6) moves in this pass or is deferred like unattended's is also unstated.

**Fix.** Add an S5 mirroring unit 1's: re-stamp `last-audit` in `memory/guides/SESSION-KICKOFF.md` in the same commit as the `run-gates.sh` edit, with a delta line in the message. Add the file to Files touched, add `kickoff-manifest ratchet` and `kit version markers` to §7, and add an AC shaped like unit 1's AC6: `manifest-check.sh` check 5 reports no watched file changed after the stamp at the landed tip. State whether `KIT_RUN_GATES_VERSION` moves here or at the closing pass.

**Left-shift.** The gate exists and would catch it at commit; the spec-side check does not. Extend the `spec tokens` leg to join a spec's Files touched against the manifest's `watch:` list and red when a watched file is named with no `memory/guides/SESSION-KICKOFF.md` beside it. One grep, no new fixture.

---

## MEDIUM

### B — `TOOL-aRatifiedRulings-1` §4 Rollout, write-set paragraph (ids 2, 13, 34; id 44 shared with C)

The Rollout says unit 2 "edits check 23, which also lives in `tools/unattended/unattended.sh`, and stages its red arm in `tools/unattended/unattended.test.sh`". Against source: check 23 is `tools/unattended/check-unattended.sh:2222-2361` (unit 2's own §4 says so) and its fixtures go in `check-unattended.test.sh`; `unattended.sh:712` holds a different `fail 23`, the driver's object-substitution check. Unit 1's product edits (`unattended.sh:4096`, `unattended.test.sh:4589/4601`) touch neither. The "SEQUENCED, never concurrent under M6" conclusion and the "first to land bumps" rule are derived from an overlap that does not exist. The only true intersection is the `KIT_UNATTENDED_VERSION` line at `check-unattended.sh:40`, which exists only under the in-pass bump that cluster A removes. M6 (`memory/guides/BUILD-METHOD.md:188`) REQUIRES concurrency when write sets do not intersect, and `--dispatch` condition 1 (`unattended.sh:4853`) refuses only on overlap.

**Fix.** Name unit 2's real files and state the write sets are disjoint (`unattended.sh` + `unattended.test.sh` here; `check-unattended.sh` + `check-unattended.test.sh` in unit 2), so M6 parallel-when-disjoint permits the pair and no ordering rule is owed. If sequencing is still wanted, name a true ground (the shared `unattended.test.sh` MARK counts, or the closing-pass bump); otherwise accept concurrency explicitly. Falls out of the cluster A fix.

**Left-shift.** A `check <N>` cited beside a path reds when that path holds no `fail <N>` for the dispatch-subset sense; a grep the `spec tokens` leg can carry. Better: the roster reads each pass's DECLARED write set from `--dispatch` output rather than from a sibling spec's prose, which is what the driver already computes.

### C — `TOOL-aRatifiedRulings-2` §3 non-goals ("No kit version bump inside this unit", "Sequencing with unit 1") and §8 F1 (ids 4, 14; id 44 shared with B)

"`TOOL-aRatifiedRulings-1` edits the same file for check 37" and "Both units write `tools/unattended/check-unattended.sh`, so `--dispatch` refuses them as a concurrent pair" are both false as stated: check 37 branch 10 is `unattended.sh:4096`, `check-unattended.sh` contains no check 37, and unit 1's non-bump write set is `unattended.sh`, `unattended.test.sh`, the BUILD-METHOD template/render and `SESSION-KICKOFF.md`. F1 opens on the same false premise. With the bump deferred, the two declared sets are disjoint and `verb_dispatch`'s check 49 (`unattended.sh:4853-4864`) will NOT refuse the pair; the sequencing the spec relies on is enforced by nothing. The resolution survives; the spec's reasons for it do not.

**Fix.** Rewrite both bullets: unit 1 edits `unattended.sh`/`unattended.test.sh`; the shared surface is the carrier line `check-unattended.sh:40` only if a pass bumps, which F1 forbids; the units are disjoint and the build plan (README, which declares no order) may run them in either order. F1's opening sentence names the carrier line, not the checker, as the shared surface.

**Left-shift.** Same as B.

### I — `TOOL-aRatifiedRulings-3` §6 AC5 (Red-when) · §6 AC6 · §7 "New arm" (ids 7, 22)

The staged break for "satisfied by rc alone" is "pointing the runner at a script path that does not exist, so every invocation exits 127, and observing that the arm still prints `ok`". For the control arm this neither reaches it nor can detect the defect it is staged for. §4 says the control reads `_b1rc`/`_b1out` from the existing run, the direct `bash "$HERE/check-memory-hygiene.sh"` at `check-memory-hygiene.test.sh:2198`, not through `pk_out`, so redirecting the runner leaves it green. And even routed through the runner, rc 127 reds an rc-only control (`[ rc = 0 ]`) exactly as it reds the rc-plus-notice one, so "the arm still prints ok" cannot occur for the control whether or not it asserts the notice, and AC6's "the three value arms of AC5 go red" is satisfied by an rc-only control too. The `READ_PATH_CEILING is declared` notice assertion, the VALUE half S3 adds, has no staged failing case anywhere, against S6's "every arm ... has its failing case observed RED".

**Fix.** Stage the control's break as a run with rc 0 and no notice: drop the `READ_PATH_CEILING` line from the fixture conf for that one run, or substitute a `true` stub for the checker, and observe the control arm red on the notice. Keep the 127 break for the two red arms. Record which invocation the control actually reads.

**Left-shift.** The acceptance ledger (check 23 joins it under `build/`) carries one row per arm naming the break and the invocation read; an arm row whose break is shared with an arm of a different assertion form is the smell. A ledger check refusing a value-arm row whose named break also reds the rc-only form is the mechanical version; the documented check is S6 applied per assertion, not per arm.

### J — `TOOL-aRatifiedRulings-3` §8 F2 · §7 "New arm" · §6 AC4 (id 20), and the floor's position (id 31)

The F2 bullet ends "Left OPEN ... the owner may prefer the slack" and the paragraph appended beneath it reads "RESOLVED ... `FLOOR_ASSERTIONS` is RAISED to the post-change executed count". §7 still defers with "whether it moves up is §8 F2", and AC4 still accepts "at least the 235 it reads today", which a build that never raises the pin satisfies. One fork returns two verdicts and the acceptance observes the OPEN one; the resolved obligation has no criterion that reds if it is skipped. Separately (id 31): the floor's only check sits at `check-memory-hygiene.test.sh:2212-2213`, BEFORE the project-key section that starts at `:2215` and carries nine literal `n=$((n+1))` increments plus loop-driven ones; the PASS line at `:2306` prints the final `n`. A floor pinned to that final `n` is compared against `n` minus the section's increments and the suite reds itself on the first run, so AC2's "exits 0" fails for a reason the RESOLVED mark introduced.

**Fix.** Delete "Left OPEN ..." from the bullet body and fold the mark in place. Change AC4 to require `FLOOR_ASSERTIONS` equal to the post-change `n` AS OBSERVED AT THE CHECK POINT (the counter's value at `:2213`), or move the floor comparison to just above the PASS line and say so in S4 and AC4; the second is the better fix because it makes the pin mean the printed number. Update §7's "whether it moves up" to "it moves up to `n`".

**Left-shift.** Check 12's fork-mark predicate: a fork bullet carrying both `Left OPEN` and a `RESOLVED` paragraph reds. For the floor: hoist the comparison to immediately before the PASS line in the suite itself, so a pin read from PASS output cannot disagree with the value graded.

### N — `TOOL-aRatifiedRulings-4` §2 S3 · §4 "The gate arm" placement paragraph · §10 (ids 16, 33)

The arm is placed OUTSIDE the `HAVE_TIMEOUT` guard and is said to run "the same tbl-loose profile ... so the arm executes on every host" and to "add no fixture". But `fx/tbl-loose.txt` is written INSIDE that guard (`run-gates.test.sh:1150`, between the `if` at `:1131` and the `fi` at `:1211`); `selfkill.sh` at `:977` is outside it, the profile is not. On a timeout-less host the file does not exist and `run-gates.sh:270` (`if [ -f "$PROFILES" ]`) silently falls back to the built-in formula, as its header at `:9-10` says. The arm reaches the no-bound branch there only because `CEILINGS_LIVE=0` (`:1394`) forces bound 0, a dependency the spec never states and the runner header calls "the rollback". S3, §4 "Both reach the same branch with the same fixture" and AC5's placement rationale are untrue of the suite as it stands, and AC5 concedes that host class cannot be observed here.

**Fix.** Have the arm write its own `loose\t0\t0\twidth=2,timeout=0` row before its `runp`, or hoist the `:1150` printf above the guard, and say so in S3, §4 and Files touched. Drop "adds no fixture" from §10 or qualify it to `selfkill.sh`.

**Left-shift.** The suite's `runp` wrapper refuses a `GATE_PROFILES` that names an absent path, so a test can never run under the fallback while believing it runs under a fixture. One `[ -f ]` and a `FAIL`; the runner's own silent fallback stays, because that is production behaviour and a documented rollback.

---

## LOW

### K — `TOOL-aRatifiedRulings-3` §3 main-tree bullet · §5 perf · §4 region table (id 23); §4 "The mechanism" vs Inventory (id 24)

§3 and §5 say the main-tree and scratch sections are "55% of a run"; the §4 table gives 33% + 27% = 60% (196.2 + 164.4 of 598.7 s), and checker-seconds alone give 54.4%. Neither rounds to 55, and §3 hands that figure to the next unit as its starting number. Fix: replace 55% with the table's 60%, or say "checker seconds, 54%", in both places. Id 24: "The mechanism" says `pk_rc` "goes, or stays as a one-line wrapper if its removal moves the lexicon pin"; `lexicon.py:2767` fails on offenders UNDER the pin as well as over, so removal always moves it and the rule resolves to "stays", while Inventory and Files touched plan for it going. Both paths are green if done consistently. Fix: decide once, remove `pk_rc` and lower the pin in the same commit (read off `--check`), and delete the "stays as a wrapper" alternative.

**Left-shift.** Prose figures beside a table reproduce from it; the arithmetic lens from cluster G covers this. For `pk_rc`, none owed beyond the edit.

### L — `TOOL-aRatifiedRulings-1` §4 "The M4 bytes" · §8 F1 (id 26)

The quoted paragraph (three wrapped lines plus its blank line, em dashes at 3 bytes) measures 258 bytes and the qualifier adds 46, so the two edits are 304 bytes, not the 264 + 46 = 310 the section and F1 state; headroom is then 905 and 198 under the high-water. No verdict changes, no `--bump` is owed either way, but AC2 asks the build to re-derive a figure the quoted bytes cannot produce. Fix: re-measure the scratch render or quote the exact paragraph it held; state one pair of figures.

**Left-shift.** None beyond AC2's own re-derivation, which will catch it at build.

### F — `TOOL-aRatifiedRulings-2` status header tail · §8 F1 (ids 28, 49)

§8 F1 carries `RESOLVED (agent, 2026-09-13, delegated)` but the status line ends at `streams tooling` with no `ratified <date>` pointer; `memory/TEMPLATE-SPEC.md:129-133` says to add it when marking a fork RESOLVED, and units 1, 3 and 4 carry `ratified 2026-09-13` for the same mark. The one spec whose fork settles the build-wide bump is the one whose header does not say so. Fix: append `· ratified 2026-09-13` to the status line.

**Left-shift.** Extend check 12's fork-mark predicate: a spec with a `RESOLVED` mark in §8 and no `ratified` token in its status header reds, and the converse. One awk over the population the check already reads; stage the break on this spec, observe RED, then fix it.

---

## What this round did not cover

The lenses were spec-audit lenses reading the four specs against the tree at `16da4c6a`; no product code was reviewed, because none exists yet for this build. The 24 refuted findings are recorded in the harness's own artefacts and are not restated here. Nothing was sampled: every lens read every spec, and every finding met a skeptic. A second round is owed after the cluster A edit and the four HIGH edits land, scoped to the changed sections at their new blobs.
