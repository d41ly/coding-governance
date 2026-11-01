# TOOL-dBoundRoles-69 — the round-1 audit of units 65 and 66, its 18 minors: ledger criteria read through the revision arm, one root source, printed operands, one cleanup rule, loops swept by a pinned class, and a hard kill recovered

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 39 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 |
| [2026-10-26-build-TOOL-dBoundRoles-69-deviation-691.md](../build/2026-10-26-build-TOOL-dBoundRoles-69-deviation-691.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-owner-review-stop.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-owner-review-stop.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted specs 65 and 66
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md`)
exited CONVERGED with no blocker. It confirmed 20 findings: two HIGH, 13 MEDIUM and five LOW. Ids 1 and
14, the HIGHs, are `TOOL-dBoundRoles-67`'s and `TOOL-dBoundRoles-68`'s. BUILD-METHOD M4 promotes every
minor, batched into one unit, because they do not split into two disjoint write sets by M6 (§4 "Why
one unit"). This unit takes all 18: MEDIUM ids 2, 13, 3, 7, 21, 8, 22, 12, 16, 15, 6, 23 and 19, and
LOW ids 5, 9, 11, 17 and 18. Each id is its own scope item, even where the report merged several ids
into one item.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 2 | spec 65 AC5, S6; spec 66 AC17 | S1 |
| M1 | 13 | spec 65 §4 Rollout; spec 66 §4 "Where each item lands", Rollout | S2 |
| M2 | 3 | spec 66 AC16 | S3 |
| M3 | 7 | spec 65 S2, AC1 | S4 |
| M3 | 21 | spec 63 S12; spec 65 AC4 | S5 |
| M4 | 8 | spec 63 S12; spec 66 S10 | S6 |
| M4 | 22 | spec 66 AC8 | S7 |
| M5 | 12 | spec 63 S12; spec 64 S18; spec 65 S5; spec 66 S10, S11 | S8 |
| M5 | 16 | spec 65 S2, S5, §5; spec 66 AC9 | S9 |
| M6 | 15 | spec 60 §4, AC6; spec 65 S3, AC2, Files touched | S10 |
| M7 | 6 | spec 66 S4, §4 Evidence, AC2 | S11 |
| M7 | 23 | spec 66 S4, AC2 | S12 |
| M8 | 19 | spec 63 S12, §5; spec 64 §5; spec 66 S10, AC8 | S13 |
| L1 | 5 | spec 66 S4, AC2; the spawn guard's floor | S14 |
| L2 | 9 | spec 63 S8, §5; spec 64 §5; spec 65 S3, AC2 | S15 |
| L3 | 11 | spec 65 §4 Evidence; spec 66 S8, §4 Evidence | S16 |
| L4 | 17 | spec 64 S12, §4 table; spec 66 S12, AC1, Files touched | S17 |
| L5 | 18 | the roles adopter suite; spec 66 S20, AC13 | S18 |

## 2. Scope (IN)

- **S1** — id 2. Spec 65's AC5 and spec 66's AC17 each hold when the revision naming their own unit is
  the revision `LEDGER` captures on the line, or one inside the parenthesised list after it, in spec
  66's S23 grammar `- AC<n> — amended rev-<latest> (rev-<a>, rev-<b>) — <observation>`. Spec 65's S6
  states its ledger answers in that grammar. Observed by AC1.
- **S2** — id 13. Spec 65's §4 Rollout and spec 66's §4 "Where each item lands" and Rollout hold no
  claim that either order lands both because each criterion reads only its own unit's clauses. Each
  says that units 65 and 66 both rewrite unit 64's AC13 ledger line, and that S1's reading keeps both
  criteria green in either order. Observed by AC2.
- **S3** — id 3. Spec 66's AC16 reads unit 60's AC15 line this way: `LEDGER` captures the highest
  revision on the line, and the revision naming `TOOL-dBoundRoles-64` is that revision or one inside the
  parenthesised list. Where spec 66's S9 bumped spec 60, the captured revision names unit 66; otherwise
  it names unit 64. Observed by AC3.
- **S4** — id 7. Spec 65's S2 derives `<TEMP>` from one source, the `TEMP` environment variable:
  `os.environ["TEMP"]` in Python and `cygpath -m "$TEMP"` in bash. It names `tempfile.gettempdir()` only
  to refuse it, because that reads `TMPDIR` first. Spec 65's AC1 gains the half that S2 names one
  source. Observed by AC4.
- **S5** — id 21. Spec 63's S12 probe prints the absolute root it used, on a `root: <path>` line,
  before its `git worktree add`. A check run in the same pass as the probe reads that printed root
  rather than deriving its own. Spec 65's AC4 gains a half: where the probe ran in the pass, the root the
  check compared equals the printed one by `derive_key` of `os.path.realpath`. Observed by AC4.
- **S6** — id 8. Spec 63's S12 probe prints its run's worktree path, on a `worktree: <path>` line,
  once `git worktree list --porcelain -z` names that path by `derive_key`, and before the import. The
  line is printed only after the entry is registered. Spec 66's S10 names that line as the run's own
  path. Observed by AC5.
- **S7** — id 22. Spec 66's AC8 reads the staged run's `worktree:` line. The line must be present,
  which proves an entry was registered before the failure. After the run, no porcelain entry's
  `derive_key` equals it. The checker records the root's entries before the staged run, and the entries
  after must be a subset of those, so an earlier leftover cannot mask the result. Observed by AC5.
- **S8** — id 12. One cleanup rule, with one owner. Spec 63's S12 states every entry a pass may hand to
  git's forced worktree removal, and it is the only text that does. Its run's own path. Under spec 65's
  S2 root, an entry the porcelain marks `prunable`, and a non-`locked` entry stale by S13. The
  signature entries `TOOL-dBoundRoles-67`'s S3 admits. Spec 64's S18, spec 65's S5 and spec 66's S10
  and S11 cite "S12's cleanup rule" and restate none of it. Spec 65's S5 records a live entry under the
  root in unit 64's ledger and leaves it in place. Observed by AC6.
- **S9** — id 16. Spec 65's S2, S5 and §5 security line hold no premise that the root holds nothing but
  the probe's worktrees. S2 says a concurrent session's live observation may sit under it. Spec 66's
  AC9 also extracts spec 65's S5 and §5 security line, and requires each to cite S12's cleanup rule.
  Observed by AC6.
- **S10** — id 15. Spec 65's S3 lists every text that states the observation's location, found by
  `git grep -n 'TEMP%' -- memory/builds/dBoundRoles/spec` and read clause by clause. Spec 60's §4 "Where
  each item lands" and its AC6 `fixture:` line describe the detached worktree of spec 63's S12 under
  `<TEMP>/dbr63obs`, not an archive under `%TEMP%`. Spec 65's AC2 extracts both. Spec 65's Files
  touched names spec 60 and its ledger. Observed by AC7.
- **S11** — id 6. Spec 66's S4, §4 Evidence second bullet and AC2 define the loop class in three parts.
  A loop line matches `^[[:space:]]*(for|while) [^#]*; do([[:space:]]|$)`, which no JavaScript or Python
  loop inside a heredoc or a quoted body matches. Its body runs from that line to its matching `done`,
  counting nested loop openers. It counts when S14's helper predicate matches the body, or when the
  body holds both an `echo "ok ` line and `pass=$((pass+1))`. A loop over a glob or a variable counts by
  spec 64's §4 table, the fewest items the list can hold. Observed by AC8.
- **S12** — id 23. Spec 66's S4 and AC2 name the controls at `462d20f3`. Should-match: lines 797, 883,
  933, 1810, 1816, 1898, 1959, 1967, 1970 and 2480 of the agent-cap suite. Should-not-match: 451, a
  JavaScript loop in a heredoc; 1403, which echoes `FAIL` and never raises `pass`, so it adds 0 to E;
  1879, JavaScript in a single-quoted string; 2415, Python in a `-c` string; and 1331, whose body spells
  `msg` only inside `$TMP/msg.err`. Observed by AC8.
- **S13** — id 19. A hard kill leaves its directory, so git never marks its entry `prunable`. Spec 63's
  S12 recovery, the probe's first step, also hands to forced removal a non-`locked` entry under the root
  whose `<epoch>` name is more than 3600 seconds older than the run's own epoch. Spec 63's and spec 64's
  §5 security lines price it as a stale entry under the probe's own root. Spec 66's S10 names AC8's
  hard-kill half as what observes it. Observed by AC9.
- **S14** — id 5. Spec 66's S4 and AC2 pin the helper predicate, matched line by line over the loop
  text: `(^|;|&&|\|\||\bdo|\bthen|\belse)[[:space:]]*(check|js|jso|msg|check_spec_audit|check_cap|check_spawn|run_spawn)[[:space:]]`.
  With S11's class it selects exactly S12's ten should-match lines at `462d20f3` (measured 2026-10-26,
  PINNED). Where unit 66's pass counted a loop outside the class, this pass corrects E and
  `FLOOR_ASSERTIONS` in `tools/roles/spawn-guard.test.sh`, and records the check in its ledger.
  Observed by AC8 and AC10.
- **S15** — id 9. Spec 63's S8, spec 63's §5 security line and spec 64's §5 security line name
  `dbr63obs` wherever they state the observation's location, and hold no bare short `%TEMP%` location.
  Spec 65's S3 lists them and its AC2 extracts each. Observed by AC7.
- **S16** — id 11. The citations read at HEAD. Spec 65's §4 Evidence cites the dWitnessedBar-58 review
  at `:89` and `:253`, spec 64's S18 at 116-121 and AC13 at 417-421, and spec 63's §5 security line at
  213. It says that `os.path.realpath("C:/PROGRA~1")` prints `C:\Program Files` and that `derive_key`
  folds the case. Spec 66's §4 Evidence cites spec 62's §7 spawn-guard line at 171. Spec 66's S8 lists
  spec 52 line 81 as a `handoff.py:1027` hit, not a bare-token hit. Observed by AC11.
- **S17** — id 17. Spec 64's S12 and its §4 "The executed-count rule" table row read
  `# out of the floor: <label>`, the label being the skip echo's text up to its em dash. Spec 66's S12
  restates both, its AC1 extracts both and holds no bare `<arm>` placeholder, and its Files touched
  credits S12 on the spawn-guard suite. Observed by AC12.
- **S18** — id 18. In `tools/roles/adopt-roles.test.sh`, the arm-11 header comment's sentence "It stays
  out of the floor." reads "Its floor status is stated once, beside FLOOR_ASSERTIONS." No line of the
  file matches `[Oo]ut of the floor|[Ii]n the floor` except a line opening `# out of the floor: `.
  Spec 66's S20 and AC13 state that whole-file form. Observed by AC13.
- **S19** — The route. Spec 66's §4 "How an item closes" with S23's grammar. Each item states the built
  tree's end state, and the pass does what is missing or records that a landed unit already left it.
  Where an item changes another unit's criterion or scope item, the pass bumps that spec FIRST with a
  §9 line naming this unit (BUILD-METHOD M2, READY). That unit's ledger answers each changed criterion
  on one line in S23's grammar. Observed by AC14.

## 3. Non-goals (OUT)

- Ids 1 and 14, the HIGHs: `TOOL-dBoundRoles-67` and `TOOL-dBoundRoles-68`. S8 admits 67's signature
  entries into the one rule and restates nothing else of either unit.
- Rewording specs 1 to 68 beyond what an item changes.
- A PID liveness test for S13 (§4 "Alternatives rejected").
- The report's left-shift gates: the leftover-location entry, the two-units-one-criterion entry, the
  conditional-branch ledger entry, the one-source operand entry, the named-operand entry, the
  restated-rule entry, the retired-spelling inventory entry, the predicate-against-the-tree entry, the
  observed-by staging entry, the citation-resolution gate and the restated-row-shape entry. No clause of
  this build names them; each item's criterion is its regression. M7's gate leg in particular is the
  report's proposal, and `TOOL-aSparedSpawn-21` is the open ask nearest it.

### Edges

- **consumes-from** `TOOL-dBoundRoles-65` — S2, S3, S5, S6, AC1, AC2, AC4, AC5, §4 Evidence, Rollout and Files touched, and §5, which S1, S2, S4, S5 and S8 to S10, S15 and S16 restate (ids 2, 13, 7, 21, 12, 16, 15, 9 and 11 of the round-1 audit of units 65 and 66)
- **consumes-from** `TOOL-dBoundRoles-66` — S4, S8, S10, S11, S12, S20, AC1, AC2, AC8, AC9, AC13, AC16, AC17, §4 and the spawn guard's floor its pass left, which S1 to S3, S6 to S9 and S11 to S18 restate or correct (ids 2, 13, 3, 8, 22, 12, 16, 6, 23, 19, 5, 11, 17 and 18)
- **consumes-from** `TOOL-dBoundRoles-63` — S8, S12 and §5, the observation probe and its cleanup, which S5, S6, S8, S13 and S15 restate (ids 21, 8, 12, 19 and 9)
- **consumes-from** `TOOL-dBoundRoles-64` — S12, S18, §4 "The executed-count rule" table and §5, which S8, S13, S15 and S17 restate (ids 12, 19, 9 and 17)
- **consumes-from** `TOOL-dBoundRoles-60` — §4 "Where each item lands" and AC6's `fixture:` line, which S10 restates (id 15)
- **consumes-from** `TOOL-dBoundRoles-67` — S3's take-away of signature entries, which S8's one rule admits by name (id 12)

## 4. Design

### Why one unit

M4 admits two units only when the minors split into two disjoint write sets by M6. They do not. S1,
S8, S9 and S16 each write both spec 65 and spec 66, so any split has both halves writing one spec, and
M6 clause 1 refuses it. S5, S6, S8, S13 and S15 also write spec 63, the probe's text that S7's and
S9's criteria read as acceptance input, which clause 2 refuses.

### Where each item lands at order 39

Every other unit has built, units 65 to 68 included, so the specs, ledgers and floors these items
correct are on the tree. Order 39 is above every unit of the build, because the minors land on two
units, 65 and 66, at order 37. S8 also names 67's S3, which builds at order 38.

### The ledger reading of S1 to S3

```python
import re
LEDGER = re.compile(r"^- (\S+) — amended rev-(\d+)\b")          # deviation_join.py:163
LIST = re.compile(r"^- \S+ — amended rev-\d+ \(((?:rev-\d+, )*rev-\d+)\)")
def revisions(line):
    m = LEDGER.match(line)
    if not m:
        return None
    rest = LIST.match(line)
    return [int(m.group(2))] + ([int(r[4:]) for r in rest.group(1).split(", ")] if rest else [])
```

A criterion holds when its unit's revision is in `revisions(line)`. `LEDGER` still addresses the latest
bump, so the deviation join is unchanged. The block shows the design's shape; the pass fits it to each
criterion it restates.

### The one cleanup rule

S12's rule lists four kinds of entry, and each is one a pass can prove it owns. The run's own path was
made by that run. A `prunable` entry has lost its directory. A stale entry carries an epoch older than
any live observation, which records price at seconds (spec 66 AC8's `cost:` line), so 3600 seconds
leaves a wide margin. A signature entry belongs to a pass whose spec is `CLOSED` (67's S3). Every other
entry is recorded and left in place.

### Evidence

Read at base `462d20f3` on 2026-10-26; HEAD equals base for every code file cited here:

- `tools/memory-tree/deviation_join.py:163` is `LEDGER`, capturing one revision.
- `tools/branch-reconcile/branch_reconcile.py:208-209` keeps `locked` and `prunable` in `flags`.
- With `TMPDIR` set to a scratch directory, `tempfile.gettempdir()` printed that directory, while
  `os.environ["TEMP"]` and `cygpath -m "$TEMP"` both printed `C:\Users\d41ly\AppData\Local\Temp`.
- In the agent-cap suite, `grep -cE '^[[:space:]]*(for|while) '` prints 66. S11's line pattern prints
  20: 15, 44, 797, 815, 883, 933, 1254, 1278, 1281, 1306, 1331, 1394, 1403, 1810, 1816, 1898, 1959,
  1967, 1970 and 2480. With bodies bounded at their matching `done` and S14's predicate, a scratch probe
  selected exactly S12's ten. The loop at 1403 matched only on `echo "FAIL `.
- The skeptic of id 19 reproduced that a worktree whose directory is present shows no `prunable` line,
  and shows one only after the directory is gone.
- `git grep -n 'TEMP%' -- memory/builds/dBoundRoles/spec` finds the observation's location at spec
  60:212 and :297, spec 63:87 and :213, and spec 64:118 and :337. Spec 64:118 says spec 63's S8 states
  it too once unit 64 has built.
- `tools/roles/adopt-roles.test.sh` matches `[Oo]ut of the floor|[Ii]n the floor` at lines 73, 76
  and 415. Spec 66's S20 rewrites 73 and 76, and S18 rewrites 415.
- Spec 64's S12 keeps `# out of the floor: <arm>` at line 96 and its §4 table row at line 239.

### Inventory

Minted: none. `root:` and `worktree:` are output line prefixes of a probe this build owns.

### Migration

None: no stored data changes. The ledger answers this unit writes are lines this build's passes own.

### Rollout

Live at landing, at order 39, after units 67 and 68 at order 38. No other unit shares the order.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`, the arm-11 header comment (S18)
- `tools/roles/spawn-guard.test.sh`, the floor and its comment, only where unit 66's pass counted a loop
  outside S11's class (S14)
- the specs of units 60, 63, 64, 65 and 66, rev bumps, named here for the dispatch write set
- the acceptance ledgers of units 60, 63, 64, 65 and 66 and this unit's own, the AMENDED answers and
  the predicate check, named here for the dispatch write set

### Alternatives rejected

- **Two units.** §4 "Why one unit".
- **A PID liveness test for S13, the report's first option.** The probe's `<pid>` is a Windows PID
  from Python or an MSYS PID from bash, and the two do not compare. Python's `os.kill(pid, 0)` on
  Windows calls `TerminateProcess` rather than testing liveness. An age bound reads only the name.
- **Taking out a hard-killed run's directory before the forced removal.** It turns a live concurrent
  observation into a `prunable` entry, the hazard S8 exists to refuse.
- **Excluding heredoc bodies by tracking delimiters, as the report words it.** Lines 1879 and 2415 sit
  in quoted strings, not heredocs. S11's `; do` line pattern excludes all four kinds by the loop's own
  syntax.
- **The report's first fix for id 5, judged UNSOUND by its skeptic.** S14 is the skeptic's corrected
  predicate.

## 5. Production-readiness checklist

- security — no new write path in shipped code. S8 confines every forced removal to four kinds of
  entry a pass can prove it owns, and S13 adds only the stale kind under the probe's own root.
- perf / scale — extraction probes, one fixture ledger, one staged observation and one read of a
  suite's source.
- error / empty / loading states — a probe whose `worktree:` line is absent reds AC5 rather than
  comparing against nothing.
- observability — the ledgers record the predicate's selection and each corrected count, and the
  probe prints its root and worktree.
- risks — a live observation older than an hour would be taken away by S13. Records price one at
  seconds, and a `locked` entry is never taken.
- testing — AC1 to AC14 by extraction probes, a fixture ledger, a staged observation and a count of
  source.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe extracts spec 65's AC5 and S6 and spec 66's AC17, each joined, AC5
  and AC17 each accept their unit's revision as the one `LEDGER` captures or one inside the
  parenthesised list, and S6 writes `amended rev-<latest> (`.
  Red when: a criterion reads only the first revision, so whichever unit lands second reds the other.
- **AC2** — When a `python -c` probe runs §4's `revisions` over a scratch ledger block holding unit
  64's AC13 line in each landing order, `- AC13 — amended rev-6 (rev-5) — ...` and the same with the two
  revisions standing for the other unit, the restated AC5 and AC17 checks are green on both. Spec 65's
  §4 Rollout and spec 66's §4 "Where each item lands" hold no "either order lands both".
  Red when: one landing order leaves a correct tree with a red criterion.
  fixture: a scratch ledger file under the run's scratch directory.
- **AC3** — When a `python -c` probe extracts spec 66's AC16, joined, it names the highest revision and
  the parenthesised list. Over the scratch line `- AC15 — amended rev-6 (rev-5) — ...`, with rev-5
  standing for unit 64, the restated check is green.
  Red when: S9's bump of spec 60 makes AC16 and AC17 demand two different revisions of one line.
- **AC4** — When a `python -c` probe extracts spec 65's S2 and AC4 and spec 63's S12, each joined, S2
  names `os.environ["TEMP"]` and `cygpath -m "$TEMP"` and admits `gettempdir` only as refused. S12 names
  the `root:` line, and AC4 names the equality with the printed root.
  Red when: the probe and the check can resolve `<TEMP>` from two sources that differ under `TMPDIR`.
- **AC5** — When a `python -c` probe extracts spec 63's S12 and spec 66's S10 and AC8, joined, S12
  names the `worktree:` line printed after the porcelain names the entry and before the import. AC8
  requires that line, the entries recorded before the staged run, and a subset after it.
  Red when: AC8's equality has no operand, so a failed import that leaves its worktree passes.
- **AC6** — When a `python -c` probe extracts spec 63's S12, joined, it names the run's own path,
  `prunable`, `locked`, the 3600-second stale bound and `TOOL-dBoundRoles-67`. Spec 64's S18, spec
  65's S5 and spec 66's S10 and S11 each name "S12's cleanup rule". None of spec 65's S2, S5 or §5 holds
  "holds nothing but" or "holds nothing else", and spec 66's AC9 names spec 65's S5.
  Red when: two specs state two cleanup rules for one root, so one can take away a live entry the other
  protects.
- **AC7** — When a `python -c` probe extracts spec 60's §4 "Where each item lands" and AC6 `fixture:`
  line, spec 63's S8 and §5 security line, and spec 64's §5 security line, each names `dbr63obs` where
  it states the location and none holds "short `%TEMP%`" or "extracted with `git archive`". Spec 65's S3
  lists each, and its Files touched names spec 60.
  Red when: a second spelling of the observation's location survives outside spec 65's AC2.
- **AC8** — When a `python -c` probe applies S11's class and S14's predicate to the agent-cap suite at
  `462d20f3` through `git show`, it selects exactly lines 797, 883, 933, 1810, 1816, 1898, 1959, 1967,
  1970 and 2480, and none of 451, 1403, 1879, 2415 or 1331. Spec 66's S4, §4 Evidence and AC2 state the
  class, the predicate and both control lists.
  Red when: a JavaScript or Python loop, or a loop that never raises `pass`, enters the count.
  figure: PINNED, measured 2026-10-26 at `462d20f3`.
- **AC9** — When the pass plants two entries in this repository with `git worktree add --detach` under
  the observation's root, `1-1` with its directory kept and a second named with the current epoch, the
  porcelain shows `1-1` registered and not `prunable`. After the probe of spec 63's S12 runs once, `1-1`
  is gone and the current-epoch entry stays. The pass then takes that entry away itself.
  Red when: a hard-killed run's worktree, directory present, stays registered through every recovery.
  cost: two worktree checkouts of this repository, seconds.
- **AC10** — When a `python -c` probe applies S11's class to the spawn-guard suite unit 25 adds, every
  selected loop appears with its iteration count in this unit's ledger line for AC10, and
  `FLOOR_ASSERTIONS` equals the E that line records.
  Red when: a loop outside the class was counted, so the floor sits above what the suite executes.
  figure: DERIVED from source at the pass; PINNED in the ledger at that pass's commit.
- **AC11** — When a `python -c` probe reads spec 65's §4 Evidence and spec 66's S8 and §4 Evidence, they
  cite the dWitnessedBar-58 review at `:89`, spec 64's S18 at `116-121`, its AC13 at `417-421`, spec
  63's §5 at `213` and spec 62's §7 at `171`. Spec 65 names `C:\Program Files`, and spec 66's S8 holds
  no spec 52 line 81 among its bare-token hits.
  Red when: a builder re-checking a citation lands on the wrong line.
- **AC12** — When a `python -c` probe extracts spec 64's S12 and its §4 table rows and spec 66's S12 and
  AC1, each reads `# out of the floor: <label>`, none holds `# out of the floor: <arm>`, and spec 66's
  Files touched names S12 for the spawn-guard suite.
  Red when: a restated row shape keeps the field's old payload.
- **AC13** — When a `python -c` probe reads the roles adopter suite (its path in S18 and Files touched)
  whole, no line matches `[Oo]ut of the floor|[Ii]n the floor` except lines opening
  `# out of the floor: `. Spec 66's S20 and AC13 state that whole-file form.
  Red when: the file states arm 11's floor status in two places.
- **AC14** — When a `python -c` probe reads the `**Evidences:**` blocks of units 60 and 63 to 66, no
  criterion label is answered twice in one block, and each criterion this unit changed has the revision
  whose §9 line names `TOOL-dBoundRoles-69` among the `revisions` of its line.
  Red when: an amendment adds a second answer beside the first.

## 7. Gates

`roles adopter self-test` · `agent-cap self-test` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`agent-cap self-test` stands for the spawn guard's suite; unit 25's pass renames it on every live §7 line
when it renames the leg. No arm moves here: a floor correction is re-observed by spec 64's two
`New arm:` lines, with the bound unit 66's S5 adds.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause, so veto 1 discards
  (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1
  set. widens: none · relaxes: none
- **F2 — Which text owns the one cleanup rule (id 12)?** Options: (a) spec 63's S12, the probe's own
  text, which spec 66's S11 already writes the rule into; (b) spec 65's S5, beside the comparison; (c)
  spec 66's S11. Under (b) or (c) the probe's own text would cite a spec of a later order for what it
  may do, and spec 66's AC9 already reads S12 for it. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3, the most feature-rich survivor and the seam AC9 already reads. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the 13 MEDIUM and 5 LOW findings of the round-1 audit of units 65
  and 66, each id its own item, in one unit.

## 10. Reuse audit

The seams are the units' own and the tree's: `LEDGER` of `tools/memory-tree/deviation_join.py:163`,
which §4's reading extends rather than replaces, spec 66's "How an item closes" route and S23 grammar,
spec 63's S12 probe, and `tools/branch-reconcile/branch_reconcile.py`'s `parse_worktrees` with its
`prunable` and `locked` flags. `python tools/codebase-map/reuse_lookup.py "find leftover git worktrees by their checked-out commit wherever they sit"`
ranked `git`, `check`, `build_commit`, `run_git` and `add_scratch_worktree`, none a cleanup rule or a
loop classifier, so no existing seam fits beyond those named. The recall query's hits include
`TOOL-dSweptBranches-8`, whose take-away reaches only a proven worktree, the rule S8 follows, and
`TOOL-aSparedSpawn-21`, the open ask to compare a floored suite's floor against its executed lines.

Recall terms used: `python tools/memory-recall/query.py "how is a leftover scratch worktree found and removed safely without touching another session's" --terms "worktree porcelain detached HEAD signature leftover sweep prunable locked forced removal temp root"`
