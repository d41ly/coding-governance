**Serves:** spec-audit TOOL-aBatchedArm-3

# Tier-2 spec audit — TOOL-aBatchedArm-3, ROUND 2

*The fold audit. Round 1 (BLOCKED, eight blocker rows over nine defects) was held until
`TOOL-aBatchedArm-4` — the runner's declared modes — was built and CLOSED at `0422ea2e`, then folded
into rev-3 of the unit that re-cuts `tools/unattended/check-unattended.test.sh` into eight declared
shards. This round grades the FOLD — where it is wrong and where it is incomplete — and does not
re-report what round 1 already found. Node `a`, 2026-09-13, ROUND 2. Every finding below survived a
skeptic prompted to REFUTE it, and every cited line was re-read in the tree by the author of this
report rather than transcribed from a lens: the floor grade and both epilogue increments were
re-read, every op that moves `main` or the origin was enumerated, the fourteen region-local helper
spans were re-measured definition-to-last-use, the three control candidates were opened, the runner's
`--kit` filter and width resolution were read, and the six cited records were read at their rows.
Each row carries its address inside the spec, the fix, and the gate that would have caught it before
a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md`@`fa4338ea5f1be209e21e9c7af4f3d59e65d823b5` — rev-3, the fold of round 1's nine defects. ROUND 2.

The sibling specs are NOT in scope and are not re-graded. `TOOL-aBatchedArm-4` is cited only as the
live fact this fold rests on: `run-selftests.sh` has `--serial`/`--pooled`, bare refuses, the row
regex admits `1/8`; `run-unattended-gates.sh` takes verb+mode; `--check` is green on the 61 rows.
Suite lines below are HEAD (`9da019e2`) unless a row says otherwise; the spec's own status line
declares base `e9ed269b`, and one LOW row records that its anchors match neither tree.

## Verdict: BLOCKED

Nine rows at BLOCKER, thirteen at HIGH, six at MEDIUM, seven at LOW. Those thirty-five rows collapse
to **fourteen distinct defects**; the table below names which rows share one, so a fold that repairs
a defect repairs every row under it rather than thirty-five separately.

Three defects are blockers, and each is a fold that took half of a round-1 fix and dropped the half
that made it consistent. **AC1 is false by construction** (D-1): it reads the FLOOR-GRADED count and
adds `7 × PROLOGUE_ARMS` with `PROLOGUE_ARMS = 2`, but the two arms that make 2 are the C21 pair at
`:3215`/`:3222`, which run AFTER the floor grade at `:3168`, so no floor-graded count contains them
and a correct cut reds AC1 by exactly 14 — the only cut that turns it green double-counts seven arms.
Round 1's H1 paired "declare 2" with "move the floor to the end"; the fold kept the first half. **S5
derives seven replays from the arity, not from the ref state** (D-2): the file has ONE producer of
the `unit`-ancestor-of-`main` property (the lifecycle merge at `:1252-1257`), ONE consumer (the
tWaive merge at `:1588`) and a restore at `:1646`, so at most one boundary owes a replay, and AC8's
"each of seven observed FAILING when removed" cannot be met at six of them — the could-not-fail class
§7 forbids, commissioned six times. **AC9 has no mechanism** (D-3): S6 prescribes placement only,
and the note it cites at `:3172-3175` says a separated control stays GREEN, so the staged break AC9
demands cannot red; round 1's B7/H3/H4 named the mutation counter and the fold dropped it.

The rest of the fold is right about what round 1 said mattered most — the mode exists, the token
passes, the join is a port, the reuse audit was re-run with this unit's own terms and found the
crossover — and wrong or incomplete on six items it claimed to close: S1's balance metric is the one
the file's own seam note and `TOOL-aShardedFloor-3` §4 reject (D-4); AC4's fixture pools fourteen
rows at a host-declared width, not eight in eight slots (D-5); AC4's ratio cannot detect the
crossover it exists to record, and no two-shard wall is taken to compare against (D-6); a third
cross-region carrier — fourteen helpers defined inside a region and called up to 336 lines later — is
unnamed, and the header's HOIST SET claim goes false at the first cut (D-7); the driver row becomes
the pooled floor the moment `TOOL-aTracedSpawn-1` lands, on a citation this spec inverts (D-8); and
S3's eight floors have no criterion that can tell a floor from a number (D-9). Two record-shape
defects follow (D-10), and four low rows: every line anchor in the spec is wrong in both trees, the
cost line prices a row S2 deletes, half of round-1 M2 was dropped, and §10 cites a backlog-sharding
ruling as a test-shard decision.

**Convergence.** Under `memory/guides/BUILD-METHOD.md` (the paragraph at `:140`) the loop re-arms
only on a STRICTLY SMALLER confirmed-blocker count. Round 1 stood at eight blocker rows; this round
stands at nine. By the rule's letter the fold did not converge and the exit is reached: every
blocker still standing is DISPOSED here, none parked. Read by defect rather than by row, round 1's
six blocker defects became three, which is the direction a fold should move; the rule counts rows,
and this report does too. **Disposition of all three standing blockers: FOLD.** Each is a defect in
the document this review read, and the mechanism each needs — a floor moved below the epilogue or a
constant defined at the floor (D-1), a per-boundary ref-state DELTA derived by running rather than a
count typed from the arity (D-2), a process-local mutation counter the control asserts (D-3) — lies
inside this unit's own scope and touches no file the unit does not already name. Nothing here needs
a PROMOTE.

## Review shape

- raw 52 · confirmed 35 · refuted 17 · unverified 0 · precision 0.67

Precision at 0.67 is above the ~0.5 floor `AGENTS.md` §8 sets for adding agents, so the lens fan was
scoped about right for this target. Read the confirmed count with the table below in hand: the
pipeline reports zero duplicates because each row addresses a different clause of the spec, but four
lenses hit the AC1 arithmetic independently (four rows), four hit the replay derivation (five rows),
three hit AC9's missing mechanism (four rows), four hit the balance metric (four rows) and four hit
AC4's population (four rows). Thirty-five rows is fourteen defects.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## The fourteen defects, and which rows carry each

| Defect | Rows (severity as adjudicated here) | Section |
|---|---|---|
| D-1 · AC1's identity is false by construction: `PROLOGUE_ARMS = 2` counts arms the floor never grades | id=1 blocker · id=11 blocker · id=24 blocker · id=39 blocker | B1 |
| D-2 · seven replays derived from the arity; the ref state has one producer, one consumer, one restore, and one un-derived leak | id=2 blocker · id=12 blocker · id=26 blocker · id=40 blocker · id=27 high | B2 |
| D-3 · AC9 has no mechanism; S6 is placement only; the population is one by the key, three by the brief | id=3 blocker · id=16 high · id=41 high · id=48 medium | B3 |
| D-4 · S1 balances by invocation count, the metric the seam note and `aShardedFloor-3` §4 reject, with no block-edge rule and no balance observable | id=15 high · id=31 high · id=42 high · id=9 medium | H1 |
| D-5 · AC4's fixture pools fourteen rows at a host-declared width, not eight in eight slots | id=5 high · id=13 high · id=30 high · id=45 medium | H2 |
| D-6 · AC4's 0.5-of-serial-sum threshold sits at the ambiguity point; no two-shard wall is recorded for F2 | id=6 high | H3 |
| D-7 · a third carrier: fourteen region-local helper definitions cross any ~350-line cut; the HOIST SET claim goes false | id=28 high · id=7 medium | H4 |
| D-8 · the driver row is the pooled floor once `aTracedSpawn-1` lands, and §3 inverts that record to exclude it | id=43 high | H5 |
| D-9 · S3's eight floors have no criterion that can tell a floor from a number | id=4 high | H6 |
| D-10 · two open records own this scope with no edge: `aGradedDoorway-7` S2 (inverted order) and `-8` (a third copy of the join) | id=46 medium · id=47 medium | M1 |
| D-11 · every line anchor matches neither the declared base nor HEAD | id=10 low · id=20 low · id=38 low | L1 |
| D-12 · AC4's `cost:` prices the row S2 deletes | id=19 low · id=51 low | L2 |
| D-13 · half of round-1 M2 dropped: the suite's own whole-suite note is unretargeted | id=52 low | L3 |
| D-14 · §10 cites `TOOL-aRelaxedShard-4`, a backlog-sharding ruling | id=49 low | L4 |

## Round 1 against the fold, item by item

- **B1, B2 (mode; no cost verdict)** — dissolved by `TOOL-aBatchedArm-4`. Accepted. The fold's
  residue is the fixture AC4 names for that mode, which is D-5 and D-6.
- **B3, B4 (the `1/8` token)** — dissolved by unit 4's regex. Accepted; AC3 and AC7 are right.
- **B5 (ref-state replay)** — folded into S5/AC8 as "seven derived replays". WRONG: D-2.
- **B6 (the join is manifest-scoped)** — folded into S4/AC5 as a port scoped to `--shard` callers.
  Right on the scope; incomplete on where the predicate lives, which `aGradedDoorway-8` already
  ruled: D-10.
- **B7, H3, H4 (controls that lose meaning)** — folded into S6/AC9 as enumerate-and-pin. INCOMPLETE:
  the counter mechanism all three rows named was dropped, so AC9 cannot red: D-3.
- **B8 (reuse audit declined)** — §10 re-run with this unit's own terms; found the crossover.
  Right, with one miscite: D-14.
- **H1, H2 (`PROLOGUE_ARMS` undeclared; two counts conflated)** — folded into S1/S3/AC1. WRONG: the
  fold kept "declare 2, read the floor" and dropped "move the floor", which is the only pairing under
  which both are true: D-1.
- **M1 (§7 leg)** — fixed. Not re-graded.
- **M2 (help text falsified by S2)** — half folded: the kit runner's paragraph is in Files touched,
  the suite's own note at `:3169-3170` is not: D-13.

---

# BLOCKERS

## B1 · id=1, id=11, id=24, id=39 — AC1 is false by construction: the constant counts arms the floor never grades

**Address:** section 6 AC1 (`:149-153`), section 2 S1 (`:23-27`), section 4 "Why the two counts
differ" (`:96-102`).

The floor grades `$n` at `check-unattended.test.sh:3168`. The only increments outside every
`in_shard` region are the C21 pair at `:3215` and `:3222`, and both run AFTER `:3168` — region two's
`fi` is at `:3112`, the C21 block opens at `:3178`. Nothing unconditional precedes region one at
`:299`: the `n=$((n+1))` at `:264` is inside `mutate()`. So every FLOOR-GRADED count — unsharded and
each shard's — excludes the pair, and the eight floor-graded counts partition the unsharded one
EXACTLY. The file's own five measurement lines at `:3130-3141` say so for the two-way cut, and the
`:3153` comment ("PROLOGUE_ARMS is 0 … nothing paid twice") is TRUE for the figure it names.

AC1 reads the floor-graded count — its own text, and §4's "every reading names the floor-graded
figure" — and demands `sum(eight) == unsharded + (SHARD_ARITY − 1) × PROLOGUE_ARMS` with S1 declaring
`PROLOGUE_ARMS = 2` "from the epilogue". A correct cut yields `+0` and reds AC1 by 14. The only cut
that turns it green double-counts seven arms, which is the defect AC1 exists to catch. The `+14`
identity holds only for the PASS-printed count at `:3227`, which the spec explicitly does not use.

Worse, S1 orders the `:3153` comment "corrected" to 2, which rewrites a true statement into a false
one, and §4 calls it false. The sibling suite defines the constant the other way round —
`unattended.test.sh:5435-5447` derives `PROLOGUE_ARMS` over floor-graded counts as
`n1 + n2 − n_unsharded`, arms paid BEFORE the floor — so the constant S1 declares would mean "paid
after the floor" in this file and "paid before" in the sibling.

Round 1's H1 fix was two halves: declare the constant, AND move the floor check to the very end of
the file so the graded and printed figures coincide by construction. The fold kept the first.

**Fix.** Pick one and say it in S1, §4 and AC1 together. (a) Move the floor grade below the C21
block, after every increment, so floor-graded == PASS-printed; `PROLOGUE_ARMS = 2` then holds at the
floor and AC1's `+14` is right. Or (b) keep the floor at `:3168`, declare `PROLOGUE_ARMS` as the
floor-graded figure — 0 at HEAD, DERIVED the way the sibling derives it, not reasoned from a static
count — name the C21 pair as an EPILOGUE constant only the PASS line carries, and restate AC1 as
`sum(eight) == unsharded` exactly. Under (b), S1's "the true figure is 2" and its comment correction
are dropped; `:3153` stands. Either way the identity and the constant come from one measurement
point.

**Left-shift gate.** Option (a) IS the left-shift: one grade after every increment deletes the class.
Failing that, have the suite print the identity's three terms itself — executed, mode, prologue-arm
count — at the floor line, so a nine-run union check compares printed numbers rather than an
arithmetic claim a reader reconstructs from two different lines.

## B2 · id=2, id=12, id=26, id=40, id=27 — seven replays are the arity minus one, not the file's ref state

**Address:** section 2 S5 (`:42-46`), section 6 AC8 (`:182-185`), section 4 "Why the split is safe"
(`:85-94`).

Every op that moves `main` or the origin, enumerated at HEAD:

- `anchor_break` (`:274-283`) / `anchor_restore` (`:284-295`): paired at every call site
  (`:1193-1210`, `:2125-2224`); the restore resets `main` to `ANCHOR0`, force-pushes it, and puts
  `unit` at `PRISTINE`.
- `:1112` pushes `unit:main`; `:1135` pushes `ANCHOR0:main` back.
- `:1252-1257`, the lifecycle block: `main` takes a `--no-ff` merge of `unit` and is pushed. Nothing
  restores it. **This is the ONE producer** of "unit is an ancestor of main".
- `:1290-1291`, the existing `SH_I = 2` replay, reproduces exactly that.
- `:1529-1646`, the tWaive block: `:1588`'s `git checkout -q unit && git merge -q --no-edit main` is
  **the ONE consumer** — a fast-forward when the property holds, a swallowed conflict when it does
  not; `:1646` resets `main` to `ANCHOR0`, force-pushes, and `reset_tree`s `unit`.
- After `:1646`: `:3046-3047` moves `trunk`, not `main`; `:3064`/`:3067` set and restore `main` in
  four lines.

So the property exists in one window, `(:1257, :1646]`, and a fresh shard's start state (`main` at
`ANCHOR0`, `unit` at `PRISTINE`) is what the whole run holds at every boundary outside it. A boundary
outside the window has NOTHING to replay; a copied `:1289` block there would fast-forward `main` to
`PRISTINE`, a state the whole run never has at that line — `:745`'s `git merge-base main HEAD` would
then read `unit`'s tip instead of `ANCHOR0` — which is the divergence AC6 exists to catch. S5's
"seven" is `SHARD_ARITY − 1`, typed, not derived from the file. AC8's observable, "that shard's
`tWaive` merge conflicts", can occur in at most the one shard holding `:1588`, and in zero if that
shard also holds `:1252`. "Each replay observed FAILING when removed" is unsatisfiable at six or
seven of seven indices, so the unit either ships six dead replays it cannot observe or closes with
AC8 unmet.

One carrier S5 does not derive: `:1243` pushes `refs/heads/ahead` to the origin and nothing deletes
it, so every later `is_published()` read of the advertised tips sees a ref a fresh shard's origin
lacks. The design brief this seam was cut from
(`memory/builds/aShardedFloor/build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md:209`)
names it and says: settle it by RUNNING both shards, never by reasoning.

**Fix.** Rewrite S5 as a rule, not a count: for each boundary the cut produces, dump the whole-run
ref state at that boundary's first line (local branches, `refs/remotes`, the bare origin's heads and
HEAD) and diff it against fresh-start state; a replay exists exactly where a ref some arm at or after
that line reads differs. Record the per-boundary result in the spec — expected non-empty at the one
boundary preceding the shard that holds `:1588`, if that shard does not also hold `:1252`; and the
`ahead` tip either replayed or shown unread. Re-key or delete the `SH_I = 2` block. Rewrite AC8: the
non-empty replay is observed failing when removed, with the tWaive conflict named as ITS observable;
every empty boundary is recorded as measured-empty and covered by AC6's FAIL-set identity, which is
the observable for a replay applied where none belongs. Drop "seven" from §4.

**Left-shift gate.** Round 1's B5 gate, still owed: each region asserts its precondition on entry —
`git merge-base --is-ancestor unit main` inside the window, `main == ANCHOR0` outside it — so a shard
deprived of a predecessor's state REDS on a named line instead of on three waiver arms, and a replay
applied at the wrong boundary reds the same way.

## B3 · id=3, id=16, id=41, id=48 — AC9 has no mechanism, and S6's key finds one control where the brief names three

**Address:** section 2 S6 (`:47-49`), section 6 AC9 (`:186-189`), section 5 risks and testing
(`:138-143`), section 7 (`:196-198`).

S6's whole mechanism is "pin each into the same shard as the mutations it counts". Pinning prevents
the separation; it cannot make a separated control red. AC9 demands the opposite: a control cut away
from its mutations makes "its shard REDS". Traced at HEAD: the control at `:1513` is
`reset_tree; same 'the tree is still clean after nine mutations' "$(run …; echo $?)" 0` after check
16's nine mutations at `:1409-1507`. Moved into any other shard it runs `reset_tree; run` on a clean
tree and exits 0 — which is exactly what the note S6 cites says at `:3172-3175`: "degrades into a
duplicate of the opening control — still green, and no longer evidence". Staging the separation
always yields green, so AC9 is either never exercised or permanently red, and §5 names this class as
the one AC1 cannot see with S6 as its sole mitigation.

The population is also wrong three ways. S6's key phrase matches ONE line at HEAD (`:1513`); the
file's note says TWO (and said TWO at `b0029e43`, when there was also one); the design brief that
wrote the note (`…-aShardedFloor-1-design-brief.md:210`) enumerated THREE by line, today `:776` (a
TERMINAL archived record silent after the archive mutation, region one), `:1513`, and `:2077` ("move
1 leaves a terminal record green"). S6 says "enumerate BY LINE" and cites no line.

Round 1's B7, H3 and H4 all named one mechanism — a per-control mutation counter — and its Left-shift
gate said "one mechanism closes B7, H3 and H4". The fold kept the enumeration and dropped the
counter.

**Fix.** S6 names the mechanism: each mutating arm in a counted block increments a process-local
`MUT`, and the control asserts it before calling `run` — `same 'nine mutations ran in this process'
"$MUT" 9` — so a control cut away from its mutations reds at runtime in the shard that carries it.
S6 names the brief as its population source, lists the three candidates by today's line, reconciles
which still depend on same-process mutations against HEAD, and corrects the note's "TWO". AC9 then
names that assertion as the red. Alternatively AC9 becomes structural: a static arm asserts that
the control's line and its block's first mutation resolve to the same `in_shard` index — but say
which, because the two fire in different places.

**Left-shift gate.** The counter is the gate. Cheaper and complementary: a lint over the suite that
any assertion message carrying `after N mutations` sits in the same `in_shard` region as N mutating
lines, redding at `--check` time before the suite is run.

---

# HIGH

## H1 · id=15, id=31, id=42, id=9 — S1 balances by the metric its own cited sources reject, with no block-edge rule and no observable

**Address:** section 2 S1 (`:23-27`), section 4 first paragraph (`:78-81`), section 6 AC4
(`:161-170`), section 10 first bullet (`:232-242`).

S1: "re-cut the two `in_shard` regions into eight, balanced by invocation count". The seam note in
the file S1 edits, at `:1265-1273`, records for the existing cut: "NOT chosen by arm count. One
tokenisation of this file splits nearly evenly while the git-operation weight splits about 2:1 — and
the bar's floor is the LARGER shard, so an imbalance measured the wrong way eats the win directly."
§10 claims to have read that seam. `TOOL-aShardedFloor-3` §4
(`memory/builds/aShardedFloor/spec/2026-08-21-spec-TOOL-aShardedFloor-3.md:44-66`), the CLOSED record
that designed the seam, rules "Do not pick by arm count" for the same reason, and rules "one
boundary, at a block edge (the `reset_tree`-led block), never between independent arms" — because
arms chain inside blocks and the obvious cut one line early separates an arm from its control.
S1 names the forbidden metric and omits the block-edge rule.

The file's own node-a readings at `:3149` bear it out: region one 84 arms / 190 s = 2.26 s per arm,
region two 146 / 246 s = 1.68 s, because the anchor force-push blocks and the lifecycle cluster at
`:1193-1261`. §4's own cost model says cost is per FORK, not per arm. A count-balanced eight-way cut
hands the region-one shards ~35 % more wall than the rest; against the budget file's 9067 s reading,
an even eighth is already 1133 s beside AC4's 1200 s red, so the imbalance alone can red AC4 — and
AC4's single longest-wall reading cannot tell an unbalanced cut from a throughput-bound pool, so F2
lowers the arity on a mis-cut and records "the crossover held".

**Fix.** S1: cut ONLY at `reset_tree`-led block edges, citing `aShardedFloor-3` §4 by id; take
invocation count as the first guess and re-balance against the per-shard SERIAL readings S2 takes,
iterating until max(shard) is within a declared tolerance of sum/8; record each candidate's timing
beside the one chosen, as that record did for two candidates. Add a balance observable to AC4: all
eight walls recorded, max/mean reported beside the ratio, and a cut that fails the tolerance is
re-cut before S2's rows are written.

**Left-shift gate.** A static arm in the suite's `--check` path that refuses a region boundary not
immediately preceded by `reset_tree` (or a helper that calls it), so a between-arms cut cannot land.

## H2 · id=5, id=13, id=30, id=45 — AC4's fixture pools fourteen rows at a host-declared width, not eight in eight slots

**Address:** section 6 AC4 fixture (`:161-166`), section 4 first paragraph (`:77-78`).

§4: "the on-demand pooled run holds only these rows, so eight fill eight slots". AC4 names
`run-unattended-gates.sh --pooled`, which at `run-unattended-gates.sh:300` runs
`run-selftests.sh --kit tools/unattended --pooled`. `--kit` is the only population filter
(`run-selftests.sh:116`), a substring test on argv (`:278-279`), so it takes every row whose script
lies under the dir — seven today (`selftest-budgets.txt:110-116`, the driver at 3860 s budget / 2569 s
reading among them), fourteen after S2. Under `--pooled`, `OUTER = W` (`:308-310`), and `W` is the
bar profile's declared width (`:288`; `run-gates.sh --print-profile` on this node: `capable`, width
8); `SELFTEST_OUTER_WIDTH` is clamped to it (`:313-326`), so nothing lifts it. Rows dispatch in
declaration order until `live -ge OUTER`.

So on node a the driver and the five small suites hold slots, at most seven shards start together
and the rest queue behind whichever row finishes first; the longest-shard wall and the ratio are
read under contention from six sibling suites the AC does not name. On a `modest` (4) or `minimal`
(2) profile the eight shards run in two or four waves and the 0.5 ratio is unreachable by
construction, so the same commit reads green on node a and red on a four-core box while AC4 names
no width. The reading that seeds `TOOL-aBatchedArm-5` and decides F2 measures the kit's pool, not the
split.

**Fix.** AC4 names a run whose population is exactly the eight rows and states its width: either a
row filter narrower than `--kit` added as an S-item (`--only <name>`, or `--kit
tools/unattended/check-unattended.test.sh`, which the substring filter already honours), or a
scratch budget file holding the eight rows. `fixture:` records the runner's own `SWEEP of N suite(s),
width W (outer O, inner I)` line and the profile row; the threshold is stated at `O >= 8` or
normalised by `O/8`. Correct §4's sentence to the kit's row count with the driver named as a
co-occupant when the kit runner is used instead, and then record the co-running rows and their
serial readings beside the ratio.

**Left-shift gate.** AC4's record carries the runner's printed width line verbatim; a spec-lint arm
refuses a `figure:` derived from a pooled run whose record lacks it.

## H3 · id=6 — AC4's ratio threshold sits at the ambiguity point, and no two-shard wall exists for F2 to compare against

**Address:** section 6 AC4 red condition (`:168-170`), section 8 F2 (`:207-209`).

F2 lowers the arity when "AC4's ratio shows eight bought less than two would", but AC4 never records
a two-shard wall. Its ratio is longest-shard wall over the SUM of eight serial readings, and that
denominator is at least the unsharded time plus seven extra fixture setups. On the file's own node-a
readings (`:3149`: shards 190 s and 246 s, unsharded 478 s) the two-shard pooled wall is already
~0.51 of unsharded; a throughput-bound eight-way run that buys NOTHING over two still walls at
~246 s, giving 246 / (≥ 478) < 0.5 — green. The exact case F2's branch exists for is recorded as
passing. With the budget file's 9067 s reading, the ratio arm can bind only when the serial sum is
≤ 2400 s, so the 20-minute arm decides every plausible run and the ratio decides none.

**Fix.** AC4 records the two-shard pooled wall at the same commit — one arity-2 `--pooled` run before
S1 lands, or the row from `<git-dir>/gate-ledger.tsv` — and reds when eight's longest shard is
≥ 0.5 × two's longest. Drop or re-derive the 0.5-of-serial-sum arm, and say what the 20-minute arm
decides on its own (the goal) as distinct from what the ratio decides (the arity).

**Left-shift gate.** The measurement AC4 seeds is a build-record figure; make the arity-2 baseline a
`figure:` line with its sha, so a later re-measurement has something to diff against.

## H4 · id=28, id=7 — a third carrier: fourteen helpers defined inside a region and called up to 336 lines later

**Address:** section 2 S1 and S5 (`:23-27`, `:42-46`), section 4 "Why the split is safe" (`:85-94`),
the file header's HOIST SET claim at `check-unattended.test.sh:28`.

S5 says "the coupling is git REF state, not shell variables" and names no third carrier. Measured
definition-to-last-use at HEAD, all inside the regions: `dispconf`/`mkdisp` `:843-844 → :912`;
`_bm_sections` `:1459 → :2044`; `wreset`/`drive` `:1590-1591 → :1640`; `_bm31`/`_mkskill`
`:1768-1840 → :1871`; `pedit` `:1912 → :2248`; `gut_parser` `:2456 → :2669`; `seed_ros`/`add_u7`/
`rrow` `:2719-2736 → :2772`; `drow` `:2814 → :3011`; `land_as` `:3024 → :3096`. Roughly 1100 of the
~2800 region lines sit inside such a span, so seven count-balanced cuts at ~350 lines each almost
surely land in one; the shard that starts after a definition fails every use with `command not
found`, the mutation never runs, and the hit reds. AC6 catches it after a full nine-run cycle rather
than the spec preventing it; rev-1's zero-variable scan was taken at the ONE old boundary, never at
the seven new ones. Nothing in scope authorises the hoist, so the first cut lands as unspecced rework
and the header's "HOIST SET is two" goes false.

**Fix.** S1 adds: hoist every helper defined inside a region and used past a cut into the prologue
beside `anchor_break`, or list the spans as uncuttable constraints on the cut; update the HOIST SET
note to the DERIVED count. S5 re-runs the scan at each new boundary for all three carriers —
variables, functions, refs — and records the result per boundary. AC6 remains the observable.

**Left-shift gate.** A `--check`-time arm: for every function defined inside an `in_shard` region,
its last textual use resolves to the same index as its definition, else red naming the span.

## H5 · id=43 — the driver row is the pooled floor once `aTracedSpawn-1` lands, and §3 inverts that record to exclude it

**Address:** section 3 "Sharding the sibling driver suite" (`:60`), section 4 first paragraph
(`:74-78`), section 6 AC4 (`:161-170`).

`TOOL-aPacedTurnstile-8` (`memory/backlog/TOOL.md:177`), cited here only for the crossover, also
records "BOTH must move together or the work is wasted — the other suite just becomes the new
floor". The kit's `--pooled` run holds every kit row (H2), and the driver row — 3860 s budget,
2569 s reading — becomes that floor the moment its bare invocation stops aborting. §3 cites
`TOOL-aTracedSpawn-1` (`TOOL.md:440`) as "cannot run unsharded" to EXCLUDE sharding it; that record
says bare aborts in seconds on `set -u` at line 4107, and `--shard 1/2` and `2/2` are the only
invocations that complete. AC4 measures "the longest SHARD's wall", which goes green while the kit's
pooled verdict — the figure the build README targets at under 20 minutes — stays floored at
~43 minutes by a row this unit declares out of scope. Today that floor is hidden only because the
bare driver row aborts, so a green AC4 here is an artefact of a sibling bug.

**Fix.** Either add the driver's two existing shard rows (`--shard 1/2`, `--shard 2/2`) to S2 so
S4's join covers both suites and AC5's second clause inverts; or state in §1 and §4 that this unit
lowers one row and the population's pooled wall stays floored at the driver until it is declared
sharded, naming the record. Either way cite `aPacedTurnstile-8`'s "both must move together" and
correct the `aTracedSpawn-1` citation.

**Left-shift gate.** AC4 records the pooled run's WHOLE wall beside the longest shard's, so the
floor the goal is measured against is in the record whether or not this unit moves it.

## H6 · id=4 — S3's eight floors have no criterion that can tell a floor from a number

**Address:** section 2 S3 (`:34-36`), section 6 AC2 (`:154-157`), section 7 (`:199`).

S3 says "Observed by AC2". AC2 observes a mis-cut arm losing its state; it says nothing about floors.
AC1 reads the executed count, not the floor. No §6 criterion checks that the eight `FLOOR_SHARD_i`
or the re-measured `FLOOR_ASSERTIONS` sit at headroom against their readings, or that a stranded
block reds one. The file's own history at `:3118-3124` — a 338 floor under a 398 count hid SIXTY
stranded arms, twice in one session, while the suite printed PASS — is the failure S3 exists to
prevent, and eight floors set with slack or never re-measured cannot fail any AC as written.

**Fix.** Add an AC: for each index, `FLOOR_SHARD_i` lies within the ~3 % headroom the file's own
block argues for, both figures written beside the constant; and one shard with a block deliberately
stranded past an `exit` is observed redding its floor, then unstaged.

**Left-shift gate.** The suite prints `executed N against floor F` per mode already; a `--check`-time
arm that parses the eight measurement comments and refuses a floor more than the declared headroom
below its recorded reading.

---

# MEDIUM

## M1 · id=46, id=47 — two open records own this scope with no edge, and S4 lands a third copy of a predicate one of them ruled upstream

**Address:** section 3 Edges (`:62-68`), section 2 S4 (`:37-41`), section 8 F1 (`:203-206`),
section 9.

`TOOL-aGradedDoorway-7` is INPROGRESS (`TOOL.md:286`) and its S2 (spec `:39-45`) owns "raise
`SHARD_ARITY` to 8 in both suites and fix what breaks", explicitly "Ordered AFTER S4 [batching] at
rev-3". This spec builds the check-unattended half of that S2, orders batching (`-1`) to land ON TOP
of the split, cites `-7` S2 in §4 as the ruling's source, and declares no edge to it. Two open
records own one scope item with opposite orderings; whichever closes second finds the other's S2
still open. §6's rule is supersede-with-a-note, never silent duplication.

`TOOL-aGradedDoorway-8` (`TOOL.md:287`, OPEN) already ruled the shard-join predicate "belongs
upstream, as a kit file rather than a canary arm". S4 adds a THIRD in-tree copy — the canary at
`run-gates.gov.test.sh:360-406`, the inCMS port, now a budget-row port — and F1 leaves `-8` open to
build a fourth over the manifest. §12's rule is a factory at instance #2. Both readers take
(script, argv-list) pairs; one predicate with two thin readers is a small refactor, not a port.

Not a lens row and not counted in the shape above, but the gate says the same thing about the
Edges block already: `bash tools/memory-tree/check-memory-hygiene.sh` at HEAD reds check 12 on this
spec — "§3 declares **hands-off** `TOOL-aBatchedArm-1` and that unit declares no matching
**consumes-from** `TOOL-aBatchedArm-3` back" (`…-spec-TOOL-aBatchedArm-1.md:74` reads
`consumes-from none`). The edge the fold added at rev-2 was never mirrored, so the same fold that
adds the `-7` edge owes the `-1` mirror or the leg stays red.

**Fix.** Add the edge: "supersedes `TOOL-aGradedDoorway-7` S2 for this suite" (or `consumes-from` if
`-7` keeps the driver half), state the order inversion and its reason (batching alone measured 40 to
44 minutes) in §4, and annotate `-7`'s S2 as carried by this id in the same commit. Mirror the
existing `hands-off -1` edge as `consumes-from -3` in `-1`'s §3. Make S4's port
the ONE join function fed by the budget rows here and by the manifest in `-8`'s kit file and the
canary, running under `--check` so the unguarded `every held leg is budgeted, every budget row
resolves` leg carries it; either close `-8` with this unit or record in F1 why it stays a separate
copy.

**Left-shift gate.** The drift audit's closed-plans probe already looks for records that overlap; add
the pair (open unit citing another open unit's S-item as its ruling, no edge declared) as a signal.

---

# LOW

## L1 · id=10, id=20, id=38 — every line anchor in the spec matches neither the declared base nor HEAD

**Address:** section 2 S1, S5, S6; section 4; section 6 AC8, AC9; Files touched.

Verified in both trees. The floor grade is `:3160` at base `e9ed269b` and `:3168` at HEAD; the spec
says `:3130`, the "MEASURED unsharded 271" comment in both trees. The "TWO CONTROLS LOSE THEIR
MEANING" note is `:3164` (base) / `:3172-3175` (HEAD); the spec's `:3132-3140` and `:3132` land inside
the RE-MEASURED block in both. `:1277-1293` and `:3153` are HEAD numbers (base: `:1281-1285` for the
replay, `:3145` for the comment). The kit runner's help text is `:157` at base and `:175` at HEAD;
the spec says `:157-158`. And the `:3153` comment S1 orders corrected has five siblings at
`:3130-3141` asserting the same "no prologue arm" that S1 leaves uncorrected. S5 and S6 are
line-addressed DoR items, so a builder following them lands on measurement comments.

**Fix.** Anchor by text (`FLOOR_ASSERTIONS=`, `[ "$n" -ge "$FLOOR" ]`, `TWO CONTROLS LOSE THEIR
MEANING`, `PROLOGUE_ARMS is 0`) beside one tree's line, and cite that tree — the base the status
line names, or HEAD with the base bumped. Extend S1's comment correction to the `:3130-3141` block
or say why those readings stand (under B1's option (b), they stand).

**Left-shift gate.** A spec-lint arm that resolves every `file:line` cite in a spec against the base
sha its status line names and prints the line's text, so a cite pointing at a comment is visible at
`--check` time.

## L2 · id=19, id=51 — AC4's `cost:` prices the row S2 deletes

**Address:** section 6 AC4 `cost:` (`:167`), section 2 S2 (`:28-33`), section 4 Rollout (`:106-108`).

"27200 s at the largest row" is 13600 × the `sweep-ceiling-factor` of 2
(`selftest-budgets.txt:49`; `run-selftests.sh:597`), the bound of the single `unattended gate
selftest` row. Rollout puts S2 before AC4's run and S2 deletes that row; the largest unattended row
is then the driver at 3860 × 2 = 7720 s, and the run wall is the runner's derived `SWEEP_WALL` over
fourteen rows. The ceiling the builder plans the idle window around belongs to a row that will not
exist, off by 3.5×.

**Fix.** Derive the line: "per-row bound = shard budget × sweep-ceiling-factor; run wall = the
runner's `SWEEP_WALL` over the kit's rows, printed at start", no typed number.

**Left-shift gate.** Charter §7 already bans a typed count of a derived population; a spec-lint arm
that flags a `cost:` line carrying a bare integer with no `DERIVED` marker.

## L3 · id=52 — half of round-1 M2 was dropped: the suite's own whole-suite note is unretargeted

**Address:** section 2 S4 (`:37-41`), section 4 Files touched (`:121-126`), section 9 (`:224-225`).

Round 1 M2's fix (round-1 record `:453-455`) named TWO texts falsified by S2: the kit runner's help
paragraph AND the suite's own shard-contract note. rev-3 carries the first in Files touched, §5 and
§9. The suite's note at `check-unattended.test.sh:3169-3170` still says "the whole-suite claim lives
only in a run with no `--shard` argument"; after S2 no declaration invokes such a run, so the note
sends its reader to a run that no longer exists. No S-item, AC or Files-touched entry directs its
rewrite.

**Fix.** S4 retargets both texts at the ported join in the same commit; Files touched names the note
by text.

**Left-shift gate.** The round-1 M2 gate, still owed: a drift-audit probe that a file whose prose
asserts a property of a declaration it delegates to is re-read when that declaration's rows for its
kit change.

## L4 · id=49 — §10 cites a backlog-sharding ruling as a test-shard decision

**Address:** section 10 second bullet (`:243-248`).

`TOOL-aRelaxedShard-4` (`memory/DECISIONS.md:24`) rules that the backlog's bound is its live row
count, reports `live_backlog_rows_per_shard` per BACKLOG shard, and ends "Sharding rejected on the
slope". It decides nothing about test-suite shards; the probe returned it on the token `shard`. The
reuse audit rev-3 rewrote because round-1 B8 found the previous one miscited now names a record
that does not bear on the unit.

**Fix.** Drop it, or state what it decided and why it is irrelevant. The records that DO decide the
contract are `TOOL-aShardedFloor-2`, `-3` and the design brief.

**Left-shift gate.** None worth building; the reader of §10 is the check.

---

## What a fold should do first

B1 is one decision — move the floor, or define the constant at the floor — and every other
arithmetic sentence in the spec follows from it; make it first, because B2's per-boundary record and
H6's floor AC both name the same measurement point. B2 is answered by RUNNING, as the brief said:
dump the ref state at each candidate boundary once the cut is chosen under H1's block-edge rule, and
write the per-boundary result into S5 instead of a count. B3 is one helper and one assertion per
counted block.

Two things the fold should decide rather than re-draft. H5: whether this unit's goal sentence is
"one row under 20 minutes" or "the kit's pooled verdict under 20 minutes" — the build README says the
second, and only the first is what AC4 measures. H2/H3: what population and what baseline AC4's
reading is taken against, because `TOOL-aBatchedArm-5` and F2 both consume that reading, and as
written it measures neither the split nor the crossover.
