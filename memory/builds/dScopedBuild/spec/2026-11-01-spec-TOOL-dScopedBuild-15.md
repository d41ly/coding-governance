# TOOL-dScopedBuild-15 — `build.acceptance` writing the seen-red record: each gate a unit adds or changes re-run on its planted red beside the unit's acceptance commands

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 10 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0506@2200c4c7 whole
**Carries:** node:item.build.acceptance
**Carries:** node:item.build.fix-pass

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-14 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

A gate a build adds or changes is "seen red" today only when the main loop says so: M8 tells it to
observe each new arm red and green and record both (`memory/guides/BUILD-METHOD.md:280-282`), and
nothing re-runs that observation (gap-test-06). This unit makes `build.acceptance` the writer of the
seen-red record: the acceptance re-run executes each gate's planted red beside the unit's acceptance
commands, writes one seen-red line per gate keyed by leg and red SHA, which dWitnessedBar's
`test.seen-red` reads, and fails the acceptance, routing to `build.fix-pass`, when a planted red stays
green or never ran (the owner's FK-4-12 and FK-5-2).

## 2. Scope (IN)

Build-run preconditions: TOOL-dWitnessedBar-7 (`tools/memory-tree/seen_red.py`, its line grammar,
`read_seen_red_records` and `derive_owed_gates`), TOOL-dWitnessedBar-21 (`tools/unattended/fix_keeps.py`
and `--dispatch --fix-of`), TOOL-dDeclaredLoop-17 (`tools/loop/loop_witness.py`, its `acceptance` verb
and `run_witness_commands`) and TOOL-dScopedBuild-1 S2 (`read_build_base`) have landed. None of their
files exists at base; dWitnessedBar is a parent, dDeclaredLoop an ancestor of every parent.

- **S1** — The unit's gates, `derive_unit_gates(root, slug, unit, base)` in
  `tools/memory-tree/seen_red.py`, returning the leg names a unit adds or changes, each once: (a) every
  leg whose `tools/gate-legs.json` row is new, or carries another `argv`, across one of the unit's own
  commits, compared at that commit and its first parent exactly as TOOL-dWitnessedBar-7 S4 (a)
  compares base and HEAD; and (b) every leg TOOL-dWitnessedBar-7 S4 (b) resolves from a `New arm:`
  line of the unit's own spec, read at HEAD. The unit's own commits are the non-merge commits in
  `<base>..HEAD` that `routed_commits.extract_unit_ids` (`tools/memory-tree/routed_commits.py:119`)
  names the unit in, over subject plus `Pass:` trailer (I8), only those touching
  `tools/gate-legs.json` opened. The unit's spec is the file under `<MEMORY_ROOT>/builds/<slug>/spec/`
  whose H1 defines the id. Observed by AC1, AC2.
- **S2** — The owed-set verb, `python seen_red.py --owed <slug> --unit <unit id> [--base <sha>]`,
  printing one line per S1 leg, `owed: <leg>`, or `seen-red: <unit id> adds or changes no gate ·
  nothing owed`, and exiting 0; exit 2 when it cannot answer (no base, an unreadable manifest, no spec
  defining the id). `base` defaults to `routed_commits.read_build_base(repo, slug)` (I1), the parent of
  the oldest first pass `read_first_passes` attributes, never the `base:` fact of a `RUN.md`, which an
  attended build does not have. Observed by AC1, AC2, AC3.
- **S3** — The writer, `write_seen_red_lines(record, unit, lines)` in `seen_red.py`, and its verb
  `python seen_red.py --write <record> --unit <unit id> --leg <leg> --red <sha> --green <sha> --break
  <text>`. It appends one TOOL-dWitnessedBar-7 S1 line, the seen-red line (I19), under the record's
  `**Evidences:** <unit id>` block, creating the file as a `journal` record (`**Serves:** journal <unit id>`) and the block when
  either is absent. A field the reader would refuse is refused here by the same validator
  `read_seen_red_records` applies, exit 2, nothing written. A line already carrying the same
  `(leg, red)` key writes nothing and exits 0, printing `seen-red: <leg> · <red sha8> · present`.
  Observed by AC4, AC5.
- **S4** — The plant declaration. The acceptance verb `python tools/loop/loop_witness.py acceptance`
  (TOOL-dDeclaredLoop-17 S3) gains a repeatable `--plant <leg> <path> <from> <to>`, named by the
  caller beside its `--cmd` acceptance commands, the flag shape TOOL-dDeclaredLoop-17 §3 gives them:
  "the caller names them". `<path>` is a file tracked at `--sha`; `<from>` and `<to>` are one-line
  literals, `<from>` occurring exactly once in that file at `--sha`. A plant breaking any of the three
  is refused before any run, exit 2, naming the leg and the rule. Observed by AC6, AC9.
- **S5** — The re-run. The verb reads S2 for `--build` and `--unit` through `seen_red.py --owed`, the
  memory-tree kit found by the inlined `resolve_kit_dir` (`tools/memory-tree/backlog.py:1757`), never
  imported. For each owed leg with a plant, the one `run_witness_commands` call that re-runs the
  acceptance commands at `--sha` (TOOL-dDeclaredLoop-17 S2) also runs, in order: the stage,
  `python loop_witness.py stage <path> <from> <to>`; the leg through the bar's runner; the
  restore, `git checkout -- <path>`; and the leg again. The leg is satisfied when the staged run exits
  non-zero and the restored run exits 0. S3 then writes its line, `red` and `green` both `--sha`, the
  break `<path>: <from> → <to>`, into `<MEMORY_ROOT>/builds/<slug>/build/<date>-build-<unit
  id>-gate-ledger.md`. Every run joins the acceptance record's `run` lines. Observed by AC6.
- **S6** — The failure. An owed leg with no plant prints `acceptance: <leg> · no plant declared`; a
  staged run exiting 0 prints `acceptance: <leg> · planted red stayed green`; a restored run exiting
  non-zero prints `acceptance: <leg> · red at <sha8> without the plant`. Each writes no seen-red line
  for that leg, and the verb exits 1 with its last line
  `route: build.fix-pass · --dispatch <slug> --pass <unit id> --writes <path>… --fix-of acceptance`.
  A unit owing no gate prints S2's line and the verb's verdict is its acceptance commands' alone.
  Observed by AC7, AC8.
- **S7** — `build.fix-pass`'s red set (I17). TOOL-dWitnessedBar-21 S3's `--fix-of` gains the value
  `reuse-check`, the red `build.reuse-check` routes (TOOL-dScopedBuild-12). `python fix_keeps.py --keeps
  reuse-check --spec <path>` prints `read_acceptance_files`' paths and the reuse check's own module,
  `tools/codebase-map/reuse_check.py` (TOOL-dScopedBuild-12 S2), found by `resolve_kit_dir`. A failed
  acceptance, this unit's red, dispatches `--fix-of acceptance` as TOOL-dWitnessedBar-21 already
  allows. The `--fix-of` line of `unattended.sh`'s argv fence and the verbs carrier's paragraph name
  the third value. Observed by AC10.
- **S8** — The plants. `python loop_witness.py --fixture --plant <case>` gains the cases `gate-seen`,
  `gate-stays-green`, `gate-no-plant`, `gate-restored-red` and `gate-none`; `python seen_red.py
  --fixture --plant <case>` gains `owed-unit`, `owed-attended`, `write-twice` and `write-bad-sha`; and
  `python fix_keeps.py --fixture --plant reuse-check-module` joins TOOL-dWitnessedBar-21 S6's set. Each
  builds a throwaway repository under the system temp directory (§4 "The plants"). Observed by AC1 to
  AC10.

## 3. Non-goals (OUT)

- `test.seen-red`, the reader that reds a gate with no record: TOOL-dWitnessedBar-7. This unit writes
  through its grammar and adds no second reader.
- M8's "Observe the owed arms" wording: TOOL-dWitnessedBar-7 S9 re-words it inside M1's budget, and
  `memory/guides/BUILD-METHOD.md` stands at 29354 of 30720 bytes at base.
- Parsing a spec's acceptance criteria into commands: TOOL-dDeclaredLoop-17 §3 leaves them to the
  caller, and so this unit leaves the plants.
- The executor itself and its `[[adapter]]` row: dWellOiledMachine's executor replaces the
  `stand-in` writer on the same verb (TOOL-dDeclaredLoop-17 §3).
- Drawing a fix pass on `flow.rework-budget` or ending a loop past `flow.route-backs`:
  TOOL-dDeclaredLoop-30.
- The reuse check and its rows: TOOL-dScopedBuild-12. This unit names its red value and keeps only.
- Seen-red lines for landed builds: a closed build's gates are not re-run.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — `read_first_passes`, behind `read_build_base`, the base S2 defaults to; without it an attended build, which has no `RUN.md`, has no base
- **hands-off** `TOOL-dScopedBuild-12` — `--fix-of`, with the `reuse-check` value and its keeps S7 adds, the dispatch a `duplicate` or `bypassed` row routes to
- **consumes-from** external — TOOL-dWitnessedBar-7 S1 to S6 and TOOL-dWitnessedBar-21 S1 to S6, both DEFERRED at base and a parent's, and TOOL-dDeclaredLoop-17 S2 and S3, an ancestor's
- **hands-off** external — dWellOiledMachine's executor runs the acceptance verb in place of the `stand-in` writer, as TOOL-dDeclaredLoop-17 §3 says its build does
- **consumes-from** `TOOL-dScopedBuild-33` — §4's sentence that `read_first_passes` moves beside `read_routed_commits`, which that unit supersedes; S2's default base still comes from `read_build_base`, without which an attended build has no base (id 30)
- **hands-off** `TOOL-dScopedBuild-35` — S7's `--keeps reuse-check`, which that unit's S33 prints `not-installed` while unit 12's module does not resolve (id 7)

## 4. Design

### Evidence at base

- The item: `build.acceptance` "re-runs the spec's acceptance commands on the commit, and for each gate
  the unit adds or changes, re-runs its planted red and writes the seen-red record, one per gate, keyed
  by leg and red SHA"; fail, "a planted red that stays green included", goes to `build.fix-pass`
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:290`, `:291`).
- The owner's FK-5-2 A: the writer is "the executor's re-run of the unit's acceptance commands, which
  include each new gate's planted red", not the agent, and B, the leg factory registering each leg's
  planted case, was not taken (`…-fold-return-w5.md:59-64`). B3-F1: the writer must be the run that
  observed the red, or the check writes what it checks for (`…-walk-return-b3.md:12-19`).
- Running a leg at a SHA: the bar's attribution adds a detached worktree, `add_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`); a kit never sources a sibling's file, so this unit runs the
  runner and never that library. The runner reads its manifest from `GATE_LEGS` when set
  (`tools/run-gates/run-gates.sh:252`), and `GATE_FULL` bypasses every guard (`:408`).
- The base: `read_first_passes` is at `tools/memory-tree/deviation_join.py:325` at base and moves
  beside `read_routed_commits` with TOOL-dScopedBuild-1 S1, `read_build_base` its S2.

### The re-run, one owed leg

```
worktree at --sha (run_witness_commands, one call with the --cmd acceptance commands)
  1. python loop_witness.py stage <path> <from> <to>     # exit 0, or 2: find not exactly once
  2. GATE_LEGS=<one-row manifest> GATE_FULL=1 bash <runner>    # owed: non-zero
  3. git checkout -- <path>                                     # exit 0
  4. GATE_LEGS=<one-row manifest> GATE_FULL=1 bash <runner>    # owed: 0
```

The one-row manifest is the leg's row as `git show <sha>:tools/gate-legs.json` holds it, written to
the verb's own temporary directory. The runner is the one `resolve_kit_dir("run-gates",
"run-gates.sh", here)` finds, the reading TOOL-dWitnessedBar-21 §4 uses for the manifest. Steps 2 and
4 differ only by the staged literal, so a red in 2 is the plant's: a manifest or runner fault reds 4
as well and reads as `red at <sha8> without the plant`, never as seen.

| Staged run (2) | Restored run (4) | Verdict | Line written |
|---|---|---|---|
| non-zero | 0 | seen | ``- seen-red — `<leg>` — red `<sha>` — green `<sha>` — <path>: <from> → <to>`` |
| 0 | 0 | `planted red stayed green` | none |
| any | non-zero | `red at <sha8> without the plant` | none |
| no plant | — | `no plant declared` | none |

### The plants

| Case | Fixture | Expected |
|---|---|---|
| `owed-unit` | two units, each adding a leg in its own commit, one `New arm:` line on unit 1's spec | `--owed` for unit 1 prints its leg and the arm's leg, not unit 2's |
| `owed-attended` | as `owed-unit`, no `RUN.md` | the same, the base `read_build_base`'s |
| `write-twice` | `--write` run twice with one key | one line, `present` on the second run |
| `write-bad-sha` | `--red` of seven hex | exit 2, nothing written |
| `gate-seen` | a leg whose script exits 1 on a planted literal | exit 0, one line read back by `read_seen_red_records` |
| `gate-stays-green` | a plant on a line the leg never reads | exit 1, `planted red stayed green` |
| `gate-no-plant` | an owed leg, no `--plant` | exit 1, `no plant declared`, and `seen_red.py --build` prints `NO RECORD` |
| `gate-restored-red` | a leg red at the SHA | exit 1, `red at <sha8> without the plant` |
| `gate-none` | a unit adding no leg | exit 0, the `nothing owed` line |
| `reuse-check-module` | `--keeps reuse-check` over a spec naming a fixture file | the fixture file and `reuse_check.py` printed |

### Inventory

Minted: `derive_unit_gates` and `write_seen_red_lines`, and the verbs `--owed`, `--unit`, `--write`,
`--leg`, `--red`, `--green`, `--break` of `seen_red.py`; the `loop_witness.py` verb `stage` and the
`acceptance` flag `--plant`; the `--fix-of` value `reuse-check`; the record name
`<date>-build-<unit id>-gate-ledger.md`. Naming cells: `derive_unit_gates` and `write_seen_red_lines`
answer `OK` from `python tools/lexicon/lexicon.py --suggest <name> --as py.function`, asked at writing.

### Migration

Additive. A unit with no owed gate behaves as TOOL-dDeclaredLoop-17 S3 ships it. A `--dispatch`
without `--fix-of reuse-check` is unchanged.

### Rollout

Live at landing on the stand-in route: the main loop runs the acceptance verb with each unit's
commands and plants, and commits the gate ledger beside the acceptance record. The memory-tree,
loop and unattended kits' versions move.

### Files touched (estimate)

- `tools/memory-tree/seen_red.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/loop/loop_witness.py`
- `tools/unattended/fix_keeps.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **A `plant` command field on the `New arm:` line.** Tested against the corpus: a spec is written
  before its code, so a plant naming source text that does not yet exist forces a rev bump on every
  unit once its code lands; and it changes `memory/TEMPLATE-SPEC.md`'s "the rest of the line is
  prose", a governance carrier no word of the clause names.
- **A plant as an arbitrary command expected to exit 1.** It executes caller text, and a command that
  fails for any reason, a missing file included, reads as red: there is no restored run to tell the
  plant's red from a broken invocation.
- **The leg factory registering each leg's planted case.** FK-5-2 B, the option the owner did not
  take.
- **Running the leg's `argv` directly.** It bypasses the runner's `{prefix}` resolution, ceiling and
  guard handling, so a leg could read green here and red at the bar.
- **The whole build's owed set at every unit.** It makes unit 3 answer for unit 9's gate, and its
  fix pass would hold another unit's write set.

## 5. Production-readiness checklist

- security — the only authored text the re-run applies is a one-line literal substitution in a tracked
  file inside a scratch worktree; nothing named by a caller is executed but the manifest's own leg.
- perf / scale — two runner calls per owed leg, each bounded by the leg's manifest ceiling; a unit
  adds or changes few legs.
- error / empty / loading states — an empty owed set prints its `nothing owed` line, never silence; an
  unanswerable base or manifest is exit 2 naming it.
- observability — each verdict names the leg and the SHA; every run is a `run` line of the
  acceptance record.
- risks — a builder whose plant names no literal the leg reads meets `planted red stayed green`,
  which is the case the clause wants red; `GATE_FULL=1` keeps a guard from skipping the leg.
- testing — AC1 to AC10 by the fixtures of S8; the arms of §7 at the close.
- migration — none beyond §4.
- user docs — `memory/guides/UNATTENDED-VERBS.md` (S7); no `help/` page covers the verbs
  (`help/README.md`).

## 6. Acceptance criteria

- **AC1** — When `python seen_red.py --fixture --plant owed-unit` runs in `tools/memory-tree/`, `--owed`
  for unit 1 prints `owed:` for the leg unit 1's commit added and for the leg its `New arm:` line
  resolves to, and not unit 2's leg; it exits 0.
  Red when: a leg another unit's commit added is owed by this one, or the arm's leg is missed.
- **AC2** — When the fixture runs `--plant owed-attended`, a tree with no `RUN.md`, `--owed` prints the
  same lines as AC1, its base the one `read_build_base` returns.
  Red when: the owed set needs a `RUN.md` `base:` fact, which an attended build lacks.
- **AC3** — When `python seen_red.py --owed <slug> --unit <id>` runs on a fixture unit adding no leg,
  it prints `nothing owed` and exits 0.
  Red when: an empty owed set reads as silence or as a failure.
- **AC4** — When `python seen_red.py --fixture --plant write-twice` runs, the gate ledger holds one
  `- seen-red` line for the key, and the second run prints `present`.
  Red when: a re-run of the acceptance writes a second line for one `(leg, red)` key.
- **AC5** — When the fixture runs `--plant write-bad-sha`, `--write` exits 2 and the record is
  unchanged; `read_seen_red_records` over the fixture reads no line.
  Red when: the writer admits a line its reader refuses.
- **AC6** — When `python loop_witness.py --fixture --plant gate-seen` runs in the loop kit, the verb
  exits 0, the gate ledger holds one line naming the leg with `red` and `green` equal to the unit's SHA,
  and `read_seen_red_records` returns it.
  Red when: the line is written without the staged run having exited non-zero.
- **AC7** — When the fixture runs `--plant gate-stays-green`, `loop_witness.py acceptance` exits 1,
  prints `planted red stayed green` and the `route: build.fix-pass` line naming `--fix-of acceptance`,
  and writes no seen-red line.
  Red when: a plant that leaves the leg green passes the acceptance.
- **AC8** — When the fixture runs `--plant gate-no-plant`, `loop_witness.py acceptance` exits 1
  printing `no plant declared`, and `python seen_red.py --build <slug>` over the fixture prints the leg
  with `NO RECORD`.
  Red when: a gate whose red never ran passes the acceptance or reads as seen.
- **AC9** — When the fixture runs `--plant gate-restored-red`, `loop_witness.py acceptance` exits 1
  printing `without the plant`; and a `--plant` whose `<from>` occurs twice exits 2 before any run.
  Red when: a leg red at the SHA on its own reads as the plant's red.
- **AC10** — When `python fix_keeps.py --fixture --plant reuse-check-module` runs in
  `tools/unattended/`, `--keeps reuse-check` prints the fixture's acceptance file and `reuse_check.py`,
  and `grep -c 'reuse-check' tools/unattended/unattended.sh` prints at least 1.
  Red when: a reuse-check fix pass may write the reuse check's own module.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `unattended kit gate` · `pass-order history` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

TOOL-dDeclaredLoop-17's leg `loop computed witness` runs `loop_witness.py --selftest`; it is not in
the manifest at base, so it is named here and kept green from its landing on.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the `seen_red.py` plants through `--fixture`, staged red by dropping the own-commit filter from `derive_unit_gates` and the `(leg, red)` check from `write_seen_red_lines` · none
New arm: tools/loop/loop_witness.py · covers AC6 AC7 AC8 AC9 · its `--selftest` over the `gate-*` plants, staged red by reading the staged run's exit alone · none
New arm: tools/unattended/unattended.test.sh · covers AC10 · the `reuse-check-module` plant through `fix_keeps.py --fixture`, staged red by dropping `reuse-check` from the keeps table · none

## 8. Open questions

- **F1 — Where is a gate's planted red declared?** Options: (a) a `--plant` on the acceptance verb,
  named by the caller beside its `--cmd` commands; (b) a `plant` field on the spec's `New arm:` line;
  (c) the leg factory registering each leg's planted case; (d) a patch file committed under the build.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 1: FK-5-2 A makes the planted red one of "the unit's acceptance commands", which TOOL-dDeclaredLoop-17 §3 has the caller name, and the owner did not take (c), FK-5-2 B; (b) fails at writing time for code not yet written and changes a governance carrier the clause does not name; (d) adds a file kind no reader exists for. widens: none · relaxes: none
- **F2 — What is a plant, a command or a substitution?** Options: (a) a one-line literal
  substitution the verb stages, with the leg run staged and restored; (b) a command owed to exit 1.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich survivor: it executes no caller text, and its restored run tells the plant's red from a broken invocation, which (b) cannot (§4 "Alternatives rejected"). widens: none · relaxes: none
- **F3 — Which gates does a unit owe?** Options: (a) legs changed across its own commits and legs its
  own spec's `New arm:` lines resolve to; (b) the build's whole owed set at every unit; (c) its
  `New arm:` lines alone. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3: it is TOOL-dWitnessedBar-7 S4's two arms narrowed to the unit by I8, so the per-unit records union to the build's owed set; (b) charges a unit for a sibling's gate; (c) misses a leg added with no arm line, which S4 (a) owes. widens: none · relaxes: none
- **F4 — What does `--fix-of reuse-check` keep?** Options: (a) the acceptance commands' files only;
  (b) those and the reuse check's own module. RESOLVED (agent, 2026-11-01, delegated): (b), rung 3: `build.fix-pass`'s allowance is the write set "less the red check's own test files and gate script and the acceptance commands' files" (flow-steps.md:291), and the reuse check's module is that red check's script. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 15, scout A's row 15, shared interfaces
  I1, I8, I17 and I19, and the sources read at `5f0b11f12`.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-33, TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are TOOL-dWitnessedBar-7's `seen_red.py` (its grammar, `read_seen_red_records` and
`derive_owed_gates`, of which S1 is the per-unit reading), TOOL-dDeclaredLoop-17's `loop_witness.py
acceptance` and `run_witness_commands` (the one re-run at a SHA, which S5 extends with the plants rather
than adding a second worktree runner), TOOL-dWitnessedBar-21's `fix_keeps.py` and `--fix-of` (S7 adds a
value), and the bar's runner through `GATE_LEGS` (`tools/run-gates/run-gates.sh:252`). `python
tools/codebase-map/reuse_lookup.py "re-run a gate's planted red at a commit and write a seen-red record
keyed by leg and red sha"` ranked name stems (`key`, `run`, `write`, `legs`, `build_commit`), none of
which writes a seen-red line or stages a plant: no landed seam fits beyond the specced parents above,
which are absent at base. Scout A's lines held at `5f0b11f12`: `lib-attribute.sh:57-63` holds
`add_scratch_worktree` (its body at :59), `run-gates.sh:4635` `read_row_at`, `deviation_join.py:325`
`read_first_passes`. Where the scout proposed `seen_red.py --write` as the whole writer, the re-run is
put in the loop kit's acceptance verb instead, because TOOL-dDeclaredLoop-17 S2 already owns the
worktree re-run and FK-5-2 A puts the planted red among the acceptance commands; `seen_red.py` keeps the
grammar's one writer.

Recall terms used: `python tools/memory-recall/query.py "who writes the seen-red record for a gate a unit adds and how is its planted red re-run" --terms "seen-red build.acceptance planted red New arm acceptance ledger observe owed arms derive_owed_gates fix-of executor"`
