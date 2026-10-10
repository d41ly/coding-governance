# DEPL-aLevelledCopy-1 — govkit update carries gov's exec bit onto an existing engine row

**Status:** CLOSED · rev-3 · 2026-10-09 · node a · Tier-2 · base ce9192c0 · streams deployer · order 1 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-DEPL-aLevelledCopy-1-1-acceptance-ledger.md](../build/2026-10-09-build-DEPL-aLevelledCopy-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-10-build-DEPL-aLevelledCopy-1-runlog-9380159b.md](../build/2026-10-10-build-DEPL-aLevelledCopy-1-runlog-9380159b.md) | journal | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9 |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md) | journal | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md) | journal | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1.md) | research | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 |
| [2026-10-09-review-TOOL-aLevelledCopy-1-closing-diff-round1.md](../reviews/2026-10-09-review-TOOL-aLevelledCopy-1-closing-diff-round1.md) | diff-review | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit update` lands an engine row through `land_through_index`, which takes the file mode from
the target's EXISTING index entry whenever one exists, and from gov's tree only for a row with none.
So `.githooks/pre-push`, an `engine` row in both adopters and tracked 100644 there today, stays
100644 forever, even once gov ships it 100755; on a POSIX node git then never runs it. And when gov
changes only a MODE, update's verdict grid sees equal blobs and never reaches a write at all. This
unit makes update carry gov's executable bit onto an existing engine row, upgrade only, reports the
carry in its read-only run so the adoption session's dry run predicts it, and records the decision
the owner's clarification asked for. The aScouredKit wave-3 cross-OS lens recorded the defect on
2026-08-31; no unit built it.

## 2. Scope (IN)

- **S1 — one mode rule, upgrade only.** A new `resolve_landed_mode(entry_mode, gov_mode)` in
  `tools/govkit/govkit.py` returns the mode a landed engine row takes. Observed by AC1, AC2, AC6.

  | target index entry | gov's mode at the target commit | result |
  |---|---|---|
  | none | any | gov's mode, else `100644` (today's §8 F1 rule, unchanged) |
  | `100644` | `100755` | `100755` — the carry |
  | `100755` | `100644` | `100755` — never a downgrade |
  | `120000`, or gov `120000` | any | the entry's mode — symlinks are untouched |
  | equal | equal | unchanged |

  `land_through_index` takes its mode from this rule in place of its current expression. Its three
  callers, the raw-write, `renamed` and clean-`diverged` arms, all sit under the `table` disposition,
  which `UPDATE_ROLE` gives to `engine` alone (verified 2026-10-09). So the rule reaches no
  `merged`, `seed`, `project-owned`, `generated`, `rendered` or `attributes` row by construction,
  not by a guard.
- **S2 — gov's modes, read once.** A new `read_tree_modes(root, commit)` returns `{path: mode}` for
  a whole commit from ONE `git ls-tree -r -z`, memoised per commit. `gov_tree_mode` becomes a lookup
  through it, so there is one reader of gov's modes rather than two. Observed by AC7.
- **S3 — the mode-only row joins the update flow.** After `classify_row`, for every `table` row
  with an index entry, the loop asks S1 with gov's mode at `to_commit` for the row's source, or for
  the NEW source on a `renamed` row. When the rule changes the entry's mode, the acted entry carries
  `mode_to`, and the run prints one line per such row, outside the row-line shape:
  `govkit update — mode-carry <path> · <old> -> <new> · gov at <to8>`. The verdict word is NOT
  changed: the bytes are what the verdict says they are, and verdict lines are parsed by their
  trailing path elsewhere, so a second line about the path is the lone-CR finding's precedent rather
  than a new row shape. Observed by AC1, AC4.
- **S4 — `--write` applies it, and a rollback restores it.** A row whose verdict lands bytes
  through `land_through_index` takes the mode there (S1). A row whose verdict lands no bytes, such as
  `current`, `patched` or a `carried` one, gets `git update-index --cacheinfo
  <mode_to>,<ours_oid>,<path>` and `os.chmod` adding the execute bits to the working file. The
  snapshot predicate that builds `snap_rows` admits a row carrying `mode_to` beside the touching
  verdicts, so its kit is in `touched_kits`, is verified after the write, and a rollback restores
  the pre-run entry, mode included. Observed by AC1, AC3, AC4, AC5.
- **S5 — `govkit check` notes a mode deficit, and never fails on one** (§8 F2). For each engine
  row, `cmd_check` compares the target's index mode with gov's mode at the RECEIPT's `gov_commit`
  through S1, and a row the rule would change gets one `r.note` naming the path, both modes and the
  remedy, `govkit update --write`. It reads the index with one batched `index_read` and gov's modes
  with S2, one spawn in all. rev-2: not the row's own `commit`, because `update` re-stamps a row's
  `commit` only where it lands bytes, so after a mode-only carry the row still names the commit its
  bytes came from, where gov ships `100644`, and AC8 could never see the deficit. Observed by AC8.
- **S6 — the receipt is unchanged, said where the writer is.** A receipt row records `sha256`,
  `oid`, `gov_oid` and `commit`, and no file mode: the `mode` key on a `merged` or `attributes` row
  is its block-insertion mode, not a file mode (verified 2026-10-09 against the row builders). So no
  receipt field, schema or re-stamp changes, and the docstring of `land_through_index` says the
  mode rule lives in S1. NOT OBSERVED by a criterion, because it is an absence of change; AC1's
  second read-only run is its practical witness.

## 3. Non-goals (OUT)

- **Any non-engine role.** A `merged` row such as `.githooks/pre-commit` is the adopter's file and
  keeps the adopter's mode; `TOOL-aLevelledCopy-3`'s `check-wiring.sh --fix` is what repairs an
  adopter's own hook.
- **A downgrade.** An adopter that set a bit gov lacks keeps it (§8 F1).
- **`govkit apply`'s first install.** It writes bytes with `write_bytes` and sets no mode, so a
  fresh target's first `git add` decides the mode. This unit changes `update` only; the §3 Edges
  hand-off names the follow-up.
- **The receipt schema** (S6) and **the kit-version bump**, which happens once after the last unit.

### Edges

- **consumes-from** external — gov's four executed hooks at 100755, the real-world input this unit
  carries to adopters; this build's TOOL-aLevelledCopy-3 ships them, at a later `order`. The fixtures
  build their own gov tree, so no criterion here rests on that unit, and the edge is not a sibling join.
- **hands-off** external — `govkit apply` landing a new engine row at gov's mode; filed as an ask at
  the close.

## 4. Design

### Where the mode-only row joins the flow

`classify_row` keys its OURS and THEIRS states on blob identity, so a mode-only delta lands in the
`("equal", "equal")` cell, `current`, and no write arm runs. S3 does not add a grid cell, because a
mode is not a byte question and `VERDICT_GRID` is asserted complete by `selfcheck`; it adds one
field to the acted entry, decided from the same `index0` read the classifier already holds. The
write loop's existing arms are unchanged; S4 adds one arm after them for a `mode_to` the bytes arm
did not already apply.

### Cost

A git spawn costs about 0.75 s on node a (PINNED, measured 2026-10-02, memory note "A git spawn
costs 751ms"). Today `gov_tree_mode` spawns one `ls-tree` per row that has no index entry. S2
replaces every such read with one `ls-tree -r -z` per distinct commit: one for `update` at
`to_commit`, and for `check` one at the receipt's `gov_commit` (rev-2).
On a 190-row receipt a per-row read would cost about 140 s.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `resolve_landed_mode` | function in `govkit.py` | `py.function` |
| `read_tree_modes` | function in `govkit.py` | `py.function` |
| `mode_to` | key on an `acted` entry | not a definition; no cell |
| `check_mode_carry` | selftest function in `selftest.py` | `py.function` |
| `measure_mode_carry` | selftest function in `selftest.py`, the fixtures over a given `govkit.py` text | `py.function` |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for all three
functions on 2026-10-09.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Rollout

The govkit kit ships to adopters, so the carry takes effect on the first `govkit update --write`
after this lands, and the adoption session's read-only dry run shows each `mode-carry` line first.
Neither adopter needs a manual step. Two build traps the memory tree records: a comment sentence in
`govkit.py` naming `update` and a re-render without `GOVKIT_RERENDER` reds selfcheck 7l; and the
govkit self-test pins the common dir's HEAD, so a slice that reds on its pin in a linked worktree
is re-run from the primary before it is believed.

### Alternatives rejected

- **A new verdict word for a mode-only row.** Rejected: verdict lines are parsed by name and
  trailing path, the tally would count one row under two questions, and `VERDICT_GRID`'s
  completeness assertion would need a mode axis it does not have.
- **Carrying the mode in both directions.** Rejected at §8 F1.
- **A per-row `gov_tree_mode` call for the mode-only check.** Rejected on cost (§4 Cost).
- **A receipt field for the mode.** Rejected: gov's tree already answers it at any recorded commit,
  so a stored copy is a second spelling of a derivable fact.

## 5. Production-readiness checklist

- security — no new path: the mode write targets the same receipt-validated, containment-checked
  path the bytes arm writes, through `update-index --cacheinfo` with the oid the target already
  holds. It adds execute permission only to an engine row, and only where gov's own tree carries it.
- perf / scale — one `ls-tree -r -z` per distinct commit instead of one spawn per row (§4 Cost).
- error / empty / loading states — gov's mode unresolvable: no carry, no line. `update-index`
  refusing: `r.fail` naming the path, which holds the kit back like any other refused row.
- observability — one `mode-carry` line per row in both modes; one `check` note per deficit.
- risks — a hook gov ships 100755 now runs on POSIX nodes where it silently did not. That is the
  intended effect, and an adopter sees each line in the read-only run first.
- testing — `check_mode_carry`, a module-level selftest function so it can be run alone.
- migration — none; no receipt change.
- user docs — the `land_through_index` and `gov_tree_mode` docstrings, and `update`'s own output.

## 6. Acceptance criteria

The fixtures follow `check_update_safety`'s scratch-gov construction in `tools/govkit/selftest.py`:
a scratch gov whose `govkit.py` is a copy taken at build time, a demo kit, `SAFE_REG`, and a target
installed with `apply`. The new arms live in a module-level `check_mode_carry(tmp)` that `main`
calls, which runs `measure_mode_carry(tmp, source, arms)` over this tree's `govkit.py`; rev-2 adds
that seam so a staged copy runs the same fixtures. Two fixtures cover every arm: `cm` carries each
mode case in one update, and `rb` makes a mode carry the only change of a kit whose check reds.
Each criterion is observed by running that one function alone, under the default `%TEMP%` because
a scratchpad temp root false-reds on path length:

```bash
python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.check_mode_carry(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"
```

- **AC1** — When the demo kit's engine hook is installed at 100644 and the scratch gov's next commit
  changes only its mode to 100755, a read-only `update` prints one `mode-carry` line naming the path
  and `100644 -> 100755`, `--write` leaves `git ls-files -s` reporting 100755 with the blob
  unchanged, and a second read-only `update` prints no `mode-carry` line. Red when: the index stays
  100644, which is BASE's behaviour, observed by building the same scratch gov from the `govkit.py`
  read with `git show` at base `ce9192c0`.
- **AC2** — When the target has set 100755 on an engine row gov ships 100644 and gov changes that
  file's bytes, `--write` lands the new blob and `git ls-files -s` still reports 100755. Red when:
  the row is downgraded.
- **AC3** — When a non-`table` row, a `merged` row where the demo kit can declare one cheaply and
  otherwise a `seed` row, is tracked 100644 and gov's commit makes it 100755, read-only `update`
  prints no `mode-carry` line for it and `--write` leaves its index mode 100644. Red when: a
  non-engine row is carried.
- **AC4** — When gov's commit changes an engine row's bytes AND its mode, one `--write` leaves the
  new blob at 100755, and the read-only run before it printed both the `stale` verdict line and the
  `mode-carry` line. Red when: either half is missing after the write.
- **AC5** — When the demo kit's post-write check is made to fail and the run's only change is a
  mode carry, `--write` rolls the kit back and `git ls-files -s` reports 100644 again. Red when: the
  carried mode survives a rolled-back kit.
- **AC6** — When `resolve_landed_mode` is called over the five rows of the S1 table, from
  `check_mode_carry`, each returns the table's result. Red when: a symlink or an adopter's 100755 is
  changed.
- **AC7** — When a read-only `update` runs over a fixture receipt of five engine rows under
  `GIT_TRACE=1`, the trace shows one `ls-tree -r` at the target commit and no per-row `ls-tree`.
  Red when: the `ls-tree` count grows with the row count.
- **AC8** — When an AC1 target after `--write` has its hook returned to 100644 with
  `git update-index --chmod=-x` and `govkit check` runs, it prints one note naming the path and both modes
  and its exit status is the one it had before the edit. Red when: no note prints, or the deficit
  fails the check.
- **AC9** — When each arm's failing case is staged at build time by editing the scratch gov's
  `govkit.py` copy handed to `measure_mode_carry` — disabling the S4 mode arm for AC1, swapping
  the rule to mirror both directions for AC2 and AC6, restoring the old mode expression in
  `land_through_index` for AC4, and dropping `mode_to` from the snapshot predicate for AC5 — the
  named arm reports a failure in `s.FAILURES`. Red when: a staged break leaves its arm passing.
  rev-2: the old mode expression reds AC4 and not AC1, because a mode-only row never reaches
  `land_through_index`; its carry is the S4 arm's. The breaks are an observation recorded in the
  acceptance ledger and not committed arms, because each rebuilds a fixture.
  cost: 137 s for `check_mode_carry` on node a, measured 2026-10-09 over its eight govkit
  verbs, against about an hour for the whole suite, which this pass does not run.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · each arm's break staged in the scratch gov's copy of the deployer per AC9 · none

## 8. Open questions

- **F1 — does `update` carry gov's mode onto an EXISTING engine row, and in which direction?**
  Options: (a) mirror gov's mode both ways; (b) carry upgrade only; (c) never, which is today.
  (c) leaves the defect the owner's clarification names. (a) and (b) both deliver gov's bit; (a)
  additionally strips an execute bit an adopter set on an engine copy it runs directly, which is a
  follow-up an adopter would have to file, and it buys only symmetry. (b) satisfies every criterion
  with no follow-up. RESOLVED (agent, 2026-10-09, delegated): (b), for `engine` rows only, symlinks
  untouched.
- **F2 — should `govkit check` report a mode deficit?** Options: (a) a note per engine row whose
  index mode the S1 rule would change, against gov's mode at the row's own `commit`, never a
  failure; (b) nothing, leaving `update`'s read-only run as the only predictor. Neither trips an M3
  veto: (a) adds a line to an existing verb's output, no surface and no write. (a) detects a state (b)
  cannot, at one spawn per distinct row commit, so it is the more feature-rich. It is a note and not
  a failure for the reason `check-receipt.py` gives its unattributed count: redding a target on a
  state no release has yet let it clear hands it a failure it cannot act on. RESOLVED (agent,
  2026-10-09, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief and the owner's clarification.
- rev-2 · 2026-10-09 · built. S5 and §4 Cost read gov's mode at the receipt's `gov_commit`, since a
  carried row keeps its old `commit`; §6 names `measure_mode_carry` and the two fixtures; AC9's AC1
  break is re-pointed (the old expression reds AC4), its breaks are a build-time observation, and its
  cost line is measured.
- rev-3 · 2026-10-09 · §3 Edges: the sibling edge onto TOOL-aLevelledCopy-3 becomes an `external`
  one, because check 12 reads a sibling edge as an ordering claim and that unit is built later; no
  criterion rested on it. §6 AC8: the `git update-index` token is rewrapped onto one line, because
  a token split across a line break mispairs every backtick after it and the ledger join read none.
  Record corrections found by the close's bar; no criterion moves.

## 10. Reuse audit

The seams are in `tools/govkit/govkit.py`: `land_through_index`, whose mode expression S1 replaces;
`gov_tree_mode`, which S2 turns into a lookup; `index_read`, the batched index reader `index0` and
S5 already use; and the snapshot predicate building `snap_rows`, which S4 widens by one field.
`python tools/codebase-map/reuse_lookup.py "carry a file mode from gov's tree onto a target's
existing index entry"` returned only name-stem matches on `tree` and `index` in other kits, so no
existing mode-rule seam fits beyond those named. Recall ranked the aScouredKit wave-3 cross-OS
review and `DEPL-dCarriedReceipt-7` §8 F1, which set today's no-entry rule this unit keeps. Where
recall and source disagreed: that review cites `land_through_index` at `govkit.py:5127` and two
`gov_tree_mode` call sites; at base the line is near 8269 and there is ONE call site.

Recall terms used: gov_tree_mode land_through_index update-index cacheinfo 100755 exec bit hook mode engine row cross-os lens
