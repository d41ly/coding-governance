# TOOL-dPavedRoad-4 — `--staged` grades the edge joins and the ledger joins for what it stages

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-dPavedRoad-4-ledger.md](../build/2026-11-10-build-TOOL-dPavedRoad-4-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md](../prompts/2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md) | research | TOOL-dPavedRoad-1 TOOL-dPavedRoad-2 TOOL-dPavedRoad-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/check-memory-hygiene.sh --staged` grades check 12's three §3 edge joins and
check 23's acceptance-ledger joins for the specs and journal records a commit stages, each read
against its own build folder as it stands in the worktree. Both are held under `--staged` today, so
dSafePassage's 6 one-way edges and 10 unjoined ledger lines surfaced only at the close and cost it
two adopted units (the brief, `2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md`, item 4).

## 2. Scope (IN)

- **S1** — Check 12's selection under `--staged`. The loop at
  `tools/memory-tree/check-memory-hygiene.sh:2050-2055` still tags each staged spec `P`. It also tags
  `J` every other spec in `c12_all` that sits in a build folder holding a staged spec, when
  `SPEC_EDGES_CUTOFF` is non-blank. The build set comes from the staged spec paths, never from
  `FILES`, so a commit that stages the conf (`FILES` is then the whole listing, :793-795) reads no
  extra build. Full mode tags nothing `J`. Observed by AC1 and AC2.
- **S2** — The batched awk reads a `J` spec for its edges only. The edge block at :2661-2721 becomes
  one awk function, `extract_edges`, that sets the shape counters and emits the `\003` E and U
  records. The `P` path
  calls it where the block sits today and keeps the three shape prints at :2711-2716 at that call
  site. A `J` record is read, and if its header parses and is not Tier-1, the function runs and the
  record ends there, so no other arm sees it. The two emissions at :2709 and :2720 print in both
  modes. Each E and U record carries one more field, 1 for a `P` spec and 0 for a `J` spec. Observed
  by AC1, AC2 and AC5.
- **S3** — The joins at :2902-2952 run under `--staged`. The hold branch at :2902-2903 becomes the
  announce line in §4. Under `--staged` a reciprocity or order finding is reported when either end
  of its edge is a `P` spec. A no-payload or external-payload finding is reported when its own file
  is a `P` spec. In full mode every spec is `P`, so every finding is reported as before. Observed by
  AC1 and AC2.
- **S4** — Check 23 runs under `--staged`. The hold branch at :3335-3338 becomes the announce line in
  §4, and the guard at :3339 reads only `ACCEPTANCE_LEDGER_CUTOFF`. Under `--staged` its two listings
  (:3350 and :3390) keep only paths whose build slug is in `_SBUILD` (:775-786). The specs it grades
  are those whose file is staged, or whose H1 id a staged journal record's `**Evidences:**` line
  names. The three zero-population notices at :3547-3558 stay full-mode only. Observed by AC3, AC4
  and AC5.
- **S5** — The prose agrees. That means the script header at :19-21, the block comments at
  :2865-2869 and :3308-3334, the §3 Edges paragraph of `tools/memory-tree/SPEC-TEMPLATE.template.md`
  (:235-241) and its rendered copy `memory/TEMPLATE-SPEC.md`, and check 12's edges sentence of
  `tools/memory-tree/HYGIENE.template.md` (:322) and its rendered copy `memory/HYGIENE.md`. The
  acceptance-ledger section of both HYGIENE copies gains one bullet after :713. The text is in §4.
  Observed by AC6.
- **S6** — `tools/memory-tree/check-memory-hygiene.test.sh` gains one scratch-tree block that builds
  §4's fixture and asserts AC1 to AC4. Observed by AC1, AC2, AC3 and AC4, re-run by the arm in §7.

## 3. Non-goals (OUT)

- No change to any verdict of the full run (`STAGED=0`), which AC5 compares byte for byte.
- No other held check moves: 13-16, 17-19, 21, the row-grammar arm, 26, check 10 and the stale-line
  guard keep their holds.
- No cross-build ledger read under `--staged`. A record in build A that evidences a unit of build B
  is read only by the full run. Measured 2026-11-10 at `14320c98` (PINNED): 1210 `**Evidences:**`
  lines in tracked records, and none names a unit outside its own build folder.
- No new `fail` branch and no `ARMS_FLOORS` move. Every finding text exists today and is armed.
- No staged-blob reading. The script reads worktree content under `--staged` (:2007-2008), and the
  joins inherit that.
- No hand bump of `KIT_MEMORY_TREE_VERSION`. The lander's `mint` moves it (build README rule 4).
- No page under `help/`. `git grep -n staged -- help` names no hygiene page.

### Edges

none

## 4. Design

### Why the two holds were there, and what changes

The edge hold (:2902-2903) exists because `c12_sel` is the staged set under `--staged`, so the
unstaged end of a correct pair read as missing (the `TOOL-aJoinedCanon-8` spec audit, finding B2).
The cure is to read the other end, not to drop the join. Every edge payload names a sibling under
the same `builds/<slug>/spec/` prefix (`memory/TEMPLATE-SPEC.md:225-226`). So the staged spec's own
build folder is the whole population a join can need, and `FILES` already lists that folder under
`--staged` (:762-763, :789-790).

Check 23's hold (:3335-3338) exists for cost: the staged leg measured 963 s with the check and 54 s
with it held (:3313-3315, PINNED 2026-08-27). Scoping it to the staged build folders keeps the cost
to one build's records.

### The report rule

A finding is reported under `--staged` when the commit can have caused it.

| finding | reported when |
|---|---|
| reciprocity (`\003R`) | the declaring spec or its target is staged |
| order (`\003O`) | the declaring spec or its target is staged |
| no payload (`\003E`) | the declaring spec is staged |
| external payload names a sibling (`\003X`) | the declaring spec is staged |
| check 23, any arm | the unit's spec is staged, or a staged journal record evidences it |

"Either end" is what closes the measured cost. A spec that declares `hands-off` lands first and its
target lands later with no reciprocal. Only the second commit can red, and the finding names the
first file. A rule keyed on the declaring file alone stays silent there.

Check 23 grades whole units, not lines. A unit selected by one staged record is graded against every
record in its build folder, which is what the full run does for that unit. A unit the commit names
nowhere stays silent, as `check-memory-hygiene.test.sh:1640-1641` requires: a red is the committer's
own file, never another stream's debt.

### The awk change

The `J` record joins the driver stream beside `P` and `M` (:2119-2120). On a `J` record the awk reads
the body, takes `hdr` (:2143-2144) and returns silently if `hdr` fails the header pattern at :2145 or
carries `Tier-1`. Otherwise it computes `fdate` as :2156-2159 do, calls the edge function, and ends
the record. The function holds :2661-2721 verbatim apart from the two `stg == 0` guards and the new
last field. Its counters (`eg_has`, `eg_n`, `eg_none`, `eg_nb`, `eg_bad`) stay global, so the `P`
call site prints the shape findings from them unchanged.

The join awk at :2905 keeps a `staged[slug SUBSEP uid]` map from the U rows and an `estaged[k]` per E
row. Under `--staged` it tests the table above before each print, and in full mode the test is
skipped.

### Check 23 under `--staged`

1. The record stream at :3350 and the spec listing at :3390 each pass through one filter that keeps
   a path when its third segment is a key of `_SBUILD`. That is one awk per listing and no per-path
   process.
2. One awk over the staged paths in `STAGED_MD` under `<M>/builds/*/build/` or `reviews/` prints
   the id after each `**Evidences:**` line. These ids, space-joined, ride into the `alsel` awk
   (:3410) as `-v only=`, beside `-v sfiles=` for the staged spec paths and `-v stg=`. After the uid
   is read, a spec is skipped when `stg` is 1, its path is not in `sfiles` and its uid is not in
   `only`.
3. Every arm after that is unchanged. It reads `alU` and the L rows, so the selection decides the
   whole population.

### The announce lines

```text
memory-hygiene: the §3 edge JOINS grade each staged spec against its own build's specs as they stand in the worktree, and report an edge when either end of it is staged; the push-boundary run grades every edge
memory-hygiene: check 23 graded <N> unit(s) that a staged spec or journal record names, against the records of their own build folders; the push-boundary run grades every closed unit
```

`<N>` is `alpop`. A staged commit that names no closed unit prints 0, so an empty selection is
visible rather than read as a pass.

### The prose

`SPEC-TEMPLATE.template.md` :235-237 and the same lines of `memory/TEMPLATE-SPEC.md` become:

```text
**Three of the four arms are JOINS, and under `--staged` they read each staged spec's whole build**:
the staged spec is joined against its build's specs as they stand in the worktree, and an edge is
reported when either end of it is staged, so the commit that leaves a declared edge one-way is the
commit that reds. The shape arm reads one file and grades only the staged specs. A join whose
target is outside the graded
```

The rest of that paragraph stands. `HYGIENE.template.md` :322 and `memory/HYGIENE.md` :322 become:

```text
    runs under `--staged`; there the reciprocity, order and payload JOINS read each staged spec's
    whole build from the worktree and report an edge either of whose ends is staged.
```

Both HYGIENE copies gain this bullet after the one at :713:

```text
- Under `--staged` it grades the closed units a staged spec or a staged journal record names,
  against the records of their own build folders. A record in another build that evidences one of
  them is read only by the full run.
```

The script header at :19-21 names check 23 among the narrowed checks rather than the held ones, and
the two block comments say what the narrowing reads. The template and its live copy carry identical
text. The `kit/dogfood doc parity` leg at the close compares them.

### The fixture

A scratch git repository at `%TEMP%/pr4`, short because a long path breaks a clone on Windows. Its
conf:

```text
MEMORY_ROOT=memory
DISCIPLINES="architecture"
FAMILIES="architecture:ARCH"
SPEC_FORMAT_CUTOFF="2026-07-15"
SPEC_EDGES_CUTOFF="2026-09-08"
ACCEPTANCE_LEDGER_CUTOFF="2026-08-20"
LEDGER_LABEL_CUTOFF="2026-09-08"
```

Each spec is `memory/builds/tPair/spec/2026-11-10-spec-ARCH-tPair-<n>.md`. Its body is the ten
canonical headings, each followed by one line of `x`, under its H1 and header. §3 carries the
`### Edges` block from the table, and §9 carries `- rev-1 · 2026-11-10 · initial draft.`. A
CLOSED spec's §8 reads `none`, and its §6 numbers each criterion it carries as below.

```text
# ARCH-tPair-1 — fixture
**Status:** OPEN · rev-1 · 2026-11-10 · node a · Tier-2 · base 0123abcd · order 1

- **AC1** — `x` holds.
```

| spec | status | Edges | criteria | its ledger record, in `tPair/build/` |
|---|---|---|---|---|
| 1 | OPEN, order 1 | **hands-off** `ARCH-tPair-2` | — | — |
| 2 | OPEN, order 2 | none | — | — |
| 3 | CLOSED | none | AC1, AC2 | evidences AC1 only |
| 4 | OPEN | **hands-off** `ARCH-tPair-5` | — | — |
| 5 | OPEN | **consumes-from** `ARCH-tPair-4` | — | — |
| 6 | OPEN | **hands-off** `ARCH-tPair-7` | — | — |
| 7 | OPEN | none | — | — |
| 8 | OPEN | no `### Edges` block | — | — |
| 9 | CLOSED | none | AC1 | evidences AC1 and AC9 |
| 10 | CLOSED | none | AC1 | evidences AC1 and AC9 |

Each ledger record is `2026-11-10-build-ARCH-tPair-<n>-1-acceptance-ledger.md` and reads as below, with
one criterion line per criterion the table gives it. A second build, `tOther`, holds one such record
under `tOther/build/` that evidences `ARCH-tPair-9` with the single line for AC8.

```text
**Serves:** journal ARCH-tPair-9

**Evidences:** ARCH-tPair-9
- AC1 — `x` — seen.
- AC9 — `x` — seen.
```

Everything is committed with `--no-verify`. Each AC stages a one-line append, runs from the fixture
root, and resets.

### Inventory

| identifier | kind | where |
|---|---|---|
| `extract_edges` | awk function, the lexicon's `extract` verb | check 12's batched awk |
| `J` | driver-stream tag, beside `P` and `M` | the `c12_sel` stream |
| `staged`, `estaged` | awk arrays | the edge-join awk at :2905 |
| `only`, `sfiles` | awk `-v` variables | the `alsel` awk at :3410 |

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/TEMPLATE-SPEC.md`
- `memory/HYGIENE.md`

### Rollout

Unit 1 of this build may also edit both spec-template copies, at the DEFERRED sentence near
`memory/TEMPLATE-SPEC.md:114-116`. That shares a write set with S5, so this unit builds after unit 1
(order 4) and rebases on its text. The pre-commit hook calls `--staged` unchanged
(`.githooks/pre-commit:226-231`), so adopters receive the narrowing with the kit's next minted
version and no conf key.

### Alternatives rejected

- **Grade the staged set alone.** That is the B2 defect the hold was written to stop: the unstaged
  end of a correct pair reads as missing.
- **Grade the whole build folder for every finding.** A commit touching dSafePassage's folder would
  red on any unit's standing debt there. The suite at `check-memory-hygiene.test.sh:1640-1641`
  forbids that.
- **Read the corpus for check 23's ledger side.** That is the 16-minute cost the hold exists for, and
  it buys only the cross-build case, which measures 0 of 1210.
- **Parse edges with `read_spec_edges` in `tools/memory-tree/design_lib.py`.** That would add a
  Python process to the leg and put a second edge reader in the gate, beside the awk that already
  parses edges for the full run.

## 5. Production-readiness checklist

- security — N/A — the leg reads tracked files in the worktree and writes nothing; no new input
  crosses a trust boundary.
- perf / scale — the edge side adds one body read per spec in the staged builds, inside the existing
  awk. Check 23 adds one awk per listing plus one over the staged records. dSafePassage, the largest
  build at 631 tracked files (PINNED 2026-11-10), bounds the record stream.
- error / empty / loading states — a staged commit naming no closed unit announces 0 graded units. A
  `J` spec whose header does not parse is silent, because its own shape is the full run's to grade.
- observability — both announce lines print on every `--staged` run with a cutoff set.
- risks — a regression in the full run, which AC5 compares byte for byte; a sibling's shape finding
  leaking into a staged run, which AC2 observes.
- testing — AC1 to AC6, with the scratch-tree block in the suite declared in §7.
- migration — none: no conf key, no record and no hook changes.
- user docs — both HYGIENE copies and both spec-template copies (S5); no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When only `2026-11-10-spec-ARCH-tPair-2.md` is staged in §4's fixture and
  `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs, the output carries
  a `HYGIENE check 12` line opening `2026-11-10-spec-ARCH-tPair-1.md (§3 declares **hands-off**` that
  names `ARCH-tPair-2` and `declares no matching **consumes-from**`. Run again with only spec 1
  staged, it carries the same line.
  Red when: the joins stay held under `--staged`, or a finding is reported only when its declaring
  file is staged, which makes the first run silent.
- **AC2** — When only specs 2 and 5 are staged and
  `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs, the output names no `ARCH-tPair-4`
  or `ARCH-tPair-5` edge, no `2026-11-10-spec-ARCH-tPair-6.md (` and no
  `2026-11-10-spec-ARCH-tPair-8.md (`. It carries the first announce line of §4 and not
  `the §3 edge JOINS are held under --staged`.
  Red when: a `J` sibling reports its own shape finding, a join finding neither end of which is
  staged is reported, or the conforming pair 4 and 5 reds because spec 4 was not read.
- **AC3** — When only spec 3 is staged and `bash tools/memory-tree/check-memory-hygiene.sh --staged`
  runs, the output carries `ARCH-tPair-3/AC2` in the `HYGIENE check 23` line that opens
  `a CLOSED unit numbers an acceptance criterion that no journal record evidences`. With only
  spec 9's ledger record staged, it carries `ARCH-tPair-9/AC9` in the line that opens
  `a journal record evidences a criterion label its own spec does not number`.
  Red when: check 23 stays held, or a unit named only by a staged record is not selected.
- **AC4** — In the two runs of AC3 the output names neither `ARCH-tPair-10/AC9` nor
  `ARCH-tPair-9/AC8`, carries no `check 23 HELD under --staged`, and carries the second announce line
  of §4 with `graded 1 unit(s)`.
  Red when: the unit filter is missing and the unstaged unit 10 reds, or the record stream reads
  past `_SBUILD` and the `tOther` record's AC8 reds.
- **AC5** — When the fixture has nothing staged and `bash tools/memory-tree/check-memory-hygiene.sh`
  runs in full from this unit's tip and from a clone of `ae6735c1` at `%TEMP%/pr4b`, the two outputs
  are identical once each run's own repository path is replaced by one fixed token (`diff` prints
  nothing). Both name the one-way edges of specs 1 and 6, spec 8's missing Edges block, and
  `ARCH-tPair-3/AC2`, `ARCH-tPair-9/AC8`, `ARCH-tPair-9/AC9` and `ARCH-tPair-10/AC9`.
  Red when: the new last field on the E and U records shifts a column the join awk reads, or a
  full-mode notice moves.
- **AC6** — When `grep -cF 'are JOINS and are HELD'` runs over `memory/TEMPLATE-SPEC.md` and
  `tools/memory-tree/SPEC-TEMPLATE.template.md`, and `grep -cF 'JOINS are held there'` over
  `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`, each prints 0. The §4 replacement
  sentences are present in all four, and `grep -nF '23 and 26'` over
  `tools/memory-tree/check-memory-hygiene.sh` prints nothing.
  Red when: one copy keeps the held prose, or the header still lists check 23 as held.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `check-arms selftest` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh (in the `memory-hygiene self-test` leg) · covers AC1 AC2 AC3 AC4 · the scratch-tree block of S6, staged red by restoring the two holds at :2902 and :3335 · none

`policy fixtures` is owed by its exact guard on `tools/memory-tree/check-memory-hygiene.sh`, and the
doc-parity and recall-floor legs by their guards on the two `memory/` copies. Every other leg the
estimate trips is broad.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.

## 10. Reuse audit

The seam is the `--staged` selection in `tools/memory-tree/check-memory-hygiene.sh`: `STAGED_SET`,
`_SBUILD` and `in_scope` (:759-800). This unit extends it with the check-12 batched awk's existing
edge records (:2661-2721) and check 23's single-pass streams (:3350, :3410). No second reader is
built. `tools/codebase-map/reuse_lookup.py`, asked "grade edge reciprocity and acceptance ledger
joins for staged files in the pre-commit hygiene leg", returned name-stem neighbours only (`pre`,
`legs`, `cmd_staged`, `write_staged`) and one parser, `read_spec_edges` in
`tools/memory-tree/design_lib.py`, rejected in §4. Recall found no record ruling against the
narrowing. `TOOL-aJoinedCanon-8`'s S13 and its round-1 finding B2 hold the joins for the
partial-pair reason this unit's sibling read answers, and `TOOL-aTrimmedHook-2`'s N2 kept the holds
as a non-goal of that build, not a ruling.

Recall terms used: staged held edge joins reciprocity ledger check 23 pre-commit narrowed build
folder push-boundary. The full invocation:

```bash
python tools/memory-recall/query.py "why are the edge joins and the acceptance ledger check held under --staged, and was narrowing them to the staged set ever ruled out" --terms "staged held edge joins reciprocity ledger check 23 pre-commit narrowed build folder push-boundary"
```
