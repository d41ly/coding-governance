# PLAY-dOrderedCharter-73 — the close bar's other code reds: encodings, shell idioms, a remote literal, the scratch matrix and the cap census

**Status:** DEFERRED · rev-1 · 2026-11-08 · node d · Tier-2 · base 93c4e987e · streams tooling · order 17 · advances PLAY-dOrderedCharter-38 · ratified 2026-11-08

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief.md) | research | PLAY-dOrderedCharter-72 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-73-build-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-73-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Six close-bar legs that are green on `origin/main` stop naming any code this build wrote: the encoding posture,
both shell-hygiene legs, the remote-literal ban, the govkit acceptance matrix and the policy check's cap census.
Each fix takes the cause the checker's own remedy names, and none is a waiver. The harness-arms leg's three new
refusal sites get the pinned rows the main loop writes, because no sibling suite can stage them.

## 2. Scope (IN)

Every line below was read at base `93c4e987e`. This unit builds after PLAY-dOrderedCharter-72 and reads its result
in `tools/playbook/core.py`, `tools/playbook/instruction_units.py`, `tools/playbook/positional.py`,
`tools/playbook/adopt-playbook.sh` and `tools/playbook/kit.toml`. The Design section holds what a one-line item
cannot.

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
- **S5** — `tools/playbook/kit.toml` declares `requires = ["playbook", "memory-tree"]`, as the Open questions
  section's F1 rules. Observed by AC7.
- **S6** — The scratch install in `tools/govkit/matrix.py` installs the graded entries plus every dependency
  `govkit.derive_unsatisfied_requires` names for them, and still grades only the legs of `SCRATCH_KITS`.
  `tools/govkit/matrix.py#SCRATCH_EXPECT` gains the install-day verdicts of `core selftest`, `tags bundle selftest`
  and `tags positional selftest`, each the line that leg prints in the scratch install. Observed by AC8.
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
- **Widening the matrix's graded set.** The memory-tree kit is installed in the scratch target so the graded legs
  can run, and its own legs stay graded where they are today, by its own suites.
- **A version line.** The kit-epoch leg reads every kit this build moved as owed at the lander.
- **The kit-path spellings in the same files.** They are PLAY-dOrderedCharter-72's, which lands first.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-72` — this unit's edits to `tools/playbook/core.py`,
  `tools/playbook/instruction_units.py`, `tools/playbook/positional.py`, `tools/playbook/adopt-playbook.sh` and
  `tools/playbook/kit.toml` are written over that unit's result. The unencoded `subprocess.run` calls, the
  shell-idiom fix and the `requires` row are this unit's. Built first, the two units conflict line by line in those
  five files
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

### The scratch matrix

`tools/govkit/matrix.py` installs `SCRATCH_KITS` today and fails twice. The leg set holds three legs the table does
not state, and `playbook render selftest` dies with a traceback in `tools/playbook/check_layers.py`, whose
module-level `resolve_kit_dir("memory-tree", ...)` finds no memory-tree kit in the scratch target. The three unstated
legs reach the same kit too: `tools/playbook/tag_index.py#load_memory_tree` and
`tools/playbook/core.py#load_memory_tree` resolve it, and refuse by name where it is absent.

Under F1's ruling, `tools/playbook/kit.toml` requires the memory-tree kit, and `apply` refuses a
selection that lacks it, through `govkit.derive_unsatisfied_requires`. So the matrix reads the descriptors before it
writes `deploy.toml`, derives the install selection as `SCRATCH_KITS` plus every dependency that function names for
it, writes that selection into `deploy.toml` and passes it to `apply`. The leg loop still walks `SCRATCH_KITS` alone,
so the graded set grows by the three legs and no more.

The three new `SCRATCH_EXPECT` rows state the line each leg prints in that scratch install, cut before any count, as
the table's own comment requires of `playbook render selftest`. At base the code prints
`PASS — the positional plants,`, `PASS — the bundle plants,` and `core: fixture · green`, from `tools/playbook/positional.py#run_selftest`,
`tools/playbook/tag_bundle.py` and `tools/playbook/core.py#run_fixture`. The builder takes each value from a scratch
install's run of that leg, and AC8 observes the matrix printing each one where it was installed.

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

N/A — no data shape moves. The `requires` edge reaches an adopter at its next `govkit update`, and the Open
questions section weighs that.

### Rollout

Live at landing. AC1 to AC10 turn their legs at once, the matrix's included, F1 being ruled.

### Files touched (estimate)

- `tools/lib/common_dir.py`, `tools/memory-tree/build_records.py`, `tools/memory-tree/id_grammar.py`: S1
- `tools/playbook/core.py`, `tools/playbook/positional.py`: S1
- `tools/playbook/instruction_units.py`: S1, S4
- `tools/unattended/unattended.sh`: S2
- `tools/memory-tree/merge-rows.test.sh`, `skills/session-kickoff/manifest-check.test.sh`,
  `tools/unattended/check-unattended.test.sh`: S3
- `tools/playbook/adopt-playbook.sh`: S3, S8
- `tools/playbook/kit.toml`: S5
- `tools/govkit/matrix.py`: S6
- `tools/run-gates/owed_rows.py`: S7

### Alternatives rejected

- **Registry rows for the nine calls.** The scan's remedy is `encoding="utf-8"`, and every one of these calls
  decodes git or Python output this repo writes as UTF-8.
- **`< <(printf '%s' "$out")` in the loop.** It forks once per call, which the fork leg exists to refuse.
- **Keeping `printf "%s" "$(...)"` and growing the spawn-idiom row from one to seven.** A row that may only shrink
  would grow to admit code this build wrote.
- **Building `tools/playbook/adopt-playbook.test.sh` to arm the three tallies.** The Non-goals section states why no
  suite can stage a failing plant row.
- **Stating the four scratch verdicts as refusals.** Under F1's option (b) the scratch install still lacks the
  memory-tree kit, so the table would state four failures as install-day verdicts. That certifies a broken install.

## 5. Production-readiness checklist

- security: N/A — no write path, surface or grant moves.
- perf / scale: the loop and fork fixes save one fork per call site, the measured cost the fork leg names.
- error / empty / loading states: an empty listing in `check_branch_carried` gives an array of one empty line, which
  the existing `""` arm of its `case` skips, as the here-string loop did.
- observability: N/A — every message a reader greps keeps its text.
- risks: the `requires` edge refuses an update at an adopter that deselected the memory-tree kit. The Open
  questions section weighs it.
- testing: AC1 to AC10, and the matrix arm the gates section declares.
- migration: N/A — no data shape moves.
- user docs: N/A — no page under `help/` names a changed call, idiom or matrix row.

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
- **AC7** — When `grep '^requires' tools/playbook/kit.toml` runs, it prints
  `requires = ["playbook", "memory-tree"]`, and `python tools/govkit/govkit.py selfcheck` exits 0.
  Red when: the descriptor still declares a renderer that runs without the kit its checks resolve.
  permission: `selfcheck` is a leg's argv, so the main loop observes it.
- **AC8** — When `python tools/govkit/matrix.py` runs, it prints no `FAIL` line, and prints
  `prints its stated verdict where it was installed` for `core selftest`, `tags bundle selftest` and
  `tags positional selftest`.
  Red when: the table misses a declared leg, or a scratch leg dies with a traceback.
  figure: 2 FAILED at base, PINNED from the bar's log.
  cost: several minutes. permission: the command is a leg's argv, so the main loop observes it.
- **AC9** — When `grep -c 'budgets.py resolve' tools/run-gates/owed_rows.py` runs, it prints `0`, and
  `python tools/run-gates/owed_rows.py --selftest` exits 0.
  Red when: a line still spells the request shape, so the census reads its words as cap names.
- **AC10** — When `grep -cE 'arm\(s\) failed"; exit 1' tools/playbook/adopt-playbook.sh` runs, it prints `3`.
  Red when: a message moves out from under the signature the main loop's pinned row names.

## 7. Gates

`encoding posture (text IO names its encoding)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `remote literals (kit code names no remote)` · `govkit acceptance matrix` · `policy check` · `harness arms (fail branches armed or pinned)` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `policy fixtures` · `playbook render selftest` · `core selftest` · `tags positional selftest` · `instruction units selftest` · `row-keyed merge driver replay` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `unattended kit gate` · `memory-hygiene self-test` · `corpus-ids selftest` · `memory-recall kit selftest` · `drift-audit selftest` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary`

The first seven are the legs this unit turns or keeps. The guards join owes the next group: `{prefix}/govkit/` and
the exact-path guards of `policy fixtures`, `{prefix}/playbook/` and `{prefix}/memory-tree/id_grammar.py` for the
render selftest and the recall and drift-audit legs, and `skills/session-kickoff/manifest-check.test.sh` for three
legs. `{prefix}/`, `{prefix}/lib/`, `{prefix}/memory-tree/` and `{prefix}/run-gates/` are broad under
`BROAD_LEG_FLOOR` 5 and excluded. The rest run the code this unit moves: the fixtures, the merge driver's cases, the
unattended driver, the id grammar, the parity table that reads `tools/lib/common_dir.py`, and
`owed_rows.py --selftest`, which `run-gates.test.sh` runs.

New arm: tools/govkit/matrix.py · covers AC8 · three `SCRATCH_EXPECT` rows, red with any one of them absent through the table's both-directions arm · none

## 8. Open questions

- **F1 — Does `playbook render selftest` fail in the scratch install because the renderer requires the
  memory-tree kit, or because `tools/playbook/check_layers.py` resolves that kit too early?**
  - (a) `tools/playbook/kit.toml` declares `requires = ["playbook", "memory-tree"]`, and the matrix installs the
    dependency. The declaration then says what four of the kit's legs already do: the layer check's import walk and
    shell lexer, the tag index's blob reader and the core's joins all live in the memory-tree kit. The memory-tree
    kit is in the default selection and the renderer is not, so a default adopter already holds it. An adopter that
    deselected it is refused at its next `govkit update` until it selects it, with the refusal naming the edge.
  - (b) `tools/playbook/check_layers.py` resolves the memory-tree kit inside the function that walks imports. The
    traceback becomes a named refusal. But the layer arms still need that kit to run, and the tag and core
    fixtures refuse without it, so all four scratch verdicts are failures. The table would have to state them as
    such, or the matrix would stay red.
  - Recommendation: (a). It is the only option under which the four legs pass in a scratch install, and it
    declares a dependency the code already has. The Design section is written for (a). Under (b), S5 becomes the
    move of the module-level resolution in `tools/playbook/check_layers.py` into its use, S6 keeps `SCRATCH_KITS` as
    the install selection, and the three `SCRATCH_EXPECT` rows state refusals.
  RESOLVED (agent, 2026-11-08, delegated): (a), the main loop's ruling.
  Veto 1 discards (b), the loser: its four install-day verdicts fail, so the matrix stays red. (a) passes veto 2:
  memory-tree is an internal kit already in the default selection, not an external dependency, so the edge declares
  a dependency the code already has and a default adopter's install does not change.

## 9. Revision log

- rev-1 · 2026-11-08 · initial draft, by `2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief`, every line read at
  `93c4e987e`.

## 10. Reuse audit

Every fix reuses a form the tree already carries, so no new mechanism is minted. The array drain is
`tools/unattended/unattended.sh`'s own `mapfile -t` here-string read. The indented failure output is the
`printf '      %s\n'` expansion of `tools/memory-tree/check-memory-hygiene.test.sh`. The tool-root prefix is the
`_b1tr` that `tools/unattended/check-unattended.test.sh` already derives. The install selection reuses
`govkit.derive_unsatisfied_requires`, the one predicate `apply` refuses on, so the matrix and the deployer cannot
disagree about what a selection lacks. The `reuse_lookup.py` query ranked `resolve_kit_dir`, `scratch` and
`kit_rel` symbols and no install-selection seam, so the requires predicate was found by reading `apply`. The recall
query returned TOOL-aWalkedCorpus-8, that `requires` orders an install, and PLAY-dOrderedCharter-16's reuse scout,
which lists the renderer among the memory-tree kit's `requires_if` edges, an edge in the other direction that this
unit leaves as it is. No record weighed a plain edge from the renderer to the memory-tree kit.

Recall terms used: `python tools/memory-recall/query.py "the scratch install lacks the memory-tree kit the playbook renderer resolves" --terms "SCRATCH_EXPECT SCRATCH_KITS requires memory-tree playbook-render check_layers resolve_kit_dir scratch install traceback derive_unsatisfied_requires"`, and `python tools/codebase-map/reuse_lookup.py "derive an install selection from the requires edges of the kits a scratch target installs"`
