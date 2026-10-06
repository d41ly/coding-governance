# TOOL-aGraftedHelix-41 — the driver suite runs in the pooled sweep as eight shards cut by its own region costs

**Status:** SPECCED · rev-1 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 25 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-prompt-TOOL-aGraftedHelix-40-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-40-1-spec-brief.md) | journal | TOOL-aGraftedHelix-40 |

<!-- /gen:spec-records -->

## 1. Goal

The pooled sweep at `b04ab0da0` ran the driver suite as one row for 19871 s and the run wall killed
it with no verdict, while every gate shard had finished by +10210 s. For 2 h 40 m the pool ran one
suite with seven lanes idle. This unit declares the driver suite as eight `--shard` rows the way the
gate suite is declared, cut at the suite's existing seams by a measured cost census, so that no
driver shard is predicted to run longer than the longest gate shard and one row no longer sets the
sweep's floor alone.

## 2. Scope (IN)

- **S1** — `SHARD_ARITY` in `tools/unattended/unattended.test.sh` moves from 2 to 8, and the fifteen
  top-level blocks of today's region two are relabelled, in text order and contiguously, into regions
  2 to 8 by the §4 cut rule. Region one does not move. No block is split, no arm is reordered or
  reindented, and every new region boundary reuses an existing seam line, which is respelled
  `fi   # ---- end REGION <k>`; a seam inside a region is respelled `fi   # ---- region <k> continues`.
  The suite's header and region comments read the count from `SHARD_ARITY` rather than typing it.
  Observed by AC1 and AC2.
- **S2** — every region from 2 to 8 opens with an entry line guarded by `[ "$SH_I" = <k> ]`, which
  runs `bcsetup; bcrestore` exactly as region two's entry does today, then re-executes whatever the
  region reads that only another region assigns or builds. Every helper a region calls whose
  definition sits in another region moves, byte-identical, into the prologue beside `bcrestore`. The
  unsharded run therefore executes the same commands in the same order as at the parent. Observed by
  AC2, AC3 and AC4.
- **S3** — the first block of each region from 2 to 8 carries the two-line `FOREIGN_PREFIX_PROBE`
  site after its first arm, copied from region one's. Observed by AC4.
- **S4** — the floor is selected by `FLOOR_SHARD_$SH_I` indirection, as the gate suite selects it,
  with `FLOOR_SHARD_2` to `FLOOR_SHARD_8` declared by the §4 split rule. `FLOOR_SHARD_1` and
  `FLOOR_ASSERTIONS` keep their values, `PROLOGUE_ARMS` is re-read, and its comment states the
  identity for `SHARD_ARITY` regions. The shard trailer names the other `SHARD_ARITY - 1` regions as
  not exercised. Observed by AC5.
- **S5** — the block-length arm in region one reads every `if in_shard <k>; then` label rather than
  `[12]`, and closes a block only at a seam line, never at the inner
  `fi   # ---- end the run_bounded host gate`. Observed by AC6.
- **S6** — in `tools/run-gates/selftest-budgets.txt` the `unattended driver selftest` row is replaced
  by eight rows `unattended driver selftest shard <k>/8`, argv
  `bash {prefix}/unattended/unattended.test.sh --shard <k>/8`, each budget DERIVED by the §4 rule
  and its reading field saying so. The row's line in `tools/run-gates/selftest-pooled-evidence.txt`
  is deleted with it, or the declaration gate reads it as an orphan. Observed by AC7.
  - **Readers:** by name: `tools/run-gates/selftest-budgets.txt` and
    `tools/run-gates/selftest-pooled-evidence.txt` spell the row name, one line each, and this item
    rewrites both. by value: `tools/run-gates/run-selftests.sh` reads the rows as its population, its
    shard join, its evidence orphan check and its pooled dispatch order;
    `tools/unattended/run-unattended-gates.sh` counts this kit's rows; `.github/workflows/remote-ci.yml`
    expands one held-matrix entry per row and requires each row's argv to select only that row;
    `tools/run-gates/foreign-prefix.gov.test.sh` runs every row in probe mode.
- **S7** — the prose that states the old shape is corrected: the `--help` sentence in
  `tools/unattended/run-unattended-gates.sh` that declares the driver suite one whole row, its parity
  comment that counts "the eight shard rows", and the clause of the shard-join comment in
  `tools/run-gates/run-selftests.sh` that justifies the unported reverse half by the driver suite
  being called whole. None of the replacements types a row or shard count. Observed by AC8.
- **S8** — the unattended kit and the run-gates kit each move one minor step in every carrier
  `tools/check-kit-versions.sh` pairs, once, after the pass's last move; the rendered unattended
  guides and Skill are re-adopted; and `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit`,
  because `tools/run-gates/run-selftests.sh` is in its `watch:` list. Observed by AC9.

## 3. Non-goals (OUT)

- **Choosing an arity other than eight.** The owner ruled eight for both unattended suites (§8 F1);
  the census in §4 measures that eight meets the target and is where the target stops improving.
- **Splitting a block.** The largest block, the one that opens with the declared spec-token
  checker's dispatch arms, holds a fifth of the driver's calls and is the floor no cut at existing
  seams goes below. A new seam inside a block is a state analysis this unit does not do.
- **Changing the pooled runner.** Its dispatch is declaration order, which puts the eight driver rows
  ahead of the gate shards. Longest-first dispatch would be a run-gates mechanism of its own.
- **Porting the canary's reverse shard-join half** into `tools/run-gates/run-selftests.sh`. S7
  corrects the comment's reason; the rule and its pinning arm in `tools/run-gates/run-selftests.test.sh`
  stand.
- **A standing prologue arm for cross-region helper calls**, the analogue of the gate suite's
  `check_helpers_hoisted`. A cross-region call fails its shard loudly at the next sweep, and the arm
  would be a mechanism and an inventory key of its own.
- **Running any shard whole.** Every per-shard reading, the comparison against the gate shards and
  the identity are the close's, below. No suite, whole shard or bar runs in the pass; §6 runs only
  one-arm probes and a prologue-only staged break.
- **Re-declaring any row but the driver's**, and filing anything.

### Edges

- **consumes-from** external — the recorded sweep readings this unit sizes against: the longest gate shard at 7391 s and the driver row walled at 19871 s in the b04ab0da0 sweep, and the driver row's completed 17142 s in the 90a6f6fae sweep, both in this build's prompt records; and the owner's arity ruling of 2026-08-29 in TOOL-aGradedDoorway-7.
- **hands-off** external — the close: the pooled calibrate over the unattended kit, which writes the eight rows' first readings into the evidence file; each driver shard running to its own end with no FAIL line and an executed count at or above its floor; the longest driver shard reading compared with the longest gate shard reading in that same calibrate; and the identity, that the eight executed counts less seven times PROLOGUE_ARMS equal the unsharded count.

## 4. Design

### Evidence

Every figure in this subsection is PINNED, measured on node `a` on 2026-10-06 at `1b4f7720e`, the
branch HEAD this spec was written against. The pass re-derives every one over its own parent before
any code, and a moved figure is a rev bump of this spec committed before the code commit.

- The sweep at `b04ab0da0`, from this unit's brief: the driver row started at +0 and was killed by
  the run wall at 19871 s; the gate shards ran 4724 to 7391 s each and finished by +10210 s; every
  other row ran under 1200 s. Effective parallelism was about 3.7 of 8 lanes.
- The sweep at `90a6f6fae`, from unit 34's brief: the driver row completed in 17142 s pooled.
- The calibrate at `eb96ea8b2`, from its frozen clone's driver output: unsharded, complete, `3978`
  assertions executed.
- The driver suite has 16 top-level blocks. Region one is one block, lines 630 to 1889; region two
  is fifteen, lines 1898 to 15754, cut at "region two continues" seams for the Cygwin stack ceiling.
  Region two's only entry is `if [ "$SH_I" = 2 ]; then bcsetup; bcrestore; fi`, and neither helper
  executes an assertion.

### The census, and the target

The cost unit is the driver call site, the analogue of unit 34's leg invocation. A driver call site
is a block line, comments dropped and single-quoted spans blanked, that holds `bash "$SCRIPT"` or
calls at command position `run` or any helper whose body holds a driver call site, closed
transitively. A block runs from an `if in_shard <k>; then` line at column 0 to the seam line that
closes it. A block's share is its call sites over the file's. At `1b4f7720e` the closure holds 37
driver-reaching helpers and the file holds 1835 call sites:

| Block | Lines at `1b4f7720e` | Share | Static assertion sites |
|---|---|---|---|
| 1 | 630–1889 | 6.8 % | 226 |
| 2 | 1898–3537 | 9.9 % | 304 |
| 3 | 3539–5230 | 13.0 % | 344 |
| 4 | 5232–7321 | 20.1 % | 566 |
| 5 | 7323–8852 | 11.4 % | 371 |
| 6 | 8854–8998 | 1.3 % | 44 |
| 7 | 9000–9527 | 2.8 % | 124 |
| 8 | 9529–11246 | 12.5 % | 404 |
| 9 | 11248–11382 | 0.8 % | 34 |
| 10 | 11384–13282 | 8.9 % | 354 |
| 11 | 13284–13617 | 3.0 % | 110 |
| 12 | 13619–13744 | 0.2 % | 33 |
| 13 | 13746–14268 | 2.1 % | 166 |
| 14 | 14270–14423 | 0.3 % | 29 |
| 15 | 14425–14725 | 1.0 % | 73 |
| 16 | 14727–15754 | 6.0 % | 225 |

A static assertion site is a command-position `hit`, `miss`, `same` or `mutate` call, or a bare
`n=$((n+1))`, on the same lines. The first census pass counted only direct calls and undercounted
every block that reaches the driver through a fixture helper; block 7 read 0 direct calls and holds
51 through helpers, which is why the closure is part of the predicate.

**The target.** A driver shard's pooled cost is estimated as its share of the whole driver's pooled
cost D, and must be at most the longest gate shard's G, so the target share is G / D. G is 7391 s.
D is at least 19871 s and unknown above it, because the row was walled, and for its last 2 h 40 m
it ran with lanes idle and faster than a shard would under a full pool. The target therefore takes
D as 1.5 times the walled reading, this repo's measured-plus-headroom habit: 7391 / 29807, a share
of 24.8 %. figure: G and D PINNED from the sweep at `b04ab0da0`; the share DERIVED from them.

**What the census says about the arity.** With region one fixed, the smallest arity whose best
contiguous cut puts every region at or under 24.8 % is six, at 22.9 %; five reaches only 28.0 %. At
eight the best achievable largest region is block 4 alone, 20.1 %, and no higher arity lowers it
without splitting a block. Eight is the owner's ruling (§8 F1), and the census measures it at the
knee. Its predicted longest shard is 21.5 % of D: 4272 s at the walled reading and 6408 s at the
target's D, both under G.

### The cut rule, and the cut it gives at 1b4f7720e

Among the contiguous partitions of region two's fifteen blocks into seven regions whose shares are
each at most the target, take the one with the fewest crossings, then the smallest largest region.
A crossing is a helper or a variable whose resolution leaves its region. A call resolves to the
nearest column-0 definition above it in text order, and an `unset -f` of the name ends that
definition's reach. A read of `$v` resolves to the nearest assignment above it, where `v=`, the
`local`, `export` and `declare` forms, `for v in` and `read` all assign. Of 222 partitions within
the target at `1b4f7720e`, the rule takes this one:

| Region | Blocks | Lines at `1b4f7720e` | Share | Static assertion sites |
|---|---|---|---|---|
| 1 | 1 | 630–1889 | 6.8 % | 226 |
| 2 | 2 | 1898–3537 | 9.9 % | 304 |
| 3 | 3 | 3539–5230 | 13.0 % | 344 |
| 4 | 4 | 5232–7321 | 20.1 % | 566 |
| 5 | 5 | 7323–8852 | 11.4 % | 371 |
| 6 | 6–7 | 8854–9527 | 4.1 % | 168 |
| 7 | 8–9 | 9529–11382 | 13.3 % | 438 |
| 8 | 10–16 | 11384–15754 | 21.5 % | 990 |

Keeping blocks 10 to 16 together is the rule at work: the minimum-largest cut splits them and
carries the process-ledger fixture across a region boundary, at 45 crossings against this cut's 32.
The predicate's hits for this cut at `1b4f7720e`, with its near-misses, which the pass re-reads rather
than trusts:

| Kind | Hits | Near-misses, and why |
|---|---|---|
| helpers to hoist | `askmode` `askrows` `build_dd_landing` `build_hold_fixture` `dispbacklog` `dispreset` `dispspec` `drop_lease_facts` `read_hole_probe` `read_lease_hash` `restore_dd_origin` `scope` `set_lease_fact` `slice_fn` `write_aged_commit` `write_published_conf` | `mktemp`, a shadow defined and unset on the next two lines |
| variables to rebuild | `ASKSTUB` `DD_C` `DD_CD` `DD_LOG` `DD_PID` `DSTUB` `LEASE` `OWN_PID` `STOP7` | `PATH`, the environment; `body` `s` `t` `want` `x`, loop, `read` or quoted forms the first scan did not model |

### Region entry and the hoist

A **helper** that crosses moves into the prologue beside `bcrestore`, byte-identical. A function
definition executes nothing, so the unsharded run is unchanged by the move. A name defined twice,
as `read_run_fact` is in blocks 6 and 13, hoists at most its first definition and leaves the second
in place, so every call resolves to the body it resolves to today in every mode.

A **variable** that crosses is never hoisted, because an assignment hoisted into the prologue runs
earlier in the unsharded run than it does today. It is rebuilt by the reading region's entry line,
inside the `SH_I` guard, so only a shard run executes it: the assignment re-executed verbatim when
its right-hand side reads only the prologue's fixture and the entry's own state, or the hoisted
fixture builder called when the read needs state that builder makes. An entry never executes an
assertion, and it never calls a helper whose body holds an assertion site; that keeps the identity
below exact. When a read cannot be rebuilt on those terms, the seam is wrong and the cut takes the
rule's next partition.

```bash
if in_shard 3; then
if [ "$SH_I" = 3 ]; then bcsetup; bcrestore; fi   # plus this region's rebuilds, if the scan names any
```

### Floors, PROLOGUE_ARMS and the identity

`PROLOGUE_ARMS` is re-read as the executed count of a shard whose region holds no block, which AC5
stages. Each new floor is that count plus a share of the parent's region-two floor:

```text
FLOOR_SHARD_k = PROLOGUE_ARMS + floor(0.9 × R × a_k / A)     k = 2 .. 8
R   = the parent's FLOOR_SHARD_2 less the parent's PROLOGUE_ARMS
a_k = region k's static assertion sites;  A = the sum over regions 2 to 8
```

The 0.9 is this derivation's own discount. Static sites stand in for executed counts, and a region
whose arms execute less than its sites suggest would otherwise red a healthy shard at the close.
At `1b4f7720e`, with `PROLOGUE_ARMS` at 18, the rule gives 218, 244, 391, 262, 128, 306 and 671 for
regions 2 to 8. figure: DERIVED at the pass over its parent; the next measured executed count of a
shard re-declares its floor at the suite's usual headroom.

Since neither the entry's helpers nor the probe sites execute an assertion in a run that is not a
probe, the eight shards' executed counts less seven `PROLOGUE_ARMS` equal the unsharded count. The
comment beside `PROLOGUE_ARMS` states that identity for `SHARD_ARITY` regions, and the close
observes it.

### The declaration

Each row's budget is `ceil(1.5 × (p_k + s_k × 17142))`, where `s_k` is region k's census share and
`p_k` is the seconds AC4 measures for that shard's probe run, which is the prologue, the entry and
one arm. 17142 s is the latest COMPLETED whole reading of the driver suite, pooled, so these
budgets are loose ceilings as a serial cost verdict. Each row's reading field says that in the
file's grammar: derived, the date, node `a`, the share, the whole reading and its sha, the probe
seconds, x1.5. Before the probe seconds, the shares give 1749, 2546, 3343, 5169, 2932, 1055, 3420 and
5529 s for regions 1 to 8. `run-selftests.sh --rank` already lists derived and pooled readings as
unbacked, so these rows join an existing population there rather than starting one.

The old evidence row is deleted, and the eight new rows carry none until the close calibrates. That
is the evidence file's own announced-unarmed state: `--pooled` refuses an uncalibrated row by name
and runs nothing.

### Who runs the suite whole

At the parent the one declared row ran the suite whole under `--serial`, `--pooled` and
`--pooled --calibrate`, and in the remote CI held matrix. The foreign-prefix leg ran it in probe
mode. No merge-bar leg runs it, and none has since the 2026-08-23 ruling; the bar's declaration gate
reads the row and runs nothing. After this unit every one of those routes runs the eight shard rows,
and nothing runs the suite whole.

Two things read a whole run. `FLOOR_ASSERTIONS` is graded only unsharded and stays, binding a
developer's hand-run whole suite. The identity's unsharded term is the other, and the close takes it
from one unsharded run or from the recorded `3978` plus the floor raises of the units after
`eb96ea8b2`. Nothing automated depends on a whole run, so no route is kept whole. A cross-region
state dependency, the hazard the region-two comment names as ungated, now reds in its own shard,
which is the safer direction.

### Inventory

No function, file, leg, conf key or naming cell is minted. Eight budget rows and seven floor
constants are declared, and helpers move within one file under their own names.

### Rollout

The pass first re-derives the census, the cut and the crossing scan over its parent, and commits a
rev bump of this spec if any figure moved. Then one build commit: the suite, the declaration and
the evidence, the prose of S7, both kits' versions, the re-adopted renders, the manifest re-stamp
and the status flip. The acceptance ledger follows in a records commit.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`, the arity, the cut, entries, hoist, probe sites, floors and the block-length arm
- `tools/unattended/run-unattended-gates.sh`, the help sentence and the parity comment
- `tools/unattended/unattended.sh`, the version line
- `tools/unattended/`, every other unattended version carrier
- `tools/run-gates/selftest-budgets.txt`, the eight rows
- `tools/run-gates/selftest-pooled-evidence.txt`, the driver row
- `tools/run-gates/run-selftests.sh`, the shard-join comment
- `tools/run-gates/run-gates.sh` and `tools/run-gates/README.md`, the run-gates version carriers
- `memory/guides/`, the re-adopted unattended guides and the kickoff manifest's `last-audit`
- `.claude/skills/unattended/SKILL.md`, re-adopted

### Alternatives rejected

Each with the test that rejected it, per BUILD-METHOD M12.

- **Six regions, the census's smallest arity.** The owner ruled eight for both suites, and the
  census shows six meets the target only at 22.9 % against eight's 21.5 %.
- **The minimum-largest cut at eight**, 20.1 % largest. It cuts the process-ledger fixture across
  regions 7 and 8 and costs 45 crossings against 32; both cuts are under the target.
- **Hoisting crossing assignments into the prologue.** It moves when the unsharded run executes
  them, and `STOP7`'s line also runs `mkdir -p` under the fixture's git dir, a side effect that
  would then precede every arm between the prologue and its block.
- **A sizing proxy of direct driver calls only.** It read block 7 at zero calls and block 16 at
  16, where the closure through fixture helpers counts 51 and 110.
- **Measuring each region by running it.** That is a suite run inside a pass, refused by §8 F2.

## 5. Production-readiness checklist

- security — N/A: a test suite's region labels, a declaration, an evidence row and comments.
- perf / scale — the sweep's driver floor moves from at least 19871 s to a predicted longest shard of
  21.5 % of the driver's cost. Seven more prologue runs join every sweep, and the foreign-prefix leg
  gains seven probe rows at each of its three prefixes.
- error / empty / loading states — an index outside 1 to 8 is refused before the scratch dir exists;
  an empty region reds its floor and still prints its trailer; a missing `FLOOR_SHARD_k` dies under
  `set -u` with no trailer, which the pool reads as untrailed.
- observability — every shard prints its floor-graded count and names the seven regions it did not
  exercise; the close's calibrate writes a reading per shard.
- risks — a block may read shell or git state a predecessor in another region leaves behind, which
  only the close's shard runs can show. The crossing scan covers helpers and variables, and each
  entry rebuilds the region-two epoch; other state an earlier region leaves under the git dir is
  absent in a shard run, so the arm that needed it reds rather than passes. The derived floors may
  sit above a region's true count, which the 0.9 discount guards against.
- testing — §6, and the close's calibrate in §3.
- migration — none. Reverting is relabelling the regions and restoring one row.
- user docs — N/A: suites, declarations and one help sentence.

## 6. Acceptance criteria

Every criterion runs in the pass's worktree unless it names a clone. A clone is a `git clone --local`
under a short `%TEMP%` root, and a copy of the suite is written into the clone's kit directory under
a name that is not a suite's, so the copy resolves the clone's driver exactly as the suite does.

- **AC1** — When `grep -oE '^if in_shard [0-9]+' tools/unattended/unattended.test.sh | uniq -c` runs,
  it prints eight lines, labels 1 to 8 in ascending order, and `grep -n '^SHARD_ARITY=8$'` over the
  same file prints one line; and when the §4 census predicate runs over that file, every region's
  share is at most 24.8 %.
  Red when: a scratch copy labels block 16 as region 9, which prints a ninth line, or labels block 3
  as region 2, which leaves region 3 out of the sequence.
  figure: the shares are DERIVED at observation; 24.8 % is DERIVED from the readings PINNED in §4.
- **AC2** — When the sorted lines of the file are compared with its parent's,
  `sort tools/unattended/unattended.test.sh | diff <(git show <parent>:tools/unattended/unattended.test.sh | sort) -`,
  every differing line is an `in_shard` label, a seam line, a region entry, a probe site, the
  block-length arm, a floor or its selection, the trailer, `SHARD_ARITY`, or a comment; and
  `bash -n tools/unattended/unattended.test.sh` exits 0.
  Red when: a hoisted helper is edited in transit in a scratch copy, which the diff prints as a body
  line, or an `if in_shard` line loses its `fi`, which the syntax check reports.
- **AC3** — When the §4 crossing predicate runs over the file, no helper call resolves to a
  definition outside the prologue and its own region, every variable read that resolves into another
  region is assigned in its own region's `SH_I`-guarded entry, and no entry calls a helper whose body
  holds an assertion site; the near-misses print beside the result.
  Red when: a scratch copy moves `build_hold_fixture` back into block 5, which the predicate names as
  called from regions 6 and 7.
  figure: the hits at `1b4f7720e` are PINNED in §4; the result is DERIVED at observation.
- **AC4** — When a copy of the suite runs in a clone with `FOREIGN_PREFIX_PROBE=1` at each of
  `--shard 1/8` to `--shard 8/8`, eight at once, each prints `foreign-prefix-probe: stopped after 1 arm`
  and a `PASS (` line and exits 0, and each run's seconds are recorded as that shard's `p_k`.
  Red when: the copy's region-6 probe site is deleted, so `--shard 6/8` prints no marker, whether
  the region finishes or a 120 s `timeout` stops it first.
  cost: about the prologue's time, a few minutes for all eight on node `a`.
- **AC5** — When a copy in a clone relabels every `if in_shard 8; then` line as 7 and runs
  `--shard 8/8`, it exits 1 printing `FAIL executed` with `in shard 8/8 against a floor of` and the
  value `FLOOR_SHARD_8` holds, then its `assertions executed` trailer, whose count is the prologue's;
  `PROLOGUE_ARMS` in the file equals that count; and the unstaged copy refuses `--shard 9/8` naming
  `index out of range 1..8` and `--shard 1/2` naming `arity must be 8`, each exiting 2.
  Red when: the copy keeps the parent's two-arm `case`, which grades shard 8 as `unsharded` against
  `FLOOR_ASSERTIONS`.
  cost: the prologue alone, about a minute.
  figure: the prologue count is DERIVED at observation.
- **AC6** — When the block-length arm's `awk` runs standalone over the file, it measures every block
  from its `in_shard` line to the seam line closing it and prints a longest block of at most 2500
  lines; and the parent's pattern `^if in_shard [12]; then` over the same file reaches no block of
  regions 3 to 8.
  Red when: a scratch copy pads region 7's last block past 2500 lines, which the arm's `same` reds;
  or the close pattern is the parent's bare `^fi   # ---- `, which ends block 5 at the run_bounded
  host gate and reports it hundreds of lines short.
- **AC7** — When the leg `every held leg is budgeted, every budget row resolves` runs, it passes with
  eight rows named `unattended driver selftest shard <k>/8` and no row named
  `unattended driver selftest` alone;
  `grep -c 'unattended driver selftest' tools/run-gates/selftest-pooled-evidence.txt`
  prints 0; each row's budget equals the §4 rule over AC1's shares and AC4's seconds; and the
  runner's `--list` with `--kit` set to each row's argv selects that row alone.
  Red when: a scratch clone deletes the shard-5 row, which the gate reds naming `no row for index 5`;
  or keeps the old evidence row, which the gate names an `ORPHAN`.
- **AC8** — When `grep -n 'one whole row' tools/unattended/run-unattended-gates.sh`,
  `grep -n 'the eight shard rows' tools/unattended/run-unattended-gates.sh` and
  `grep -n 'called whole here on purpose' tools/run-gates/run-selftests.sh` run, none prints a line,
  and the replacing sentences carry no digit.
  Red when: either file still states the driver suite is declared or called whole.
- **AC9** — When `python tools/govkit/govkit.py epoch --base <parent>` runs at the pass's commit, it
  names no unattended and no run-gates carrier; `bash tools/check-kit-versions.sh` exits 0;
  `bash tools/unattended/adopt-unattended.sh --check` reports the renders in sync; and
  `bash skills/session-kickoff/manifest-check.sh` exits 0.
  Red when: either kit's shipped bytes moved without its version, or the runner moved without the
  manifest's `last-audit` re-stamp.
  figure: both versions are DERIVED from the pass's parent at observation.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kit/dogfood doc parity` · `every held leg is budgeted, every budget row resolves` · `kickoff-manifest ratchet` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `install-prefix (shipped surface)` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates` · `run-selftests self-test`

New arm: tools/unattended/unattended.test.sh · the floor selected per shard for eight regions; staged by relabelling region 8's blocks as 7, so shard 8 executes the prologue alone · FLOOR_SHARD_2 to FLOOR_SHARD_8 by the split rule
New arm: tools/unattended/unattended.test.sh · the block-length arm over every region label, closed only at seam lines; staged by a scratch copy whose region-7 block passes 2500 lines · none

The close runs the legs, the pooled calibrate that takes the eight rows' first readings, and the
identity. A pass runs the probes, copies and predicates of §6 as its check.

## 8. Open questions

- **F1 — What arity does the driver suite take?**
  Option A takes the census's smallest arity that meets the target, six, at a largest region of
  22.9 %. Option B takes eight, the owner's ruling of 2026-08-29 for both unattended suites, whose
  gate half TOOL-aBatchedArm-3 carried and whose driver half it left standing. Option C keeps two,
  which leaves region two at 93.2 % of the driver's calls and fails the target outright.
  The census measures eight at the knee: from eight on, the largest region cannot fall below one
  block's 20.1 % without splitting a block.
  RESOLVED (owner, 2026-08-29): B, eight — TOOL-aGradedDoorway-7 §8, "pick 8 and fix what breaks",
  for both suites. This spec carries that ruling's driver half and measures that eight meets the
  target.
- **F2 — Where do the per-shard readings come from, when a pass may run no suite?**
  Option A has the pass run each shard on a frozen clone and declare every budget and floor from what
  it measures. Option B has the pass derive budgets and floors from the census and the recorded whole
  readings, measure only the prologue through one-arm and empty-region runs, and leave each shard's
  first reading to the close's calibrate. Option C splits the old row's 3860 s budget by share.
  A is refused by shared invariant 11 of this build's brief and by BUILD-METHOD M6; it is the
  hours-long pass this harness exists to prevent. C declares from a 2569 s reading taken when the
  suite held well under half of today's assertions, and that row was already measured overrun.
  RESOLVED (agent, 2026-10-06, delegated): B. Each budget's reading field says DERIVED and names its
  base, the probe seconds are fresh node-`a` measurements, and the close's calibrate is the first
  reading of each shard.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, adopted at VERIFYING after the pooled sweep at `b04ab0da0`
  walled the unsharded driver row. The census, the cut and the crossing scan were run read-only over
  the suite at `1b4f7720e`; no suite or shard was run.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "split one long self-test suite into shard regions sized
by measured cost"` ranked name-stem neighbours, `build_self_chain` and the measure family among them,
none a seam, and printed `unscanned layers: .sh`, so it cannot see either unattended suite and a
"no seam fits" resting on it alone would be unfounded. The seams were found by reading the suites,
and each change extends one: the gate suite's eight-region shape in
`tools/unattended/check-unattended.test.sh`, whose `FLOOR_SHARD_$SH_I` selection, other-regions
trailer and per-region probe sites S3 and S4 copy; the driver suite's own region-two entry, which S2
repeats per region, and its hoisted `bcsetup` to `bcrestore` group, which the S2 hoist joins; the
runner's shard join in `tools/run-gates/run-selftests.sh`, which already grades every index 1..n of
a sharded script; and unit 34's sizing of regions by a per-block invocation predicate, which §4's
census follows with the driver call site as its unit. Recall returned this unit's brief; the gate
suite's sharding spec, TOOL-aBatchedArm-3, whose hoist rule and serial-reading method this unit
follows as far as a pass may; TOOL-aShardedFloor-2's shard contract; TOOL-aGradedDoorway-7's owner
ruling of eight for both suites; and TOOL-aBatchedArm-3's round-3 audit finding that once no runner
runs a suite whole `FLOOR_ASSERTIONS` is never graded, which §4's whole-run subsection answers. It
also returned TOOL-aTracedSpawn-1, whose claim that the suite dies unsharded is stale against
`eb96ea8b2`'s complete unsharded run.

Recall terms used: shard arity region floor re-cut in_shard SHARD_ARITY pooled sweep budget selftest driver seam hoist

The question passed with them: "how was a long unattended self-test suite split into shard regions
and how were the cut, floors and budgets chosen".
