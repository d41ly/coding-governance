**Serves:** spec-audit TOOL-cSteadyMetronome-1

## Verdict: BLOCKED

Three lenses ran over `TOOL-cSteadyMetronome-1` rev-1 (Tier-2 spec audit, M4 synthesis). 19 raw
findings; 15 confirmed, 4 refuted, precision 79%. No dead lens — every lens landed at least one
confirmed finding (L1: 5, L2: 3, L3: 7). After merging duplicates the confirmed set is 11: **2
BLOCKER, 4 HIGH, 2 MEDIUM, 3 LOW**. Two findings were reproduced by running the real unmodified
runner rather than reasoned about. Shorthand below: `spec:N` = this build's
`spec/2026-08-14-spec-cSteadyMetronome-1.md` line N; `test:N` = `tools/run-gates.test.sh`; `run:N` =
`tools/run-gates.sh`.

---

### R1 - BLOCKER - The per-fixture timestamp scheme is unimplementable: three legs run one script

*(raw 1 + raw 13, lenses L1 and L3; raw 8 folded in — see Refuted.)*

**Claim.** S1's `fx/<name>.start` / `fx/<name>.end` keying (spec:69-79) cannot produce per-leg
records. Four legs run only TWO scripts, and the runner hands a leg no identity, so three of the four
write the same two paths. Both of S1's load-bearing sentences are false against source, and §4's
"read the four pairs" is arithmetically impossible.

**Evidence.**
- `test:76` writes exactly ONE `fx/mid.sh`; `test:81-85` declares four legs of which `beta fast`,
  `gamma fast` and `delta fast` all carry the byte-identical argv `["bash", "fx/mid.sh"]`.
- `run:137-140` splits that argv and execs `"${argv[@]}" </dev/null` verbatim — no per-leg argument,
  no per-leg variable exported into the child. A fixture cannot self-key.
- Reproduced (L3, real unmodified runner, spec's exact scheme, width 4, three reps): the
  `fx/<name>.{start,end}` set was always exactly `mid.start mid.end slow.start slow.end` — 4 files
  for 4 legs, not 8. So `spec:83`'s "the four pairs" yields TWO, and `spec:76-77`'s "two concurrent
  fixtures never write the same path" is false for three of the four.
- Because `.start` and `.end` are SEPARATE files (spec:71-74), the survivor is `[max start, max end]`
  and the endpoints need not come from one process — rep 2 produced a record whose start came from
  pid 1003352 and whose end came from pid 1003340.
- **Failure direction, corrected against raw 8:** `max start` is always >= the max-end leg's own
  start, so the franken-interval is a SUBSET of a real leg's interval. It cannot fake an overlap; it
  can HIDE one (slow `[0,2]` with mids at `[0.5,2.0] [1.0,2.5] [2.5,4.0]` leaves mid = `[2.5,4.0]`
  and no intersection). The collision therefore reintroduces the false RED this unit exists to
  retire, and the surviving start is measured to be the LAST mid to start (+602/+504/+651ms over
  three reps) — the clobber selects precisely the worst-case leg for the assertion. It also silently
  shrinks AC2's population from 6 comparisons to 1.
- The spec never picks the mechanism that would make per-leg keying reachable, and one obvious
  candidate is closed: splitting `mid.sh` into three scripts breaks arm 3d, whose `cp bad.sh mid.sh`
  (`test:122`) is exactly what produces its `gates RED — 3/4 legs failed` assertion (`test:128`) —
  while §3 (spec:32) declares arm 3d untouched.

**Spec edit.** In §4 Data model, key the record on the INVOCATION, not the script. Replace the table
rows with `fx/ts/<leg>.start` / `fx/ts/<leg>.end` and add one Inventory row naming the mechanism:
extend the scratch manifest at `test:81-85` to `["bash", "fx/mid.sh", "beta fast"]` (etc.) and have
each fixture write `fx/ts/$1.start` / `fx/ts/$1.end`, defaulting `$1` to its own basename. State in
§4 that `fx/mid.sh` is shared by three legs (`test:76`, `test:82-84`), that the runner exposes no leg
name (`run:135-140`), and that `mid.sh` must STAY one shared file because arm 3d depends on it. Add
to S1: "a fixture run by more than one leg is keyed by the leg name it is passed, never by its script
name." Delete "read the four pairs" from spec:83 and make the arm assert it found exactly four pairs
before comparing — the count is the guard against the `fixture-passes-by-finding-nothing` shape.

---

### R2 - BLOCKER - Intersection is not load-independent: the arm rests on unmeasured dispatch skew

*(raw 14a + raw 9, lenses L3 and L2; raw 4 folded in — see Refuted.)*

**Claim.** §1's "a fact about the RUNNER that no amount of machine load can change" (spec:7-8) and
§4's "Why intersection is immune" (spec:60-65) are false as stated. Intersection is immune to per-leg
SLOWDOWN but depends entirely on the SKEW between fixture start instants, which is almost pure
process-spawn cost — the single most contention-sensitive component in the system, and the exact axis
the corpus already identified (see R6). The spec bounds none of it, measures none of it, and lists
no such risk.

**Evidence.**
- The instant is recorded INSIDE the fixture, after the whole spawn chain: the dispatch loop pays a
  `live()` subshell plus `jobs -rp | wc -l` per decision (`run:180`, `run:184`), forks `runleg &`
  (`run:187`), which forks `date +%s%N` (`run:139`) and then `bash fx/*.sh` before the fixture's
  first line runs. `sleep` needing no CPU (spec:62) is irrelevant to the quantity that decides the
  assertion.
- Measured on this node at width 4, first→last leg START spread: 602 / 504 / 651ms in one batch,
  then 935ms minutes later on the same tree — against `slow.sh`'s 2000ms sleep (`test:75`). That is
  2.1x-3.3x headroom, visibly moving, not immunity.
- The dilation factor is already recorded in-tree by this same arm: `test:115-116` records the
  width-4 run at 2.7-3.6s idle but 4.1-9.8s contended, and `README.md:34-37` records contended
  width-4 runs of 17146ms and 32649ms against the same 2s sleep floor — non-sleep overhead dilating
  ~10-20x. 600-900ms of skew × 3-10 crosses the 2000ms budget.
- The retired arm's own arithmetic agrees the axis is overhead-vs-sleeps: with fixed overhead S,
  `2(S+2) < S+6.5` only ever passed when `S < 2.5s`.
- The Inventory (spec:87-97) leaves the 1.5s/2.0s sleeps at `test:75-76` unchanged, and §5's risk
  list (spec:130-131) names only a coarse clock.

If the skew exceeds the shortest fixture sleep, the new arm reds a correct runner under exactly the
AC6 condition — the same flake in a new form, minus the elapsed-time number that used to explain it.

**Spec edit.** (a) Delete the absolute immunity language at spec:7-8 and spec:65 and replace §4's
"Why intersection is immune" with the bound that is true: "the arm is sound while the smallest
pairwise dispatch skew stays below the earlier leg's sleep; measured on node c at width 4, first→last
start spread 504-935ms against a 2000ms sleep, adjacent-mid spread 88-247ms against 1.5s." (b) Add a
§5 risk row for dispatch skew, naming the knob that absorbs a regression (lengthening the fixture
sleeps). (c) Add an AC and an Inventory row: the failure message prints each recorded interval AND
`max start − min start`, so a future red says whether the pool or the node produced it. (d) Before
landing, measure the skew under the same second-bar contention that produced `README.md:34` and
record the figures in §4 the way the README records the nine elapsed-time runs — or make overlap
independent of the scheduler (each fixture writes `.start`, then waits bounded for the peers' `.start`
files before sleeping, so a rendezvous and not the scheduler's punctuality is what the arm reads).

---

### R3 - HIGH - The set of pairs the arm evaluates is never fixed, and §4 picks the worst one

*(raw 2 + raw 14b, lenses L1 and L3.)*

**Claim.** spec:83-85 uses "pair" in three senses in three sentences, and §4 and AC1 range over
different comparison sets. §4's chosen set — "the two longest-lived fixtures" — is exactly one
fixture-pair, and it is the least robust pair available, precisely under the AC6 condition.

**Evidence.**
- spec:83 "the four pairs" = (start,end); spec:84 "at least one pair intersects" = (fixture,fixture);
  spec:85 "the pair is the point" = the two assertions. Over two fixtures there is exactly ONE
  fixture-pair, so AC1 (spec:140) "at least one pair" and AC2 (spec:142) "NO pair" range over a set
  the spec never fixes — 1 comparison or all C(4,2)=6.
- Dispatch order is longest-first from the timing cache (`run:110`); the width-1 run at `test:93`
  writes that cache before the width-4 run at `test:94`, so `alpha slow` is dispatched FIRST in both.
  "The two longest-lived fixtures" therefore selects slow (first dispatched) and the longest mid
  (last dispatched) — the MAXIMUM-skew pair.
- Measured at width 4: 6 of 6 pairs intersected, with adjacent mids starting only 88-247ms apart
  against 1.5s lifetimes (6-15x headroom) versus 2.1-3.3x for the slow/last-mid pair. §4 discards
  roughly 3-5x of the margin AC1 promises.
- "Longest-lived" is also measured post-hoc from the very contended durations this unit exists to
  stop depending on, so a descheduled mid can outmeasure `alpha slow` and the compared pair silently
  changes identity run to run.

**Spec edit.** Replace spec:83-85 with: "After each scratch run, read the four (start, end) records
and compute intersection over ALL pairs of intervals. At width 4 at least one pair must intersect; at
width 1 no pair may. Both are asserted, and the negative control is the point: one arm alone is
satisfied by any implementation that records timestamps." Delete "the two longest-lived fixtures".
Restate AC1 (spec:140) and AC2 (spec:142) over the same all-pairs set so `pair` carries one meaning
throughout.

---

### R4 - HIGH - "At least one pair intersects" is strictly weaker than the assertion it replaces

*(raw 10, lens L2.)*

**Claim.** spec:65's "The property is preserved" is false. Any pool that reaches width 2 satisfies
the new arm, while the retired ratio red on exactly that regression — so the replacement drops
detection of every partial-width regression, and nothing else on the bar covers it.

**Evidence.** At width 2 the schedule is slow+mid, then mid at 1.5s and mid at 2.0s: `par ≈ S+3.5`,
`ser ≈ S+6.5`, so `2(S+3.5) < S+6.5` requires `S < -0.5` — unsatisfiable, i.e. the retired ratio REDS
a width-2 clamp. The proposed arm passes it under either reading of R3's comparison set: slow `[0,2]`
intersects mid `[0,1.5]`, and "the two longest-lived fixtures" selects that very pair. The clamp
block at `run:74-82` is live code, and arm 3f (`test:141-156`) only asserts that a garbage width still
runs every leg, never the resulting width. §4 names only full serial degradation as the failure it
still catches (spec:63-65).

**Spec edit.** Either (a) assert the PEAK, not the existence: add to S2 and §4 "the arm computes the
maximum number of intervals covering a common instant and requires it to reach the requested width —
4 at width 4, and the negative control becomes peak == 1", restating AC1/AC2 accordingly; or (b) keep
the weaker form deliberately and say so in §3 as an explicit non-goal — "a partial-width regression is
no longer detected by this arm" — naming what does detect it. **The choice is coupled to R2 and R3
and must be made knowingly:** peak == 4 requires ALL four intervals to cover one instant, i.e. total
dispatch skew < 1.5s, which is a strictly harder skew budget than the all-pairs form R3 recommends
(88-247ms measured). Whichever is chosen, §4 must state the budget it is spending.

---

### R5 - HIGH - The width-1 intervals AC2 asserts on no longer exist when arm 3c runs

*(raw 15, lens L3; raw 11 folded in — see Refuted.)*

**Claim.** With the clear placed inside `run_scratch`, the width-4 run erases the width-1 records
before arm 3c reads anything, and the Inventory lists no site that captures them in between.
Separately, §3 forbids editing the block the change must edit.

**Evidence.** Both scratch runs are inside arm 3a — `test:93` (`run_scratch 1`) and `test:94`
(`run_scratch 4`) — while arm 3c is at `test:118`, after both; `run_scratch` is then called again at
`test:123` and `test:137`. spec:78 and Inventory row spec:92 put the clearing in `run_scratch`, so by
`test:118` only the width-4 records survive and AC2 (spec:141-143) has no data. The Inventory
(spec:88-97) lists seven rows and none snapshots, copies or namespaces the width-1 reading. Meanwhile
§3 (spec:32-33) declares arm 3a "unaffected and untouched" while Inventory row spec:96 removes
`ser_ms`/`par_ms` and the two `date` fences, which sit physically on `test:93-94` inside arm 3a's
block.

The negative control itself is sound — verified: at width 1 the runner dispatches only while
`live() < JOBS` (`run:184`) and the forced-progress path (`run:205-208`) fires only when nothing is
running, so no two fixtures can overlap; measured 0 of 6 intersecting pairs with 1.1-2.7s of dead
time between legs. The defect is purely that the spec cannot read it.

**Spec edit.** Add an Inventory row for the capture, naming one mechanism: `run_scratch` writes its
records under `fx/ts/w$1/` and empties only that directory, so each width's evidence survives the
other run; arm 3c at `test:118` then reads `fx/ts/w1/*` and `fx/ts/w4/*`. (The alternative — asserting
the width-1 control between `test:93` and `test:94` — is acceptable but must be written down, because
nothing today says when the read happens.) Rewrite §3's first bullet to stop claiming arm 3a is
untouched: name what changes there (the two `date` fences leave) and scope the non-goal to arm 3a's
ASSERTION.

---

### R6 - HIGH - The spec re-adopts a diagnosis the corpus retired one commit ago, and §10 misses the row it closes

*(raw 16, lens L3.)*

**Claim.** §4's statement of the defect reverts to the narrow "load-sensitive" reading that commit
`9d371c0` — the immediate predecessor of this spec's base — explicitly retired, and §10's "no earlier
ruling this unit re-opens" is written without ever finding the OPEN backlog row this unit closes.

**Evidence.** `memory/backlog/TOOL.md:85` carries `TOOL-cFinalBerth-5 · OPEN`: the ratio "FLIPS run to
run on one tree: red then GREEN on two consecutive full bars at 550d9b6, no edit between, red missing
by 4.5%. Its fixtures are fixed sleeps, so the margin is overhead-dependent". `git log -1 9d371c0`
states: "the assertion's headroom is a function of how per-process overhead compares to those sleeps
— machine-dependent by construction. The earlier reading of 'load-sensitive' was too narrow; it flips
unloaded too." The spec reverts to the narrow reading verbatim at spec:49-50 ("can only be satisfied
when the machine actually had capacity") and spec:56-58 ("The ratio therefore moves the wrong way
under load"). `grep -rn cFinalBerth-5 memory/builds/cSteadyMetronome/` returns nothing, although §4
Files touched (spec:101) edits `memory/backlog/TOOL.md`. This is mechanical, not editorial: the
retired axis — per-process overhead against fixed sleeps — is precisely the axis measured threatening
the replacement in R2, so re-narrowing the diagnosis is what left §4's immunity claim unexamined.

**Spec edit.** In §4 "The defect, stated precisely", restate it on the recorded axis: "the assertion's
margin is per-process overhead measured against fixed sleeps — machine-dependent by construction,
which is why it flipped red→GREEN on a byte-identical tree at 550d9b6 (`memory/backlog/TOOL.md:85`,
commit 9d371c0). Load is one contributor, not the mechanism." Cite `TOOL-cFinalBerth-5` by id in §4
and in the README's "Start here". Correct §10's last sentence: the earlier row EXISTS, is OPEN, and is
closed by this unit — not "no earlier ruling this unit re-opens".

---

### R7 - MEDIUM - §7 names a meta-gate that structurally cannot see this file, and AC3/AC4 name no seam

*(raw 5 + raw 12, lenses L1 and L2.)*

**Claim.** §7 defers the arming question to `check-arms.py`, which excludes this file by
construction, so the two new `fail`-shaped branches S3 and S6 introduce are graded by no gate the
spec names and by no harness that exists. AC3 and AC4 likewise name conditions no seam can produce.

**Evidence.** `tools/memory-tree/check-arms.py:121-122` — `if rel.endswith(".test.sh"): continue`
("a fixture that quotes a fail line is not a gate") — drops the file from discovery before anything
else, and discovery additionally requires `HELPER_RE = ^\s*fail\(\)\s*\{` (check-arms.py:54, :127).
`tools/run-gates.test.sh` ends `.test.sh` AND uses a bare `fail=0` variable (`test:9`, `test:119`,
`test:125`) — it has no `fail() {` helper at all. The clause at spec:156 is therefore unsatisfiable,
not conditional, and it invites the builder to hunt for pin rows in
`memory/project/unarmed-branches.txt` this file can never own. There is also no sibling harness:
`tools/run-gates.evidence.test.sh` drives `run-gates.sh` through the `GATE_LEGS` seam and never
exercises the canary's arms. And the only width knob is `run_scratch`'s own `$1` (`test:89`), so AC3
as phrased is AC2's measurement read with the inverted predicate.

**Spec edit.** Replace §7's conditional clause with the fact: "`check-arms.py` does not grade this
file — `tools/memory-tree/check-arms.py:121` excludes `*.test.sh` and :127 requires a `fail()`
helper this file does not define. The two new refusal branches are armed inside arm 3c itself." Then
give AC3 and AC4 their mechanisms: AC3 = "the width-1 records, read with the width-4 predicate,
produce the red and its message" (the data AC2 already collects); AC4 = "a record file truncated to
empty by the arm's own fixture step produces the clock refusal."

---

### R8 - MEDIUM - Two scope items carry no acceptance criterion

*(raw 6, lens L1.)*

**Claim.** `memory/TEMPLATE-SPEC.md:108` requires every scope item to be verifiable at DoD. S5 is
named by no AC at all, and S1 — the item R1 shows is the whole mechanism — is observed only
indirectly, by criteria a broken implementation satisfies.

**Evidence.** The AC set (spec:139-152) maps AC1/AC2 to S2 and S3, AC3 to serial degradation, AC4 to
S6, AC5 to S4, and AC6/AC7 to the bar. S5 (spec:24-26, the comment stating the arm claims dispatch
concurrency and not execution speed) appears nowhere. AC1 and AC2 are satisfied by ANY two usable
intervals, so the three-legs-one-record implementation of R1 passes both while destroying the property
S1 exists to buy — the `fixture-passes-by-finding-nothing` class the spec itself invokes at
spec:78-79 for staleness but never for collision.

**Spec edit.** Add **AC8** — "When the scratch bar runs at width 4, FOUR distinct start records and
four distinct end records exist, one per leg name in the scratch manifest; a missing or duplicated one
reds naming the leg." Add **AC9** — "A grep of `tools/run-gates.test.sh` finds the arm-3c comment
stating that it asserts dispatch concurrency and makes no claim about execution speed."

---

### R9 - LOW - The fixture-writer site list undercounts, and "last line of the fixture" is unimplementable

*(raw 7 + raw 17, lenses L1 and L3.)*

**Claim.** Two small statements about the fixtures are wrong against source, and one of them is a
trap: followed literally it produces an absent `.end` file and an S6 refusal.

**Evidence.** spec:74 specifies the end record on "last line of the fixture", but every fixture's last
line is `exit 0` (`test:75`, `test:76`), so a write placed literally last never executes. spec:91
assigns the change to "the four `printf` fixture writers", but `test:132` —
`printf '#!/usr/bin/env bash\nsleep 1.5\nexit 0\n' > "$SCRATCH/fx/mid.sh"` — is a FIFTH writer of a
fixture body, restoring `mid.sh` after arm 3d overwrites it at `test:122`. Instrumenting only
`test:75-78` leaves two divergent spellings of the same fixture, one recording nothing — the
`two-answers-to-one-question` class the spec invokes at S4 (spec:22-23). Latent today only because
nothing reads timestamps after arm 3c; note the same undercount reaches further, since arm 3f
(`test:150`) and arm 3g (`test:169`) copy `instant.sh` into other fixture roles.

**Spec edit.** Change spec:74's "Written" cell to "immediately before the fixture's `exit`". Change
Inventory row spec:91's site to "every `printf` that materializes a fixture body — `test:75-78` AND
the arm-3d restore at `test:132`" (or single-source the body into a variable so there is one spelling
to instrument).

---

### R10 - LOW - Files touched names a map dossier that does not exist

*(raw 18, lens L3.)*

**Claim.** spec:102 estimates an edit to "`memory/map/features/` (the dossier claiming this leg, if
its prose names the ratio)". No such dossier exists; the key is unclaimed.

**Evidence.** `memory/map/baseline.toml:33` lists `"run-gates canary"` in the shrink-only unclaimed
set, and `memory/map/generated/MAP.md:52` shows `| `run-gates canary` | baseline |`.
`grep -rln run-gates memory/map/features/` returns only `memory-tree-merge-driver.md`, whose mentions
are unrelated. The parenthetical's condition is on whether the prose names the ratio, not on whether
the dossier exists, so it does not cover this. §7's conclusion that the map inventories do not move is
correct.

**Spec edit.** Replace the `memory/map/features/` entry in §4 Files touched with: "no map dossier —
`run-gates canary` sits unclaimed in `memory/map/baseline.toml:33`, so no dossier prose names the
ratio and none needs editing."

---

### R11 - LOW - "strictly cheaper" is backwards

*(raw 19, lens L2.)*

**Claim.** §5's perf line claims a net reduction the change does not deliver: it adds process spawns
to a leg the timing cache already records at 65s.

**Evidence.** The removed fences are 4 `date` invocations in the whole file (`test:93-94`, two per
line). The replacement adds 2 per fixture process per run — 8 per scratch run on the spec's own
arithmetic (spec:124-125), across the runs at `test:93`, `:94`, `:123` and `:137`, so roughly 32
spawns replace 4. That is conservative: if `instant.sh` is instrumented as Inventory row spec:91
implies, arm 3f (`test:151-156`, 5 runs × 4 legs) and arm 3g (`test:181`, 4 reps × 30 legs) push the
count past 300. `run:174-176` records ~25ms of pure spawn overhead per process on this platform.

**Spec edit.** Replace spec:124-125 with: "perf / scale — a sub-second cost on a leg already recorded
at 65s: the arm trades 4 wall-clock `date` fences for ~8 per scratch run (~30 extra process spawns at
~25ms each, more if the instant fixtures are instrumented), and no run is repeated."

---

## Refuted

- **raw 3 (MEDIUM, "nothing owns preserving the width-1 timestamps")** — the escape it declares closed
  is not closed. spec:83's "After each scratch run, read the four pairs" already permits an
  interleaved read between `test:93` and `test:94`, and §3's "arm 3a unaffected and untouched" cannot
  be byte-literal because the Inventory (spec:96) removes the `date` fences that sit on those very
  lines. The real defect — that no Inventory row NAMES the capture — is carried by R5.
- **raw 4 (MEDIUM, dispatch-skew immunity)** — duplicate of raw 9/14a; same spec passage (spec:60-65),
  same runner lines, same README figure. Folded into R2.
- **raw 8 (BLOCKER, timestamp collision)** — duplicate of raw 1/13, and its distinctive failure mode is
  wrong: the survivor is `[max start, max end]`, and since the max-end leg's own start is one of the
  candidates, `max start >= that leg's start`, so the record is always a SUBSET of a real interval. It
  cannot be "wider than any real leg's interval" and produces no silent false PASS. Its correct unique
  point (arm 3d's `cp` at `test:122` blocks the split-the-script fix) is folded into R1.
- **raw 11 (MEDIUM, when the width-1 intervals are read)** — duplicate of raw 15 at lower severity;
  same root, same lines. Its unique branch (a third scratch run would contradict §5's "no run is
  repeated") is an argument inside the same defect. Folded into R5.

## Unverified

None — every raw finding reached a verdict, and the two load-bearing empirical claims (R1's file
collision, R2's dispatch skew) were reproduced against the real unmodified runner rather than reasoned
about.
