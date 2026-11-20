# TOOL-dWitnessedBar-41 — the selection a bar ran under travels on the per-tree verdict, and the hook re-derives it before adopting

**Status:** INPROGRESS · rev-3 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 22 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-41-deviation-411.md](../build/2026-10-25-build-TOOL-dWitnessedBar-41-deviation-411.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-41-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-41-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-41-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-41-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-41-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-41-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 59 at HIGH**, its item **H2**, alone in that item. `TOOL-dWitnessedBar-5` S7, as
landed (`eef75404f`), re-derives a selection at R only from the run record of the bar the hook itself
ran, `<git-dir>/gate-run/<run id>/selection` (`.githooks/pre-push@cfb339de:2555-2576`). Run records sit
in the per-worktree `<git-dir>/gate-run/` (`tools/run-gates/run-gates.sh@d9c0c2e8:2782`) and are swept
past `GATE_RUN_KEEP` (`tools/run-gates/run-gates.sh@d9c0c2e8:6110-6113`). The per-tree record the hook
adopts with no bar of its own, `TOOL-dWitnessedBar-4`'s `<common-dir>/gate-verdict/<tree>`, names no
selection, and neither of its two readers reads one: the scoped-base pass through
`.githooks/pre-push#check_tree_verdict` and the cover pass through `.githooks/pre-push#check_cover_record`.
A bar run in worktree A under a `GATE_SELECTION` holding legs writes a GREEN per-tree verdict; a push of
the same tree from worktree B, or after A's run dir is swept, adopts that GREEN with nothing re-derived.
This unit takes the report's fix. It repairs `TOOL-dWitnessedBar-5`.

## 2. Scope (IN)

- **S1** — The selection on the per-tree record. The runner's per-tree record gains `selection`, the
  `git hash-object` of the canonical selection text (§4 "The canonical text"), or `none` when the run
  read no `GATE_SELECTION` or the knob named no file; and one `selection.<n>` key per row of that text,
  `<n>` an index from 1, its value `<leg name> · <source> · <note>`. The keys are written beside
  `run_id` in the writer `TOOL-dWitnessedBar-4` landed (`tools/run-gates/run-gates.sh@d9c0c2e8:6037-6067`),
  for a GREEN and a RED record alike. Observed by AC1.
- **S2** — The hook re-derives from the record. One function, `check_tree_selection`, reads the
  `selection` key `read_bar_file` now collects: `none` passes; a hash rebuilds the canonical text from
  `selection.1` onward, refuses when its `git hash-object` differs from `selection`, and otherwise runs
  `verdict_flow.py select --check --selection <file> --rev <R>` over the rebuilt text, passing only on
  exit 0. Both per-tree readers call it, as both call `check_tree_reuse` today:
  `.githooks/pre-push#check_tree_verdict`, which `check_bar_record` and `check_bar_base` reach, and the
  `bar` branch of `.githooks/pre-push#check_cover_record`. Observed by AC2 and AC3.
- **S3** — Absent means refused. A per-tree record carrying no `selection` key is not adopted, because it
  cannot say whether its bar held legs. Every per-tree record a hook suite plants for adoption carries
  `selection none` from this unit's pass, since the key it lacks would otherwise refuse it (§4 "The
  plants"). Observed by AC3.
- **S4** — `select --check` reads a file. `verdict_flow.py select --check` gains `--selection <path>`
  beside unit 5's `--run <run dir>`, exactly one of the two: `--run` reads `<run dir>/selection` as
  today, and `--selection` reads the named file, both compared row by row with a fresh derivation at R
  in `tools/run-gates/verdict_flow.py#cmd_select_check`. `tools/run-gates/verdict_flow.py#main`, which
  asks `--run` of `select --check` today, asks one of the two. Observed by AC2.

## 3. Non-goals (OUT)

- The selection record, `select`, `SELECT_SOURCES` and the hold predicate: `TOOL-dWitnessedBar-5`'s,
  and `SELECT_SOURCES`'s `quarantine` reader `TOOL-dWitnessedBar-8`'s.
- The per-tree record's other keys and its write rule: `TOOL-dWitnessedBar-4`'s and
  `TOOL-dWitnessedBar-40`'s.
- The runner stamps `gate-full-green` and `gate-full-green.shared`, which the same two readers also
  adopt and which carry no selection either: not this finding's record, and no clause of this build
  names them.
- `tools/loop/loop_transition.py`, which reads the full per-tree record at `item.test.exit` and adopts
  nothing for a push: outside S3's population.
- Retaining run records across worktrees: the per-tree record now carries what the hook reads, so no
  run record is needed at the push.
- A spec-set lint that every key the hook's adoption predicate reads appears in unit 4's key table, the
  report's left-shift: no clause of this build names it, and AC3 is the arm for this key.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-5` — `verdict_flow.py select --check` and the selection record's row grammar, which the hook runs over the rebuilt selection
- **consumes-from** `TOOL-dWitnessedBar-4` — the runner's per-tree record and the hook's adoption of it, which gain the `selection` keys and the re-derivation
- **hands-off** `TOOL-dWitnessedBar-56` — the `selection` keys, their canonical text and the hook's rebuild, which the verdict-boundary minors batch makes lossless over the accepted rows (ids 2, 3, 16, 33, 47)

## 4. Design

### Evidence

Read at HEAD `cb1494fc5`, which holds every unit through order 21 landed, units 3, 4, 40, 44 and 5
among them, with their pass-leg fixes `b94fc8d10`. Every cited file is clean in the working tree, and
each line citation is pinned to the blob HEAD holds.

- Run records: `RUNROOT="$gd/gate-run"` (`tools/run-gates/run-gates.sh@d9c0c2e8:2782`), `$gd` the
  worktree's own git dir; the sweep keeps the newest `GATE_RUN_KEEP`
  (`tools/run-gates/run-gates.sh@d9c0c2e8:2749`, `tools/run-gates/run-gates.sh@d9c0c2e8:6110-6113`).
- The per-tree record lives under the common dir, read once as `RG_COMMON_RAW`
  (`tools/run-gates/run-gates.sh@d9c0c2e8:124-129`) and resolved by the writer
  (`tools/run-gates/run-gates.sh@d9c0c2e8:6038`), so every worktree reads one directory
  (`TOOL-dWitnessedBar-4` §4 "The record"). Its `tail.<n>` keys (`TOOL-dWitnessedBar-25`) are the
  precedent for an indexed key family on it (`tools/run-gates/run-gates.sh@d9c0c2e8:6057`).
- The runner reads `GATE_SELECTION` once into `SEL_FILE` and unsets it
  (`tools/run-gates/run-gates.sh@d9c0c2e8:429-430`). Its read loop holds a row whose first field is
  `held`, whose source is `quarantine` or `level` and whose leg the manifest carries, prints and ignores
  every other row, and copies the whole file into the run record as `selection`
  (`tools/run-gates/run-gates.sh@d9c0c2e8:3105-3131`).
- Unit 5's selection rows are `held<TAB><leg name><TAB><source><TAB><note>` under a `#` header naming
  the values read (`TOOL-dWitnessedBar-5` §4 "The selection record"); `select` never writes a leg name
  holding ` · ` (`tools/run-gates/verdict_flow.py#derive_selection`). A `level` row's note reads
  `<level>, outside tests.landing-levels <levels>` (`tools/run-gates/verdict_flow.py#derive_level_rows`).
- `select --check` compares every non-blank line of the recorded file not opening with `#` against
  the rows derived at R, and exits 1 naming each row added or lacking
  (`tools/run-gates/verdict_flow.py#cmd_select_check`). Today `SELECT_SOURCES` holds `level` alone, so
  no `quarantine` row is ever derived at R until `TOOL-dWitnessedBar-8` adds its reader.
- The hook's S7 block resolves the run-gates kit, R, a python, vets `verdict_flow.py` with
  `check_reviewed_file` and runs `select --check --run`, setting `SEL_NOT` to the first reason
  (`.githooks/pre-push@cfb339de:2555-2576`). `check_reviewed_file` exits the hook on a refusal
  (`.githooks/pre-push#check_reviewed_file`).
- `read_bar_file` reads a fixed key set into `bg_*` variables, and `check_bar_base` declares those
  variables `local` so the caller's record is kept (`.githooks/pre-push#read_bar_file`,
  `.githooks/pre-push#check_bar_base`). `check_tree_reuse` is the precedent of one predicate both
  per-tree readers call (`.githooks/pre-push#check_tree_reuse`, `TOOL-dWitnessedBar-40` S4).

### The canonical text

Every line of the file `GATE_SELECTION` named whose first TAB field is `held`, in file order, one
trailing CR cut, each LF-terminated; the header and every other line are left out. A row the runner
printed and ignored stays in the text, so `select --check` names it and the record is refused, the
direction S7 already takes for the same row. The runner hashes the text with `git hash-object --stdin`,
which applies no filter to standard input. It writes one `selection.<n>` per line, the line's `held`
field cut and each TAB after it turned into ` · `. The hook rebuilds the text from `selection.1`
upward, stopping at the first absent index, each value's ` · ` turned back into a TAB and `held` and a
TAB put before it, and hashes it the same way. A mismatch means a key was edited or lost, and the record
is refused. A note holding ` · ` rebuilds with an extra TAB and is refused the same way, which is the
loss `TOOL-dWitnessedBar-56` S1 closes.

```
selection	<blob id of the canonical text>      or      selection	none
selection.1	unit-heavy suite · level · e2e, outside tests.landing-levels unit integration
selection.2	flaky leg · quarantine · TOOL-x-7
```

### The hook's check

The S7 block's four refusals and its `select --check` call become one function,
`check_selection_at_r <--run|--selection> <path>`, which sets `SEL_NOT` empty or to the reason. S7
calls it with `--run "$gd/gate-run/$RUNLOG_GATE_RUN"`, and every message it prints stays byte-identical.
`check_tree_selection <label>` sets `force` as the other per-tree predicates do:

| `selection` on the record | `force` |
|---|---|
| absent | `the recorded <label> carries no selection, so it cannot say whether its bar held legs` |
| `none` | empty |
| a hash the rebuilt text does not match | `the recorded <label>'s selection rows do not hash to <sel8>, so a row was edited or lost` |
| a hash `check_selection_at_r --selection` refuses | `SEL_NOT`, which names the row `select --check` printed |
| a hash it admits | empty |

The rebuilt text is written to a `mktemp` file and removed after the check, as
`.githooks/pre-push#read_post_merge_red` does with its scratch file. One push reads the same record in
the scoped-base pass and again in the cover pass, so a result is kept in `SEL_SEEN`, one
`<hash><TAB><force>` line per hash checked, read with builtins: each distinct hash runs `select --check`
at most once per push. `read_bar_file` gains `bg_sel` and the rebuilt rows, and `check_bar_base`'s
`local` list gains both.

### The plants

S3 refuses a keyless record, so every per-tree record a hook suite plants for adoption gains
`selection none`. The population is DERIVED by
`git grep -nF 'verdict\tGREEN\nkind\t' -- .githooks tools`, run 2026-11-20 at `cb1494fc5`:

| Plant | Its arms |
|---|---|
| `.githooks/pre-push.test.sh#write_bg_verdict` | every `BG` arm that adopts a per-tree record |
| the `DEC covered` plant of `.githooks/pre-push.runlog.test.sh` (`.githooks/pre-push.runlog.test.sh@2ed9424c:873-875`) | `DEC covered` |

The second plant carries neither `reused` nor `reused_cache` either, which `check_tree_reuse` has
refused since `TOOL-dWitnessedBar-40`; it gains `reused 0` and `reused_cache 0` beside `selection none`.
UNVERIFIED: whether its `DEC covered` checks read green at HEAD; the pass observes that suite before the
change. `tools/run-gates/run-gates.evidence.test.sh` reads records the runner writes and plants none,
and `tools/unattended/unattended.test.sh` names the record in a comment alone: both are outside the
population.

### Inventory

Minted: the per-tree keys `selection` and `selection.<n>`; the flag `--selection` of
`verdict_flow.py select --check`; the hook functions `check_tree_selection` and `check_selection_at_r`;
the hook variables `bg_sel` and `SEL_SEEN`. Naming cells: `python tools/lexicon/lexicon.py --suggest
check_tree_selection --as sh.function` and the same for `check_selection_at_r` each answered OK on
2026-11-20. The keys and the flag sit in no declared cell, since the lexicon conf declares
`js.function js.type py.function py.type sh.function` alone.

### Migration

A per-tree record written before this pass carries no `selection` and is not adopted (S3); the first
push of such a tree runs its bar.

### Rollout

Live at landing; the runner, the hook and `verdict_flow.py` change in one commit. Units 41, 8 and 55 sit
at order 22. Unit 8 also edits `tools/run-gates/run-gates.sh`, `tools/run-gates/verdict_flow.py` and
`tools/run-gates/README.md`: its hunks sit in `SELECT_SOURCES` and the quarantine reader, and this
unit's in `cmd_select_check`, `main`, the selection read loop and the per-tree writer, so a parallel
build merges them without a shared hunk.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`: the selection read loop gathers the canonical text; the per-tree writer prints the keys
- `tools/run-gates/verdict_flow.py`: `cmd_select_check`, `main` and the module docstring's `select --check` line
- `tools/run-gates/README.md`: "The verdict per tree" key table, the "Held by policy" paragraph and the `verdict_flow.py` row
- `tools/run-gates/run-gates.evidence.test.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh`
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, since its `watch:` line names `tools/run-gates/run-gates.sh`

### Alternatives rejected

- **Key the selection by hash under the common dir.** A second directory needs its own retention rule,
  and a record whose selection file was swept is refused anyway; the record carrying its own rows has
  nothing to sweep.
- **Retain run records across worktrees for the hook.** It keeps every worktree's run dirs alive for
  the one key the per-tree record can carry itself.
- **Hand the hook's rebuilt text to `select --check --run` in a scratch directory.** It needs no new
  flag, and it names a scratch directory a run record, which `verdict_flow.py`'s `<run dir>` contract
  says it is not.

## 5. Production-readiness checklist

- security — closes a fail-open path: a loosening made in one worktree is re-derived at R before any
  worktree adopts its GREEN, and a record that cannot say whether it held legs is refused.
- perf / scale — a few keys per record; `select --check` runs only for a record whose `selection` is a
  hash, and at most once per hash per push (`SEL_SEEN`).
- error / empty / loading states — absent key: refused; hash mismatch: refused naming it; `--check` exit
  1: refused naming the row R does not derive; a `verdict_flow.py` whose working copy is not the blob
  tracked at the pushed tip: the push is refused as S7 refuses it, through `check_reviewed_file`.
- observability — the hook's `not covered` line, or the scoped decision's refusal list, names which of
  the three refused the record.
- risks — a push of a tree whose bar held a quarantined leg now pays one `select --check` run; a
  selection carrying a row the runner ignored makes its record unadoptable, the conservative direction.
- testing — AC1 to AC3 by fixture; the arms of §7 at the close.
- migration — §4.
- user docs — `tools/run-gates/README.md` names the keys and the flag at the pass; no page under `help/`
  covers the boundary.

## 6. Acceptance criteria

- **AC1** — When the runner makes a full run over a fixture manifest in a clean scratch clone with
  `GATE_SELECTION` naming a file holding one `quarantine` row, the per-tree record under
  `gate-verdict/` holds `selection.1` naming that leg and a `selection` equal to `git hash-object` of
  the canonical text; with no `GATE_SELECTION` it holds `selection none`.
  Red when: the per-tree record omits the selection, so another worktree cannot see it.
  fixture: `rec_repo`'s scratch clone, the run-gates evidence suite's builder, whose two legs leave one
  running beside the held one; the selection file sits outside the clone, because an
  untracked file inside it starts the run dirty and no per-tree record is written.
- **AC2** — When `.githooks/pre-push` runs from a second worktree of a clone whose R holds the
  run-gates kit's `verdict_flow.py`, with no run dir of the first worktree, over a GREEN per-tree record
  whose selection holds a row R does not derive, it runs the bar and names the row; over one whose
  selection R derives exactly it adopts the record; and
  `python tools/run-gates/verdict_flow.py select --check --selection <file> --rev <R>` exits 1 and 0 on
  the same two rebuilt files.
  Red when: the hook adopts a GREEN made under a selection nothing re-derived.
  fixture: a `level` row R derives where R's policy declares `tests.landing-levels` `unit integration`
  and `tests.without-cadence` `report-unrun` and the manifest gives the leg level `e2e`, as the
  `--fixture select` case of `tools/run-gates/verdict_flow.py` plants; the tree holds none.
- **AC3** — When the per-tree record's `selection.1` is edited after the run, or its `selection` key is
  deleted, `.githooks/pre-push` runs the bar and names the reason.
  Red when: an edited or keyless record is adopted.

## 7. Gates

`measure-legs selftest` · `pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `run-gates canary` · `run-gates evidence` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: .githooks/pre-push.test.sh · covers AC2 AC3 · a push from a second worktree over a planted record whose selection R does not derive and one it derives, on `build_bg_fixture` with the selection reader's files `build_sel_fixture` copies beside its stand-in runner; then an edited and a keyless record as two more cases of the BG AC6-8 refusal table; staged red by skipping `check_tree_selection` · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 · a full run under a one-row selection on `rec_repo`'s clone, staged red by dropping the `selection` keys from the writer · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-5`'s clause, which would split a
  clause that unit carries whole. (b) reds the parts join; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none ·
  relaxes: none
- **F2 — Where do the selection's rows live for the hook?** Options: (a) as `selection.<n>` keys on the
  per-tree record itself, with a hash for integrity; (b) a content-addressed file under
  `<common-dir>/gate-selection/`; (c) the run record, retained across worktrees. (b) needs a retention
  rule of its own; (c) keeps every run dir alive for one key. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3, the record's own additive-key grammar. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 59 (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.
- rev-3 · 2026-11-20 · §1 · §3 · §4 · §5 · §6 · §7 · §10 · S1 · S2 · S3 · S4 · AC1 · AC2 · AC3 ·
  re-grounded at HEAD `cb1494fc5` over order 21 as landed, by brief
  2026-11-19-prompt-TOOL-dWitnessedBar-41-reground-brief. Bare line citations become blob-pinned or
  `path#symbol`; S2 names the two per-tree readers as landed and the S7 block extracted as
  `check_selection_at_r`; S3 names the hook suites' plants, the runlog suite's joining Files touched;
  S4 names `cmd_select_check` and `main`; the canonical text cuts a trailing CR and keeps ignored rows;
  the README and the kickoff manifest join Files touched, and `pre-push run-log line`,
  `kickoff-manifest ratchet`, `recall floor` and `recall floor arms` the leg line. Goal and scope intent
  unchanged.

## 10. Reuse audit

The seams extended are unit 4's per-tree record and its additive `<key>TAB<value>` grammar, with the
`tail.<n>` keys as the precedent for an indexed family; unit 5's `select --check`, given a file form
in `tools/run-gates/verdict_flow.py#cmd_select_check`; unit 5's S7 block in `.githooks/pre-push`,
extracted as the one re-derivation both its callers share; and unit 40's `check_tree_reuse` placement,
one predicate both per-tree readers call. `python tools/codebase-map/reuse_lookup.py "carry a held-leg
selection with the verdict another worktree adopts"` ranked `legs`, `leg`, `adopt`,
`add_scratch_worktree` and `require_adopted_root` on 2026-11-20, none of which carries a record across
worktrees; `python tools/codebase-map/reuse_lookup.py "re-derive a selection at R before the pre-push
hook adopts a per-tree verdict"` ranked `tree`, `before`, `pre`, `remove_tree` and `adopt`, none a
selection or verdict reader. No existing seam fits beyond the four named.

Recall terms used: `python tools/memory-recall/query.py "how does a held-leg selection travel with a verdict adopted from another worktree" --terms "GATE_SELECTION selection record held leg select check common-dir gate-verdict worktree adopt witness"`
