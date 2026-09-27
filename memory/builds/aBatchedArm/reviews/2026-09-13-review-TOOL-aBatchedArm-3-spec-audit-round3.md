**Serves:** spec-audit TOOL-aBatchedArm-3

# Tier-2 spec audit — TOOL-aBatchedArm-3, ROUND 3

*The second fold audit. Round 2 (BLOCKED, nine blocker rows over fourteen defects) graded rev-3, the
fold of round 1; rev-4 is the fold of round 2, and this round grades THAT fold — where it is wrong
and where it is incomplete — and does not re-report what rounds 1 and 2 already found and rev-4
closed. Node `a`, 2026-09-13, ROUND 3. In this run's record the subject is on its second round: the
first (nine blocker rows) was CONVERGING with no predecessor, and this one is measured against it.
Every finding below survived a skeptic prompted to REFUTE it, and every cited line was re-read in the
tree by the author of this report rather than transcribed from a lens: the region-local definitions
were re-counted between the first `in_shard` and the floor (27, and the 28th regex hit is a quoted
string), the check-16 block was re-counted `reset_tree` line by `reset_tree` line (12 mutation
cycles, 12 `hit` calls, no `mutate()` call), every producer of origin-side ref state was enumerated
and its deletion searched for (none for `ahead`, none for `trunk`), `reset_tree`'s body was read, the
budget file's one row and the runner's hard-coded `BUDGETS` path were read, the base's ancestry to
`0422ea2e` and the absence of `--pooled` at that base were checked with git, and the `-7` records
were grepped for any note back. Each row carries its address inside the spec, the fix, and the gate
that would have caught it before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md`@`285b3787d44eb80f56684b81af6e0ae198d18c86` — rev-4, the fold of round 2's fourteen defects. ROUND 3.

The sibling specs are NOT in scope and are not re-graded. `TOOL-aBatchedArm-4` is cited only as the
live fact this fold rests on: CLOSED at `0422ea2e`, `--pooled` exists, the row regex admits `1/8`,
bare routes refuse. Suite lines below are HEAD (`dfc402fc`), which for
`tools/unattended/check-unattended.test.sh` and `tools/run-gates/selftest-budgets.txt` is byte-identical
to the spec's declared base `c2db2f5d` (`git diff --stat` between the two is empty for both files), so
every suite anchor holds at the base the spec names. One MEDIUM row records that the base nonetheless
predates the runner the spec's own commands need.

## Verdict: BLOCKED

Eight rows at BLOCKER, four at HIGH, eight at MEDIUM, one at LOW. Those twenty-one rows collapse to
**nine distinct defects**; the table below names which rows share one, so a fold that repairs a
defect repairs every row under it rather than twenty-one separately.

Two defects are blockers, and both are the same shape: round 2 handed the fold a MECHANISM and said
"settle it by running"; the fold took the mechanism and typed the number. **AC8 is unsatisfiable at
every boundary after `:1243`** (D-1): S5 dumps "the bare origin's heads" and diffs against fresh-start
state, AC8 owes a replay "observed FAILING when removed" wherever that diff is non-empty, and
`refs/heads/ahead` is pushed to the origin at `:1243` and deleted by nothing — `reset_tree` clears
only local `refs/remotes/` and `refs/replace/` — so the diff is non-empty at every boundary in region
two, `trunk` joins it after `:3047`, and origin `main` sits off `ANCHOR0` from `:1257` to `:1646`.
Nothing's verdict depends on `ahead` or `trunk`, so no replay of them can be observed failing, and
AC8 has no third outcome for non-empty-but-inert. The rev-4 log's "exactly one non-empty boundary"
is false at the spec's own base by the spec's own leak sentence. **S6 reds the correct whole-suite
run** (D-2): it pins `same "nine mutations ran in this process" "$MUT" 9` and says each mutating arm
in the counted block increments `MUT`, but the block from `# arm 1:` to the control holds TWELVE
`reset_tree`-led mutation cycles — arms 1 to 9 plus the three arm-6b fixtures `TOOL-aHoistedPass-2`
added after the control was labelled — none of them a `mutate()` call, so a build that does what S6
says reds the control in the UNSHARDED run, the verdict change §3 forbids and AC6 cannot see because
both sides carry the same new FAIL. That is round 2's D-1 shape again: a typed constant beside a
derived population, wrong against the file it cites, redding a correct build.

One defect is HIGH: AC4's two readings "at the SAME commit" cannot both exist, because S1 changes
`SHARD_ARITY` and `--shard i/2` is refused at any commit carrying it, and the two-shard POOLED reading
has no fixture — the budget file holds ONE unsharded row for this suite and the runner reads only
`$HERE/selftest-budgets.txt` — so the reading that decides the arity rests on a two-row edit the spec
nowhere describes (D-3). The medium rows are anchors and records: S1's hoist range starts at a helper
already in the prologue and stops twelve definitions short, and its 28 is 27 (D-4); S5 and §4 put
the producer "inside the `ahead` block" when the producer is the lifecycle block and the `ahead` block
is the leak (D-5); seven criteria costing hours carry no `cost:` line (D-6); after S2 no runner path
grades the suite whole, so a region no shard carries is green by absence (D-7); the declared base
predates the runner the ACs invoke (D-8); and `-7` S2 carries no note back although the rev-4 log
claims an edge the Edges block does not have (D-9).

**Convergence.** Under `memory/guides/BUILD-METHOD.md` (the paragraph at `:140`) the loop re-arms
only on a STRICTLY SMALLER confirmed-blocker count. Round 2 stood at nine blocker rows; this round
stands at eight. By the rule's letter the fold converged by one row and the loop RE-ARMS: the two
blockers here are folded and the fold is what round 4 measures. Read by defect, round 2's three
blocker defects became two, and both survivors are rev-4's own restatements of round 2's D-2 and
D-3 — the two the round-2 report closed with "answered by RUNNING" and "one helper and one assertion
per counted block" — so the direction is right and the remaining distance is one derived count and
one two-class rule. **Disposition of both standing blockers: FOLD.** Each is a defect in the document
this review read, each fix lies inside S5 or S6, and neither needs a mechanism this build lacks.
Nothing here needs a PROMOTE.

## Review shape

- raw 50 · confirmed 21 · refuted 29 · unverified 0 · precision 0.42

Precision at 0.42 is BELOW the ~0.5 floor `AGENTS.md` §8 sets, so the next round should tighten the
lens priming before it adds agents; the refuted twenty-nine were mostly rows that re-graded what
rev-4 had already fixed (the floor-graded `PROLOGUE_ARMS`, the block-edge cut rule, the substring
filter, the driver-row floor). Read the confirmed count with the table below in hand: the pipeline
reports zero duplicates because each row addresses a different clause, but four lenses hit the
AC8/S5 leak independently (four rows), four hit the S6 count (four rows), four hit AC4's missing
two-shard fixture (four rows) and three hit the hoist-set anchor (three rows, one of which also
carries the producer-anchor defect). Twenty-one rows is nine defects.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## The nine defects, and which rows carry each

| Defect | Rows (severity as adjudicated here) | Section |
|---|---|---|
| D-1 · AC8 is unsatisfiable: the `ahead` and `trunk` leaks make S5's diff non-empty at every boundary after `:1243`, and a verdict-inert difference has no replay that can fail | id=11 blocker · id=23 blocker · id=1 blocker · id=38 blocker | B1 |
| D-2 · S6 types 9 against a block holding 12 mutation cycles; built as written the control reds the correct whole-suite run | id=2 blocker · id=12 blocker · id=24 blocker · id=37 blocker | B2 |
| D-3 · AC4's two readings "at the SAME commit" cannot coexist, and the two-shard pooled reading has no fixture at any commit | id=3 high · id=14 high · id=26 high · id=40 high | H1 |
| D-4 · S1's hoist range names a prologue helper and stops twelve short; 28 is 27; S1 and §4 disagree on the set; AC10 can pass vacuously | id=5 medium · id=43 medium · id=35 low | M1 |
| D-5 · S5 and §4 put the producer "inside the `ahead` block"; the producer is the lifecycle block and the anchor text occurs four times | id=18 medium | M2 |
| D-6 · only AC4 carries `cost:`; AC1, AC2, AC6, AC8, AC9, AC10, AC11 are hours of suite time with no line and S1's loop is uncapped | id=19 medium · id=47 medium | M3 |
| D-7 · after S2 no runner path grades the suite whole; `FLOOR_ASSERTIONS` is never graded again and an `in_shard k > 8` region runs nowhere | id=31 medium | M4 |
| D-8 · the declared base `c2db2f5d` predates `TOOL-aBatchedArm-4`; `--pooled` and the `1/8` regex do not exist there | id=45 medium | M5 |
| D-9 · `-7` S2 carries no note back; the rev-4 log claims a `supersedes` edge the Edges block does not carry | id=46 medium | M6 |

## Round 2 against the fold, item by item

- **D-1 (AC1 false by construction)** — rev-4 took option (b): the floor-graded figure,
  `PROLOGUE_ARMS = 0`, the C21 pair named as an epilogue constant, the `:3153` comment left standing,
  AC1 restated as `sum(eight) == unsharded`. Verified against the file: the floor is at `:3168`, the
  pair at `:3186` onward. RIGHT. Not re-graded.
- **D-2 (seven replays from the arity)** — folded into S5 as a per-boundary ref-state diff rule and
  into AC8 as "replay where non-empty, skip where empty". WRONG: the rule as keyed is non-empty
  almost everywhere and the fold typed "exactly one": B1 here.
- **D-3 (AC9 has no mechanism)** — folded into S6 as a `MUT` counter the control asserts. RIGHT on
  the mechanism, WRONG on the number and INCOMPLETE on the block's extent and increment sites: B2.
- **D-4 (balance by invocation count)** — folded: cuts only at `reset_tree`-led block edges,
  re-balanced by S2's serial readings, every candidate recorded. RIGHT. The iteration has no cap,
  which M3 carries as cost rather than as a design defect.
- **D-5 (AC4 pools fourteen rows)** — folded: the substring `--kit` filter isolates the eight rows,
  and the width is asserted from the runner's own `SWEEP` line. Verified: `--kit` sets `FILTER` at
  `run-selftests.sh:116` and the eight argv literals share the script path. RIGHT.
- **D-6 (no two-shard wall for F2)** — folded: a two-shard reading is now taken. INCOMPLETE and
  wrong where it is placed: H1.
- **D-7 (the third carrier, fourteen helpers)** — folded: S1 hoists every region-local helper called
  past a cut, the count derived. RIGHT on the rule, WRONG on both anchors and the typed count: M1.
- **D-8 (driver row as pooled floor; `aTracedSpawn-1` inverted)** — folded in §1 and §3. RIGHT. Not
  re-graded.
- **D-9 (floors with no criterion)** — folded into S3/AC11 as ~3 % headroom with both figures beside
  each constant. RIGHT. Not re-graded.
- **D-10 (`-7` S2 and `-8` with no edge)** — half folded: §4 and §10 declare the supersession and F1
  resolves the join's home against `-8`; the note back into `-7` was not written: M6.
- **D-11 (anchors match neither tree)** — folded to text anchors. RIGHT in method; two of the new
  text anchors resolve wrong: M1 and M2. And the base they are declared against predates the runner
  the ACs call: M5.
- **D-12 (`cost:` prices a deleted row)** — folded: AC4's `cost:` is now derived from the runner's
  own bound. RIGHT for AC4; the other criteria still carry none: M3.
- **D-13 (the suite's own note unretargeted)** — folded into S4. RIGHT that both notes are named;
  INCOMPLETE on what the retargeted claim rests on once no run is whole: M4.
- **D-14 (`aRelaxedShard-4` miscited)** — dropped from §10 and `TOOL-dScriptedRepeat-15` disposed
  NOT-THIS-SEAM. RIGHT. Not re-graded.

---

# BLOCKERS

## B1 · id=11, id=23, id=1, id=38 — AC8 is unsatisfiable: the diff is non-empty at every boundary after `:1243`, and an inert difference has no replay that can fail

**Address:** section 2 S5 (`:55-63`), section 6 AC8 (`:198-202`), section 4 "Why the split is safe"
(`:112-116`), section 9 rev-4 log (`:240-242`, "AC8 expects exactly one non-empty boundary").

S5's dump covers "local branches, `refs/remotes`, the bare origin's heads and HEAD", diffed against
fresh-start state; a replay exists "exactly where a ref some arm at or after that line reads
differs". AC8 keys its obligation on the raw diff: "at every boundary where it is non-empty, the
replay is observed FAILING when removed", and its only other branch is "where it is empty, the arm
SKIPS naming the boundary and that no ref differed". There is no third outcome.

The origin-side producers, enumerated at HEAD and never undone:

- `check-unattended.test.sh:1243` — `git push -q -f origin "$ahead:refs/heads/ahead"`. The only
  write to that ref. A grep for `:refs/heads/ahead`, `--delete` and `update-ref -d` over the file
  finds no deletion; the bare origin created at `:177` is never recreated; `reset_tree` (`:240-246`)
  deletes only local `refs/remotes/` and `refs/replace/` and re-pins `refs/remotes/origin/main`;
  `anchor_restore` (`:284-295`) re-pins `main` only. So `refs/heads/ahead` differs from fresh-start
  at EVERY boundary from `:1243` to exit — the whole of region two, on every candidate eight-cut.
- `:3046-3047` — `git branch -f trunk main` and `git push -q origin trunk`, never deleted either. Same
  class, after `:3047`.
- `:1257` — the lifecycle block's `git push -q -f origin main` leaves origin `main` off `ANCHOR0`
  until the tWaive restore at `:1646` (`:1112`'s `unit:main` push is undone at `:1135`). Any boundary
  inside `(:1257, :1646]` differs on `main` too, and a cut may place zero, one or two boundaries there.

And under S5's OWN read-keyed rule these are read: `check-unattended.sh:912` runs
`observe_remote ls-remote --heads` on every `run()` and feeds `ADV_TIPS` from it, so every advertised
head — `ahead` and `trunk` included — is a ref an arm at or after the boundary reads. S5's predicate
and AC8's raw-diff predicate therefore AGREE that the diff is non-empty at every boundary after
`:1243`; the spec's "expected at exactly the boundary preceding the shard holding the consumer" and
the rev-4 log's "exactly one non-empty boundary" are false under both, at the spec's own base, by the
spec's own sentence naming the leak.

What AC8 then demands cannot be produced. `ahead` is a child of `ANCHOR0` already published via
`main`; `trunk` is `main` renamed; no later arm's verdict depends on either — `TOOL-aShardedFloor-3`
§3 records the `ahead` leak as real and verdict-inert, and the existing `SH_I = 2` replay at
`:1289-1293` omits it with shard 2 green. So at every `ahead`-only boundary there is no replay whose
removal can fail, AC8's red clause "a non-empty boundary's replay is absent" fires, and the builder's
choices are a replay nothing can observe or an AC left unmet. That is the could-not-fail class round
2's B2 flagged, re-created for a different ref: round 2 asked for "replayed or SHOWN UNREAD", and the
fold kept only "the dump must catch it".

Two smaller consequences. S5's "the arm SKIPS naming the boundary" is written as a runtime line, but
a shard run has no whole-run state to diff against — the dump is an offline, once-per-cut
measurement — so the skip cannot be emitted where AC8 places it. And "if that shard does not also
hold the producer" is the one cut-dependent clause S5 got right; the count of replays inside the
`(:1257, :1646]` window is derived from the cut, zero, one or two, and "exactly one" would read a
correct two as a defect.

**Fix.** Split the rule into two classes and make the count DERIVED. Per boundary, every differing
ref carries a disposition: **verdict-bearing** — replayed, observable AC8's red-when-removed — or
**read but inert** — named in the build log with the arm scan that found no verdict reading it,
observable AC6's per-boundary FAIL-set identity (the brief's "settle by RUNNING": run the shard bare,
compare its FAIL set to the same arms' whole-run FAIL set; a replay exists exactly where they differ,
and the dump is the diagnostic that says what to replay). Name `refs/heads/ahead` and `trunk` as the
measured-inert class today. Strike "exactly one" and "expected at exactly" from S5, §4 and the rev
log; say the count is derived from the chosen cut and that every boundary inside the
producer-to-restore window replays. Drop the runtime skip line: a replay block is guarded
`if [ "$SH_I" = k ]` like the existing one, and a boundary with nothing to replay is recorded, not
printed. Lazier and also honest: close the leaks at source in S5 — `git push -q origin
:refs/heads/ahead` after the check-9 arm and the same for `trunk` after `:3047` — so the raw diff and
the verdict predicate coincide and the inert class is empty by construction; say which was chosen.

**Left-shift gate.** The per-boundary AC6 comparison IS the gate: a staged shard run whose FAIL set
matches the whole run's for the same arms proves the boundary needs no replay, and one that does
not names the arm. Record it once per cut in the build log as a table — boundary, raw diff,
disposition per ref, FAIL-set delta — so a reader can see a non-empty diff beside a zero delta and
not mistake it for a missing replay.

## B2 · id=2, id=12, id=24, id=37 — S6 types 9 against a block holding 12 mutation cycles; built as written the control reds the correct whole-suite run

**Address:** section 2 S6 (`:64-69`), section 6 AC9 (`:203-205`), section 3 "must not change any
arm's verdict" (`:77-78`), section 5 risks (`:154-156`).

S6: "Each mutating arm in its counted block increments a process-local `MUT`, and the control asserts
`same "nine mutations ran in this process" "$MUT" 9` BEFORE calling `run`". The block, at HEAD, from
`# arm 1: the kit ships no template` (`check-unattended.test.sh:1409`) to the control `same "the tree
is still clean after nine mutations"` (`:1513`), counted `reset_tree`-led line by line:

- arms 1 to 9 at `:1410`, `:1416`, `:1422`, `:1426`, `:1431`, `:1436`, `:1497`, `:1502`, `:1506` —
  nine;
- arm 6b, headed `# arm 6b: THE BODY TERM (TOOL-aHoistedPass-2)` at `:1455`, three `reset_tree;
  _bm_sections … > memory/guides/BUILD-METHOD.md` cycles at `:1482`, `:1485`, `:1490` — three more;
- the control's own bare `reset_tree` at `:1512`, which mutates nothing.

Twelve mutation cycles, twelve `hit "$(run)"` calls, ten labelled arms, ZERO `mutate()` calls — the
edits are `mv`, `grep -v … && mv`, `sed -i`, `printf >` and `_bm_sections >`. The control's "nine"
and the block header's "Nine branches, nine arms" (`:1404`) both predate arm 6b and are stale
against the file today.

So S6 has two readings and both break the suite. Per mutating arm, `MUT` is 10 (or 12 per site) at
the control and `same … "$MUT" 9` REDS in the unsharded run at the landing commit — a new FAIL line,
the verdict change §3 forbids, and AC6 cannot see it because the eight shards and the whole run carry
the same new FAIL. Per `mutate()` caller, of which the block has none, `MUT` is 0 and the control reds
everywhere. The only green implementation instruments nine of twelve sites by hand, which the spec
does not say and which leaves three mutations the control does not count. A typed 9 beside a
population the spec did not derive is the §7 class, and the spec's own hoist-set sentence — "DERIVED
at build time, never asserted" — is the rule S6 breaks four lines later.

**Fix.** S6 states the block's extent by text (`# arm 1: the kit ships no template` through the
control), the increment site (the `reset_tree;` line of every mutation cycle in it, arm 6b's three
included), that `mutate()` is NOT the hook (99 callers file-wide would count into `MUT`), and that
the asserted value is DERIVED — the count of `MUT=$((MUT+1))` lines in the block at build time,
written into the `same` label and the control's comment in the same commit as a LABEL change, not a
verdict change. AC9's grep key becomes the derived label. The lazier variant, which adds no counter
and touches none of the twelve arms: capture `_c16=$n` at the block's first line and have the control
assert `$((n - _c16))` against the block's own cycle count derived from `$0` (`grep -c '^reset_tree;'`
between the `# arm 1:` marker and the control); a control moved alone aborts under `set -u`, moved
with its marker it reads 0 — both red, which is what AC9 needs. Either way, relabel "nine".

**Left-shift gate.** Make the control's expected value a derivation the control performs itself, so
the next arm added to the block cannot stale it: the `grep -c` over `$0` above is the gate, and a
comment beside it says the number is read, never typed. AC6 then stays the check that the unsharded
run's FAIL set did not move.

---

# HIGH

## H1 · id=3, id=14, id=26, id=40 — AC4's two readings "at the SAME commit" cannot coexist, and the two-shard pooled reading has no fixture at any commit

**Address:** section 6 AC4 (`:176-187`, "the two-shard longest wall taken at the SAME commit before
S1 landed"), section 4 measurement paragraph (`:102-106`), Rollout (`:130`), Alternatives
(`:138`), F2 (`:230-232`), §5 perf (`:149`).

Two impossibilities. First, `SHARD_ARITY` is a constant in the suite (`check-unattended.test.sh:29`,
2 today), S1 sets it to 8, and the arity refusal is exact — so `--shard i/2` is refused at any commit
carrying S1 and `--shard i/8` at any commit without it. "Two readings at the same commit" across a
change to that constant is two commits by construction; the spec says "before S1 landed" and "after"
in the same sentence and then calls both the same commit.

Second, the two-shard POOLED reading the runner's `SWEEP` line reports needs two `--shard i/2` budget
rows, and none exist anywhere. `tools/run-gates/selftest-budgets.txt:114` is the ONE row for this
suite, unsharded (`bash tools/unattended/check-unattended.test.sh`, budget 13600 against a 9067 s
reading), S2 itself calls it "the single unsharded row", and no `--shard` row exists in the budget
file, `tools/gate-legs.json` or the kit's `kit.toml`. `run-selftests.sh:35` hard-codes
`BUDGETS="$HERE/selftest-budgets.txt"` with no override — the only knobs are `SELFTEST_OUTER_WIDTH`,
`SELFTEST_WALL` and `SELFTEST_TIMEOUT_BIN` — and `--pooled` runs declared rows only, each bounded at
budget × `sweep-ceiling-factor`. So `run-selftests.sh --pooled --kit tools/unattended/check-unattended.test.sh`
at S1's parent runs ONE unsharded suite, N = 1, and prints an unsharded wall. A builder following the
Rollout ("AC4's two-shard reading is taken FIRST, before any of it") records the wrong quantity, and
AC4's `fixture:` line names only "the eight rows", which is exactly the field the template provides to
say what a reading needs and whether the tree holds it. The recorded pair in `run-unattended-gates.sh`
(`:207`, "846.0 + 2013.7") is pre-de-spawn and bar-dilated, not like for like. The ratio that decides
the arity — F2's "RESOLVED … MEASURED rather than argued" — rests on a reading the spec's own instrument
cannot take.

**Fix.** Replace "the SAME commit" with "the same BASE: the two trees differ only by this unit's
diff". Name the two-shard fixture in AC4's `fixture:` line: on the frozen clone at B = S1's parent
sha, an UNCOMMITTED edit of `selftest-budgets.txt` replacing `:114` with `--shard 1/2` and
`--shard 2/2` rows, budgets = the whole row's 13600 (or the last recorded sharded pair × 1.5 by the
file's own rule), run through the identical `--pooled --kit` invocation; the eight-shard reading at
the unit's tip; both shas and the scratch diff recorded verbatim beside the walls in the AC4 record.
Say "like with like" is the arm set (AC1 and AC6 hold at both readings), not the commit.

**Left-shift gate.** The AC4 record carries the two shas and the `SWEEP of N suite(s)` line from each
run, with N = 2 and N = 8 asserted by grep; a record whose two-shard line reads N = 1 is the wrong
quantity and reds by inspection.

---

# MEDIUM

## M1 · id=5, id=43, id=35 (low) — S1's hoist range names a prologue helper and stops twelve short; 28 is 27; S1 and §4 disagree on the set; AC10 can pass vacuously

**Address:** section 2 S1 (`:33-36`, "28 helpers are defined inside the regions today
(`anchor_restore` at the text `anchor_restore() {` through `frozen`)"), section 4 "Why the split is
safe" (`:111-112`, "Functions: 28 are defined inside regions"), section 6 AC10 (`:206-209`).

Verified at HEAD. `anchor_restore() {` is at `check-unattended.test.sh:284`, ABOVE region one's
`if in_shard 1; then` at `:299`, under the comment `HOISTED FOR THE SHARD CONTRACT` at `:268` — it is
the file's EXISTING hoist set, not a region-local helper. Column-0 definitions strictly between the
first `in_shard` and the floor grade number 27: six in region one (`dispconf` at `:843` through
`noop_break` at `:1207`) and twenty-one in region two (`_bm_sections` at `:1459` through `land_as` at
`:3024`). `frozen` (`:2067`) is followed by twelve more (`add_mode` at `:2124` … `land_as`), so the
range stops twelve definitions short at one end and starts one helper above the region at the other.
The 28th match of a naive `\(\) *\{` regex over the file is the quoted string `'fail() { :; }'` inside
the `for _hijack in` list at `:311`, which is data, not a definition. The spec types 28 in S1 and again
in §4 while saying the count is "DERIVED at build time, never asserted".

Two definitions of the set also coexist: S1 says "every helper defined inside a region and CALLED PAST
A CUT is hoisted", §4 says "28 are defined inside regions … S1 hoists them" — all of them — and AC10's
observation ("hoisting all but one and running the shard that calls it") reads as all. Every
region-local helper's use span today lies inside its own region — the longest, `pedit`, is
`:1912→:2248`, 336 lines — so a cut that crosses no span leaves AC10 with no instance to un-hoist and
it passes vacuously; a cut that does cross one has an instance the spec should name.

**Fix.** One rule: hoist only helpers whose use span crosses the chosen cut, the set DERIVED from the
cut. Define the derivation: definition lines matching `^[A-Za-z_][A-Za-z0-9_]*\(\) *\{` strictly
between the text `if in_shard 1; then` and the text `fi   # ---- end REGION TWO`, excluding matches
inside quotes; drop the named endpoints and the typed 28, or mark the figure PINNED at this base with
the awk that produced it. Give AC10 a SKIP shape that names the cut when no helper crosses it, or make
the instance deliberate by naming the crosser the record un-hoists.

**Left-shift gate.** The derivation above, run at build time and written into the build log beside
the cut, so the hoist set and the cut are one record; AC10's staged break then names a helper from
that list rather than "one".

## M2 · id=18 — S5 and §4 put the producer "inside the `ahead` block"; the producer is the lifecycle block and the anchor text occurs four times

**Address:** section 2 S5 (`:58-59`, "one producer today (the text `git push -q -f origin main`
inside the `ahead` block)"), section 4 "Why the split is safe" (`:112-113`, "region one's `ahead`
block force-pushes `main` and leaves `unit` its ancestor").

Verified at HEAD. The `ahead` block (`check-unattended.test.sh:1230-1245`) pushes
`refs/heads/ahead` and nothing else; the producer of "unit is an ancestor of main" is the LIFECYCLE
block at the text `THE LIFECYCLE` (`:1247-1261`), whose `git checkout -q main && git merge -q --no-ff
unit -m "land the run"` at `:1252` plus `git push -q -f origin main` at `:1257` is what the tWaive
merge at `:1588` fast-forwards onto. And the anchor text `git push -q -f origin main` occurs at
`:278`, `:1257`, `:1585` and `:1646` (with variants at `:1112` and `:1291`), so it resolves to no one
line. §1 promises text anchors "so a moved line is a moved anchor rather than a wrong one"; this one
is wrong at the base itself, and a builder following it instruments the leak as the producer — the
same confusion B1 is made of. The row also carries M1's `anchor_restore` point.

**Fix.** S5 and §4: "the lifecycle block at the text `THE LIFECYCLE`, whose `git merge -q --no-ff
unit -m "land the run"` plus force-push is the producer; the `ahead` block at the text
`"$ahead:refs/heads/ahead"` is the leak". Anchor by a text that occurs once.

**Left-shift gate.** A text anchor must be unique in its file: a one-line check over the spec's
backticked anchors (`grep -c -F` per anchor against the file it names, expecting 1) reds an anchor
that resolves to four lines or to none. Cheap, and it would have caught D-11 last round too.

## M3 · id=19, id=47 — only AC4 carries `cost:`; seven criteria are hours of suite time with no line, and S1's loop is uncapped

**Address:** section 6 AC1, AC2, AC6, AC8, AC9, AC10, AC11 (`:165-213`), section 2 S1 (`:31-33`,
"iterating until `max(shard)` is within a declared tolerance").

`memory/TEMPLATE-SPEC.md:346` owes `cost:` "when it is not seconds" and `:343` says an omission "gets
paid for in build-time amendments"; this spec's own rev-4 log records folding a `cost:` onto AC4 for
that reason. AC1 needs eight shard runs plus one unsharded run of a suite whose budget row records
9067 s; AC6 needs the same nine captures; AC2, AC9, AC10 and AC11 each stage a break and run one shard
(~1100 s at an even cut); AC8 is one run per boundary it replays; and S1's candidate-cut loop adds a
serial pass per candidate with no cap and no declared tolerance value. At one balance iteration the
DoD is roughly eight to nine hours of suite time; beyond it, unbounded. Nothing in the spec says so
or says which runs are shared.

**Fix.** AC1 carries `cost:` and states its eight readings ARE S2's final serial pass plus one
unsharded run; AC6 says it is read from those same outputs; AC2, AC8, AC9, AC10 and AC11 share one
`cost:` line (one shard run each, ≈ sum/8, AC8 per replayed boundary); S1 names the tolerance and a
cap on iterations, and the derived total in suite-runs sits beside it.

**Left-shift gate.** The template's own rule is the gate; a hygiene arm that reds a `figure:` line
with no `cost:` beside it when the criterion names a run would make it mechanical, but the reader of
§6 is the check today.

## M4 · id=31 — after S2 no runner path grades the suite whole; `FLOOR_ASSERTIONS` is never graded again and an `in_shard k > 8` region runs nowhere

**Address:** section 2 S4 (`:50-54`, the retargeted whole-suite notes), section 2 S3 (`:43`,
"re-measure `FLOOR_ASSERTIONS`").

Verified. Today the only caller of `check-unattended.test.sh` is the one unsharded budget row
(`selftest-budgets.txt:114`); `run-unattended-gates.sh --selftests` (`:135`) delegates to
`run-selftests.sh --kit tools/unattended`, which runs declared rows only. S2 replaces that row with
eight `--shard` rows and AC3 requires exactly eight, so after this unit no runner path executes the
suite whole: the `FLOOR_ASSERTIONS` S3 re-measures is graded by no declared run, and `in_shard()`
(`[ SH_I = 0 ] || [ SH_I = N ]`) makes a region guarded by an index no row carries run nowhere and
red nothing — a de-collected test, the charter's green-by-absence class and the one the floors exist
for. The gov canary's join (`run-gates.gov.test.sh:346-407`) checks declared indices 1..N against the
rows' own arity and says outright it does not check that a shard runs the region it claims; S4
retargets both whole-suite notes at that join with no compensating check.

**Fix.** S4's retargeted note states what survives once no run is whole — the join, the per-shard
floors, and AC1's identity as a recorded measurement — and the ported join gains one derived check:
every `in_shard <k>` literal in a `--shard`-called script satisfies `k ≤` its `SHARD_ARITY`, so an
unrunnable region reds statically.

**Left-shift gate.** That check is the gate. Stage `in_shard 9` around an empty block, observe the
join RED, unstage.

## M5 · id=45 — the declared base `c2db2f5d` predates `TOOL-aBatchedArm-4`; `--pooled` and the `1/8` regex do not exist there

**Address:** status line (`:3`, "base c2db2f5d"), section 1 anchor paragraph (`:24-25`), Edges
(`:86-87`), AC3 and AC4 (`:173-187`).

Verified with git: `c2db2f5d` is an ancestor of `3bb5c8a2` (the regex that admits a numeric-ratio
token) and of `0422ea2e` (both runners declare `--serial`/`--pooled`); `git show
c2db2f5d:tools/run-gates/run-selftests.sh` contains zero occurrences of `--pooled` where `0422ea2e`
has ten. The status line pins that base and §1 says every anchor is against it, while Edges consume
`-4` and AC3/AC4 invoke `--pooled` and the `--shard i/8` rows. The suite and budget files ARE
byte-identical between the base and HEAD, so the suite anchors hold; the runner the ACs call does
not exist at the tree the record names.

**Fix.** Bump the base to `0422ea2e` or later; the anchors are by text and survive. Keep "every anchor
is against the tree at this base" true.

**Left-shift gate.** The kickoff's pinned BASE is the source; a spec whose `consumes-from` edge names
a unit CLOSED after its own base is a one-line check over the two shas that a records leg could carry.

## M6 · id=46 — `-7` S2 carries no note back; the rev-4 log claims a `supersedes` edge the Edges block does not carry

**Address:** section 4 first paragraph (`:95-97`), section 10 dispositions (`:271-272`), section 9
rev-4 log (`:249`, "`supersedes` edge to `aGradedDoorway-7` S2"), Edges (`:84-89`).

Grep for `aBatchedArm` across `memory/builds/aGradedDoorway/` and `memory/backlog/TOOL.md` returns
nothing; `-7`'s S2 still reads "Ordered AFTER S4 at rev-3" with no pointer, and its backlog row
(`TOOL.md:286`) says "S4 now precedes S2". Round 2's M1 fix named the annotation "in the same
commit"; the rev-4 commit (`dfc402fc`) touched only this build's records. The rev-4 log records a
`supersedes` edge while §4 itself says the grammar admits none, so the log misdescribes what was
done. §6's supersede-with-a-note rule is applied on one side: whoever closes `-7` finds S2 open with
its ordering intact and no pointer to the record that carried it.

**Fix.** Annotate `-7` S2 ("the check-unattended half is carried by `TOOL-aBatchedArm-3`; the driver
half stays here") and its backlog row in the next records commit; cite that commit in §9; correct the
rev-4 log line to say the supersession is stated in §4 prose, not as an edge.

**Left-shift gate.** A record that declares a supersession names the commit that annotated the
superseded side, and the hygiene leg that already joins `Serves:` ids can join a `SUPERSEDED` word to
a citation in the named spec. Until then, the §6 rule and the reader.

---

## What a fold should do first

B1 and B2 are one decision each, and the same decision: derive, do not type. B1 is answered by the
per-boundary AC6 run the round-2 brief already asked for — run each candidate shard bare, diff its
FAIL set against the whole run's for the same arms, and let the ref dump explain any delta — with
`ahead` and `trunk` either closed at source or written down as the inert class. B2 is a `grep -c`
over the block in the control itself and a relabel. Once both are derived, "exactly one" and "nine"
leave the spec and cannot be wrong again.

H1 is a sentence and a fixture line: "same base", and the two-row scratch edit at S1's parent named
in AC4's `fixture:`. Do it before the Rollout's "taken FIRST" is followed literally at a commit where
it measures the wrong thing.

The medium rows are anchors and bookkeeping and can land in one records commit: the hoist range
bounded by the region markers with the count derived (M1), the producer anchored at `THE LIFECYCLE`
(M2), `cost:` on the seven criteria (M3), the `k ≤ SHARD_ARITY` check named in S4 (M4), the base
bumped past `0422ea2e` (M5), and the note into `-7` (M6). Precision this round was 0.42; the next
lens fan should be primed with rev-4's closed items as by-design so it hunts the fold, not the
history.
