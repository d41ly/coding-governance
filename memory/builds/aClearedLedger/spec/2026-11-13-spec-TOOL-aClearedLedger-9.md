# TOOL-aClearedLedger-9 — a path-less `Red-fix:` commit owes no record: the join holds it out by name and the door says why it refuses

**Status:** SPECCED · rev-1 · 2026-11-13 · node a · Tier-2 · base 8db6f4be · streams tooling · order 9 · closes TOOL-aNimbleMend-23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

A commit that carries a `Red-fix:` trailer and touches no path can never be recorded: the door
refuses it because it has no `Files`, and the join then reports it as J1 for good once it is below
HEAD, and refuses every commit made on top of it under `--staged`. This unit states what such a
commit owes, which is nothing, in the join that grades it and the door that refuses it, and holds
the rule with plant cases.

## 2. Scope (IN)

- **S1** — The join, `tools/memory-tree/build_records.py#check_red_fix_join`, holds a path-less fix
  commit out of the population that owes a record. A commit is path-less when
  `tools/memory-tree/routed_commits.py#read_routed_commits` returns it with a `red_fix` value and an
  empty `paths` list. It raises no J1 at any depth, in the full form and under `--staged`. Observed
  by AC1 and AC2.
- **S2** — The join prints one line per trailer value of a path-less commit, and its summary line
  gains a path-less count, both in the shape §4 "The join" gives. Observed by AC1 and AC2.
- **S3** — The door, `build_records.py#write_red_fix`, keeps refusing a path-less commit, and its
  refusal text states the rule: the commit owes no red-fix record. Observed by AC3.
- **S4** — A record whose `Commit` names a path-less commit is J2, since that commit is outside the
  population. Observed by AC4.
- **S5** — The `red-fix-join` plant of `build_records.py#run_fixture` gains the cases of §4 "The
  plant": an empty fix commit at HEAD, the same commit under `--staged`, the door's refusal of it,
  a merge carrying the trailer, both below HEAD, and a record naming one. Observed by AC1 to AC4.
- **S6** — The rule is stated where the join is documented: the module docstring of
  `build_records.py`, check 31 and the "Red-fix records" paragraph of
  `tools/memory-tree/HYGIENE.template.md`, with `memory/HYGIENE.md` re-rendered from it, and the
  section "The record" of `help/red-fix-lane.md`, its usage anchor answered as `help/docs-leg.md`
  says under "How to answer a stale page". Observed by AC5.

## 3. Non-goals (OUT)

- Refusing the trailer on a path-less commit. Whether a commit may carry `Red-fix:` is the commit
  gate's, built by TOOL-aNimbleMend-8, and a history that already holds such a commit cannot be
  rewritten to satisfy a new refusal.
- Reading a merge against its first parent. The join keeps the one log pass
  `read_routed_commits` makes, in which every merge is path-less.
- A second `Files` grammar, such as a `none` value. F1 lists it as option B.
- Any change to J1 to J6 for a commit that touches a path, or to the lane's limits in
  `routed_commits.py#check_red_fix_limits`.
- A new arm in `tools/memory-tree/check-memory-hygiene.test.sh`. Its existing assertion on the
  plant's PASS line already re-observes every plant case, and units 6 and 8 of this build write
  that suite.
- The kit version, which the lander's `mint` moves once, after the last unit.

### Edges

none

## 4. Design

### The rule

A `Red-fix:` commit that touches no path owes no red-fix record. The record is the account of a
change made with no spec, and its `Files` field is that change. A commit with no path holds no
change to account for.

Two kinds of commit are path-less in the join's read, verified on a scratch repository at
`82ceaab5`:

| Commit | Why `paths` is empty |
|---|---|
| an empty commit, made with `--allow-empty` | its tree equals its parent's |
| any merge | `git log --name-only` prints no path for a merge unless a merge-diff flag is passed, and `read_routed_commits` passes none |

The second row matches the lane as its grader already defines it. `routed_commits.py` grades the
limits over "every non-merge commit" carrying the trailer, and its docstring says a merge's own
content is not graded.

### The join

`check_red_fix_join` splits the trailer commits it reads into two sets before it reads a record.
A commit with a non-empty `paths` list is a fix, graded exactly as today. A commit with an empty
list is path-less. For each trailer value of a path-less commit the join prints:

```
build-records: red-fix join · path-less · <sha8> · <leg> · touches no path, so it owes no record
```

The summary line gains one field at its end, and its first three fields keep their meaning: the
fix count is the commits that owe a record.

```
build-records: red-fix join · <N> fix commit(s) · <M> record(s) · <K> owed · <P> path-less
```

`<P>` counts commits, as `<N>` does. The line is the join's liveness for this rule: a path-less
commit is named on every run and never silently skipped. Every reader of the summary matches its
leading fields as a substring: `tools/memory-tree/check-memory-hygiene.sh` prints the line whole
under check 31, and `tools/memory-tree/check-memory-hygiene.test.sh` asserts the text up to
`0 owed`.

Under `--staged` the join reads HEAD alone. A path-less HEAD prints its `path-less` line and the
summary, and exits 0, so the next commit is not held for a record no door can write. The existing
held line, which says HEAD carries no trailer, stays for a HEAD that carries none.

A record whose `Commit` is a path-less commit meets the existing J2 branch, because that sha is
not in the fix set. Its finding line is J2's as it stands.

### The door

`write_red_fix` keeps its refusal of a commit with no path, exit 1 and nothing written. The text
becomes:

```
commit <sha8> touches no path, so it owes no red-fix record and the join asks none
```

### The plant

The cases join the `red-fix-join` plant after its `clean` case, where the fixture holds one fix
and its record, and before the J-row loop. Each is one `check_case` call or one counted refusal,
as the cases beside it are.

| Case | Stages | Holds |
|---|---|---|
| `path-less at HEAD` | an empty commit carrying the fixture leg's trailer | exit 0, one `path-less` line naming its sha and the leg |
| `staged, path-less at HEAD` | the same HEAD, `--staged` | exit 0, the same line |
| `refusal · a commit that touches no path` | the door over that commit | exit 1, the record count unchanged, the text of "The door" |
| `path-less below HEAD` | a side branch merged with `--no-ff` under a message carrying the trailer, then one plain commit | exit 0, the summary ending `0 owed · 2 path-less` |
| `J2, a record naming a path-less commit` | the fixture's record with its `Commit` set to the empty commit's sha | exit 1, `· J2 ·`, the record and that sha |

The J-row loop and the closing J1 case then run over a history that holds both path-less commits,
and each still finds its own row. The PASS line's case count is derived by the plant.

### What the join does not check

- Whether a merge's resolution changed a file. A merge is path-less in this read whatever its
  content, as the commit grader also leaves a merge's content ungraded.
- Whether a path-less commit should carry the trailer at all. Nothing refuses it at commit time.
- Everything TOOL-aNimbleMend-9 lists under the same heading, which stands.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| join line kind `path-less` | `check_red_fix_join` | AC1 |
| summary field `<P> path-less` | `check_red_fix_join` | AC2 |
| five plant cases | `run_fixture`, plant `red-fix-join` | AC1 to AC4 |

No function, flag, kind or field is minted.

### Migration

Additive. A tree holding no path-less trailer commit reads a zero in the new summary field and no
other change. A tree holding one stops reporting J1 for it. No record changes.

### Files touched (estimate)

- `tools/memory-tree/build_records.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `help/red-fix-lane.md`

### Alternatives rejected

- **A commit-time refusal of the trailer on a path-less commit, alone.** It leaves any such commit
  already in history a permanent J1, which is the ask.
- **A waiver list of shas for the join.** It is a typed exemption beside the history that already
  says which commits are path-less, so the join derives the set.

## 5. Production-readiness checklist

- security — no new write path. The door still writes nothing for a path-less commit, and the join
  reads git through the pinned reader it already uses.
- perf / scale — no new git call. The split reads the `paths` list the one log pass already
  returns.
- error / empty / loading states — a history with no path-less commit prints a zero in the new
  field. Exit 2 on an unreadable git or record population is unchanged.
- observability — one line per path-less trailer value and a count on the summary, on every run.
- risks — a merge whose resolution fixes a red carries no record. The trailer on a merge is
  ungraded by the limits pass too, so the lane already treats a merge as outside it.
- testing — the five plant cases of §4; the hygiene suite's existing assertion on the plant's PASS
  line carries them into the suite.
- migration — additive; see §4 "Migration".
- user docs — `memory/HYGIENE.md` through its template and `help/red-fix-lane.md` are S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/build_records.py --fixture --plant red-fix-join` runs,
  its `path-less at HEAD` and `staged, path-less at HEAD` cases each print exit 0 and one line
  holding `path-less`, the empty commit's abbreviated sha and the fixture leg.
  Red when: the join still counts the empty commit as a fix, so the first case prints `owed` and
  the staged case exits 1 on J1.
- **AC2** — When the same `red-fix-join` plant runs, its `path-less below HEAD` case prints exit 0
  and a summary line ending `0 owed · 2 path-less`, with an empty commit and a merge, both carrying
  the trailer, below HEAD.
  Red when: either commit is reported as J1, which is the behaviour at `8db6f4be`, or the merge is
  not counted.
  figure: the count is DERIVED by the join from the fixture's history at run time.
- **AC3** — When the same `red-fix-join` plant runs, its `refusal · a commit that touches no path`
  case prints exit 1 and an unchanged record count, and the door's text holds
  `owes no red-fix record`.
  Red when: the door writes a record with an empty `Files`, or refuses without stating the rule.
- **AC4** — When the same `red-fix-join` plant runs, its `J2, a record naming a path-less commit`
  case prints exit 1 and one `· J2 ·` line naming the record and the empty commit's sha.
  Red when: the join accepts a record for a commit that owes none.
- **AC5** — When `grep -c 'path-less' tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md help/red-fix-lane.md`
  runs, every count is at least 1, and the counts of `memory/HYGIENE.md` and of its template are
  equal.
  Red when: the rendered document was edited in place and the template was not, or the help page
  still shows the summary line without its last field.
- **AC6** — When `python tools/memory-tree/build_records.py join red-fix` runs in this repository,
  it exits 0 and its last line ends with a `path-less` count.
  Red when: the summary field is missing, or this history holds a fix the change now misreads.
  figure: the counts on the line are DERIVED from this tree's history at run time.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `docs` · `policy fixtures` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit; no pass of this unit runs one. The
`memory hygiene` leg runs the changed join as its check 31. The `docs` leg grades the help page's
usage anchor. `policy fixtures` guards the changed module. `memory-hygiene self-test` is in the held
tier, and the main loop runs it on a frozen clone.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 · the suite's existing assertion on the `red-fix-join` plant's PASS line, moved by the plant's five new cases; staged by restoring the join's fix set to every trailer commit, which fails the `path-less below HEAD` case · none, no assertion is added

## 8. Open questions

- **F1 — What does a path-less `Red-fix:` commit owe?** The ask leaves the choice to this build,
  and the aNimbleMend specs did not make it. The code decides half: the lane's grader already
  leaves a merge outside its limits. Nothing in the code or the records decides the empty commit.
  - Option A: it owes nothing. The join holds it out of the record-owing set and names it on every
    run, and the door's refusal says so. No record grammar changes. This spec is written to A.
  - Option B: it owes a record like any fix, whose `Files` reads `none`. The door writes that
    value and J4 compares against it. Every trailer keeps one record, at the cost of a second
    `Files` grammar in `memory/HYGIENE.md`, and a merge that carries the trailer then owes a
    record whose `Files` says `none` whatever the merge changed.
  - Option C: the commit gate refuses the trailer on a path-less commit. It is TOOL-aNimbleMend-8's
    surface, it cannot reach a commit already in history, and so it does not close the ask alone.
  - Recommendation: A. It is the one option under which no record states something false, it adds
    no grammar, and it agrees with the grader's own treatment of a merge.
  RESOLVED (owner, 2026-11-13): A, a path-less fix commit owes nothing. The join holds it out by name and the door says why it refuses.

## 9. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 10. Reuse audit

The seam is the join and its plant, extended in place. `python tools/codebase-map/reuse_lookup.py
"a fix commit that touches no path joined to its red-fix record"` ranked `read_routed_commits` of
`tools/memory-tree/routed_commits.py` and `read_records` and `write_record` of
`tools/memory-tree/build_records.py` as seams, and reading both files confirms it: the join already
holds each commit's `paths` list from the one log pass, so the split needs no new read, and the
plant's `check_case`, `write_commit` and `run_door` helpers stage every new case. For a typed
exemption of a commit from a join, no existing seam fits and none is built: the set is derived from
the history. The probe was checked against the code on a scratch repository at `82ceaab5`: an
empty trailer commit and a trailer merge both read with an empty `paths` list, the door refused
the first with exit 1, and the join reported both as J1 once below HEAD. Recall returned the ask,
TOOL-aNimbleMend-23, and the specs of TOOL-aNimbleMend-8, TOOL-aNimbleMend-9 and
TOOL-aNimbleMend-10; none states a rule for a path-less commit, and TOOL-aNimbleMend-9 §4 says a
merge's trailer is read like any other, which this unit's rule replaces for the join.

Recall terms used: `python tools/memory-recall/query.py "what does a Red-fix commit that touches no
path owe, a merge or an empty commit, and how does the join grade it" --terms "red-fix join record
door Files J1 merge empty commit trailer routed_commits lane limits non-merge path-less"`
