# TOOL-dTotalRecall-92 — the round-8 minors: each reading of units 77 to 88 that miscounted, misplaced or went unrecorded is made once at the tip, and each record it decides is written once

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 39 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-89 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 77 to 88
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md`)
exited CONVERGED with 27 confirmed findings. Its three high ids are units 89 to 91: id 1 is
`TOOL-dTotalRecall-89`, id 22 `TOOL-dTotalRecall-90` and id 23 `TOOL-dTotalRecall-91`. This unit is
the batch BUILD-METHOD M4 makes of the rest:

- the 17 MEDIUM findings, ids 2, 3, 5, 6, 10, 11, 12, 13, 16, 17, 18, 19, 20, 24, 25, 26 and 27
  (items M1 to M15);
- the 7 LOW findings, ids 7, 8, 9, 14, 15, 21 and 28 (items L1 to L7).

Each id keeps its own scope item. Ids 2, 11 and 25 share item M1, and each takes its own facet of it.
Id 10 (M5) is one defect with id 22 (H2), and ids 26 (M14) and 7 (L1), and 16 (M8) and 21 (L6), are
pairs the report grades apart; each takes its half below. The minors land on units 77 to 88, so this
unit repairs none in particular and builds after every unit: order 39, above the 38 unit 89 holds.
The review record holds each item's text.

## 2. Scope (IN)

Every item states its change to the unit it lands on, as that unit was built. A spec is frozen once
its unit builds; a reading made wrongly is made again here, and a departure is a deviation record.
Every revision read goes through `TOOL-dTotalRecall-81`'s `pass_of` and `read_at`, or this unit's
corrected `read_at` where S24 says so. Every record is written by `TOOL-dTotalRecall-90` §4's recipe,
its Evidence carrying the token `audit-77 id <report id>`, only where `has_deviation` prints 0 for its
unit and token. A correcting record names the record it corrects in `**Supersedes:**`. "The tip scan"
is §4's.

- **S1** — id 2 (M1). Unit 81's S3 case: `pass_of 67` at this pass's base prints a sha, the resolving
  input S3 relies on, set in the ledger beside unit 81's AC1 answer for its fourth input. Observed by
  AC1.
- **S2** — id 11 (M1). Unit 81's AC1 fourth input, `pass_of 67` "before unit 67's pass", cannot be
  produced at its base, and its §4 pin's reason was true only at `af814dba8`. A deviation record of
  `TOOL-dTotalRecall-81` names the input as unobservable at order 22 and `pass_of 999`, an id off the
  roster, as its replacement, with the date and sha this pass measured it at. Observed by AC2.
- **S3** — id 25 (M1). The no-pass-commit red branch every later `$(pass_of N)` rests on is seen red:
  `pass_of 999` prints `red 999 no pass commit` and returns 1 at this pass's base. Observed by AC3.
- **S4** — id 3 (M2). Unit 79's liveness is isolated: §4's span derivation is fed unit 78's sweep, a
  closing `sep rc=0` line, then unit 77's two `live` lines, so a span still open at the last swept unit
  is closed before the liveness opens its own. Where unit 79's AC1 answer folded `live` into a real
  span, a deviation record of `TOOL-dTotalRecall-79` names it. Observed by AC4.
- **S5** — id 5 (M3). Unit 79's AC3 tip read is recorded: the main loop runs `read_checker` in a
  `gate-mc92` worktree of `pass_of 79` with the label `p79` and records it under a `Pass: none` commit
  before this pass. Where it prints a non-zero status, or unit 79's AC3 answer rests on the read taken before its
  own remedy, a deviation record of `TOOL-dTotalRecall-79` names it. Observed by AC5.
- **S6** — id 6 (M4). Unit 87's plant on the fixture base `TOOL-dTotalRecall-88` S15 built: the plant
  `kept-home-trailing-root` prints a compare line naming a base sha. The ledger sets it beside unit
  87's AC2 answer at order 34; where that answer was red on the compare, or green through a remote its
  spec does not state, a deviation record of `TOOL-dTotalRecall-87` names it. Observed by AC6.
- **S7** — id 10 (M5). An unresolved pass in the re-read form prints a `red` line:
  `s1 s1-999 999 '' 57` (`TOOL-dTotalRecall-90` §4) prints `s1-999 red 999 no pass commit`. The
  ledger names, for each of units 82, 83 and 84 whose AC1 line recorded an empty S1, the cause unit
  90's labelled line gives. Observed by AC7.
- **S8** — id 12 (M6). Every deviation record under the build folder carries all eleven REQUIRED
  fields, a Risk in `RISKS` and a Follow-through in the `FOLLOW` grammar: the tip scan prints no
  `malformed` line. A record that does gets a correcting record carrying every field. Observed by AC8.
- **S9** — id 13 (M7). Unit 78's sweep cost is pinned and its record is complete. The main loop times
  one add, `read_checker` and remove at this pass's base and records the figure. Where unit 78's block
  holds fewer verdict lines than its `population` value, the main loop sweeps the missing units by §4's
  resumable form and records their lines. Observed by AC9.
  permission: the checker is the `kickoff-manifest ratchet` leg's argv, which no role agent may run
  (`.claude/roles.json`); the main loop runs it and records the output under a `Pass: none` commit.
  **Readers:** by name: no name retires, the item removing only the scratch worktree it added for the
  timing and the sweep, whose path is spelled by `add_scratch_worktree` and `remove_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`, `:63`) and their callers `tools/run-gates/post-merge.sh`,
  `tools/run-gates/run-gates.sh` and `tools/run-gates/run-selftests.sh`
  · by value: `check_pockets`, minted by `TOOL-dTotalRecall-18`, which reds a common-directory entry
  no witness row names; the `gate-ledger` pocket row covers this item's `gate-mc92`, as S13 states.
- **S10** — id 16 (M8). Unit 87 §4's precedent sentence is corrected by a deviation record of
  `TOOL-dTotalRecall-87`, Hand-off `spec-revised`, Risk `editorial`. Its Before is the sentence. Its
  After states that `tools/runlog/runlog_lib.py:393` refuses any backslash or `:`, and that unit 87's
  resolver folds `\` and refuses a leading drive only, a deliberate divergence agreeing with the
  memory-tree kit's own reader at `tools/memory-tree/design_lib.py:680`. No criterion asks the two
  resolvers to agree. Observed by AC10.
- **S11** — id 17 (M9). A record a pass of this build took out of the tree is put back as it stood
  before that commit, by `git checkout <commit>^ -- <path>`, with any record that commit appended to.
  The duplicate pair is then made one by a correcting record whose `**Supersedes:**` names the later
  and whose Evidence names its path and not `pass(59)`. Nothing is edited by hand. Observed by AC11.
  **Readers:** by name: no name retires, the item putting back record files whose names are read
  through the glob of `deviation_join.read_records` (`tools/memory-tree/deviation_join.py:278`)
  · by value: `deviation_join.read_records` and `has_deviation`, which count each restored record and
  read the correcting record's `**Supersedes:**` relation.
- **S12** — id 18 (M10). After unit 88's close-rule sentence lands, the README's `## Build-level rules`
  slot measures at most 1800 B by `gen_build_index.measure_slot_sizes`, holds seven bullets, and its
  fourth bullet, the close, carries `last-body-change`. Where it does not, the sentence moves into
  the fourth bullet and is shortened to fit, the step kept whole. Observed by AC12.
- **S13** — id 19 (M11). No scratch worktree of units 77, 78 or 80 outlives the build: at the tip no
  entry of the git common directory starts `mc`, and `git worktree list --porcelain` names none. This
  unit's own worktree is `gate-mc92`, which the `gate-ledger` pocket row of `TOOL-dTotalRecall-18`
  covers. The ledger corrects the Readers lines of unit 77 S2, unit 78 S3 and unit 80's reads:
  `check_pockets` is a value reader of those paths. Observed by AC13.
  **Readers:** by name: no name retires, the item clearing only scratch worktrees whose paths are
  spelled by `add_scratch_worktree` and `remove_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`, `:63`) · by value: `check_pockets`, minted by
  `TOOL-dTotalRecall-18`, which reds a common-directory entry no witness row names.
- **S14** — id 20 (M12). No write-once decision of units 79 to 88 rests on a file that is not a
  record. The tip scan's `quoted` lines name every non-record file an unanchored grep for a record's
  Serves token lists. Where a unit's ledger names such a file as the record that made a write
  needless, the owed record is written. Observed by AC14.
- **S15** — id 24 (M13). No record is left written and uncommitted: the tip scan prints no
  `untracked` line at this pass's tip. One found at this pass's base, from an interrupted pass, is
  committed where it is the only record of its departure, and is named in the ledger and left out of
  the tree where a committed record already names it. Observed by AC15.
- **S16** — id 26 (M14). Two records of one build never share an `<n>`: the tip scan prints no
  `shared-n` line. The ledger states the mechanism: the driver dispatches strictly in sequence inside
  one order value (`tools/workflows/unattended-build.js:76-80`), so the door's next free `<n>` is read
  after the previous pass's commit. Observed by AC16.
- **S17** — id 27 (M15). §4's span derivation reads unit 78's `population` line and exits 1 with a
  `red population` line where the distinct swept units differ from it, and prints `red unplaced` for
  any non-blank line it cannot place. Where unit 79's spans were derived from a block this check
  reds, a deviation record of `TOOL-dTotalRecall-79` names it. Observed by AC17.
- **S18** — id 7 (L1). The ledger corrects unit 83 §4 "Why order 35": unit 84 also writes a record of
  unit 74, for its `s1-46` departure. The tip scan's `by` lines for unit 74 caused by unit 83 and by
  unit 84 each count at most one. Observed by AC18.
- **S19** — id 8 (L2). Unit 88's AC3 is run with its carriers proven present:
  `git ls-files --error-unmatch` on `kit.toml` and the three `legacy_ledger.py` copies, then the
  `absorbs` greps. An untracked carrier is a red, named with its path. Observed by AC19.
- **S20** — id 9 (L3). Unit 88's AC5 and AC19 are made able to fail: AC5 is read as `last-body-change`
  inside the fourth bullet of the rules slot, which the generated unit row cannot satisfy, and AC19's
  counts over specs 74 and 76 are compared with the values this spec pins, 5 and 1. Observed by AC20.
- **S21** — id 14 (L4). The ledger corrects unit 88's AC15 citation: the call shape is
  `tempfile.TemporaryDirectory(prefix='kg')`, and `tools/govkit/govkit.py:5229`, whose prefix is ten
  characters, is cited only as the tree's one prefixed call. Observed by AC21.
- **S22** — id 15 (L5). The written-once key is computed: the tip scan groups the live records by
  address, Before and After and prints a `dup` line for any group of two or more. Each such pair is
  made one by a correcting record. Observed by AC22.
- **S23** — id 21 (L6). `tree_lib.resolve_memory_root`'s docstring states its divergence from
  `tools/runlog/runlog_lib.py:393` and names the third definition of the name at
  `tools/memory-recall/selftest.py:112`. The ledger hands the three definitions to the close's
  left-shift step. Observed by AC23.
- **S24** — id 28 (L7). `read_at` normalises each needle as it normalises the body, and refuses a
  strings file holding no needle with a red line. §4's needle scan shows no strings block in this
  build's specs holds a whitespace run or no needle; a block that does is read again by the corrected
  `read_at` and recorded. Observed by AC24.

## 3. Non-goals (OUT)

- The high ids: units 89 to 91.
- Editing any spec of units 77 to 88, frozen once each builds, as §2's opening states.
- The spec lints and checklist entries the report suggests as left-shift gates: the close's
  left-shift step (BUILD-METHOD M8). S23 hands it the shared memory-root reader's three definitions.
- Re-deriving unit 88's AC13 over the records of unit 59: `TOOL-dTotalRecall-89`.

### Edges

- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door every record of this unit is written through (ids 2, 3, 5, 6, 11, 12, 15, 16, 17, 27)
- **consumes-from** `TOOL-dTotalRecall-77` — `read_checker` and the `mc77` worktree path (ids 5, 13, 19)
- **consumes-from** `TOOL-dTotalRecall-78` — the sweep's block, its `population` line and the `mc78` worktree path (ids 3, 13, 19, 27)
- **consumes-from** `TOOL-dTotalRecall-79` — its span derivation, its AC1 and AC3 answers and its remedy (ids 3, 5, 27)
- **consumes-from** `TOOL-dTotalRecall-80` — the `mc80` worktree path and its Readers line (id 19)
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, `read_at`, its AC1 and S3 and its pin (ids 2, 11, 25, 28)
- **consumes-from** `TOOL-dTotalRecall-82` — its AC1 line and its write-once guard (ids 10, 12, 20, 24)
- **consumes-from** `TOOL-dTotalRecall-83` — its AC1 line, its order paragraph and its records of units 59 and 74 (ids 7, 10, 12, 20, 24, 26)
- **consumes-from** `TOOL-dTotalRecall-84` — its AC1 line and its record of unit 74 (ids 7, 10, 12, 20, 24, 26)
- **consumes-from** `TOOL-dTotalRecall-85` — its records and its write-once guard (ids 12, 15, 24, 26)
- **consumes-from** `TOOL-dTotalRecall-86` — its records and its write-once guard (ids 12, 15, 20, 24, 26)
- **consumes-from** `TOOL-dTotalRecall-87` — its plant `kept-home-trailing-root`, its AC2 answer, its §4 precedent and `resolve_memory_root` (ids 6, 16, 21)
- **consumes-from** `TOOL-dTotalRecall-88` — its fixture base, its S8 sentence, its S19 merge and its AC3, AC5, AC15 and AC19 (ids 6, 8, 9, 14, 17, 18)
- **consumes-from** `TOOL-dTotalRecall-90` — `s1`, `has_deviation` and the record recipe (ids 10, 12, 15, 20, 24)
- **consumes-from** `TOOL-dTotalRecall-93` — the re-keyed `has_deviation` and `unit_of`, by which this batch's guards count and its tip scan groups its `by` and `dup` lines in place of the Departs from address (the round-1 audit of units 89 to 92, id 1)
- **hands-off** `TOOL-dTotalRecall-98` — its restore listing and its AC11 answer, which that unit lists again with rename detection off (the round-1 audit of units 89 to 92, id 15)
- **hands-off** `TOOL-dTotalRecall-99` — its tip scan and its tip criteria, which that unit witnesses and grades again (the round-1 audit of units 89 to 92, id 29)
- **hands-off** `TOOL-dTotalRecall-100` — its S8, S11 and S22 records, its sweep, its needle scan and its span script, which that batch makes again at the tip (the round-1 audit of units 89 to 92, ids 3, 4, 9, 10, 23, 24, 25, 32)

## 4. Design

### How the batch builds

One pass, after every other unit is terminal, in this order:

1. The main loop's recordings of S5 and S9, under `Pass: none` commits, before the pass starts.
2. The read-only items: S1, S3, S7, S16, S18, S19, S20 and S24's scan, then S4 and S17 over unit 78's
   block, and the tip scan at this pass's base.
3. The tree items: S11's restore, S12's README rule, S13's worktree clearing and S23's docstring.
4. The records: S2, S4, S5, S6, S10, S11, S14, S15, S17 and S22, each through the door.
5. The tip scan again over the pass's own records, last.

### The tip scan

```bash
# run from the repository root; prints nothing on a clean folder
python - memory/builds/dTotalRecall/build <<'SCAN'
import collections, glob, os, pathlib, subprocess, sys
sys.path.insert(0, 'tools/memory-tree')
import deviation_join
folder = sys.argv[1]
paths = sorted(p.replace(os.sep, '/') for p in glob.glob(os.path.join(folder, '*-deviation-*.md')))
tracked = set(subprocess.run(['git', 'ls-files', '--', folder], capture_output=True, text=True).stdout.split())
recs = [deviation_join.read_record(p, pathlib.Path(p).read_text(encoding='utf-8')) for p in paths]
seen = collections.Counter(r['n'] for r in recs if r['n'] is not None)
for r in recs:
    for field, why in r['malformed']:
        print('malformed', r['path'], field, why)
    if r['n'] is not None and seen[r['n']] > 1:
        print('shared-n', r['path'], r['n'])
    if r['path'] not in tracked:
        print('untracked', r['path'])
gone = {r['supersedes'] for r in recs if r['supersedes']}
live = [r for r in recs if r['id'] not in gone]
key = collections.defaultdict(list)
for r in live:
    key[(r['address'], r['before'], r['after'])].append(r['path'])
for ps in key.values():
    if len(ps) > 1:
        print('dup', *ps)
by = collections.Counter((r['address'].split('@')[0], (r['caused_by'] or '').strip('`')) for r in live)
for (u, c), n in sorted(by.items()):
    print('by', u, c, n)
for q in subprocess.run(['git', 'grep', '-l', 'deviation TOOL-dTotalRecall-', '--', folder],
                        capture_output=True, text=True).stdout.split():
    if q not in paths:
        print('quoted', q)
SCAN
```

Only `by` lines print on a clean folder. PINNED, measured 2026-10-26 at `1e255b0c6`: over the build
folder's 8 records it printed eight `by` lines, each a count of 1, and no other line.

### The span derivation, corrected

Unit 79 §4's script, with three changes: blank and fence lines are skipped, the `population` line is
read, and an unplaced line is a red. Units labelled `sep` and `live` are not swept units.

```bash
# SWEEP holds unit 78's fenced block; LIVE holds `sep rc=0` and unit 77's two live lines
python - "$SCRATCH/spans-in.txt" <<'SPANS'
import re, sys
order, rc, checks, pop, bad = [], {}, {}, None, []
for raw in open(sys.argv[1], encoding='utf-8'):
    line = raw.strip()
    if not line or line.startswith('```'):
        continue
    m = re.match(r'^population (\d+)$', line)
    if m:
        pop = int(m.group(1)); continue
    m = re.match(r'^(\S+)(?: [0-9a-f]{40})? rc=(\d+)$', line)
    if m:
        order.append(m.group(1)); rc[m.group(1)] = int(m.group(2)); continue
    m = re.match(r'^(\S+)(?: [0-9a-f]{40})? MANIFEST check (\d+) FAILED', line)
    if m:
        checks.setdefault(m.group(1), set()).add(m.group(2)); continue
    m = re.match(r'^(\S+) red ', line)
    if m:
        order.append(m.group(1)); rc[m.group(1)] = None; continue
    bad.append(line)
for line in bad:
    print('red unplaced', line)
swept = {u for u in order if u not in ('sep', 'live')}
if pop is None or len(swept) != pop:
    print('red population', pop, 'read', len(swept))
if bad or pop is None or len(swept) != pop:
    sys.exit(1)
spans, cur = [], None
for u in order:
    if rc[u] is None:
        print('unresolved', u)
    elif rc[u]:
        cur = cur or [u, u, set()]
        cur[1] = u
        cur[2] |= checks.get(u, set())
    elif cur:
        spans.append(cur + [u]); cur = None
if cur:
    spans.append(cur + [None])
for first, last, cks, closer in spans:
    print('span', first, last, 'checks', ','.join(sorted(cks)) or 'none-printed', 'closed-by', closer or 'OPEN')
print('spans', len(spans))
SPANS
```

It runs twice, over `$SWEEP` with `$LIVE` appended and over `$SWEEP` alone. PINNED, measured
2026-10-26 over a sample whose last swept unit, 84, is red with check 5 and whose `population` is 2:
with the liveness it printed `span 84 84 checks 5 closed-by sep`,
`span live live checks 9 closed-by OPEN` and `spans 2`; alone, `span 84 84 checks 5 closed-by OPEN` and `spans 1`. With one verdict line
deleted it printed `red population 2 read 1` and exited 1, and with `rc=1` garbled to `rc = 1` it also
printed `red unplaced` with that line.

### The read, corrected

Unit 81 §4's `read_at` with its needles read before the body is counted:

```python
needles = [n for n in (re.sub(r'\s+', ' ', l).strip() for l in open(sys.argv[1], encoding='utf-8')) if n]
if not needles:
    raise OSError('no needle in %s' % sys.argv[1])
```

That block sits inside the `try`, so an empty strings file is a red line and exit 1. PINNED, measured
2026-10-26: the needles `is  absent` and `is absent` each printed 2 over spec 59 at `653bed738`, and an
empty file and a file of blank lines each printed `red no needle in <path>` and exited 1.

### The needle scan

```bash
python - memory/builds/dTotalRecall/spec/*.md <<'NEEDLES'
import re, sys
blocks = 0
for p in sys.argv[1:]:
    lines = open(p, encoding='utf-8').read().split('\n')
    i = 0
    while i < len(lines):
        if re.search(r"<<'STRINGS'\s*$", lines[i]):
            j, body = i + 1, []
            while j < len(lines) and lines[j].strip() != 'STRINGS':
                body.append(lines[j]); j += 1
            blocks += 1
            if not any(b.strip() for b in body):
                print('empty', p, i + 1)
            for b in body:
                if re.search(r'\S\s{2,}\S|\t', b.strip()):
                    print('run', p, repr(b))
            i = j
        i += 1
print('blocks', blocks)
NEEDLES
```

PINNED, measured 2026-10-26 at `1e255b0c6` with specs 89 to 92 written: it printed `blocks 8` and no
other line.

### The sweep's completion

Unit 78's loop, with the worktree made once and moved per unit, each unit's lines written to its own
scratch file so a killed run resumes at the first unit with no file:

```bash
W="$(git rev-parse --git-common-dir)/gate-mc92"
add_scratch_worktree "$W" HEAD || echo "gate-mc92 red worktree-add-failed"
for N in $MISSING; do
  [ -s "$SCRATCH/sweep92-$N.txt" ] && continue
  { P=$(pass_of "$N") || { echo "$N $P"; continue; }
    git -C "$W" checkout --quiet --detach "$P" || { echo "$N red checkout-failed $P"; continue; }
    read_checker "$W" "$N $P"; } > "$SCRATCH/sweep92-$N.txt"
done
remove_scratch_worktree "$W" || echo "gate-mc92 red orphan $W"
```

`$MISSING` is the population units with no verdict line in unit 78's block. The main loop runs it in
the background and records the files' lines.

### The restore

```bash
git log --diff-filter=D --format='%H' --name-only 462d20f3..HEAD -- 'memory/builds/dTotalRecall/build/*-deviation-*.md'
```

Each path it lists under commit `C` is checked out from `C^`, with every record `C` modified, which
`git diff --name-only --diff-filter=M "C^" "C" -- <the same pathspec>` lists.

### The rules slot

The sentence unit 88's S8 adds sits inside the fourth bullet, so no later rule renumbers and the
packet's "README rule 7" keeps its meaning. PINNED, measured 2026-10-26 at `1e255b0c6` by
`measure_slot_sizes`: `## Build-level rules` at 1540 B of its 1800 B ceiling, seven bullets.

### The docstring

`tree_lib.resolve_memory_root` gains one paragraph naming `runlog_lib.resolve_memory_root`
(`tools/runlog/runlog_lib.py:393`), which refuses any backslash or `:`, and the `memory-recall`
selftest's definition (`tools/memory-recall/selftest.py:112`), with the reason this one folds `\`.

### Why order 39

Unit 89 holds 38, after unit 88 at 37. Every item reads a landed unit or its records, so this unit
builds last.

### Inventory

Minted: nothing in code beyond one docstring paragraph; deviation records where §2's reads are red;
correcting records where the tip scan finds a malformed or duplicated record; at most one moved
README sentence. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (the records, the restored records and this unit's ledger)
- `memory/builds/dTotalRecall/README.md` (only where S12 moves the sentence)
- `tools/memory-tree/tree_lib.py` (S23's docstring)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Two batches.** Every item but S12 and S23 writes deviation records, whose `<n>` the door mints from
  the folder; two concurrent writers are the collision S16 rules out, so BUILD-METHOD M6's clause 1
  keeps them one unit.
- **Keep unit 88's hand merge and record it as an exception (id 17).** The report's alternative. It
  leaves a record out of the tree, and a deviation record is evidence of what a pass did.
- **Edit the specs of units 79, 81, 83, 87 and 88 by rev bump.** Each is frozen once its unit builds,
  and each builds before order 39.

## 5. Production-readiness checklist

- security — no new write surface; S11 restores files the door wrote.
- perf / scale — the tip scan and the span derivation read about a hundred lines each; S9 adds one
  timed iteration and a sweep only of missing units.
- error / empty / loading states — an unresolved pass is a labelled red line; a population mismatch
  and an unplaced line each exit 1; an empty strings file is a red.
- observability — every red names its read; the ledger sets each value beside the landed unit's own.
- risks — S11 restores a file a pass took out; the restored bytes are git's, never retyped.
- testing — AC1 to AC24 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `pass_of 67` runs at this pass's base, it prints a 40-hex sha, and the ledger's AC1
  line sets it beside unit 81's AC1 answer for its fourth input.
  Red when: the resolving case is read as a red.
- **AC2** — When `has_deviation memory/builds/dTotalRecall/build 81 'audit-77 id 11'` runs after the
  pass, it prints 1, and that record names `pass_of 999` with the sha it was measured at.
  Red when: the stale pin stands with no record.
- **AC3** — When `pass_of 999` runs at this pass's base, it prints `red 999 no pass commit` and
  returns 1.
  Red when: it prints a sha or nothing.
- **AC4** — When §4's span derivation runs over unit 78's block with `$LIVE` appended, its last span
  line is `span live live checks 9 closed-by OPEN`, and its `spans` value is one more than the run
  without `$LIVE`.
  Red when: `live` joins a real span, or the two runs differ by other than one span.
- **AC5** — When the ledger's AC5 line is read, it quotes the main loop's `p79 rc=` line, and
  `has_deviation memory/builds/dTotalRecall/build 79 'audit-77 id 5'` prints 1 where that status is
  non-zero or unit 79's AC3 answer predates its remedy, else 0.
  Red when: unit 79's AC3 stands on a read nobody recorded.
  permission: as S9's; the main loop records the read before this pass.
- **AC6** — When `python record_causes.py --fixture --plant kept-home-trailing-root` runs from
  `tools/memory-tree/`, its compare line names a base sha, and the ledger sets it beside unit 87's AC2
  answer.
  Red when: the compare reads a first seed.
- **AC7** — When `s1 s1-999 999 '' 57 "$SCRATCH/s82.txt"` runs, it prints
  `s1-999 red 999 no pass commit`, and the ledger's AC7 line names a cause for each empty S1 of units
  82 to 84.
  Red when: an unresolved pass prints nothing.
- **AC8** — When §4's tip scan runs at the pass tip, it prints no `malformed` line.
  Red when: a record lacks a REQUIRED field or carries a value outside its grammar.
- **AC9** — When the ledger's AC9 line is read, it quotes the figure the main loop timed over one
  `add_scratch_worktree`, `read_checker` and `remove_scratch_worktree` at this pass's base, and the
  verdict lines of unit 78's block and of S9's completion, each unit's scratch file of §4's sweep,
  together lead each population unit once.
  Red when: a population unit has no verdict line, or the cost is stated unmeasured.
  cost: one timed iteration, plus one checker run per missing unit.
  permission: as S9's.
- **AC10** — When `has_deviation memory/builds/dTotalRecall/build 87 'audit-77 id 16'` runs after the
  pass, it prints 1, and that record's After names `runlog_lib.py:393` and `design_lib.py:680`.
  Red when: unit 87's precedent sentence stands uncorrected.
- **AC11** — When §4's restore listing runs at the pass tip, every path it prints exists in the tree,
  and the tip scan prints no `dup` line naming a record of unit 59.
  Red when: a record a pass took out stays out, or a duplicate is made one by hand.
- **AC12** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import gen_build_index as g; print([x for x in g.measure_slot_sizes(open(sys.argv[1], encoding='utf-8').read()) if 'Build-level' in x[0]])"`
  runs at the pass tip with the build README as its argument, it prints a size at or under 1800, and the slot's fourth of seven bullets
  holds `last-body-change`.
  Red when: the slot exceeds its ceiling or a rule renumbers.
  figure: 1540 B is PINNED in §4; the tip's size is DERIVED.
- **AC13** — When `ls "$(git rev-parse --git-common-dir)"` and `git worktree list --porcelain` run at
  the pass tip, no entry starts `mc` and no worktree path ends `/mc77`, `/mc78` or `/mc80`.
  Red when: a sweep's orphan is still registered or on disk.
- **AC14** — When the ledger's AC14 line is read, it lists every `quoted` line of the tip scan, and
  every record a unit of 79 to 88 skipped as already written is a `*-deviation-*.md` file.
  Red when: a write was skipped on a ledger's quotation.
- **AC15** — When §4's tip scan runs at the pass tip, it prints no `untracked` line.
  Red when: a record is written and not committed.
- **AC16** — When §4's tip scan runs at the pass tip, it prints no `shared-n` line, and the ledger's
  AC16 line cites `tools/workflows/unattended-build.js:76-80`.
  Red when: two records share an `<n>`.
- **AC17** — When §4's span derivation runs over unit 78's block with one verdict line deleted, it
  prints `red population` and exits 1, and over the block whole it exits 0.
  Red when: a lost line leaves the spans silently.
- **AC18** — When §4's tip scan runs at the pass tip, its `by` lines for `TOOL-dTotalRecall-74` caused
  by `TOOL-dTotalRecall-83` and by `TOOL-dTotalRecall-84` each print at most 1.
  Red when: one unit's departure of unit 74 is recorded twice.
- **AC19** — When `git ls-files --error-unmatch kit.toml legacy_ledger.py` runs from
  `tools/memory-tree/`, and `git ls-files --error-unmatch legacy_ledger.py` from `tools/lib/` and from
  `tools/gate-lint/`, each exits 0 at the pass tip, and each of unit 88's AC3 greps then prints
  nothing.
  Red when: a carrier is untracked and the grep reads green over it.
- **AC20** — When the rules slot's fourth bullet is read, it holds `last-body-change`, and unit 88's
  AC19 python prints 5 over spec 74 and 1 over spec 76.
  Red when: either criterion passes on text unit 88 did not write.
  figure: 5 and 1 are PINNED, measured 2026-10-26 at `1e255b0c6`.
- **AC21** — When unit 88's AC15 python runs from `tools/memory-tree/`, every prefix it prints is at
  most 4, and the ledger's AC21 line cites `tempfile.TemporaryDirectory(prefix='kg')`.
  Red when: the ledger cites a prefix longer than the rule as the idiom.
- **AC22** — When §4's tip scan runs over a scratch folder holding two records of one unit with equal
  Before and After whose Evidence differs by one byte, it prints one `dup` line, and at the pass tip
  it prints none.
  Red when: the duplicate is told apart by its Evidence.
  fixture: the folder is made in the run's scratch by the pass.
- **AC23** — When `python -c "import tree_lib; print(tree_lib.resolve_memory_root.__doc__)"` runs from
  `tools/memory-tree/`, it prints `runlog_lib` and `memory-recall`.
  Red when: the divergence or the third definition goes unnamed.
- **AC24** — When the corrected `read_at` runs over spec 59 at `653bed738` with the needles
  `is  absent` and `is absent`, it prints 2 for each, an empty strings file prints a `red` line and
  exits 1, and §4's needle scan prints only its `blocks` line.
  Red when: a whitespace run changes a count, or an empty file reads green.
  figure: the counts are PINNED in §4, measured 2026-10-26.

## 7. Gates

`kickoff-manifest ratchet` · `build README slot contract` · `memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

No new arm: each observation is a probe this spec spells, a fixture folder, or a read of a landed
unit's output.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 77 to 88, its 24
  confirmed minors: 17 MEDIUM, ids 2 3 5 6 10 11 12 13 16 17 18 19 20 24 25 26 27 (items M1 to M15),
  and 7 LOW, ids 7 8 9 14 15 21 28 (items L1 to L7).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the consumes-from edge to TOOL-dTotalRecall-93, the mirror of TOOL-dTotalRecall-98, the mirror of TOOL-dTotalRecall-99, the mirror of TOOL-dTotalRecall-100, each the other end of an edge a unit the
  round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams are those the minors name: `TOOL-dTotalRecall-90`'s `s1`, `has_deviation` and record
recipe; `TOOL-dTotalRecall-81`'s `pass_of` and `read_at`; `TOOL-dTotalRecall-77`'s `read_checker`;
unit 79's span script, corrected here; `deviation_join.read_record`
(`tools/memory-tree/deviation_join.py:212`) for the tip scan; `gen_build_index.measure_slot_sizes`
for the rules slot; and the scratch-worktree pair of `tools/run-gates/lib-attribute.sh:59` and `:63`.
`python tools/codebase-map/reuse_lookup.py "count deviation records of one unit by a computed key over the working tree"`
ranked `read_records` among its SEAM candidates, which reads tracked files only, so the scan calls
`read_record` per file. The recall query below found this audit's items M6, M12, M13, M14 and L5,
specs 82 to 86 whose guards they name, and the `TOOL-dTrueNorth-18` ledger that probed
`**Supersedes:**`. No mechanism is minted beyond the scan, two corrected probes and one docstring.

Recall terms used: `python tools/memory-recall/query.py "how does a write-once guard find a deviation record already written, including one not yet committed" --terms "deviation record written once untracked git grep Serves anchored evidence token read_record Supersedes duplicate door"`
