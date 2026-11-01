# TOOL-dTendedCadence-74 — the round-1 spec audit of units 49 to 59, its 26 minors batched: the hold's readers renamed, staleness and security claims that hold, criteria scoped to what they claim, and the population rules that can reach their fallback

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 24 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 49 to 59,
`reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`, confirmed 40 findings,
and TOOL-dTendedCadence-60 to -73 take its 14 HIGH. This unit is BUILD-METHOD M4's batch of its 19
MEDIUM and 7 LOW by raw id, one scope item per id, in report order, M1 to M15 and then L1 to L7. They
land on units 6, 16, 17, 37, 38, 43, 48, 49, 52, 54, 55, 56, 58 and 59, so it repairs no unit in
particular and builds last, order 24, above every unit of the build. They do not split into two
disjoint write sets: the drift-audit items share `tools/drift-audit/selftest.py`, and the criterion
items of units 58 and 59 share those specs with the drift-audit items that correct them, so one unit
carries them all.

Every id: M1 2; M2 3; M3 6, 40; M4 7; M5 8; M6 9, 33; M7 15; M8 16, 42; M9 18, 32; M10 20; M11 23;
M12 25; M13 31; M14 41; M15 43; L1 11; L2 12; L3 17; L4 19; L5 34; L6 39; L7 44.

A correction to a sibling spec's prose is made in that spec's text, a rev bump with a §9 line naming
the review id, in this unit's build pass, whatever the sibling's status by then, as
TOOL-dTendedCadence-59 §1 states for its own batch.

## 2. Scope (IN)

- **S1** — id 2, M1, landing on unit 37. Unit 37 AC1 routes its held reading `red-leg` in place of
  `held`, so unit 37 AC1 and unit 56 AC2 no longer require opposite outcomes for one input; the arm
  of unit 37 is corrected to match. Observed by AC1.
- **S2** — id 3, M2, landing on units 6 and 37. The kit-descriptor copies unit 6 AC8's and unit 37
  AC1's fixtures read plant `[[item]]` rows routing every route their readings carry to
  `item.maintain.record`, so unit 56 S3's refusal leaves both arms green. Observed by AC2.
- **S3** — id 6, M3, landing on unit 59. Unit 59 S13 reads: `seen` from an open build appends a
  receipt where the intake is on record in that store, and files no new intake only where it is not,
  so an open cycle still recurs as unit 53 S3 says. Observed by AC3.
- **S4** — id 40, M3, landing on unit 54. Unit 54's three-cycle case runs after S13 is built and
  still answers `seen 2026-W46` with two receipts, W45 and W46, on the second intake. Observed by AC3.
- **S5** — id 7, M4, landing on unit 59. Unit 59 AC36's second half reads only each spec's `### Files
  touched` block, the lines between that heading and the next, for `help/maintain.md`; at base that
  restricted probe prints 0 for specs 36, 43, 45, 46 and 47. Observed by AC4.
- **S6** — id 8, M5, landing on unit 59. Unit 59 AC34 greps only spec-41's §5 `migration` bullet for
  `by name`, so spec-41's unrelated sentence at :84 cannot fail it. Observed by AC5.
- **S7** — id 9, M6, landing on unit 59. Unit 59 AC35's Skill measure reads the build's own tip, `git
  cat-file -s HEAD^2:.claude/skills/unattended/SKILL.md` when `HEAD` is the prepared merge, else
  `HEAD:`, and expects 10234, so main's edits to the Skill cannot fail it. Observed by AC6.
- **S8** — id 33, M6, landing on unit 59. Unit 59 §5 risks states that a prepared merge crossing the
  Skill's 10240-byte cap (`tools/template-size-limits.txt:154`) reds the `unattended skill size` leg,
  answered by trimming the Skill in the merge. Observed by AC6.
- **S9** — id 15, M7, landing on units 16, 17, 37, 38 and 43. Each by-value reader of the red leg's
  hold spells `red-leg`: spec-16:126, spec-17:129 and :292, spec-37:30-35, :86 and :99, spec-38:65 and
  spec-43:50; unit 3's direct outcome `held` keeps its name wherever it is the subject. Spec-1 and
  spec-15 are TOOL-dTendedCadence-60's and -62's. Observed by AC7.
- **S10** — id 16, M8, landing on unit 58. Unit 58's merge search is bounded to the build's range,
  `git rev-list --first-parent --min-parents=2 --max-count=1 f4597719..HEAD`, so with no prepared
  merge the answer is empty and the `f4597719..HEAD` fallback runs. Observed by AC8.
- **S11** — id 42, M8, landing on unit 58. Unit 58 S1 takes `check_prepared_merge`'s three facts
  rather than its first alone: a found `t` is used only when `bash tools/push-main.sh --prepared
  --slug dTendedCadence` exits 0 (`tools/push-main.sh:24`, read-only), else the fallback runs; a
  scratch-clone case puts the branch's base above an older first-parent merge and requires the
  fallback. Observed by AC8.
- **S12** — id 18, M9, landing on unit 49. Unit 49 §4's paragraph after "The payload commit" and its
  §5 security line state the boundary at base: the secret scan of `refs/gov/*` pushes is
  TOOL-dWellOiledMachine-17 S7 and S8, DEFERRED, and `.githooks/pre-push` reads only `refs/gov/bar-red`
  (`:42`, `:1912-1974`), so until it lands the record leaves the node unscanned; the exposure is the
  record the patch build commits anyway. Observed by AC9.
- **S13** — id 32, M9, landing on unit 49. Unit 49 §3 declares the precondition: a `consumes-from
  external` edge naming TOOL-dWellOiledMachine-17's scan, DEFERRED. Observed by AC9.
- **S14** — id 20, M10, landing on unit 52. Unit 52 AC3 extracts the section first, `awk '/^## The
  security review/{f=1;next} /^## /{f=0} f' maintain.md | grep -c 'four lines'`, and keeps no
  `maintenance.py land` alternative. Observed by AC10.
- **S15** — id 23, M11, landing on units 56 and 1. `read_maintain_items(kit_dir)`, with unit 1 S2's
  refusals of a route naming no row, a route with no `stand-in:` and an outcome with no route, lives
  in `tools/drift-audit/maintenance.py`; `derive_record_routes` is built over it, and `maintain.py`
  imports it from there. Unit 56 §10 names `read_maintain_items` and ask TOOL-dTendedCadence-25.
  **Readers:** by name: `2026-11-01-spec-TOOL-dTendedCadence-1.md`, S2, which defines the function in
  `maintain.py`; READER NOT IN TREE for `read_maintain_items` itself, which unit 1 builds at order 8.
  by value: NO VALUE READERS — the rows it returns are read by the walk and the derivation in the same
  call, and never written. Observed by AC11.
- **S16** — id 25, M12, landing on units 58 and 59. Unit 58 AC2 and unit 59 AC12 read: `bash
  skills/session-kickoff/manifest-check.sh` exits 0 at the close, after the last `--prepare`, printing
  no C5 line; unit 58 §4's hand-typed `<restamp>` rule is not kept, and C5 (`manifest-check.sh:1517`)
  is named in unit 58 §9 and unit 59 §10. Observed by AC12.
- **S17** — id 31, M13, landing on unit 49. Unit 49 AC3 states that unit 1's walk fixture gains §6's
  scratch bare remote as its one remote, resolved by TOOL-dTendedCadence-68's ladder, with
  `refs/remotes/<name>/HEAD` recorded; a zero-remote case exits the walk 1 with no filing. Observed by
  AC13.
- **S18** — id 41, M14, landing on unit 55. `read_breach_records` reads node records only for the
  nodes the current `maintain.node-readings` value runs: none under `lease-holder`, so node records
  committed under an earlier `every-node` leave the population when the policy changes. Observed by
  AC14.
- **S19** — id 43, M15, landing on units 59 and 48. Unit 59 S14's lock lives in
  `add_detached_worktree` (unit 48 S40), taken on `<tree>.lock` before `git worktree add` and held
  until the take-down, so `resolve_reading_tree` and `security_review.py` both get it. A tree with no
  lock file is pruned only once its directory is older than 3600 s. At take-down the holder takes the
  tree down, then closes and unlinks its lock file. Unit 59 S14's Readers name `security_review.py`.
  Observed by AC15.
- **S20** — id 11, L1, landing on unit 52. Unit 52 AC2 states that the landing clone pushes its commit
  to the bare remote and the fixture repository fetches and fast-forwards before its second run.
  Observed by AC16.
- **S21** — id 12, L2, landing on unit 59. Unit 59 S33 spells the citation `spec-8 :131, :156`, the
  form AC31 greps. Observed by AC17.
- **S22** — id 17, L3, landing on unit 58. Unit 58 AC2's subset clause reads instead as a
  scratch-clone observation: a main-side commit touching `tools/gate-legs.json`, reachable only
  through the prepared merge's first parent, is absent from the second command's output, and a
  branch commit touching it is present. Observed by AC18.
- **S23** — id 19, L4, landing on unit 49. Unit 49 S2 cites `write_claim`'s push at
  `tools/unattended/unattended.sh:2423`, a `--force-with-lease` push, and states the deliberate
  difference: a plain `--force`, because the ref is content-addressed and moved only by a newer record.
  Observed by AC19.
- **S24** — id 34, L5, landing on unit 59. Unit 59 §4 Files touched lists
  `memory/builds/dLinkedLibrary/README.md` as re-rendered by S25's escaping, and AC25 splits that
  build's TOOL-dLinkedLibrary-85 row too. Observed by AC20.
- **S25** — id 39, L6, landing on unit 49. `write_record_landing` runs `git check-ref-format
  refs/gov/maintain-record/<key>` before it builds the commit and raises naming the key on a refusal.
  Observed by AC21.
- **S26** — id 44, L7, landing on unit 59. A `probe:` line with fewer than two TABs is refused by name
  at write, exit 2, and skipped with one line at read; unit 59 S28 says so and AC28 adds the case
  `probe: rA<TAB>probe-7`. Observed by AC22.

## 3. Non-goals (OUT)

- Every HIGH: TOOL-dTendedCadence-60 to -73.
- The left-shift gates the report names beside each minor: each is a gate of its own, outside the one
  mechanism M4 admits for this batch.
- Re-reviewing a sibling spec corrected in place: a correction moves the cited prose and nothing else.

### Edges

- **consumes-from** `TOOL-dTendedCadence-37` — AC1, its arm and the hold's spelling (S1, S2, S9)
- **consumes-from** `TOOL-dTendedCadence-6` — AC8's fixture, which plants item rows (S2)
- **consumes-from** `TOOL-dTendedCadence-59` — S13, S14, S28, S33, AC34, AC35, AC36 and its Files touched (S3, S5 to S8, S16, S19, S21, S24, S26)
- **consumes-from** `TOOL-dTendedCadence-54` — the three-cycle case re-run after S13 (S4)
- **consumes-from** `TOOL-dTendedCadence-16` — the hold's spelling at :126 (S9)
- **consumes-from** `TOOL-dTendedCadence-17` — the hold's spelling at :129 and :292 (S9)
- **consumes-from** `TOOL-dTendedCadence-38` — the hold's spelling at :65 (S9)
- **consumes-from** `TOOL-dTendedCadence-43` — the hold's spelling at :50 (S9)
- **consumes-from** `TOOL-dTendedCadence-58` — the merge search, its fact 2, AC2's re-stamp and subset clauses (S10, S11, S16, S22)
- **consumes-from** `TOOL-dTendedCadence-49` — the security claim, its precondition, AC3's fixture, the push citation and the ref check (S12, S13, S17, S23, S25)
- **consumes-from** `TOOL-dTendedCadence-52` — AC2's clones and AC3's section probe (S14, S20)
- **consumes-from** `TOOL-dTendedCadence-56` — `derive_record_routes` over the one row reader, and its §10 (S15)
- **consumes-from** `TOOL-dTendedCadence-1` — `read_maintain_items`, imported from `maintenance.py`, and the walk fixture (S15, S17)
- **consumes-from** `TOOL-dTendedCadence-55` — `read_breach_records`' node population (S18)
- **consumes-from** `TOOL-dTendedCadence-48` — `add_detached_worktree` (S40), where the scratch tree's lock lives (S19)
- **consumes-from** `TOOL-dTendedCadence-68` — the remote ladder AC3's walk fixture is phrased in (S17)

## 4. Design

### Evidence

Each item's finding, its cited lines and its skeptic verdict are the report's, by id; ids 3 and 23
carry the skeptic's corrected fix, which S2 and S15 take, and id 33's corrected fix is S7 and S8.
Read at base for this unit: `tools/push-main.sh:504-537` (`check_prepared_merge`'s three facts),
`skills/session-kickoff/manifest-check.sh:1517-1534` (C5 and its `blockstamp` validation),
`tools/template-size-limits.txt:154` (10240) against `wc -c .claude/skills/unattended/SKILL.md`'s
10237, `tools/memory-tree/gen_build_index.py:1564` (the unescaped label), and
`memory/builds/dLinkedLibrary/README.md`'s TOOL-dLinkedLibrary-85 row. `git check-ref-format
refs/gov/maintain-record/2026-11-01.lock` exits 1 (probe at writing, 2026-11-01), and unit 35's `node`
pattern admits the segment `lock` (spec-35:72).

### The scratch tree's lock (S19)

```
add_detached_worktree(root, sha, subdir):
    lock = open(<tree>.lock, "a+"); flock / msvcrt.locking, exclusive   # before the add
    git worktree add --detach <tree> <sha>
    yield <tree>
    finally: take the tree down; unlock; close; unlink <tree>.lock
prune(tree):
    <tree>.lock absent  -> prune only if the directory is older than 3600 s
    lock acquired       -> prune, then unlink the lock
    contention          -> alive, keep
```

The lock is taken before the add, so no prune can acquire a lock for a tree that is being created.
3600 s is PINNED, a `ponytail:` ceiling: a scratch tree lives for one reading or one review, minutes,
and the upgrade is the run's own budget once one is declared.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_maintain_items` | function, moved from `maintain.py` to `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S15, S18, S25, S26
- `tools/drift-audit/maintain.py`: S15
- `tools/drift-audit/readings.py`: S3
- `tools/drift-audit/drift_report.py`: S19
- `tools/drift-audit/security_review.py`: S19
- `tools/drift-audit/selftest.py`: the arm of §7
- `memory/builds/dTendedCadence/spec/`: the in-place corrections of S1, S3, S5 to S14, S16, S17, S19
  to S24 and S26

## 5. Production-readiness checklist

- security — S12 and S13 state the unscanned exposure instead of claiming a scan; S25 refuses a ref
  name git refuses before any object is built.
- perf / scale — S10 bounds a graph walk to the build's range; S19 adds one lock per scratch tree.
- error / empty / loading states — S26 refuses a short `probe:` line; S17's zero-remote case exits 1.
- observability — S25's raise names the key; S26's skip line names the record.
- risks — an in-place correction to a terminal sibling moves prose only, never its status or scope;
  S18 drops a departed node's stale record from the leg, so a node that still runs under a policy that
  no longer names it is read by no leg, which is what the policy says.
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — nothing exists at base.
- user docs — N/A — no page names an item here beyond what units 49 to 59 already document.

## 6. Acceptance criteria

The fixtures are each landing unit's own, named per criterion.

- **AC1** — When `grep -n "route\s*.held." 2026-11-01-spec-TOOL-dTendedCadence-37.md` runs in the spec
  folder, no hit sits in AC1, and unit 37's arm, run with a reading routed `red-leg` and one key over
  rows routing `red-leg` to the record, writes one `over-pin:` line.
  Red when: units 37 and 56 still require opposite exits for one input.
- **AC2** — When the arms of unit 6 AC8 and unit 37 AC1 run after unit 56 is built, each passes; with
  their planted rows taken out, each exits 2 naming `no item row routes to item.maintain.record`.
  Red when: an earlier unit's arm reds on the later refusal.
- **AC3** — When two scratch intake stores file one target, the fixture commits an OPEN build README
  naming its key, and each store runs once more, the store holding the intake gains a receipt and the
  other files nothing; and unit 54's three-cycle case prints `seen 2026-W46` with two receipts on the
  second intake.
  Red when: an open cycle loses its receipt, or a second node files a second intake.
- **AC4** — When `awk '/^### Files touched/,/^## /'` over each of specs 36, 43, 45, 46 and 47 is piped
  to `grep -c "help/maintain.md"`, it prints 0 for each at base (PINNED 2026-11-01) and 1 for each once
  unit 59 S38 lands; and `grep -n "### Files touched" 2026-11-01-spec-TOOL-dTendedCadence-59.md`
  matches inside AC36.
  Red when: the probe still counts a §5 docs line.
- **AC5** — When `grep -n "by name" 2026-11-01-spec-TOOL-dTendedCadence-59.md` runs in the spec
  folder, AC34's command names spec-41's `migration` bullet as its range.
  Red when: AC34 still fails on spec-41:84.
- **AC6** — When `grep -n "HEAD^2:.claude/skills/unattended/SKILL.md\|10240"
  2026-11-01-spec-TOOL-dTendedCadence-59.md` runs in the spec folder, AC35 and §5 risks each match.
  Red when: AC35 measures the prepared merge's absolute bytes.
- **AC7** — When `grep -n "held" 2026-11-01-spec-TOOL-dTendedCadence-16.md
  2026-11-01-spec-TOOL-dTendedCadence-17.md 2026-11-01-spec-TOOL-dTendedCadence-38.md
  2026-11-01-spec-TOOL-dTendedCadence-43.md` runs in the spec folder, no hit names the red leg's hold.
  Red when: a reader still spells the hold `held`.
- **AC8** — When unit 58's first command runs on a scratch clone whose branch base sits above an older
  first-parent merge and carries no prepared merge, `t` is empty and the population is the base range;
  and run over this tree before the last `--prepare` it prints nothing (probe at writing, 2026-11-01,
  where the unbounded form printed `142feb0c1`).
  Red when: a foreign merge stands in for the prepared one.
- **AC9** — When `grep -n "DEFERRED" 2026-11-01-spec-TOOL-dTendedCadence-49.md` runs in the spec
  folder, §4, §5 security and a §3 `consumes-from external` edge each match.
  Red when: the security case still cites an unbuilt scan as coverage.
- **AC10** — When unit 52 AC3's section probe runs over a `maintain.md` whose "The Maintain run" says
  `four lines` and whose "The security review" does not, it prints 0.
  Red when: a match in another section passes the criterion.
- **AC11** — When `grep -c "def read_maintain_items" maintenance.py maintain.py` runs in
  `tools/drift-audit/`, it prints 1 and 0, and `derive_record_routes` over a row with no `routes`
  exits 2 with the reader's refusal, never a `KeyError`.
  Red when: two readers of one table exist.
- **AC12** — When `grep -n "C5" 2026-11-01-spec-TOOL-dTendedCadence-58.md
  2026-11-01-spec-TOOL-dTendedCadence-59.md` runs in the spec folder, unit 58 AC2 and unit 59 AC12
  match, and `grep -c "newest commit of the population touching"` over spec-58 prints 0.
  Red when: a criterion re-types C5 with a weaker re-stamp.
- **AC13** — When unit 49 AC3's walk runs over unit 1's fixture with the bare remote and its recorded
  HEAD, the recorded text's first line is `land maintenance-record 2026-11-01`; with no remote, the
  walk exits 1 and records nothing.
  Red when: the criterion's fixture cannot reach a landing.
- **AC14** — When unit 55's fixture commits a node record with one `over-pin:` line, then plants
  `node-readings = "lease-holder"` and commits a clean period record, `python maintain_file.py leg`
  exits 0.
  Red when: a policy switch leaves the leg red forever.
- **AC15** — When `add_detached_worktree` holds a tree and a sibling prune runs, the tree survives; a
  tree with no lock file younger than 3600 s survives and an older one is pruned; after take-down no
  `<tree>.lock` remains; and `security_review.py`'s tree passes through the same function.
  Red when: a live tree is pruned, a lock file is left behind, or a caller bypasses the lock.
- **AC16** — When `awk '/^- \*\*AC2\*\*/,/Red when/' 2026-11-01-spec-TOOL-dTendedCadence-52.md` runs in
  the spec folder, piped once to `grep -c "push"` and once to `grep -c "fast-forward"`, each prints a
  count above 0, where at base each prints 0; S20's text names the push from the landing clone and the
  fixture's fetch and fast-forward before the second run.
  Red when: the second run's repository is unstated.
- **AC17** — When `grep -n ":131, :156" 2026-11-01-spec-TOOL-dTendedCadence-59.md` runs in the spec
  folder, S33 and AC31 each match.
  Red when: the S-item and its criterion spell one citation two ways.
- **AC18** — When unit 58 AC2's scratch clone runs the second command, the main-side commit touching
  `tools/gate-legs.json` is absent and the branch commit touching it is present.
  Red when: the clause cannot fail.
- **AC19** — When `grep -n "unattended.sh:2423" 2026-11-01-spec-TOOL-dTendedCadence-49.md` runs in the
  spec folder, S2 matches and names the plain `--force` and its reason.
  Red when: the citation still names lines the flag is not on.
- **AC20** — When `gen_build_index.py --write` renders the dLinkedLibrary README, its
  TOOL-dLinkedLibrary-85 row splits into six cells on unescaped pipes, and unit 59's Files touched names
  that README.
  Red when: a re-rendered file outside the write set goes undeclared.
- **AC21** — When `write_record_landing` runs with the key `2026-11-01.lock`, it raises naming the key
  before any object is written, and `git -C <bare> for-each-ref refs/gov/` prints nothing new.
  Red when: a ref name git refuses reaches the push.
- **AC22** — When `python maintenance.py write` runs with `fields.probe` holding a line that parses as
  `probe: rA<TAB>probe-7`, it exits 2 naming the line; a committed record carrying it is read with one
  skip line.
  Red when: a short `probe:` line yields an empty offender key silently.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 AC10 AC11 AC13 AC14 AC15 AC21 AC22 · one plant per item over the fixtures its landing unit's arm builds, staged against each unit's text as the audit read it · none

## 8. Open questions

- **F1 — Which bound prunes a scratch tree that has no lock file (id 43)?** Options: (a) a fixed
  3600 s; (b) never prune one; (c) a policy key. (b) leaks every tree a crash leaves between the lock
  and the add, which S19's order makes impossible but a pre-existing tree is not; (c) adds a public
  surface, veto 2. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, with a `ponytail:` ceiling.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the 19 MEDIUM and 7 LOW of the round-1 spec audit
  of units 49 to 59, one scope item per raw id.

## 10. Reuse audit

Every item extends the seam its landing unit names: unit 56's derivation over unit 1's row reader,
`check_prepared_merge` (`tools/push-main.sh:504-537`), C5 of `manifest-check.sh`, unit 48's
`add_detached_worktree`, TOOL-dTendedCadence-68's ladder and git's own `check-ref-format`. `python
tools/codebase-map/reuse_lookup.py "derive the outcomes the item rows route to one item"` and `"take a
lock before pushing from a git dir"` ranked name stems only, so no existing seam fits beyond those.

Recall terms used: `python tools/memory-recall/query.py "which minors did the round-1 audit of units
49 to 59 confirm" --terms "red-leg held readers superseded receipt open cycle prepared merge C5
restamp scratch tree lock check-ref-format probe line"`
