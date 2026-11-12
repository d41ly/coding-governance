# TOOL-aNimbleMend-9 — the red-fix record: a typed kind written after the fix and joined to its commit

**Status:** INPROGRESS · rev-2 · 2026-11-12 · node a · Tier-2 · base 1265772c · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-9-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-9-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

An inline red fix has no spec, so its only account is the record written after it. This unit gives
that record a typed kind with a door that derives what it can from the fix commit, and a hygiene
check that joins every `Red-fix:` commit to its record in both directions.

## 2. Scope (IN)

- **S1** — A fifth typed kind, `red-fix`, in `tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS` and
  in `tools/memory-tree/build_records.py#KINDS`, with the required fields of §4, "Data model". The
  bindings reader then joins the kind to its file name both ways with no further change. Observed
  by AC1.
- **S2** — A door, `build_records.py new red-fix`, that writes the next record of the kind through
  `build_records.py#write_record`. It takes the build, the unit, the leg, the red line, the commit
  and the re-run. It derives `Files` and the full `Commit` sha from the commit, and it refuses a
  commit that does not carry a `Red-fix:` trailer naming that leg. Observed by AC2 and AC3.
- **S3** — A join, `build_records.py join red-fix`, over every commit reachable from HEAD that
  carries a `Red-fix:` trailer and every tracked `red-fix` record. Its findings are the six rows of
  §4, "The join". A fix commit at HEAD with no record is printed as owed and is not a finding in the
  full form. Observed by AC4, AC5 and AC6.
- **S4** — The join's `--staged` form, which grades HEAD alone: a HEAD that carries the trailer and
  has no record in the index is a finding, so the commit after a fix is its record's commit or is
  refused. Observed by AC6.
- **S5** — Hygiene check 31 in `tools/memory-tree/check-memory-hygiene.sh`, which delegates to the
  join as check 30 delegates to `--check-asbuilt`, passes `--staged` through, and is selectable by
  `--only 31`. Observed by AC7.
- **S6** — The kind and the check are stated in `tools/memory-tree/HYGIENE.template.md`, and
  `memory/HYGIENE.md` is re-rendered from it: `red-fix` joins the closed kind list under "Record
  bindings", a "Red-fix records" paragraph states the fields, and the check list gains item 31.
  Observed by AC8.
- **S7** — A fixture, `build_records.py --fixture --plant red-fix-join`, that stages the door's
  refusals and each of the join's findings in a scratch repository and prints one line per case.
  The `typed-kinds` plant gains the new door's flags in `DOOR_ARGV`. Observed by AC1 to AC6.

## 3. Non-goals (OUT)

- Admitting the fix. Whether a write or a commit may carry the trailer, and whether the named leg is
  an open red, is TOOL-aNimbleMend-8's. This unit reads a trailer that is already on a commit.
- Grading what the fix touched. The size bound and the refused paths are TOOL-aNimbleMend-10's.
- A record written in the fix's own commit. The record names the commit by sha, and a commit cannot
  hold its own sha, so the record is always the next commit. The prompt allows either.
- Running the leg. The door records the re-run the caller names and runs nothing.
- Reading a policy key. A fix commit that landed while the lane was on still owes its record after
  the lane is turned off, so the join grades whatever history holds and asks no switch.
- A page under `help/`. The lane's page is TOOL-aNimbleMend-11's.
- The kit version, which the lander's `mint` moves once, after the last unit.

### Edges

- **consumes-from** `TOOL-aNimbleMend-8` — the `Red-fix:` trailer on the fix commit, one leg name
  per trailer line, and its read: the `red_fix` list `read_routed_commits` returns per commit.
  Without it no commit is in the join's population and the door refuses every commit.

## 4. Design

### Data model

One record is `<date>-build-<unit id>-red-fix-<n>.md` in a build's `build/` folder, headed and
bound by `write_record` as every typed kind is. Its fields are bold-key bullets read by
`build_records.py#FIELD`, each one line.

| Field | Holds | Source |
|---|---|---|
| `Leg` | the leg's `name` as the trailer spells it | `--leg`, compared with the commit's trailer |
| `Red line` | the line of the failure record or pass-leg run the fix clears | `--red-line` |
| `Files` | the commit's paths, sorted, joined by a comma and a space | derived from the commit |
| `Commit` | the fix commit's full 40-hex sha | `--commit`, resolved |
| `Rerun` | the command that showed the leg green and its result | `--rerun` |
| `Caused-by` | the unit id | `--unit` |

All six are required. No field has a closed set. `Commit` is 40 lowercase hex, checked on read.
`FIELD` admits a capitalised word and one lower-case word, which is why the re-run field is one
word.

### The door

```
python tools/memory-tree/build_records.py new red-fix --build <slug> --unit <id> \
    --leg "<leg name>" --red-line "<line>" --commit <rev> --rerun "<command · result>"
```

It resolves `<rev>` to a commit reachable from HEAD, reads that commit's `red_fix` values and
its paths through `routed_commits.py#read_routed_commits` over that one commit, and refuses, exit 1 and writing nothing, when the rev names no such
commit, when the commit carries no `Red-fix:` trailer, when no trailer value equals `--leg`, or
when a text flag is empty. `write_record` already refuses a value that holds a line break or forges
a field, a build that is no folder of this tree, and a unit that is no id.

The record's unit is the caller's: the unit whose pass the red followed, or for a red at the close
the unit the fix commit names. The door checks that it is an id and nothing more, as every door
does. F1 asks what a fix made outside any build names.

### The join

```
python tools/memory-tree/build_records.py join red-fix [--staged] [--root <path>]
```

The full form calls `routed_commits.py#read_routed_commits` over HEAD, which is one `git log`
pass, and keeps the commits whose `red_fix` list is not empty. TOOL-aNimbleMend-8 adds that list
and the trailer's one spelling, `RED_FIX_TRAILER` in `tree_lib.py`, so this unit holds no format
string and no second parse of the trailer. The module is imported inside the join, as
`routed_commits.py` imports `deviation_join` inside its host, so no import cycle forms at load.
Records are read by `build_records.py#read_records`, so the population is the tracked one and a
staged record counts.

Each trailer value of a commit owes one record whose `Commit` is that sha and whose `Leg` is that
value.

| # | Finding | Names |
|---|---|---|
| J1 | a fix commit below HEAD has a trailer value no record answers | the sha and the leg |
| J2 | a record's `Commit` is no commit in the population | the record and the sha |
| J3 | a record's `Leg` is no trailer value of its commit | the record, the leg and the commit's legs |
| J4 | a record's `Files` differs from the commit's derived list | the record and both lists |
| J5 | two records answer one commit and leg | both records |
| J6 | a record is malformed by `read_record` | the record and each refusal |

Exit 0 clean, 1 on any finding, 2 when `git` fails or the tracked population cannot be read. The
last line is always a summary, which is the check's liveness:

```
build-records: red-fix join · <N> fix commit(s) · <M> record(s) · <K> owed
```

A trailer value at HEAD with no record prints `build-records: red-fix join · owed · <sha8> ·
<leg>` and counts in `<K>`, with exit 0. It is owed and not late, because the record is the next
commit and a pass leg that runs hygiene between the two must not red on it.

The `--staged` form reads HEAD alone, through the same reader limited to one commit. HEAD with a trailer value that no
record in the index answers is J1, exit 1. HEAD with no trailer prints one held line and exits 0.
Check 31 delegates in both forms, so the trailer is spelled in the kit's Python alone.

### What the join does not check

- That the record was added by the fix's direct child. The full form accepts a record added any
  number of commits later. Promptness is the `--staged` form's, at the pre-commit hook, and a clone
  with no hook has no such check.
- That `Rerun` is true, or that `Red line` was ever printed. Both are the caller's words.
- That the leg was red. TOOL-aNimbleMend-8 admits the trailer.
- A merge commit's own trailer is read like any other commit's; nothing is special-cased.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| kind `red-fix` | `TYPED_RECORD_KINDS`, `KINDS`, `DOORS` | the import-time table compare in `build_records.py` |
| door flags `--leg`, `--red-line`, `--commit`, `--rerun` | `build_records.py#main` | the `typed-kinds` plant's foreign-flag refusals |
| verb `join` | `build_records.py#main` | AC4 to AC6 |
| plant `red-fix-join` | `build_records.py#PLANTS` | AC2 to AC6 |
| functions `read_red_fix`, `write_red_fix`, `check_red_fix_join` | `build_records.py` | the `lexicon naming predicates` leg |
| hygiene check 31 | `check-memory-hygiene.sh` | AC7 |

### Migration

Additive. A tree with no `Red-fix:` commit and no `red-fix` record gains one summary line under
check 31 and no finding. No landed record changes kind.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`

### Alternatives rejected

- **The deviation kind with a new `Cause`.** A deviation departs from a clause or a spec revision
  and its `Departs from` field is graded against one. A red fix departs from neither, so every
  record would be malformed or would name a fictitious clause.
- **Hosting the join in `routed_commits.py` beside the deviation join.** That host lists and never
  moves the exit, and it runs only where the routed-commits leg runs. The roster asks for a hygiene
  check, which also gives the `--staged` form its place at the pre-commit hook.
- **A `--files` flag.** The commit already holds the list, so a typed copy is one fact twice. The
  door derives it and J4 re-derives it.
- **A record in the fix's own commit, named by a placeholder.** It could not name its commit or a
  re-run made after it, and the join would need a second rule for it.

## 5. Production-readiness checklist

- security — the door is a write path into the memory tree. Every value is validated at the door,
  `write_record` refuses a forged field and never overwrites, and the commit is resolved by `git`,
  never spliced into a shell string.
- perf / scale — the full join is one `git log` pass over HEAD, the read the routed-commits leg
  already makes, and the staged form reads one commit.
- error / empty / loading states — an empty population prints the summary line with zeros; a `git`
  failure is exit 2 and a check-31 failure, never a clean read.
- observability — the summary line on every run, one line per finding, one per owed record.
- risks — a tree with a long history pays the whole-history log on every full hygiene run. A
  kind name holding a hyphen is new to
  `TYPED_RECORD_KINDS`; AC1 observes the name grammar reads it.
- testing — the `red-fix-join` plant stages every finding and refusal; the hygiene suite gains the
  arms of §7.
- migration — additive; see §4, "Migration".
- user docs — `memory/HYGIENE.md` through its template is S6. The help page is
  TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` runs, it
  prints a line `build-records: typed-kinds · red-fix ·` ending `· bound`, and its PASS line counts
  5 typed kinds.
  Red when: `red-fix` is missing from `TYPED_RECORD_KINDS` or from `KINDS`, which is an
  `ImportError`, or the hyphen in the kind breaks the name grammar and the record reads malformed.
  figure: 5 is DERIVED by the plant from the tuple at run time; it prints 4 at 1265772c.
- **AC2** — When `python tools/memory-tree/build_records.py --fixture --plant red-fix-join` runs,
  its `door` case prints the written record's `Commit` as the fixture commit's 40-hex sha and its
  `Files` as that commit's two paths in sorted order, with only an abbreviated rev passed in.
  Red when: the door stores the rev as typed, or takes the file list from a flag.
- **AC3** — When the same `red-fix-join` plant runs, its three `refusal` cases each print exit 1
  and an unchanged record count: a commit with no `Red-fix:` trailer, a `--leg` no trailer names,
  and a rev that names no commit.
  Red when: the door writes a record for a commit that is not a fix of that leg.
- **AC4** — When the `red-fix-join` plant runs `join red-fix` over one fix commit and its record,
  the case prints exit 0 and the summary `1 fix commit(s) · 1 record(s) · 0 owed`.
  Red when: the join reads no trailer, or reads no record, and so reports a zero on either side.
- **AC5** — When the `red-fix-join` plant stages each of J1 to J6 in turn, each case prints exit 1
  and the finding's row number with the sha or record it names; J1 is staged by committing once
  more on top of an unrecorded fix.
  Red when: any one finding is not raised, or is raised without naming its subject.
- **AC6** — When the `red-fix-join` plant leaves an unrecorded fix at HEAD, `join red-fix` prints
  the `owed` line and exits 0, `join red-fix --staged` exits 1 naming the sha, and after
  `git add` of its record `--staged` exits 0.
  Red when: the full form reds on a fix whose record is not yet due, or the staged form lets a
  commit follow an unrecorded fix.
- **AC7** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 31` runs in this
  repository, it prints one `check 31:` line carrying the join's summary and exits 0.
  Red when: the check is not wired, or `--only` does not select it.
  figure: the counts on the line are DERIVED from this tree's history at run time.
- **AC8** — When `grep -c 'red-fix' memory/HYGIENE.md tools/memory-tree/HYGIENE.template.md` runs,
  both counts are at least 3, and `diff <(tail -n +2 memory/HYGIENE.md) <(tail -n +2
  tools/memory-tree/HYGIENE.template.md)` shows no line naming `red-fix` on one side only.
  Red when: the rendered doc was edited in place and the template was not, or the kind list, the
  field paragraph or item 31 is missing.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit`

The close's bar runs these once, after the last unit. `kit/dogfood doc parity`, `recall floor` and
`recall floor arms` guard `memory/HYGIENE.md`. `memory-hygiene self-test` holds the new arms and is
in the held tier, so the close runs it only where it asks for that tier. `memory hygiene` runs the
new check 31 itself.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 AC4 AC5 AC6 · the `red-fix-join` plant's staged cases, each finding and refusal · the suite's assertion-count floor, raised by the arms added

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC7 · a fixture tree holding an unrecorded fix below HEAD, which check 31 must fail · the same floor

## 8. Open questions

- **F1 — What does the record of a red fixed outside any open build name?** `write_record` needs a
  build folder and a unit id, and the bindings reader resolves the id against a spec H1. A red at a
  push boundary with no build open has neither to hand.
  - Option A: the record goes in any existing build folder, under a unit of it, at the caller's
    choice: the build whose unit last changed the fixed file. No new home and no new code.
  - Option B: a standing build folder for red fixes, with one standing unit and spec. It needs a
    spec that is never built and a slug the adopter must create.
  - Option C: the lane is closed outside a build, so the question does not arise. That is
    TOOL-aNimbleMend-8's admission rule, not this unit's.
  - Recommendation: A. It is what the door does with no change, and the join grades the commit and
    the record, never which unit the record sits under.
  RESOLVED (agent, 2026-11-12, delegated): A. The record sits under a unit of the build whose unit last changed the fixed file, which the door does with no change.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

The seam is the typed record factory. `python tools/codebase-map/reuse_lookup.py "a typed record
written after a fix and joined to its commit by a hygiene check"` ranked `write_record` and
`read_records` of `tools/memory-tree/build_records.py` as seams, and reading the file confirms it:
a kind is one `KINDS` row, one member of `tree_lib.py#TYPED_RECORD_KINDS`, a `write_<kind>` door
and a `read_<kind>` reader, three times over already. The join's shape is check 30's delegation in
`check-memory-hygiene.sh`, and its trailer read is `routed_commits.py#read_routed_commits` with
the `red_fix` list TOOL-aNimbleMend-8 adds. For joining a record to a commit by a trailer, no existing
seam fits: the deviation join in `deviation_join.py` joins a record to a clause or a spec revision,
and `tree_lib.py#read_adding_commits` answers which commit added a path, not which commit a record
names. Recall returned the factory's own specs, PLAY-dOrderedCharter-7 and PLAY-dOrderedCharter-42,
and PLAY-dOrderedCharter-59, the loose-stem defect whose fix, `derive_record_name`, this kind
inherits. It also returned `record_kinds.py`, a registry TOOL-dTotalRecall-1 specs; no such file is
in the tree at 1265772c, so the stale hit is not built on.

Recall terms used: `python tools/memory-recall/query.py "how is a typed build record joined to the
commit it describes and how is a commit graded for what it may touch" --terms "typed record kind
build_records deviation join routed commits trailer hygiene check guarded-paths red fix inline lane
size bound"`
