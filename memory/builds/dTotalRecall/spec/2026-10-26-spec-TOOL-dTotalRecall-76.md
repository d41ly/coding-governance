# TOOL-dTotalRecall-76 — the round-6 minors: each reading units 67 to 70 made by a broken probe or a stale rule is made again at the tip, and each gap it hid is closed

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 35 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-74 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
exited BOUNDED with 28 confirmed findings. Its blocker and four highs are units 71 to 75: id 23 is
`TOOL-dTotalRecall-71`, id 10 is `TOOL-dTotalRecall-72`, id 5 is `TOOL-dTotalRecall-73`, id 11 is
`TOOL-dTotalRecall-74` and id 17 is `TOOL-dTotalRecall-75`. This unit is the batch BUILD-METHOD M4
makes of the rest:

- the 16 MEDIUM findings, ids 1, 2, 3, 4, 6, 12, 13, 18, 19, 20, 21, 26, 27, 29, 30 and 31 (items M1
  to M15);
- the 7 LOW findings, ids 7, 8, 9, 15, 16, 25 and 28 (items L1 to L7).

Each keeps its report id and its own scope item. The minors land on units 67 to 70, so this unit
repairs none in particular and builds after every unit: order 35, above the 34 that unit 74 holds.
The review record holds each item's text.

Ids 1 and 12 share item M1. Ids 2 and 25 (M2 and L6), ids 13 and 7 (M6 and L1) and ids 5 and 20 (H1
and M8) each see one defect at two grades. Id 20's direction is settled by unit 73's one
registration (`TOOL-dTotalRecall-73` §8 F1), and its item here names that registration's consumers.

## 2. Scope (IN)

Every item states its change to the unit it lands on, as that unit was built. A landed spec is
frozen and is not edited. An item whose unit's criterion observed nothing, or observed by a broken
probe, makes the observation at the tip. Where that observation is red, the item repairs the code,
or writes a deviation record when the departure is in a spec. "pass(N)" is the first line of
`git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-N$' 462d20f3..HEAD`. "The blob
probe" is §4's. "The registry" is `census-kept-paths.txt` at the home
`resolve_kept_registration(root)` returns (`TOOL-dTotalRecall-73`).

- **S1** — id 12 (M1). Unit 61's rewrite of unit 55's consumes-from line to unit 53 is read by the
  blob probe at pass(55)^: `holding only the build-folder rows this unit moves`, wanting 1. A 0 is a
  deviation record of unit 55, and `git grep -n CAUSE_WRITER_KEPT -- tools`, the code that line
  governs, is run at the tip. Observed by AC1.
- **S2** — id 1 (M1). Unit 61's hands-off from unit 56 to unit 57 is read the same way at
  pass(56)^: ``**hands-off** `TOOL-dTotalRecall-57` ``, wanting 1. A 0 is a deviation record of unit
  56. The ledger records unit 67's reading as covering six of unit 61's eight amendments, so its
  Goal's "each amendment" is answered here for the other two. Observed by AC1.
- **S3** — id 13 (M6). Two of the strings unit 67 handed to unit 70 and unit 70 did not re-read are
  read by the blob probe: `git grep -n CAUSE_WRITER_KEPT -- tools` over unit 55's spec at pass(55)^
  and `git grep -n ALIAS_COMPARE_KEPT -- tools` over unit 56's at pass(56)^, each wanting 1. Each
  command then runs at the tip and prints nothing. Observed by AC1.
- **S4** — id 7 (L1). The third, ``**consumes-from** `TOOL-dTotalRecall-56` ``, is read over unit
  57's spec at pass(57)^, wanting 1: the text unit 57 built from, where unit 71 certified the spec at
  step 21. Observed by AC1.
- **S5** — id 2 (M2). Every row of unit 70's §4 table but the ``` `absorbs` is absent ``` row, unit
  74's, is read by the blob probe over `git show pass(T)^:<spec path>`. No row reads a working-tree
  file, and a failed `git show` is a red, never a 0. Each count is set beside the count unit 70's
  AC1 line recorded. A row whose wanted count fails, with no deviation record of its unit, gets that
  record. Observed by AC2.
- **S6** — id 25 (L6). Unit 70's AC8 text reads, `whose body this unit rebuilds` and
  `rebuilds the parser on that regex` over unit 46's spec at pass(46)^, are made by the blob probe,
  with the liveness count §4 pins taken by the same command. Observed by AC2.
- **S7** — id 3 (M3). Unit 70's AC7 is keyed on unit 64's pass, never on every commit that touched
  unit 38's spec. `git merge-base --is-ancestor pass(38) pass(64)` exits 0, and pass(64)'s diff of
  unit 38's spec changes a line outside its `<!-- gen:spec-records -->` region. The deviation record
  of unit 38 names pass(64). Where unit 70's S14 record names a render-only commit instead, this
  pass writes the record naming pass(64). Observed by AC3.
- **S8** — id 4 (M4). The registry's filename has one spelling. Outside the fixture plants, no
  module under `tools/memory-tree/` spells `census-kept-paths.txt`. Unit 70's domain refusal and
  marker remedy format the path from `resolve_kept_registration(root)`'s home. A message site that
  spells the literal is re-pointed. Observed by AC4.
- **S9** — id 20 (M8). The consumers of the memory root read unit 73's one home. Unit 66's plant
  `kept-row-docs-root` keeps its row with the registry under `docs/memory/project/`, and its compare
  line names that home. Unit 70's S8 messages name it, as S8 here observes. Unit 70's check-3
  admission is by name, so it holds under any memory root. Observed by AC4.
- **S10** — id 6 (M5). The plant `kept-row-gained` runs its git in a child environment that carries
  no `GOV_REMOTE`, no `GOV_DEFAULT_BRANCH` and no `GIT_*` variable. Its remote is
  made with `-b main` and `origin/HEAD` set, as unit 66's S22 does for unit 59's fixture. Observed
  by AC5.
- **S11** — id 29 (M13). The plant `kept-row-gained` makes its scratch repository in a
  `tempfile.TemporaryDirectory()` with a short prefix, the idiom of
  `tools/codebase-map/selftest.py:1815`, never at `%TEMP%/<short>`. Observed by AC5 and AC6.
- **S12** — id 30 (M14). Fixed scratch paths are swept as a class. Every fixture or plant builder in
  `tools/memory-tree/record_causes.py`, `tools/lib/legacy_ledger.py` and `tools/govkit/selftest.py`
  is read for `%TEMP%`, a `gettempdir()` joined with a literal, or another hard-coded scratch path.
  A hit moves to a `tempfile.TemporaryDirectory()`. Observed by AC6 for the two modules, and for the
  govkit suite by §7's arm on it.
- **S13** — id 19 (M9). Unit 66's seven registry plants, `kept-row-caused`, `kept-row-untracked`,
  `alias-row-drained`, `alias-row-outside-domain`, `kept-row-traversal`, `kept-row-nested` and
  `kept-row-docs-root`, and unit 65's `adopter-no-registry`, write their fixture home through
  `write_rows` in the factory grammar. Each scratch tree tracks a `kit.toml` holding the
  `census-kept-paths` registration. Each plant's red is then the refusal it targets, never a
  malformed row or a missing registration. Observed by AC7.
- **S14** — id 26 (M11). Unit 68's precondition is read where it built. At pass(68)^,
  `tools/lib/legacy_ledger.py` is tracked and defines `read_registrations`, `read_rows`,
  `write_rows` and `compare_to_base` (`TOOL-dWitnessedBar-13` §4), and the first-seed reading
  `TOOL-dWitnessedBar-51` S30 rules. No module under `tools/memory-tree/` defines a function of those
  names at the tip. A failure is a deviation record of unit 68. Observed by AC8.
- **S15** — id 27 (M12). With no compare base, `record_causes.py --check` exits 1 and prints
  `unresolved` with the base's reason, as `TOOL-dWitnessedBar-51` S33 rules for a live ratchet leg.
  The plant `kept-base-unresolved` builds a scratch repository with no `origin/main`. Observed by
  AC9.
- **S16** — id 21 (M10). The `record causes` row of `tools/gate-legs.json` declares
  `"reads": {"base": ..., "history": ...}`, each with its reason: `compare_to_base` reads the
  registry at the merge-base with the remote, out of history. Observed by AC10.
- **S17** — id 15 (L4). `census-kept-paths.txt` leaves `PROJECT_REGISTRY_EXTRA` in
  `.memory-tree.conf`, since check 3 admits it by name (unit 70's S12). This follows the rule at
  `tools/memory-tree/check-memory-hygiene.sh:732-737`, which `TOOL-dWitnessedBar-57` AC21 enforces
  for its five homes. Observed by AC11.
- **S18** — id 18 (M7). This pass's own watched edits, S16's and S17's, are followed in one commit,
  last in the pass, by a re-read of §B, a `last-audit` re-stamp and a `last-body-change` advance.
  This also covers unit 70's S12 edit, whose re-stamp left C9 unhandled. Observed by AC12.
- **S19** — id 31 (M15). The `kickoff-manifest ratchet` leg's red span is derived, never argued.
  `manifest-check.sh` runs in a scratch worktree at each pass commit from pass(1) to this pass's
  base. The ledger records, per step, whether it printed `fail 5` or `fail 9`, and names the re-stamp
  that closed each span: unit 43's at step 27, unit 60's at 31, unit 69's at 32, and units 70 and
  75 at 33. Observed by AC13.
- **S20** — id 16 (L5). Unit 69's AC1 pair is answered by the checker, never by a copy of its
  predicate. The S19 sweep's line for pass(69) is C5's verdict there, and the ledger records unit
  69's AC1 as answered by it. Observed by AC13.
- **S21** — id 8 (L2). Unit 67's AC3 answer is read for nine counts: six strings, each over the spec
  it amends, and the §9 form over each of the three. A count of a string over a spec it does not
  amend is recorded as void. Observed by AC14.
- **S22** — id 9 (L3). Unit 67's AC1 answer keeps each backticked string on a physical line that
  carries the AC1 label, or lists the counts as a sub-list, one bullet per string. Where it wraps a
  token onto a line hygiene check 23 does not join, this pass rewrites that answer as the sub-list.
  Observed by AC14.
- **S23** — id 28 (L7). Unit 66's S26 ask read takes the row's `keep:` disposition. At the tip no
  module spells `CAUSE_WRITER_PINNED`, and the plant `pinned-ask-is-spec` (unit 66's AC20) reds
  naming the `keep:` disposition of its row. Observed by AC15.
  **Readers:** by name: READER NOT IN TREE — `CAUSE_WRITER_PINNED` is minted by
  `TOOL-dTotalRecall-50` in this build and is absent at base `462d20f3` · by value: unit 66's S26
  ask read and its plant `pinned-ask-is-spec`, each pointed at the row's `keep:` disposition.

## 3. Non-goals (OUT)

- The blocker and the four highs: units 71 to 75.
- Editing a landed spec's text, frozen once its unit builds, as §2's opening states.
- The spec lints, checklist entries and shared fixture helper the report suggests as gates. The
  close's left-shift step (BUILD-METHOD M8) takes them.
- The factory-side readers of a literal ledger home, handed off by unit 73 to the parent factory's
  owner.

### Edges

- **consumes-from** `TOOL-dTotalRecall-65` — its plant `adopter-no-registry`, rewritten through the factory grammar (id 19)
- **consumes-from** `TOOL-dTotalRecall-66` — its seven registry plants, its docs-root plant and its S26 ask read with `pinned-ask-is-spec`, re-staged and re-read at the tip (ids 19, 20, 28)
- **consumes-from** `TOOL-dTotalRecall-67` — the strings of its table and the two it left out, read against the text units 55, 56 and 57 built from, and its AC1 and AC3 ledger answers (ids 1, 7, 8, 9, 12, 13)
- **consumes-from** `TOOL-dTotalRecall-68` — `kept-row-gained`, the registration, the `--check` compare and its factory precondition (ids 6, 21, 26, 27, 29)
- **consumes-from** `TOOL-dTotalRecall-69` — its re-stamp, its AC1 pair and the steps its argument left unnamed (ids 16, 31)
- **consumes-from** `TOOL-dTotalRecall-70` — its §4 table and AC8 readings, its AC7 and S14 record, its messages, its fixture sweep, its check-3 admission and its S12 re-stamp (ids 2, 3, 4, 15, 18, 25, 30)
- **consumes-from** `TOOL-dTotalRecall-73` — `resolve_kept_registration`, the one home S8 and S9 point every consumer at (ids 4, 20)
- **hands-off** `TOOL-dTotalRecall-77` — its S19 sweep and its AC12 and AC13 lines, whose grep that unit's checker read replaces (the round-1 audit of units 71 to 76, id 23)
- **hands-off** `TOOL-dTotalRecall-78` — its S19 population and loop, which that unit's sweep replaces (the round-1 audit of units 71 to 76, id 34)
- **hands-off** `TOOL-dTotalRecall-79` — its AC13 answer and its S19 list of re-stamps, which that unit sets beside the derived spans (the round-1 audit of units 71 to 76, id 1)
- **hands-off** `TOOL-dTotalRecall-80` — its S20 answer, which that unit replaces with the checker's C5 verdict at unit 69's pass (the round-1 audit of units 71 to 76, id 16)
- **hands-off** `TOOL-dTotalRecall-85` — its S1 to S4 and its AC1 line, whose five counts that unit re-reads at verified revisions (the round-1 audit of units 71 to 76, id 11)
- **hands-off** `TOOL-dTotalRecall-86` — its S5 and S6 and its AC2 line, whose counts that unit re-reads at verified revisions (the round-1 audit of units 71 to 76, id 38)
- **hands-off** `TOOL-dTotalRecall-88` — its AC7, AC12 and §10, its plants and its S19 sweep's leftovers, which that batch re-reads or repairs (the round-1 audit of units 71 to 76, ids 5, 6, 7, 15, 18, 21, 22, 26, 31, 33, 42)

## 4. Design

### How the batch builds

One pass, after every other unit is terminal. Inside it the order is:

1. The read-only items: S1 to S7, S14, S19 to S22. Each red they find decides a repair below or a
   deviation record.
2. The registry and fixture items: S8 to S13, S15 and S23.
3. S16 and S17, the two watched edits.
4. S18's re-read, re-stamp and advance, last, so that they follow every watched edit of the pass.
5. The deviation records and the ledger lines.

### The blob probe

Each string is a Python literal inside a heredoc whose delimiter is quoted, so bash expands nothing
in it. Each revision is read by `git show` inside Python with `check=True`, so a failed read raises
and is a red, never a 0. This is the bridge from a blob to the count that unit 70 never spelled
(ids 2 and 25), and the quoting units 71, 72 and 74 use.

```bash
# run from memory/builds/dTotalRecall/spec/ ; REV is the revision, N the unit
REV=<revision> N=<unit number> python - <<'PROBE'
import os, re, subprocess
STRINGS = ['<string>', '<string>']
raw = subprocess.run(['git', 'show', os.environ['REV'] + ':./2026-10-26-spec-TOOL-dTotalRecall-%s.md' % os.environ['N']],
                     capture_output=True, check=True).stdout.decode('utf-8')
t = re.sub(r'\s+', ' ', raw)
for s in STRINGS:
    print(t.count(s), s)
PROBE
```

PINNED, measured 2026-10-26 at `653bed738` with this form: `whose body this unit rebuilds` and
`rebuilds the parser on that regex` print 1 each over spec 46, and the first prints 2 over spec 64.
`holding only the build-folder rows this unit moves`, `git grep -n CAUSE_WRITER_KEPT -- tools` and
`git grep -n ALIAS_COMPARE_KEPT -- tools` print 0 over their target specs and 1 each over spec 61.
``**hands-off** `TOOL-dTotalRecall-57` `` prints 0 over spec 56 and 1 over spec 61. So each read of
§2 can return either value.

### The sweep of S19

```bash
# run from the repository root; one scratch worktree, removed after
D=$(python -c "import tempfile; print(tempfile.mkdtemp(prefix='mc'))")
for N in <every unit id with a pass commit, in order of its pass>; do
  P=$(git log --reverse --format=%H --grep="^Pass: $N\$" 462d20f3..HEAD | head -1)
  git worktree add --detach "$D/w" "$P" >/dev/null && (cd "$D/w" && bash skills/session-kickoff/manifest-check.sh 2>&1 | grep -E 'fail (5|9)' | sed "s|^|$N |")
  git worktree remove --force "$D/w"
done
```

A line it prints names a pass commit at which the leg was red, and why. The worktree directory comes
from `tempfile.mkdtemp`, so two runs never share it.

### The registry items S8, S9, S13 and S23

The filename comes from the registration in `tools/memory-tree/kit.toml`, through
`resolve_kept_registration(root)`. Every plant that writes a registry writes it with `write_rows` at
the home that function returns in its scratch tree. A plant whose staged refusal is skipped must then
read green, which is how S13's AC proves the red belongs to the refusal and not to the fixture.

### Inventory

Minted: the fixture plant `kept-base-unresolved` in `record_causes.py --fixture`; the `reads` key
of the `record causes` row; deviation records where §2's reads are red. Naming cell: none, no
function minted.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/record_causes.py`, `tools/memory-tree/record_kinds.py`
- `tools/gate-legs.json`
- `.memory-tree.conf`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/lib/legacy_ledger.py`, `tools/memory-tree/legacy_ledger.py`, `tools/gate-lint/legacy_ledger.py` (only where S12 moves a fixture, the three edited in one commit under `PARITY_ROWS`)
- `tools/govkit/selftest.py` (only where S12 moves a fixture)
- `memory/builds/dTotalRecall/build/` (the deviation records, unit 67's rewritten AC1 answer where S22 finds a wrap, and this unit's ledger lines)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Two batches**, the history reads (S1 to S7, S14, S19 to S22) beside the code items. S19's sweep
  ends at this pass's tip, which S18's re-stamp writes, and S3 runs its two greps over the code S12
  and S13 edit. Each half reads the other's output as an acceptance input, so BUILD-METHOD M6's
  clause 2 keeps them one unit.
- **Re-read every string over the working tree.** The working-tree spec is the text after later
  amendments, not the text each unit built from. Only `pass(T)^` answers what a unit built from.
- **Count C5 and C9 by a copy of their predicates.** Item L5 is that defect. The sweep runs the
  checker itself.

## 5. Production-readiness checklist

- security — no new write surface. S17 narrows gov's local check-3 escape by one name.
- perf / scale — S19 runs the checker once per pass commit, about seventy worktree checkouts, each
  seconds. The other reads are one `git show` each.
- error / empty / loading states — a failed `git show` is a red. A plant whose scratch repository
  cannot be made is a fixture fault, never a pass. A `None` base exits 1 under S15.
- observability — each read writes its count beside the count the landed unit recorded, and a void
  or false reading is recorded as such.
- risks — S15 makes the `record causes` leg red on a checkout with no remote, as the parent rules.
  S17 makes check 3 admit the registry by its by-name case alone.
- testing — AC1 to AC15 by the pass; the two arms of §7 at the close.
- migration — none. S13's plants change their fixtures only.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the blob probe runs for S1 to S4, `holding only the build-folder rows this unit moves`
  and `git grep -n CAUSE_WRITER_KEPT -- tools` print at least 1 over unit 55's spec at pass(55)^,
  ``**hands-off** `TOOL-dTotalRecall-57` `` and `git grep -n ALIAS_COMPARE_KEPT -- tools` over unit
  56's at pass(56)^, and ``**consumes-from** `TOOL-dTotalRecall-56` `` over unit 57's at pass(57)^,
  or `git grep -lE "deviation TOOL-dTotalRecall-5[567]$" -- memory/builds/dTotalRecall/build` prints
  a record of that unit naming the string. `git grep -n CAUSE_WRITER_KEPT -- tools` and
  `git grep -n ALIAS_COMPARE_KEPT -- tools` print nothing at the tip.
  Red when: a unit built from text its amending unit had not written, and no deviation record names
  it.
  figure: the counts at writing are PINNED in §4; the counts at each pass are DERIVED by the pass.
- **AC2** — When the blob probe runs over each row of unit 70's §4 table but the `absorbs` row, and
  over unit 46's spec at pass(46)^ for S6's two strings, each prints its wanted count or a deviation
  record of its unit names it. The ledger sets each count beside unit 70's.
  Red when: a count is read from a working-tree file, or a failed `git show` is recorded as 0.
- **AC3** — When `git merge-base --is-ancestor <pass(38)> <pass(64)>` runs, it exits 0, and
  `git show <pass(64)> -- memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-38.md`
  changes a line outside the `gen:spec-records` markers.
  `git grep -l "deviation TOOL-dTotalRecall-38" -- memory/builds/dTotalRecall/build` prints a
  record whose Evidence names pass(64).
  Red when: the record names a render-only commit, or no record names pass(64).
- **AC4** — When `git grep -c "census-kept-paths.txt" -- 'tools/memory-tree/*.py'` runs at the tip,
  only fixture-plant lines carry it. `python record_causes.py --fixture --plant kept-row-editable`,
  `--plant kept-row-drained` and `--plant unkept-build-alias`, run from `tools/memory-tree/`, each
  print a refusal or remedy naming the registry's file under the `project` folder of its tree's
  memory root, the home `resolve_kept_registration` returns. `--plant kept-row-docs-root` keeps its
  row, and its compare line names the registry's file under the fixture's memory root `docs/memory`.
  Red when: a message site retypes the filename, or a consumer reads a home other than unit 73's.
- **AC5** — When `GOV_REMOTE=nope GOV_DEFAULT_BRANCH=nope python record_causes.py --fixture --plant kept-row-gained`
  runs from `tools/memory-tree/`, `--check` still names the planted key `gained`.
  Red when: an exported variable changes the fixture's base.
- **AC6** — When a `python -c` probe reads the source of every function in `record_causes.py` under
  the memory-tree kit and `legacy_ledger.py` under the shared library whose name or body builds a
  fixture or plant, it prints no `%TEMP%`, no `gettempdir()` joined with
  a literal and no other literal scratch path. In a scratch copy where one such function gains a
  write to a literal scratch path beside its `tempfile.TemporaryDirectory()` call, it names that
  function.
  Red when: a fixture builds or writes at a fixed path.
- **AC7** — When each plant S13 names runs with the refusal it targets staged off, it reads green, and
  with the refusal on it reds naming that refusal.
  `python -c "import inspect, record_causes; print('write_rows' in inspect.getsource(record_causes))"`
  run from `tools/memory-tree/` prints `True`.
  Red when: a plant's red comes from a malformed row or a missing registration.
- **AC8** — When `git show <pass(68)^>:tools/lib/legacy_ledger.py` runs, it prints a file defining
  `read_registrations`, `read_rows`, `write_rows` and `compare_to_base`.
  `git grep -nE "def (read_registrations|read_rows|write_rows|compare_to_base)\b" -- tools/memory-tree ':!tools/memory-tree/legacy_ledger.py'`
  prints nothing at the tip. Where either fails,
  `git grep -l "deviation TOOL-dTotalRecall-68" -- memory/builds/dTotalRecall/build` prints a
  record naming it.
  Red when: unit 68 built on an improvised factory and no record names it.
- **AC9** — When `python record_causes.py --fixture --plant kept-base-unresolved` runs from
  `tools/memory-tree/`, `--check` prints `unresolved` with the base's reason and exits 1.
  Red when: it exits 0.
- **AC10** — When `python -c "import json, sys; r=[l for l in json.load(open(sys.argv[1])) if l['name'].startswith('record causes')][0]; print(sorted(r.get('reads', {})))" tools/gate-legs.json`
  runs from the repository root at the tip, it prints a list holding `base`.
  Red when: the leg reads the base and declares no `reads.base`.
- **AC11** — When `grep -c census-kept-paths .memory-tree.conf` runs at the tip it prints 0, and
  `bash tools/memory-tree/check-memory-hygiene.sh --only 3` names no `census-kept-paths.txt` path.
  Red when: gov keeps the name in its local escape, or check 3 reds gov's registry.
- **AC12** — When `bash skills/session-kickoff/manifest-check.sh` runs at the tip it exits 0 with no
  `fail 5` or `fail 9` line, and
  `git rev-list --count --no-merges <last-body-change>..HEAD -- <each path of the watch: line>`
  prints a value under 10.
  Red when: a watched edit of this pass has no re-stamp after it, or C9 counts ten.
- **AC13** — When §4's sweep runs `manifest-check.sh` at each pass commit, the ledger lists each
  pass commit it found red with its fail line, and names the re-stamp that closed each span. Its
  line for pass(69) is C5's verdict there. Its run at this pass's tip prints nothing.
  Red when: a red span has no closing re-stamp, or the tip is red.
  cost: one checker run per pass commit, minutes in all.
- **AC14** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-67" -- memory/builds/dTotalRecall/build`
  runs, the AC1 answer beneath it names nine counts, each with its spec, and each backticked string
  sits on a line carrying the AC1 label or on its own sub-bullet.
  `bash tools/memory-tree/check-memory-hygiene.sh --only 23` names no unanswered criterion of
  `TOOL-dTotalRecall-67`.
  Red when: a token wraps onto a line the check does not join.
- **AC15** — When `git grep -n CAUSE_WRITER_PINNED -- tools` runs at the tip it prints nothing, and
  `python record_causes.py --fixture --plant pinned-ask-is-spec`, run from `tools/memory-tree/`, reds
  naming the `keep:` disposition of its row.
  Red when: the ask is read from anything but the row's disposition.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `shell-hygiene selftest` · `kickoff-manifest ratchet` · `kit/dogfood doc parity` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `python resolver (behaviour + inline parity + idiom ban)` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC5 AC7 AC9 · the plant `kept-base-unresolved`, the scrubbed `kept-row-gained` and S13's eight re-staged plants, staged by skipping each refusal and, for `kept-base-unresolved`, by exiting 0 on a `None` base · none
New arm: tools/govkit/selftest.py · covers none · S12's sweep of its fixture builders, a hit moved to a `tempfile.TemporaryDirectory()`, staged by restoring one moved builder's literal scratch path with a file already at it · none

## 8. Open questions

- **F1 — May this pass edit `.memory-tree.conf` and `tools/gate-legs.json`, and move the stamps of
  `memory/guides/SESSION-KICKOFF.md`, governance carriers?** Options: (a) yes, under the build's
  grant: S16 declares a key the leg's own reads require, S17 removes one name check 3 already admits,
  and S18's stamps follow those edits; (b) no, leaving the leg's base read undeclared, gov's escape
  in place and the ratchet leg red. (b) fails AC10, AC11 and AC12. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 5, the README's `may:` grant, as `TOOL-dTotalRecall-70` §8 F2 and
  `TOOL-dTotalRecall-75` §8 F1 use it. grants: PLAY-dClosedLoop-3 the record-causes leg's reads key,
  the conf's check-3 escape and SESSION-KICKOFF.md's stamps after them · widens: none · relaxes:
  none
- **F2 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 67 to 70, its 23
  confirmed minors: 16 MEDIUM, ids 1 2 3 4 6 12 13 18 19 20 21 26 27 29 30 31 (items M1 to M15),
  and 7 LOW, ids 7 8 9 15 16 25 28 (items L1 to L7).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-77, TOOL-dTotalRecall-78, TOOL-dTotalRecall-79, TOOL-dTotalRecall-80, TOOL-dTotalRecall-85, TOOL-dTotalRecall-86, TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams are those the minors already name:

- the joined-text probe of `TOOL-dTotalRecall-67` §4, with the quoting of units 71, 72 and 74 and the
  `git show` read of unit 70 §4's body compare;
- `resolve_kept_registration` (`TOOL-dTotalRecall-73`) and the factory's `write_rows`;
- `manifest-check.sh` itself, run per pass commit rather than re-implemented;
- the scratch-directory idiom of `tools/codebase-map/selftest.py:1815`;
- the `reads` declarations of `tools/gate-legs.json`, for example the `codebase-map coverage +
  freshness` row's.

No mechanism is minted beyond one plant and one leg key.
`python tools/codebase-map/reuse_lookup.py "count a phrase holding backticks in a spec file without shell quoting"`
ranked name-stem neighbours only, none of which counts a phrase in a spec body. The recall query
below found the audit's own items and unit 67's probe. S10 follows the bug class
`memory/gotchas/fixture-inherits-ambient-machine-state.md`, the class the report names for id 6.

Recall terms used: `python tools/memory-recall/query.py "how does a probe pass a string holding backticks to python without the shell running it" --terms "probe backtick double-quote command-substitution argv joined-text count spec amendment liveness stdin heredoc"`
