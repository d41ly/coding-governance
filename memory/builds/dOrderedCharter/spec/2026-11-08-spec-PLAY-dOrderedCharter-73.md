# PLAY-dOrderedCharter-73 — the close bar's other code reds: encodings, shell idioms, a remote literal, and the cap census

**Status:** CLOSED · rev-2 · 2026-11-08 · node d · Tier-2 · base 93c4e987e · streams tooling · order 17 · advances PLAY-dOrderedCharter-38 · ratified 2026-11-08

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-84 PLAY-dOrderedCharter-85 |
| [2026-11-08-build-PLAY-dOrderedCharter-73-1-builder-return.md](../build/2026-11-08-build-PLAY-dOrderedCharter-73-1-builder-return.md) | journal | — |
| [2026-11-08-build-PLAY-dOrderedCharter-73-ledger.md](../build/2026-11-08-build-PLAY-dOrderedCharter-73-ledger.md) | journal | — |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief.md) | research | PLAY-dOrderedCharter-72 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-73-build-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-73-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Five close-bar legs that are green on `origin/main` stop naming any code this build wrote: the encoding posture,
both shell-hygiene legs, the remote-literal ban and the policy check's cap census. Each fix takes the cause the
checker's own remedy names, and none is a waiver. The harness-arms leg's three new refusal sites get the pinned rows
the main loop writes, because no sibling suite can stage them. The govkit acceptance matrix stays red: its fix needs
a dependency decision the Open questions section parks for the owner.

## 2. Scope (IN)

Every line below was read at base `93c4e987e`. This unit builds after PLAY-dOrderedCharter-72 and reads its result
in `tools/playbook/core.py`, `tools/playbook/instruction_units.py`, `tools/playbook/positional.py`,
and `tools/playbook/adopt-playbook.sh`. The Design section holds what a one-line item cannot. S5 and S6 left the
scope at rev-2, and their numbers are not reused.

- **S1** — Nine `subprocess.run(..., text=True)` calls gain `encoding="utf-8"`: one in
  `tools/lib/common_dir.py#read_git_stdout`, two in `tools/memory-tree/build_records.py#run_fixture`, one in
  `tools/memory-tree/id_grammar.py#git`, one each in `tools/playbook/core.py#run_fixture_git` and
  `tools/playbook/core.py#run_door`, one in `tools/playbook/instruction_units.py#arm_render`, and two in
  `tools/playbook/positional.py#run_pin`. Observed by AC1 and AC2.
- **S2** — `tools/unattended/unattended.sh#check_branch_carried` reads the listing into an array with
  `mapfile -t` and walks the array, where a `while read` loop drained a here-string over the substitution's
  variable. Observed by AC3.
- **S3** — Four fork-leg sites take the no-fork form. `tools/memory-tree/merge-rows.test.sh` gains
  `derive_fx_unterminated`, which prints a unit row with no trailing newline, and its six
  `printf "%s" "$(derive_fx_unit ...)"` sites call it directly. `skills/session-kickoff/manifest-check.test.sh`
  spells its id-grammar directory `${READER_REL%/*}`. `tools/unattended/check-unattended.test.sh` reuses the
  tool-root prefix `_b1tr` it already derived. `tools/playbook/adopt-playbook.sh` indents a failed arm's output in
  one `printf` with an expansion, at both of its sites. Observed by AC4 and AC5.
- **S4** — `tools/playbook/instruction_units.py` declares `DERIVED_UNIT_KEYS = ("status", "origin")` at module
  level, and `tools/playbook/instruction_units.py#check_unit_row` tests membership against it. Observed by AC6.
- **S7** — The four lines of `tools/run-gates/owed_rows.py` that spell the policy kit's budgets script followed by
  its `resolve` verb, in the module docstring, in `tools/run-gates/owed_rows.py#read_cap_values`'s docstring and in
  its refusal message, name the verb another way. Observed by AC9.
- **S8** — The three refusal sites of `tools/playbook/adopt-playbook.sh`, the tallies after the layer check's, the
  tag resolver's and the edge grammar's plants, keep their messages, and the Design section names the three pinned
  rows the main loop writes for them. Observed by AC10.

## 3. Non-goals (OUT)

- **The registry rows.** The encoding registry's row for `tools/memory-recall/extract.py`, which the scan no longer
  finds, the spawn-idiom row of `tools/check-wiring.test.sh`, whose scan now counts one site fewer, and the three
  pinned refusal rows are records under `memory/project/`, and the main loop writes them.
- **The policy check's reader-coverage arm.** Its five `review.*` keys belong to `origin/main`'s dFairHearing, and
  the merge with `origin/main` clears them.
- **A sibling suite for `tools/playbook/adopt-playbook.sh`.** No such suite exists, and the plant rows are
  here-documents inside the script, so a suite could reach a failing row only by editing the script under test.
- **The govkit acceptance matrix and the renderer's `requires` row.** `tools/govkit/matrix.py` and
  `tools/playbook/kit.toml` stay as they are. F1 parks the dependency question for the owner, so the matrix leg stays
  red until that ruling.
- **A version line.** The kit-epoch leg reads every kit this build moved as owed at the lander.
- **The kit-path spellings in the same files.** They are PLAY-dOrderedCharter-72's, which lands first.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-72` — this unit's edits to `tools/playbook/core.py`,
  `tools/playbook/instruction_units.py`, `tools/playbook/positional.py` and `tools/playbook/adopt-playbook.sh` are
  written over that unit's result. The unencoded `subprocess.run` calls and the shell-idiom fix are this unit's.
  Built first, the two units conflict line by line in those four files. The `requires` row of
  `tools/playbook/kit.toml`, which that unit hands here, stays as it left it: its change is parked for the owner under
  F1
- **hands-off** external — the three pinned rows in `memory/project/unarmed-branches.txt`, the stale encoding
  registry row and the spawn-idiom row of `tools/check-wiring.test.sh`, which the main loop writes

## 4. Design

### Encoding posture

Each call keeps `text=True` and adds `encoding="utf-8"`, the form the scan's remedy names and the form
`tools/playbook/positional.py#read_git_grep` and `tools/playbook/positional.py#read_line_commits` already pass. A call that reads a child's stderr text adds no
`errors=` unless its sibling in the same file already does, so no new decoding policy is minted. The
`common_git_dir` block in `tools/lib/common_dir.py` is gated byte for byte against its two inline copies, and
`tools/lib/common_dir.py#read_git_stdout` sits outside that block, so the parity row is unmoved.

### The loop leg

`tools/unattended/unattended.sh#check_branch_carried` captures `git log` into `out`, then drains `<<<"$out"` in a
`while read` loop. The scan counts three such sites in the file against a registry row of two. The no-fork form is
the one this file already uses at its own `_dp_rows` reads:

```bash
    local -a rows
    mapfile -t rows <<<"$out"
    for line in "${rows[@]}"; do
      line=${line%$'\r'}
      ...
    done
```

The body, its `continue`s and its `break` are unchanged. A `mapfile` read is no `while … done` loop, so the gated
class does not read it, and the file's `_dp_rows` reads already pass the scan in that form. `< <(printf ...)` would
have spent the fork this leg's sibling bans.

### The fork leg

| File | Site | No-fork form |
|---|---|---|
| `tools/memory-tree/merge-rows.test.sh` | six `printf "%s" "$(derive_fx_unit ...)"` in the two unterminated-entry cases | a new helper beside `derive_fx_unit`, its format without the closing `\n`, called directly with the same arguments |
| `skills/session-kickoff/manifest-check.test.sh` | `$(dirname -- "$READER_REL")` in the exit-3 arm | `${READER_REL%/*}`: `READER_REL` is `$READER` with the gov root stripped, a file under a kit, so it always holds a `/` |
| `tools/unattended/check-unattended.test.sh` | `$(dirname -- "$KIT_REL")` in the id-grammar copy | `"$ak/$_b1tr${_ig_src##*/}"`, where `_b1tr` is the tool-root prefix with its slash, or empty at a root install, derived once earlier in the same suite |
| `tools/playbook/adopt-playbook.sh` | `printf '%s\n' "$_lout" \| sed 's/^/      /'` in the layer loop, and its twin over `$_tout` in `run_plant_rows` | `printf '      %s\n' "${_lout//$'\n'/$'\n'      }"`, and the same over `$_tout`, the form `tools/memory-tree/check-memory-hygiene.test.sh` already uses |

The new helper is named `derive_fx_unterminated`, which `lexicon.py --suggest` grades OK under `sh.function` at base.
Its bytes equal `printf "%s" "$(derive_fx_unit ...)"` for every argument: a command substitution strips exactly the
trailing newline the helper no longer prints, and the helper's last line carries no other trailing whitespace.

### The remote literal

`check_unit_row` names two unit-row keys that are derived and never carried, `status` and `origin`. The ban's
default shape reads a quoted remote name as the last element of a parenthesised list, and its comment states that a
list assigned to a name is not that shape. So the tuple moves to a module constant beside `UNIT_KEYS`, with a one-line
comment saying the row derives these two and never carries them. The remedy text is unchanged.

### The cap census

`tools/policy/check_policy.py` reads a request as the budgets script's name followed by whitespace and `resolve` or
`check`, and every word after it on the line as a cap name. Four lines of `tools/run-gates/owed_rows.py` spell that
sequence in prose, so the census reads 30 English words as requested caps. Each line names the verb as the
`resolve` verb of `budgets.py`, which the request shape does not match, and the subprocess argv is untouched: its
script and verb are separate list elements, which the census does not read.

### The three refusal sites

`tools/memory-tree/check-arms.py` finds each `exit 1` after a plant loop of `tools/playbook/adopt-playbook.sh`
neither armed by a sibling suite nor pinned. The three rows the main loop writes in
`memory/project/unarmed-branches.txt`, in its second row shape:

```
tools/playbook/adopt-playbook.sh	exit	1	layer-check arm(s) failed	no sibling suite: tools/playbook/adopt-playbook.test.sh does not exist, and the site is the selftest's own tally, taken whenever a plant row above it fails; the playbook render selftest leg runs every row on each bar
tools/playbook/adopt-playbook.sh	exit	1	tag-resolver arm(s) failed	the same reason, for the tag resolver's plant rows
tools/playbook/adopt-playbook.sh	exit	1	edge-grammar arm(s) failed	the same reason, for the edge grammar's plant rows
```

The signature is each message's literal tail, so this unit keeps the three messages byte for byte. S3's `printf`
change sits inside the per-row failure branch and moves none of them.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_fx_unterminated` | shell function | `sh.function`, graded OK by `lexicon.py --suggest` at base |
| `DERIVED_UNIT_KEYS` | Python module constant | none: no `py.constant` cell is declared |

### Migration

N/A — no data shape moves.

### Rollout

Live at landing. AC1 to AC6, AC9 and AC10 turn their legs at once. The matrix leg stays red, as F1 records.

The unit 73 builder's work-in-progress patch for the remaining items is at
`C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/play73-wip.patch`.
It is a starting point the builder re-verifies against this revision, never a result to apply unread: it was cut
while the scope still held the requires row and the matrix.

### Files touched (estimate)

- `tools/lib/common_dir.py`, `tools/memory-tree/build_records.py`, `tools/memory-tree/id_grammar.py`: S1
- `tools/playbook/core.py`, `tools/playbook/positional.py`: S1
- `tools/playbook/instruction_units.py`: S1, S4
- `tools/unattended/unattended.sh`: S2
- `tools/memory-tree/merge-rows.test.sh`, `skills/session-kickoff/manifest-check.test.sh`,
  `tools/unattended/check-unattended.test.sh`: S3
- `tools/playbook/adopt-playbook.sh`: S3, S8
- `tools/run-gates/owed_rows.py`: S7

### Alternatives rejected

- **Registry rows for the nine calls.** The scan's remedy is `encoding="utf-8"`, and every one of these calls
  decodes git or Python output this repo writes as UTF-8.
- **`< <(printf '%s' "$out")` in the loop.** It forks once per call, which the fork leg exists to refuse.
- **Keeping `printf "%s" "$(...)"` and growing the spawn-idiom row from one to seven.** A row that may only shrink
  would grow to admit code this build wrote.
- **Building `tools/playbook/adopt-playbook.test.sh` to arm the three tallies.** The Non-goals section states why no
  suite can stage a failing plant row.

## 5. Production-readiness checklist

- security: N/A — no write path, surface or grant moves.
- perf / scale: the loop and fork fixes save one fork per call site, the measured cost the fork leg names.
- error / empty / loading states: an empty listing in `check_branch_carried` gives an array of one empty line, which
  the existing `""` arm of its `case` skips, as the here-string loop did.
- observability: N/A — every message a reader greps keeps its text.
- risks: the matrix leg stays red until the owner rules F1, the cost the Open questions section records.
- testing: AC1 to AC6, AC9 and AC10.
- migration: N/A — no data shape moves.
- user docs: N/A — no page under `help/` names a changed call or idiom.

## 6. Acceptance criteria

- **AC1** — When `python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`
  runs, it prints no `unencoded` line.
  Red when: one of the nine calls still decodes with the platform default.
  figure: 9 unencoded calls at base, PINNED from the bar's log at `93c4e987e`.
  permission: the command is a leg's argv, so the main loop observes it.
- **AC2** — When `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` and
  `python tools/playbook/core.py fixture` run, each exits 0.
  Red when: an added keyword breaks a fixture's call.
  cost: a minute for the core fixture.
- **AC3** — When `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt` runs, it exits 0,
  and `grep -c 'mapfile -t rows' tools/unattended/unattended.sh` prints `1`.
  Red when: the loop still reads a here-string over the substitution's variable.
  permission: the scan is a leg's argv, so the main loop observes it.
- **AC4** — When `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
  runs, no finding names `tools/memory-tree/merge-rows.test.sh`, `skills/session-kickoff/manifest-check.test.sh`,
  `tools/unattended/check-unattended.test.sh` or `tools/playbook/adopt-playbook.sh`.
  Red when: a site still forks for work bash does in-process.
  permission: the scan is a leg's argv, so the main loop observes it.
- **AC5** — When `bash -c 'eval "$(grep -E "^derive_fx_(unit|unterminated)\(\)" tools/memory-tree/merge-rows.test.sh)"; cmp <(printf "%s" "$(derive_fx_unit b x)") <(derive_fx_unterminated b x)'`
  runs, it prints nothing and exits 0.
  Red when: the new helper prints a trailing newline, so the unterminated cases feed the driver terminated bytes.
- **AC6** — When `bash tools/check-remote-literals.sh` runs, it exits 0, and
  `grep -c DERIVED_UNIT_KEYS tools/playbook/instruction_units.py` prints `2`.
  Red when: the tuple stays inline as a call's last argument.
  permission: the command is a leg's argv, so the main loop observes it.
- **AC9** — When `grep -c 'budgets.py resolve' tools/run-gates/owed_rows.py` runs, it prints `0`, and
  `python tools/run-gates/owed_rows.py --selftest` exits 0.
  Red when: a line still spells the request shape, so the census reads its words as cap names.
- **AC10** — When `grep -cE 'arm\(s\) failed"; exit 1' tools/playbook/adopt-playbook.sh` runs, it prints `3`.
  Red when: a message moves out from under the signature the main loop's pinned row names.

## 7. Gates

`encoding posture (text IO names its encoding)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `remote literals (kit code names no remote)` · `policy check` · `harness arms (fail branches armed or pinned)` · `govkit acceptance matrix` · `playbook render selftest` · `core selftest` · `tags positional selftest` · `instruction units selftest` · `row-keyed merge driver replay` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `unattended kit gate` · `memory-hygiene self-test` · `corpus-ids selftest` · `memory-recall kit selftest` · `drift-audit selftest` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary`

The first six are the legs this unit turns or keeps. The guards join owes the next group: `{prefix}/playbook/` for
the matrix and the render selftest, `{prefix}/memory-tree/id_grammar.py` for the render selftest and the recall and
drift-audit legs, and `skills/session-kickoff/manifest-check.test.sh` for three legs. The matrix stays red, as F1
records. `{prefix}/`, `{prefix}/lib/`, `{prefix}/memory-tree/` and `{prefix}/run-gates/` are broad under
`BROAD_LEG_FLOOR` 5 and excluded. The rest run the code this unit moves: the fixtures, the merge driver's cases, the
unattended driver, the id grammar, the parity table that reads `tools/lib/common_dir.py`, and
`owed_rows.py --selftest`, which `run-gates.test.sh` runs.

## 8. Open questions

- **F1 — What makes the playbook-render legs pass in the matrix's scratch install, and may this unit decide it?**
  The scratch install of `tools/govkit/matrix.py` holds no memory-tree kit, so `playbook render selftest` dies with
  a traceback in `tools/playbook/check_layers.py`, whose module-level `resolve_kit_dir("memory-tree", ...)` finds
  nothing. `core selftest`, `tags bundle selftest` and `tags positional selftest` are declared and absent from
  `tools/govkit/matrix.py#SCRATCH_EXPECT`.
  - (a) `tools/playbook/kit.toml` requires the kits the legs read, and the matrix installs them. The unit 73 builder
    measured it: with `requires = ["playbook", "memory-tree"]` the three unstated legs still refuse in the scratch
    install with `no policy kit found`, and with `requires = ["playbook", "memory-tree", "policy"]` all three pass.
    The policy kit is not in the registry's default selection, so (a) adds a new install requirement for adopters.
    That trips veto 2, and the choice is the owner's.
  - (b) `tools/playbook/check_layers.py` resolves the memory-tree kit inside the function that walks imports. The
    traceback becomes a named refusal, but the layer arms still need that kit, and the tag and core fixtures refuse
    without it. Veto 1 discards it: its four install-day verdicts fail and the matrix stays red.
  - (c) The run's interim: this unit leaves `tools/govkit/matrix.py` and `tools/playbook/kit.toml` alone, and the
    dependency question goes to the owner. Cost: the govkit acceptance matrix leg stays red until the ruling.
  - Known gap, whichever option the owner takes: with the policy kit installed, the builder saw the existing
    `playbook render selftest` leg end `FAIL — 1 tag-resolver arm(s) failed` in the scratch install, while its
    matrix substring `render_playbook.selftest OK` still matches. The matrix reads that leg as passing when one of its
    arms fails.
  RESOLVED (agent, 2026-11-08, delegated): (c), the run's interim — this unit leaves the matrix and the renderer's requires row alone; the dependency question is parked for the owner.
  (b) loses on veto 1, and (a) waits on the owner because it trips veto 2. The main loop records the parked
  question in the run record.

## 9. Revision log

- rev-1 · 2026-11-08 · initial draft, by `2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief`, every line read at
  `93c4e987e`.
- rev-2 · 2026-11-08 · S5 · S6 · AC7 · AC8 · section 8 · the unit 73 builder handed the spec back before building,
  having measured that the three tag and core legs also need the policy kit, a kit outside the default selection.
  F1 is re-ruled (c), the run's interim, and the requires row, the matrix work and their criteria and arm leave
  the scope; the builder's work-in-progress patch is named in Rollout, and the consumes-from edge says the row unit 72
  hands here stays as it left it.

## 10. Reuse audit

Every fix reuses a form the tree already carries, so no new mechanism is minted. The array drain is
`tools/unattended/unattended.sh`'s own `mapfile -t` here-string read. The indented failure output is the
`printf '      %s\n'` expansion of `tools/memory-tree/check-memory-hygiene.test.sh`. The tool-root prefix is the
`_b1tr` that `tools/unattended/check-unattended.test.sh` already derives. The `reuse_lookup.py` query, run for the
matrix design that F1 now parks, ranked `resolve_kit_dir`, `scratch` and `kit_rel` symbols and no install-selection
seam. The recall query returned TOOL-aWalkedCorpus-8, that `requires` orders an install, and
PLAY-dOrderedCharter-16's reuse scout, which lists the renderer among the memory-tree kit's `requires_if` edges. No
record weighed a plain edge from the renderer to either kit.

Recall terms used: `python tools/memory-recall/query.py "the scratch install lacks the memory-tree kit the playbook renderer resolves" --terms "SCRATCH_EXPECT SCRATCH_KITS requires memory-tree playbook-render check_layers resolve_kit_dir scratch install traceback derive_unsatisfied_requires"`, and `python tools/codebase-map/reuse_lookup.py "derive an install selection from the requires edges of the kits a scratch target installs"`
