# TOOL-aMendedFleet-52 — the hand-kept signal compares the drift README's signal names against the names the engine reports

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 52

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`handkept_inventories_disagreeing_with_source` exists to catch a hand-kept list drifting from what
generates it, and it has graded nothing since its one row went with the charter section it read: it
is declared empty. Meanwhile the drift-audit README's own signal table omits two of the nineteen
signals the engine reports, and the Skill keeps a second table of six. This unit re-arms the signal
on the one hand-kept list the kit itself owns: the README table's signal names are compared, as a
SET, with the names the engine's `SIGNALS` actually report, so a signal added without a README row,
or a row left behind by a deleted signal, reds `drift-audit records`. The Skill's second table goes,
replaced by a pointer, so there is one list to keep.

## 2. Scope (IN)

- **S1** — SET-VALUED PROBES. `signal_handkept` in `tools/drift-audit/drift_report.py` accepts a
  probe returning two sets as `(claims, actual)`. Such a row scores the size of their symmetric
  difference as its gap and the size of their union as its population, and its detail row carries
  `missing`, the sorted names in `actual` and not in `claims`, and `extra`, the sorted names in
  `claims` and not in `actual`, with `claims` and `actual` written as counts so `--json`
  serialises. A probe returning integers is scored as today. Observed by AC1, AC2, AC3.
- **S2** — THE NAMES THE ENGINE REPORTS. `main` evaluates every `SIGNALS` entry except
  `signal_handkept`, sets `ctx.signal_names` to the set of `signal` values they returned plus the
  hand-kept signal's own name, then evaluates `signal_handkept`, and emits the records in `SIGNALS`
  order, so the table and the JSON keep their order. A caller that never sets `ctx.signal_names`
  makes the probe raise, which `signal_handkept` already reports as an error row. Observed by AC1.
- **S3** — THE ROW. `HANDKEPT` in `tools/drift-audit/drift_signals.py` gains one row whose probe,
  `read_signal_table_names`, reads the README beside that file, takes the first-column backticked
  names of the table under the `## The signals` heading and nothing after the next heading of ANY
  level, and returns them with `ctx.signal_names`. The bound matters: a later table in the same
  README holds the harness note states `clean`, `partial` and `dead`, and a whole-file read counts
  them as three extra signals; that table sits under a `### ` subheading INSIDE the `## The signals`
  section, so a bound at the next `## ` heading counts them too. Observed by AC1, AC3.
- **S4** — The hand-kept signal is no longer empty by declaration: its name leaves
  `DECLARED_EMPTY` in `tools/drift-audit/drift_signals.py`, and the comment above `HANDKEPT` says
  what the row grades. Its pin stays 0 and its existing `RATCHETS` row stays. Observed by AC1.
  **Readers:** by name: `tools/drift-audit/drift_report.py` reads `DECLARED_EMPTY` in `main`, for
  `--check`'s dead filter and the human table's `empty by declaration` status. by value: those two
  readers consult the set only for a record whose `live` is false, and S3 makes this one live.
- **S5** — The README's `## The signals` table gains the two rows it lacks today,
  `lexicon_marginal_offense_rate` and `source_cited_ids_resolving_to_no_record`, so the signal
  reads 0 on the commit that arms it. Observed by AC1.
- **S6** — The Skill keeps one list, not two. The six-row signal table in
  `tools/drift-audit/SKILL.template.md` is dropped for one sentence pointing at the README's
  `## The signals` section and at `--json`, which names every signal the engine reports, and
  `.claude/skills/drift-audit/SKILL.md` is re-rendered by `bash tools/drift-audit/adopt-drift-audit.sh`.
  Observed by AC4.
  **Readers:** by name: `tools/drift-audit/adopt-drift-audit.sh` spells `SKILL.template.md`, renders
  it, and diffs the render under `--check`. by value: NO VALUE READERS — no program parses the
  table's rows; agents read them as prose.
- **S7** — Self-test arms in `tools/drift-audit/selftest.py` over a fixture project layer whose
  `HANDKEPT` row returns sets: equal sets read value 0 and live; a name missing from the claims and
  a stale extra name each count one and appear in `missing` and `extra`; and the existing arm that
  asserts an empty `HANDKEPT` reads as declared keeps passing. NOT OBSERVED by a criterion here: the
  suite runs once at the close, and the arms are declared under `New arm:` in §7.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.

## 3. Non-goals (OUT)

- Shipping the row in `tools/drift-audit/drift_signals.template.py`. An adopter's project layer is
  theirs; the template keeps `HANDKEPT` empty and a follow-up can offer the row as an example.
- Comparing the README's `Gateable` column with each record's `gateable` field. Names first; a
  second column is a second comparison and a follow-up.
- Any other hand-kept table: the charter, the layout table and the kickoff manifest are not graded
  here.
- Bumping the drift-audit kit version, owed once at the close.

### Edges

- **hands-off** external — every later unit that adds a signal owes its README row in the same
  commit, or `drift-audit records` reds on it; units 8, 21 and 37 before this unit, and units 54,
  55 and 92 after it, already name that row in their scope.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `fee9f62b`, whose bytes under `tools/` and `.claude/` equal base
`7af5f564`'s.

- `HANDKEPT` is `[]` and `DECLARED_EMPTY` names `handkept_inventories_disagreeing_with_source`; the
  report prints that signal as `empty by declaration`.
- `python tools/drift-audit/drift_report.py --json` returned 19 records. The README's signal table
  carries 17 names and lacks `lexicon_marginal_offense_rate` and
  `source_cited_ids_resolving_to_no_record`; the Skill's table carries 6. A scratch probe compared
  the name sets. PINNED, measured 2026-10-04, matching the source synthesis's 2 of 19 and 6 of 19.
- A whole-file read of the README returned 20 names, three of them `clean`, `partial` and `dead`
  from the harness-note table under a later heading, which is why S3 bounds the section. That
  heading is `### The harness note is a DERIVED contract, not prose`, a subsection of `## The
  signals`, so the bound is the next heading of any level (re-read at the build, rev-3).
- `signal_handkept` counts an integer pair by `max(0, actual - claims)`, and any other pair as one
  offender when the two differ, so a set pair today scores at most 1 and names nothing.
- Node d's live branch adds three signals and three README rows; after its reconcile the set
  comparison holds if both halves arrive together, which they do on that branch.

### Inventory

- `read_signal_table_names` — cell `py.function`; answered OK from
  `python tools/lexicon/lexicon.py --suggest read_signal_table_names --as py.function`.
- `ctx.signal_names` — an attribute of `Ctx`, set in `main`; no naming cell grades attributes.

### Rollout

Units 8, 21 and 37 each add a signal and a README row and are ordered before this unit, so the set
compares equal when this lands; a sibling that forgot its row reds here, at the right commit. Unit
51 edits the same two files and is ordered first.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `tools/drift-audit/SKILL.template.md`
- `.claude/skills/drift-audit/SKILL.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Return counts from the probe.** `(17, 19)` scores 2 today but cannot see a stale row standing in
  for a missing one: an extra name and a missing name cancel to equal counts.
- **Derive the names statically from the engine source.** A signal's name is a string built in each
  builder, sometimes through a local variable or a helper; a source scan would be a second parser
  with its own blind spots, and running the signals already yields the names.
- **Keep the Skill's table and grade it too.** Two lists of one fact is the defect; the Skill points.

## 5. Production-readiness checklist

- security — N/A: reads a tracked README beside the project layer; no new input.
- perf / scale — one file read; S2 reorders evaluation and adds no signal run.
- error / empty / loading states — a README with no `## The signals` heading returns an empty set,
  which reads every engine name as `missing` rather than passing; a probe without `ctx.signal_names`
  raises into the existing error row.
- observability — `missing` and `extra` name the exact row to add or delete.
- risks — the signal is gateable at pin 0 on an unguarded leg, so a unit that adds a signal without
  its README row reds the bar; that is the intent, and every such unit's spec can name the row.
- testing — AC1 to AC4 here; the arms in S7.
- migration — N/A: nothing stored changes.
- user docs — S5 and S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs at the worktree root, the
  `handkept_inventories_disagreeing_with_source` record has `live` true, `value` 0, and an `of`
  equal to the number of records in that same JSON array.
  Red when: the README omits a reported signal, or the probe counts the harness-note states.
  figure: DERIVED at observation time; 19 records at writing.
- **AC2** — When the `readme_mechanism_drift` row is deleted from `tools/drift-audit/README.md` in
  the working tree and `python tools/drift-audit/drift_report.py --offenders` runs, it prints a line
  opening with `handkept_inventories_disagreeing_with_source` whose detail key carries
  `readme_mechanism_drift` under `missing`; restoring the row removes that line.
  Red when: a signal can lose its README row with no offender.
- **AC3** — When a row naming `no_such_signal` is added to that table in the working tree and
  `python tools/drift-audit/drift_report.py --json` runs, the hand-kept record's detail lists
  `no_such_signal` under `extra` and its `value` is 1; restoring the README returns it to 0.
  Red when: a stale row naming a signal the engine does not report passes.
- **AC4** — When `grep -c "^| Signal | Asks |" tools/drift-audit/SKILL.template.md` runs it reports
  0, and `bash tools/drift-audit/adopt-drift-audit.sh --check` exits 0.
  Red when: the Skill keeps its own table, or its render is stale.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `check-wiring self-test` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a fixture `HANDKEPT` row returning equal sets, then a set missing one name, then a set with one stale name · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — Where do the names the engine reports come from?
  Options: run every signal twice; parse the engine's source; evaluate the hand-kept signal last and
  hand it the names the others returned. Running twice doubles a report that already takes tens of
  seconds on node a; parsing source is the static derivation §4 rejects.
  RESOLVED (agent, 2026-10-04, delegated): evaluate it last, per S2, keeping the output order.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#58] and a probe of the README,
  Skill and engine name sets at base.
- rev-2 · 2026-10-04 · §3 · §4 · S8 · §7 · M2 cross-read: the Edges line and the Rollout named units
  8 and 37 as the earlier signal-adding units, but `TOOL-aMendedFleet-21` adds `cutoff_keys_armed`
  and its README row before this unit too, and units 54, 55 and 92 add rows after it; and the new
  definition owes `symbols.json`, which units 57, 59 and 90 regenerate for theirs and this spec
  omitted.
- rev-3 · 2026-10-05 · S3 · §4 · build: S3 bounded the table at the next `## ` heading, but the
  harness-note table sits under a `### ` subheading inside `## The signals`, so that bound still
  counts `clean`, `partial` and `dead`; the bound is the next heading of any level. Re-measured at
  the build: the engine reports 22 signals and the README table names 20, lacking exactly the two
  S5 adds.

## 10. Reuse audit

The seams extended are `signal_handkept` and its probe protocol in
`tools/drift-audit/drift_report.py`, the `HANDKEPT` and `DECLARED_EMPTY` declarations in
`tools/drift-audit/drift_signals.py`, where `_charter_mentions_every_leg` is the retired probe this
row replaces, and the render-and-diff of `tools/drift-audit/adopt-drift-audit.sh`.
`python tools/codebase-map/reuse_lookup.py "compare a hand-kept README table of names against the
set a registry generates"` returned `resolve_pattern_sets` in the lexicon kit and
`test_generated_artifacts_are_fresh` in the codebase-map tests, which compare other artifacts, and
prose seams naming `check-testsuite-counts.sh`, which grades suite counts rather than names; no
existing seam fits the name-set comparison, so it lives in the probe protocol that already exists
for it. The scan names `.sh` as unscanned, and the one shell file involved is the adopter, which
this unit only re-runs. Recall returned `TOOL-aMendedLedger-3`, the rule that a drained gateable
probe goes to `DECLARED_EMPTY` and comes back live when a row returns, which S4 follows, and
`TOOL-aKeyedAnnotation-12`, on asserting a signal's liveness. Where the report and the tree
disagree: nowhere; 2 of 19 and 6 of 19 re-measured exactly.

Recall terms used: `python tools/memory-recall/query.py "why was the hand-kept inventory signal
emptied and how should it compare the README table" --terms "handkept_inventories_disagreeing_with_source
HANDKEPT DECLARED_EMPTY drift-audit README signal table SIGNALS Skill name-set"`
